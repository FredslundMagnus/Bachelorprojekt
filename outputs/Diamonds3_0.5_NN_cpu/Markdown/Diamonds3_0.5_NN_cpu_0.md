/zhome/ee/d/137643/Desktop/Bachelor/project-env/lib/python3.8/site-packages/torch/cuda/__init__.py:52: UserWarning: CUDA initialization: Found no NVIDIA driver on your system. Please check that you have an NVIDIA GPU and installed a driver from http://www.nvidia.com/Download/index.aspx (Triggered internally at  /pytorch/c10/cuda/CUDAFunctions.cpp:100.)
  return torch._C._cuda_getDeviceCount() > 0

# Parameters

    Name :                      Diamonds3_0.5_NN_cpu-0
    Main :                      graphTrain
    Level :                     Levels.Causal6
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


      12026406169 function calls (11502147868 primitive calls) in 35702.29 seconds

##    Ordered by: cumulative time
   List reduced from 442 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35702.294 35702.294 {built-in method builtins.exec}
                      1    0.001    0.001 35702.293 35702.293 <string>:1(<module>)
                      1   29.109   29.109 35702.292 35702.292 allGraphsTrain.py:13(graphTrain)
                 105466   19.973    0.000 27103.430    0.257 allGraphsTrain.py:40(<listcomp>)
                 560231    3.142    0.000 27077.333    0.048 allGraphs.py:179(getInterventionsmodel)
        43771697/405536 2284.691    0.000 25143.233    0.062 allGraphs.py:186(recursiveBEST)
        529775105/49500045 2769.404    0.000 22629.675    0.000 module.py:715(_call_impl)
               48027506  858.800    0.000 22145.656    0.000 container.py:115(forward)
               47816574  151.915    0.000 21444.643    0.000 BayesianNN.py:18(forward)
               41742322 1300.616    0.000 20090.781    0.000 BayesianNN.py:65(predict_no_convert)
              143449722  180.270    0.000 7396.360    0.000 dropout.py:57(forward)
              143449722  704.421    0.000 7216.089    0.000 functional.py:960(dropout)
              143871586  527.682    0.000 7029.781    0.000 linear.py:92(forward)
              143449722 6353.181    0.000 6353.181    0.000 {built-in method dropout}
              143871586  735.856    0.000 6318.166    0.000 functional.py:1669(linear)
                 105466  790.092    0.007 3493.476    0.033 allGraphs.py:156(transformNot)
              143871586 3235.619    0.000 3235.619    0.000 {built-in method addmm}
                4707179   64.179    0.000 2624.242    0.001 BayesianNN.py:61(predict)
                1367073   16.593    0.000 2604.552    0.002 BayesianNN.py:57(learn)
                1367073   21.361    0.000 2481.119    0.002 BayesianNN.py:21(learn)
              144082518  145.993    0.000 2071.249    0.000 activation.py:713(forward)
                 105466    0.672    0.000 1928.568    0.018 agent.py:29(learn)
                 105466    8.152    0.000 1927.578    0.018 agent.py:117(_learn)
              144082518  241.095    0.000 1925.256    0.000 functional.py:1292(leaky_relu)
                 105466    8.783    0.000 1919.427    0.018 learner.py:42(Qlearn)
          771363/154695   57.714    0.000 1878.657    0.012 allGraphs.py:202(recursiveExplore)
              144082518 1658.244    0.000 1658.244    0.000 {built-in method torch._C._nn.leaky_relu}
              143871586 1516.550    0.000 1516.550    0.000 {method 't' of 'torch._C._TensorBase' objects}
                1472539   10.586    0.000 1450.995    0.001 tensor.py:181(backward)
                1472539    6.571    0.000 1440.409    0.001 __init__.py:68(backward)
                1472539 1403.675    0.001 1403.675    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                 210932    0.896    0.000 1300.916    0.006 network.py:28(forward)
                1472539   10.635    0.000 1162.683    0.001 grad_mode.py:23(decorate_context)
                 421864    1.636    0.000 1140.991    0.003 conv.py:422(forward)
                 421864    1.734    0.000 1138.776    0.003 conv.py:414(_conv_forward)
                 421864 1136.787    0.003 1136.787    0.003 {built-in method conv2d}
                1472539   50.464    0.000 1130.513    0.001 adam.py:55(step)
               44088295  203.595    0.000 1036.953    0.000 tensor.py:506(__rsub__)
               55162225  265.478    0.000 1011.978    0.000 tensor.py:21(wrapped)
                 105466   24.266    0.000  880.777    0.008 allGraphsTrain.py:33(<listcomp>)
                1472539  222.536    0.000  869.398    0.001 functional.py:53(adam)
               10652167  426.676    0.000  856.520    0.000 allGraphs.py:114(states)
               44088295  833.357    0.000  833.357    0.000 {built-in method rsub}
              236855279  237.059    0.000  778.615    0.000 overrides.py:1070(has_torch_function)
              116013100  682.729    0.000  682.729    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 105466    2.256    0.000  677.724    0.006 agent.py:112(__call__)
                 105466    0.726    0.000  631.381    0.006 game.py:42(step)
              394133464  260.814    0.000  618.720    0.000 {built-in method builtins.any}
                 105466    1.010    0.000  618.094    0.006 layers.py:827(step)
              530091503  565.676    0.000  565.676    0.000 {built-in method torch._C._get_tracing_state}
                6074252  359.939    0.000  498.046    0.000 BayesianNN.py:43(convert_data)
               43982829  466.300    0.000  466.300    0.000 {method 'gt' of 'torch._C._TensorBase' objects}
                 105466    4.216    0.000  417.385    0.004 allGraphs.py:141(transform)
               63323222  230.655    0.000  377.864    0.000 tensor.py:933(grad)
                 105466   14.140    0.000  322.691    0.003 layers.py:17(step)
              638196339  256.219    0.000  310.658    0.000 overrides.py:1083(<genexpr>)
               10546600   27.021    0.000  307.115    0.000 layer.py:106(move)
                 105467   21.917    0.000  293.015    0.003 layers.py:793(update)
             2167127926  291.813    0.000  291.813    0.000 {method 'values' of 'collections.OrderedDict' objects}
                1472539   31.973    0.000  279.657    0.000 optimizer.py:167(zero_grad)
              337981984  265.443    0.000  265.443    0.000 module.py:765(__getattr__)
              127927613  245.243    0.000  245.243    0.000 {method 'item' of 'torch._C._TensorBase' objects}
        1313873096/1313873094  216.228    0.000  219.109    0.000 {built-in method builtins.len}
               18092332  210.274    0.000  210.274    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               48238438   39.763    0.000  180.254    0.000 flatten.py:39(forward)
               58785038  179.256    0.000  179.256    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                 105466   13.192    0.000  172.468    0.002 allGraphsTrain.py:51(<listcomp>)
               65708925   59.890    0.000  169.406    0.000 {built-in method builtins.all}
               10546600   38.220    0.000  155.726    0.000 layers.py:844(check)
                 105466   21.718    0.000  153.302    0.001 allGraphsTrain.py:44(<listcomp>)
               18092332  134.248    0.000  134.248    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              144922261   94.822    0.000  133.937    0.000 _VF.py:25(__getattr__)
              143871586  116.906    0.000  116.906    0.000 functional.py:1686(<listcomp>)
               12148505  105.397    0.000  105.397    0.000 {built-in method zeros}
               46660433  102.546    0.000  102.546    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               10546600   25.395    0.000  101.209    0.000 layers.py:838(isFree)
                1472539    2.945    0.000   97.211    0.000 loss.py:445(forward)
               11073930   96.305    0.000   96.305    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                1472539   10.728    0.000   94.266    0.000 functional.py:2637(mse_loss)
              381884958   93.662    0.000   93.662    0.000 {built-in method builtins.getattr}
                1562967   92.371    0.000   92.371    0.000 {built-in method tensor}
                9046166   90.192    0.000   90.192    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                 105466   29.628    0.000   83.340    0.001 agent.py:67(modify)
                9046166   81.708    0.000   81.708    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               71623311   62.424    0.000   78.969    0.000 types.py:171(__get__)
                1087562    1.843    0.000   78.748    0.000 game.py:38(board)
                 843736   43.015    0.000   77.528    0.000 layer.py:175(NoRock_update)
               77778728   61.558    0.000   75.814    0.000 layer.py:103(isFree)
              435821563   73.708    0.000   73.708    0.000 _jit_internal.py:750(is_scripting)
              144926366   70.934    0.000   70.934    0.000 {method 'dim' of 'torch._C._TensorBase' objects}
               10546600   70.807    0.000   70.807    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                9046166   69.824    0.000   69.824    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              167910555   45.259    0.000   65.986    0.000 enum.py:646(__hash__)
                  85179    1.521    0.000   65.767    0.001 layers.py:849(restart)
              165486675   63.512    0.000   63.512    0.000 tensor.py:24(<genexpr>)
                 316398    2.011    0.000   60.530    0.000 tensor.py:576(__iter__)
                2677604   60.489    0.000   60.489    0.000 {built-in method cat}
               48027506   40.557    0.000   58.737    0.000 container.py:107(__iter__)
               42949971   17.216    0.000   57.898    0.000 layers.py:799(<genexpr>)
                 316398   57.447    0.000   57.447    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9653087: <Diamonds3_0.5_NN_cpu_0> in cluster <dcc> Done

