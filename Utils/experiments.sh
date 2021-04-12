#!/bin/sh
mkdir ../outputs/causal7_online_var_0.5/
mkdir ../outputs/causal7_online_var_0.5/Markdown
bsub -o "../outputs/causal7_online_var_0.5/Markdown/causal7_online_var_0.5_0.md" -J "causal7_online_var_0.5_0" -P "-name causal7_online_var_0.5-0 -hours 12.0 -level Levels.Causal7 -main graphTrain -K1 200000.0 -K2 100000.0 -softmax_cap 0.0 -failed_actions_chance 0.5" < submit.sh
