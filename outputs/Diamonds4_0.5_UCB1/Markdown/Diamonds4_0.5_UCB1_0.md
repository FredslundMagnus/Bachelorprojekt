
# Parameters

    Name :                      Diamonds4_0.5_UCB1-0
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


      19962321930 function calls (19268687045 primitive calls) in 35704.01 seconds

##    Ordered by: cumulative time
   List reduced from 464 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35704.010 35704.010 {built-in method builtins.exec}
                      1    0.001    0.001 35704.010 35704.010 <string>:1(<module>)
                      1  170.626  170.626 35704.009 35704.009 allGraphsTrain.py:10(graphTrain)
                 735046 5581.568    0.008 13234.392    0.018 allGraphs.py:146(transformNot)
              735052280 8459.752    0.000 8459.752    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                 735046   18.901    0.000 8341.120    0.011 allGraphsTrain.py:29(<listcomp>)
               74239747 1958.336    0.000 8322.240    0.000 allGraphs.py:110(states)
              661541800 6244.469    0.000 6244.469    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 735046  709.103    0.001 4042.734    0.005 allGraphsTrain.py:35(<listcomp>)
               17104477   22.988    0.000 3333.631    0.000 allGraphs.py:158(getInterventions)
                 735046    2.639    0.000 3224.804    0.004 game.py:41(step)
                 735046    3.396    0.000 3078.046    0.004 layers.py:718(step)
                 735046  135.461    0.000 2072.724    0.003 allGraphsTrain.py:37(<listcomp>)
               23900199 1934.671    0.000 1934.671    0.000 {built-in method tensor}
               20779708   10.816    0.000 1839.960    0.000 game.py:37(board)
                 735047  103.246    0.000 1805.185    0.002 layers.py:684(update)
               17104477   16.049    0.000 1735.320    0.000 allGraphs.py:133(UCB1)
        154287700/17104477  115.066    0.000 1651.684    0.000 {built-in method builtins.min}
               43256266   20.732    0.000 1622.748    0.000 allGraphs.py:134(<lambda>)
        291470923/43256266  439.087    0.000 1602.016    0.000 allGraphs.py:68(expected_moves_UCB1)
                 735046    2.310    0.000 1597.901    0.002 agent.py:29(learn)
                 735046   15.134    0.000 1594.105    0.002 agent.py:117(_learn)
                 735046   45.980    0.000 1578.971    0.002 learner.py:42(Qlearn)
               17104477   71.476    0.000 1575.323    0.000 allGraphs.py:153(format)
        385397880/91862178  124.255    0.000 1316.235    0.000 allGraphs.py:72(<genexpr>)
               77914876  175.731    0.000 1267.653    0.000 tensor.py:21(wrapped)
                 735046   54.648    0.000 1265.574    0.002 layers.py:17(step)
                 735046   58.086    0.000 1207.246    0.002 allGraphsTrain.py:44(<listcomp>)
               73504600  116.352    0.000 1204.369    0.000 layer.py:98(move)
                2350149   18.444    0.000  886.832    0.000 layers.py:740(restart)
               77179830  876.146    0.000  876.146    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               73504600  824.630    0.000  824.630    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                2350149    8.974    0.000  712.402    0.000 level.py:8(__init__)
                 735046  386.320    0.001  702.212    0.001 agent.py:67(modify)
             2782402186  469.672    0.000  682.578    0.000 enum.py:646(__hash__)
                 735046    4.135    0.000  632.782    0.001 grad_mode.py:23(decorate_context)
                 735046   21.925    0.000  620.698    0.001 adam.py:55(step)
                2350149   26.270    0.000  619.878    0.000 levels.py:441(generate)
        16906058/2205138   63.846    0.000  612.773    0.000 module.py:715(_call_impl)
               73504600  155.751    0.000  602.377    0.000 layers.py:735(check)
               11283788  103.204    0.000  566.089    0.000 level.py:41(notUsed)
                1470092    3.743    0.000  559.813    0.000 network.py:27(forward)
                1470092   15.003    0.000  546.944    0.000 container.py:115(forward)
                 735046  113.030    0.000  510.550    0.001 functional.py:53(adam)
              154287700   95.961    0.000  450.442    0.000 allGraphs.py:83(layers_not_in)
              291470923  258.324    0.000  413.392    0.000 allGraphs.py:60(UCB1)
               73504600  100.083    0.000  377.119    0.000 layers.py:729(isFree)
                 735046    4.505    0.000  371.472    0.001 tensor.py:181(backward)
              203462966  110.047    0.000  369.342    0.000 {built-in method builtins.any}
                 735046    2.466    0.000  366.967    0.000 __init__.py:68(backward)
              154287700  175.069    0.000  354.482    0.000 allGraphs.py:84(<listcomp>)
                 735046  348.620    0.000  348.620    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                5145329  188.462    0.000  326.266    0.000 layer.py:167(NoRock_update)
                 735046    8.751    0.000  324.799    0.000 agent.py:112(__call__)
              151419576   61.099    0.000  280.837    0.000 {built-in method builtins.all}
              485593925  214.601    0.000  277.036    0.000 layer.py:95(isFree)
               11283788    8.757    0.000  263.643    0.000 level.py:38(elementsIn)
               76444784  256.053    0.000  256.053    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                2205138    8.454    0.000  249.252    0.000 tensor.py:576(__iter__)
                2205138  235.373    0.000  235.373    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
                2940184    4.998    0.000  219.476    0.000 conv.py:422(forward)
             2782404615  212.907    0.000  212.907    0.000 {built-in method builtins.hash}
                2940184    5.521    0.000  212.635    0.000 conv.py:414(_conv_forward)
              127898138   63.732    0.000  209.175    0.000 overrides.py:1070(has_torch_function)
                2940184  206.084    0.000  206.084    0.000 {built-in method conv2d}
              329294597   90.777    0.000  200.685    0.000 layers.py:690(<genexpr>)
              569236408  142.938    0.000  176.086    0.000 layers.py:700(<genexpr>)
               11283788   83.594    0.000  170.141    0.000 level.py:39(<listcomp>)
                2940184    6.847    0.000  160.891    0.000 linear.py:92(forward)
               41162630   94.755    0.000  157.173    0.000 tensor.py:933(grad)
                2940184   11.582    0.000  151.092    0.000 functional.py:1669(linear)
               16451043   12.558    0.000  150.326    0.000 layer.py:69(restart)
                 735046   13.757    0.000  137.960    0.000 optimizer.py:167(zero_grad)
                2350249   59.241    0.000  119.319    0.000 layers.py:36(reset)
              541756181  118.243    0.000  118.243    0.000 level.py:32(inverse)
                 735046    5.623    0.000  111.948    0.000 agent.py:59(modify_board)
                 735046   63.568    0.000  108.883    0.000 collector.py:46(collect)
                2940184  107.353    0.000  107.353    0.000 {built-in method addmm}
               36762544   64.761    0.000  105.916    0.000 layers.py:617(check)
               36754784   63.319    0.000  104.600    0.000 layers.py:632(check)
               36749959   61.634    0.000  101.656    0.000 layers.py:602(check)
               11760736  101.628    0.000  101.628    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
             1006825070   94.049    0.000   94.049    0.000 layer.py:91(positions)
              490823225   87.924    0.000   87.924    0.000 enum.py:352(<genexpr>)
               11760736   84.762    0.000   84.762    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               11283788   52.897    0.000   84.746    0.000 {built-in method _functools.reduce}
              336651336   69.585    0.000   82.725    0.000 overrides.py:1083(<genexpr>)
              316828087   82.468    0.000   82.468    0.000 layer.py:146(elements)
              154208701   59.140    0.000   80.875    0.000 layer.py:130(add)
                2350149   41.272    0.000   77.770    0.000 level.py:16(<dictcomp>)
                 735046   51.538    0.000   77.509    0.000 allGraphsTrain.py:43(<listcomp>)
                 735046   73.133    0.000   73.133    0.000 {built-in method torch._C._nn.one_hot}
                4410276    3.753    0.000   72.264    0.000 activation.py:713(forward)
                4410276    6.021    0.000   68.511    0.000 functional.py:1292(leaky_relu)
                5880368   64.318    0.000   64.318    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                4410276   61.896    0.000   61.896    0.000 {built-in method torch._C._nn.leaky_relu}
              293676061   58.237    0.000   58.237    0.000 {built-in method builtins.max}
                 735046   15.695    0.000   57.630    0.000 allGraphs.py:137(transform)
              291464969   54.938    0.000   54.938    0.000 {built-in method math.log}
                5880368   54.467    0.000   54.467    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}


Traceback (most recent call last):
  File "main.py", line 227, in <module>
    run(Defaults)
  File "/zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/auxillaries.py", line 132, in run
    (serverRun if isServer else Defaults.main).__call__(getvals(Defaults))
  File "/zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils/server.py", line 37, in serverRun
    profilingStats()
  File "/zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils/debug.py", line 62, in profilingStats
    os.remove('stats')
FileNotFoundError: [Errno 2] No such file or directory: 'stats'

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9531991: <Diamonds4_0.5_UCB1_0> in cluster <dcc> Exited

Job <Diamonds4_0.5_UCB1_0> was submitted from host <n-62-30-7> by user <s183905> in cluster <dcc> at Sat Apr 17 13:24:04 2021
Job was executed on host(s) <n-62-11-13>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sat Apr 17 23:54:07 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat Apr 17 23:54:07 2021
Terminated at Sun Apr 18 09:49:15 2021
Results reported at Sun Apr 18 09:49:15 2021

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

Exited with exit code 1.

Resource usage summary:

    CPU time :                                   35640.37 sec.
    Max Memory :                                 2057 MB
    Average Memory :                             2042.04 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14327.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35707 sec.
    Turnaround time :                            73511 sec.

The output (if any) is above this job summary.

