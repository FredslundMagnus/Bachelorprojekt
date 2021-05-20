/zhome/ee/d/137643/Desktop/Bachelor/project-env/lib/python3.8/site-packages/torch/cuda/__init__.py:52: UserWarning: CUDA initialization: Found no NVIDIA driver on your system. Please check that you have an NVIDIA GPU and installed a driver from http://www.nvidia.com/Download/index.aspx (Triggered internally at  /pytorch/c10/cuda/CUDAFunctions.cpp:100.)
  return torch._C._cuda_getDeviceCount() > 0

# Parameters

    Name :                      Diamonds4_0.5_NN_cpu-2
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
    Num :                       2
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      12028667796 function calls (11512800505 primitive calls) in 35700.51 seconds

##    Ordered by: cumulative time
   List reduced from 444 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35700.511 35700.511 {built-in method builtins.exec}
                      1    0.001    0.001 35700.511 35700.511 <string>:1(<module>)
                      1   27.573   27.573 35700.509 35700.509 allGraphsTrain.py:13(graphTrain)
                 115641   24.056    0.000 26887.882    0.233 allGraphsTrain.py:40(<listcomp>)
                 995343    5.608    0.000 26854.053    0.027 allGraphs.py:179(getInterventionsmodel)
        43182816/786245 2309.425    0.000 24948.651    0.032 allGraphs.py:186(recursiveBEST)
        521970424/49093944 2768.820    0.000 22267.543    0.000 module.py:715(_call_impl)
               47287648  860.314    0.000 21767.103    0.000 container.py:115(forward)
               47056366  174.786    0.000 21350.562    0.000 BayesianNN.py:18(forward)
               40065388 1254.861    0.000 19491.806    0.000 BayesianNN.py:65(predict_no_convert)
              141169098  185.124    0.000 7305.079    0.000 dropout.py:57(forward)
              141169098  697.604    0.000 7119.955    0.000 functional.py:960(dropout)
              141631662  471.177    0.000 7049.095    0.000 linear.py:92(forward)
              141631662  725.742    0.000 6400.270    0.000 functional.py:1669(linear)
              141169098 6269.144    0.000 6269.144    0.000 {built-in method dropout}
                 115641  774.024    0.007 3852.774    0.033 allGraphs.py:156(transformNot)
              141631662 3239.440    0.000 3239.440    0.000 {built-in method addmm}
                1690655   19.770    0.000 3199.185    0.002 BayesianNN.py:57(learn)
                1690655   25.193    0.000 3044.134    0.002 BayesianNN.py:21(learn)
                5300323   70.322    0.000 2972.206    0.001 BayesianNN.py:61(predict)
              141862944  146.257    0.000 2043.382    0.000 activation.py:713(forward)
              141862944  237.810    0.000 1897.125    0.000 functional.py:1292(leaky_relu)
          802926/209098   58.670    0.000 1824.133    0.009 allGraphs.py:202(recursiveExplore)
                 115641    0.748    0.000 1784.462    0.015 agent.py:29(learn)
                 115641   17.077    0.000 1783.410    0.015 agent.py:117(_learn)
                 115641    9.515    0.000 1766.333    0.015 learner.py:42(Qlearn)
              141862944 1634.351    0.000 1634.351    0.000 {built-in method torch._C._nn.leaky_relu}
              141631662 1585.561    0.000 1585.561    0.000 {method 't' of 'torch._C._TensorBase' objects}
                1806296   12.572    0.000 1481.434    0.001 tensor.py:181(backward)
                1806296    7.667    0.000 1468.862    0.001 __init__.py:68(backward)
                1806296 1426.782    0.001 1426.782    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                1806296   14.093    0.000 1402.798    0.001 grad_mode.py:23(decorate_context)
                1806296   59.176    0.000 1363.729    0.001 adam.py:55(step)
                1806296  273.437    0.000 1055.950    0.001 functional.py:53(adam)
               55248345  256.462    0.000 1051.187    0.000 tensor.py:21(wrapped)
                 231282    0.925    0.000 1033.666    0.004 network.py:28(forward)
               43106040  205.178    0.000  997.463    0.000 tensor.py:506(__rsub__)
                 462564    1.601    0.000  872.459    0.002 conv.py:422(forward)
                 462564    1.731    0.000  870.282    0.002 conv.py:414(_conv_forward)
                 462564  868.286    0.002  868.286    0.002 {built-in method conv2d}
              253960287  254.931    0.000  835.117    0.000 overrides.py:1070(has_torch_function)
                 115641    7.112    0.000  797.664    0.007 allGraphsTrain.py:33(<listcomp>)
               43106040  792.286    0.000  792.286    0.000 {built-in method rsub}
               11679842  380.684    0.000  790.563    0.000 allGraphs.py:114(states)
              104077300  677.990    0.000  677.990    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
              410652157  270.067    0.000  656.315    0.000 {built-in method builtins.any}
                 115641    4.938    0.000  637.799    0.006 allGraphs.py:141(transform)
                 115641    0.764    0.000  601.817    0.005 game.py:42(step)
                 115641    1.126    0.000  588.434    0.005 layers.py:827(step)
              522317347  574.571    0.000  574.571    0.000 {built-in method torch._C._get_tracing_state}
                6990978  410.548    0.000  568.337    0.000 BayesianNN.py:43(convert_data)
                 115641    2.255    0.000  515.245    0.004 agent.py:112(__call__)
               42990399  490.706    0.000  490.706    0.000 {method 'gt' of 'torch._C._TensorBase' objects}
               77483466  269.146    0.000  440.781    0.000 tensor.py:933(grad)
              673328227  269.530    0.000  341.807    0.000 overrides.py:1083(<genexpr>)
                1806296   36.663    0.000  323.183    0.000 optimizer.py:167(zero_grad)
                 115641   14.789    0.000  310.785    0.003 layers.py:17(step)
               11564100   27.933    0.000  294.454    0.000 layer.py:106(move)
             2135169344  278.823    0.000  278.823    0.000 {method 'values' of 'collections.OrderedDict' objects}
                 115642   24.141    0.000  274.999    0.002 layers.py:793(update)
              333167282  262.003    0.000  262.004    0.000 module.py:765(__getattr__)
               22138116  256.873    0.000  256.873    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              117332975  230.822    0.000  230.822    0.000 {method 'item' of 'torch._C._TensorBase' objects}
        1297226744/1297226742  217.686    0.000  220.704    0.000 {built-in method builtins.len}
                 115641   14.609    0.000  192.134    0.002 allGraphsTrain.py:51(<listcomp>)
               59083030  174.818    0.000  174.818    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               47518930   39.403    0.000  170.728    0.000 flatten.py:39(forward)
                 115641   22.119    0.000  170.311    0.001 allGraphsTrain.py:44(<listcomp>)
               22138116  160.284    0.000  160.284    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               11564100   37.881    0.000  142.127    0.000 layers.py:844(check)
               66812545   57.387    0.000  138.327    0.000 {built-in method builtins.all}
              142975394   94.435    0.000  129.720    0.000 _VF.py:25(__getattr__)
               13981957  120.769    0.000  120.769    0.000 {built-in method zeros}
                1806296    3.668    0.000  119.538    0.000 loss.py:445(forward)
              141631662  116.274    0.000  116.274    0.000 functional.py:1686(<listcomp>)
                1806296   12.644    0.000  115.869    0.000 functional.py:2637(mse_loss)
                2091500  112.217    0.000  112.217    0.000 {built-in method tensor}
               12142305  109.586    0.000  109.586    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
              397046710  107.671    0.000  107.671    0.000 {built-in method builtins.getattr}
               11069058  106.993    0.000  106.993    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               45596993  100.713    0.000  100.713    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               11069058   98.878    0.000   98.878    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                1573549    2.467    0.000   98.877    0.000 game.py:38(board)
               11564100   22.457    0.000   98.771    0.000 layers.py:838(isFree)
                 115641   34.077    0.000   92.124    0.001 agent.py:67(modify)
               11069058   85.711    0.000   85.711    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               75294134   64.762    0.000   82.544    0.000 types.py:171(__get__)
               11564100   80.237    0.000   80.237    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                 809494   45.086    0.000   79.198    0.000 layer.py:175(NoRock_update)
               72768980   62.866    0.000   76.314    0.000 layer.py:103(isFree)
                 116584    1.929    0.000   75.166    0.001 layers.py:849(restart)
                 995343   10.636    0.000   75.154    0.000 allGraphs.py:167(format)
              430082712   71.225    0.000   71.225    0.000 _jit_internal.py:750(is_scripting)
              142788192   70.503    0.000   70.503    0.000 {method 'dim' of 'torch._C._TensorBase' objects}
               11069058   69.963    0.000   69.963    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                1806296   68.884    0.000   68.884    0.000 {built-in method torch._C._nn.mse_loss}
                 346923    2.120    0.000   67.084    0.000 tensor.py:576(__iter__)
               10216212   64.119    0.000   64.119    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              165745035   63.872    0.000   63.872    0.000 tensor.py:24(<genexpr>)
                 346923   63.814    0.000   63.814    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}


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
Subject: Job 9653092: <Diamonds4_0.5_NN_cpu_2> in cluster <dcc> Exited

