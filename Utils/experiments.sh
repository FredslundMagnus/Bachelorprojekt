#!/bin/sh
mkdir ../outputs/Rock_level/
mkdir ../outputs/Rock_level/Markdown
bsub -o "../outputs/Rock_level/Markdown/Rock_level_0.md" -J "Rock_level_0" -P "-name Rock_level-0 -hours 12.0 -level Levels.Rocks" < submit.sh
mkdir ../outputs/Rock_level_Khigh/
mkdir ../outputs/Rock_level_Khigh/Markdown
bsub -o "../outputs/Rock_level_Khigh/Markdown/Rock_level_Khigh_0.md" -J "Rock_level_Khigh_0" -P "-name Rock_level_Khigh-0 -hours 12.0 -level Levels.Rocks -K 1000000.0" < submit.sh
mkdir ../outputs/Rock_level_epshigh/
mkdir ../outputs/Rock_level_epshigh/Markdown
bsub -o "../outputs/Rock_level_epshigh/Markdown/Rock_level_epshigh_0.md" -J "Rock_level_epshigh_0" -P "-name Rock_level_epshigh-0 -hours 12.0 -level Levels.Rocks -epsilon_cap 0.2" < submit.sh
mkdir ../outputs/Rock_level_epslow/
mkdir ../outputs/Rock_level_epslow/Markdown
bsub -o "../outputs/Rock_level_epslow/Markdown/Rock_level_epslow_0.md" -J "Rock_level_epslow_0" -P "-name Rock_level_epslow-0 -hours 12.0 -level Levels.Rocks -epsilon_cap 0.0" < submit.sh
mkdir ../outputs/Rock_level_softhigh/
mkdir ../outputs/Rock_level_softhigh/Markdown
bsub -o "../outputs/Rock_level_softhigh/Markdown/Rock_level_softhigh_0.md" -J "Rock_level_softhigh_0" -P "-name Rock_level_softhigh-0 -hours 12.0 -level Levels.Rocks -softmax_cap 0.05" < submit.sh
mkdir ../outputs/Rock_level_softlow/
mkdir ../outputs/Rock_level_softlow/Markdown
bsub -o "../outputs/Rock_level_softlow/Markdown/Rock_level_softlow_0.md" -J "Rock_level_softlow_0" -P "-name Rock_level_softlow-0 -hours 12.0 -level Levels.Rocks -softmax_cap 0.01" < submit.sh
mkdir ../outputs/Rock_level_gammalow/
mkdir ../outputs/Rock_level_gammalow/Markdown
bsub -o "../outputs/Rock_level_gammalow/Markdown/Rock_level_gammalow_0.md" -J "Rock_level_gammalow_0" -P "-name Rock_level_gammalow-0 -hours 12.0 -level Levels.Rocks -gamma 0.95" < submit.sh
mkdir ../outputs/Rock_level_resethigh/
mkdir ../outputs/Rock_level_resethigh/Markdown
bsub -o "../outputs/Rock_level_resethigh/Markdown/Rock_level_resethigh_0.md" -J "Rock_level_resethigh_0" -P "-name Rock_level_resethigh-0 -hours 12.0 -level Levels.Rocks -reset_chance 0.005" < submit.sh
mkdir ../outputs/Rock_level_modresetlow/
mkdir ../outputs/Rock_level_modresetlow/Markdown
bsub -o "../outputs/Rock_level_modresetlow/Markdown/Rock_level_modresetlow_0.md" -J "Rock_level_modresetlow_0" -P "-name Rock_level_modresetlow-0 -hours 12.0 -level Levels.Rocks -modified_done_chance 0.02" < submit.sh
mkdir ../outputs/Rock_level_misslow/
mkdir ../outputs/Rock_level_misslow/Markdown
bsub -o "../outputs/Rock_level_misslow/Markdown/Rock_level_misslow_0.md" -J "Rock_level_misslow_0" -P "-name Rock_level_misslow-0 -hours 12.0 -level Levels.Rocks -miss_intervention_cost -0.1" < submit.sh
mkdir ../outputs/Rock_level_interventionlow/
mkdir ../outputs/Rock_level_interventionlow/Markdown
bsub -o "../outputs/Rock_level_interventionlow/Markdown/Rock_level_interventionlow_0.md" -J "Rock_level_interventionlow_0" -P "-name Rock_level_interventionlow-0 -hours 12.0 -level Levels.Rocks -intervention_cost -0.1" < submit.sh
