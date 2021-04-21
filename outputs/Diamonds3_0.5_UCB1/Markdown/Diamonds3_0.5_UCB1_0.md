
# Parameters

    Name :                      Diamonds3_0.5_UCB1-0
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


      36058516204 function calls (32599558337 primitive calls) in 35710.20 seconds

##    Ordered by: cumulative time
   List reduced from 464 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35710.199 35710.199 {built-in method builtins.exec}
                      1    0.001    0.001 35710.199 35710.199 <string>:1(<module>)
                      1  137.164  137.164 35710.198 35710.198 allGraphsTrain.py:10(graphTrain)
                 489162 4459.448    0.009 11221.157    0.023 allGraphs.py:146(transformNot)
                 489162  557.828    0.001 9385.443    0.019 allGraphsTrain.py:35(<listcomp>)
               10790440   15.721    0.000 8827.615    0.001 allGraphs.py:158(getInterventions)
              586998812 7913.719    0.000 7913.719    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               10790440   10.975    0.000 7572.352    0.001 allGraphs.py:133(UCB1)
        619329757/10790440  364.911    0.000 7512.347    0.001 {built-in method builtins.min}
               42058047   19.093    0.000 7490.406    0.000 allGraphs.py:134(<lambda>)
        1227869074/42058047 1975.481    0.000 7471.313    0.000 allGraphs.py:68(expected_moves_UCB1)
                 489162   13.213    0.000 7338.959    0.015 allGraphsTrain.py:29(<listcomp>)
               49405463 1590.116    0.000 7325.800    0.000 allGraphs.py:110(states)
        1794350344/139526444  532.155    0.000 7143.208    0.000 allGraphs.py:72(<genexpr>)
              538078700 5131.646    0.000 5131.646    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 489162    2.053    0.000 2819.625    0.006 game.py:41(step)
                 489162    2.859    0.000 2704.008    0.006 layers.py:718(step)
              619329757  351.149    0.000 2083.582    0.000 allGraphs.py:83(layers_not_in)
             8567046669 1417.187    0.000 2068.590    0.000 enum.py:646(__hash__)
             1227869074 1111.893    0.000 1767.414    0.000 allGraphs.py:60(UCB1)
              619329757  852.526    0.000 1732.433    0.000 allGraphs.py:84(<listcomp>)
                 489163   80.566    0.000 1648.429    0.003 layers.py:684(update)
               15323311 1533.940    0.000 1533.940    0.000 {built-in method tensor}
                 489162   93.011    0.000 1490.073    0.003 allGraphsTrain.py:37(<listcomp>)
               13236251    7.768    0.000 1461.090    0.000 game.py:37(board)
               10790440   52.729    0.000 1239.542    0.000 allGraphs.py:153(format)
                 489162    2.114    0.000 1127.259    0.002 agent.py:29(learn)
                 489162   11.410    0.000 1124.015    0.002 agent.py:117(_learn)
                 489162   33.483    0.000 1112.605    0.002 learner.py:42(Qlearn)
                 489162   41.997    0.000 1049.359    0.002 layers.py:17(step)
               48916200   81.204    0.000 1002.625    0.000 layer.py:98(move)
                1900821   16.890    0.000  890.709    0.000 layers.py:740(restart)
               51851172  129.692    0.000  867.558    0.000 tensor.py:21(wrapped)
                 489162   36.603    0.000  818.130    0.002 allGraphsTrain.py:44(<listcomp>)
                1900821    8.307    0.000  735.770    0.000 level.py:8(__init__)
                1900821   26.037    0.000  654.993    0.000 levels.py:288(generate)
             8567048298  651.403    0.000  651.403    0.000 {built-in method builtins.hash}
               11405508  108.813    0.000  601.105    0.000 level.py:41(notUsed)
               51362010  586.290    0.000  586.290    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               48916200  559.081    0.000  559.081    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                 489162  283.637    0.001  517.707    0.001 agent.py:67(modify)
               48916200  121.653    0.000  517.251    0.000 layers.py:735(check)
        11250726/1467486   48.417    0.000  451.458    0.000 module.py:715(_call_impl)
                 489162    3.468    0.000  432.228    0.001 grad_mode.py:23(decorate_context)
                 489162   15.607    0.000  422.251    0.001 adam.py:55(step)
                 978324    2.862    0.000  410.285    0.000 network.py:27(forward)
                 978324   11.156    0.000  400.477    0.000 container.py:115(forward)
                 489162   77.180    0.000  343.259    0.001 functional.py:53(adam)
               48916200   79.999    0.000  327.502    0.000 layers.py:729(isFree)
              135064774   78.800    0.000  282.230    0.000 {built-in method builtins.any}
               11405508    8.245    0.000  279.399    0.000 level.py:38(elementsIn)
                3913304  161.577    0.000  275.025    0.000 layer.py:167(NoRock_update)
                 489162    3.007    0.000  265.726    0.001 tensor.py:181(backward)
                 489162    2.174    0.000  262.719    0.001 __init__.py:68(backward)
                 489162  248.193    0.001  248.193    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
              359466979  201.770    0.000  247.503    0.000 layer.py:95(isFree)
                 489162    7.466    0.000  247.134    0.001 agent.py:112(__call__)
             1229336560  232.563    0.000  232.563    0.000 {built-in method builtins.max}
              100767472   36.531    0.000  229.809    0.000 {built-in method builtins.all}
             1227805113  223.475    0.000  223.475    0.000 {built-in method math.log}
                1467486    6.713    0.000  183.774    0.000 tensor.py:576(__iter__)
               11405508   92.335    0.000  183.076    0.000 level.py:39(<listcomp>)
              181816458   51.529    0.000  180.216    0.000 layers.py:690(<genexpr>)
               50872848  173.122    0.000  173.122    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                1467486  172.807    0.000  172.807    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
                1956648    3.928    0.000  160.958    0.000 conv.py:422(forward)
                1956648    4.559    0.000  155.435    0.000 conv.py:414(_conv_forward)
                1956648  150.123    0.000  150.123    0.000 {built-in method conv2d}
               85114322   46.996    0.000  147.043    0.000 overrides.py:1070(has_torch_function)
              423139311  118.670    0.000  145.983    0.000 layers.py:700(<genexpr>)
             1231718544  138.131    0.000  138.131    0.000 {built-in method math.sqrt}
               15206568   12.342    0.000  132.845    0.000 layer.py:69(restart)
              540999080  129.046    0.000  129.046    0.000 level.py:32(inverse)
                1956648    4.985    0.000  118.128    0.000 linear.py:92(forward)
               27393126   68.883    0.000  112.737    0.000 tensor.py:933(grad)
               24459061   68.327    0.000  112.532    0.000 layers.py:424(check)
                1956648    8.415    0.000  110.771    0.000 functional.py:1669(linear)
                1900921   50.047    0.000   99.962    0.000 layers.py:36(reset)
                 489162    9.156    0.000   96.315    0.000 optimizer.py:167(zero_grad)
              479029373   89.109    0.000   89.109    0.000 enum.py:352(<genexpr>)
               11405508   54.815    0.000   88.078    0.000 {built-in method _functools.reduce}
               48916300   55.900    0.000   87.929    0.000 layers.py:442(isDone)
                 489162    4.148    0.000   84.818    0.000 agent.py:59(modify_board)
                1956648   78.883    0.000   78.883    0.000 {built-in method addmm}
               24458815   48.617    0.000   76.628    0.000 layers.py:437(check)
                 489162   43.987    0.000   76.014    0.000 collector.py:46(collect)
              726671524   74.229    0.000   74.229    0.000 layer.py:91(positions)
               24453719   46.285    0.000   73.251    0.000 layers.py:452(check)
              239521662   69.389    0.000   69.389    0.000 layer.py:146(elements)
                7826592   69.087    0.000   69.087    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                1900821   35.784    0.000   67.366    0.000 level.py:16(<dictcomp>)
              116599377   47.089    0.000   64.370    0.000 layer.py:130(add)
                 489162   39.436    0.000   57.505    0.000 allGraphsTrain.py:43(<listcomp>)
              224036464   48.040    0.000   57.099    0.000 overrides.py:1083(<genexpr>)
                7826592   56.881    0.000   56.881    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                 489162   56.152    0.000   56.152    0.000 {built-in method torch._C._nn.one_hot}
                2934972    2.922    0.000   51.319    0.000 activation.py:713(forward)
                2934972    4.864    0.000   48.398    0.000 functional.py:1292(leaky_relu)
                 489162   11.581    0.000   44.128    0.000 allGraphs.py:137(transform)
                2934972   43.078    0.000   43.078    0.000 {built-in method torch._C._nn.leaky_relu}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9531988: <Diamonds3_0.5_UCB1_0> in cluster <dcc> Done

Job <Diamonds3_0.5_UCB1_0> was submitted from host <n-62-30-7> by user <s183905> in cluster <dcc> at Sat Apr 17 13:24:03 2021
Job was executed on host(s) <n-62-20-12>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sat Apr 17 23:19:32 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat Apr 17 23:19:32 2021
Terminated at Sun Apr 18 09:14:49 2021
Results reported at Sun Apr 18 09:14:49 2021

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

    CPU time :                                   35620.93 sec.
    Max Memory :                                 2063 MB
    Average Memory :                             2059.90 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14321.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35717 sec.
    Turnaround time :                            71446 sec.

The output (if any) is above this job summary.

