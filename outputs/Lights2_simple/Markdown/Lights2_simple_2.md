
# Parameters

    Name :                      Lights2_simple-2
    Main :                      simple
    Level :                     Levels.Causal4
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


      173786646526 function calls (173539908395 primitive calls) in 86108.27 seconds

##    Ordered by: cumulative time
   List reduced from 419 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86108.271 86108.271 {built-in method builtins.exec}
                      1    0.001    0.001 86108.271 86108.271 <string>:1(<module>)
                      1  149.999  149.999 86108.270 86108.270 main.py:66(simple)
               10280740   33.444    0.000 53580.966    0.005 game.py:41(step)
               10280740   47.773    0.000 51216.466    0.005 layers.py:718(step)
               10280740  766.583    0.000 32978.866    0.003 layers.py:17(step)
             1028074000 2307.993    0.000 32120.403    0.000 layer.py:98(move)
               10280740   30.199    0.000 25080.278    0.002 agent.py:29(learn)
               10280740  225.933    0.000 25029.727    0.002 agent.py:117(_learn)
               10280740  643.937    0.000 24803.794    0.002 learner.py:42(Qlearn)
             1028074000 4471.219    0.000 22630.032    0.000 layers.py:735(check)
               10280741 1312.533    0.000 18130.364    0.002 layers.py:684(update)
               10280740   61.103    0.000 10209.458    0.001 grad_mode.py:23(decorate_context)
               10280740  324.426    0.000 10034.079    0.001 adam.py:55(step)
        277579980/30842220  978.259    0.000 9836.219    0.000 module.py:715(_call_impl)
               20561480   45.042    0.000 9106.947    0.000 network.py:27(forward)
               20561480  229.113    0.000 8944.347    0.000 container.py:115(forward)
               10280740 1844.689    0.000 8255.657    0.001 functional.py:53(adam)
              102807410 3389.518    0.000 5812.982    0.000 layer.py:151(update)
             1028074000 1304.831    0.000 5753.704    0.000 layers.py:729(isFree)
               10280740   53.386    0.000 5559.461    0.001 tensor.py:181(backward)
               10280740   35.385    0.000 5506.075    0.001 __init__.py:68(backward)
               10280740 5251.481    0.001 5251.481    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               10280740  117.482    0.000 5108.994    0.000 agent.py:112(__call__)
             1981761512 1321.706    0.000 5101.256    0.000 {built-in method builtins.any}
            19517763275 3337.300    0.000 4758.753    0.000 enum.py:646(__hash__)
             5988927954 3483.119    0.000 4448.873    0.000 layer.py:95(isFree)
               12702229  116.516    0.000 4135.913    0.000 layers.py:740(restart)
             1028074000 2614.071    0.000 3539.812    0.000 layers.py:77(check)
               43520064 3440.774    0.000 3440.774    0.000 {built-in method tensor}
            11169090581 2708.153    0.000 3298.681    0.000 layers.py:700(<genexpr>)
               41122960   65.373    0.000 3253.897    0.000 conv.py:422(forward)
             1028074000 1977.696    0.000 3189.223    0.000 layers.py:246(check)
               41122960   82.008    0.000 3162.942    0.000 conv.py:414(_conv_forward)
               41122960 3066.789    0.000 3066.789    0.000 {built-in method conv2d}
             1028074000 1831.345    0.000 3011.018    0.000 layers.py:286(check)
               61684440  130.234    0.000 2984.104    0.000 linear.py:92(forward)
               12702229   52.572    0.000 2928.599    0.000 level.py:8(__init__)
               20561480   19.975    0.000 2818.062    0.000 game.py:37(board)
               61684440  208.795    0.000 2794.500    0.000 functional.py:1669(linear)
              719651830 1563.156    0.000 2606.143    0.000 tensor.py:933(grad)
               12702229  388.617    0.000 2453.409    0.000 levels.py:199(generate)
               10280740  207.799    0.000 2265.836    0.000 optimizer.py:167(zero_grad)
            23451672392 2236.230    0.000 2236.230    0.000 layer.py:91(positions)
             1028074100  445.739    0.000 2204.363    0.000 {built-in method builtins.all}
               61684440 1964.137    0.000 1964.137    0.000 {built-in method addmm}
             5159871412 1243.010    0.000 1872.825    0.000 layers.py:690(<genexpr>)
             1028074000 1095.935    0.000 1710.291    0.000 layers.py:273(check)
               25404458  183.179    0.000 1690.684    0.000 level.py:41(notUsed)
              205614800 1679.445    0.000 1679.445    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
             1028074000 1220.768    0.000 1666.034    0.000 layers.py:62(check)
             1028074000 1048.071    0.000 1631.321    0.000 layers.py:313(check)
            19517804504 1421.460    0.000 1421.460    0.000 {built-in method builtins.hash}
              205614800 1390.859    0.000 1390.859    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
             1028074000  918.035    0.000 1373.111    0.000 layers.py:48(check)
             2984261656 1340.806    0.000 1340.806    0.000 layer.py:146(elements)
              884143720  426.578    0.000 1279.017    0.000 overrides.py:1070(has_torch_function)
               82245920   61.867    0.000 1242.457    0.000 activation.py:713(forward)
               82245920  107.247    0.000 1180.589    0.000 functional.py:1292(leaky_relu)
             1028074000  730.943    0.000 1080.973    0.000 layers.py:23(check)
               82245920 1062.707    0.000 1062.707    0.000 {built-in method torch._C._nn.leaky_relu}
              127022290  144.852    0.000 1050.548    0.000 layer.py:69(restart)
              102807400  952.674    0.000  952.674    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              102807400  883.016    0.000  883.016    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
            11357201427  858.365    0.000  858.365    0.000 {method 'random' of '_random.Random' objects}
               10280740  486.429    0.000  841.183    0.000 collector.py:46(collect)
        13070515674/13070515673  749.671    0.000  810.351    0.000 {built-in method builtins.len}
              102807400  793.425    0.000  793.425    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
             1391369347  509.145    0.000  696.846    0.000 layer.py:130(add)
              102807400  685.935    0.000  685.935    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              516343199  671.117    0.000  671.117    0.000 level.py:32(inverse)
               25404458   22.337    0.000  647.248    0.000 level.py:38(elementsIn)
               12702329  310.089    0.000  620.301    0.000 layers.py:36(reset)
            10153718710  590.529    0.000  590.529    0.000 layer.py:84(isDead)
              102807400  530.818    0.000  530.818    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
             4861118383  490.252    0.000  490.252    0.000 layer.py:203(isBlocking)
               10280740   17.492    0.000  488.155    0.000 loss.py:445(forward)
             1829971880  382.282    0.000  474.145    0.000 overrides.py:1083(<genexpr>)
               10280740   51.259    0.000  470.663    0.000 functional.py:2637(mse_loss)
               10280740   34.298    0.000  413.592    0.000 exploration.py:47(epsilonGreedy)
             1028074100  296.785    0.000  411.718    0.000 layers.py:52(isDone)
              588236835  274.028    0.000  409.271    0.000 layer.py:126(remove)
               25404458  198.998    0.000  391.037    0.000 level.py:39(<listcomp>)
               12702229  187.862    0.000  382.465    0.000 level.py:16(<dictcomp>)
               61684440  361.755    0.000  361.755    0.000 {method 't' of 'torch._C._TensorBase' objects}
             4334593360  318.699    0.000  318.699    0.000 {method 'append' of 'list' objects}
              102807410  314.883    0.000  314.883    0.000 layer.py:163(<listcomp>)
              102807410  294.801    0.000  294.801    0.000 layer.py:164(<listcomp>)
               10280740  289.747    0.000  289.747    0.000 {method 'tolist' of 'torch._C._TensorBase' objects}
               20561480  275.619    0.000  275.619    0.000 {built-in method sum}
               10280740  273.647    0.000  273.647    0.000 {built-in method torch._C._nn.mse_loss}
              102807450  114.207    0.000  261.905    0.000 tensor.py:596(__hash__)
             1371842335  256.458    0.000  256.458    0.000 enum.py:352(<genexpr>)
               10281768  244.984    0.000  244.984    0.000 {built-in method max}
               25404458  138.349    0.000  233.875    0.000 {built-in method _functools.reduce}
               10280740   39.523    0.000  210.950    0.000 __init__.py:28(_make_grads)
               41122960   27.347    0.000  209.674    0.000 flatten.py:39(forward)
              139003255   85.651    0.000  209.553    0.000 random.py:285(choice)
               10280740  208.713    0.000  208.713    0.000 {built-in method gather}
             3093974646  199.103    0.000  199.103    0.000 layer.py:81(isDone)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9578833: <Lights2_simple_2> in cluster <dcc> Done

Job <Lights2_simple_2> was submitted from host <n-62-30-3> by user <s183905> in cluster <dcc> at Mon Apr 26 20:44:04 2021
Job was executed on host(s) <n-62-20-3>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Wed Apr 28 12:22:05 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed Apr 28 12:22:05 2021
Terminated at Thu Apr 29 12:17:18 2021
Results reported at Thu Apr 29 12:17:18 2021

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

    CPU time :                                   85900.11 sec.
    Max Memory :                                 2065 MB
    Average Memory :                             2064.83 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14319.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86114 sec.
    Turnaround time :                            228794 sec.

The output (if any) is above this job summary.

