/zhome/ee/d/137643/Desktop/Bachelor/project-env/lib/python3.8/site-packages/torch/cuda/__init__.py:52: UserWarning: CUDA initialization: Found no NVIDIA driver on your system. Please check that you have an NVIDIA GPU and installed a driver from http://www.nvidia.com/Download/index.aspx (Triggered internally at  /pytorch/c10/cuda/CUDAFunctions.cpp:100.)
  return torch._C._cuda_getDeviceCount() > 0

# Parameters

    Name :                      Diamonds4_0.5_NN_cpu-1
    Main :                      graphTrain
    Level :                     Levels.Causal7
    Failed actions chance :     0.5
    Use model :                 True
    Depth :                     3
    Model explore :             100000
    Samples :                   5
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
    Layer super1 :              True
    Layer super2 :              True
    Layer super3 :              True
    Layer super4 :              True
    Layer super5 :              True
    Layer super6 :              True
    Layer super7 :              True
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
    Num :                       1
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      12082021277 function calls (11561407578 primitive calls) in 35700.76 seconds

##    Ordered by: cumulative time
   List reduced from 443 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35700.762 35700.762 {built-in method builtins.exec}
                      1    0.001    0.001 35700.761 35700.761 <string>:1(<module>)
                      1   29.591   29.591 35700.760 35700.760 allGraphsTrain.py:13(graphTrain)
                 113152   24.126    0.000 26957.904    0.238 allGraphsTrain.py:40(<listcomp>)
                1048160    6.190    0.000 26922.814    0.026 allGraphs.py:179(getInterventionsmodel)
        43468350/821559 2311.275    0.000 24826.475    0.030 allGraphs.py:186(recursiveBEST)
        526804225/49482185 2751.629    0.000 22275.244    0.000 module.py:715(_call_impl)
               47732204  832.910    0.000 21766.812    0.000 container.py:115(forward)
               47505900  156.162    0.000 21299.843    0.000 BayesianNN.py:18(forward)
               40246762 1251.383    0.000 19317.809    0.000 BayesianNN.py:65(predict_no_convert)
              142517700  181.293    0.000 7343.547    0.000 dropout.py:57(forward)
              142517700  695.493    0.000 7162.253    0.000 functional.py:960(dropout)
              142970308  474.819    0.000 7037.405    0.000 linear.py:92(forward)
              142970308  730.015    0.000 6386.156    0.000 functional.py:1669(linear)
              142517700 6311.183    0.000 6311.183    0.000 {built-in method dropout}
                 113152  714.718    0.006 3716.666    0.033 allGraphs.py:156(transformNot)
              142970308 3312.995    0.000 3312.995    0.000 {built-in method addmm}
                1636829   22.152    0.000 3222.208    0.002 BayesianNN.py:57(learn)
                5622309   79.100    0.000 3173.156    0.001 BayesianNN.py:61(predict)
                1636829   27.658    0.000 3059.913    0.002 BayesianNN.py:21(learn)
              143196612  146.966    0.000 2044.225    0.000 activation.py:713(forward)
          871057/226601   66.381    0.000 1999.600    0.009 allGraphs.py:202(recursiveExplore)
              143196612  243.081    0.000 1897.259    0.000 functional.py:1292(leaky_relu)
                 113152    0.773    0.000 1832.231    0.016 agent.py:29(learn)
                 113152   12.685    0.000 1831.135    0.016 agent.py:117(_learn)
                 113152    9.755    0.000 1818.451    0.016 learner.py:42(Qlearn)
              143196612 1627.891    0.000 1627.891    0.000 {built-in method torch._C._nn.leaky_relu}
              142970308 1532.240    0.000 1532.240    0.000 {method 't' of 'torch._C._TensorBase' objects}
                1749981   13.552    0.000 1531.797    0.001 tensor.py:181(backward)
                1749981    8.630    0.000 1518.245    0.001 __init__.py:68(backward)
                1749981 1473.725    0.001 1473.725    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                1749981   13.685    0.000 1413.227    0.001 grad_mode.py:23(decorate_context)
                1749981   61.052    0.000 1373.024    0.001 adam.py:55(step)
                1749981  275.113    0.000 1073.190    0.001 functional.py:53(adam)
                 226304    0.990    0.000 1066.890    0.005 network.py:28(forward)
               55285359  259.078    0.000 1052.647    0.000 tensor.py:21(wrapped)
               43404399  201.447    0.000  994.830    0.000 tensor.py:506(__rsub__)
                 452608    1.708    0.000  900.709    0.002 conv.py:422(forward)
                 452608    2.050    0.000  898.390    0.002 conv.py:414(_conv_forward)
                 452608  896.086    0.002  896.086    0.002 {built-in method conv2d}
              252533954  250.204    0.000  796.291    0.000 overrides.py:1070(has_torch_function)
               43404399  793.384    0.000  793.384    0.000 {built-in method rsub}
                 113152    6.858    0.000  746.778    0.007 allGraphsTrain.py:33(<listcomp>)
               11428453  355.062    0.000  739.927    0.000 allGraphs.py:114(states)
                 113152    5.656    0.000  701.999    0.006 allGraphs.py:141(transform)
              101837200  625.816    0.000  625.816    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
              410198462  265.976    0.000  625.156    0.000 {built-in method builtins.any}
                7259138  446.665    0.000  623.270    0.000 BayesianNN.py:43(convert_data)
                 113152    0.785    0.000  606.249    0.005 game.py:42(step)
                 113152    1.150    0.000  592.362    0.005 layers.py:827(step)
              527143681  542.767    0.000  542.767    0.000 {built-in method torch._C._get_tracing_state}
                 113152    2.326    0.000  532.621    0.005 agent.py:112(__call__)
               43291247  495.067    0.000  495.067    0.000 {method 'gt' of 'torch._C._TensorBase' objects}
               75083390  261.938    0.000  429.588    0.000 tensor.py:933(grad)
                1749981   37.204    0.000  323.358    0.000 optimizer.py:167(zero_grad)
              671792172  261.111    0.000  316.705    0.000 overrides.py:1083(<genexpr>)
                 113152   14.965    0.000  308.889    0.003 layers.py:17(step)
               11315200   28.250    0.000  292.420    0.000 layer.py:106(move)
             2154949104  287.420    0.000  287.420    0.000 {method 'values' of 'collections.OrderedDict' objects}
                 113153   24.216    0.000  280.818    0.002 layers.py:793(update)
               21452380  263.120    0.000  263.120    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              336215392  258.772    0.000  258.772    0.000 module.py:765(__getattr__)
        1305939753/1305939751  222.781    0.000  225.813    0.000 {built-in method builtins.len}
              114790133  219.860    0.000  219.860    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                 113152   13.722    0.000  184.793    0.002 allGraphsTrain.py:51(<listcomp>)
               59273708  180.051    0.000  180.051    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               47958508   40.090    0.000  179.217    0.000 flatten.py:39(forward)
               21452380  160.480    0.000  160.480    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                 113152   20.784    0.000  158.407    0.001 allGraphsTrain.py:44(<listcomp>)
               66600659   56.934    0.000  143.478    0.000 {built-in method builtins.all}
               11315200   36.773    0.000  138.688    0.000 layers.py:844(check)
               14518277  135.522    0.000  135.522    0.000 {built-in method zeros}
              144267681   96.317    0.000  131.203    0.000 _VF.py:25(__getattr__)
                2121304  125.287    0.000  125.287    0.000 {built-in method tensor}
                1749981    4.667    0.000  124.036    0.000 loss.py:445(forward)
                1749981   13.812    0.000  119.369    0.000 functional.py:2637(mse_loss)
              142970308  115.192    0.000  115.192    0.000 functional.py:1686(<listcomp>)
                1613921    2.648    0.000  111.789    0.000 game.py:38(board)
               10726190  110.862    0.000  110.862    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               11880960  105.612    0.000  105.612    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               10726190  101.189    0.000  101.189    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               11315200   23.945    0.000  100.557    0.000 layers.py:838(isFree)
               46095375   98.659    0.000   98.659    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                 113152   34.104    0.000   92.332    0.001 agent.py:67(modify)
              396911440   90.584    0.000   90.584    0.000 {built-in method builtins.getattr}
                1048160   13.056    0.000   89.759    0.000 allGraphs.py:167(format)
               77268419   69.469    0.000   88.537    0.000 types.py:171(__get__)
               10726190   87.520    0.000   87.520    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                 121062    2.069    0.000   78.612    0.001 layers.py:849(restart)
                 792071   43.755    0.000   77.983    0.000 layer.py:175(NoRock_update)
               74211235   62.913    0.000   76.612    0.000 layer.py:103(isFree)
              433934683   73.679    0.000   73.679    0.000 _jit_internal.py:750(is_scripting)
               11315200   73.307    0.000   73.307    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                1749981   70.650    0.000   70.650    0.000 {built-in method torch._C._nn.mse_loss}
               10726190   70.381    0.000   70.381    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               10524335   69.978    0.000   69.978    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                 339456    2.114    0.000   67.668    0.000 tensor.py:576(__iter__)
              165856077   65.961    0.000   65.961    0.000 tensor.py:24(<genexpr>)
                 339456   64.396    0.000   64.396    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
                2804128   64.075    0.000   64.075    0.000 {built-in method cat}


