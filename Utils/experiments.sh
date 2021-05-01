#!/bin/sh
mkdir ../outputs/Test_CPU/
mkdir ../outputs/Test_CPU/Markdown
bsub -o "../outputs/Test_CPU/Markdown/Test_CPU_0.md" -J "Test_CPU_0" -env MYARGS="-name Test_CPU-0 -hours 0.1 -level Levels.Causal3 -main option_critic_run -batch 25" < submit_cpu.sh
