#!/bin/sh
mkdir ../outputs/CFv2cau1/
mkdir ../outputs/CFv2cau1/Markdown
bsub -o "../outputs/CFv2cau1/Markdown/CFv2cau1_0.md" -J "CFv2cau1_0" -P "-name CFv2cau1-0 -hours 10.0 -level Levels.Causal1 -main CFagentv2 -CF_convert 6 -Counterfacts 1" < submit.sh
bsub -o "../outputs/CFv2cau1/Markdown/CFv2cau1_1.md" -J "CFv2cau1_1" -P "-name CFv2cau1-1 -hours 10.0 -level Levels.Causal1 -main CFagentv2 -CF_convert 6 -Counterfacts 1" < submit.sh
mkdir ../outputs/CFv2cau2/
mkdir ../outputs/CFv2cau2/Markdown
bsub -o "../outputs/CFv2cau2/Markdown/CFv2cau2_0.md" -J "CFv2cau2_0" -P "-name CFv2cau2-0 -hours 10.0 -level Levels.Causal2 -main CFagentv2 -CF_convert 6 -Counterfacts 1" < submit.sh
bsub -o "../outputs/CFv2cau2/Markdown/CFv2cau2_1.md" -J "CFv2cau2_1" -P "-name CFv2cau2-1 -hours 10.0 -level Levels.Causal2 -main CFagentv2 -CF_convert 6 -Counterfacts 1" < submit.sh
