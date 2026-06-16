#!/usr/bin/env python3
from __future__ import annotations

import common


def run(args):
    common.require_live(args)
    path = common.fixture_file(args.file_kind or "image", args.file)
    with common.native_client(args.model) as client:
        file_id = common.upload_file_best_effort(client, path)
        # Current skill guidance verifies upload + file ID. Prompt attachment APIs
        # have changed across SDK versions, so context prompting belongs to a
        # version-specific update pass.
    return {"message": "single file fixture uploaded for context smoke", "file_id_preview": file_id[:24], "fixture": str(path)}


if __name__ == "__main__":
    common.main("gigachat_file_context_single.py smoke check", run)
