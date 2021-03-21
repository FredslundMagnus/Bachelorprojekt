#!/bin/sh
mkdir ../outputs/Rock_level_hard/
mkdir ../outputs/Rock_level_hard/Markdown
bsub -o "../outputs/Rock_level_hard/Markdown/Rock_level_hard_0.md" -J "Rock_level_hard_0" -P "-name Rock_level_hard-0 -hours 11.0 -level Levels.Rocks" < submit.sh
mkdir ../outputs/Rock_level_hard_Klow/
mkdir ../outputs/Rock_level_hard_Klow/Markdown
bsub -o "../outputs/Rock_level_hard_Klow/Markdown/Rock_level_hard_Klow_0.md" -J "Rock_level_hard_Klow_0" -P "-name Rock_level_hard_Klow-0 -hours 11.0 -level Levels.Rocks -K 10000.0" < submit.sh
mkdir ../outputs/Rock_level_hard_Khigh/
mkdir ../outputs/Rock_level_hard_Khigh/Markdown
bsub -o "../outputs/Rock_level_hard_Khigh/Markdown/Rock_level_hard_Khigh_0.md" -J "Rock_level_hard_Khigh_0" -P "-name Rock_level_hard_Khigh-0 -hours 11.0 -level Levels.Rocks -K 1000000.0" < submit.sh
mkdir ../outputs/Rock_level_hard_epshigh/
mkdir ../outputs/Rock_level_hard_epshigh/Markdown
bsub -o "../outputs/Rock_level_hard_epshigh/Markdown/Rock_level_hard_epshigh_0.md" -J "Rock_level_hard_epshigh_0" -P "-name Rock_level_hard_epshigh-0 -hours 11.0 -level Levels.Rocks -epsilon_cap 0.2" < submit.sh
mkdir ../outputs/Rock_level_hard_epslow/
mkdir ../outputs/Rock_level_hard_epslow/Markdown
bsub -o "../outputs/Rock_level_hard_epslow/Markdown/Rock_level_hard_epslow_0.md" -J "Rock_level_hard_epslow_0" -P "-name Rock_level_hard_epslow-0 -hours 11.0 -level Levels.Rocks -epsilon_cap 0.0" < submit.sh
mkdir ../outputs/Rock_level_hard_softhigh/
mkdir ../outputs/Rock_level_hard_softhigh/Markdown
bsub -o "../outputs/Rock_level_hard_softhigh/Markdown/Rock_level_hard_softhigh_0.md" -J "Rock_level_hard_softhigh_0" -P "-name Rock_level_hard_softhigh-0 -hours 11.0 -level Levels.Rocks -softmax_cap 0.05" < submit.sh
mkdir ../outputs/Rock_level_hard_softlow/
mkdir ../outputs/Rock_level_hard_softlow/Markdown
bsub -o "../outputs/Rock_level_hard_softlow/Markdown/Rock_level_hard_softlow_0.md" -J "Rock_level_hard_softlow_0" -P "-name Rock_level_hard_softlow-0 -hours 11.0 -level Levels.Rocks -softmax_cap 0.01" < submit.sh
mkdir ../outputs/Rock_level_hard_gammalow/
mkdir ../outputs/Rock_level_hard_gammalow/Markdown
bsub -o "../outputs/Rock_level_hard_gammalow/Markdown/Rock_level_hard_gammalow_0.md" -J "Rock_level_hard_gammalow_0" -P "-name Rock_level_hard_gammalow-0 -hours 11.0 -level Levels.Rocks -gamma 0.95" < submit.sh
mkdir ../outputs/Rock_level_hard_resethigh/
mkdir ../outputs/Rock_level_hard_resethigh/Markdown
bsub -o "../outputs/Rock_level_hard_resethigh/Markdown/Rock_level_hard_resethigh_0.md" -J "Rock_level_hard_resethigh_0" -P "-name Rock_level_hard_resethigh-0 -hours 11.0 -level Levels.Rocks -reset_chance 0.005" < submit.sh
mkdir ../outputs/Rock_level_hard_modresetlow/
mkdir ../outputs/Rock_level_hard_modresetlow/Markdown
bsub -o "../outputs/Rock_level_hard_modresetlow/Markdown/Rock_level_hard_modresetlow_0.md" -J "Rock_level_hard_modresetlow_0" -P "-name Rock_level_hard_modresetlow-0 -hours 11.0 -level Levels.Rocks -modified_done_chance 0.02" < submit.sh
mkdir ../outputs/Rock_level_hard_misslow/
mkdir ../outputs/Rock_level_hard_misslow/Markdown
bsub -o "../outputs/Rock_level_hard_misslow/Markdown/Rock_level_hard_misslow_0.md" -J "Rock_level_hard_misslow_0" -P "-name Rock_level_hard_misslow-0 -hours 11.0 -level Levels.Rocks -miss_intervention_cost -0.1" < submit.sh
mkdir ../outputs/Rock_level_hard_interventionlow/
mkdir ../outputs/Rock_level_hard_interventionlow/Markdown
bsub -o "../outputs/Rock_level_hard_interventionlow/Markdown/Rock_level_hard_interventionlow_0.md" -J "Rock_level_hard_interventionlow_0" -P "-name Rock_level_hard_interventionlow-0 -hours 11.0 -level Levels.Rocks -intervention_cost -0.1" < submit.sh