Traceback (most recent call last):
  File "main.py", line 268, in <module>
    run(Defaults)
  File "/zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/auxillaries.py", line 133, in run
    (serverRun if isServer else Defaults.main).__call__(getvals(Defaults))
  File "/zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils/server.py", line 37, in serverRun
    profilingStats()
  File "/zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils/debug.py", line 62, in profilingStats
    os.remove('stats')
FileNotFoundError: [Errno 2] No such file or directory: 'stats'

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9653091: <Diamonds4_0.5_NN_cpu_1> in cluster <dcc> Exited

Job <Diamonds4_0.5_NN_cpu_1> was submitted from host <n-62-30-5> by user <s183905> in cluster <dcc> at Wed May 19 11:40:31 2021
Job was executed on host(s) <n-62-21-108>, in queue <hpc>, as user <s183905> in cluster <dcc> at Wed May 19 11:40:32 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 19 11:40:32 2021
Terminated at Wed May 19 21:35:39 2021
Results reported at Wed May 19 21:35:39 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -n 1
#BSUB -R "rusage[mem=16G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 4320
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $MYARGS
------------------------------------------------------------

Exited with exit code 1.

Resource usage summary:

    CPU time :                                   35697.50 sec.
    Max Memory :                                 103 MB
    Average Memory :                             99.79 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               16281.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   35791 sec.
    Turnaround time :                            35708 sec.

