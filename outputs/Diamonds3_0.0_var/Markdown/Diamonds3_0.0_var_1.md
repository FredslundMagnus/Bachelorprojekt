
# Parameters

    Name :                      Diamonds3_0.0_var-1
    Main :                      graphTrain
    Level :                     Levels.Causal6
    Failed actions chance :     0.0
    Hours :                     10.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.var
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
    Counterfacts :              1
    Topn :                      6
    Random counterfacts :       False
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      28681176907 function calls (26420258630 primitive calls) in 35708.97 seconds

##    Ordered by: cumulative time
   List reduced from 465 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35708.965 35708.965 {built-in method builtins.exec}
                      1    0.001    0.001 35708.965 35708.965 <string>:1(<module>)
                      1  213.886  213.886 35708.964 35708.964 allGraphsTrain.py:10(graphTrain)
                 521717 4857.892    0.009 12070.629    0.023 allGraphs.py:146(transformNot)
              626065068 8468.847    0.000 8468.847    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                 521717   16.871    0.000 7982.645    0.015 allGraphsTrain.py:29(<listcomp>)
               52693518 1727.454    0.000 7965.828    0.000 allGraphs.py:110(states)
                 521717  579.709    0.001 5856.986    0.011 allGraphsTrain.py:35(<listcomp>)
              573889200 5559.933    0.000 5559.933    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                8033209   15.883    0.000 5277.277    0.001 allGraphs.py:158(getInterventions)
                7263125    7.505    0.000 4298.797    0.001 allGraphs.py:129(rightIntervention)
        404560644/7263125  230.469    0.000 4256.676    0.001 {built-in method builtins.min}
               27950500   13.129    0.000 4240.771    0.000 allGraphs.py:130(<lambda>)
        801858163/27950500 1253.146    0.000 4227.641    0.000 allGraphs.py:74(expected_moves)
        1171205182/91926810  351.308    0.000 4034.037    0.000 allGraphs.py:78(<genexpr>)
                 521717    3.419    0.000 3867.816    0.007 game.py:41(step)
                 521717    4.604    0.000 3704.696    0.007 layers.py:718(step)
                 521718   88.461    0.000 2015.518    0.004 layers.py:684(update)
                 521717   52.608    0.000 1678.448    0.003 layers.py:17(step)
               52171700   93.859    0.000 1620.723    0.000 layer.py:98(move)
                 521717  104.839    0.000 1618.110    0.003 allGraphsTrain.py:37(<listcomp>)
             6503903057 1083.501    0.000 1562.466    0.000 enum.py:646(__hash__)
                 521717    3.111    0.000 1390.493    0.003 agent.py:29(learn)
                 521717   18.761    0.000 1385.599    0.003 agent.py:117(_learn)
                 521717   43.905    0.000 1366.838    0.003 learner.py:42(Qlearn)
               12865963 1359.889    0.000 1359.889    0.000 {built-in method tensor}
              405330728  227.759    0.000 1311.422    0.000 allGraphs.py:83(layers_not_in)
               10641795    9.195    0.000 1261.968    0.000 game.py:37(board)
                2517529   25.230    0.000 1209.133    0.000 layers.py:740(restart)
              405330728  520.610    0.000 1083.663    0.000 allGraphs.py:84(<listcomp>)
               52171700  191.208    0.000  994.292    0.000 layers.py:735(check)
                2517529   11.893    0.000  990.784    0.000 level.py:8(__init__)
               55302002  133.057    0.000  956.006    0.000 tensor.py:21(wrapped)
                8033209   43.609    0.000  948.423    0.000 allGraphs.py:153(format)
                 521717   44.039    0.000  893.819    0.002 allGraphsTrain.py:44(<listcomp>)
                2517529   35.214    0.000  873.326    0.000 levels.py:288(generate)
               15103066  146.769    0.000  800.813    0.000 level.py:41(notUsed)
                 521717  355.744    0.001  667.015    0.001 agent.py:67(modify)
               54780285  656.311    0.000  656.311    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
        11999491/1565151   65.819    0.000  622.935    0.000 module.py:715(_call_impl)
              801858163  430.141    0.000  620.290    0.000 allGraphs.py:45(p)
               52171700  609.622    0.000  609.622    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                1043434    4.258    0.000  562.388    0.001 network.py:27(forward)
                1043434   14.694    0.000  548.503    0.001 container.py:115(forward)
                 521717    5.135    0.000  490.792    0.001 grad_mode.py:23(decorate_context)
             6503904814  478.965    0.000  478.965    0.000 {built-in method builtins.hash}
                 521717   19.693    0.000  475.734    0.001 adam.py:55(step)
               52171700   92.064    0.000  433.424    0.000 layers.py:729(isFree)
                 521717   87.572    0.000  388.118    0.001 functional.py:53(adam)
               15103066   11.671    0.000  368.775    0.000 level.py:38(elementsIn)
                4173744  206.833    0.000  350.207    0.000 layer.py:167(NoRock_update)
                 521717   13.406    0.000  346.324    0.001 agent.py:112(__call__)
                 521717    3.998    0.000  341.637    0.001 tensor.py:181(backward)
              412940964  285.609    0.000  341.360    0.000 layer.py:95(isFree)
                 521717    3.387    0.000  337.638    0.001 __init__.py:68(backward)
                 521717  317.523    0.001  317.523    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
              143563466   85.831    0.000  298.737    0.000 {built-in method builtins.any}
                1565151   11.447    0.000  257.585    0.000 tensor.py:576(__iter__)
               15103066  116.652    0.000  238.176    0.000 level.py:39(<listcomp>)
                1565151  238.145    0.000  238.145    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
                2086868    5.054    0.000  232.677    0.000 conv.py:422(forward)
               52171700  141.930    0.000  232.386    0.000 layers.py:424(check)
                2086868    6.928    0.000  225.459    0.000 conv.py:414(_conv_forward)
                2086868  217.610    0.000  217.610    0.000 {built-in method conv2d}
              107473802   32.683    0.000  189.063    0.000 {built-in method builtins.all}
               54258568  187.847    0.000  187.847    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               20140232   17.556    0.000  186.071    0.000 layer.py:69(restart)
              716393888  173.571    0.000  173.571    0.000 level.py:32(inverse)
               52171700  109.246    0.000  168.463    0.000 layers.py:437(check)
                2086868    6.338    0.000  161.191    0.000 linear.py:92(forward)
               90778892   48.302    0.000  158.263    0.000 overrides.py:1070(has_torch_function)
               52171700   99.047    0.000  156.382    0.000 layers.py:452(check)
                2086868   11.582    0.000  151.759    0.000 functional.py:1669(linear)
              804193398  143.780    0.000  149.557    0.000 {built-in method builtins.max}
              446888439  120.811    0.000  149.210    0.000 layers.py:700(<genexpr>)
              121865136   31.062    0.000  141.771    0.000 layers.py:690(<genexpr>)
                2517629   67.496    0.000  134.042    0.000 layers.py:36(reset)
             1205451621  124.618    0.000  124.618    0.000 layer.py:91(positions)
                 521717    6.792    0.000  122.816    0.000 agent.py:59(modify_board)
               15103066   74.110    0.000  118.928    0.000 {built-in method _functools.reduce}
              634342949  118.844    0.000  118.844    0.000 enum.py:352(<genexpr>)
               29216206   71.165    0.000  117.494    0.000 tensor.py:933(grad)
                2086868  110.240    0.000  110.240    0.000 {built-in method addmm}
                 521717    9.986    0.000  102.669    0.000 optimizer.py:167(zero_grad)
               52171800   69.352    0.000  101.153    0.000 layers.py:113(isDone)
                2517529   55.319    0.000   98.303    0.000 level.py:16(<dictcomp>)
                 521717   53.644    0.000   93.868    0.000 collector.py:46(collect)
              297086698   92.493    0.000   92.493    0.000 layer.py:146(elements)
              145622576   61.780    0.000   87.342    0.000 layer.py:130(add)
                 521717   80.152    0.000   80.152    0.000 {built-in method torch._C._nn.one_hot}
                8347472   77.250    0.000   77.250    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               52171700   50.512    0.000   75.738    0.000 layers.py:413(check)
                 521717   53.366    0.000   73.105    0.000 allGraphsTrain.py:43(<listcomp>)
                 521717   17.786    0.000   70.479    0.000 allGraphs.py:137(transform)
               52171700   44.495    0.000   68.974    0.000 layers.py:402(check)
                3130302    4.653    0.000   66.646    0.000 activation.py:713(forward)
              238946654   53.121    0.000   63.261    0.000 overrides.py:1083(<genexpr>)
                8347472   62.359    0.000   62.359    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                3130302    7.617    0.000   61.992    0.000 functional.py:1292(leaky_relu)
                1565151   58.475    0.000   58.475    0.000 {method 'tolist' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9532041: <Diamonds3_0.0_var_1> in cluster <dcc> Done

Job <Diamonds3_0.0_var_1> was submitted from host <n-62-30-7> by user <s183905> in cluster <dcc> at Sat Apr 17 13:28:45 2021
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Tue Apr 20 17:10:11 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue Apr 20 17:10:11 2021
Terminated at Wed Apr 21 03:05:25 2021
Results reported at Wed Apr 21 03:05:25 2021

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

    CPU time :                                   35620.89 sec.
    Max Memory :                                 2058 MB
    Average Memory :                             2056.98 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14326.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35714 sec.
    Turnaround time :                            308200 sec.

The output (if any) is above this job summary.

