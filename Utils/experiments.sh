#!/bin/sh
mkdir ../outputs/MagicalLights2_convert3/
mkdir ../outputs/MagicalLights2_convert3/Markdown
bsub -o "../outputs/MagicalLights2_convert3/Markdown/MagicalLights2_convert3_0.md" -J "MagicalLights2_convert3_0" -P "-name MagicalLights2_convert3-0 -hours 24.0 -level Levels.Causal4 -main CFagent -CF_convert 3 -TopN 1" < submit.sh
bsub -o "../outputs/MagicalLights2_convert3/Markdown/MagicalLights2_convert3_1.md" -J "MagicalLights2_convert3_1" -P "-name MagicalLights2_convert3-1 -hours 24.0 -level Levels.Causal4 -main CFagent -CF_convert 3 -TopN 1" < submit.sh
bsub -o "../outputs/MagicalLights2_convert3/Markdown/MagicalLights2_convert3_2.md" -J "MagicalLights2_convert3_2" -P "-name MagicalLights2_convert3-2 -hours 24.0 -level Levels.Causal4 -main CFagent -CF_convert 3 -TopN 1" < submit.sh
mkdir ../outputs/MagicalLights2_convert4/
mkdir ../outputs/MagicalLights2_convert4/Markdown
bsub -o "../outputs/MagicalLights2_convert4/Markdown/MagicalLights2_convert4_0.md" -J "MagicalLights2_convert4_0" -P "-name MagicalLights2_convert4-0 -hours 24.0 -level Levels.Causal4 -main CFagent -CF_convert 4 -TopN 1" < submit.sh
bsub -o "../outputs/MagicalLights2_convert4/Markdown/MagicalLights2_convert4_1.md" -J "MagicalLights2_convert4_1" -P "-name MagicalLights2_convert4-1 -hours 24.0 -level Levels.Causal4 -main CFagent -CF_convert 4 -TopN 1" < submit.sh
bsub -o "../outputs/MagicalLights2_convert4/Markdown/MagicalLights2_convert4_2.md" -J "MagicalLights2_convert4_2" -P "-name MagicalLights2_convert4-2 -hours 24.0 -level Levels.Causal4 -main CFagent -CF_convert 4 -TopN 1" < submit.sh
