#!/bin/sh
mkdir ../outputs/Attempt2_Lights1_option_critic/
mkdir ../outputs/Attempt2_Lights1_option_critic/Markdown
bsub -o "../outputs/Attempt2_Lights1_option_critic/Markdown/Attempt2_Lights1_option_critic_0.md" -J "Attempt2_Lights1_option_critic_0" -env MYARGS="-name Attempt2_Lights1_option_critic-0 -hours 72.0 -level Levels.Causal3 -main option_critic_run -batch 25" < submit_cpu.sh
bsub -o "../outputs/Attempt2_Lights1_option_critic/Markdown/Attempt2_Lights1_option_critic_1.md" -J "Attempt2_Lights1_option_critic_1" -env MYARGS="-name Attempt2_Lights1_option_critic-1 -hours 72.0 -level Levels.Causal3 -main option_critic_run -batch 25" < submit_cpu.sh
bsub -o "../outputs/Attempt2_Lights1_option_critic/Markdown/Attempt2_Lights1_option_critic_2.md" -J "Attempt2_Lights1_option_critic_2" -env MYARGS="-name Attempt2_Lights1_option_critic-2 -hours 72.0 -level Levels.Causal3 -main option_critic_run -batch 25" < submit_cpu.sh
mkdir ../outputs/Attempt2_Lights2_option_critic/
mkdir ../outputs/Attempt2_Lights2_option_critic/Markdown
bsub -o "../outputs/Attempt2_Lights2_option_critic/Markdown/Attempt2_Lights2_option_critic_0.md" -J "Attempt2_Lights2_option_critic_0" -env MYARGS="-name Attempt2_Lights2_option_critic-0 -hours 72.0 -level Levels.Causal4 -main option_critic_run -batch 25" < submit_cpu.sh
bsub -o "../outputs/Attempt2_Lights2_option_critic/Markdown/Attempt2_Lights2_option_critic_1.md" -J "Attempt2_Lights2_option_critic_1" -env MYARGS="-name Attempt2_Lights2_option_critic-1 -hours 72.0 -level Levels.Causal4 -main option_critic_run -batch 25" < submit_cpu.sh
bsub -o "../outputs/Attempt2_Lights2_option_critic/Markdown/Attempt2_Lights2_option_critic_2.md" -J "Attempt2_Lights2_option_critic_2" -env MYARGS="-name Attempt2_Lights2_option_critic-2 -hours 72.0 -level Levels.Causal4 -main option_critic_run -batch 25" < submit_cpu.sh
mkdir ../outputs/Attempt2_Diamonds1_option_critic/
mkdir ../outputs/Attempt2_Diamonds1_option_critic/Markdown
bsub -o "../outputs/Attempt2_Diamonds1_option_critic/Markdown/Attempt2_Diamonds1_option_critic_0.md" -J "Attempt2_Diamonds1_option_critic_0" -env MYARGS="-name Attempt2_Diamonds1_option_critic-0 -hours 72.0 -level Levels.Causal2 -main option_critic_run -batch 25" < submit_cpu.sh
bsub -o "../outputs/Attempt2_Diamonds1_option_critic/Markdown/Attempt2_Diamonds1_option_critic_1.md" -J "Attempt2_Diamonds1_option_critic_1" -env MYARGS="-name Attempt2_Diamonds1_option_critic-1 -hours 72.0 -level Levels.Causal2 -main option_critic_run -batch 25" < submit_cpu.sh
bsub -o "../outputs/Attempt2_Diamonds1_option_critic/Markdown/Attempt2_Diamonds1_option_critic_2.md" -J "Attempt2_Diamonds1_option_critic_2" -env MYARGS="-name Attempt2_Diamonds1_option_critic-2 -hours 72.0 -level Levels.Causal2 -main option_critic_run -batch 25" < submit_cpu.sh
mkdir ../outputs/Attempt2_Diamonds2_option_critic/
mkdir ../outputs/Attempt2_Diamonds2_option_critic/Markdown
bsub -o "../outputs/Attempt2_Diamonds2_option_critic/Markdown/Attempt2_Diamonds2_option_critic_0.md" -J "Attempt2_Diamonds2_option_critic_0" -env MYARGS="-name Attempt2_Diamonds2_option_critic-0 -hours 72.0 -level Levels.Causal5 -main option_critic_run -batch 25" < submit_cpu.sh
bsub -o "../outputs/Attempt2_Diamonds2_option_critic/Markdown/Attempt2_Diamonds2_option_critic_1.md" -J "Attempt2_Diamonds2_option_critic_1" -env MYARGS="-name Attempt2_Diamonds2_option_critic-1 -hours 72.0 -level Levels.Causal5 -main option_critic_run -batch 25" < submit_cpu.sh
bsub -o "../outputs/Attempt2_Diamonds2_option_critic/Markdown/Attempt2_Diamonds2_option_critic_2.md" -J "Attempt2_Diamonds2_option_critic_2" -env MYARGS="-name Attempt2_Diamonds2_option_critic-2 -hours 72.0 -level Levels.Causal5 -main option_critic_run -batch 25" < submit_cpu.sh
mkdir ../outputs/Attempt2_Diamonds3_option_critic/
mkdir ../outputs/Attempt2_Diamonds3_option_critic/Markdown
bsub -o "../outputs/Attempt2_Diamonds3_option_critic/Markdown/Attempt2_Diamonds3_option_critic_0.md" -J "Attempt2_Diamonds3_option_critic_0" -env MYARGS="-name Attempt2_Diamonds3_option_critic-0 -hours 72.0 -level Levels.Causal6 -main option_critic_run -batch 25" < submit_cpu.sh
bsub -o "../outputs/Attempt2_Diamonds3_option_critic/Markdown/Attempt2_Diamonds3_option_critic_1.md" -J "Attempt2_Diamonds3_option_critic_1" -env MYARGS="-name Attempt2_Diamonds3_option_critic-1 -hours 72.0 -level Levels.Causal6 -main option_critic_run -batch 25" < submit_cpu.sh
bsub -o "../outputs/Attempt2_Diamonds3_option_critic/Markdown/Attempt2_Diamonds3_option_critic_2.md" -J "Attempt2_Diamonds3_option_critic_2" -env MYARGS="-name Attempt2_Diamonds3_option_critic-2 -hours 72.0 -level Levels.Causal6 -main option_critic_run -batch 25" < submit_cpu.sh
mkdir ../outputs/Attempt2_Diamonds4_option_critic/
mkdir ../outputs/Attempt2_Diamonds4_option_critic/Markdown
bsub -o "../outputs/Attempt2_Diamonds4_option_critic/Markdown/Attempt2_Diamonds4_option_critic_0.md" -J "Attempt2_Diamonds4_option_critic_0" -env MYARGS="-name Attempt2_Diamonds4_option_critic-0 -hours 72.0 -level Levels.Causal7 -main option_critic_run -batch 25" < submit_cpu.sh
bsub -o "../outputs/Attempt2_Diamonds4_option_critic/Markdown/Attempt2_Diamonds4_option_critic_1.md" -J "Attempt2_Diamonds4_option_critic_1" -env MYARGS="-name Attempt2_Diamonds4_option_critic-1 -hours 72.0 -level Levels.Causal7 -main option_critic_run -batch 25" < submit_cpu.sh
bsub -o "../outputs/Attempt2_Diamonds4_option_critic/Markdown/Attempt2_Diamonds4_option_critic_2.md" -J "Attempt2_Diamonds4_option_critic_2" -env MYARGS="-name Attempt2_Diamonds4_option_critic-2 -hours 72.0 -level Levels.Causal7 -main option_critic_run -batch 25" < submit_cpu.sh
mkdir ../outputs/Attempt2_SuperLevel1_option_critic/
mkdir ../outputs/Attempt2_SuperLevel1_option_critic/Markdown
bsub -o "../outputs/Attempt2_SuperLevel1_option_critic/Markdown/Attempt2_SuperLevel1_option_critic_0.md" -J "Attempt2_SuperLevel1_option_critic_0" -env MYARGS="-name Attempt2_SuperLevel1_option_critic-0 -hours 72.0 -level Levels.SuperLevel -main option_critic_run -batch 25" < submit_cpu.sh
bsub -o "../outputs/Attempt2_SuperLevel1_option_critic/Markdown/Attempt2_SuperLevel1_option_critic_1.md" -J "Attempt2_SuperLevel1_option_critic_1" -env MYARGS="-name Attempt2_SuperLevel1_option_critic-1 -hours 72.0 -level Levels.SuperLevel -main option_critic_run -batch 25" < submit_cpu.sh
bsub -o "../outputs/Attempt2_SuperLevel1_option_critic/Markdown/Attempt2_SuperLevel1_option_critic_2.md" -J "Attempt2_SuperLevel1_option_critic_2" -env MYARGS="-name Attempt2_SuperLevel1_option_critic-2 -hours 72.0 -level Levels.SuperLevel -main option_critic_run -batch 25" < submit_cpu.sh
mkdir ../outputs/Attempt2_SuperLevel2_option_critic/
mkdir ../outputs/Attempt2_SuperLevel2_option_critic/Markdown
bsub -o "../outputs/Attempt2_SuperLevel2_option_critic/Markdown/Attempt2_SuperLevel2_option_critic_0.md" -J "Attempt2_SuperLevel2_option_critic_0" -env MYARGS="-name Attempt2_SuperLevel2_option_critic-0 -hours 72.0 -level Levels.SuperLevel2 -main option_critic_run -batch 25" < submit_cpu.sh
bsub -o "../outputs/Attempt2_SuperLevel2_option_critic/Markdown/Attempt2_SuperLevel2_option_critic_1.md" -J "Attempt2_SuperLevel2_option_critic_1" -env MYARGS="-name Attempt2_SuperLevel2_option_critic-1 -hours 72.0 -level Levels.SuperLevel2 -main option_critic_run -batch 25" < submit_cpu.sh
bsub -o "../outputs/Attempt2_SuperLevel2_option_critic/Markdown/Attempt2_SuperLevel2_option_critic_2.md" -J "Attempt2_SuperLevel2_option_critic_2" -env MYARGS="-name Attempt2_SuperLevel2_option_critic-2 -hours 72.0 -level Levels.SuperLevel2 -main option_critic_run -batch 25" < submit_cpu.sh
mkdir ../outputs/Attempt2_Maze_option_critic/
mkdir ../outputs/Attempt2_Maze_option_critic/Markdown
bsub -o "../outputs/Attempt2_Maze_option_critic/Markdown/Attempt2_Maze_option_critic_0.md" -J "Attempt2_Maze_option_critic_0" -env MYARGS="-name Attempt2_Maze_option_critic-0 -hours 72.0 -level Levels.Maze -main option_critic_run -batch 25" < submit_cpu.sh
bsub -o "../outputs/Attempt2_Maze_option_critic/Markdown/Attempt2_Maze_option_critic_1.md" -J "Attempt2_Maze_option_critic_1" -env MYARGS="-name Attempt2_Maze_option_critic-1 -hours 72.0 -level Levels.Maze -main option_critic_run -batch 25" < submit_cpu.sh
bsub -o "../outputs/Attempt2_Maze_option_critic/Markdown/Attempt2_Maze_option_critic_2.md" -J "Attempt2_Maze_option_critic_2" -env MYARGS="-name Attempt2_Maze_option_critic-2 -hours 72.0 -level Levels.Maze -main option_critic_run -batch 25" < submit_cpu.sh
mkdir ../outputs/Attempt2_Coconuts_option_critic/
mkdir ../outputs/Attempt2_Coconuts_option_critic/Markdown
bsub -o "../outputs/Attempt2_Coconuts_option_critic/Markdown/Attempt2_Coconuts_option_critic_0.md" -J "Attempt2_Coconuts_option_critic_0" -env MYARGS="-name Attempt2_Coconuts_option_critic-0 -hours 72.0 -level Levels.Coconuts -main option_critic_run -batch 25" < submit_cpu.sh
bsub -o "../outputs/Attempt2_Coconuts_option_critic/Markdown/Attempt2_Coconuts_option_critic_1.md" -J "Attempt2_Coconuts_option_critic_1" -env MYARGS="-name Attempt2_Coconuts_option_critic-1 -hours 72.0 -level Levels.Coconuts -main option_critic_run -batch 25" < submit_cpu.sh
bsub -o "../outputs/Attempt2_Coconuts_option_critic/Markdown/Attempt2_Coconuts_option_critic_2.md" -J "Attempt2_Coconuts_option_critic_2" -env MYARGS="-name Attempt2_Coconuts_option_critic-2 -hours 72.0 -level Levels.Coconuts -main option_critic_run -batch 25" < submit_cpu.sh
mkdir ../outputs/Attempt2_Monsters_option_critic/
mkdir ../outputs/Attempt2_Monsters_option_critic/Markdown
bsub -o "../outputs/Attempt2_Monsters_option_critic/Markdown/Attempt2_Monsters_option_critic_0.md" -J "Attempt2_Monsters_option_critic_0" -env MYARGS="-name Attempt2_Monsters_option_critic-0 -hours 72.0 -level Levels.MonsterLevel -main option_critic_run -batch 25" < submit_cpu.sh
bsub -o "../outputs/Attempt2_Monsters_option_critic/Markdown/Attempt2_Monsters_option_critic_1.md" -J "Attempt2_Monsters_option_critic_1" -env MYARGS="-name Attempt2_Monsters_option_critic-1 -hours 72.0 -level Levels.MonsterLevel -main option_critic_run -batch 25" < submit_cpu.sh
bsub -o "../outputs/Attempt2_Monsters_option_critic/Markdown/Attempt2_Monsters_option_critic_2.md" -J "Attempt2_Monsters_option_critic_2" -env MYARGS="-name Attempt2_Monsters_option_critic-2 -hours 72.0 -level Levels.MonsterLevel -main option_critic_run -batch 25" < submit_cpu.sh
mkdir ../outputs/Attempt2_DoorsAndKey_option_critic/
mkdir ../outputs/Attempt2_DoorsAndKey_option_critic/Markdown
bsub -o "../outputs/Attempt2_DoorsAndKey_option_critic/Markdown/Attempt2_DoorsAndKey_option_critic_0.md" -J "Attempt2_DoorsAndKey_option_critic_0" -env MYARGS="-name Attempt2_DoorsAndKey_option_critic-0 -hours 72.0 -level Levels.Causal1 -main option_critic_run -batch 25" < submit_cpu.sh
bsub -o "../outputs/Attempt2_DoorsAndKey_option_critic/Markdown/Attempt2_DoorsAndKey_option_critic_1.md" -J "Attempt2_DoorsAndKey_option_critic_1" -env MYARGS="-name Attempt2_DoorsAndKey_option_critic-1 -hours 72.0 -level Levels.Causal1 -main option_critic_run -batch 25" < submit_cpu.sh
bsub -o "../outputs/Attempt2_DoorsAndKey_option_critic/Markdown/Attempt2_DoorsAndKey_option_critic_2.md" -J "Attempt2_DoorsAndKey_option_critic_2" -env MYARGS="-name Attempt2_DoorsAndKey_option_critic-2 -hours 72.0 -level Levels.Causal1 -main option_critic_run -batch 25" < submit_cpu.sh
