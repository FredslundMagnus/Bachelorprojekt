#!/bin/sh
mkdir ../outputs/Test_CPU_10/
mkdir ../outputs/Test_CPU_10/Markdown
bsub -o "../outputs/Test_CPU_10/Markdown/Test_CPU_10_0.md" -J "Test_CPU_10_0" -env MYARGS="-name Test_CPU_10-0 -hours 0.1 -level Levels.Causal3 -batch 25" < submit_cpu.sh
