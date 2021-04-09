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
KeyError: frozenset({<LayerType.Brown3: 23>})


# Parameters

    Name :                      causal5_online-0
    Main :                      graphTrain
    Level :                     Levels.Causal5
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


      7972982 function calls (7965819 primitive calls) in 27.45 seconds

##    Ordered by: cumulative time
   List reduced from 420 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000   27.446   27.446 {built-in method builtins.exec}
                      1    0.000    0.000   27.446   27.446 <string>:1(<module>)
                      1    0.088    0.088   27.446   27.446 allGraphsTrain.py:5(graphTrain)
                    340    3.441    0.010    8.319    0.024 allGraphs.py:220(transformNot)
                      2    0.000    0.000    8.164    4.082 agent.py:16(__init__)
                      2    0.000    0.000    8.163    4.082 network.py:33(__init__)
                      1    0.000    0.000    8.155    8.155 agent.py:109(__init__)
                      6    0.000    0.000    8.125    1.354 module.py:529(to)
                   72/6    0.001    0.000    8.125    1.354 module.py:357(_apply)
                    393    8.123    0.021    8.123    0.021 {method 'to' of 'torch._C._TensorBase' objects}
                     54    0.000    0.000    8.123    0.150 module.py:607(convert)
                  34441    1.275    0.000    5.573    0.000 allGraphs.py:141(states)
                    340    0.009    0.000    5.535    0.016 allGraphsTrain.py:27(<listcomp>)
                 476500    5.486    0.000    5.486    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                 442600    3.985    0.000    3.985    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                    339    0.001    0.000    1.367    0.004 game.py:41(step)
                    339    0.002    0.000    1.296    0.004 layers.py:710(step)
                    339    0.060    0.000    0.915    0.003 allGraphsTrain.py:35(<listcomp>)
                    339    0.024    0.000    0.848    0.003 layers.py:17(step)
                  33900    0.052    0.000    0.820    0.000 layer.py:98(move)
                    339    0.001    0.000    0.747    0.002 agent.py:29(learn)
                    339    0.007    0.000    0.746    0.002 agent.py:117(_learn)
                    339    0.021    0.000    0.739    0.002 learner.py:42(Qlearn)
                    340    0.328    0.001    0.717    0.002 allGraphsTrain.py:33(<listcomp>)
                  35934    0.080    0.000    0.565    0.000 tensor.py:21(wrapped)
                  33900    0.090    0.000    0.535    0.000 layers.py:727(check)
                    339    0.025    0.000    0.526    0.002 allGraphsTrain.py:42(<listcomp>)
                    340    0.046    0.000    0.496    0.001 layers.py:676(update)
                   1035    0.007    0.000    0.389    0.000 allGraphs.py:228(getInterventions)
                   4428    0.376    0.000    0.376    0.000 {built-in method tensor}
                  35595    0.376    0.000    0.376    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                  33900    0.351    0.000    0.351    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
              7797/1017    0.029    0.000    0.323    0.000 module.py:715(_call_impl)
                   2732    0.002    0.000    0.315    0.000 game.py:37(board)
                    678    0.002    0.000    0.299    0.000 network.py:24(forward)
                    339    0.143    0.000    0.296    0.001 agent.py:67(modify)
                    678    0.007    0.000    0.293    0.000 container.py:115(forward)
                    339    0.002    0.000    0.286    0.001 grad_mode.py:23(decorate_context)
                    339    0.009    0.000    0.280    0.001 adam.py:55(step)
                1208610    0.192    0.000    0.277    0.000 enum.py:646(__hash__)
                   1034    0.048    0.000    0.261    0.000 allGraphs.py:170(bestIntervention)
                    339    0.049    0.000    0.231    0.001 functional.py:53(adam)
                    339    0.004    0.000    0.212    0.001 agent.py:112(__call__)
                    339    0.002    0.000    0.196    0.001 tensor.py:181(backward)
                  95051    0.054    0.000    0.194    0.000 {built-in method builtins.any}
                    339    0.001    0.000    0.194    0.001 __init__.py:68(backward)
                  33900    0.055    0.000    0.186    0.000 layers.py:721(isFree)
                    339    0.185    0.001    0.185    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                   3060    0.081    0.000    0.149    0.000 layer.py:167(NoRock_update)
                 275346    0.100    0.000    0.131    0.000 layer.py:95(isFree)
                   1356    0.002    0.000    0.117    0.000 conv.py:422(forward)
                   1356    0.003    0.000    0.114    0.000 conv.py:414(_conv_forward)
                  35256    0.114    0.000    0.114    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                   1356    0.110    0.000    0.110    0.000 {built-in method conv2d}
                   1018    0.004    0.000    0.110    0.000 tensor.py:576(__iter__)
                   1018    0.104    0.000    0.104    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
                 338320    0.084    0.000    0.103    0.000 layers.py:692(<genexpr>)
                  97275    0.065    0.000    0.100    0.000 allGraphs.py:157(compress)
                  69934    0.018    0.000    0.098    0.000 {built-in method builtins.all}
                  59120    0.030    0.000    0.095    0.000 overrides.py:1070(has_torch_function)
                  42898    0.051    0.000    0.090    0.000 allGraphs.py:150(expand)
                  33900    0.056    0.000    0.090    0.000 layers.py:331(check)
                  33900    0.055    0.000    0.088    0.000 layers.py:343(check)
                  33900    0.055    0.000    0.088    0.000 layers.py:369(check)
                   1356    0.003    0.000    0.087    0.000 linear.py:92(forward)
                  33900    0.054    0.000    0.087    0.000 layers.py:381(check)
                1208703    0.085    0.000    0.085    0.000 {built-in method builtins.hash}
                   1356    0.006    0.000    0.083    0.000 functional.py:1669(linear)
                    168    0.002    0.000    0.081    0.000 layers.py:731(restart)
                   4025    0.021    0.000    0.072    0.000 allGraphs.py:163(flip_chance)
                  19038    0.043    0.000    0.071    0.000 tensor.py:933(grad)
                  71990    0.016    0.000    0.071    0.000 layers.py:682(<genexpr>)
                 775392    0.070    0.000    0.070    0.000 layer.py:91(positions)
                    168    0.001    0.000    0.067    0.000 level.py:8(__init__)
                      1    0.002    0.002    0.063    0.063 game.py:9(__init__)
                   1356    0.062    0.000    0.062    0.000 {built-in method addmm}
                    339    0.006    0.000    0.061    0.000 optimizer.py:167(zero_grad)
                    168    0.002    0.000    0.061    0.000 levels.py:249(generate)
                   1099    0.010    0.000    0.055    0.000 level.py:41(notUsed)
                  34000    0.036    0.000    0.055    0.000 layers.py:107(isDone)
                    339    0.003    0.000    0.050    0.000 agent.py:59(modify_board)
                      1    0.000    0.000    0.049    0.049 save.py:15(__exit__)
                      1    0.000    0.000    0.049    0.049 save.py:18(save)
                    339    0.029    0.000    0.049    0.000 collector.py:53(collect)
                      4    0.025    0.006    0.048    0.012 save.py:24(saveObject)
                      1    0.000    0.000    0.047    0.047 allGraphsTrain.py:22(<listcomp>)
                   2034    0.002    0.000    0.046    0.000 activation.py:713(forward)
                   5424    0.044    0.000    0.044    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                  33900    0.029    0.000    0.044    0.000 layers.py:320(check)
                   2034    0.003    0.000    0.044    0.000 functional.py:1292(leaky_relu)
                   2034    0.040    0.000    0.040    0.000 {built-in method torch._C._nn.leaky_relu}
                  33900    0.026    0.000    0.040    0.000 layers.py:358(check)
                      6    0.000    0.000    0.038    0.006 network.py:15(__init__)
                 155530    0.031    0.000    0.037    0.000 overrides.py:1083(<genexpr>)
                   5424    0.037    0.000    0.037    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                    339    0.024    0.000    0.036    0.000 allGraphsTrain.py:41(<listcomp>)
                   2712    0.036    0.000    0.036    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                  76479    0.035    0.000    0.035    0.000 layer.py:146(elements)
                    339    0.033    0.000    0.033    0.000 {built-in method torch._C._nn.one_hot}
                    339    0.002    0.000    0.033    0.000 exploration.py:47(epsilonGreedy)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-5>
Subject: Job 9505744: <causal5_online_0> in cluster <dcc> Done

Job <causal5_online_0> was submitted from host <n-62-30-2> by user <s183905> in cluster <dcc> at Thu Apr  8 23:40:13 2021
Job was executed on host(s) <n-62-20-5>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Thu Apr  8 23:44:57 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Apr  8 23:44:57 2021
Terminated at Thu Apr  8 23:45:30 2021
Results reported at Thu Apr  8 23:45:30 2021

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

    CPU time :                                   23.48 sec.
    Max Memory :                                 2075 MB
    Average Memory :                             2074.67 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14309.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   34 sec.
    Turnaround time :                            317 sec.

The output (if any) is above this job summary.

