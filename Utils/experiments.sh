#!/bin/sh
mkdir ../outputs/Attempt6_Lights1_option_critic/
mkdir ../outputs/Attempt6_Lights1_option_critic/Markdown
bsub -o "../outputs/Attempt6_Lights1_option_critic/Markdown/Attempt6_Lights1_option_critic_0.md" -J "Attempt6_Lights1_option_critic_0" -env MYARGS="-name Attempt6_Lights1_option_critic-0 -hours 72.0 -level Levels.Causal3 -main option_critic_run -batch 32 -num 0" < submit_cpu.sh
bsub -o "../outputs/Attempt6_Lights1_option_critic/Markdown/Attempt6_Lights1_option_critic_1.md" -J "Attempt6_Lights1_option_critic_1" -env MYARGS="-name Attempt6_Lights1_option_critic-1 -hours 72.0 -level Levels.Causal3 -main option_critic_run -batch 32 -num 1" < submit_cpu.sh
bsub -o "../outputs/Attempt6_Lights1_option_critic/Markdown/Attempt6_Lights1_option_critic_2.md" -J "Attempt6_Lights1_option_critic_2" -env MYARGS="-name Attempt6_Lights1_option_critic-2 -hours 72.0 -level Levels.Causal3 -main option_critic_run -batch 32 -num 2" < submit_cpu.sh
mkdir ../outputs/Attempt6_Lights2_option_critic/
mkdir ../outputs/Attempt6_Lights2_option_critic/Markdown
bsub -o "../outputs/Attempt6_Lights2_option_critic/Markdown/Attempt6_Lights2_option_critic_0.md" -J "Attempt6_Lights2_option_critic_0" -env MYARGS="-name Attempt6_Lights2_option_critic-0 -hours 72.0 -level Levels.Causal4 -main option_critic_run -batch 32 -num 0" < submit_cpu.sh
bsub -o "../outputs/Attempt6_Lights2_option_critic/Markdown/Attempt6_Lights2_option_critic_1.md" -J "Attempt6_Lights2_option_critic_1" -env MYARGS="-name Attempt6_Lights2_option_critic-1 -hours 72.0 -level Levels.Causal4 -main option_critic_run -batch 32 -num 1" < submit_cpu.sh
bsub -o "../outputs/Attempt6_Lights2_option_critic/Markdown/Attempt6_Lights2_option_critic_2.md" -J "Attempt6_Lights2_option_critic_2" -env MYARGS="-name Attempt6_Lights2_option_critic-2 -hours 72.0 -level Levels.Causal4 -main option_critic_run -batch 32 -num 2" < submit_cpu.sh
mkdir ../outputs/Attempt6_Diamonds1_option_critic/
mkdir ../outputs/Attempt6_Diamonds1_option_critic/Markdown
bsub -o "../outputs/Attempt6_Diamonds1_option_critic/Markdown/Attempt6_Diamonds1_option_critic_0.md" -J "Attempt6_Diamonds1_option_critic_0" -env MYARGS="-name Attempt6_Diamonds1_option_critic-0 -hours 72.0 -level Levels.Causal2 -main option_critic_run -batch 32 -num 0" < submit_cpu.sh
bsub -o "../outputs/Attempt6_Diamonds1_option_critic/Markdown/Attempt6_Diamonds1_option_critic_1.md" -J "Attempt6_Diamonds1_option_critic_1" -env MYARGS="-name Attempt6_Diamonds1_option_critic-1 -hours 72.0 -level Levels.Causal2 -main option_critic_run -batch 32 -num 1" < submit_cpu.sh
bsub -o "../outputs/Attempt6_Diamonds1_option_critic/Markdown/Attempt6_Diamonds1_option_critic_2.md" -J "Attempt6_Diamonds1_option_critic_2" -env MYARGS="-name Attempt6_Diamonds1_option_critic-2 -hours 72.0 -level Levels.Causal2 -main option_critic_run -batch 32 -num 2" < submit_cpu.sh
mkdir ../outputs/Attempt6_Diamonds2_option_critic/
mkdir ../outputs/Attempt6_Diamonds2_option_critic/Markdown
bsub -o "../outputs/Attempt6_Diamonds2_option_critic/Markdown/Attempt6_Diamonds2_option_critic_0.md" -J "Attempt6_Diamonds2_option_critic_0" -env MYARGS="-name Attempt6_Diamonds2_option_critic-0 -hours 72.0 -level Levels.Causal5 -main option_critic_run -batch 32 -num 0" < submit_cpu.sh
bsub -o "../outputs/Attempt6_Diamonds2_option_critic/Markdown/Attempt6_Diamonds2_option_critic_1.md" -J "Attempt6_Diamonds2_option_critic_1" -env MYARGS="-name Attempt6_Diamonds2_option_critic-1 -hours 72.0 -level Levels.Causal5 -main option_critic_run -batch 32 -num 1" < submit_cpu.sh
bsub -o "../outputs/Attempt6_Diamonds2_option_critic/Markdown/Attempt6_Diamonds2_option_critic_2.md" -J "Attempt6_Diamonds2_option_critic_2" -env MYARGS="-name Attempt6_Diamonds2_option_critic-2 -hours 72.0 -level Levels.Causal5 -main option_critic_run -batch 32 -num 2" < submit_cpu.sh
mkdir ../outputs/Attempt6_Diamonds3_option_critic/
mkdir ../outputs/Attempt6_Diamonds3_option_critic/Markdown
bsub -o "../outputs/Attempt6_Diamonds3_option_critic/Markdown/Attempt6_Diamonds3_option_critic_0.md" -J "Attempt6_Diamonds3_option_critic_0" -env MYARGS="-name Attempt6_Diamonds3_option_critic-0 -hours 72.0 -level Levels.Causal6 -main option_critic_run -batch 32 -num 0" < submit_cpu.sh
bsub -o "../outputs/Attempt6_Diamonds3_option_critic/Markdown/Attempt6_Diamonds3_option_critic_1.md" -J "Attempt6_Diamonds3_option_critic_1" -env MYARGS="-name Attempt6_Diamonds3_option_critic-1 -hours 72.0 -level Levels.Causal6 -main option_critic_run -batch 32 -num 1" < submit_cpu.sh
bsub -o "../outputs/Attempt6_Diamonds3_option_critic/Markdown/Attempt6_Diamonds3_option_critic_2.md" -J "Attempt6_Diamonds3_option_critic_2" -env MYARGS="-name Attempt6_Diamonds3_option_critic-2 -hours 72.0 -level Levels.Causal6 -main option_critic_run -batch 32 -num 2" < submit_cpu.sh
mkdir ../outputs/Attempt6_Diamonds4_option_critic/
mkdir ../outputs/Attempt6_Diamonds4_option_critic/Markdown
bsub -o "../outputs/Attempt6_Diamonds4_option_critic/Markdown/Attempt6_Diamonds4_option_critic_0.md" -J "Attempt6_Diamonds4_option_critic_0" -env MYARGS="-name Attempt6_Diamonds4_option_critic-0 -hours 72.0 -level Levels.Causal7 -main option_critic_run -batch 32 -num 0" < submit_cpu.sh
bsub -o "../outputs/Attempt6_Diamonds4_option_critic/Markdown/Attempt6_Diamonds4_option_critic_1.md" -J "Attempt6_Diamonds4_option_critic_1" -env MYARGS="-name Attempt6_Diamonds4_option_critic-1 -hours 72.0 -level Levels.Causal7 -main option_critic_run -batch 32 -num 1" < submit_cpu.sh
bsub -o "../outputs/Attempt6_Diamonds4_option_critic/Markdown/Attempt6_Diamonds4_option_critic_2.md" -J "Attempt6_Diamonds4_option_critic_2" -env MYARGS="-name Attempt6_Diamonds4_option_critic-2 -hours 72.0 -level Levels.Causal7 -main option_critic_run -batch 32 -num 2" < submit_cpu.sh
mkdir ../outputs/Attempt6_SuperLevel1_option_critic/
mkdir ../outputs/Attempt6_SuperLevel1_option_critic/Markdown
bsub -o "../outputs/Attempt6_SuperLevel1_option_critic/Markdown/Attempt6_SuperLevel1_option_critic_0.md" -J "Attempt6_SuperLevel1_option_critic_0" -env MYARGS="-name Attempt6_SuperLevel1_option_critic-0 -hours 72.0 -level Levels.SuperLevel -main option_critic_run -batch 32 -num 0" < submit_cpu.sh
bsub -o "../outputs/Attempt6_SuperLevel1_option_critic/Markdown/Attempt6_SuperLevel1_option_critic_1.md" -J "Attempt6_SuperLevel1_option_critic_1" -env MYARGS="-name Attempt6_SuperLevel1_option_critic-1 -hours 72.0 -level Levels.SuperLevel -main option_critic_run -batch 32 -num 1" < submit_cpu.sh
bsub -o "../outputs/Attempt6_SuperLevel1_option_critic/Markdown/Attempt6_SuperLevel1_option_critic_2.md" -J "Attempt6_SuperLevel1_option_critic_2" -env MYARGS="-name Attempt6_SuperLevel1_option_critic-2 -hours 72.0 -level Levels.SuperLevel -main option_critic_run -batch 32 -num 2" < submit_cpu.sh
mkdir ../outputs/Attempt6_SuperLevel2_option_critic/
mkdir ../outputs/Attempt6_SuperLevel2_option_critic/Markdown
bsub -o "../outputs/Attempt6_SuperLevel2_option_critic/Markdown/Attempt6_SuperLevel2_option_critic_0.md" -J "Attempt6_SuperLevel2_option_critic_0" -env MYARGS="-name Attempt6_SuperLevel2_option_critic-0 -hours 72.0 -level Levels.SuperLevel2 -main option_critic_run -batch 32 -num 0" < submit_cpu.sh
bsub -o "../outputs/Attempt6_SuperLevel2_option_critic/Markdown/Attempt6_SuperLevel2_option_critic_1.md" -J "Attempt6_SuperLevel2_option_critic_1" -env MYARGS="-name Attempt6_SuperLevel2_option_critic-1 -hours 72.0 -level Levels.SuperLevel2 -main option_critic_run -batch 32 -num 1" < submit_cpu.sh
bsub -o "../outputs/Attempt6_SuperLevel2_option_critic/Markdown/Attempt6_SuperLevel2_option_critic_2.md" -J "Attempt6_SuperLevel2_option_critic_2" -env MYARGS="-name Attempt6_SuperLevel2_option_critic-2 -hours 72.0 -level Levels.SuperLevel2 -main option_critic_run -batch 32 -num 2" < submit_cpu.sh
mkdir ../outputs/Attempt6_Maze_option_critic/
mkdir ../outputs/Attempt6_Maze_option_critic/Markdown
bsub -o "../outputs/Attempt6_Maze_option_critic/Markdown/Attempt6_Maze_option_critic_0.md" -J "Attempt6_Maze_option_critic_0" -env MYARGS="-name Attempt6_Maze_option_critic-0 -hours 72.0 -level Levels.Maze -main option_critic_run -batch 32 -num 0" < submit_cpu.sh
bsub -o "../outputs/Attempt6_Maze_option_critic/Markdown/Attempt6_Maze_option_critic_1.md" -J "Attempt6_Maze_option_critic_1" -env MYARGS="-name Attempt6_Maze_option_critic-1 -hours 72.0 -level Levels.Maze -main option_critic_run -batch 32 -num 1" < submit_cpu.sh
bsub -o "../outputs/Attempt6_Maze_option_critic/Markdown/Attempt6_Maze_option_critic_2.md" -J "Attempt6_Maze_option_critic_2" -env MYARGS="-name Attempt6_Maze_option_critic-2 -hours 72.0 -level Levels.Maze -main option_critic_run -batch 32 -num 2" < submit_cpu.sh
mkdir ../outputs/Attempt6_Coconuts_option_critic/
mkdir ../outputs/Attempt6_Coconuts_option_critic/Markdown
bsub -o "../outputs/Attempt6_Coconuts_option_critic/Markdown/Attempt6_Coconuts_option_critic_0.md" -J "Attempt6_Coconuts_option_critic_0" -env MYARGS="-name Attempt6_Coconuts_option_critic-0 -hours 72.0 -level Levels.Coconuts -main option_critic_run -batch 32 -num 0" < submit_cpu.sh
bsub -o "../outputs/Attempt6_Coconuts_option_critic/Markdown/Attempt6_Coconuts_option_critic_1.md" -J "Attempt6_Coconuts_option_critic_1" -env MYARGS="-name Attempt6_Coconuts_option_critic-1 -hours 72.0 -level Levels.Coconuts -main option_critic_run -batch 32 -num 1" < submit_cpu.sh
bsub -o "../outputs/Attempt6_Coconuts_option_critic/Markdown/Attempt6_Coconuts_option_critic_2.md" -J "Attempt6_Coconuts_option_critic_2" -env MYARGS="-name Attempt6_Coconuts_option_critic-2 -hours 72.0 -level Levels.Coconuts -main option_critic_run -batch 32 -num 2" < submit_cpu.sh
mkdir ../outputs/Attempt6_Monsters_option_critic/
mkdir ../outputs/Attempt6_Monsters_option_critic/Markdown
bsub -o "../outputs/Attempt6_Monsters_option_critic/Markdown/Attempt6_Monsters_option_critic_0.md" -J "Attempt6_Monsters_option_critic_0" -env MYARGS="-name Attempt6_Monsters_option_critic-0 -hours 72.0 -level Levels.MonsterLevel -main option_critic_run -batch 32 -num 0" < submit_cpu.sh
bsub -o "../outputs/Attempt6_Monsters_option_critic/Markdown/Attempt6_Monsters_option_critic_1.md" -J "Attempt6_Monsters_option_critic_1" -env MYARGS="-name Attempt6_Monsters_option_critic-1 -hours 72.0 -level Levels.MonsterLevel -main option_critic_run -batch 32 -num 1" < submit_cpu.sh
bsub -o "../outputs/Attempt6_Monsters_option_critic/Markdown/Attempt6_Monsters_option_critic_2.md" -J "Attempt6_Monsters_option_critic_2" -env MYARGS="-name Attempt6_Monsters_option_critic-2 -hours 72.0 -level Levels.MonsterLevel -main option_critic_run -batch 32 -num 2" < submit_cpu.sh
mkdir ../outputs/Attempt6_DoorsAndKey_option_critic/
mkdir ../outputs/Attempt6_DoorsAndKey_option_critic/Markdown
bsub -o "../outputs/Attempt6_DoorsAndKey_option_critic/Markdown/Attempt6_DoorsAndKey_option_critic_0.md" -J "Attempt6_DoorsAndKey_option_critic_0" -env MYARGS="-name Attempt6_DoorsAndKey_option_critic-0 -hours 72.0 -level Levels.Causal1 -main option_critic_run -batch 32 -num 0" < submit_cpu.sh
bsub -o "../outputs/Attempt6_DoorsAndKey_option_critic/Markdown/Attempt6_DoorsAndKey_option_critic_1.md" -J "Attempt6_DoorsAndKey_option_critic_1" -env MYARGS="-name Attempt6_DoorsAndKey_option_critic-1 -hours 72.0 -level Levels.Causal1 -main option_critic_run -batch 32 -num 1" < submit_cpu.sh
bsub -o "../outputs/Attempt6_DoorsAndKey_option_critic/Markdown/Attempt6_DoorsAndKey_option_critic_2.md" -J "Attempt6_DoorsAndKey_option_critic_2" -env MYARGS="-name Attempt6_DoorsAndKey_option_critic-2 -hours 72.0 -level Levels.Causal1 -main option_critic_run -batch 32 -num 2" < submit_cpu.sh