The output (if any) is above this job summary.

/zhome/ee/d/137643/Desktop/Bachelor/project-env/lib/python3.8/site-packages/torch/cuda/__init__.py:52: UserWarning: CUDA initialization: Found no NVIDIA driver on your system. Please check that you have an NVIDIA GPU and installed a driver from http://www.nvidia.com/Download/index.aspx (Triggered internally at  /pytorch/c10/cuda/CUDAFunctions.cpp:100.)
  return torch._C._cuda_getDeviceCount() > 0

# Parameters

    Name :                      Diamonds4_0.5_NN_cpu-1
    Main :                      graphTrain
    Level :                     Levels.Causal7
    Failed actions chance :     0.5
    Use model :                 True
    Depth :                     1
    Model explore :             100000
    Samples :                   5
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
    Layer super1 :              True
    Layer super2 :              True
    Layer super3 :              True
    Layer super4 :              True
    Layer super5 :              True
    Layer super6 :              True
    Layer super7 :              True
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
    Num :                       1
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      16803265420 function calls (16441925534 primitive calls) in 35700.29 seconds

##    Ordered by: cumulative time
   List reduced from 441 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35700.295 35700.295 {built-in method builtins.exec}
                      1    0.001    0.001 35700.294 35700.294 <string>:1(<module>)
                      1   76.293   76.293 35700.293 35700.293 allGraphsTrain.py:13(graphTrain)
        379729548/41236038 1438.606    0.000 12535.112    0.000 module.py:715(_call_impl)
                 325472   65.187    0.000 12091.170    0.037 allGraphsTrain.py:40(<listcomp>)
                5244169   19.455    0.000 11983.485    0.002 allGraphs.py:179(getInterventionsmodel)
               33849351  384.933    0.000 11908.038    0.000 container.py:115(forward)
                 325472 2026.552    0.006 11631.579    0.036 allGraphs.py:156(transformNot)
               33198407   77.513    0.000 10135.898    0.000 BayesianNN.py:18(forward)
                7061215   69.921    0.000 10061.461    0.001 BayesianNN.py:57(learn)
        27060270/5037113 1114.670    0.000 9953.795    0.002 allGraphs.py:186(recursiveBEST)
               26137192  257.525    0.000 9714.993    0.000 BayesianNN.py:61(predict)
                7061215   84.099    0.000 9565.811    0.001 BayesianNN.py:21(learn)
                7386687   42.927    0.000 4341.788    0.001 grad_mode.py:23(decorate_context)
                7386687  207.886    0.000 4218.099    0.001 adam.py:55(step)
                 325472    1.953    0.000 3885.074    0.012 agent.py:29(learn)
                 325472   37.431    0.000 3882.220    0.012 agent.py:117(_learn)
                 325472   24.268    0.000 3844.789    0.012 learner.py:42(Qlearn)
                7386687   37.928    0.000 3788.031    0.001 tensor.py:181(backward)
                7386687   23.975    0.000 3750.103    0.001 __init__.py:68(backward)
                7386687 3617.161    0.000 3617.161    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
              100897109  220.015    0.000 3484.032    0.000 linear.py:92(forward)
               99595221   85.177    0.000 3432.302    0.000 dropout.py:57(forward)
               99595221  330.594    0.000 3347.125    0.000 functional.py:960(dropout)
              100897109  389.017    0.000 3172.394    0.000 functional.py:1669(linear)
                7386687  798.901    0.000 3160.327    0.000 functional.py:53(adam)
               99595221 2922.699    0.000 2922.699    0.000 {built-in method dropout}
                 650944    2.149    0.000 2111.862    0.003 network.py:28(forward)
                 325472   42.621    0.000 2106.393    0.006 allGraphsTrain.py:33(<listcomp>)
               32872773  994.698    0.000 2063.778    0.000 allGraphs.py:114(states)
               33198407 1440.001    0.000 1980.200    0.000 BayesianNN.py:43(convert_data)
                 325472   16.437    0.000 1799.968    0.006 allGraphs.py:141(transform)
              358019700 1754.298    0.000 1754.298    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 325472    1.883    0.000 1717.957    0.005 game.py:42(step)
         1029863/207056   61.273    0.000 1715.889    0.008 allGraphs.py:202(recursiveExplore)
                1301888    4.465    0.000 1715.699    0.001 conv.py:422(forward)
                1301888    4.999    0.000 1709.389    0.001 conv.py:414(_conv_forward)
                1301888 1703.757    0.001 1703.757    0.001 {built-in method conv2d}
                 325472    2.792    0.000 1682.808    0.005 layers.py:827(step)
              100897109 1626.044    0.000 1626.044    0.000 {built-in method addmm}
              314797522  883.090    0.000 1504.653    0.000 tensor.py:933(grad)
                7386687  134.534    0.000 1116.917    0.000 optimizer.py:167(zero_grad)
              101548053   73.344    0.000 1086.398    0.000 activation.py:713(forward)
                 325472    5.904    0.000 1068.747    0.003 agent.py:112(__call__)
              500410008  329.570    0.000 1043.654    0.000 overrides.py:1070(has_torch_function)
              101548053  120.103    0.000 1013.054    0.000 functional.py:1292(leaky_relu)
                 325472   37.035    0.000  886.108    0.003 layers.py:17(step)
              101548053  879.439    0.000  879.439    0.000 {built-in method torch._C._nn.leaky_relu}
               32547200   68.807    0.000  845.262    0.000 layer.py:106(move)
              648205458  327.599    0.000  843.676    0.000 {built-in method builtins.any}
                 325473   57.812    0.000  790.440    0.002 layers.py:793(update)
               89942132  787.325    0.000  787.325    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               57345996  166.144    0.000  746.785    0.000 tensor.py:21(wrapped)
              100897109  707.520    0.000  707.520    0.000 {method 't' of 'torch._C._TensorBase' objects}
              397630715  608.009    0.000  608.009    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               89942132  501.190    0.000  501.190    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               32547200  102.270    0.000  419.297    0.000 layers.py:844(check)
               66396815  405.849    0.000  405.849    0.000 {built-in method zeros}
                 325472   27.109    0.000  395.892    0.001 allGraphsTrain.py:51(<listcomp>)
             1141461326  322.858    0.000  395.586    0.000 overrides.py:1083(<genexpr>)
                 325472   48.828    0.000  387.567    0.001 allGraphsTrain.py:44(<listcomp>)
               23171436   75.750    0.000  368.859    0.000 tensor.py:506(__rsub__)
                8271076  359.894    0.000  359.894    0.000 {built-in method tensor}
                7386687   10.703    0.000  358.971    0.000 loss.py:445(forward)
                7386687   42.169    0.000  348.268    0.000 functional.py:2637(mse_loss)
                6871530    7.192    0.000  329.914    0.000 game.py:38(board)
               44971066  305.060    0.000  305.060    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               44971066  301.824    0.000  301.824    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               23171436  293.110    0.000  293.110    0.000 {built-in method rsub}
                5244169   44.284    0.000  292.169    0.000 allGraphs.py:167(format)
               32547200   67.095    0.000  288.986    0.000 layers.py:838(isFree)
                 422333    5.847    0.000  265.827    0.001 layers.py:849(restart)
              380705964  244.974    0.000  244.974    0.000 {built-in method torch._C._get_tracing_state}
               44971066  241.625    0.000  241.625    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              249226265  184.334    0.000  221.892    0.000 layer.py:103(isFree)
               34174560  220.838    0.000  220.838    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                 422333    2.987    0.000  220.323    0.001 level.py:8(__init__)
               44971066  209.670    0.000  209.670    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                 325472   75.731    0.000  209.063    0.001 agent.py:67(modify)
               42881652  205.911    0.000  205.911    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                7386687  199.509    0.000  199.509    0.000 {built-in method torch._C._nn.mse_loss}
                2603784  110.887    0.000  197.479    0.000 layer.py:175(NoRock_update)
                 422333    7.715    0.000  194.924    0.000 levels.py:303(generate)
               22845964  191.075    0.000  191.075    0.000 {method 'gt' of 'torch._C._TensorBase' objects}
              546237906  128.562    0.000  188.159    0.000 enum.py:646(__hash__)
               67047495  184.687    0.000  184.687    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               32547200  182.032    0.000  182.032    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                2533715   30.746    0.000  179.117    0.000 level.py:41(notUsed)
               89893296   42.333    0.000  169.390    0.000 {built-in method builtins.all}
               44971176   67.589    0.000  155.655    0.000 tensor.py:596(__hash__)
                 976416    4.620    0.000  155.060    0.000 tensor.py:576(__iter__)
             1552767543  152.970    0.000  152.970    0.000 {method 'values' of 'collections.OrderedDict' objects}
        1253904772/1253904770  142.644    0.000  148.345    0.000 {built-in method builtins.len}
              245309549  147.967    0.000  147.968    0.000 module.py:765(__getattr__)
                 976416  147.332    0.000  147.332    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
              152397862   90.671    0.000  117.980    0.000 types.py:171(__get__)
              289124703   94.338    0.000  114.973    0.000 layers.py:809(<genexpr>)
               44971066  113.817    0.000  113.817    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               34500295   25.806    0.000  108.902    0.000 flatten.py:39(forward)
                7386687   34.272    0.000  101.151    0.000 __init__.py:28(_make_grads)


