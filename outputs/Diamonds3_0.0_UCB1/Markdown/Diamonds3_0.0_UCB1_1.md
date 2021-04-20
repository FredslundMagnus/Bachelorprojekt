
# Parameters

    Name :                      Diamonds3_0.0_UCB1-1
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


      35326983202 function calls (32570743093 primitive calls) in 35708.31 seconds

##    Ordered by: cumulative time
   List reduced from 463 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35708.315 35708.315 {built-in method builtins.exec}
                      1    0.001    0.001 35708.315 35708.315 <string>:1(<module>)
                      1  132.224  132.224 35708.314 35708.314 allGraphsTrain.py:10(graphTrain)
                 563519 4821.065    0.009 11691.874    0.021 allGraphs.py:146(transformNot)
              676227804 7715.081    0.000 7715.081    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                 563519   13.690    0.000 7690.214    0.014 allGraphsTrain.py:29(<listcomp>)
               56915520 1746.532    0.000 7676.571    0.000 allGraphs.py:110(states)
                 563519  499.833    0.001 7294.823    0.013 allGraphsTrain.py:35(<listcomp>)
                8822494   12.055    0.000 6794.990    0.001 allGraphs.py:158(getInterventions)
                8822494    8.348    0.000 5842.473    0.001 allGraphs.py:133(UCB1)
        493357567/8822494  275.006    0.000 5795.300    0.001 {built-in method builtins.min}
               34011231   14.569    0.000 5778.334    0.000 allGraphs.py:134(<lambda>)
        977892640/34011231 1520.972    0.000 5763.765    0.000 allGraphs.py:68(expected_moves_UCB1)
              619871400 5618.443    0.000 5618.443    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
        1428416482/111863618  409.602    0.000 5505.264    0.000 allGraphs.py:72(<genexpr>)
                 563519    1.904    0.000 3823.738    0.007 game.py:41(step)
                 563519    2.702    0.000 3704.320    0.007 layers.py:718(step)
                 563520   81.005    0.000 2088.375    0.004 layers.py:684(update)
             7740239939 1256.872    0.000 1897.782    0.000 enum.py:646(__hash__)
              493357567  279.661    0.000 1616.392    0.000 allGraphs.py:83(layers_not_in)
                 563519   41.820    0.000 1610.144    0.003 layers.py:17(step)
               56351900   90.669    0.000 1562.587    0.000 layer.py:98(move)
                 563519   99.870    0.000 1547.457    0.003 allGraphsTrain.py:37(<listcomp>)
              977892640  838.428    0.000 1355.172    0.000 allGraphs.py:60(UCB1)
              493357567  633.089    0.000 1336.731    0.000 allGraphs.py:84(<listcomp>)
                2900346   22.966    0.000 1296.022    0.000 layers.py:740(restart)
               14039280 1269.913    0.000 1269.913    0.000 {built-in method tensor}
               11640090    7.120    0.000 1193.550    0.000 game.py:37(board)
                 563519    1.762    0.000 1190.336    0.002 agent.py:29(learn)
                 563519   11.373    0.000 1187.365    0.002 agent.py:117(_learn)
                 563519   34.445    0.000 1175.992    0.002 learner.py:42(Qlearn)
                2900346   11.178    0.000 1071.356    0.000 level.py:8(__init__)
               56351900  199.201    0.000 1027.452    0.000 layers.py:735(check)
                2900346   37.147    0.000  961.313    0.000 levels.py:288(generate)
               59733014  136.164    0.000  945.801    0.000 tensor.py:21(wrapped)
                8822494   40.292    0.000  940.461    0.000 allGraphs.py:153(format)
                 563519   41.523    0.000  897.687    0.002 allGraphsTrain.py:44(<listcomp>)
               17401757  157.160    0.000  883.267    0.000 level.py:41(notUsed)
             7740241824  640.910    0.000  640.910    0.000 {built-in method builtins.hash}
               59169495  638.133    0.000  638.133    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               56351900  610.665    0.000  610.665    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                 563519  313.364    0.001  552.390    0.001 agent.py:67(modify)
        12960937/1690557   49.143    0.000  469.003    0.000 module.py:715(_call_impl)
                 563519    3.253    0.000  466.458    0.001 grad_mode.py:23(decorate_context)
                 563519   15.846    0.000  456.983    0.001 adam.py:55(step)
                1127038    2.969    0.000  428.339    0.000 network.py:27(forward)
                1127038   12.012    0.000  418.609    0.000 container.py:115(forward)
               17401757   11.846    0.000  414.673    0.000 level.py:38(elementsIn)
                 563519   82.678    0.000  370.881    0.001 functional.py:53(adam)
               56351900  104.386    0.000  357.126    0.000 layers.py:729(isFree)
              154885209   88.181    0.000  312.790    0.000 {built-in method builtins.any}
                4508160  181.620    0.000  311.907    0.000 layer.py:167(NoRock_update)
               17401757  130.613    0.000  274.490    0.000 level.py:39(<listcomp>)
                 563519    3.037    0.000  272.775    0.000 tensor.py:181(backward)
                 563519    1.993    0.000  269.737    0.000 __init__.py:68(backward)
                 563519  255.580    0.000  255.580    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
              442060864  197.395    0.000  252.739    0.000 layer.py:95(isFree)
                 563519    6.569    0.000  250.796    0.000 agent.py:112(__call__)
               56351900  147.621    0.000  245.055    0.000 layers.py:424(check)
              116085014   39.861    0.000  217.374    0.000 {built-in method builtins.all}
               23202768   17.242    0.000  193.692    0.000 layer.py:69(restart)
                1690557    6.653    0.000  188.818    0.000 tensor.py:576(__iter__)
               58605976  188.280    0.000  188.280    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              825424466  187.507    0.000  187.507    0.000 level.py:32(inverse)
              977817078  177.933    0.000  177.933    0.000 {built-in method math.log}
                1690557  177.860    0.000  177.860    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
              979583197  175.239    0.000  175.239    0.000 {built-in method builtins.max}
                2254076    4.218    0.000  166.629    0.000 conv.py:422(forward)
               56351900  100.707    0.000  166.110    0.000 layers.py:452(check)
               98052440   49.038    0.000  165.473    0.000 overrides.py:1070(has_torch_function)
              188071173   49.676    0.000  161.390    0.000 layers.py:690(<genexpr>)
                2254076    4.457    0.000  160.888    0.000 conv.py:414(_conv_forward)
               56351900   95.128    0.000  156.233    0.000 layers.py:437(check)
              481064886  125.889    0.000  155.822    0.000 layers.py:700(<genexpr>)
                2254076  155.636    0.000  155.636    0.000 {built-in method conv2d}
                2900446   72.987    0.000  149.058    0.000 layers.py:36(reset)
             1302860356  132.380    0.000  132.380    0.000 layer.py:91(positions)
              730877237  128.403    0.000  128.403    0.000 enum.py:352(<genexpr>)
               17401757   80.136    0.000  128.336    0.000 {built-in method _functools.reduce}
               31557118   74.960    0.000  124.631    0.000 tensor.py:933(grad)
                2254076    5.368    0.000  122.787    0.000 linear.py:92(forward)
                2254076    9.395    0.000  115.065    0.000 functional.py:1669(linear)
                 563519    9.675    0.000  105.769    0.000 optimizer.py:167(zero_grad)
              982325365   98.835    0.000   98.835    0.000 {built-in method math.sqrt}
               56352000   62.478    0.000   97.187    0.000 layers.py:113(isDone)
                2900346   44.664    0.000   90.822    0.000 level.py:16(<dictcomp>)
              164379345   63.007    0.000   87.947    0.000 layer.py:130(add)
                 563519    4.128    0.000   84.827    0.000 agent.py:59(modify_board)
                 563519   46.872    0.000   81.121    0.000 collector.py:46(collect)
                2254076   80.953    0.000   80.953    0.000 {built-in method addmm}
              334885703   79.823    0.000   79.823    0.000 layer.py:146(elements)
               56351900   50.382    0.000   78.237    0.000 layers.py:413(check)
                9016304   74.540    0.000   74.540    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               56351900   47.480    0.000   74.466    0.000 layers.py:402(check)
              258091970   57.152    0.000   68.418    0.000 overrides.py:1083(<genexpr>)
                 563519   41.087    0.000   62.009    0.000 allGraphsTrain.py:43(<listcomp>)
                9016304   61.751    0.000   61.751    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               56351900   40.160    0.000   61.009    0.000 layers.py:23(check)
                 563519   55.795    0.000   55.795    0.000 {built-in method torch._C._nn.one_hot}
                3381114    2.983    0.000   55.275    0.000 activation.py:713(forward)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9532028: <Diamonds3_0.0_UCB1_1> in cluster <dcc> Done

Job <Diamonds3_0.0_UCB1_1> was submitted from host <n-62-30-7> by user <s183905> in cluster <dcc> at Sat Apr 17 13:28:43 2021
Job was executed on host(s) <n-62-20-3>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Mon Apr 19 15:48:53 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Apr 19 15:48:53 2021
Terminated at Tue Apr 20 01:44:07 2021
Results reported at Tue Apr 20 01:44:07 2021

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

    CPU time :                                   35619.75 sec.
    Max Memory :                                 2062 MB
    Average Memory :                             2061.33 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14322.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35714 sec.
    Turnaround time :                            216924 sec.

The output (if any) is above this job summary.

