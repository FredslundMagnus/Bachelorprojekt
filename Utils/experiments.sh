#!/bin/sh
mkdir ../outputs/causal2_9x9/
mkdir ../outputs/causal2_9x9/Markdown
bsub -o "../outputs/causal2_9x9/Markdown/causal2_9x9_0.md" -J "causal2_9x9_0" -P "-name causal2_9x9-0 -hours 10.0 -level Levels.Causal2" < submit.sh
bsub -o "../outputs/causal2_9x9/Markdown/causal2_9x9_1.md" -J "causal2_9x9_1" -P "-name causal2_9x9-1 -hours 10.0 -level Levels.Causal2" < submit.sh
bsub -o "../outputs/causal2_9x9/Markdown/causal2_9x9_2.md" -J "causal2_9x9_2" -P "-name causal2_9x9-2 -hours 10.0 -level Levels.Causal2" < submit.sh
bsub -o "../outputs/causal2_9x9/Markdown/causal2_9x9_3.md" -J "causal2_9x9_3" -P "-name causal2_9x9-3 -hours 10.0 -level Levels.Causal2" < submit.sh
