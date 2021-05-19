
# Parameters

    Name :                      Diamonds1_0.5_NN-1
    Main :                      graphTrain
    Level :                     Levels.Causal2
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
    Num :                       1
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      14901993273 function calls (14146645815 primitive calls) in 35720.09 seconds

##    Ordered by: cumulative time
   List reduced from 483 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35720.089 35720.089 {built-in method builtins.exec}
                      1    0.001    0.001 35720.089 35720.089 <string>:1(<module>)
                      1   36.387   36.387 35720.088 35720.088 allGraphsTrain.py:13(graphTrain)
                 133754  135.218    0.001 27504.208    0.206 allGraphsTrain.py:40(<listcomp>)
                1224479    5.980    0.000 27360.142    0.022 allGraphs.py:179(getInterventionsmodel)
        65250950/1051016 4474.015    0.000 26049.961    0.025 allGraphs.py:186(recursiveBEST)
               60852174 2176.410    0.000 19213.586    0.000 BayesianNN.py:65(predict_no_convert)
               68794779  178.649    0.000 19168.326    0.000 BayesianNN.py:18(forward)
        761792561/71169691 2689.436    0.000 19105.227    0.000 module.py:866(_call_impl)
               69062287  854.988    0.000 18573.653    0.000 container.py:117(forward)
              206919353  365.046    0.000 7289.766    0.000 linear.py:93(forward)
              206919353  159.608    0.000 6764.855    0.000 functional.py:1737(linear)
              206919353 6571.478    0.000 6571.478    0.000 {built-in method torch._C._nn.linear}
                 133754  933.494    0.007 4598.466    0.034 allGraphs.py:156(transformNot)
              206384337  158.337    0.000 4234.762    0.000 dropout.py:57(forward)
              206384337  534.968    0.000 4076.425    0.000 functional.py:1059(dropout)
              206384337 3384.446    0.000 3384.446    0.000 {built-in method dropout}
                1973650   25.563    0.000 2868.750    0.001 BayesianNN.py:57(learn)
              207186861  136.350    0.000 2692.884    0.000 activation.py:713(forward)
                1973650   21.845    0.000 2643.399    0.001 BayesianNN.py:21(learn)
              207186861  150.678    0.000 2556.534    0.000 functional.py:1364(leaky_relu)
                5968955   80.191    0.000 2438.769    0.000 BayesianNN.py:61(predict)
              207186861 2379.327    0.000 2379.327    0.000 {built-in method torch._C._nn.leaky_relu}
              135729114 1576.149    0.000 1576.149    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                 133754    8.195    0.000 1419.779    0.011 allGraphsTrain.py:33(<listcomp>)
               13509255  310.037    0.000 1411.595    0.000 allGraphs.py:114(states)
          697702/173463   57.336    0.000 1174.606    0.007 allGraphs.py:202(recursiveExplore)
                2107404   15.658    0.000 1132.794    0.001 optimizer.py:84(wrapper)
              120379000 1067.651    0.000 1067.651    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                2107404    8.082    0.000 1059.457    0.001 grad_mode.py:24(decorate_context)
                2107404   45.624    0.000 1032.326    0.000 adam.py:55(step)
               64857927   62.774    0.000  966.871    0.000 tensor.py:525(__rsub__)
                2107404  211.360    0.000  936.636    0.000 _functional.py:53(adam)
               64857927  894.146    0.000  894.146    0.000 {built-in method rsub}
                7942605  632.789    0.000  827.475    0.000 BayesianNN.py:43(convert_data)
                2107404    7.166    0.000  699.344    0.000 tensor.py:195(backward)
                2107404    7.560    0.000  691.894    0.000 __init__.py:68(backward)
                2107404  644.449    0.000  644.449    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                 133754    4.726    0.000  597.454    0.004 allGraphs.py:141(transform)
                 133754    0.492    0.000  531.222    0.004 game.py:42(step)
                 133754    0.813    0.000  504.434    0.004 layers.py:827(step)
              762193823  375.026    0.000  375.026    0.000 {built-in method torch._C._get_tracing_state}
                 133754   25.905    0.000  348.711    0.003 allGraphsTrain.py:44(<listcomp>)
        3384483861/3384483859  330.727    0.000  332.037    0.000 {built-in method builtins.len}
             3116232531  271.050    0.000  271.050    0.000 {method 'values' of 'collections.OrderedDict' objects}
                 133754    0.556    0.000  253.691    0.002 agent.py:29(learn)
              485945246  253.251    0.000  253.251    0.000 module.py:934(__getattr__)
                 133754   10.955    0.000  253.028    0.002 layers.py:17(step)
                 133754    3.466    0.000  252.796    0.002 agent.py:117(_learn)
                 133755   20.052    0.000  249.625    0.002 layers.py:793(update)
                 133754    8.335    0.000  249.331    0.002 learner.py:42(Qlearn)
               13375400   22.136    0.000  240.787    0.000 layer.py:106(move)
                2487240  202.848    0.000  202.848    0.000 {built-in method tensor}
               69329795   44.789    0.000  198.718    0.000 flatten.py:39(forward)
               82705195  191.515    0.000  191.515    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               20100019  186.279    0.000  186.279    0.000 {built-in method zeros}
                1893250    1.699    0.000  182.998    0.000 game.py:38(board)
               25823864  182.464    0.000  182.464    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                2107404   32.982    0.000  181.081    0.000 optimizer.py:189(zero_grad)
               25823864  164.404    0.000  164.404    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               13375400  134.906    0.000  134.906    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                1224479    9.438    0.000  129.084    0.000 allGraphs.py:167(format)
              208491741   87.147    0.000  128.869    0.000 _VF.py:25(__getattr__)
               13375400   31.303    0.000  118.887    0.000 layers.py:844(check)
               67088637  117.385    0.000  117.385    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                 133754  111.954    0.001  111.954    0.001 allGraphsTrain.py:51(<listcomp>)
               12911932  107.273    0.000  107.273    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                 133754   67.462    0.001  102.157    0.001 agent.py:67(modify)
               98177789   76.512    0.000   98.482    0.000 types.py:171(__get__)
                 267508    0.830    0.000   96.648    0.000 network.py:28(forward)
                2107404    2.909    0.000   94.085    0.000 loss.py:527(forward)
                2107404    8.029    0.000   91.177    0.000 functional.py:2898(mse_loss)
               12911932   90.628    0.000   90.628    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               12911932   88.640    0.000   88.640    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                 166784    1.873    0.000   88.490    0.001 layers.py:849(restart)
               12911932   88.417    0.000   88.417    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               69062287   60.644    0.000   80.470    0.000 container.py:109(__iter__)
               90383584   63.566    0.000   79.212    0.000 tensor.py:906(grad)
               13375400   19.525    0.000   79.017    0.000 layers.py:838(isFree)
                 166784    0.872    0.000   73.598    0.000 level.py:8(__init__)
               12911932   67.194    0.000   67.194    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              520312021   64.740    0.000   64.740    0.000 {built-in method torch._C._has_torch_function_unary}
                2107404   61.844    0.000   61.844    0.000 {built-in method torch._C._nn.mse_loss}
                 133754    2.137    0.000   60.521    0.000 agent.py:112(__call__)
               86246932   48.459    0.000   59.492    0.000 layer.py:103(isFree)
                 936285   32.843    0.000   58.982    0.000 layer.py:175(NoRock_update)
              177114897   37.006    0.000   54.209    0.000 enum.py:646(__hash__)
                 166784    2.189    0.000   53.689    0.000 levels.py:151(generate)
                 800659    8.607    0.000   49.213    0.000 level.py:41(notUsed)
               13208717   11.247    0.000   46.509    0.000 {built-in method builtins.any}
                2364464   44.237    0.000   44.237    0.000 {built-in method cat}
              273884684   44.104    0.000   44.104    0.000 {built-in method torch._C._has_torch_function_variadic}
              208610338   41.793    0.000   41.793    0.000 {built-in method builtins.getattr}
                 401262    0.985    0.000   41.334    0.000 tensor.py:575(__iter__)
                 401262   39.482    0.000   39.482    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
                 535016    1.324    0.000   38.608    0.000 conv.py:398(forward)
                2107404    8.064    0.000   37.739    0.000 __init__.py:28(_make_grads)
                 535016    0.889    0.000   36.689    0.000 conv.py:390(_conv_forward)
                4214808    7.953    0.000   36.445    0.000 profiler.py:615(__enter__)
               11365995   36.228    0.000   36.228    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9651523: <Diamonds1_0.5_NN_1> in cluster <dcc> Done

Job <Diamonds1_0.5_NN_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Tue May 18 21:04:57 2021
Job was executed on host(s) <n-62-20-16>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Tue May 18 21:04:59 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue May 18 21:04:59 2021
Terminated at Wed May 19 07:00:27 2021
Results reported at Wed May 19 07:00:27 2021

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

    CPU time :                                   35615.51 sec.
    Max Memory :                                 3604 MB
    Average Memory :                             3105.87 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               12780.00 MB
    Max Swap :                                   2 MB
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35835 sec.
    Turnaround time :                            35730 sec.

The output (if any) is above this job summary.

