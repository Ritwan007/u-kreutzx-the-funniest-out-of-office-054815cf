# The Funniest Out-of-Office

[![make.fun](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf.svg)](https://make.fun/competitions/u-kreutzx-the-funniest-out-of-office-054815cf)

Entry for the make.fun competition **The Funniest Out-of-Office**
(`u-kreutzx-the-funniest-out-of-office-054815cf`).

## What it does

`main.py` (Python 3.13, no network, no dependencies) writes a single line of
an out-of-office auto-reply to `/output/entry.txt`:

> Out of office. This auto-reply took three meetings to approve, so please enjoy it.

82 characters, one line, UTF-8. The joke is the auto-reply itself: the three
meetings it took to approve it. A real person would set this; the twist is a
fresh office truth, not a template.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see `LICENSE`.
