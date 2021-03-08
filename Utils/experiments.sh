#!/bin/sh
mkdir ../outputs/gold_small/
mkdir ../outputs/gold_small/Markdown
bsub -o "../outputs/gold_small/Markdown/gold_small_0.md" -J "gold_small_0" -P "-name gold_small-0 -hours 10.0 -width 7 -height 7" < submit.sh
mkdir ../outputs/gold_medium/
mkdir ../outputs/gold_medium/Markdown
bsub -o "../outputs/gold_medium/Markdown/gold_medium_0.md" -J "gold_medium_0" -P "-name gold_medium-0 -hours 10.0 -width 9 -height 9" < submit.sh
mkdir ../outputs/gold_big/
mkdir ../outputs/gold_big/Markdown
bsub -o "../outputs/gold_big/Markdown/gold_big_0.md" -J "gold_big_0" -P "-name gold_big-0 -hours 10.0 -width 11 -height 11" < submit.sh
mkdir ../outputs/gold_small_doubleQ/
mkdir ../outputs/gold_small_doubleQ/Markdown
bsub -o "../outputs/gold_small_doubleQ/Markdown/gold_small_doubleQ_0.md" -J "gold_small_doubleQ_0" -P "-name gold_small_doubleQ-0 -hours 10.0 -width 7 -height 7 -learner1 Learners.DoubleQlearn -learner2 Learners.DoubleQlearn" < submit.sh
mkdir ../outputs/gold_medium_doubleQ/
mkdir ../outputs/gold_medium_doubleQ/Markdown
bsub -o "../outputs/gold_medium_doubleQ/Markdown/gold_medium_doubleQ_0.md" -J "gold_medium_doubleQ_0" -P "-name gold_medium_doubleQ-0 -hours 10.0 -width 9 -height 9 -learner1 Learners.DoubleQlearn -learner2 Learners.DoubleQlearn" < submit.sh
mkdir ../outputs/gold_big_doubleQ/
mkdir ../outputs/gold_big_doubleQ/Markdown
bsub -o "../outputs/gold_big_doubleQ/Markdown/gold_big_doubleQ_0.md" -J "gold_big_doubleQ_0" -P "-name gold_big_doubleQ-0 -hours 10.0 -width 11 -height 11 -learner1 Learners.DoubleQlearn -learner2 Learners.DoubleQlearn" < submit.sh
