/zhome/ee/d/137643/Desktop/Bachelor/project-env/lib/python3.8/site-packages/torch/cuda/__init__.py:52: UserWarning: CUDA initialization: Found no NVIDIA driver on your system. Please check that you have an NVIDIA GPU and installed a driver from http://www.nvidia.com/Download/index.aspx (Triggered internally at  /pytorch/c10/cuda/CUDAFunctions.cpp:100.)
  return torch._C._cuda_getDeviceCount() > 0

# Parameters

    Name :                      Diamonds3_0.0_NN_cpu-0
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
    Num :                       0
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      9652896814 function calls (9258412528 primitive calls) in 35700.39 seconds

##    Ordered by: cumulative time
   List reduced from 442 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35700.391 35700.391 {built-in method builtins.exec}
                      1    0.001    0.001 35700.391 35700.391 <string>:1(<module>)
                      1   25.637   25.637 35700.389 35700.389 allGraphsTrain.py:13(graphTrain)
                  94107   21.048    0.000 26464.079    0.281 allGraphsTrain.py:40(<listcomp>)
                 482055    2.646    0.000 26438.041    0.055 allGraphs.py:179(getInterventionsmodel)
        31851414/301757 2351.152    0.000 23640.306    0.078 allGraphs.py:186(recursiveBEST)
        399575941/37335491 2407.986    0.000 21702.193    0.001 module.py:715(_call_impl)
               36224045  836.537    0.000 21295.033    0.001 container.py:115(forward)
               36035831  140.108    0.000 20643.785    0.001 BayesianNN.py:18(forward)
               30356088 1181.199    0.000 18672.420    0.001 BayesianNN.py:65(predict_no_convert)
              108107493  142.937    0.000 7073.597    0.000 dropout.py:57(forward)
              108107493  577.832    0.000 6930.661    0.000 functional.py:960(dropout)
              108483921  376.618    0.000 6751.082    0.000 linear.py:92(forward)
              108483921  628.330    0.000 6245.575    0.000 functional.py:1669(linear)
              108107493 6231.204    0.000 6231.204    0.000 {built-in method dropout}
                  94107 1111.335    0.012 3538.821    0.038 allGraphs.py:156(transformNot)
                4662404   69.736    0.000 3377.568    0.001 BayesianNN.py:61(predict)
              108483921 3317.539    0.000 3317.539    0.000 {built-in method addmm}
          874065/180298   89.396    0.000 2757.375    0.015 allGraphs.py:202(recursiveExplore)
                1017339   13.661    0.000 2534.079    0.002 BayesianNN.py:57(learn)
                1017339   17.994    0.000 2401.072    0.002 BayesianNN.py:21(learn)
              108672135  117.430    0.000 2261.715    0.000 activation.py:713(forward)
              108672135  193.894    0.000 2144.284    0.000 functional.py:1292(leaky_relu)
              108672135 1929.661    0.000 1929.661    0.000 {built-in method torch._C._nn.leaky_relu}
                  94107    0.559    0.000 1712.165    0.018 agent.py:29(learn)
                  94107    8.860    0.000 1711.338    0.018 agent.py:117(_learn)
                  94107    9.054    0.000 1702.478    0.018 learner.py:42(Qlearn)
              108483921 1629.657    0.000 1629.657    0.000 {method 't' of 'torch._C._TensorBase' objects}
                1111446    9.250    0.000 1283.377    0.001 tensor.py:181(backward)
                1111446    5.035    0.000 1274.127    0.001 __init__.py:68(backward)
                1111446 1242.383    0.001 1242.383    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                1111446    7.915    0.000 1200.895    0.001 grad_mode.py:23(decorate_context)
                  94107   20.135    0.000 1190.870    0.013 allGraphsTrain.py:33(<listcomp>)
                1111446   39.888    0.000 1177.252    0.001 adam.py:55(step)
                9504908  540.841    0.000 1170.749    0.000 allGraphs.py:114(states)
                 188214    0.737    0.000 1158.188    0.006 network.py:28(forward)
              103518200 1036.097    0.000 1036.097    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
               42218766  234.985    0.000 1007.350    0.000 tensor.py:21(wrapped)
                 376428    1.329    0.000 1000.706    0.003 conv.py:422(forward)
                 376428    1.398    0.000  998.892    0.003 conv.py:414(_conv_forward)
                 376428  997.295    0.003  997.295    0.003 {built-in method conv2d}
               32337531  191.192    0.000  984.248    0.000 tensor.py:506(__rsub__)
                1111446  239.807    0.000  968.947    0.001 functional.py:53(adam)
                  94107    4.470    0.000  850.754    0.009 allGraphs.py:141(transform)
               32337531  793.056    0.000  793.056    0.000 {built-in method rsub}
                5679743  516.306    0.000  694.516    0.000 BayesianNN.py:43(convert_data)
                  94107    0.581    0.000  686.522    0.007 game.py:42(step)
                  94107    0.907    0.000  675.172    0.007 layers.py:827(step)
              399858262  646.472    0.000  646.472    0.000 {built-in method torch._C._get_tracing_state}
              180278018  192.611    0.000  612.750    0.000 overrides.py:1070(has_torch_function)
                  94107    1.825    0.000  609.190    0.006 agent.py:112(__call__)
               32243424  491.312    0.000  491.312    0.000 {method 'gt' of 'torch._C._TensorBase' objects}
              300282399  208.137    0.000  485.194    0.000 {built-in method builtins.any}
                  94107   11.773    0.000  386.081    0.004 layers.py:17(step)
                9410700   23.518    0.000  373.132    0.000 layer.py:106(move)
              113946991  329.754    0.000  329.754    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               47998290  206.808    0.000  319.486    0.000 tensor.py:933(grad)
                  94108   19.596    0.000  287.162    0.003 layers.py:793(update)
                1111446   30.013    0.000  260.817    0.000 optimizer.py:167(zero_grad)
                9410700   47.913    0.000  241.553    0.000 layers.py:844(check)
             1634527809  237.619    0.000  237.619    0.000 {method 'values' of 'collections.OrderedDict' objects}
               13713780  237.207    0.000  237.207    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              485978764  188.710    0.000  235.865    0.000 overrides.py:1083(<genexpr>)
        1013683545/1013683543  215.827    0.000  218.701    0.000 {built-in method builtins.len}
                  94107   14.920    0.000  209.445    0.002 allGraphsTrain.py:51(<listcomp>)
                  94107   26.305    0.000  204.844    0.002 allGraphsTrain.py:44(<listcomp>)
               45822959  195.935    0.000  195.935    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              254962565  192.389    0.000  192.389    0.000 module.py:765(__getattr__)
               36412259   31.158    0.000  173.739    0.000 flatten.py:39(forward)
               13713780  157.992    0.000  157.992    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               11359487  140.364    0.000  140.364    0.000 {built-in method zeros}
               51629566   47.467    0.000  139.912    0.000 {built-in method builtins.all}
                9881235  133.244    0.000  133.244    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               35206706  114.846    0.000  114.846    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
              109218939   69.404    0.000  103.614    0.000 _VF.py:25(__getattr__)
                6856890   97.502    0.000   97.502    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                9410700   95.839    0.000   95.839    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                  94107   35.340    0.000   91.006    0.001 agent.py:67(modify)
              108483921   90.453    0.000   90.453    0.000 functional.py:1686(<listcomp>)
                9410700   21.563    0.000   87.975    0.000 layers.py:838(isFree)
                1111446    2.243    0.000   87.146    0.000 loss.py:445(forward)
                6856890   85.799    0.000   85.799    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                 113232    1.842    0.000   85.030    0.001 layers.py:849(restart)
                1111446    8.124    0.000   84.904    0.000 functional.py:2637(mse_loss)
              224221184   57.542    0.000   83.774    0.000 enum.py:646(__hash__)
                6856890   82.675    0.000   82.675    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              289599167   81.505    0.000   81.505    0.000 {built-in method builtins.getattr}
                2963282   75.681    0.000   75.681    0.000 {built-in method cat}
                1379948   74.529    0.000   74.529    0.000 {built-in method tensor}
              109425111   71.337    0.000   71.337    0.000 {method 'dim' of 'torch._C._TensorBase' objects}
                 113232    0.936    0.000   70.718    0.001 level.py:8(__init__)
               59784305   54.938    0.000   69.801    0.000 types.py:171(__get__)
                8366937   69.731    0.000   69.731    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                 752864   37.984    0.000   68.052    0.000 layer.py:175(NoRock_update)
               69448940   52.714    0.000   66.412    0.000 layer.py:103(isFree)
                6856890   64.372    0.000   64.372    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                 113232    2.495    0.000   62.992    0.001 levels.py:303(generate)
                 952591    1.461    0.000   60.710    0.000 game.py:38(board)
                9410700   37.600    0.000   60.557    0.000 layers.py:424(check)
               36224045   44.566    0.000   59.427    0.000 container.py:107(__iter__)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9653099: <Diamonds3_0.0_NN_cpu_0> in cluster <dcc> Done

