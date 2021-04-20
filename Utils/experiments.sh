#!/bin/sh
mkdir ../outputs/Lights1_teleport/
mkdir ../outputs/Lights1_teleport/Markdown
bsub -o "../outputs/Lights1_teleport/Markdown/Lights1_teleport_0.md" -J "Lights1_teleport_0" -P "-name Lights1_teleport-0 -hours 24.0 -level Levels.Causal3 -main teleport" < submit.sh
bsub -o "../outputs/Lights1_teleport/Markdown/Lights1_teleport_1.md" -J "Lights1_teleport_1" -P "-name Lights1_teleport-1 -hours 24.0 -level Levels.Causal3 -main teleport" < submit.sh
bsub -o "../outputs/Lights1_teleport/Markdown/Lights1_teleport_2.md" -J "Lights1_teleport_2" -P "-name Lights1_teleport-2 -hours 24.0 -level Levels.Causal3 -main teleport" < submit.sh
mkdir ../outputs/Lights2_teleport/
mkdir ../outputs/Lights2_teleport/Markdown
bsub -o "../outputs/Lights2_teleport/Markdown/Lights2_teleport_0.md" -J "Lights2_teleport_0" -P "-name Lights2_teleport-0 -hours 24.0 -level Levels.Causal4 -main teleport" < submit.sh
bsub -o "../outputs/Lights2_teleport/Markdown/Lights2_teleport_1.md" -J "Lights2_teleport_1" -P "-name Lights2_teleport-1 -hours 24.0 -level Levels.Causal4 -main teleport" < submit.sh
bsub -o "../outputs/Lights2_teleport/Markdown/Lights2_teleport_2.md" -J "Lights2_teleport_2" -P "-name Lights2_teleport-2 -hours 24.0 -level Levels.Causal4 -main teleport" < submit.sh
mkdir ../outputs/Diamonds1_teleport/
mkdir ../outputs/Diamonds1_teleport/Markdown
bsub -o "../outputs/Diamonds1_teleport/Markdown/Diamonds1_teleport_0.md" -J "Diamonds1_teleport_0" -P "-name Diamonds1_teleport-0 -hours 24.0 -level Levels.Causal2 -main teleport" < submit.sh
bsub -o "../outputs/Diamonds1_teleport/Markdown/Diamonds1_teleport_1.md" -J "Diamonds1_teleport_1" -P "-name Diamonds1_teleport-1 -hours 24.0 -level Levels.Causal2 -main teleport" < submit.sh
bsub -o "../outputs/Diamonds1_teleport/Markdown/Diamonds1_teleport_2.md" -J "Diamonds1_teleport_2" -P "-name Diamonds1_teleport-2 -hours 24.0 -level Levels.Causal2 -main teleport" < submit.sh
mkdir ../outputs/Diamonds2_teleport/
mkdir ../outputs/Diamonds2_teleport/Markdown
bsub -o "../outputs/Diamonds2_teleport/Markdown/Diamonds2_teleport_0.md" -J "Diamonds2_teleport_0" -P "-name Diamonds2_teleport-0 -hours 24.0 -level Levels.Causal5 -main teleport" < submit.sh
bsub -o "../outputs/Diamonds2_teleport/Markdown/Diamonds2_teleport_1.md" -J "Diamonds2_teleport_1" -P "-name Diamonds2_teleport-1 -hours 24.0 -level Levels.Causal5 -main teleport" < submit.sh
bsub -o "../outputs/Diamonds2_teleport/Markdown/Diamonds2_teleport_2.md" -J "Diamonds2_teleport_2" -P "-name Diamonds2_teleport-2 -hours 24.0 -level Levels.Causal5 -main teleport" < submit.sh
mkdir ../outputs/Diamonds3_teleport/
mkdir ../outputs/Diamonds3_teleport/Markdown
bsub -o "../outputs/Diamonds3_teleport/Markdown/Diamonds3_teleport_0.md" -J "Diamonds3_teleport_0" -P "-name Diamonds3_teleport-0 -hours 24.0 -level Levels.Causal6 -main teleport" < submit.sh
bsub -o "../outputs/Diamonds3_teleport/Markdown/Diamonds3_teleport_1.md" -J "Diamonds3_teleport_1" -P "-name Diamonds3_teleport-1 -hours 24.0 -level Levels.Causal6 -main teleport" < submit.sh
bsub -o "../outputs/Diamonds3_teleport/Markdown/Diamonds3_teleport_2.md" -J "Diamonds3_teleport_2" -P "-name Diamonds3_teleport-2 -hours 24.0 -level Levels.Causal6 -main teleport" < submit.sh
mkdir ../outputs/Diamonds4_teleport/
mkdir ../outputs/Diamonds4_teleport/Markdown
bsub -o "../outputs/Diamonds4_teleport/Markdown/Diamonds4_teleport_0.md" -J "Diamonds4_teleport_0" -P "-name Diamonds4_teleport-0 -hours 24.0 -level Levels.Causal7 -main teleport" < submit.sh
bsub -o "../outputs/Diamonds4_teleport/Markdown/Diamonds4_teleport_1.md" -J "Diamonds4_teleport_1" -P "-name Diamonds4_teleport-1 -hours 24.0 -level Levels.Causal7 -main teleport" < submit.sh
bsub -o "../outputs/Diamonds4_teleport/Markdown/Diamonds4_teleport_2.md" -J "Diamonds4_teleport_2" -P "-name Diamonds4_teleport-2 -hours 24.0 -level Levels.Causal7 -main teleport" < submit.sh
mkdir ../outputs/SuperLevel1_teleport/
mkdir ../outputs/SuperLevel1_teleport/Markdown
bsub -o "../outputs/SuperLevel1_teleport/Markdown/SuperLevel1_teleport_0.md" -J "SuperLevel1_teleport_0" -P "-name SuperLevel1_teleport-0 -hours 24.0 -level Levels.SuperLevel -main teleport" < submit.sh
bsub -o "../outputs/SuperLevel1_teleport/Markdown/SuperLevel1_teleport_1.md" -J "SuperLevel1_teleport_1" -P "-name SuperLevel1_teleport-1 -hours 24.0 -level Levels.SuperLevel -main teleport" < submit.sh
bsub -o "../outputs/SuperLevel1_teleport/Markdown/SuperLevel1_teleport_2.md" -J "SuperLevel1_teleport_2" -P "-name SuperLevel1_teleport-2 -hours 24.0 -level Levels.SuperLevel -main teleport" < submit.sh
mkdir ../outputs/SuperLevel2_teleport/
mkdir ../outputs/SuperLevel2_teleport/Markdown
bsub -o "../outputs/SuperLevel2_teleport/Markdown/SuperLevel2_teleport_0.md" -J "SuperLevel2_teleport_0" -P "-name SuperLevel2_teleport-0 -hours 24.0 -level Levels.SuperLevel2 -main teleport" < submit.sh
bsub -o "../outputs/SuperLevel2_teleport/Markdown/SuperLevel2_teleport_1.md" -J "SuperLevel2_teleport_1" -P "-name SuperLevel2_teleport-1 -hours 24.0 -level Levels.SuperLevel2 -main teleport" < submit.sh
bsub -o "../outputs/SuperLevel2_teleport/Markdown/SuperLevel2_teleport_2.md" -J "SuperLevel2_teleport_2" -P "-name SuperLevel2_teleport-2 -hours 24.0 -level Levels.SuperLevel2 -main teleport" < submit.sh
mkdir ../outputs/Maze_teleport/
mkdir ../outputs/Maze_teleport/Markdown
bsub -o "../outputs/Maze_teleport/Markdown/Maze_teleport_0.md" -J "Maze_teleport_0" -P "-name Maze_teleport-0 -hours 24.0 -level Levels.Maze -main teleport" < submit.sh
bsub -o "../outputs/Maze_teleport/Markdown/Maze_teleport_1.md" -J "Maze_teleport_1" -P "-name Maze_teleport-1 -hours 24.0 -level Levels.Maze -main teleport" < submit.sh
bsub -o "../outputs/Maze_teleport/Markdown/Maze_teleport_2.md" -J "Maze_teleport_2" -P "-name Maze_teleport-2 -hours 24.0 -level Levels.Maze -main teleport" < submit.sh
mkdir ../outputs/Rocks_teleport/
mkdir ../outputs/Rocks_teleport/Markdown
bsub -o "../outputs/Rocks_teleport/Markdown/Rocks_teleport_0.md" -J "Rocks_teleport_0" -P "-name Rocks_teleport-0 -hours 24.0 -level Levels.Rocks -main teleport" < submit.sh
bsub -o "../outputs/Rocks_teleport/Markdown/Rocks_teleport_1.md" -J "Rocks_teleport_1" -P "-name Rocks_teleport-1 -hours 24.0 -level Levels.Rocks -main teleport" < submit.sh
bsub -o "../outputs/Rocks_teleport/Markdown/Rocks_teleport_2.md" -J "Rocks_teleport_2" -P "-name Rocks_teleport-2 -hours 24.0 -level Levels.Rocks -main teleport" < submit.sh
mkdir ../outputs/Coconuts_teleport/
mkdir ../outputs/Coconuts_teleport/Markdown
bsub -o "../outputs/Coconuts_teleport/Markdown/Coconuts_teleport_0.md" -J "Coconuts_teleport_0" -P "-name Coconuts_teleport-0 -hours 24.0 -level Levels.Coconuts -main teleport" < submit.sh
bsub -o "../outputs/Coconuts_teleport/Markdown/Coconuts_teleport_1.md" -J "Coconuts_teleport_1" -P "-name Coconuts_teleport-1 -hours 24.0 -level Levels.Coconuts -main teleport" < submit.sh
bsub -o "../outputs/Coconuts_teleport/Markdown/Coconuts_teleport_2.md" -J "Coconuts_teleport_2" -P "-name Coconuts_teleport-2 -hours 24.0 -level Levels.Coconuts -main teleport" < submit.sh
mkdir ../outputs/Monsters_teleport/
mkdir ../outputs/Monsters_teleport/Markdown
bsub -o "../outputs/Monsters_teleport/Markdown/Monsters_teleport_0.md" -J "Monsters_teleport_0" -P "-name Monsters_teleport-0 -hours 24.0 -level Levels.MonsterLevel -main teleport" < submit.sh
bsub -o "../outputs/Monsters_teleport/Markdown/Monsters_teleport_1.md" -J "Monsters_teleport_1" -P "-name Monsters_teleport-1 -hours 24.0 -level Levels.MonsterLevel -main teleport" < submit.sh
bsub -o "../outputs/Monsters_teleport/Markdown/Monsters_teleport_2.md" -J "Monsters_teleport_2" -P "-name Monsters_teleport-2 -hours 24.0 -level Levels.MonsterLevel -main teleport" < submit.sh
mkdir ../outputs/DoorsAndKey_teleport/
mkdir ../outputs/DoorsAndKey_teleport/Markdown
bsub -o "../outputs/DoorsAndKey_teleport/Markdown/DoorsAndKey_teleport_0.md" -J "DoorsAndKey_teleport_0" -P "-name DoorsAndKey_teleport-0 -hours 24.0 -level Levels.Causal1 -main teleport" < submit.sh
bsub -o "../outputs/DoorsAndKey_teleport/Markdown/DoorsAndKey_teleport_1.md" -J "DoorsAndKey_teleport_1" -P "-name DoorsAndKey_teleport-1 -hours 24.0 -level Levels.Causal1 -main teleport" < submit.sh
bsub -o "../outputs/DoorsAndKey_teleport/Markdown/DoorsAndKey_teleport_2.md" -J "DoorsAndKey_teleport_2" -P "-name DoorsAndKey_teleport-2 -hours 24.0 -level Levels.Causal1 -main teleport" < submit.sh
