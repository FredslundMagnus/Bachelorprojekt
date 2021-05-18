#!/bin/sh
mkdir ../outputs/Diamonds1_0.5_NN/
mkdir ../outputs/Diamonds1_0.5_NN/Markdown
bsub -o "../outputs/Diamonds1_0.5_NN/Markdown/Diamonds1_0.5_NN_0.md" -J "Diamonds1_0.5_NN_0" -env MYARGS="-name Diamonds1_0.5_NN-0 -hours 10.0 -level Levels.Causal2 -main graphTrain -K1 200000.0 -K2 100000.0 -softmax_cap 0.0 -failed_actions_chance 0.5 -use_model True -num 0" < submit_gpu.sh
bsub -o "../outputs/Diamonds1_0.5_NN/Markdown/Diamonds1_0.5_NN_1.md" -J "Diamonds1_0.5_NN_1" -env MYARGS="-name Diamonds1_0.5_NN-1 -hours 10.0 -level Levels.Causal2 -main graphTrain -K1 200000.0 -K2 100000.0 -softmax_cap 0.0 -failed_actions_chance 0.5 -use_model True -num 1" < submit_gpu.sh
bsub -o "../outputs/Diamonds1_0.5_NN/Markdown/Diamonds1_0.5_NN_2.md" -J "Diamonds1_0.5_NN_2" -env MYARGS="-name Diamonds1_0.5_NN-2 -hours 10.0 -level Levels.Causal2 -main graphTrain -K1 200000.0 -K2 100000.0 -softmax_cap 0.0 -failed_actions_chance 0.5 -use_model True -num 2" < submit_gpu.sh
mkdir ../outputs/Diamonds2_0.5_NN/
mkdir ../outputs/Diamonds2_0.5_NN/Markdown
bsub -o "../outputs/Diamonds2_0.5_NN/Markdown/Diamonds2_0.5_NN_0.md" -J "Diamonds2_0.5_NN_0" -env MYARGS="-name Diamonds2_0.5_NN-0 -hours 10.0 -level Levels.Causal5 -main graphTrain -K1 200000.0 -K2 100000.0 -softmax_cap 0.0 -failed_actions_chance 0.5 -use_model True -num 0" < submit_gpu.sh
bsub -o "../outputs/Diamonds2_0.5_NN/Markdown/Diamonds2_0.5_NN_1.md" -J "Diamonds2_0.5_NN_1" -env MYARGS="-name Diamonds2_0.5_NN-1 -hours 10.0 -level Levels.Causal5 -main graphTrain -K1 200000.0 -K2 100000.0 -softmax_cap 0.0 -failed_actions_chance 0.5 -use_model True -num 1" < submit_gpu.sh
bsub -o "../outputs/Diamonds2_0.5_NN/Markdown/Diamonds2_0.5_NN_2.md" -J "Diamonds2_0.5_NN_2" -env MYARGS="-name Diamonds2_0.5_NN-2 -hours 10.0 -level Levels.Causal5 -main graphTrain -K1 200000.0 -K2 100000.0 -softmax_cap 0.0 -failed_actions_chance 0.5 -use_model True -num 2" < submit_gpu.sh
mkdir ../outputs/Diamonds3_0.5_NN/
mkdir ../outputs/Diamonds3_0.5_NN/Markdown
bsub -o "../outputs/Diamonds3_0.5_NN/Markdown/Diamonds3_0.5_NN_0.md" -J "Diamonds3_0.5_NN_0" -env MYARGS="-name Diamonds3_0.5_NN-0 -hours 10.0 -level Levels.Causal6 -main graphTrain -K1 200000.0 -K2 100000.0 -softmax_cap 0.0 -failed_actions_chance 0.5 -use_model True -num 0" < submit_gpu.sh
bsub -o "../outputs/Diamonds3_0.5_NN/Markdown/Diamonds3_0.5_NN_1.md" -J "Diamonds3_0.5_NN_1" -env MYARGS="-name Diamonds3_0.5_NN-1 -hours 10.0 -level Levels.Causal6 -main graphTrain -K1 200000.0 -K2 100000.0 -softmax_cap 0.0 -failed_actions_chance 0.5 -use_model True -num 1" < submit_gpu.sh
bsub -o "../outputs/Diamonds3_0.5_NN/Markdown/Diamonds3_0.5_NN_2.md" -J "Diamonds3_0.5_NN_2" -env MYARGS="-name Diamonds3_0.5_NN-2 -hours 10.0 -level Levels.Causal6 -main graphTrain -K1 200000.0 -K2 100000.0 -softmax_cap 0.0 -failed_actions_chance 0.5 -use_model True -num 2" < submit_gpu.sh
mkdir ../outputs/Diamonds4_0.5_NN/
mkdir ../outputs/Diamonds4_0.5_NN/Markdown
bsub -o "../outputs/Diamonds4_0.5_NN/Markdown/Diamonds4_0.5_NN_0.md" -J "Diamonds4_0.5_NN_0" -env MYARGS="-name Diamonds4_0.5_NN-0 -hours 10.0 -level Levels.Causal7 -main graphTrain -K1 200000.0 -K2 100000.0 -softmax_cap 0.0 -failed_actions_chance 0.5 -use_model True -num 0" < submit_gpu.sh
bsub -o "../outputs/Diamonds4_0.5_NN/Markdown/Diamonds4_0.5_NN_1.md" -J "Diamonds4_0.5_NN_1" -env MYARGS="-name Diamonds4_0.5_NN-1 -hours 10.0 -level Levels.Causal7 -main graphTrain -K1 200000.0 -K2 100000.0 -softmax_cap 0.0 -failed_actions_chance 0.5 -use_model True -num 1" < submit_gpu.sh
bsub -o "../outputs/Diamonds4_0.5_NN/Markdown/Diamonds4_0.5_NN_2.md" -J "Diamonds4_0.5_NN_2" -env MYARGS="-name Diamonds4_0.5_NN-2 -hours 10.0 -level Levels.Causal7 -main graphTrain -K1 200000.0 -K2 100000.0 -softmax_cap 0.0 -failed_actions_chance 0.5 -use_model True -num 2" < submit_gpu.sh
