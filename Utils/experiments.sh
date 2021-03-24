#!/bin/sh
mkdir ../outputs/test_METAk100000new/
mkdir ../outputs/test_METAk100000new/Markdown
bsub -o "../outputs/test_METAk100000new/Markdown/test_METAk100000new_0.md" -J "test_METAk100000new_0" -P "-name test_METAk100000new-0 -hours 4.0 -level Levels.Causal1 -K 100000.0" < submit.sh
mkdir ../outputs/test_METAk500000new/
mkdir ../outputs/test_METAk500000new/Markdown
bsub -o "../outputs/test_METAk500000new/Markdown/test_METAk500000new_0.md" -J "test_METAk500000new_0" -P "-name test_METAk500000new-0 -hours 4.0 -level Levels.Causal1 -K 500000.0" < submit.sh
mkdir ../outputs/test_METAk1000000new/
mkdir ../outputs/test_METAk1000000new/Markdown
bsub -o "../outputs/test_METAk1000000new/Markdown/test_METAk1000000new_0.md" -J "test_METAk1000000new_0" -P "-name test_METAk1000000new-0 -hours 4.0 -level Levels.Causal1 -K 1000000.0" < submit.sh
