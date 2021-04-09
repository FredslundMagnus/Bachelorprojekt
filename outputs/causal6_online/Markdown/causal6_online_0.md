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
KeyError: frozenset({<LayerType.Greenup: 25>})


# Parameters

    Name :                      causal6_online-0
    Main :                      graphTrain
    Level :                     Levels.Causal6
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
    Counterfacts :              1
    Topn :                      7
    Minutes used :              0 minutes.
    Hours used :                0 hours.

# Profiling


      14129351 function calls (14114908 primitive calls) in 42.89 seconds

##    Ordered by: cumulative time
   List reduced from 419 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000   42.888   42.888 {built-in method builtins.exec}
                      1    0.000    0.000   42.888   42.888 <string>:1(<module>)
                      1    0.171    0.171   42.888   42.888 allGraphsTrain.py:5(graphTrain)
                    704    6.076    0.009   14.712    0.021 allGraphs.py:220(transformNot)
                 845200    9.751    0.000    9.751    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                  71205    2.162    0.000    9.556    0.000 allGraphs.py:141(states)
                    704    0.016    0.000    9.526    0.014 allGraphsTrain.py:27(<listcomp>)
                      2    0.000    0.000    8.101    4.051 agent.py:16(__init__)
                      2    0.000    0.000    8.101    4.050 network.py:33(__init__)
                      1    0.000    0.000    8.093    8.093 agent.py:109(__init__)
                      6    0.000    0.000    8.061    1.344 module.py:529(to)
                   72/6    0.001    0.000    8.061    1.344 module.py:357(_apply)
                    757    8.060    0.011    8.061    0.011 {method 'to' of 'torch._C._TensorBase' objects}
                     54    0.000    0.000    8.059    0.149 module.py:607(convert)
                 774900    6.931    0.000    6.931    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                    703    0.003    0.000    2.853    0.004 game.py:41(step)
                    703    0.003    0.000    2.708    0.004 layers.py:710(step)
                    703    0.121    0.000    1.886    0.003 allGraphsTrain.py:35(<listcomp>)
                    703    0.050    0.000    1.665    0.002 layers.py:17(step)
                  70300    0.111    0.000    1.609    0.000 layer.py:98(move)
                    703    0.003    0.000    1.523    0.002 agent.py:29(learn)
                    703    0.015    0.000    1.520    0.002 agent.py:117(_learn)
                    703    0.044    0.000    1.505    0.002 learner.py:42(Qlearn)
                  74518    0.165    0.000    1.167    0.000 tensor.py:21(wrapped)
                    703    0.050    0.000    1.093    0.002 allGraphsTrain.py:42(<listcomp>)
                    704    0.095    0.000    1.086    0.002 layers.py:676(update)
                    704    0.679    0.001    1.055    0.001 allGraphsTrain.py:33(<listcomp>)
                  70300    0.172    0.000    1.025    0.000 layers.py:727(check)
                  73815    0.787    0.000    0.787    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                  70300    0.731    0.000    0.731    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                   8389    0.650    0.000    0.650    0.000 {built-in method tensor}
             16169/2109    0.062    0.000    0.629    0.000 module.py:715(_call_impl)
                    703    0.309    0.000    0.619    0.001 agent.py:67(modify)
                    703    0.004    0.000    0.588    0.001 grad_mode.py:23(decorate_context)
                   1406    0.004    0.000    0.577    0.000 network.py:24(forward)
                    703    0.020    0.000    0.576    0.001 adam.py:55(step)
                   1406    0.014    0.000    0.564    0.000 container.py:115(forward)
                   4874    0.004    0.000    0.529    0.000 game.py:37(board)
                    703    0.103    0.000    0.472    0.001 functional.py:53(adam)
                1789424    0.298    0.000    0.430    0.000 enum.py:646(__hash__)
                    703    0.009    0.000    0.396    0.001 agent.py:112(__call__)
                 196741    0.107    0.000    0.391    0.000 {built-in method builtins.any}
                  70300    0.113    0.000    0.378    0.000 layers.py:721(isFree)
                   1357    0.009    0.000    0.376    0.000 allGraphs.py:228(getInterventions)
                    703    0.004    0.000    0.373    0.001 tensor.py:181(backward)
                    703    0.003    0.000    0.369    0.001 __init__.py:68(backward)
                    703    0.350    0.000    0.350    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                 144918    0.047    0.000    0.285    0.000 {built-in method builtins.all}
                  70300    0.176    0.000    0.284    0.000 layers.py:418(check)
                   5632    0.155    0.000    0.283    0.000 layer.py:167(NoRock_update)
                 503192    0.203    0.000    0.264    0.000 layer.py:95(isFree)
                   2110    0.008    0.000    0.235    0.000 tensor.py:576(__iter__)
                  73112    0.228    0.000    0.228    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                   2812    0.005    0.000    0.223    0.000 conv.py:422(forward)
                   2110    0.221    0.000    0.221    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
                 242913    0.062    0.000    0.219    0.000 layers.py:682(<genexpr>)
                   1353    0.046    0.000    0.217    0.000 allGraphs.py:170(bestIntervention)
                   2812    0.005    0.000    0.216    0.000 conv.py:414(_conv_forward)
                   2812    0.210    0.000    0.210    0.000 {built-in method conv2d}
                 630018    0.169    0.000    0.205    0.000 layers.py:692(<genexpr>)
                 122456    0.061    0.000    0.197    0.000 overrides.py:1070(has_torch_function)
                  70300    0.122    0.000    0.193    0.000 layers.py:446(check)
                  70300    0.117    0.000    0.186    0.000 layers.py:431(check)
                    398    0.004    0.000    0.184    0.000 layers.py:731(restart)
                   2812    0.007    0.000    0.166    0.000 linear.py:92(forward)
                   2812    0.012    0.000    0.156    0.000 functional.py:1669(linear)
                    398    0.002    0.000    0.151    0.000 level.py:8(__init__)
                  39422    0.090    0.000    0.150    0.000 tensor.py:933(grad)
                1454253    0.142    0.000    0.142    0.000 layer.py:91(positions)
                1789517    0.132    0.000    0.132    0.000 {built-in method builtins.hash}
                    398    0.006    0.000    0.131    0.000 levels.py:293(generate)
                    703    0.013    0.000    0.129    0.000 optimizer.py:167(zero_grad)
                   2406    0.022    0.000    0.120    0.000 level.py:41(notUsed)
                   2812    0.113    0.000    0.113    0.000 {built-in method addmm}
                  70400    0.068    0.000    0.107    0.000 layers.py:451(isDone)
                    703    0.005    0.000    0.106    0.000 agent.py:59(modify_board)
                    703    0.060    0.000    0.102    0.000 collector.py:53(collect)
                  50229    0.056    0.000    0.096    0.000 allGraphs.py:150(expand)
                  11248    0.093    0.000    0.093    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                  70300    0.055    0.000    0.086    0.000 layers.py:396(check)
                  70300    0.055    0.000    0.085    0.000 layers.py:407(check)
                   4218    0.004    0.000    0.085    0.000 activation.py:713(forward)
                   4218    0.007    0.000    0.081    0.000 functional.py:1292(leaky_relu)
                 322242    0.066    0.000    0.078    0.000 overrides.py:1083(<genexpr>)
                    703    0.052    0.000    0.077    0.000 allGraphsTrain.py:41(<listcomp>)
                  11248    0.077    0.000    0.077    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                   4218    0.073    0.000    0.073    0.000 {built-in method torch._C._nn.leaky_relu}
                    703    0.004    0.000    0.070    0.000 exploration.py:47(epsilonGreedy)
                    703    0.070    0.000    0.070    0.000 {built-in method torch._C._nn.one_hot}
                 161651    0.069    0.000    0.069    0.000 layer.py:146(elements)
                  71314    0.051    0.000    0.068    0.000 allGraphs.py:157(compress)
                    704    0.016    0.000    0.061    0.000 allGraphs.py:209(transform)
                   5624    0.061    0.000    0.061    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                      1    0.002    0.002    0.061    0.061 game.py:9(__init__)
                   2406    0.002    0.000    0.056    0.000 level.py:38(elementsIn)
                   5624    0.054    0.000    0.054    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                 503192    0.050    0.000    0.050    0.000 layer.py:203(isBlocking)
          632956/632954    0.037    0.000    0.048    0.000 {built-in method builtins.len}
                      1    0.000    0.000    0.048    0.048 save.py:15(__exit__)
                      1    0.000    0.000    0.048    0.048 save.py:18(save)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-3>
