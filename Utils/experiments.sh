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
mkdir ../outputs/Attempt7_Lights1_option_critic/
mkdir ../outputs/Attempt7_Lights1_option_critic/Markdown
bsub -o "../outputs/Attempt7_Lights1_option_critic/Markdown/Attempt7_Lights1_option_critic_0.md" -J "Attempt7_Lights1_option_critic_0" -env MYARGS="-name Attempt7_Lights1_option_critic-0 -hours 72.0 -level Levels.Causal3 -main option_critic_run -batch 32 -num 0" < submit_cpu.sh
bsub -o "../outputs/Attempt7_Lights1_option_critic/Markdown/Attempt7_Lights1_option_critic_1.md" -J "Attempt7_Lights1_option_critic_1" -env MYARGS="-name Attempt7_Lights1_option_critic-1 -hours 72.0 -level Levels.Causal3 -main option_critic_run -batch 32 -num 1" < submit_cpu.sh
bsub -o "../outputs/Attempt7_Lights1_option_critic/Markdown/Attempt7_Lights1_option_critic_2.md" -J "Attempt7_Lights1_option_critic_2" -env MYARGS="-name Attempt7_Lights1_option_critic-2 -hours 72.0 -level Levels.Causal3 -main option_critic_run -batch 32 -num 2" < submit_cpu.sh
mkdir ../outputs/Attempt7_Lights2_option_critic/
mkdir ../outputs/Attempt7_Lights2_option_critic/Markdown
bsub -o "../outputs/Attempt7_Lights2_option_critic/Markdown/Attempt7_Lights2_option_critic_0.md" -J "Attempt7_Lights2_option_critic_0" -env MYARGS="-name Attempt7_Lights2_option_critic-0 -hours 72.0 -level Levels.Causal4 -main option_critic_run -batch 32 -num 0" < submit_cpu.sh
bsub -o "../outputs/Attempt7_Lights2_option_critic/Markdown/Attempt7_Lights2_option_critic_1.md" -J "Attempt7_Lights2_option_critic_1" -env MYARGS="-name Attempt7_Lights2_option_critic-1 -hours 72.0 -level Levels.Causal4 -main option_critic_run -batch 32 -num 1" < submit_cpu.sh
bsub -o "../outputs/Attempt7_Lights2_option_critic/Markdown/Attempt7_Lights2_option_critic_2.md" -J "Attempt7_Lights2_option_critic_2" -env MYARGS="-name Attempt7_Lights2_option_critic-2 -hours 72.0 -level Levels.Causal4 -main option_critic_run -batch 32 -num 2" < submit_cpu.sh
mkdir ../outputs/Attempt7_Diamonds1_option_critic/
mkdir ../outputs/Attempt7_Diamonds1_option_critic/Markdown
bsub -o "../outputs/Attempt7_Diamonds1_option_critic/Markdown/Attempt7_Diamonds1_option_critic_0.md" -J "Attempt7_Diamonds1_option_critic_0" -env MYARGS="-name Attempt7_Diamonds1_option_critic-0 -hours 72.0 -level Levels.Causal2 -main option_critic_run -batch 32 -num 0" < submit_cpu.sh
bsub -o "../outputs/Attempt7_Diamonds1_option_critic/Markdown/Attempt7_Diamonds1_option_critic_1.md" -J "Attempt7_Diamonds1_option_critic_1" -env MYARGS="-name Attempt7_Diamonds1_option_critic-1 -hours 72.0 -level Levels.Causal2 -main option_critic_run -batch 32 -num 1" < submit_cpu.sh
bsub -o "../outputs/Attempt7_Diamonds1_option_critic/Markdown/Attempt7_Diamonds1_option_critic_2.md" -J "Attempt7_Diamonds1_option_critic_2" -env MYARGS="-name Attempt7_Diamonds1_option_critic-2 -hours 72.0 -level Levels.Causal2 -main option_critic_run -batch 32 -num 2" < submit_cpu.sh
mkdir ../outputs/Attempt7_Diamonds2_option_critic/
mkdir ../outputs/Attempt7_Diamonds2_option_critic/Markdown
bsub -o "../outputs/Attempt7_Diamonds2_option_critic/Markdown/Attempt7_Diamonds2_option_critic_0.md" -J "Attempt7_Diamonds2_option_critic_0" -env MYARGS="-name Attempt7_Diamonds2_option_critic-0 -hours 72.0 -level Levels.Causal5 -main option_critic_run -batch 32 -num 0" < submit_cpu.sh
bsub -o "../outputs/Attempt7_Diamonds2_option_critic/Markdown/Attempt7_Diamonds2_option_critic_1.md" -J "Attempt7_Diamonds2_option_critic_1" -env MYARGS="-name Attempt7_Diamonds2_option_critic-1 -hours 72.0 -level Levels.Causal5 -main option_critic_run -batch 32 -num 1" < submit_cpu.sh
bsub -o "../outputs/Attempt7_Diamonds2_option_critic/Markdown/Attempt7_Diamonds2_option_critic_2.md" -J "Attempt7_Diamonds2_option_critic_2" -env MYARGS="-name Attempt7_Diamonds2_option_critic-2 -hours 72.0 -level Levels.Causal5 -main option_critic_run -batch 32 -num 2" < submit_cpu.sh
mkdir ../outputs/Attempt7_Diamonds3_option_critic/
mkdir ../outputs/Attempt7_Diamonds3_option_critic/Markdown
bsub -o "../outputs/Attempt7_Diamonds3_option_critic/Markdown/Attempt7_Diamonds3_option_critic_0.md" -J "Attempt7_Diamonds3_option_critic_0" -env MYARGS="-name Attempt7_Diamonds3_option_critic-0 -hours 72.0 -level Levels.Causal6 -main option_critic_run -batch 32 -num 0" < submit_cpu.sh
bsub -o "../outputs/Attempt7_Diamonds3_option_critic/Markdown/Attempt7_Diamonds3_option_critic_1.md" -J "Attempt7_Diamonds3_option_critic_1" -env MYARGS="-name Attempt7_Diamonds3_option_critic-1 -hours 72.0 -level Levels.Causal6 -main option_critic_run -batch 32 -num 1" < submit_cpu.sh
bsub -o "../outputs/Attempt7_Diamonds3_option_critic/Markdown/Attempt7_Diamonds3_option_critic_2.md" -J "Attempt7_Diamonds3_option_critic_2" -env MYARGS="-name Attempt7_Diamonds3_option_critic-2 -hours 72.0 -level Levels.Causal6 -main option_critic_run -batch 32 -num 2" < submit_cpu.sh
mkdir ../outputs/Attempt7_Diamonds4_option_critic/
mkdir ../outputs/Attempt7_Diamonds4_option_critic/Markdown
bsub -o "../outputs/Attempt7_Diamonds4_option_critic/Markdown/Attempt7_Diamonds4_option_critic_0.md" -J "Attempt7_Diamonds4_option_critic_0" -env MYARGS="-name Attempt7_Diamonds4_option_critic-0 -hours 72.0 -level Levels.Causal7 -main option_critic_run -batch 32 -num 0" < submit_cpu.sh
bsub -o "../outputs/Attempt7_Diamonds4_option_critic/Markdown/Attempt7_Diamonds4_option_critic_1.md" -J "Attempt7_Diamonds4_option_critic_1" -env MYARGS="-name Attempt7_Diamonds4_option_critic-1 -hours 72.0 -level Levels.Causal7 -main option_critic_run -batch 32 -num 1" < submit_cpu.sh
bsub -o "../outputs/Attempt7_Diamonds4_option_critic/Markdown/Attempt7_Diamonds4_option_critic_2.md" -J "Attempt7_Diamonds4_option_critic_2" -env MYARGS="-name Attempt7_Diamonds4_option_critic-2 -hours 72.0 -level Levels.Causal7 -main option_critic_run -batch 32 -num 2" < submit_cpu.sh
mkdir ../outputs/Attempt7_Maze_option_critic/
mkdir ../outputs/Attempt7_Maze_option_critic/Markdown
bsub -o "../outputs/Attempt7_Maze_option_critic/Markdown/Attempt7_Maze_option_critic_0.md" -J "Attempt7_Maze_option_critic_0" -env MYARGS="-name Attempt7_Maze_option_critic-0 -hours 72.0 -level Levels.Maze -main option_critic_run -batch 32 -num 0" < submit_cpu.sh
bsub -o "../outputs/Attempt7_Maze_option_critic/Markdown/Attempt7_Maze_option_critic_1.md" -J "Attempt7_Maze_option_critic_1" -env MYARGS="-name Attempt7_Maze_option_critic-1 -hours 72.0 -level Levels.Maze -main option_critic_run -batch 32 -num 1" < submit_cpu.sh
bsub -o "../outputs/Attempt7_Maze_option_critic/Markdown/Attempt7_Maze_option_critic_2.md" -J "Attempt7_Maze_option_critic_2" -env MYARGS="-name Attempt7_Maze_option_critic-2 -hours 72.0 -level Levels.Maze -main option_critic_run -batch 32 -num 2" < submit_cpu.sh
mkdir ../outputs/Attempt7_Coconuts_option_critic/
mkdir ../outputs/Attempt7_Coconuts_option_critic/Markdown
bsub -o "../outputs/Attempt7_Coconuts_option_critic/Markdown/Attempt7_Coconuts_option_critic_0.md" -J "Attempt7_Coconuts_option_critic_0" -env MYARGS="-name Attempt7_Coconuts_option_critic-0 -hours 72.0 -level Levels.Coconuts -main option_critic_run -batch 32 -num 0" < submit_cpu.sh
bsub -o "../outputs/Attempt7_Coconuts_option_critic/Markdown/Attempt7_Coconuts_option_critic_1.md" -J "Attempt7_Coconuts_option_critic_1" -env MYARGS="-name Attempt7_Coconuts_option_critic-1 -hours 72.0 -level Levels.Coconuts -main option_critic_run -batch 32 -num 1" < submit_cpu.sh
bsub -o "../outputs/Attempt7_Coconuts_option_critic/Markdown/Attempt7_Coconuts_option_critic_2.md" -J "Attempt7_Coconuts_option_critic_2" -env MYARGS="-name Attempt7_Coconuts_option_critic-2 -hours 72.0 -level Levels.Coconuts -main option_critic_run -batch 32 -num 2" < submit_cpu.sh
mkdir ../outputs/Attempt7_Monsters_option_critic/
mkdir ../outputs/Attempt7_Monsters_option_critic/Markdown
bsub -o "../outputs/Attempt7_Monsters_option_critic/Markdown/Attempt7_Monsters_option_critic_0.md" -J "Attempt7_Monsters_option_critic_0" -env MYARGS="-name Attempt7_Monsters_option_critic-0 -hours 72.0 -level Levels.MonsterLevel -main option_critic_run -batch 32 -num 0" < submit_cpu.sh
bsub -o "../outputs/Attempt7_Monsters_option_critic/Markdown/Attempt7_Monsters_option_critic_1.md" -J "Attempt7_Monsters_option_critic_1" -env MYARGS="-name Attempt7_Monsters_option_critic-1 -hours 72.0 -level Levels.MonsterLevel -main option_critic_run -batch 32 -num 1" < submit_cpu.sh
bsub -o "../outputs/Attempt7_Monsters_option_critic/Markdown/Attempt7_Monsters_option_critic_2.md" -J "Attempt7_Monsters_option_critic_2" -env MYARGS="-name Attempt7_Monsters_option_critic-2 -hours 72.0 -level Levels.MonsterLevel -main option_critic_run -batch 32 -num 2" < submit_cpu.sh
mkdir ../outputs/Attempt7_DoorsAndKey_option_critic/
mkdir ../outputs/Attempt7_DoorsAndKey_option_critic/Markdown
bsub -o "../outputs/Attempt7_DoorsAndKey_option_critic/Markdown/Attempt7_DoorsAndKey_option_critic_0.md" -J "Attempt7_DoorsAndKey_option_critic_0" -env MYARGS="-name Attempt7_DoorsAndKey_option_critic-0 -hours 72.0 -level Levels.Causal1 -main option_critic_run -batch 32 -num 0" < submit_cpu.sh
bsub -o "../outputs/Attempt7_DoorsAndKey_option_critic/Markdown/Attempt7_DoorsAndKey_option_critic_1.md" -J "Attempt7_DoorsAndKey_option_critic_1" -env MYARGS="-name Attempt7_DoorsAndKey_option_critic-1 -hours 72.0 -level Levels.Causal1 -main option_critic_run -batch 32 -num 1" < submit_cpu.sh
bsub -o "../outputs/Attempt7_DoorsAndKey_option_critic/Markdown/Attempt7_DoorsAndKey_option_critic_2.md" -J "Attempt7_DoorsAndKey_option_critic_2" -env MYARGS="-name Attempt7_DoorsAndKey_option_critic-2 -hours 72.0 -level Levels.Causal1 -main option_critic_run -batch 32 -num 2" < submit_cpu.sh
