#!/bin/sh
mkdir ../outputs/Diamonds2_convert1/
mkdir ../outputs/Diamonds2_convert1/Markdown
bsub -o "../outputs/Diamonds2_convert1/Markdown/Diamonds2_convert1_0.md" -J "Diamonds2_convert1_0" -env MYARGS="-name Diamonds2_convert1-0 -hours 24.0 -level Levels.Causal5 -main CFagent -CF_convert 1 -TopN 2 -K1 2000000.0 -num 0" < submit_gpu.sh
bsub -o "../outputs/Diamonds2_convert1/Markdown/Diamonds2_convert1_1.md" -J "Diamonds2_convert1_1" -env MYARGS="-name Diamonds2_convert1-1 -hours 24.0 -level Levels.Causal5 -main CFagent -CF_convert 1 -TopN 2 -K1 2000000.0 -num 1" < submit_gpu.sh
bsub -o "../outputs/Diamonds2_convert1/Markdown/Diamonds2_convert1_2.md" -J "Diamonds2_convert1_2" -env MYARGS="-name Diamonds2_convert1-2 -hours 24.0 -level Levels.Causal5 -main CFagent -CF_convert 1 -TopN 2 -K1 2000000.0 -num 2" < submit_gpu.sh
mkdir ../outputs/Diamonds2_convert2/
mkdir ../outputs/Diamonds2_convert2/Markdown
bsub -o "../outputs/Diamonds2_convert2/Markdown/Diamonds2_convert2_0.md" -J "Diamonds2_convert2_0" -env MYARGS="-name Diamonds2_convert2-0 -hours 24.0 -level Levels.Causal5 -main CFagent -CF_convert 2 -TopN 2 -K1 2000000.0 -num 0" < submit_gpu.sh
bsub -o "../outputs/Diamonds2_convert2/Markdown/Diamonds2_convert2_1.md" -J "Diamonds2_convert2_1" -env MYARGS="-name Diamonds2_convert2-1 -hours 24.0 -level Levels.Causal5 -main CFagent -CF_convert 2 -TopN 2 -K1 2000000.0 -num 1" < submit_gpu.sh
bsub -o "../outputs/Diamonds2_convert2/Markdown/Diamonds2_convert2_2.md" -J "Diamonds2_convert2_2" -env MYARGS="-name Diamonds2_convert2-2 -hours 24.0 -level Levels.Causal5 -main CFagent -CF_convert 2 -TopN 2 -K1 2000000.0 -num 2" < submit_gpu.sh
mkdir ../outputs/Diamonds2_convert4/
mkdir ../outputs/Diamonds2_convert4/Markdown
bsub -o "../outputs/Diamonds2_convert4/Markdown/Diamonds2_convert4_0.md" -J "Diamonds2_convert4_0" -env MYARGS="-name Diamonds2_convert4-0 -hours 24.0 -level Levels.Causal5 -main CFagent -CF_convert 4 -TopN 2 -K1 2000000.0 -num 0" < submit_gpu.sh
bsub -o "../outputs/Diamonds2_convert4/Markdown/Diamonds2_convert4_1.md" -J "Diamonds2_convert4_1" -env MYARGS="-name Diamonds2_convert4-1 -hours 24.0 -level Levels.Causal5 -main CFagent -CF_convert 4 -TopN 2 -K1 2000000.0 -num 1" < submit_gpu.sh
bsub -o "../outputs/Diamonds2_convert4/Markdown/Diamonds2_convert4_2.md" -J "Diamonds2_convert4_2" -env MYARGS="-name Diamonds2_convert4-2 -hours 24.0 -level Levels.Causal5 -main CFagent -CF_convert 4 -TopN 2 -K1 2000000.0 -num 2" < submit_gpu.sh
