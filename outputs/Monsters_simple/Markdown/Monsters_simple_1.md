
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
    Num :                       1
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      158740516022 function calls (158538899763 primitive calls) in 86112.82 seconds

##    Ordered by: cumulative time
   List reduced from 418 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86112.823 86112.823 {built-in method builtins.exec}
                      1    0.001    0.001 86112.823 86112.823 <string>:1(<module>)
                      1  133.602  133.602 86112.822 86112.822 main.py:67(simple)
                8400662   33.219    0.000 52909.640    0.006 game.py:42(step)
                8400662   40.420    0.000 51118.183    0.006 layers.py:827(step)
                8400662  671.410    0.000 26610.256    0.003 layers.py:17(step)
                8400662   26.448    0.000 26410.887    0.003 agent.py:29(learn)
                8400662  183.991    0.000 26368.376    0.003 agent.py:117(_learn)
                8400662  663.834    0.000 26184.385    0.003 learner.py:42(Qlearn)
              840066200 2107.099    0.000 25866.352    0.000 layer.py:106(move)
                8400663 1121.395    0.000 24420.579    0.003 layers.py:793(update)
              840066200 2553.048    0.000 18025.462    0.000 layers.py:844(check)
                8400662   47.480    0.000 11466.038    0.001 grad_mode.py:23(decorate_context)
                8400662  277.929    0.000 11329.614    0.001 adam.py:55(step)
              840066200 5436.938    0.000 10175.772    0.000 layers.py:538(check)
               18348023  134.636    0.000 10057.209    0.001 layers.py:849(restart)
                8400662 2069.250    0.000 9805.513    0.001 functional.py:53(adam)
        226817874/25201986  877.459    0.000 9542.986    0.000 module.py:715(_call_impl)
               16801324   38.603    0.000 8867.083    0.001 network.py:28(forward)
               16801324  224.893    0.000 8728.936    0.001 container.py:115(forward)
               18348023   66.400    0.000 8613.705    0.000 level.py:8(__init__)
               18348023 1284.050    0.000 7889.481    0.000 levels.py:428(generate)
             1619925338  885.548    0.000 6175.081    0.000 {built-in method builtins.any}
                8400662   45.797    0.000 5787.290    0.001 tensor.py:181(backward)
                8400662   27.131    0.000 5741.493    0.001 __init__.py:68(backward)
                8400662 5502.679    0.001 5502.679    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               91740115  815.242    0.000 5334.822    0.000 level.py:41(notUsed)
                8400662  101.706    0.000 4929.024    0.001 agent.py:112(__call__)
             5794751699 1530.337    0.000 4907.551    0.000 layers.py:809(<genexpr>)
               50403978 3313.307    0.000 4827.826    0.000 layer.py:159(update)
              840066200 1022.646    0.000 4208.598    0.000 layers.py:838(isFree)
            16910272404 2841.892    0.000 4098.423    0.000 enum.py:646(__hash__)
             4481881596 2524.201    0.000 3185.951    0.000 layer.py:103(isFree)
              830263029 1882.032    0.000 3059.019    0.000 layers.py:575(isDead)
               33602648   59.077    0.000 3053.378    0.000 conv.py:422(forward)
               33602648   62.723    0.000 2973.192    0.000 conv.py:414(_conv_forward)
               50403972  110.828    0.000 2970.121    0.000 linear.py:92(forward)
               33602648 2898.188    0.000 2898.188    0.000 {built-in method conv2d}
               50403972  181.788    0.000 2809.471    0.000 functional.py:1669(linear)
              840066200 1837.256    0.000 2604.164    0.000 layers.py:77(check)
              840066300  326.036    0.000 2572.363    0.000 {built-in method builtins.all}
               91740115   68.827    0.000 2490.109    0.000 level.py:38(elementsIn)
               35618537 2378.252    0.000 2378.252    0.000 {built-in method tensor}
             3454825991  895.121    0.000 2344.742    0.000 layers.py:799(<genexpr>)
              588046370 1480.905    0.000 2336.474    0.000 tensor.py:933(grad)
                8400662  207.465    0.000 2276.163    0.000 optimizer.py:167(zero_grad)
              168013240 2047.511    0.000 2047.511    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               50403972 2008.783    0.000 2008.783    0.000 {built-in method addmm}
             1221974467  359.811    0.000 1875.689    0.000 random.py:244(randint)
               16801324   17.386    0.000 1768.982    0.000 game.py:38(board)
              168013240 1754.696    0.000 1754.696    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
            18227178783 1638.417    0.000 1638.417    0.000 layer.py:99(positions)
               91740115  798.939    0.000 1599.792    0.000 level.py:39(<listcomp>)
             1221974467  622.230    0.000 1515.878    0.000 random.py:200(randrange)
             2782410161 1023.635    0.000 1384.530    0.000 layer.py:138(add)
              840066300  861.805    0.000 1305.720    0.000 layers.py:113(isDone)
               67205296   55.953    0.000 1304.219    0.000 activation.py:713(forward)
             1953437820  824.943    0.000 1293.207    0.000 layer.py:134(remove)
             3913969818 1284.302    0.000 1284.302    0.000 level.py:32(inverse)
              840066200  832.266    0.000 1273.442    0.000 layers.py:48(check)
              110088138  128.148    0.000 1272.835    0.000 layer.py:77(restart)
            16910306113 1256.536    0.000 1256.536    0.000 {built-in method builtins.hash}
               67205296   79.893    0.000 1248.267    0.000 functional.py:1292(leaky_relu)
              840066200  430.752    0.000 1225.544    0.000 layers.py:572(<listcomp>)
             1631162138  821.611    0.000 1172.370    0.000 random.py:250(_randbelow_with_getrandbits)
               67205296 1159.662    0.000 1159.662    0.000 {built-in method torch._C._nn.leaky_relu}
               84006620 1110.582    0.000 1110.582    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              722457012  362.207    0.000 1044.974    0.000 overrides.py:1070(has_torch_function)
             5617636677 1038.806    0.000 1038.806    0.000 layer.py:154(elements)
               84006620 1019.894    0.000 1019.894    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              840066200  392.942    0.000 1000.449    0.000 layers.py:573(<listcomp>)
               84006620  936.854    0.000  936.854    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               18348123  472.848    0.000  911.841    0.000 layers.py:36(reset)
                8400662  528.418    0.000  893.748    0.000 collector.py:46(collect)
              840066200  600.738    0.000  879.073    0.000 layers.py:23(check)
               84006620  840.729    0.000  840.729    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
             4733791975  824.652    0.000  824.652    0.000 enum.py:352(<genexpr>)
               91740115  505.705    0.000  821.490    0.000 {built-in method _functools.reduce}
               91740115  310.057    0.000  788.892    0.000 random.py:315(sample)
               84006620  656.938    0.000  656.938    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               18348023  294.847    0.000  620.922    0.000 level.py:16(<dictcomp>)
             8238389162  585.615    0.000  585.615    0.000 {method 'append' of 'list' objects}
             5888864062  474.664    0.000  474.664    0.000 {method 'random' of '_random.Random' objects}
        6107287967/6107287966  411.002    0.000  466.912    0.000 {built-in method builtins.len}
                8400662   10.933    0.000  459.574    0.000 loss.py:445(forward)
             4481881596  457.206    0.000  457.206    0.000 layer.py:211(isBlocking)
                8400662   42.879    0.000  448.641    0.000 functional.py:2637(mse_loss)
               50403972  401.198    0.000  401.198    0.000 {method 't' of 'torch._C._TensorBase' objects}
             1495317996  301.856    0.000  378.121    0.000 overrides.py:1083(<genexpr>)
                8400662   29.443    0.000  375.947    0.000 exploration.py:47(epsilonGreedy)
             4134225641  318.194    0.000  318.194    0.000 layer.py:92(isDead)
             3853084830  315.785    0.000  315.785    0.000 level.py:39(<lambda>)
             1953437820  306.243    0.000  306.243    0.000 {method 'remove' of 'list' objects}
               16801324  291.292    0.000  291.292    0.000 {built-in method sum}
                8400662  284.380    0.000  284.380    0.000 {built-in method torch._C._nn.mse_loss}
                8400662  261.287    0.000  261.287    0.000 {method 'tolist' of 'torch._C._TensorBase' objects}
                8401502  250.477    0.000  250.477    0.000 {built-in method max}
               33602648   22.946    0.000  226.316    0.000 flatten.py:39(forward)
             2589903676  216.943    0.000  216.943    0.000 {method 'add' of 'set' objects}
             2606677737  216.159    0.000  216.159    0.000 {method 'getrandbits' of '_random.Random' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9623998: <Monsters_simple_1> in cluster <dcc> Done

Job <Monsters_simple_1> was submitted from host <n-62-30-2> by user <s183905> in cluster <dcc> at Sat May  8 23:34:13 2021
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sat May  8 23:34:15 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat May  8 23:34:15 2021
Terminated at Sun May  9 23:29:43 2021
Results reported at Sun May  9 23:29:43 2021

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

    CPU time :                                   85896.02 sec.
    Max Memory :                                 2066 MB
    Average Memory :                             2063.03 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14318.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86224 sec.
    Turnaround time :                            86130 sec.

The output (if any) is above this job summary.

