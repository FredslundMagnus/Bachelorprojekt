#!/bin/sh
mkdir ../outputs/test_run/
mkdir ../outputs/test_run/Markdown
mkdir ../outputs/test_run/Agents
mkdir ../outputs/test_run/Collectors
bsub -o "../outputs/test_run/Markdown/test_run_0.md" -J "test_run_0" -P "-name test_run-0 -gamma 1 -network Networks.Small -learner Learners.DoubleQlearn -hours 0.2" < submit.sh
