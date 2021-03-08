#!/bin/sh
mkdir ../outputs/maze_size_13_low_rest_chance/
mkdir ../outputs/maze_size_13_low_rest_chance/Markdown
bsub -o "../outputs/maze_size_13_low_rest_chance/Markdown/maze_size_13_low_rest_chance_0.md" -J "maze_size_13_low_rest_chance_0" -P "-name maze_size_13_low_rest_chance-0 -hours 10.0 -width 13 -height 13" < submit.sh
mkdir ../outputs/maze_size_15_low_rest_chance/
mkdir ../outputs/maze_size_15_low_rest_chance/Markdown
bsub -o "../outputs/maze_size_15_low_rest_chance/Markdown/maze_size_15_low_rest_chance_0.md" -J "maze_size_15_low_rest_chance_0" -P "-name maze_size_15_low_rest_chance-0 -hours 10.0 -width 15 -height 15" < submit.sh
mkdir ../outputs/maze_size_17_low_rest_chance/
mkdir ../outputs/maze_size_17_low_rest_chance/Markdown
bsub -o "../outputs/maze_size_17_low_rest_chance/Markdown/maze_size_17_low_rest_chance_0.md" -J "maze_size_17_low_rest_chance_0" -P "-name maze_size_17_low_rest_chance-0 -hours 10.0 -width 17 -height 17" < submit.sh
mkdir ../outputs/maze_size_19_low_rest_chance/
mkdir ../outputs/maze_size_19_low_rest_chance/Markdown
bsub -o "../outputs/maze_size_19_low_rest_chance/Markdown/maze_size_19_low_rest_chance_0.md" -J "maze_size_19_low_rest_chance_0" -P "-name maze_size_19_low_rest_chance-0 -hours 10.0 -width 19 -height 19" < submit.sh
mkdir ../outputs/maze_size_13_high_rest_chance/
mkdir ../outputs/maze_size_13_high_rest_chance/Markdown
bsub -o "../outputs/maze_size_13_high_rest_chance/Markdown/maze_size_13_high_rest_chance_0.md" -J "maze_size_13_high_rest_chance_0" -P "-name maze_size_13_high_rest_chance-0 -hours 10.0 -width 13 -height 13 -reset_chance 0.005" < submit.sh
mkdir ../outputs/maze_size_15_high_rest_chance/
mkdir ../outputs/maze_size_15_high_rest_chance/Markdown
bsub -o "../outputs/maze_size_15_high_rest_chance/Markdown/maze_size_15_high_rest_chance_0.md" -J "maze_size_15_high_rest_chance_0" -P "-name maze_size_15_high_rest_chance-0 -hours 10.0 -width 15 -height 15 -reset_chance 0.005" < submit.sh
mkdir ../outputs/maze_size_17_high_rest_chance/
mkdir ../outputs/maze_size_17_high_rest_chance/Markdown
bsub -o "../outputs/maze_size_17_high_rest_chance/Markdown/maze_size_17_high_rest_chance_0.md" -J "maze_size_17_high_rest_chance_0" -P "-name maze_size_17_high_rest_chance-0 -hours 10.0 -width 17 -height 17 -reset_chance 0.005" < submit.sh
mkdir ../outputs/maze_size_19_high_rest_chance/
mkdir ../outputs/maze_size_19_high_rest_chance/Markdown
bsub -o "../outputs/maze_size_19_high_rest_chance/Markdown/maze_size_19_high_rest_chance_0.md" -J "maze_size_19_high_rest_chance_0" -P "-name maze_size_19_high_rest_chance-0 -hours 10.0 -width 19 -height 19 -reset_chance 0.005" < submit.sh
