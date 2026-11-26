"""Entry for make.fun bounty "The Painfully Honest Out-of-Office".

One line, in a real employee's own voice: out until Monday, inbox at
4,312 unread, and none of them read with enthusiasm. The honesty is
specific (a concrete inbox number + an admission no one says out loud),
the politeness is the wrapper ("please expect the same energy on my
return") so a manager lets it stand, and the punchline lands on the
last words. One sentence, one clean punchline, no list of complaints,
no cliche ("limited access to email", "thank you for your patience").
"""

from pathlib import Path

TEXT = "I'm out until Monday. My inbox has 4,312 unread emails and I have read none of them with enthusiasm — please expect the same energy on my return."

OUT = Path("/output/entry.txt")


def check_len(text, lo=1, hi=200):
    size = len(text)
    assert lo <= size <= hi, f"entry must be {lo}-{hi} chars, got {size}"
    return size


def check_single_line(text):
    """Entry must be exactly one line: no newline chars, no trailing space.

    The bounty is a single out-of-office line; a stray newline or trailing
    space would break the one-line format and change the character count
    on round-trip. Checked here, and re-checked after the write.
    """
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text == text.rstrip(), "entry must not end with trailing space"
    assert text == text.strip(), "entry must not start with whitespace"
    return text


def save_line(path, text):
    check_single_line(text)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as fh:
        fh.write(text)


def main():
    check_len(TEXT)
    check_single_line(TEXT)
    save_line(OUT, TEXT)
    saved = OUT.read_text(encoding="utf-8")
    assert saved == TEXT, "round-trip mismatch"
    check_single_line(saved)
    print(f"wrote {len(TEXT)} chars to {OUT}")


if __name__ == "__main__":
    main()
