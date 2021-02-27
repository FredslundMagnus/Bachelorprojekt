#!/bin/sh
mkdir ../outputs/test_run_6/
mkdir ../outputs/test_run_6/Markdown
mkdir ../outputs/test_run_6/Agents
mkdir ../outputs/test_run_6/Collectors
bsub -o "../outputs/test_run_6/Markdown/test_run_6_0.md" -J "test_run_6_0" -P "-name test_run_6-0 -gamma 1 -network Networks.Small -learner Learners.DoubleQlearn -hours 0.2" < submit.sh
