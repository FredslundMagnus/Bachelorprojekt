
# Parameters

    Name :                      Diamonds2_0.5_NN-1
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
    Num :                       1
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      16649462657 function calls (15785362083 primitive calls) in 35721.27 seconds

##    Ordered by: cumulative time
   List reduced from 485 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35721.268 35721.268 {built-in method builtins.exec}
                      1    0.001    0.001 35721.268 35721.268 <string>:1(<module>)
                      1   24.601   24.601 35721.267 35721.267 allGraphsTrain.py:13(graphTrain)
                 113151  104.002    0.001 28064.718    0.248 allGraphsTrain.py:40(<listcomp>)
                 846706    3.899    0.000 27953.953    0.033 allGraphs.py:179(getInterventionsmodel)
        74175921/661242 4712.458    0.000 26343.860    0.040 allGraphs.py:186(recursiveBEST)
               70962746 2239.571    0.000 19605.332    0.000 BayesianNN.py:65(predict_no_convert)
               78761229  193.806    0.000 19137.619    0.000 BayesianNN.py:18(forward)
        870671692/80796382 2662.418    0.000 19001.214    0.000 module.py:866(_call_impl)
               78987531  864.431    0.000 18486.824    0.000 container.py:117(forward)
              236736291  379.372    0.000 7187.602    0.000 linear.py:93(forward)
              236736291  155.286    0.000 6641.748    0.000 functional.py:1737(linear)
              236736291 6451.434    0.000 6451.434    0.000 {built-in method torch._C._nn.linear}
                 113151  983.044    0.009 4362.109    0.039 allGraphs.py:156(transformNot)
              236283687  160.498    0.000 4259.155    0.000 dropout.py:57(forward)
              236283687  553.553    0.000 4098.657    0.000 functional.py:1059(dropout)
              236283687 3382.304    0.000 3382.304    0.000 {built-in method dropout}
              236962593  141.696    0.000 2717.181    0.000 activation.py:713(forward)
              236962593  151.794    0.000 2575.485    0.000 functional.py:1364(leaky_relu)
              236962593 2396.392    0.000 2396.392    0.000 {built-in method torch._C._nn.leaky_relu}
                6102783   67.486    0.000 2356.558    0.000 BayesianNN.py:61(predict)
                1695700   18.297    0.000 2327.638    0.001 BayesianNN.py:57(learn)
                1695700   17.540    0.000 2097.733    0.001 BayesianNN.py:21(learn)
              160108604 1700.640    0.000 1700.640    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                 113151    2.708    0.000 1606.166    0.014 allGraphsTrain.py:33(<listcomp>)
               11428352  330.601    0.000 1603.569    0.000 allGraphs.py:114(states)
          895634/185464   70.022    0.000 1503.400    0.008 allGraphs.py:202(recursiveExplore)
              147096900 1175.363    0.000 1175.363    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
               74338000   65.531    0.000 1013.092    0.000 tensor.py:525(__rsub__)
                7798483  781.983    0.000  963.043    0.000 BayesianNN.py:43(convert_data)
               74338000  937.394    0.000  937.394    0.000 {built-in method rsub}
                1808851   13.823    0.000  914.189    0.001 optimizer.py:84(wrapper)
                1808851    6.635    0.000  852.820    0.000 grad_mode.py:24(decorate_context)
                1808851   36.069    0.000  831.106    0.000 adam.py:55(step)
                1808851  167.907    0.000  755.315    0.000 _functional.py:53(adam)
                1808851    7.558    0.000  569.043    0.000 tensor.py:195(backward)
                1808851    6.130    0.000  561.263    0.000 __init__.py:68(backward)
                1808851  524.158    0.000  524.158    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                 113151    0.358    0.000  439.674    0.004 game.py:42(step)
                 113151    3.528    0.000  438.175    0.004 allGraphs.py:141(transform)
                 113151    0.527    0.000  416.947    0.004 layers.py:827(step)
              871011145  387.457    0.000  387.457    0.000 {built-in method torch._C._get_tracing_state}
        3852078899/3852078897  339.071    0.000  340.058    0.000 {built-in method builtins.len}
             3561674299  270.660    0.000  270.660    0.000 {method 'values' of 'collections.OrderedDict' objects}
                 113151   17.576    0.000  263.841    0.002 allGraphsTrain.py:44(<listcomp>)
              555061548  262.862    0.000  262.862    0.000 module.py:934(__getattr__)
                 113151    7.988    0.000  225.240    0.002 layers.py:17(step)
               11315100   17.052    0.000  216.312    0.000 layer.py:106(move)
               79213833   43.401    0.000  195.695    0.000 flatten.py:39(forward)
                 113151    0.456    0.000  192.080    0.002 agent.py:29(learn)
                 113151    2.180    0.000  191.393    0.002 agent.py:117(_learn)
                 113152   14.460    0.000  190.638    0.002 layers.py:793(update)
                 113151    6.095    0.000  189.213    0.002 learner.py:42(Qlearn)
               90528933  179.480    0.000  179.480    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                1919572  177.350    0.000  177.350    0.000 {built-in method tensor}
               19214669  164.392    0.000  164.392    0.000 {built-in method zeros}
                1412462    1.185    0.000  158.941    0.000 game.py:38(board)
               22158816  146.902    0.000  146.902    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                1808851   25.384    0.000  142.236    0.000 optimizer.py:189(zero_grad)
              238092538   91.617    0.000  132.884    0.000 _VF.py:25(__getattr__)
               22158816  130.892    0.000  130.892    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               77291831  126.723    0.000  126.723    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               11315100   29.197    0.000  117.725    0.000 layers.py:844(check)
              124341870   83.967    0.000  106.552    0.000 types.py:171(__get__)
                 846706    6.118    0.000  102.467    0.000 allGraphs.py:167(format)
               11315100  102.449    0.000  102.449    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               11079408   92.340    0.000   92.340    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                 113151   83.524    0.001   83.524    0.001 allGraphsTrain.py:51(<listcomp>)
                 113151   49.284    0.000   74.997    0.001 agent.py:67(modify)
               11079408   72.998    0.000   72.998    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               11079408   71.239    0.000   71.239    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                 226302    0.658    0.000   71.079    0.000 network.py:28(forward)
               11079408   70.169    0.000   70.169    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                1808851    2.262    0.000   69.556    0.000 loss.py:527(forward)
                1808851    6.258    0.000   67.294    0.000 functional.py:2898(mse_loss)
               11315100   17.713    0.000   65.900    0.000 layers.py:838(isFree)
               78987531   46.301    0.000   65.856    0.000 container.py:109(__iter__)
              564822296   65.137    0.000   65.137    0.000 {built-in method torch._C._has_torch_function_unary}
               77555916   50.449    0.000   62.629    0.000 tensor.py:906(grad)
               11079408   53.381    0.000   53.381    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                3066982   51.181    0.000   51.181    0.000 {built-in method cat}
                1018368   27.218    0.000   50.682    0.000 layer.py:175(NoRock_update)
               92232462   37.747    0.000   48.186    0.000 layer.py:103(isFree)
              179294540   32.807    0.000   47.696    0.000 enum.py:646(__hash__)
              312883142   45.493    0.000   45.493    0.000 {built-in method torch._C._has_torch_function_variadic}
               11228480   10.439    0.000   44.493    0.000 {built-in method builtins.any}
                  86721    0.855    0.000   44.416    0.001 layers.py:849(restart)
                1808851   44.384    0.000   44.384    0.000 {built-in method torch._C._nn.mse_loss}
                 113151    1.340    0.000   44.240    0.000 agent.py:112(__call__)
              238202297   41.324    0.000   41.324    0.000 {built-in method builtins.getattr}
                  86721    0.404    0.000   37.357    0.000 level.py:8(__init__)
              112284790   27.537    0.000   34.055    0.000 layers.py:809(<genexpr>)
                  86721    1.262    0.000   33.486    0.000 levels.py:249(generate)
               11253976   32.753    0.000   32.753    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               11315200    5.548    0.000   32.429    0.000 {built-in method builtins.all}
                 563642    5.190    0.000   30.863    0.000 level.py:41(notUsed)
                1808851    6.458    0.000   29.396    0.000 __init__.py:28(_make_grads)
                3617702    6.046    0.000   29.270    0.000 profiler.py:615(__enter__)
                 452604    0.995    0.000   28.231    0.000 conv.py:398(forward)
               64605465   16.578    0.000   28.154    0.000 layers.py:799(<genexpr>)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9651527: <Diamonds2_0.5_NN_1> in cluster <dcc> Done

Job <Diamonds2_0.5_NN_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Tue May 18 21:04:58 2021
Job was executed on host(s) <n-62-20-7>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed May 19 07:00:29 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 19 07:00:29 2021
Terminated at Wed May 19 16:56:02 2021
Results reported at Wed May 19 16:56:02 2021

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

    CPU time :                                   35666.26 sec.
    Max Memory :                                 2298 MB
    Average Memory :                             2289.41 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14086.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35843 sec.
    Turnaround time :                            71464 sec.

The output (if any) is above this job summary.

