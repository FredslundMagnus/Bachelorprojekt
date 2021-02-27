#!/bin/sh
mkdir ../outputs/test_run_7/
mkdir ../outputs/test_run_7/Markdown
mkdir ../outputs/test_run_7/Agents
mkdir ../outputs/test_run_7/Collectors
bsub -o "../outputs/test_run_7/Markdown/test_run_7_0.md" -J "test_run_7_0" -P "-name test_run_7-0 -gamma 1 -network Networks.Small -learner Learners.DoubleQlearn -hours 0.2" < submit.sh
