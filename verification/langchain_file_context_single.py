#!/usr/bin/env python3
from __future__ import annotations

import common


def run(args):
    common.require_live(args)
    common.import_or_skip("langchain_gigachat.chat_models")
    path = common.fixture_file(args.file_kind or "image", args.file)
    with common.native_client(args.model) as client:
        file_id = common.upload_file_best_effort(client, path)
    return {"message": "LangChain file-context prerequisite uploaded through underlying SDK", "file_id_preview": file_id[:24], "fixture": str(path)}


if __name__ == "__main__":
    common.main("langchain_file_context_single.py smoke check", run)
