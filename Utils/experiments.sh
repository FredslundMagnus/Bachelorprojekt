#!/bin/sh
mkdir ../outputs/causal2_online_var_0.5_full_UCB1/
mkdir ../outputs/causal2_online_var_0.5_full_UCB1/Markdown
bsub -o "../outputs/causal2_online_var_0.5_full_UCB1/Markdown/causal2_online_var_0.5_full_UCB1_0.md" -J "causal2_online_var_0.5_full_UCB1_0" -P "-name causal2_online_var_0.5_full_UCB1-0 -hours 12.0 -level Levels.Causal2 -main graphTrain -K1 200000.0 -K2 100000.0 -softmax_cap 0.0 -failed_actions_chance 0.5 -graphMode GraphMode.UCB1" < submit.sh
mkdir ../outputs/causal5_online_var_0.5_full_UCB1/
mkdir ../outputs/causal5_online_var_0.5_full_UCB1/Markdown
bsub -o "../outputs/causal5_online_var_0.5_full_UCB1/Markdown/causal5_online_var_0.5_full_UCB1_0.md" -J "causal5_online_var_0.5_full_UCB1_0" -P "-name causal5_online_var_0.5_full_UCB1-0 -hours 12.0 -level Levels.Causal5 -main graphTrain -K1 200000.0 -K2 100000.0 -softmax_cap 0.0 -failed_actions_chance 0.5 -graphMode GraphMode.UCB1" < submit.sh
mkdir ../outputs/causal6_online_var_0.5_full_UCB1/
mkdir ../outputs/causal6_online_var_0.5_full_UCB1/Markdown
bsub -o "../outputs/causal6_online_var_0.5_full_UCB1/Markdown/causal6_online_var_0.5_full_UCB1_0.md" -J "causal6_online_var_0.5_full_UCB1_0" -P "-name causal6_online_var_0.5_full_UCB1-0 -hours 12.0 -level Levels.Causal6 -main graphTrain -K1 200000.0 -K2 100000.0 -softmax_cap 0.0 -failed_actions_chance 0.5 -graphMode GraphMode.UCB1" < submit.sh
mkdir ../outputs/causal7_online_var_0.5_full_UCB1/
mkdir ../outputs/causal7_online_var_0.5_full_UCB1/Markdown
bsub -o "../outputs/causal7_online_var_0.5_full_UCB1/Markdown/causal7_online_var_0.5_full_UCB1_0.md" -J "causal7_online_var_0.5_full_UCB1_0" -P "-name causal7_online_var_0.5_full_UCB1-0 -hours 12.0 -level Levels.Causal7 -main graphTrain -K1 200000.0 -K2 100000.0 -softmax_cap 0.0 -failed_actions_chance 0.5 -graphMode GraphMode.UCB1" < submit.sh
