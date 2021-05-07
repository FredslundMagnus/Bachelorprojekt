
# Parameters

    Name :                      Causal3_Conver4-0
    Main :                      CFagent
    Level :                     Levels.Causal3
    Failed actions chance :     0
    Use model :                 True
    Depth :                     3
    Model explore :             1000000
    Samples :                   5
    Hours :                     24.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.UCB1
    Network1 :                  Networks.Teleporter
    K1 :                        5000000
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
    K2 :                        1000000
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
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                4
    Counterfacts :              1
    Topn :                      3
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      58984511323 function calls (58678184236 primitive calls) in 86109.99 seconds

##    Ordered by: cumulative time
   List reduced from 510 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86109.995 86109.995 {built-in method builtins.exec}
                      1    5.127    5.127 86109.995 86109.995 <string>:1(<module>)
                      1  434.035  434.035 86104.867 86104.867 main.py:80(CFagent)
                9602070   40.450    0.000 24839.855    0.003 agent.py:29(learn)
                9602068  631.699    0.000 20041.487    0.002 learner.py:42(Qlearn)
                3200690   17.229    0.000 17466.729    0.005 game.py:42(step)
                3200690   21.903    0.000 16746.058    0.005 layers.py:827(step)
        342521477/36196081 1492.843    0.000 11789.336    0.000 module.py:866(_call_impl)
               26594013   82.328    0.000 11012.398    0.000 network.py:28(forward)
               26594013  368.122    0.000 10738.480    0.000 container.py:117(forward)
                3200690  324.542    0.000 10354.681    0.003 layers.py:17(step)
              319958426  568.399    0.000 9994.735    0.000 layer.py:106(move)
                3200690  412.902    0.000 9681.246    0.003 agent.py:54(_learn)
                3200690  958.687    0.000 9392.767    0.003 agent.py:212(counterfact)
                3200690  404.551    0.000 8823.096    0.003 agent.py:204(_learn)
                3200690 7402.403    0.002 8553.898    0.003 replaybuffer.py:22(sample_data)
                3200690 7315.957    0.002 8415.171    0.003 replaybuffer.py:67(sample_data)
                9602068   91.623    0.000 7688.258    0.001 optimizer.py:84(wrapper)
                9602068   48.652    0.000 7303.225    0.001 grad_mode.py:24(decorate_context)
                9602068  315.254    0.000 7151.610    0.001 adam.py:55(step)
                9602068 1507.403    0.000 6492.083    0.001 _functional.py:53(adam)
                3200691  502.214    0.000 6334.261    0.002 layers.py:793(update)
                3200690  109.989    0.000 6271.953    0.002 agent.py:117(_learn)
                8494787  260.305    0.000 5806.435    0.001 agent.py:49(__call__)
              319958426 1202.826    0.000 5698.763    0.000 layers.py:844(check)
                3200690 3343.986    0.001 5655.196    0.002 replaybuffer.py:28(teleporter_save_data)
                9602068   40.657    0.000 5272.084    0.001 tensor.py:195(backward)
                9602068   41.906    0.000 5230.182    0.001 __init__.py:68(backward)
                9602068 4983.245    0.001 4983.245    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3200690 2789.774    0.001 4945.493    0.002 agent.py:88(interveen)
               45747648 4142.236    0.000 4142.236    0.000 {built-in method tensor}
               38368048   25.989    0.000 3952.417    0.000 game.py:38(board)
               53188026  122.224    0.000 3944.188    0.000 conv.py:398(forward)
               51211048 2105.899    0.000 3766.245    0.000 layer.py:175(NoRock_update)
               53188026   80.753    0.000 3757.119    0.000 conv.py:390(_conv_forward)
               53188026 3676.367    0.000 3676.367    0.000 {built-in method conv2d}
              319958426  552.057    0.000 3181.900    0.000 layers.py:838(isFree)
                2095780   48.236    0.000 3050.638    0.001 agent.py:176(choose_action)
               73380659  153.649    0.000 3033.971    0.000 linear.py:93(forward)
               73380659   62.440    0.000 2798.807    0.000 functional.py:1737(linear)
               73380659 2720.898    0.000 2720.898    0.000 {built-in method torch._C._nn.linear}
             2389007910 2238.403    0.000 2629.844    0.000 layer.py:103(isFree)
                3200690 1679.406    0.001 2524.181    0.001 agent.py:67(modify)
              218679310 2183.818    0.000 2183.818    0.000 {built-in method clone}
               43702367 1861.334    0.000 1861.334    0.000 {built-in method cat}
               11695477   81.951    0.000 1603.197    0.000 agent.py:59(modify_board)
               99974672   87.649    0.000 1590.529    0.000 activation.py:713(forward)
                4265369   61.199    0.000 1553.446    0.000 layers.py:849(restart)
                3200688   66.604    0.000 1529.146    0.000 agent.py:172(__call__)
               99974672   87.476    0.000 1502.880    0.000 functional.py:1364(leaky_relu)
                3200690   63.376    0.000 1435.988    0.000 agent.py:112(__call__)
                3200690 1117.510    0.000 1428.116    0.000 replaybuffer.py:73(CF_save_data)
               99974672 1398.981    0.000 1398.981    0.000 {built-in method torch._C._nn.leaky_relu}
              179238600 1292.311    0.000 1292.311    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
             4845553615  884.178    0.000 1275.311    0.000 enum.py:646(__hash__)
              319004422  293.390    0.000 1258.950    0.000 {built-in method builtins.any}
              319958426  819.814    0.000 1255.852    0.000 layers.py:286(check)
                9602068  206.765    0.000 1135.061    0.000 optimizer.py:189(zero_grad)
                4265369   25.027    0.000 1114.279    0.000 level.py:8(__init__)
              179238600 1101.406    0.000 1101.406    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              319958426  641.525    0.000 1070.057    0.000 layers.py:246(check)
               11695477 1063.371    0.000 1063.371    0.000 {built-in method torch._C._nn.one_hot}
             1139649932 1008.026    0.000 1008.026    0.000 layer.py:154(elements)
              320069100  132.970    0.000  970.278    0.000 {built-in method builtins.all}
             2842233579  798.552    0.000  965.560    0.000 layers.py:809(<genexpr>)
                3200690   76.774    0.000  890.132    0.000 replaybuffer.py:18(stacker)
             1404471957  394.330    0.000  878.798    0.000 layers.py:799(<genexpr>)
                4265369   99.683    0.000  859.768    0.000 levels.py:164(generate)
                3200688   76.809    0.000  851.136    0.000 replaybuffer.py:63(stacker)
               89619300  736.859    0.000  736.859    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               89619300  662.038    0.000  662.038    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                2095780  548.074    0.000  638.065    0.000 agent.py:187(convert_values)
                8530738   90.393    0.000  635.280    0.000 level.py:41(notUsed)
                8494787  215.663    0.000  593.054    0.000 exploration.py:53(softmaxer)
               89619300  591.952    0.000  591.952    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               14932118  230.553    0.000  586.009    0.000 random.py:315(sample)
             6023617942  584.688    0.000  584.688    0.000 layer.py:99(positions)
               89619300  575.031    0.000  575.031    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
        7224124263/7224124260  504.564    0.000  569.872    0.000 {built-in method builtins.len}
              319958426  343.201    0.000  538.011    0.000 layers.py:273(check)
              627335184  432.003    0.000  535.028    0.000 tensor.py:906(grad)
              319958426  327.571    0.000  519.082    0.000 layers.py:313(check)
                3200690  296.793    0.000  504.710    0.000 collector.py:46(collect)
              233575475  492.065    0.000  492.065    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              319958426  329.043    0.000  481.797    0.000 layers.py:48(check)
                9602068   15.615    0.000  454.996    0.000 loss.py:527(forward)
               89619300  446.548    0.000  446.548    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                9602068   48.379    0.000  439.381    0.000 functional.py:2898(mse_loss)
             4845590158  391.140    0.000  391.140    0.000 {built-in method builtins.hash}
               34122952   45.391    0.000  366.022    0.000 layer.py:77(restart)
              319958426  239.562    0.000  361.480    0.000 layers.py:23(check)
              520464390  237.239    0.000  331.508    0.000 layer.py:138(add)
              151675879  206.939    0.000  301.141    0.000 layers.py:113(isDone)
              428642285  198.854    0.000  295.908    0.000 random.py:250(_randbelow_with_getrandbits)
              304462423  199.163    0.000  292.772    0.000 layer.py:134(remove)
                8530738   10.380    0.000  273.186    0.000 level.py:38(elementsIn)
                6401382  271.845    0.000  271.845    0.000 {built-in method nonzero}
                9602068  264.244    0.000  264.244    0.000 {built-in method torch._C._nn.mse_loss}
               53188026   39.029    0.000  257.811    0.000 flatten.py:39(forward)
                9603237  247.174    0.000  247.174    0.000 {built-in method max}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9615513: <Causal3_Conver4_0> in cluster <dcc> Done

Job <Causal3_Conver4_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Tue May  4 23:51:54 2021
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed May  5 06:24:40 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May  5 06:24:40 2021
Terminated at Thu May  6 06:19:57 2021
Results reported at Thu May  6 06:19:57 2021

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

    CPU time :                                   85905.35 sec.
    Max Memory :                                 9503 MB
    Average Memory :                             6478.66 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               6881.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86119 sec.
    Turnaround time :                            109683 sec.

The output (if any) is above this job summary.

