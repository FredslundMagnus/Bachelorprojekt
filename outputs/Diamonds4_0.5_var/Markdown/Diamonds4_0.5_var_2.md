
# Parameters

    Name :                      Diamonds4_0.5_var-2
    Main :                      graphTrain
    Level :                     Levels.Causal7
    Failed actions chance :     0.5
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
    Counterfacts :              2
    Topn :                      5
    Random counterfacts :       False
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      19090255791 function calls (18444940130 primitive calls) in 35703.98 seconds

##    Ordered by: cumulative time
   List reduced from 466 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35703.985 35703.985 {built-in method builtins.exec}
                      1    0.001    0.001 35703.985 35703.985 <string>:1(<module>)
                      1  176.430  176.430 35703.984 35703.984 allGraphsTrain.py:10(graphTrain)
                 735817 5603.170    0.008 13311.037    0.018 allGraphs.py:146(transformNot)
              735823280 8550.335    0.000 8550.335    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                 735817   19.286    0.000 8413.587    0.011 allGraphsTrain.py:29(<listcomp>)
               74317618 1998.350    0.000 8394.318    0.000 allGraphs.py:110(states)
              662235700 6245.078    0.000 6245.078    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 735817  714.052    0.001 3758.016    0.005 allGraphsTrain.py:35(<listcomp>)
                 735817    2.499    0.000 3312.723    0.005 game.py:41(step)
                 735817    3.402    0.000 3163.800    0.004 layers.py:718(step)
               16984080   28.553    0.000 3043.964    0.000 allGraphs.py:158(getInterventions)
                 735817  137.214    0.000 2085.544    0.003 allGraphsTrain.py:37(<listcomp>)
               23786766 1936.193    0.000 1936.193    0.000 {built-in method tensor}
                 735818  104.527    0.000 1839.729    0.003 layers.py:684(update)
               20663166   10.802    0.000 1839.232    0.000 game.py:37(board)
                 735817    2.466    0.000 1587.157    0.002 agent.py:29(learn)
                 735817   15.034    0.000 1583.149    0.002 agent.py:117(_learn)
               16984080   69.586    0.000 1568.751    0.000 allGraphs.py:153(format)
                 735817   46.592    0.000 1568.115    0.002 learner.py:42(Qlearn)
               15902589   15.037    0.000 1430.869    0.000 allGraphs.py:129(rightIntervention)
        143333010/15902589  104.050    0.000 1354.369    0.000 {built-in method builtins.min}
               40209136   19.305    0.000 1327.648    0.000 allGraphs.py:130(<lambda>)
                 735817   59.473    0.000 1316.408    0.002 layers.py:17(step)
        270763431/40209136  410.521    0.000 1308.344    0.000 allGraphs.py:74(expected_moves)
               77996602  179.259    0.000 1280.849    0.000 tensor.py:21(wrapped)
               73581700  120.539    0.000 1250.104    0.000 layer.py:98(move)
                 735817   60.003    0.000 1219.468    0.002 allGraphsTrain.py:44(<listcomp>)
        357984716/85370494  114.767    0.000 1078.094    0.000 allGraphs.py:78(<genexpr>)
                2342811   19.159    0.000  901.471    0.000 layers.py:740(restart)
               77260785  879.489    0.000  879.489    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               73581700  827.820    0.000  827.820    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                2342811    9.515    0.000  724.995    0.000 level.py:8(__init__)
                 735817  388.321    0.001  710.083    0.001 agent.py:67(modify)
             2679200431  455.539    0.000  665.953    0.000 enum.py:646(__hash__)
                2342811   26.828    0.000  627.332    0.000 levels.py:441(generate)
        16923791/2207451   67.090    0.000  626.187    0.000 module.py:715(_call_impl)
                 735817    4.331    0.000  623.444    0.001 grad_mode.py:23(decorate_context)
               73581700  157.779    0.000  613.333    0.000 layers.py:735(check)
                 735817   21.872    0.000  610.559    0.001 adam.py:55(step)
               11246265  104.035    0.000  572.391    0.000 level.py:41(notUsed)
                1471634    4.281    0.000  571.725    0.000 network.py:27(forward)
                1471634   15.171    0.000  557.760    0.000 container.py:115(forward)
                 735817  111.559    0.000  499.440    0.001 functional.py:53(adam)
              144414501   89.228    0.000  423.270    0.000 allGraphs.py:83(layers_not_in)
               73581700  108.356    0.000  407.191    0.000 layers.py:729(isFree)
              203686184  111.849    0.000  376.183    0.000 {built-in method builtins.any}
                 735817    4.063    0.000  363.293    0.000 tensor.py:181(backward)
                 735817    2.668    0.000  359.230    0.000 __init__.py:68(backward)
                 735817  340.083    0.000  340.083    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                5150726  193.071    0.000  334.969    0.000 layer.py:167(NoRock_update)
                 735817    9.120    0.000  334.131    0.000 agent.py:112(__call__)
              144414501  164.172    0.000  334.042    0.000 allGraphs.py:84(<listcomp>)
              484916065  236.981    0.000  298.835    0.000 layer.py:95(isFree)
              151578402   64.007    0.000  287.974    0.000 {built-in method builtins.all}
               11246265    8.695    0.000  268.935    0.000 level.py:38(elementsIn)
               76524968  253.956    0.000  253.956    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                2207451    8.643    0.000  253.557    0.000 tensor.py:576(__iter__)
                2207451  239.363    0.000  239.363    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
                2943268    4.970    0.000  222.488    0.000 conv.py:422(forward)
                2943268    6.366    0.000  215.502    0.000 conv.py:414(_conv_forward)
              128032292   66.195    0.000  214.662    0.000 overrides.py:1070(has_torch_function)
             2679202860  210.414    0.000  210.414    0.000 {built-in method builtins.hash}
                2943268  208.055    0.000  208.055    0.000 {built-in method conv2d}
              338697746   93.134    0.000  204.027    0.000 layers.py:690(<genexpr>)
              270763431  138.985    0.000  203.433    0.000 allGraphs.py:45(p)
              569911912  146.970    0.000  179.500    0.000 layers.py:700(<genexpr>)
               11246265   88.400    0.000  176.448    0.000 level.py:39(<listcomp>)
                2943268    6.837    0.000  164.463    0.000 linear.py:92(forward)
               41205806   94.951    0.000  158.623    0.000 tensor.py:933(grad)
                2943268   12.071    0.000  154.559    0.000 functional.py:1669(linear)
               16399677   13.056    0.000  151.630    0.000 layer.py:69(restart)
                 735817   14.190    0.000  138.835    0.000 optimizer.py:167(zero_grad)
                2342911   59.544    0.000  119.654    0.000 layers.py:36(reset)
              539959215  116.977    0.000  116.977    0.000 level.py:32(inverse)
                 735817    5.692    0.000  113.763    0.000 agent.py:59(modify_board)
                 735817   63.742    0.000  109.623    0.000 collector.py:46(collect)
                2943268  109.335    0.000  109.335    0.000 {built-in method addmm}
               36787749   66.274    0.000  108.446    0.000 layers.py:632(check)
               36789566   65.307    0.000  105.785    0.000 layers.py:617(check)
               36787519   63.686    0.000  104.545    0.000 layers.py:602(check)
               11773072  100.280    0.000  100.280    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
             1011055822   96.143    0.000   96.143    0.000 layer.py:91(positions)
              489208229   89.787    0.000   89.787    0.000 enum.py:352(<genexpr>)
              315977027   84.533    0.000   84.533    0.000 layer.py:146(elements)
              337004454   71.176    0.000   84.343    0.000 overrides.py:1083(<genexpr>)
               11246265   52.427    0.000   83.792    0.000 {built-in method _functools.reduce}
               11773072   83.617    0.000   83.617    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                2342811   45.015    0.000   82.385    0.000 level.py:16(<dictcomp>)
              153769950   59.189    0.000   81.311    0.000 layer.py:130(add)
                 735817   52.934    0.000   78.465    0.000 allGraphsTrain.py:43(<listcomp>)
                 735817   74.419    0.000   74.419    0.000 {built-in method torch._C._nn.one_hot}
                4414902    3.914    0.000   73.644    0.000 activation.py:713(forward)
                4414902    6.695    0.000   69.730    0.000 functional.py:1292(leaky_relu)
                4414902   62.408    0.000   62.408    0.000 {built-in method torch._C._nn.leaky_relu}
              274052373   55.617    0.000   60.487    0.000 {built-in method builtins.max}
                 735817   16.060    0.000   58.959    0.000 allGraphs.py:137(transform)
                5886536   58.796    0.000   58.796    0.000 {method 'add' of 'torch._C._TensorBase' objects}
        627308871/627308869   41.629    0.000   54.023    0.000 {built-in method builtins.len}
                5886536   53.832    0.000   53.832    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9532020: <Diamonds4_0.5_var_2> in cluster <dcc> Done

Job <Diamonds4_0.5_var_2> was submitted from host <n-62-30-7> by user <s183905> in cluster <dcc> at Sat Apr 17 13:28:42 2021
Job was executed on host(s) <n-62-11-16>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sun Apr 18 21:26:23 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun Apr 18 21:26:23 2021
Terminated at Mon Apr 19 07:21:30 2021
Results reported at Mon Apr 19 07:21:30 2021

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

    CPU time :                                   35619.12 sec.
    Max Memory :                                 2063 MB
    Average Memory :                             2062.83 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14321.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35707 sec.
    Turnaround time :                            150768 sec.

The output (if any) is above this job summary.

