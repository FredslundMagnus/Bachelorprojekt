#!/bin/sh
mkdir ../outputs/causal2_online/
mkdir ../outputs/causal2_online/Markdown
bsub -o "../outputs/causal2_online/Markdown/causal2_online_0.md" -J "causal2_online_0" -P "-name causal2_online-0 -hours 12.0 -level Levels.Causal2 -main graphTrain -K1 200000.0 -K2 100000.0 -softmax_cap 0.0" < submit.sh
mkdir ../outputs/causal5_online/
mkdir ../outputs/causal5_online/Markdown
bsub -o "../outputs/causal5_online/Markdown/causal5_online_0.md" -J "causal5_online_0" -P "-name causal5_online-0 -hours 12.0 -level Levels.Causal5 -main graphTrain -K1 200000.0 -K2 100000.0 -softmax_cap 0.0" < submit.sh
mkdir ../outputs/causal6_online/
mkdir ../outputs/causal6_online/Markdown
bsub -o "../outputs/causal6_online/Markdown/causal6_online_0.md" -J "causal6_online_0" -P "-name causal6_online-0 -hours 12.0 -level Levels.Causal6 -main graphTrain -K1 200000.0 -K2 100000.0 -softmax_cap 0.0" < submit.sh
mkdir ../outputs/causal7_online/
mkdir ../outputs/causal7_online/Markdown
bsub -o "../outputs/causal7_online/Markdown/causal7_online_0.md" -J "causal7_online_0" -P "-name causal7_online-0 -hours 12.0 -level Levels.Causal7 -main graphTrain -K1 200000.0 -K2 100000.0 -softmax_cap 0.0" < submit.sh
