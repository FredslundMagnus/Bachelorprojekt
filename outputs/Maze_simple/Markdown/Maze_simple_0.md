
# Parameters

    Name :                      Maze_simple-0
    Main :                      simple
    Level :                     Levels.Maze
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


      143801651473 function calls (143572216958 primitive calls) in 85906.15 seconds

##    Ordered by: cumulative time
   List reduced from 424 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86114.184 86114.184 {built-in method builtins.exec}
                      1    0.001    0.001 86114.184 86114.184 <string>:1(<module>)
                      1  151.968  151.968 86114.183 86114.183 main.py:67(simple)
                9559756   35.381    0.000 46254.789    0.005 game.py:42(step)
                9559756   47.792    0.000 44000.742    0.005 layers.py:827(step)
                9559756   31.032    0.000 31621.009    0.003 agent.py:29(learn)
                9559756  220.823    0.000 31568.330    0.003 agent.py:117(_learn)
                9559756  789.860    0.000 31347.507    0.003 learner.py:42(Qlearn)
                9559757 1329.062    0.000 22784.512    0.002 layers.py:793(update)
                9559756  737.007    0.000 21114.483    0.002 layers.py:17(step)
              955975600 1464.903    0.000 20294.814    0.000 layer.py:106(move)
                9559756   54.796    0.000 13710.023    0.001 grad_mode.py:23(decorate_context)
              955975600 3297.995    0.000 13637.796    0.000 layers.py:844(check)
                9559756  342.661    0.000 13547.016    0.001 adam.py:55(step)
                9559756 2458.299    0.000 11661.982    0.001 functional.py:53(adam)
        258113412/28679268 1024.540    0.000 11383.096    0.000 module.py:715(_call_impl)
               19119512   47.224    0.000 10587.294    0.001 network.py:28(forward)
               14161015  151.497    0.000 10534.245    0.001 layers.py:849(restart)
               19119512  267.166    0.000 10425.229    0.001 container.py:115(forward)
               14161015   98.756    0.000 9189.751    0.001 level.py:8(__init__)
               19310614 1122.532    0.000 8360.442    0.000 levels.py:9(generate)
                9559756   56.221    0.000 6897.722    0.001 tensor.py:181(backward)
                9559756   31.995    0.000 6841.502    0.001 __init__.py:68(backward)
                9559756 6556.259    0.001 6556.259    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                9559756  119.264    0.000 5897.320    0.001 agent.py:112(__call__)
               76478056 2529.035    0.000 4482.885    0.000 layer.py:175(NoRock_update)
              955975600 1061.384    0.000 4431.882    0.000 layers.py:838(isFree)
              955975600 2406.370    0.000 4259.117    0.000 layers.py:168(check)
             1840431830 1167.636    0.000 4232.790    0.000 {built-in method builtins.any}
               38239024   66.420    0.000 3628.427    0.000 conv.py:422(forward)
               57358536  131.347    0.000 3573.097    0.000 linear.py:92(forward)
               38239024   75.828    0.000 3537.873    0.000 conv.py:414(_conv_forward)
               38239024 3448.736    0.000 3448.736    0.000 {built-in method conv2d}
               57358536  222.489    0.000 3384.432    0.000 functional.py:1669(linear)
             4689399393 2652.668    0.000 3370.498    0.000 layer.py:103(isFree)
            12858461918 2312.367    0.000 3347.530    0.000 enum.py:646(__hash__)
               42483045  353.699    0.000 3093.924    0.000 level.py:41(notUsed)
               40489495 3089.624    0.000 3089.624    0.000 {built-in method tensor}
              669182950 1870.674    0.000 2910.624    0.000 tensor.py:933(grad)
                9559756  281.222    0.000 2833.998    0.000 optimizer.py:167(zero_grad)
             8476332165 2114.277    0.000 2604.543    0.000 layers.py:809(<genexpr>)
              955975700  312.800    0.000 2603.661    0.000 {built-in method builtins.all}
               19310614 1299.633    0.000 2478.043    0.000 levels.py:75(RFS)
              191195120 2450.537    0.000 2450.537    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               57358536 2427.998    0.000 2427.998    0.000 {built-in method addmm}
             2921309098  736.649    0.000 2411.782    0.000 layers.py:799(<genexpr>)
               19119512   20.523    0.000 2358.342    0.000 game.py:38(board)
              191195120 2091.645    0.000 2091.645    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              955975600 1044.892    0.000 1636.870    0.000 layers.py:141(check)
              955975700 1025.025    0.000 1581.065    0.000 layers.py:113(isDone)
               76478048   66.212    0.000 1562.893    0.000 activation.py:713(forward)
            16863806134 1513.969    0.000 1513.969    0.000 layer.py:99(positions)
               76478048   99.980    0.000 1496.681    0.000 functional.py:1292(leaky_relu)
               76478048 1386.994    0.000 1386.994    0.000 {built-in method torch._C._nn.leaky_relu}
              955975600  903.433    0.000 1349.490    0.000 layers.py:48(check)
               95597560 1300.218    0.000 1300.218    0.000 {method 'add' of 'torch._C._TensorBase' objects}
             1414816776 1279.534    0.000 1279.534    0.000 level.py:32(inverse)
              822139096  443.240    0.000 1271.416    0.000 overrides.py:1070(has_torch_function)
              955975600  822.558    0.000 1268.072    0.000 layers.py:124(check)
               42483045   36.435    0.000 1260.629    0.000 level.py:38(elementsIn)
               95597560 1209.990    0.000 1209.990    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              113288120  154.166    0.000 1154.259    0.000 layer.py:77(restart)
             3489014477 1131.348    0.000 1131.348    0.000 layer.py:154(elements)
               95597560 1116.899    0.000 1116.899    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                9559756  631.826    0.000 1063.383    0.000 collector.py:46(collect)
            12858500227 1035.170    0.000 1035.170    0.000 {built-in method builtins.hash}
              955975600  681.666    0.000 1010.925    0.000 layers.py:23(check)
               95597560 1002.530    0.000 1002.530    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
             1669519649  652.347    0.000  885.734    0.000 layer.py:138(add)
               95597560  786.246    0.000  786.246    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               42483045  378.569    0.000  772.284    0.000 level.py:39(<listcomp>)
        10359206583/10359206582  672.351    0.000  738.126    0.000 {built-in method builtins.len}
               14161115  358.388    0.000  710.409    0.000 layers.py:36(reset)
               19310614  322.368    0.000  679.817    0.000 level.py:16(<dictcomp>)
             8613340156  652.784    0.000  652.784    0.000 {method 'random' of '_random.Random' objects}
             1158636840  397.992    0.000  598.121    0.000 levels.py:31(<genexpr>)
              835060243  403.058    0.000  576.830    0.000 layer.py:134(remove)
                9559756   12.245    0.000  550.081    0.000 loss.py:445(forward)
                9559756   50.860    0.000  537.835    0.000 functional.py:2637(mse_loss)
             7534517480  490.266    0.000  490.266    0.000 layer.py:92(isDead)
             2657129464  487.739    0.000  487.739    0.000 enum.py:352(<genexpr>)
               57358536  473.839    0.000  473.839    0.000 {method 't' of 'torch._C._TensorBase' objects}
             1701636728  363.874    0.000  454.702    0.000 overrides.py:1083(<genexpr>)
               42483045  270.100    0.000  451.910    0.000 {built-in method _functools.reduce}
              337291854  154.782    0.000  446.098    0.000 random.py:285(choice)
                9559756   33.814    0.000  442.801    0.000 exploration.py:47(epsilonGreedy)
             5470203643  423.098    0.000  423.098    0.000 {method 'append' of 'list' objects}
             3733423793  403.422    0.000  403.422    0.000 layer.py:211(isBlocking)
               52782243  158.975    0.000  368.231    0.000 random.py:315(sample)
              462624219  254.986    0.000  364.432    0.000 random.py:250(_randbelow_with_getrandbits)
               19119512  343.654    0.000  343.654    0.000 {built-in method sum}
                9559756  336.815    0.000  336.815    0.000 {built-in method torch._C._nn.mse_loss}
                9559756  307.546    0.000  307.546    0.000 {method 'tolist' of 'torch._C._TensorBase' objects}
                9560711  300.243    0.000  300.243    0.000 {built-in method max}
               38239024   28.500    0.000  269.010    0.000 flatten.py:39(forward)
               95597610  117.849    0.000  263.724    0.000 tensor.py:596(__hash__)
             2867926800  254.803    0.000  254.803    0.000 layer.py:86(check)
                9559756  252.126    0.000  252.126    0.000 {built-in method gather}
                9559756   42.806    0.000  244.754    0.000 __init__.py:28(_make_grads)
               38239024  240.510    0.000  240.510    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9578852: <Maze_simple_0> in cluster <dcc> Done

Job <Maze_simple_0> was submitted from host <n-62-30-3> by user <s183905> in cluster <dcc> at Mon Apr 26 20:44:07 2021
Job was executed on host(s) <n-62-11-14>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Tue May  4 16:50:17 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue May  4 16:50:17 2021
Terminated at Wed May  5 16:45:43 2021
Results reported at Wed May  5 16:45:43 2021

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

    CPU time :                                   85894.35 sec.
    Max Memory :                                 2061 MB
    Average Memory :                             2057.59 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14323.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86126 sec.
    Turnaround time :                            763296 sec.

The output (if any) is above this job summary.

