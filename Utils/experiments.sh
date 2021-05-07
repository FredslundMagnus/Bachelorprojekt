#!/bin/sh
mkdir ../outputs/Causal4_Conver4_3counterfacts_2/
mkdir ../outputs/Causal4_Conver4_3counterfacts_2/Markdown
bsub -o "../outputs/Causal4_Conver4_3counterfacts_2/Markdown/Causal4_Conver4_3counterfacts_2_0.md" -J "Causal4_Conver4_3counterfacts_2_0" -env MYARGS="-name Causal4_Conver4_3counterfacts_2-0 -hours 11.0 -level Levels.Causal4 -main Load_Cfagent -CF_convert 4 -TopN 5 -Counterfacts 3 -num 0" < submit_gpu.sh
bsub -o "../outputs/Causal4_Conver4_3counterfacts_2/Markdown/Causal4_Conver4_3counterfacts_2_1.md" -J "Causal4_Conver4_3counterfacts_2_1" -env MYARGS="-name Causal4_Conver4_3counterfacts_2-1 -hours 11.0 -level Levels.Causal4 -main Load_Cfagent -CF_convert 4 -TopN 5 -Counterfacts 3 -num 1" < submit_gpu.sh
bsub -o "../outputs/Causal4_Conver4_3counterfacts_2/Markdown/Causal4_Conver4_3counterfacts_2_2.md" -J "Causal4_Conver4_3counterfacts_2_2" -env MYARGS="-name Causal4_Conver4_3counterfacts_2-2 -hours 11.0 -level Levels.Causal4 -main Load_Cfagent -CF_convert 4 -TopN 5 -Counterfacts 3 -num 2" < submit_gpu.sh
