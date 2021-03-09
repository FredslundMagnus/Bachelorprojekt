#!/bin/sh
mkdir ../outputs/9x9_gamme0.99_eps_intervention/
mkdir ../outputs/9x9_gamme0.99_eps_intervention/Markdown
bsub -o "../outputs/9x9_gamme0.99_eps_intervention/Markdown/9x9_gamme0.99_eps_intervention_0.md" -J "9x9_gamme0.99_eps_intervention_0" -P "-name 9x9_gamme0.99_eps_intervention-0 -hours 10.0 -width 9 -height 9 -layer_Keys True -layer_Door True -layer_Holder True -layer_Putter True -layer_Gold True -gamma 0.99 -exploration1 Explorations.epsilonGreedy" < submit.sh
mkdir ../outputs/9x9_gamme0.95/
mkdir ../outputs/9x9_gamme0.95/Markdown
bsub -o "../outputs/9x9_gamme0.95/Markdown/9x9_gamme0.95_0.md" -J "9x9_gamme0.95_0" -P "-name 9x9_gamme0.95-0 -hours 10.0 -width 9 -height 9 -layer_Keys True -layer_Door True -layer_Holder True -layer_Putter True -layer_Gold True -gamma 0.95" < submit.sh
mkdir ../outputs/9x9_gamme0.99/
mkdir ../outputs/9x9_gamme0.99/Markdown
bsub -o "../outputs/9x9_gamme0.99/Markdown/9x9_gamme0.99_0.md" -J "9x9_gamme0.99_0" -P "-name 9x9_gamme0.99-0 -hours 10.0 -width 9 -height 9 -layer_Keys True -layer_Door True -layer_Holder True -layer_Putter True -layer_Gold True -gamma 0.99" < submit.sh
mkdir ../outputs/9x9_gamme0.995/
mkdir ../outputs/9x9_gamme0.995/Markdown
bsub -o "../outputs/9x9_gamme0.995/Markdown/9x9_gamme0.995_0.md" -J "9x9_gamme0.995_0" -P "-name 9x9_gamme0.995-0 -hours 10.0 -width 9 -height 9 -layer_Keys True -layer_Door True -layer_Holder True -layer_Putter True -layer_Gold True -gamma 0.995" < submit.sh
mkdir ../outputs/9x9_gamme0.99_softmax0.05/
mkdir ../outputs/9x9_gamme0.99_softmax0.05/Markdown
bsub -o "../outputs/9x9_gamme0.99_softmax0.05/Markdown/9x9_gamme0.99_softmax0.05_0.md" -J "9x9_gamme0.99_softmax0.05_0" -P "-name 9x9_gamme0.99_softmax0.05-0 -hours 10.0 -width 9 -height 9 -layer_Keys True -layer_Door True -layer_Holder True -layer_Putter True -layer_Gold True -gamma 0.95 -softmax_cap 0.05" < submit.sh
mkdir ../outputs/9x9_gamme0.99_softmax0.05/
mkdir ../outputs/9x9_gamme0.99_softmax0.05/Markdown
bsub -o "../outputs/9x9_gamme0.99_softmax0.05/Markdown/9x9_gamme0.99_softmax0.05_0.md" -J "9x9_gamme0.99_softmax0.05_0" -P "-name 9x9_gamme0.99_softmax0.05-0 -hours 10.0 -width 9 -height 9 -layer_Keys True -layer_Door True -layer_Holder True -layer_Putter True -layer_Gold True -gamma 0.99 -softmax_cap 0.05" < submit.sh
mkdir ../outputs/9x9_gamme0.995_softmax0.05/
mkdir ../outputs/9x9_gamme0.995_softmax0.05/Markdown
bsub -o "../outputs/9x9_gamme0.995_softmax0.05/Markdown/9x9_gamme0.995_softmax0.05_0.md" -J "9x9_gamme0.995_softmax0.05_0" -P "-name 9x9_gamme0.995_softmax0.05-0 -hours 10.0 -width 9 -height 9 -layer_Keys True -layer_Door True -layer_Holder True -layer_Putter True -layer_Gold True -gamma 0.995 -softmax_cap 0.05" < submit.sh
