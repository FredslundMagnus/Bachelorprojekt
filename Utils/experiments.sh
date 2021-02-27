#!/bin/sh
mkdir ../outputs/test_run_4/
mkdir ../outputs/test_run_4/Markdown
mkdir ../outputs/test_run_4/Agents
mkdir ../outputs/test_run_4/Collectors
bsub -o "../outputs/test_run_4/Markdown/test_run_4_0.md" -J "test_run_4_0" -P "-name test_run_4-0 -gamma 1 -network Networks.Small -learner Learners.DoubleQlearn -hours 0.2" < submit.sh
