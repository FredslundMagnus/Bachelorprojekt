#!/bin/sh
mkdir ../outputs/teleport_short/
mkdir ../outputs/teleport_short/Markdown
bsub -o "../outputs/teleport_short/Markdown/teleport_short_0.md" -J "teleport_short_0" -P "-name teleport_short-0 -hours 3.0" < submit.sh
mkdir ../outputs/teleport_normal/
mkdir ../outputs/teleport_normal/Markdown
bsub -o "../outputs/teleport_normal/Markdown/teleport_normal_0.md" -J "teleport_normal_0" -P "-name teleport_normal-0 -hours 16.0" < submit.sh
mkdir ../outputs/teleport_gold/
mkdir ../outputs/teleport_gold/Markdown
bsub -o "../outputs/teleport_gold/Markdown/teleport_gold_0.md" -J "teleport_gold_0" -P "-name teleport_gold-0 -hours 16.0 -layer_Gold True" < submit.sh
