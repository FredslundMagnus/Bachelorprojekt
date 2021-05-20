/zhome/ee/d/137643/Desktop/Bachelor/project-env/lib/python3.8/site-packages/torch/cuda/__init__.py:52: UserWarning: CUDA initialization: Found no NVIDIA driver on your system. Please check that you have an NVIDIA GPU and installed a driver from http://www.nvidia.com/Download/index.aspx (Triggered internally at  /pytorch/c10/cuda/CUDAFunctions.cpp:100.)
  return torch._C._cuda_getDeviceCount() > 0

# Parameters

    Name :                      Diamonds1_0.5_NN_cpu-2
    Main :                      graphTrain
    Level :                     Levels.Causal2
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
    Num :                       2
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      12182421202 function calls (11653686375 primitive calls) in 35701.41 seconds

##    Ordered by: cumulative time
   List reduced from 440 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35701.413 35701.413 {built-in method builtins.exec}
                      1    0.001    0.001 35701.413 35701.413 <string>:1(<module>)
                      1   31.966   31.966 35701.411 35701.411 allGraphsTrain.py:13(graphTrain)
                 113859   23.386    0.000 27382.596    0.240 allGraphsTrain.py:40(<listcomp>)
                 904276    4.765    0.000 27349.451    0.030 allGraphs.py:179(getInterventionsmodel)
        44617609/719251 2317.334    0.000 25563.901    0.036 allGraphs.py:186(recursiveBEST)
        534324030/50047170 2765.734    0.000 22682.194    0.000 module.py:715(_call_impl)
               48427686  904.893    0.000 22184.811    0.000 container.py:115(forward)
               48199968  152.830    0.000 21674.219    0.000 BayesianNN.py:18(forward)
               41618852 1314.012    0.000 20089.614    0.000 BayesianNN.py:65(predict_no_convert)
              144599904  225.167    0.000 7523.313    0.000 dropout.py:57(forward)
              144599904  739.746    0.000 7298.146    0.000 functional.py:960(dropout)
              145055340  449.819    0.000 7118.650    0.000 linear.py:92(forward)
              145055340  749.994    0.000 6488.318    0.000 functional.py:1669(linear)
              144599904 6394.604    0.000 6394.604    0.000 {built-in method dropout}
                 113859  711.588    0.006 3406.096    0.030 allGraphs.py:156(transformNot)
              145055340 3351.169    0.000 3351.169    0.000 {built-in method addmm}
                1505625   18.255    0.000 2832.234    0.002 BayesianNN.py:57(learn)
                5075491   68.834    0.000 2831.613    0.001 BayesianNN.py:61(predict)
                1505625   23.498    0.000 2695.509    0.002 BayesianNN.py:21(learn)
              145283058  154.170    0.000 2087.268    0.000 activation.py:713(forward)
              145283058  238.195    0.000 1933.098    0.000 functional.py:1292(leaky_relu)
                 113859    0.754    0.000 1823.630    0.016 agent.py:29(learn)
                 113859   11.875    0.000 1822.555    0.016 agent.py:117(_learn)
                 113859    9.637    0.000 1810.680    0.016 learner.py:42(Qlearn)
          744222/185025   53.025    0.000 1708.522    0.009 allGraphs.py:202(recursiveExplore)
              145283058 1670.026    0.000 1670.026    0.000 {built-in method torch._C._nn.leaky_relu}
              145055340 1552.171    0.000 1552.171    0.000 {method 't' of 'torch._C._TensorBase' objects}
                1619484   11.147    0.000 1449.041    0.001 tensor.py:181(backward)
                1619484    7.249    0.000 1437.894    0.001 __init__.py:68(backward)
                1619484 1399.650    0.001 1399.650    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                1619484   11.509    0.000 1244.409    0.001 grad_mode.py:23(decorate_context)
                1619484   54.774    0.000 1210.243    0.001 adam.py:55(step)
                 227718    0.961    0.000 1113.699    0.005 network.py:28(forward)
               44571414  211.584    0.000 1047.816    0.000 tensor.py:506(__rsub__)
               56526609  256.058    0.000 1025.949    0.000 tensor.py:21(wrapped)
                1619484  244.481    0.000  936.475    0.001 functional.py:53(adam)
                 455436    1.673    0.000  935.015    0.002 conv.py:422(forward)
                 455436    1.812    0.000  932.753    0.002 conv.py:414(_conv_forward)
                 455436  930.689    0.002  930.689    0.002 {built-in method conv2d}
               44571414  836.232    0.000  836.232    0.000 {built-in method rsub}
              248210150  238.641    0.000  795.628    0.000 overrides.py:1070(has_torch_function)
                 113859    9.033    0.000  708.983    0.006 allGraphsTrain.py:33(<listcomp>)
               11499860  343.389    0.000  699.957    0.000 allGraphs.py:114(states)
                 113859    0.750    0.000  628.658    0.006 game.py:42(step)
              407758540  266.648    0.000  625.790    0.000 {built-in method builtins.any}
                 113859    1.100    0.000  615.224    0.005 layers.py:827(step)
                 113859    4.880    0.000  589.723    0.005 allGraphs.py:141(transform)
              102473500  584.704    0.000  584.704    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 113859    2.294    0.000  563.121    0.005 agent.py:112(__call__)
              534665607  550.406    0.000  550.406    0.000 {built-in method torch._C._get_tracing_state}
                6581116  383.440    0.000  532.959    0.000 BayesianNN.py:43(convert_data)
               44457555  478.204    0.000  478.204    0.000 {method 'gt' of 'torch._C._TensorBase' objects}
               69612414  239.532    0.000  393.459    0.000 tensor.py:933(grad)
              665073304  259.380    0.000  315.926    0.000 overrides.py:1083(<genexpr>)
                 113859   14.691    0.000  312.087    0.003 layers.py:17(step)
                 113860   23.749    0.000  300.499    0.003 layers.py:793(update)
               11385900   28.251    0.000  295.919    0.000 layer.py:106(move)
                1619484   33.418    0.000  292.511    0.000 optimizer.py:167(zero_grad)
             2185723806  282.103    0.000  282.103    0.000 {method 'values' of 'collections.OrderedDict' objects}
              340955390  261.537    0.000  261.538    0.000 module.py:765(__getattr__)
        1322492545/1322492543  225.368    0.000  228.183    0.000 {built-in method builtins.len}
               19889244  224.658    0.000  224.658    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              115365929  206.015    0.000  206.015    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               60041304  179.247    0.000  179.247    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                 113859   13.074    0.000  174.563    0.002 allGraphsTrain.py:51(<listcomp>)
               48655404   37.536    0.000  174.499    0.000 flatten.py:39(forward)
                 113859   20.754    0.000  163.437    0.001 allGraphsTrain.py:44(<listcomp>)
               67912609   62.459    0.000  159.277    0.000 {built-in method builtins.all}
               19889244  142.770    0.000  142.770    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               11385900   35.951    0.000  141.440    0.000 layers.py:844(check)
              146219388   97.721    0.000  141.192    0.000 _VF.py:25(__getattr__)
              145055340  117.255    0.000  117.255    0.000 functional.py:1686(<listcomp>)
               13162233  114.092    0.000  114.092    0.000 {built-in method zeros}
                1983717  108.248    0.000  108.248    0.000 {built-in method tensor}
                1619484    3.340    0.000  107.191    0.000 loss.py:445(forward)
                1619484   11.515    0.000  103.852    0.000 functional.py:2637(mse_loss)
               11385900   25.974    0.000  100.815    0.000 layers.py:838(isFree)
              394539211  100.128    0.000  100.128    0.000 {built-in method builtins.getattr}
               11955195   97.882    0.000   97.882    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               46922061   97.657    0.000   97.657    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                9944622   95.515    0.000   95.515    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                1473572    2.317    0.000   94.826    0.000 game.py:38(board)
                 113859   34.251    0.000   91.436    0.001 agent.py:67(modify)
                9944622   88.618    0.000   88.618    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                 131918    2.042    0.000   84.458    0.001 layers.py:849(restart)
               72737029   67.643    0.000   84.280    0.000 types.py:171(__get__)
                 797020   43.824    0.000   78.131    0.000 layer.py:175(NoRock_update)
               11385900   77.477    0.000   77.477    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                9944622   75.011    0.000   75.011    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               69377208   62.169    0.000   74.842    0.000 layer.py:103(isFree)
              146194050   73.657    0.000   73.657    0.000 {method 'dim' of 'torch._C._TensorBase' objects}
                 904276   11.104    0.000   71.788    0.000 allGraphs.py:167(format)
              439796874   70.706    0.000   70.706    0.000 _jit_internal.py:750(is_scripting)
                 131918    1.084    0.000   68.115    0.001 level.py:8(__init__)
                 341577    2.080    0.000   65.779    0.000 tensor.py:576(__iter__)
              169579827   65.153    0.000   65.153    0.000 tensor.py:24(<genexpr>)
                 341577   62.530    0.000   62.530    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
                1619484   62.031    0.000   62.031    0.000 {built-in method torch._C._nn.mse_loss}
                9944622   61.736    0.000   61.736    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9653083: <Diamonds1_0.5_NN_cpu_2> in cluster <dcc> Done

