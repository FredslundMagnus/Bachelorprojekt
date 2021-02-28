#!/bin/sh
mkdir ../outputs/test_run_8/
mkdir ../outputs/test_run_8/Markdown
mkdir ../outputs/test_run_8/Agents
mkdir ../outputs/test_run_8/Collectors
bsub -o "../outputs/test_run_8/Markdown/test_run_8_0.md" -J "test_run_8_0" -P "-name test_run_8-0 -gamma 1.0 -network Networks.Small -learner Learners.DoubleQlearn -hours 3.0" < submit.sh
