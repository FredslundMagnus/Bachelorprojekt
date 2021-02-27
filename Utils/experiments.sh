#!/bin/sh
mkdir ../outputs/test_run_2/
mkdir ../outputs/test_run_2/Markdown
mkdir ../outputs/test_run_2/Agents
mkdir ../outputs/test_run_2/Collectors
bsub -o "../outputs/test_run_2/Markdown/test_run_2_0.md" -J "test_run_2_0" -P "-name test_run_2-0 -gamma 1 -network Networks.Small -learner Learners.DoubleQlearn -hours 0.2" < submit.sh
