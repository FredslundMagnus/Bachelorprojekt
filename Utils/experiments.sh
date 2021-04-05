#!/bin/sh
mkdir ../outputs/causal4_CF_convert0/
mkdir ../outputs/causal4_CF_convert0/Markdown
bsub -o "../outputs/causal4_CF_convert0/Markdown/causal4_CF_convert0_0.md" -J "causal4_CF_convert0_0" -P "-name causal4_CF_convert0-0 -hours 16.0 -level Levels.Causal4 -main CFagent -CF_convert 0" < submit.sh
mkdir ../outputs/causal4_CF_convert1/
mkdir ../outputs/causal4_CF_convert1/Markdown
bsub -o "../outputs/causal4_CF_convert1/Markdown/causal4_CF_convert1_0.md" -J "causal4_CF_convert1_0" -P "-name causal4_CF_convert1-0 -hours 16.0 -level Levels.Causal4 -main CFagent -CF_convert 1" < submit.sh
mkdir ../outputs/causal4_CF_convert2/
mkdir ../outputs/causal4_CF_convert2/Markdown
bsub -o "../outputs/causal4_CF_convert2/Markdown/causal4_CF_convert2_0.md" -J "causal4_CF_convert2_0" -P "-name causal4_CF_convert2-0 -hours 16.0 -level Levels.Causal4 -main CFagent -CF_convert 2" < submit.sh
mkdir ../outputs/causal4_CF_convert3/
mkdir ../outputs/causal4_CF_convert3/Markdown
bsub -o "../outputs/causal4_CF_convert3/Markdown/causal4_CF_convert3_0.md" -J "causal4_CF_convert3_0" -P "-name causal4_CF_convert3-0 -hours 16.0 -level Levels.Causal4 -main CFagent -CF_convert 3" < submit.sh
mkdir ../outputs/causal4_CF_convert4/
mkdir ../outputs/causal4_CF_convert4/Markdown
bsub -o "../outputs/causal4_CF_convert4/Markdown/causal4_CF_convert4_0.md" -J "causal4_CF_convert4_0" -P "-name causal4_CF_convert4-0 -hours 16.0 -level Levels.Causal4 -main CFagent -CF_convert 4" < submit.sh
mkdir ../outputs/causal4_teleport/
mkdir ../outputs/causal4_teleport/Markdown
bsub -o "../outputs/causal4_teleport/Markdown/causal4_teleport_0.md" -J "causal4_teleport_0" -P "-name causal4_teleport-0 -hours 16.0 -level Levels.Causal4 -main teleport" < submit.sh
