/zhome/ee/d/137643/Desktop/Bachelor/project-env/lib/python3.8/site-packages/torch/cuda/__init__.py:52: UserWarning: CUDA initialization: Found no NVIDIA driver on your system. Please check that you have an NVIDIA GPU and installed a driver from http://www.nvidia.com/Download/index.aspx (Triggered internally at  /pytorch/c10/cuda/CUDAFunctions.cpp:100.)
  return torch._C._cuda_getDeviceCount() > 0

# Parameters

    Name :                      Diamonds1_0.5_NN_cpu_2-2
    Main :                      graphTrain
    Level :                     Levels.Causal2
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


      16992193047 function calls (16663537760 primitive calls) in 35700.23 seconds

##    Ordered by: cumulative time
   List reduced from 440 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35700.230 35700.230 {built-in method builtins.exec}
                      1    0.002    0.002 35700.230 35700.230 <string>:1(<module>)
                      1  100.931  100.931 35700.227 35700.227 allGraphsTrain.py:13(graphTrain)
        347727319/38990369 1296.648    0.000 12230.721    0.000 module.py:715(_call_impl)
               30873695  350.994    0.000 11583.593    0.000 container.py:115(forward)
                 365560 1892.185    0.005 11511.831    0.031 allGraphs.py:156(transformNot)
                7751114   76.884    0.000 10950.970    0.001 BayesianNN.py:57(learn)
                 365560   76.236    0.000 10448.564    0.029 allGraphsTrain.py:40(<listcomp>)
                7751114   92.043    0.000 10390.657    0.001 BayesianNN.py:21(learn)
                6239226   22.362    0.000 10326.537    0.002 allGraphs.py:179(getInterventionsmodel)
               30142575   70.800    0.000 9199.078    0.000 BayesianNN.py:18(forward)
        25333245/6033704  962.893    0.000 8718.447    0.001 allGraphs.py:186(recursiveBEST)
               22391461  226.010    0.000 8307.706    0.000 BayesianNN.py:61(predict)
                8116674   48.800    0.000 4771.940    0.001 grad_mode.py:23(decorate_context)
                8116674  226.332    0.000 4632.387    0.001 adam.py:55(step)
                 365560    2.551    0.000 4241.793    0.012 agent.py:29(learn)
                 365560   52.656    0.000 4238.405    0.012 agent.py:117(_learn)
                 365560   30.141    0.000 4185.749    0.011 learner.py:42(Qlearn)
                8116674   39.726    0.000 3956.775    0.000 tensor.py:181(backward)
                8116674   29.385    0.000 3917.049    0.000 __init__.py:68(backward)
                8116674 3770.483    0.000 3770.483    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                8116674  881.077    0.000 3502.287    0.000 functional.py:53(adam)
               91889965  200.723    0.000 3227.491    0.000 linear.py:92(forward)
               90427725   75.965    0.000 3112.646    0.000 dropout.py:57(forward)
               90427725  299.226    0.000 3036.681    0.000 functional.py:960(dropout)
               91889965  344.869    0.000 2933.874    0.000 functional.py:1669(linear)
                 731120    2.684    0.000 2694.745    0.004 network.py:28(forward)
               90427725 2656.652    0.000 2656.652    0.000 {built-in method dropout}
                 365560   21.481    0.000 2610.955    0.007 allGraphs.py:141(transform)
                1462240    5.309    0.000 2140.120    0.001 conv.py:422(forward)
                1462240    6.689    0.000 2132.753    0.001 conv.py:414(_conv_forward)
                1462240 2125.247    0.001 2125.247    0.001 {built-in method conv2d}
                 365560   59.976    0.000 1946.093    0.005 allGraphsTrain.py:33(<listcomp>)
                 365560    2.609    0.000 1897.916    0.005 game.py:42(step)
               36921661  913.854    0.000 1886.122    0.000 allGraphs.py:114(states)
                 365560    3.316    0.000 1854.426    0.005 layers.py:827(step)
               30142575 1341.240    0.000 1824.580    0.000 BayesianNN.py:43(convert_data)
              329004400 1607.795    0.000 1607.795    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
              346018208  947.275    0.000 1589.214    0.000 tensor.py:933(grad)
               91889965 1524.214    0.000 1524.214    0.000 {built-in method addmm}
                 365560    7.789    0.000 1428.271    0.004 agent.py:112(__call__)
          823906/205522   44.853    0.000 1275.945    0.006 allGraphs.py:202(recursiveExplore)
                8116674  143.829    0.000 1184.127    0.000 optimizer.py:167(zero_grad)
               92621085   72.930    0.000 1117.616    0.000 activation.py:713(forward)
              532328033  335.555    0.000 1051.952    0.000 overrides.py:1070(has_torch_function)
               92621085  113.182    0.000 1044.687    0.000 functional.py:1292(leaky_relu)
                 365561   66.182    0.000  924.146    0.003 layers.py:793(update)
                 365560   45.030    0.000  922.143    0.003 layers.py:17(step)
               92621085  918.424    0.000  918.424    0.000 {built-in method torch._C._nn.leaky_relu}
               98862328  881.966    0.000  881.966    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               36556000   78.976    0.000  872.835    0.000 layer.py:106(move)
              676352863  322.560    0.000  842.407    0.000 {built-in method builtins.any}
               58667285  172.239    0.000  781.235    0.000 tensor.py:21(wrapped)
               91889965  654.149    0.000  654.149    0.000 {method 't' of 'torch._C._TensorBase' objects}
              373314434  580.414    0.000  580.414    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               98862328  554.314    0.000  554.314    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                 365560   32.309    0.000  454.102    0.001 allGraphsTrain.py:51(<listcomp>)
                 365560   56.473    0.000  433.191    0.001 allGraphsTrain.py:44(<listcomp>)
             1201534617  324.736    0.000  399.243    0.000 overrides.py:1083(<genexpr>)
               36556000  102.417    0.000  396.890    0.000 layers.py:844(check)
                8116674   11.512    0.000  391.049    0.000 loss.py:445(forward)
                8116674   46.198    0.000  379.536    0.000 functional.py:2637(mse_loss)
                9634736  378.028    0.000  378.028    0.000 {built-in method tensor}
               60285151  360.804    0.000  360.804    0.000 {built-in method zeros}
                8067027    8.725    0.000  345.694    0.000 game.py:38(board)
                 654583    8.279    0.000  342.565    0.001 layers.py:849(restart)
               49431164  334.003    0.000  334.003    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               49431164  328.851    0.000  328.851    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               20283485   67.117    0.000  318.120    0.000 tensor.py:506(__rsub__)
               36556000   69.105    0.000  317.396    0.000 layers.py:838(isFree)
                6239226   54.944    0.000  307.357    0.000 allGraphs.py:167(format)
                 654583    4.430    0.000  276.426    0.000 level.py:8(__init__)
               49431164  272.621    0.000  272.621    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               38383800  253.124    0.000  253.124    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               20283485  251.003    0.000  251.003    0.000 {built-in method rsub}
              248023993  209.833    0.000  248.292    0.000 layer.py:103(isFree)
                 365560   90.080    0.000  245.923    0.001 agent.py:67(modify)
                 654583   10.077    0.000  238.491    0.000 levels.py:151(generate)
               49431164  232.926    0.000  232.926    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              348823999  228.768    0.000  228.768    0.000 {built-in method torch._C._get_tracing_state}
                3141959   39.451    0.000  217.712    0.000 level.py:41(notUsed)
                8116674  215.620    0.000  215.620    0.000 {built-in method torch._C._nn.mse_loss}
                2558927  122.705    0.000  213.528    0.000 layer.py:175(NoRock_update)
               36556000  203.898    0.000  203.898    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
              574890760  137.800    0.000  197.603    0.000 enum.py:646(__hash__)
               95223385   46.317    0.000  195.865    0.000 {built-in method builtins.all}
               40227137  191.375    0.000  191.375    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               68160815  189.437    0.000  189.437    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                1096680    5.538    0.000  184.938    0.000 tensor.py:576(__iter__)
                1096680  176.070    0.000  176.070    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               19917925  175.940    0.000  175.940    0.000 {method 'gt' of 'torch._C._TensorBase' objects}
               49431274   72.021    0.000  164.437    0.000 tensor.py:596(__hash__)
              225330296  146.221    0.000  146.221    0.000 module.py:765(__getattr__)
             1421782971  143.222    0.000  143.222    0.000 {method 'values' of 'collections.OrderedDict' objects}
        1179387370/1179387368  130.433    0.000  136.861    0.000 {built-in method builtins.len}
               49431164  127.852    0.000  127.852    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              117279013   37.820    0.000  122.801    0.000 layers.py:799(<genexpr>)
              287212136   94.148    0.000  114.452    0.000 layers.py:809(<genexpr>)
                8116674   37.425    0.000  108.885    0.000 __init__.py:28(_make_grads)
              143012576   82.618    0.000  107.815    0.000 types.py:171(__get__)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9668391: <Diamonds1_0.5_NN_cpu_2_2> in cluster <dcc> Done

Job <Diamonds1_0.5_NN_cpu_2_2> was submitted from host <n-62-30-8> by user <s183905> in cluster <dcc> at Wed May 19 22:58:59 2021
Job was executed on host(s) <n-62-11-62>, in queue <hpc>, as user <s183905> in cluster <dcc> at Wed May 19 22:59:00 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 19 22:59:00 2021
Terminated at Thu May 20 08:54:02 2021
Results reported at Thu May 20 08:54:02 2021

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

    CPU time :                                   35615.02 sec.
    Max Memory :                                 107 MB
    Average Memory :                             101.76 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               16277.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   35771 sec.
    Turnaround time :                            35703 sec.

The output (if any) is above this job summary.

