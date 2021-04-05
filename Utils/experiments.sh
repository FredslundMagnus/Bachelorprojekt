#!/bin/sh
mkdir ../outputs/causal4_CF_convert0_2/
mkdir ../outputs/causal4_CF_convert0_2/Markdown
bsub -o "../outputs/causal4_CF_convert0_2/Markdown/causal4_CF_convert0_2_0.md" -J "causal4_CF_convert0_2_0" -P "-name causal4_CF_convert0_2-0 -hours 24.0 -level Levels.Causal4 -main CFagent -CF_convert 0" < submit.sh
mkdir ../outputs/causal4_CF_convert1_2/
mkdir ../outputs/causal4_CF_convert1_2/Markdown
bsub -o "../outputs/causal4_CF_convert1_2/Markdown/causal4_CF_convert1_2_0.md" -J "causal4_CF_convert1_2_0" -P "-name causal4_CF_convert1_2-0 -hours 24.0 -level Levels.Causal4 -main CFagent -CF_convert 1" < submit.sh
mkdir ../outputs/causal4_CF_convert2_2/
mkdir ../outputs/causal4_CF_convert2_2/Markdown
bsub -o "../outputs/causal4_CF_convert2_2/Markdown/causal4_CF_convert2_2_0.md" -J "causal4_CF_convert2_2_0" -P "-name causal4_CF_convert2_2-0 -hours 24.0 -level Levels.Causal4 -main CFagent -CF_convert 2" < submit.sh
mkdir ../outputs/causal4_CF_convert3_2/
mkdir ../outputs/causal4_CF_convert3_2/Markdown
bsub -o "../outputs/causal4_CF_convert3_2/Markdown/causal4_CF_convert3_2_0.md" -J "causal4_CF_convert3_2_0" -P "-name causal4_CF_convert3_2-0 -hours 24.0 -level Levels.Causal4 -main CFagent -CF_convert 3" < submit.sh
mkdir ../outputs/causal4_CF_convert4_2/
mkdir ../outputs/causal4_CF_convert4_2/Markdown
bsub -o "../outputs/causal4_CF_convert4_2/Markdown/causal4_CF_convert4_2_0.md" -J "causal4_CF_convert4_2_0" -P "-name causal4_CF_convert4_2-0 -hours 24.0 -level Levels.Causal4 -main CFagent -CF_convert 4" < submit.sh
mkdir ../outputs/causal4_CF_convert5_2/
mkdir ../outputs/causal4_CF_convert5_2/Markdown
bsub -o "../outputs/causal4_CF_convert5_2/Markdown/causal4_CF_convert5_2_0.md" -J "causal4_CF_convert5_2_0" -P "-name causal4_CF_convert5_2-0 -hours 24.0 -level Levels.Causal4 -main CFagent -CF_convert 5" < submit.sh
