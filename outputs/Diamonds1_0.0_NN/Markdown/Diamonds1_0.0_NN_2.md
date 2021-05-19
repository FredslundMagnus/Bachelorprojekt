
# Parameters

    Name :                      Diamonds1_0.0_NN-2
    Main :                      graphTrain
    Level :                     Levels.Causal2
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
    Num :                       2
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      11312722009 function calls (10846685187 primitive calls) in 35709.69 seconds

##    Ordered by: cumulative time
   List reduced from 472 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35709.694 35709.694 {built-in method builtins.exec}
                      1    0.001    0.001 35709.694 35709.694 <string>:1(<module>)
                      1   30.788   30.788 35709.694 35709.694 allGraphsTrain.py:13(graphTrain)
                 113473  155.384    0.001 25658.230    0.226 allGraphsTrain.py:40(<listcomp>)
                 809592    4.010    0.000 25496.555    0.031 allGraphs.py:179(getInterventionsmodel)
        39015737/628020 3543.488    0.000 23521.353    0.037 allGraphs.py:186(recursiveBEST)
        471313862/44207652 1700.191    0.000 17437.764    0.000 module.py:715(_call_impl)
               42483675  111.717    0.000 17400.669    0.000 BayesianNN.py:18(forward)
               42710621  587.690    0.000 17077.423    0.000 container.py:115(forward)
               36397016 1849.822    0.000 16841.383    0.000 BayesianNN.py:65(predict_no_convert)
              127904917  261.018    0.000 7683.603    0.000 linear.py:92(forward)
              127904917  470.712    0.000 7315.186    0.000 functional.py:1669(linear)
              127904917 5092.773    0.000 5092.773    0.000 {built-in method addmm}
                 113473 1362.740    0.012 5012.948    0.044 allGraphs.py:156(transformNot)
              127451025  102.306    0.000 3901.482    0.000 dropout.py:57(forward)
              127451025  432.624    0.000 3799.176    0.000 functional.py:960(dropout)
              127451025 3262.904    0.000 3262.904    0.000 {built-in method dropout}
                1383558   17.078    0.000 3234.792    0.002 BayesianNN.py:57(learn)
                1383558   17.213    0.000 2974.803    0.002 BayesianNN.py:21(learn)
                4703101   66.630    0.000 2921.409    0.001 BayesianNN.py:61(predict)
              128131863   84.841    0.000 2533.317    0.000 activation.py:713(forward)
              128131863  138.993    0.000 2448.476    0.000 functional.py:1292(leaky_relu)
              128131863 2293.580    0.000 2293.580    0.000 {built-in method torch._C._nn.leaky_relu}
          724052/181572   75.065    0.000 1878.341    0.010 allGraphs.py:202(recursiveExplore)
                 113473    3.394    0.000 1822.349    0.016 allGraphsTrain.py:33(<listcomp>)
               11460874  477.574    0.000 1819.055    0.000 allGraphs.py:114(states)
              114857862 1720.092    0.000 1720.092    0.000 {method 'item' of 'torch._C._TensorBase' objects}
              102126100 1465.641    0.000 1465.641    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                1497031    8.275    0.000 1425.301    0.001 grad_mode.py:23(decorate_context)
                1497031   38.808    0.000 1400.655    0.001 adam.py:55(step)
                 113473    4.932    0.000 1269.134    0.011 allGraphs.py:141(transform)
               50958335  180.562    0.000 1214.769    0.000 tensor.py:21(wrapped)
              127904917 1202.370    0.000 1202.370    0.000 {method 't' of 'torch._C._TensorBase' objects}
                1497031  252.926    0.000 1199.290    0.001 functional.py:53(adam)
                6086659  875.794    0.000 1106.649    0.000 BayesianNN.py:43(convert_data)
               39043670  136.634    0.000  974.551    0.000 tensor.py:506(__rsub__)
               39043670  837.917    0.000  837.917    0.000 {built-in method rsub}
                1497031    9.040    0.000  733.433    0.000 tensor.py:181(backward)
                1497031    4.850    0.000  724.392    0.000 __init__.py:68(backward)
               38930197  698.540    0.000  698.540    0.000 {method 'gt' of 'torch._C._TensorBase' objects}
                1497031  679.253    0.000  679.253    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                 113473    0.458    0.000  536.965    0.005 game.py:42(step)
              223700413  162.381    0.000  535.355    0.000 overrides.py:1070(has_torch_function)
                 113473    0.571    0.000  510.903    0.005 layers.py:827(step)
                 113473   33.218    0.000  447.976    0.004 allGraphsTrain.py:44(<listcomp>)
              365747128  179.173    0.000  420.989    0.000 {built-in method builtins.any}
              471654281  406.858    0.000  406.858    0.000 {built-in method torch._C._get_tracing_state}
                 113473    0.397    0.000  331.553    0.003 agent.py:29(learn)
                 113473    2.563    0.000  330.921    0.003 agent.py:117(_learn)
                 113473    9.507    0.000  328.358    0.003 learner.py:42(Qlearn)
               64463984  191.970    0.000  303.076    0.000 tensor.py:933(grad)
                1497031   27.449    0.000  290.505    0.000 optimizer.py:167(zero_grad)
                 113473    8.780    0.000  281.292    0.002 layers.py:17(step)
               11347300   19.617    0.000  271.469    0.000 layer.py:106(move)
                 113473   11.710    0.000  263.446    0.002 allGraphsTrain.py:51(<listcomp>)
               18418264  251.910    0.000  251.910    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                 113474   16.200    0.000  228.450    0.002 layers.py:793(update)
               18418264  213.607    0.000  213.607    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              597428013  174.084    0.000  210.817    0.000 overrides.py:1083(<genexpr>)
               11914665  203.348    0.000  203.348    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               12173319  199.592    0.000  199.592    0.000 {built-in method zeros}
               54284867  192.696    0.000  192.696    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               11347300  185.499    0.000  185.499    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
             1927966069  180.241    0.000  180.241    0.000 {method 'values' of 'collections.OrderedDict' objects}
               11347300   36.766    0.000  172.249    0.000 layers.py:844(check)
              300812324  168.957    0.000  168.957    0.000 module.py:765(__getattr__)
                1885552  164.294    0.000  164.294    0.000 {built-in method tensor}
               42937567   27.069    0.000  160.295    0.000 flatten.py:39(forward)
        1188730982/1188730980  152.811    0.000  154.991    0.000 {built-in method builtins.len}
                1376958    1.438    0.000  144.689    0.000 game.py:38(board)
                9209132  135.476    0.000  135.476    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                 113473   72.741    0.001  133.420    0.001 agent.py:67(modify)
                9209132  124.714    0.000  124.714    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                9209132  114.869    0.000  114.869    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                 226946    0.695    0.000  108.118    0.000 network.py:28(forward)
                9209132  102.733    0.000  102.733    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               62305735   40.023    0.000   96.011    0.000 {built-in method builtins.all}
                 809592    6.816    0.000   92.519    0.000 allGraphs.py:167(format)
               41327063   91.965    0.000   91.965    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                 199665    1.710    0.000   91.142    0.000 layers.py:849(restart)
              128948056   62.931    0.000   89.166    0.000 _VF.py:25(__getattr__)
                1497031    1.934    0.000   88.035    0.000 loss.py:445(forward)
                1497031    7.342    0.000   86.101    0.000 functional.py:2637(mse_loss)
               65638462   53.186    0.000   81.894    0.000 types.py:171(__get__)
                9209132   81.223    0.000   81.223    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                 199665    0.842    0.000   75.158    0.000 level.py:8(__init__)
              127904917   72.551    0.000   72.551    0.000 functional.py:1686(<listcomp>)
                 113473    1.491    0.000   64.411    0.001 agent.py:112(__call__)
              223209670   44.168    0.000   64.230    0.000 enum.py:646(__hash__)
                2396866   63.532    0.000   63.532    0.000 {built-in method cat}
              352758480   63.039    0.000   63.039    0.000 {built-in method builtins.getattr}
                 199665    2.443    0.000   62.769    0.000 levels.py:151(generate)
               11347300   16.965    0.000   62.577    0.000 layers.py:838(isFree)
                 958217   10.019    0.000   57.817    0.000 level.py:41(notUsed)
                1497031   57.426    0.000   57.426    0.000 {built-in method torch._C._nn.mse_loss}
              129039767   55.997    0.000   55.997    0.000 {method 'dim' of 'torch._C._TensorBase' objects}
                8895596   55.318    0.000   55.318    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                 794318   27.717    0.000   49.372    0.000 layer.py:175(NoRock_update)
              387979018   46.824    0.000   46.824    0.000 _jit_internal.py:750(is_scripting)
               73292956   36.135    0.000   45.613    0.000 layer.py:103(isFree)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9651545: <Diamonds1_0.0_NN_2> in cluster <dcc> Done

Job <Diamonds1_0.0_NN_2> was submitted from host <n-62-27-18> by user <s183905> in cluster <dcc> at Tue May 18 21:12:59 2021
Job was executed on host(s) <n-62-20-14>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Tue May 18 21:13:01 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue May 18 21:13:01 2021
Terminated at Wed May 19 07:08:29 2021
Results reported at Wed May 19 07:08:29 2021

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

    CPU time :                                   35619.07 sec.
    Max Memory :                                 2062 MB
    Average Memory :                             2054.46 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14322.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35729 sec.
    Turnaround time :                            35730 sec.

The output (if any) is above this job summary.

