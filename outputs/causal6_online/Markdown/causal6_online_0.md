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
    Counterfacts :              10
    Topn :                      7
    Minutes used :              1 minutes.
    Hours used :                0 hours.

# Profiling


      25062821 function calls (25037698 primitive calls) in 69.13 seconds

##    Ordered by: cumulative time
   List reduced from 419 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000   69.129   69.129 {built-in method builtins.exec}
                      1    0.000    0.000   69.129   69.129 <string>:1(<module>)
                      1    0.285    0.285   69.129   69.129 allGraphsTrain.py:5(graphTrain)
                   1238   10.748    0.009   25.935    0.021 allGraphs.py:220(transformNot)
                1486008   17.145    0.000   17.145    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                 125139    3.977    0.000   17.028    0.000 allGraphs.py:141(states)
                   1238    0.027    0.000   17.009    0.014 allGraphsTrain.py:27(<listcomp>)
                1362300   12.232    0.000   12.232    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                      2    0.000    0.000    8.096    4.048 agent.py:16(__init__)
                      2    0.000    0.000    8.096    4.048 network.py:33(__init__)
                      1    0.000    0.000    8.088    8.088 agent.py:109(__init__)
                   1291    8.057    0.006    8.058    0.006 {method 'to' of 'torch._C._TensorBase' objects}
                      6    0.000    0.000    8.057    1.343 module.py:529(to)
                   72/6    0.001    0.000    8.057    1.343 module.py:357(_apply)
                     54    0.000    0.000    8.055    0.149 module.py:607(convert)
                   1237    0.004    0.000    5.028    0.004 game.py:41(step)
                   1237    0.005    0.000    4.779    0.004 layers.py:710(step)
                   1237    0.211    0.000    3.318    0.003 allGraphsTrain.py:35(<listcomp>)
                   1237    0.089    0.000    2.834    0.002 layers.py:17(step)
                 123700    0.192    0.000    2.732    0.000 layer.py:98(move)
                   1237    0.004    0.000    2.573    0.002 agent.py:29(learn)
                   1237    0.025    0.000    2.567    0.002 agent.py:117(_learn)
                   1237    0.075    0.000    2.542    0.002 learner.py:42(Qlearn)
                 131122    0.287    0.000    2.005    0.000 tensor.py:21(wrapped)
                   1238    0.170    0.000    1.983    0.002 layers.py:676(update)
                   1237    0.088    0.000    1.891    0.002 allGraphsTrain.py:42(<listcomp>)
                   1238    1.193    0.001    1.768    0.001 allGraphsTrain.py:33(<listcomp>)
                 123700    0.290    0.000    1.740    0.000 layers.py:727(check)
                 129885    1.353    0.000    1.353    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                 123700    1.288    0.000    1.288    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                  14461    1.097    0.000    1.097    0.000 {built-in method tensor}
                   1237    0.528    0.000    1.053    0.001 agent.py:67(modify)
             28451/3711    0.106    0.000    1.044    0.000 module.py:715(_call_impl)
                   1237    0.007    0.000    0.999    0.001 grad_mode.py:23(decorate_context)
                   1237    0.035    0.000    0.978    0.001 adam.py:55(step)
                   2474    0.006    0.000    0.956    0.000 network.py:24(forward)
                   2474    0.024    0.000    0.936    0.000 container.py:115(forward)
                   8282    0.007    0.000    0.889    0.000 game.py:37(board)
                   1237    0.175    0.000    0.799    0.001 functional.py:53(adam)
                3103996    0.529    0.000    0.756    0.000 enum.py:646(__hash__)
                 346120    0.189    0.000    0.671    0.000 {built-in method builtins.any}
                   1237    0.015    0.000    0.645    0.001 agent.py:112(__call__)
                 123700    0.191    0.000    0.638    0.000 layers.py:721(isFree)
                 254922    0.098    0.000    0.629    0.000 {built-in method builtins.all}
                   1237    0.007    0.000    0.614    0.000 tensor.py:181(backward)
                   1237    0.004    0.000    0.607    0.000 __init__.py:68(backward)
                   1237    0.577    0.000    0.577    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                   2095    0.014    0.000    0.575    0.000 allGraphs.py:228(getInterventions)
                 638571    0.170    0.000    0.500    0.000 layers.py:682(<genexpr>)
                   9904    0.271    0.000    0.495    0.000 layer.py:167(NoRock_update)
                 123700    0.292    0.000    0.480    0.000 layers.py:418(check)
                 865854    0.348    0.000    0.447    0.000 layer.py:95(isFree)
                 128648    0.406    0.000    0.406    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                   3712    0.014    0.000    0.405    0.000 tensor.py:576(__iter__)
                   3712    0.382    0.000    0.382    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
                   4948    0.008    0.000    0.368    0.000 conv.py:422(forward)
                   4948    0.009    0.000    0.357    0.000 conv.py:414(_conv_forward)
                1108773    0.286    0.000    0.347    0.000 layers.py:692(<genexpr>)
                   4948    0.346    0.000    0.346    0.000 {built-in method conv2d}
                 215372    0.105    0.000    0.342    0.000 overrides.py:1070(has_torch_function)
                   2090    0.068    0.000    0.330    0.000 allGraphs.py:170(bestIntervention)
                 123700    0.203    0.000    0.324    0.000 layers.py:431(check)
                 123700    0.197    0.000    0.317    0.000 layers.py:446(check)
                    603    0.006    0.000    0.278    0.000 layers.py:731(restart)
                   4948    0.012    0.000    0.277    0.000 linear.py:92(forward)
                   4948    0.019    0.000    0.261    0.000 functional.py:1669(linear)
                  69326    0.155    0.000    0.258    0.000 tensor.py:933(grad)
                2630662    0.245    0.000    0.245    0.000 layer.py:91(positions)
                    603    0.003    0.000    0.230    0.000 level.py:8(__init__)
                3104089    0.227    0.000    0.227    0.000 {built-in method builtins.hash}
                   1237    0.021    0.000    0.220    0.000 optimizer.py:167(zero_grad)
                    603    0.009    0.000    0.199    0.000 levels.py:293(generate)
                   4948    0.187    0.000    0.187    0.000 {built-in method addmm}
                 123800    0.113    0.000    0.187    0.000 layers.py:436(isDone)
                   1237    0.009    0.000    0.184    0.000 agent.py:59(modify_board)
                   3660    0.034    0.000    0.181    0.000 level.py:41(notUsed)
                   1237    0.104    0.000    0.178    0.000 collector.py:53(collect)
                  19792    0.159    0.000    0.159    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                 123700    0.100    0.000    0.153    0.000 layers.py:407(check)
                 123700    0.095    0.000    0.146    0.000 layers.py:396(check)
                  72791    0.083    0.000    0.144    0.000 allGraphs.py:150(expand)
                   7422    0.007    0.000    0.135    0.000 activation.py:713(forward)
                 566814    0.113    0.000    0.135    0.000 overrides.py:1083(<genexpr>)
                   1237    0.089    0.000    0.133    0.000 allGraphsTrain.py:41(<listcomp>)
                  19792    0.132    0.000    0.132    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                   7422    0.012    0.000    0.128    0.000 functional.py:1292(leaky_relu)
                   1237    0.121    0.000    0.121    0.000 {built-in method torch._C._nn.one_hot}
                 276819    0.120    0.000    0.120    0.000 layer.py:146(elements)
                   1237    0.007    0.000    0.118    0.000 exploration.py:47(epsilonGreedy)
                   7422    0.115    0.000    0.115    0.000 {built-in method torch._C._nn.leaky_relu}
                 114137    0.082    0.000    0.112    0.000 allGraphs.py:157(compress)
                   1238    0.027    0.000    0.104    0.000 allGraphs.py:209(transform)
                   9896    0.095    0.000    0.095    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                   9896    0.092    0.000    0.092    0.000 {method 'add' of 'torch._C._TensorBase' objects}
        1107337/1107335    0.064    0.000    0.084    0.000 {built-in method builtins.len}
                   3660    0.003    0.000    0.084    0.000 level.py:38(elementsIn)
                   3713    0.080    0.000    0.080    0.000 {method 'tolist' of 'torch._C._TensorBase' objects}
                 865854    0.079    0.000    0.079    0.000 layer.py:203(isBlocking)
                  47465    0.050    0.000    0.077    0.000 layers.py:107(isDone)
                   9896    0.076    0.000    0.076    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-5>
Subject: Job 9505745: <causal6_online_0> in cluster <dcc> Done

Job <causal6_online_0> was submitted from host <n-62-30-2> by user <s183905> in cluster <dcc> at Thu Apr  8 23:40:14 2021
Job was executed on host(s) <n-62-20-5>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Thu Apr  8 23:45:31 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Apr  8 23:45:31 2021
Terminated at Thu Apr  8 23:46:45 2021
Results reported at Thu Apr  8 23:46:45 2021

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

    CPU time :                                   64.96 sec.
    Max Memory :                                 2082 MB
    Average Memory :                             2082.00 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14302.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   75 sec.
    Turnaround time :                            391 sec.

The output (if any) is above this job summary.

