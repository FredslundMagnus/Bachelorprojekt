#!/bin/sh
mkdir ../outputs/Option_Critic/
mkdir ../outputs/Option_Critic/Markdown
bsub -o "../outputs/Option_Critic/Markdown/Option_Critic_0.md" -J "Option_Critic_0" -P "-name Option_Critic-0 -hours 24.0 -level Levels.Causal2 -main option_critic_run" < submit.sh
