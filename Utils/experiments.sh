#!/bin/sh
mkdir ../outputs/causal7_demo/
mkdir ../outputs/causal7_demo/Markdown
bsub -o "../outputs/causal7_demo/Markdown/causal7_demo_0.md" -J "causal7_demo_0" -P "-name causal7_demo-0 -hours 16.0 -level Levels.Causal7 -main teleport" < submit.sh
bsub -o "../outputs/causal7_demo/Markdown/causal7_demo_1.md" -J "causal7_demo_1" -P "-name causal7_demo-1 -hours 16.0 -level Levels.Causal7 -main teleport" < submit.sh
