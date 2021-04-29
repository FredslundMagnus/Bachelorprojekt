#!/bin/sh
mkdir ../outputs/Causal3_Conver1/
mkdir ../outputs/Causal3_Conver1/Markdown
bsub -o "../outputs/Causal3_Conver1/Markdown/Causal3_Conver1_0.md" -J "Causal3_Conver1_0" -P "-name Causal3_Conver1-0 -hours 24.0 -level Levels.Causal3 -main CFagent -CF_convert 1 -TopN 3" < submit.sh
bsub -o "../outputs/Causal3_Conver1/Markdown/Causal3_Conver1_1.md" -J "Causal3_Conver1_1" -P "-name Causal3_Conver1-1 -hours 24.0 -level Levels.Causal3 -main CFagent -CF_convert 1 -TopN 3" < submit.sh
bsub -o "../outputs/Causal3_Conver1/Markdown/Causal3_Conver1_2.md" -J "Causal3_Conver1_2" -P "-name Causal3_Conver1-2 -hours 24.0 -level Levels.Causal3 -main CFagent -CF_convert 1 -TopN 3" < submit.sh
mkdir ../outputs/Causal3_Conver2/
mkdir ../outputs/Causal3_Conver2/Markdown
bsub -o "../outputs/Causal3_Conver2/Markdown/Causal3_Conver2_0.md" -J "Causal3_Conver2_0" -P "-name Causal3_Conver2-0 -hours 24.0 -level Levels.Causal3 -main CFagent -CF_convert 2 -TopN 3" < submit.sh
bsub -o "../outputs/Causal3_Conver2/Markdown/Causal3_Conver2_1.md" -J "Causal3_Conver2_1" -P "-name Causal3_Conver2-1 -hours 24.0 -level Levels.Causal3 -main CFagent -CF_convert 2 -TopN 3" < submit.sh
bsub -o "../outputs/Causal3_Conver2/Markdown/Causal3_Conver2_2.md" -J "Causal3_Conver2_2" -P "-name Causal3_Conver2-2 -hours 24.0 -level Levels.Causal3 -main CFagent -CF_convert 2 -TopN 3" < submit.sh
mkdir ../outputs/Causal4_Conver1/
mkdir ../outputs/Causal4_Conver1/Markdown
bsub -o "../outputs/Causal4_Conver1/Markdown/Causal4_Conver1_0.md" -J "Causal4_Conver1_0" -P "-name Causal4_Conver1-0 -hours 24.0 -level Levels.Causal4 -main CFagent -CF_convert 1 -TopN 3" < submit.sh
bsub -o "../outputs/Causal4_Conver1/Markdown/Causal4_Conver1_1.md" -J "Causal4_Conver1_1" -P "-name Causal4_Conver1-1 -hours 24.0 -level Levels.Causal4 -main CFagent -CF_convert 1 -TopN 3" < submit.sh
bsub -o "../outputs/Causal4_Conver1/Markdown/Causal4_Conver1_2.md" -J "Causal4_Conver1_2" -P "-name Causal4_Conver1-2 -hours 24.0 -level Levels.Causal4 -main CFagent -CF_convert 1 -TopN 3" < submit.sh
mkdir ../outputs/Causal4_Conver2/
mkdir ../outputs/Causal4_Conver2/Markdown
bsub -o "../outputs/Causal4_Conver2/Markdown/Causal4_Conver2_0.md" -J "Causal4_Conver2_0" -P "-name Causal4_Conver2-0 -hours 24.0 -level Levels.Causal4 -main CFagent -CF_convert 2 -TopN 3" < submit.sh
bsub -o "../outputs/Causal4_Conver2/Markdown/Causal4_Conver2_1.md" -J "Causal4_Conver2_1" -P "-name Causal4_Conver2-1 -hours 24.0 -level Levels.Causal4 -main CFagent -CF_convert 2 -TopN 3" < submit.sh
bsub -o "../outputs/Causal4_Conver2/Markdown/Causal4_Conver2_2.md" -J "Causal4_Conver2_2" -P "-name Causal4_Conver2-2 -hours 24.0 -level Levels.Causal4 -main CFagent -CF_convert 2 -TopN 3" < submit.sh
mkdir ../outputs/Coconuts_Conver1/
mkdir ../outputs/Coconuts_Conver1/Markdown
bsub -o "../outputs/Coconuts_Conver1/Markdown/Coconuts_Conver1_0.md" -J "Coconuts_Conver1_0" -P "-name Coconuts_Conver1-0 -hours 24.0 -level Levels.Coconuts -main CFagent -CF_convert 1 -TopN 3" < submit.sh
bsub -o "../outputs/Coconuts_Conver1/Markdown/Coconuts_Conver1_1.md" -J "Coconuts_Conver1_1" -P "-name Coconuts_Conver1-1 -hours 24.0 -level Levels.Coconuts -main CFagent -CF_convert 1 -TopN 3" < submit.sh
bsub -o "../outputs/Coconuts_Conver1/Markdown/Coconuts_Conver1_2.md" -J "Coconuts_Conver1_2" -P "-name Coconuts_Conver1-2 -hours 24.0 -level Levels.Coconuts -main CFagent -CF_convert 1 -TopN 3" < submit.sh
mkdir ../outputs/Coconuts_Conver2/
mkdir ../outputs/Coconuts_Conver2/Markdown
bsub -o "../outputs/Coconuts_Conver2/Markdown/Coconuts_Conver2_0.md" -J "Coconuts_Conver2_0" -P "-name Coconuts_Conver2-0 -hours 24.0 -level Levels.Coconuts -main CFagent -CF_convert 2 -TopN 3" < submit.sh
bsub -o "../outputs/Coconuts_Conver2/Markdown/Coconuts_Conver2_1.md" -J "Coconuts_Conver2_1" -P "-name Coconuts_Conver2-1 -hours 24.0 -level Levels.Coconuts -main CFagent -CF_convert 2 -TopN 3" < submit.sh
bsub -o "../outputs/Coconuts_Conver2/Markdown/Coconuts_Conver2_2.md" -J "Coconuts_Conver2_2" -P "-name Coconuts_Conver2-2 -hours 24.0 -level Levels.Coconuts -main CFagent -CF_convert 2 -TopN 3" < submit.sh
mkdir ../outputs/Maze_Conver1/
mkdir ../outputs/Maze_Conver1/Markdown
bsub -o "../outputs/Maze_Conver1/Markdown/Maze_Conver1_0.md" -J "Maze_Conver1_0" -P "-name Maze_Conver1-0 -hours 24.0 -level Levels.Maze -main CFagent -CF_convert 1 -TopN 3" < submit.sh
bsub -o "../outputs/Maze_Conver1/Markdown/Maze_Conver1_1.md" -J "Maze_Conver1_1" -P "-name Maze_Conver1-1 -hours 24.0 -level Levels.Maze -main CFagent -CF_convert 1 -TopN 3" < submit.sh
bsub -o "../outputs/Maze_Conver1/Markdown/Maze_Conver1_2.md" -J "Maze_Conver1_2" -P "-name Maze_Conver1-2 -hours 24.0 -level Levels.Maze -main CFagent -CF_convert 1 -TopN 3" < submit.sh
mkdir ../outputs/Maze_Conver2/
mkdir ../outputs/Maze_Conver2/Markdown
bsub -o "../outputs/Maze_Conver2/Markdown/Maze_Conver2_0.md" -J "Maze_Conver2_0" -P "-name Maze_Conver2-0 -hours 24.0 -level Levels.Maze -main CFagent -CF_convert 2 -TopN 3" < submit.sh
bsub -o "../outputs/Maze_Conver2/Markdown/Maze_Conver2_1.md" -J "Maze_Conver2_1" -P "-name Maze_Conver2-1 -hours 24.0 -level Levels.Maze -main CFagent -CF_convert 2 -TopN 3" < submit.sh
bsub -o "../outputs/Maze_Conver2/Markdown/Maze_Conver2_2.md" -J "Maze_Conver2_2" -P "-name Maze_Conver2-2 -hours 24.0 -level Levels.Maze -main CFagent -CF_convert 2 -TopN 3" < submit.sh
mkdir ../outputs/MonsterLevel_Conver1/
mkdir ../outputs/MonsterLevel_Conver1/Markdown
bsub -o "../outputs/MonsterLevel_Conver1/Markdown/MonsterLevel_Conver1_0.md" -J "MonsterLevel_Conver1_0" -P "-name MonsterLevel_Conver1-0 -hours 24.0 -level Levels.MonsterLevel -main CFagent -CF_convert 1 -TopN 3" < submit.sh
bsub -o "../outputs/MonsterLevel_Conver1/Markdown/MonsterLevel_Conver1_1.md" -J "MonsterLevel_Conver1_1" -P "-name MonsterLevel_Conver1-1 -hours 24.0 -level Levels.MonsterLevel -main CFagent -CF_convert 1 -TopN 3" < submit.sh
bsub -o "../outputs/MonsterLevel_Conver1/Markdown/MonsterLevel_Conver1_2.md" -J "MonsterLevel_Conver1_2" -P "-name MonsterLevel_Conver1-2 -hours 24.0 -level Levels.MonsterLevel -main CFagent -CF_convert 1 -TopN 3" < submit.sh
mkdir ../outputs/MonsterLevel_Conver2/
mkdir ../outputs/MonsterLevel_Conver2/Markdown
bsub -o "../outputs/MonsterLevel_Conver2/Markdown/MonsterLevel_Conver2_0.md" -J "MonsterLevel_Conver2_0" -P "-name MonsterLevel_Conver2-0 -hours 24.0 -level Levels.MonsterLevel -main CFagent -CF_convert 2 -TopN 3" < submit.sh
bsub -o "../outputs/MonsterLevel_Conver2/Markdown/MonsterLevel_Conver2_1.md" -J "MonsterLevel_Conver2_1" -P "-name MonsterLevel_Conver2-1 -hours 24.0 -level Levels.MonsterLevel -main CFagent -CF_convert 2 -TopN 3" < submit.sh
bsub -o "../outputs/MonsterLevel_Conver2/Markdown/MonsterLevel_Conver2_2.md" -J "MonsterLevel_Conver2_2" -P "-name MonsterLevel_Conver2-2 -hours 24.0 -level Levels.MonsterLevel -main CFagent -CF_convert 2 -TopN 3" < submit.sh
