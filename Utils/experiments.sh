#!/bin/sh
mkdir ../outputs/simul_gold_9x9/
mkdir ../outputs/simul_gold_9x9/Markdown
bsub -o "../outputs/simul_gold_9x9/Markdown/simul_gold_9x9_0.md" -J "simul_gold_9x9_0" -P "-name simul_gold_9x9-0 -hours 4.0" < submit.sh
bsub -o "../outputs/simul_gold_9x9/Markdown/simul_gold_9x9_1.md" -J "simul_gold_9x9_1" -P "-name simul_gold_9x9-1 -hours 4.0" < submit.sh
bsub -o "../outputs/simul_gold_9x9/Markdown/simul_gold_9x9_2.md" -J "simul_gold_9x9_2" -P "-name simul_gold_9x9-2 -hours 4.0" < submit.sh
