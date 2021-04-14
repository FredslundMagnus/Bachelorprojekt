#!/bin/sh
mkdir ../outputs/ReTest13/
mkdir ../outputs/ReTest13/Markdown
bsub -o "../outputs/ReTest13/Markdown/ReTest13_0.md" -J "ReTest13_0" -P "-name ReTest13-0 -hours 24.0 -level Levels.Coconuts -main CFagent -CF_convert 3 -Counterfacts 1 -Random_counterfacts True" < submit.sh
mkdir ../outputs/ReTest14/
mkdir ../outputs/ReTest14/Markdown
bsub -o "../outputs/ReTest14/Markdown/ReTest14_0.md" -J "ReTest14_0" -P "-name ReTest14-0 -hours 24.0 -level Levels.Coconuts -main CFagent -CF_convert 3 -Counterfacts 2 -Random_counterfacts True" < submit.sh
mkdir ../outputs/ReTest15/
mkdir ../outputs/ReTest15/Markdown
bsub -o "../outputs/ReTest15/Markdown/ReTest15_0.md" -J "ReTest15_0" -P "-name ReTest15-0 -hours 24.0 -level Levels.Coconuts -main CFagent -CF_convert 3 -Counterfacts 3 -Random_counterfacts True" < submit.sh
mkdir ../outputs/ReTest16/
mkdir ../outputs/ReTest16/Markdown
bsub -o "../outputs/ReTest16/Markdown/ReTest16_0.md" -J "ReTest16_0" -P "-name ReTest16-0 -hours 24.0 -level Levels.Coconuts -main CFagent -CF_convert 4 -Counterfacts 1 -Random_counterfacts True" < submit.sh
mkdir ../outputs/ReTest17/
mkdir ../outputs/ReTest17/Markdown
bsub -o "../outputs/ReTest17/Markdown/ReTest17_0.md" -J "ReTest17_0" -P "-name ReTest17-0 -hours 24.0 -level Levels.Coconuts -main CFagent -CF_convert 4 -Counterfacts 2 -Random_counterfacts True" < submit.sh
mkdir ../outputs/ReTest18/
mkdir ../outputs/ReTest18/Markdown
bsub -o "../outputs/ReTest18/Markdown/ReTest18_0.md" -J "ReTest18_0" -P "-name ReTest18-0 -hours 24.0 -level Levels.Coconuts -main CFagent -CF_convert 4 -Counterfacts 3 -Random_counterfacts True" < submit.sh
