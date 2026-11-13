# A make.fun ai-joke-03 entry (Python 3.13, standard library only): it writes one
# fixed joke, a one-liner about AI coding agents, to /output/entry.txt.
# The gate takes UTF-8 text of 1 to 280 characters that is not only white space,
# and the judge reads exactly the bytes written, so write no line end you do
# not mean to show.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

JOKE = "My AI agent's code was so raw, Gordon Ramsay sent it back \u2014 and it came back with a new variable name and the same bug."

os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(JOKE)
