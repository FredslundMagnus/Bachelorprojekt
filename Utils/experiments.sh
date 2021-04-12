#!/bin/sh
mkdir ../outputs/CFv2TESTCAU1cf1/
mkdir ../outputs/CFv2TESTCAU1cf1/Markdown
bsub -o "../outputs/CFv2TESTCAU1cf1/Markdown/CFv2TESTCAU1cf1_0.md" -J "CFv2TESTCAU1cf1_0" -P "-name CFv2TESTCAU1cf1-0 -hours 16.0 -level Levels.Causal1 -main CFagentv2 -CF_convert 3 -Counterfacts 1" < submit.sh
mkdir ../outputs/CFv2TESTCAU1cf2/
mkdir ../outputs/CFv2TESTCAU1cf2/Markdown
bsub -o "../outputs/CFv2TESTCAU1cf2/Markdown/CFv2TESTCAU1cf2_0.md" -J "CFv2TESTCAU1cf2_0" -P "-name CFv2TESTCAU1cf2-0 -hours 16.0 -level Levels.Causal1 -main CFagentv2 -CF_convert 3 -Counterfacts 2" < submit.sh
mkdir ../outputs/CFv2TESTCAU2cf1/
mkdir ../outputs/CFv2TESTCAU2cf1/Markdown
bsub -o "../outputs/CFv2TESTCAU2cf1/Markdown/CFv2TESTCAU2cf1_0.md" -J "CFv2TESTCAU2cf1_0" -P "-name CFv2TESTCAU2cf1-0 -hours 16.0 -level Levels.Causal2 -main CFagentv2 -CF_convert 3 -Counterfacts 1" < submit.sh
mkdir ../outputs/CFv2TESTCAU2cf2/
mkdir ../outputs/CFv2TESTCAU2cf2/Markdown
bsub -o "../outputs/CFv2TESTCAU2cf2/Markdown/CFv2TESTCAU2cf2_0.md" -J "CFv2TESTCAU2cf2_0" -P "-name CFv2TESTCAU2cf2-0 -hours 16.0 -level Levels.Causal2 -main CFagentv2 -CF_convert 3 -Counterfacts 2" < submit.sh
mkdir ../outputs/CFv2TESTCAU4cf1/
mkdir ../outputs/CFv2TESTCAU4cf1/Markdown
bsub -o "../outputs/CFv2TESTCAU4cf1/Markdown/CFv2TESTCAU4cf1_0.md" -J "CFv2TESTCAU4cf1_0" -P "-name CFv2TESTCAU4cf1-0 -hours 16.0 -level Levels.Causal4 -main CFagentv2 -CF_convert 3 -Counterfacts 1" < submit.sh
mkdir ../outputs/CFv2TESTCAU4cf2/
mkdir ../outputs/CFv2TESTCAU4cf2/Markdown
bsub -o "../outputs/CFv2TESTCAU4cf2/Markdown/CFv2TESTCAU4cf2_0.md" -J "CFv2TESTCAU4cf2_0" -P "-name CFv2TESTCAU4cf2-0 -hours 16.0 -level Levels.Causal4 -main CFagentv2 -CF_convert 3 -Counterfacts 2" < submit.sh
