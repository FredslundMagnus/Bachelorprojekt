#!/bin/sh
mkdir ../outputs/ReTest1/
mkdir ../outputs/ReTest1/Markdown
bsub -o "../outputs/ReTest1/Markdown/ReTest1_0.md" -J "ReTest1_0" -P "-name ReTest1-0 -hours 12.0 -K1 2000000.0 -K2 500000.0 -level Levels.Causal3 -main CFagent -CF_convert 3 -Counterfacts 1 -Random_counterfacts False" < submit.sh
mkdir ../outputs/ReTest2/
mkdir ../outputs/ReTest2/Markdown
bsub -o "../outputs/ReTest2/Markdown/ReTest2_0.md" -J "ReTest2_0" -P "-name ReTest2-0 -hours 12.0 -K1 2000000.0 -K2 500000.0 -level Levels.Causal3 -main CFagent -CF_convert 4 -Counterfacts 1 -Random_counterfacts False" < submit.sh
mkdir ../outputs/ReTest3/
mkdir ../outputs/ReTest3/Markdown
bsub -o "../outputs/ReTest3/Markdown/ReTest3_0.md" -J "ReTest3_0" -P "-name ReTest3-0 -hours 12.0 -K1 2000000.0 -K2 500000.0 -level Levels.Causal3 -main CFagent -CF_convert 3 -Counterfacts 1 -Random_counterfacts True" < submit.sh
mkdir ../outputs/ReTest4/
mkdir ../outputs/ReTest4/Markdown
bsub -o "../outputs/ReTest4/Markdown/ReTest4_0.md" -J "ReTest4_0" -P "-name ReTest4-0 -hours 12.0 -K1 2000000.0 -K2 500000.0 -level Levels.Causal3 -main CFagent -CF_convert 4 -Counterfacts 1 -Random_counterfacts True" < submit.sh
mkdir ../outputs/ReTest5/
mkdir ../outputs/ReTest5/Markdown
bsub -o "../outputs/ReTest5/Markdown/ReTest5_0.md" -J "ReTest5_0" -P "-name ReTest5-0 -hours 12.0 -K1 2000000.0 -K2 500000.0 -level Levels.Causal3 -main CFagentv2 -CF_convert 3 -Counterfacts 1 -Random_counterfacts False" < submit.sh
mkdir ../outputs/ReTest6/
mkdir ../outputs/ReTest6/Markdown
bsub -o "../outputs/ReTest6/Markdown/ReTest6_0.md" -J "ReTest6_0" -P "-name ReTest6-0 -hours 12.0 -K1 2000000.0 -K2 500000.0 -level Levels.Causal3 -main CFagentv2 -CF_convert 4 -Counterfacts 1 -Random_counterfacts False" < submit.sh
