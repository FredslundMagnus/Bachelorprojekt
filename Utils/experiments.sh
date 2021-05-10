#!/bin/sh
mkdir ../outputs/Maze_Conver4_3counterfactsNOCRASH/
mkdir ../outputs/Maze_Conver4_3counterfactsNOCRASH/Markdown
bsub -o "../outputs/Maze_Conver4_3counterfactsNOCRASH/Markdown/Maze_Conver4_3counterfactsNOCRASH_0.md" -J "Maze_Conver4_3counterfactsNOCRASH_0" -env MYARGS="-name Maze_Conver4_3counterfactsNOCRASH-0 -hours 24.0 -level Levels.Maze -main CFagent -CF_convert 4 -TopN 5 -Counterfacts 3 -num 0" < submit_gpu.sh
bsub -o "../outputs/Maze_Conver4_3counterfactsNOCRASH/Markdown/Maze_Conver4_3counterfactsNOCRASH_1.md" -J "Maze_Conver4_3counterfactsNOCRASH_1" -env MYARGS="-name Maze_Conver4_3counterfactsNOCRASH-1 -hours 24.0 -level Levels.Maze -main CFagent -CF_convert 4 -TopN 5 -Counterfacts 3 -num 1" < submit_gpu.sh
bsub -o "../outputs/Maze_Conver4_3counterfactsNOCRASH/Markdown/Maze_Conver4_3counterfactsNOCRASH_2.md" -J "Maze_Conver4_3counterfactsNOCRASH_2" -env MYARGS="-name Maze_Conver4_3counterfactsNOCRASH-2 -hours 24.0 -level Levels.Maze -main CFagent -CF_convert 4 -TopN 5 -Counterfacts 3 -num 2" < submit_gpu.sh
mkdir ../outputs/Coconuts_Conver4_3counterfactsNOCRASH/
mkdir ../outputs/Coconuts_Conver4_3counterfactsNOCRASH/Markdown
bsub -o "../outputs/Coconuts_Conver4_3counterfactsNOCRASH/Markdown/Coconuts_Conver4_3counterfactsNOCRASH_0.md" -J "Coconuts_Conver4_3counterfactsNOCRASH_0" -env MYARGS="-name Coconuts_Conver4_3counterfactsNOCRASH-0 -hours 24.0 -level Levels.Coconuts -main CFagent -CF_convert 4 -TopN 5 -Counterfacts 3 -num 0" < submit_gpu.sh
bsub -o "../outputs/Coconuts_Conver4_3counterfactsNOCRASH/Markdown/Coconuts_Conver4_3counterfactsNOCRASH_1.md" -J "Coconuts_Conver4_3counterfactsNOCRASH_1" -env MYARGS="-name Coconuts_Conver4_3counterfactsNOCRASH-1 -hours 24.0 -level Levels.Coconuts -main CFagent -CF_convert 4 -TopN 5 -Counterfacts 3 -num 1" < submit_gpu.sh
bsub -o "../outputs/Coconuts_Conver4_3counterfactsNOCRASH/Markdown/Coconuts_Conver4_3counterfactsNOCRASH_2.md" -J "Coconuts_Conver4_3counterfactsNOCRASH_2" -env MYARGS="-name Coconuts_Conver4_3counterfactsNOCRASH-2 -hours 24.0 -level Levels.Coconuts -main CFagent -CF_convert 4 -TopN 5 -Counterfacts 3 -num 2" < submit_gpu.sh
mkdir ../outputs/MonsterLevel_Conver4_3counterfactsNOCRASH/
mkdir ../outputs/MonsterLevel_Conver4_3counterfactsNOCRASH/Markdown
bsub -o "../outputs/MonsterLevel_Conver4_3counterfactsNOCRASH/Markdown/MonsterLevel_Conver4_3counterfactsNOCRASH_0.md" -J "MonsterLevel_Conver4_3counterfactsNOCRASH_0" -env MYARGS="-name MonsterLevel_Conver4_3counterfactsNOCRASH-0 -hours 24.0 -level Levels.MonsterLevel -main CFagent -CF_convert 4 -TopN 5 -Counterfacts 3 -num 0" < submit_gpu.sh
bsub -o "../outputs/MonsterLevel_Conver4_3counterfactsNOCRASH/Markdown/MonsterLevel_Conver4_3counterfactsNOCRASH_1.md" -J "MonsterLevel_Conver4_3counterfactsNOCRASH_1" -env MYARGS="-name MonsterLevel_Conver4_3counterfactsNOCRASH-1 -hours 24.0 -level Levels.MonsterLevel -main CFagent -CF_convert 4 -TopN 5 -Counterfacts 3 -num 1" < submit_gpu.sh
bsub -o "../outputs/MonsterLevel_Conver4_3counterfactsNOCRASH/Markdown/MonsterLevel_Conver4_3counterfactsNOCRASH_2.md" -J "MonsterLevel_Conver4_3counterfactsNOCRASH_2" -env MYARGS="-name MonsterLevel_Conver4_3counterfactsNOCRASH-2 -hours 24.0 -level Levels.MonsterLevel -main CFagent -CF_convert 4 -TopN 5 -Counterfacts 3 -num 2" < submit_gpu.sh
mkdir ../outputs/Causal3_Conver4_3counterfactsNOCRASH/
mkdir ../outputs/Causal3_Conver4_3counterfactsNOCRASH/Markdown
bsub -o "../outputs/Causal3_Conver4_3counterfactsNOCRASH/Markdown/Causal3_Conver4_3counterfactsNOCRASH_0.md" -J "Causal3_Conver4_3counterfactsNOCRASH_0" -env MYARGS="-name Causal3_Conver4_3counterfactsNOCRASH-0 -hours 24.0 -level Levels.Causal3 -main CFagent -CF_convert 4 -TopN 5 -Counterfacts 3 -num 0" < submit_gpu.sh
bsub -o "../outputs/Causal3_Conver4_3counterfactsNOCRASH/Markdown/Causal3_Conver4_3counterfactsNOCRASH_1.md" -J "Causal3_Conver4_3counterfactsNOCRASH_1" -env MYARGS="-name Causal3_Conver4_3counterfactsNOCRASH-1 -hours 24.0 -level Levels.Causal3 -main CFagent -CF_convert 4 -TopN 5 -Counterfacts 3 -num 1" < submit_gpu.sh
bsub -o "../outputs/Causal3_Conver4_3counterfactsNOCRASH/Markdown/Causal3_Conver4_3counterfactsNOCRASH_2.md" -J "Causal3_Conver4_3counterfactsNOCRASH_2" -env MYARGS="-name Causal3_Conver4_3counterfactsNOCRASH-2 -hours 24.0 -level Levels.Causal3 -main CFagent -CF_convert 4 -TopN 5 -Counterfacts 3 -num 2" < submit_gpu.sh
