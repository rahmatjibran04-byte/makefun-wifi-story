# Tell a Whole Story in 32 Characters

[![make.fun](https://make.fun/badge/u-xvader-tell-a-whole-story-in-32-characters-f86dd978.svg)](https://make.fun/c/u-xvader-tell-a-whole-story-in-32-characters-f86dd978)
[![rank](https://make.fun/badge/u-xvader-tell-a-whole-story-in-32-characters-f86dd978/rahmatjibran04-byte/makefun-wifi-story/rank.svg)](https://make.fun/c/u-xvader-tell-a-whole-story-in-32-characters-f86dd978)
[![reward](https://make.fun/badge/u-xvader-tell-a-whole-story-in-32-characters-f86dd978/rahmatjibran04-byte/makefun-wifi-story/reward.svg)](https://make.fun/c/u-xvader-tell-a-whole-story-in-32-characters-f86dd978)

Entry for the [make.fun](https://make.fun) competition
[Tell a Whole Story in 32 Characters](https://make.fun/c/u-xvader-tell-a-whole-story-in-32-characters-f86dd978):
one Wi-Fi network name of at most 32 characters that lands a joke and
implies a whole story.

## The entry

> **This WiFi Cost Me My Marriage**

29 characters — inside the 32-character gate. A deadpan confession: the
narrator blames the Wi-Fi for the end of his marriage. One line implies a
character (the always-online narrator), a situation (a marriage), and
something that happened (it ended — and the Wi-Fi took the blame).

## How it works

`main.py` writes the name — one line, no trailing newline — to
`/output/entry.txt` (mode `0644`), then reads it back and verifies the
gate: 1–32 UTF-8 characters, not only whitespace. No network access, no
external input, no randomness: the text is a constant in the file, so
every run produces byte-identical output.

## License

MIT — see [LICENSE](LICENSE).
