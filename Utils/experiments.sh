#!/bin/sh
mkdir ../outputs/Causal3_Conver4/
mkdir ../outputs/Causal3_Conver4/Markdown
bsub -o "../outputs/Causal3_Conver4/Markdown/Causal3_Conver4_0.md" -J "Causal3_Conver4_0" -env MYARGS="-name Causal3_Conver4-0 -hours 24.0 -level Levels.Causal3 -main CFagent -CF_convert 4 -TopN 3" < submit_gpu.sh
bsub -o "../outputs/Causal3_Conver4/Markdown/Causal3_Conver4_1.md" -J "Causal3_Conver4_1" -env MYARGS="-name Causal3_Conver4-1 -hours 24.0 -level Levels.Causal3 -main CFagent -CF_convert 4 -TopN 3" < submit_gpu.sh
bsub -o "../outputs/Causal3_Conver4/Markdown/Causal3_Conver4_2.md" -J "Causal3_Conver4_2" -env MYARGS="-name Causal3_Conver4-2 -hours 24.0 -level Levels.Causal3 -main CFagent -CF_convert 4 -TopN 3" < submit_gpu.sh
