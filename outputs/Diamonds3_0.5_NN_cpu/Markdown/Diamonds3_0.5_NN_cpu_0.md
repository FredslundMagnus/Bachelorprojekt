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

