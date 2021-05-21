
# Parameters

    Name :                      Diamonds3_0.5_NN-2
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
    Num :                       2
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      12749837509 function calls (12103483631 primitive calls) in 35722.92 seconds

##    Ordered by: cumulative time
   List reduced from 484 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35722.924 35722.924 {built-in method builtins.exec}
                      1    0.001    0.001 35722.924 35722.924 <string>:1(<module>)
                      1   31.334   31.334 35722.923 35722.923 allGraphsTrain.py:13(graphTrain)
                 107897  124.813    0.001 27133.548    0.251 allGraphsTrain.py:40(<listcomp>)
                 672240    3.249    0.000 27003.839    0.040 allGraphs.py:179(getInterventionsmodel)
        54539230/497965 4685.101    0.000 25086.156    0.050 allGraphs.py:186(recursiveBEST)
               52030150 2131.290    0.000 18451.186    0.000 BayesianNN.py:65(predict_no_convert)
               58945874  154.155    0.000 18363.881    0.000 BayesianNN.py:18(forward)
        652313264/60696584 2212.902    0.000 18305.873    0.000 module.py:866(_call_impl)
               59161668  782.812    0.000 17873.113    0.000 container.py:117(forward)
              177269210  292.024    0.000 7121.936    0.000 linear.py:93(forward)
              177269210  128.904    0.000 6706.164    0.000 functional.py:1737(linear)
              177269210 6545.266    0.000 6545.266    0.000 {built-in method torch._C._nn.linear}
                 107897 1234.591    0.011 4943.938    0.046 allGraphs.py:156(transformNot)
              176837622  128.403    0.000 4102.157    0.000 dropout.py:57(forward)
              176837622  430.989    0.000 3973.754    0.000 functional.py:1059(dropout)
              176837622 3420.468    0.000 3420.468    0.000 {built-in method dropout}
              177485004  104.296    0.000 2855.404    0.000 activation.py:713(forward)
              177485004  121.714    0.000 2751.107    0.000 functional.py:1364(leaky_relu)
                5488705   72.340    0.000 2620.031    0.000 BayesianNN.py:61(predict)
              177485004 2606.828    0.000 2606.828    0.000 {built-in method torch._C._nn.leaky_relu}
                1427019   18.755    0.000 2542.838    0.002 BayesianNN.py:57(learn)
                1427019   16.627    0.000 2335.950    0.002 BayesianNN.py:21(learn)
          869793/174275   89.054    0.000 1835.217    0.011 allGraphs.py:202(recursiveExplore)
                 107897    6.896    0.000 1748.879    0.016 allGraphsTrain.py:33(<listcomp>)
               10897698  431.709    0.000 1742.108    0.000 allGraphs.py:114(states)
              130904775 1635.190    0.000 1635.190    0.000 {method 'item' of 'torch._C._TensorBase' objects}
              118687200 1414.056    0.000 1414.056    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                1534916   11.985    0.000 1094.181    0.001 optimizer.py:84(wrapper)
                1534916    5.901    0.000 1036.245    0.001 grad_mode.py:24(decorate_context)
                1534916   30.854    0.000 1017.000    0.001 adam.py:55(step)
                6915724  766.751    0.000  975.500    0.000 BayesianNN.py:43(convert_data)
               54844680   55.129    0.000  965.745    0.000 tensor.py:525(__rsub__)
                1534916  205.669    0.000  953.623    0.001 _functional.py:53(adam)
               54844680  898.923    0.000  898.923    0.000 {built-in method rsub}
                1534916    5.452    0.000  621.279    0.000 tensor.py:195(backward)
                1534916    5.622    0.000  615.612    0.000 __init__.py:68(backward)
                1534916  577.991    0.000  577.991    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                 107897    3.170    0.000  440.312    0.004 allGraphs.py:141(transform)
                 107897    0.436    0.000  421.528    0.004 game.py:42(step)
              652636955  403.549    0.000  403.549    0.000 {built-in method torch._C._get_tracing_state}
                 107897    0.635    0.000  397.608    0.004 layers.py:827(step)
                 107897   28.008    0.000  348.768    0.003 allGraphsTrain.py:44(<listcomp>)
        2900547728/2900547726  293.692    0.000  294.733    0.000 {built-in method builtins.len}
                 107897    0.422    0.000  246.489    0.002 agent.py:29(learn)
                 107897    2.672    0.000  245.821    0.002 agent.py:117(_learn)
                 107897    7.935    0.000  243.149    0.002 learner.py:42(Qlearn)
             2668414724  218.119    0.000  218.119    0.000 {method 'values' of 'collections.OrderedDict' objects}
               59377462   50.640    0.000  201.840    0.000 flatten.py:39(forward)
                 107897    7.895    0.000  201.158    0.002 layers.py:17(step)
              415990788  201.002    0.000  201.002    0.000 module.py:934(__getattr__)
               16901281  199.575    0.000  199.575    0.000 {built-in method zeros}
               18850580  195.255    0.000  195.255    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                 107898   14.558    0.000  195.173    0.002 layers.py:793(update)
               70167162  195.171    0.000  195.171    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               10789700   16.579    0.000  192.330    0.000 layer.py:106(move)
               18850580  172.858    0.000  172.858    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                1534916   25.839    0.000  160.473    0.000 optimizer.py:189(zero_grad)
                1697140  151.292    0.000  151.292    0.000 {built-in method tensor}
               10789700  142.997    0.000  142.997    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                1211726    1.101    0.000  131.983    0.000 game.py:38(board)
                 107897  128.983    0.001  128.983    0.001 allGraphsTrain.py:51(<listcomp>)
               57734649  122.506    0.000  122.506    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                9425290  106.121    0.000  106.121    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               10789700   24.521    0.000  101.607    0.000 layers.py:844(check)
              178372538   66.894    0.000   98.125    0.000 _VF.py:25(__getattr__)
                 107897   61.577    0.001   92.848    0.001 agent.py:67(modify)
                9425290   90.642    0.000   90.642    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                9425290   90.240    0.000   90.240    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                9425290   89.883    0.000   89.883    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                 215794    0.637    0.000   85.151    0.000 network.py:28(forward)
                 672240    5.384    0.000   78.957    0.000 allGraphs.py:167(format)
               86142533   58.579    0.000   77.297    0.000 types.py:171(__get__)
                1534916    1.960    0.000   74.576    0.000 loss.py:527(forward)
                1534916    5.421    0.000   72.616    0.000 functional.py:2898(mse_loss)
                9425290   69.344    0.000   69.344    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                2997866   62.543    0.000   62.543    0.000 {built-in method cat}
               10789700   15.722    0.000   59.049    0.000 layers.py:838(isFree)
                  97203    1.082    0.000   57.180    0.001 layers.py:849(restart)
               65977090   43.653    0.000   54.205    0.000 tensor.py:906(grad)
              432339207   53.692    0.000   53.692    0.000 {built-in method torch._C._has_torch_function_unary}
                 107897    1.701    0.000   53.236    0.000 agent.py:112(__call__)
                1534916   51.345    0.000   51.345    0.000 {built-in method torch._C._nn.mse_loss}
                  97203    0.529    0.000   49.209    0.001 level.py:8(__init__)
               59161668   34.770    0.000   48.990    0.000 container.py:109(__iter__)
                 863184   25.147    0.000   45.750    0.000 layer.py:175(NoRock_update)
              233648806   43.976    0.000   43.976    0.000 {built-in method torch._C._has_torch_function_variadic}
              163330669   29.723    0.000   43.340    0.000 enum.py:646(__hash__)
               75551632   34.672    0.000   43.327    0.000 layer.py:103(isFree)
               10057470   40.306    0.000   40.306    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               10692598    9.120    0.000   39.155    0.000 {built-in method builtins.any}
                  97203    1.343    0.000   34.453    0.000 levels.py:303(generate)
                 431588    1.006    0.000   33.989    0.000 conv.py:398(forward)
               10789800    3.850    0.000   33.863    0.000 {built-in method builtins.all}
                 431588    0.688    0.000   32.568    0.000 conv.py:390(_conv_forward)
                 431588   31.880    0.000   31.880    0.000 {built-in method conv2d}
                 583295    5.493    0.000   31.665    0.000 level.py:41(notUsed)
               43966545   11.434    0.000   31.297    0.000 layers.py:799(<genexpr>)
              178480856   31.296    0.000   31.296    0.000 {built-in method builtins.getattr}
                3069832    6.905    0.000   31.252    0.000 profiler.py:615(__enter__)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9651531: <Diamonds3_0.5_NN_2> in cluster <dcc> Done

Job <Diamonds3_0.5_NN_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Tue May 18 21:04:58 2021
Job was executed on host(s) <n-62-20-5>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed May 19 16:57:34 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 19 16:57:34 2021
Terminated at Thu May 20 02:53:20 2021
Results reported at Thu May 20 02:53:20 2021

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

    CPU time :                                   35618.47 sec.
    Max Memory :                                 3254 MB
    Average Memory :                             2910.95 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13130.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35746 sec.
    Turnaround time :                            107302 sec.

The output (if any) is above this job summary.

