"""Pigeon Pitch, One Line — make.fun entry.

Writes the one-line elevator pitch a city pigeon gives investors for its
startup to the output file. Standard library only.
"""

import os

LINE = (
    "Invest in my startup: a million couriers, zero payroll, "
    "perfect retention \u2014 because none of us has ever left the park."
)


def resolve_output_path():
    """Pick the output path: explicit env first, then /output, then local."""
    for env_name in ("ENTRY_OUTPUT", "OUTPUT_DIR", "MAKEFUN_OUTPUT_DIR"):
        value = os.environ.get(env_name)
        if value:
            if env_name == "ENTRY_OUTPUT":
                return value
            return os.path.join(value, "entry.txt")
    return "/output/entry.txt"


def main():
    # Validation guard: the gate requires 1-200 non-blank UTF-8 characters.
    assert 1 <= len(LINE) <= 200 and LINE.strip(), "entry line out of range"
    path = resolve_output_path()
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    os.chmod(path, 0o644)
    # Read-back check: what we wrote must be exactly the line, byte for byte.
    with open(path, "r", encoding="utf-8") as handle:
        assert handle.read() == LINE, "entry.txt differs from LINE"


if __name__ == "__main__":
    main()
