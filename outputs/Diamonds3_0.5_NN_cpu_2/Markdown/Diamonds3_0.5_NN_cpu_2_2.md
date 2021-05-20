/zhome/ee/d/137643/Desktop/Bachelor/project-env/lib/python3.8/site-packages/torch/cuda/__init__.py:52: UserWarning: CUDA initialization: Found no NVIDIA driver on your system. Please check that you have an NVIDIA GPU and installed a driver from http://www.nvidia.com/Download/index.aspx (Triggered internally at  /pytorch/c10/cuda/CUDAFunctions.cpp:100.)
  return torch._C._cuda_getDeviceCount() > 0

# Parameters

    Name :                      Diamonds3_0.5_NN_cpu_2-2
    Main :                      graphTrain
    Level :                     Levels.Causal6
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


      12445087636 function calls (12211564477 primitive calls) in 35700.25 seconds

##    Ordered by: cumulative time
   List reduced from 443 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35700.254 35700.254 {built-in method builtins.exec}
                      1    0.001    0.001 35700.254 35700.254 <string>:1(<module>)
                      1   75.175   75.175 35700.253 35700.253 allGraphsTrain.py:13(graphTrain)
        247978976/28047416 1369.758    0.000 13154.453    0.000 module.py:715(_call_impl)
               21993156  413.019    0.000 12504.220    0.001 container.py:115(forward)
                 284689 1920.106    0.007 11413.162    0.040 allGraphs.py:156(transformNot)
                5769571   69.163    0.000 10856.227    0.002 BayesianNN.py:57(learn)
                 284689   68.744    0.000 10732.296    0.038 allGraphsTrain.py:40(<listcomp>)
                4499520   20.092    0.000 10623.825    0.002 allGraphs.py:179(getInterventionsmodel)
                5769571   88.301    0.000 10317.090    0.002 BayesianNN.py:21(learn)
               21423778   76.308    0.000 9951.186    0.000 BayesianNN.py:18(forward)
        17395569/4320137  890.276    0.000 8730.205    0.002 allGraphs.py:186(recursiveBEST)
               15654207  213.145    0.000 8698.349    0.001 BayesianNN.py:61(predict)
                 284689    2.159    0.000 4643.184    0.016 agent.py:29(learn)
                 284689   46.429    0.000 4640.211    0.016 agent.py:117(_learn)
                6054260   44.007    0.000 4594.431    0.001 grad_mode.py:23(decorate_context)
                 284689   25.750    0.000 4593.782    0.016 learner.py:42(Qlearn)
                6054260  201.036    0.000 4468.089    0.001 adam.py:55(step)
                6054260   42.636    0.000 4200.820    0.001 tensor.py:181(backward)
                6054260   26.624    0.000 4158.184    0.001 __init__.py:68(backward)
                6054260 4013.544    0.001 4013.544    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                6054260  891.470    0.000 3454.280    0.001 functional.py:53(adam)
               64271334   88.132    0.000 3435.851    0.000 dropout.py:57(forward)
               65410090  213.454    0.000 3407.580    0.000 linear.py:92(forward)
               64271334  330.310    0.000 3347.720    0.000 functional.py:960(dropout)
               65410090  352.664    0.000 3110.198    0.000 functional.py:1669(linear)
               64271334 2942.429    0.000 2942.429    0.000 {built-in method dropout}
                 569378    2.529    0.000 2857.103    0.005 network.py:28(forward)
                 284689   16.767    0.000 2616.003    0.009 allGraphs.py:141(transform)
                1138756    4.366    0.000 2400.255    0.002 conv.py:422(forward)
                1138756    4.625    0.000 2394.339    0.002 conv.py:414(_conv_forward)
                1138756 2389.073    0.002 2389.073    0.002 {built-in method conv2d}
                 284689   29.734    0.000 1803.790    0.006 allGraphsTrain.py:33(<listcomp>)
               28753690  870.547    0.000 1774.063    0.000 allGraphs.py:114(states)
               21423778 1234.054    0.000 1703.094    0.000 BayesianNN.py:43(convert_data)
               65410090 1654.327    0.000 1654.327    0.000 {built-in method addmm}
          695138/179383   50.650    0.000 1590.360    0.009 allGraphs.py:202(recursiveExplore)
                 284689    2.053    0.000 1582.384    0.006 game.py:42(step)
                 284689    2.851    0.000 1546.414    0.005 layers.py:827(step)
              256220500 1543.134    0.000 1543.134    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
              258264626  867.980    0.000 1444.439    0.000 tensor.py:933(grad)
                 284689    6.165    0.000 1434.715    0.005 agent.py:112(__call__)
               65979468   68.283    0.000 1106.254    0.000 activation.py:713(forward)
                6054260  125.199    0.000 1072.160    0.000 optimizer.py:167(zero_grad)
               65979468  121.422    0.000 1037.972    0.000 functional.py:1292(leaky_relu)
              395246318  314.366    0.000  956.832    0.000 overrides.py:1070(has_torch_function)
               65979468  903.731    0.000  903.731    0.000 {built-in method torch._C._nn.leaky_relu}
               73789876  840.618    0.000  840.618    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                 284689   36.714    0.000  782.987    0.003 layers.py:17(step)
              500817256  292.375    0.000  759.959    0.000 {built-in method builtins.any}
                 284690   59.306    0.000  756.467    0.003 layers.py:793(update)
               28468900   69.489    0.000  742.562    0.000 layer.py:106(move)
               43768221  168.958    0.000  734.693    0.000 tensor.py:21(wrapped)
               65410090  712.330    0.000  712.330    0.000 {method 't' of 'torch._C._TensorBase' objects}
              290461243  554.276    0.000  554.276    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               73789876  522.551    0.000  522.551    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                 284689   31.678    0.000  418.227    0.001 allGraphsTrain.py:51(<listcomp>)
                6054260   11.605    0.000  397.696    0.000 loss.py:445(forward)
                 284689   51.466    0.000  392.389    0.001 allGraphsTrain.py:44(<listcomp>)
                6054260   42.981    0.000  386.092    0.000 functional.py:2637(mse_loss)
              890579280  297.297    0.000  360.277    0.000 overrides.py:1083(<genexpr>)
               42847557  359.025    0.000  359.025    0.000 {built-in method zeros}
               36894938  355.695    0.000  355.695    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                7151303  350.689    0.000  350.689    0.000 {built-in method tensor}
               28468900   90.035    0.000  347.128    0.000 layers.py:844(check)
               13875876   67.905    0.000  325.484    0.000 tensor.py:506(__rsub__)
               36894938  325.480    0.000  325.480    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                5922966    8.794    0.000  321.982    0.000 game.py:38(board)
                4499520   44.889    0.000  281.316    0.000 allGraphs.py:167(format)
              248833043  278.424    0.000  278.424    0.000 {built-in method torch._C._get_tracing_state}
               36894938  276.636    0.000  276.636    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                 416672    6.458    0.000  265.651    0.001 layers.py:849(restart)
               28468900   59.534    0.000  261.514    0.000 layers.py:838(isFree)
               13875876  257.579    0.000  257.579    0.000 {built-in method rsub}
                 284689   90.197    0.000  234.865    0.001 agent.py:67(modify)
               29892345  233.143    0.000  233.143    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                6054260  230.918    0.000  230.918    0.000 {built-in method torch._C._nn.mse_loss}
               36894938  229.813    0.000  229.813    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                 416672    3.207    0.000  214.870    0.001 level.py:8(__init__)
              192190171  162.671    0.000  201.980    0.000 layer.py:103(isFree)
                1992830  113.753    0.000  199.507    0.000 layer.py:175(NoRock_update)
               29078926  188.112    0.000  188.112    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                 416672    7.769    0.000  186.150    0.000 levels.py:456(generate)
               28468900  179.898    0.000  179.898    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               51031434  176.764    0.000  176.764    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                 854067    5.172    0.000  175.916    0.000 tensor.py:576(__iter__)
                2000534   30.384    0.000  170.879    0.000 level.py:41(notUsed)
                 854067  167.773    0.000  167.773    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               13591187  162.124    0.000  162.124    0.000 {method 'gt' of 'torch._C._TensorBase' objects}
              402029514  108.297    0.000  154.897    0.000 enum.py:646(__hash__)
               36895048   65.209    0.000  144.847    0.000 tensor.py:596(__hash__)
               72237221   41.724    0.000  142.170    0.000 {built-in method builtins.all}
        860458808/860458806  132.195    0.000  139.554    0.000 {built-in method builtins.len}
              160861320  134.070    0.000  134.071    0.000 module.py:765(__getattr__)
             1013909060  133.443    0.000  133.443    0.000 {method 'values' of 'collections.OrderedDict' objects}
                6054260   32.871    0.000  110.066    0.000 __init__.py:28(_make_grads)
               36894938  109.376    0.000  109.376    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              224418624   84.300    0.000  101.827    0.000 layers.py:809(<genexpr>)
               22562534   27.867    0.000  100.923    0.000 flatten.py:39(forward)
              105504450   74.219    0.000   94.620    0.000 types.py:171(__get__)


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
Subject: Job 9668397: <Diamonds3_0.5_NN_cpu_2_2> in cluster <dcc> Exited

Job <Diamonds3_0.5_NN_cpu_2_2> was submitted from host <n-62-30-8> by user <s183905> in cluster <dcc> at Wed May 19 22:59:00 2021
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

    CPU time :                                   35687.74 sec.
    Max Memory :                                 106 MB
    Average Memory :                             100.38 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               16278.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   35733 sec.
    Turnaround time :                            35705 sec.

The output (if any) is above this job summary.

