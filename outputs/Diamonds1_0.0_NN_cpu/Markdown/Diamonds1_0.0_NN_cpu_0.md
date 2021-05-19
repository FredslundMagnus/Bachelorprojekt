/zhome/ee/d/137643/Desktop/Bachelor/project-env/lib/python3.8/site-packages/torch/cuda/__init__.py:52: UserWarning: CUDA initialization: Found no NVIDIA driver on your system. Please check that you have an NVIDIA GPU and installed a driver from http://www.nvidia.com/Download/index.aspx (Triggered internally at  /pytorch/c10/cuda/CUDAFunctions.cpp:100.)
  return torch._C._cuda_getDeviceCount() > 0

# Parameters

    Name :                      Diamonds1_0.0_NN_cpu-0
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
    Num :                       0
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      12272132095 function calls (11764826680 primitive calls) in 35700.80 seconds

##    Ordered by: cumulative time
   List reduced from 440 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35700.796 35700.796 {built-in method builtins.exec}
                      1    0.002    0.002 35700.796 35700.796 <string>:1(<module>)
                      1   36.454   36.454 35700.794 35700.794 allGraphsTrain.py:13(graphTrain)
                 120493   22.987    0.000 26498.695    0.220 allGraphsTrain.py:40(<listcomp>)
                 817201    4.345    0.000 26467.451    0.032 allGraphs.py:179(getInterventionsmodel)
        43229447/675435 2259.731    0.000 25081.281    0.037 allGraphs.py:186(recursiveBEST)
        512414308/48084668 2720.803    0.000 22233.060    0.000 module.py:715(_call_impl)
               46432964  855.521    0.000 21737.007    0.000 container.py:115(forward)
               46191978  155.965    0.000 21066.361    0.000 BayesianNN.py:18(forward)
               40400300 1286.237    0.000 19768.430    0.000 BayesianNN.py:65(predict_no_convert)
              138575934  242.693    0.000 7330.342    0.000 dropout.py:57(forward)
              138575934  697.800    0.000 7087.649    0.000 functional.py:960(dropout)
              139057906  447.474    0.000 6854.341    0.000 linear.py:92(forward)
              138575934 6243.282    0.000 6243.282    0.000 {built-in method dropout}
              139057906  709.693    0.000 6241.184    0.000 functional.py:1669(linear)
              139057906 3216.036    0.000 3216.036    0.000 {built-in method addmm}
                 120493  767.104    0.006 3174.758    0.026 allGraphs.py:156(transformNot)
                1531211   18.539    0.000 2938.081    0.002 BayesianNN.py:57(learn)
                1531211   23.884    0.000 2793.511    0.002 BayesianNN.py:21(learn)
                4260467   58.504    0.000 2416.217    0.001 BayesianNN.py:61(predict)
              139298892  144.704    0.000 2098.115    0.000 activation.py:713(forward)
                 120493    0.795    0.000 1993.277    0.017 agent.py:29(learn)
                 120493   15.199    0.000 1992.128    0.017 agent.py:117(_learn)
                 120493   10.387    0.000 1976.929    0.016 learner.py:42(Qlearn)
              139298892  232.541    0.000 1953.411    0.000 functional.py:1292(leaky_relu)
              139298892 1696.240    0.000 1696.240    0.000 {built-in method torch._C._nn.leaky_relu}
                1651704   12.057    0.000 1549.074    0.001 tensor.py:181(backward)
                1651704    7.731    0.000 1537.017    0.001 __init__.py:68(backward)
              139057906 1509.626    0.000 1509.626    0.000 {method 't' of 'torch._C._TensorBase' objects}
                1651704 1495.852    0.001 1495.852    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
          563117/141766   41.090    0.000 1312.086    0.009 allGraphs.py:202(recursiveExplore)
                1651704   12.014    0.000 1296.500    0.001 grad_mode.py:23(decorate_context)
                 240986    1.044    0.000 1272.876    0.005 network.py:28(forward)
                1651704   55.240    0.000 1261.829    0.001 adam.py:55(step)
                 481972    1.788    0.000 1077.747    0.002 conv.py:422(forward)
                 481972    2.122    0.000 1075.343    0.002 conv.py:414(_conv_forward)
                 481972 1072.951    0.002 1072.951    0.002 {built-in method conv2d}
                 120493    6.461    0.000 1072.855    0.009 allGraphs.py:141(transform)
               55747621  261.500    0.000 1037.873    0.000 tensor.py:21(wrapped)
               43095856  202.321    0.000 1000.624    0.000 tensor.py:506(__rsub__)
                1651704  249.103    0.000  980.511    0.001 functional.py:53(adam)
                 120493   22.281    0.000  840.630    0.007 allGraphsTrain.py:33(<listcomp>)
               12169894  383.754    0.000  818.357    0.000 allGraphs.py:114(states)
                 120493    0.828    0.000  816.714    0.007 game.py:42(step)
                 120493    1.105    0.000  802.017    0.007 layers.py:827(step)
               43095856  798.304    0.000  798.304    0.000 {built-in method rsub}
              244002575  239.917    0.000  790.170    0.000 overrides.py:1070(has_torch_function)
              108444100  717.295    0.000  717.295    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 120493    2.466    0.000  660.226    0.005 agent.py:112(__call__)
              398205666  262.849    0.000  623.268    0.000 {built-in method builtins.any}
              512775787  521.971    0.000  521.971    0.000 {built-in method torch._C._get_tracing_state}
                5791678  346.001    0.000  481.919    0.000 BayesianNN.py:43(convert_data)
               42975363  477.084    0.000  477.084    0.000 {method 'gt' of 'torch._C._TensorBase' objects}
                 120493   15.402    0.000  433.579    0.004 layers.py:17(step)
               12049300   30.160    0.000  416.644    0.000 layer.py:106(move)
               71058530  250.394    0.000  410.102    0.000 tensor.py:933(grad)
                 120494   25.454    0.000  365.709    0.003 layers.py:793(update)
              650797875  256.603    0.000  314.793    0.000 overrides.py:1083(<genexpr>)
                1651704   35.759    0.000  312.937    0.000 optimizer.py:167(zero_grad)
             2096090196  263.682    0.000  263.682    0.000 {method 'values' of 'collections.OrderedDict' objects}
               12049300   54.856    0.000  254.440    0.000 layers.py:844(check)
              327044480  248.491    0.000  248.492    0.000 module.py:765(__getattr__)
              122025571  238.349    0.000  238.349    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               20302420  237.092    0.000  237.092    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
        1289944004/1289944002  224.948    0.000  228.240    0.000 {built-in method builtins.len}
                 120493   14.154    0.000  190.691    0.002 allGraphsTrain.py:51(<listcomp>)
               58723250  173.340    0.000  173.340    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                 120493   21.645    0.000  167.856    0.001 allGraphsTrain.py:44(<listcomp>)
               46673950   36.743    0.000  166.847    0.000 flatten.py:39(forward)
               67797021   60.674    0.000  162.911    0.000 {built-in method builtins.all}
               20302420  150.921    0.000  150.921    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                 207623    2.991    0.000  132.062    0.001 layers.py:849(restart)
              140227638   90.371    0.000  123.774    0.000 _VF.py:25(__getattr__)
              139057906  110.993    0.000  110.993    0.000 functional.py:1686(<listcomp>)
                1651704    3.299    0.000  110.896    0.000 loss.py:445(forward)
               12651765  108.022    0.000  108.022    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                1957770  107.602    0.000  107.602    0.000 {built-in method tensor}
                1651704   11.955    0.000  107.596    0.000 functional.py:2637(mse_loss)
                 207623    1.557    0.000  106.976    0.001 level.py:8(__init__)
               12049300   23.870    0.000  105.346    0.000 layers.py:838(isFree)
               11583357  105.267    0.000  105.267    0.000 {built-in method zeros}
               10151210  102.804    0.000  102.804    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                 120493   39.022    0.000  101.149    0.001 agent.py:67(modify)
               44901753   93.809    0.000   93.809    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                1419667    2.366    0.000   93.277    0.000 game.py:38(board)
                 207623    3.733    0.000   93.049    0.000 levels.py:151(generate)
               10151210   92.265    0.000   92.265    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              384342714   91.709    0.000   91.709    0.000 {built-in method builtins.getattr}
              243692485   62.504    0.000   90.158    0.000 enum.py:646(__hash__)
                 996909   15.371    0.000   85.577    0.000 level.py:41(notUsed)
                 843458   48.203    0.000   84.611    0.000 layer.py:175(NoRock_update)
               74684452   67.681    0.000   81.475    0.000 layer.py:103(isFree)
               10151210   79.734    0.000   79.734    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               12049300   78.584    0.000   78.584    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               67643861   60.883    0.000   76.381    0.000 types.py:171(__get__)
                 361479    2.223    0.000   70.342    0.000 tensor.py:576(__iter__)
                 817201   13.787    0.000   69.284    0.000 allGraphs.py:167(format)
              421887964   68.953    0.000   68.953    0.000 _jit_internal.py:750(is_scripting)
              140262956   68.044    0.000   68.044    0.000 {method 'dim' of 'torch._C._TensorBase' objects}
                 361479   66.909    0.000   66.909    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9653093: <Diamonds1_0.0_NN_cpu_0> in cluster <dcc> Done

Job <Diamonds1_0.0_NN_cpu_0> was submitted from host <n-62-30-5> by user <s183905> in cluster <dcc> at Wed May 19 11:40:31 2021
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

    CPU time :                                   35692.96 sec.
    Max Memory :                                 106 MB
    Average Memory :                             99.20 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               16278.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   35709 sec.
    Turnaround time :                            35709 sec.

The output (if any) is above this job summary.

