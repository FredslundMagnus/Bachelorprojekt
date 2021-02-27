#!/bin/sh
mkdir ../outputs/test_run_3/
mkdir ../outputs/test_run_3/Markdown
mkdir ../outputs/test_run_3/Agents
mkdir ../outputs/test_run_3/Collectors
bsub -o "../outputs/test_run_3/Markdown/test_run_3_0.md" -J "test_run_3_0" -P "-name test_run_3-0 -gamma 1 -network Networks.Small -learner Learners.DoubleQlearn -hours 0.2" < submit.sh
