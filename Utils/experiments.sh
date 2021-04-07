#!/bin/sh
mkdir ../outputs/cococonuts_CF_conver2/
mkdir ../outputs/cococonuts_CF_conver2/Markdown
bsub -o "../outputs/cococonuts_CF_conver2/Markdown/cococonuts_CF_conver2_0.md" -J "cococonuts_CF_conver2_0" -P "-name cococonuts_CF_conver2-0 -hours 24.0 -level Levels.Coconuts -main CFagent -CF_convert 2" < submit.sh
mkdir ../outputs/cococonuts_CF_conver3/
mkdir ../outputs/cococonuts_CF_conver3/Markdown
bsub -o "../outputs/cococonuts_CF_conver3/Markdown/cococonuts_CF_conver3_0.md" -J "cococonuts_CF_conver3_0" -P "-name cococonuts_CF_conver3-0 -hours 24.0 -level Levels.Coconuts -main CFagent -CF_convert 3" < submit.sh
mkdir ../outputs/cococonuts_CF_conver4/
mkdir ../outputs/cococonuts_CF_conver4/Markdown
bsub -o "../outputs/cococonuts_CF_conver4/Markdown/cococonuts_CF_conver4_0.md" -J "cococonuts_CF_conver4_0" -P "-name cococonuts_CF_conver4-0 -hours 24.0 -level Levels.Coconuts -main CFagent -CF_convert 4" < submit.sh
mkdir ../outputs/cococonuts_CF_conver6/
mkdir ../outputs/cococonuts_CF_conver6/Markdown
bsub -o "../outputs/cococonuts_CF_conver6/Markdown/cococonuts_CF_conver6_0.md" -J "cococonuts_CF_conver6_0" -P "-name cococonuts_CF_conver6-0 -hours 24.0 -level Levels.Coconuts -main CFagent -CF_convert 6" < submit.sh
mkdir ../outputs/cococonuts_CF_conver9/
mkdir ../outputs/cococonuts_CF_conver9/Markdown
bsub -o "../outputs/cococonuts_CF_conver9/Markdown/cococonuts_CF_conver9_0.md" -J "cococonuts_CF_conver9_0" -P "-name cococonuts_CF_conver9-0 -hours 24.0 -level Levels.Coconuts -main CFagent -CF_convert 9" < submit.sh
mkdir ../outputs/cococonuts_teleport/
mkdir ../outputs/cococonuts_teleport/Markdown
bsub -o "../outputs/cococonuts_teleport/Markdown/cococonuts_teleport_0.md" -J "cococonuts_teleport_0" -P "-name cococonuts_teleport-0 -hours 24.0 -level Levels.Coconuts -main teleport" < submit.sh
