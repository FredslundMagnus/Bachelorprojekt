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

