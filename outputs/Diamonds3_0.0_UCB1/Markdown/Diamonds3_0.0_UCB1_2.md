
# Parameters

    Name :                      Diamonds3_0.0_UCB1-2
    Main :                      graphTrain
    Level :                     Levels.Causal6
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


      28248248556 function calls (26089773023 primitive calls) in 35708.29 seconds

##    Ordered by: cumulative time
   List reduced from 463 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35708.291 35708.291 {built-in method builtins.exec}
                      1    0.001    0.001 35708.291 35708.291 <string>:1(<module>)
                      1  116.256  116.256 35708.289 35708.289 allGraphsTrain.py:10(graphTrain)
                 467942 5923.623    0.013 13379.109    0.029 allGraphs.py:146(transformNot)
                 467942   12.519    0.000 8394.750    0.018 allGraphsTrain.py:29(<listcomp>)
               47262243 2156.587    0.000 8382.284    0.000 allGraphs.py:110(states)
              561534636 7595.134    0.000 7595.134    0.000 {method 'item' of 'torch._C._TensorBase' objects}
              514736700 6622.816    0.000 6622.816    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 467942  525.802    0.001 5620.795    0.012 allGraphsTrain.py:35(<listcomp>)
                6869578   11.070    0.000 5094.994    0.001 allGraphs.py:158(getInterventions)
                6869578    6.302    0.000 4323.659    0.001 allGraphs.py:133(UCB1)
        386174796/6869578  210.235    0.000 4288.307    0.001 {built-in method builtins.min}
               26530290   10.955    0.000 4274.245    0.000 allGraphs.py:134(<lambda>)
        765480014/26530290 1136.235    0.000 4263.291    0.000 allGraphs.py:68(expected_moves_UCB1)
        1118254942/87393574  309.594    0.000 4071.045    0.000 allGraphs.py:72(<genexpr>)
                 467942    1.636    0.000 2944.534    0.006 game.py:41(step)
                 467942    2.231    0.000 2836.304    0.006 layers.py:718(step)
                 467942  126.209    0.000 1672.749    0.004 allGraphsTrain.py:37(<listcomp>)
                 467943   63.067    0.000 1613.059    0.003 layers.py:684(update)
             6163526620  930.261    0.000 1364.469    0.000 enum.py:646(__hash__)
                 467942    1.530    0.000 1251.477    0.003 agent.py:29(learn)
                 467942    9.724    0.000 1248.915    0.003 agent.py:117(_learn)
                 467942   35.733    0.000 1239.191    0.003 learner.py:42(Qlearn)
                 467942   33.046    0.000 1218.537    0.003 layers.py:17(step)
               46794200   71.202    0.000 1181.443    0.000 layer.py:98(move)
              386174796  204.147    0.000 1167.451    0.000 allGraphs.py:83(layers_not_in)
               11206906 1050.824    0.000 1050.824    0.000 {built-in method tensor}
              765480014  631.675    0.000 1018.795    0.000 allGraphs.py:60(UCB1)
               49601852  125.288    0.000 1018.206    0.000 tensor.py:21(wrapped)
                9209289    5.936    0.000  978.880    0.000 game.py:37(board)
                 467942   44.012    0.000  977.019    0.002 allGraphsTrain.py:44(<listcomp>)
                2274269   17.530    0.000  967.290    0.000 layers.py:740(restart)
              386174796  466.378    0.000  963.305    0.000 allGraphs.py:84(<listcomp>)
                2274269    8.034    0.000  798.745    0.000 level.py:8(__init__)
               46794200  153.977    0.000  779.268    0.000 layers.py:735(check)
                6869578   33.965    0.000  760.265    0.000 allGraphs.py:153(format)
               49133910  758.051    0.000  758.051    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                2274269   28.277    0.000  717.246    0.000 levels.py:288(generate)
               46794200  689.110    0.000  689.110    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               13645277  117.641    0.000  658.518    0.000 level.py:41(notUsed)
                 467942  323.645    0.001  552.441    0.001 agent.py:67(modify)
                 467942    2.679    0.000  524.269    0.001 grad_mode.py:23(decorate_context)
                 467942   13.466    0.000  516.257    0.001 adam.py:55(step)
        10762666/1403826   41.492    0.000  445.154    0.000 module.py:715(_call_impl)
                 467942   93.550    0.000  444.937    0.001 functional.py:53(adam)
             6163528185  434.208    0.000  434.208    0.000 {built-in method builtins.hash}
                 935884    2.541    0.000  408.260    0.000 network.py:27(forward)
                 935884   10.127    0.000  399.986    0.000 container.py:115(forward)
               13645277    9.189    0.000  308.206    0.000 level.py:38(elementsIn)
                 467942    3.037    0.000  288.812    0.001 tensor.py:181(backward)
                 467942    1.581    0.000  285.774    0.001 __init__.py:68(backward)
                 467942  272.423    0.001  272.423    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               46794200   79.300    0.000  265.000    0.000 layers.py:729(isFree)
              128749726   69.720    0.000  245.961    0.000 {built-in method builtins.any}
                3743544  139.363    0.000  238.634    0.000 layer.py:167(NoRock_update)
                 467942    6.057    0.000  236.568    0.001 agent.py:112(__call__)
               48665968  229.740    0.000  229.740    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               13645277  101.773    0.000  200.782    0.000 level.py:39(<listcomp>)
               96396152   29.539    0.000  196.021    0.000 {built-in method builtins.all}
              364166160  145.812    0.000  185.700    0.000 layer.py:95(isFree)
               46794200  109.511    0.000  180.523    0.000 layers.py:424(check)
                1871768    3.282    0.000  157.385    0.000 conv.py:422(forward)
                1403826    5.622    0.000  156.710    0.000 tensor.py:576(__iter__)
              138761949   35.021    0.000  154.485    0.000 layers.py:690(<genexpr>)
                1871768    3.738    0.000  152.931    0.000 conv.py:414(_conv_forward)
                1871768  148.564    0.000  148.564    0.000 {built-in method conv2d}
                1403826  147.318    0.000  147.318    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               18194152   14.025    0.000  145.063    0.000 layer.py:69(restart)
              765435254  143.991    0.000  143.991    0.000 {built-in method math.log}
              647242019  139.238    0.000  139.238    0.000 level.py:32(inverse)
              766883840  134.192    0.000  134.192    0.000 {built-in method builtins.max}
               81422042   40.633    0.000  129.484    0.000 overrides.py:1070(has_torch_function)
               46794200   78.267    0.000  126.506    0.000 layers.py:452(check)
              400680279  103.629    0.000  126.007    0.000 layers.py:700(<genexpr>)
               46794200   74.586    0.000  121.778    0.000 layers.py:437(check)
                1871768    4.434    0.000  119.458    0.000 linear.py:92(forward)
                1871768    7.721    0.000  113.225    0.000 functional.py:1669(linear)
                2274369   55.218    0.000  110.491    0.000 layers.py:36(reset)
               26204806   68.035    0.000  107.324    0.000 tensor.py:933(grad)
                 467942    9.965    0.000  104.269    0.000 optimizer.py:167(zero_grad)
             1093896304  100.414    0.000  100.414    0.000 layer.py:91(positions)
              573105185   98.251    0.000   98.251    0.000 enum.py:352(<genexpr>)
               13645277   61.406    0.000   98.235    0.000 {built-in method _functools.reduce}
                7487072   92.725    0.000   92.725    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                 467942   53.490    0.000   89.980    0.000 collector.py:46(collect)
                1871768   81.531    0.000   81.531    0.000 {built-in method addmm}
                 467942    3.939    0.000   78.805    0.000 agent.py:59(modify_board)
                7487072   78.782    0.000   78.782    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               46794300   46.561    0.000   74.123    0.000 layers.py:457(isDone)
              769178925   73.489    0.000   73.489    0.000 {built-in method math.sqrt}
                2274269   34.272    0.000   67.982    0.000 level.py:16(<dictcomp>)
              130672425   47.463    0.000   64.649    0.000 layer.py:130(add)
              266579218   61.225    0.000   61.225    0.000 layer.py:146(elements)
               46794200   37.167    0.000   58.384    0.000 layers.py:402(check)
                2807652    2.486    0.000   57.009    0.000 activation.py:713(forward)
               46794200   35.579    0.000   55.720    0.000 layers.py:413(check)
                2807652    3.697    0.000   54.523    0.000 functional.py:1292(leaky_relu)
                3743536   53.102    0.000   53.102    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                2807652   50.466    0.000   50.466    0.000 {built-in method torch._C._nn.leaky_relu}
              214317704   42.044    0.000   49.952    0.000 overrides.py:1083(<genexpr>)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9532029: <Diamonds3_0.0_UCB1_2> in cluster <dcc> Done

Job <Diamonds3_0.0_UCB1_2> was submitted from host <n-62-30-7> by user <s183905> in cluster <dcc> at Sat Apr 17 13:28:44 2021
Job was executed on host(s) <n-62-20-7>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Mon Apr 19 15:57:31 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Apr 19 15:57:31 2021
Terminated at Tue Apr 20 01:52:43 2021
Results reported at Tue Apr 20 01:52:43 2021

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

    CPU time :                                   35656.04 sec.
    Max Memory :                                 2063 MB
    Average Memory :                             2062.80 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14321.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35714 sec.
    Turnaround time :                            217439 sec.

The output (if any) is above this job summary.

