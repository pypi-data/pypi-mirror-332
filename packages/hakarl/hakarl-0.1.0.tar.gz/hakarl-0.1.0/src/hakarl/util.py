import re
from typing import Any


MULTIPLICATION_SIGN = "\u00D7"
DOUBLE_PRIME = "\u2033"
FRACTION_SLASH = "\u2044"
DEGREE = "\u00B0"
EN_DASH = "\u2013"
ELLIPSIS = "\u2026"
NARROW_NBSP = "\u202F"
APOSTROPHE = "\u2019"


def pretty(text: Any) -> str:
    text = str(text)

    def fix_dimensions(match: re.Match) -> str:
        chunk = match.group(0)
        parts = re.split(r'\s*x\s*', chunk)
        parts = [re.sub(r'(\d+)"', rf'\1{DOUBLE_PRIME}', p) for p in parts]
        return f'{NARROW_NBSP}{MULTIPLICATION_SIGN}{NARROW_NBSP}'.join(parts)

    # Replace dimension notation (e.g., 24" x 36")
    text = re.sub(r'\d+"(?:\s*x\s*\d+")+', fix_dimensions, text)

    # Replace inch marks with double primes
    text = re.sub(r'(\d+)"', rf'\1{DOUBLE_PRIME}', text)

    # Replace ASCII fraction slashes with proper fraction slashes
    text = re.sub(r'(\d+)/(\d+)', rf'\1{FRACTION_SLASH}\2', text)

    # Replace spaces in mixed numbers with narrow non-breaking spaces
    text = re.sub(r'(\d+)\s+(\d+%s\d+)' % FRACTION_SLASH, rf'\1{NARROW_NBSP}\2', text)

    # Ensure proper spacing in temperature
    text = re.sub(fr'(\d+)\s*{DEGREE}F', rf'\1{NARROW_NBSP}{DEGREE}F', text)

    # Replace hyphens between numbers with en dashes
    text = re.sub(r'\d+(?:-\d+)+', lambda m: m.group().replace('-', EN_DASH), text)

    # Replace ASCII ellipsis with single character ellipsis
    text = text.replace("...", ELLIPSIS)

    # Replace single quotes with apostrophes
    text = text.replace("'", APOSTROPHE)

    return text
