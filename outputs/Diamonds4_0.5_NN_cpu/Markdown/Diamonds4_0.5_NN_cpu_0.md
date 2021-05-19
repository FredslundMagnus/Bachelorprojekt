/zhome/ee/d/137643/Desktop/Bachelor/project-env/lib/python3.8/site-packages/torch/cuda/__init__.py:52: UserWarning: CUDA initialization: Found no NVIDIA driver on your system. Please check that you have an NVIDIA GPU and installed a driver from http://www.nvidia.com/Download/index.aspx (Triggered internally at  /pytorch/c10/cuda/CUDAFunctions.cpp:100.)
  return torch._C._cuda_getDeviceCount() > 0

# Parameters

    Name :                      Diamonds4_0.5_NN_cpu-0
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
    Num :                       0
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      11703439016 function calls (11206147238 primitive calls) in 35700.72 seconds

##    Ordered by: cumulative time
   List reduced from 443 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35700.716 35700.716 {built-in method builtins.exec}
                      1    0.001    0.001 35700.716 35700.716 <string>:1(<module>)
                      1   31.276   31.276 35700.714 35700.714 allGraphsTrain.py:13(graphTrain)
                 116777   24.895    0.000 26804.455    0.230 allGraphsTrain.py:40(<listcomp>)
                 968078    5.780    0.000 26769.375    0.028 allGraphs.py:179(getInterventionsmodel)
        41594895/765697 2233.485    0.000 24841.927    0.032 allGraphs.py:186(recursiveBEST)
        503256225/47367025 2804.137    0.000 22518.439    0.000 module.py:715(_call_impl)
               45588920  823.641    0.000 21997.114    0.000 container.py:115(forward)
               45355366  170.593    0.000 21456.041    0.000 BayesianNN.py:18(forward)
               38566480 1204.792    0.000 19466.244    0.001 BayesianNN.py:65(predict_no_convert)
              136066098  209.620    0.000 7493.948    0.000 dropout.py:57(forward)
              136066098  729.518    0.000 7284.328    0.000 functional.py:960(dropout)
              136533206  447.162    0.000 6970.168    0.000 linear.py:92(forward)
              136066098 6399.317    0.000 6399.317    0.000 {built-in method dropout}
              136533206  746.834    0.000 6350.294    0.000 functional.py:1669(linear)
                 116777  727.172    0.006 3802.941    0.033 allGraphs.py:156(transformNot)
              136533206 3260.645    0.000 3260.645    0.000 {built-in method addmm}
                1661328   22.469    0.000 3256.292    0.002 BayesianNN.py:57(learn)
                1661328   28.246    0.000 3099.823    0.002 BayesianNN.py:21(learn)
                5127558   71.191    0.000 2998.535    0.001 BayesianNN.py:61(predict)
              136766760  150.098    0.000 2052.383    0.000 activation.py:713(forward)
                 116777    0.794    0.000 1925.909    0.016 agent.py:29(learn)
                 116777   14.940    0.000 1924.782    0.016 agent.py:117(_learn)
                 116777   10.115    0.000 1909.842    0.016 learner.py:42(Qlearn)
              136766760  250.588    0.000 1902.284    0.000 functional.py:1292(leaky_relu)
          775349/202381   58.123    0.000 1835.101    0.009 allGraphs.py:202(recursiveExplore)
              136766760 1627.720    0.000 1627.720    0.000 {built-in method torch._C._nn.leaky_relu}
                1778105   14.477    0.000 1578.998    0.001 tensor.py:181(backward)
                1778105    8.783    0.000 1564.521    0.001 __init__.py:68(backward)
              136533206 1552.983    0.000 1552.983    0.000 {method 't' of 'torch._C._TensorBase' objects}
                1778105 1517.729    0.001 1517.729    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                1778105   14.408    0.000 1374.208    0.001 grad_mode.py:23(decorate_context)
                1778105   63.596    0.000 1332.367    0.001 adam.py:55(step)
                 233554    1.023    0.000 1159.916    0.005 network.py:28(forward)
                1778105  265.760    0.000 1022.943    0.001 functional.py:53(adam)
               53780528  252.001    0.000 1017.678    0.000 tensor.py:21(wrapped)
               41518943  220.260    0.000 1000.152    0.000 tensor.py:506(__rsub__)
                 467108    1.845    0.000  979.981    0.002 conv.py:422(forward)
                 467108    1.986    0.000  977.474    0.002 conv.py:414(_conv_forward)
                 467108  975.226    0.002  975.226    0.002 {built-in method conv2d}
              247277054  243.662    0.000  786.780    0.000 overrides.py:1070(has_torch_function)
               41518943  779.892    0.000  779.892    0.000 {built-in method rsub}
                 116777   10.267    0.000  718.837    0.006 allGraphsTrain.py:33(<listcomp>)
               11794578  346.180    0.000  708.577    0.000 allGraphs.py:114(states)
                 116777    5.648    0.000  647.020    0.006 allGraphs.py:141(transform)
              398927995  268.532    0.000  618.947    0.000 {built-in method builtins.any}
                 116777    0.805    0.000  612.933    0.005 game.py:42(step)
                 116777    1.157    0.000  598.470    0.005 layers.py:827(step)
              105099700  592.557    0.000  592.557    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
              503606556  589.070    0.000  589.070    0.000 {built-in method torch._C._get_tracing_state}
                 116777    2.662    0.000  575.376    0.005 agent.py:112(__call__)
                6788886  396.797    0.000  558.235    0.000 BayesianNN.py:43(convert_data)
               41402166  475.403    0.000  475.403    0.000 {method 'gt' of 'torch._C._TensorBase' objects}
               76315348  266.067    0.000  438.365    0.000 tensor.py:933(grad)
                1778105   38.048    0.000  326.979    0.000 optimizer.py:167(zero_grad)
                 116777   15.386    0.000  318.479    0.003 layers.py:17(step)
              654613520  253.260    0.000  305.619    0.000 overrides.py:1083(<genexpr>)
               11677700   29.181    0.000  301.601    0.000 layer.py:106(move)
                 116778   24.464    0.000  277.248    0.002 layers.py:793(update)
             2058613820  271.513    0.000  271.513    0.000 {method 'values' of 'collections.OrderedDict' objects}
              321251403  253.412    0.000  253.412    0.000 module.py:765(__getattr__)
               21804368  245.506    0.000  245.506    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
        1255177529/1255177527  217.404    0.000  220.478    0.000 {built-in method builtins.len}
              118439656  214.011    0.000  214.011    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                 116777   13.880    0.000  182.038    0.002 allGraphsTrain.py:51(<listcomp>)
               45822474   41.506    0.000  178.763    0.000 flatten.py:39(forward)
               57500174  178.406    0.000  178.406    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                 116777   21.366    0.000  158.846    0.001 allGraphsTrain.py:44(<listcomp>)
               21804368  153.344    0.000  153.344    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               11677700   37.577    0.000  142.676    0.000 layers.py:844(check)
              137844203   98.314    0.000  133.912    0.000 _VF.py:25(__getattr__)
               65458328   54.263    0.000  132.430    0.000 {built-in method builtins.all}
                1778105    4.247    0.000  127.837    0.000 loss.py:445(forward)
               13577773  124.199    0.000  124.199    0.000 {built-in method zeros}
                1778105   14.342    0.000  123.589    0.000 functional.py:2637(mse_loss)
                2074523  122.920    0.000  122.920    0.000 {built-in method tensor}
              136533206  114.908    0.000  114.908    0.000 functional.py:1686(<listcomp>)
                1551964    2.633    0.000  108.960    0.000 game.py:38(board)
               10902184  105.390    0.000  105.390    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               11677700   24.458    0.000  104.069    0.000 layers.py:838(isFree)
               12261585  102.992    0.000  102.992    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               10902184   98.590    0.000   98.590    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                 116777   34.747    0.000   94.446    0.001 agent.py:67(modify)
               43927592   93.467    0.000   93.467    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
              385232414   88.064    0.000   88.064    0.000 {built-in method builtins.getattr}
                 968078   13.941    0.000   85.832    0.000 allGraphs.py:167(format)
               72751442   65.386    0.000   83.624    0.000 types.py:171(__get__)
               10902184   82.444    0.000   82.444    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                 817446   44.808    0.000   80.191    0.000 layer.py:175(NoRock_update)
               80097353   65.728    0.000   79.611    0.000 layer.py:103(isFree)
                 116275    1.947    0.000   76.140    0.001 layers.py:849(restart)
               11677700   73.346    0.000   73.346    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                1778105   72.774    0.000   72.774    0.000 {built-in method torch._C._nn.mse_loss}
                 350331    2.204    0.000   70.738    0.000 tensor.py:576(__iter__)
               10902184   67.911    0.000   67.911    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                 350331   67.291    0.000   67.291    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
              414700499   67.143    0.000   67.143    0.000 _jit_internal.py:750(is_scripting)
                9946481   66.844    0.000   66.844    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              161341584   62.330    0.000   62.330    0.000 tensor.py:24(<genexpr>)
              137701096   61.417    0.000   61.417    0.000 {method 'dim' of 'torch._C._TensorBase' objects}


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
Subject: Job 9653090: <Diamonds4_0.5_NN_cpu_0> in cluster <dcc> Exited

Job <Diamonds4_0.5_NN_cpu_0> was submitted from host <n-62-30-5> by user <s183905> in cluster <dcc> at Wed May 19 11:40:30 2021
Job was executed on host(s) <n-62-21-108>, in queue <hpc>, as user <s183905> in cluster <dcc> at Wed May 19 11:40:32 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 19 11:40:32 2021
Terminated at Wed May 19 21:35:40 2021
Results reported at Wed May 19 21:35:40 2021

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

    CPU time :                                   35687.60 sec.
    Max Memory :                                 106 MB
    Average Memory :                             100.52 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               16278.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   35791 sec.
    Turnaround time :                            35710 sec.

The output (if any) is above this job summary.

