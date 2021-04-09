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
KeyError: frozenset({<LayerType.Pink3: 20>})


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
    Counterfacts :              1
    Topn :                      7
    Minutes used :              0 minutes.
    Hours used :                0 hours.

# Profiling


      8388155 function calls (8380892 primitive calls) in 29.07 seconds

##    Ordered by: cumulative time
   List reduced from 419 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000   29.069   29.069 {built-in method builtins.exec}
                      1    0.000    0.000   29.069   29.069 <string>:1(<module>)
                      1    0.107    0.107   29.069   29.069 allGraphsTrain.py:5(graphTrain)
                      2    0.000    0.000    9.526    4.763 agent.py:16(__init__)
                      2    0.000    0.000    9.525    4.763 network.py:33(__init__)
                      1    0.000    0.000    9.517    9.517 agent.py:109(__init__)
                      6    0.000    0.000    9.452    1.575 module.py:529(to)
                   72/6    0.001    0.000    9.452    1.575 module.py:357(_apply)
                    398    9.450    0.024    9.450    0.024 {method 'to' of 'torch._C._TensorBase' objects}
                     54    0.000    0.000    9.450    0.175 module.py:607(convert)
                    345    3.434    0.010    8.366    0.024 allGraphs.py:220(transformNot)
                  34946    1.257    0.000    5.624    0.000 allGraphs.py:141(states)
                    345    0.008    0.000    5.578    0.016 allGraphsTrain.py:27(<listcomp>)
                 483500    5.556    0.000    5.556    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                 449100    4.039    0.000    4.039    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                    344    0.001    0.000    1.435    0.004 game.py:41(step)
                    344    0.002    0.000    1.361    0.004 layers.py:710(step)
                    344    0.060    0.000    0.924    0.003 allGraphsTrain.py:35(<listcomp>)
                    344    0.025    0.000    0.840    0.002 layers.py:17(step)
                  34400    0.054    0.000    0.811    0.000 layer.py:98(move)
                    344    0.001    0.000    0.758    0.002 agent.py:29(learn)
                    344    0.007    0.000    0.756    0.002 agent.py:117(_learn)
                    344    0.022    0.000    0.750    0.002 learner.py:42(Qlearn)
                    345    0.335    0.001    0.725    0.002 allGraphsTrain.py:33(<listcomp>)
                  36464    0.081    0.000    0.578    0.000 tensor.py:21(wrapped)
                    345    0.046    0.000    0.570    0.002 layers.py:676(update)
                    344    0.025    0.000    0.536    0.002 allGraphsTrain.py:42(<listcomp>)
                  34400    0.085    0.000    0.524    0.000 layers.py:727(check)
                   1014    0.007    0.000    0.390    0.000 allGraphs.py:228(getInterventions)
                  36120    0.385    0.000    0.385    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                   4458    0.382    0.000    0.382    0.000 {built-in method tensor}
                  34400    0.354    0.000    0.354    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
              7912/1032    0.030    0.000    0.344    0.000 module.py:715(_call_impl)
                    688    0.002    0.000    0.319    0.000 network.py:24(forward)
                   2736    0.002    0.000    0.319    0.000 game.py:37(board)
                    688    0.007    0.000    0.314    0.000 container.py:115(forward)
                    344    0.145    0.000    0.302    0.001 agent.py:67(modify)
                    344    0.002    0.000    0.292    0.001 grad_mode.py:23(decorate_context)
                    344    0.010    0.000    0.286    0.001 adam.py:55(step)
                1196230    0.189    0.000    0.272    0.000 enum.py:646(__hash__)
                   1013    0.049    0.000    0.263    0.000 allGraphs.py:170(bestIntervention)
                    344    0.049    0.000    0.234    0.001 functional.py:53(adam)
                    344    0.004    0.000    0.232    0.001 agent.py:112(__call__)
                  96445    0.057    0.000    0.204    0.000 {built-in method builtins.any}
                    344    0.002    0.000    0.195    0.001 tensor.py:181(backward)
                    344    0.001    0.000    0.193    0.001 __init__.py:68(backward)
                  34400    0.057    0.000    0.189    0.000 layers.py:721(isFree)
                    344    0.184    0.001    0.184    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                  70964    0.033    0.000    0.156    0.000 {built-in method builtins.all}
                   3105    0.083    0.000    0.153    0.000 layer.py:167(NoRock_update)
                   1376    0.002    0.000    0.133    0.000 conv.py:422(forward)
                 288996    0.101    0.000    0.132    0.000 layer.py:95(isFree)
                   1376    0.003    0.000    0.130    0.000 conv.py:414(_conv_forward)
                   1376    0.126    0.000    0.126    0.000 {built-in method conv2d}
                  35776    0.117    0.000    0.117    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                 257071    0.064    0.000    0.114    0.000 layers.py:682(<genexpr>)
                   1033    0.004    0.000    0.112    0.000 tensor.py:576(__iter__)
                 343260    0.090    0.000    0.109    0.000 layers.py:692(<genexpr>)
                   1033    0.106    0.000    0.106    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
                  95922    0.065    0.000    0.100    0.000 allGraphs.py:157(compress)
                  59990    0.030    0.000    0.097    0.000 overrides.py:1070(has_torch_function)
                  44163    0.052    0.000    0.093    0.000 allGraphs.py:150(expand)
                  34400    0.056    0.000    0.090    0.000 layers.py:369(check)
                   1376    0.003    0.000    0.088    0.000 linear.py:92(forward)
                  34400    0.055    0.000    0.088    0.000 layers.py:343(check)
                  34400    0.054    0.000    0.086    0.000 layers.py:381(check)
                  34400    0.054    0.000    0.086    0.000 layers.py:331(check)
                    174    0.002    0.000    0.084    0.000 layers.py:731(restart)
                   1376    0.006    0.000    0.083    0.000 functional.py:1669(linear)
                1196323    0.083    0.000    0.083    0.000 {built-in method builtins.hash}
                  19318    0.044    0.000    0.074    0.000 tensor.py:933(grad)
                      6    0.000    0.000    0.073    0.012 network.py:15(__init__)
                   3979    0.021    0.000    0.071    0.000 allGraphs.py:163(flip_chance)
                 762678    0.070    0.000    0.070    0.000 layer.py:91(positions)
                    174    0.001    0.000    0.070    0.000 level.py:8(__init__)
                     12    0.000    0.000    0.068    0.006 conv.py:394(__init__)
                     12    0.002    0.000    0.068    0.006 conv.py:37(__init__)
                     27    0.000    0.000    0.067    0.002 init.py:352(kaiming_uniform_)
                     12    0.000    0.000    0.064    0.005 conv.py:85(reset_parameters)
                    174    0.003    0.000    0.063    0.000 levels.py:249(generate)
                      1    0.002    0.002    0.063    0.063 game.py:9(__init__)
                   1376    0.062    0.000    0.062    0.000 {built-in method addmm}
                    344    0.006    0.000    0.062    0.000 optimizer.py:167(zero_grad)
                   1144    0.010    0.000    0.058    0.000 level.py:41(notUsed)
                      1    0.000    0.000    0.054    0.054 allGraphsTrain.py:22(<listcomp>)
                    344    0.003    0.000    0.052    0.000 agent.py:59(modify_board)
                   2064    0.002    0.000    0.049    0.000 activation.py:713(forward)
                      1    0.000    0.000    0.049    0.049 save.py:15(__exit__)
                      1    0.000    0.000    0.049    0.049 save.py:18(save)
                    344    0.029    0.000    0.049    0.000 collector.py:53(collect)
                      4    0.025    0.006    0.048    0.012 save.py:24(saveObject)
                   2064    0.003    0.000    0.047    0.000 functional.py:1292(leaky_relu)
                   5504    0.044    0.000    0.044    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                   2064    0.043    0.000    0.043    0.000 {built-in method torch._C._nn.leaky_relu}
                     54    0.043    0.001    0.043    0.001 {method 'uniform_' of 'torch._C._TensorBase' objects}
                  34400    0.026    0.000    0.040    0.000 layers.py:320(check)
                  34400    0.026    0.000    0.040    0.000 layers.py:358(check)
                   2752    0.038    0.000    0.038    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                 157820    0.032    0.000    0.038    0.000 overrides.py:1083(<genexpr>)
                    344    0.025    0.000    0.037    0.000 allGraphsTrain.py:41(<listcomp>)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-3>
Subject: Job 9507028: <causal5_online_0> in cluster <dcc> Done

Job <causal5_online_0> was submitted from host <n-62-27-21> by user <s183905> in cluster <dcc> at Fri Apr  9 15:59:44 2021
Job was executed on host(s) <n-62-20-3>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Fri Apr  9 16:06:34 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Fri Apr  9 16:06:34 2021
Terminated at Fri Apr  9 16:07:10 2021
Results reported at Fri Apr  9 16:07:10 2021

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

    CPU time :                                   23.87 sec.
    Max Memory :                                 1252 MB
    Average Memory :                             1252.00 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15132.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                7
    Run time :                                   37 sec.
    Turnaround time :                            446 sec.

The output (if any) is above this job summary.

