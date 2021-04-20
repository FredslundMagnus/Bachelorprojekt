
# Parameters

    Name :                      Diamonds3_0.5_UCB1-2
    Main :                      graphTrain
    Level :                     Levels.Causal6
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


      36412426018 function calls (32933642371 primitive calls) in 35703.04 seconds

##    Ordered by: cumulative time
   List reduced from 463 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35703.041 35703.041 {built-in method builtins.exec}
                      1    0.001    0.001 35703.041 35703.041 <string>:1(<module>)
                      1  137.054  137.054 35703.040 35703.040 allGraphsTrain.py:10(graphTrain)
                 496530 4488.482    0.009 11266.611    0.023 allGraphs.py:146(transformNot)
                 496530  560.849    0.001 9274.726    0.019 allGraphsTrain.py:35(<listcomp>)
               10897269   15.933    0.000 8713.878    0.001 allGraphs.py:158(getInterventions)
              595840468 7944.610    0.000 7944.610    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               10897269   10.454    0.000 7490.964    0.001 allGraphs.py:133(UCB1)
        622984235/10897269  368.476    0.000 7431.931    0.001 {built-in method builtins.min}
               42428213   20.051    0.000 7409.533    0.000 allGraphs.py:134(<lambda>)
                 496530   12.241    0.000 7391.487    0.015 allGraphsTrain.py:29(<listcomp>)
        1235071201/42428213 1953.725    0.000 7389.482    0.000 allGraphs.py:68(expected_moves_UCB1)
               50149631 1617.378    0.000 7379.262    0.000 allGraphs.py:110(states)
        1804729954/140607244  549.854    0.000 7065.718    0.000 allGraphs.py:72(<genexpr>)
              546183500 5146.048    0.000 5146.048    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 496530    2.099    0.000 2843.994    0.006 game.py:41(step)
                 496530    2.880    0.000 2733.487    0.006 layers.py:718(step)
             8623103629 1405.687    0.000 2038.475    0.000 enum.py:646(__hash__)
              622984235  360.600    0.000 2028.554    0.000 allGraphs.py:83(layers_not_in)
             1235071201 1090.408    0.000 1753.308    0.000 allGraphs.py:60(UCB1)
              622984235  805.255    0.000 1667.954    0.000 allGraphs.py:84(<listcomp>)
                 496531   75.206    0.000 1663.397    0.003 layers.py:684(update)
                 496530   93.082    0.000 1497.033    0.003 allGraphsTrain.py:37(<listcomp>)
               15498155 1492.135    0.000 1492.135    0.000 {built-in method tensor}
               13379920    8.088    0.000 1420.795    0.000 game.py:37(board)
               10897269   52.203    0.000 1206.981    0.000 allGraphs.py:153(format)
                 496530    1.993    0.000 1122.468    0.002 agent.py:29(learn)
                 496530   10.845    0.000 1119.180    0.002 agent.py:117(_learn)
                 496530   33.270    0.000 1108.335    0.002 learner.py:42(Qlearn)
                 496530   40.497    0.000 1063.849    0.002 layers.py:17(step)
               49653000   83.217    0.000 1018.515    0.000 layer.py:98(move)
                1911800   17.219    0.000  890.450    0.000 layers.py:740(restart)
               52632180  122.965    0.000  864.312    0.000 tensor.py:21(wrapped)
                 496530   37.459    0.000  817.864    0.002 allGraphsTrain.py:44(<listcomp>)
                1911800    8.135    0.000  733.324    0.000 level.py:8(__init__)
                1911800   26.539    0.000  652.842    0.000 levels.py:288(generate)
             8623105290  632.788    0.000  632.788    0.000 {built-in method builtins.hash}
               11470912  111.654    0.000  598.145    0.000 level.py:41(notUsed)
               52135650  587.085    0.000  587.085    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               49653000  560.825    0.000  560.825    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               49653000  124.707    0.000  522.597    0.000 layers.py:735(check)
                 496530  281.865    0.001  512.480    0.001 agent.py:67(modify)
        11420190/1489590   49.507    0.000  445.882    0.000 module.py:715(_call_impl)
                 496530    3.411    0.000  433.418    0.001 grad_mode.py:23(decorate_context)
                 496530   16.288    0.000  423.666    0.001 adam.py:55(step)
                 993060    2.955    0.000  404.865    0.000 network.py:27(forward)
                 993060   10.946    0.000  394.975    0.000 container.py:115(forward)
                 496530   77.580    0.000  345.695    0.001 functional.py:53(adam)
               49653000   84.534    0.000  333.740    0.000 layers.py:729(isFree)
              137116835   81.307    0.000  293.628    0.000 {built-in method builtins.any}
               11470912    8.470    0.000  275.690    0.000 level.py:38(elementsIn)
                3972248  159.844    0.000  275.032    0.000 layer.py:167(NoRock_update)
                 496530    3.196    0.000  267.016    0.001 tensor.py:181(backward)
                 496530    2.091    0.000  263.820    0.001 __init__.py:68(backward)
                 496530  249.653    0.001  249.653    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
              383914464  204.578    0.000  249.206    0.000 layer.py:95(isFree)
                 496530    7.754    0.000  246.503    0.000 agent.py:112(__call__)
              102285280   38.590    0.000  242.647    0.000 {built-in method builtins.all}
             1236560791  234.149    0.000  234.149    0.000 {built-in method builtins.max}
             1235002203  230.236    0.000  230.236    0.000 {built-in method math.log}
              198771890   59.306    0.000  190.583    0.000 layers.py:690(<genexpr>)
                1489590    6.510    0.000  184.954    0.000 tensor.py:576(__iter__)
               11470912   87.429    0.000  177.876    0.000 level.py:39(<listcomp>)
               51639120  176.015    0.000  176.015    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                1489590  174.629    0.000  174.629    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
                1986120    3.806    0.000  157.494    0.000 conv.py:422(forward)
              429671700  126.623    0.000  153.798    0.000 layers.py:700(<genexpr>)
                1986120    4.792    0.000  152.176    0.000 conv.py:414(_conv_forward)
               86396354   46.135    0.000  149.108    0.000 overrides.py:1070(has_torch_function)
                1986120  146.635    0.000  146.635    0.000 {built-in method conv2d}
             1238974578  137.751    0.000  137.751    0.000 {built-in method math.sqrt}
               15294400   12.934    0.000  134.699    0.000 layer.py:69(restart)
              544103584  127.414    0.000  127.414    0.000 level.py:32(inverse)
                1986120    4.917    0.000  116.032    0.000 linear.py:92(forward)
               24832845   66.960    0.000  110.011    0.000 layers.py:424(check)
               27805734   65.546    0.000  109.283    0.000 tensor.py:933(grad)
                1986120    8.526    0.000  108.827    0.000 functional.py:1669(linear)
                1911900   50.878    0.000  100.566    0.000 layers.py:36(reset)
                 496530    9.370    0.000   94.665    0.000 optimizer.py:167(zero_grad)
               11470912   55.749    0.000   89.344    0.000 {built-in method _functools.reduce}
               49653100   56.481    0.000   88.633    0.000 layers.py:457(isDone)
              481779161   88.083    0.000   88.083    0.000 enum.py:352(<genexpr>)
                 496530    4.387    0.000   83.422    0.000 agent.py:59(modify_board)
                1986120   77.254    0.000   77.254    0.000 {built-in method addmm}
               24825785   48.460    0.000   76.959    0.000 layers.py:452(check)
                 496530   43.872    0.000   75.628    0.000 collector.py:46(collect)
               24827161   46.769    0.000   75.225    0.000 layers.py:437(check)
              737900354   75.121    0.000   75.121    0.000 layer.py:91(positions)
              242159553   70.371    0.000   70.371    0.000 layer.py:146(elements)
                7944480   69.634    0.000   69.634    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                1911800   35.519    0.000   67.052    0.000 level.py:16(<dictcomp>)
              117868200   47.570    0.000   65.457    0.000 layer.py:130(add)
              227411008   48.857    0.000   58.153    0.000 overrides.py:1083(<genexpr>)
                7944480   57.074    0.000   57.074    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                 496530   37.231    0.000   55.136    0.000 allGraphsTrain.py:43(<listcomp>)
                 496530   54.946    0.000   54.946    0.000 {built-in method torch._C._nn.one_hot}
                2979180    3.116    0.000   51.211    0.000 activation.py:713(forward)
                2979180    4.740    0.000   48.096    0.000 functional.py:1292(leaky_relu)
                 496530   11.651    0.000   44.047    0.000 allGraphs.py:137(transform)
                2979180   42.922    0.000   42.922    0.000 {built-in method torch._C._nn.leaky_relu}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9531990: <Diamonds3_0.5_UCB1_2> in cluster <dcc> Done

Job <Diamonds3_0.5_UCB1_2> was submitted from host <n-62-30-7> by user <s183905> in cluster <dcc> at Sat Apr 17 13:24:04 2021
Job was executed on host(s) <n-62-20-10>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sat Apr 17 23:19:56 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat Apr 17 23:19:56 2021
Terminated at Sun Apr 18 09:15:02 2021
Results reported at Sun Apr 18 09:15:02 2021

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

    CPU time :                                   35586.69 sec.
    Max Memory :                                 2077 MB
    Average Memory :                             2076.66 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14307.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35707 sec.
    Turnaround time :                            71458 sec.

The output (if any) is above this job summary.

