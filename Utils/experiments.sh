#!/bin/sh
mkdir ../outputs/Test_CPU_9/
mkdir ../outputs/Test_CPU_9/Markdown
bsub -o "../outputs/Test_CPU_9/Markdown/Test_CPU_9_0.md" -J "Test_CPU_9_0" -env MYARGS="-name Test_CPU_9-0 -level Levels.Causal3 -batch 25" < submit_cpu.sh
