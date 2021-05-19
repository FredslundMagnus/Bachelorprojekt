/zhome/ee/d/137643/Desktop/Bachelor/project-env/lib/python3.8/site-packages/torch/cuda/__init__.py:52: UserWarning: CUDA initialization: Found no NVIDIA driver on your system. Please check that you have an NVIDIA GPU and installed a driver from http://www.nvidia.com/Download/index.aspx (Triggered internally at  /pytorch/c10/cuda/CUDAFunctions.cpp:100.)
  return torch._C._cuda_getDeviceCount() > 0

# Parameters

    Name :                      Diamonds1_0.0_NN_cpu-1
    Main :                      graphTrain
    Level :                     Levels.Causal2
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
    Num :                       1
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      11906343777 function calls (11386343758 primitive calls) in 35700.43 seconds

##    Ordered by: cumulative time
   List reduced from 442 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35700.430 35700.430 {built-in method builtins.exec}
                      1    0.002    0.002 35700.429 35700.429 <string>:1(<module>)
                      1   31.115   31.115 35700.427 35700.427 allGraphsTrain.py:13(graphTrain)
                 105542   21.508    0.000 27086.772    0.257 allGraphsTrain.py:40(<listcomp>)
                 547440    3.150    0.000 27059.190    0.049 allGraphs.py:179(getInterventionsmodel)
        43462917/396459 2315.744    0.000 25145.218    0.063 allGraphs.py:186(recursiveBEST)
        525402179/49073159 2760.344    0.000 22588.821    0.000 module.py:715(_call_impl)
               47632902  875.408    0.000 22125.329    0.000 container.py:115(forward)
               47421818  153.723    0.000 21430.698    0.000 BayesianNN.py:18(forward)
               41469864 1289.492    0.000 20099.588    0.000 BayesianNN.py:65(predict_no_convert)
              142265454  188.240    0.000 7348.786    0.000 dropout.py:57(forward)
              142265454  706.146    0.000 7160.546    0.000 functional.py:960(dropout)
              142687622  482.434    0.000 6977.591    0.000 linear.py:92(forward)
              142687622  725.227    0.000 6297.588    0.000 functional.py:1669(linear)
              142265454 6297.424    0.000 6297.424    0.000 {built-in method dropout}
                 105542  833.598    0.008 3542.868    0.034 allGraphs.py:156(transformNot)
              142687622 3231.486    0.000 3231.486    0.000 {built-in method addmm}
                4617239   61.480    0.000 2593.608    0.001 BayesianNN.py:61(predict)
                1334715   16.102    0.000 2551.091    0.002 BayesianNN.py:57(learn)
                1334715   20.218    0.000 2431.690    0.002 BayesianNN.py:21(learn)
              142898706  142.707    0.000 2159.613    0.000 activation.py:713(forward)
              142898706  244.577    0.000 2016.906    0.000 functional.py:1292(leaky_relu)
                 105542    0.733    0.000 1939.780    0.018 agent.py:29(learn)
                 105542   13.027    0.000 1938.756    0.018 agent.py:117(_learn)
                 105542    8.952    0.000 1925.729    0.018 learner.py:42(Qlearn)
          755110/150981   58.729    0.000 1856.534    0.012 allGraphs.py:202(recursiveExplore)
              142898706 1746.928    0.000 1746.928    0.000 {built-in method torch._C._nn.leaky_relu}
              142687622 1513.259    0.000 1513.259    0.000 {method 't' of 'torch._C._TensorBase' objects}
                1440257   10.062    0.000 1455.647    0.001 tensor.py:181(backward)
                1440257    6.469    0.000 1445.585    0.001 __init__.py:68(backward)
                1440257 1411.392    0.001 1411.392    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                 211084    0.872    0.000 1298.593    0.006 network.py:28(forward)
                 422168    1.529    0.000 1133.990    0.003 conv.py:422(forward)
                1440257   10.153    0.000 1133.958    0.001 grad_mode.py:23(decorate_context)
                 422168    1.970    0.000 1131.893    0.003 conv.py:414(_conv_forward)
                 422168 1129.574    0.003 1129.574    0.003 {built-in method conv2d}
                1440257   48.498    0.000 1103.999    0.001 adam.py:55(step)
               43776129  203.656    0.000 1026.216    0.000 tensor.py:506(__rsub__)
               54858039  250.560    0.000  980.715    0.000 tensor.py:21(wrapped)
                 105542   16.188    0.000  880.271    0.008 allGraphsTrain.py:33(<listcomp>)
               10659843  412.323    0.000  864.092    0.000 allGraphs.py:114(states)
                1440257  217.807    0.000  858.331    0.001 functional.py:53(adam)
               43776129  822.560    0.000  822.560    0.000 {built-in method rsub}
              234010262  237.089    0.000  768.787    0.000 overrides.py:1070(has_torch_function)
              116096700  748.561    0.000  748.561    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 105542    2.143    0.000  665.655    0.006 agent.py:112(__call__)
                 105542    0.703    0.000  627.809    0.006 game.py:42(step)
                 105542    1.042    0.000  614.849    0.006 layers.py:827(step)
              390047166  257.879    0.000  608.635    0.000 {built-in method builtins.any}
              525718805  531.027    0.000  531.027    0.000 {built-in method torch._C._get_tracing_state}
                5951954  349.644    0.000  486.874    0.000 BayesianNN.py:43(convert_data)
               43670587  454.953    0.000  454.953    0.000 {method 'gt' of 'torch._C._TensorBase' objects}
                 105542    4.094    0.000  400.239    0.004 allGraphs.py:141(transform)
               61968442  216.027    0.000  354.352    0.000 tensor.py:933(grad)
                 105542   13.858    0.000  325.480    0.003 layers.py:17(step)
               10554200   26.305    0.000  310.265    0.000 layer.py:106(move)
              631209608  250.111    0.000  303.987    0.000 overrides.py:1083(<genexpr>)
              335187702  300.251    0.000  300.251    0.000 module.py:765(__getattr__)
                 105543   22.381    0.000  286.931    0.003 layers.py:793(update)
             2149241618  280.283    0.000  280.283    0.000 {method 'values' of 'collections.OrderedDict' objects}
                1440257   30.470    0.000  266.787    0.000 optimizer.py:167(zero_grad)
              127986455  244.782    0.000  244.782    0.000 {method 'item' of 'torch._C._TensorBase' objects}
        1303720907/1303720905  229.272    0.000  231.862    0.000 {built-in method builtins.len}
               17705252  210.042    0.000  210.042    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               47843986   51.771    0.000  191.487    0.000 flatten.py:39(forward)
               58398186  177.671    0.000  177.671    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                 105542   11.693    0.000  162.361    0.002 allGraphsTrain.py:51(<listcomp>)
               65412339   59.249    0.000  160.457    0.000 {built-in method builtins.all}
               10554200   38.594    0.000  158.307    0.000 layers.py:844(check)
                 105542   19.691    0.000  150.057    0.001 allGraphsTrain.py:44(<listcomp>)
              143705711   93.604    0.000  133.584    0.000 _VF.py:25(__getattr__)
               17705252  132.535    0.000  132.535    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              142687622  118.415    0.000  118.415    0.000 functional.py:1686(<listcomp>)
               11903909  105.379    0.000  105.379    0.000 {built-in method zeros}
               10554200   24.939    0.000  101.357    0.000 layers.py:838(isFree)
               46298187  100.840    0.000  100.840    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                1440257    2.821    0.000   96.607    0.000 loss.py:445(forward)
              377822731   93.963    0.000   93.963    0.000 {built-in method builtins.getattr}
                1440257   11.185    0.000   93.786    0.000 functional.py:2637(mse_loss)
               11081910   91.915    0.000   91.915    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                1550530   90.415    0.000   90.415    0.000 {built-in method tensor}
                8852626   88.339    0.000   88.339    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                 105542   29.942    0.000   83.089    0.001 agent.py:67(modify)
                 844344   44.881    0.000   80.779    0.000 layer.py:175(NoRock_update)
                8852626   79.624    0.000   79.624    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               70518808   62.953    0.000   79.094    0.000 types.py:171(__get__)
                1075151    1.872    0.000   77.062    0.000 game.py:38(board)
               81021014   62.439    0.000   76.417    0.000 layer.py:103(isFree)
              432172673   71.106    0.000   71.106    0.000 _jit_internal.py:750(is_scripting)
               10554200   70.187    0.000   70.187    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                8852626   69.328    0.000   69.328    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              143743162   67.723    0.000   67.723    0.000 {method 'dim' of 'torch._C._TensorBase' objects}
                  85532    1.557    0.000   65.762    0.001 layers.py:849(restart)
              167361762   45.418    0.000   65.565    0.000 enum.py:646(__hash__)
              164574117   63.465    0.000   63.465    0.000 tensor.py:24(<genexpr>)
                 316626    1.969    0.000   60.647    0.000 tensor.py:576(__iter__)
                2627600   59.447    0.000   59.447    0.000 {built-in method cat}
                8852626   57.792    0.000   57.792    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               47632902   40.193    0.000   57.680    0.000 container.py:107(__iter__)
                 316626   57.623    0.000   57.623    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9653094: <Diamonds1_0.0_NN_cpu_1> in cluster <dcc> Done

Job <Diamonds1_0.0_NN_cpu_1> was submitted from host <n-62-30-5> by user <s183905> in cluster <dcc> at Wed May 19 11:40:31 2021
Job was executed on host(s) <n-62-21-107>, in queue <hpc>, as user <s183905> in cluster <dcc> at Wed May 19 11:40:32 2021
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

Successfully completed.

Resource usage summary:

    CPU time :                                   35702.11 sec.
    Max Memory :                                 108 MB
    Average Memory :                             103.32 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               16276.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   35709 sec.
    Turnaround time :                            35709 sec.

The output (if any) is above this job summary.

