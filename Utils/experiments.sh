#!/bin/sh
mkdir ../outputs/Newcausal1_CFagent_convert1/
mkdir ../outputs/Newcausal1_CFagent_convert1/Markdown
bsub -o "../outputs/Newcausal1_CFagent_convert1/Markdown/Newcausal1_CFagent_convert1_0.md" -J "Newcausal1_CFagent_convert1_0" -P "-name Newcausal1_CFagent_convert1-0 -hours 3.0 -level Levels.Causal1 -main CFagent -CF_convert 0 -K1 500000.0 -K2 100000.0" < submit.sh
mkdir ../outputs/Newcausal1_CFagent_convert2/
mkdir ../outputs/Newcausal1_CFagent_convert2/Markdown
bsub -o "../outputs/Newcausal1_CFagent_convert2/Markdown/Newcausal1_CFagent_convert2_0.md" -J "Newcausal1_CFagent_convert2_0" -P "-name Newcausal1_CFagent_convert2-0 -hours 3.0 -level Levels.Causal1 -main CFagent -CF_convert 1 -K1 500000.0 -K2 100000.0" < submit.sh
mkdir ../outputs/Newcausal1_CFagent_convert3/
mkdir ../outputs/Newcausal1_CFagent_convert3/Markdown
bsub -o "../outputs/Newcausal1_CFagent_convert3/Markdown/Newcausal1_CFagent_convert3_0.md" -J "Newcausal1_CFagent_convert3_0" -P "-name Newcausal1_CFagent_convert3-0 -hours 3.0 -level Levels.Causal1 -main CFagent -CF_convert 2 -K1 500000.0 -K2 100000.0" < submit.sh
