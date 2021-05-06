#!/bin/sh
mkdir ../outputs/Attempt5_Lights1_option_critic/
mkdir ../outputs/Attempt5_Lights1_option_critic/Markdown
bsub -o "../outputs/Attempt5_Lights1_option_critic/Markdown/Attempt5_Lights1_option_critic_0.md" -J "Attempt5_Lights1_option_critic_0" -env MYARGS="-name Attempt5_Lights1_option_critic-0 -hours 72.0 -level Levels.Causal3 -main option_critic_run -batch 32" < submit_cpu.sh
bsub -o "../outputs/Attempt5_Lights1_option_critic/Markdown/Attempt5_Lights1_option_critic_1.md" -J "Attempt5_Lights1_option_critic_1" -env MYARGS="-name Attempt5_Lights1_option_critic-1 -hours 72.0 -level Levels.Causal3 -main option_critic_run -batch 32" < submit_cpu.sh
bsub -o "../outputs/Attempt5_Lights1_option_critic/Markdown/Attempt5_Lights1_option_critic_2.md" -J "Attempt5_Lights1_option_critic_2" -env MYARGS="-name Attempt5_Lights1_option_critic-2 -hours 72.0 -level Levels.Causal3 -main option_critic_run -batch 32" < submit_cpu.sh
mkdir ../outputs/Attempt5_Lights2_option_critic/
mkdir ../outputs/Attempt5_Lights2_option_critic/Markdown
bsub -o "../outputs/Attempt5_Lights2_option_critic/Markdown/Attempt5_Lights2_option_critic_0.md" -J "Attempt5_Lights2_option_critic_0" -env MYARGS="-name Attempt5_Lights2_option_critic-0 -hours 72.0 -level Levels.Causal4 -main option_critic_run -batch 32" < submit_cpu.sh
bsub -o "../outputs/Attempt5_Lights2_option_critic/Markdown/Attempt5_Lights2_option_critic_1.md" -J "Attempt5_Lights2_option_critic_1" -env MYARGS="-name Attempt5_Lights2_option_critic-1 -hours 72.0 -level Levels.Causal4 -main option_critic_run -batch 32" < submit_cpu.sh
bsub -o "../outputs/Attempt5_Lights2_option_critic/Markdown/Attempt5_Lights2_option_critic_2.md" -J "Attempt5_Lights2_option_critic_2" -env MYARGS="-name Attempt5_Lights2_option_critic-2 -hours 72.0 -level Levels.Causal4 -main option_critic_run -batch 32" < submit_cpu.sh
mkdir ../outputs/Attempt5_Diamonds1_option_critic/
mkdir ../outputs/Attempt5_Diamonds1_option_critic/Markdown
bsub -o "../outputs/Attempt5_Diamonds1_option_critic/Markdown/Attempt5_Diamonds1_option_critic_0.md" -J "Attempt5_Diamonds1_option_critic_0" -env MYARGS="-name Attempt5_Diamonds1_option_critic-0 -hours 72.0 -level Levels.Causal2 -main option_critic_run -batch 32" < submit_cpu.sh
bsub -o "../outputs/Attempt5_Diamonds1_option_critic/Markdown/Attempt5_Diamonds1_option_critic_1.md" -J "Attempt5_Diamonds1_option_critic_1" -env MYARGS="-name Attempt5_Diamonds1_option_critic-1 -hours 72.0 -level Levels.Causal2 -main option_critic_run -batch 32" < submit_cpu.sh
bsub -o "../outputs/Attempt5_Diamonds1_option_critic/Markdown/Attempt5_Diamonds1_option_critic_2.md" -J "Attempt5_Diamonds1_option_critic_2" -env MYARGS="-name Attempt5_Diamonds1_option_critic-2 -hours 72.0 -level Levels.Causal2 -main option_critic_run -batch 32" < submit_cpu.sh
mkdir ../outputs/Attempt5_Diamonds2_option_critic/
mkdir ../outputs/Attempt5_Diamonds2_option_critic/Markdown
bsub -o "../outputs/Attempt5_Diamonds2_option_critic/Markdown/Attempt5_Diamonds2_option_critic_0.md" -J "Attempt5_Diamonds2_option_critic_0" -env MYARGS="-name Attempt5_Diamonds2_option_critic-0 -hours 72.0 -level Levels.Causal5 -main option_critic_run -batch 32" < submit_cpu.sh
bsub -o "../outputs/Attempt5_Diamonds2_option_critic/Markdown/Attempt5_Diamonds2_option_critic_1.md" -J "Attempt5_Diamonds2_option_critic_1" -env MYARGS="-name Attempt5_Diamonds2_option_critic-1 -hours 72.0 -level Levels.Causal5 -main option_critic_run -batch 32" < submit_cpu.sh
bsub -o "../outputs/Attempt5_Diamonds2_option_critic/Markdown/Attempt5_Diamonds2_option_critic_2.md" -J "Attempt5_Diamonds2_option_critic_2" -env MYARGS="-name Attempt5_Diamonds2_option_critic-2 -hours 72.0 -level Levels.Causal5 -main option_critic_run -batch 32" < submit_cpu.sh
mkdir ../outputs/Attempt5_Diamonds3_option_critic/
mkdir ../outputs/Attempt5_Diamonds3_option_critic/Markdown
bsub -o "../outputs/Attempt5_Diamonds3_option_critic/Markdown/Attempt5_Diamonds3_option_critic_0.md" -J "Attempt5_Diamonds3_option_critic_0" -env MYARGS="-name Attempt5_Diamonds3_option_critic-0 -hours 72.0 -level Levels.Causal6 -main option_critic_run -batch 32" < submit_cpu.sh
bsub -o "../outputs/Attempt5_Diamonds3_option_critic/Markdown/Attempt5_Diamonds3_option_critic_1.md" -J "Attempt5_Diamonds3_option_critic_1" -env MYARGS="-name Attempt5_Diamonds3_option_critic-1 -hours 72.0 -level Levels.Causal6 -main option_critic_run -batch 32" < submit_cpu.sh
bsub -o "../outputs/Attempt5_Diamonds3_option_critic/Markdown/Attempt5_Diamonds3_option_critic_2.md" -J "Attempt5_Diamonds3_option_critic_2" -env MYARGS="-name Attempt5_Diamonds3_option_critic-2 -hours 72.0 -level Levels.Causal6 -main option_critic_run -batch 32" < submit_cpu.sh
mkdir ../outputs/Attempt5_Diamonds4_option_critic/
mkdir ../outputs/Attempt5_Diamonds4_option_critic/Markdown
bsub -o "../outputs/Attempt5_Diamonds4_option_critic/Markdown/Attempt5_Diamonds4_option_critic_0.md" -J "Attempt5_Diamonds4_option_critic_0" -env MYARGS="-name Attempt5_Diamonds4_option_critic-0 -hours 72.0 -level Levels.Causal7 -main option_critic_run -batch 32" < submit_cpu.sh
bsub -o "../outputs/Attempt5_Diamonds4_option_critic/Markdown/Attempt5_Diamonds4_option_critic_1.md" -J "Attempt5_Diamonds4_option_critic_1" -env MYARGS="-name Attempt5_Diamonds4_option_critic-1 -hours 72.0 -level Levels.Causal7 -main option_critic_run -batch 32" < submit_cpu.sh
bsub -o "../outputs/Attempt5_Diamonds4_option_critic/Markdown/Attempt5_Diamonds4_option_critic_2.md" -J "Attempt5_Diamonds4_option_critic_2" -env MYARGS="-name Attempt5_Diamonds4_option_critic-2 -hours 72.0 -level Levels.Causal7 -main option_critic_run -batch 32" < submit_cpu.sh
mkdir ../outputs/Attempt5_SuperLevel1_option_critic/
mkdir ../outputs/Attempt5_SuperLevel1_option_critic/Markdown
bsub -o "../outputs/Attempt5_SuperLevel1_option_critic/Markdown/Attempt5_SuperLevel1_option_critic_0.md" -J "Attempt5_SuperLevel1_option_critic_0" -env MYARGS="-name Attempt5_SuperLevel1_option_critic-0 -hours 72.0 -level Levels.SuperLevel -main option_critic_run -batch 32" < submit_cpu.sh
bsub -o "../outputs/Attempt5_SuperLevel1_option_critic/Markdown/Attempt5_SuperLevel1_option_critic_1.md" -J "Attempt5_SuperLevel1_option_critic_1" -env MYARGS="-name Attempt5_SuperLevel1_option_critic-1 -hours 72.0 -level Levels.SuperLevel -main option_critic_run -batch 32" < submit_cpu.sh
bsub -o "../outputs/Attempt5_SuperLevel1_option_critic/Markdown/Attempt5_SuperLevel1_option_critic_2.md" -J "Attempt5_SuperLevel1_option_critic_2" -env MYARGS="-name Attempt5_SuperLevel1_option_critic-2 -hours 72.0 -level Levels.SuperLevel -main option_critic_run -batch 32" < submit_cpu.sh
mkdir ../outputs/Attempt5_SuperLevel2_option_critic/
mkdir ../outputs/Attempt5_SuperLevel2_option_critic/Markdown
bsub -o "../outputs/Attempt5_SuperLevel2_option_critic/Markdown/Attempt5_SuperLevel2_option_critic_0.md" -J "Attempt5_SuperLevel2_option_critic_0" -env MYARGS="-name Attempt5_SuperLevel2_option_critic-0 -hours 72.0 -level Levels.SuperLevel2 -main option_critic_run -batch 32" < submit_cpu.sh
bsub -o "../outputs/Attempt5_SuperLevel2_option_critic/Markdown/Attempt5_SuperLevel2_option_critic_1.md" -J "Attempt5_SuperLevel2_option_critic_1" -env MYARGS="-name Attempt5_SuperLevel2_option_critic-1 -hours 72.0 -level Levels.SuperLevel2 -main option_critic_run -batch 32" < submit_cpu.sh
bsub -o "../outputs/Attempt5_SuperLevel2_option_critic/Markdown/Attempt5_SuperLevel2_option_critic_2.md" -J "Attempt5_SuperLevel2_option_critic_2" -env MYARGS="-name Attempt5_SuperLevel2_option_critic-2 -hours 72.0 -level Levels.SuperLevel2 -main option_critic_run -batch 32" < submit_cpu.sh
mkdir ../outputs/Attempt5_Maze_option_critic/
mkdir ../outputs/Attempt5_Maze_option_critic/Markdown
bsub -o "../outputs/Attempt5_Maze_option_critic/Markdown/Attempt5_Maze_option_critic_0.md" -J "Attempt5_Maze_option_critic_0" -env MYARGS="-name Attempt5_Maze_option_critic-0 -hours 72.0 -level Levels.Maze -main option_critic_run -batch 32" < submit_cpu.sh
bsub -o "../outputs/Attempt5_Maze_option_critic/Markdown/Attempt5_Maze_option_critic_1.md" -J "Attempt5_Maze_option_critic_1" -env MYARGS="-name Attempt5_Maze_option_critic-1 -hours 72.0 -level Levels.Maze -main option_critic_run -batch 32" < submit_cpu.sh
bsub -o "../outputs/Attempt5_Maze_option_critic/Markdown/Attempt5_Maze_option_critic_2.md" -J "Attempt5_Maze_option_critic_2" -env MYARGS="-name Attempt5_Maze_option_critic-2 -hours 72.0 -level Levels.Maze -main option_critic_run -batch 32" < submit_cpu.sh
mkdir ../outputs/Attempt5_Coconuts_option_critic/
mkdir ../outputs/Attempt5_Coconuts_option_critic/Markdown
bsub -o "../outputs/Attempt5_Coconuts_option_critic/Markdown/Attempt5_Coconuts_option_critic_0.md" -J "Attempt5_Coconuts_option_critic_0" -env MYARGS="-name Attempt5_Coconuts_option_critic-0 -hours 72.0 -level Levels.Coconuts -main option_critic_run -batch 32" < submit_cpu.sh
bsub -o "../outputs/Attempt5_Coconuts_option_critic/Markdown/Attempt5_Coconuts_option_critic_1.md" -J "Attempt5_Coconuts_option_critic_1" -env MYARGS="-name Attempt5_Coconuts_option_critic-1 -hours 72.0 -level Levels.Coconuts -main option_critic_run -batch 32" < submit_cpu.sh
bsub -o "../outputs/Attempt5_Coconuts_option_critic/Markdown/Attempt5_Coconuts_option_critic_2.md" -J "Attempt5_Coconuts_option_critic_2" -env MYARGS="-name Attempt5_Coconuts_option_critic-2 -hours 72.0 -level Levels.Coconuts -main option_critic_run -batch 32" < submit_cpu.sh
mkdir ../outputs/Attempt5_Monsters_option_critic/
mkdir ../outputs/Attempt5_Monsters_option_critic/Markdown
bsub -o "../outputs/Attempt5_Monsters_option_critic/Markdown/Attempt5_Monsters_option_critic_0.md" -J "Attempt5_Monsters_option_critic_0" -env MYARGS="-name Attempt5_Monsters_option_critic-0 -hours 72.0 -level Levels.MonsterLevel -main option_critic_run -batch 32" < submit_cpu.sh
bsub -o "../outputs/Attempt5_Monsters_option_critic/Markdown/Attempt5_Monsters_option_critic_1.md" -J "Attempt5_Monsters_option_critic_1" -env MYARGS="-name Attempt5_Monsters_option_critic-1 -hours 72.0 -level Levels.MonsterLevel -main option_critic_run -batch 32" < submit_cpu.sh
bsub -o "../outputs/Attempt5_Monsters_option_critic/Markdown/Attempt5_Monsters_option_critic_2.md" -J "Attempt5_Monsters_option_critic_2" -env MYARGS="-name Attempt5_Monsters_option_critic-2 -hours 72.0 -level Levels.MonsterLevel -main option_critic_run -batch 32" < submit_cpu.sh
mkdir ../outputs/Attempt5_DoorsAndKey_option_critic/
mkdir ../outputs/Attempt5_DoorsAndKey_option_critic/Markdown
bsub -o "../outputs/Attempt5_DoorsAndKey_option_critic/Markdown/Attempt5_DoorsAndKey_option_critic_0.md" -J "Attempt5_DoorsAndKey_option_critic_0" -env MYARGS="-name Attempt5_DoorsAndKey_option_critic-0 -hours 72.0 -level Levels.Causal1 -main option_critic_run -batch 32" < submit_cpu.sh
bsub -o "../outputs/Attempt5_DoorsAndKey_option_critic/Markdown/Attempt5_DoorsAndKey_option_critic_1.md" -J "Attempt5_DoorsAndKey_option_critic_1" -env MYARGS="-name Attempt5_DoorsAndKey_option_critic-1 -hours 72.0 -level Levels.Causal1 -main option_critic_run -batch 32" < submit_cpu.sh
bsub -o "../outputs/Attempt5_DoorsAndKey_option_critic/Markdown/Attempt5_DoorsAndKey_option_critic_2.md" -J "Attempt5_DoorsAndKey_option_critic_2" -env MYARGS="-name Attempt5_DoorsAndKey_option_critic-2 -hours 72.0 -level Levels.Causal1 -main option_critic_run -batch 32" < submit_cpu.sh
