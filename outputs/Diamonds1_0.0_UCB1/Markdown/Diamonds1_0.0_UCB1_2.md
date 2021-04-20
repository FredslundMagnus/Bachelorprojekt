
# Parameters

    Name :                      Diamonds1_0.0_UCB1-2
    Main :                      graphTrain
    Level :                     Levels.Causal2
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


      22173283586 function calls (21605425395 primitive calls) in 35706.44 seconds

##    Ordered by: cumulative time
   List reduced from 461 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35706.438 35706.438 {built-in method builtins.exec}
                      1    0.001    0.001 35706.438 35706.438 <string>:1(<module>)
                      1  168.873  168.873 35706.437 35706.437 allGraphsTrain.py:10(graphTrain)
                 701419 5440.799    0.008 13034.806    0.019 allGraphs.py:146(transformNot)
              701425008 8453.609    0.000 8453.609    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                 701419   17.403    0.000 8269.950    0.012 allGraphsTrain.py:29(<listcomp>)
               70843420 1949.771    0.000 8252.568    0.000 allGraphs.py:110(states)
              631277500 6151.115    0.000 6151.115    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 701419    2.418    0.000 4452.587    0.006 game.py:41(step)
                 701419    3.220    0.000 4307.447    0.006 layers.py:718(step)
                 701419  658.666    0.001 3124.656    0.004 allGraphsTrain.py:35(<listcomp>)
                 701420  103.928    0.000 2564.230    0.004 layers.py:684(update)
               10734091   14.612    0.000 2465.990    0.000 allGraphs.py:158(getInterventions)
                 701419  137.213    0.000 2059.615    0.003 allGraphsTrain.py:37(<listcomp>)
                 701419   52.508    0.000 1736.093    0.002 layers.py:17(step)
               70141900  115.009    0.000 1677.399    0.000 layer.py:98(move)
                 701419    2.198    0.000 1564.706    0.002 agent.py:29(learn)
                 701419   14.764    0.000 1560.811    0.002 agent.py:117(_learn)
                 701419   45.100    0.000 1546.047    0.002 learner.py:42(Qlearn)
                3859127   29.820    0.000 1518.495    0.000 layers.py:740(restart)
               10734091   10.490    0.000 1429.909    0.000 allGraphs.py:133(UCB1)
               17220434 1405.547    0.000 1405.547    0.000 {built-in method tensor}
        121588980/10734091   84.562    0.000 1375.805    0.000 {built-in method builtins.min}
               30556792   13.894    0.000 1357.122    0.000 allGraphs.py:134(<lambda>)
        232443869/30556792  362.559    0.000 1343.227    0.000 allGraphs.py:68(expected_moves_UCB1)
               14241187    8.795    0.000 1308.228    0.000 game.py:37(board)
               74350414  180.146    0.000 1254.724    0.000 tensor.py:21(wrapped)
                3859127   13.913    0.000 1217.635    0.000 level.py:8(__init__)
                 701419   53.907    0.000 1189.961    0.002 allGraphsTrain.py:44(<listcomp>)
        312741966/71654504   96.415    0.000 1126.461    0.000 allGraphs.py:72(<genexpr>)
                3859127   43.533    0.000 1064.379    0.000 levels.py:151(generate)
               70141900  227.006    0.000 1059.374    0.000 layers.py:735(check)
               10734091   46.540    0.000 1021.469    0.000 allGraphs.py:153(format)
               18521783  176.060    0.000  974.674    0.000 level.py:41(notUsed)
               73648995  853.764    0.000  853.764    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
             3152752955  562.385    0.000  826.073    0.000 enum.py:646(__hash__)
               70141900  813.342    0.000  813.342    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                 701419  420.483    0.001  733.170    0.001 agent.py:67(modify)
                 701419    4.147    0.000  618.866    0.001 grad_mode.py:23(decorate_context)
        16132637/2104257   63.380    0.000  607.828    0.000 module.py:715(_call_impl)
                 701419   20.472    0.000  606.933    0.001 adam.py:55(step)
                1402838    3.625    0.000  555.587    0.000 network.py:27(forward)
                1402838   14.319    0.000  543.198    0.000 container.py:115(forward)
                 701419  110.538    0.000  497.042    0.001 functional.py:53(adam)
               18521783   13.827    0.000  460.321    0.000 level.py:38(elementsIn)
               70141900  105.563    0.000  390.341    0.000 layers.py:729(isFree)
              192538428  111.279    0.000  379.622    0.000 {built-in method builtins.any}
              121588980   76.919    0.000  375.359    0.000 allGraphs.py:83(layers_not_in)
                4909940  225.885    0.000  374.867    0.000 layer.py:167(NoRock_update)
                 701419    3.764    0.000  357.887    0.001 tensor.py:181(backward)
                 701419    2.412    0.000  354.123    0.001 __init__.py:68(backward)
              144492414   68.486    0.000  351.835    0.000 {built-in method builtins.all}
              232443869  217.677    0.000  349.760    0.000 allGraphs.py:60(UCB1)
                 701419  335.616    0.000  335.616    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                 701419    8.404    0.000  322.911    0.000 agent.py:112(__call__)
               18521783  148.659    0.000  300.696    0.000 level.py:39(<listcomp>)
              121588980  144.015    0.000  298.440    0.000 allGraphs.py:84(<listcomp>)
              476482312  221.562    0.000  284.777    0.000 layer.py:95(isFree)
             3152755288  263.688    0.000  263.688    0.000 {built-in method builtins.hash}
              429211246  117.877    0.000  263.547    0.000 layers.py:690(<genexpr>)
               27013889   21.166    0.000  261.224    0.000 layer.py:69(restart)
               72947576  254.504    0.000  254.504    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                2104257    8.259    0.000  252.542    0.000 tensor.py:576(__iter__)
                2104257  238.897    0.000  238.897    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
                2805676    5.044    0.000  218.135    0.000 conv.py:422(forward)
              122047040   65.011    0.000  214.225    0.000 overrides.py:1070(has_torch_function)
                2805676    5.599    0.000  211.146    0.000 conv.py:414(_conv_forward)
                3859227  103.927    0.000  207.273    0.000 layers.py:36(reset)
               70141900  127.380    0.000  206.914    0.000 layers.py:207(check)
                2805676  204.529    0.000  204.529    0.000 {built-in method conv2d}
               70141900  123.339    0.000  201.557    0.000 layers.py:219(check)
               70141900  123.176    0.000  201.359    0.000 layers.py:231(check)
              889281588  197.670    0.000  197.670    0.000 level.py:32(inverse)
              530262984  150.203    0.000  183.865    0.000 layers.py:700(<genexpr>)
               39279518   95.731    0.000  160.298    0.000 tensor.py:933(grad)
                2805676    6.776    0.000  159.466    0.000 linear.py:92(forward)
              805714253  154.449    0.000  154.449    0.000 enum.py:352(<genexpr>)
                2805676   11.498    0.000  149.733    0.000 functional.py:1669(linear)
               18521783   91.331    0.000  145.798    0.000 {built-in method _functools.reduce}
                 701419   12.679    0.000  137.677    0.000 optimizer.py:167(zero_grad)
             1404278829  134.342    0.000  134.342    0.000 layer.py:91(positions)
                3859127   64.992    0.000  129.539    0.000 level.py:16(<dictcomp>)
               70142000   80.910    0.000  123.784    0.000 layers.py:113(isDone)
              209740449   84.103    0.000  114.852    0.000 layer.py:130(add)
                 701419    4.949    0.000  109.728    0.000 agent.py:59(modify_board)
                 701419   62.489    0.000  107.474    0.000 collector.py:46(collect)
                2805676  106.138    0.000  106.138    0.000 {built-in method addmm}
               11222704  101.539    0.000  101.539    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              425453271   93.724    0.000   93.724    0.000 layer.py:146(elements)
               70141900   58.767    0.000   90.347    0.000 layers.py:196(check)
              321250170   69.669    0.000   84.023    0.000 overrides.py:1083(<genexpr>)
               11222704   83.272    0.000   83.272    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               70141900   53.438    0.000   78.347    0.000 layers.py:23(check)
                 701419   52.037    0.000   77.636    0.000 allGraphsTrain.py:43(<listcomp>)
                 701419   72.264    0.000   72.264    0.000 {built-in method torch._C._nn.one_hot}
                4208514    4.191    0.000   71.683    0.000 activation.py:713(forward)
                4208514    6.189    0.000   67.492    0.000 functional.py:1292(leaky_relu)
                 701419   16.390    0.000   61.272    0.000 allGraphs.py:137(transform)
                4208514   60.712    0.000   60.712    0.000 {built-in method torch._C._nn.leaky_relu}
        674633744/674633742   47.502    0.000   59.435    0.000 {built-in method builtins.len}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9532023: <Diamonds1_0.0_UCB1_2> in cluster <dcc> Done

Job <Diamonds1_0.0_UCB1_2> was submitted from host <n-62-30-7> by user <s183905> in cluster <dcc> at Sat Apr 17 13:28:43 2021
Job was executed on host(s) <n-62-20-16>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Mon Apr 19 05:05:30 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Apr 19 05:05:30 2021
Terminated at Mon Apr 19 15:00:40 2021
Results reported at Mon Apr 19 15:00:40 2021

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

    CPU time :                                   35614.00 sec.
    Max Memory :                                 2061 MB
    Average Memory :                             2060.06 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14323.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35758 sec.
    Turnaround time :                            178317 sec.

The output (if any) is above this job summary.

