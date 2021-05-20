[W NNPACK.cpp:80] Could not initialize NNPACK! Reason: Unsupported hardware.

# Parameters

    Name :                      Attempt8_Lights2_option_critic-2
    Main :                      option_critic_run
    Level :                     Levels.Causal4
    Failed actions chance :     0
    Use model :                 True
    Depth :                     3
    Model explore :             1000000
    Samples :                   5
    Hours :                     72.0
    Batch :                     32
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
    Num :                       2
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              4315 minutes.
    Hours used :                71 hours.

# Profiling


      33578647799 function calls (32570001591 primitive calls) in 258901.09 seconds

##    Ordered by: cumulative time
   List reduced from 438 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258901.093 258901.093 {built-in method builtins.exec}
                      1    0.353    0.353 258901.093 258901.093 <string>:1(<module>)
                      1 3745.302 3745.302 258900.740 258900.740 optionCritic.py:195(option_critic_run)
        1336275841/331304890 9462.717    0.000 119847.587    0.000 module.py:866(_call_impl)
               36184608 8485.373    0.000 113555.887    0.003 optionCritic.py:143(actor_loss_fn)
              111663439  713.404    0.000 111020.530    0.001 optionCritic.py:70(get_state)
              111663439 2540.452    0.000 108128.754    0.001 container.py:117(forward)
              223326878  863.846    0.000 72869.085    0.000 conv.py:398(forward)
              223326878  354.996    0.000 71697.223    0.000 conv.py:390(_conv_forward)
              223326878 71342.226    0.000 71342.226    0.000 {built-in method conv2d}
                1130769    8.999    0.000 64574.274    0.057 tensor.py:195(backward)
                1130769   10.149    0.000 64565.058    0.057 __init__.py:68(backward)
                1130769 64527.174    0.057 64527.174    0.057 {method 'run_backward' of 'torch._C._EngineBase' objects}
               36184608 3664.769    0.000 21852.402    0.001 optionCritic.py:91(get_action)
              442968329 1524.341    0.000 20031.559    0.000 linear.py:93(forward)
              442968329  544.925    0.000 17943.478    0.000 functional.py:1737(linear)
              442968329 17291.864    0.000 17291.864    0.000 {built-in method torch._C._nn.linear}
                1130769   23.918    0.000 16815.527    0.015 optimizer.py:84(wrapper)
                1130769   13.200    0.000 16715.852    0.015 grad_mode.py:24(decorate_context)
                1130769   75.340    0.000 16679.169    0.015 rmsprop.py:56(step)
                1130769  122.019    0.000 16517.924    0.015 _functional.py:203(rmsprop)
               15830760 14381.575    0.001 14381.575    0.001 {method 'sqrt' of 'torch._C._TensorBase' objects}
               36184608 1115.109    0.000 11963.762    0.000 optionCritic.py:80(predict_option_termination)
               72369216  999.131    0.000 7906.432    0.000 distribution.py:34(__init__)
              334990317  414.568    0.000 7652.618    0.000 activation.py:713(forward)
              334990317  407.903    0.000 7238.050    0.000 functional.py:1364(leaky_relu)
               36184608  579.174    0.000 7166.323    0.000 categorical.py:115(log_prob)
              334990317 6745.189    0.000 6745.189    0.000 {built-in method torch._C._nn.leaky_relu}
                 282692   63.910    0.000 6678.466    0.024 optionCritic.py:116(critic_loss_fn)
               36184608  835.582    0.000 6420.245    0.000 categorical.py:49(__init__)
              110804935  444.473    0.000 6140.033    0.000 optionCritic.py:77(get_Q)
               72651908  426.067    0.000 4917.686    0.000 optionCritic.py:88(get_terminations)
               36184608  243.505    0.000 4154.961    0.000 bernoulli.py:34(__init__)
               36184608 2649.922    0.000 4002.113    0.000 constraints.py:398(check)
                1130769    7.193    0.000 3975.807    0.004 game.py:42(step)
                1130769   11.878    0.000 3881.350    0.003 layers.py:827(step)
               36184608  446.018    0.000 3012.502    0.000 distribution.py:240(_validate_sample)
              111663439  153.352    0.000 2173.294    0.000 activation.py:101(forward)
               36184608 1036.812    0.000 2120.196    0.000 categorical.py:123(entropy)
               36184608 2031.812    0.000 2031.812    0.000 constraints.py:249(check)
              111663439  135.694    0.000 2019.942    0.000 functional.py:1195(relu)
                1130769   58.834    0.000 1974.291    0.002 layers.py:17(step)
               36184608  146.305    0.000 1910.836    0.000 layer.py:106(move)
               36184608 1899.391    0.000 1899.391    0.000 constraints.py:364(check)
                1130770  126.165    0.000 1889.603    0.002 layers.py:793(update)
              111663439 1857.945    0.000 1857.945    0.000 {built-in method relu}
             1348714300 1767.547    0.000 1767.547    0.000 {built-in method torch._C._get_tracing_state}
              108553824  192.381    0.000 1754.628    0.000 utils.py:106(__get__)
              253292256 1663.034    0.000 1663.034    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              109119208  164.853    0.000 1569.264    0.000 tensor.py:525(__rsub__)
               36184608  264.566    0.000 1535.120    0.000 bernoulli.py:86(sample)
              111663439  120.546    0.000 1504.368    0.000 flatten.py:39(forward)
              108553824 1496.365    0.000 1496.365    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
             1736411571 1489.827    0.000 1489.941    0.000 module.py:934(__getattr__)
               36184608   68.559    0.000 1410.481    0.000 categorical.py:88(logits)
              111663439 1383.822    0.000 1383.822    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              108836516 1383.072    0.000 1383.072    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
              109119208 1374.637    0.000 1374.637    0.000 {built-in method rsub}
               36184608  348.505    0.000 1360.944    0.000 categorical.py:108(sample)
               36184608  275.058    0.000 1344.795    0.000 layers.py:844(check)
               36184608   71.563    0.000 1341.922    0.000 utils.py:82(probs_to_logits)
               15830760 1195.928    0.000 1195.928    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               72369216  358.061    0.000 1142.853    0.000 functional.py:46(broadcast_tensors)
               72651908 1139.566    0.000 1139.566    0.000 {method 'max' of 'torch._C._TensorBase' objects}
              108553824 1032.772    0.000 1032.772    0.000 {method 'all' of 'torch._C._TensorBase' objects}
             5875457362  992.112    0.000 1002.639    0.000 {built-in method builtins.len}
                1685760   32.807    0.000  916.941    0.001 layers.py:849(restart)
               12438459   34.447    0.000  891.414    0.000 tensor.py:575(__iter__)
               36184608  129.151    0.000  831.643    0.000 utils.py:77(clamp_probs)
               12438459  830.715    0.000  830.715    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               36184608  805.688    0.000  805.688    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
             5456766803  799.031    0.000  799.031    0.000 {method 'values' of 'collections.OrderedDict' objects}
               36184608  158.312    0.000  781.071    0.000 utils.py:11(broadcast_all)
               36184608  702.492    0.000  702.492    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
              109401900  692.254    0.000  692.254    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               72369216  689.139    0.000  689.139    0.000 {built-in method broadcast_tensors}
                1130769   68.991    0.000  670.403    0.001 replaybuffer.py:34(save_option_critic)
                1685760   13.464    0.000  653.980    0.000 level.py:8(__init__)
               36184608  653.859    0.000  653.859    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
              217673032  610.258    0.000  610.258    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               11734056  285.257    0.000  602.565    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               36184608  591.576    0.000  591.576    0.000 {built-in method clamp}
               37870335  569.091    0.000  569.091    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               72369216  566.429    0.000  566.429    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               11307700  373.298    0.000  557.431    0.000 layer.py:159(update)
                1685760   84.801    0.000  540.890    0.000 levels.py:199(generate)
                 282692  387.680    0.001  508.531    0.002 replaybuffer.py:42(sample_option_critic)
               36184608  500.795    0.000  500.795    0.000 {built-in method bernoulli}
               36184608  452.217    0.000  452.217    0.000 {built-in method all}
               36184608  438.715    0.000  438.715    0.000 {built-in method log}
               36184608  436.732    0.000  436.732    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
                3371520   40.814    0.000  373.110    0.000 level.py:41(notUsed)
                1130769   68.447    0.000  366.653    0.000 optimizer.py:189(zero_grad)
               36184608   77.252    0.000  345.314    0.000 layers.py:838(isFree)
              927232784  226.106    0.000  328.172    0.000 enum.py:646(__hash__)
               36184608  327.177    0.000  327.177    0.000 {built-in method multinomial}
               11734056   19.180    0.000  317.308    0.000 <__array_function__ internals>:2(prod)
               11734056   17.760    0.000  293.882    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
              110241842  291.000    0.000  291.000    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               15830760  289.172    0.000  289.172    0.000 {method 'add_' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9632923: <Attempt8_Lights2_option_critic_2> in cluster <dcc> Done

Job <Attempt8_Lights2_option_critic_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed May 12 15:36:14 2021
Job was executed on host(s) <n-62-23-24>, in queue <hpc>, as user <s183914> in cluster <dcc> at Sun May 16 23:16:53 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun May 16 23:16:53 2021
Terminated at Wed May 19 23:12:23 2021
Results reported at Wed May 19 23:12:23 2021

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

    CPU time :                                   258888.59 sec.
    Max Memory :                                 1092 MB
    Average Memory :                             1080.51 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15292.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   259038 sec.
    Turnaround time :                            632169 sec.

The output (if any) is above this job summary.

