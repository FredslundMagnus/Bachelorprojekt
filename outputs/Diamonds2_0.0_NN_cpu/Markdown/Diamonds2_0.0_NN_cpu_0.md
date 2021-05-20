/zhome/ee/d/137643/Desktop/Bachelor/project-env/lib/python3.8/site-packages/torch/cuda/__init__.py:52: UserWarning: CUDA initialization: Found no NVIDIA driver on your system. Please check that you have an NVIDIA GPU and installed a driver from http://www.nvidia.com/Download/index.aspx (Triggered internally at  /pytorch/c10/cuda/CUDAFunctions.cpp:100.)
  return torch._C._cuda_getDeviceCount() > 0

# Parameters

    Name :                      Diamonds2_0.0_NN_cpu-0
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
    Num :                       0
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      12254296356 function calls (11735143696 primitive calls) in 35701.00 seconds

##    Ordered by: cumulative time
   List reduced from 443 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35700.998 35700.998 {built-in method builtins.exec}
                      1    0.001    0.001 35700.998 35700.998 <string>:1(<module>)
                      1   26.135   26.135 35700.997 35700.997 allGraphsTrain.py:13(graphTrain)
                 105792   16.800    0.000 27154.415    0.257 allGraphsTrain.py:40(<listcomp>)
                 500298    2.438    0.000 27132.281    0.054 allGraphs.py:179(getInterventionsmodel)
        43756447/359562 2396.927    0.000 25358.253    0.071 allGraphs.py:186(recursiveBEST)
        524004776/48797636 2681.840    0.000 22356.955    0.000 module.py:715(_call_impl)
               47520714  827.050    0.000 21895.950    0.000 container.py:115(forward)
               47309130  147.472    0.000 21231.665    0.000 BayesianNN.py:18(forward)
               41947698 1328.873    0.000 20241.210    0.000 BayesianNN.py:65(predict_no_convert)
              141927390  183.157    0.000 7313.037    0.000 dropout.py:57(forward)
              141927390  702.149    0.000 7129.880    0.000 functional.py:960(dropout)
              142350558  437.424    0.000 6962.432    0.000 linear.py:92(forward)
              142350558  741.476    0.000 6345.015    0.000 functional.py:1669(linear)
              141927390 6282.556    0.000 6282.556    0.000 {built-in method dropout}
              142350558 3265.429    0.000 3265.429    0.000 {built-in method addmm}
                 105792  904.347    0.009 3169.190    0.030 allGraphs.py:156(transformNot)
                4190302   57.631    0.000 2425.299    0.001 BayesianNN.py:61(predict)
                1171130   13.905    0.000 2274.152    0.002 BayesianNN.py:57(learn)
              142562142  149.963    0.000 2156.511    0.000 activation.py:713(forward)
                1171130   17.774    0.000 2140.242    0.002 BayesianNN.py:21(learn)
              142562142  243.909    0.000 2006.548    0.000 functional.py:1292(leaky_relu)
                 105792    0.617    0.000 1825.133    0.017 agent.py:29(learn)
                 105792   10.317    0.000 1824.242    0.017 agent.py:117(_learn)
                 105792    7.997    0.000 1813.925    0.017 learner.py:42(Qlearn)
              142562142 1737.742    0.000 1737.742    0.000 {built-in method torch._C._nn.leaky_relu}
          688959/140736   53.283    0.000 1735.940    0.012 allGraphs.py:202(recursiveExplore)
              142350558 1501.780    0.000 1501.780    0.000 {method 't' of 'torch._C._TensorBase' objects}
                1276922    8.738    0.000 1331.885    0.001 tensor.py:181(backward)
                1276922    5.456    0.000 1323.147    0.001 __init__.py:68(backward)
                1276922 1293.039    0.001 1293.039    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                 211584    0.744    0.000 1255.452    0.006 network.py:28(forward)
                 423168    1.369    0.000 1092.307    0.003 conv.py:422(forward)
                 423168    1.323    0.000 1090.421    0.003 conv.py:414(_conv_forward)
                 423168 1088.854    0.003 1088.854    0.003 {built-in method conv2d}
               44050900  208.011    0.000 1055.792    0.000 tensor.py:506(__rsub__)
                1276922    8.881    0.000 1032.195    0.001 grad_mode.py:23(decorate_context)
               55159060  255.926    0.000 1011.852    0.000 tensor.py:21(wrapped)
                1276922   41.702    0.000 1006.937    0.001 adam.py:55(step)
                 105792   14.398    0.000 1002.455    0.009 allGraphsTrain.py:33(<listcomp>)
               10685093  479.757    0.000  988.066    0.000 allGraphs.py:114(states)
               44050900  847.781    0.000  847.781    0.000 {built-in method rsub}
              137530200  816.454    0.000  816.454    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                1276922  199.918    0.000  791.021    0.001 functional.py:53(adam)
                 105792    0.536    0.000  746.409    0.007 game.py:42(step)
              225313784  222.045    0.000  741.545    0.000 overrides.py:1070(has_torch_function)
                 105792    0.817    0.000  735.764    0.007 layers.py:827(step)
                 105792    1.636    0.000  657.888    0.006 agent.py:112(__call__)
                 105792    4.510    0.000  607.511    0.006 allGraphs.py:141(transform)
              380708784  255.330    0.000  602.448    0.000 {built-in method builtins.any}
                5361432  416.915    0.000  548.133    0.000 BayesianNN.py:43(convert_data)
              524322152  541.294    0.000  541.294    0.000 {built-in method torch._C._get_tracing_state}
               43945108  480.402    0.000  480.402    0.000 {method 'gt' of 'torch._C._TensorBase' objects}
                 105792   12.299    0.000  456.233    0.004 layers.py:17(step)
               10579200   26.488    0.000  442.642    0.000 layer.py:106(move)
               55111872  191.543    0.000  313.750    0.000 tensor.py:933(grad)
              612956254  242.750    0.000  297.674    0.000 overrides.py:1083(<genexpr>)
               10579200   60.739    0.000  292.854    0.000 layers.py:844(check)
             2143539818  289.386    0.000  289.386    0.000 {method 'values' of 'collections.OrderedDict' objects}
                 105793   21.450    0.000  277.735    0.003 layers.py:793(update)
              149281370  266.538    0.000  266.538    0.000 {method 'item' of 'torch._C._TensorBase' objects}
              334239801  263.356    0.000  263.357    0.000 module.py:765(__getattr__)
                1276922   28.114    0.000  237.712    0.000 optimizer.py:167(zero_grad)
        1320157462/1320157460  220.985    0.000  223.547    0.000 {built-in method builtins.len}
               15746232  191.822    0.000  191.822    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               58311498  180.577    0.000  180.577    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               47732298   37.741    0.000  179.933    0.000 flatten.py:39(forward)
                 105792   11.839    0.000  170.156    0.002 allGraphsTrain.py:51(<listcomp>)
                 105792   19.495    0.000  147.150    0.001 allGraphsTrain.py:44(<listcomp>)
               65738360   56.340    0.000  140.249    0.000 {built-in method builtins.all}
              143204312   90.185    0.000  122.883    0.000 _VF.py:25(__getattr__)
              142350558  122.546    0.000  122.546    0.000 functional.py:1686(<listcomp>)
               15746232  122.173    0.000  122.173    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               46349584  104.824    0.000  104.824    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               10579200   27.357    0.000  101.226    0.000 layers.py:838(isFree)
               11108160   97.412    0.000   97.412    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               10722865   94.412    0.000   94.412    0.000 {built-in method zeros}
              252899601   63.153    0.000   91.693    0.000 enum.py:646(__hash__)
              368625125   87.729    0.000   87.729    0.000 {built-in method builtins.getattr}
               78047212   69.734    0.000   87.561    0.000 types.py:171(__get__)
                1276922    2.310    0.000   83.669    0.000 loss.py:445(forward)
              143408598   81.716    0.000   81.716    0.000 {method 'dim' of 'torch._C._TensorBase' objects}
                1276922    8.935    0.000   81.358    0.000 functional.py:2637(mse_loss)
                7873116   81.163    0.000   81.163    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                 952137   44.439    0.000   80.821    0.000 layer.py:175(NoRock_update)
                 105792   28.562    0.000   78.552    0.001 agent.py:67(modify)
               86065980   58.576    0.000   73.870    0.000 layer.py:103(isFree)
                7873116   72.275    0.000   72.275    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                1505741   71.629    0.000   71.629    0.000 {built-in method tensor}
                  88702    1.465    0.000   71.607    0.001 layers.py:849(restart)
              430670976   69.086    0.000   69.086    0.000 _jit_internal.py:750(is_scripting)
               10579200   68.776    0.000   68.776    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                7873116   66.156    0.000   66.156    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              165477180   61.164    0.000   61.164    0.000 tensor.py:24(<genexpr>)
                  88702    0.718    0.000   60.186    0.001 level.py:8(__init__)
                1029259    1.415    0.000   58.403    0.000 game.py:38(board)
               47520714   39.153    0.000   56.988    0.000 container.py:107(__iter__)
                7873116   54.863    0.000   54.863    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                  88702    2.177    0.000   54.150    0.001 levels.py:249(generate)
                2404476   53.928    0.000   53.928    0.000 {built-in method cat}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9653096: <Diamonds2_0.0_NN_cpu_0> in cluster <dcc> Done