Job <Diamonds3_0.5_NN_cpu_0> was submitted from host <n-62-30-5> by user <s183905> in cluster <dcc> at Wed May 19 11:40:30 2021
Job was executed on host(s) <n-62-21-107>, in queue <hpc>, as user <s183905> in cluster <dcc> at Wed May 19 11:40:31 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 19 11:40:31 2021
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

Successfully completed.

Resource usage summary:

    CPU time :                                   35704.78 sec.
    Max Memory :                                 110 MB
    Average Memory :                             104.58 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               16274.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   35709 sec.
    Turnaround time :                            35712 sec.

The output (if any) is above this job summary.

/zhome/ee/d/137643/Desktop/Bachelor/project-env/lib/python3.8/site-packages/torch/cuda/__init__.py:52: UserWarning: CUDA initialization: Found no NVIDIA driver on your system. Please check that you have an NVIDIA GPU and installed a driver from http://www.nvidia.com/Download/index.aspx (Triggered internally at  /pytorch/c10/cuda/CUDAFunctions.cpp:100.)
  return torch._C._cuda_getDeviceCount() > 0

# Parameters

    Name :                      Diamonds3_0.5_NN_cpu-0
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
    Num :                       0
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      16803265420 function calls (16441925534 primitive calls) in 35700.29 seconds

