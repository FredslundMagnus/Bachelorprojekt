
# Parameters

    Name :                      Diamonds2_0.5_NN-2
    Main :                      graphTrain
    Level :                     Levels.Causal5
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


      16397079204 function calls (15548318781 primitive calls) in 35723.06 seconds

##    Ordered by: cumulative time
   List reduced from 485 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35723.058 35723.058 {built-in method builtins.exec}
                      1    0.001    0.001 35723.058 35723.058 <string>:1(<module>)
                      1   31.905   31.905 35723.057 35723.057 allGraphsTrain.py:13(graphTrain)
                 119084  111.076    0.001 27977.043    0.235 allGraphsTrain.py:40(<listcomp>)
                 763384    3.498    0.000 27860.051    0.036 allGraphs.py:179(getInterventionsmodel)
        73394814/611303 4635.355    0.000 26481.944    0.043 allGraphs.py:186(recursiveBEST)
               70348092 2273.235    0.000 19888.479    0.000 BayesianNN.py:65(predict_no_convert)
               77299752  171.933    0.000 19223.806    0.000 BayesianNN.py:18(forward)
        854565960/79186760 2672.266    0.000 19125.590    0.000 module.py:866(_call_impl)
               77537920  846.483    0.000 18621.224    0.000 container.py:117(forward)
              232375592  359.939    0.000 7339.215    0.000 linear.py:93(forward)
              232375592  155.798    0.000 6822.902    0.000 functional.py:1737(linear)
              232375592 6629.012    0.000 6629.012    0.000 {built-in method torch._C._nn.linear}
                 119084 1027.666    0.009 4285.345    0.036 allGraphs.py:156(transformNot)
              231899256  152.828    0.000 4273.821    0.000 dropout.py:57(forward)
              231899256  570.359    0.000 4120.993    0.000 functional.py:1059(dropout)
              231899256 3389.567    0.000 3389.567    0.000 {built-in method dropout}
              232613760  132.696    0.000 2699.873    0.000 activation.py:713(forward)
              232613760  148.886    0.000 2567.177    0.000 functional.py:1364(leaky_relu)
              232613760 2391.041    0.000 2391.041    0.000 {built-in method torch._C._nn.leaky_relu}
                5421904   66.051    0.000 2121.947    0.000 BayesianNN.py:61(predict)
                1529756   18.637    0.000 2073.574    0.001 BayesianNN.py:57(learn)
                1529756   15.720    0.000 1869.668    0.001 BayesianNN.py:21(learn)
              168248908 1786.131    0.000 1786.131    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                 119084    8.837    0.000 1707.275    0.014 allGraphsTrain.py:33(<listcomp>)
               12027585  356.053    0.000 1698.490    0.000 allGraphs.py:114(states)
          749378/152081   59.085    0.000 1281.403    0.008 allGraphs.py:202(recursiveExplore)
              154809800 1237.237    0.000 1237.237    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
               73499892   59.967    0.000  978.210    0.000 tensor.py:525(__rsub__)
               73499892  906.646    0.000  906.646    0.000 {built-in method rsub}
                6951660  678.555    0.000  839.522    0.000 BayesianNN.py:43(convert_data)
                1648840   11.962    0.000  809.213    0.000 optimizer.py:84(wrapper)
                1648840    5.750    0.000  754.926    0.000 grad_mode.py:24(decorate_context)
                1648840   32.368    0.000  734.976    0.000 adam.py:55(step)
                1648840  151.254    0.000  667.957    0.000 _functional.py:53(adam)
                1648840    5.334    0.000  504.278    0.000 tensor.py:195(backward)
                1648840    5.981    0.000  498.742    0.000 __init__.py:68(backward)
                 119084    0.424    0.000  469.564    0.004 game.py:42(step)
                1648840  464.441    0.000  464.441    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                 119084    0.632    0.000  444.770    0.004 layers.py:827(step)
                 119084    3.669    0.000  382.638    0.003 allGraphs.py:141(transform)
              854923212  377.845    0.000  377.845    0.000 {built-in method torch._C._get_tracing_state}
        3787962541/3787962539  330.002    0.000  331.047    0.000 {built-in method builtins.len}
                 119084   19.528    0.000  280.877    0.002 allGraphsTrain.py:44(<listcomp>)
             3495801760  269.697    0.000  269.697    0.000 {method 'values' of 'collections.OrderedDict' objects}
                 119084    8.845    0.000  247.405    0.002 layers.py:17(step)
              544772059  246.608    0.000  246.608    0.000 module.py:934(__getattr__)
               11908400   18.208    0.000  237.527    0.000 layer.py:106(move)
                 119084    0.459    0.000  206.770    0.002 agent.py:29(learn)
                 119084    2.878    0.000  206.042    0.002 agent.py:117(_learn)
                 119084    6.905    0.000  203.164    0.002 learner.py:42(Qlearn)
                1890958  197.189    0.000  197.189    0.000 {built-in method tensor}
                 119085   15.884    0.000  196.017    0.002 layers.py:793(update)
               77776088   43.873    0.000  194.164    0.000 flatten.py:39(forward)
               89684488  179.162    0.000  179.162    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                1358805    1.212    0.000  154.000    0.000 game.py:38(board)
               17201001  146.030    0.000  146.030    0.000 {built-in method zeros}
              233548096   92.789    0.000  131.419    0.000 _VF.py:25(__getattr__)
               20262416  128.944    0.000  128.944    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               11908400   31.930    0.000  127.834    0.000 layers.py:844(check)
                1648840   22.709    0.000  126.252    0.000 optimizer.py:189(zero_grad)
               76008164  125.173    0.000  125.173    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               20262416  116.163    0.000  116.163    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               11908400  108.922    0.000  108.922    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
              116474528   81.116    0.000  104.511    0.000 types.py:171(__get__)
                 763384    5.696    0.000   92.911    0.000 allGraphs.py:167(format)
                 119084   87.735    0.001   87.735    0.001 allGraphsTrain.py:51(<listcomp>)
                 119084   52.884    0.000   81.497    0.001 agent.py:67(modify)
                 238168    0.680    0.000   78.895    0.000 network.py:28(forward)
               10131208   77.913    0.000   77.913    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               11908400   19.975    0.000   74.998    0.000 layers.py:838(isFree)
                1648840    2.088    0.000   72.280    0.000 loss.py:527(forward)
                1648840    5.595    0.000   70.192    0.000 functional.py:2898(mse_loss)
               10131208   64.876    0.000   64.876    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              548402751   64.140    0.000   64.140    0.000 {built-in method torch._C._has_torch_function_unary}
               77537920   44.346    0.000   63.790    0.000 container.py:109(__iter__)
               10131208   63.229    0.000   63.229    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               10131208   62.720    0.000   62.720    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                1071765   29.849    0.000   55.139    0.000 layer.py:175(NoRock_update)
              103049338   43.754    0.000   55.023    0.000 layer.py:103(isFree)
               70918516   43.477    0.000   54.541    0.000 tensor.py:906(grad)
              307524324   49.994    0.000   49.994    0.000 {built-in method torch._C._has_torch_function_variadic}
                 119084    1.684    0.000   49.982    0.000 agent.py:112(__call__)
              186348931   34.034    0.000   49.111    0.000 enum.py:646(__hash__)
                1648840   48.825    0.000   48.825    0.000 {built-in method torch._C._nn.mse_loss}
               10131208   47.423    0.000   47.423    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                  91067    1.007    0.000   47.342    0.001 layers.py:849(restart)
               11817434   10.779    0.000   46.324    0.000 {built-in method builtins.any}
                2627356   45.367    0.000   45.367    0.000 {built-in method cat}
                  91067    0.525    0.000   39.764    0.000 level.py:8(__init__)
              233660477   38.692    0.000   38.692    0.000 {built-in method builtins.getattr}
              118174330   29.083    0.000   35.544    0.000 layers.py:809(<genexpr>)
                  91067    1.372    0.000   35.116    0.000 levels.py:249(generate)
                 591628    5.568    0.000   32.265    0.000 level.py:41(notUsed)
                 476336    1.052    0.000   31.765    0.000 conv.py:398(forward)
                 476336    0.665    0.000   30.235    0.000 conv.py:390(_conv_forward)
                 476336   29.569    0.000   29.569    0.000 {built-in method conv2d}
               10033262   28.842    0.000   28.842    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                1648840    5.965    0.000   26.879    0.000 __init__.py:28(_make_grads)
                3297680    5.792    0.000   26.834    0.000 profiler.py:615(__enter__)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9651528: <Diamonds2_0.5_NN_2> in cluster <dcc> Done

Job <Diamonds2_0.5_NN_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Tue May 18 21:04:58 2021
Job was executed on host(s) <n-62-20-2>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed May 19 07:00:31 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 19 07:00:31 2021
Terminated at Wed May 19 16:56:04 2021
Results reported at Wed May 19 16:56:04 2021

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

    CPU time :                                   35622.16 sec.
    Max Memory :                                 3336 MB
    Average Memory :                             2932.01 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13048.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35846 sec.
    Turnaround time :                            71466 sec.

The output (if any) is above this job summary.

