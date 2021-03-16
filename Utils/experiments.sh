#!/bin/sh
mkdir ../outputs/gold_9x9/
mkdir ../outputs/gold_9x9/Markdown
bsub -o "../outputs/gold_9x9/Markdown/gold_9x9_0.md" -J "gold_9x9_0" -P "-name gold_9x9-0 -hours 24.0 -width 9 -height 9" < submit.sh
bsub -o "../outputs/gold_9x9/Markdown/gold_9x9_1.md" -J "gold_9x9_1" -P "-name gold_9x9-1 -hours 24.0 -width 9 -height 9" < submit.sh
bsub -o "../outputs/gold_9x9/Markdown/gold_9x9_2.md" -J "gold_9x9_2" -P "-name gold_9x9-2 -hours 24.0 -width 9 -height 9" < submit.sh
mkdir ../outputs/gold_11x11/
mkdir ../outputs/gold_11x11/Markdown
bsub -o "../outputs/gold_11x11/Markdown/gold_11x11_0.md" -J "gold_11x11_0" -P "-name gold_11x11-0 -hours 24.0 -width 11 -height 11" < submit.sh
bsub -o "../outputs/gold_11x11/Markdown/gold_11x11_1.md" -J "gold_11x11_1" -P "-name gold_11x11-1 -hours 24.0 -width 11 -height 11" < submit.sh
bsub -o "../outputs/gold_11x11/Markdown/gold_11x11_2.md" -J "gold_11x11_2" -P "-name gold_11x11-2 -hours 24.0 -width 11 -height 11" < submit.sh
