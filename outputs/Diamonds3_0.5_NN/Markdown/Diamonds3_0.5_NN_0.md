
# Parameters

    Name :                      Diamonds3_0.5_NN-0
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
    Num :                       0
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      12974481093 function calls (12323581961 primitive calls) in 35703.03 seconds

##    Ordered by: cumulative time
   List reduced from 485 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35703.035 35703.035 {built-in method builtins.exec}
                      1    0.001    0.001 35703.035 35703.035 <string>:1(<module>)
                      1   27.524   27.524 35703.034 35703.034 allGraphsTrain.py:13(graphTrain)
                 115891  132.824    0.001 26781.233    0.231 allGraphsTrain.py:40(<listcomp>)
                 619280    3.002    0.000 26643.959    0.043 allGraphs.py:179(getInterventionsmodel)
        55574624/482311 4746.950    0.000 25122.000    0.052 allGraphs.py:186(recursiveBEST)
               53089586 2076.051    0.000 18442.272    0.000 BayesianNN.py:65(predict_no_convert)
               59293276  172.309    0.000 18150.114    0.000 BayesianNN.py:18(forward)
        656313372/61062792 2270.493    0.000 18075.405    0.000 module.py:866(_call_impl)
               59525058  774.924    0.000 17634.195    0.000 container.py:117(forward)
              178343392  306.376    0.000 6887.276    0.000 linear.py:93(forward)
              178343392  131.161    0.000 6453.893    0.000 functional.py:1737(linear)
              178343392 6290.593    0.000 6290.593    0.000 {built-in method torch._C._nn.linear}
                 115891 1316.149    0.011 5169.430    0.045 allGraphs.py:156(transformNot)
              177879828  134.051    0.000 4065.987    0.000 dropout.py:57(forward)
              177879828  442.884    0.000 3931.936    0.000 functional.py:1059(dropout)
              177879828 3361.515    0.000 3361.515    0.000 {built-in method dropout}
              178575174  123.404    0.000 2858.477    0.000 activation.py:713(forward)
              178575174  122.842    0.000 2735.073    0.000 functional.py:1364(leaky_relu)
              178575174 2589.388    0.000 2589.388    0.000 {built-in method torch._C._nn.leaky_relu}
                1421843   16.804    0.000 2524.766    0.002 BayesianNN.py:57(learn)
                1421843   16.604    0.000 2329.619    0.002 BayesianNN.py:21(learn)
                4781847   58.254    0.000 2244.125    0.000 BayesianNN.py:61(predict)
                 115891    3.023    0.000 1862.420    0.016 allGraphsTrain.py:33(<listcomp>)
               11705092  451.769    0.000 1859.413    0.000 allGraphs.py:114(states)
              140492463 1763.172    0.000 1763.172    0.000 {method 'item' of 'torch._C._TensorBase' objects}
              127480600 1505.473    0.000 1505.473    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
          692793/136969   70.314    0.000 1446.148    0.011 allGraphs.py:202(recursiveExplore)
                1537734   11.988    0.000 1101.889    0.001 optimizer.py:84(wrapper)
                1537734    5.747    0.000 1043.367    0.001 grad_mode.py:24(decorate_context)
                1537734   31.060    0.000 1024.148    0.001 adam.py:55(step)
               55764028   56.799    0.000  973.979    0.000 tensor.py:525(__rsub__)
                1537734  206.310    0.000  959.801    0.001 _functional.py:53(adam)
               55764028  905.924    0.000  905.924    0.000 {built-in method rsub}
                6203690  664.835    0.000  849.771    0.000 BayesianNN.py:43(convert_data)
                1537734    6.727    0.000  637.458    0.000 tensor.py:195(backward)
                1537734    5.515    0.000  630.519    0.000 __init__.py:68(backward)
                1537734  593.009    0.000  593.009    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                 115891    0.397    0.000  443.664    0.004 game.py:42(step)
                 115891    0.586    0.000  418.807    0.004 layers.py:827(step)
              656661045  403.422    0.000  403.422    0.000 {built-in method torch._C._get_tracing_state}
                 115891    2.977    0.000  388.629    0.003 allGraphs.py:141(transform)
                 115891   29.190    0.000  371.535    0.003 allGraphsTrain.py:44(<listcomp>)
        2924718590/2924718588  296.814    0.000  297.939    0.000 {built-in method builtins.len}
                 115891    0.388    0.000  258.671    0.002 agent.py:29(learn)
                 115891    2.384    0.000  258.052    0.002 agent.py:117(_learn)
                 115891    8.095    0.000  255.668    0.002 learner.py:42(Qlearn)
             2684778546  220.246    0.000  220.246    0.000 {method 'values' of 'collections.OrderedDict' objects}
                 115892   15.442    0.000  210.811    0.002 layers.py:793(update)
                 115891    7.931    0.000  206.858    0.002 layers.py:17(step)
              418561340  200.879    0.000  200.879    0.000 module.py:934(__getattr__)
               71345940  198.643    0.000  198.643    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               11589100   17.854    0.000  197.902    0.000 layer.py:106(move)
               18916372  195.145    0.000  195.145    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               59756840   36.015    0.000  187.944    0.000 flatten.py:39(forward)
               15482849  180.292    0.000  180.292    0.000 {built-in method zeros}
               18916372  172.876    0.000  172.876    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                1537734   26.178    0.000  162.023    0.000 optimizer.py:189(zero_grad)
               11589100  151.103    0.000  151.103    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                1717829  147.625    0.000  147.625    0.000 {built-in method tensor}
                 115891  136.997    0.001  136.997    0.001 allGraphsTrain.py:51(<listcomp>)
                1198736    1.201    0.000  130.207    0.000 game.py:38(board)
               58103215  122.943    0.000  122.943    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                9458186  111.411    0.000  111.411    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               11589100   26.608    0.000  107.270    0.000 layers.py:844(check)
              179417562   70.619    0.000  101.965    0.000 _VF.py:25(__getattr__)
                 115891   64.422    0.001   96.320    0.001 agent.py:67(modify)
                9458186   90.652    0.000   90.652    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                9458186   90.307    0.000   90.307    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                9458186   90.222    0.000   90.222    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                 231782    0.771    0.000   86.964    0.000 network.py:28(forward)
               82687114   59.377    0.000   73.858    0.000 types.py:171(__get__)
                 619280    4.917    0.000   72.558    0.000 allGraphs.py:167(format)
                1537734    1.834    0.000   71.250    0.000 loss.py:527(forward)
                9458186   70.338    0.000   70.338    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                1537734    5.315    0.000   69.415    0.000 functional.py:2898(mse_loss)
               11589100   15.228    0.000   57.446    0.000 layers.py:838(isFree)
              434817525   55.554    0.000   55.554    0.000 {built-in method torch._C._has_torch_function_unary}
               66207362   44.277    0.000   55.107    0.000 tensor.py:906(grad)
                 115891    1.515    0.000   53.108    0.000 agent.py:112(__call__)
                 103704    0.950    0.000   52.593    0.001 layers.py:849(restart)
                2455078   51.044    0.000   51.044    0.000 {built-in method cat}
               11589200    5.360    0.000   49.877    0.000 {built-in method builtins.all}
               59525058   34.201    0.000   49.588    0.000 container.py:109(__iter__)
              186334642   33.432    0.000   48.942    0.000 enum.py:646(__hash__)
                1537734   48.359    0.000   48.359    0.000 {built-in method torch._C._nn.mse_loss}
                 927136   25.662    0.000   47.130    0.000 layer.py:175(NoRock_update)
               61805302   16.439    0.000   45.886    0.000 layers.py:799(<genexpr>)
                 103704    0.471    0.000   44.573    0.000 level.py:8(__init__)
              235645154   43.675    0.000   43.675    0.000 {built-in method torch._C._has_torch_function_variadic}
               78041857   33.338    0.000   42.218    0.000 layer.py:103(isFree)
               11485497    9.805    0.000   41.363    0.000 {built-in method builtins.any}
                 103704    1.377    0.000   36.277    0.000 levels.py:303(generate)
                9084854   36.143    0.000   36.143    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                 463564    1.095    0.000   33.504    0.000 conv.py:398(forward)
                 622245    5.709    0.000   33.423    0.000 level.py:41(notUsed)
                 463564    0.607    0.000   31.984    0.000 conv.py:390(_conv_forward)
              103369464   25.866    0.000   31.557    0.000 layers.py:809(<genexpr>)
              179529302   31.414    0.000   31.414    0.000 {built-in method builtins.getattr}
                 463564   31.378    0.000   31.378    0.000 {built-in method conv2d}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9651529: <Diamonds3_0.5_NN_0> in cluster <dcc> Done

Job <Diamonds3_0.5_NN_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Tue May 18 21:04:58 2021
Job was executed on host(s) <n-62-20-7>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed May 19 07:02:18 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 19 07:02:18 2021
Terminated at Wed May 19 16:57:24 2021
Results reported at Wed May 19 16:57:24 2021

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

    CPU time :                                   35662.23 sec.
    Max Memory :                                 2296 MB
    Average Memory :                             2295.71 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14088.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35803 sec.
    Turnaround time :                            71546 sec.

The output (if any) is above this job summary.

