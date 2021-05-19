/zhome/ee/d/137643/Desktop/Bachelor/project-env/lib/python3.8/site-packages/torch/cuda/__init__.py:52: UserWarning: CUDA initialization: Found no NVIDIA driver on your system. Please check that you have an NVIDIA GPU and installed a driver from http://www.nvidia.com/Download/index.aspx (Triggered internally at  /pytorch/c10/cuda/CUDAFunctions.cpp:100.)
  return torch._C._cuda_getDeviceCount() > 0

# Parameters

    Name :                      Diamonds3_0.0_NN_cpu-2
    Main :                      graphTrain
    Level :                     Levels.Causal6
    Failed actions chance :     0.0
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


      12276285251 function calls (11752280047 primitive calls) in 35700.93 seconds

##    Ordered by: cumulative time
   List reduced from 442 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35700.934 35700.934 {built-in method builtins.exec}
                      1    0.001    0.001 35700.934 35700.934 <string>:1(<module>)
                      1   22.344   22.344 35700.933 35700.933 allGraphsTrain.py:13(graphTrain)
                 104561   17.358    0.000 27321.500    0.261 allGraphsTrain.py:40(<listcomp>)
                 548606    2.733    0.000 27298.757    0.050 allGraphs.py:179(getInterventionsmodel)
        43825372/391631 2356.983    0.000 25367.449    0.065 allGraphs.py:186(recursiveBEST)
        529329675/49374315 2774.089    0.000 22612.533    0.000 module.py:715(_call_impl)
               47995536  861.017    0.000 22140.419    0.000 container.py:115(forward)
               47786414  150.950    0.000 21528.698    0.000 BayesianNN.py:18(forward)
               41844638 1322.607    0.000 20259.231    0.000 BayesianNN.py:65(predict_no_convert)
              143359242  212.871    0.000 7500.500    0.000 dropout.py:57(forward)
              143359242  715.064    0.000 7287.629    0.000 functional.py:960(dropout)
              143777486  474.465    0.000 6994.774    0.000 linear.py:92(forward)
              143359242 6420.343    0.000 6420.343    0.000 {built-in method dropout}
              143777486  732.490    0.000 6347.636    0.000 functional.py:1669(linear)
              143777486 3242.169    0.000 3242.169    0.000 {built-in method addmm}
                 104561  794.705    0.008 3076.812    0.029 allGraphs.py:156(transformNot)
                4667558   63.338    0.000 2616.928    0.001 BayesianNN.py:61(predict)
                1274218   15.283    0.000 2447.439    0.002 BayesianNN.py:57(learn)
                1274218   19.361    0.000 2331.433    0.002 BayesianNN.py:21(learn)
              143986608  143.659    0.000 2115.545    0.000 activation.py:713(forward)
              143986608  240.232    0.000 1971.886    0.000 functional.py:1292(leaky_relu)
          772666/156975   59.807    0.000 1890.649    0.012 allGraphs.py:202(recursiveExplore)
                 104561    0.567    0.000 1869.599    0.018 agent.py:29(learn)
                 104561   20.312    0.000 1868.767    0.018 agent.py:117(_learn)
                 104561    8.065    0.000 1848.454    0.018 learner.py:42(Qlearn)
              143986608 1706.168    0.000 1706.168    0.000 {built-in method torch._C._nn.leaky_relu}
              143777486 1534.876    0.000 1534.876    0.000 {method 't' of 'torch._C._TensorBase' objects}
                1378779    9.391    0.000 1372.680    0.001 tensor.py:181(backward)
                1378779    5.971    0.000 1363.289    0.001 __init__.py:68(backward)
                1378779 1331.594    0.001 1331.594    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                 209122    0.767    0.000 1212.585    0.006 network.py:28(forward)
                1378779    9.722    0.000 1099.299    0.001 grad_mode.py:23(decorate_context)
                1378779   46.419    0.000 1071.140    0.001 adam.py:55(step)
                 418244    1.431    0.000 1051.547    0.003 conv.py:422(forward)
                 418244    1.522    0.000 1049.586    0.003 conv.py:414(_conv_forward)
                 418244 1047.843    0.003 1047.843    0.003 {built-in method conv2d}
               44153993  226.164    0.000 1036.529    0.000 tensor.py:506(__rsub__)
               55132898  256.640    0.000 1006.828    0.000 tensor.py:21(wrapped)
                 104561   10.352    0.000  863.002    0.008 allGraphsTrain.py:33(<listcomp>)
               10560762  409.979    0.000  852.659    0.000 allGraphs.py:114(states)
                1378779  214.582    0.000  832.323    0.001 functional.py:53(adam)
               44153993  810.365    0.000  810.365    0.000 {built-in method rsub}
              232043784  233.563    0.000  771.256    0.000 overrides.py:1070(has_torch_function)
                 104561    0.621    0.000  744.790    0.007 game.py:42(step)
                 104561    0.903    0.000  733.883    0.007 layers.py:827(step)
              115017600  727.973    0.000  727.973    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 104561    4.648    0.000  707.890    0.007 allGraphs.py:141(transform)
              388908941  259.552    0.000  616.106    0.000 {built-in method builtins.any}
                 104561    1.763    0.000  581.219    0.006 agent.py:112(__call__)
              529643358  541.626    0.000  541.626    0.000 {built-in method torch._C._get_tracing_state}
                5941776  359.151    0.000  494.193    0.000 BayesianNN.py:43(convert_data)
               44049432  474.976    0.000  474.976    0.000 {method 'gt' of 'torch._C._TensorBase' objects}
                 104561   12.988    0.000  428.060    0.004 layers.py:17(step)
               10456100   25.923    0.000  413.785    0.000 layer.py:106(move)
               59372632  215.923    0.000  348.657    0.000 tensor.py:933(grad)
              628276814  254.844    0.000  311.167    0.000 overrides.py:1083(<genexpr>)
                 104562   21.877    0.000  303.841    0.003 layers.py:793(update)
             2165314236  272.050    0.000  272.050    0.000 {method 'values' of 'collections.OrderedDict' objects}
               10456100   52.732    0.000  267.594    0.000 layers.py:844(check)
                1378779   30.607    0.000  260.944    0.000 optimizer.py:167(zero_grad)
              337661719  258.649    0.000  258.649    0.000 module.py:765(__getattr__)
              126748750  241.440    0.000  241.440    0.000 {method 'item' of 'torch._C._TensorBase' objects}
        1321581821/1321581819  216.985    0.000  219.821    0.000 {built-in method builtins.len}
               16963592  201.957    0.000  201.957    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               48204658   40.205    0.000  179.964    0.000 flatten.py:39(forward)
               58660758  177.794    0.000  177.794    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                 104561   12.095    0.000  166.419    0.002 allGraphsTrain.py:51(<listcomp>)
               65589098   56.908    0.000  154.768    0.000 {built-in method builtins.all}
                 104561   19.597    0.000  149.666    0.001 allGraphsTrain.py:44(<listcomp>)
              144738021   92.078    0.000  127.569    0.000 _VF.py:25(__getattr__)
               16963592  126.969    0.000  126.969    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              143777486  111.351    0.000  111.351    0.000 functional.py:1686(<listcomp>)
               11883553  103.411    0.000  103.411    0.000 {built-in method zeros}
               46721318  102.896    0.000  102.896    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               10456100   24.308    0.000   98.076    0.000 layers.py:838(isFree)
                 126087    2.040    0.000   93.919    0.001 layers.py:849(restart)
               10978905   93.873    0.000   93.873    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
              376888465   91.951    0.000   91.951    0.000 {built-in method builtins.getattr}
              245846566   62.752    0.000   91.124    0.000 enum.py:646(__hash__)
                1378779    2.615    0.000   90.513    0.000 loss.py:445(forward)
                1378779    9.598    0.000   87.898    0.000 functional.py:2637(mse_loss)
                8481796   83.697    0.000   83.697    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                 104561   30.548    0.000   81.142    0.001 agent.py:67(modify)
               71342409   63.556    0.000   79.684    0.000 types.py:171(__get__)
                 126087    1.012    0.000   78.067    0.001 level.py:8(__init__)
                8481796   78.060    0.000   78.060    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                 836496   41.665    0.000   74.640    0.000 layer.py:175(NoRock_update)
              144823216   73.890    0.000   73.890    0.000 {method 'dim' of 'torch._C._TensorBase' objects}
               79001416   59.474    0.000   73.768    0.000 layer.py:103(isFree)
              435259793   73.357    0.000   73.357    0.000 _jit_internal.py:750(is_scripting)
                1542818   72.327    0.000   72.327    0.000 {built-in method tensor}
               10456100   70.465    0.000   70.465    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                 126087    2.752    0.000   69.531    0.001 levels.py:303(generate)
                8481796   68.008    0.000   68.008    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                 755846   11.007    0.000   64.018    0.000 level.py:41(notUsed)
               10456100   39.191    0.000   63.556    0.000 layers.py:424(check)
              165398694   63.336    0.000   63.336    0.000 tensor.py:24(<genexpr>)
               47995536   43.900    0.000   62.709    0.000 container.py:107(__iter__)
                1071412    1.598    0.000   59.358    0.000 game.py:38(board)


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
Subject: Job 9653101: <Diamonds3_0.0_NN_cpu_2> in cluster <dcc> Exited

Job <Diamonds3_0.0_NN_cpu_2> was submitted from host <n-62-30-5> by user <s183905> in cluster <dcc> at Wed May 19 11:40:33 2021
Job was executed on host(s) <n-62-21-107>, in queue <hpc>, as user <s183905> in cluster <dcc> at Wed May 19 11:40:33 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 19 11:40:33 2021
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

    CPU time :                                   35703.75 sec.
    Max Memory :                                 106 MB
    Average Memory :                             99.27 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               16278.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   35709 sec.
    Turnaround time :                            35709 sec.

The output (if any) is above this job summary.

