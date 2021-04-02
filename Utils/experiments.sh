#!/bin/sh
mkdir ../outputs/causal1_CFagent_convert1/
mkdir ../outputs/causal1_CFagent_convert1/Markdown
bsub -o "../outputs/causal1_CFagent_convert1/Markdown/causal1_CFagent_convert1_0.md" -J "causal1_CFagent_convert1_0" -P "-name causal1_CFagent_convert1-0 -hours 13.0 -level Levels.Causal1 -main CFagent -CF_convert 0" < submit.sh
mkdir ../outputs/causal1_CFagent_convert2/
mkdir ../outputs/causal1_CFagent_convert2/Markdown
bsub -o "../outputs/causal1_CFagent_convert2/Markdown/causal1_CFagent_convert2_0.md" -J "causal1_CFagent_convert2_0" -P "-name causal1_CFagent_convert2-0 -hours 13.0 -level Levels.Causal1 -main CFagent -CF_convert 1" < submit.sh
mkdir ../outputs/causal1_CFagent_convert3/
mkdir ../outputs/causal1_CFagent_convert3/Markdown
bsub -o "../outputs/causal1_CFagent_convert3/Markdown/causal1_CFagent_convert3_0.md" -J "causal1_CFagent_convert3_0" -P "-name causal1_CFagent_convert3-0 -hours 13.0 -level Levels.Causal1 -main CFagent -CF_convert 2" < submit.sh
mkdir ../outputs/causal2_CFagent_convert1/
mkdir ../outputs/causal2_CFagent_convert1/Markdown
bsub -o "../outputs/causal2_CFagent_convert1/Markdown/causal2_CFagent_convert1_0.md" -J "causal2_CFagent_convert1_0" -P "-name causal2_CFagent_convert1-0 -hours 13.0 -level Levels.Causal2 -main CFagent -CF_convert 0" < submit.sh
mkdir ../outputs/causal2_CFagent_convert2/
mkdir ../outputs/causal2_CFagent_convert2/Markdown
bsub -o "../outputs/causal2_CFagent_convert2/Markdown/causal2_CFagent_convert2_0.md" -J "causal2_CFagent_convert2_0" -P "-name causal2_CFagent_convert2-0 -hours 13.0 -level Levels.Causal2 -main CFagent -CF_convert 1" < submit.sh
mkdir ../outputs/causal2_CFagent_convert3/
mkdir ../outputs/causal2_CFagent_convert3/Markdown
bsub -o "../outputs/causal2_CFagent_convert3/Markdown/causal2_CFagent_convert3_0.md" -J "causal2_CFagent_convert3_0" -P "-name causal2_CFagent_convert3-0 -hours 13.0 -level Levels.Causal2 -main CFagent -CF_convert 2" < submit.sh
mkdir ../outputs/causal3_CFagent_convert1/
mkdir ../outputs/causal3_CFagent_convert1/Markdown
bsub -o "../outputs/causal3_CFagent_convert1/Markdown/causal3_CFagent_convert1_0.md" -J "causal3_CFagent_convert1_0" -P "-name causal3_CFagent_convert1-0 -hours 13.0 -level Levels.Causal3 -main CFagent -CF_convert 0" < submit.sh
mkdir ../outputs/causal3_CFagent_convert2/
mkdir ../outputs/causal3_CFagent_convert2/Markdown
bsub -o "../outputs/causal3_CFagent_convert2/Markdown/causal3_CFagent_convert2_0.md" -J "causal3_CFagent_convert2_0" -P "-name causal3_CFagent_convert2-0 -hours 13.0 -level Levels.Causal3 -main CFagent -CF_convert 1" < submit.sh
mkdir ../outputs/causal3_CFagent_convert3/
mkdir ../outputs/causal3_CFagent_convert3/Markdown
bsub -o "../outputs/causal3_CFagent_convert3/Markdown/causal3_CFagent_convert3_0.md" -J "causal3_CFagent_convert3_0" -P "-name causal3_CFagent_convert3-0 -hours 13.0 -level Levels.Causal3 -main CFagent -CF_convert 2" < submit.sh
