
# Parameters

    Name :                      Diamonds2_simple-1
    Main :                      simple
    Level :                     Levels.Causal5
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


      174522249565 function calls (174286505178 primitive calls) in 86102.91 seconds

##    Ordered by: cumulative time
   List reduced from 409 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86102.912 86102.912 {built-in method builtins.exec}
                      1    0.001    0.001 86102.912 86102.912 <string>:1(<module>)
                      1  149.469  149.469 86102.911 86102.911 main.py:66(simple)
                9822668   32.312    0.000 52768.138    0.005 game.py:41(step)
                9822668   46.081    0.000 50563.660    0.005 layers.py:718(step)
                9822668  746.647    0.000 30042.077    0.003 layers.py:17(step)
              982266800 1605.622    0.000 29208.468    0.000 layer.py:98(move)
                9822668   29.715    0.000 25850.570    0.003 agent.py:29(learn)
                9822668  225.240    0.000 25799.763    0.003 agent.py:117(_learn)
                9822668  670.003    0.000 25574.523    0.003 learner.py:42(Qlearn)
                9822669 1381.223    0.000 20418.433    0.002 layers.py:684(update)
              982266800 4031.853    0.000 20036.142    0.000 layers.py:735(check)
                9822668   59.412    0.000 10527.191    0.001 grad_mode.py:23(decorate_context)
                9822668  338.334    0.000 10358.037    0.001 adam.py:55(step)
        265212036/29468004  999.026    0.000 10131.402    0.000 module.py:715(_call_impl)
               19645336   46.157    0.000 9395.943    0.000 network.py:27(forward)
               19645336  246.766    0.000 9230.020    0.000 container.py:115(forward)
                9822668 1914.877    0.000 8504.929    0.001 functional.py:53(adam)
               12404309  118.919    0.000 6289.425    0.001 layers.py:740(restart)
              982266800 1766.249    0.000 6190.205    0.000 layers.py:729(isFree)
                9822668   54.258    0.000 5734.076    0.001 tensor.py:181(backward)
                9822668   32.848    0.000 5679.817    0.001 __init__.py:68(backward)
                9822668 5419.932    0.001 5419.932    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                9822668  118.924    0.000 5265.454    0.001 agent.py:112(__call__)
               12404309   56.911    0.000 5234.736    0.000 level.py:8(__init__)
            18959784760 3514.239    0.000 5097.938    0.000 enum.py:646(__hash__)
             1893193464 1322.460    0.000 5086.867    0.000 {built-in method builtins.any}
               88404021 2660.951    0.000 4888.024    0.000 layer.py:167(NoRock_update)
               12404309  192.693    0.000 4717.847    0.000 levels.py:249(generate)
             8415832642 3441.158    0.000 4423.957    0.000 layer.py:95(isFree)
               80623520  777.872    0.000 4321.186    0.000 level.py:41(notUsed)
               39290672   70.950    0.000 3295.364    0.000 conv.py:422(forward)
             9698625910 2675.568    0.000 3271.849    0.000 layers.py:700(<genexpr>)
              982266900  530.581    0.000 3210.741    0.000 {built-in method builtins.all}
               39290672   78.307    0.000 3199.316    0.000 conv.py:414(_conv_forward)
               41595595 3141.372    0.000 3141.372    0.000 {built-in method tensor}
               39290672 3106.922    0.000 3106.922    0.000 {built-in method conv2d}
               58936008  134.086    0.000 3091.889    0.000 linear.py:92(forward)
              982266800 1876.802    0.000 2955.943    0.000 layers.py:387(check)
               58936008  220.065    0.000 2898.517    0.000 functional.py:1669(linear)
              982266800 1729.530    0.000 2820.970    0.000 layers.py:375(check)
              982266800 1705.485    0.000 2813.505    0.000 layers.py:337(check)
             5630318276 1521.781    0.000 2804.352    0.000 layers.py:690(<genexpr>)
              982266800 1701.012    0.000 2784.594    0.000 layers.py:349(check)
              687586790 1622.513    0.000 2716.891    0.000 tensor.py:933(grad)
               19645336   18.554    0.000 2504.865    0.000 game.py:37(board)
                9822668  212.700    0.000 2345.063    0.000 optimizer.py:167(zero_grad)
            22435942740 2238.022    0.000 2238.022    0.000 layer.py:91(positions)
               58936008 2038.162    0.000 2038.162    0.000 {built-in method addmm}
               80623520   60.999    0.000 2000.688    0.000 level.py:38(elementsIn)
              196453360 1698.192    0.000 1698.192    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
            18959824149 1583.705    0.000 1583.705    0.000 {built-in method builtins.hash}
              196453360 1436.001    0.000 1436.001    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              982266800  893.945    0.000 1376.483    0.000 layers.py:326(check)
              844749528  455.115    0.000 1335.395    0.000 overrides.py:1070(has_torch_function)
               78581344   70.816    0.000 1300.923    0.000 activation.py:713(forward)
               80623520  625.295    0.000 1293.418    0.000 level.py:39(<listcomp>)
              982266800  818.520    0.000 1276.440    0.000 layers.py:364(check)
               78581344  100.595    0.000 1230.107    0.000 functional.py:1292(leaky_relu)
             2666612580 1208.943    0.000 1208.943    0.000 layer.py:146(elements)
               78581344 1119.070    0.000 1119.070    0.000 {built-in method torch._C._nn.leaky_relu}
              982266800  727.924    0.000 1091.349    0.000 layers.py:23(check)
               98226680  983.251    0.000  983.251    0.000 {method 'add' of 'torch._C._TensorBase' objects}
             3802501396  933.984    0.000  933.984    0.000 level.py:32(inverse)
               98226680  920.242    0.000  920.242    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              111638781   85.773    0.000  897.799    0.000 layer.py:69(restart)
                9822668  500.362    0.000  868.226    0.000 collector.py:46(collect)
               98226680  826.167    0.000  826.167    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
             8415832642  821.427    0.000  821.427    0.000 layer.py:203(isBlocking)
             9906916522  810.185    0.000  810.185    0.000 {method 'random' of '_random.Random' objects}
        11590150110/11590150109  737.637    0.000  800.822    0.000 {built-in method builtins.len}
             1247547129  517.290    0.000  714.503    0.000 layer.py:130(add)
               98226680  698.973    0.000  698.973    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               12404409  337.339    0.000  674.944    0.000 layers.py:36(reset)
               80623520  402.558    0.000  646.271    0.000 {built-in method _functools.reduce}
             3349003411  630.233    0.000  630.233    0.000 enum.py:352(<genexpr>)
              341984370  402.674    0.000  627.597    0.000 layers.py:113(isDone)
             8728763319  596.281    0.000  596.281    0.000 layer.py:84(isDead)
              780236285  374.591    0.000  557.137    0.000 layer.py:126(remove)
               98226680  547.971    0.000  547.971    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                9822668   16.024    0.000  501.005    0.000 loss.py:445(forward)
             1748435064  390.075    0.000  485.859    0.000 overrides.py:1083(<genexpr>)
                9822668   52.046    0.000  484.981    0.000 functional.py:2637(mse_loss)
               12404309  215.515    0.000  421.604    0.000 level.py:16(<dictcomp>)
                9822668   35.206    0.000  421.554    0.000 exploration.py:47(epsilonGreedy)
              982266900  301.566    0.000  409.704    0.000 layers.py:392(isDone)
               58936008  376.777    0.000  376.777    0.000 {method 't' of 'torch._C._TensorBase' objects}
             3856998870  331.108    0.000  331.108    0.000 {method 'append' of 'list' objects}
                9822668  293.739    0.000  293.739    0.000 {method 'tolist' of 'torch._C._TensorBase' objects}
               88404021  289.836    0.000  289.836    0.000 layer.py:178(<listcomp>)
               19645336  285.591    0.000  285.591    0.000 {built-in method sum}
                9822668  283.628    0.000  283.628    0.000 {built-in method torch._C._nn.mse_loss}
               88404021  275.825    0.000  275.825    0.000 layer.py:179(<listcomp>)
               98226730  118.421    0.000  273.610    0.000 tensor.py:596(__hash__)
                9823650  254.112    0.000  254.112    0.000 {built-in method max}
             2821823200  243.713    0.000  243.713    0.000 level.py:39(<lambda>)
             3307589003  238.485    0.000  238.485    0.000 layer.py:81(isDone)
               39290672   35.544    0.000  224.419    0.000 flatten.py:39(forward)
                9822668   40.466    0.000  218.022    0.000 __init__.py:28(_make_grads)
                9822668  214.232    0.000  214.232    0.000 {built-in method gather}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9578838: <Diamonds2_simple_1> in cluster <dcc> Done

Job <Diamonds2_simple_1> was submitted from host <n-62-30-3> by user <s183905> in cluster <dcc> at Mon Apr 26 20:44:05 2021
Job was executed on host(s) <n-62-20-15>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Fri Apr 30 17:33:31 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Fri Apr 30 17:33:31 2021
Terminated at Sat May  1 17:28:37 2021
Results reported at Sat May  1 17:28:37 2021

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

    CPU time :                                   85888.36 sec.
    Max Memory :                                 2063 MB
    Average Memory :                             2062.91 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14321.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86107 sec.
    Turnaround time :                            420272 sec.

The output (if any) is above this job summary.

