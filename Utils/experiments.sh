#!/bin/sh
mkdir ../outputs/Causal4_Conver4_3counterfacts/
mkdir ../outputs/Causal4_Conver4_3counterfacts/Markdown
bsub -o "../outputs/Causal4_Conver4_3counterfacts/Markdown/Causal4_Conver4_3counterfacts_0.md" -J "Causal4_Conver4_3counterfacts_0" -env MYARGS="-name Causal4_Conver4_3counterfacts-0 -hours 24.0 -level Levels.Causal4 -main CFagent -CF_convert 4 -TopN 5 -Counterfacts 3" < submit_gpu.sh
bsub -o "../outputs/Causal4_Conver4_3counterfacts/Markdown/Causal4_Conver4_3counterfacts_1.md" -J "Causal4_Conver4_3counterfacts_1" -env MYARGS="-name Causal4_Conver4_3counterfacts-1 -hours 24.0 -level Levels.Causal4 -main CFagent -CF_convert 4 -TopN 5 -Counterfacts 3" < submit_gpu.sh
bsub -o "../outputs/Causal4_Conver4_3counterfacts/Markdown/Causal4_Conver4_3counterfacts_2.md" -J "Causal4_Conver4_3counterfacts_2" -env MYARGS="-name Causal4_Conver4_3counterfacts-2 -hours 24.0 -level Levels.Causal4 -main CFagent -CF_convert 4 -TopN 5 -Counterfacts 3" < submit_gpu.sh
