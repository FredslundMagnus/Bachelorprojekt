#!/bin/sh
mkdir ../outputs/Rocks_9x9_META_attemp2/
mkdir ../outputs/Rocks_9x9_META_attemp2/Markdown
bsub -o "../outputs/Rocks_9x9_META_attemp2/Markdown/Rocks_9x9_META_attemp2_0.md" -J "Rocks_9x9_META_attemp2_0" -P "-name Rocks_9x9_META_attemp2-0 -hours 11.0 -level Levels.Rocks" < submit.sh
bsub -o "../outputs/Rocks_9x9_META_attemp2/Markdown/Rocks_9x9_META_attemp2_1.md" -J "Rocks_9x9_META_attemp2_1" -P "-name Rocks_9x9_META_attemp2-1 -hours 11.0 -level Levels.Rocks" < submit.sh
mkdir ../outputs/causal2_9x9_META_attempe2/
mkdir ../outputs/causal2_9x9_META_attempe2/Markdown
bsub -o "../outputs/causal2_9x9_META_attempe2/Markdown/causal2_9x9_META_attempe2_0.md" -J "causal2_9x9_META_attempe2_0" -P "-name causal2_9x9_META_attempe2-0 -hours 11.0 -level Levels.Causal1" < submit.sh
bsub -o "../outputs/causal2_9x9_META_attempe2/Markdown/causal2_9x9_META_attempe2_1.md" -J "causal2_9x9_META_attempe2_1" -P "-name causal2_9x9_META_attempe2-1 -hours 11.0 -level Levels.Causal1" < submit.sh