Job <Diamonds4_0.5_NN_cpu_2> was submitted from host <n-62-30-5> by user <s183905> in cluster <dcc> at Wed May 19 11:40:31 2021
Job was executed on host(s) <n-62-21-107>, in queue <hpc>, as user <s183905> in cluster <dcc> at Wed May 19 11:40:32 2021
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

    CPU time :                                   35702.37 sec.
    Max Memory :                                 109 MB
    Average Memory :                             103.59 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               16275.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   35709 sec.
    Turnaround time :                            35708 sec.

The output (if any) is above this job summary.

/zhome/ee/d/137643/Desktop/Bachelor/project-env/lib/python3.8/site-packages/torch/cuda/__init__.py:52: UserWarning: CUDA initialization: Found no NVIDIA driver on your system. Please check that you have an NVIDIA GPU and installed a driver from http://www.nvidia.com/Download/index.aspx (Triggered internally at  /pytorch/c10/cuda/CUDAFunctions.cpp:100.)
  return torch._C._cuda_getDeviceCount() > 0

# Parameters

    Name :                      Diamonds4_0.5_NN_cpu-2
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
    Num :                       2
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling

Traceback (most recent call last):
  File "main.py", line 268, in <module>
    run(Defaults)
  File "/zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/auxillaries.py", line 133, in run
    (serverRun if isServer else Defaults.main).__call__(getvals(Defaults))
  File "/zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils/server.py", line 37, in serverRun
    profilingStats()
  File "/zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils/debug.py", line 59, in profilingStats
    p = Stats('stats')
  File "/appl/python/3.8.4/lib/python3.8/pstats.py", line 96, in __init__
    self.init(arg)
  File "/appl/python/3.8.4/lib/python3.8/pstats.py", line 110, in init
    self.load_stats(arg)
  File "/appl/python/3.8.4/lib/python3.8/pstats.py", line 123, in load_stats
    with open(arg, 'rb') as f:
FileNotFoundError: [Errno 2] No such file or directory: 'stats'

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9668374: <Diamonds4_0.5_NN_cpu_2> in cluster <dcc> Exited

Job <Diamonds4_0.5_NN_cpu_2> was submitted from host <n-62-30-8> by user <s183905> in cluster <dcc> at Wed May 19 22:55:26 2021
Job was executed on host(s) <n-62-11-67>, in queue <hpc>, as user <s183905> in cluster <dcc> at Wed May 19 22:55:27 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 19 22:55:27 2021
Terminated at Thu May 20 08:50:52 2021
Results reported at Thu May 20 08:50:52 2021

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

    CPU time :                                   35614.32 sec.
    Max Memory :                                 104 MB
    Average Memory :                             98.26 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               16280.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   35751 sec.
    Turnaround time :                            35726 sec.

The output (if any) is above this job summary.

