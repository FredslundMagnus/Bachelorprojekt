#!/bin/sh
mkdir ../outputs/Test_CPU_8/
mkdir ../outputs/Test_CPU_8/Markdown
bsub -o "../outputs/Test_CPU_8/Markdown/Test_CPU_8_0.md" -J "Test_CPU_8_0" -env MYARGS="-name Test_CPU_8-0 -level Levels.Causal3 -batch 25" < submit_cpu.sh
