/zhome/ee/d/137643/Desktop/Bachelor/project-env/lib/python3.8/site-packages/torch/cuda/__init__.py:52: UserWarning: CUDA initialization: Found no NVIDIA driver on your system. Please check that you have an NVIDIA GPU and installed a driver from http://www.nvidia.com/Download/index.aspx (Triggered internally at  /pytorch/c10/cuda/CUDAFunctions.cpp:100.)
  return torch._C._cuda_getDeviceCount() > 0

# Parameters

    Name :                      Diamonds2_0.0_NN_cpu-2
    Main :                      graphTrain
    Level :                     Levels.Causal5
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


      11853096647 function calls (11353337777 primitive calls) in 35701.46 seconds

##    Ordered by: cumulative time
   List reduced from 443 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35701.465 35701.465 {built-in method builtins.exec}
                      1    0.003    0.003 35701.465 35701.465 <string>:1(<module>)
                      1   30.374   30.374 35701.462 35701.462 allGraphsTrain.py:13(graphTrain)
                  99237   18.773    0.000 27153.593    0.274 allGraphsTrain.py:40(<listcomp>)
                 552851    3.251    0.000 27128.277    0.049 allGraphs.py:179(getInterventionsmodel)
        41452775/373846 2279.859    0.000 24874.756    0.067 allGraphs.py:186(recursiveBEST)
        505064551/47058041 2737.610    0.000 22484.950    0.000 module.py:715(_call_impl)
               45800651  892.314    0.000 22028.247    0.000 container.py:115(forward)
               45602177  150.661    0.000 21370.858    0.000 BayesianNN.py:18(forward)
               39640534 1260.942    0.000 19917.467    0.001 BayesianNN.py:65(predict_no_convert)
              136806531  179.638    0.000 7319.659    0.000 dropout.py:57(forward)
              136806531  712.303    0.000 7140.021    0.000 functional.py:960(dropout)
              137203479  430.345    0.000 6937.053    0.000 linear.py:92(forward)
              137203479  730.730    0.000 6330.070    0.000 functional.py:1669(linear)
              136806531 6278.423    0.000 6278.423    0.000 {built-in method dropout}
              137203479 3271.987    0.000 3271.987    0.000 {built-in method addmm}
                  99237  888.775    0.009 3024.413    0.030 allGraphs.py:156(transformNot)
                4803490   65.208    0.000 2870.442    0.001 BayesianNN.py:61(predict)
                1158153   14.248    0.000 2297.908    0.002 BayesianNN.py:57(learn)
              137401953  153.934    0.000 2197.902    0.000 activation.py:713(forward)
          852024/179005   66.316    0.000 2196.274    0.012 allGraphs.py:202(recursiveExplore)
                1158153   19.350    0.000 2160.628    0.002 BayesianNN.py:21(learn)
              137401953  234.920    0.000 2043.968    0.000 functional.py:1292(leaky_relu)
                  99237    0.698    0.000 1815.940    0.018 agent.py:29(learn)
                  99237   11.975    0.000 1814.978    0.018 agent.py:117(_learn)
                  99237    8.592    0.000 1803.003    0.018 learner.py:42(Qlearn)
              137401953 1784.923    0.000 1784.923    0.000 {built-in method torch._C._nn.leaky_relu}
              137203479 1513.974    0.000 1513.974    0.000 {method 't' of 'torch._C._TensorBase' objects}
                1257390    9.212    0.000 1331.465    0.001 tensor.py:181(backward)
                1257390    5.564    0.000 1322.253    0.001 __init__.py:68(backward)
                1257390 1291.507    0.001 1291.507    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                 198474    0.905    0.000 1241.162    0.006 network.py:28(forward)
                 396948    1.491    0.000 1085.218    0.003 conv.py:422(forward)
                 396948    1.690    0.000 1083.174    0.003 conv.py:414(_conv_forward)
                 396948 1081.274    0.003 1081.274    0.003 {built-in method conv2d}
                1257390    9.100    0.000 1026.570    0.001 grad_mode.py:23(decorate_context)
               41851185  203.352    0.000 1007.614    0.000 tensor.py:506(__rsub__)
                1257390   42.307    0.000  999.657    0.001 adam.py:55(step)
                  99237   20.146    0.000  992.553    0.010 allGraphsTrain.py:33(<listcomp>)
               52271070  250.345    0.000  988.897    0.000 tensor.py:21(wrapped)
               10023038  465.734    0.000  972.418    0.000 allGraphs.py:114(states)
               41851185  804.262    0.000  804.262    0.000 {built-in method rsub}
              129008700  801.224    0.000  801.224    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                1257390  196.785    0.000  783.170    0.001 functional.py:53(adam)
                  99237    5.568    0.000  762.260    0.008 allGraphs.py:141(transform)
                  99237    0.673    0.000  752.235    0.008 game.py:42(step)
                  99237    1.024    0.000  738.979    0.007 layers.py:827(step)
              218214392  224.344    0.000  730.849    0.000 overrides.py:1070(has_torch_function)
                  99237    2.188    0.000  652.319    0.007 agent.py:112(__call__)
                5961643  469.814    0.000  617.750    0.000 BayesianNN.py:43(convert_data)
              367760889  246.467    0.000  587.215    0.000 {built-in method builtins.any}
              505362262  553.438    0.000  553.438    0.000 {built-in method torch._C._get_tracing_state}
               41751948  472.491    0.000  472.491    0.000 {method 'gt' of 'torch._C._TensorBase' objects}
                  99237   12.820    0.000  445.387    0.004 layers.py:17(step)
                9923700   25.147    0.000  431.313    0.000 layer.py:106(move)
               54199758  190.879    0.000  312.419    0.000 tensor.py:933(grad)
              592700494  239.296    0.000  294.408    0.000 overrides.py:1083(<genexpr>)
                  99238   20.836    0.000  291.219    0.003 layers.py:793(update)
                9923700   58.939    0.000  284.154    0.000 layers.py:844(check)
              140091345  281.503    0.000  281.503    0.000 {method 'item' of 'torch._C._TensorBase' objects}
             2066058855  280.769    0.000  280.769    0.000 {method 'values' of 'collections.OrderedDict' objects}
              322160141  258.162    0.000  258.163    0.000 module.py:765(__getattr__)
                1257390   26.233    0.000  232.915    0.000 optimizer.py:167(zero_grad)
        1269527673/1269527671  214.361    0.000  217.056    0.000 {built-in method builtins.len}
               15485628  191.988    0.000  191.988    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               55922825  172.802    0.000  172.802    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               45999125   35.185    0.000  170.330    0.000 flatten.py:39(forward)
                  99237   11.177    0.000  158.941    0.002 allGraphsTrain.py:51(<listcomp>)
               62194870   59.424    0.000  150.903    0.000 {built-in method builtins.all}
                  99237   19.167    0.000  147.957    0.001 allGraphsTrain.py:44(<listcomp>)
              138063921   90.968    0.000  126.185    0.000 _VF.py:25(__getattr__)
               15485628  121.004    0.000  121.004    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              137203479  119.835    0.000  119.835    0.000 functional.py:1686(<listcomp>)
               11923287  107.316    0.000  107.316    0.000 {built-in method zeros}
               44642498  103.348    0.000  103.348    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                9923700   25.606    0.000  100.450    0.000 layers.py:838(isFree)
                1498199   94.568    0.000   94.568    0.000 {built-in method tensor}
               10419885   90.920    0.000   90.920    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
              356383158   90.436    0.000   90.436    0.000 {built-in method builtins.getattr}
              237579755   60.697    0.000   88.286    0.000 enum.py:646(__hash__)
                1257390    3.461    0.000   87.667    0.000 loss.py:445(forward)
               81293263   67.814    0.000   86.015    0.000 types.py:171(__get__)
                1257390    9.751    0.000   84.206    0.000 functional.py:2637(mse_loss)
                1049037    1.875    0.000   81.915    0.000 game.py:38(board)
                  99237   29.300    0.000   81.572    0.001 agent.py:67(modify)
                 893142   44.797    0.000   80.982    0.000 layer.py:175(NoRock_update)
                7742814   80.373    0.000   80.373    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                  95562    1.752    0.000   78.144    0.001 layers.py:849(restart)
               78796885   60.838    0.000   74.844    0.000 layer.py:103(isFree)
                7742814   73.732    0.000   73.732    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              138195969   70.296    0.000   70.296    0.000 {method 'dim' of 'torch._C._TensorBase' objects}
                9923700   68.834    0.000   68.834    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
              415184253   68.184    0.000   68.184    0.000 _jit_internal.py:750(is_scripting)
                2890550   66.454    0.000   66.454    0.000 {built-in method cat}
                  95562    0.860    0.000   65.449    0.001 level.py:8(__init__)
                7742814   64.870    0.000   64.870    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              156813210   61.216    0.000   61.216    0.000 tensor.py:24(<genexpr>)
                 297711    1.891    0.000   58.584    0.000 tensor.py:576(__iter__)
                  95562    2.429    0.000   58.497    0.001 levels.py:249(generate)
               45800651   38.540    0.000   57.417    0.000 container.py:107(__iter__)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9653098: <Diamonds2_0.0_NN_cpu_2> in cluster <dcc> Done

Job <Diamonds2_0.0_NN_cpu_2> was submitted from host <n-62-30-5> by user <s183905> in cluster <dcc> at Wed May 19 11:40:32 2021
Job was executed on host(s) <n-62-21-107>, in queue <hpc>, as user <s183905> in cluster <dcc> at Wed May 19 11:40:33 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 19 11:40:33 2021
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

    CPU time :                                   35703.30 sec.
    Max Memory :                                 113 MB
    Average Memory :                             107.66 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               16271.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   35709 sec.
    Turnaround time :                            35711 sec.

The output (if any) is above this job summary.

