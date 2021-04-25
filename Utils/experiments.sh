#!/bin/sh
mkdir ../outputs/MagicalLights2_convert3_TEST/
mkdir ../outputs/MagicalLights2_convert3_TEST/Markdown
bsub -o "../outputs/MagicalLights2_convert3_TEST/Markdown/MagicalLights2_convert3_TEST_0.md" -J "MagicalLights2_convert3_TEST_0" -P "-name MagicalLights2_convert3_TEST-0 -hours 24.0 -level Levels.Causal4 -main CFagent -CF_convert 3 -TopN 3" < submit.sh
bsub -o "../outputs/MagicalLights2_convert3_TEST/Markdown/MagicalLights2_convert3_TEST_1.md" -J "MagicalLights2_convert3_TEST_1" -P "-name MagicalLights2_convert3_TEST-1 -hours 24.0 -level Levels.Causal4 -main CFagent -CF_convert 3 -TopN 3" < submit.sh
mkdir ../outputs/MagicalLights2_convert4_TEST/
mkdir ../outputs/MagicalLights2_convert4_TEST/Markdown
bsub -o "../outputs/MagicalLights2_convert4_TEST/Markdown/MagicalLights2_convert4_TEST_0.md" -J "MagicalLights2_convert4_TEST_0" -P "-name MagicalLights2_convert4_TEST-0 -hours 24.0 -level Levels.Causal4 -main CFagent -CF_convert 4 -TopN 3" < submit.sh
bsub -o "../outputs/MagicalLights2_convert4_TEST/Markdown/MagicalLights2_convert4_TEST_1.md" -J "MagicalLights2_convert4_TEST_1" -P "-name MagicalLights2_convert4_TEST-1 -hours 24.0 -level Levels.Causal4 -main CFagent -CF_convert 4 -TopN 3" < submit.sh
mkdir ../outputs/Coconuts_convert3_TEST/
mkdir ../outputs/Coconuts_convert3_TEST/Markdown
bsub -o "../outputs/Coconuts_convert3_TEST/Markdown/Coconuts_convert3_TEST_0.md" -J "Coconuts_convert3_TEST_0" -P "-name Coconuts_convert3_TEST-0 -hours 24.0 -level Levels.Coconuts -main CFagent -CF_convert 3 -TopN 3" < submit.sh
mkdir ../outputs/Coconuts_convert4_TEST/
mkdir ../outputs/Coconuts_convert4_TEST/Markdown
bsub -o "../outputs/Coconuts_convert4_TEST/Markdown/Coconuts_convert4_TEST_0.md" -J "Coconuts_convert4_TEST_0" -P "-name Coconuts_convert4_TEST-0 -hours 24.0 -level Levels.Coconuts -main CFagent -CF_convert 4 -TopN 3" < submit.sh
