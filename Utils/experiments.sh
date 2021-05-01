#!/bin/sh
mkdir ../outputs/Test_CPU_2/
mkdir ../outputs/Test_CPU_2/Markdown
bsub -o "../outputs/Test_CPU_2/Markdown/Test_CPU_2_0.md" -J "Test_CPU_2_0" -env MYARGS="-name Test_CPU_2-0 -hours 0.1 -level Levels.Causal3 -main option_critic_run -batch 25" < submit_cpu.sh
