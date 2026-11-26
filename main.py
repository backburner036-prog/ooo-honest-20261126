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


EM_DASH = "\u2014"


def validate_entry(text, lo=1, hi=200):
    """Single validation gate for the entry: length, one line, punctuation.

    Consolidates the old check_len + check_single_line into one function
    so every writer (main, save_line, round-trip re-check) runs the same
    gate: length bounds, exactly one line (no newline/CR, no leading or
    trailing whitespace), and the punchline's dash must be the real
    em-dash U+2014 -- not a hyphen or double hyphen, which would flatten
    the pause before "please expect the same energy on my return".
    """
    size = len(text)
    assert lo <= size <= hi, f"entry must be {lo}-{hi} chars, got {size}"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text == text.strip(), "entry must not start/end with whitespace"
    assert EM_DASH in text, "entry must keep its em-dash (U+2014)"
    assert "--" not in text, "entry must not use a double hyphen for the dash"
    return size


def save_line(path, text):
    validate_entry(text)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as fh:
        fh.write(text)


def main():
    validate_entry(TEXT)
    save_line(OUT, TEXT)
    saved = OUT.read_text(encoding="utf-8")
    assert saved == TEXT, "round-trip mismatch"
    validate_entry(saved)
    print(f"wrote {len(TEXT)} chars to {OUT}")


if __name__ == "__main__":
    main()
