#!/bin/sh
mkdir ../outputs/Diamonds1_0.5_var/
mkdir ../outputs/Diamonds1_0.5_var/Markdown
bsub -o "../outputs/Diamonds1_0.5_var/Markdown/Diamonds1_0.5_var_0.md" -J "Diamonds1_0.5_var_0" -P "-name Diamonds1_0.5_var-0 -hours 10.0 -level Levels.Causal2 -main graphTrain -K1 200000.0 -K2 100000.0 -softmax_cap 0.0 -failed_actions_chance 0.5 -graphMode GraphMode.var" < submit.sh
bsub -o "../outputs/Diamonds1_0.5_var/Markdown/Diamonds1_0.5_var_1.md" -J "Diamonds1_0.5_var_1" -P "-name Diamonds1_0.5_var-1 -hours 10.0 -level Levels.Causal2 -main graphTrain -K1 200000.0 -K2 100000.0 -softmax_cap 0.0 -failed_actions_chance 0.5 -graphMode GraphMode.var" < submit.sh
bsub -o "../outputs/Diamonds1_0.5_var/Markdown/Diamonds1_0.5_var_2.md" -J "Diamonds1_0.5_var_2" -P "-name Diamonds1_0.5_var-2 -hours 10.0 -level Levels.Causal2 -main graphTrain -K1 200000.0 -K2 100000.0 -softmax_cap 0.0 -failed_actions_chance 0.5 -graphMode GraphMode.var" < submit.sh
mkdir ../outputs/Diamonds2_0.5_var/
mkdir ../outputs/Diamonds2_0.5_var/Markdown
bsub -o "../outputs/Diamonds2_0.5_var/Markdown/Diamonds2_0.5_var_0.md" -J "Diamonds2_0.5_var_0" -P "-name Diamonds2_0.5_var-0 -hours 10.0 -level Levels.Causal5 -main graphTrain -K1 200000.0 -K2 100000.0 -softmax_cap 0.0 -failed_actions_chance 0.5 -graphMode GraphMode.var" < submit.sh
bsub -o "../outputs/Diamonds2_0.5_var/Markdown/Diamonds2_0.5_var_1.md" -J "Diamonds2_0.5_var_1" -P "-name Diamonds2_0.5_var-1 -hours 10.0 -level Levels.Causal5 -main graphTrain -K1 200000.0 -K2 100000.0 -softmax_cap 0.0 -failed_actions_chance 0.5 -graphMode GraphMode.var" < submit.sh
bsub -o "../outputs/Diamonds2_0.5_var/Markdown/Diamonds2_0.5_var_2.md" -J "Diamonds2_0.5_var_2" -P "-name Diamonds2_0.5_var-2 -hours 10.0 -level Levels.Causal5 -main graphTrain -K1 200000.0 -K2 100000.0 -softmax_cap 0.0 -failed_actions_chance 0.5 -graphMode GraphMode.var" < submit.sh
mkdir ../outputs/Diamonds3_0.5_var/
mkdir ../outputs/Diamonds3_0.5_var/Markdown
bsub -o "../outputs/Diamonds3_0.5_var/Markdown/Diamonds3_0.5_var_0.md" -J "Diamonds3_0.5_var_0" -P "-name Diamonds3_0.5_var-0 -hours 10.0 -level Levels.Causal6 -main graphTrain -K1 200000.0 -K2 100000.0 -softmax_cap 0.0 -failed_actions_chance 0.5 -graphMode GraphMode.var" < submit.sh
bsub -o "../outputs/Diamonds3_0.5_var/Markdown/Diamonds3_0.5_var_1.md" -J "Diamonds3_0.5_var_1" -P "-name Diamonds3_0.5_var-1 -hours 10.0 -level Levels.Causal6 -main graphTrain -K1 200000.0 -K2 100000.0 -softmax_cap 0.0 -failed_actions_chance 0.5 -graphMode GraphMode.var" < submit.sh
bsub -o "../outputs/Diamonds3_0.5_var/Markdown/Diamonds3_0.5_var_2.md" -J "Diamonds3_0.5_var_2" -P "-name Diamonds3_0.5_var-2 -hours 10.0 -level Levels.Causal6 -main graphTrain -K1 200000.0 -K2 100000.0 -softmax_cap 0.0 -failed_actions_chance 0.5 -graphMode GraphMode.var" < submit.sh
mkdir ../outputs/Diamonds4_0.5_var/
mkdir ../outputs/Diamonds4_0.5_var/Markdown
bsub -o "../outputs/Diamonds4_0.5_var/Markdown/Diamonds4_0.5_var_0.md" -J "Diamonds4_0.5_var_0" -P "-name Diamonds4_0.5_var-0 -hours 10.0 -level Levels.Causal7 -main graphTrain -K1 200000.0 -K2 100000.0 -softmax_cap 0.0 -failed_actions_chance 0.5 -graphMode GraphMode.var" < submit.sh
bsub -o "../outputs/Diamonds4_0.5_var/Markdown/Diamonds4_0.5_var_1.md" -J "Diamonds4_0.5_var_1" -P "-name Diamonds4_0.5_var-1 -hours 10.0 -level Levels.Causal7 -main graphTrain -K1 200000.0 -K2 100000.0 -softmax_cap 0.0 -failed_actions_chance 0.5 -graphMode GraphMode.var" < submit.sh
bsub -o "../outputs/Diamonds4_0.5_var/Markdown/Diamonds4_0.5_var_2.md" -J "Diamonds4_0.5_var_2" -P "-name Diamonds4_0.5_var-2 -hours 10.0 -level Levels.Causal7 -main graphTrain -K1 200000.0 -K2 100000.0 -softmax_cap 0.0 -failed_actions_chance 0.5 -graphMode GraphMode.var" < submit.sh
mkdir ../outputs/Diamonds1_0.0_UCB1/
mkdir ../outputs/Diamonds1_0.0_UCB1/Markdown
bsub -o "../outputs/Diamonds1_0.0_UCB1/Markdown/Diamonds1_0.0_UCB1_0.md" -J "Diamonds1_0.0_UCB1_0" -P "-name Diamonds1_0.0_UCB1-0 -hours 10.0 -level Levels.Causal2 -main graphTrain -K1 200000.0 -K2 100000.0 -softmax_cap 0.0 -failed_actions_chance 0.0 -graphMode GraphMode.UCB1" < submit.sh
bsub -o "../outputs/Diamonds1_0.0_UCB1/Markdown/Diamonds1_0.0_UCB1_1.md" -J "Diamonds1_0.0_UCB1_1" -P "-name Diamonds1_0.0_UCB1-1 -hours 10.0 -level Levels.Causal2 -main graphTrain -K1 200000.0 -K2 100000.0 -softmax_cap 0.0 -failed_actions_chance 0.0 -graphMode GraphMode.UCB1" < submit.sh
bsub -o "../outputs/Diamonds1_0.0_UCB1/Markdown/Diamonds1_0.0_UCB1_2.md" -J "Diamonds1_0.0_UCB1_2" -P "-name Diamonds1_0.0_UCB1-2 -hours 10.0 -level Levels.Causal2 -main graphTrain -K1 200000.0 -K2 100000.0 -softmax_cap 0.0 -failed_actions_chance 0.0 -graphMode GraphMode.UCB1" < submit.sh
mkdir ../outputs/Diamonds2_0.0_UCB1/
mkdir ../outputs/Diamonds2_0.0_UCB1/Markdown
bsub -o "../outputs/Diamonds2_0.0_UCB1/Markdown/Diamonds2_0.0_UCB1_0.md" -J "Diamonds2_0.0_UCB1_0" -P "-name Diamonds2_0.0_UCB1-0 -hours 10.0 -level Levels.Causal5 -main graphTrain -K1 200000.0 -K2 100000.0 -softmax_cap 0.0 -failed_actions_chance 0.0 -graphMode GraphMode.UCB1" < submit.sh
bsub -o "../outputs/Diamonds2_0.0_UCB1/Markdown/Diamonds2_0.0_UCB1_1.md" -J "Diamonds2_0.0_UCB1_1" -P "-name Diamonds2_0.0_UCB1-1 -hours 10.0 -level Levels.Causal5 -main graphTrain -K1 200000.0 -K2 100000.0 -softmax_cap 0.0 -failed_actions_chance 0.0 -graphMode GraphMode.UCB1" < submit.sh
bsub -o "../outputs/Diamonds2_0.0_UCB1/Markdown/Diamonds2_0.0_UCB1_2.md" -J "Diamonds2_0.0_UCB1_2" -P "-name Diamonds2_0.0_UCB1-2 -hours 10.0 -level Levels.Causal5 -main graphTrain -K1 200000.0 -K2 100000.0 -softmax_cap 0.0 -failed_actions_chance 0.0 -graphMode GraphMode.UCB1" < submit.sh
mkdir ../outputs/Diamonds3_0.0_UCB1/
mkdir ../outputs/Diamonds3_0.0_UCB1/Markdown
bsub -o "../outputs/Diamonds3_0.0_UCB1/Markdown/Diamonds3_0.0_UCB1_0.md" -J "Diamonds3_0.0_UCB1_0" -P "-name Diamonds3_0.0_UCB1-0 -hours 10.0 -level Levels.Causal6 -main graphTrain -K1 200000.0 -K2 100000.0 -softmax_cap 0.0 -failed_actions_chance 0.0 -graphMode GraphMode.UCB1" < submit.sh
bsub -o "../outputs/Diamonds3_0.0_UCB1/Markdown/Diamonds3_0.0_UCB1_1.md" -J "Diamonds3_0.0_UCB1_1" -P "-name Diamonds3_0.0_UCB1-1 -hours 10.0 -level Levels.Causal6 -main graphTrain -K1 200000.0 -K2 100000.0 -softmax_cap 0.0 -failed_actions_chance 0.0 -graphMode GraphMode.UCB1" < submit.sh
bsub -o "../outputs/Diamonds3_0.0_UCB1/Markdown/Diamonds3_0.0_UCB1_2.md" -J "Diamonds3_0.0_UCB1_2" -P "-name Diamonds3_0.0_UCB1-2 -hours 10.0 -level Levels.Causal6 -main graphTrain -K1 200000.0 -K2 100000.0 -softmax_cap 0.0 -failed_actions_chance 0.0 -graphMode GraphMode.UCB1" < submit.sh
mkdir ../outputs/Diamonds4_0.0_UCB1/
mkdir ../outputs/Diamonds4_0.0_UCB1/Markdown
bsub -o "../outputs/Diamonds4_0.0_UCB1/Markdown/Diamonds4_0.0_UCB1_0.md" -J "Diamonds4_0.0_UCB1_0" -P "-name Diamonds4_0.0_UCB1-0 -hours 10.0 -level Levels.Causal7 -main graphTrain -K1 200000.0 -K2 100000.0 -softmax_cap 0.0 -failed_actions_chance 0.0 -graphMode GraphMode.UCB1" < submit.sh
bsub -o "../outputs/Diamonds4_0.0_UCB1/Markdown/Diamonds4_0.0_UCB1_1.md" -J "Diamonds4_0.0_UCB1_1" -P "-name Diamonds4_0.0_UCB1-1 -hours 10.0 -level Levels.Causal7 -main graphTrain -K1 200000.0 -K2 100000.0 -softmax_cap 0.0 -failed_actions_chance 0.0 -graphMode GraphMode.UCB1" < submit.sh
bsub -o "../outputs/Diamonds4_0.0_UCB1/Markdown/Diamonds4_0.0_UCB1_2.md" -J "Diamonds4_0.0_UCB1_2" -P "-name Diamonds4_0.0_UCB1-2 -hours 10.0 -level Levels.Causal7 -main graphTrain -K1 200000.0 -K2 100000.0 -softmax_cap 0.0 -failed_actions_chance 0.0 -graphMode GraphMode.UCB1" < submit.sh
mkdir ../outputs/Diamonds1_0.0_var/
mkdir ../outputs/Diamonds1_0.0_var/Markdown
bsub -o "../outputs/Diamonds1_0.0_var/Markdown/Diamonds1_0.0_var_0.md" -J "Diamonds1_0.0_var_0" -P "-name Diamonds1_0.0_var-0 -hours 10.0 -level Levels.Causal2 -main graphTrain -K1 200000.0 -K2 100000.0 -softmax_cap 0.0 -failed_actions_chance 0.0 -graphMode GraphMode.var" < submit.sh
bsub -o "../outputs/Diamonds1_0.0_var/Markdown/Diamonds1_0.0_var_1.md" -J "Diamonds1_0.0_var_1" -P "-name Diamonds1_0.0_var-1 -hours 10.0 -level Levels.Causal2 -main graphTrain -K1 200000.0 -K2 100000.0 -softmax_cap 0.0 -failed_actions_chance 0.0 -graphMode GraphMode.var" < submit.sh
bsub -o "../outputs/Diamonds1_0.0_var/Markdown/Diamonds1_0.0_var_2.md" -J "Diamonds1_0.0_var_2" -P "-name Diamonds1_0.0_var-2 -hours 10.0 -level Levels.Causal2 -main graphTrain -K1 200000.0 -K2 100000.0 -softmax_cap 0.0 -failed_actions_chance 0.0 -graphMode GraphMode.var" < submit.sh
mkdir ../outputs/Diamonds2_0.0_var/
mkdir ../outputs/Diamonds2_0.0_var/Markdown
bsub -o "../outputs/Diamonds2_0.0_var/Markdown/Diamonds2_0.0_var_0.md" -J "Diamonds2_0.0_var_0" -P "-name Diamonds2_0.0_var-0 -hours 10.0 -level Levels.Causal5 -main graphTrain -K1 200000.0 -K2 100000.0 -softmax_cap 0.0 -failed_actions_chance 0.0 -graphMode GraphMode.var" < submit.sh
bsub -o "../outputs/Diamonds2_0.0_var/Markdown/Diamonds2_0.0_var_1.md" -J "Diamonds2_0.0_var_1" -P "-name Diamonds2_0.0_var-1 -hours 10.0 -level Levels.Causal5 -main graphTrain -K1 200000.0 -K2 100000.0 -softmax_cap 0.0 -failed_actions_chance 0.0 -graphMode GraphMode.var" < submit.sh
bsub -o "../outputs/Diamonds2_0.0_var/Markdown/Diamonds2_0.0_var_2.md" -J "Diamonds2_0.0_var_2" -P "-name Diamonds2_0.0_var-2 -hours 10.0 -level Levels.Causal5 -main graphTrain -K1 200000.0 -K2 100000.0 -softmax_cap 0.0 -failed_actions_chance 0.0 -graphMode GraphMode.var" < submit.sh
mkdir ../outputs/Diamonds3_0.0_var/
mkdir ../outputs/Diamonds3_0.0_var/Markdown
bsub -o "../outputs/Diamonds3_0.0_var/Markdown/Diamonds3_0.0_var_0.md" -J "Diamonds3_0.0_var_0" -P "-name Diamonds3_0.0_var-0 -hours 10.0 -level Levels.Causal6 -main graphTrain -K1 200000.0 -K2 100000.0 -softmax_cap 0.0 -failed_actions_chance 0.0 -graphMode GraphMode.var" < submit.sh
bsub -o "../outputs/Diamonds3_0.0_var/Markdown/Diamonds3_0.0_var_1.md" -J "Diamonds3_0.0_var_1" -P "-name Diamonds3_0.0_var-1 -hours 10.0 -level Levels.Causal6 -main graphTrain -K1 200000.0 -K2 100000.0 -softmax_cap 0.0 -failed_actions_chance 0.0 -graphMode GraphMode.var" < submit.sh
bsub -o "../outputs/Diamonds3_0.0_var/Markdown/Diamonds3_0.0_var_2.md" -J "Diamonds3_0.0_var_2" -P "-name Diamonds3_0.0_var-2 -hours 10.0 -level Levels.Causal6 -main graphTrain -K1 200000.0 -K2 100000.0 -softmax_cap 0.0 -failed_actions_chance 0.0 -graphMode GraphMode.var" < submit.sh
mkdir ../outputs/Diamonds4_0.0_var/
mkdir ../outputs/Diamonds4_0.0_var/Markdown
bsub -o "../outputs/Diamonds4_0.0_var/Markdown/Diamonds4_0.0_var_0.md" -J "Diamonds4_0.0_var_0" -P "-name Diamonds4_0.0_var-0 -hours 10.0 -level Levels.Causal7 -main graphTrain -K1 200000.0 -K2 100000.0 -softmax_cap 0.0 -failed_actions_chance 0.0 -graphMode GraphMode.var" < submit.sh
bsub -o "../outputs/Diamonds4_0.0_var/Markdown/Diamonds4_0.0_var_1.md" -J "Diamonds4_0.0_var_1" -P "-name Diamonds4_0.0_var-1 -hours 10.0 -level Levels.Causal7 -main graphTrain -K1 200000.0 -K2 100000.0 -softmax_cap 0.0 -failed_actions_chance 0.0 -graphMode GraphMode.var" < submit.sh
bsub -o "../outputs/Diamonds4_0.0_var/Markdown/Diamonds4_0.0_var_2.md" -J "Diamonds4_0.0_var_2" -P "-name Diamonds4_0.0_var-2 -hours 10.0 -level Levels.Causal7 -main graphTrain -K1 200000.0 -K2 100000.0 -softmax_cap 0.0 -failed_actions_chance 0.0 -graphMode GraphMode.var" < submit.sh
