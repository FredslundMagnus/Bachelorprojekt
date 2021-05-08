#!/bin/sh
mkdir ../outputs/Monsters_simple/
mkdir ../outputs/Monsters_simple/Markdown
bsub -o "../outputs/Monsters_simple/Markdown/Monsters_simple_0.md" -J "Monsters_simple_0" -env MYARGS="-name Monsters_simple-0 -hours 24.0 -level Levels.MonsterLevel -main simple -network2 Networks.MiniBig -num 0" < submit_gpu.sh
bsub -o "../outputs/Monsters_simple/Markdown/Monsters_simple_1.md" -J "Monsters_simple_1" -env MYARGS="-name Monsters_simple-1 -hours 24.0 -level Levels.MonsterLevel -main simple -network2 Networks.MiniBig -num 1" < submit_gpu.sh
bsub -o "../outputs/Monsters_simple/Markdown/Monsters_simple_2.md" -J "Monsters_simple_2" -env MYARGS="-name Monsters_simple-2 -hours 24.0 -level Levels.MonsterLevel -main simple -network2 Networks.MiniBig -num 2" < submit_gpu.sh
mkdir ../outputs/DoorsAndKey_simple/
mkdir ../outputs/DoorsAndKey_simple/Markdown
bsub -o "../outputs/DoorsAndKey_simple/Markdown/DoorsAndKey_simple_0.md" -J "DoorsAndKey_simple_0" -env MYARGS="-name DoorsAndKey_simple-0 -hours 24.0 -level Levels.Causal1 -main simple -network2 Networks.MiniBig -num 0" < submit_gpu.sh
bsub -o "../outputs/DoorsAndKey_simple/Markdown/DoorsAndKey_simple_1.md" -J "DoorsAndKey_simple_1" -env MYARGS="-name DoorsAndKey_simple-1 -hours 24.0 -level Levels.Causal1 -main simple -network2 Networks.MiniBig -num 1" < submit_gpu.sh
bsub -o "../outputs/DoorsAndKey_simple/Markdown/DoorsAndKey_simple_2.md" -J "DoorsAndKey_simple_2" -env MYARGS="-name DoorsAndKey_simple-2 -hours 24.0 -level Levels.Causal1 -main simple -network2 Networks.MiniBig -num 2" < submit_gpu.sh
