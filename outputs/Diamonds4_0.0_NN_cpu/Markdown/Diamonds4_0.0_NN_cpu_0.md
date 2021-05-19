/zhome/ee/d/137643/Desktop/Bachelor/project-env/lib/python3.8/site-packages/torch/cuda/__init__.py:52: UserWarning: CUDA initialization: Found no NVIDIA driver on your system. Please check that you have an NVIDIA GPU and installed a driver from http://www.nvidia.com/Download/index.aspx (Triggered internally at  /pytorch/c10/cuda/CUDAFunctions.cpp:100.)
  return torch._C._cuda_getDeviceCount() > 0

# Parameters

    Name :                      Diamonds4_0.0_NN_cpu-0
    Main :                      graphTrain
    Level :                     Levels.Causal7
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


      11932213318 function calls (11447561534 primitive calls) in 35700.48 seconds

##    Ordered by: cumulative time
   List reduced from 444 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35700.483 35700.483 {built-in method builtins.exec}
                      1    0.001    0.001 35700.483 35700.483 <string>:1(<module>)
                      1   35.876   35.876 35700.481 35700.481 allGraphsTrain.py:13(graphTrain)
                 125867   26.882    0.000 25998.024    0.207 allGraphsTrain.py:40(<listcomp>)
                 910405    5.867    0.000 25960.506    0.029 allGraphs.py:179(getInterventionsmodel)
        41113899/755801 2238.834    0.000 24461.773    0.032 allGraphs.py:186(recursiveBEST)
        489965297/46107937 2695.863    0.000 21915.674    0.000 module.py:715(_call_impl)
               44385736  852.029    0.000 21411.155    0.000 container.py:115(forward)
               44134002  147.408    0.000 20706.013    0.000 BayesianNN.py:18(forward)
               38127050 1225.476    0.000 19111.710    0.001 BayesianNN.py:65(predict_no_convert)
              132402006  187.756    0.000 7193.419    0.000 dropout.py:57(forward)
              132402006  703.895    0.000 7005.663    0.000 functional.py:960(dropout)
              132905474  427.018    0.000 6729.039    0.000 linear.py:92(forward)
              132402006 6152.839    0.000 6152.839    0.000 {built-in method dropout}
              132905474  716.033    0.000 6131.883    0.000 functional.py:1669(linear)
                 125867  801.806    0.006 3394.747    0.027 allGraphs.py:156(transformNot)
                1596334   23.082    0.000 3233.538    0.002 BayesianNN.py:57(learn)
              132905474 3144.544    0.000 3144.544    0.000 {built-in method addmm}
                1596334   27.435    0.000 3063.503    0.002 BayesianNN.py:21(learn)
                4410618   62.970    0.000 2587.680    0.001 BayesianNN.py:61(predict)
                 125867    0.955    0.000 2131.430    0.017 agent.py:29(learn)
                 125867   20.672    0.000 2130.108    0.017 agent.py:117(_learn)
                 125867   13.062    0.000 2109.436    0.017 learner.py:42(Qlearn)
              133157208  145.710    0.000 2027.732    0.000 activation.py:713(forward)
              133157208  230.925    0.000 1882.023    0.000 functional.py:1292(leaky_relu)
                1722201   14.083    0.000 1655.064    0.001 tensor.py:181(backward)
                1722201    9.293    0.000 1640.981    0.001 __init__.py:68(backward)
              133157208 1626.620    0.000 1626.620    0.000 {built-in method torch._C._nn.leaky_relu}
                1722201 1593.196    0.001 1593.196    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
              132905474 1440.419    0.000 1440.419    0.000 {method 't' of 'torch._C._TensorBase' objects}
          590518/154604   46.804    0.000 1400.584    0.009 allGraphs.py:202(recursiveExplore)
                1722201   15.323    0.000 1392.089    0.001 grad_mode.py:23(decorate_context)
                1722201   62.697    0.000 1347.899    0.001 adam.py:55(step)
                 251734    1.303    0.000 1284.231    0.005 network.py:28(forward)
                 125867    8.769    0.000 1169.983    0.009 allGraphs.py:141(transform)
                 503468    2.439    0.000 1077.298    0.002 conv.py:422(forward)
                 503468    2.903    0.000 1074.100    0.002 conv.py:414(_conv_forward)
                 503468 1070.910    0.002 1070.910    0.002 {built-in method conv2d}
                1722201  268.279    0.000 1042.581    0.001 functional.py:53(adam)
               54135914  249.439    0.000 1036.769    0.000 tensor.py:21(wrapped)
               40919879  195.761    0.000  975.299    0.000 tensor.py:506(__rsub__)
                 125867    0.959    0.000  845.537    0.007 game.py:42(step)
                 125867   11.726    0.000  830.869    0.007 allGraphsTrain.py:33(<listcomp>)
                 125867    1.504    0.000  824.989    0.007 layers.py:827(step)
               12712668  395.851    0.000  819.150    0.000 allGraphs.py:114(states)
              241879457  241.038    0.000  817.734    0.000 overrides.py:1070(has_torch_function)
               40919879  779.538    0.000  779.538    0.000 {built-in method rsub}
              113280700  691.469    0.000  691.469    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
              390634956  262.100    0.000  651.708    0.000 {built-in method builtins.any}
                 125867    2.922    0.000  629.576    0.005 agent.py:112(__call__)
              490342898  546.860    0.000  546.860    0.000 {built-in method torch._C._get_tracing_state}
                6006952  373.654    0.000  531.296    0.000 BayesianNN.py:43(convert_data)
               40794012  479.442    0.000  479.442    0.000 {method 'gt' of 'torch._C._TensorBase' objects}
                 125867   16.950    0.000  465.361    0.004 layers.py:17(step)
               12586700   31.994    0.000  446.777    0.000 layer.py:106(move)
               74094640  266.206    0.000  431.469    0.000 tensor.py:933(grad)
                 125868   28.718    0.000  356.183    0.003 layers.py:793(update)
              640958681  256.733    0.000  341.991    0.000 overrides.py:1083(<genexpr>)
                1722201   37.379    0.000  322.991    0.000 optimizer.py:167(zero_grad)
               12586700   57.229    0.000  269.773    0.000 layers.py:844(check)
             2004246924  261.114    0.000  261.114    0.000 {method 'values' of 'collections.OrderedDict' objects}
              312800503  254.951    0.000  254.952    0.000 module.py:765(__getattr__)
               21169880  248.143    0.000  248.143    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              127464734  233.079    0.000  233.079    0.000 {method 'item' of 'torch._C._TensorBase' objects}
        1244274156/1244274154  219.970    0.000  223.236    0.000 {built-in method builtins.len}
                 125867   15.777    0.000  200.855    0.002 allGraphsTrain.py:51(<listcomp>)
                 125867   24.233    0.000  184.948    0.001 allGraphsTrain.py:44(<listcomp>)
               57224170  180.137    0.000  180.137    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               44637470   39.408    0.000  172.324    0.000 flatten.py:39(forward)
               21169880  154.236    0.000  154.236    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               66722714   55.322    0.000  150.099    0.000 {built-in method builtins.all}
                2100774  142.705    0.000  142.705    0.000 {built-in method tensor}
                1722201    4.373    0.000  132.103    0.000 loss.py:445(forward)
                1722201   14.930    0.000  127.730    0.000 functional.py:2637(mse_loss)
                1539741    2.860    0.000  126.624    0.000 game.py:38(board)
              134124207   90.699    0.000  126.371    0.000 _VF.py:25(__getattr__)
               12013905  122.914    0.000  122.914    0.000 {built-in method zeros}
              376119033  121.042    0.000  121.042    0.000 {built-in method builtins.getattr}
                 181177    2.993    0.000  117.775    0.001 layers.py:849(restart)
               12586700   27.164    0.000  116.064    0.000 layers.py:838(isFree)
               13216035  113.615    0.000  113.615    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                 125867   41.692    0.000  112.598    0.001 agent.py:67(modify)
              132905474  111.598    0.000  111.598    0.000 functional.py:1686(<listcomp>)
               10584940  109.384    0.000  109.384    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               10584940  101.260    0.000  101.260    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               42789402   98.481    0.000   98.481    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                 181177    1.601    0.000   94.845    0.001 level.py:8(__init__)
              247987905   65.286    0.000   93.972    0.000 enum.py:646(__hash__)
                 881076   52.480    0.000   92.436    0.000 layer.py:175(NoRock_update)
                 910405   13.862    0.000   91.523    0.000 allGraphs.py:167(format)
               79562935   73.788    0.000   88.900    0.000 layer.py:103(isFree)
               12586700   88.264    0.000   88.264    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               10584940   84.621    0.000   84.621    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                 181177    3.490    0.000   82.011    0.000 levels.py:456(generate)
               68729365   62.777    0.000   80.460    0.000 types.py:171(__get__)
                 377601    2.487    0.000   78.555    0.000 tensor.py:576(__iter__)
                 869264   14.198    0.000   75.117    0.000 level.py:41(notUsed)
                 377601   74.381    0.000   74.381    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
                1722201   74.356    0.000   74.356    0.000 {built-in method torch._C._nn.mse_loss}
               10584940   71.941    0.000   71.941    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9653102: <Diamonds4_0.0_NN_cpu_0> in cluster <dcc> Done

Job <Diamonds4_0.0_NN_cpu_0> was submitted from host <n-62-30-5> by user <s183905> in cluster <dcc> at Wed May 19 11:40:33 2021
Job was executed on host(s) <n-62-21-103>, in queue <hpc>, as user <s183905> in cluster <dcc> at Wed May 19 11:40:35 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 19 11:40:35 2021
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

    CPU time :                                   35700.64 sec.
    Max Memory :                                 108 MB
    Average Memory :                             103.63 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               16276.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   35768 sec.
    Turnaround time :                            35707 sec.

The output (if any) is above this job summary.

