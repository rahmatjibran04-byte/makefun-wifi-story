#!/usr/bin/env python3
"""Write the Wi-Fi network name entry to /output/entry.txt.

Entry: "This WiFi Cost Me My Marriage" (29 characters, inside the
32-character gate). The text is a constant baked into this file: no
network access, no external input, no randomness, so every run
produces byte-identical output.
"""

import os

ENTRY = "This WiFi Cost Me My Marriage"
OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(OUTPUT_PATH, 0o644)

    # Gate self-check: read back and verify the sealed scorer's rules
    # (UTF-8 text, 1-32 characters, not only whitespace) before exiting.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == ENTRY, "entry.txt does not match ENTRY"
    assert 1 <= len(written) <= 32, "entry must be 1-32 characters"
    assert written.strip(), "entry must not be only whitespace"


if __name__ == "__main__":
    main()