Subject: Job 9507029: <causal6_online_0> in cluster <dcc> Done

Job <causal6_online_0> was submitted from host <n-62-27-21> by user <s183905> in cluster <dcc> at Fri Apr  9 15:59:44 2021
Job was executed on host(s) <n-62-20-3>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Fri Apr  9 16:07:11 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Fri Apr  9 16:07:11 2021
Terminated at Fri Apr  9 16:07:59 2021
Results reported at Fri Apr  9 16:07:59 2021

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

    CPU time :                                   39.00 sec.
    Max Memory :                                 2078 MB
    Average Memory :                             2078.00 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14306.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   49 sec.
    Turnaround time :                            495 sec.

The output (if any) is above this job summary.

[<LayerType.Greendown: 24>, <LayerType.Greenup: 25>, <LayerType.Greenstar: 26>, <LayerType.Yellowstar: 27>, <LayerType.Bluestar: 28>]
Levels.Causal6
{<LayerType.Greendown: 24>: {frozenset(): 1, frozenset({<LayerType.Greenup: 25>}): 1, frozenset({<LayerType.Greenstar: 26>}): 1, frozenset({<LayerType.Yellowstar: 27>}): 1, frozenset({<LayerType.Bluestar: 28>}): 1, frozenset({<LayerType.Greenup: 25>, <LayerType.Greenstar: 26>}): 1, frozenset({<LayerType.Greenup: 25>, <LayerType.Yellowstar: 27>}): 1, frozenset({<LayerType.Greenup: 25>, <LayerType.Bluestar: 28>}): 1, frozenset({<LayerType.Yellowstar: 27>, <LayerType.Greenstar: 26>}): 1, frozenset({<LayerType.Greenstar: 26>, <LayerType.Bluestar: 28>}): 1, frozenset({<LayerType.Yellowstar: 27>, <LayerType.Bluestar: 28>}): 1, frozenset({<LayerType.Greenup: 25>, <LayerType.Yellowstar: 27>, <LayerType.Greenstar: 26>}): 1, frozenset({<LayerType.Greenup: 25>, <LayerType.Greenstar: 26>, <LayerType.Bluestar: 28>}): 1, frozenset({<LayerType.Greenup: 25>, <LayerType.Yellowstar: 27>, <LayerType.Bluestar: 28>}): 1, frozenset({<LayerType.Yellowstar: 27>, <LayerType.Greenstar: 26>, <LayerType.Bluestar: 28>}): 1, frozenset({<LayerType.Greenup: 25>, <LayerType.Yellowstar: 27>, <LayerType.Greenstar: 26>, <LayerType.Bluestar: 28>}): 1}, <LayerType.Greenup: 25>: {frozenset(): 1, frozenset({<LayerType.Greendown: 24>}): 1, frozenset({<LayerType.Greenstar: 26>}): 1, frozenset({<LayerType.Yellowstar: 27>}): 1, frozenset({<LayerType.Bluestar: 28>}): 1, frozenset({<LayerType.Greendown: 24>, <LayerType.Greenstar: 26>}): 1, frozenset({<LayerType.Greendown: 24>, <LayerType.Yellowstar: 27>}): 1, frozenset({<LayerType.Greendown: 24>, <LayerType.Bluestar: 28>}): 1, frozenset({<LayerType.Yellowstar: 27>, <LayerType.Greenstar: 26>}): 1, frozenset({<LayerType.Greenstar: 26>, <LayerType.Bluestar: 28>}): 1, frozenset({<LayerType.Yellowstar: 27>, <LayerType.Bluestar: 28>}): 1, frozenset({<LayerType.Greendown: 24>, <LayerType.Yellowstar: 27>, <LayerType.Greenstar: 26>}): 1, frozenset({<LayerType.Greendown: 24>, <LayerType.Greenstar: 26>, <LayerType.Bluestar: 28>}): 1, frozenset({<LayerType.Greendown: 24>, <LayerType.Yellowstar: 27>, <LayerType.Bluestar: 28>}): 1, frozenset({<LayerType.Yellowstar: 27>, <LayerType.Greenstar: 26>, <LayerType.Bluestar: 28>}): 1, frozenset({<LayerType.Greendown: 24>, <LayerType.Yellowstar: 27>, <LayerType.Greenstar: 26>, <LayerType.Bluestar: 28>}): 1}, <LayerType.Greenstar: 26>: {frozenset(): 1, frozenset({<LayerType.Greendown: 24>}): 1, frozenset({<LayerType.Greenup: 25>}): 1, frozenset({<LayerType.Yellowstar: 27>}): 1, frozenset({<LayerType.Bluestar: 28>}): 1, frozenset({<LayerType.Greenup: 25>, <LayerType.Greendown: 24>}): 1, frozenset({<LayerType.Greendown: 24>, <LayerType.Yellowstar: 27>}): 1, frozenset({<LayerType.Greendown: 24>, <LayerType.Bluestar: 28>}): 1, frozenset({<LayerType.Greenup: 25>, <LayerType.Yellowstar: 27>}): 1, frozenset({<LayerType.Greenup: 25>, <LayerType.Bluestar: 28>}): 1, frozenset({<LayerType.Yellowstar: 27>, <LayerType.Bluestar: 28>}): 1, frozenset({<LayerType.Greenup: 25>, <LayerType.Greendown: 24>, <LayerType.Yellowstar: 27>}): 1, frozenset({<LayerType.Greenup: 25>, <LayerType.Greendown: 24>, <LayerType.Bluestar: 28>}): 1, frozenset({<LayerType.Greendown: 24>, <LayerType.Yellowstar: 27>, <LayerType.Bluestar: 28>}): 1, frozenset({<LayerType.Greenup: 25>, <LayerType.Yellowstar: 27>, <LayerType.Bluestar: 28>}): 1, frozenset({<LayerType.Greenup: 25>, <LayerType.Greendown: 24>, <LayerType.Yellowstar: 27>, <LayerType.Bluestar: 28>}): 1}, <LayerType.Yellowstar: 27>: {frozenset(): 1, frozenset({<LayerType.Greendown: 24>}): 1, frozenset({<LayerType.Greenup: 25>}): 1, frozenset({<LayerType.Greenstar: 26>}): 1, frozenset({<LayerType.Bluestar: 28>}): 1, frozenset({<LayerType.Greenup: 25>, <LayerType.Greendown: 24>}): 1, frozenset({<LayerType.Greendown: 24>, <LayerType.Greenstar: 26>}): 1, frozenset({<LayerType.Greendown: 24>, <LayerType.Bluestar: 28>}): 1, frozenset({<LayerType.Greenup: 25>, <LayerType.Greenstar: 26>}): 1, frozenset({<LayerType.Greenup: 25>, <LayerType.Bluestar: 28>}): 1, frozenset({<LayerType.Greenstar: 26>, <LayerType.Bluestar: 28>}): 1, frozenset({<LayerType.Greenup: 25>, <LayerType.Greendown: 24>, <LayerType.Greenstar: 26>}): 1, frozenset({<LayerType.Greenup: 25>, <LayerType.Greendown: 24>, <LayerType.Bluestar: 28>}): 1, frozenset({<LayerType.Greendown: 24>, <LayerType.Greenstar: 26>, <LayerType.Bluestar: 28>}): 1, frozenset({<LayerType.Greenup: 25>, <LayerType.Greenstar: 26>, <LayerType.Bluestar: 28>}): 1, frozenset({<LayerType.Greenup: 25>, <LayerType.Greendown: 24>, <LayerType.Greenstar: 26>, <LayerType.Bluestar: 28>}): 1}, <LayerType.Bluestar: 28>: {frozenset(): 1, frozenset({<LayerType.Greendown: 24>}): 1, frozenset({<LayerType.Greenup: 25>}): 1, frozenset({<LayerType.Greenstar: 26>}): 1, frozenset({<LayerType.Yellowstar: 27>}): 1, frozenset({<LayerType.Greenup: 25>, <LayerType.Greendown: 24>}): 1, frozenset({<LayerType.Greendown: 24>, <LayerType.Greenstar: 26>}): 1, frozenset({<LayerType.Greendown: 24>, <LayerType.Yellowstar: 27>}): 1, frozenset({<LayerType.Greenup: 25>, <LayerType.Greenstar: 26>}): 1, frozenset({<LayerType.Greenup: 25>, <LayerType.Yellowstar: 27>}): 1, frozenset({<LayerType.Yellowstar: 27>, <LayerType.Greenstar: 26>}): 1, frozenset({<LayerType.Greenup: 25>, <LayerType.Greendown: 24>, <LayerType.Greenstar: 26>}): 1, frozenset({<LayerType.Greenup: 25>, <LayerType.Greendown: 24>, <LayerType.Yellowstar: 27>}): 1, frozenset({<LayerType.Greendown: 24>, <LayerType.Yellowstar: 27>, <LayerType.Greenstar: 26>}): 1, frozenset({<LayerType.Greenup: 25>, <LayerType.Yellowstar: 27>, <LayerType.Greenstar: 26>}): 1, frozenset({<LayerType.Greenup: 25>, <LayerType.Greendown: 24>, <LayerType.Yellowstar: 27>, <LayerType.Greenstar: 26>}): 1}, <LayerType.Goal: 3>: {frozenset(): 1, frozenset({<LayerType.Greendown: 24>}): 1, frozenset({<LayerType.Greenup: 25>}): 1, frozenset({<LayerType.Greenstar: 26>}): 1, frozenset({<LayerType.Yellowstar: 27>}): 1, frozenset({<LayerType.Bluestar: 28>}): 1, frozenset({<LayerType.Greenup: 25>, <LayerType.Greendown: 24>}): 1, frozenset({<LayerType.Greendown: 24>, <LayerType.Greenstar: 26>}): 1, frozenset({<LayerType.Greendown: 24>, <LayerType.Yellowstar: 27>}): 1, frozenset({<LayerType.Greendown: 24>, <LayerType.Bluestar: 28>}): 1, frozenset({<LayerType.Greenup: 25>, <LayerType.Greenstar: 26>}): 1, frozenset({<LayerType.Greenup: 25>, <LayerType.Yellowstar: 27>}): 1, frozenset({<LayerType.Greenup: 25>, <LayerType.Bluestar: 28>}): 1, frozenset({<LayerType.Yellowstar: 27>, <LayerType.Greenstar: 26>}): 1, frozenset({<LayerType.Greenstar: 26>, <LayerType.Bluestar: 28>}): 1, frozenset({<LayerType.Yellowstar: 27>, <LayerType.Bluestar: 28>}): 1, frozenset({<LayerType.Greenup: 25>, <LayerType.Greendown: 24>, <LayerType.Greenstar: 26>}): 1, frozenset({<LayerType.Greenup: 25>, <LayerType.Greendown: 24>, <LayerType.Yellowstar: 27>}): 1, frozenset({<LayerType.Greenup: 25>, <LayerType.Greendown: 24>, <LayerType.Bluestar: 28>}): 1, frozenset({<LayerType.Greendown: 24>, <LayerType.Yellowstar: 27>, <LayerType.Greenstar: 26>}): 1, frozenset({<LayerType.Greendown: 24>, <LayerType.Greenstar: 26>, <LayerType.Bluestar: 28>}): 1, frozenset({<LayerType.Greendown: 24>, <LayerType.Yellowstar: 27>, <LayerType.Bluestar: 28>}): 1, frozenset({<LayerType.Greenup: 25>, <LayerType.Yellowstar: 27>, <LayerType.Greenstar: 26>}): 1, frozenset({<LayerType.Greenup: 25>, <LayerType.Greenstar: 26>, <LayerType.Bluestar: 28>}): 1, frozenset({<LayerType.Greenup: 25>, <LayerType.Yellowstar: 27>, <LayerType.Bluestar: 28>}): 1, frozenset({<LayerType.Yellowstar: 27>, <LayerType.Greenstar: 26>, <LayerType.Bluestar: 28>}): 1, frozenset({<LayerType.Greenup: 25>, <LayerType.Greendown: 24>, <LayerType.Yellowstar: 27>, <LayerType.Greenstar: 26>}): 1, frozenset({<LayerType.Greenup: 25>, <LayerType.Greendown: 24>, <LayerType.Greenstar: 26>, <LayerType.Bluestar: 28>}): 1, frozenset({<LayerType.Greenup: 25>, <LayerType.Greendown: 24>, <LayerType.Yellowstar: 27>, <LayerType.Bluestar: 28>}): 1, frozenset({<LayerType.Greendown: 24>, <LayerType.Yellowstar: 27>, <LayerType.Greenstar: 26>, <LayerType.Bluestar: 28>}): 1, frozenset({<LayerType.Greenup: 25>, <LayerType.Yellowstar: 27>, <LayerType.Greenstar: 26>, <LayerType.Bluestar: 28>}): 1, frozenset({<LayerType.Yellowstar: 27>, <LayerType.Bluestar: 28>, <LayerType.Greenup: 25>, <LayerType.Greenstar: 26>, <LayerType.Greendown: 24>}): 1}}
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
  File "/zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/allGraphsTrain.py", line 39, in graphTrain
    interventions = [(getInterventions(env, state, data, layers, exploration) if should else old) for state, should, old in zip(new_states, shouldInterviene, interventions)]
  File "/zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/allGraphsTrain.py", line 39, in <listcomp>
    interventions = [(getInterventions(env, state, data, layers, exploration) if should else old) for state, should, old in zip(new_states, shouldInterviene, interventions)]
  File "/zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/allGraphs.py", line 232, in getInterventions
    best = env.layers.types.index(rightIntervention(state, data, layers))
  File "/zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/allGraphs.py", line 198, in rightIntervention
    chances = {layer: flip_chance(state, layer, data) for layer in max(stats, key=stats.get) if layer not in stats and layer not in used}
  File "/zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/allGraphs.py", line 198, in <dictcomp>
    chances = {layer: flip_chance(state, layer, data) for layer in max(stats, key=stats.get) if layer not in stats and layer not in used}
  File "/zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/allGraphs.py", line 166, in flip_chance
    chanceForFlip *= (1 - data[layer][partial])
