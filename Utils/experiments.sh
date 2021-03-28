#!/bin/sh
mkdir ../outputs/causal1_good_24h/
mkdir ../outputs/causal1_good_24h/Markdown
bsub -o "../outputs/causal1_good_24h/Markdown/causal1_good_24h_0.md" -J "causal1_good_24h_0" -P "-name causal1_good_24h-0 -hours 24.0 -level Levels.Causal1 -layer_Blocks True -layer_Goal True -layer_Gold True -layer_Keys True -layer_Door True -layer_Holder False -layer_Putter False -layer_Rock False -layer_Dirt False -layer_Diamond1 False -layer_Diamond2 False -layer_Diamond3 False -layer_Diamond4 False -layer_Reddoors False -layer_Redkeys False -layer_Bluedoors False -layer_Bluekeys False" < submit.sh
bsub -o "../outputs/causal1_good_24h/Markdown/causal1_good_24h_1.md" -J "causal1_good_24h_1" -P "-name causal1_good_24h-1 -hours 24.0 -level Levels.Causal1 -layer_Blocks True -layer_Goal True -layer_Gold True -layer_Keys True -layer_Door True -layer_Holder False -layer_Putter False -layer_Rock False -layer_Dirt False -layer_Diamond1 False -layer_Diamond2 False -layer_Diamond3 False -layer_Diamond4 False -layer_Reddoors False -layer_Redkeys False -layer_Bluedoors False -layer_Bluekeys False" < submit.sh
bsub -o "../outputs/causal1_good_24h/Markdown/causal1_good_24h_2.md" -J "causal1_good_24h_2" -P "-name causal1_good_24h-2 -hours 24.0 -level Levels.Causal1 -layer_Blocks True -layer_Goal True -layer_Gold True -layer_Keys True -layer_Door True -layer_Holder False -layer_Putter False -layer_Rock False -layer_Dirt False -layer_Diamond1 False -layer_Diamond2 False -layer_Diamond3 False -layer_Diamond4 False -layer_Reddoors False -layer_Redkeys False -layer_Bluedoors False -layer_Bluekeys False" < submit.sh
mkdir ../outputs/causal2_good_24h/
mkdir ../outputs/causal2_good_24h/Markdown
bsub -o "../outputs/causal2_good_24h/Markdown/causal2_good_24h_0.md" -J "causal2_good_24h_0" -P "-name causal2_good_24h-0 -hours 24.0 -level Levels.Causal2 -layer_Blocks False -layer_Goal True -layer_Gold False -layer_Keys False -layer_Door False -layer_Holder False -layer_Putter False -layer_Rock False -layer_Dirt False -layer_Diamond1 True -layer_Diamond2 True -layer_Diamond3 True -layer_Diamond4 True -layer_Reddoors False -layer_Redkeys False -layer_Bluedoors False -layer_Bluekeys False" < submit.sh
bsub -o "../outputs/causal2_good_24h/Markdown/causal2_good_24h_1.md" -J "causal2_good_24h_1" -P "-name causal2_good_24h-1 -hours 24.0 -level Levels.Causal2 -layer_Blocks False -layer_Goal True -layer_Gold False -layer_Keys False -layer_Door False -layer_Holder False -layer_Putter False -layer_Rock False -layer_Dirt False -layer_Diamond1 True -layer_Diamond2 True -layer_Diamond3 True -layer_Diamond4 True -layer_Reddoors False -layer_Redkeys False -layer_Bluedoors False -layer_Bluekeys False" < submit.sh
bsub -o "../outputs/causal2_good_24h/Markdown/causal2_good_24h_2.md" -J "causal2_good_24h_2" -P "-name causal2_good_24h-2 -hours 24.0 -level Levels.Causal2 -layer_Blocks False -layer_Goal True -layer_Gold False -layer_Keys False -layer_Door False -layer_Holder False -layer_Putter False -layer_Rock False -layer_Dirt False -layer_Diamond1 True -layer_Diamond2 True -layer_Diamond3 True -layer_Diamond4 True -layer_Reddoors False -layer_Redkeys False -layer_Bluedoors False -layer_Bluekeys False" < submit.sh
