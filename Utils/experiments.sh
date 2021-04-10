#!/bin/sh
mkdir ../outputs/MONTEST_CF_5c1/
mkdir ../outputs/MONTEST_CF_5c1/Markdown
bsub -o "../outputs/MONTEST_CF_5c1/Markdown/MONTEST_CF_5c1_0.md" -J "MONTEST_CF_5c1_0" -P "-name MONTEST_CF_5c1-0 -hours 22.0 -level Levels.MonsterLevel -main CFagent -CF_convert 5 -Counterfacts 1" < submit.sh
bsub -o "../outputs/MONTEST_CF_5c1/Markdown/MONTEST_CF_5c1_1.md" -J "MONTEST_CF_5c1_1" -P "-name MONTEST_CF_5c1-1 -hours 22.0 -level Levels.MonsterLevel -main CFagent -CF_convert 5 -Counterfacts 1" < submit.sh
mkdir ../outputs/MONTEST_CF_5c2/
mkdir ../outputs/MONTEST_CF_5c2/Markdown
bsub -o "../outputs/MONTEST_CF_5c2/Markdown/MONTEST_CF_5c2_0.md" -J "MONTEST_CF_5c2_0" -P "-name MONTEST_CF_5c2-0 -hours 22.0 -level Levels.MonsterLevel -main CFagent -CF_convert 5 -Counterfacts 2" < submit.sh
bsub -o "../outputs/MONTEST_CF_5c2/Markdown/MONTEST_CF_5c2_1.md" -J "MONTEST_CF_5c2_1" -P "-name MONTEST_CF_5c2-1 -hours 22.0 -level Levels.MonsterLevel -main CFagent -CF_convert 5 -Counterfacts 2" < submit.sh
mkdir ../outputs/MONTEST_CF_5c3/
mkdir ../outputs/MONTEST_CF_5c3/Markdown
bsub -o "../outputs/MONTEST_CF_5c3/Markdown/MONTEST_CF_5c3_0.md" -J "MONTEST_CF_5c3_0" -P "-name MONTEST_CF_5c3-0 -hours 22.0 -level Levels.MonsterLevel -main CFagent -CF_convert 5 -Counterfacts 3" < submit.sh
bsub -o "../outputs/MONTEST_CF_5c3/Markdown/MONTEST_CF_5c3_1.md" -J "MONTEST_CF_5c3_1" -P "-name MONTEST_CF_5c3-1 -hours 22.0 -level Levels.MonsterLevel -main CFagent -CF_convert 5 -Counterfacts 3" < submit.sh
mkdir ../outputs/MONTEST_CF_6c1/
mkdir ../outputs/MONTEST_CF_6c1/Markdown
bsub -o "../outputs/MONTEST_CF_6c1/Markdown/MONTEST_CF_6c1_0.md" -J "MONTEST_CF_6c1_0" -P "-name MONTEST_CF_6c1-0 -hours 22.0 -level Levels.MonsterLevel -main CFagent -CF_convert 6 -Counterfacts 1" < submit.sh
bsub -o "../outputs/MONTEST_CF_6c1/Markdown/MONTEST_CF_6c1_1.md" -J "MONTEST_CF_6c1_1" -P "-name MONTEST_CF_6c1-1 -hours 22.0 -level Levels.MonsterLevel -main CFagent -CF_convert 6 -Counterfacts 1" < submit.sh
mkdir ../outputs/MONTEST_CF_6c2/
mkdir ../outputs/MONTEST_CF_6c2/Markdown
bsub -o "../outputs/MONTEST_CF_6c2/Markdown/MONTEST_CF_6c2_0.md" -J "MONTEST_CF_6c2_0" -P "-name MONTEST_CF_6c2-0 -hours 22.0 -level Levels.MonsterLevel -main CFagent -CF_convert 6 -Counterfacts 2" < submit.sh
bsub -o "../outputs/MONTEST_CF_6c2/Markdown/MONTEST_CF_6c2_1.md" -J "MONTEST_CF_6c2_1" -P "-name MONTEST_CF_6c2-1 -hours 22.0 -level Levels.MonsterLevel -main CFagent -CF_convert 6 -Counterfacts 2" < submit.sh
mkdir ../outputs/MONTEST_CF_6c3/
mkdir ../outputs/MONTEST_CF_6c3/Markdown
bsub -o "../outputs/MONTEST_CF_6c3/Markdown/MONTEST_CF_6c3_0.md" -J "MONTEST_CF_6c3_0" -P "-name MONTEST_CF_6c3-0 -hours 22.0 -level Levels.MonsterLevel -main CFagent -CF_convert 6 -Counterfacts 3" < submit.sh
bsub -o "../outputs/MONTEST_CF_6c3/Markdown/MONTEST_CF_6c3_1.md" -J "MONTEST_CF_6c3_1" -P "-name MONTEST_CF_6c3-1 -hours 22.0 -level Levels.MonsterLevel -main CFagent -CF_convert 6 -Counterfacts 3" < submit.sh