Job <Diamonds3_0.0_NN_cpu_0> was submitted from host <n-62-30-5> by user <s183905> in cluster <dcc> at Wed May 19 11:40:32 2021
Job was executed on host(s) <n-62-21-107>, in queue <hpc>, as user <s183905> in cluster <dcc> at Wed May 19 11:40:33 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 19 11:40:33 2021
Terminated at Wed May 19 21:35:39 2021
Results reported at Wed May 19 21:35:39 2021

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

    CPU time :                                   35703.20 sec.
    Max Memory :                                 111 MB
    Average Memory :                             104.18 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               16273.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   35709 sec.
    Turnaround time :                            35707 sec.

The output (if any) is above this job summary.

/zhome/ee/d/137643/Desktop/Bachelor/project-env/lib/python3.8/site-packages/torch/cuda/__init__.py:52: UserWarning: CUDA initialization: Found no NVIDIA driver on your system. Please check that you have an NVIDIA GPU and installed a driver from http://www.nvidia.com/Download/index.aspx (Triggered internally at  /pytorch/c10/cuda/CUDAFunctions.cpp:100.)
  return torch._C._cuda_getDeviceCount() > 0

# Parameters

    Name :                      Diamonds3_0.0_NN_cpu-0
    Main :                      graphTrain
    Level :                     Levels.Causal6
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


      18013157257 function calls (17676791511 primitive calls) in 35700.32 seconds

