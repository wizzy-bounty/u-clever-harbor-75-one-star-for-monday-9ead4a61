"""One Star for Monday — a one-star review of Monday as if it were a restaurant.

The entry line (109 characters, 21 words, single line, plain text):

    One star. The waiter took my order at 9 a.m. and served it next Monday.
    Cold coffee, warm apology, no refund.

Why this line: it opens in the voice of a real restaurant review ("One
star."), it names a concrete diner's complaint (a waiter, a cold coffee, a
bill with no refund), and its joke only works for Monday — the order placed
on a Monday morning is not served until the *next* Monday. Short enough to
retype into a group chat without trimming a word.
"""

import os
import sys

ENTRY = (
    "One star. The waiter took my order at 9 a.m. and served it "
    "next Monday. Cold coffee, warm apology, no refund."
)

MAX_CHARS = 180
MAX_WORDS = 25


def check_is_string(text):
    """Gate step: the entry must be a str."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")


def check_is_utf8(text):
    """Gate step: the entry must be encodable as UTF-8."""
    text.encode("utf-8")  # raises UnicodeEncodeError if not encodable


def check_char_length(text):
    """Gate step: 1 to MAX_CHARS characters."""
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(
            "entry must be 1 to %d characters, got %d" % (MAX_CHARS, len(text))
        )


def check_not_whitespace_only(text):
    """Gate step: the entry must contain more than whitespace."""
    if not text.strip():
        raise ValueError("entry must not be only whitespace")


def check_single_line(text):
    """Gate step: the entry must be one line, no line breaks."""
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def check_word_count(text):
    """Gate step: at most MAX_WORDS words."""
    words = text.split()
    if len(words) > MAX_WORDS:
        raise ValueError(
            "entry must be at most %d words, got %d" % (MAX_WORDS, len(words))
        )


def validate_entry(text):
    """Check one entry line against the competition gate.

    Rules: UTF-8 text of 1 to 180 characters, not only whitespace, a
    single line, at most 25 words. Raises ValueError on any violation.
    Each rule is checked by its own named step, in gate order.
    """
    check_is_string(text)
    check_is_utf8(text)
    check_char_length(text)
    check_not_whitespace_only(text)
    check_single_line(text)
    check_word_count(text)
    return text


def main():
    validate_entry(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = ENTRY.encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(data)
    # Round-trip check: what was written must read back byte-identical.
    with open(path, "rb") as fh:
        if fh.read() != data:
            raise SystemExit("round-trip check failed: entry.txt differs")
    print("chars: %d" % len(ENTRY))
    print(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
