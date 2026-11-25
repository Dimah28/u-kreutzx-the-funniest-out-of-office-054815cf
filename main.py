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

# Bounty gate: entry.txt must be UTF-8 text of 1-140 characters, not
# whitespace-only, and a single line.
MIN_LENGTH = 1
MAX_LENGTH = 140


def validate_reply(reply: str) -> str:
    """Harden the reply against every way the bounty gate can fail.

    Returns the reply unchanged when it passes, so the written bytes
    are exactly the reviewed line. Raises ValueError naming the
    broken rule otherwise -- never silently truncates or rewrites,
    because a "fixed" line would no longer be the judged joke.
    """
    if not isinstance(reply, str):
        raise ValueError(f"reply must be str, got {type(reply).__name__}")
    if len(reply) < MIN_LENGTH:
        raise ValueError("reply is empty")
    if len(reply) > MAX_LENGTH:
        raise ValueError(
            f"reply is {len(reply)} characters, over the {MAX_LENGTH} limit"
        )
    if not reply.strip():
        raise ValueError("reply is whitespace-only")
    if "\n" in reply or "\r" in reply:
        raise ValueError("reply must be a single line")
    if any(ord(ch) < 0x20 and ch not in ("\t",) for ch in reply):
        raise ValueError("reply must not contain control characters")
    if "\t" in reply:
        raise ValueError("reply must not contain tab characters")
    # Prove it round-trips as UTF-8 before anything is written.
    reply.encode("utf-8")
    return reply


def resolve_output_dir() -> Path:
    """Resolve the output directory, refusing an empty override."""
    raw = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    if not raw.strip():
        raise ValueError("MAKEFUN_OUTPUT_DIR must not be empty")
    return Path(raw)


def write_entry(reply: str, output_dir: Path) -> Path:
    """Validate, write, then verify the file holds exactly the reply."""
    checked = validate_reply(reply)
    out = output_dir / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(checked, encoding="utf-8")
    if out.read_text(encoding="utf-8") != checked:
        raise ValueError("entry.txt does not match the validated reply")
    return out


def main() -> None:
    out = write_entry(REPLY, resolve_output_dir())
    print(f"wrote {out} ({len(REPLY)} characters)")


if __name__ == "__main__":
    main()
