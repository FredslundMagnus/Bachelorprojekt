#!/bin/sh
mkdir ../outputs/coconuts_CF_conver5/
mkdir ../outputs/coconuts_CF_conver5/Markdown
bsub -o "../outputs/coconuts_CF_conver5/Markdown/coconuts_CF_conver5_0.md" -J "coconuts_CF_conver5_0" -P "-name coconuts_CF_conver5-0 -hours 24.0 -level Levels.Coconuts -main CFagent -CF_convert 5" < submit.sh
mkdir ../outputs/coconuts_CF_conver6/
mkdir ../outputs/coconuts_CF_conver6/Markdown
bsub -o "../outputs/coconuts_CF_conver6/Markdown/coconuts_CF_conver6_0.md" -J "coconuts_CF_conver6_0" -P "-name coconuts_CF_conver6-0 -hours 24.0 -level Levels.Coconuts -main CFagent -CF_convert 6" < submit.sh
mkdir ../outputs/coconuts_CF_conver7/
mkdir ../outputs/coconuts_CF_conver7/Markdown
bsub -o "../outputs/coconuts_CF_conver7/Markdown/coconuts_CF_conver7_0.md" -J "coconuts_CF_conver7_0" -P "-name coconuts_CF_conver7-0 -hours 24.0 -level Levels.Coconuts -main CFagent -CF_convert 7" < submit.sh
mkdir ../outputs/coconuts_CF_conver8/
mkdir ../outputs/coconuts_CF_conver8/Markdown
bsub -o "../outputs/coconuts_CF_conver8/Markdown/coconuts_CF_conver8_0.md" -J "coconuts_CF_conver8_0" -P "-name coconuts_CF_conver8-0 -hours 24.0 -level Levels.Coconuts -main CFagent -CF_convert 8" < submit.sh
mkdir ../outputs/coconuts_CF_conver9/
mkdir ../outputs/coconuts_CF_conver9/Markdown
bsub -o "../outputs/coconuts_CF_conver9/Markdown/coconuts_CF_conver9_0.md" -J "coconuts_CF_conver9_0" -P "-name coconuts_CF_conver9-0 -hours 24.0 -level Levels.Coconuts -main CFagent -CF_convert 9" < submit.sh
mkdir ../outputs/coconuts_teleport/
mkdir ../outputs/coconuts_teleport/Markdown
bsub -o "../outputs/coconuts_teleport/Markdown/coconuts_teleport_0.md" -J "coconuts_teleport_0" -P "-name coconuts_teleport-0 -hours 24.0 -level Levels.Coconuts -main teleport" < submit.sh
