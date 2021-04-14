#!/bin/sh
mkdir ../outputs/ReTest7/
mkdir ../outputs/ReTest7/Markdown
bsub -o "../outputs/ReTest7/Markdown/ReTest7_0.md" -J "ReTest7_0" -P "-name ReTest7-0 -hours 24.0 -level Levels.Causal4 -main CFagent -CF_convert 3 -Counterfacts 1 -Random_counterfacts True" < submit.sh
mkdir ../outputs/ReTest8/
mkdir ../outputs/ReTest8/Markdown
bsub -o "../outputs/ReTest8/Markdown/ReTest8_0.md" -J "ReTest8_0" -P "-name ReTest8-0 -hours 24.0 -level Levels.Causal4 -main CFagent -CF_convert 3 -Counterfacts 2 -Random_counterfacts True" < submit.sh
mkdir ../outputs/ReTest9/
mkdir ../outputs/ReTest9/Markdown
bsub -o "../outputs/ReTest9/Markdown/ReTest9_0.md" -J "ReTest9_0" -P "-name ReTest9-0 -hours 24.0 -level Levels.Causal4 -main CFagent -CF_convert 3 -Counterfacts 3 -Random_counterfacts True" < submit.sh
mkdir ../outputs/ReTest10/
mkdir ../outputs/ReTest10/Markdown
bsub -o "../outputs/ReTest10/Markdown/ReTest10_0.md" -J "ReTest10_0" -P "-name ReTest10-0 -hours 24.0 -level Levels.Causal4 -main CFagent -CF_convert 4 -Counterfacts 1 -Random_counterfacts True" < submit.sh
mkdir ../outputs/ReTest11/
mkdir ../outputs/ReTest11/Markdown
bsub -o "../outputs/ReTest11/Markdown/ReTest11_0.md" -J "ReTest11_0" -P "-name ReTest11-0 -hours 24.0 -level Levels.Causal4 -main CFagent -CF_convert 4 -Counterfacts 2 -Random_counterfacts True" < submit.sh
mkdir ../outputs/ReTest12/
mkdir ../outputs/ReTest12/Markdown
bsub -o "../outputs/ReTest12/Markdown/ReTest12_0.md" -J "ReTest12_0" -P "-name ReTest12-0 -hours 24.0 -level Levels.Causal4 -main CFagent -CF_convert 4 -Counterfacts 3 -Random_counterfacts True" < submit.sh
