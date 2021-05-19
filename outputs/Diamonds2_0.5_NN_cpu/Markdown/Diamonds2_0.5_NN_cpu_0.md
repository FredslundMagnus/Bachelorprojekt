/zhome/ee/d/137643/Desktop/Bachelor/project-env/lib/python3.8/site-packages/torch/cuda/__init__.py:52: UserWarning: CUDA initialization: Found no NVIDIA driver on your system. Please check that you have an NVIDIA GPU and installed a driver from http://www.nvidia.com/Download/index.aspx (Triggered internally at  /pytorch/c10/cuda/CUDAFunctions.cpp:100.)
  return torch._C._cuda_getDeviceCount() > 0

# Parameters

    Name :                      Diamonds2_0.5_NN_cpu-0
    Main :                      graphTrain
    Level :                     Levels.Causal5
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
    Num :                       0
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      11565527621 function calls (11058990795 primitive calls) in 35700.71 seconds

##    Ordered by: cumulative time
   List reduced from 444 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35700.706 35700.706 {built-in method builtins.exec}
                      1    0.001    0.001 35700.706 35700.706 <string>:1(<module>)
                      1   25.867   25.867 35700.705 35700.705 allGraphsTrain.py:13(graphTrain)
                  92572   18.157    0.000 27554.443    0.298 allGraphsTrain.py:40(<listcomp>)
                 586167    3.480    0.000 27529.443    0.047 allGraphs.py:179(getInterventionsmodel)
        41181538/363899 2298.053    0.000 24717.408    0.068 allGraphs.py:186(recursiveBEST)
        512698470/47827090 2749.027    0.000 22648.975    0.000 module.py:715(_call_impl)
               46487138  854.642    0.000 22181.564    0.000 container.py:115(forward)
               46301994  150.070    0.000 21618.755    0.000 BayesianNN.py:18(forward)
               39396720 1268.988    0.000 19743.688    0.001 BayesianNN.py:65(predict_no_convert)
              138905982  188.834    0.000 7565.759    0.000 dropout.py:57(forward)
              138905982  703.094    0.000 7376.925    0.000 functional.py:960(dropout)
              139276270  436.971    0.000 6981.042    0.000 linear.py:92(forward)
              138905982 6520.990    0.000 6520.990    0.000 {built-in method dropout}
              139276270  738.839    0.000 6368.636    0.000 functional.py:1669(linear)
                  92572  832.696    0.009 3426.866    0.037 allGraphs.py:156(transformNot)
                5657894   78.531    0.000 3361.496    0.001 BayesianNN.py:61(predict)
              139276270 3285.990    0.000 3285.990    0.000 {built-in method addmm}
         1069663/222268   84.283    0.000 2750.937    0.012 allGraphs.py:202(recursiveExplore)
                1247380   15.365    0.000 2505.595    0.002 BayesianNN.py:57(learn)
                1247380   19.869    0.000 2362.176    0.002 BayesianNN.py:21(learn)
              139461414  143.515    0.000 2171.432    0.000 activation.py:713(forward)
              139461414  238.218    0.000 2027.917    0.000 functional.py:1292(leaky_relu)
              139461414 1764.613    0.000 1764.613    0.000 {built-in method torch._C._nn.leaky_relu}
                  92572    0.604    0.000 1744.755    0.019 agent.py:29(learn)
                  92572   23.300    0.000 1743.833    0.019 agent.py:117(_learn)
                  92572    8.106    0.000 1720.533    0.019 learner.py:42(Qlearn)
              139276270 1512.793    0.000 1512.793    0.000 {method 't' of 'torch._C._TensorBase' objects}
                1339952    9.623    0.000 1282.452    0.001 tensor.py:181(backward)
                1339952    6.295    0.000 1272.829    0.001 __init__.py:68(backward)
                1339952 1240.287    0.001 1240.287    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                 185144    0.787    0.000 1155.769    0.006 network.py:28(forward)
                1339952    9.602    0.000 1124.111    0.001 grad_mode.py:23(decorate_context)
                1339952   44.685    0.000 1095.463    0.001 adam.py:55(step)
               41757606  196.767    0.000 1031.194    0.000 tensor.py:506(__rsub__)
                 370288    1.419    0.000  998.973    0.003 conv.py:422(forward)
                 370288    1.493    0.000  997.045    0.003 conv.py:414(_conv_forward)
                 370288  995.352    0.003  995.352    0.003 {built-in method conv2d}
               51477666  249.259    0.000  984.760    0.000 tensor.py:21(wrapped)
                  92572   14.902    0.000  877.637    0.009 allGraphsTrain.py:33(<listcomp>)
                1339952  216.657    0.000  868.293    0.001 functional.py:53(adam)
                9349873  413.470    0.000  862.746    0.000 allGraphs.py:114(states)
               41757606  834.427    0.000  834.427    0.000 {built-in method rsub}
              223409333  233.436    0.000  749.698    0.000 overrides.py:1070(has_torch_function)
              120344200  731.091    0.000  731.091    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                6905274  532.785    0.000  706.772    0.000 BayesianNN.py:43(convert_data)
              374555142  250.538    0.000  587.334    0.000 {built-in method builtins.any}
                  92572    0.610    0.000  564.844    0.006 game.py:42(step)
                  92572    1.860    0.000  562.540    0.006 agent.py:112(__call__)
              512976186  560.220    0.000  560.220    0.000 {built-in method torch._C._get_tracing_state}
                  92572    0.898    0.000  552.850    0.006 layers.py:827(step)
               41665034  472.961    0.000  472.961    0.000 {method 'gt' of 'torch._C._TensorBase' objects}
                  92572    4.166    0.000  460.283    0.005 allGraphs.py:141(transform)
               57574052  202.770    0.000  331.276    0.000 tensor.py:933(grad)
                  92572   12.085    0.000  302.833    0.003 layers.py:17(step)
              604428981  239.315    0.000  293.320    0.000 overrides.py:1083(<genexpr>)
                9257200   22.627    0.000  289.494    0.000 layer.py:106(move)
             2097281018  272.435    0.000  272.435    0.000 {method 'values' of 'collections.OrderedDict' objects}
              327028117  260.394    0.000  260.394    0.000 module.py:765(__getattr__)
                1339952   28.532    0.000  251.891    0.000 optimizer.py:167(zero_grad)
                  92573   19.140    0.000  247.875    0.003 layers.py:793(update)
              130849516  244.491    0.000  244.491    0.000 {method 'item' of 'torch._C._TensorBase' objects}
        1271239769/1271239767  223.374    0.000  225.814    0.000 {built-in method builtins.len}
               16449712  211.910    0.000  211.910    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               46672282   35.851    0.000  174.041    0.000 flatten.py:39(forward)
               55929482  171.520    0.000  171.520    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                  92572   11.377    0.000  159.790    0.002 allGraphsTrain.py:51(<listcomp>)
                9257200   37.313    0.000  150.942    0.000 layers.py:844(check)
               60734966   54.156    0.000  138.421    0.000 {built-in method builtins.all}
               16449712  131.824    0.000  131.824    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                  92572   17.348    0.000  129.123    0.001 allGraphsTrain.py:44(<listcomp>)
              140245934   90.795    0.000  128.611    0.000 _VF.py:25(__getattr__)
               13810549  128.217    0.000  128.217    0.000 {built-in method zeros}
              139276270  114.936    0.000  114.936    0.000 functional.py:1686(<listcomp>)
               45239758  102.840    0.000  102.840    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                9257200   25.533    0.000   95.334    0.000 layers.py:838(isFree)
                9720060   92.938    0.000   92.938    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                1469892   92.728    0.000   92.728    0.000 {built-in method tensor}
                8224856   91.974    0.000   91.974    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              363756836   91.923    0.000   91.923    0.000 {built-in method builtins.getattr}
                1339952    3.002    0.000   91.676    0.000 loss.py:445(forward)
               86831540   70.829    0.000   91.308    0.000 types.py:171(__get__)
                1339952    9.882    0.000   88.675    0.000 functional.py:2637(mse_loss)
              140202110   81.626    0.000   81.626    0.000 {method 'dim' of 'torch._C._TensorBase' objects}
                1049028    1.786    0.000   80.894    0.000 game.py:38(board)
                8224856   80.148    0.000   80.148    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                3574724   75.900    0.000   75.900    0.000 {built-in method cat}
                  92572   26.783    0.000   75.742    0.001 agent.py:67(modify)
                 833157   41.567    0.000   74.994    0.000 layer.py:175(NoRock_update)
                8224856   74.185    0.000   74.185    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              421663642   71.623    0.000   71.623    0.000 _jit_internal.py:750(is_scripting)
               78724977   56.660    0.000   69.800    0.000 layer.py:103(isFree)
               10125160   62.527    0.000   62.527    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                9257200   60.083    0.000   60.083    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
              154432998   59.914    0.000   59.914    0.000 tensor.py:24(<genexpr>)
              152806222   41.110    0.000   59.848    0.000 enum.py:646(__hash__)
                8224856   58.308    0.000   58.308    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                 586167    9.120    0.000   57.277    0.000 allGraphs.py:167(format)
               46487138   39.218    0.000   56.548    0.000 container.py:107(__iter__)
                  67665    1.246    0.000   55.378    0.001 layers.py:849(restart)


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
Subject: Job 9653084: <Diamonds2_0.5_NN_cpu_0> in cluster <dcc> Exited

Job <Diamonds2_0.5_NN_cpu_0> was submitted from host <n-62-30-5> by user <s183905> in cluster <dcc> at Wed May 19 11:40:29 2021
Job was executed on host(s) <n-62-21-107>, in queue <hpc>, as user <s183905> in cluster <dcc> at Wed May 19 11:40:30 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 19 11:40:30 2021
Terminated at Wed May 19 21:35:42 2021
Results reported at Wed May 19 21:35:42 2021

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

    CPU time :                                   35703.07 sec.
    Max Memory :                                 111 MB
    Average Memory :                             105.32 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               16273.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   35709 sec.
    Turnaround time :                            35713 sec.

The output (if any) is above this job summary.

