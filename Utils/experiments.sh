#!/bin/sh
mkdir ../outputs/Test_CPU_6/
mkdir ../outputs/Test_CPU_6/Markdown
bsub -o "../outputs/Test_CPU_6/Markdown/Test_CPU_6_0.md" -J "Test_CPU_6_0" -env MYARGS="-name Test_CPU_6-0 -level Levels.Causal3 -main option_critic_run -batch 25" < submit_cpu.sh
