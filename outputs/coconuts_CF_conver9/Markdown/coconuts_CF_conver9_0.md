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

    Name :                      coconuts_CF_conver9-0
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
    Cf convert :                9
    Minutes used :              0 minutes.
    Hours used :                0 hours.

# Profiling


      5715658 function calls (5685233 primitive calls) in 10.19 seconds

##    Ordered by: cumulative time
   List reduced from 438 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000   10.185   10.185 {built-in method builtins.exec}
                      1    0.000    0.000   10.185   10.185 <string>:1(<module>)
                      1    0.021    0.021   10.185   10.185 main.py:94(CFagent)
                      3    0.000    0.000    3.208    1.069 agent.py:16(__init__)
                      3    0.000    0.000    3.208    1.069 network.py:33(__init__)
                    424    3.194    0.008    3.195    0.008 {method 'to' of 'torch._C._TensorBase' objects}
                      9    0.000    0.000    3.191    0.355 module.py:573(to)
                  111/9    0.001    0.000    3.191    0.355 module.py:385(_apply)
                      1    0.000    0.000    3.191    3.191 agent.py:109(__init__)
                     84    0.000    0.000    3.189    0.038 module.py:667(convert)
                   1020    0.004    0.000    2.526    0.002 agent.py:29(learn)
                   1016    0.066    0.000    2.071    0.002 learner.py:42(Qlearn)
                    341    0.002    0.000    1.692    0.005 game.py:40(step)
                    341    0.002    0.000    1.620    0.005 layers.py:643(step)
                    341    0.031    0.000    1.173    0.003 layers.py:17(step)
                  34049    0.161    0.000    1.139    0.000 layer.py:93(move)
             32258/3524    0.135    0.000    1.078    0.000 module.py:866(_call_impl)
                   2508    0.007    0.000    0.998    0.000 network.py:24(forward)
                    340    0.031    0.000    0.980    0.003 agent.py:54(_learn)
                   2508    0.031    0.000    0.973    0.000 container.py:117(forward)
                    340    0.031    0.000    0.874    0.003 agent.py:208(_learn)
                   1016    0.010    0.000    0.805    0.001 optimizer.py:84(wrapper)
                   1016    0.005    0.000    0.762    0.001 grad_mode.py:24(decorate_context)
                   1016    0.033    0.000    0.746    0.001 adam.py:55(step)
                   1016    0.157    0.000    0.677    0.001 _functional.py:53(adam)
                    340    0.009    0.000    0.667    0.002 agent.py:117(_learn)
                  34048    0.092    0.000    0.666    0.000 layers.py:660(check)
                      1    0.000    0.000    0.617    0.617 save.py:15(__exit__)
                      1    0.000    0.000    0.617    0.617 save.py:18(save)
                      5    0.496    0.099    0.616    0.123 save.py:24(saveObject)
                    341    0.044    0.000    0.558    0.002 agent.py:216(counterfact)
                   1016    0.005    0.000    0.537    0.001 tensor.py:195(backward)
                    341    0.051    0.000    0.536    0.002 layers.py:609(update)
                   1016    0.005    0.000    0.532    0.001 __init__.py:68(backward)
                   1016    0.505    0.000    0.505    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                    748    0.016    0.000    0.497    0.001 agent.py:49(__call__)
                    341    0.158    0.000    0.380    0.001 agent.py:88(interveen)
                   5016    0.012    0.000    0.365    0.000 conv.py:398(forward)
                   5016    0.009    0.000    0.348    0.000 conv.py:390(_conv_forward)
                   4336    0.346    0.000    0.346    0.000 {built-in method tensor}
                   5016    0.339    0.000    0.339    0.000 {built-in method conv2d}
                    340    0.175    0.001    0.317    0.001 replaybuffer.py:28(teleporter_save_data)
                   3315    0.002    0.000    0.316    0.000 game.py:36(board)
                   4774    0.167    0.000    0.294    0.000 layer.py:148(update)
                   6843    0.014    0.000    0.270    0.000 linear.py:93(forward)
                    340    0.167    0.000    0.257    0.001 agent.py:67(modify)
                   6843    0.006    0.000    0.249    0.000 functional.py:1737(linear)
                   6843    0.242    0.000    0.242    0.000 {built-in method torch._C._nn.linear}
                  34048    0.175    0.000    0.226    0.000 layers.py:464(check)
                  33962    0.048    0.000    0.217    0.000 layers.py:654(isFree)
                  34048    0.154    0.000    0.213    0.000 layers.py:71(check)
                 210495    0.135    0.000    0.169    0.000 layer.py:90(isFree)
                    341    0.005    0.000    0.167    0.000 agent.py:112(__call__)
                    180    0.002    0.000    0.158    0.001 layers.py:664(restart)
                 609449    0.108    0.000    0.155    0.000 enum.py:646(__hash__)
                   1088    0.008    0.000    0.149    0.000 agent.py:59(modify_board)
                    336    0.004    0.000    0.148    0.000 agent.py:166(__call__)
                   4808    0.145    0.000    0.145    0.000 {built-in method cat}
                    340    0.009    0.000    0.144    0.000 replaybuffer.py:22(sample_data)
                   9351    0.008    0.000    0.143    0.000 activation.py:713(forward)
                    180    0.001    0.000    0.138    0.001 level.py:8(__init__)
                   9351    0.009    0.000    0.135    0.000 functional.py:1364(leaky_relu)
                    180    0.009    0.000    0.131    0.001 levels.py:262(generate)
                  18960    0.130    0.000    0.130    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                  12798    0.128    0.000    0.128    0.000 {built-in method clone}
                   9351    0.124    0.000    0.124    0.000 {built-in method torch._C._nn.leaky_relu}
                   1016    0.022    0.000    0.118    0.000 optimizer.py:189(zero_grad)
                  18960    0.117    0.000    0.117    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                  34262    0.027    0.000    0.116    0.000 {built-in method builtins.any}
                   2232    0.020    0.000    0.114    0.000 level.py:41(notUsed)
                    340    0.038    0.000    0.111    0.000 replaybuffer.py:18(stacker)
                 1405/5    0.039    0.000    0.106    0.021 {built-in method _pickle.dump}
                      1    0.002    0.002    0.104    0.104 game.py:9(__init__)
                     67    0.002    0.000    0.100    0.001 agent.py:170(choose_action)
                   1088    0.099    0.000    0.099    0.000 {built-in method torch._C._nn.one_hot}
                 271360    0.074    0.000    0.089    0.000 layers.py:625(<genexpr>)
                  34048    0.058    0.000    0.078    0.000 layers.py:56(check)
                   9480    0.077    0.000    0.077    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                    340    0.002    0.000    0.069    0.000 replaybuffer.py:49(sample_data)
                   9480    0.068    0.000    0.068    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                  88097    0.068    0.000    0.068    0.000 layer.py:143(elements)
                    350    0.001    0.000    0.063    0.000 storage.py:52(__reduce__)
                   9480    0.062    0.000    0.062    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                   9480    0.062    0.000    0.062    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                    350    0.001    0.000    0.062    0.000 serialization.py:333(save)
                 638521    0.061    0.000    0.061    0.000 layer.py:86(positions)
                    350    0.003    0.000    0.059    0.000 serialization.py:377(_legacy_save)
                  66444    0.045    0.000    0.056    0.000 tensor.py:906(grad)
                    340    0.031    0.000    0.053    0.000 collector.py:53(collect)
                    748    0.018    0.000    0.052    0.000 exploration.py:53(softmaxer)
                    336    0.004    0.000    0.050    0.000 replaybuffer.py:45(stacker)
                   1016    0.002    0.000    0.050    0.000 loss.py:527(forward)
          604258/604255    0.043    0.000    0.050    0.000 {built-in method builtins.len}
                   2232    0.002    0.000    0.049    0.000 level.py:38(elementsIn)
                  34048    0.033    0.000    0.048    0.000 layers.py:42(check)
                   1016    0.005    0.000    0.048    0.000 functional.py:2898(mse_loss)
                 610152    0.047    0.000    0.047    0.000 {built-in method builtins.hash}
                   9480    0.046    0.000    0.046    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                   1022    0.044    0.000    0.044    0.000 {built-in method nonzero}
                    350    0.043    0.000    0.043    0.000 {method '_write_file' of 'torch._C.CudaFloatStorageBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-12>
Subject: Job 9500348: <coconuts_CF_conver9_0> in cluster <dcc> Done

Job <coconuts_CF_conver9_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed Apr  7 04:03:47 2021
Job was executed on host(s) <n-62-20-12>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed Apr  7 04:33:13 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed Apr  7 04:33:13 2021
Terminated at Wed Apr  7 04:33:26 2021
Results reported at Wed Apr  7 04:33:26 2021

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

    CPU time :                                   11.14 sec.
    Max Memory :                                 4 MB
    Average Memory :                             4.00 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               16380.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                5
    Run time :                                   14 sec.
    Turnaround time :                            1779 sec.

The output (if any) is above this job summary.

