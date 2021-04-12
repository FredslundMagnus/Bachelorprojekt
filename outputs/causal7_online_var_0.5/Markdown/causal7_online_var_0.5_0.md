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
  File "/zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/allGraphsTrain.py", line 43, in graphTrain
    playerPositions = [(t := env.layers.dict[LayerType.Player].positions[i][0])[1] * env.layers.width + t[0] for i in range(env.batch)]
  File "/zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/allGraphsTrain.py", line 43, in <listcomp>
    playerPositions = [(t := env.layers.dict[LayerType.Player].positions[i][0])[1] * env.layers.width + t[0] for i in range(env.batch)]
IndexError: list index out of range


# Parameters

    Name :                      causal7_online_var_0.5-0
    Main :                      graphTrain
    Level :                     Levels.Causal7
    Failed actions chance :     0.5
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


      178894 function calls (178507 primitive calls) in 2.83 seconds

##    Ordered by: cumulative time
   List reduced from 412 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000    2.827    2.827 {built-in method builtins.exec}
                      1    0.000    0.000    2.827    2.827 <string>:1(<module>)
                      1    0.003    0.003    2.826    2.826 allGraphsTrain.py:10(graphTrain)
                      2    0.000    0.000    2.655    1.327 agent.py:16(__init__)
                      2    0.000    0.000    2.654    1.327 network.py:33(__init__)
                      1    0.000    0.000    2.647    2.647 agent.py:109(__init__)
                      6    0.000    0.000    2.644    0.441 module.py:529(to)
                   72/6    0.000    0.000    2.644    0.441 module.py:357(_apply)
                     54    0.000    0.000    2.642    0.049 module.py:607(convert)
                     55    2.642    0.048    2.642    0.048 {method 'to' of 'torch._C._TensorBase' objects}
                      1    0.000    0.000    0.054    0.054 save.py:15(__exit__)
                      1    0.000    0.000    0.054    0.054 save.py:18(save)
                      4    0.023    0.006    0.053    0.013 save.py:24(saveObject)
                      1    0.002    0.002    0.039    0.039 game.py:9(__init__)
                      2    0.000    0.000    0.034    0.017 layers.py:678(update)
                     80    0.001    0.000    0.029    0.000 layers.py:734(restart)
                     80    0.000    0.000    0.023    0.000 level.py:8(__init__)
                    202    0.005    0.000    0.022    0.000 allGraphs.py:88(states)
                     80    0.001    0.000    0.021    0.000 levels.py:446(generate)
                    387    0.003    0.000    0.019    0.000 level.py:41(notUsed)
                      1    0.007    0.007    0.018    0.018 allGraphs.py:120(transformNot)
                  168/4    0.006    0.000    0.017    0.004 {built-in method _pickle.dump}
                   1400    0.016    0.000    0.016    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                   1300    0.012    0.000    0.012    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                      1    0.000    0.000    0.011    0.011 allGraphsTrain.py:23(<listcomp>)
                      1    0.000    0.000    0.011    0.011 allGraphsTrain.py:29(<listcomp>)
                    180    0.005    0.000    0.011    0.000 layers.py:30(reset)
                      1    0.000    0.000    0.010    0.010 game.py:41(step)
                      6    0.000    0.000    0.010    0.002 network.py:15(__init__)
                      1    0.000    0.000    0.010    0.010 layers.py:712(step)
                     41    0.000    0.000    0.010    0.000 storage.py:32(__reduce__)
                     41    0.001    0.000    0.010    0.000 serialization.py:333(save)
                      1    0.000    0.000    0.010    0.010 layers.py:636(__init__)
                      1    0.000    0.000    0.010    0.010 allGraphsTrain.py:35(<listcomp>)
                    100    0.000    0.000    0.010    0.000 allGraphs.py:127(getInterventions)
                      6    0.000    0.000    0.009    0.002 layers.py:667(add)
                    113    0.009    0.000    0.009    0.000 {built-in method tensor}
                    106    0.000    0.000    0.009    0.000 game.py:37(board)
                     41    0.001    0.000    0.009    0.000 serialization.py:377(_legacy_save)
                    387    0.000    0.000    0.009    0.000 level.py:38(elementsIn)
                      1    0.000    0.000    0.009    0.009 agent.py:39(__init__)
                      7    0.001    0.000    0.009    0.001 layer.py:53(__init__)
                      5    0.000    0.000    0.007    0.001 save.py:28(path)
                      4    0.007    0.002    0.007    0.002 {built-in method io.open}
                    387    0.003    0.000    0.006    0.000 level.py:39(<listcomp>)
                     27    0.000    0.000    0.006    0.000 init.py:352(kaiming_uniform_)
                      1    0.000    0.000    0.005    0.005 agent.py:29(learn)
                      1    0.000    0.000    0.005    0.005 agent.py:117(_learn)
                    560    0.000    0.000    0.005    0.000 layer.py:69(restart)
                      1    0.000    0.000    0.005    0.005 learner.py:42(Qlearn)
                     41    0.005    0.000    0.005    0.000 {method '_write_file' of 'torch._C.CudaFloatStorageBase' objects}
                     54    0.005    0.000    0.005    0.000 {method 'uniform_' of 'torch._C._TensorBase' objects}
                  20482    0.003    0.000    0.005    0.000 enum.py:646(__hash__)
                      4    0.005    0.001    0.005    0.001 {built-in method posix.mkdir}
                     12    0.000    0.000    0.005    0.000 conv.py:394(__init__)
                   23/3    0.000    0.000    0.004    0.001 module.py:715(_call_impl)
                     12    0.000    0.000    0.004    0.000 conv.py:37(__init__)
                     15    0.000    0.000    0.004    0.000 linear.py:74(__init__)
                      2    0.000    0.000    0.004    0.002 network.py:24(forward)
                      2    0.000    0.000    0.004    0.002 container.py:115(forward)
                  18583    0.004    0.000    0.004    0.000 level.py:32(inverse)
                      1    0.000    0.000    0.004    0.004 agent.py:112(__call__)
                   6199    0.002    0.000    0.003    0.000 layer.py:130(add)
                  18302    0.003    0.000    0.003    0.000 enum.py:352(<genexpr>)
                     15    0.000    0.000    0.003    0.000 linear.py:85(reset_parameters)
                     12    0.000    0.000    0.003    0.000 conv.py:85(reset_parameters)
                     14    0.002    0.000    0.003    0.000 layer.py:167(NoRock_update)
                    387    0.002    0.000    0.003    0.000 {built-in method _functools.reduce}
                      4    0.000    0.000    0.003    0.001 conv.py:422(forward)
                      4    0.000    0.000    0.003    0.001 conv.py:414(_conv_forward)
                      4    0.003    0.001    0.003    0.001 {built-in method conv2d}
                      1    0.000    0.000    0.003    0.003 allGraphsTrain.py:37(<listcomp>)
                      1    0.000    0.000    0.003    0.003 tensor.py:181(backward)
                      1    0.000    0.000    0.003    0.003 __init__.py:68(backward)
                      1    0.003    0.003    0.003    0.003 {method 'run_backward' of 'torch._C._EngineBase' objects}
                  15334    0.002    0.000    0.002    0.000 layer.py:182(grid)
                      1    0.000    0.000    0.002    0.002 game.py:29(<setcomp>)
                     10    0.000    0.000    0.002    0.000 genericpath.py:16(exists)
                     34    0.001    0.000    0.002    0.000 game.py:29(<listcomp>)
                     10    0.002    0.000    0.002    0.000 {built-in method posix.stat}
                     80    0.001    0.000    0.002    0.000 level.py:16(<dictcomp>)
                   1030    0.001    0.000    0.002    0.000 module.py:781(__setattr__)
                     74    0.000    0.000    0.002    0.000 module.py:223(__init__)
                     41    0.000    0.000    0.002    0.000 {method 'dump' of '_pickle.Pickler' objects}
                      1    0.001    0.001    0.002    0.002 agent.py:67(modify)
                  20567    0.002    0.000    0.002    0.000 {built-in method builtins.hash}
                      1    0.000    0.000    0.001    0.001 grad_mode.py:23(decorate_context)
                      1    0.000    0.000    0.001    0.001 adam.py:55(step)
                    287    0.001    0.000    0.001    0.000 serialization.py:382(persistent_id)
                     41    0.001    0.000    0.001    0.000 tensor.py:83(__reduce_ex__)
                    100    0.001    0.000    0.001    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                  13545    0.001    0.000    0.001    0.000 level.py:39(<lambda>)
                  13618    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
                      1    0.000    0.000    0.001    0.001 layers.py:17(step)
                    206    0.000    0.000    0.001    0.000 {built-in method builtins.all}
                     60    0.000    0.000    0.001    0.000 layer.py:98(move)
                   1652    0.001    0.000    0.001    0.000 types.py:171(__get__)
                      1    0.000    0.000    0.001    0.001 functional.py:53(adam)
                    100    0.000    0.000    0.001    0.000 allGraphs.py:103(bestIntervention)
                   1263    0.000    0.000    0.001    0.000 layers.py:684(<genexpr>)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-2>
Subject: Job 9511309: <causal7_online_var_0.5_0> in cluster <dcc> Done

Job <causal7_online_var_0.5_0> was submitted from host <n-62-27-21> by user <s183905> in cluster <dcc> at Mon Apr 12 16:10:31 2021
Job was executed on host(s) <n-62-20-2>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Mon Apr 12 17:00:18 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Apr 12 17:00:18 2021
Terminated at Mon Apr 12 17:00:25 2021
Results reported at Mon Apr 12 17:00:25 2021

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

    CPU time :                                   4.33 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   8 sec.
    Turnaround time :                            2994 sec.

The output (if any) is above this job summary.

