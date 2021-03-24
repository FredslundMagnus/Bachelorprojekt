#!/bin/sh
mkdir ../outputs/Rocks_9x9_META_attempt2/
mkdir ../outputs/Rocks_9x9_META_attempt2/Markdown
bsub -o "../outputs/Rocks_9x9_META_attempt2/Markdown/Rocks_9x9_META_attempt2_0.md" -J "Rocks_9x9_META_attempt2_0" -P "-name Rocks_9x9_META_attempt2-0 -hours 11.0 -level Levels.Rocks" < submit.sh
mkdir ../outputs/causal1_9x9_META_attempt2/
mkdir ../outputs/causal1_9x9_META_attempt2/Markdown
bsub -o "../outputs/causal1_9x9_META_attempt2/Markdown/causal1_9x9_META_attempt2_0.md" -J "causal1_9x9_META_attempt2_0" -P "-name causal1_9x9_META_attempt2-0 -hours 11.0 -level Levels.Causal1" < submit.sh
mkdir ../outputs/Rocks_9x9_META_attempt2_highK/
mkdir ../outputs/Rocks_9x9_META_attempt2_highK/Markdown
bsub -o "../outputs/Rocks_9x9_META_attempt2_highK/Markdown/Rocks_9x9_META_attempt2_highK_0.md" -J "Rocks_9x9_META_attempt2_highK_0" -P "-name Rocks_9x9_META_attempt2_highK-0 -hours 11.0 -level Levels.Rocks -K 500000.0" < submit.sh
mkdir ../outputs/causal1_9x9_META_attempt2_highK/
mkdir ../outputs/causal1_9x9_META_attempt2_highK/Markdown
bsub -o "../outputs/causal1_9x9_META_attempt2_highK/Markdown/causal1_9x9_META_attempt2_highK_0.md" -J "causal1_9x9_META_attempt2_highK_0" -P "-name causal1_9x9_META_attempt2_highK-0 -hours 11.0 -level Levels.Causal1 -K 500000.0" < submit.sh
mkdir ../outputs/causal2_9x9_META_attempt2/
mkdir ../outputs/causal2_9x9_META_attempt2/Markdown
bsub -o "../outputs/causal2_9x9_META_attempt2/Markdown/causal2_9x9_META_attempt2_0.md" -J "causal2_9x9_META_attempt2_0" -P "-name causal2_9x9_META_attempt2-0 -hours 11.0 -level Levels.Causal2 -layer_Diamond1 True -layer_Diamond2 True -layer_Diamond3 True -layer_Diamond4 True -layer_Dirt False -layer_Rock False -layer_Gold False" < submit.sh
