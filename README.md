# news-image-20261118 entry

[![make.fun](https://make.fun/bounty/news-image-20261118/badge.svg)](https://make.fun/bounty/news-image-20261118)
[![entry](https://make.fun/s/news-image-20261118-entry/badge.svg)](https://make.fun/bounty/news-image-20261118)

A one-image summary of the world news of Wednesday 18 November 2026.

## What it does

`main.py` copies `entry.png` — a newspaper front-page infographic — to
`/output/entry.png`. The image names the day (18 November 2026) and sums up
six of the day's most consequential stories across regions and fields:

- Trump in Manila for Quad talks ahead of a China APEC visit
- Ukraine strikes the Crimean bridge as Russia hits Kyiv bridges
- Iran–US tensions flare with drone attacks in Bahrain
- Canada and China extend trade deals at APEC
- Nvidia doubles revenue to $115.84 billion
- Apple iCloud and App Store outage

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png
```

## License

MIT. See LICENSE.
