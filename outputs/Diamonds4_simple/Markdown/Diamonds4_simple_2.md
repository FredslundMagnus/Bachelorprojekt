Start
True
True
['main.py', '-name', 'Diamonds4_simple-2', '-hours', '24.0', '-level', 'Levels.Causal7', '-main', 'simple', '-network2', 'Networks.MiniBig']

# Parameters

    Name :                      Diamonds4_simple-2
    Main :                      simple
    Level :                     Levels.Causal7
    Failed actions chance :     0.5
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


      137374370833 function calls (137126130798 primitive calls) in 86115.24 seconds

##    Ordered by: cumulative time
   List reduced from 409 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86115.243 86115.243 {built-in method builtins.exec}
                      1    0.001    0.001 86115.243 86115.243 <string>:1(<module>)
                      1  171.243  171.243 86115.242 86115.242 main.py:71(simple)
               10343320   40.635    0.000 41374.869    0.004 game.py:41(step)
               10343320   53.118    0.000 38994.524    0.004 layers.py:718(step)
               10343320   32.989    0.000 35639.779    0.003 agent.py:29(learn)
               10343320  248.469    0.000 35584.702    0.003 agent.py:117(_learn)
               10343320  887.038    0.000 35336.233    0.003 learner.py:42(Qlearn)
               10343321 1472.736    0.000 23421.254    0.002 layers.py:684(update)
               10343320   61.149    0.000 15491.656    0.001 grad_mode.py:23(decorate_context)
               10343320  769.224    0.000 15457.926    0.001 layers.py:17(step)
               10343320  377.058    0.000 15310.411    0.001 adam.py:55(step)
             1034332000 1550.472    0.000 14590.886    0.000 layer.py:98(move)
               10343320 2767.905    0.000 13173.844    0.001 functional.py:53(adam)
        279269640/31029960 1136.555    0.000 12701.300    0.000 module.py:715(_call_impl)
               20686640   49.834    0.000 11819.974    0.001 network.py:27(forward)
               20686640  293.077    0.000 11644.263    0.001 container.py:115(forward)
               30046840  239.831    0.000 11631.047    0.000 layers.py:740(restart)
               30046840  109.000    0.000 9297.056    0.000 level.py:8(__init__)
             1034332000 2277.421    0.000 8727.156    0.000 layers.py:735(check)
               30046840  338.262    0.000 8217.595    0.000 levels.py:441(generate)
               10343320   67.326    0.000 7824.810    0.001 tensor.py:181(backward)
               10343320   38.303    0.000 7757.485    0.001 __init__.py:68(backward)
              144228735 1369.593    0.000 7515.665    0.000 level.py:41(notUsed)
               10343320 7437.747    0.001 7437.747    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               10343320  131.878    0.000 6582.324    0.001 agent.py:112(__call__)
               72403247 2476.807    0.000 4387.223    0.000 layer.py:167(NoRock_update)
             1976557421 1204.380    0.000 4356.585    0.000 {built-in method builtins.any}
               41373280   77.423    0.000 4051.484    0.000 conv.py:422(forward)
               62059920  146.206    0.000 3967.354    0.000 linear.py:92(forward)
               41373280   80.963    0.000 3946.455    0.000 conv.py:414(_conv_forward)
               41373280 3848.961    0.000 3848.961    0.000 {built-in method conv2d}
               62059920  248.429    0.000 3755.228    0.000 functional.py:1669(linear)
            13811603391 2434.035    0.000 3573.771    0.000 enum.py:646(__hash__)
              144228735  104.261    0.000 3510.533    0.000 level.py:38(elementsIn)
              724032430 2122.717    0.000 3306.942    0.000 tensor.py:933(grad)
             1034332000  843.002    0.000 3305.178    0.000 layers.py:729(isFree)
               43784969 3202.291    0.000 3202.291    0.000 {built-in method tensor}
               10343320  300.930    0.000 3195.421    0.000 optimizer.py:167(zero_grad)
              206866400 2783.227    0.000 2783.227    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               62059920 2686.185    0.000 2686.185    0.000 {built-in method addmm}
             8034282080 2131.803    0.000 2620.999    0.000 layers.py:700(<genexpr>)
             3218371654 1951.618    0.000 2462.176    0.000 layer.py:95(isFree)
               20686640   22.920    0.000 2390.246    0.000 game.py:37(board)
              206866400 2380.773    0.000 2380.773    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              144228735 1102.951    0.000 2266.520    0.000 level.py:39(<listcomp>)
             1034332100  359.743    0.000 2040.138    0.000 {built-in method builtins.all}
              210327880  161.471    0.000 2019.166    0.000 layer.py:69(restart)
             3691535148  988.161    0.000 1814.192    0.000 layers.py:690(<genexpr>)
               82746560   70.273    0.000 1776.961    0.000 activation.py:713(forward)
               82746560  120.630    0.000 1706.688    0.000 functional.py:1292(leaky_relu)
               30046940  817.341    0.000 1632.798    0.000 layers.py:36(reset)
               82746560 1574.712    0.000 1574.712    0.000 {built-in method torch._C._nn.leaky_relu}
             6924769906 1556.146    0.000 1556.146    0.000 level.py:32(inverse)
              517165490  931.071    0.000 1512.450    0.000 layers.py:617(check)
              517186392  921.356    0.000 1495.810    0.000 layers.py:602(check)
              517170476  912.123    0.000 1485.046    0.000 layers.py:632(check)
              103433200 1469.352    0.000 1469.352    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              889525600  495.613    0.000 1443.444    0.000 overrides.py:1070(has_torch_function)
              103433200 1352.953    0.000 1352.953    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              103433200 1249.172    0.000 1249.172    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               10343320  710.460    0.000 1195.711    0.000 collector.py:46(collect)
             6273922195 1173.473    0.000 1173.473    0.000 enum.py:352(<genexpr>)
              144228735  711.435    0.000 1139.753    0.000 {built-in method _functools.reduce}
            13811644860 1139.744    0.000 1139.744    0.000 {built-in method builtins.hash}
              103433200 1133.909    0.000 1133.909    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
            10928383725 1088.074    0.000 1088.074    0.000 layer.py:91(positions)
             3079480670 1072.164    0.000 1072.164    0.000 layer.py:146(elements)
              103433200  899.480    0.000  899.480    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               30046840  419.563    0.000  897.591    0.000 level.py:16(<dictcomp>)
             1469737424  583.985    0.000  801.259    0.000 layer.py:130(add)
              517174158  464.245    0.000  715.058    0.000 layers.py:588(check)
        9153134162/9153134161  605.693    0.000  680.701    0.000 {built-in method builtins.len}
             8405288117  666.405    0.000  666.405    0.000 {method 'random' of '_random.Random' objects}
               10343320   14.256    0.000  609.179    0.000 loss.py:445(forward)
               10343320   57.833    0.000  594.923    0.000 functional.py:2637(mse_loss)
              517155954  397.060    0.000  584.021    0.000 layers.py:23(check)
               62059920  527.105    0.000  527.105    0.000 {method 't' of 'torch._C._TensorBase' objects}
             1841111120  419.143    0.000  524.409    0.000 overrides.py:1083(<genexpr>)
               10343320   37.981    0.000  493.673    0.000 exploration.py:47(epsilonGreedy)
             7029996820  489.196    0.000  489.196    0.000 layer.py:84(isDead)
             5048005725  428.318    0.000  428.318    0.000 level.py:39(<lambda>)
             1034332100  309.472    0.000  421.047    0.000 layers.py:592(isDone)
             3218371654  384.956    0.000  384.956    0.000 layer.py:203(isBlocking)
               20686640  384.850    0.000  384.850    0.000 {built-in method sum}
               10343320  376.590    0.000  376.590    0.000 {built-in method torch._C._nn.mse_loss}
               10343320  347.490    0.000  347.490    0.000 {method 'tolist' of 'torch._C._TensorBase' objects}
               10344354  335.578    0.000  335.578    0.000 {built-in method max}
             3979511992  323.493    0.000  323.493    0.000 {method 'append' of 'list' objects}
             2463849654  313.879    0.000  313.879    0.000 layer.py:182(grid)
               41373280   32.829    0.000  303.345    0.000 flatten.py:39(forward)
              103433250  133.750    0.000  298.115    0.000 tensor.py:596(__hash__)
               10343320  279.345    0.000  279.345    0.000 {built-in method gather}
              368205755  185.207    0.000  275.384    0.000 layer.py:126(remove)
               10343320   45.387    0.000  272.532    0.000 __init__.py:28(_make_grads)
               41373280  270.516    0.000  270.516    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              279269640  258.363    0.000  258.363    0.000 {built-in method torch._C._get_tracing_state}
               10343320   51.171    0.000  256.670    0.000 tensor.py:506(__rsub__)
               72403247  241.306    0.000  241.306    0.000 layer.py:178(<listcomp>)
              144228735   83.794    0.000  238.107    0.000 random.py:285(choice)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9578845: <Diamonds4_simple_2> in cluster <dcc> Done

Job <Diamonds4_simple_2> was submitted from host <n-62-30-3> by user <s183905> in cluster <dcc> at Mon Apr 26 20:44:06 2021
Job was executed on host(s) <n-62-20-15>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sun May  2 03:51:16 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun May  2 03:51:16 2021
Terminated at Mon May  3 03:46:38 2021
Results reported at Mon May  3 03:46:38 2021

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

    CPU time :                                   85897.11 sec.
    Max Memory :                                 2062 MB
    Average Memory :                             2059.53 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14322.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86122 sec.
    Turnaround time :                            543752 sec.

The output (if any) is above this job summary.

