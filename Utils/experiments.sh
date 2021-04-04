#!/bin/sh
mkdir ../outputs/NOBUGcausal3_teleport/
mkdir ../outputs/NOBUGcausal3_teleport/Markdown
bsub -o "../outputs/NOBUGcausal3_teleport/Markdown/NOBUGcausal3_teleport_0.md" -J "NOBUGcausal3_teleport_0" -P "-name NOBUGcausal3_teleport-0 -hours 16.0 -level Levels.Causal3 -main teleport" < submit.sh
mkdir ../outputs/NOBUGcausal3_CFagent_convert0/
mkdir ../outputs/NOBUGcausal3_CFagent_convert0/Markdown
bsub -o "../outputs/NOBUGcausal3_CFagent_convert0/Markdown/NOBUGcausal3_CFagent_convert0_0.md" -J "NOBUGcausal3_CFagent_convert0_0" -P "-name NOBUGcausal3_CFagent_convert0-0 -hours 16.0 -level Levels.Causal3 -main CFagent -CF_convert 0" < submit.sh
mkdir ../outputs/NOBUGcausal3_CFagent_convert1/
mkdir ../outputs/NOBUGcausal3_CFagent_convert1/Markdown
bsub -o "../outputs/NOBUGcausal3_CFagent_convert1/Markdown/NOBUGcausal3_CFagent_convert1_0.md" -J "NOBUGcausal3_CFagent_convert1_0" -P "-name NOBUGcausal3_CFagent_convert1-0 -hours 16.0 -level Levels.Causal3 -main CFagent -CF_convert 1" < submit.sh
mkdir ../outputs/NOBUGcausal3_CFagent_convert2/
mkdir ../outputs/NOBUGcausal3_CFagent_convert2/Markdown
bsub -o "../outputs/NOBUGcausal3_CFagent_convert2/Markdown/NOBUGcausal3_CFagent_convert2_0.md" -J "NOBUGcausal3_CFagent_convert2_0" -P "-name NOBUGcausal3_CFagent_convert2-0 -hours 16.0 -level Levels.Causal3 -main CFagent -CF_convert 2" < submit.sh
mkdir ../outputs/NOBUGcausal4_teleport/
mkdir ../outputs/NOBUGcausal4_teleport/Markdown
bsub -o "../outputs/NOBUGcausal4_teleport/Markdown/NOBUGcausal4_teleport_0.md" -J "NOBUGcausal4_teleport_0" -P "-name NOBUGcausal4_teleport-0 -hours 16.0 -level Levels.Causal4 -main teleport" < submit.sh
mkdir ../outputs/NOBUGcausal4_CFagent_convert0/
mkdir ../outputs/NOBUGcausal4_CFagent_convert0/Markdown
bsub -o "../outputs/NOBUGcausal4_CFagent_convert0/Markdown/NOBUGcausal4_CFagent_convert0_0.md" -J "NOBUGcausal4_CFagent_convert0_0" -P "-name NOBUGcausal4_CFagent_convert0-0 -hours 16.0 -level Levels.Causal4 -main CFagent -CF_convert 0" < submit.sh
mkdir ../outputs/NOBUGcausal4_CFagent_convert1/
mkdir ../outputs/NOBUGcausal4_CFagent_convert1/Markdown
bsub -o "../outputs/NOBUGcausal4_CFagent_convert1/Markdown/NOBUGcausal4_CFagent_convert1_0.md" -J "NOBUGcausal4_CFagent_convert1_0" -P "-name NOBUGcausal4_CFagent_convert1-0 -hours 16.0 -level Levels.Causal4 -main CFagent -CF_convert 1" < submit.sh
mkdir ../outputs/NOBUGcausal4_CFagent_convert2/
mkdir ../outputs/NOBUGcausal4_CFagent_convert2/Markdown
bsub -o "../outputs/NOBUGcausal4_CFagent_convert2/Markdown/NOBUGcausal4_CFagent_convert2_0.md" -J "NOBUGcausal4_CFagent_convert2_0" -P "-name NOBUGcausal4_CFagent_convert2-0 -hours 16.0 -level Levels.Causal4 -main CFagent -CF_convert 2" < submit.sh
