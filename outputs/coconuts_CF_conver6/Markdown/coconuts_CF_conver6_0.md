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
  File "main.py", line 110, in CFagent
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

    Name :                      coconuts_CF_conver6-0
    Main :                      CFagent
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
    Cf convert :                6
    Minutes used :              0 minutes.
    Hours used :                0 hours.

# Profiling


      3015742 function calls (3000437 primitive calls) in 12.34 seconds

##    Ordered by: cumulative time
   List reduced from 437 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000   12.337   12.337 {built-in method builtins.exec}
                      1    0.000    0.000   12.337   12.337 <string>:1(<module>)
                      1    0.010    0.010   12.337   12.337 main.py:94(CFagent)
                      3    0.000    0.000    8.318    2.773 agent.py:16(__init__)
                      3    0.000    0.000    8.318    2.773 network.py:33(__init__)
                      1    0.000    0.000    8.302    8.302 agent.py:109(__init__)
                    244    8.265    0.034    8.267    0.034 {method 'to' of 'torch._C._TensorBase' objects}
                      9    0.000    0.000    8.267    0.919 module.py:573(to)
                  111/9    0.001    0.000    8.267    0.919 module.py:385(_apply)
                     84    0.000    0.000    8.264    0.098 module.py:667(convert)
                    480    0.002    0.000    1.254    0.003 agent.py:29(learn)
                    478    0.031    0.000    1.037    0.002 learner.py:42(Qlearn)
                    161    0.001    0.000    0.857    0.005 game.py:40(step)
                    161    0.001    0.000    0.823    0.005 layers.py:643(step)
                      1    0.000    0.000    0.626    0.626 save.py:15(__exit__)
                      1    0.000    0.000    0.626    0.626 save.py:18(save)
                      5    0.508    0.102    0.625    0.125 save.py:24(saveObject)
                    161    0.015    0.000    0.570    0.004 layers.py:17(step)
             15280/1666    0.066    0.000    0.562    0.000 module.py:866(_call_impl)
                  16071    0.072    0.000    0.553    0.000 layer.py:93(move)
                   1188    0.003    0.000    0.523    0.000 network.py:24(forward)
                   1188    0.016    0.000    0.511    0.000 container.py:117(forward)
                    160    0.017    0.000    0.474    0.003 agent.py:54(_learn)
                    160    0.014    0.000    0.411    0.003 agent.py:208(_learn)
                    161    0.033    0.000    0.406    0.003 agent.py:216(counterfact)
                    478    0.005    0.000    0.401    0.001 optimizer.py:84(wrapper)
                    478    0.002    0.000    0.380    0.001 grad_mode.py:24(decorate_context)
                    478    0.016    0.000    0.373    0.001 adam.py:55(step)
                    160    0.004    0.000    0.367    0.002 agent.py:117(_learn)
                    161    0.025    0.000    0.345    0.002 layers.py:609(update)
                    356    0.008    0.000    0.342    0.001 agent.py:49(__call__)
                    478    0.072    0.000    0.335    0.001 _functional.py:53(adam)
                  16070    0.042    0.000    0.329    0.000 layers.py:660(check)
                    478    0.002    0.000    0.290    0.001 tensor.py:195(backward)
                    478    0.003    0.000    0.288    0.001 __init__.py:68(backward)
                    478    0.275    0.001    0.275    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                   2376    0.006    0.000    0.192    0.000 conv.py:398(forward)
                   2376    0.004    0.000    0.183    0.000 conv.py:390(_conv_forward)
                    161    0.077    0.000    0.181    0.001 agent.py:88(interveen)
                   2376    0.180    0.000    0.180    0.000 {built-in method conv2d}
                   2104    0.169    0.000    0.169    0.000 {built-in method tensor}
                     35    0.001    0.000    0.164    0.005 agent.py:170(choose_action)
                   1623    0.001    0.000    0.155    0.000 game.py:36(board)
                   2254    0.086    0.000    0.147    0.000 layer.py:148(update)
                   3243    0.007    0.000    0.143    0.000 linear.py:93(forward)
                    160    0.100    0.001    0.142    0.001 agent.py:67(modify)
                    160    0.078    0.000    0.142    0.001 replaybuffer.py:28(teleporter_save_data)
                   3243    0.003    0.000    0.132    0.000 functional.py:1737(linear)
                   3243    0.128    0.000    0.128    0.000 {built-in method torch._C._nn.linear}
                    140    0.001    0.000    0.123    0.001 layers.py:664(restart)
                  16070    0.086    0.000    0.112    0.000 layers.py:464(check)
                  16059    0.025    0.000    0.109    0.000 layers.py:654(isFree)
                      1    0.002    0.002    0.108    0.108 game.py:9(__init__)
                    140    0.001    0.000    0.107    0.001 level.py:8(__init__)
                  16070    0.080    0.000    0.107    0.000 layers.py:71(check)
                    140    0.007    0.000    0.103    0.001 levels.py:262(generate)
                 1405/5    0.039    0.000    0.102    0.020 {built-in method _pickle.dump}
                    516    0.004    0.000    0.098    0.000 agent.py:59(modify_board)
                   1734    0.016    0.000    0.090    0.000 level.py:41(notUsed)
                 103371    0.068    0.000    0.084    0.000 layer.py:90(isFree)
                 326190    0.059    0.000    0.083    0.000 enum.py:646(__hash__)
                   4431    0.004    0.000    0.082    0.000 activation.py:713(forward)
                    161    0.002    0.000    0.081    0.001 agent.py:112(__call__)
                   4431    0.004    0.000    0.078    0.000 functional.py:1364(leaky_relu)
                    160    0.002    0.000    0.078    0.000 replaybuffer.py:22(sample_data)
                    516    0.074    0.000    0.074    0.000 {built-in method torch._C._nn.one_hot}
                   4431    0.074    0.000    0.074    0.000 {built-in method torch._C._nn.leaky_relu}
                    158    0.002    0.000    0.071    0.000 agent.py:166(__call__)
                    160    0.031    0.000    0.064    0.000 replaybuffer.py:18(stacker)
                   2266    0.064    0.000    0.064    0.000 {built-in method cat}
                   8920    0.062    0.000    0.062    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                    350    0.001    0.000    0.059    0.000 storage.py:52(__reduce__)
                    350    0.001    0.000    0.058    0.000 serialization.py:333(save)
                   5902    0.058    0.000    0.058    0.000 {built-in method clone}
                    478    0.011    0.000    0.057    0.000 optimizer.py:189(zero_grad)
                  16122    0.013    0.000    0.056    0.000 {built-in method builtins.any}
                    356    0.029    0.000    0.056    0.000 exploration.py:53(softmaxer)
                    350    0.004    0.000    0.055    0.000 serialization.py:377(_legacy_save)
                   8920    0.055    0.000    0.055    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                  16100    0.006    0.000    0.051    0.000 {built-in method builtins.all}
                      9    0.000    0.000    0.051    0.006 network.py:15(__init__)
                   4460    0.050    0.000    0.050    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                  59306    0.017    0.000    0.047    0.000 layers.py:615(<genexpr>)
                    482    0.047    0.000    0.047    0.000 {built-in method nonzero}
                 127680    0.035    0.000    0.043    0.000 layers.py:625(<genexpr>)
                     18    0.000    0.000    0.041    0.002 conv.py:370(__init__)
                  16070    0.031    0.000    0.041    0.000 layers.py:56(check)
                     18    0.009    0.000    0.041    0.002 conv.py:66(__init__)
                      1    0.000    0.000    0.039    0.039 agent.py:105(pre_process)
                   1734    0.001    0.000    0.039    0.000 level.py:38(elementsIn)
                    350    0.038    0.000    0.038    0.000 {method '_write_file' of 'torch._C.CudaFloatStorageBase' objects}
                   4460    0.036    0.000    0.036    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                     42    0.000    0.000    0.035    0.001 init.py:347(kaiming_uniform_)
                  48839    0.034    0.000    0.034    0.000 layer.py:143(elements)
                     84    0.033    0.000    0.033    0.000 {method 'uniform_' of 'torch._C._TensorBase' objects}
                 336872    0.032    0.000    0.032    0.000 layer.py:86(positions)
                     18    0.000    0.000    0.031    0.002 conv.py:114(reset_parameters)
                  31304    0.025    0.000    0.030    0.000 tensor.py:906(grad)
                   4460    0.030    0.000    0.030    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                   4460    0.029    0.000    0.029    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-12>
Subject: Job 9500345: <coconuts_CF_conver6_0> in cluster <dcc> Done

Job <coconuts_CF_conver6_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed Apr  7 04:03:47 2021
Job was executed on host(s) <n-62-20-12>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed Apr  7 04:28:55 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed Apr  7 04:28:55 2021
Terminated at Wed Apr  7 04:29:13 2021
Results reported at Wed Apr  7 04:29:13 2021

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

    CPU time :                                   9.08 sec.
    Max Memory :                                 2115 MB
    Average Memory :                             2115.00 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14269.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                7
    Run time :                                   19 sec.
    Turnaround time :                            1526 sec.

The output (if any) is above this job summary.