##    Ordered by: cumulative time
   List reduced from 441 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35700.322 35700.322 {built-in method builtins.exec}
                      1    0.002    0.002 35700.322 35700.322 <string>:1(<module>)
                      1   85.447   85.447 35700.320 35700.320 allGraphsTrain.py:13(graphTrain)
        353165875/38424285 1327.519    0.000 12033.481    0.000 module.py:715(_call_impl)
               31474159  365.582    0.000 11442.827    0.000 container.py:115(forward)
                 335181   67.715    0.000 11192.380    0.033 allGraphsTrain.py:40(<listcomp>)
                5052433   19.054    0.000 11082.422    0.002 allGraphs.py:179(getInterventionsmodel)
        25872552/4890085 1044.310    0.000 9457.128    0.002 allGraphs.py:186(recursiveBEST)
                6614945   65.880    0.000 9417.027    0.001 BayesianNN.py:57(learn)
               30803797   72.329    0.000 9350.587    0.000 BayesianNN.py:18(forward)
                 335181 2050.473    0.006 9246.242    0.028 allGraphs.py:156(transformNot)
               24188852  240.463    0.000 8974.544    0.000 BayesianNN.py:61(predict)
                6614945   79.770    0.000 8932.244    0.001 BayesianNN.py:21(learn)
                 335181    2.334    0.000 4200.974    0.013 agent.py:29(learn)
                 335181   17.493    0.000 4197.791    0.013 agent.py:117(_learn)
                 335181   27.975    0.000 4180.298    0.012 learner.py:42(Qlearn)
                6950126   41.782    0.000 4148.771    0.001 grad_mode.py:23(decorate_context)
                6950126  199.011    0.000 4028.261    0.001 adam.py:55(step)
                6950126   37.075    0.000 3880.166    0.001 tensor.py:181(backward)
                6950126   24.926    0.000 3843.091    0.001 __init__.py:68(backward)
                6950126 3717.927    0.001 3717.927    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                 335181   25.127    0.000 3635.435    0.011 allGraphs.py:141(transform)
               93752115  202.594    0.000 3239.618    0.000 linear.py:92(forward)
               92411391   81.459    0.000 3154.533    0.000 dropout.py:57(forward)
               92411391  302.572    0.000 3073.074    0.000 functional.py:960(dropout)
                6950126  769.410    0.000 3048.766    0.000 functional.py:53(adam)
               93752115  359.284    0.000 2950.282    0.000 functional.py:1669(linear)
               92411391 2688.529    0.000 2688.529    0.000 {built-in method dropout}
                 335181    2.488    0.000 2437.509    0.007 game.py:42(step)
                 670362    2.738    0.000 2405.616    0.004 network.py:28(forward)
                 335181    2.843    0.000 2393.812    0.007 layers.py:827(step)
                 335181   73.563    0.000 2216.220    0.007 allGraphsTrain.py:33(<listcomp>)
               33853382 1029.491    0.000 2142.665    0.000 allGraphs.py:114(states)
                1340724    5.270    0.000 1984.742    0.001 conv.py:422(forward)
                1340724    6.561    0.000 1977.606    0.001 conv.py:414(_conv_forward)
                1340724 1970.393    0.001 1970.393    0.001 {built-in method conv2d}
               30803797 1371.515    0.000 1877.676    0.000 BayesianNN.py:43(convert_data)
              368699600 1817.619    0.000 1817.619    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
               93752115 1526.935    0.000 1526.935    0.000 {built-in method addmm}
              296597886  817.239    0.000 1374.269    0.000 tensor.py:933(grad)
          803625/162348   46.050    0.000 1323.137    0.008 allGraphs.py:202(recursiveExplore)
                 335181    7.113    0.000 1276.762    0.004 agent.py:112(__call__)
                 335181   40.514    0.000 1274.130    0.004 layers.py:17(step)
               33518100   76.426    0.000 1229.932    0.000 layer.py:106(move)
                 335182   63.824    0.000 1112.397    0.003 layers.py:793(update)
               94422477   74.037    0.000 1026.974    0.000 activation.py:713(forward)
                6950126  123.439    0.000 1025.261    0.000 optimizer.py:167(zero_grad)
              473302848  302.961    0.000  959.094    0.000 overrides.py:1070(has_torch_function)
               94422477  117.437    0.000  952.937    0.000 functional.py:1292(leaky_relu)
               94422477  822.860    0.000  822.860    0.000 {built-in method torch._C._nn.leaky_relu}
              613648593  301.531    0.000  792.130    0.000 {built-in method builtins.any}
               33518100  152.584    0.000  766.981    0.000 layers.py:844(check)
               84742236  763.516    0.000  763.516    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               57152930  164.918    0.000  741.047    0.000 tensor.py:21(wrapped)
               93752115  644.095    0.000  644.095    0.000 {method 't' of 'torch._C._TensorBase' objects}
              408835325  640.255    0.000  640.255    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                 824822   10.358    0.000  506.472    0.001 layers.py:849(restart)
               84742236  480.374    0.000  480.374    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                 824822    5.078    0.000  422.051    0.001 level.py:8(__init__)
                 335181   28.742    0.000  409.335    0.001 allGraphsTrain.py:51(<listcomp>)
                 335181   52.205    0.000  396.473    0.001 allGraphsTrain.py:44(<listcomp>)
                 824822   14.544    0.000  375.810    0.000 levels.py:303(generate)
               61607595  372.723    0.000  372.723    0.000 {built-in method zeros}
                8168839  371.344    0.000  371.344    0.000 {built-in method tensor}
             1080939430  302.398    0.000  368.005    0.000 overrides.py:1083(<genexpr>)
               21958925   72.554    0.000  346.160    0.000 tensor.py:506(__rsub__)
                4949648   59.733    0.000  345.898    0.000 level.py:41(notUsed)
                6950126   10.285    0.000  341.121    0.000 loss.py:445(forward)
                6728339    7.616    0.000  338.757    0.000 game.py:38(board)
                6950126   41.176    0.000  330.837    0.000 functional.py:2637(mse_loss)
               33518100   71.849    0.000  315.446    0.000 layers.py:838(isFree)
              936115931  210.244    0.000  302.377    0.000 enum.py:646(__hash__)
               42371118  291.054    0.000  291.054    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               42371118  290.527    0.000  290.527    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                5052433   41.358    0.000  280.844    0.000 allGraphs.py:167(format)
               21958925  273.606    0.000  273.606    0.000 {built-in method rsub}
              263713430  203.775    0.000  243.597    0.000 layer.py:103(isFree)
               42371118  236.045    0.000  236.045    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                 335181   87.809    0.000  234.587    0.001 agent.py:67(modify)
              354171418  232.538    0.000  232.538    0.000 {built-in method torch._C._get_tracing_state}
               35194005  228.950    0.000  228.950    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                2681456  127.610    0.000  223.255    0.000 layer.py:175(NoRock_update)
               90671130   46.815    0.000  212.574    0.000 {built-in method builtins.all}
               42371118  203.575    0.000  203.575    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               39706839  188.674    0.000  188.674    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                6950126  188.271    0.000  188.271    0.000 {built-in method torch._C._nn.mse_loss}
               33518100  186.577    0.000  186.577    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               65662621  181.210    0.000  181.210    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               21623744  179.309    0.000  179.309    0.000 {method 'gt' of 'torch._C._TensorBase' objects}
               33518100  108.915    0.000  179.012    0.000 layers.py:424(check)
                1005543    5.423    0.000  175.811    0.000 tensor.py:576(__iter__)
                4949648    4.563    0.000  168.695    0.000 level.py:38(elementsIn)
                1005543  167.296    0.000  167.296    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
             1444137659  143.279    0.000  143.279    0.000 {method 'values' of 'collections.OrderedDict' objects}
               42371228   62.595    0.000  142.293    0.000 tensor.py:596(__hash__)
        1228500650/1228500648  134.023    0.000  140.422    0.000 {built-in method builtins.len}
              228275793  139.461    0.000  139.462    0.000 module.py:765(__getattr__)
              120424172   40.250    0.000  137.963    0.000 layers.py:799(<genexpr>)
               33518100   80.693    0.000  125.123    0.000 layers.py:437(check)
              147173419   92.481    0.000  118.930    0.000 types.py:171(__get__)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9668381: <Diamonds3_0.0_NN_cpu_0> in cluster <dcc> Done

Job <Diamonds3_0.0_NN_cpu_0> was submitted from host <n-62-30-8> by user <s183905> in cluster <dcc> at Wed May 19 22:55:27 2021
Job was executed on host(s) <n-62-11-62>, in queue <hpc>, as user <s183905> in cluster <dcc> at Wed May 19 22:55:29 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 19 22:55:29 2021
Terminated at Thu May 20 08:50:37 2021
Results reported at Thu May 20 08:50:37 2021

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

    CPU time :                                   35611.74 sec.
    Max Memory :                                 104 MB
    Average Memory :                             97.66 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               16280.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   35734 sec.
    Turnaround time :                            35710 sec.

The output (if any) is above this job summary.

