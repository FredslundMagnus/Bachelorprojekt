#!/bin/sh
mkdir ../outputs/keys_door_small/
mkdir ../outputs/keys_door_small/Markdown
bsub -o "../outputs/keys_door_small/Markdown/keys_door_small_0.md" -J "keys_door_small_0" -P "-name keys_door_small-0 -hours 10.0 -width 9 -height 9 -layer_Keys True -layer_Door True" < submit.sh
mkdir ../outputs/holder_putter_small/
mkdir ../outputs/holder_putter_small/Markdown
bsub -o "../outputs/holder_putter_small/Markdown/holder_putter_small_0.md" -J "holder_putter_small_0" -P "-name holder_putter_small-0 -hours 10.0 -width 9 -height 9 -layer_Holder True -layer_Putter True" < submit.sh
mkdir ../outputs/keys_door_gold_small/
mkdir ../outputs/keys_door_gold_small/Markdown
bsub -o "../outputs/keys_door_gold_small/Markdown/keys_door_gold_small_0.md" -J "keys_door_gold_small_0" -P "-name keys_door_gold_small-0 -hours 10.0 -width 9 -height 9 -layer_Keys True -layer_Door True -layer_Gold True" < submit.sh
mkdir ../outputs/holder_putter_gold_small/
mkdir ../outputs/holder_putter_gold_small/Markdown
bsub -o "../outputs/holder_putter_gold_small/Markdown/holder_putter_gold_small_0.md" -J "holder_putter_gold_small_0" -P "-name holder_putter_gold_small-0 -hours 10.0 -width 9 -height 9 -layer_Holder True -layer_Putter True -layer_Gold True" < submit.sh
mkdir ../outputs/keys_door_holder_putter_gold_small/
mkdir ../outputs/keys_door_holder_putter_gold_small/Markdown
bsub -o "../outputs/keys_door_holder_putter_gold_small/Markdown/keys_door_holder_putter_gold_small_0.md" -J "keys_door_holder_putter_gold_small_0" -P "-name keys_door_holder_putter_gold_small-0 -hours 10.0 -width 9 -height 9 -layer_Keys True -layer_Door True -layer_Holder True -layer_Putter True -layer_Gold True" < submit.sh
