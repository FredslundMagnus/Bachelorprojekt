#!/bin/sh
mkdir ../outputs/test_run_5/
mkdir ../outputs/test_run_5/Markdown
mkdir ../outputs/test_run_5/Agents
mkdir ../outputs/test_run_5/Collectors
bsub -o "../outputs/test_run_5/Markdown/test_run_5_0.md" -J "test_run_5_0" -P "-name test_run_5-0 -gamma 1 -network Networks.Small -learner Learners.DoubleQlearn -hours 0.2" < submit.sh
