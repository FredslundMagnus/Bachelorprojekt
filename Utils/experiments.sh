#!/bin/sh
mkdir ../outputs/Test_CPU_7/
mkdir ../outputs/Test_CPU_7/Markdown
bsub -o "../outputs/Test_CPU_7/Markdown/Test_CPU_7_0.md" -J "Test_CPU_7_0" -env MYARGS="-name Test_CPU_7-0 -level Levels.Causal3 -main option_critic_run -batch 25" < submit_cpu.sh
