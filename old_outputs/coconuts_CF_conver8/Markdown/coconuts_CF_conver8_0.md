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

    Name :                      coconuts_CF_conver8-0
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
    Cf convert :                8
    Minutes used :              0 minutes.
    Hours used :                0 hours.

# Profiling


      18283664 function calls (18186111 primitive calls) in 25.11 seconds

##    Ordered by: cumulative time
   List reduced from 438 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000   25.106   25.106 {built-in method builtins.exec}
                      1    0.000    0.000   25.106   25.106 <string>:1(<module>)
                      1    0.076    0.076   25.105   25.105 main.py:94(CFagent)
                   3432    0.015    0.000    8.634    0.003 agent.py:29(learn)
                   3427    0.234    0.000    7.074    0.002 learner.py:42(Qlearn)
                   1145    0.006    0.000    5.785    0.005 game.py:40(step)
                   1145    0.007    0.000    5.536    0.005 layers.py:643(step)
                   1145    0.107    0.000    3.996    0.003 layers.py:17(step)
                 114430    0.565    0.000    3.878    0.000 layer.py:93(move)
           107659/11797    0.456    0.000    3.628    0.000 module.py:866(_call_impl)
                   8370    0.023    0.000    3.353    0.000 network.py:24(forward)
                   1144    0.110    0.000    3.339    0.003 agent.py:54(_learn)
                   8370    0.107    0.000    3.270    0.000 container.py:117(forward)
                   1228    3.205    0.003    3.206    0.003 {method 'to' of 'torch._C._TensorBase' objects}
                      3    0.000    0.000    3.205    1.068 agent.py:16(__init__)
                      3    0.000    0.000    3.204    1.068 network.py:33(__init__)
                      9    0.000    0.000    3.188    0.354 module.py:573(to)
                  111/9    0.001    0.000    3.188    0.354 module.py:385(_apply)
                      1    0.000    0.000    3.188    3.188 agent.py:109(__init__)
                     84    0.000    0.000    3.186    0.038 module.py:667(convert)
                   1144    0.106    0.000    2.997    0.003 agent.py:208(_learn)
                   3427    0.034    0.000    2.726    0.001 optimizer.py:84(wrapper)
                   3427    0.018    0.000    2.577    0.001 grad_mode.py:24(decorate_context)
                   3427    0.112    0.000    2.520    0.001 adam.py:55(step)
                   3427    0.530    0.000    2.284    0.001 _functional.py:53(adam)
                   1144    0.031    0.000    2.278    0.002 agent.py:117(_learn)
                 114429    0.307    0.000    2.191    0.000 layers.py:660(check)
                   3427    0.015    0.000    1.849    0.001 tensor.py:195(backward)
                   3427    0.017    0.000    1.834    0.001 __init__.py:68(backward)
                   3427    1.742    0.001    1.742    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                   1145    0.102    0.000    1.725    0.002 agent.py:216(counterfact)
                   2471    0.057    0.000    1.654    0.001 agent.py:49(__call__)
                   1145    0.170    0.000    1.616    0.001 layers.py:609(update)
                   1145    0.515    0.000    1.268    0.001 agent.py:88(interveen)
                  16740    0.039    0.000    1.219    0.000 conv.py:398(forward)
                  16740    0.026    0.000    1.162    0.000 conv.py:390(_conv_forward)
                  14231    1.145    0.000    1.145    0.000 {built-in method tensor}
                  16740    1.136    0.000    1.136    0.000 {built-in method conv2d}
                   1144    0.578    0.001    1.048    0.001 replaybuffer.py:28(teleporter_save_data)
                  10798    0.007    0.000    1.043    0.000 game.py:36(board)
                  16030    0.564    0.000    0.990    0.000 layer.py:148(update)
                  22821    0.049    0.000    0.909    0.000 linear.py:93(forward)
                   1144    0.579    0.001    0.892    0.001 agent.py:67(modify)
                  22821    0.021    0.000    0.836    0.000 functional.py:1737(linear)
                  22821    0.811    0.000    0.811    0.000 {built-in method torch._C._nn.linear}
                 114416    0.160    0.000    0.778    0.000 layers.py:654(isFree)
                 114429    0.560    0.000    0.722    0.000 layers.py:464(check)
                 114429    0.527    0.000    0.720    0.000 layers.py:71(check)
                      1    0.000    0.000    0.619    0.619 save.py:15(__exit__)
                      1    0.000    0.000    0.619    0.619 save.py:18(save)
                      5    0.499    0.100    0.618    0.124 save.py:24(saveObject)
                 644944    0.513    0.000    0.618    0.000 layer.py:90(isFree)
                   1145    0.017    0.000    0.574    0.001 agent.py:112(__call__)
                  16174    0.544    0.000    0.544    0.000 {built-in method cat}
                   1139    0.017    0.000    0.510    0.000 agent.py:166(__call__)
                   3615    0.026    0.000    0.507    0.000 agent.py:59(modify_board)
                   1144    0.069    0.000    0.490    0.000 replaybuffer.py:22(sample_data)
                  31191    0.028    0.000    0.489    0.000 activation.py:713(forward)
                1882440    0.344    0.000    0.487    0.000 enum.py:646(__hash__)
                  31191    0.029    0.000    0.461    0.000 functional.py:1364(leaky_relu)
                  63964    0.441    0.000    0.441    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                  31191    0.426    0.000    0.426    0.000 {built-in method torch._C._nn.leaky_relu}
                  42282    0.420    0.000    0.420    0.000 {built-in method clone}
                 115340    0.093    0.000    0.406    0.000 {built-in method builtins.any}
                   3427    0.074    0.000    0.401    0.000 optimizer.py:189(zero_grad)
                  63964    0.388    0.000    0.388    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                   3615    0.336    0.000    0.336    0.000 {built-in method torch._C._nn.one_hot}
                   1144    0.070    0.000    0.334    0.000 replaybuffer.py:18(stacker)
                 913552    0.260    0.000    0.313    0.000 layers.py:625(<genexpr>)
                   1144    0.013    0.000    0.288    0.000 replaybuffer.py:49(sample_data)
                    306    0.003    0.000    0.275    0.001 layers.py:664(restart)
                    188    0.004    0.000    0.269    0.001 agent.py:170(choose_action)
                  31982    0.259    0.000    0.259    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                 114429    0.182    0.000    0.241    0.000 layers.py:56(check)
                    306    0.002    0.000    0.240    0.001 level.py:8(__init__)
                  31982    0.235    0.000    0.235    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                 258328    0.235    0.000    0.235    0.000 layer.py:143(elements)
                    306    0.015    0.000    0.226    0.001 levels.py:262(generate)
                  31982    0.211    0.000    0.211    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                  31982    0.211    0.000    0.211    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                   1139    0.016    0.000    0.211    0.000 replaybuffer.py:45(stacker)
                2139036    0.206    0.000    0.206    0.000 layer.py:86(positions)
                   3792    0.034    0.000    0.196    0.000 level.py:41(notUsed)
                 223958    0.156    0.000    0.193    0.000 tensor.py:906(grad)
                   1144    0.106    0.000    0.180    0.000 collector.py:53(collect)
                   2471    0.061    0.000    0.176    0.000 exploration.py:53(softmaxer)
                   3427    0.006    0.000    0.175    0.000 loss.py:527(forward)
                 114429    0.117    0.000    0.170    0.000 layers.py:42(check)
                   3427    0.018    0.000    0.169    0.000 functional.py:2898(mse_loss)
        2083048/2083045    0.141    0.000    0.164    0.000 {built-in method builtins.len}
                 114500    0.031    0.000    0.162    0.000 {built-in method builtins.all}
                  31982    0.155    0.000    0.155    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                   3434    0.151    0.000    0.151    0.000 {built-in method nonzero}
                   1145    0.008    0.000    0.150    0.000 exploration.py:47(epsilonGreedy)
                   2288    0.052    0.000    0.147    0.000 random.py:315(sample)
                 344553    0.086    0.000    0.144    0.000 layers.py:615(<genexpr>)
                1883143    0.143    0.000    0.143    0.000 {built-in method builtins.hash}
                   1144    0.021    0.000    0.107    0.000 replaybuffer.py:55(CF_save_data)
                 1405/5    0.040    0.000    0.106    0.021 {built-in method _pickle.dump}
                      1    0.002    0.002    0.104    0.104 game.py:9(__init__)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-12>
Subject: Job 9500347: <coconuts_CF_conver8_0> in cluster <dcc> Done

Job <coconuts_CF_conver8_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed Apr  7 04:03:47 2021
Job was executed on host(s) <n-62-20-12>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed Apr  7 04:32:44 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed Apr  7 04:32:44 2021
Terminated at Wed Apr  7 04:33:11 2021
Results reported at Wed Apr  7 04:33:11 2021

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

    CPU time :                                   26.07 sec.
    Max Memory :                                 2332 MB
    Average Memory :                             2332.00 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14052.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   29 sec.
    Turnaround time :                            1764 sec.

The output (if any) is above this job summary.

