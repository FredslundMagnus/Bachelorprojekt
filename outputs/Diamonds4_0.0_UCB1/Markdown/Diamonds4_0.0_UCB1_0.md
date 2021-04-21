
# Parameters

    Name :                      Diamonds4_0.0_UCB1-0
    Main :                      graphTrain
    Level :                     Levels.Causal7
    Failed actions chance :     0.0
    Hours :                     10.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.UCB1
    Network1 :                  Networks.Teleporter
    K1 :                        200000.0
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
    K2 :                        100000.0
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
    Softmax cap :               0.0
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                3
    Counterfacts :              2
    Topn :                      5
    Random counterfacts :       False
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      16693794333 function calls (16329740850 primitive calls) in 35702.72 seconds

##    Ordered by: cumulative time
   List reduced from 465 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35702.725 35702.725 {built-in method builtins.exec}
                      1    0.001    0.001 35702.725 35702.725 <string>:1(<module>)
                      1  148.724  148.724 35702.724 35702.724 allGraphsTrain.py:10(graphTrain)
                 607051 6446.192    0.011 14502.159    0.024 allGraphs.py:146(transformNot)
                 607051   15.513    0.000 8817.554    0.015 allGraphsTrain.py:29(<listcomp>)
               61312252 2288.089    0.000 8802.056    0.000 allGraphs.py:110(states)
              607056256 8217.259    0.000 8217.259    0.000 {method 'item' of 'torch._C._TensorBase' objects}
              546346300 7044.616    0.000 7044.616    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 607051    2.114    0.000 3081.326    0.005 game.py:41(step)
                 607051    2.873    0.000 2946.878    0.005 layers.py:718(step)
                 607051  679.707    0.001 2422.822    0.004 allGraphsTrain.py:35(<listcomp>)
                 607051  162.018    0.000 2171.742    0.004 allGraphsTrain.py:37(<listcomp>)
                8903801   13.002    0.000 1743.115    0.000 allGraphs.py:158(getInterventions)
                 607051    1.838    0.000 1598.322    0.003 agent.py:29(learn)
                 607051   12.371    0.000 1595.095    0.003 agent.py:117(_learn)
                 607051   46.173    0.000 1582.725    0.003 learner.py:42(Qlearn)
                 607052   78.500    0.000 1575.753    0.003 layers.py:684(update)
                 607051   42.189    0.000 1365.135    0.002 layers.py:17(step)
               64347406  162.854    0.000 1321.071    0.000 tensor.py:21(wrapped)
               60705100   89.914    0.000 1317.745    0.000 layer.py:98(move)
                 607051   57.556    0.000 1268.339    0.002 allGraphsTrain.py:44(<listcomp>)
               14521883 1227.849    0.000 1227.849    0.000 {built-in method tensor}
               11939057    7.173    0.000 1137.389    0.000 game.py:37(board)
               63740355  980.219    0.000  980.219    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               60705100  895.150    0.000  895.150    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                8903801   40.859    0.000  877.194    0.000 allGraphs.py:153(format)
                2406485   17.628    0.000  853.837    0.000 layers.py:740(restart)
                8903801    7.867    0.000  852.919    0.000 allGraphs.py:133(UCB1)
               60705100  173.058    0.000  831.373    0.000 layers.py:735(check)
        80071815/8903801   52.191    0.000  811.761    0.000 {built-in method builtins.min}
               22532115    9.240    0.000  797.557    0.000 allGraphs.py:134(<lambda>)
        151239829/22532115  211.644    0.000  788.317    0.000 allGraphs.py:68(expected_moves_UCB1)
                 607051  400.892    0.001  695.433    0.001 agent.py:67(modify)
                2406485    8.431    0.000  685.152    0.000 level.py:8(__init__)
                 607051    3.394    0.000  673.091    0.001 grad_mode.py:23(decorate_context)
                 607051   17.021    0.000  663.074    0.001 adam.py:55(step)
        199875728/47839376   55.778    0.000  645.582    0.000 allGraphs.py:72(<genexpr>)
                2406485   24.002    0.000  596.982    0.000 levels.py:441(generate)
        13962173/1821153   53.807    0.000  574.252    0.000 module.py:715(_call_impl)
                 607051  120.594    0.000  572.247    0.001 functional.py:53(adam)
               11550762   98.397    0.000  546.954    0.000 level.py:41(notUsed)
             2250271329  367.759    0.000  539.804    0.000 enum.py:646(__hash__)
                1214102    3.102    0.000  526.450    0.000 network.py:27(forward)
                1214102   13.174    0.000  515.901    0.000 container.py:115(forward)
                 607051    3.412    0.000  360.329    0.001 tensor.py:181(backward)
                 607051    1.931    0.000  356.916    0.001 __init__.py:68(backward)
                 607051  339.678    0.001  339.678    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               60705100   80.289    0.000  310.693    0.000 layers.py:729(isFree)
                 607051    7.348    0.000  303.651    0.001 agent.py:112(__call__)
               63133304  300.486    0.000  300.486    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              167568030   86.752    0.000  296.540    0.000 {built-in method builtins.any}
                4249364  158.094    0.000  268.687    0.000 layer.py:167(NoRock_update)
               11550762    7.660    0.000  261.115    0.000 level.py:38(elementsIn)
              413213075  181.389    0.000  230.405    0.000 layer.py:95(isFree)
               80071815   47.133    0.000  224.332    0.000 allGraphs.py:83(layers_not_in)
              151239829  130.997    0.000  212.954    0.000 allGraphs.py:60(UCB1)
              125052606   42.205    0.000  207.522    0.000 {built-in method builtins.all}
                2428204    3.954    0.000  203.865    0.000 conv.py:422(forward)
                1821153    7.224    0.000  202.287    0.000 tensor.py:576(__iter__)
                2428204    4.592    0.000  198.450    0.000 conv.py:414(_conv_forward)
                2428204  193.076    0.000  193.076    0.000 {built-in method conv2d}
                1821153  190.256    0.000  190.256    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               80071815   85.793    0.000  177.199    0.000 allGraphs.py:84(<listcomp>)
             2250273342  172.045    0.000  172.045    0.000 {built-in method builtins.hash}
               11550762   83.690    0.000  170.734    0.000 level.py:39(<listcomp>)
              105627008   51.949    0.000  169.383    0.000 overrides.py:1070(has_torch_function)
               60705100  101.411    0.000  165.020    0.000 layers.py:617(check)
               60705100   95.196    0.000  157.642    0.000 layers.py:632(check)
               60705100   95.113    0.000  156.887    0.000 layers.py:602(check)
                2428204    5.362    0.000  152.868    0.000 linear.py:92(forward)
              231222161   59.316    0.000  149.207    0.000 layers.py:690(<genexpr>)
               16845395   11.784    0.000  145.575    0.000 layer.py:69(restart)
                2428204    9.456    0.000  145.222    0.000 functional.py:1669(linear)
              466389720  116.384    0.000  143.395    0.000 layers.py:700(<genexpr>)
               33994910   87.735    0.000  138.039    0.000 tensor.py:933(grad)
                 607051   12.294    0.000  133.702    0.000 optimizer.py:167(zero_grad)
                9712816  120.267    0.000  120.267    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                 607051   69.471    0.000  116.347    0.000 collector.py:46(collect)
                2406585   57.976    0.000  116.066    0.000 layers.py:36(reset)
             1220680664  111.700    0.000  111.700    0.000 layer.py:91(positions)
              554582187  111.258    0.000  111.258    0.000 level.py:32(inverse)
                2428204  105.006    0.000  105.006    0.000 {built-in method addmm}
                9712816  101.440    0.000  101.440    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                 607051    4.344    0.000  101.013    0.000 agent.py:59(modify_board)
              502462385   83.188    0.000   83.188    0.000 enum.py:352(<genexpr>)
               11550762   51.335    0.000   82.721    0.000 {built-in method _functools.reduce}
               60705100   46.936    0.000   74.186    0.000 layers.py:588(check)
                2406485   38.255    0.000   74.069    0.000 level.py:16(<dictcomp>)
                3642306    3.527    0.000   73.863    0.000 activation.py:713(forward)
              146922057   52.391    0.000   71.941    0.000 layer.py:130(add)
                3642306    5.054    0.000   70.335    0.000 functional.py:1292(leaky_relu)
              299947492   67.436    0.000   67.436    0.000 layer.py:146(elements)
              278029626   55.601    0.000   66.019    0.000 overrides.py:1083(<genexpr>)
                4856408   65.335    0.000   65.335    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                3642306   64.810    0.000   64.810    0.000 {built-in method torch._C._nn.leaky_relu}
                 607051   64.466    0.000   64.466    0.000 {built-in method torch._C._nn.one_hot}
               60705100   42.210    0.000   62.202    0.000 layers.py:23(check)
                 607051   40.231    0.000   60.678    0.000 allGraphsTrain.py:43(<listcomp>)
                4856408   59.635    0.000   59.635    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                4856408   54.767    0.000   54.767    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9532030: <Diamonds4_0.0_UCB1_0> in cluster <dcc> Done

Job <Diamonds4_0.0_UCB1_0> was submitted from host <n-62-30-7> by user <s183905> in cluster <dcc> at Sat Apr 17 13:28:44 2021
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Mon Apr 19 18:36:29 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Apr 19 18:36:29 2021
Terminated at Tue Apr 20 04:31:36 2021
Results reported at Tue Apr 20 04:31:36 2021

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
#BSUB -W 720
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $LSB_PROJECT_NAME


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   35616.22 sec.
    Max Memory :                                 2059 MB
    Average Memory :                             2058.76 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14325.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35707 sec.
    Turnaround time :                            226972 sec.

The output (if any) is above this job summary.

