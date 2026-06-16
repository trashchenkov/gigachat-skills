#!/usr/bin/env python3
from __future__ import annotations

import common


def run(args):
    common.require_live(args)
    image = common.fixture_file("image", None)
    pdf = common.fixture_file("pdf", None)
    with common.native_client(args.model) as client:
        image_id = common.upload_file_best_effort(client, image)
        pdf_id = common.upload_file_best_effort(client, pdf)
    return {
        "status": "pass",
        "message": "mixed-context prerequisites uploaded; actual multi-turn mixed modality remains a caution scenario",
        "caution": True,
        "file_ids": [image_id[:24], pdf_id[:24]],
    }


if __name__ == "__main__":
    common.main("gigachat_multiturn_mixed_context.py caution smoke check", run)
