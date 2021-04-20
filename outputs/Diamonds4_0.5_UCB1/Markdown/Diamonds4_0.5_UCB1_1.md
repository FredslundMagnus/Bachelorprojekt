
# Parameters

    Name :                      Diamonds4_0.5_UCB1-1
    Main :                      graphTrain
    Level :                     Levels.Causal7
    Failed actions chance :     0.5
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


      15326015175 function calls (14802681938 primitive calls) in 35703.99 seconds

##    Ordered by: cumulative time
   List reduced from 465 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35703.992 35703.992 {built-in method builtins.exec}
                      1    0.001    0.001 35703.992 35703.992 <string>:1(<module>)
                      1  146.841  146.841 35703.991 35703.991 allGraphsTrain.py:10(graphTrain)
                 574291 6491.029    0.011 14371.292    0.025 allGraphs.py:146(transformNot)
                 574291   17.002    0.000 8670.263    0.015 allGraphsTrain.py:29(<listcomp>)
               58003492 2290.380    0.000 8653.286    0.000 allGraphs.py:110(states)
              574295992 7840.122    0.000 7840.122    0.000 {method 'item' of 'torch._C._TensorBase' objects}
              516862300 7041.884    0.000 7041.884    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 574291  692.154    0.001 3309.675    0.006 allGraphsTrain.py:35(<listcomp>)
               12820570   20.055    0.000 2617.522    0.000 allGraphs.py:158(getInterventions)
                 574291    2.057    0.000 2534.595    0.004 game.py:41(step)
                 574291    2.763    0.000 2405.264    0.004 layers.py:718(step)
                 574291  157.853    0.000 2128.573    0.004 allGraphsTrain.py:37(<listcomp>)
                 574291    2.066    0.000 1621.165    0.003 agent.py:29(learn)
                 574291   12.438    0.000 1617.824    0.003 agent.py:117(_learn)
                 574291   46.720    0.000 1605.386    0.003 learner.py:42(Qlearn)
               18136885 1573.510    0.000 1573.510    0.000 {built-in method tensor}
               15692026    9.227    0.000 1487.002    0.000 game.py:37(board)
                 574292   80.201    0.000 1386.207    0.002 layers.py:684(update)
               12820570   12.269    0.000 1329.676    0.000 allGraphs.py:133(UCB1)
               60874846  161.243    0.000 1316.807    0.000 tensor.py:21(wrapped)
               12820570   60.925    0.000 1267.790    0.000 allGraphs.py:153(format)
        116209957/12820570   88.065    0.000 1267.094    0.000 {built-in method builtins.min}
                 574291   57.949    0.000 1263.695    0.002 allGraphsTrain.py:44(<listcomp>)
               32490407   15.178    0.000 1243.125    0.000 allGraphs.py:134(<lambda>)
        219599344/32490407  332.793    0.000 1227.947    0.000 allGraphs.py:68(expected_moves_UCB1)
                 574291   43.979    0.000 1013.146    0.002 layers.py:17(step)
        290498324/69149614   93.643    0.000 1008.275    0.000 allGraphs.py:72(<genexpr>)
               60300555  978.998    0.000  978.998    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               57429100   94.773    0.000  963.719    0.000 layer.py:98(move)
               57429100  891.536    0.000  891.536    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                 574291    3.447    0.000  681.747    0.001 grad_mode.py:23(decorate_context)
                 574291  381.655    0.001  675.665    0.001 agent.py:67(modify)
                 574291   17.881    0.000  671.711    0.001 adam.py:55(step)
                1776946   14.232    0.000  667.281    0.000 layers.py:740(restart)
                 574291  122.711    0.000  580.353    0.001 functional.py:53(adam)
        13208693/1722873   54.484    0.000  577.153    0.000 module.py:715(_call_impl)
                1776946    6.826    0.000  534.018    0.000 level.py:8(__init__)
                1148582    3.088    0.000  528.894    0.000 network.py:27(forward)
             2125765653  358.982    0.000  527.295    0.000 enum.py:646(__hash__)
                1148582   14.203    0.000  518.416    0.000 container.py:115(forward)
               57429100  124.224    0.000  482.315    0.000 layers.py:735(check)
                1776946   19.350    0.000  464.666    0.000 levels.py:441(generate)
                8529683   79.054    0.000  424.851    0.000 level.py:41(notUsed)
                 574291    3.776    0.000  368.952    0.001 tensor.py:181(backward)
                 574291    2.052    0.000  365.176    0.001 __init__.py:68(backward)
                 574291  348.106    0.001  348.106    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
              116209957   75.565    0.000  343.251    0.000 allGraphs.py:83(layers_not_in)
              219599344  202.731    0.000  326.054    0.000 allGraphs.py:60(UCB1)
                 574291    7.460    0.000  304.202    0.001 agent.py:112(__call__)
               57429100   80.405    0.000  301.323    0.000 layers.py:729(isFree)
               59726264  300.992    0.000  300.992    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              159024769   86.955    0.000  294.208    0.000 {built-in method builtins.any}
              116209957  132.849    0.000  267.686    0.000 allGraphs.py:84(<listcomp>)
                4020044  147.533    0.000  255.467    0.000 layer.py:167(NoRock_update)
              375992395  169.766    0.000  220.918    0.000 layer.py:95(isFree)
              118304046   46.935    0.000  218.445    0.000 {built-in method builtins.all}
                2297164    4.062    0.000  203.749    0.000 conv.py:422(forward)
                1722873    7.074    0.000  202.663    0.000 tensor.py:576(__iter__)
                2297164    4.885    0.000  198.232    0.000 conv.py:414(_conv_forward)
                8529683    6.536    0.000  197.943    0.000 level.py:38(elementsIn)
                2297164  192.542    0.000  192.542    0.000 {built-in method conv2d}
                1722873  190.683    0.000  190.683    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               99926768   51.161    0.000  168.369    0.000 overrides.py:1070(has_torch_function)
             2125767570  168.314    0.000  168.314    0.000 {built-in method builtins.hash}
              239752160   64.379    0.000  156.027    0.000 layers.py:690(<genexpr>)
                2297164    5.639    0.000  154.153    0.000 linear.py:92(forward)
                2297164    9.686    0.000  146.134    0.000 functional.py:1669(linear)
              445218032  115.061    0.000  141.196    0.000 layers.py:700(<genexpr>)
               32160350   87.336    0.000  137.566    0.000 tensor.py:933(grad)
                 574291   13.965    0.000  135.760    0.000 optimizer.py:167(zero_grad)
                8529683   63.046    0.000  127.568    0.000 level.py:39(<listcomp>)
                9188656  120.785    0.000  120.785    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                 574291   69.705    0.000  116.723    0.000 collector.py:46(collect)
               12438622    9.379    0.000  114.761    0.000 layer.py:69(restart)
                2297164  105.096    0.000  105.096    0.000 {built-in method addmm}
                9188656  102.373    0.000  102.373    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                 574291    4.658    0.000  100.031    0.000 agent.py:59(modify_board)
                1777046   45.471    0.000   90.855    0.000 layers.py:36(reset)
              409529917   87.056    0.000   87.056    0.000 level.py:32(inverse)
               28711263   51.136    0.000   84.707    0.000 layers.py:617(check)
               28713674   49.597    0.000   83.295    0.000 layers.py:602(check)
               28717959   50.381    0.000   82.434    0.000 layers.py:632(check)
              785791736   78.118    0.000   78.118    0.000 layer.py:91(positions)
                3445746    3.081    0.000   73.221    0.000 activation.py:713(forward)
                3445746    4.937    0.000   70.140    0.000 functional.py:1292(leaky_relu)
                4594328   69.568    0.000   69.568    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              371040137   66.409    0.000   66.409    0.000 enum.py:352(<genexpr>)
              263025546   55.239    0.000   65.703    0.000 overrides.py:1083(<genexpr>)
                3445746   64.739    0.000   64.739    0.000 {built-in method torch._C._nn.leaky_relu}
              241877301   63.997    0.000   63.997    0.000 layer.py:146(elements)
                8529683   40.167    0.000   63.839    0.000 {built-in method _functools.reduce}
                 574291   62.865    0.000   62.865    0.000 {built-in method torch._C._nn.one_hot}
              117621994   45.887    0.000   62.495    0.000 layer.py:130(add)
                 574291   39.844    0.000   59.718    0.000 allGraphsTrain.py:43(<listcomp>)
                4594328   59.711    0.000   59.711    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                1776946   30.671    0.000   58.281    0.000 level.py:16(<dictcomp>)
                4594328   54.850    0.000   54.850    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                 574291   12.588    0.000   49.953    0.000 allGraphs.py:137(transform)
                4594328   48.783    0.000   48.783    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9531992: <Diamonds4_0.5_UCB1_1> in cluster <dcc> Done

Job <Diamonds4_0.5_UCB1_1> was submitted from host <n-62-30-7> by user <s183905> in cluster <dcc> at Sat Apr 17 13:24:04 2021
Job was executed on host(s) <n-62-11-13>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sat Apr 17 23:54:07 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat Apr 17 23:54:07 2021
Terminated at Sun Apr 18 09:49:14 2021
Results reported at Sun Apr 18 09:49:14 2021

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

    CPU time :                                   35638.59 sec.
    Max Memory :                                 2064 MB
    Average Memory :                             2062.37 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14320.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35707 sec.
    Turnaround time :                            73510 sec.

The output (if any) is above this job summary.

