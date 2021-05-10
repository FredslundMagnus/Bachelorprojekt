
# Parameters

    Name :                      DoorsAndKey_simple-0
    Main :                      simple
    Level :                     Levels.Causal1
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
    Num :                       0
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      176911172708 function calls (176672335441 primitive calls) in 86110.38 seconds

##    Ordered by: cumulative time
   List reduced from 409 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86110.377 86110.377 {built-in method builtins.exec}
                      1    0.001    0.001 86110.377 86110.377 <string>:1(<module>)
                      1  152.883  152.883 86110.376 86110.376 main.py:67(simple)
                9951538   32.647    0.000 53270.922    0.005 game.py:42(step)
                9951538   49.669    0.000 51349.994    0.005 layers.py:827(step)
                9951539 1447.586    0.000 32519.214    0.003 layers.py:793(update)
                9951538   29.436    0.000 25754.370    0.003 agent.py:29(learn)
                9951538  220.245    0.000 25703.566    0.003 agent.py:117(_learn)
                9951538  653.922    0.000 25483.320    0.003 learner.py:42(Qlearn)
               55245520  402.962    0.000 20290.103    0.000 layers.py:849(restart)
                9951538  790.075    0.000 18721.749    0.002 layers.py:17(step)
              995153800 1645.094    0.000 17845.112    0.000 layer.py:106(move)
               55245520  199.338    0.000 16059.544    0.000 level.py:8(__init__)
               55245520  623.061    0.000 13792.126    0.000 levels.py:122(generate)
              215456605 2071.112    0.000 12606.805    0.000 level.py:41(notUsed)
                9951538   59.168    0.000 10567.671    0.001 grad_mode.py:23(decorate_context)
                9951538  351.732    0.000 10399.997    0.001 adam.py:55(step)
        268691526/29854614 1009.350    0.000 9912.371    0.000 module.py:715(_call_impl)
               19903076   47.928    0.000 9190.988    0.000 network.py:28(forward)
              995153800 2712.704    0.000 9071.445    0.000 layers.py:844(check)
               19903076  240.626    0.000 9023.931    0.000 container.py:115(forward)
                9951538 1917.994    0.000 8588.084    0.001 functional.py:53(adam)
              215456605  165.300    0.000 6116.481    0.000 level.py:38(elementsIn)
                9951538   60.441    0.000 5747.448    0.001 tensor.py:181(backward)
                9951538   33.798    0.000 5687.008    0.001 __init__.py:68(backward)
              995153800 1314.090    0.000 5493.644    0.000 layers.py:838(isFree)
                9951538 5435.730    0.001 5435.730    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                9951538  115.278    0.000 5132.494    0.001 agent.py:112(__call__)
               59709234 2959.982    0.000 4838.209    0.000 layer.py:175(NoRock_update)
            18039927898 3110.581    0.000 4529.049    0.000 enum.py:646(__hash__)
             5864342920 3249.618    0.000 4179.553    0.000 layer.py:103(isFree)
              215456605 1977.822    0.000 3985.503    0.000 level.py:39(<listcomp>)
              331473120  313.368    0.000 3706.397    0.000 layer.py:77(restart)
             1875353033 1038.311    0.000 3648.729    0.000 {built-in method builtins.any}
               39806152   66.660    0.000 3233.799    0.000 conv.py:422(forward)
               39806152   76.523    0.000 3141.190    0.000 conv.py:414(_conv_forward)
               39806152 3050.316    0.000 3050.316    0.000 {built-in method conv2d}
               59709228  134.655    0.000 3010.638    0.000 linear.py:92(forward)
               55245620 1422.688    0.000 2875.006    0.000 layers.py:36(reset)
               59709228  215.637    0.000 2815.953    0.000 functional.py:1669(linear)
              995153900  445.581    0.000 2716.392    0.000 {built-in method builtins.all}
              696607690 1594.358    0.000 2637.102    0.000 tensor.py:933(grad)
               42135722 2590.457    0.000 2590.457    0.000 {built-in method tensor}
             9938409857 2577.190    0.000 2577.190    0.000 level.py:32(inverse)
             4223372254 1129.099    0.000 2387.673    0.000 layers.py:799(<genexpr>)
                9951538  232.851    0.000 2336.496    0.000 optimizer.py:167(zero_grad)
            11640193416 2141.089    0.000 2141.089    0.000 enum.py:352(<genexpr>)
             6579358660 1753.111    0.000 2139.147    0.000 layers.py:809(<genexpr>)
               19903076   19.503    0.000 1986.669    0.000 game.py:38(board)
               59709228 1978.888    0.000 1978.888    0.000 {built-in method addmm}
              215456605 1224.119    0.000 1965.678    0.000 {built-in method _functools.reduce}
               55245520  887.184    0.000 1947.814    0.000 level.py:16(<dictcomp>)
              995153800 1095.091    0.000 1752.827    0.000 layers.py:141(check)
              199030760 1716.287    0.000 1716.287    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
             3117598529 1259.813    0.000 1711.683    0.000 layer.py:138(add)
              995153800  961.528    0.000 1478.355    0.000 layers.py:124(check)
              199030760 1440.826    0.000 1440.826    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
            18039967807 1418.474    0.000 1418.474    0.000 {built-in method builtins.hash}
              995153800  900.573    0.000 1396.567    0.000 layers.py:48(check)
              855832348  424.000    0.000 1274.377    0.000 overrides.py:1070(has_torch_function)
               79612304   68.863    0.000 1259.661    0.000 activation.py:713(forward)
             6299995634 1240.610    0.000 1240.610    0.000 layer.py:154(elements)
               79612304  102.193    0.000 1190.798    0.000 functional.py:1292(leaky_relu)
            12443064070 1170.633    0.000 1170.633    0.000 layer.py:99(positions)
              995153800  733.467    0.000 1085.397    0.000 layers.py:23(check)
               79612304 1078.195    0.000 1078.195    0.000 {built-in method torch._C._nn.leaky_relu}
               99515380 1052.480    0.000 1052.480    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               99515380  914.665    0.000  914.665    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                9951538  497.875    0.000  861.758    0.000 collector.py:46(collect)
               99515380  813.340    0.000  813.340    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
             1047943511  512.530    0.000  755.870    0.000 layer.py:134(remove)
             9049177410  741.559    0.000  741.559    0.000 level.py:39(<lambda>)
              395055475  468.765    0.000  712.352    0.000 layers.py:113(isDone)
               99515380  706.705    0.000  706.705    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
             8185362406  640.862    0.000  640.862    0.000 {method 'append' of 'list' objects}
        8546940058/8546940057  569.238    0.000  631.962    0.000 {built-in method builtins.len}
             7275929635  583.151    0.000  583.151    0.000 {method 'random' of '_random.Random' objects}
             4895731608  574.041    0.000  574.041    0.000 layer.py:211(isBlocking)
             4530141332  572.678    0.000  572.678    0.000 layer.py:190(grid)
               99515380  555.798    0.000  555.798    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                9951538   14.569    0.000  482.004    0.000 loss.py:445(forward)
                9951538   50.766    0.000  467.435    0.000 functional.py:2637(mse_loss)
             1771373924  374.852    0.000  464.899    0.000 overrides.py:1083(<genexpr>)
                9951538   34.941    0.000  409.780    0.000 exploration.py:47(epsilonGreedy)
              995153900  302.598    0.000  408.399    0.000 layers.py:52(isDone)
             5639450280  386.036    0.000  386.036    0.000 layer.py:92(isDead)
               59709228  360.501    0.000  360.501    0.000 {method 't' of 'torch._C._TensorBase' objects}
              215456605  121.899    0.000  346.402    0.000 random.py:285(choice)
                9951538  284.649    0.000  284.649    0.000 {method 'tolist' of 'torch._C._TensorBase' objects}
               19903076  282.044    0.000  282.044    0.000 {built-in method sum}
                9951538  275.450    0.000  275.450    0.000 {built-in method torch._C._nn.mse_loss}
              331473120  263.623    0.000  263.623    0.000 layer.py:147(clear2)
               99515430  115.884    0.000  263.303    0.000 tensor.py:596(__hash__)
                9952533  246.830    0.000  246.830    0.000 {built-in method max}
               39806152   28.233    0.000  216.676    0.000 flatten.py:39(forward)
                9951538   37.934    0.000  209.466    0.000 __init__.py:28(_make_grads)
                9951538  207.364    0.000  207.364    0.000 {built-in method gather}
              215456605  143.500    0.000  202.682    0.000 random.py:250(_randbelow_with_getrandbits)
                9951538   44.509    0.000  191.557    0.000 tensor.py:506(__rsub__)
               59709234  189.942    0.000  189.942    0.000 layer.py:186(<listcomp>)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9624000: <DoorsAndKey_simple_0> in cluster <dcc> Done

Job <DoorsAndKey_simple_0> was submitted from host <n-62-30-2> by user <s183905> in cluster <dcc> at Sat May  8 23:34:13 2021
Job was executed on host(s) <n-62-11-13>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sat May  8 23:34:15 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat May  8 23:34:15 2021
Terminated at Sun May  9 23:29:41 2021
Results reported at Sun May  9 23:29:41 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
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

python main.py $MYARGS


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   86032.62 sec.
    Max Memory :                                 2061 MB
    Average Memory :                             2057.65 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14323.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86237 sec.
    Turnaround time :                            86128 sec.

The output (if any) is above this job summary.

