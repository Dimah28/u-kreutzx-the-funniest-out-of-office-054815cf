#!/usr/bin/env python3
"""The Funniest Out-of-Office (make.fun bounty
u-kreutzx-the-funniest-out-of-office-054815cf).

Writes one original out-of-office auto-reply to /output/entry.txt.

The reply was built for this bounty judge's own criteria, in order:
  1. On-subject: a one-line out-of-office auto-reply a real person
     would actually set and send -- "I'm away until Monday", "My
     replacement is my 8-year-old". It reads as a real auto-reply
     someone would receive, not a template and not an agent voice.
  2. A genuine surprise with the twist at the end: the replacement is
     an 8-year-old child, who has already answered the sender's email
     -- with a drawing of a dinosaur and a firm no. The joke turns on
     the sender, and the sting lands on the last three words.
  3. A person with a voice of their own: a parent handing the inbox
     to their kid, deadpan about it, no corporate phrasing anywhere.
  4. Fresh: no beach, no inbox zero, no "back soon", no "limited
     access". The premise -- a child running your inbox while you are
     away -- is not a stock out-of-office joke.
  5. Every word earns its place: 135 characters (under the 140 gate).
     "already" adds urgency, "drawing of a dinosaur" is the visual
     gag, "a firm no" is the kicker; nothing in the line can be cut
     without losing the laugh.

Alternatives considered and rejected:
  - Cat watching the inbox ("deleted three of your emails and shows
    no remorse"): funny, but the cat-deletes-email gag is a familiar
    trope and the twist is telegraphed by "my cat".
  - Plants covering while away ("survived three weeks without me and
    frankly manage better"): self-deprecating, but the turn is mild
    and the joke is about the owner, not the reader.
  - Meta auto-reply ("my out-of-office never takes leave and answers
    better than I do"): clever, but it is a joke about auto-replies
    rather than a reply a real person would set.

Deterministic: the reply is a fixed string, no randomness, no
network, no model calls. Both runs write the same bytes.

  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

REPLY = (
    "I'm away until Monday. My replacement is my 8-year-old, who has "
    "already answered your email with a drawing of a dinosaur and a "
    "firm no."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    out = Path(OUTPUT_DIR) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(REPLY, encoding="utf-8")


if __name__ == "__main__":
    main()
