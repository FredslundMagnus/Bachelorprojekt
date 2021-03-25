#!/bin/sh
mkdir ../outputs/causal3_9x9_20hoursONLYMOVERsoftmax/
mkdir ../outputs/causal3_9x9_20hoursONLYMOVERsoftmax/Markdown
bsub -o "../outputs/causal3_9x9_20hoursONLYMOVERsoftmax/Markdown/causal3_9x9_20hoursONLYMOVERsoftmax_0.md" -J "causal3_9x9_20hoursONLYMOVERsoftmax_0" -P "-name causal3_9x9_20hoursONLYMOVERsoftmax-0 -hours 20.0 -level Levels.Causal3 -main simple -K2 5000000.0 -exploration2 Explorations.softmaxer -gamma2 0.98" < submit.sh
mkdir ../outputs/causal3_9x9_20hoursONLYMOVERepsgreed/
mkdir ../outputs/causal3_9x9_20hoursONLYMOVERepsgreed/Markdown
bsub -o "../outputs/causal3_9x9_20hoursONLYMOVERepsgreed/Markdown/causal3_9x9_20hoursONLYMOVERepsgreed_0.md" -J "causal3_9x9_20hoursONLYMOVERepsgreed_0" -P "-name causal3_9x9_20hoursONLYMOVERepsgreed-0 -hours 20.0 -level Levels.Causal3 -main simple -K2 5000000.0 -exploration2 Explorations.epsilonGreedy -gamma2 0.98" < submit.sh
mkdir ../outputs/causal3_9x9_20hoursONLYMOVERsoftmaxgam0995/
mkdir ../outputs/causal3_9x9_20hoursONLYMOVERsoftmaxgam0995/Markdown
bsub -o "../outputs/causal3_9x9_20hoursONLYMOVERsoftmaxgam0995/Markdown/causal3_9x9_20hoursONLYMOVERsoftmaxgam0995_0.md" -J "causal3_9x9_20hoursONLYMOVERsoftmaxgam0995_0" -P "-name causal3_9x9_20hoursONLYMOVERsoftmaxgam0995-0 -hours 20.0 -level Levels.Causal3 -main simple -K2 5000000.0 -exploration2 Explorations.softmaxer -gamma2 0.995" < submit.sh
mkdir ../outputs/causal3_9x9_20hoursONLYMOVERepsgreedgam0995/
mkdir ../outputs/causal3_9x9_20hoursONLYMOVERepsgreedgam0995/Markdown
bsub -o "../outputs/causal3_9x9_20hoursONLYMOVERepsgreedgam0995/Markdown/causal3_9x9_20hoursONLYMOVERepsgreedgam0995_0.md" -J "causal3_9x9_20hoursONLYMOVERepsgreedgam0995_0" -P "-name causal3_9x9_20hoursONLYMOVERepsgreedgam0995-0 -hours 20.0 -level Levels.Causal3 -main simple -K2 5000000.0 -exploration2 Explorations.epsilonGreedy -gamma2 0.995" < submit.sh
