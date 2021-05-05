[W NNPACK.cpp:80] Could not initialize NNPACK! Reason: Unsupported hardware.

# Parameters

    Name :                      Coconuts_option_critic-2
    Main :                      option_critic_run
    Level :                     Levels.Coconuts
    Failed actions chance :     0.0
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


      33406105646 function calls (32364514146 primitive calls) in 258900.53 seconds

##    Ordered by: cumulative time
   List reduced from 437 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.534 258900.534 {built-in method builtins.exec}
                      1    0.311    0.311 258900.533 258900.533 <string>:1(<module>)
                      1 3810.481 3810.481 258900.223 258900.223 optionCritic.py:195(option_critic_run)
        1375825566/339050073 10291.713    0.000 106071.316    0.000 module.py:866(_call_impl)
               37040925 9926.788    0.000 104945.776    0.003 optionCritic.py:143(actor_loss_fn)
              115197277  748.487    0.000 96958.787    0.001 optionCritic.py:70(get_state)
              115197277 2764.224    0.000 93885.022    0.001 container.py:117(forward)
                1481637   11.466    0.000 79452.797    0.054 tensor.py:195(backward)
                1481637   13.540    0.000 79441.051    0.054 __init__.py:68(backward)
                1481637 79390.793    0.054 79390.793    0.054 {method 'run_backward' of 'torch._C._EngineBase' objects}
              230394554  876.635    0.000 55970.635    0.000 conv.py:398(forward)
              230394554  376.132    0.000 54768.747    0.000 conv.py:390(_conv_forward)
              230394554 54392.616    0.000 54392.616    0.000 {built-in method conv2d}
               37040925 3884.856    0.000 23009.676    0.001 optionCritic.py:91(get_action)
              454247350 1567.754    0.000 21473.148    0.000 linear.py:93(forward)
              454247350  555.525    0.000 19314.996    0.000 functional.py:1737(linear)
              454247350 18642.736    0.000 18642.736    0.000 {built-in method torch._C._nn.linear}
               37040925 1182.939    0.000 12857.511    0.000 optionCritic.py:80(predict_option_termination)
                1481637   34.583    0.000 11521.065    0.008 optimizer.py:84(wrapper)
                1481637   17.178    0.000 11391.345    0.008 grad_mode.py:24(decorate_context)
                1481637  107.502    0.000 11342.069    0.008 rmsprop.py:56(step)
                1481637  155.937    0.000 11121.052    0.008 _functional.py:203(rmsprop)
               20742912 8732.901    0.000 8732.901    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               74081850 1091.287    0.000 8436.937    0.000 distribution.py:34(__init__)
              345591831  412.969    0.000 7946.571    0.000 activation.py:713(forward)
              345591831  430.884    0.000 7533.602    0.000 functional.py:1364(leaky_relu)
               37040925  604.174    0.000 7525.284    0.000 categorical.py:115(log_prob)
              345591831 7014.505    0.000 7014.505    0.000 {built-in method torch._C._nn.leaky_relu}
               37040925  872.044    0.000 6802.103    0.000 categorical.py:49(__init__)
              112359612  447.658    0.000 6334.720    0.000 optionCritic.py:77(get_Q)
                 370409   84.845    0.000 6045.275    0.016 optionCritic.py:116(critic_loss_fn)
               74452259  444.084    0.000 5130.044    0.000 optionCritic.py:88(get_terminations)
               37040925  284.446    0.000 4533.870    0.000 bernoulli.py:34(__init__)
               37040925 2816.898    0.000 4243.101    0.000 constraints.py:398(check)
                1481637    8.632    0.000 3726.046    0.003 game.py:41(step)
                1481637   13.619    0.000 3613.022    0.002 layers.py:718(step)
               37040925  469.625    0.000 3193.805    0.000 distribution.py:240(_validate_sample)
              115197277  158.559    0.000 2248.896    0.000 activation.py:101(forward)
               37040925 1081.538    0.000 2229.719    0.000 categorical.py:123(entropy)
                1481637   67.362    0.000 2170.177    0.001 layers.py:17(step)
               37040925 2157.181    0.000 2157.181    0.000 constraints.py:249(check)
               37040925  219.258    0.000 2097.692    0.000 layer.py:98(move)
              115197277  144.327    0.000 2090.337    0.000 functional.py:1195(relu)
               37040925 2025.377    0.000 2025.377    0.000 constraints.py:364(check)
              115197277 1918.503    0.000 1918.503    0.000 {built-in method relu}
              111122775  219.496    0.000 1844.287    0.000 utils.py:106(__get__)
             1392123573 1829.489    0.000 1829.489    0.000 {built-in method torch._C._get_tracing_state}
              259286475 1794.172    0.000 1794.172    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               37040925  307.716    0.000 1730.562    0.000 bernoulli.py:86(sample)
              111863593  181.059    0.000 1668.926    0.000 tensor.py:525(__rsub__)
              111122775 1590.404    0.000 1590.404    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
              115197277  105.877    0.000 1561.197    0.000 flatten.py:39(forward)
             1782608412 1560.250    0.000 1560.402    0.000 module.py:934(__getattr__)
              111493184 1465.296    0.000 1465.296    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
               37040925   73.003    0.000 1459.552    0.000 categorical.py:88(logits)
              111863593 1456.822    0.000 1456.822    0.000 {built-in method rsub}
              115197277 1455.321    0.000 1455.321    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               37040925  375.071    0.000 1438.062    0.000 categorical.py:108(sample)
               37040925  232.811    0.000 1435.121    0.000 layers.py:735(check)
                1481638  139.870    0.000 1423.256    0.001 layers.py:684(update)
               37040925   75.249    0.000 1386.549    0.000 utils.py:82(probs_to_logits)
               74081850  386.634    0.000 1221.459    0.000 functional.py:46(broadcast_tensors)
               74452259 1187.603    0.000 1187.603    0.000 {method 'max' of 'torch._C._TensorBase' objects}
              111122775 1099.485    0.000 1099.485    0.000 {method 'all' of 'torch._C._TensorBase' objects}
             5943508161 1058.222    0.000 1071.399    0.000 {built-in method builtins.len}
               16298007   45.622    0.000 1038.854    0.000 tensor.py:575(__iter__)
               16298007  958.741    0.000  958.741    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               20742912  952.077    0.000  952.077    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
             5618499541  876.667    0.000  876.667    0.000 {method 'values' of 'collections.OrderedDict' objects}
               37040925  173.082    0.000  856.765    0.000 utils.py:11(broadcast_all)
               37040925  132.045    0.000  839.595    0.000 utils.py:77(clamp_probs)
               37040925  805.504    0.000  805.504    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               74081850  732.554    0.000  732.554    0.000 {built-in method broadcast_tensors}
              112234002  714.267    0.000  714.267    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
                1481637   74.166    0.000  707.692    0.000 replaybuffer.py:34(save_option_critic)
               37040925  707.550    0.000  707.550    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
                 370409  522.547    0.001  680.289    0.002 replaybuffer.py:42(sample_option_critic)
               37040925  675.860    0.000  675.860    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
               12755366  322.291    0.000  674.877    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               37040925  625.366    0.000  625.366    0.000 {built-in method clamp}
              222986368  610.042    0.000  610.042    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               74081850  598.057    0.000  598.057    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               37536944  584.200    0.000  584.200    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                 496043    9.499    0.000  548.935    0.001 layers.py:740(restart)
               37040925  537.711    0.000  537.711    0.000 {built-in method bernoulli}
               20742912  477.690    0.000  477.690    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               37040925  477.060    0.000  477.060    0.000 {built-in method all}
               37040925  471.705    0.000  471.705    0.000 {built-in method log}
                1481637   90.549    0.000  468.238    0.000 optimizer.py:189(zero_grad)
                 496043    4.599    0.000  462.437    0.001 level.py:8(__init__)
               37040925  459.174    0.000  459.174    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
               37040925  326.337    0.000  438.087    0.000 layers.py:471(check)
                 496043   33.415    0.000  430.045    0.001 levels.py:262(generate)
               20742912  421.312    0.000  421.312    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               10371466  273.637    0.000  413.981    0.000 layer.py:151(update)
               37040925  291.967    0.000  384.023    0.000 layers.py:77(check)
               20742912  381.136    0.000  381.136    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                4424670   56.517    0.000  371.455    0.000 level.py:41(notUsed)
               12755366   20.148    0.000  352.586    0.000 <__array_function__ internals>:2(prod)
               37040925  341.075    0.000  341.075    0.000 {built-in method multinomial}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9601883: <Coconuts_option_critic_2> in cluster <dcc> Done

Job <Coconuts_option_critic_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Thu Apr 29 21:41:22 2021
Job was executed on host(s) <n-62-23-21>, in queue <hpc>, as user <s183914> in cluster <dcc> at Thu Apr 29 21:41:24 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Apr 29 21:41:24 2021
Terminated at Sun May  2 21:36:27 2021
Results reported at Sun May  2 21:36:27 2021

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

python main.py $LSB_PROJECT_NAME
------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   258873.59 sec.
    Max Memory :                                 872 MB
    Average Memory :                             861.21 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15512.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258963 sec.
    Turnaround time :                            258905 sec.

The output (if any) is above this job summary.

