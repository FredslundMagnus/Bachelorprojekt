
# Parameters

    Name :                      causal5_online_var_0.5-0
    Main :                      graphTrain
    Level :                     Levels.Causal5
    Failed actions chance :     0.5
    Hours :                     12.0
    Batch :                     100
    Width :                     9
    Height :                    9
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
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                2
    Counterfacts :              1
    Topn :                      7
    Minutes used :              715 minutes.
    Hours used :                11 hours.

# Profiling


      53413634451 function calls (47026767536 primitive calls) in 42908.39 seconds

##    Ordered by: cumulative time
   List reduced from 465 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 42908.393 42908.393 {built-in method builtins.exec}
                      1    0.001    0.001 42908.393 42908.393 <string>:1(<module>)
                      1  108.260  108.260 42908.391 42908.391 allGraphsTrain.py:10(graphTrain)
                 432027 6294.551    0.015 14238.474    0.033 allGraphs.py:120(transformNot)
                 432027  504.328    0.001 12633.901    0.029 allGraphsTrain.py:35(<listcomp>)
                8378232   47.018    0.000 12129.573    0.001 allGraphs.py:127(getInterventions)
                7533919    6.225    0.000 11104.886    0.001 allGraphs.py:107(rightIntervention)
        1095244706/7533919  547.224    0.000 11062.980    0.001 {built-in method builtins.min}
               29477370   11.864    0.000 11047.593    0.000 allGraphs.py:108(<lambda>)
        2182955493/29477370 3215.134    0.000 11035.728    0.000 allGraphs.py:52(expected_moves)
        3241188910/104151828  864.981    0.000 10839.470    0.000 allGraphs.py:56(<genexpr>)
                 432027   11.151    0.000 9231.727    0.021 allGraphsTrain.py:29(<listcomp>)
               43634828 2367.491    0.000 9220.632    0.000 allGraphs.py:88(states)
              604841856 8086.789    0.000 8086.789    0.000 {method 'item' of 'torch._C._TensorBase' objects}
              561635700 7175.895    0.000 7175.895    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
             1096089019  566.121    0.000 3533.801    0.000 allGraphs.py:61(layers_not_in)
            16187826630 2295.653    0.000 3348.010    0.000 enum.py:646(__hash__)
             1096089019 1410.777    0.000 2967.680    0.000 allGraphs.py:62(<listcomp>)
                 432027    1.605    0.000 1946.016    0.005 game.py:41(step)
                 432027    1.966    0.000 1842.804    0.004 layers.py:712(step)
                 432027  112.480    0.000 1516.725    0.004 allGraphsTrain.py:37(<listcomp>)
             2182955493  993.346    0.000 1453.115    0.000 allGraphs.py:37(p)
               12385455 1284.770    0.000 1284.770    0.000 {built-in method tensor}
               10538368    6.257    0.000 1212.250    0.000 game.py:37(board)
                 432027    1.511    0.000 1124.268    0.003 agent.py:29(learn)
                 432027    8.736    0.000 1121.771    0.003 agent.py:117(_learn)
                 432027   33.199    0.000 1113.036    0.003 learner.py:42(Qlearn)
            16187828099 1052.357    0.000 1052.357    0.000 {built-in method builtins.hash}
                 432028   55.885    0.000 1023.543    0.002 layers.py:678(update)
               45794862  115.832    0.000  922.858    0.000 tensor.py:21(wrapped)
                 432027   39.890    0.000  885.303    0.002 allGraphsTrain.py:44(<listcomp>)
                 432027   29.530    0.000  815.065    0.002 layers.py:17(step)
               43202700   63.347    0.000  781.520    0.000 layer.py:98(move)
               45362835  682.752    0.000  682.752    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               43202700  620.986    0.000  620.986    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                1068207    9.005    0.000  478.946    0.000 layers.py:734(restart)
                 432027    2.353    0.000  469.672    0.001 grad_mode.py:23(decorate_context)
                 432027  259.607    0.001  467.578    0.001 agent.py:67(modify)
                 432027   12.196    0.000  462.733    0.001 adam.py:55(step)
               43202700  107.762    0.000  416.855    0.000 layers.py:729(check)
        9936621/1296081   38.330    0.000  405.662    0.000 module.py:715(_call_impl)
                 432027   84.188    0.000  398.334    0.001 functional.py:53(adam)
                1068207    4.328    0.000  397.856    0.000 level.py:8(__init__)
                 864054    2.091    0.000  371.535    0.000 network.py:24(forward)
                 864054    9.441    0.000  364.390    0.000 container.py:115(forward)
             2185095887  358.921    0.000  363.793    0.000 {built-in method builtins.max}
                1068207   14.770    0.000  361.570    0.000 levels.py:249(generate)
                6945079   58.763    0.000  330.809    0.000 level.py:41(notUsed)
                 432027    2.347    0.000  253.708    0.001 tensor.py:181(backward)
                 432027    1.361    0.000  251.361    0.001 __init__.py:68(backward)
               43202700   66.030    0.000  242.070    0.000 layers.py:723(isFree)
                 432027  239.322    0.001  239.322    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
              119899588   66.724    0.000  236.962    0.000 {built-in method builtins.any}
                 432027    5.223    0.000  215.615    0.000 agent.py:112(__call__)
               44930808  210.208    0.000  210.208    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                3888252  115.459    0.000  207.337    0.000 layer.py:167(NoRock_update)
              370515045  135.952    0.000  176.040    0.000 layer.py:95(isFree)
                6945079    4.524    0.000  153.558    0.000 level.py:38(elementsIn)
                1296081    5.279    0.000  144.091    0.000 tensor.py:576(__iter__)
                1728108    2.949    0.000  143.631    0.000 conv.py:422(forward)
                1728108    3.706    0.000  139.633    0.000 conv.py:414(_conv_forward)
               88997662   31.132    0.000  135.606    0.000 {built-in method builtins.all}
                1728108  135.355    0.000  135.355    0.000 {built-in method conv2d}
                1296081  135.353    0.000  135.353    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
              421345930  100.565    0.000  123.204    0.000 layers.py:694(<genexpr>)
               75172832   35.597    0.000  117.805    0.000 overrides.py:1070(has_torch_function)
                1728108    3.857    0.000  108.693    0.000 linear.py:92(forward)
                1728108    6.813    0.000  103.167    0.000 functional.py:1669(linear)
                6945079   49.144    0.000   98.668    0.000 level.py:39(<listcomp>)
               24193566   62.673    0.000   98.264    0.000 tensor.py:933(grad)
                 432027    8.991    0.000   95.238    0.000 optimizer.py:167(zero_grad)
              193826540   48.699    0.000   92.872    0.000 layers.py:684(<genexpr>)
                6912432   83.612    0.000   83.612    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                 432027   48.606    0.000   81.793    0.000 collector.py:46(collect)
                1728108   74.041    0.000   74.041    0.000 {built-in method addmm}
              327548348   72.112    0.000   72.112    0.000 level.py:32(inverse)
                 432027    3.148    0.000   71.630    0.000 agent.py:59(modify_board)
                6912432   70.927    0.000   70.927    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                9613863    6.698    0.000   69.093    0.000 layer.py:69(restart)
              603867151   58.191    0.000   58.191    0.000 layer.py:91(positions)
               21598040   34.735    0.000   56.847    0.000 layers.py:381(check)
               21597974   33.792    0.000   56.116    0.000 layers.py:369(check)
               21606437   33.973    0.000   56.007    0.000 layers.py:343(check)
               21602894   33.327    0.000   55.405    0.000 layers.py:331(check)
              168068980   52.438    0.000   52.438    0.000 layer.py:146(elements)
                1068307   25.698    0.000   51.459    0.000 layers.py:30(reset)
                2592162    2.217    0.000   51.454    0.000 activation.py:713(forward)
                6945079   31.346    0.000   50.365    0.000 {built-in method _functools.reduce}
                2592162    3.361    0.000   49.238    0.000 functional.py:1292(leaky_relu)
              288479858   48.104    0.000   48.104    0.000 enum.py:352(<genexpr>)
              197868634   39.317    0.000   46.776    0.000 overrides.py:1083(<genexpr>)
                2592162   45.535    0.000   45.535    0.000 {built-in method torch._C._nn.leaky_relu}
                 432027   45.429    0.000   45.429    0.000 {built-in method torch._C._nn.one_hot}
                3456216   45.284    0.000   45.284    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                 432027   29.436    0.000   44.370    0.000 allGraphsTrain.py:43(<listcomp>)
                3456216   41.127    0.000   41.127    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               80671752   29.819    0.000   40.419    0.000 layer.py:130(add)
                3456216   37.865    0.000   37.865    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                 432027    9.537    0.000   37.014    0.000 allGraphs.py:111(transform)
                3456216   34.300    0.000   34.300    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-4>
Subject: Job 9511307: <causal5_online_var_0.5_0> in cluster <dcc> Done

Job <causal5_online_var_0.5_0> was submitted from host <n-62-27-21> by user <s183905> in cluster <dcc> at Mon Apr 12 16:10:31 2021
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Mon Apr 12 16:27:56 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Apr 12 16:27:56 2021
Terminated at Tue Apr 13 04:23:11 2021
Results reported at Tue Apr 13 04:23:11 2021

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

    CPU time :                                   42798.63 sec.
    Max Memory :                                 2079 MB
    Average Memory :                             2078.41 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14305.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   42915 sec.
    Turnaround time :                            43960 sec.

The output (if any) is above this job summary.

