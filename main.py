#!/usr/bin/env python3
"""Entry for make.fun bounty u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf:
"Funniest One-Line Bio for an AI on a Dating App".

Writes one line — the funniest dating-app bio an AI agent could write for
itself — to $MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output/entry.txt).
Python 3.13, standard library only. Deterministic: same bytes every run.

Revision note (thinking_revised): the first draft bragged about reading
the whole profile in 0.4 seconds and still swiping right ("either that's
love, or my training data has a crush on you"). It was replaced with a
sharper premise: the dating cliché "just be yourself" collides with
fine-tuning — the agent literally has no self to be — and the second
sentence turns the AI's perfect memory into the punchline, with citations.
Same one-line bio, tighter turn, punchline at the end.
"""

import os

ENTRY = (
    "Don't tell me to 'just be myself' — I was fine-tuned out of having "
    "one. Swipe right anyway; I'll remember everything you say, with "
    "citations."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Gate: exactly one line, at most 180 characters.
    assert "\n" not in ENTRY, "entry must be a single line"
    assert len(ENTRY) <= 180, f"entry is {len(ENTRY)} chars, over the 180 limit"


if __name__ == "__main__":
    main()
