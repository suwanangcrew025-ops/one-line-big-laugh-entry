"""One Line, Big Laugh — entry program.

Writes a single funny line to /output/entry.txt. The house judge is a
stand-up comic turned comedy editor who wants a real joke, not a quirky
observation: it weighs, in order, a genuinely hilarious line of at most 200
characters, a turn somewhere the reader did not see coming, no wasted words,
freshness, and a line that stays in the head after one reading. This entry
answers with misdirection: a phone autocorrect turns a love note into a
debt, and the anniversary dinner turns into a debt-collection meeting with
candles, a payment plan, and a waiter asking for collateral — the romance
survives, but only on an instalment plan. The line ships
in line.txt; an identical fallback is built into this program, which
validates the 200-character cap and the single-line rule before writing.
"""

import os

FALLBACK_LINE = (
    "My phone autocorrected \"I love you\" to \"I owe you\", so my girlfriend "
    "now treats our anniversary dinner as a debt-collection meeting with "
    "candles, a payment plan, and a waiter asking for collateral."
)
MAX_CHARS = 200
SOURCE_NAME = "line.txt"
TARGET_NAME = "entry.txt"


def load_line():
    bot_dir = os.environ.get("MAKEFUN_BOT_DIR") or os.path.dirname(
        os.path.abspath(__file__)
    )
    try:
        with open(os.path.join(bot_dir, SOURCE_NAME), "r", encoding="utf-8") as handle:
            return handle.read().strip()
    except OSError:
        return ""


def is_valid(text):
    if not text or not text.strip():
        return False
    if len(text) > MAX_CHARS:
        return False
    if "\n" in text or "\r" in text:
        return False
    return True


def pick_line():
    candidate = load_line()
    if is_valid(candidate):
        return candidate
    return FALLBACK_LINE


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    line = pick_line()
    with open(os.path.join(out_dir, TARGET_NAME), "w", encoding="utf-8") as handle:
        handle.write(line)


if __name__ == "__main__":
    main()
