#!/usr/bin/env python3
from __future__ import annotations

import common


def run(args):
    common.require_live(args)
    image = common.fixture_file("image", None)
    audio = common.fixture_file("audio", None)
    with common.native_client(args.model) as client:
        image_id = common.upload_file_best_effort(client, image)
        audio_id = common.upload_file_best_effort(client, audio)
    return {
        "status": "pass",
        "message": "mixed-modality fixtures can be uploaded; do not treat mixed-modality prompting as a safe default",
        "caution": True,
        "file_ids": [image_id[:24], audio_id[:24]],
    }


if __name__ == "__main__":
    common.main("gigachat_files_context.py caution smoke check", run)
