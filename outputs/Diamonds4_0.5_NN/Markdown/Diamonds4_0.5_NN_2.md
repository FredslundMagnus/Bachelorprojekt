
# Parameters

    Name :                      Diamonds4_0.5_NN-2
    Main :                      graphTrain
    Level :                     Levels.Causal7
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
    Num :                       2
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      12612462319 function calls (11992964855 primitive calls) in 35708.00 seconds

##    Ordered by: cumulative time
   List reduced from 485 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35707.999 35707.999 {built-in method builtins.exec}
                      1    0.001    0.001 35707.998 35707.998 <string>:1(<module>)
                      1   34.410   34.410 35707.997 35707.997 allGraphsTrain.py:13(graphTrain)
                 127509  150.008    0.001 26064.481    0.204 allGraphsTrain.py:40(<listcomp>)
                1206696    5.582    0.000 25906.109    0.021 allGraphs.py:179(getInterventionsmodel)
        52609311/1001120 4461.027    0.000 24214.420    0.024 allGraphs.py:186(recursiveBEST)
               56475783  150.726    0.000 17802.450    0.000 BayesianNN.py:18(forward)
        626129672/58821662 2202.804    0.000 17800.043    0.000 module.py:866(_call_impl)
               48693692 1972.360    0.000 17395.879    0.000 BayesianNN.py:65(predict_no_convert)
               56730801  777.490    0.000 17342.009    0.000 container.py:117(forward)
              169937385  285.792    0.000 6875.087    0.000 linear.py:93(forward)
              169937385  126.680    0.000 6466.006    0.000 functional.py:1737(linear)
              169937385 6309.334    0.000 6309.334    0.000 {built-in method torch._C._nn.linear}
                 127509 1220.695    0.010 5577.527    0.044 allGraphs.py:156(transformNot)
              169427349  121.292    0.000 3974.997    0.000 dropout.py:57(forward)
              169427349  434.200    0.000 3853.706    0.000 functional.py:1059(dropout)
                1963352   25.590    0.000 3510.882    0.002 BayesianNN.py:57(learn)
              169427349 3300.217    0.000 3300.217    0.000 {built-in method dropout}
                1963352   22.024    0.000 3208.959    0.002 BayesianNN.py:21(learn)
                5818739   77.064    0.000 2826.680    0.000 BayesianNN.py:61(predict)
              170192403  107.682    0.000 2756.778    0.000 activation.py:713(forward)
              170192403  118.860    0.000 2649.095    0.000 functional.py:1364(leaky_relu)
              170192403 2508.379    0.000 2508.379    0.000 {built-in method torch._C._nn.leaky_relu}
                 127509    7.195    0.000 1666.346    0.013 allGraphsTrain.py:33(<listcomp>)
               12878510  412.407    0.000 1659.197    0.000 allGraphs.py:114(states)
              129473768 1629.815    0.000 1629.815    0.000 {method 'item' of 'torch._C._TensorBase' objects}
          786424/205576   75.487    0.000 1554.494    0.008 allGraphs.py:202(recursiveExplore)
                2090861   15.947    0.000 1482.398    0.001 optimizer.py:84(wrapper)
                2090861    7.742    0.000 1403.527    0.001 grad_mode.py:24(decorate_context)
                2090861   42.580    0.000 1377.602    0.001 adam.py:55(step)
              114758500 1373.593    0.000 1373.593    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                2090861  279.583    0.000 1290.187    0.001 _functional.py:53(adam)
                7782091  890.926    0.000 1127.079    0.000 BayesianNN.py:43(convert_data)
               52316548   51.956    0.000  916.066    0.000 tensor.py:525(__rsub__)
               52316548  853.982    0.000  853.982    0.000 {built-in method rsub}
                2090861    7.071    0.000  838.656    0.000 tensor.py:195(backward)
                2090861    7.081    0.000  831.310    0.000 __init__.py:68(backward)
                2090861  780.880    0.000  780.880    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                 127509    4.337    0.000  749.679    0.006 allGraphs.py:141(transform)
                 127509    0.496    0.000  446.626    0.004 game.py:42(step)
                 127509    0.752    0.000  419.357    0.003 layers.py:827(step)
                 127509   33.834    0.000  414.289    0.003 allGraphsTrain.py:44(<listcomp>)
              626512199  389.413    0.000  389.413    0.000 {built-in method torch._C._get_tracing_state}
                 127509    0.480    0.000  290.893    0.002 agent.py:29(learn)
                 127509    3.132    0.000  290.132    0.002 agent.py:117(_learn)
                 127509    9.415    0.000  287.000    0.002 learner.py:42(Qlearn)
        2798755158/2798755156  285.590    0.000  286.824    0.000 {built-in method builtins.len}
               25600368  263.383    0.000  263.383    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               25600368  232.722    0.000  232.722    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               19745905  230.283    0.000  230.283    0.000 {built-in method zeros}
                2090861   34.865    0.000  218.170    0.000 optimizer.py:189(zero_grad)
                 127509    9.089    0.000  212.800    0.002 layers.py:17(step)
             2561249489  209.868    0.000  209.868    0.000 {method 'values' of 'collections.OrderedDict' objects}
                 127510   17.199    0.000  204.995    0.002 layers.py:793(update)
                2412107  204.319    0.000  204.319    0.000 {built-in method tensor}
               12750900   19.090    0.000  202.652    0.000 layer.py:106(move)
               69736719  200.776    0.000  200.776    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              399589544  195.982    0.000  195.982    0.000 module.py:934(__getattr__)
                1844242    1.775    0.000  184.613    0.000 game.py:38(board)
               56985819   34.003    0.000  181.989    0.000 flatten.py:39(forward)
               12750900  168.992    0.000  168.992    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                 127509  153.037    0.001  153.037    0.001 allGraphsTrain.py:51(<listcomp>)
               12800184  144.637    0.000  144.637    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                1206696    9.557    0.000  131.102    0.000 allGraphs.py:167(format)
               12800184  122.273    0.000  122.273    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               12800184  122.230    0.000  122.230    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               12800184  121.450    0.000  121.450    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               54767449  114.672    0.000  114.672    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                 127509   73.187    0.001  109.882    0.001 agent.py:67(modify)
                2090861    2.658    0.000  102.575    0.000 loss.py:527(forward)
                 255018    0.755    0.000  100.949    0.000 network.py:28(forward)
                2090861    7.361    0.000   99.917    0.000 functional.py:2898(mse_loss)
               12750900   25.671    0.000   99.679    0.000 layers.py:844(check)
              171518210   65.819    0.000   96.563    0.000 _VF.py:25(__getattr__)
               12800184   94.068    0.000   94.068    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               88371873   58.638    0.000   78.277    0.000 types.py:171(__get__)
               89601348   59.664    0.000   74.184    0.000 tensor.py:906(grad)
                2090861   70.695    0.000   70.695    0.000 {built-in method torch._C._nn.mse_loss}
               12750900   16.581    0.000   66.147    0.000 layers.py:838(isFree)
                 139082    1.294    0.000   65.577    0.000 layers.py:849(restart)
                 127509    1.967    0.000   62.247    0.000 agent.py:112(__call__)
                 139082    0.672    0.000   54.962    0.000 level.py:8(__init__)
                2578410   54.767    0.000   54.767    0.000 {built-in method cat}
              445387582   54.043    0.000   54.043    0.000 {built-in method torch._C._has_torch_function_unary}
               84176715   39.714    0.000   49.566    0.000 layer.py:103(isFree)
                 892570   27.271    0.000   49.103    0.000 layer.py:175(NoRock_update)
              175283750   32.779    0.000   48.548    0.000 enum.py:646(__hash__)
               56730801   32.967    0.000   47.448    0.000 container.py:109(__iter__)
               11289666   45.878    0.000   45.878    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                4181722    8.843    0.000   43.203    0.000 profiler.py:615(__enter__)
                2090861    8.011    0.000   41.427    0.000 __init__.py:28(_make_grads)
              224344794   40.505    0.000   40.505    0.000 {built-in method torch._C._has_torch_function_variadic}
               12611919    9.625    0.000   39.864    0.000 {built-in method builtins.any}
                 139082    1.625    0.000   39.838    0.000 levels.py:456(generate)
                 510036    1.181    0.000   39.777    0.000 conv.py:398(forward)
                 510036    0.909    0.000   38.097    0.000 conv.py:390(_conv_forward)
                 510036   37.188    0.000   37.188    0.000 {built-in method conv2d}
                 667115    6.446    0.000   36.490    0.000 level.py:41(notUsed)
                 382527    0.862    0.000   35.095    0.000 tensor.py:575(__iter__)
                4181722   34.359    0.000   34.359    0.000 {built-in method torch._ops.profiler._record_function_enter}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9651534: <Diamonds4_0.5_NN_2> in cluster <dcc> Done

Job <Diamonds4_0.5_NN_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Tue May 18 21:04:59 2021
Job was executed on host(s) <n-62-20-3>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed May 19 17:05:35 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 19 17:05:35 2021
Terminated at Thu May 20 03:00:49 2021
Results reported at Thu May 20 03:00:49 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=16G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 1440
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $MYARGS


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   35616.61 sec.
    Max Memory :                                 3595 MB
    Average Memory :                             3087.17 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               12789.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35796 sec.
    Turnaround time :                            107750 sec.

The output (if any) is above this job summary.

