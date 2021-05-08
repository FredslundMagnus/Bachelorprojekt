
# Parameters

    Name :                      Monsters_simple-1
    Main :                      simple
    Level :                     Levels.MonsterLevel
    Failed actions chance :     0
    Use model :                 True
    Depth :                     3
    Model explore :             1000000
    Samples :                   5
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
    Layer super1 :              True
    Layer super2 :              True
    Layer super3 :              True
    Layer super4 :              True
    Layer super5 :              True
    Layer super6 :              True
    Layer super7 :              True
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


      157056880918 function calls (156852475595 primitive calls) in 86122.27 seconds

##    Ordered by: cumulative time
   List reduced from 417 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86122.274 86122.274 {built-in method builtins.exec}
                      1    0.002    0.002 86122.273 86122.273 <string>:1(<module>)
                      1  132.829  132.829 86122.272 86122.272 main.py:67(simple)
                8516873   29.574    0.000 52552.980    0.006 game.py:42(step)
                8516873   39.110    0.000 50713.625    0.006 layers.py:827(step)
                8516873  685.038    0.000 27031.908    0.003 layers.py:17(step)
                8516873   25.557    0.000 26702.338    0.003 agent.py:29(learn)
                8516873  184.901    0.000 26659.181    0.003 agent.py:117(_learn)
                8516873  664.262    0.000 26474.279    0.003 learner.py:42(Qlearn)
              851687300 2129.894    0.000 26267.308    0.000 layer.py:106(move)
                8516874 1179.192    0.000 23594.602    0.003 layers.py:793(update)
              851687300 2564.695    0.000 18375.164    0.000 layers.py:844(check)
                8516873   50.119    0.000 11560.276    0.001 grad_mode.py:23(decorate_context)
                8516873  282.363    0.000 11420.252    0.001 adam.py:55(step)
              851687300 5544.185    0.000 10415.160    0.000 layers.py:538(check)
               18109513  139.366    0.000 9879.851    0.001 layers.py:849(restart)
                8516873 2057.859    0.000 9819.759    0.001 functional.py:53(adam)
        229955571/25550619  869.180    0.000 9586.256    0.000 module.py:715(_call_impl)
               17033746   39.138    0.000 8919.753    0.001 network.py:28(forward)
               17033746  222.264    0.000 8782.613    0.001 container.py:115(forward)
               18109513   68.009    0.000 8499.926    0.000 level.py:8(__init__)
               18109513 1276.505    0.000 7783.255    0.000 levels.py:428(generate)
             1642710348  877.192    0.000 6163.025    0.000 {built-in method builtins.any}
                8516873   47.687    0.000 5851.873    0.001 tensor.py:181(backward)
                8516873   27.797    0.000 5804.186    0.001 __init__.py:68(backward)
                8516873 5562.935    0.001 5562.935    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               90547565  803.560    0.000 5259.987    0.000 level.py:41(notUsed)
               51101244 3416.725    0.000 4968.200    0.000 layer.py:159(update)
                8516873  102.364    0.000 4962.162    0.001 agent.py:112(__call__)
             5886323117 1536.152    0.000 4897.269    0.000 layers.py:809(<genexpr>)
              851687300  971.448    0.000 4224.120    0.000 layers.py:838(isFree)
            16966877692 2780.148    0.000 4057.703    0.000 enum.py:646(__hash__)
             4549824948 2552.772    0.000 3252.672    0.000 layer.py:103(isFree)
               34067492   58.658    0.000 3073.339    0.000 conv.py:422(forward)
              842124205 1884.008    0.000 3051.117    0.000 layers.py:575(isDead)
               34067492   68.754    0.000 2994.292    0.000 conv.py:414(_conv_forward)
               51101238  115.599    0.000 2991.463    0.000 linear.py:92(forward)
               34067492 2914.156    0.000 2914.156    0.000 {built-in method conv2d}
               51101238  185.620    0.000 2829.000    0.000 functional.py:1669(linear)
              851687300 1846.380    0.000 2637.033    0.000 layers.py:77(check)
              596181140 1601.883    0.000 2479.778    0.000 tensor.py:933(grad)
               90547565   67.207    0.000 2476.800    0.000 level.py:38(elementsIn)
               36106738 2451.979    0.000 2451.979    0.000 {built-in method tensor}
                8516873  221.647    0.000 2394.929    0.000 optimizer.py:167(zero_grad)
              170337460 2063.132    0.000 2063.132    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               51101238 2029.817    0.000 2029.817    0.000 {built-in method addmm}
             1239646647  390.782    0.000 1958.877    0.000 random.py:244(randint)
               17033746   18.553    0.000 1833.418    0.000 game.py:38(board)
              170337460 1763.152    0.000 1763.152    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              851687400  179.122    0.000 1744.671    0.000 {built-in method builtins.all}
            18348243533 1698.651    0.000 1698.651    0.000 layer.py:99(positions)
             1807882001  387.230    0.000 1666.321    0.000 layers.py:799(<genexpr>)
               90547565  808.050    0.000 1595.412    0.000 level.py:39(<listcomp>)
             1239646647  663.571    0.000 1568.095    0.000 random.py:200(randrange)
             2796256023 1030.676    0.000 1386.621    0.000 layer.py:138(add)
             1977590286  855.407    0.000 1318.021    0.000 layer.py:134(remove)
               68134984   53.894    0.000 1313.170    0.000 activation.py:713(forward)
            16966911841 1277.560    0.000 1277.560    0.000 {built-in method builtins.hash}
             3863156013 1265.779    0.000 1265.779    0.000 level.py:32(inverse)
              851687300  817.055    0.000 1263.634    0.000 layers.py:48(check)
              851687300  446.067    0.000 1261.669    0.000 layers.py:572(<listcomp>)
               68134984   86.493    0.000 1259.276    0.000 functional.py:1292(leaky_relu)
              851687400  840.909    0.000 1258.264    0.000 layers.py:113(isDone)
              108657078  119.362    0.000 1205.166    0.000 layer.py:77(restart)
             1643517432  831.241    0.000 1178.225    0.000 random.py:250(_randbelow_with_getrandbits)
               68134984 1164.418    0.000 1164.418    0.000 {built-in method torch._C._nn.leaky_relu}
               85168730 1102.839    0.000 1102.839    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              732451158  368.529    0.000 1068.568    0.000 overrides.py:1070(has_torch_function)
             5647391806 1048.447    0.000 1048.447    0.000 layer.py:154(elements)
              851687300  394.258    0.000 1015.170    0.000 layers.py:573(<listcomp>)
               85168730 1008.609    0.000 1008.609    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              851687300  639.269    0.000  950.390    0.000 layers.py:23(check)
               85168730  940.331    0.000  940.331    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                8516873  531.911    0.000  898.958    0.000 collector.py:46(collect)
               85168730  856.304    0.000  856.304    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               18109613  424.392    0.000  850.894    0.000 layers.py:36(reset)
               90547565  502.809    0.000  814.182    0.000 {built-in method _functools.reduce}
             4672256395  788.431    0.000  788.431    0.000 enum.py:352(<genexpr>)
               90547565  307.049    0.000  776.432    0.000 random.py:315(sample)
               85168730  675.358    0.000  675.358    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               18109513  292.284    0.000  608.790    0.000 level.py:16(<dictcomp>)
             8292348674  579.692    0.000  579.692    0.000 {method 'append' of 'list' objects}
        6756271323/6756271322  453.134    0.000  509.212    0.000 {built-in method builtins.len}
             4549824948  484.460    0.000  484.460    0.000 layer.py:211(isBlocking)
             5970327973  469.594    0.000  469.594    0.000 {method 'random' of '_random.Random' objects}
                8516873   10.699    0.000  459.603    0.000 loss.py:445(forward)
                8516873   42.842    0.000  448.904    0.000 functional.py:2637(mse_loss)
               51101238  395.583    0.000  395.583    0.000 {method 't' of 'torch._C._TensorBase' objects}
             1516003554  304.921    0.000  384.264    0.000 overrides.py:1083(<genexpr>)
                8516873   29.740    0.000  383.288    0.000 exploration.py:47(epsilonGreedy)
             3802997730  311.373    0.000  311.373    0.000 level.py:39(<lambda>)
             4202074707  310.000    0.000  310.000    0.000 layer.py:92(isDead)
             1977590286  303.433    0.000  303.433    0.000 {method 'remove' of 'list' objects}
               17033746  291.201    0.000  291.201    0.000 {built-in method sum}
                8516873  282.291    0.000  282.291    0.000 {built-in method torch._C._nn.mse_loss}
                8516873  267.103    0.000  267.103    0.000 {method 'tolist' of 'torch._C._TensorBase' objects}
                8517724  253.367    0.000  253.367    0.000 {built-in method max}
               34067492   24.424    0.000  226.727    0.000 flatten.py:39(forward)
               85168780  101.184    0.000  222.435    0.000 tensor.py:596(__hash__)
             2626512099  213.722    0.000  213.722    0.000 {method 'getrandbits' of '_random.Random' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9578862: <Monsters_simple_1> in cluster <dcc> Done

Job <Monsters_simple_1> was submitted from host <n-62-30-3> by user <s183905> in cluster <dcc> at Mon Apr 26 20:44:08 2021
Job was executed on host(s) <n-62-20-2>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Fri May  7 12:43:21 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Fri May  7 12:43:21 2021
Terminated at Sat May  8 12:38:57 2021
Results reported at Sat May  8 12:38:57 2021

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

    CPU time :                                   85897.99 sec.
    Max Memory :                                 2065 MB
    Average Memory :                             2061.97 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14319.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86188 sec.
    Turnaround time :                            1007689 sec.

The output (if any) is above this job summary.

