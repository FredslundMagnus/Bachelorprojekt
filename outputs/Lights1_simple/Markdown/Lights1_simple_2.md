
# Parameters

    Name :                      Lights1_simple-2
    Main :                      simple
    Level :                     Levels.Causal3
    Failed actions chance :     0.0
    Hours :                     24.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.UCB1
    Network1 :                  Networks.Teleporter
    K1 :                        5000000
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.MiniBig
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
    Layer greencross :          True
    Layer bluecross :           True
    Layer redcross :            True
    Layer purplecross :         True
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                3
    Counterfacts :              1
    Topn :                      6
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      177259813640 function calls (176984187669 primitive calls) in 86102.70 seconds

##    Ordered by: cumulative time
   List reduced from 414 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86102.702 86102.702 {built-in method builtins.exec}
                      1    0.001    0.001 86102.702 86102.702 <string>:1(<module>)
                      1  158.787  158.787 86102.701 86102.701 main.py:66(simple)
               11484400   35.026    0.000 50758.332    0.004 game.py:41(step)
               11484400   50.438    0.000 48401.835    0.004 layers.py:718(step)
               11484400   33.978    0.000 27438.743    0.002 agent.py:29(learn)
               11484400  238.994    0.000 27383.145    0.002 agent.py:117(_learn)
               11484400  702.477    0.000 27144.151    0.002 learner.py:42(Qlearn)
               11484400  793.213    0.000 25576.542    0.002 layers.py:17(step)
             1148440000 1628.254    0.000 24690.631    0.000 layer.py:98(move)
               11484401 1470.420    0.000 22711.189    0.002 layers.py:684(update)
             1148440000 3768.683    0.000 17317.038    0.000 layers.py:735(check)
               11484400   63.643    0.000 11210.650    0.001 grad_mode.py:23(decorate_context)
               11484400  354.960    0.000 11030.004    0.001 adam.py:55(step)
        310078800/34453200 1049.029    0.000 10697.401    0.000 module.py:715(_call_impl)
               22968800   49.709    0.000 9910.187    0.000 network.py:27(forward)
               22968800  251.125    0.000 9737.611    0.000 container.py:115(forward)
               11484400 2044.384    0.000 9078.517    0.001 functional.py:53(adam)
               32162081  257.829    0.000 8836.757    0.000 layers.py:740(restart)
               32162081  119.171    0.000 6234.115    0.000 level.py:8(__init__)
               11484400   60.337    0.000 6069.232    0.001 tensor.py:181(backward)
               11484400   34.701    0.000 6008.894    0.001 __init__.py:68(backward)
               11484400 5732.855    0.000 5732.855    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
               11484400  126.830    0.000 5553.350    0.000 agent.py:112(__call__)
               32162081  557.311    0.000 5131.087    0.000 levels.py:164(generate)
               91875208 2885.651    0.000 5130.943    0.000 layer.py:167(NoRock_update)
             2195811700 1301.861    0.000 4787.666    0.000 {built-in method builtins.any}
             1148440000 1088.698    0.000 4765.567    0.000 layers.py:729(isFree)
            19663588924 3221.104    0.000 4608.089    0.000 enum.py:646(__hash__)
               64324162  511.980    0.000 3784.738    0.000 level.py:41(notUsed)
             4805424012 2942.220    0.000 3676.869    0.000 layer.py:95(isFree)
               45937600   74.075    0.000 3519.919    0.000 conv.py:422(forward)
             1148440000 2139.567    0.000 3419.194    0.000 layers.py:246(check)
               45937600   85.973    0.000 3418.580    0.000 conv.py:414(_conv_forward)
               48578643 3338.501    0.000 3338.501    0.000 {built-in method tensor}
               45937600 3317.493    0.000 3317.493    0.000 {built-in method conv2d}
               68906400  144.900    0.000 3257.832    0.000 linear.py:92(forward)
             1148440000 1987.338    0.000 3251.776    0.000 layers.py:286(check)
               68906400  229.497    0.000 3051.309    0.000 functional.py:1669(linear)
            10046502171 2439.381    0.000 2968.462    0.000 layers.py:700(<genexpr>)
             1148440100  525.848    0.000 2932.250    0.000 {built-in method builtins.all}
              803908030 1731.878    0.000 2873.546    0.000 tensor.py:933(grad)
               22968800   19.430    0.000 2663.309    0.000 game.py:37(board)
             6216663908 1486.912    0.000 2540.171    0.000 layers.py:690(<genexpr>)
               11484400  221.980    0.000 2497.755    0.000 optimizer.py:167(zero_grad)
              257296648  265.341    0.000 2261.381    0.000 layer.py:69(restart)
               68906400 2158.814    0.000 2158.814    0.000 {built-in method addmm}
              229688000 1829.677    0.000 1829.677    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
             1148440000 1087.977    0.000 1715.341    0.000 layers.py:273(check)
             1148440000 1077.320    0.000 1701.821    0.000 layers.py:313(check)
            19235076562 1700.365    0.000 1700.365    0.000 layer.py:91(positions)
              229688000 1538.945    0.000 1538.945    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               64324162   51.382    0.000 1532.254    0.000 level.py:38(elementsIn)
               32162181  761.536    0.000 1509.395    0.000 layers.py:36(reset)
             1148440000  941.414    0.000 1429.184    0.000 layers.py:48(check)
              987658480  474.237    0.000 1392.618    0.000 overrides.py:1070(has_torch_function)
            19663634953 1386.994    0.000 1386.994    0.000 {built-in method builtins.hash}
               91875200   68.059    0.000 1365.110    0.000 activation.py:713(forward)
               91875200  107.199    0.000 1297.051    0.000 functional.py:1292(leaky_relu)
             2109965391 1296.990    0.000 1296.990    0.000 level.py:32(inverse)
             4410834102 1295.517    0.000 1295.517    0.000 layer.py:146(elements)
               91875200 1178.646    0.000 1178.646    0.000 {built-in method torch._C._nn.leaky_relu}
             1148440000  786.866    0.000 1164.261    0.000 layers.py:23(check)
              114844000 1034.899    0.000 1034.899    0.000 {method 'add' of 'torch._C._TensorBase' objects}
             2116445738  736.663    0.000 1003.342    0.000 layer.py:130(add)
              114844000  976.376    0.000  976.376    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               64324162  460.756    0.000  941.978    0.000 level.py:39(<listcomp>)
               11484400  539.343    0.000  925.778    0.000 collector.py:46(collect)
               32162081  423.140    0.000  904.351    0.000 level.py:16(<dictcomp>)
              114844000  860.924    0.000  860.924    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
        12201842267/12201842266  709.373    0.000  777.238    0.000 {built-in method builtins.len}
            10495390910  772.748    0.000  772.748    0.000 {method 'random' of '_random.Random' objects}
              114844000  764.566    0.000  764.566    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
             3473506279  610.659    0.000  610.659    0.000 enum.py:352(<genexpr>)
              114844000  590.472    0.000  590.472    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               64324162  212.377    0.000  542.566    0.000 random.py:315(sample)
               64324162  323.283    0.000  538.894    0.000 {built-in method _functools.reduce}
               11484400   18.809    0.000  531.348    0.000 loss.py:445(forward)
             8930224152  529.081    0.000  529.081    0.000 layer.py:84(isDead)
               11484400   55.610    0.000  512.539    0.000 functional.py:2637(mse_loss)
             2044223360  411.303    0.000  510.409    0.000 overrides.py:1083(<genexpr>)
               11484400   37.684    0.000  442.889    0.000 exploration.py:47(epsilonGreedy)
             1148440100  311.966    0.000  425.517    0.000 layers.py:52(isDone)
             3944879397  420.986    0.000  420.986    0.000 layer.py:203(isBlocking)
             5906186601  408.155    0.000  408.155    0.000 {method 'append' of 'list' objects}
              237182586  255.353    0.000  395.263    0.000 layers.py:113(isDone)
               68906400  384.216    0.000  384.216    0.000 {method 't' of 'torch._C._TensorBase' objects}
              461431092  211.002    0.000  320.470    0.000 layer.py:126(remove)
               11484400  316.867    0.000  316.867    0.000 {method 'tolist' of 'torch._C._TensorBase' objects}
             2637299498  303.628    0.000  303.628    0.000 layer.py:182(grid)
              400831175  209.120    0.000  299.240    0.000 random.py:250(_randbelow_with_getrandbits)
               11484400  298.685    0.000  298.685    0.000 {built-in method torch._C._nn.mse_loss}
               22968800  298.290    0.000  298.290    0.000 {built-in method sum}
              114844050  128.289    0.000  289.100    0.000 tensor.py:596(__hash__)
               91875208  279.412    0.000  279.412    0.000 layer.py:178(<listcomp>)
               11485548  270.456    0.000  270.456    0.000 {built-in method max}
               91875208  260.890    0.000  260.890    0.000 layer.py:179(<listcomp>)
               45937600   29.787    0.000  234.593    0.000 flatten.py:39(forward)
             3682601122  232.479    0.000  232.479    0.000 layer.py:81(isDone)
               11484400   45.029    0.000  232.281    0.000 __init__.py:28(_make_grads)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9578830: <Lights1_simple_2> in cluster <dcc> Done

Job <Lights1_simple_2> was submitted from host <n-62-30-3> by user <s183905> in cluster <dcc> at Mon Apr 26 20:44:04 2021
Job was executed on host(s) <n-62-20-6>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Wed Apr 28 11:30:34 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed Apr 28 11:30:34 2021
Terminated at Thu Apr 29 11:25:40 2021
Results reported at Thu Apr 29 11:25:40 2021

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

    CPU time :                                   85899.73 sec.
    Max Memory :                                 2062 MB
    Average Memory :                             2061.00 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14322.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86107 sec.
    Turnaround time :                            225696 sec.

The output (if any) is above this job summary.

