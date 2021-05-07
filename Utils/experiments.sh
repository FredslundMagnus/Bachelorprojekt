#!/bin/sh
mkdir ../outputs/Maze_Conver4_3counterfacts/
mkdir ../outputs/Maze_Conver4_3counterfacts/Markdown
bsub -o "../outputs/Maze_Conver4_3counterfacts/Markdown/Maze_Conver4_3counterfacts_0.md" -J "Maze_Conver4_3counterfacts_0" -env MYARGS="-name Maze_Conver4_3counterfacts-0 -hours 24.0 -level Levels.Maze -main CFagent -CF_convert 4 -TopN 5 -Counterfacts 3 -num 0" < submit_gpu.sh
bsub -o "../outputs/Maze_Conver4_3counterfacts/Markdown/Maze_Conver4_3counterfacts_1.md" -J "Maze_Conver4_3counterfacts_1" -env MYARGS="-name Maze_Conver4_3counterfacts-1 -hours 24.0 -level Levels.Maze -main CFagent -CF_convert 4 -TopN 5 -Counterfacts 3 -num 1" < submit_gpu.sh
bsub -o "../outputs/Maze_Conver4_3counterfacts/Markdown/Maze_Conver4_3counterfacts_2.md" -J "Maze_Conver4_3counterfacts_2" -env MYARGS="-name Maze_Conver4_3counterfacts-2 -hours 24.0 -level Levels.Maze -main CFagent -CF_convert 4 -TopN 5 -Counterfacts 3 -num 2" < submit_gpu.sh
