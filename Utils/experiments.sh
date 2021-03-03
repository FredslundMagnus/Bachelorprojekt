#!/bin/sh
mkdir ../outputs/test_run_9/
mkdir ../outputs/test_run_9/Markdown
bsub -o "../outputs/test_run_9/Markdown/test_run_9_0.md" -J "test_run_9_0" -P "-name test_run_9-0 -gamma 1.0 -network1 Networks.Small -learner1 Learners.DoubleQlearn -hours 0.3 -main simple" < submit.sh
