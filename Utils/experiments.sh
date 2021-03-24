#!/bin/sh
mkdir ../outputs/test_METAk100000/
mkdir ../outputs/test_METAk100000/Markdown
bsub -o "../outputs/test_METAk100000/Markdown/test_METAk100000_0.md" -J "test_METAk100000_0" -P "-name test_METAk100000-0 -hours 4.0 -level Levels.Causal1 -K 100000.0" < submit.sh
mkdir ../outputs/test_METAk500000/
mkdir ../outputs/test_METAk500000/Markdown
bsub -o "../outputs/test_METAk500000/Markdown/test_METAk500000_0.md" -J "test_METAk500000_0" -P "-name test_METAk500000-0 -hours 4.0 -level Levels.Causal1 -K 500000.0" < submit.sh
mkdir ../outputs/test_METAk1000000/
mkdir ../outputs/test_METAk1000000/Markdown
bsub -o "../outputs/test_METAk1000000/Markdown/test_METAk1000000_0.md" -J "test_METAk1000000_0" -P "-name test_METAk1000000-0 -hours 4.0 -level Levels.Causal1 -K 1000000.0" < submit.sh
