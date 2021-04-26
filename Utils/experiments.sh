#!/bin/sh
mkdir ../outputs/Lights1_simple/
mkdir ../outputs/Lights1_simple/Markdown
bsub -o "../outputs/Lights1_simple/Markdown/Lights1_simple_0.md" -J "Lights1_simple_0" -P "-name Lights1_simple-0 -hours 24.0 -level Levels.Causal3 -main simple -network2 Networks.MiniBig" < submit.sh
bsub -o "../outputs/Lights1_simple/Markdown/Lights1_simple_1.md" -J "Lights1_simple_1" -P "-name Lights1_simple-1 -hours 24.0 -level Levels.Causal3 -main simple -network2 Networks.MiniBig" < submit.sh
bsub -o "../outputs/Lights1_simple/Markdown/Lights1_simple_2.md" -J "Lights1_simple_2" -P "-name Lights1_simple-2 -hours 24.0 -level Levels.Causal3 -main simple -network2 Networks.MiniBig" < submit.sh
mkdir ../outputs/Lights2_simple/
mkdir ../outputs/Lights2_simple/Markdown
bsub -o "../outputs/Lights2_simple/Markdown/Lights2_simple_0.md" -J "Lights2_simple_0" -P "-name Lights2_simple-0 -hours 24.0 -level Levels.Causal4 -main simple -network2 Networks.MiniBig" < submit.sh
bsub -o "../outputs/Lights2_simple/Markdown/Lights2_simple_1.md" -J "Lights2_simple_1" -P "-name Lights2_simple-1 -hours 24.0 -level Levels.Causal4 -main simple -network2 Networks.MiniBig" < submit.sh
bsub -o "../outputs/Lights2_simple/Markdown/Lights2_simple_2.md" -J "Lights2_simple_2" -P "-name Lights2_simple-2 -hours 24.0 -level Levels.Causal4 -main simple -network2 Networks.MiniBig" < submit.sh
mkdir ../outputs/Diamonds1_simple/
mkdir ../outputs/Diamonds1_simple/Markdown
bsub -o "../outputs/Diamonds1_simple/Markdown/Diamonds1_simple_0.md" -J "Diamonds1_simple_0" -P "-name Diamonds1_simple-0 -hours 24.0 -level Levels.Causal2 -main simple -network2 Networks.MiniBig" < submit.sh
bsub -o "../outputs/Diamonds1_simple/Markdown/Diamonds1_simple_1.md" -J "Diamonds1_simple_1" -P "-name Diamonds1_simple-1 -hours 24.0 -level Levels.Causal2 -main simple -network2 Networks.MiniBig" < submit.sh
bsub -o "../outputs/Diamonds1_simple/Markdown/Diamonds1_simple_2.md" -J "Diamonds1_simple_2" -P "-name Diamonds1_simple-2 -hours 24.0 -level Levels.Causal2 -main simple -network2 Networks.MiniBig" < submit.sh
mkdir ../outputs/Diamonds2_simple/
mkdir ../outputs/Diamonds2_simple/Markdown
bsub -o "../outputs/Diamonds2_simple/Markdown/Diamonds2_simple_0.md" -J "Diamonds2_simple_0" -P "-name Diamonds2_simple-0 -hours 24.0 -level Levels.Causal5 -main simple -network2 Networks.MiniBig" < submit.sh
bsub -o "../outputs/Diamonds2_simple/Markdown/Diamonds2_simple_1.md" -J "Diamonds2_simple_1" -P "-name Diamonds2_simple-1 -hours 24.0 -level Levels.Causal5 -main simple -network2 Networks.MiniBig" < submit.sh
bsub -o "../outputs/Diamonds2_simple/Markdown/Diamonds2_simple_2.md" -J "Diamonds2_simple_2" -P "-name Diamonds2_simple-2 -hours 24.0 -level Levels.Causal5 -main simple -network2 Networks.MiniBig" < submit.sh
mkdir ../outputs/Diamonds3_simple/
mkdir ../outputs/Diamonds3_simple/Markdown
bsub -o "../outputs/Diamonds3_simple/Markdown/Diamonds3_simple_0.md" -J "Diamonds3_simple_0" -P "-name Diamonds3_simple-0 -hours 24.0 -level Levels.Causal6 -main simple -network2 Networks.MiniBig" < submit.sh
bsub -o "../outputs/Diamonds3_simple/Markdown/Diamonds3_simple_1.md" -J "Diamonds3_simple_1" -P "-name Diamonds3_simple-1 -hours 24.0 -level Levels.Causal6 -main simple -network2 Networks.MiniBig" < submit.sh
bsub -o "../outputs/Diamonds3_simple/Markdown/Diamonds3_simple_2.md" -J "Diamonds3_simple_2" -P "-name Diamonds3_simple-2 -hours 24.0 -level Levels.Causal6 -main simple -network2 Networks.MiniBig" < submit.sh
mkdir ../outputs/Diamonds4_simple/
mkdir ../outputs/Diamonds4_simple/Markdown
bsub -o "../outputs/Diamonds4_simple/Markdown/Diamonds4_simple_0.md" -J "Diamonds4_simple_0" -P "-name Diamonds4_simple-0 -hours 24.0 -level Levels.Causal7 -main simple -network2 Networks.MiniBig" < submit.sh
bsub -o "../outputs/Diamonds4_simple/Markdown/Diamonds4_simple_1.md" -J "Diamonds4_simple_1" -P "-name Diamonds4_simple-1 -hours 24.0 -level Levels.Causal7 -main simple -network2 Networks.MiniBig" < submit.sh
bsub -o "../outputs/Diamonds4_simple/Markdown/Diamonds4_simple_2.md" -J "Diamonds4_simple_2" -P "-name Diamonds4_simple-2 -hours 24.0 -level Levels.Causal7 -main simple -network2 Networks.MiniBig" < submit.sh
mkdir ../outputs/SuperLevel1_simple/
mkdir ../outputs/SuperLevel1_simple/Markdown
bsub -o "../outputs/SuperLevel1_simple/Markdown/SuperLevel1_simple_0.md" -J "SuperLevel1_simple_0" -P "-name SuperLevel1_simple-0 -hours 24.0 -level Levels.SuperLevel -main simple -network2 Networks.MiniBig" < submit.sh
bsub -o "../outputs/SuperLevel1_simple/Markdown/SuperLevel1_simple_1.md" -J "SuperLevel1_simple_1" -P "-name SuperLevel1_simple-1 -hours 24.0 -level Levels.SuperLevel -main simple -network2 Networks.MiniBig" < submit.sh
bsub -o "../outputs/SuperLevel1_simple/Markdown/SuperLevel1_simple_2.md" -J "SuperLevel1_simple_2" -P "-name SuperLevel1_simple-2 -hours 24.0 -level Levels.SuperLevel -main simple -network2 Networks.MiniBig" < submit.sh
mkdir ../outputs/SuperLevel2_simple/
mkdir ../outputs/SuperLevel2_simple/Markdown
bsub -o "../outputs/SuperLevel2_simple/Markdown/SuperLevel2_simple_0.md" -J "SuperLevel2_simple_0" -P "-name SuperLevel2_simple-0 -hours 24.0 -level Levels.SuperLevel2 -main simple -network2 Networks.MiniBig" < submit.sh
bsub -o "../outputs/SuperLevel2_simple/Markdown/SuperLevel2_simple_1.md" -J "SuperLevel2_simple_1" -P "-name SuperLevel2_simple-1 -hours 24.0 -level Levels.SuperLevel2 -main simple -network2 Networks.MiniBig" < submit.sh
bsub -o "../outputs/SuperLevel2_simple/Markdown/SuperLevel2_simple_2.md" -J "SuperLevel2_simple_2" -P "-name SuperLevel2_simple-2 -hours 24.0 -level Levels.SuperLevel2 -main simple -network2 Networks.MiniBig" < submit.sh
mkdir ../outputs/Maze_simple/
mkdir ../outputs/Maze_simple/Markdown
bsub -o "../outputs/Maze_simple/Markdown/Maze_simple_0.md" -J "Maze_simple_0" -P "-name Maze_simple-0 -hours 24.0 -level Levels.Maze -main simple -network2 Networks.MiniBig" < submit.sh
bsub -o "../outputs/Maze_simple/Markdown/Maze_simple_1.md" -J "Maze_simple_1" -P "-name Maze_simple-1 -hours 24.0 -level Levels.Maze -main simple -network2 Networks.MiniBig" < submit.sh
bsub -o "../outputs/Maze_simple/Markdown/Maze_simple_2.md" -J "Maze_simple_2" -P "-name Maze_simple-2 -hours 24.0 -level Levels.Maze -main simple -network2 Networks.MiniBig" < submit.sh
mkdir ../outputs/Rocks_simple/
mkdir ../outputs/Rocks_simple/Markdown
bsub -o "../outputs/Rocks_simple/Markdown/Rocks_simple_0.md" -J "Rocks_simple_0" -P "-name Rocks_simple-0 -hours 24.0 -level Levels.Rocks -main simple -network2 Networks.MiniBig" < submit.sh
bsub -o "../outputs/Rocks_simple/Markdown/Rocks_simple_1.md" -J "Rocks_simple_1" -P "-name Rocks_simple-1 -hours 24.0 -level Levels.Rocks -main simple -network2 Networks.MiniBig" < submit.sh
bsub -o "../outputs/Rocks_simple/Markdown/Rocks_simple_2.md" -J "Rocks_simple_2" -P "-name Rocks_simple-2 -hours 24.0 -level Levels.Rocks -main simple -network2 Networks.MiniBig" < submit.sh
mkdir ../outputs/Coconuts_simple/
mkdir ../outputs/Coconuts_simple/Markdown
bsub -o "../outputs/Coconuts_simple/Markdown/Coconuts_simple_0.md" -J "Coconuts_simple_0" -P "-name Coconuts_simple-0 -hours 24.0 -level Levels.Coconuts -main simple -network2 Networks.MiniBig" < submit.sh
bsub -o "../outputs/Coconuts_simple/Markdown/Coconuts_simple_1.md" -J "Coconuts_simple_1" -P "-name Coconuts_simple-1 -hours 24.0 -level Levels.Coconuts -main simple -network2 Networks.MiniBig" < submit.sh
bsub -o "../outputs/Coconuts_simple/Markdown/Coconuts_simple_2.md" -J "Coconuts_simple_2" -P "-name Coconuts_simple-2 -hours 24.0 -level Levels.Coconuts -main simple -network2 Networks.MiniBig" < submit.sh
mkdir ../outputs/Monsters_simple/
mkdir ../outputs/Monsters_simple/Markdown
bsub -o "../outputs/Monsters_simple/Markdown/Monsters_simple_0.md" -J "Monsters_simple_0" -P "-name Monsters_simple-0 -hours 24.0 -level Levels.MonsterLevel -main simple -network2 Networks.MiniBig" < submit.sh
bsub -o "../outputs/Monsters_simple/Markdown/Monsters_simple_1.md" -J "Monsters_simple_1" -P "-name Monsters_simple-1 -hours 24.0 -level Levels.MonsterLevel -main simple -network2 Networks.MiniBig" < submit.sh
bsub -o "../outputs/Monsters_simple/Markdown/Monsters_simple_2.md" -J "Monsters_simple_2" -P "-name Monsters_simple-2 -hours 24.0 -level Levels.MonsterLevel -main simple -network2 Networks.MiniBig" < submit.sh
mkdir ../outputs/DoorsAndKey_simple/
mkdir ../outputs/DoorsAndKey_simple/Markdown
bsub -o "../outputs/DoorsAndKey_simple/Markdown/DoorsAndKey_simple_0.md" -J "DoorsAndKey_simple_0" -P "-name DoorsAndKey_simple-0 -hours 24.0 -level Levels.Causal1 -main simple -network2 Networks.MiniBig" < submit.sh
bsub -o "../outputs/DoorsAndKey_simple/Markdown/DoorsAndKey_simple_1.md" -J "DoorsAndKey_simple_1" -P "-name DoorsAndKey_simple-1 -hours 24.0 -level Levels.Causal1 -main simple -network2 Networks.MiniBig" < submit.sh
bsub -o "../outputs/DoorsAndKey_simple/Markdown/DoorsAndKey_simple_2.md" -J "DoorsAndKey_simple_2" -P "-name DoorsAndKey_simple-2 -hours 24.0 -level Levels.Causal1 -main simple -network2 Networks.MiniBig" < submit.sh
