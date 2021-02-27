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
  File "main.py", line 27, in main
    agent.learn(observations, actions, rewards, dones)
  File "/zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/agent.py", line 20, in learn
    self.learner.learn(self.values, state_after, action, reward, done)
  File "/zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/learner.py", line 32, in DoubleQlearn
    value_next = torch.gather(vals_target_next, 2, torch.argmax(vals_next, 2).unsqueeze(2))
IndexError: Dimension out of range (expected to be in range of [-2, 1], but got 2)


# Parameters

    Name :                      test_run_7-0
    Network :                   Networks.Small
    Learner :                   Learners.DoubleQlearn
    Gamma :                     1.0
    Batch :                     100
    Hours :                     0.2
    Width :                     15
    Height :                    15
    Minutes used :              0 minutes.
    Hours used :                0 hours.

# Profiling


      16007831 function calls (15965646 primitive calls) in 12.36 seconds

##    Ordered by: cumulative time
   List reduced from 233 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000   12.368   12.368 {built-in method builtins.exec}
                      1    0.000    0.000   12.367   12.367 <string>:1(<module>)
                      1    0.030    0.030   12.367   12.367 main.py:18(main)
                   3000    0.011    0.000    6.486    0.002 game.py:19(step)
                   3000    0.005    0.000    5.388    0.002 layers.py:202(step)
                   3000    0.182    0.000    3.953    0.001 layers.py:16(step)
                 300000    0.153    0.000    3.746    0.000 layer.py:65(move)
                   3000    0.072    0.000    2.998    0.001 agent.py:14(__call__)
                 300000    0.596    0.000    2.890    0.000 layers.py:218(check)
                      1    0.000    0.000    2.646    2.646 agent.py:10(__init__)
                      1    0.000    0.000    2.646    2.646 network.py:27(__init__)
                      3    0.000    0.000    2.641    0.880 module.py:529(to)
                   45/3    0.000    0.000    2.641    0.880 module.py:357(_apply)
                     36    0.000    0.000    2.640    0.073 module.py:607(convert)
                     36    2.640    0.073    2.640    0.073 {method 'to' of 'torch._C._TensorBase' objects}
             45030/3002    0.177    0.000    2.143    0.001 module.py:715(_call_impl)
                   3002    0.008    0.000    2.116    0.001 network.py:18(forward)
                   3002    0.052    0.000    2.090    0.001 container.py:115(forward)
                  12000    1.666    0.000    1.666    0.000 {built-in method tensor}
                   3001    0.169    0.000    1.597    0.001 layers.py:189(update)
                   6000    0.006    0.000    1.462    0.000 game.py:15(board)
                  18012    0.030    0.000    1.425    0.000 conv.py:422(forward)
                  18012    0.028    0.000    1.383    0.000 conv.py:414(_conv_forward)
                  18012    1.350    0.000    1.350    0.000 {built-in method conv2d}
                 300000    0.590    0.000    0.940    0.000 layers.py:123(check)
                 300100    0.072    0.000    0.707    0.000 {built-in method builtins.all}
                 300000    0.117    0.000    0.702    0.000 layers.py:212(isFree)
                 900900    0.196    0.000    0.667    0.000 layers.py:193(<genexpr>)
                2414108    0.419    0.000    0.595    0.000 enum.py:646(__hash__)
                 317228    0.522    0.000    0.585    0.000 layer.py:62(isFree)
                  24008    0.125    0.000    0.513    0.000 layer.py:90(update)
                 300000    0.308    0.000    0.487    0.000 layers.py:94(check)
                 300100    0.295    0.000    0.447    0.000 layers.py:64(isDone)
                 300000    0.271    0.000    0.393    0.000 layers.py:49(check)
                 300000    0.254    0.000    0.381    0.000 layers.py:76(check)
                4228739    0.358    0.000    0.358    0.000 layer.py:58(positions)
                  15010    0.013    0.000    0.300    0.000 activation.py:101(forward)
                  15010    0.020    0.000    0.287    0.000 functional.py:1124(relu)
                  15010    0.265    0.000    0.265    0.000 {built-in method relu}
                 116482    0.246    0.000    0.246    0.000 layer.py:85(elements)
                      1    0.000    0.000    0.194    0.194 game.py:8(__init__)
                2414108    0.176    0.000    0.176    0.000 {built-in method builtins.hash}
                    100    0.001    0.000    0.156    0.002 layers.py:222(restart)
                    100    0.000    0.000    0.139    0.001 levels.py:8(__init__)
                    100    0.000    0.000    0.139    0.001 level.py:8(__init__)
                    100    0.014    0.000    0.138    0.001 levels.py:11(generate)
                   3000    0.104    0.000    0.104    0.000 {method 'tolist' of 'torch._C._TensorBase' objects}
                   3000    0.095    0.000    0.095    0.000 {built-in method max}
                1200000    0.093    0.000    0.093    0.000 layer.py:48(check)
                   3002    0.004    0.000    0.079    0.000 activation.py:1197(forward)
                   3002    0.004    0.000    0.075    0.000 functional.py:1479(softmax)
                  24008    0.073    0.000    0.073    0.000 layer.py:97(<listcomp>)
                   3002    0.070    0.000    0.070    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
                  24008    0.069    0.000    0.069    0.000 layer.py:98(<listcomp>)
                    300    0.003    0.000    0.066    0.000 level.py:34(notUsed)
                  34500    0.062    0.000    0.062    0.000 level.py:25(inverse)
                    100    0.020    0.000    0.038    0.000 levels.py:71(RFS)
                 310494    0.037    0.000    0.037    0.000 layer.py:125(isBlocking)
                    200    0.014    0.000    0.037    0.000 layers.py:36(reset)
                  45030    0.034    0.000    0.034    0.000 {built-in method torch._C._get_tracing_state}
                   3002    0.002    0.000    0.031    0.000 flatten.py:39(forward)
                   3002    0.029    0.000    0.029    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                      1    0.000    0.000    0.028    0.028 layers.py:146(__init__)
                      8    0.000    0.000    0.028    0.003 layer.py:26(__init__)
                 300500    0.024    0.000    0.024    0.000 layer.py:51(isDone)
                  39173    0.023    0.000    0.023    0.000 module.py:765(__getattr__)
                  40358    0.017    0.000    0.022    0.000 layer.py:77(add)
                 183122    0.017    0.000    0.017    0.000 {method 'values' of 'collections.OrderedDict' objects}
                  45200    0.016    0.000    0.016    0.000 layer.py:100(grid)
                  21004    0.012    0.000    0.016    0.000 layer.py:73(remove)
                    800    0.002    0.000    0.016    0.000 layer.py:39(restart)
                   3001    0.012    0.000    0.012    0.000 layers.py:190(<listcomp>)
            95671/95670    0.012    0.000    0.012    0.000 {built-in method builtins.len}
                  19200    0.006    0.000    0.009    0.000 levels.py:28(<genexpr>)
                 117093    0.008    0.000    0.008    0.000 {method 'append' of 'list' objects}
                      1    0.000    0.000    0.008    0.008 agent.py:19(learn)
                      1    0.000    0.000    0.008    0.008 learner.py:29(DoubleQlearn)
                   3001    0.007    0.000    0.007    0.000 layers.py:191(<listcomp>)
                   5100    0.002    0.000    0.006    0.000 random.py:285(choice)
                      1    0.006    0.006    0.006    0.006 {built-in method argmax}
                   3001    0.004    0.000    0.005    0.000 auxillaries.py:17(loop)
                      3    0.000    0.000    0.005    0.002 network.py:13(__init__)
                   5715    0.003    0.000    0.004    0.000 random.py:250(_randbelow_with_getrandbits)
                   4800    0.004    0.000    0.004    0.000 {method 'intersection_update' of 'set' objects}
                     18    0.000    0.000    0.004    0.000 conv.py:394(__init__)
                     18    0.000    0.000    0.003    0.000 conv.py:37(__init__)
                   3002    0.002    0.000    0.003    0.000 container.py:107(__iter__)
                   4800    0.003    0.000    0.003    0.000 levels.py:81(<listcomp>)
                  21756    0.003    0.000    0.003    0.000 {method 'remove' of 'list' objects}
                  24669    0.003    0.000    0.003    0.000 {method 'add' of 'set' objects}
                    300    0.000    0.000    0.003    0.000 level.py:31(elementsIn)
                  14274    0.002    0.000    0.002    0.000 {built-in method builtins.min}
                  14274    0.002    0.000    0.002    0.000 {built-in method builtins.max}
                  18084    0.002    0.000    0.002    0.000 _jit_internal.py:750(is_scripting)
                   3001    0.002    0.000    0.002    0.000 {built-in method time.time}
                    200    0.001    0.000    0.002    0.000 random.py:315(sample)
                     18    0.000    0.000    0.002    0.000 conv.py:85(reset_parameters)
                    722    0.001    0.000    0.001    0.000 module.py:781(__setattr__)
                   6734    0.001    0.000    0.001    0.000 layers.py:97(isBlocking)
                    300    0.001    0.000    0.001    0.000 {built-in method _functools.reduce}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-2>
Subject: Job 9335761: <test_run_7_0> in cluster <dcc> Done

Job <test_run_7_0> was submitted from host <n-62-27-18> by user <s183905> in cluster <dcc> at Sat Feb 27 17:57:54 2021
Job was executed on host(s) <n-62-20-2>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sat Feb 27 17:57:55 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat Feb 27 17:57:55 2021
Terminated at Sat Feb 27 18:00:25 2021
Results reported at Sat Feb 27 18:00:25 2021

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

    CPU time :                                   13.62 sec.
    Max Memory :                                 2057 MB
    Average Memory :                             2057.00 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               6135.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                7
    Run time :                                   143 sec.
    Turnaround time :                            151 sec.

The output (if any) is above this job summary.

