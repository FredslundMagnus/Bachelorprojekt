Traceback (most recent call last):
  File "/zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils/debug.py", line 71, in __init__
    cProfile.run(
  File "/appl/python/3.8.4/lib/python3.8/cProfile.py", line 16, in run
    return _pyprofile._Utils(Profile).run(statement, filename, sort)
  File "/appl/python/3.8.4/lib/python3.8/profile.py", line 53, in run
    prof.run(statement)
  File "/appl/python/3.8.4/lib/python3.8/cProfile.py", line 95, in run
    return self.runctx(cmd, dict, dict)
  File "/appl/python/3.8.4/lib/python3.8/cProfile.py", line 100, in runctx
    exec(cmd, globals, locals)
  File "<string>", line 2, in <module>
  File "/zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/allGraphsTrain.py", line 33, in graphTrain
    interventions = [(getInterventions(env, state, data, layers, exploration) if should else old) for state, should, old in zip(new_states, shouldInterviene, interventions)]
  File "/zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/allGraphsTrain.py", line 33, in <listcomp>
    interventions = [(getInterventions(env, state, data, layers, exploration) if should else old) for state, should, old in zip(new_states, shouldInterviene, interventions)]
  File "/zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/allGraphs.py", line 232, in getInterventions
    best = env.layers.types.index(rightIntervention(state, data, layers))
  File "/zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/allGraphs.py", line 198, in rightIntervention
    chances = {layer: flip_chance(state, layer, data) for layer in max(stats, key=stats.get) if layer not in stats and layer not in used}
  File "/zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/allGraphs.py", line 198, in <dictcomp>
    chances = {layer: flip_chance(state, layer, data) for layer in max(stats, key=stats.get) if layer not in stats and layer not in used}
  File "/zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/allGraphs.py", line 166, in flip_chance
    chanceForFlip *= (1 - data[layer][partial])
KeyError: frozenset({<LayerType.Greencross: 31>})


# Parameters

    Name :                      causal7_online-0
    Main :                      graphTrain
    Level :                     Levels.Causal7
    Hours :                     12.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Network1 :                  Networks.Teleporter
    K1 :                        200000.0
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
    K2 :                        100000.0
    Learner2 :                  Learners.Qlearn
    Exploration2 :              Explorations.epsilonGreedy
    Gamma2 :                    0.95
    Layer blocks :              True
    Layer goal :                True
    Layer gold :                True
    Layer keys :                True
    Layer door :                True
    Layer holder :              True
    Layer putter :              True
    Layer rock :                True
    Layer dirt :                True
    Layer diamond1 :            True
    Layer diamond2 :            True
    Layer diamond3 :            True
    Layer diamond4 :            True
    Layer reddoor :             True
    Layer redkeys :             True
    Layer bluedoor :            True
    Layer bluekeys :            True
    Layer pink1 :               True
    Layer pink2 :               True
    Layer pink3 :               True
    Layer brown1 :              True
    Layer brown2 :              True
    Layer brown3 :              True
    Layer greendown :           True
    Layer greenup :             True
    Layer greenstar :           True
    Layer yellowstar :          True
    Layer bluestar :            True
    Layer coconut :             True
    Layer monster :             True
    Layer greencross :          True
    Layer bluecross :           True
    Layer redcross :            True
    Layer purplecross :         True
    Epsilon cap :               0.2
    Softmax cap :               0.0
    Update :                    10000
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                2
    Counterfacts :              10
    Topn :                      7
    Minutes used :              0 minutes.
    Hours used :                0 hours.

# Profiling


      7521815 function calls (7512692 primitive calls) in 26.62 seconds

##    Ordered by: cumulative time
   List reduced from 420 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000   26.621   26.621 {built-in method builtins.exec}
                      1    0.000    0.000   26.621   26.621 <string>:1(<module>)
                      1    0.104    0.104   26.621   26.621 allGraphsTrain.py:5(graphTrain)
                      2    0.000    0.000    8.041    4.020 agent.py:16(__init__)
                      2    0.000    0.000    8.040    4.020 network.py:33(__init__)
                      1    0.000    0.000    8.033    8.033 agent.py:109(__init__)
                      6    0.000    0.000    8.002    1.334 module.py:529(to)
                   72/6    0.000    0.000    8.002    1.334 module.py:357(_apply)
                    491    8.000    0.016    8.001    0.016 {method 'to' of 'torch._C._TensorBase' objects}
                     54    0.000    0.000    8.000    0.148 module.py:607(convert)
                    438    3.169    0.007    7.639    0.017 allGraphs.py:220(transformNot)
                 438300    5.041    0.000    5.041    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                  44339    1.101    0.000    4.797    0.000 allGraphs.py:141(states)
                    438    0.011    0.000    4.763    0.011 allGraphsTrain.py:27(<listcomp>)
                 394600    3.528    0.000    3.528    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                    437    0.001    0.000    1.451    0.003 game.py:41(step)
                    437    0.002    0.000    1.368    0.003 layers.py:710(step)
                    437    0.075    0.000    1.159    0.003 allGraphsTrain.py:35(<listcomp>)
                    437    0.002    0.000    0.941    0.002 agent.py:29(learn)
                    437    0.008    0.000    0.939    0.002 agent.py:117(_learn)
                    437    0.026    0.000    0.931    0.002 learner.py:42(Qlearn)
                    437    0.031    0.000    0.863    0.002 layers.py:17(step)
                  43700    0.068    0.000    0.828    0.000 layer.py:98(move)
                  46322    0.106    0.000    0.724    0.000 tensor.py:21(wrapped)
                    437    0.031    0.000    0.676    0.002 allGraphsTrain.py:42(<listcomp>)
                    438    0.418    0.001    0.606    0.001 allGraphsTrain.py:33(<listcomp>)
                    438    0.058    0.000    0.543    0.001 layers.py:676(update)
                  43700    0.086    0.000    0.492    0.000 layers.py:727(check)
                  45885    0.481    0.000    0.481    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                  43700    0.444    0.000    0.444    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
             10051/1311    0.038    0.000    0.400    0.000 module.py:715(_call_impl)
                   5374    0.383    0.000    0.383    0.000 {built-in method tensor}
                    437    0.186    0.000    0.379    0.001 agent.py:67(modify)
                    874    0.002    0.000    0.369    0.000 network.py:24(forward)
                    437    0.003    0.000    0.363    0.001 grad_mode.py:23(decorate_context)
                    874    0.009    0.000    0.361    0.000 container.py:115(forward)
                    437    0.012    0.000    0.356    0.001 adam.py:55(step)
                   3188    0.002    0.000    0.311    0.000 game.py:37(board)
                    437    0.062    0.000    0.292    0.001 functional.py:53(adam)
                    437    0.005    0.000    0.259    0.001 agent.py:112(__call__)
                    437    0.002    0.000    0.238    0.001 tensor.py:181(backward)
                    437    0.002    0.000    0.236    0.001 __init__.py:68(backward)
                    437    0.225    0.001    0.225    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                 122390    0.063    0.000    0.219    0.000 {built-in method builtins.any}
                  43700    0.063    0.000    0.211    0.000 layers.py:721(isFree)
                 799155    0.139    0.000    0.199    0.000 enum.py:646(__hash__)
                   1001    0.006    0.000    0.189    0.000 allGraphs.py:228(getInterventions)
                   3066    0.086    0.000    0.156    0.000 layer.py:167(NoRock_update)
                 299535    0.114    0.000    0.149    0.000 layer.py:95(isFree)
                  45448    0.146    0.000    0.146    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                   1748    0.003    0.000    0.141    0.000 conv.py:422(forward)
                   1312    0.005    0.000    0.141    0.000 tensor.py:576(__iter__)
                   1748    0.003    0.000    0.137    0.000 conv.py:414(_conv_forward)
                   1748    0.133    0.000    0.133    0.000 {built-in method conv2d}
                   1312    0.132    0.000    0.132    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
                  76172    0.038    0.000    0.121    0.000 overrides.py:1070(has_torch_function)
                  43700    0.073    0.000    0.117    0.000 layers.py:595(check)
                  90122    0.027    0.000    0.117    0.000 {built-in method builtins.all}
                  43700    0.071    0.000    0.114    0.000 layers.py:625(check)
                  43700    0.070    0.000    0.114    0.000 layers.py:610(check)
                 348632    0.088    0.000    0.107    0.000 layers.py:692(<genexpr>)
                   1748    0.004    0.000    0.107    0.000 linear.py:92(forward)
                   1748    0.007    0.000    0.101    0.000 functional.py:1669(linear)
                  24526    0.055    0.000    0.092    0.000 tensor.py:933(grad)
                    221    0.002    0.000    0.087    0.000 layers.py:731(restart)
                   1000    0.018    0.000    0.085    0.000 allGraphs.py:170(bestIntervention)
                    437    0.008    0.000    0.078    0.000 optimizer.py:167(zero_grad)
                 134460    0.033    0.000    0.078    0.000 layers.py:682(<genexpr>)
                   1748    0.075    0.000    0.075    0.000 {built-in method addmm}
                 758707    0.070    0.000    0.070    0.000 layer.py:91(positions)
                    221    0.001    0.000    0.070    0.000 level.py:8(__init__)
                    437    0.003    0.000    0.064    0.000 agent.py:59(modify_board)
                    437    0.036    0.000    0.062    0.000 collector.py:53(collect)
                 799248    0.060    0.000    0.060    0.000 {built-in method builtins.hash}
                    221    0.003    0.000    0.060    0.000 levels.py:446(generate)
                   2622    0.002    0.000    0.058    0.000 activation.py:713(forward)
                   6992    0.057    0.000    0.057    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                   2622    0.004    0.000    0.055    0.000 functional.py:1292(leaky_relu)
                   1074    0.010    0.000    0.054    0.000 level.py:41(notUsed)
                      1    0.002    0.002    0.053    0.053 game.py:9(__init__)
                  43700    0.033    0.000    0.051    0.000 layers.py:581(check)
                   2622    0.051    0.000    0.051    0.000 {built-in method torch._C._nn.leaky_relu}
                 200414    0.041    0.000    0.048    0.000 overrides.py:1083(<genexpr>)
                   6992    0.047    0.000    0.047    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                      1    0.000    0.000    0.046    0.046 save.py:15(__exit__)
                      1    0.000    0.000    0.046    0.046 save.py:18(save)
                    437    0.031    0.000    0.046    0.000 allGraphsTrain.py:41(<listcomp>)
                      4    0.024    0.006    0.045    0.011 save.py:24(saveObject)
                      1    0.000    0.000    0.044    0.044 allGraphsTrain.py:22(<listcomp>)
                    437    0.003    0.000    0.043    0.000 exploration.py:47(epsilonGreedy)
                    437    0.042    0.000    0.042    0.000 {built-in method torch._C._nn.one_hot}
                   3496    0.041    0.000    0.041    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                      6    0.000    0.000    0.038    0.006 network.py:15(__init__)
                  96616    0.038    0.000    0.038    0.000 layer.py:146(elements)
                  36900    0.026    0.000    0.035    0.000 allGraphs.py:157(compress)
                   3496    0.033    0.000    0.033    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                     12    0.000    0.000    0.033    0.003 conv.py:394(__init__)
                     12    0.003    0.000    0.032    0.003 conv.py:37(__init__)
                     27    0.000    0.000    0.031    0.001 init.py:352(kaiming_uniform_)
                     54    0.029    0.001    0.029    0.001 {method 'uniform_' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-5>
Subject: Job 9505746: <causal7_online_0> in cluster <dcc> Done

Job <causal7_online_0> was submitted from host <n-62-30-2> by user <s183905> in cluster <dcc> at Thu Apr  8 23:40:14 2021
Job was executed on host(s) <n-62-20-5>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Thu Apr  8 23:46:46 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Apr  8 23:46:46 2021
Terminated at Thu Apr  8 23:47:17 2021
Results reported at Thu Apr  8 23:47:17 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=16G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 1440
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $LSB_PROJECT_NAME


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   22.79 sec.
    Max Memory :                                 2084 MB
    Average Memory :                             2084.00 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14300.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   32 sec.
    Turnaround time :                            423 sec.

The output (if any) is above this job summary.