##    Ordered by: cumulative time
   List reduced from 441 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35700.295 35700.295 {built-in method builtins.exec}
                      1    0.001    0.001 35700.294 35700.294 <string>:1(<module>)
                      1   76.293   76.293 35700.293 35700.293 allGraphsTrain.py:13(graphTrain)
        379729548/41236038 1438.606    0.000 12535.112    0.000 module.py:715(_call_impl)
                 325472   65.187    0.000 12091.170    0.037 allGraphsTrain.py:40(<listcomp>)
                5244169   19.455    0.000 11983.485    0.002 allGraphs.py:179(getInterventionsmodel)
               33849351  384.933    0.000 11908.038    0.000 container.py:115(forward)
                 325472 2026.552    0.006 11631.579    0.036 allGraphs.py:156(transformNot)
               33198407   77.513    0.000 10135.898    0.000 BayesianNN.py:18(forward)
                7061215   69.921    0.000 10061.461    0.001 BayesianNN.py:57(learn)
        27060270/5037113 1114.670    0.000 9953.795    0.002 allGraphs.py:186(recursiveBEST)
               26137192  257.525    0.000 9714.993    0.000 BayesianNN.py:61(predict)
                7061215   84.099    0.000 9565.811    0.001 BayesianNN.py:21(learn)
                7386687   42.927    0.000 4341.788    0.001 grad_mode.py:23(decorate_context)
                7386687  207.886    0.000 4218.099    0.001 adam.py:55(step)
                 325472    1.953    0.000 3885.074    0.012 agent.py:29(learn)
                 325472   37.431    0.000 3882.220    0.012 agent.py:117(_learn)
                 325472   24.268    0.000 3844.789    0.012 learner.py:42(Qlearn)
                7386687   37.928    0.000 3788.031    0.001 tensor.py:181(backward)
                7386687   23.975    0.000 3750.103    0.001 __init__.py:68(backward)
                7386687 3617.161    0.000 3617.161    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
              100897109  220.015    0.000 3484.032    0.000 linear.py:92(forward)
               99595221   85.177    0.000 3432.302    0.000 dropout.py:57(forward)
               99595221  330.594    0.000 3347.125    0.000 functional.py:960(dropout)
              100897109  389.017    0.000 3172.394    0.000 functional.py:1669(linear)
                7386687  798.901    0.000 3160.327    0.000 functional.py:53(adam)
               99595221 2922.699    0.000 2922.699    0.000 {built-in method dropout}
                 650944    2.149    0.000 2111.862    0.003 network.py:28(forward)
                 325472   42.621    0.000 2106.393    0.006 allGraphsTrain.py:33(<listcomp>)
               32872773  994.698    0.000 2063.778    0.000 allGraphs.py:114(states)
               33198407 1440.001    0.000 1980.200    0.000 BayesianNN.py:43(convert_data)
                 325472   16.437    0.000 1799.968    0.006 allGraphs.py:141(transform)
              358019700 1754.298    0.000 1754.298    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 325472    1.883    0.000 1717.957    0.005 game.py:42(step)
         1029863/207056   61.273    0.000 1715.889    0.008 allGraphs.py:202(recursiveExplore)
                1301888    4.465    0.000 1715.699    0.001 conv.py:422(forward)
                1301888    4.999    0.000 1709.389    0.001 conv.py:414(_conv_forward)
                1301888 1703.757    0.001 1703.757    0.001 {built-in method conv2d}
                 325472    2.792    0.000 1682.808    0.005 layers.py:827(step)
              100897109 1626.044    0.000 1626.044    0.000 {built-in method addmm}
              314797522  883.090    0.000 1504.653    0.000 tensor.py:933(grad)
                7386687  134.534    0.000 1116.917    0.000 optimizer.py:167(zero_grad)
              101548053   73.344    0.000 1086.398    0.000 activation.py:713(forward)
                 325472    5.904    0.000 1068.747    0.003 agent.py:112(__call__)
              500410008  329.570    0.000 1043.654    0.000 overrides.py:1070(has_torch_function)
              101548053  120.103    0.000 1013.054    0.000 functional.py:1292(leaky_relu)
                 325472   37.035    0.000  886.108    0.003 layers.py:17(step)
              101548053  879.439    0.000  879.439    0.000 {built-in method torch._C._nn.leaky_relu}
               32547200   68.807    0.000  845.262    0.000 layer.py:106(move)
              648205458  327.599    0.000  843.676    0.000 {built-in method builtins.any}
                 325473   57.812    0.000  790.440    0.002 layers.py:793(update)
               89942132  787.325    0.000  787.325    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               57345996  166.144    0.000  746.785    0.000 tensor.py:21(wrapped)
              100897109  707.520    0.000  707.520    0.000 {method 't' of 'torch._C._TensorBase' objects}
              397630715  608.009    0.000  608.009    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               89942132  501.190    0.000  501.190    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               32547200  102.270    0.000  419.297    0.000 layers.py:844(check)
               66396815  405.849    0.000  405.849    0.000 {built-in method zeros}
                 325472   27.109    0.000  395.892    0.001 allGraphsTrain.py:51(<listcomp>)
             1141461326  322.858    0.000  395.586    0.000 overrides.py:1083(<genexpr>)
                 325472   48.828    0.000  387.567    0.001 allGraphsTrain.py:44(<listcomp>)
               23171436   75.750    0.000  368.859    0.000 tensor.py:506(__rsub__)
                8271076  359.894    0.000  359.894    0.000 {built-in method tensor}
                7386687   10.703    0.000  358.971    0.000 loss.py:445(forward)
                7386687   42.169    0.000  348.268    0.000 functional.py:2637(mse_loss)
                6871530    7.192    0.000  329.914    0.000 game.py:38(board)
               44971066  305.060    0.000  305.060    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               44971066  301.824    0.000  301.824    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               23171436  293.110    0.000  293.110    0.000 {built-in method rsub}
                5244169   44.284    0.000  292.169    0.000 allGraphs.py:167(format)
               32547200   67.095    0.000  288.986    0.000 layers.py:838(isFree)
                 422333    5.847    0.000  265.827    0.001 layers.py:849(restart)
              380705964  244.974    0.000  244.974    0.000 {built-in method torch._C._get_tracing_state}
               44971066  241.625    0.000  241.625    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              249226265  184.334    0.000  221.892    0.000 layer.py:103(isFree)
               34174560  220.838    0.000  220.838    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                 422333    2.987    0.000  220.323    0.001 level.py:8(__init__)
               44971066  209.670    0.000  209.670    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                 325472   75.731    0.000  209.063    0.001 agent.py:67(modify)
               42881652  205.911    0.000  205.911    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                7386687  199.509    0.000  199.509    0.000 {built-in method torch._C._nn.mse_loss}
                2603784  110.887    0.000  197.479    0.000 layer.py:175(NoRock_update)
                 422333    7.715    0.000  194.924    0.000 levels.py:303(generate)
               22845964  191.075    0.000  191.075    0.000 {method 'gt' of 'torch._C._TensorBase' objects}
              546237906  128.562    0.000  188.159    0.000 enum.py:646(__hash__)
               67047495  184.687    0.000  184.687    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               32547200  182.032    0.000  182.032    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                2533715   30.746    0.000  179.117    0.000 level.py:41(notUsed)
               89893296   42.333    0.000  169.390    0.000 {built-in method builtins.all}
               44971176   67.589    0.000  155.655    0.000 tensor.py:596(__hash__)
                 976416    4.620    0.000  155.060    0.000 tensor.py:576(__iter__)
             1552767543  152.970    0.000  152.970    0.000 {method 'values' of 'collections.OrderedDict' objects}
        1253904772/1253904770  142.644    0.000  148.345    0.000 {built-in method builtins.len}
              245309549  147.967    0.000  147.968    0.000 module.py:765(__getattr__)
                 976416  147.332    0.000  147.332    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
              152397862   90.671    0.000  117.980    0.000 types.py:171(__get__)
              289124703   94.338    0.000  114.973    0.000 layers.py:809(<genexpr>)
               44971066  113.817    0.000  113.817    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               34500295   25.806    0.000  108.902    0.000 flatten.py:39(forward)
                7386687   34.272    0.000  101.151    0.000 __init__.py:28(_make_grads)


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
Subject: Job 9668369: <Diamonds3_0.5_NN_cpu_0> in cluster <dcc> Exited

Job <Diamonds3_0.5_NN_cpu_0> was submitted from host <n-62-30-8> by user <s183905> in cluster <dcc> at Wed May 19 22:55:25 2021
Job was executed on host(s) <n-62-11-61>, in queue <hpc>, as user <s183905> in cluster <dcc> at Wed May 19 22:55:27 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 19 22:55:27 2021
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

Exited with exit code 1.

Resource usage summary:

    CPU time :                                   35617.29 sec.
    Max Memory :                                 100 MB
    Average Memory :                             94.75 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               16284.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   35732 sec.
    Turnaround time :                            35708 sec.

The output (if any) is above this job summary.

