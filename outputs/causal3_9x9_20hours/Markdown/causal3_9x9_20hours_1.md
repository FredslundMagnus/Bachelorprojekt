Traceback (most recent call last):
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils/debug.py", line 71, in __init__
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
  File "main.py", line 59, in teleport
    board_before, board_after, intervention, tele_rewards, tele_dones, normal_rewards = buffer.sample_data()
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/replaybuffer.py", line 25, in sample_data
    return self.stacker(samples)
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/replaybuffer.py", line 21, in stacker
    return concatenation(arays[0], 0), concatenation(arays[1], 0), concatenation(arays[2], 0).long(), concatenation(arays[3], 0), concatenation(arays[4], 0), concatenation(arays[5], 0)
IndexError: list index out of range


# Parameters

    Name :                      causal3_9x9_20hours-1
    Main :                      teleport
    Level :                     Levels.Causal3
    Hours :                     20.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Network1 :                  Networks.Teleporter
    K1 :                        5000000
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
    K2 :                        1000000
    Learner2 :                  Learners.Qlearn
    Exploration2 :              Explorations.epsilonGreedy
    Gamma2 :                    0.95
    Layer blocks :              True
    Layer goal :                True
    Layer gold :                True
    Layer keys :                False
    Layer door :                False
    Layer holder :              False
    Layer putter :              False
    Layer rock :                False
    Layer dirt :                True
    Layer diamond1 :            False
    Layer diamond2 :            False
    Layer diamond3 :            False
    Layer diamond4 :            False
    Layer reddoors :            True
    Layer redkeys :             True
    Layer bluedoors :           True
    Layer bluekeys :            True
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Minutes used :              0 minutes.
    Hours used :                0 hours.

# Profiling


      142381 function calls (141438 primitive calls) in 3.31 seconds

