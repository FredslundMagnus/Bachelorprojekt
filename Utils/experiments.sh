#!/bin/sh
mkdir ../outputs/Lights1_option_critic/
mkdir ../outputs/Lights1_option_critic/Markdown
bsub -o "../outputs/Lights1_option_critic/Markdown/Lights1_option_critic_0.md" -J "Lights1_option_critic_0" -P "-name Lights1_option_critic-0 -hours 72.0 -level Levels.Causal3 -main option_critic_run -batch 25" < submit_cpu.sh
bsub -o "../outputs/Lights1_option_critic/Markdown/Lights1_option_critic_1.md" -J "Lights1_option_critic_1" -P "-name Lights1_option_critic-1 -hours 72.0 -level Levels.Causal3 -main option_critic_run -batch 25" < submit_cpu.sh
bsub -o "../outputs/Lights1_option_critic/Markdown/Lights1_option_critic_2.md" -J "Lights1_option_critic_2" -P "-name Lights1_option_critic-2 -hours 72.0 -level Levels.Causal3 -main option_critic_run -batch 25" < submit_cpu.sh
mkdir ../outputs/Lights2_option_critic/
mkdir ../outputs/Lights2_option_critic/Markdown
bsub -o "../outputs/Lights2_option_critic/Markdown/Lights2_option_critic_0.md" -J "Lights2_option_critic_0" -P "-name Lights2_option_critic-0 -hours 72.0 -level Levels.Causal4 -main option_critic_run -batch 25" < submit_cpu.sh
bsub -o "../outputs/Lights2_option_critic/Markdown/Lights2_option_critic_1.md" -J "Lights2_option_critic_1" -P "-name Lights2_option_critic-1 -hours 72.0 -level Levels.Causal4 -main option_critic_run -batch 25" < submit_cpu.sh
bsub -o "../outputs/Lights2_option_critic/Markdown/Lights2_option_critic_2.md" -J "Lights2_option_critic_2" -P "-name Lights2_option_critic-2 -hours 72.0 -level Levels.Causal4 -main option_critic_run -batch 25" < submit_cpu.sh
mkdir ../outputs/Diamonds1_option_critic/
mkdir ../outputs/Diamonds1_option_critic/Markdown
bsub -o "../outputs/Diamonds1_option_critic/Markdown/Diamonds1_option_critic_0.md" -J "Diamonds1_option_critic_0" -P "-name Diamonds1_option_critic-0 -hours 72.0 -level Levels.Causal2 -main option_critic_run -batch 25" < submit_cpu.sh
bsub -o "../outputs/Diamonds1_option_critic/Markdown/Diamonds1_option_critic_1.md" -J "Diamonds1_option_critic_1" -P "-name Diamonds1_option_critic-1 -hours 72.0 -level Levels.Causal2 -main option_critic_run -batch 25" < submit_cpu.sh
bsub -o "../outputs/Diamonds1_option_critic/Markdown/Diamonds1_option_critic_2.md" -J "Diamonds1_option_critic_2" -P "-name Diamonds1_option_critic-2 -hours 72.0 -level Levels.Causal2 -main option_critic_run -batch 25" < submit_cpu.sh
mkdir ../outputs/Diamonds2_option_critic/
mkdir ../outputs/Diamonds2_option_critic/Markdown
bsub -o "../outputs/Diamonds2_option_critic/Markdown/Diamonds2_option_critic_0.md" -J "Diamonds2_option_critic_0" -P "-name Diamonds2_option_critic-0 -hours 72.0 -level Levels.Causal5 -main option_critic_run -batch 25" < submit_cpu.sh
bsub -o "../outputs/Diamonds2_option_critic/Markdown/Diamonds2_option_critic_1.md" -J "Diamonds2_option_critic_1" -P "-name Diamonds2_option_critic-1 -hours 72.0 -level Levels.Causal5 -main option_critic_run -batch 25" < submit_cpu.sh
bsub -o "../outputs/Diamonds2_option_critic/Markdown/Diamonds2_option_critic_2.md" -J "Diamonds2_option_critic_2" -P "-name Diamonds2_option_critic-2 -hours 72.0 -level Levels.Causal5 -main option_critic_run -batch 25" < submit_cpu.sh
mkdir ../outputs/Diamonds3_option_critic/
mkdir ../outputs/Diamonds3_option_critic/Markdown
bsub -o "../outputs/Diamonds3_option_critic/Markdown/Diamonds3_option_critic_0.md" -J "Diamonds3_option_critic_0" -P "-name Diamonds3_option_critic-0 -hours 72.0 -level Levels.Causal6 -main option_critic_run -batch 25" < submit_cpu.sh
bsub -o "../outputs/Diamonds3_option_critic/Markdown/Diamonds3_option_critic_1.md" -J "Diamonds3_option_critic_1" -P "-name Diamonds3_option_critic-1 -hours 72.0 -level Levels.Causal6 -main option_critic_run -batch 25" < submit_cpu.sh
bsub -o "../outputs/Diamonds3_option_critic/Markdown/Diamonds3_option_critic_2.md" -J "Diamonds3_option_critic_2" -P "-name Diamonds3_option_critic-2 -hours 72.0 -level Levels.Causal6 -main option_critic_run -batch 25" < submit_cpu.sh
mkdir ../outputs/Diamonds4_option_critic/
mkdir ../outputs/Diamonds4_option_critic/Markdown
bsub -o "../outputs/Diamonds4_option_critic/Markdown/Diamonds4_option_critic_0.md" -J "Diamonds4_option_critic_0" -P "-name Diamonds4_option_critic-0 -hours 72.0 -level Levels.Causal7 -main option_critic_run -batch 25" < submit_cpu.sh
bsub -o "../outputs/Diamonds4_option_critic/Markdown/Diamonds4_option_critic_1.md" -J "Diamonds4_option_critic_1" -P "-name Diamonds4_option_critic-1 -hours 72.0 -level Levels.Causal7 -main option_critic_run -batch 25" < submit_cpu.sh
bsub -o "../outputs/Diamonds4_option_critic/Markdown/Diamonds4_option_critic_2.md" -J "Diamonds4_option_critic_2" -P "-name Diamonds4_option_critic-2 -hours 72.0 -level Levels.Causal7 -main option_critic_run -batch 25" < submit_cpu.sh
mkdir ../outputs/SuperLevel1_option_critic/
mkdir ../outputs/SuperLevel1_option_critic/Markdown
bsub -o "../outputs/SuperLevel1_option_critic/Markdown/SuperLevel1_option_critic_0.md" -J "SuperLevel1_option_critic_0" -P "-name SuperLevel1_option_critic-0 -hours 72.0 -level Levels.SuperLevel -main option_critic_run -batch 25" < submit_cpu.sh
bsub -o "../outputs/SuperLevel1_option_critic/Markdown/SuperLevel1_option_critic_1.md" -J "SuperLevel1_option_critic_1" -P "-name SuperLevel1_option_critic-1 -hours 72.0 -level Levels.SuperLevel -main option_critic_run -batch 25" < submit_cpu.sh
bsub -o "../outputs/SuperLevel1_option_critic/Markdown/SuperLevel1_option_critic_2.md" -J "SuperLevel1_option_critic_2" -P "-name SuperLevel1_option_critic-2 -hours 72.0 -level Levels.SuperLevel -main option_critic_run -batch 25" < submit_cpu.sh
mkdir ../outputs/SuperLevel2_option_critic/
mkdir ../outputs/SuperLevel2_option_critic/Markdown
bsub -o "../outputs/SuperLevel2_option_critic/Markdown/SuperLevel2_option_critic_0.md" -J "SuperLevel2_option_critic_0" -P "-name SuperLevel2_option_critic-0 -hours 72.0 -level Levels.SuperLevel2 -main option_critic_run -batch 25" < submit_cpu.sh
bsub -o "../outputs/SuperLevel2_option_critic/Markdown/SuperLevel2_option_critic_1.md" -J "SuperLevel2_option_critic_1" -P "-name SuperLevel2_option_critic-1 -hours 72.0 -level Levels.SuperLevel2 -main option_critic_run -batch 25" < submit_cpu.sh
bsub -o "../outputs/SuperLevel2_option_critic/Markdown/SuperLevel2_option_critic_2.md" -J "SuperLevel2_option_critic_2" -P "-name SuperLevel2_option_critic-2 -hours 72.0 -level Levels.SuperLevel2 -main option_critic_run -batch 25" < submit_cpu.sh
mkdir ../outputs/Maze_option_critic/
mkdir ../outputs/Maze_option_critic/Markdown
bsub -o "../outputs/Maze_option_critic/Markdown/Maze_option_critic_0.md" -J "Maze_option_critic_0" -P "-name Maze_option_critic-0 -hours 72.0 -level Levels.Maze -main option_critic_run -batch 25" < submit_cpu.sh
bsub -o "../outputs/Maze_option_critic/Markdown/Maze_option_critic_1.md" -J "Maze_option_critic_1" -P "-name Maze_option_critic-1 -hours 72.0 -level Levels.Maze -main option_critic_run -batch 25" < submit_cpu.sh
bsub -o "../outputs/Maze_option_critic/Markdown/Maze_option_critic_2.md" -J "Maze_option_critic_2" -P "-name Maze_option_critic-2 -hours 72.0 -level Levels.Maze -main option_critic_run -batch 25" < submit_cpu.sh
mkdir ../outputs/Rocks_option_critic/
mkdir ../outputs/Rocks_option_critic/Markdown
bsub -o "../outputs/Rocks_option_critic/Markdown/Rocks_option_critic_0.md" -J "Rocks_option_critic_0" -P "-name Rocks_option_critic-0 -hours 72.0 -level Levels.Rocks -main option_critic_run -batch 25" < submit_cpu.sh
bsub -o "../outputs/Rocks_option_critic/Markdown/Rocks_option_critic_1.md" -J "Rocks_option_critic_1" -P "-name Rocks_option_critic-1 -hours 72.0 -level Levels.Rocks -main option_critic_run -batch 25" < submit_cpu.sh
bsub -o "../outputs/Rocks_option_critic/Markdown/Rocks_option_critic_2.md" -J "Rocks_option_critic_2" -P "-name Rocks_option_critic-2 -hours 72.0 -level Levels.Rocks -main option_critic_run -batch 25" < submit_cpu.sh
mkdir ../outputs/Coconuts_option_critic/
mkdir ../outputs/Coconuts_option_critic/Markdown
bsub -o "../outputs/Coconuts_option_critic/Markdown/Coconuts_option_critic_0.md" -J "Coconuts_option_critic_0" -P "-name Coconuts_option_critic-0 -hours 72.0 -level Levels.Coconuts -main option_critic_run -batch 25" < submit_cpu.sh
bsub -o "../outputs/Coconuts_option_critic/Markdown/Coconuts_option_critic_1.md" -J "Coconuts_option_critic_1" -P "-name Coconuts_option_critic-1 -hours 72.0 -level Levels.Coconuts -main option_critic_run -batch 25" < submit_cpu.sh
bsub -o "../outputs/Coconuts_option_critic/Markdown/Coconuts_option_critic_2.md" -J "Coconuts_option_critic_2" -P "-name Coconuts_option_critic-2 -hours 72.0 -level Levels.Coconuts -main option_critic_run -batch 25" < submit_cpu.sh
mkdir ../outputs/Monsters_option_critic/
mkdir ../outputs/Monsters_option_critic/Markdown
bsub -o "../outputs/Monsters_option_critic/Markdown/Monsters_option_critic_0.md" -J "Monsters_option_critic_0" -P "-name Monsters_option_critic-0 -hours 72.0 -level Levels.MonsterLevel -main option_critic_run -batch 25" < submit_cpu.sh
bsub -o "../outputs/Monsters_option_critic/Markdown/Monsters_option_critic_1.md" -J "Monsters_option_critic_1" -P "-name Monsters_option_critic-1 -hours 72.0 -level Levels.MonsterLevel -main option_critic_run -batch 25" < submit_cpu.sh
bsub -o "../outputs/Monsters_option_critic/Markdown/Monsters_option_critic_2.md" -J "Monsters_option_critic_2" -P "-name Monsters_option_critic-2 -hours 72.0 -level Levels.MonsterLevel -main option_critic_run -batch 25" < submit_cpu.sh
mkdir ../outputs/DoorsAndKey_option_critic/
mkdir ../outputs/DoorsAndKey_option_critic/Markdown
bsub -o "../outputs/DoorsAndKey_option_critic/Markdown/DoorsAndKey_option_critic_0.md" -J "DoorsAndKey_option_critic_0" -P "-name DoorsAndKey_option_critic-0 -hours 72.0 -level Levels.Causal1 -main option_critic_run -batch 25" < submit_cpu.sh
bsub -o "../outputs/DoorsAndKey_option_critic/Markdown/DoorsAndKey_option_critic_1.md" -J "DoorsAndKey_option_critic_1" -P "-name DoorsAndKey_option_critic-1 -hours 72.0 -level Levels.Causal1 -main option_critic_run -batch 25" < submit_cpu.sh
bsub -o "../outputs/DoorsAndKey_option_critic/Markdown/DoorsAndKey_option_critic_2.md" -J "DoorsAndKey_option_critic_2" -P "-name DoorsAndKey_option_critic-2 -hours 72.0 -level Levels.Causal1 -main option_critic_run -batch 25" < submit_cpu.sh
