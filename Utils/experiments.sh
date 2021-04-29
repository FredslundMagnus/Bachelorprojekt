#!/bin/sh
mkdir ../outputs/Option_critic_tests/
mkdir ../outputs/Option_critic_tests/Markdown
bsub -o "../outputs/Option_critic_tests/Markdown/Option_critic_tests_0.md" -J "Option_critic_tests_0" -P "-name Option_critic_tests-0 -hours 0.1 -level Levels.Causal1 -main option_critic_run" < submit_cpu.sh
bsub -o "../outputs/Option_critic_tests/Markdown/Option_critic_tests_1.md" -J "Option_critic_tests_1" -P "-name Option_critic_tests-1 -hours 0.1 -level Levels.Causal1 -main option_critic_run" < submit_cpu.sh
bsub -o "../outputs/Option_critic_tests/Markdown/Option_critic_tests_2.md" -J "Option_critic_tests_2" -P "-name Option_critic_tests-2 -hours 0.1 -level Levels.Causal1 -main option_critic_run" < submit_cpu.sh