Job <Diamonds1_0.5_NN_cpu_2> was submitted from host <n-62-30-5> by user <s183905> in cluster <dcc> at Wed May 19 11:40:29 2021
Job was executed on host(s) <n-62-21-107>, in queue <hpc>, as user <s183905> in cluster <dcc> at Wed May 19 11:40:30 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 19 11:40:30 2021
Terminated at Wed May 19 21:35:43 2021
Results reported at Wed May 19 21:35:43 2021

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

Successfully completed.

Resource usage summary:

    CPU time :                                   35702.95 sec.
    Max Memory :                                 106 MB
    Average Memory :                             100.48 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               16278.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   35709 sec.
    Turnaround time :                            35714 sec.

The output (if any) is above this job summary.

/zhome/ee/d/137643/Desktop/Bachelor/project-env/lib/python3.8/site-packages/torch/cuda/__init__.py:52: UserWarning: CUDA initialization: Found no NVIDIA driver on your system. Please check that you have an NVIDIA GPU and installed a driver from http://www.nvidia.com/Download/index.aspx (Triggered internally at  /pytorch/c10/cuda/CUDAFunctions.cpp:100.)
  return torch._C._cuda_getDeviceCount() > 0

# Parameters

    Name :                      Diamonds1_0.5_NN_cpu-2
    Main :                      graphTrain
    Level :                     Levels.Causal2
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
    Num :                       2
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      15278144890 function calls (14984266602 primitive calls) in 35700.32 seconds

