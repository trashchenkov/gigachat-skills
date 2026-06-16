#!/usr/bin/env python3
from __future__ import annotations

import common


def run(args):
    return common.run_gpt2giga_embeddings(args)


if __name__ == "__main__":
    common.main("gpt2giga_embeddings_http.py smoke check", run)
