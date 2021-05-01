
# Parameters

    Name :                      Diamonds1_simple-1
    Main :                      simple
    Level :                     Levels.Causal2
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


      185482311632 function calls (185254058245 primitive calls) in 86102.96 seconds

##    Ordered by: cumulative time
   List reduced from 406 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86102.960 86102.960 {built-in method builtins.exec}
                      1    0.001    0.001 86102.960 86102.960 <string>:1(<module>)
                      1  151.836  151.836 86102.959 86102.959 main.py:66(simple)
                9510543   31.475    0.000 54834.673    0.006 game.py:41(step)
                9510543   44.546    0.000 52827.887    0.006 layers.py:718(step)
                9510544 1359.788    0.000 29734.866    0.003 layers.py:684(update)
                9510543   27.107    0.000 24361.339    0.003 agent.py:29(learn)
                9510543  213.176    0.000 24313.232    0.003 agent.py:117(_learn)
                9510543  631.300    0.000 24100.056    0.003 learner.py:42(Qlearn)
                9510543  726.284    0.000 22989.842    0.002 layers.py:17(step)
              951054300 1533.370    0.000 22180.074    0.000 layer.py:98(move)
               47057842  362.105    0.000 17688.844    0.000 layers.py:740(restart)
               47057842  167.109    0.000 14147.771    0.000 level.py:8(__init__)
              951054300 2984.538    0.000 13766.466    0.000 layers.py:735(check)
               47057842  511.702    0.000 12486.046    0.000 levels.py:151(generate)
              225878534 2093.294    0.000 11441.141    0.000 level.py:41(notUsed)
                9510543   57.265    0.000 9889.341    0.001 grad_mode.py:23(decorate_context)
                9510543  327.840    0.000 9727.128    0.001 adam.py:55(step)
        256784661/28531629  963.243    0.000 9471.939    0.000 module.py:715(_call_impl)
               19021086   41.066    0.000 8751.659    0.000 network.py:27(forward)
               19021086  220.189    0.000 8597.349    0.000 container.py:115(forward)
                9510543 1788.286    0.000 7984.180    0.001 functional.py:53(adam)
                9510543   53.157    0.000 5432.355    0.001 tensor.py:181(backward)
              951054300 1410.341    0.000 5424.218    0.000 layers.py:729(isFree)
              225878534  159.521    0.000 5388.025    0.000 level.py:38(elementsIn)
                9510543   32.235    0.000 5379.198    0.001 __init__.py:68(backward)
            22211105825 3703.539    0.000 5371.137    0.000 enum.py:646(__hash__)
                9510543 5128.365    0.001 5128.365    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                9510543  112.649    0.000 4935.413    0.001 agent.py:112(__call__)
               66573808 2889.691    0.000 4844.195    0.000 layer.py:167(NoRock_update)
             6499442490 3197.886    0.000 4013.877    0.000 layer.py:95(isFree)
             1797987681 1073.332    0.000 3930.285    0.000 {built-in method builtins.any}
              225878534 1730.287    0.000 3496.748    0.000 level.py:39(<listcomp>)
               38042172   65.995    0.000 3069.755    0.000 conv.py:422(forward)
              329404894  251.653    0.000 3067.328    0.000 layer.py:69(restart)
               38042172   76.501    0.000 2978.100    0.000 conv.py:414(_conv_forward)
               57063258  125.308    0.000 2893.778    0.000 linear.py:92(forward)
               38042172 2888.321    0.000 2888.321    0.000 {built-in method conv2d}
               40283770 2751.487    0.000 2751.487    0.000 {built-in method tensor}
               57063258  208.804    0.000 2711.464    0.000 functional.py:1669(linear)
              951054300 1677.429    0.000 2710.531    0.000 layers.py:219(check)
              951054300 1603.379    0.000 2606.814    0.000 layers.py:207(check)
              951054300 1582.562    0.000 2562.989    0.000 layers.py:231(check)
              665738040 1540.875    0.000 2537.691    0.000 tensor.py:933(grad)
               47057942 1208.313    0.000 2410.240    0.000 layers.py:36(reset)
             7231972464 1956.162    0.000 2402.911    0.000 layers.py:700(<genexpr>)
            10844995557 2354.569    0.000 2354.569    0.000 level.py:32(inverse)
              951054400  226.368    0.000 2307.501    0.000 {built-in method builtins.all}
             2245238586  523.416    0.000 2197.878    0.000 layers.py:690(<genexpr>)
                9510543  203.552    0.000 2194.000    0.000 optimizer.py:167(zero_grad)
               19021086   16.938    0.000 2132.982    0.000 game.py:37(board)
               57063258 1905.352    0.000 1905.352    0.000 {built-in method addmm}
            18085502220 1767.088    0.000 1767.088    0.000 layer.py:91(positions)
             9825711031 1754.660    0.000 1754.660    0.000 enum.py:352(<genexpr>)
              225878534 1085.448    0.000 1731.757    0.000 {built-in method _functools.reduce}
            22211143974 1667.606    0.000 1667.606    0.000 {built-in method builtins.hash}
              951054400 1066.504    0.000 1620.921    0.000 layers.py:113(isDone)
              190210860 1592.535    0.000 1592.535    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
             2651199456 1011.708    0.000 1400.363    0.000 layer.py:130(add)
               47057842  652.083    0.000 1387.356    0.000 level.py:16(<dictcomp>)
              190210860 1358.913    0.000 1358.913    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
             5388799255 1227.952    0.000 1227.952    0.000 layer.py:146(elements)
              817906778  408.863    0.000 1222.527    0.000 overrides.py:1070(has_torch_function)
              951054300  778.293    0.000 1209.730    0.000 layers.py:196(check)
               76084344   59.965    0.000 1195.711    0.000 activation.py:713(forward)
               76084344  102.726    0.000 1135.746    0.000 functional.py:1292(leaky_relu)
               76084344 1023.047    0.000 1023.047    0.000 {built-in method torch._C._nn.leaky_relu}
              951054300  682.897    0.000 1005.619    0.000 layers.py:23(check)
               95105430  919.900    0.000  919.900    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               95105430  863.676    0.000  863.676    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                9510543  464.367    0.000  809.059    0.000 collector.py:46(collect)
               95105430  770.470    0.000  770.470    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
             1003585632  463.141    0.000  696.733    0.000 layer.py:126(remove)
               95105430  664.482    0.000  664.482    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
        9237699061/9237699060  599.966    0.000  659.373    0.000 {built-in method builtins.len}
             6499442490  654.337    0.000  654.337    0.000 layer.py:203(isBlocking)
             7905748690  646.308    0.000  646.308    0.000 level.py:39(<lambda>)
             7806176311  629.693    0.000  629.693    0.000 {method 'random' of '_random.Random' objects}
             7016986632  555.413    0.000  555.413    0.000 {method 'append' of 'list' objects}
               95105430  508.010    0.000  508.010    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                9510543   13.423    0.000  489.512    0.000 loss.py:445(forward)
                9510543   53.896    0.000  476.088    0.000 functional.py:2637(mse_loss)
             3858751818  469.984    0.000  469.984    0.000 layer.py:182(grid)
             1692876814  357.795    0.000  447.449    0.000 overrides.py:1083(<genexpr>)
             6327975906  446.749    0.000  446.749    0.000 layer.py:84(isDead)
                9510543   37.855    0.000  446.118    0.000 exploration.py:47(epsilonGreedy)
               57063258  348.134    0.000  348.134    0.000 {method 't' of 'torch._C._TensorBase' objects}
              225878534  122.017    0.000  348.018    0.000 random.py:285(choice)
                9510543  292.340    0.000  292.340    0.000 {method 'tolist' of 'torch._C._TensorBase' objects}
                9510543  278.667    0.000  278.667    0.000 {built-in method torch._C._nn.mse_loss}
               19021086  266.178    0.000  266.178    0.000 {built-in method sum}
               95105480  112.983    0.000  255.342    0.000 tensor.py:596(__hash__)
              329404894  249.364    0.000  249.364    0.000 layer.py:139(clear2)
                9511494  243.558    0.000  243.558    0.000 {built-in method max}
               66573808  214.932    0.000  214.932    0.000 layer.py:178(<listcomp>)
                9510543   40.886    0.000  210.019    0.000 __init__.py:28(_make_grads)
                9510543  206.141    0.000  206.141    0.000 {built-in method gather}
               38042172   30.647    0.000  205.698    0.000 flatten.py:39(forward)
              225878534  140.152    0.000  203.347    0.000 random.py:250(_randbelow_with_getrandbits)
               66573808  201.449    0.000  201.449    0.000 layer.py:179(<listcomp>)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9578835: <Diamonds1_simple_1> in cluster <dcc> Done

Job <Diamonds1_simple_1> was submitted from host <n-62-30-3> by user <s183905> in cluster <dcc> at Mon Apr 26 20:44:04 2021
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Thu Apr 29 14:28:59 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Apr 29 14:28:59 2021
Terminated at Fri Apr 30 14:24:06 2021
Results reported at Fri Apr 30 14:24:06 2021

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

    CPU time :                                   85898.66 sec.
    Max Memory :                                 2062 MB
    Average Memory :                             2061.85 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14322.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86108 sec.
    Turnaround time :                            322802 sec.

The output (if any) is above this job summary.

