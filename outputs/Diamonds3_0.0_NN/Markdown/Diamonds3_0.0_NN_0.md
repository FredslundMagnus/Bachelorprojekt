
# Parameters

    Name :                      Diamonds3_0.0_NN-0
    Main :                      graphTrain
    Level :                     Levels.Causal6
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


      12320409497 function calls (11792547871 primitive calls) in 35708.74 seconds

##    Ordered by: cumulative time
   List reduced from 475 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35708.743 35708.743 {built-in method builtins.exec}
                      1    0.001    0.001 35708.743 35708.743 <string>:1(<module>)
                      1   25.969   25.969 35708.742 35708.742 allGraphsTrain.py:13(graphTrain)
                 101478  126.408    0.001 26735.157    0.263 allGraphsTrain.py:40(<listcomp>)
                 577280    2.826    0.000 26604.415    0.046 allGraphs.py:179(getInterventionsmodel)
        43792263/392876 3673.426    0.000 24258.397    0.062 allGraphs.py:186(recursiveBEST)
               48171682  111.028    0.000 18030.478    0.000 BayesianNN.py:18(forward)
        533417571/49671191 1755.434    0.000 18024.749    0.000 module.py:715(_call_impl)
               41803944 1956.482    0.000 17694.978    0.000 BayesianNN.py:65(predict_no_convert)
               48374638  619.795    0.000 17670.732    0.000 container.py:115(forward)
              144920958  261.581    0.000 7938.814    0.000 linear.py:92(forward)
              144920958  492.016    0.000 7569.736    0.000 functional.py:1669(linear)
              144920958 5267.992    0.000 5267.992    0.000 {built-in method addmm}
                 101478 1309.050    0.013 4650.326    0.046 allGraphs.py:156(transformNot)
              144515046  104.957    0.000 4077.668    0.000 dropout.py:57(forward)
              144515046  421.330    0.000 3972.711    0.000 functional.py:960(dropout)
              144515046 3421.317    0.000 3421.317    0.000 {built-in method dropout}
                5172663   67.770    0.000 2957.326    0.001 BayesianNN.py:61(predict)
              145123914   92.952    0.000 2613.785    0.000 activation.py:713(forward)
                1195075   13.704    0.000 2541.427    0.002 BayesianNN.py:57(learn)
              145123914  141.447    0.000 2520.833    0.000 functional.py:1292(leaky_relu)
              145123914 2363.933    0.000 2363.933    0.000 {built-in method torch._C._nn.leaky_relu}
                1195075   13.948    0.000 2336.749    0.002 BayesianNN.py:21(learn)
          899848/184404   90.128    0.000 2273.132    0.012 allGraphs.py:202(recursiveExplore)
                 101478    2.781    0.000 1833.452    0.018 allGraphsTrain.py:33(<listcomp>)
               10249379  475.332    0.000 1830.727    0.000 allGraphs.py:114(states)
              122969983 1676.273    0.000 1676.273    0.000 {method 'item' of 'torch._C._TensorBase' objects}
              111626300 1450.421    0.000 1450.421    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
              144920958 1241.018    0.000 1241.018    0.000 {method 't' of 'torch._C._TensorBase' objects}
               54871499  180.734    0.000 1190.722    0.000 tensor.py:21(wrapped)
                1296553    6.758    0.000 1118.400    0.001 grad_mode.py:23(decorate_context)
                1296553   30.913    0.000 1098.518    0.001 adam.py:55(step)
                6367738  870.774    0.000 1089.543    0.000 BayesianNN.py:43(convert_data)
               44216309  141.328    0.000 1021.348    0.000 tensor.py:506(__rsub__)
                1296553  199.211    0.000  942.969    0.001 functional.py:53(adam)
               44216309  880.020    0.000  880.020    0.000 {built-in method rsub}
                 101478    3.777    0.000  840.814    0.008 allGraphs.py:141(transform)
               44114831  725.536    0.000  725.536    0.000 {method 'gt' of 'torch._C._TensorBase' objects}
                1296553    7.353    0.000  581.032    0.000 tensor.py:181(backward)
                1296553    3.939    0.000  573.678    0.000 __init__.py:68(backward)
                1296553  537.026    0.000  537.026    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
              228909970  158.942    0.000  502.047    0.000 overrides.py:1070(has_torch_function)
                 101478    0.374    0.000  495.426    0.005 game.py:42(step)
                 101478    0.502    0.000  472.135    0.005 layers.py:827(step)
              533722005  410.016    0.000  410.016    0.000 {built-in method torch._C._get_tracing_state}
              386432640  177.266    0.000  399.396    0.000 {built-in method builtins.any}
                 101478   27.235    0.000  363.893    0.004 allGraphsTrain.py:44(<listcomp>)
                 101478    0.387    0.000  269.404    0.003 agent.py:29(learn)
                 101478    2.118    0.000  268.807    0.003 agent.py:117(_learn)
                 101478    7.782    0.000  266.690    0.003 learner.py:42(Qlearn)
                 101478    7.388    0.000  260.770    0.003 layers.py:17(step)
               10147800   15.880    0.000  252.546    0.000 layer.py:106(move)
               55875978  146.260    0.000  231.187    0.000 tensor.py:933(grad)
                1296553   21.513    0.000  223.741    0.000 optimizer.py:167(zero_grad)
                 101478    9.571    0.000  212.714    0.002 allGraphsTrain.py:51(<listcomp>)
                 101479   13.598    0.000  210.372    0.002 layers.py:793(update)
               15964548  197.302    0.000  197.302    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              622871548  157.335    0.000  192.914    0.000 overrides.py:1083(<genexpr>)
               12735477  188.984    0.000  188.984    0.000 {built-in method zeros}
               58725394  187.051    0.000  187.051    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
             2182044922  180.456    0.000  180.456    0.000 {method 'values' of 'collections.OrderedDict' objects}
              340223958  171.137    0.000  171.138    0.000 module.py:765(__getattr__)
               10147800   34.630    0.000  169.271    0.000 layers.py:844(check)
               48577594   30.749    0.000  169.202    0.000 flatten.py:39(forward)
               15964548  166.907    0.000  166.907    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               10655190  164.239    0.000  164.239    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
        1327192847/1327192845  151.622    0.000  153.391    0.000 {built-in method builtins.len}
               10147800  149.517    0.000  149.517    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                1542739  138.479    0.000  138.479    0.000 {built-in method tensor}
                1084671    1.139    0.000  121.608    0.000 game.py:38(board)
              145811599   63.097    0.000  115.549    0.000 _VF.py:25(__getattr__)
               65019399   40.607    0.000  112.630    0.000 {built-in method builtins.all}
                 101478   57.790    0.001  107.479    0.001 agent.py:67(modify)
                7982274  107.420    0.000  107.420    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                7982274   98.820    0.000   98.820    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               47179563   95.550    0.000   95.550    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                7982274   90.209    0.000   90.209    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                 202956    0.515    0.000   88.422    0.000 network.py:28(forward)
              374826537   88.090    0.000   88.090    0.000 {built-in method builtins.getattr}
                7982274   80.536    0.000   80.536    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              144920958   74.965    0.000   74.965    0.000 functional.py:1686(<listcomp>)
                3064732   73.898    0.000   73.898    0.000 {built-in method cat}
               74045723   55.412    0.000   70.372    0.000 types.py:171(__get__)
                 577280    4.727    0.000   69.843    0.000 allGraphs.py:167(format)
                1296553    1.578    0.000   69.784    0.000 loss.py:445(forward)
                 139295    1.284    0.000   68.698    0.000 layers.py:849(restart)
                1296553    6.294    0.000   68.207    0.000 functional.py:2637(mse_loss)
                7982274   63.780    0.000   63.780    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              247079199   42.427    0.000   61.831    0.000 enum.py:646(__hash__)
              145935858   60.175    0.000   60.175    0.000 {method 'dim' of 'torch._C._TensorBase' objects}
                 139295    0.581    0.000   57.917    0.000 level.py:8(__init__)
               10147800   14.476    0.000   53.724    0.000 layers.py:838(isFree)
                 101478    1.294    0.000   53.149    0.001 agent.py:112(__call__)
                9298135   51.601    0.000   51.601    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                 139295    1.809    0.000   48.940    0.000 levels.py:303(generate)
              438449697   45.510    0.000   45.510    0.000 _jit_internal.py:750(is_scripting)
                1296553   45.320    0.000   45.320    0.000 {built-in method torch._C._nn.mse_loss}
                 836094    7.636    0.000   45.199    0.000 level.py:41(notUsed)
               48374638   29.976    0.000   43.322    0.000 container.py:107(__iter__)
                 811832   23.357    0.000   42.553    0.000 layer.py:175(NoRock_update)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9651549: <Diamonds3_0.0_NN_0> in cluster <dcc> Done

Job <Diamonds3_0.0_NN_0> was submitted from host <n-62-27-18> by user <s183905> in cluster <dcc> at Tue May 18 21:12:59 2021
Job was executed on host(s) <n-62-20-6>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Wed May 19 07:10:18 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 19 07:10:18 2021
Terminated at Wed May 19 17:05:34 2021
Results reported at Wed May 19 17:05:34 2021

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

    CPU time :                                   35618.13 sec.
    Max Memory :                                 2059 MB
    Average Memory :                             2057.78 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14325.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35814 sec.
    Turnaround time :                            71555 sec.

The output (if any) is above this job summary.

