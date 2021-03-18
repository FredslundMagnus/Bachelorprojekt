#!/bin/sh
mkdir ../outputs/causal1_9x9/
mkdir ../outputs/causal1_9x9/Markdown
bsub -o "../outputs/causal1_9x9/Markdown/causal1_9x9_0.md" -J "causal1_9x9_0" -P "-name causal1_9x9-0 -hours 12.0 -width 9 -height 9 -level Levels.Causal1 -main teleport" < submit.sh
bsub -o "../outputs/causal1_9x9/Markdown/causal1_9x9_1.md" -J "causal1_9x9_1" -P "-name causal1_9x9-1 -hours 12.0 -width 9 -height 9 -level Levels.Causal1 -main teleport" < submit.sh
bsub -o "../outputs/causal1_9x9/Markdown/causal1_9x9_2.md" -J "causal1_9x9_2" -P "-name causal1_9x9-2 -hours 12.0 -width 9 -height 9 -level Levels.Causal1 -main teleport" < submit.sh
