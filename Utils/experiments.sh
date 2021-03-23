#!/bin/sh
mkdir ../outputs/Rocks_9x9_META/
mkdir ../outputs/Rocks_9x9_META/Markdown
bsub -o "../outputs/Rocks_9x9_META/Markdown/Rocks_9x9_META_0.md" -J "Rocks_9x9_META_0" -P "-name Rocks_9x9_META-0 -hours 11.0 -level Levels.Rocks" < submit.sh
bsub -o "../outputs/Rocks_9x9_META/Markdown/Rocks_9x9_META_1.md" -J "Rocks_9x9_META_1" -P "-name Rocks_9x9_META-1 -hours 11.0 -level Levels.Rocks" < submit.sh
mkdir ../outputs/causal2_9x9_META/
mkdir ../outputs/causal2_9x9_META/Markdown
bsub -o "../outputs/causal2_9x9_META/Markdown/causal2_9x9_META_0.md" -J "causal2_9x9_META_0" -P "-name causal2_9x9_META-0 -hours 11.0 -level Levels.Causal2" < submit.sh
bsub -o "../outputs/causal2_9x9_META/Markdown/causal2_9x9_META_1.md" -J "causal2_9x9_META_1" -P "-name causal2_9x9_META-1 -hours 11.0 -level Levels.Causal2" < submit.sh
