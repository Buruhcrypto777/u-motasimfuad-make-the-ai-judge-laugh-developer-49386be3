"""Make the AI Judge Laugh: Developer Excuses.

Writes one funny single-line excuse a developer gives when code breaks
in production to /output/entry.txt. Pure stdlib, deterministic.
"""

import os

EXCUSE = (
    "The config typo was one character. "
    "The outage was four hours. "
    "The postmortem is twelve pages."
)


def main():
    # Gate: one line, 1-200 characters, not only whitespace.
    text = EXCUSE.strip()
    assert 1 <= len(text) <= 200, "excuse must be 1-200 characters"
    assert "\n" not in text, "excuse must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError:
        out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
        os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(EXCUSE + "\n")
    print(path)


if __name__ == "__main__":
    main()
