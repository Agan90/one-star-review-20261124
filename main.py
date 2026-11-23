"""One-Star Review of Something Essential entry.

Writes one deadpan one-star review of sleep to /output/entry.txt.
Standard library only, so the program runs unchanged in the grader's
Python 3.13 sandbox.
"""

import os

LINE = (
    "One star. Sleep requires eight uninterrupted hours, offers no pause "
    "button, and ends exactly when it gets good."
)


def resolve_output_dir():
    """The grader provides /output; a local run may point elsewhere."""
    override = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if override:
        return override
    return "/output"


def main():
    if not 1 <= len(LINE) <= 160:
        raise SystemExit("entry line must be 1-160 characters")
    out_dir = resolve_output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