KeyError: frozenset({<LayerType.Greenup: 25>})


# Parameters

    Name :                      causal6_online-0
    Main :                      graphTrain
    Level :                     Levels.Causal6
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
    Counterfacts :              1
    Topn :                      7
    Minutes used :              1 minutes.
    Hours used :                0 hours.

# Profiling


      36162253 function calls (36125450 primitive calls) in 108.56 seconds

##    Ordered by: cumulative time
   List reduced from 425 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000  108.561  108.561 {built-in method builtins.exec}
                      1    0.000    0.000  108.561  108.561 <string>:1(<module>)
                      1    0.678    0.678  108.561  108.561 allGraphsTrain.py:6(graphTrain)
                   1822   16.811    0.009   41.791    0.023 allGraphs.py:220(transformNot)
                2186808   29.348    0.000   29.348    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                 184123    6.044    0.000   27.320    0.000 allGraphs.py:141(states)
                   1822    0.051    0.000   27.319    0.015 allGraphsTrain.py:33(<listcomp>)
                2004700   18.824    0.000   18.824    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                   1821    0.012    0.000    8.422    0.005 game.py:41(step)
                   1821    0.015    0.000    7.989    0.004 layers.py:710(step)
                      2    0.000    0.000    7.971    3.985 agent.py:16(__init__)
                      2    0.000    0.000    7.970    3.985 network.py:33(__init__)
                      1    0.000    0.000    7.962    7.962 agent.py:109(__init__)
                   1875    7.932    0.004    7.935    0.004 {method 'to' of 'torch._C._TensorBase' objects}
                      6    0.000    0.000    7.930    1.322 module.py:529(to)
                   72/6    0.001    0.000    7.930    1.322 module.py:357(_apply)
                     54    0.000    0.000    7.928    0.147 module.py:607(convert)
                   1821    0.338    0.000    5.424    0.003 allGraphsTrain.py:41(<listcomp>)
                   1821    0.173    0.000    4.944    0.003 layers.py:17(step)
                 182100    0.320    0.000    4.754    0.000 layer.py:98(move)
                   1821    0.011    0.000    4.692    0.003 agent.py:29(learn)
                   1821    0.053    0.000    4.677    0.003 agent.py:117(_learn)
                   1821    0.155    0.000    4.623    0.003 learner.py:42(Qlearn)
                 193026    0.470    0.000    3.245    0.000 tensor.py:21(wrapped)
                   1822    2.150    0.001    3.121    0.002 allGraphsTrain.py:39(<listcomp>)
                   1822    0.289    0.000    3.064    0.002 layers.py:676(update)
                   1821    0.141    0.000    3.020    0.002 allGraphsTrain.py:48(<listcomp>)
                 182100    0.433    0.000    2.839    0.000 layers.py:727(check)
                 191205    2.192    0.000    2.192    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
             41883/5463    0.224    0.000    2.104    0.000 module.py:715(_call_impl)
                 182100    1.989    0.000    1.989    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                   1821    0.943    0.001    1.966    0.001 agent.py:67(modify)
                  21206    1.931    0.000    1.931    0.000 {built-in method tensor}
                   3642    0.014    0.000    1.903    0.001 network.py:24(forward)
                   3642    0.049    0.000    1.854    0.001 container.py:115(forward)
                   1821    0.016    0.000    1.678    0.001 grad_mode.py:23(decorate_context)
                   1821    0.067    0.000    1.630    0.001 adam.py:55(step)
                  12114    0.019    0.000    1.552    0.000 game.py:37(board)
                   1821    0.046    0.000    1.377    0.001 agent.py:112(__call__)
                   1821    0.292    0.000    1.325    0.001 functional.py:53(adam)
                 182100    0.319    0.000    1.305    0.000 layers.py:721(isFree)
                4495740    0.824    0.000    1.191    0.000 enum.py:646(__hash__)
                   1821    0.014    0.000    1.173    0.001 tensor.py:181(backward)
                   1821    0.011    0.000    1.159    0.001 __init__.py:68(backward)
                   1821    1.094    0.001    1.094    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                 509515    0.298    0.000    1.057    0.000 {built-in method builtins.any}
                1378221    0.815    0.000    0.986    0.000 layer.py:95(isFree)
                   3007    0.031    0.000    0.971    0.000 allGraphs.py:228(getInterventions)
                  14576    0.493    0.000    0.894    0.000 layer.py:167(NoRock_update)
                 182100    0.528    0.000    0.841    0.000 layers.py:418(check)
                   5464    0.039    0.000    0.841    0.000 tensor.py:576(__iter__)
                 375226    0.129    0.000    0.786    0.000 {built-in method builtins.all}
                   5464    0.776    0.000    0.776    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
                   7284    0.018    0.000    0.767    0.000 conv.py:422(forward)
                   7284    0.026    0.000    0.742    0.000 conv.py:414(_conv_forward)
                   7284    0.713    0.000    0.713    0.000 {built-in method conv2d}
                 189384    0.660    0.000    0.660    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                 619449    0.172    0.000    0.608    0.000 layers.py:682(<genexpr>)
                 316988    0.169    0.000    0.550    0.000 overrides.py:1070(has_torch_function)
                   7284    0.022    0.000    0.546    0.000 linear.py:92(forward)
                1631952    0.443    0.000    0.539    0.000 layers.py:692(<genexpr>)
                 182100    0.333    0.000    0.526    0.000 layers.py:446(check)
                   2996    0.113    0.000    0.524    0.000 allGraphs.py:170(bestIntervention)
                 182100    0.334    0.000    0.522    0.000 layers.py:431(check)
                   7284    0.040    0.000    0.514    0.000 functional.py:1669(linear)
                    872    0.012    0.000    0.451    0.001 layers.py:731(restart)
                 102030    0.250    0.000    0.414    0.000 tensor.py:933(grad)
                   1821    0.024    0.000    0.386    0.000 agent.py:59(modify_board)
                   7284    0.376    0.000    0.376    0.000 {built-in method addmm}
                3775263    0.373    0.000    0.373    0.000 layer.py:91(positions)
                4495833    0.368    0.000    0.368    0.000 {built-in method builtins.hash}
                    872    0.006    0.000    0.366    0.000 level.py:8(__init__)
                   1821    0.036    0.000    0.355    0.000 optimizer.py:167(zero_grad)
                    872    0.015    0.000    0.311    0.000 levels.py:293(generate)
                   1821    0.171    0.000    0.294    0.000 collector.py:53(collect)
                 182200    0.181    0.000    0.291    0.000 layers.py:436(isDone)
                   1821    0.016    0.000    0.285    0.000 exploration.py:47(epsilonGreedy)
                   5231    0.054    0.000    0.281    0.000 level.py:41(notUsed)
                  29136    0.263    0.000    0.263    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                   1821    0.250    0.000    0.250    0.000 {built-in method torch._C._nn.one_hot}
                   1821    0.179    0.000    0.249    0.000 allGraphsTrain.py:47(<listcomp>)
                  10926    0.017    0.000    0.245    0.000 activation.py:713(forward)
                 182100    0.154    0.000    0.236    0.000 layers.py:407(check)
                   1822    0.061    0.000    0.234    0.000 allGraphs.py:209(transform)
                 182100    0.152    0.000    0.232    0.000 layers.py:396(check)
                 406045    0.229    0.000    0.229    0.000 layer.py:146(elements)
                  10926    0.030    0.000    0.228    0.000 functional.py:1292(leaky_relu)
                  99762    0.130    0.000    0.221    0.000 allGraphs.py:150(expand)
                 834286    0.184    0.000    0.218    0.000 overrides.py:1083(<genexpr>)
                  29136    0.213    0.000    0.213    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                  10926    0.196    0.000    0.196    0.000 {built-in method torch._C._nn.leaky_relu}
                 166339    0.139    0.000    0.187    0.000 allGraphs.py:157(compress)
                   5465    0.178    0.000    0.178    0.000 {method 'tolist' of 'torch._C._TensorBase' objects}
                   1806    0.084    0.000    0.173    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                   3642    0.167    0.000    0.167    0.000 {built-in method cat}
                  14568    0.159    0.000    0.159    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                  14568    0.149    0.000    0.149    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                1378221    0.141    0.000    0.141    0.000 layer.py:203(isBlocking)
        1628519/1628517    0.104    0.000    0.136    0.000 {built-in method builtins.len}
                   9105    0.131    0.000    0.131    0.000 {built-in method sum}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-12>
Subject: Job 9507135: <causal6_online_0> in cluster <dcc> Done

Job <causal6_online_0> was submitted from host <n-62-27-21> by user <s183905> in cluster <dcc> at Fri Apr  9 17:22:04 2021
Job was executed on host(s) <n-62-20-12>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Fri Apr  9 17:33:58 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Fri Apr  9 17:33:58 2021
Terminated at Fri Apr  9 17:35:53 2021
Results reported at Fri Apr  9 17:35:53 2021

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

    CPU time :                                   105.61 sec.
    Max Memory :                                 2080 MB
    Average Memory :                             2070.33 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14304.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   115 sec.
    Turnaround time :                            829 sec.

The output (if any) is above this job summary.