Traceback (most recent call last):
  File "main.py", line 268, in <module>
    run(Defaults)
  File "/zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/auxillaries.py", line 133, in run
    (serverRun if isServer else Defaults.main).__call__(getvals(Defaults))
  File "/zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils/server.py", line 37, in serverRun
    profilingStats()
  File "/zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils/debug.py", line 62, in profilingStats
    os.remove('stats')
FileNotFoundError: [Errno 2] No such file or directory: 'stats'

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9668373: <Diamonds4_0.5_NN_cpu_1> in cluster <dcc> Exited

Job <Diamonds4_0.5_NN_cpu_1> was submitted from host <n-62-30-8> by user <s183905> in cluster <dcc> at Wed May 19 22:55:26 2021
Job was executed on host(s) <n-62-11-66>, in queue <hpc>, as user <s183905> in cluster <dcc> at Wed May 19 22:55:27 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 19 22:55:27 2021
Terminated at Thu May 20 08:50:33 2021
Results reported at Thu May 20 08:50:33 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -n 1
#BSUB -R "rusage[mem=16G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 4320
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $MYARGS
------------------------------------------------------------

Exited with exit code 1.

Resource usage summary:

    CPU time :                                   35616.66 sec.
    Max Memory :                                 104 MB
    Average Memory :                             96.45 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               16280.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   35706 sec.
    Turnaround time :                            35707 sec.

The output (if any) is above this job summary.

