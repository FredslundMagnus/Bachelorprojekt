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
  File "main.py", line 52, in teleport
    observations, rewards, dones, info = env.step(actions)
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/game.py", line 41, in step
    rewards, dones, info = self.layers.step(action.tolist())
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/layers.py", line 645, in step
    self.player.step(action, self)
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/layers.py", line 21, in step
    self.move(batch, (x, y), (x + deltas[action][0], y + deltas[action][1]), layers, deltas[action])
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/layer.py", line 119, in move
    self.remove(batch, _from)
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/layer.py", line 124, in remove
    self._positions[batch].remove(_pos)
ValueError: list.remove(x): x not in list


# Parameters

    Name :                      coconuts_teleport-0
    Main :                      teleport
    Level :                     Levels.Coconuts
    Hours :                     34.0
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
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                2
    Minutes used :              0 minutes.
    Hours used :                0 hours.

# Profiling


      2599000 function calls (2589063 primitive calls) in 11.24 seconds

##    Ordered by: cumulative time
   List reduced from 421 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000   11.240   11.240 {built-in method builtins.exec}
                      1    0.000    0.000   11.240   11.240 <string>:1(<module>)
                      1    0.007    0.007   11.240   11.240 main.py:40(teleport)
                      2    0.000    0.000    8.324    4.162 agent.py:16(__init__)
                      2    0.000    0.000    8.324    4.162 network.py:33(__init__)
                      1    0.000    0.000    8.316    8.316 agent.py:109(__init__)
                    213    8.275    0.039    8.277    0.039 {method 'to' of 'torch._C._TensorBase' objects}
                      6    0.000    0.000    8.276    1.379 module.py:573(to)
                   72/6    0.000    0.000    8.276    1.379 module.py:385(_apply)
                     54    0.000    0.000    8.275    0.153 module.py:667(convert)
                    318    0.001    0.000    0.819    0.003 agent.py:29(learn)
                    160    0.001    0.000    0.809    0.005 game.py:40(step)
                    160    0.001    0.000    0.776    0.005 layers.py:643(step)
                    318    0.021    0.000    0.692    0.002 learner.py:42(Qlearn)
                    160    0.014    0.000    0.555    0.003 layers.py:17(step)
                  15955    0.074    0.000    0.539    0.000 layer.py:93(move)
                    159    0.015    0.000    0.464    0.003 agent.py:54(_learn)
             10041/1115    0.045    0.000    0.393    0.000 module.py:866(_call_impl)
                    797    0.002    0.000    0.365    0.000 network.py:24(forward)
                    797    0.010    0.000    0.357    0.000 container.py:117(forward)
                    159    0.004    0.000    0.354    0.002 agent.py:117(_learn)
                      1    0.000    0.000    0.336    0.336 save.py:15(__exit__)
                      1    0.000    0.000    0.336    0.336 save.py:18(save)
                      4    0.260    0.065    0.335    0.084 save.py:24(saveObject)
                  15954    0.042    0.000    0.323    0.000 layers.py:660(check)
                    319    0.006    0.000    0.317    0.001 agent.py:49(__call__)
                    160    0.024    0.000    0.314    0.002 layers.py:609(update)
                    160    0.085    0.001    0.296    0.002 agent.py:88(interveen)
                    318    0.003    0.000    0.266    0.001 optimizer.py:84(wrapper)
                    318    0.002    0.000    0.253    0.001 grad_mode.py:24(decorate_context)
                    318    0.010    0.000    0.248    0.001 adam.py:55(step)
                    318    0.048    0.000    0.226    0.001 _functional.py:53(adam)
                    318    0.001    0.000    0.192    0.001 tensor.py:195(backward)
                    318    0.002    0.000    0.191    0.001 __init__.py:68(backward)
                    318    0.183    0.001    0.183    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                    159    0.108    0.001    0.149    0.001 agent.py:67(modify)
                    159    0.081    0.001    0.149    0.001 replaybuffer.py:28(teleporter_save_data)
                   1594    0.004    0.000    0.135    0.000 conv.py:398(forward)
                   1594    0.002    0.000    0.129    0.000 conv.py:390(_conv_forward)
                   1594    0.127    0.000    0.127    0.000 {built-in method conv2d}
                    138    0.001    0.000    0.121    0.001 layers.py:664(restart)
                  15954    0.087    0.000    0.114    0.000 layers.py:464(check)
                      1    0.002    0.002    0.109    0.109 game.py:9(__init__)
                    138    0.001    0.000    0.106    0.001 level.py:8(__init__)
                  15954    0.074    0.000    0.103    0.000 layers.py:71(check)
                    138    0.007    0.000    0.101    0.001 levels.py:262(generate)
                   2072    0.005    0.000    0.100    0.000 linear.py:93(forward)
                  15955    0.022    0.000    0.098    0.000 layers.py:654(isFree)
                    478    0.003    0.000    0.093    0.000 agent.py:59(modify_board)
                   2072    0.002    0.000    0.093    0.000 functional.py:1737(linear)
                   2072    0.090    0.000    0.090    0.000 {built-in method torch._C._nn.linear}
                   1715    0.015    0.000    0.088    0.000 level.py:41(notUsed)
                 314508    0.057    0.000    0.083    0.000 enum.py:646(__hash__)
                   1120    0.050    0.000    0.081    0.000 layer.py:148(update)
                    160    0.002    0.000    0.077    0.000 agent.py:112(__call__)
                  93003    0.060    0.000    0.076    0.000 layer.py:90(isFree)
                    159    0.003    0.000    0.075    0.000 replaybuffer.py:22(sample_data)
                    478    0.071    0.000    0.071    0.000 {built-in method torch._C._nn.one_hot}
                  796/4    0.021    0.000    0.063    0.016 {built-in method _pickle.dump}
                   2869    0.003    0.000    0.061    0.000 activation.py:713(forward)
                    159    0.028    0.000    0.060    0.000 replaybuffer.py:18(stacker)
                   5694    0.058    0.000    0.058    0.000 {built-in method clone}
                   2869    0.003    0.000    0.058    0.000 functional.py:1364(leaky_relu)
                  15863    0.013    0.000    0.055    0.000 {built-in method builtins.any}
                   2869    0.055    0.000    0.055    0.000 {built-in method torch._C._nn.leaky_relu}
                    797    0.052    0.000    0.052    0.000 {built-in method tensor}
                    319    0.027    0.000    0.050    0.000 exploration.py:53(softmaxer)
                      6    0.000    0.000    0.048    0.008 network.py:15(__init__)
                   1432    0.045    0.000    0.045    0.000 {built-in method cat}
                 126896    0.035    0.000    0.042    0.000 layers.py:625(<genexpr>)
                     12    0.000    0.000    0.040    0.003 conv.py:370(__init__)
                     12    0.008    0.001    0.040    0.003 conv.py:66(__init__)
                    198    0.000    0.000    0.040    0.000 storage.py:52(__reduce__)
                   5724    0.040    0.000    0.040    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                    198    0.001    0.000    0.039    0.000 serialization.py:333(save)
                      1    0.000    0.000    0.039    0.039 agent.py:105(pre_process)
                   2862    0.039    0.000    0.039    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                    198    0.002    0.000    0.038    0.000 serialization.py:377(_legacy_save)
                   1715    0.001    0.000    0.038    0.000 level.py:38(elementsIn)
                    318    0.007    0.000    0.038    0.000 optimizer.py:189(zero_grad)
                  15954    0.027    0.000    0.038    0.000 layers.py:56(check)
                    319    0.000    0.000    0.038    0.000 game.py:36(board)
                   5724    0.035    0.000    0.035    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                     27    0.000    0.000    0.034    0.001 init.py:347(kaiming_uniform_)
                    160    0.032    0.000    0.032    0.000 {built-in method nonzero}
                     54    0.032    0.001    0.032    0.001 {method 'uniform_' of 'torch._C._TensorBase' objects}
                     12    0.000    0.000    0.030    0.003 conv.py:114(reset_parameters)
                    198    0.029    0.000    0.029    0.000 {method '_write_file' of 'torch._C.CudaFloatStorageBase' objects}
                 308271    0.029    0.000    0.029    0.000 layer.py:86(positions)
                  16000    0.004    0.000    0.026    0.000 {built-in method builtins.all}
                 314907    0.026    0.000    0.026    0.000 {built-in method builtins.hash}
                    159    0.015    0.000    0.025    0.000 collector.py:53(collect)
                   1715    0.012    0.000    0.024    0.000 level.py:39(<listcomp>)
                   2862    0.024    0.000    0.024    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                  76452    0.023    0.000    0.023    0.000 level.py:32(inverse)
                  45551    0.011    0.000    0.023    0.000 layers.py:615(<genexpr>)
                  15954    0.015    0.000    0.022    0.000 layers.py:42(check)
                   2862    0.019    0.000    0.019    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                   2862    0.019    0.000    0.019    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                    160    0.001    0.000    0.018    0.000 exploration.py:47(epsilonGreedy)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-12>
Subject: Job 9500349: <coconuts_teleport_0> in cluster <dcc> Done

Job <coconuts_teleport_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed Apr  7 04:03:47 2021
Job was executed on host(s) <n-62-20-12>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed Apr  7 04:33:28 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed Apr  7 04:33:28 2021
Terminated at Wed Apr  7 04:33:45 2021
Results reported at Wed Apr  7 04:33:45 2021

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

    CPU time :                                   8.18 sec.
    Max Memory :                                 2069 MB
    Average Memory :                             2069.00 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14315.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                7
    Run time :                                   18 sec.
    Turnaround time :                            1798 sec.

The output (if any) is above this job summary.

