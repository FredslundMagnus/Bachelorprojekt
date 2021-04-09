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
KeyError: frozenset({<LayerType.Purplecross: 34>})


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
    Counterfacts :              1
    Topn :                      7
    Minutes used :              0 minutes.
    Hours used :                0 hours.

# Profiling


      5124025 function calls (5117782 primitive calls) in 20.70 seconds

##    Ordered by: cumulative time
   List reduced from 419 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000   20.698   20.698 {built-in method builtins.exec}
                      1    0.000    0.000   20.698   20.698 <string>:1(<module>)
                      1    0.075    0.075   20.697   20.697 allGraphsTrain.py:5(graphTrain)
                      2    0.000    0.000    8.179    4.089 agent.py:16(__init__)
                      2    0.000    0.000    8.178    4.089 network.py:33(__init__)
                      1    0.000    0.000    8.170    8.170 agent.py:109(__init__)
                      6    0.000    0.000    8.138    1.356 module.py:529(to)
                   72/6    0.001    0.000    8.138    1.356 module.py:357(_apply)
                    347    8.135    0.023    8.137    0.023 {method 'to' of 'torch._C._TensorBase' objects}
                     54    0.000    0.000    8.136    0.151 module.py:607(convert)
                    294    2.099    0.007    5.092    0.017 allGraphs.py:220(transformNot)
                 294300    3.378    0.000    3.378    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                  29795    0.728    0.000    3.212    0.000 allGraphs.py:141(states)
                    294    0.007    0.000    3.175    0.011 allGraphsTrain.py:27(<listcomp>)
                 265000    2.369    0.000    2.369    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                    293    0.001    0.000    0.965    0.003 game.py:41(step)
                    293    0.001    0.000    0.909    0.003 layers.py:710(step)
                    293    0.050    0.000    0.775    0.003 allGraphsTrain.py:35(<listcomp>)
                    293    0.001    0.000    0.655    0.002 agent.py:29(learn)
                    293    0.006    0.000    0.653    0.002 agent.py:117(_learn)
                    293    0.018    0.000    0.648    0.002 learner.py:42(Qlearn)
                    293    0.020    0.000    0.575    0.002 layers.py:17(step)
                  29300    0.045    0.000    0.552    0.000 layer.py:98(move)
                  31058    0.069    0.000    0.489    0.000 tensor.py:21(wrapped)
                    293    0.021    0.000    0.453    0.002 allGraphsTrain.py:42(<listcomp>)
                    294    0.281    0.001    0.424    0.001 allGraphsTrain.py:33(<listcomp>)
                    294    0.039    0.000    0.370    0.001 layers.py:676(update)
                  29300    0.058    0.000    0.328    0.000 layers.py:727(check)
                  30765    0.325    0.000    0.325    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                  29300    0.298    0.000    0.298    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               6739/879    0.025    0.000    0.289    0.000 module.py:715(_call_impl)
                    586    0.001    0.000    0.267    0.000 network.py:24(forward)
                   3692    0.266    0.000    0.266    0.000 {built-in method tensor}
                    586    0.006    0.000    0.262    0.000 container.py:115(forward)
                    293    0.125    0.000    0.260    0.001 agent.py:67(modify)
                    293    0.002    0.000    0.249    0.001 grad_mode.py:23(decorate_context)
                    293    0.008    0.000    0.244    0.001 adam.py:55(step)
                   2225    0.002    0.000    0.218    0.000 game.py:37(board)
                    293    0.041    0.000    0.201    0.001 functional.py:53(adam)
                    293    0.003    0.000    0.191    0.001 agent.py:112(__call__)
                    293    0.002    0.000    0.174    0.001 tensor.py:181(backward)
                    293    0.001    0.000    0.172    0.001 __init__.py:68(backward)
                    293    0.165    0.001    0.165    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                  82129    0.042    0.000    0.145    0.000 {built-in method builtins.any}
                    758    0.005    0.000    0.144    0.000 allGraphs.py:228(getInterventions)
                  29300    0.040    0.000    0.141    0.000 layers.py:721(isFree)
                 546581    0.093    0.000    0.134    0.000 enum.py:646(__hash__)
                   2058    0.058    0.000    0.105    0.000 layer.py:167(NoRock_update)
                   1172    0.002    0.000    0.103    0.000 conv.py:422(forward)
                 196866    0.075    0.000    0.101    0.000 layer.py:95(isFree)
                   1172    0.002    0.000    0.101    0.000 conv.py:414(_conv_forward)
                   1172    0.098    0.000    0.098    0.000 {built-in method conv2d}
                    880    0.004    0.000    0.096    0.000 tensor.py:576(__iter__)
                  30472    0.095    0.000    0.095    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                    880    0.090    0.000    0.090    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
                  60458    0.019    0.000    0.084    0.000 {built-in method builtins.all}
                  51116    0.026    0.000    0.082    0.000 overrides.py:1070(has_torch_function)
                  29300    0.048    0.000    0.078    0.000 layers.py:595(check)
                   1172    0.003    0.000    0.078    0.000 linear.py:92(forward)
                  29300    0.048    0.000    0.077    0.000 layers.py:625(check)
                  29300    0.046    0.000    0.075    0.000 layers.py:610(check)
                   1172    0.005    0.000    0.074    0.000 functional.py:1669(linear)
                 233904    0.058    0.000    0.070    0.000 layers.py:692(<genexpr>)
                    757    0.013    0.000    0.064    0.000 allGraphs.py:170(bestIntervention)
                  16462    0.037    0.000    0.061    0.000 tensor.py:933(grad)
                    162    0.001    0.000    0.059    0.000 layers.py:731(restart)
                 104091    0.026    0.000    0.057    0.000 layers.py:682(<genexpr>)
                   1172    0.056    0.000    0.056    0.000 {built-in method addmm}
                    293    0.005    0.000    0.053    0.000 optimizer.py:167(zero_grad)
                      1    0.000    0.000    0.051    0.051 save.py:15(__exit__)
                      1    0.000    0.000    0.051    0.051 save.py:18(save)
                      1    0.002    0.002    0.050    0.050 game.py:9(__init__)
                      4    0.025    0.006    0.049    0.012 save.py:24(saveObject)
                    162    0.001    0.000    0.047    0.000 level.py:8(__init__)
                 514293    0.046    0.000    0.046    0.000 layer.py:91(positions)
                   1758    0.002    0.000    0.045    0.000 activation.py:713(forward)
                      1    0.000    0.000    0.044    0.044 allGraphsTrain.py:22(<listcomp>)
                    293    0.002    0.000    0.044    0.000 agent.py:59(modify_board)
                   1758    0.003    0.000    0.043    0.000 functional.py:1292(leaky_relu)
                    293    0.025    0.000    0.042    0.000 collector.py:53(collect)
                 546674    0.041    0.000    0.041    0.000 {built-in method builtins.hash}
                    162    0.002    0.000    0.041    0.000 levels.py:446(generate)
                      6    0.000    0.000    0.040    0.007 network.py:15(__init__)
                   1758    0.040    0.000    0.040    0.000 {built-in method torch._C._nn.leaky_relu}
                   4688    0.038    0.000    0.038    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                    754    0.007    0.000    0.037    0.000 level.py:41(notUsed)
                  29300    0.023    0.000    0.035    0.000 layers.py:581(check)
                     12    0.000    0.000    0.034    0.003 conv.py:394(__init__)
                     12    0.002    0.000    0.034    0.003 conv.py:37(__init__)
                     27    0.000    0.000    0.033    0.001 init.py:352(kaiming_uniform_)
                 134462    0.027    0.000    0.032    0.000 overrides.py:1083(<genexpr>)
                   2344    0.032    0.000    0.032    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                   4688    0.032    0.000    0.032    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                     12    0.000    0.000    0.031    0.003 conv.py:85(reset_parameters)
                    293    0.021    0.000    0.031    0.000 allGraphsTrain.py:41(<listcomp>)
                     54    0.031    0.001    0.031    0.001 {method 'uniform_' of 'torch._C._TensorBase' objects}
                    293    0.029    0.000    0.029    0.000 {built-in method torch._C._nn.one_hot}
                    293    0.002    0.000    0.029    0.000 exploration.py:47(epsilonGreedy)
                  28453    0.020    0.000    0.027    0.000 allGraphs.py:157(compress)
                  65950    0.025    0.000    0.025    0.000 layer.py:146(elements)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-3>
Subject: Job 9507030: <causal7_online_0> in cluster <dcc> Done

Job <causal7_online_0> was submitted from host <n-62-27-21> by user <s183905> in cluster <dcc> at Fri Apr  9 15:59:44 2021
Job was executed on host(s) <n-62-20-3>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Fri Apr  9 16:08:02 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Fri Apr  9 16:08:02 2021
Terminated at Fri Apr  9 16:08:27 2021
Results reported at Fri Apr  9 16:08:27 2021

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

    CPU time :                                   16.86 sec.
    Max Memory :                                 2083 MB
    Average Memory :                             2083.00 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14301.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                7
    Run time :                                   27 sec.
    Turnaround time :                            523 sec.

The output (if any) is above this job summary.

