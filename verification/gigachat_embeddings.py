#!/usr/bin/env python3
from __future__ import annotations

import common


def run(args):
    return common.run_native_embeddings(args)


if __name__ == "__main__":
    common.main("gigachat_embeddings.py smoke check", run)
