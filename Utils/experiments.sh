#!/bin/sh
mkdir ../outputs/Causal4_Conver3/
mkdir ../outputs/Causal4_Conver3/Markdown
bsub -o "../outputs/Causal4_Conver3/Markdown/Causal4_Conver3_0.md" -J "Causal4_Conver3_0" -env MYARGS="-name Causal4_Conver3-0 -hours 24.0 -level Levels.Causal4 -main CFagent -CF_convert 3 -TopN 3" < submit_gpu.sh
bsub -o "../outputs/Causal4_Conver3/Markdown/Causal4_Conver3_1.md" -J "Causal4_Conver3_1" -env MYARGS="-name Causal4_Conver3-1 -hours 24.0 -level Levels.Causal4 -main CFagent -CF_convert 3 -TopN 3" < submit_gpu.sh
bsub -o "../outputs/Causal4_Conver3/Markdown/Causal4_Conver3_2.md" -J "Causal4_Conver3_2" -env MYARGS="-name Causal4_Conver3-2 -hours 24.0 -level Levels.Causal4 -main CFagent -CF_convert 3 -TopN 3" < submit_gpu.sh
mkdir ../outputs/Causal4_Conver4/
mkdir ../outputs/Causal4_Conver4/Markdown
bsub -o "../outputs/Causal4_Conver4/Markdown/Causal4_Conver4_0.md" -J "Causal4_Conver4_0" -env MYARGS="-name Causal4_Conver4-0 -hours 24.0 -level Levels.Causal4 -main CFagent -CF_convert 4 -TopN 3" < submit_gpu.sh
bsub -o "../outputs/Causal4_Conver4/Markdown/Causal4_Conver4_1.md" -J "Causal4_Conver4_1" -env MYARGS="-name Causal4_Conver4-1 -hours 24.0 -level Levels.Causal4 -main CFagent -CF_convert 4 -TopN 3" < submit_gpu.sh
bsub -o "../outputs/Causal4_Conver4/Markdown/Causal4_Conver4_2.md" -J "Causal4_Conver4_2" -env MYARGS="-name Causal4_Conver4-2 -hours 24.0 -level Levels.Causal4 -main CFagent -CF_convert 4 -TopN 3" < submit_gpu.sh
