
# Parameters

    Name :                      Diamonds2_0.0_UCB1-2
    Main :                      graphTrain
    Level :                     Levels.Causal5
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


      46169530756 function calls (41516862717 primitive calls) in 35707.62 seconds

##    Ordered by: cumulative time
   List reduced from 464 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35707.621 35707.621 {built-in method builtins.exec}
                      1    0.001    0.001 35707.621 35707.621 <string>:1(<module>)
                      1  102.832  102.832 35707.620 35707.620 allGraphsTrain.py:10(graphTrain)
                 414968  387.958    0.001 11584.910    0.028 allGraphsTrain.py:35(<listcomp>)
                6028774    9.244    0.000 11196.952    0.002 allGraphs.py:158(getInterventions)
                6028774    6.442    0.000 10482.430    0.002 allGraphs.py:133(UCB1)
        798416322/6028774  514.475    0.000 10445.319    0.002 {built-in method builtins.min}
               22435200   11.396    0.000 10431.089    0.000 allGraphs.py:134(<lambda>)
                 414968 4390.242    0.011 10420.065    0.025 allGraphs.py:146(transformNot)
        1590803870/22435200 2726.885    0.000 10419.693    0.000 allGraphs.py:68(expected_moves_UCB1)
        2360756218/77144140  768.103    0.000 10226.522    0.000 allGraphs.py:72(<genexpr>)
                 414968   11.239    0.000 7081.669    0.017 allGraphsTrain.py:29(<listcomp>)
               41911869 1669.770    0.000 7070.455    0.000 allGraphs.py:110(states)
              580959112 6688.906    0.000 6688.906    0.000 {method 'item' of 'torch._C._TensorBase' objects}
              539459000 5121.759    0.000 5121.759    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
              798416322  484.486    0.000 2951.394    0.000 allGraphs.py:83(layers_not_in)
            12385894516 1970.242    0.000 2944.601    0.000 enum.py:646(__hash__)
                 414968    1.438    0.000 2633.718    0.006 game.py:41(step)
                 414968    2.218    0.000 2542.757    0.006 layers.py:718(step)
              798416322 1176.114    0.000 2466.908    0.000 allGraphs.py:84(<listcomp>)
             1590803870 1454.694    0.000 2302.358    0.000 allGraphs.py:60(UCB1)
                 414968   34.216    0.000 1292.578    0.003 layers.py:17(step)
               41496800   69.814    0.000 1254.259    0.000 layer.py:98(move)
                 414969   59.008    0.000 1245.609    0.003 layers.py:684(update)
                 414968   80.768    0.000 1178.633    0.003 allGraphsTrain.py:37(<listcomp>)
            12385895921  974.359    0.000  974.359    0.000 {built-in method builtins.hash}
                9878946  971.147    0.000  971.147    0.000 {built-in method tensor}
                 414968    1.450    0.000  906.084    0.002 agent.py:29(learn)
                8103615    5.093    0.000  904.150    0.000 game.py:37(board)
                 414968    8.394    0.000  903.800    0.002 agent.py:117(_learn)
                 414968   26.525    0.000  895.406    0.002 learner.py:42(Qlearn)
               41496800  164.024    0.000  840.602    0.000 layers.py:735(check)
               43986608  105.636    0.000  739.220    0.000 tensor.py:21(wrapped)
                6028774   31.536    0.000  705.277    0.000 allGraphs.py:153(format)
                 414968   33.583    0.000  704.285    0.002 allGraphsTrain.py:44(<listcomp>)
                1337449   11.838    0.000  655.725    0.000 layers.py:740(restart)
                1337449    5.824    0.000  545.599    0.000 level.py:8(__init__)
               43571640  503.913    0.000  503.913    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                1337449   20.076    0.000  495.349    0.000 levels.py:249(generate)
               41496800  465.278    0.000  465.278    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                8694088   79.593    0.000  453.509    0.000 level.py:41(notUsed)
                 414968  219.595    0.001  401.281    0.001 agent.py:67(modify)
                 414968    2.515    0.000  358.820    0.001 grad_mode.py:23(decorate_context)
        9544264/1244904   37.579    0.000  355.237    0.000 module.py:715(_call_impl)
                 414968   12.462    0.000  351.535    0.001 adam.py:55(step)
                 829936    2.217    0.000  324.273    0.000 network.py:27(forward)
                 829936    9.138    0.000  316.876    0.000 container.py:115(forward)
                 414968   64.773    0.000  287.600    0.001 functional.py:53(adam)
             1590628150  287.481    0.000  287.481    0.000 {built-in method math.log}
               41496800   76.908    0.000  277.771    0.000 layers.py:729(isFree)
             1592048774  273.929    0.000  273.929    0.000 {built-in method builtins.max}
              114853826   68.735    0.000  254.637    0.000 {built-in method builtins.any}
                3734721  126.497    0.000  227.105    0.000 layer.py:167(NoRock_update)
                8694088    6.423    0.000  214.240    0.000 level.py:38(elementsIn)
                 414968    2.341    0.000  205.529    0.000 tensor.py:181(backward)
                 414968    1.421    0.000  203.188    0.000 __init__.py:68(backward)
              371376675  152.367    0.000  200.864    0.000 layer.py:95(isFree)
                 414968  192.391    0.000  192.391    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                 414968    5.365    0.000  191.647    0.000 agent.py:112(__call__)
             1593948029  167.268    0.000  167.268    0.000 {built-in method math.sqrt}
               85483508   33.418    0.000  147.211    0.000 {built-in method builtins.all}
               43156672  146.748    0.000  146.748    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                1244904    5.073    0.000  143.627    0.000 tensor.py:576(__iter__)
                8694088   67.117    0.000  140.189    0.000 level.py:39(<listcomp>)
                1244904  135.279    0.000  135.279    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
              401594510  106.972    0.000  134.161    0.000 layers.py:700(<genexpr>)
                1659872    2.833    0.000  126.299    0.000 conv.py:422(forward)
               41496800   76.664    0.000  125.733    0.000 layers.py:387(check)
               72204566   36.805    0.000  123.890    0.000 overrides.py:1070(has_torch_function)
                1659872    3.415    0.000  122.320    0.000 conv.py:414(_conv_forward)
               41496800   72.298    0.000  119.725    0.000 layers.py:349(check)
               41496800   72.781    0.000  119.470    0.000 layers.py:337(check)
                1659872  118.318    0.000  118.318    0.000 {built-in method conv2d}
               41496800   71.143    0.000  117.261    0.000 layers.py:375(check)
             1011169883  104.709    0.000  104.709    0.000 layer.py:91(positions)
              164824400   44.005    0.000  101.826    0.000 layers.py:690(<genexpr>)
              410042035   97.185    0.000   97.185    0.000 level.py:32(inverse)
               12037041    8.830    0.000   94.121    0.000 layer.py:69(restart)
                1659872    4.007    0.000   92.873    0.000 linear.py:92(forward)
               23238262   55.232    0.000   91.824    0.000 tensor.py:933(grad)
                1659872    6.765    0.000   87.120    0.000 functional.py:1669(linear)
                 414968    8.076    0.000   80.497    0.000 optimizer.py:167(zero_grad)
                1337549   34.589    0.000   70.487    0.000 layers.py:36(reset)
                8694088   41.965    0.000   67.628    0.000 {built-in method _functools.reduce}
              361136897   64.655    0.000   64.655    0.000 enum.py:352(<genexpr>)
                 414968    3.138    0.000   64.343    0.000 agent.py:59(modify_board)
                 414968   36.423    0.000   62.694    0.000 collector.py:46(collect)
                1659872   61.497    0.000   61.497    0.000 {built-in method addmm}
              187937555   57.923    0.000   57.923    0.000 layer.py:146(elements)
                6639488   57.187    0.000   57.187    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               41496800   35.203    0.000   55.151    0.000 layers.py:364(check)
               41496800   34.125    0.000   53.808    0.000 layers.py:326(check)
              190055612   43.260    0.000   51.454    0.000 overrides.py:1083(<genexpr>)
               90897931   36.290    0.000   50.057    0.000 layer.py:130(add)
                6639488   48.089    0.000   48.089    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               41496800   30.687    0.000   46.058    0.000 layers.py:23(check)
                 414968   30.589    0.000   45.848    0.000 allGraphsTrain.py:43(<listcomp>)
                 414968   42.138    0.000   42.138    0.000 {built-in method torch._C._nn.one_hot}
                2489808    2.258    0.000   41.846    0.000 activation.py:713(forward)
              371376675   40.758    0.000   40.758    0.000 layer.py:203(isBlocking)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9532026: <Diamonds2_0.0_UCB1_2> in cluster <dcc> Done

Job <Diamonds2_0.0_UCB1_2> was submitted from host <n-62-30-7> by user <s183905> in cluster <dcc> at Sat Apr 17 13:28:43 2021
Job was executed on host(s) <n-62-11-16>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Mon Apr 19 07:21:32 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Apr 19 07:21:32 2021
Terminated at Mon Apr 19 17:16:44 2021
Results reported at Mon Apr 19 17:16:44 2021

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

    CPU time :                                   35618.11 sec.
    Max Memory :                                 2065 MB
    Average Memory :                             2064.77 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14319.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35714 sec.
    Turnaround time :                            186481 sec.

The output (if any) is above this job summary.

