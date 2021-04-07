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

    Name :                      coconuts_CF_conver5-0
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
    Cf convert :                5
    Minutes used :              2 minutes.
    Hours used :                0 hours.

# Profiling


      107335730 function calls (106778553 primitive calls) in 143.09 seconds

##    Ordered by: cumulative time
   List reduced from 469 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000  143.085  143.085 {built-in method builtins.exec}
                      1    0.000    0.000  143.085  143.085 <string>:1(<module>)
                      1    0.456    0.456  143.085  143.085 main.py:94(CFagent)
                  19902    0.085    0.000   50.642    0.003 agent.py:29(learn)
                  19897    1.349    0.000   41.548    0.002 learner.py:42(Qlearn)
                   6635    0.033    0.000   35.136    0.005 game.py:40(step)
                   6635    0.041    0.000   33.726    0.005 layers.py:643(step)
                   6635    0.667    0.000   24.049    0.004 layers.py:17(step)
                 663228    3.361    0.000   23.306    0.000 layer.py:93(move)
           623885/68399    2.700    0.000   21.169    0.000 module.py:866(_call_impl)
                   6634    0.649    0.000   19.644    0.003 agent.py:54(_learn)
                  48502    0.139    0.000   19.549    0.000 network.py:24(forward)
                  48502    0.614    0.000   19.071    0.000 container.py:117(forward)
                   6634    0.599    0.000   17.606    0.003 agent.py:208(_learn)
                  19897    0.205    0.000   16.238    0.001 optimizer.py:84(wrapper)
                   6718   15.487    0.002   15.489    0.002 {method 'to' of 'torch._C._TensorBase' objects}
                      3    0.000    0.000   15.433    5.144 agent.py:16(__init__)
                      3    0.000    0.000   15.432    5.144 network.py:33(__init__)
                      1    0.000    0.000   15.415   15.415 agent.py:109(__init__)
                  19897    0.103    0.000   15.381    0.001 grad_mode.py:24(decorate_context)
                      9    0.000    0.000   15.377    1.709 module.py:573(to)
                  111/9    0.001    0.000   15.377    1.709 module.py:385(_apply)
                     84    0.000    0.000   15.375    0.183 module.py:667(convert)
                  19897    0.671    0.000   15.065    0.001 adam.py:55(step)
                  19897    3.151    0.000   13.668    0.001 _functional.py:53(adam)
                   6634    0.183    0.000   13.279    0.002 agent.py:117(_learn)
                 663227    1.749    0.000   12.669    0.000 layers.py:660(check)
                  19897    0.097    0.000   10.780    0.001 tensor.py:195(backward)
                  19897    0.093    0.000   10.680    0.001 __init__.py:68(backward)
                  19897   10.151    0.001   10.151    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                   6635    0.499    0.000    9.834    0.001 agent.py:216(counterfact)
                  14294    0.337    0.000    9.777    0.001 agent.py:49(__call__)
                   6635    0.994    0.000    9.677    0.001 layers.py:609(update)
                   6635    2.981    0.000    7.356    0.001 agent.py:88(interveen)
                  97004    0.227    0.000    7.030    0.000 conv.py:398(forward)
                  97004    0.146    0.000    6.697    0.000 conv.py:390(_conv_forward)
                  97004    6.551    0.000    6.551    0.000 {built-in method conv2d}
                  81864    6.485    0.000    6.485    0.000 {built-in method tensor}
                   6634    3.374    0.001    6.154    0.001 replaybuffer.py:28(teleporter_save_data)
                  61988    0.039    0.000    5.899    0.000 game.py:36(board)
                  92890    3.216    0.000    5.721    0.000 layer.py:148(update)
                 132237    0.287    0.000    5.315    0.000 linear.py:93(forward)
                 662537    1.104    0.000    5.255    0.000 layers.py:654(isFree)
                   6634    3.348    0.001    5.145    0.001 agent.py:67(modify)
                 132237    0.117    0.000    4.889    0.000 functional.py:1737(linear)
                 132237    4.744    0.000    4.744    0.000 {built-in method torch._C._nn.linear}
                   6634    1.705    0.000    4.511    0.001 replaybuffer.py:22(sample_data)
                 663227    3.092    0.000    4.195    0.000 layers.py:71(check)
                 663227    3.257    0.000    4.182    0.000 layers.py:464(check)
                4404152    3.475    0.000    4.151    0.000 layer.py:90(isFree)
                  93877    3.476    0.000    3.476    0.000 {built-in method cat}
                   6635    0.103    0.000    3.326    0.001 agent.py:112(__call__)
                   6629    0.096    0.000    2.971    0.000 agent.py:166(__call__)
               11357399    2.093    0.000    2.964    0.000 enum.py:646(__hash__)
                  20928    0.156    0.000    2.952    0.000 agent.py:59(modify_board)
                 180739    0.165    0.000    2.896    0.000 activation.py:713(forward)
                 180739    0.167    0.000    2.730    0.000 functional.py:1364(leaky_relu)
                 371404    2.681    0.000    2.681    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                 180739    2.532    0.000    2.532    0.000 {built-in method torch._C._nn.leaky_relu}
                 245055    2.496    0.000    2.496    0.000 {built-in method clone}
                 668909    0.548    0.000    2.438    0.000 {built-in method builtins.any}
                  19897    0.444    0.000    2.366    0.000 optimizer.py:189(zero_grad)
                 371404    2.335    0.000    2.335    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                   6634    0.611    0.000    2.282    0.000 replaybuffer.py:18(stacker)
                   6634    0.115    0.000    2.014    0.000 replaybuffer.py:49(sample_data)
                  20928    1.972    0.000    1.972    0.000 {built-in method torch._C._nn.one_hot}
                5298184    1.546    0.000    1.890    0.000 layers.py:625(<genexpr>)
                 663500    0.134    0.000    1.641    0.000 {built-in method builtins.all}
                   1047    0.023    0.000    1.620    0.002 agent.py:170(choose_action)
                1382709    0.328    0.000    1.593    0.000 layers.py:615(<genexpr>)
                 185702    1.533    0.000    1.533    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                   6629    0.106    0.000    1.443    0.000 replaybuffer.py:45(stacker)
                 185702    1.405    0.000    1.405    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                 663227    1.054    0.000    1.384    0.000 layers.py:56(check)
                1415411    1.371    0.000    1.371    0.000 layer.py:143(elements)
               13958125    1.358    0.000    1.358    0.000 layer.py:86(positions)
                 185702    1.266    0.000    1.266    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                 185702    1.246    0.000    1.246    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                 663500    0.841    0.000    1.244    0.000 layers.py:107(isDone)
                1299998    0.908    0.000    1.126    0.000 tensor.py:906(grad)
                   1227    0.017    0.000    1.125    0.001 layers.py:664(restart)
                  14294    0.387    0.000    1.073    0.000 exploration.py:53(softmaxer)
                   6634    0.633    0.000    1.069    0.000 collector.py:53(collect)
                  19897    0.037    0.000    1.015    0.000 loss.py:527(forward)
                 663227    0.686    0.000    0.988    0.000 layers.py:42(check)
                  19897    0.096    0.000    0.978    0.000 functional.py:2898(mse_loss)
                   1227    0.009    0.000    0.975    0.001 level.py:8(__init__)
                  13268    0.341    0.000    0.959    0.000 random.py:315(sample)
        12018718/12018715    0.829    0.000    0.957    0.000 {built-in method builtins.len}
                   1227    0.064    0.000    0.916    0.001 levels.py:262(generate)
                 185702    0.910    0.000    0.910    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                  19904    0.910    0.000    0.910    0.000 {built-in method nonzero}
               11358102    0.872    0.000    0.872    0.000 {built-in method builtins.hash}
                   6635    0.045    0.000    0.851    0.000 exploration.py:47(epsilonGreedy)
                  15172    0.140    0.000    0.793    0.000 level.py:41(notUsed)
                      1    0.000    0.000    0.623    0.623 save.py:15(__exit__)
                      1    0.000    0.000    0.623    0.623 save.py:18(save)
                      5    0.498    0.100    0.622    0.124 save.py:24(saveObject)
                   6634    0.120    0.000    0.608    0.000 replaybuffer.py:55(CF_save_data)
                  19897    0.600    0.000    0.600    0.000 {built-in method torch._C._nn.mse_loss}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-12>
Subject: Job 9500344: <coconuts_CF_conver5_0> in cluster <dcc> Done

Job <coconuts_CF_conver5_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed Apr  7 04:03:47 2021
Job was executed on host(s) <n-62-20-12>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed Apr  7 04:26:21 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed Apr  7 04:26:21 2021
Terminated at Wed Apr  7 04:28:54 2021
Results reported at Wed Apr  7 04:28:54 2021

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

    CPU time :                                   133.88 sec.
    Max Memory :                                 2539 MB
    Average Memory :                             1987.75 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13845.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   239 sec.
    Turnaround time :                            1507 sec.

The output (if any) is above this job summary.