Job <Diamonds2_0.0_NN_cpu_0> was submitted from host <n-62-30-5> by user <s183905> in cluster <dcc> at Wed May 19 11:40:32 2021
Job was executed on host(s) <n-62-21-98>, in queue <hpc>, as user <s183905> in cluster <dcc> at Wed May 19 11:40:33 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 19 11:40:33 2021
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

    CPU time :                                   35702.44 sec.
    Max Memory :                                 116 MB
    Average Memory :                             109.47 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               16268.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   35706 sec.
    Turnaround time :                            35708 sec.

The output (if any) is above this job summary.

/zhome/ee/d/137643/Desktop/Bachelor/project-env/lib/python3.8/site-packages/torch/cuda/__init__.py:52: UserWarning: CUDA initialization: Found no NVIDIA driver on your system. Please check that you have an NVIDIA GPU and installed a driver from http://www.nvidia.com/Download/index.aspx (Triggered internally at  /pytorch/c10/cuda/CUDAFunctions.cpp:100.)
  return torch._C._cuda_getDeviceCount() > 0

# Parameters

    Name :                      Diamonds2_0.0_NN_cpu-0
    Main :                      graphTrain
    Level :                     Levels.Causal5
    Failed actions chance :     0.0
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
    Num :                       0
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      15194645797 function calls (14887971803 primitive calls) in 35700.26 seconds

