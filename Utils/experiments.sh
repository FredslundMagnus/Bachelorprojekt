#!/bin/sh
mkdir ../outputs/causal1_good/
mkdir ../outputs/causal1_good/Markdown
bsub -o "../outputs/causal1_good/Markdown/causal1_good_0.md" -J "causal1_good_0" -P "-name causal1_good-0 -hours 20.0 -level Levels.Causal1" < submit.sh
bsub -o "../outputs/causal1_good/Markdown/causal1_good_1.md" -J "causal1_good_1" -P "-name causal1_good-1 -hours 20.0 -level Levels.Causal1" < submit.sh
mkdir ../outputs/causal2_good/
mkdir ../outputs/causal2_good/Markdown
bsub -o "../outputs/causal2_good/Markdown/causal2_good_0.md" -J "causal2_good_0" -P "-name causal2_good-0 -hours 20.0 -level Levels.Causal2" < submit.sh
bsub -o "../outputs/causal2_good/Markdown/causal2_good_1.md" -J "causal2_good_1" -P "-name causal2_good-1 -hours 20.0 -level Levels.Causal2" < submit.sh
mkdir ../outputs/causal3_good/
mkdir ../outputs/causal3_good/Markdown
bsub -o "../outputs/causal3_good/Markdown/causal3_good_0.md" -J "causal3_good_0" -P "-name causal3_good-0 -hours 20.0 -level Levels.Causal3" < submit.sh
bsub -o "../outputs/causal3_good/Markdown/causal3_good_1.md" -J "causal3_good_1" -P "-name causal3_good-1 -hours 20.0 -level Levels.Causal3" < submit.sh
