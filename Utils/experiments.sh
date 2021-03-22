#!/bin/sh
mkdir ../outputs/Rock_level_hard_new_parameters/
mkdir ../outputs/Rock_level_hard_new_parameters/Markdown
bsub -o "../outputs/Rock_level_hard_new_parameters/Markdown/Rock_level_hard_new_parameters_0.md" -J "Rock_level_hard_new_parameters_0" -P "-name Rock_level_hard_new_parameters-0 -hours 11.0 -level Levels.Rocks" < submit.sh
