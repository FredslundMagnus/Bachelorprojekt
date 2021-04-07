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

    Name :                      coconuts_CF_conver7-0
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
    Cf convert :                7
    Minutes used :              1 minutes.
    Hours used :                0 hours.

# Profiling


      74243587 function calls (73863290 primitive calls) in 89.70 seconds

##    Ordered by: cumulative time
   List reduced from 438 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000   89.703   89.703 {built-in method builtins.exec}
                      1    0.000    0.000   89.703   89.703 <string>:1(<module>)
                      1    0.320    0.320   89.703   89.703 main.py:94(CFagent)
                  13557    0.061    0.000   34.114    0.003 agent.py:29(learn)
                  13547    0.920    0.000   27.969    0.002 learner.py:42(Qlearn)
                   4520    0.027    0.000   24.170    0.005 game.py:40(step)
                   4520    0.027    0.000   23.192    0.005 layers.py:643(step)
                   4520    0.436    0.000   16.222    0.004 layers.py:17(step)
                 451826    2.277    0.000   15.736    0.000 layer.py:93(move)
           425210/46604    1.815    0.000   14.287    0.000 module.py:866(_call_impl)
                   4519    0.439    0.000   13.227    0.003 agent.py:54(_learn)
                  33057    0.092    0.000   13.177    0.000 network.py:24(forward)
                  33057    0.421    0.000   12.854    0.000 container.py:117(forward)
                   4519    0.409    0.000   11.854    0.003 agent.py:208(_learn)
                  13547    0.138    0.000   10.816    0.001 optimizer.py:84(wrapper)
                  13547    0.069    0.000   10.233    0.001 grad_mode.py:24(decorate_context)
                  13547    0.440    0.000   10.016    0.001 adam.py:55(step)
                  13547    2.129    0.000    9.091    0.001 _functional.py:53(adam)
                   4519    0.125    0.000    8.953    0.002 agent.py:117(_learn)
                 451825    1.313    0.000    8.778    0.000 layers.py:660(check)
                  13547    0.061    0.000    7.315    0.001 tensor.py:195(backward)
                  13547    0.063    0.000    7.251    0.001 __init__.py:68(backward)
                   4520    0.721    0.000    7.001    0.002 layers.py:609(update)
                  13547    6.898    0.001    6.898    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                   4520    0.350    0.000    6.670    0.001 agent.py:216(counterfact)
                   9757    0.232    0.000    6.513    0.001 agent.py:49(__call__)
                   4520    2.035    0.000    5.016    0.001 agent.py:88(interveen)
                  66114    0.155    0.000    4.782    0.000 conv.py:398(forward)
                  66114    0.101    0.000    4.557    0.000 conv.py:390(_conv_forward)
                  55835    4.494    0.000    4.494    0.000 {built-in method tensor}
                  66114    4.456    0.000    4.456    0.000 {built-in method conv2d}
                   4519    2.299    0.001    4.215    0.001 replaybuffer.py:28(teleporter_save_data)
                  42284    0.029    0.000    4.087    0.000 game.py:36(board)
                  63280    2.237    0.000    3.936    0.000 layer.py:148(update)
                  90132    0.187    0.000    3.585    0.000 linear.py:93(forward)
                   4519    2.289    0.001    3.529    0.001 agent.py:67(modify)
                 451451    0.729    0.000    3.346    0.000 layers.py:654(isFree)
                  90132    0.082    0.000    3.304    0.000 functional.py:1737(linear)
                   4603    3.224    0.001    3.225    0.001 {method 'to' of 'torch._C._TensorBase' objects}
                  90132    3.203    0.000    3.203    0.000 {built-in method torch._C._nn.linear}
                      3    0.000    0.000    3.168    1.056 agent.py:16(__init__)
                      3    0.000    0.000    3.167    1.056 network.py:33(__init__)
                      1    0.000    0.000    3.152    3.152 agent.py:109(__init__)
                      9    0.000    0.000    3.151    0.350 module.py:573(to)
                  111/9    0.001    0.000    3.151    0.350 module.py:385(_apply)
                     84    0.000    0.000    3.149    0.037 module.py:667(convert)
                 451825    2.234    0.000    3.020    0.000 layers.py:71(check)
                 451825    2.078    0.000    2.725    0.000 layers.py:464(check)
                   4519    0.809    0.000    2.630    0.001 replaybuffer.py:22(sample_data)
                2637258    2.208    0.000    2.617    0.000 layer.py:90(isFree)
                  63935    2.308    0.000    2.308    0.000 {built-in method cat}
                   4520    0.072    0.000    2.269    0.001 agent.py:112(__call__)
                7773548    1.427    0.000    2.007    0.000 enum.py:646(__hash__)
                   4509    0.065    0.000    2.002    0.000 agent.py:166(__call__)
                  14276    0.108    0.000    2.000    0.000 agent.py:59(modify_board)
                 123189    0.108    0.000    1.900    0.000 activation.py:713(forward)
                 123189    0.116    0.000    1.791    0.000 functional.py:1364(leaky_relu)
                 252864    1.773    0.000    1.773    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                 166759    1.722    0.000    1.722    0.000 {built-in method clone}
                 123189    1.654    0.000    1.654    0.000 {built-in method torch._C._nn.leaky_relu}
                  13547    0.294    0.000    1.588    0.000 optimizer.py:189(zero_grad)
                 455640    0.374    0.000    1.566    0.000 {built-in method builtins.any}
                 252864    1.547    0.000    1.547    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                 452000    0.174    0.000    1.527    0.000 {built-in method builtins.all}
                   4519    0.369    0.000    1.471    0.000 replaybuffer.py:18(stacker)
                1844615    0.499    0.000    1.408    0.000 layers.py:615(<genexpr>)
                  14276    1.329    0.000    1.329    0.000 {built-in method torch._C._nn.one_hot}
                   4519    0.068    0.000    1.327    0.000 replaybuffer.py:49(sample_data)
                3608952    0.976    0.000    1.193    0.000 layers.py:625(<genexpr>)
                 126432    1.023    0.000    1.023    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                    724    0.017    0.000    0.997    0.001 agent.py:170(choose_action)
                 451825    0.726    0.000    0.960    0.000 layers.py:56(check)
                   4509    0.073    0.000    0.958    0.000 replaybuffer.py:45(stacker)
                9382009    0.945    0.000    0.945    0.000 layer.py:86(positions)
                 973631    0.942    0.000    0.942    0.000 layer.py:143(elements)
                 126432    0.923    0.000    0.923    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                 126432    0.833    0.000    0.833    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                 452000    0.557    0.000    0.831    0.000 layers.py:107(isDone)
                 126432    0.827    0.000    0.827    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                    881    0.012    0.000    0.790    0.001 layers.py:664(restart)
                 885108    0.612    0.000    0.754    0.000 tensor.py:906(grad)
                   4519    0.422    0.000    0.717    0.000 collector.py:53(collect)
                  13547    0.031    0.000    0.694    0.000 loss.py:527(forward)
                   9757    0.245    0.000    0.686    0.000 exploration.py:53(softmaxer)
                    881    0.006    0.000    0.683    0.001 level.py:8(__init__)
                  13547    0.067    0.000    0.663    0.000 functional.py:2898(mse_loss)
        8169651/8169648    0.563    0.000    0.654    0.000 {built-in method builtins.len}
                    881    0.046    0.000    0.642    0.001 levels.py:262(generate)
                   9038    0.228    0.000    0.638    0.000 random.py:315(sample)
                 451825    0.427    0.000    0.634    0.000 layers.py:42(check)
                      1    0.000    0.000    0.617    0.617 save.py:15(__exit__)
                      1    0.000    0.000    0.617    0.617 save.py:18(save)
                      5    0.497    0.099    0.616    0.123 save.py:24(saveObject)
                 126432    0.615    0.000    0.615    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                  13559    0.601    0.000    0.601    0.000 {built-in method nonzero}
                   4520    0.031    0.000    0.584    0.000 exploration.py:47(epsilonGreedy)
                7774251    0.580    0.000    0.580    0.000 {built-in method builtins.hash}
                  10887    0.099    0.000    0.555    0.000 level.py:41(notUsed)
                   4519    0.081    0.000    0.421    0.000 replaybuffer.py:55(CF_save_data)
                  13547    0.406    0.000    0.406    0.000 {built-in method torch._C._nn.mse_loss}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-12>
Subject: Job 9500346: <coconuts_CF_conver7_0> in cluster <dcc> Done

Job <coconuts_CF_conver7_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed Apr  7 04:03:47 2021
Job was executed on host(s) <n-62-20-12>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed Apr  7 04:31:09 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed Apr  7 04:31:09 2021
Terminated at Wed Apr  7 04:32:42 2021
Results reported at Wed Apr  7 04:32:42 2021

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

    CPU time :                                   90.81 sec.
    Max Memory :                                 2330 MB
    Average Memory :                             2330.00 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14054.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   94 sec.
    Turnaround time :                            1735 sec.

The output (if any) is above this job summary.

