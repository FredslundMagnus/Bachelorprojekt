#!/bin/sh
mkdir ../outputs/causal3_9x9_20hours/
mkdir ../outputs/causal3_9x9_20hours/Markdown
bsub -o "../outputs/causal3_9x9_20hours/Markdown/causal3_9x9_20hours_0.md" -J "causal3_9x9_20hours_0" -P "-name causal3_9x9_20hours-0 -hours 20.0 -level Levels.Causal3" < submit.sh
bsub -o "../outputs/causal3_9x9_20hours/Markdown/causal3_9x9_20hours_1.md" -J "causal3_9x9_20hours_1" -P "-name causal3_9x9_20hours-1 -hours 20.0 -level Levels.Causal3" < submit.sh
bsub -o "../outputs/causal3_9x9_20hours/Markdown/causal3_9x9_20hours_2.md" -J "causal3_9x9_20hours_2" -P "-name causal3_9x9_20hours-2 -hours 20.0 -level Levels.Causal3" < submit.sh
bsub -o "../outputs/causal3_9x9_20hours/Markdown/causal3_9x9_20hours_3.md" -J "causal3_9x9_20hours_3" -P "-name causal3_9x9_20hours-3 -hours 20.0 -level Levels.Causal3" < submit.sh
