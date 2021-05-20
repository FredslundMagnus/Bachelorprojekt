/zhome/ee/d/137643/Desktop/Bachelor/project-env/lib/python3.8/site-packages/torch/cuda/__init__.py:52: UserWarning: CUDA initialization: Found no NVIDIA driver on your system. Please check that you have an NVIDIA GPU and installed a driver from http://www.nvidia.com/Download/index.aspx (Triggered internally at  /pytorch/c10/cuda/CUDAFunctions.cpp:100.)
  return torch._C._cuda_getDeviceCount() > 0

# Parameters

    Name :                      Diamonds3_0.0_NN_cpu_2-1
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
    Num :                       1
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      12711311899 function calls (12482003522 primitive calls) in 35700.24 seconds

##    Ordered by: cumulative time
   List reduced from 441 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35700.238 35700.238 {built-in method builtins.exec}
                      1    0.001    0.001 35700.238 35700.238 <string>:1(<module>)
                      1   73.650   73.650 35700.237 35700.237 allGraphsTrain.py:13(graphTrain)
        241222138/26323528 1404.002    0.000 13426.494    0.001 module.py:715(_call_impl)
               21489861  425.595    0.000 12861.538    0.001 container.py:115(forward)
                 251647   59.062    0.000 11529.067    0.046 allGraphsTrain.py:40(<listcomp>)
                3297427   14.908    0.000 11437.166    0.003 allGraphs.py:179(getInterventionsmodel)
               20986567   76.227    0.000 10047.398    0.000 BayesianNN.py:18(forward)
        17082281/3171724  996.174    0.000 9581.890    0.003 allGraphs.py:186(recursiveBEST)
               16404547  226.674    0.000 9407.194    0.001 BayesianNN.py:61(predict)
                 251647 2001.293    0.008 9211.362    0.037 allGraphs.py:156(transformNot)
                4582020   56.478    0.000 8903.267    0.002 BayesianNN.py:57(learn)
                4582020   76.417    0.000 8476.991    0.002 BayesianNN.py:21(learn)
                 251647    1.848    0.000 4731.740    0.019 agent.py:29(learn)
                 251647   42.808    0.000 4729.201    0.019 agent.py:117(_learn)
                 251647   22.811    0.000 4686.393    0.019 learner.py:42(Qlearn)
                4833667   35.865    0.000 3917.268    0.001 tensor.py:181(backward)
                4833667   22.050    0.000 3881.403    0.001 __init__.py:68(backward)
                4833667   34.908    0.000 3815.393    0.001 grad_mode.py:23(decorate_context)
                4833667 3762.413    0.001 3762.413    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                4833667  163.034    0.000 3714.191    0.001 adam.py:55(step)
               63966289  210.579    0.000 3434.553    0.000 linear.py:92(forward)
               62959701   90.748    0.000 3407.331    0.000 dropout.py:57(forward)
               62959701  322.908    0.000 3316.582    0.000 functional.py:960(dropout)
               63966289  357.505    0.000 3139.837    0.000 functional.py:1669(linear)
                 503294    2.336    0.000 3111.351    0.006 network.py:28(forward)
                 251647   17.081    0.000 3009.443    0.012 allGraphs.py:141(transform)
               62959701 2919.760    0.000 2919.760    0.000 {built-in method dropout}
                4833667  745.222    0.000 2902.155    0.001 functional.py:53(adam)
                1006588    3.971    0.000 2720.173    0.003 conv.py:422(forward)
                1006588    4.353    0.000 2714.794    0.003 conv.py:414(_conv_forward)
                1006588 2709.886    0.003 2709.886    0.003 {built-in method conv2d}
                 251647   40.648    0.000 2168.304    0.009 allGraphsTrain.py:33(<listcomp>)
               25416448 1039.442    0.000 2127.664    0.000 allGraphs.py:114(states)
                 251647    1.840    0.000 2070.295    0.008 game.py:42(step)
                 251647    2.536    0.000 2034.722    0.008 layers.py:827(step)
              276812200 1709.813    0.000 1709.813    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
               20986567 1214.026    0.000 1693.757    0.000 BayesianNN.py:43(convert_data)
               63966289 1648.573    0.000 1648.573    0.000 {built-in method addmm}
          624501/125703   50.553    0.000 1603.155    0.013 allGraphs.py:202(recursiveExplore)
                 251647    5.440    0.000 1555.353    0.006 agent.py:112(__call__)
              206537132  700.202    0.000 1158.488    0.000 tensor.py:933(grad)
               64469583   79.404    0.000 1093.999    0.000 activation.py:713(forward)
                 251647   34.015    0.000 1074.733    0.004 layers.py:17(step)
               25164700   64.786    0.000 1037.597    0.000 layer.py:106(move)
               64469583  119.862    0.000 1014.595    0.000 functional.py:1292(leaky_relu)
                 251648   55.325    0.000  953.764    0.004 layers.py:793(update)
               64469583  882.094    0.000  882.094    0.000 {built-in method torch._C._nn.leaky_relu}
                4833667  104.477    0.000  869.638    0.000 optimizer.py:167(zero_grad)
              329980836  260.596    0.000  827.189    0.000 overrides.py:1070(has_torch_function)
               41083937  179.298    0.000  750.709    0.000 tensor.py:21(wrapped)
               63966289  743.201    0.000  743.201    0.000 {method 't' of 'torch._C._TensorBase' objects}
               59010592  697.482    0.000  697.482    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              428267929  259.204    0.000  693.592    0.000 {built-in method builtins.any}
               25164700  130.627    0.000  652.970    0.000 layers.py:844(check)
              306560928  641.808    0.000  641.808    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               59010592  448.283    0.000  448.283    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                 251647   30.606    0.000  422.139    0.002 allGraphsTrain.py:51(<listcomp>)
                 511330    8.034    0.000  384.182    0.001 layers.py:849(restart)
                 251647   51.262    0.000  376.139    0.001 allGraphsTrain.py:44(<listcomp>)
               41973135  370.213    0.000  370.213    0.000 {built-in method zeros}
               14661002   75.147    0.000  359.799    0.000 tensor.py:506(__rsub__)
                4833667   10.377    0.000  329.259    0.000 loss.py:445(forward)
              753899970  265.309    0.000  322.905    0.000 overrides.py:1083(<genexpr>)
                 511330    3.945    0.000  319.900    0.001 level.py:8(__init__)
                4833667   35.608    0.000  318.882    0.000 functional.py:2637(mse_loss)
                5644827  312.317    0.000  312.317    0.000 {built-in method tensor}
               29505296  301.224    0.000  301.224    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                 511330   11.017    0.000  285.054    0.001 levels.py:303(generate)
               14661002  284.651    0.000  284.651    0.000 {built-in method rsub}
                4555663    7.138    0.000  284.109    0.000 game.py:38(board)
               29505296  269.137    0.000  269.137    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              241977079  268.598    0.000  268.598    0.000 {built-in method torch._C._get_tracing_state}
                3067812   44.315    0.000  262.734    0.000 level.py:41(notUsed)
               25164700   64.467    0.000  261.460    0.000 layers.py:838(isFree)
              669005050  173.672    0.000  247.788    0.000 enum.py:646(__hash__)
               26422935  239.699    0.000  239.699    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                3297427   39.902    0.000  235.610    0.000 allGraphs.py:167(format)
               29505296  233.612    0.000  233.612    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                 251647   87.138    0.000  223.831    0.001 agent.py:67(modify)
               66248737   46.773    0.000  216.361    0.000 {built-in method builtins.all}
                2013184  116.524    0.000  204.774    0.000 layer.py:175(NoRock_update)
              196747930  157.824    0.000  196.993    0.000 layer.py:103(isFree)
               29505296  196.009    0.000  196.009    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                4833667  191.653    0.000  191.653    0.000 {built-in method torch._C._nn.mse_loss}
               27321124  187.453    0.000  187.453    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               25164700  172.549    0.000  172.549    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               14409355  171.456    0.000  171.456    0.000 {method 'gt' of 'torch._C._TensorBase' objects}
               47157855  171.329    0.000  171.329    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               25164700  103.186    0.000  161.822    0.000 layers.py:424(check)
                 754941    4.852    0.000  160.076    0.000 tensor.py:576(__iter__)
                 754941  152.602    0.000  152.602    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
              115078536   47.242    0.000  142.783    0.000 layers.py:799(<genexpr>)
        862235691/862235689  134.519    0.000  141.584    0.000 {built-in method builtins.len}
              986378413  134.450    0.000  134.450    0.000 {method 'values' of 'collections.OrderedDict' objects}
              156018470  132.418    0.000  132.419    0.000 module.py:765(__getattr__)
                3067812    3.492    0.000  128.109    0.000 level.py:38(elementsIn)
               29505406   52.205    0.000  116.368    0.000 tensor.py:596(__hash__)
              221881230   89.415    0.000  107.010    0.000 layers.py:809(<genexpr>)
               25164700   65.743    0.000  101.865    0.000 layers.py:452(check)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9668408: <Diamonds3_0.0_NN_cpu_2_1> in cluster <dcc> Done

Job <Diamonds3_0.0_NN_cpu_2_1> was submitted from host <n-62-30-8> by user <s183905> in cluster <dcc> at Wed May 19 22:59:02 2021
Job was executed on host(s) <n-62-21-108>, in queue <hpc>, as user <s183905> in cluster <dcc> at Wed May 19 22:59:03 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 19 22:59:03 2021
Terminated at Thu May 20 08:54:06 2021
Results reported at Thu May 20 08:54:06 2021

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

    CPU time :                                   35696.76 sec.
    Max Memory :                                 106 MB
    Average Memory :                             100.13 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               16278.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   35703 sec.
    Turnaround time :                            35704 sec.

The output (if any) is above this job summary.

