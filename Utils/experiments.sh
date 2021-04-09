#!/bin/sh
mkdir ../outputs/TEST_CF_CAUSAL4_2/
mkdir ../outputs/TEST_CF_CAUSAL4_2/Markdown
bsub -o "../outputs/TEST_CF_CAUSAL4_2/Markdown/TEST_CF_CAUSAL4_2_0.md" -J "TEST_CF_CAUSAL4_2_0" -P "-name TEST_CF_CAUSAL4_2-0 -hours 23.0 -level Levels.Causal4 -main CFagent -CF_convert 2" < submit.sh
mkdir ../outputs/TEST_CF_CAUSAL4_3/
mkdir ../outputs/TEST_CF_CAUSAL4_3/Markdown
bsub -o "../outputs/TEST_CF_CAUSAL4_3/Markdown/TEST_CF_CAUSAL4_3_0.md" -J "TEST_CF_CAUSAL4_3_0" -P "-name TEST_CF_CAUSAL4_3-0 -hours 23.0 -level Levels.Causal4 -main CFagent -CF_convert 3" < submit.sh
mkdir ../outputs/TEST_CF_CAUSAL4_4/
mkdir ../outputs/TEST_CF_CAUSAL4_4/Markdown
bsub -o "../outputs/TEST_CF_CAUSAL4_4/Markdown/TEST_CF_CAUSAL4_4_0.md" -J "TEST_CF_CAUSAL4_4_0" -P "-name TEST_CF_CAUSAL4_4-0 -hours 23.0 -level Levels.Causal4 -main CFagent -CF_convert 4" < submit.sh
mkdir ../outputs/TEST_CF_CAUSAL4_6c1/
mkdir ../outputs/TEST_CF_CAUSAL4_6c1/Markdown
bsub -o "../outputs/TEST_CF_CAUSAL4_6c1/Markdown/TEST_CF_CAUSAL4_6c1_0.md" -J "TEST_CF_CAUSAL4_6c1_0" -P "-name TEST_CF_CAUSAL4_6c1-0 -hours 23.0 -level Levels.Causal4 -main CFagent -CF_convert 6 -Counterfacts 1" < submit.sh
mkdir ../outputs/TEST_CF_CAUSAL4_6c2/
mkdir ../outputs/TEST_CF_CAUSAL4_6c2/Markdown
bsub -o "../outputs/TEST_CF_CAUSAL4_6c2/Markdown/TEST_CF_CAUSAL4_6c2_0.md" -J "TEST_CF_CAUSAL4_6c2_0" -P "-name TEST_CF_CAUSAL4_6c2-0 -hours 23.0 -level Levels.Causal4 -main CFagent -CF_convert 6 -Counterfacts 2" < submit.sh
mkdir ../outputs/TEST_CF_CAUSAL4_6c3/
mkdir ../outputs/TEST_CF_CAUSAL4_6c3/Markdown
bsub -o "../outputs/TEST_CF_CAUSAL4_6c3/Markdown/TEST_CF_CAUSAL4_6c3_0.md" -J "TEST_CF_CAUSAL4_6c3_0" -P "-name TEST_CF_CAUSAL4_6c3-0 -hours 23.0 -level Levels.Causal4 -main CFagent -CF_convert 6 -Counterfacts 3" < submit.sh