##    Ordered by: cumulative time
   List reduced from 400 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000    3.315    3.315 {built-in method builtins.exec}
                      1    0.000    0.000    3.315    3.315 <string>:1(<module>)
                      1    0.000    0.000    3.315    3.315 main.py:43(teleport)
                      2    0.000    0.000    2.872    1.436 agent.py:14(__init__)
                      2    0.000    0.000    2.871    1.436 network.py:33(__init__)
                      1    0.000    0.000    2.863    2.863 agent.py:104(__init__)
                      6    0.000    0.000    2.861    0.477 module.py:573(to)
                   72/6    0.000    0.000    2.861    0.477 module.py:385(_apply)
                     54    0.000    0.000    2.860    0.053 module.py:667(convert)
                     55    2.859    0.052    2.860    0.052 {method 'to' of 'torch._C._TensorBase' objects}
                      1    0.000    0.000    0.373    0.373 save.py:15(__exit__)
                      1    0.000    0.000    0.373    0.373 save.py:18(save)
                      4    0.298    0.074    0.372    0.093 save.py:24(saveObject)
                  696/4    0.021    0.000    0.062    0.015 {built-in method _pickle.dump}
                      1    0.002    0.002    0.039    0.039 game.py:9(__init__)
                    173    0.000    0.000    0.039    0.000 storage.py:52(__reduce__)
                    173    0.001    0.000    0.039    0.000 serialization.py:333(save)
                    173    0.002    0.000    0.037    0.000 serialization.py:377(_legacy_save)
                      2    0.000    0.000    0.032    0.016 layers.py:446(update)
                    173    0.030    0.000    0.030    0.000 {method '_write_file' of 'torch._C.CudaFloatStorageBase' objects}
                    100    0.001    0.000    0.027    0.000 layers.py:496(restart)
                    100    0.000    0.000    0.017    0.000 level.py:8(__init__)
                    100    0.003    0.000    0.015    0.000 levels.py:163(generate)
                      1    0.008    0.008    0.013    0.013 agent.py:83(interveen)
                      6    0.000    0.000    0.010    0.002 network.py:15(__init__)
                    200    0.001    0.000    0.010    0.000 level.py:41(notUsed)
                    200    0.005    0.000    0.010    0.000 layers.py:33(reset)
                    900    0.001    0.000    0.008    0.000 layer.py:50(restart)
                      1    0.000    0.000    0.008    0.008 agent.py:37(__init__)
                      5    0.000    0.000    0.007    0.001 save.py:28(path)
                      4    0.007    0.002    0.007    0.002 {built-in method io.open}
                      1    0.000    0.000    0.006    0.006 layers.py:336(__init__)
                      9    0.000    0.000    0.006    0.001 layer.py:36(__init__)
                      1    0.000    0.000    0.006    0.006 agent.py:27(learn)
                      1    0.000    0.000    0.006    0.006 agent.py:112(_learn)
                      1    0.000    0.000    0.006    0.006 learner.py:42(Qlearn)
                     27    0.000    0.000    0.005    0.000 init.py:347(kaiming_uniform_)
                   4187    0.005    0.000    0.005    0.000 level.py:32(inverse)
                   36/4    0.000    0.000    0.005    0.001 module.py:866(_call_impl)
                      3    0.000    0.000    0.005    0.002 network.py:24(forward)
                      3    0.000    0.000    0.005    0.002 container.py:117(forward)
                      1    0.000    0.000    0.005    0.005 agent.py:47(__call__)
                     54    0.005    0.000    0.005    0.000 {method 'uniform_' of 'torch._C._TensorBase' objects}
                      4    0.005    0.001    0.005    0.001 {built-in method posix.mkdir}
                   9637    0.003    0.000    0.004    0.000 layer.py:100(add)
                     12    0.000    0.000    0.004    0.000 conv.py:370(__init__)
                     12    0.000    0.000    0.004    0.000 conv.py:66(__init__)
                     18    0.003    0.000    0.004    0.000 layer.py:137(NoRock_update)
                     15    0.000    0.000    0.004    0.000 linear.py:75(__init__)
                      1    0.000    0.000    0.004    0.004 game.py:27(step)
                      1    0.000    0.000    0.003    0.003 layers.py:475(step)
                      6    0.000    0.000    0.003    0.001 conv.py:398(forward)
                      6    0.000    0.000    0.003    0.001 conv.py:390(_conv_forward)
                      6    0.003    0.001    0.003    0.001 {built-in method conv2d}
                    173    0.001    0.000    0.003    0.000 {method 'dump' of '_pickle.Pickler' objects}
                     15    0.000    0.000    0.003    0.000 linear.py:86(reset_parameters)
                  12580    0.002    0.000    0.003    0.000 enum.py:646(__hash__)
                     12    0.000    0.000    0.003    0.000 conv.py:114(reset_parameters)
                      1    0.000    0.000    0.003    0.003 tensor.py:195(backward)
                      1    0.000    0.000    0.003    0.003 __init__.py:68(backward)
                      1    0.003    0.003    0.003    0.003 {method 'run_backward' of 'torch._C._EngineBase' objects}
                    200    0.000    0.000    0.003    0.000 level.py:38(elementsIn)
                    173    0.000    0.000    0.003    0.000 tensor.py:93(__reduce_ex__)
                      1    0.000    0.000    0.003    0.003 replaybuffer.py:8(__init__)
                      1    0.003    0.003    0.003    0.003 replaybuffer.py:11(<listcomp>)
                      1    0.000    0.000    0.003    0.003 agent.py:100(pre_process)
                      1    0.000    0.000    0.003    0.003 layers.py:18(step)
                    173    0.002    0.000    0.003    0.000 tensor.py:103(_reduce_ex_internal)
                    100    0.000    0.000    0.003    0.000 layer.py:76(move)
                   1211    0.001    0.000    0.002    0.000 serialization.py:382(persistent_id)
                      3    0.002    0.001    0.002    0.001 {method 'long' of 'torch._C._TensorBase' objects}
                  17138    0.002    0.000    0.002    0.000 layer.py:152(grid)
                   1104    0.001    0.000    0.002    0.000 module.py:950(__setattr__)
                     10    0.000    0.000    0.002    0.000 genericpath.py:16(exists)
                      1    0.000    0.000    0.002    0.002 optimizer.py:84(wrapper)
                     10    0.002    0.000    0.002    0.000 {built-in method posix.stat}
                     74    0.000    0.000    0.002    0.000 module.py:250(__init__)
                      1    0.000    0.000    0.002    0.002 grad_mode.py:24(decorate_context)
                      1    0.000    0.000    0.002    0.002 adam.py:55(step)
                    100    0.000    0.000    0.002    0.000 layers.py:492(check)
                    100    0.001    0.000    0.002    0.000 level.py:16(<dictcomp>)
                    200    0.001    0.000    0.002    0.000 level.py:39(<listcomp>)
                  22592    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
                      1    0.001    0.001    0.001    0.001 agent.py:64(modify)
                    201    0.000    0.000    0.001    0.000 random.py:315(sample)
                   9759    0.001    0.000    0.001    0.000 layer.py:116(elements)
                   5707    0.001    0.000    0.001    0.000 enum.py:352(<genexpr>)
                      7    0.000    0.000    0.001    0.000 linear.py:93(forward)
                    200    0.001    0.000    0.001    0.000 {built-in method _functools.reduce}
                  12929    0.001    0.000    0.001    0.000 {built-in method builtins.hash}
                    900    0.001    0.000    0.001    0.000 layer.py:109(clear2)
                   4560    0.001    0.000    0.001    0.000 {built-in method builtins.isinstance}
                      7    0.000    0.000    0.001    0.000 functional.py:1737(linear)
                      1    0.000    0.000    0.001    0.001 _functional.py:53(adam)
                      7    0.001    0.000    0.001    0.000 {built-in method torch._C._nn.linear}
                      1    0.000    0.000    0.001    0.001 agent.py:107(__call__)
                    200    0.000    0.000    0.001    0.000 {built-in method builtins.all}
                   1300    0.000    0.000    0.001    0.000 layers.py:452(<genexpr>)
                      2    0.000    0.000    0.001    0.000 agent.py:56(modify_board)
                    100    0.000    0.000    0.001    0.000 layers.py:486(isFree)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-6>
Subject: Job 9464472: <causal3_9x9_20hours_1> in cluster <dcc> Done

Job <causal3_9x9_20hours_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Thu Mar 25 15:24:45 2021
Job was executed on host(s) <n-62-20-6>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Thu Mar 25 15:24:46 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Mar 25 15:24:46 2021
Terminated at Thu Mar 25 15:24:55 2021
Results reported at Thu Mar 25 15:24:55 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=8G]"
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

    CPU time :                                   4.51 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   71 sec.
    Turnaround time :                            10 sec.

The output (if any) is above this job summary.

