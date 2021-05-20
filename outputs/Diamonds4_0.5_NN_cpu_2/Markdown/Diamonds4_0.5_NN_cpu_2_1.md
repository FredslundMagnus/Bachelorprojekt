/zhome/ee/d/137643/Desktop/Bachelor/project-env/lib/python3.8/site-packages/torch/cuda/__init__.py:52: UserWarning: CUDA initialization: Found no NVIDIA driver on your system. Please check that you have an NVIDIA GPU and installed a driver from http://www.nvidia.com/Download/index.aspx (Triggered internally at  /pytorch/c10/cuda/CUDAFunctions.cpp:100.)
  return torch._C._cuda_getDeviceCount() > 0

# Parameters

    Name :                      Diamonds4_0.5_NN_cpu_2-1
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


      12424716921 function calls (12192190526 primitive calls) in 35700.32 seconds

##    Ordered by: cumulative time
   List reduced from 442 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35700.322 35700.322 {built-in method builtins.exec}
                      1    0.001    0.001 35700.322 35700.322 <string>:1(<module>)
                      1   82.165   82.165 35700.321 35700.321 allGraphsTrain.py:13(graphTrain)
        247075750/27941770 1371.912    0.000 13245.309    0.000 module.py:715(_call_impl)
               21913398  407.833    0.000 12582.883    0.001 container.py:115(forward)
                 282463 1831.277    0.006 11231.983    0.040 allGraphs.py:156(transformNot)
                5745909   67.989    0.000 10804.231    0.002 BayesianNN.py:57(learn)
                 282463   66.445    0.000 10705.250    0.038 allGraphsTrain.py:40(<listcomp>)
                4445148   19.337    0.000 10600.087    0.002 allGraphs.py:179(getInterventionsmodel)
                5745909   85.602    0.000 10275.139    0.002 BayesianNN.py:21(learn)
               21348472   83.295    0.000 9934.236    0.000 BayesianNN.py:18(forward)
               15602563  206.045    0.000 8682.438    0.001 BayesianNN.py:61(predict)
        17091567/4252204  870.282    0.000 8594.026    0.002 allGraphs.py:186(recursiveBEST)
                 282463    2.139    0.000 4651.278    0.016 agent.py:29(learn)
                 282463   41.963    0.000 4648.375    0.016 agent.py:117(_learn)
                 282463   24.607    0.000 4606.413    0.016 learner.py:42(Qlearn)
                6028372   42.454    0.000 4535.716    0.001 grad_mode.py:23(decorate_context)
                6028372  199.473    0.000 4410.798    0.001 adam.py:55(step)
                6028372   42.909    0.000 4196.964    0.001 tensor.py:181(backward)
                6028372   26.457    0.000 4154.054    0.001 __init__.py:68(backward)
                6028372 4014.851    0.001 4014.851    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               64045416   86.894    0.000 3417.585    0.000 dropout.py:57(forward)
                6028372  867.013    0.000 3408.491    0.001 functional.py:53(adam)
               65175268  205.289    0.000 3400.963    0.000 linear.py:92(forward)
               64045416  322.713    0.000 3330.690    0.000 functional.py:960(dropout)
               65175268  370.385    0.000 3113.014    0.000 functional.py:1669(linear)
                 564926    2.668    0.000 2956.136    0.005 network.py:28(forward)
               64045416 2936.586    0.000 2936.586    0.000 {built-in method dropout}
                 282463   17.097    0.000 2640.684    0.009 allGraphs.py:141(transform)
                1129852    4.218    0.000 2495.151    0.002 conv.py:422(forward)
                1129852    4.588    0.000 2489.468    0.002 conv.py:414(_conv_forward)
                1129852 2484.264    0.002 2484.264    0.002 {built-in method conv2d}
                 282463   49.806    0.000 1880.628    0.007 allGraphsTrain.py:33(<listcomp>)
               28528864  885.989    0.000 1830.828    0.000 allGraphs.py:114(states)
          745584/192944   53.654    0.000 1705.799    0.009 allGraphs.py:202(recursiveExplore)
               21348472 1224.935    0.000 1692.504    0.000 BayesianNN.py:43(convert_data)
               65175268 1631.104    0.000 1631.104    0.000 {built-in method addmm}
                 282463    1.964    0.000 1590.153    0.006 game.py:42(step)
              254217100 1584.729    0.000 1584.729    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 282463    2.643    0.000 1555.010    0.006 layers.py:827(step)
                 282463    6.434    0.000 1493.967    0.005 agent.py:112(__call__)
              257146166  865.883    0.000 1436.545    0.000 tensor.py:933(grad)
               65740194   74.794    0.000 1127.613    0.000 activation.py:713(forward)
                6028372  125.522    0.000 1073.081    0.000 optimizer.py:167(zero_grad)
               65740194  120.479    0.000 1052.819    0.000 functional.py:1292(leaky_relu)
              393442928  316.807    0.000  960.316    0.000 overrides.py:1070(has_torch_function)
               65740194  920.136    0.000  920.136    0.000 {built-in method torch._C._nn.leaky_relu}
               73470316  836.105    0.000  836.105    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                 282464   58.864    0.000  775.588    0.003 layers.py:793(update)
                 282463   36.697    0.000  772.774    0.003 layers.py:17(step)
              498501250  294.602    0.000  764.386    0.000 {built-in method builtins.any}
               43333081  173.068    0.000  751.199    0.000 tensor.py:21(wrapped)
               28246300   70.738    0.000  732.292    0.000 layer.py:106(move)
               65175268  716.857    0.000  716.857    0.000 {method 't' of 'torch._C._TensorBase' objects}
              288211565  539.664    0.000  539.664    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               73470316  520.781    0.000  520.781    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                 282463   31.240    0.000  434.203    0.002 allGraphsTrain.py:51(<listcomp>)
                 282463   53.175    0.000  407.656    0.001 allGraphsTrain.py:44(<listcomp>)
                6028372   11.686    0.000  405.461    0.000 loss.py:445(forward)
                6028372   45.612    0.000  393.775    0.000 functional.py:2637(mse_loss)
              886447350  293.239    0.000  360.434    0.000 overrides.py:1083(<genexpr>)
               42696945  354.322    0.000  354.322    0.000 {built-in method zeros}
               36735158  348.823    0.000  348.823    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               28246300   89.979    0.000  346.475    0.000 layers.py:844(check)
                7076027  345.476    0.000  345.476    0.000 {built-in method tensor}
               13674466   72.954    0.000  332.336    0.000 tensor.py:506(__rsub__)
               36735158  325.720    0.000  325.720    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                5857464    8.330    0.000  316.663    0.000 game.py:38(board)
                4445148   46.793    0.000  279.154    0.000 allGraphs.py:167(format)
              247923139  273.135    0.000  273.135    0.000 {built-in method torch._C._get_tracing_state}
               36735158  269.763    0.000  269.763    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                 420090    6.331    0.000  267.070    0.001 layers.py:849(restart)
               13674466  259.382    0.000  259.382    0.000 {built-in method rsub}
               28246300   57.023    0.000  250.067    0.000 layers.py:838(isFree)
               29658615  242.918    0.000  242.918    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                6028372  234.326    0.000  234.326    0.000 {built-in method torch._C._nn.mse_loss}
                 282463   88.015    0.000  231.279    0.001 agent.py:67(modify)
               36735158  227.595    0.000  227.595    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                 420090    3.388    0.000  216.278    0.001 level.py:8(__init__)
                1977248  112.663    0.000  196.937    0.000 layer.py:175(NoRock_update)
              183338908  158.287    0.000  193.044    0.000 layer.py:103(isFree)
               28246300  190.565    0.000  190.565    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                 420090    7.911    0.000  187.456    0.000 levels.py:456(generate)
               29047050  183.730    0.000  183.730    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               50724624  178.153    0.000  178.153    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                 847389    5.209    0.000  173.125    0.000 tensor.py:576(__iter__)
                2016826   30.605    0.000  171.808    0.000 level.py:41(notUsed)
                 847389  165.069    0.000  165.069    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               13392003  163.901    0.000  163.901    0.000 {method 'gt' of 'torch._C._TensorBase' objects}
               71579481   45.298    0.000  161.417    0.000 {built-in method builtins.all}
              401476773  109.841    0.000  161.007    0.000 enum.py:646(__hash__)
               36735268   63.494    0.000  143.370    0.000 tensor.py:596(__hash__)
             1010216398  141.483    0.000  141.483    0.000 {method 'values' of 'collections.OrderedDict' objects}
        855635311/855635309  132.178    0.000  139.433    0.000 {built-in method builtins.len}
              160270448  130.474    0.000  130.474    0.000 module.py:765(__getattr__)
               36735158  109.336    0.000  109.336    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                6028372   32.851    0.000  105.261    0.000 __init__.py:28(_make_grads)
              222610480   86.744    0.000  103.896    0.000 layers.py:809(<genexpr>)
              105338701   77.096    0.000   98.111    0.000 types.py:171(__get__)
               22478324   18.923    0.000   91.731    0.000 flatten.py:39(forward)


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
Subject: Job 9668399: <Diamonds4_0.5_NN_cpu_2_1> in cluster <dcc> Exited

Job <Diamonds4_0.5_NN_cpu_2_1> was submitted from host <n-62-30-8> by user <s183905> in cluster <dcc> at Wed May 19 22:59:00 2021
Job was executed on host(s) <n-62-21-108>, in queue <hpc>, as user <s183905> in cluster <dcc> at Wed May 19 22:59:01 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 19 22:59:01 2021
Terminated at Thu May 20 08:54:05 2021
Results reported at Thu May 20 08:54:05 2021

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

    CPU time :                                   35696.91 sec.
    Max Memory :                                 108 MB
    Average Memory :                             100.82 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               16276.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   35733 sec.
    Turnaround time :                            35705 sec.

The output (if any) is above this job summary.

