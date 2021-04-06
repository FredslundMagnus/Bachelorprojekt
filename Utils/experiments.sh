#!/bin/sh
mkdir ../outputs/causal2_demo/
mkdir ../outputs/causal2_demo/Markdown
bsub -o "../outputs/causal2_demo/Markdown/causal2_demo_0.md" -J "causal2_demo_0" -P "-name causal2_demo-0 -hours 16.0 -level Levels.Causal2 -main teleport" < submit.sh
bsub -o "../outputs/causal2_demo/Markdown/causal2_demo_1.md" -J "causal2_demo_1" -P "-name causal2_demo-1 -hours 16.0 -level Levels.Causal2 -main teleport" < submit.sh
mkdir ../outputs/causal5_demo/
mkdir ../outputs/causal5_demo/Markdown
bsub -o "../outputs/causal5_demo/Markdown/causal5_demo_0.md" -J "causal5_demo_0" -P "-name causal5_demo-0 -hours 16.0 -level Levels.Causal5 -main teleport" < submit.sh
bsub -o "../outputs/causal5_demo/Markdown/causal5_demo_1.md" -J "causal5_demo_1" -P "-name causal5_demo-1 -hours 16.0 -level Levels.Causal5 -main teleport" < submit.sh
mkdir ../outputs/causal6_demo/
mkdir ../outputs/causal6_demo/Markdown
bsub -o "../outputs/causal6_demo/Markdown/causal6_demo_0.md" -J "causal6_demo_0" -P "-name causal6_demo-0 -hours 16.0 -level Levels.Causal6 -main teleport" < submit.sh
bsub -o "../outputs/causal6_demo/Markdown/causal6_demo_1.md" -J "causal6_demo_1" -P "-name causal6_demo-1 -hours 16.0 -level Levels.Causal6 -main teleport" < submit.sh
mkdir ../outputs/causal1_demo/
mkdir ../outputs/causal1_demo/Markdown
bsub -o "../outputs/causal1_demo/Markdown/causal1_demo_0.md" -J "causal1_demo_0" -P "-name causal1_demo-0 -hours 16.0 -level Levels.Causal1 -main teleport" < submit.sh
bsub -o "../outputs/causal1_demo/Markdown/causal1_demo_1.md" -J "causal1_demo_1" -P "-name causal1_demo-1 -hours 16.0 -level Levels.Causal1 -main teleport" < submit.sh
