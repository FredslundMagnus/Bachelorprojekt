#!/bin/sh
mkdir ../outputs/causal2_9x9_0.3/
mkdir ../outputs/causal2_9x9_0.3/Markdown
bsub -o "../outputs/causal2_9x9_0.3/Markdown/causal2_9x9_0.3_0.md" -J "causal2_9x9_0.3_0" -P "-name causal2_9x9_0.3-0 -hours 10.0 -level Levels.Causal2" < submit.sh
bsub -o "../outputs/causal2_9x9_0.3/Markdown/causal2_9x9_0.3_1.md" -J "causal2_9x9_0.3_1" -P "-name causal2_9x9_0.3-1 -hours 10.0 -level Levels.Causal2" < submit.sh
bsub -o "../outputs/causal2_9x9_0.3/Markdown/causal2_9x9_0.3_2.md" -J "causal2_9x9_0.3_2" -P "-name causal2_9x9_0.3-2 -hours 10.0 -level Levels.Causal2" < submit.sh
bsub -o "../outputs/causal2_9x9_0.3/Markdown/causal2_9x9_0.3_3.md" -J "causal2_9x9_0.3_3" -P "-name causal2_9x9_0.3-3 -hours 10.0 -level Levels.Causal2" < submit.sh
