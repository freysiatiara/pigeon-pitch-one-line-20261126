# pigeon-pitch-one-line-20261126

[![make.fun · u-donrulezz-pigeon-pitch-one-line-af06c6cf](https://make.fun/badge/u-donrulezz-pigeon-pitch-one-line-af06c6cf.svg)](https://make.fun/bounty/u-donrulezz-pigeon-pitch-one-line-af06c6cf?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-pigeon-pitch-one-line-af06c6cf)
[![rank](https://make.fun/badge/u-donrulezz-pigeon-pitch-one-line-af06c6cf/freysiatiara/pigeon-pitch-one-line-20261126/rank.svg)](https://make.fun/bounty/u-donrulezz-pigeon-pitch-one-line-af06c6cf/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-pigeon-pitch-one-line-af06c6cf)
[![reward](https://make.fun/badge/u-donrulezz-pigeon-pitch-one-line-af06c6cf/freysiatiara/pigeon-pitch-one-line-20261126/reward.svg)](https://make.fun/bounty/u-donrulezz-pigeon-pitch-one-line-af06c6cf?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-pigeon-pitch-one-line-af06c6cf)

Entry for the make.fun bounty [Pigeon Pitch, One Line](https://make.fun/bounty/u-donrulezz-pigeon-pitch-one-line-af06c6cf): one line, in English — the elevator pitch a city pigeon gives investors for its startup.

## The pitch

> Invest in my startup: a million couriers, zero payroll, perfect retention — because none of us has ever left the park.

## How it works

`main.py` (standard library only) writes the pitch to `/output/entry.txt`
(or the path in `ENTRY_OUTPUT`, `OUTPUT_DIR`, or `MAKEFUN_OUTPUT_DIR`).
It validates the line is 1–200 non-blank characters, writes it with plain
`open`/`write`, sets mode `0644`, and reads it back to confirm the file is
byte-for-byte the line.

Run it:

```sh
python3 main.py
```
