
# Parameters

    Name :                      Attempt2_Lights1_option_critic-2
    Main :                      option_critic_run
    Level :                     Levels.Causal3
    Failed actions chance :     0
    Use model :                 True
    Depth :                     3
    Model explore :             1000000
    Samples :                   5
    Hours :                     72.0
    Batch :                     25
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
    Cf convert :                3
    Counterfacts :              1
    Topn :                      6
    Random counterfacts :       False
    Minutes used :              4315 minutes.
    Hours used :                71 hours.

# Profiling


      50134372832 function calls (48527209067 primitive calls) in 258900.71 seconds

##    Ordered by: cumulative time
   List reduced from 434 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.709 258900.709 {built-in method builtins.exec}
                      1    0.339    0.339 258900.709 258900.709 <string>:1(<module>)
                      1 5720.830 5720.830 258900.370 258900.370 optionCritic.py:195(option_critic_run)
               57153750 9677.723    0.000 115725.840    0.002 optionCritic.py:143(actor_loss_fn)
        2122478948/522745490 10719.568    0.000 114690.872    0.000 module.py:866(_call_impl)
              177748162  853.061    0.000 106610.889    0.001 optionCritic.py:70(get_state)
              177748162 2279.783    0.000 103161.267    0.001 container.py:117(forward)
                2286150   19.883    0.000 68904.540    0.030 tensor.py:195(backward)
                2286150   22.986    0.000 68884.315    0.030 __init__.py:68(backward)
                2286150 68808.467    0.030 68808.467    0.030 {method 'run_backward' of 'torch._C._EngineBase' objects}
              355496324 1027.430    0.000 65294.906    0.000 conv.py:398(forward)
              355496324  560.325    0.000 63799.510    0.000 conv.py:390(_conv_forward)
              355496324 63239.184    0.000 63239.184    0.000 {built-in method conv2d}
               57153750 3672.522    0.000 21780.285    0.000 optionCritic.py:91(get_action)
              700493652 1738.831    0.000 21302.559    0.000 linear.py:93(forward)
              700493652  721.931    0.000 18853.430    0.000 functional.py:1737(linear)
              700493652 17964.119    0.000 17964.119    0.000 {built-in method torch._C._nn.linear}
               57153750 1226.524    0.000 14797.997    0.000 optionCritic.py:80(predict_option_termination)
                2286150   51.823    0.000 9873.446    0.004 optimizer.py:84(wrapper)
                2286150   27.568    0.000 9666.914    0.004 grad_mode.py:24(decorate_context)
                2286150  141.941    0.000 9589.214    0.004 rmsprop.py:56(step)
                2286150  137.277    0.000 9278.235    0.004 _functional.py:203(rmsprop)
              114307500 1289.034    0.000 8456.178    0.000 distribution.py:34(__init__)
              533244486  534.407    0.000 7439.953    0.000 activation.py:713(forward)
               57153750  609.541    0.000 7252.882    0.000 categorical.py:115(log_prob)
              533244486  544.874    0.000 6905.546    0.000 functional.py:1364(leaky_relu)
              533244486 6241.518    0.000 6241.518    0.000 {built-in method torch._C._nn.leaky_relu}
               57153750  810.161    0.000 6091.551    0.000 categorical.py:49(__init__)
               57153750  457.700    0.000 5871.578    0.000 bernoulli.py:34(__init__)
              172964541  405.938    0.000 5853.825    0.000 optionCritic.py:77(get_Q)
                 571537   96.833    0.000 4937.017    0.009 optionCritic.py:116(critic_loss_fn)
               32006094 4910.325    0.000 4910.325    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              114879037  419.887    0.000 4641.681    0.000 optionCritic.py:88(get_terminations)
                2286150   13.155    0.000 4251.712    0.002 game.py:42(step)
                2286150   21.643    0.000 4108.964    0.002 layers.py:827(step)
               57153750 2491.451    0.000 3702.473    0.000 constraints.py:398(check)
               32006094 3272.354    0.000 3272.354    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               57153750  520.976    0.000 2942.909    0.000 distribution.py:240(_validate_sample)
                2286150   89.082    0.000 2557.348    0.001 layers.py:17(step)
               57153750  157.439    0.000 2460.370    0.000 layer.py:106(move)
               57153750 2219.074    0.000 2219.074    0.000 constraints.py:364(check)
               57153750  405.122    0.000 2177.417    0.000 bernoulli.py:86(sample)
              177748162  233.555    0.000 2154.474    0.000 activation.py:101(forward)
               57153750 1047.509    0.000 2005.205    0.000 categorical.py:123(entropy)
             2749330195 1988.163    0.000 1988.338    0.000 module.py:934(__getattr__)
              177748162  194.386    0.000 1920.919    0.000 functional.py:1195(relu)
               57153750 1884.244    0.000 1884.244    0.000 constraints.py:249(check)
              171461250  257.203    0.000 1815.596    0.000 utils.py:106(__get__)
              400076250 1777.781    0.000 1777.781    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              177748162 1695.689    0.000 1695.689    0.000 {built-in method relu}
              177748162  177.313    0.000 1693.044    0.000 flatten.py:39(forward)
              172604324  187.508    0.000 1620.124    0.000 tensor.py:525(__rsub__)
              114307500  551.561    0.000 1588.665    0.000 functional.py:46(broadcast_tensors)
                2286151  210.860    0.000 1521.484    0.001 layers.py:793(update)
              177748162 1515.731    0.000 1515.731    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               57153750  316.625    0.000 1437.730    0.000 layers.py:844(check)
               57153750  399.261    0.000 1431.196    0.000 categorical.py:108(sample)
              172604324 1401.126    0.000 1401.126    0.000 {built-in method rsub}
               25147650   58.741    0.000 1370.178    0.000 tensor.py:575(__iter__)
               57153750   73.678    0.000 1362.890    0.000 categorical.py:88(logits)
             2147626598 1361.725    0.000 1361.725    0.000 {built-in method torch._C._get_tracing_state}
              114879037 1359.971    0.000 1359.971    0.000 {method 'max' of 'torch._C._TensorBase' objects}
               57153750  300.978    0.000 1351.726    0.000 utils.py:11(broadcast_all)
               57153750   75.678    0.000 1289.213    0.000 utils.py:82(probs_to_logits)
              172032787 1283.093    0.000 1283.093    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
             9232686385 1255.864    0.000 1274.697    0.000 {built-in method builtins.len}
               25147650 1273.093    0.000 1273.093    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
              171461250 1251.548    0.000 1251.548    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 571537  963.815    0.002 1194.781    0.002 replaybuffer.py:42(sample_option_critic)
             8667663954 1089.337    0.000 1089.337    0.000 {method 'values' of 'collections.OrderedDict' objects}
              171461250 1088.395    0.000 1088.395    0.000 {method 'all' of 'torch._C._TensorBase' objects}
               57153750  955.641    0.000  955.641    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
              114307500  876.470    0.000  876.470    0.000 {built-in method broadcast_tensors}
                2286150   85.775    0.000  761.134    0.000 replaybuffer.py:34(save_option_critic)
               57153750  160.570    0.000  752.510    0.000 utils.py:77(clamp_probs)
               57153750  138.377    0.000  735.167    0.000 layers.py:838(isFree)
               57153750  717.347    0.000  717.347    0.000 {built-in method bernoulli}
              173175861  685.523    0.000  685.523    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
                2286150  111.047    0.000  676.380    0.000 optimizer.py:189(zero_grad)
               57153750  630.932    0.000  630.932    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
               57513967  623.784    0.000  623.784    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
              404604066  488.401    0.000  596.791    0.000 layer.py:103(isFree)
               57153750  591.940    0.000  591.940    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
              344065574  560.364    0.000  560.364    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
              114307500  526.600    0.000  526.600    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               18289208  301.801    0.000  511.089    0.000 layer.py:175(NoRock_update)
               57153750  507.844    0.000  507.844    0.000 {built-in method clamp}
               57153750  461.024    0.000  461.024    0.000 {built-in method log}
              171461275  132.495    0.000  456.269    0.000 {built-in method builtins.all}
               57153750  446.208    0.000  446.208    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
              756225886  277.654    0.000  442.402    0.000 {built-in method builtins.isinstance}
               15431515  433.614    0.000  433.614    0.000 {built-in method tensor}
              177748176  407.641    0.000  407.641    0.000 {method 'to' of 'torch._C._TensorBase' objects}
               57153750  404.398    0.000  404.398    0.000 {built-in method all}
               57153750  369.095    0.000  369.095    0.000 {built-in method multinomial}
              171826063  345.810    0.000  345.810    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               32006094  345.517    0.000  345.517    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               32006094  336.271    0.000  336.271    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                6858454   13.144    0.000  327.503    0.000 game.py:38(board)
               56793534   75.030    0.000  308.847    0.000 {built-in method builtins.any}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9606112: <Attempt2_Lights1_option_critic_2> in cluster <dcc> Done

Job <Attempt2_Lights1_option_critic_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon May  3 01:33:07 2021
Job was executed on host(s) <n-62-31-4>, in queue <hpc>, as user <s183914> in cluster <dcc> at Mon May  3 01:33:08 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon May  3 01:33:08 2021
Terminated at Thu May  6 01:28:27 2021
Results reported at Thu May  6 01:28:27 2021

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

    CPU time :                                   258095.06 sec.
    Max Memory :                                 908 MB
    Average Memory :                             894.86 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15476.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258951 sec.
    Turnaround time :                            258920 sec.

The output (if any) is above this job summary.

