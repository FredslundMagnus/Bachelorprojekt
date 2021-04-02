#!/bin/sh
mkdir ../outputs/causal5_test/
mkdir ../outputs/causal5_test/Markdown
bsub -o "../outputs/causal5_test/Markdown/causal5_test_0.md" -J "causal5_test_0" -P "-name causal5_test-0 -hours 6.0 -level Levels.Causal5 -main teleport" < submit.sh
bsub -o "../outputs/causal5_test/Markdown/causal5_test_1.md" -J "causal5_test_1" -P "-name causal5_test-1 -hours 6.0 -level Levels.Causal5 -main teleport" < submit.sh
bsub -o "../outputs/causal5_test/Markdown/causal5_test_2.md" -J "causal5_test_2" -P "-name causal5_test-2 -hours 6.0 -level Levels.Causal5 -main teleport" < submit.sh
mkdir ../outputs/causal5_good/
mkdir ../outputs/causal5_good/Markdown
bsub -o "../outputs/causal5_good/Markdown/causal5_good_0.md" -J "causal5_good_0" -P "-name causal5_good-0 -hours 20.0 -level Levels.Causal5 -main teleport" < submit.sh
bsub -o "../outputs/causal5_good/Markdown/causal5_good_1.md" -J "causal5_good_1" -P "-name causal5_good-1 -hours 20.0 -level Levels.Causal5 -main teleport" < submit.sh
bsub -o "../outputs/causal5_good/Markdown/causal5_good_2.md" -J "causal5_good_2" -P "-name causal5_good-2 -hours 20.0 -level Levels.Causal5 -main teleport" < submit.sh