##    Ordered by: cumulative time
   List reduced from 439 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35700.316 35700.316 {built-in method builtins.exec}
                      1    0.001    0.001 35700.315 35700.315 <string>:1(<module>)
                      1   93.928   93.928 35700.314 35700.314 allGraphsTrain.py:13(graphTrain)
        310521717/34797187 1325.564    0.000 12427.870    0.000 module.py:715(_call_impl)
               27572453  337.233    0.000 11769.651    0.000 container.py:115(forward)
                 339629 1880.523    0.006 11519.036    0.034 allGraphs.py:156(transformNot)
                6885105   74.597    0.000 10708.967    0.002 BayesianNN.py:57(learn)
                 339629   73.264    0.000 10275.348    0.030 allGraphsTrain.py:40(<listcomp>)
                6885105   91.428    0.000 10186.651    0.001 BayesianNN.py:21(learn)
                5377726   20.693    0.000 10157.708    0.002 allGraphs.py:179(getInterventionsmodel)
               26893195   72.615    0.000 9138.625    0.000 BayesianNN.py:18(forward)
        22917645/5227985  968.259    0.000 8774.482    0.002 allGraphs.py:186(recursiveBEST)
               20008090  220.931    0.000 8166.062    0.000 BayesianNN.py:61(predict)
                7224734   47.103    0.000 4649.655    0.001 grad_mode.py:23(decorate_context)
                7224734  221.046    0.000 4513.589    0.001 adam.py:55(step)
                 339629    2.414    0.000 4433.381    0.013 agent.py:29(learn)
                 339629   44.413    0.000 4430.099    0.013 agent.py:117(_learn)
                 339629   30.995    0.000 4385.686    0.013 learner.py:42(Qlearn)
                7224734   42.930    0.000 4075.998    0.001 tensor.py:181(backward)
                7224734   27.475    0.000 4033.068    0.001 __init__.py:68(backward)
                7224734 3890.661    0.001 3890.661    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                7224734  848.828    0.000 3378.291    0.000 functional.py:53(adam)
               82038101  212.598    0.000 3202.197    0.000 linear.py:92(forward)
               80679585   76.339    0.000 3101.224    0.000 dropout.py:57(forward)
               80679585  297.576    0.000 3024.885    0.000 functional.py:960(dropout)
                 679258    3.142    0.000 2952.347    0.004 network.py:28(forward)
               82038101  343.556    0.000 2904.442    0.000 functional.py:1669(linear)
               80679585 2639.315    0.000 2639.315    0.000 {built-in method dropout}
                1358516    5.517    0.000 2412.192    0.002 conv.py:422(forward)
                1358516    6.300    0.000 2404.693    0.002 conv.py:414(_conv_forward)
                1358516 2397.634    0.002 2397.634    0.002 {built-in method conv2d}
                 339629   20.370    0.000 2337.145    0.007 allGraphs.py:141(transform)
                 339629   79.587    0.000 1988.778    0.006 allGraphsTrain.py:33(<listcomp>)
               34302630  930.607    0.000 1909.203    0.000 allGraphs.py:114(states)
                 339629    2.908    0.000 1901.353    0.006 game.py:42(step)
                 339629    3.044    0.000 1856.786    0.005 layers.py:827(step)
               26893195 1211.274    0.000 1685.062    0.000 BayesianNN.py:43(convert_data)
                 339629    8.188    0.000 1640.739    0.005 agent.py:112(__call__)
              305666500 1609.211    0.000 1609.211    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
              308193694  953.313    0.000 1595.739    0.000 tensor.py:933(grad)
               82038101 1508.086    0.000 1508.086    0.000 {built-in method addmm}
                7224734  130.288    0.000 1163.608    0.000 optimizer.py:167(zero_grad)
               82717359   64.094    0.000 1070.819    0.000 activation.py:713(forward)
          613427/149741   37.239    0.000 1063.546    0.007 allGraphs.py:202(recursiveExplore)
              475637967  338.073    0.000 1060.507    0.000 overrides.py:1070(has_torch_function)
               82717359  110.745    0.000 1006.724    0.000 functional.py:1292(leaky_relu)
                 339629   42.864    0.000  924.965    0.003 layers.py:17(step)
                 339630   67.095    0.000  924.227    0.003 layers.py:793(update)
               82717359  883.140    0.000  883.140    0.000 {built-in method torch._C._nn.leaky_relu}
               33962900   80.203    0.000  877.614    0.000 layer.py:106(move)
              605515257  327.043    0.000  851.763    0.000 {built-in method builtins.any}
               88055324  843.648    0.000  843.648    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               54154020  172.784    0.000  776.810    0.000 tensor.py:21(wrapped)
               82038101  641.620    0.000  641.620    0.000 {method 't' of 'torch._C._TensorBase' objects}
              346517217  576.158    0.000  576.158    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               88055324  537.123    0.000  537.123    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                 339629   30.006    0.000  452.648    0.001 allGraphsTrain.py:51(<listcomp>)
                 339629   53.533    0.000  425.780    0.001 allGraphsTrain.py:44(<listcomp>)
               33962900  102.198    0.000  406.406    0.000 layers.py:844(check)
             1074692435  329.067    0.000  404.462    0.000 overrides.py:1083(<genexpr>)
                7224734   11.412    0.000  392.954    0.000 loss.py:445(forward)
                7224734   45.830    0.000  381.542    0.000 functional.py:2637(mse_loss)
                8534606  369.037    0.000  369.037    0.000 {built-in method tensor}
               53786391  356.769    0.000  356.769    0.000 {built-in method zeros}
                 573279    7.993    0.000  335.926    0.001 layers.py:849(restart)
                7075872    8.389    0.000  335.322    0.000 game.py:38(board)
               44027662  324.951    0.000  324.951    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               18492975   69.486    0.000  320.934    0.000 tensor.py:506(__rsub__)
               44027662  318.368    0.000  318.368    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               33962900   68.838    0.000  312.365    0.000 layers.py:838(isFree)
                5377726   57.178    0.000  296.635    0.000 allGraphs.py:167(format)
                 573279    4.344    0.000  271.589    0.000 level.py:8(__init__)
               44027662  263.607    0.000  263.607    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               18492975  251.448    0.000  251.448    0.000 {built-in method rsub}
               35661045  248.601    0.000  248.601    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                 339629   90.172    0.000  245.192    0.001 agent.py:67(modify)
              225221612  204.181    0.000  243.528    0.000 layer.py:103(isFree)
                 573279    9.483    0.000  234.284    0.000 levels.py:151(generate)
               44027662  226.928    0.000  226.928    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              311540604  226.210    0.000  226.210    0.000 {built-in method torch._C._get_tracing_state}
                2377410  123.959    0.000  216.876    0.000 layer.py:175(NoRock_update)
                7224734  215.507    0.000  215.507    0.000 {built-in method torch._C._nn.mse_loss}
                2750675   37.984    0.000  214.637    0.000 level.py:41(notUsed)
              518071914  137.002    0.000  202.525    0.000 enum.py:646(__hash__)
               88117020   47.081    0.000  201.025    0.000 {built-in method builtins.all}
               33962900  200.259    0.000  200.259    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                1018887    5.662    0.000  190.005    0.000 tensor.py:576(__iter__)
               35724559  188.614    0.000  188.614    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               62214611  188.248    0.000  188.248    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                1018887  180.693    0.000  180.693    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               18153346  169.525    0.000  169.525    0.000 {method 'gt' of 'torch._C._TensorBase' objects}
               44027772   73.040    0.000  166.768    0.000 tensor.py:596(__hash__)
             1269659321  143.173    0.000  143.173    0.000 {method 'values' of 'collections.OrderedDict' objects}
        1065353245/1065353243  131.883    0.000  138.633    0.000 {built-in method builtins.len}
              201251803  137.427    0.000  137.428    0.000 module.py:765(__getattr__)
              111658425   38.383    0.000  126.119    0.000 layers.py:799(<genexpr>)
               44027662  121.667    0.000  121.667    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              267117768   92.773    0.000  114.221    0.000 layers.py:809(<genexpr>)
              563742625  108.349    0.000  108.349    0.000 {built-in method builtins.getattr}
                7224734   36.127    0.000  106.540    0.000 __init__.py:28(_make_grads)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9668365: <Diamonds1_0.5_NN_cpu_2> in cluster <dcc> Done

Job <Diamonds1_0.5_NN_cpu_2> was submitted from host <n-62-30-8> by user <s183905> in cluster <dcc> at Wed May 19 22:55:24 2021
Job was executed on host(s) <n-62-31-3>, in queue <hpc>, as user <s183905> in cluster <dcc> at Wed May 19 22:55:26 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 19 22:55:26 2021
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

Successfully completed.

Resource usage summary:

    CPU time :                                   35604.02 sec.
    Max Memory :                                 104 MB
    Average Memory :                             97.92 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               16280.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   35779 sec.
    Turnaround time :                            35709 sec.

The output (if any) is above this job summary.

