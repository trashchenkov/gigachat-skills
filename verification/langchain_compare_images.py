#!/usr/bin/env python3
from __future__ import annotations

import common


def run(args):
    common.require_live(args)
    common.import_or_skip("langchain_gigachat.chat_models")
    first = common.fixture_file("image", args.file)
    second = common.fixture_file("image", None)
    with common.native_client(args.model) as client:
        id1 = common.upload_file_best_effort(client, first)
        id2 = common.upload_file_best_effort(client, second)
    return {"message": "LangChain multi-image prerequisite uploaded through underlying SDK", "file_ids": [id1[:24], id2[:24]]}


if __name__ == "__main__":
    common.main("langchain_compare_images.py smoke check", run)