##    Ordered by: cumulative time
   List reduced from 439 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35700.256 35700.256 {built-in method builtins.exec}
                      1    0.001    0.001 35700.256 35700.256 <string>:1(<module>)
                      1   80.258   80.258 35700.254 35700.254 allGraphsTrain.py:13(graphTrain)
        324351601/36030231 1354.297    0.000 12660.910    0.000 module.py:715(_call_impl)
               28832137  353.330    0.000 12012.348    0.000 container.py:115(forward)
                 321787 1796.480    0.006 11314.045    0.035 allGraphs.py:156(transformNot)
                 321787   70.346    0.000 10892.386    0.034 allGraphsTrain.py:40(<listcomp>)
                5490333   21.801    0.000 10776.056    0.002 allGraphs.py:179(getInterventionsmodel)
                6876307   77.889    0.000 10716.667    0.002 BayesianNN.py:57(learn)
                6876307   84.817    0.000 10184.391    0.001 BayesianNN.py:21(learn)
               28188563   71.860    0.000 9523.348    0.000 BayesianNN.py:18(forward)
        22858806/5246605  962.725    0.000 8748.778    0.002 allGraphs.py:186(recursiveBEST)
               21312256  236.570    0.000 8699.586    0.000 BayesianNN.py:61(predict)
                7198094   46.153    0.000 4645.921    0.001 grad_mode.py:23(decorate_context)
                 321787    2.393    0.000 4517.922    0.014 agent.py:29(learn)
                 321787   78.024    0.000 4514.606    0.014 agent.py:117(_learn)
                7198094  221.775    0.000 4506.864    0.001 adam.py:55(step)
                 321787   31.555    0.000 4436.581    0.014 learner.py:42(Qlearn)
                7198094   40.121    0.000 3976.708    0.001 tensor.py:181(backward)
                7198094   29.275    0.000 3936.587    0.001 __init__.py:68(backward)
                7198094 3788.802    0.001 3788.802    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                7198094  860.970    0.000 3382.467    0.000 functional.py:53(adam)
               85852837  212.103    0.000 3296.848    0.000 linear.py:92(forward)
               84565689   80.268    0.000 3266.786    0.000 dropout.py:57(forward)
               84565689  314.022    0.000 3186.518    0.000 functional.py:960(dropout)
               85852837  356.221    0.000 2994.411    0.000 functional.py:1669(linear)
                 643574    2.549    0.000 2803.480    0.004 network.py:28(forward)
               84565689 2790.335    0.000 2790.335    0.000 {built-in method dropout}
                 321787   20.859    0.000 2432.431    0.008 allGraphs.py:141(transform)
                1287148    5.238    0.000 2283.074    0.002 conv.py:422(forward)
                1287148    5.938    0.000 2275.731    0.002 conv.py:414(_conv_forward)
                1287148 2269.083    0.002 2269.083    0.002 {built-in method conv2d}
                 321787   67.942    0.000 1894.039    0.006 allGraphsTrain.py:33(<listcomp>)
               32500588  879.101    0.000 1826.102    0.000 allGraphs.py:114(states)
               28188563 1303.332    0.000 1800.885    0.000 BayesianNN.py:43(convert_data)
                 321787    2.272    0.000 1800.808    0.006 game.py:42(step)
                 321787    2.992    0.000 1758.190    0.005 layers.py:827(step)
          983739/243728   58.728    0.000 1682.942    0.007 allGraphs.py:202(recursiveExplore)
              306825026  947.468    0.000 1582.165    0.000 tensor.py:933(grad)
              289608700 1562.582    0.000 1562.582    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
               85852837 1551.004    0.000 1551.004    0.000 {built-in method addmm}
                 321787    7.383    0.000 1310.729    0.004 agent.py:112(__call__)
                7198094  131.757    0.000 1160.734    0.000 optimizer.py:167(zero_grad)
               86496411   70.004    0.000 1103.111    0.000 activation.py:713(forward)
              476109866  333.863    0.000 1056.325    0.000 overrides.py:1070(has_torch_function)
               86496411  117.921    0.000 1033.106    0.000 functional.py:1292(leaky_relu)
               86496411  901.940    0.000  901.940    0.000 {built-in method torch._C._nn.leaky_relu}
                 321787   40.221    0.000  890.713    0.003 layers.py:17(step)
                 321788   62.630    0.000  860.121    0.003 layers.py:793(update)
              607983990  327.285    0.000  847.731    0.000 {built-in method builtins.any}
               32178700   74.266    0.000  846.349    0.000 layer.py:106(move)
               87664276  844.581    0.000  844.581    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               52461634  174.068    0.000  777.586    0.000 tensor.py:21(wrapped)
               85852837  661.992    0.000  661.992    0.000 {method 't' of 'torch._C._TensorBase' objects}
              328666275  554.048    0.000  554.048    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               87664276  537.167    0.000  537.167    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                 321787   28.729    0.000  445.607    0.001 allGraphsTrain.py:51(<listcomp>)
                 321787   51.632    0.000  402.128    0.001 allGraphsTrain.py:44(<listcomp>)
             1077672324  328.288    0.000  400.874    0.000 overrides.py:1083(<genexpr>)
               32178700  101.600    0.000  395.223    0.000 layers.py:844(check)
                7198094   11.420    0.000  393.690    0.000 loss.py:445(forward)
                8483065  392.764    0.000  392.764    0.000 {built-in method tensor}
                7198094   48.158    0.000  382.270    0.000 functional.py:2637(mse_loss)
               56377127  374.538    0.000  374.538    0.000 {built-in method zeros}
                7099269    8.272    0.000  360.696    0.000 game.py:38(board)
               18673999   68.740    0.000  328.573    0.000 tensor.py:506(__rsub__)
                 553701    7.917    0.000  326.081    0.001 layers.py:849(restart)
               43832138  321.410    0.000  321.410    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                5490333   50.452    0.000  319.685    0.000 allGraphs.py:167(format)
               43832138  312.878    0.000  312.878    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               32178700   63.132    0.000  299.624    0.000 layers.py:838(isFree)
                 553701    4.052    0.000  262.964    0.000 level.py:8(__init__)
               43832138  261.418    0.000  261.418    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               18673999  259.832    0.000  259.832    0.000 {built-in method rsub}
               33787635  245.946    0.000  245.946    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                 321787   87.709    0.000  239.141    0.001 agent.py:67(modify)
              210725344  198.183    0.000  236.492    0.000 layer.py:103(isFree)
              325316962  233.461    0.000  233.461    0.000 {built-in method torch._C._get_tracing_state}
               43832138  228.747    0.000  228.747    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                 553701    9.133    0.000  226.739    0.000 levels.py:151(generate)
                7198094  217.126    0.000  217.126    0.000 {built-in method torch._C._nn.mse_loss}
                2657306   36.658    0.000  207.844    0.000 level.py:41(notUsed)
                2252516  118.568    0.000  207.724    0.000 layer.py:175(NoRock_update)
               37510253  195.382    0.000  195.382    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               32178700  188.985    0.000  188.985    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
              471528472  128.308    0.000  186.184    0.000 enum.py:646(__hash__)
               61654411  183.436    0.000  183.436    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                 965361    5.406    0.000  182.154    0.000 tensor.py:576(__iter__)
               18352212  176.134    0.000  176.134    0.000 {method 'gt' of 'torch._C._TensorBase' objects}
                 965361  172.930    0.000  172.930    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               43832248   72.434    0.000  164.221    0.000 tensor.py:596(__hash__)
               84640434   47.663    0.000  162.634    0.000 {built-in method builtins.all}
             1326238541  150.452    0.000  150.452    0.000 {method 'values' of 'collections.OrderedDict' objects}
              209989403  146.063    0.000  146.064    0.000 module.py:765(__getattr__)
        1080902444/1080902442  135.657    0.000  142.235    0.000 {built-in method builtins.len}
               43832138  120.680    0.000  120.680    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              253000792   93.212    0.000  113.561    0.000 layers.py:809(<genexpr>)
                7198094   39.484    0.000  110.326    0.000 __init__.py:28(_make_grads)
              125622716   82.840    0.000  108.051    0.000 types.py:171(__get__)
               29475711   26.007    0.000  107.935    0.000 flatten.py:39(forward)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9668378: <Diamonds2_0.0_NN_cpu_0> in cluster <dcc> Done

Job <Diamonds2_0.0_NN_cpu_0> was submitted from host <n-62-30-8> by user <s183905> in cluster <dcc> at Wed May 19 22:55:27 2021
Job was executed on host(s) <n-62-11-60>, in queue <hpc>, as user <s183905> in cluster <dcc> at Wed May 19 22:55:28 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 19 22:55:28 2021
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

    CPU time :                                   35616.99 sec.
    Max Memory :                                 106 MB
    Average Memory :                             99.44 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               16278.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   35732 sec.
    Turnaround time :                            35706 sec.

The output (if any) is above this job summary.

