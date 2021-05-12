#!/bin/sh
mkdir ../outputs/Attempt8_Lights1_option_critic/
mkdir ../outputs/Attempt8_Lights1_option_critic/Markdown
bsub -o "../outputs/Attempt8_Lights1_option_critic/Markdown/Attempt8_Lights1_option_critic_0.md" -J "Attempt8_Lights1_option_critic_0" -env MYARGS="-name Attempt8_Lights1_option_critic-0 -hours 72.0 -level Levels.Causal3 -main option_critic_run -batch 32 -num 0" < submit_cpu.sh
bsub -o "../outputs/Attempt8_Lights1_option_critic/Markdown/Attempt8_Lights1_option_critic_1.md" -J "Attempt8_Lights1_option_critic_1" -env MYARGS="-name Attempt8_Lights1_option_critic-1 -hours 72.0 -level Levels.Causal3 -main option_critic_run -batch 32 -num 1" < submit_cpu.sh
bsub -o "../outputs/Attempt8_Lights1_option_critic/Markdown/Attempt8_Lights1_option_critic_2.md" -J "Attempt8_Lights1_option_critic_2" -env MYARGS="-name Attempt8_Lights1_option_critic-2 -hours 72.0 -level Levels.Causal3 -main option_critic_run -batch 32 -num 2" < submit_cpu.sh
mkdir ../outputs/Attempt8_Lights2_option_critic/
mkdir ../outputs/Attempt8_Lights2_option_critic/Markdown
bsub -o "../outputs/Attempt8_Lights2_option_critic/Markdown/Attempt8_Lights2_option_critic_0.md" -J "Attempt8_Lights2_option_critic_0" -env MYARGS="-name Attempt8_Lights2_option_critic-0 -hours 72.0 -level Levels.Causal4 -main option_critic_run -batch 32 -num 0" < submit_cpu.sh
bsub -o "../outputs/Attempt8_Lights2_option_critic/Markdown/Attempt8_Lights2_option_critic_1.md" -J "Attempt8_Lights2_option_critic_1" -env MYARGS="-name Attempt8_Lights2_option_critic-1 -hours 72.0 -level Levels.Causal4 -main option_critic_run -batch 32 -num 1" < submit_cpu.sh
bsub -o "../outputs/Attempt8_Lights2_option_critic/Markdown/Attempt8_Lights2_option_critic_2.md" -J "Attempt8_Lights2_option_critic_2" -env MYARGS="-name Attempt8_Lights2_option_critic-2 -hours 72.0 -level Levels.Causal4 -main option_critic_run -batch 32 -num 2" < submit_cpu.sh
mkdir ../outputs/Attempt8_Diamonds1_option_critic/
mkdir ../outputs/Attempt8_Diamonds1_option_critic/Markdown
bsub -o "../outputs/Attempt8_Diamonds1_option_critic/Markdown/Attempt8_Diamonds1_option_critic_0.md" -J "Attempt8_Diamonds1_option_critic_0" -env MYARGS="-name Attempt8_Diamonds1_option_critic-0 -hours 72.0 -level Levels.Causal2 -main option_critic_run -batch 32 -num 0" < submit_cpu.sh
bsub -o "../outputs/Attempt8_Diamonds1_option_critic/Markdown/Attempt8_Diamonds1_option_critic_1.md" -J "Attempt8_Diamonds1_option_critic_1" -env MYARGS="-name Attempt8_Diamonds1_option_critic-1 -hours 72.0 -level Levels.Causal2 -main option_critic_run -batch 32 -num 1" < submit_cpu.sh
bsub -o "../outputs/Attempt8_Diamonds1_option_critic/Markdown/Attempt8_Diamonds1_option_critic_2.md" -J "Attempt8_Diamonds1_option_critic_2" -env MYARGS="-name Attempt8_Diamonds1_option_critic-2 -hours 72.0 -level Levels.Causal2 -main option_critic_run -batch 32 -num 2" < submit_cpu.sh
mkdir ../outputs/Attempt8_Diamonds2_option_critic/
mkdir ../outputs/Attempt8_Diamonds2_option_critic/Markdown
bsub -o "../outputs/Attempt8_Diamonds2_option_critic/Markdown/Attempt8_Diamonds2_option_critic_0.md" -J "Attempt8_Diamonds2_option_critic_0" -env MYARGS="-name Attempt8_Diamonds2_option_critic-0 -hours 72.0 -level Levels.Causal5 -main option_critic_run -batch 32 -num 0" < submit_cpu.sh
bsub -o "../outputs/Attempt8_Diamonds2_option_critic/Markdown/Attempt8_Diamonds2_option_critic_1.md" -J "Attempt8_Diamonds2_option_critic_1" -env MYARGS="-name Attempt8_Diamonds2_option_critic-1 -hours 72.0 -level Levels.Causal5 -main option_critic_run -batch 32 -num 1" < submit_cpu.sh
bsub -o "../outputs/Attempt8_Diamonds2_option_critic/Markdown/Attempt8_Diamonds2_option_critic_2.md" -J "Attempt8_Diamonds2_option_critic_2" -env MYARGS="-name Attempt8_Diamonds2_option_critic-2 -hours 72.0 -level Levels.Causal5 -main option_critic_run -batch 32 -num 2" < submit_cpu.sh
mkdir ../outputs/Attempt8_Diamonds3_option_critic/
mkdir ../outputs/Attempt8_Diamonds3_option_critic/Markdown
bsub -o "../outputs/Attempt8_Diamonds3_option_critic/Markdown/Attempt8_Diamonds3_option_critic_0.md" -J "Attempt8_Diamonds3_option_critic_0" -env MYARGS="-name Attempt8_Diamonds3_option_critic-0 -hours 72.0 -level Levels.Causal6 -main option_critic_run -batch 32 -num 0" < submit_cpu.sh
bsub -o "../outputs/Attempt8_Diamonds3_option_critic/Markdown/Attempt8_Diamonds3_option_critic_1.md" -J "Attempt8_Diamonds3_option_critic_1" -env MYARGS="-name Attempt8_Diamonds3_option_critic-1 -hours 72.0 -level Levels.Causal6 -main option_critic_run -batch 32 -num 1" < submit_cpu.sh
bsub -o "../outputs/Attempt8_Diamonds3_option_critic/Markdown/Attempt8_Diamonds3_option_critic_2.md" -J "Attempt8_Diamonds3_option_critic_2" -env MYARGS="-name Attempt8_Diamonds3_option_critic-2 -hours 72.0 -level Levels.Causal6 -main option_critic_run -batch 32 -num 2" < submit_cpu.sh
mkdir ../outputs/Attempt8_Diamonds4_option_critic/
mkdir ../outputs/Attempt8_Diamonds4_option_critic/Markdown
bsub -o "../outputs/Attempt8_Diamonds4_option_critic/Markdown/Attempt8_Diamonds4_option_critic_0.md" -J "Attempt8_Diamonds4_option_critic_0" -env MYARGS="-name Attempt8_Diamonds4_option_critic-0 -hours 72.0 -level Levels.Causal7 -main option_critic_run -batch 32 -num 0" < submit_cpu.sh
bsub -o "../outputs/Attempt8_Diamonds4_option_critic/Markdown/Attempt8_Diamonds4_option_critic_1.md" -J "Attempt8_Diamonds4_option_critic_1" -env MYARGS="-name Attempt8_Diamonds4_option_critic-1 -hours 72.0 -level Levels.Causal7 -main option_critic_run -batch 32 -num 1" < submit_cpu.sh
bsub -o "../outputs/Attempt8_Diamonds4_option_critic/Markdown/Attempt8_Diamonds4_option_critic_2.md" -J "Attempt8_Diamonds4_option_critic_2" -env MYARGS="-name Attempt8_Diamonds4_option_critic-2 -hours 72.0 -level Levels.Causal7 -main option_critic_run -batch 32 -num 2" < submit_cpu.sh
mkdir ../outputs/Attempt8_Maze_option_critic/
mkdir ../outputs/Attempt8_Maze_option_critic/Markdown
bsub -o "../outputs/Attempt8_Maze_option_critic/Markdown/Attempt8_Maze_option_critic_0.md" -J "Attempt8_Maze_option_critic_0" -env MYARGS="-name Attempt8_Maze_option_critic-0 -hours 72.0 -level Levels.Maze -main option_critic_run -batch 32 -num 0" < submit_cpu.sh
bsub -o "../outputs/Attempt8_Maze_option_critic/Markdown/Attempt8_Maze_option_critic_1.md" -J "Attempt8_Maze_option_critic_1" -env MYARGS="-name Attempt8_Maze_option_critic-1 -hours 72.0 -level Levels.Maze -main option_critic_run -batch 32 -num 1" < submit_cpu.sh
bsub -o "../outputs/Attempt8_Maze_option_critic/Markdown/Attempt8_Maze_option_critic_2.md" -J "Attempt8_Maze_option_critic_2" -env MYARGS="-name Attempt8_Maze_option_critic-2 -hours 72.0 -level Levels.Maze -main option_critic_run -batch 32 -num 2" < submit_cpu.sh
mkdir ../outputs/Attempt8_Coconuts_option_critic/
mkdir ../outputs/Attempt8_Coconuts_option_critic/Markdown
bsub -o "../outputs/Attempt8_Coconuts_option_critic/Markdown/Attempt8_Coconuts_option_critic_0.md" -J "Attempt8_Coconuts_option_critic_0" -env MYARGS="-name Attempt8_Coconuts_option_critic-0 -hours 72.0 -level Levels.Coconuts -main option_critic_run -batch 32 -num 0" < submit_cpu.sh
bsub -o "../outputs/Attempt8_Coconuts_option_critic/Markdown/Attempt8_Coconuts_option_critic_1.md" -J "Attempt8_Coconuts_option_critic_1" -env MYARGS="-name Attempt8_Coconuts_option_critic-1 -hours 72.0 -level Levels.Coconuts -main option_critic_run -batch 32 -num 1" < submit_cpu.sh
bsub -o "../outputs/Attempt8_Coconuts_option_critic/Markdown/Attempt8_Coconuts_option_critic_2.md" -J "Attempt8_Coconuts_option_critic_2" -env MYARGS="-name Attempt8_Coconuts_option_critic-2 -hours 72.0 -level Levels.Coconuts -main option_critic_run -batch 32 -num 2" < submit_cpu.sh
mkdir ../outputs/Attempt8_Monsters_option_critic/
mkdir ../outputs/Attempt8_Monsters_option_critic/Markdown
bsub -o "../outputs/Attempt8_Monsters_option_critic/Markdown/Attempt8_Monsters_option_critic_0.md" -J "Attempt8_Monsters_option_critic_0" -env MYARGS="-name Attempt8_Monsters_option_critic-0 -hours 72.0 -level Levels.MonsterLevel -main option_critic_run -batch 32 -num 0" < submit_cpu.sh
bsub -o "../outputs/Attempt8_Monsters_option_critic/Markdown/Attempt8_Monsters_option_critic_1.md" -J "Attempt8_Monsters_option_critic_1" -env MYARGS="-name Attempt8_Monsters_option_critic-1 -hours 72.0 -level Levels.MonsterLevel -main option_critic_run -batch 32 -num 1" < submit_cpu.sh
bsub -o "../outputs/Attempt8_Monsters_option_critic/Markdown/Attempt8_Monsters_option_critic_2.md" -J "Attempt8_Monsters_option_critic_2" -env MYARGS="-name Attempt8_Monsters_option_critic-2 -hours 72.0 -level Levels.MonsterLevel -main option_critic_run -batch 32 -num 2" < submit_cpu.sh
mkdir ../outputs/Attempt8_DoorsAndKey_option_critic/
mkdir ../outputs/Attempt8_DoorsAndKey_option_critic/Markdown
bsub -o "../outputs/Attempt8_DoorsAndKey_option_critic/Markdown/Attempt8_DoorsAndKey_option_critic_0.md" -J "Attempt8_DoorsAndKey_option_critic_0" -env MYARGS="-name Attempt8_DoorsAndKey_option_critic-0 -hours 72.0 -level Levels.Causal1 -main option_critic_run -batch 32 -num 0" < submit_cpu.sh
bsub -o "../outputs/Attempt8_DoorsAndKey_option_critic/Markdown/Attempt8_DoorsAndKey_option_critic_1.md" -J "Attempt8_DoorsAndKey_option_critic_1" -env MYARGS="-name Attempt8_DoorsAndKey_option_critic-1 -hours 72.0 -level Levels.Causal1 -main option_critic_run -batch 32 -num 1" < submit_cpu.sh
bsub -o "../outputs/Attempt8_DoorsAndKey_option_critic/Markdown/Attempt8_DoorsAndKey_option_critic_2.md" -J "Attempt8_DoorsAndKey_option_critic_2" -env MYARGS="-name Attempt8_DoorsAndKey_option_critic-2 -hours 72.0 -level Levels.Causal1 -main option_critic_run -batch 32 -num 2" < submit_cpu.sh
