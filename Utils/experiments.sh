#!/bin/sh
mkdir ../outputs/SuperCausal_tele/
mkdir ../outputs/SuperCausal_tele/Markdown
bsub -o "../outputs/SuperCausal_tele/Markdown/SuperCausal_tele_0.md" -J "SuperCausal_tele_0" -env MYARGS="-name SuperCausal_tele-0 -hours 24.0 -level Levels.CausalSuper -main teleport -num 0" < submit_gpu.sh
bsub -o "../outputs/SuperCausal_tele/Markdown/SuperCausal_tele_1.md" -J "SuperCausal_tele_1" -env MYARGS="-name SuperCausal_tele-1 -hours 24.0 -level Levels.CausalSuper -main teleport -num 1" < submit_gpu.sh
bsub -o "../outputs/SuperCausal_tele/Markdown/SuperCausal_tele_2.md" -J "SuperCausal_tele_2" -env MYARGS="-name SuperCausal_tele-2 -hours 24.0 -level Levels.CausalSuper -main teleport -num 2" < submit_gpu.sh
mkdir ../outputs/SuperCausal_convert4/
mkdir ../outputs/SuperCausal_convert4/Markdown
bsub -o "../outputs/SuperCausal_convert4/Markdown/SuperCausal_convert4_0.md" -J "SuperCausal_convert4_0" -env MYARGS="-name SuperCausal_convert4-0 -hours 24.0 -level Levels.CausalSuper -main CFagent -CF_convert 4 -TopN 3 -Counterfacts 2 -num 0" < submit_gpu.sh
bsub -o "../outputs/SuperCausal_convert4/Markdown/SuperCausal_convert4_1.md" -J "SuperCausal_convert4_1" -env MYARGS="-name SuperCausal_convert4-1 -hours 24.0 -level Levels.CausalSuper -main CFagent -CF_convert 4 -TopN 3 -Counterfacts 2 -num 1" < submit_gpu.sh
bsub -o "../outputs/SuperCausal_convert4/Markdown/SuperCausal_convert4_2.md" -J "SuperCausal_convert4_2" -env MYARGS="-name SuperCausal_convert4-2 -hours 24.0 -level Levels.CausalSuper -main CFagent -CF_convert 4 -TopN 3 -Counterfacts 2 -num 2" < submit_gpu.sh
