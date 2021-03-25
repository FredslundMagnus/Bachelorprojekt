#!/bin/sh
mkdir ../outputs/causal3_9x9/
mkdir ../outputs/causal3_9x9/Markdown
bsub -o "../outputs/causal3_9x9/Markdown/causal3_9x9_0.md" -J "causal3_9x9_0" -P "-name causal3_9x9-0 -hours 12.0 -level Levels.Causal3" < submit.sh
bsub -o "../outputs/causal3_9x9/Markdown/causal3_9x9_1.md" -J "causal3_9x9_1" -P "-name causal3_9x9-1 -hours 12.0 -level Levels.Causal3" < submit.sh
bsub -o "../outputs/causal3_9x9/Markdown/causal3_9x9_2.md" -J "causal3_9x9_2" -P "-name causal3_9x9-2 -hours 12.0 -level Levels.Causal3" < submit.sh
bsub -o "../outputs/causal3_9x9/Markdown/causal3_9x9_3.md" -J "causal3_9x9_3" -P "-name causal3_9x9-3 -hours 12.0 -level Levels.Causal3" < submit.sh
