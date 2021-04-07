#!/bin/sh
mkdir ../outputs/causal3_demo/
mkdir ../outputs/causal3_demo/Markdown
bsub -o "../outputs/causal3_demo/Markdown/causal3_demo_0.md" -J "causal3_demo_0" -P "-name causal3_demo-0 -hours 16.0 -level Levels.Causal3 -main teleport" < submit.sh
bsub -o "../outputs/causal3_demo/Markdown/causal3_demo_1.md" -J "causal3_demo_1" -P "-name causal3_demo-1 -hours 16.0 -level Levels.Causal3 -main teleport" < submit.sh
