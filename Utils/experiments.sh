#!/bin/sh
mkdir ../outputs/9x9_K_100000/
mkdir ../outputs/9x9_K_100000/Markdown
bsub -o "../outputs/9x9_K_100000/Markdown/9x9_K_100000_0.md" -J "9x9_K_100000_0" -P "-name 9x9_K_100000-0 -hours 10.0 -width 9 -height 9 -layer_Keys True -layer_Door True -layer_Holder True -layer_Putter True -layer_Gold True -K 100000.0" < submit.sh
mkdir ../outputs/9x9_K_500000/
mkdir ../outputs/9x9_K_500000/Markdown
bsub -o "../outputs/9x9_K_500000/Markdown/9x9_K_500000_0.md" -J "9x9_K_500000_0" -P "-name 9x9_K_500000-0 -hours 10.0 -width 9 -height 9 -layer_Keys True -layer_Door True -layer_Holder True -layer_Putter True -layer_Gold True -K 500000.0" < submit.sh
mkdir ../outputs/9x9_K_100000_epsilon_cap_0.1/
mkdir ../outputs/9x9_K_100000_epsilon_cap_0.1/Markdown
bsub -o "../outputs/9x9_K_100000_epsilon_cap_0.1/Markdown/9x9_K_100000_epsilon_cap_0.1_0.md" -J "9x9_K_100000_epsilon_cap_0.1_0" -P "-name 9x9_K_100000_epsilon_cap_0.1-0 -hours 10.0 -width 9 -height 9 -layer_Keys True -layer_Door True -layer_Holder True -layer_Putter True -layer_Gold True -K 100000.0 -epsilon_cap 0.1" < submit.sh
mkdir ../outputs/9x9_K_500000_epsilon_cap_0.1/
mkdir ../outputs/9x9_K_500000_epsilon_cap_0.1/Markdown
bsub -o "../outputs/9x9_K_500000_epsilon_cap_0.1/Markdown/9x9_K_500000_epsilon_cap_0.1_0.md" -J "9x9_K_500000_epsilon_cap_0.1_0" -P "-name 9x9_K_500000_epsilon_cap_0.1-0 -hours 10.0 -width 9 -height 9 -layer_Keys True -layer_Door True -layer_Holder True -layer_Putter True -layer_Gold True -K 500000.0 -epsilon_cap 0.1" < submit.sh
mkdir ../outputs/9x9_K_100000_epsilon_cap_0/
mkdir ../outputs/9x9_K_100000_epsilon_cap_0/Markdown
bsub -o "../outputs/9x9_K_100000_epsilon_cap_0/Markdown/9x9_K_100000_epsilon_cap_0_0.md" -J "9x9_K_100000_epsilon_cap_0_0" -P "-name 9x9_K_100000_epsilon_cap_0-0 -hours 10.0 -width 9 -height 9 -layer_Keys True -layer_Door True -layer_Holder True -layer_Putter True -layer_Gold True -K 100000.0 -epsilon_cap 0.0" < submit.sh
mkdir ../outputs/9x9_K_500000_epsilon_cap_0/
mkdir ../outputs/9x9_K_500000_epsilon_cap_0/Markdown
bsub -o "../outputs/9x9_K_500000_epsilon_cap_0/Markdown/9x9_K_500000_epsilon_cap_0_0.md" -J "9x9_K_500000_epsilon_cap_0_0" -P "-name 9x9_K_500000_epsilon_cap_0-0 -hours 10.0 -width 9 -height 9 -layer_Keys True -layer_Door True -layer_Holder True -layer_Putter True -layer_Gold True -K 500000.0 -epsilon_cap 0.0" < submit.sh
