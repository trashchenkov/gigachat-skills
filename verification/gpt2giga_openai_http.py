#!/usr/bin/env python3
from __future__ import annotations

import common


def run(args):
    return common.run_gpt2giga_openai_chat(args)


if __name__ == "__main__":
    common.main("gpt2giga_openai_http.py smoke check", run)
