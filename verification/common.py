"""Shared helpers for lightweight GigaChat skill verification scripts.

These scripts are intentionally small smoke checks, not a benchmark suite.
They avoid live network/API calls unless --live is passed.
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import sys
import tempfile
import urllib.error
import urllib.request
import wave
from pathlib import Path
from typing import Any, Callable


DEFAULT_GPT2GIGA_BASE_URL = "http://127.0.0.1:8090/v1"
DEFAULT_CHAT_MODEL = os.getenv("GIGACHAT_MODEL", "GigaChat-2")
DEFAULT_EMBEDDINGS_MODEL = os.getenv("GIGACHAT_EMBEDDINGS_MODEL", "EmbeddingsGigaR")


class SmokeSkip(RuntimeError):
    """Raised when a smoke check cannot run in the current environment."""


def parser(description: str) -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description=description)
    p.add_argument("--live", action="store_true", help="Run live API/proxy calls")
    p.add_argument("--json", action="store_true", help="Emit JSON result")
    p.add_argument("--model", default=DEFAULT_CHAT_MODEL, help="Chat model name")
    p.add_argument("--embeddings-model", default=DEFAULT_EMBEDDINGS_MODEL)
    p.add_argument("--base-url", default=os.getenv("GPT2GIGA_BASE_URL", DEFAULT_GPT2GIGA_BASE_URL))
    p.add_argument("--api-key", default=os.getenv("GPT2GIGA_API_KEY") or os.getenv("OPENAI_API_KEY") or "test")
    p.add_argument("--file", default=None, help="Optional fixture file path")
    p.add_argument("--file-kind", choices=["image", "audio", "pdf", "text"], default=None)
    return p


def main(description: str, fn: Callable[[argparse.Namespace], dict[str, Any]]) -> None:
    args = parser(description).parse_args()
    try:
        result = fn(args)
        result.setdefault("status", "pass")
    except SmokeSkip as exc:
        result = {"status": "skip", "reason": str(exc)}
    except Exception as exc:  # pragma: no cover - smoke diagnostics
        result = {"status": "fail", "error_type": type(exc).__name__, "error": str(exc)}

    if args.json:
        print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    else:
        print(f"{result['status'].upper()}: {result.get('reason') or result.get('message') or result.get('error') or ''}")
    sys.exit(0 if result["status"] in {"pass", "skip"} else 1)


def require_live(args: argparse.Namespace) -> None:
    if not args.live:
        raise SmokeSkip("pass --live to run network/API smoke checks")


def has_gigachat_auth() -> bool:
    return bool(
        os.getenv("GIGACHAT_CREDENTIALS")
        or os.getenv("GIGACHAT_ACCESS_TOKEN")
        or (os.getenv("GIGACHAT_USER") and os.getenv("GIGACHAT_PASSWORD"))
    )


def require_gigachat_auth() -> None:
    if not has_gigachat_auth():
        raise SmokeSkip("set GIGACHAT_CREDENTIALS or GIGACHAT_USER+GIGACHAT_PASSWORD")


def import_or_skip(module: str) -> Any:
    try:
        return __import__(module, fromlist=["*"])
    except ImportError as exc:
        raise SmokeSkip(f"install dependency: {module}") from exc


def text_from_native_response(response: Any) -> str:
    """Extract text from either compatibility or chat-completions SDK responses."""
    # Compatibility response: response.choices[0].message.content
    choices = getattr(response, "choices", None)
    if choices:
        msg = getattr(choices[0], "message", None)
        content = getattr(msg, "content", None)
        if isinstance(content, str):
            return content
    # Primary response: response.messages[0].content[0].text
    messages = getattr(response, "messages", None)
    if messages:
        content = getattr(messages[0], "content", None)
        if isinstance(content, str):
            return content
        if content and hasattr(content[0], "text"):
            return content[0].text
    return str(response)


def native_client(model: str | None = None) -> Any:
    require_gigachat_auth()
    gigachat = import_or_skip("gigachat")
    kwargs: dict[str, Any] = {}
    if model:
        kwargs["model"] = model
    return gigachat.GigaChat(**kwargs)


def run_native_chat(args: argparse.Namespace) -> dict[str, Any]:
    require_live(args)
    with native_client(args.model) as client:
        response = client.chat("Reply with one short sentence: smoke ok")
    text = text_from_native_response(response)
    if not text.strip():
        raise RuntimeError("empty chat response")
    return {"message": "native chat returned text", "text_preview": text[:120]}


def run_native_stream(args: argparse.Namespace) -> dict[str, Any]:
    require_live(args)
    chunks = []
    with native_client(args.model) as client:
        for chunk in client.stream("Say: stream ok"):
            delta = getattr(getattr(chunk.choices[0], "delta", None), "content", "")
            if delta:
                chunks.append(delta)
    if not "".join(chunks).strip():
        raise RuntimeError("empty stream response")
    return {"message": "native stream returned deltas", "chunks": len(chunks)}


def run_native_embeddings(args: argparse.Namespace) -> dict[str, Any]:
    require_live(args)
    with native_client(None) as client:
        result = client.embeddings(["hello", "world"], model=args.embeddings_model)
    vectors = getattr(result, "data", None) or []
    if not vectors:
        raise RuntimeError("no embeddings returned")
    dim = len(vectors[0].embedding)
    return {"message": "native embeddings returned vectors", "dimensions": dim}


def post_json(url: str, payload: dict[str, Any], api_key: str | None = None) -> dict[str, Any]:
    data = json.dumps(payload).encode("utf-8")
    headers = {"Content-Type": "application/json"}
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")[:500]
        raise RuntimeError(f"HTTP {exc.code} from {url}: {body}") from exc
    except urllib.error.URLError as exc:
        raise SmokeSkip(f"gpt2giga proxy is not reachable at {url}: {exc}") from exc


def run_gpt2giga_openai_chat(args: argparse.Namespace) -> dict[str, Any]:
    require_live(args)
    payload = {
        "model": args.model,
        "messages": [{"role": "user", "content": "Reply with: openai smoke ok"}],
        "max_tokens": 32,
    }
    result = post_json(f"{args.base_url.rstrip('/')}/chat/completions", payload, args.api_key)
    text = result.get("choices", [{}])[0].get("message", {}).get("content", "")
    if not text:
        raise RuntimeError("empty OpenAI-compatible chat response")
    return {"message": "gpt2giga OpenAI chat returned text", "text_preview": text[:120]}


def run_gpt2giga_anthropic_chat(args: argparse.Namespace) -> dict[str, Any]:
    require_live(args)
    # Anthropic-compatible routes are commonly exposed under /v1/messages.
    base = args.base_url.rstrip("/")
    if base.endswith("/v1"):
        base = base[:-3]
    payload = {
        "model": args.model,
        "messages": [{"role": "user", "content": "Reply with: anthropic smoke ok"}],
        "max_tokens": 32,
    }
    result = post_json(f"{base}/v1/messages", payload, args.api_key)
    content = result.get("content") or []
    if not content:
        raise RuntimeError("empty Anthropic-compatible response")
    return {"message": "gpt2giga Anthropic messages returned content", "blocks": len(content)}


def run_gpt2giga_embeddings(args: argparse.Namespace) -> dict[str, Any]:
    require_live(args)
    payload = {"model": args.embeddings_model, "input": ["hello", "world"]}
    result = post_json(f"{args.base_url.rstrip('/')}/embeddings", payload, args.api_key)
    data = result.get("data") or []
    if not data:
        raise RuntimeError("empty embeddings response")
    return {"message": "gpt2giga embeddings returned vectors", "vectors": len(data)}


def fixture_file(kind: str | None, explicit_path: str | None) -> Path:
    if explicit_path:
        return Path(explicit_path)
    kind = kind or "image"
    tmp = Path(tempfile.mkdtemp(prefix="gigachat-skill-smoke-"))
    if kind == "image":
        # 1x1 transparent PNG
        p = tmp / "pixel.png"
        p.write_bytes(base64.b64decode("iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+/p9sAAAAASUVORK5CYII="))
        return p
    if kind == "audio":
        p = tmp / "silence.wav"
        with wave.open(str(p), "wb") as w:
            w.setnchannels(1)
            w.setsampwidth(2)
            w.setframerate(8000)
            w.writeframes(b"\x00\x00" * 800)
        return p
    if kind == "pdf":
        p = tmp / "hello.pdf"
        p.write_bytes(b"%PDF-1.4\n1 0 obj<<>>endobj\ntrailer<<>>\n%%EOF\n")
        return p
    p = tmp / "hello.txt"
    p.write_text("Hello from a GigaChat skill smoke fixture.\n", encoding="utf-8")
    return p


def upload_file_best_effort(client: Any, path: Path) -> str:
    # SDK APIs have changed over time; try common shapes conservatively.
    if hasattr(client, "upload_file"):
        uploaded = client.upload_file(open(path, "rb"))
    elif hasattr(client, "files") and hasattr(client.files, "upload"):
        uploaded = client.files.upload(file=open(path, "rb"))
    else:
        raise SmokeSkip("installed gigachat SDK does not expose a known file upload helper")
    return str(getattr(uploaded, "id_", None) or getattr(uploaded, "id", None) or getattr(uploaded, "file_id", None) or uploaded)


def run_native_file_upload(args: argparse.Namespace) -> dict[str, Any]:
    require_live(args)
    path = fixture_file(args.file_kind or "text", args.file)
    with native_client(None) as client:
        file_id = upload_file_best_effort(client, path)
    if not file_id:
        raise RuntimeError("upload did not return a file id")
    return {"message": "native file upload returned an id", "file_id_preview": file_id[:24], "fixture": str(path)}
