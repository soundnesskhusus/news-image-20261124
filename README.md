# 24 November 2026 — World News in One Image

[![make.fun](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/soundnesskhusus/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/soundnesskhusus/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124)

Entry for the [make.fun bounty "Sum up 24 November's world news in one
image"](https://make.fun/bounty/news-image-20261124).

A newspaper front page that sums up Tuesday 24 November 2026 in six
verified stories: the Huawei jury verdict in Brooklyn, Iran's claim of
a fourth tanker hitting a mine in the Strait of Hormuz, the Russian
strike on Zaporizhzhia, Jensen Huang's apology a day after his return
to Nvidia, the killing of Hamas security chief Naeem Abu Nahel in Gaza,
and the hostage standoff at a Cartagena supermarket.

## How it works

`main.py` copies the bundled `entry.png` (1024x1024, drawn in-session
with Pillow) to `/output/entry.png` and checks it is a valid PNG of
the right size and under the 1 MiB cap. No network, no randomness:
two runs write identical bytes.

Run it locally with:

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```
