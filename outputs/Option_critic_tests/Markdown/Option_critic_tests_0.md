
# Parameters

    Name :                      Option_critic_tests-0
    Main :                      option_critic_run
    Level :                     Levels.Causal1
    Failed actions chance :     0.0
    Hours :                     0.1
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
    Minutes used :              1 minutes.
    Hours used :                0 hours.

# Profiling


      10439648 function calls (10092809 primitive calls) in 60.81 seconds

##    Ordered by: cumulative time
   List reduced from 428 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000   60.813   60.813 {built-in method builtins.exec}
                      1    0.034    0.034   60.813   60.813 <string>:1(<module>)
                      1    1.617    1.617   60.779   60.779 optionCritic.py:195(option_critic_run)
                  12700    2.526    0.000   28.255    0.002 optionCritic.py:143(actor_loss_fn)
          460819/114787    2.456    0.000   26.700    0.000 module.py:866(_call_impl)
                  38448    0.187    0.000   24.751    0.001 optionCritic.py:70(get_state)
                  38448    0.556    0.000   23.975    0.001 container.py:117(forward)
                    127    0.001    0.000   17.414    0.137 tensor.py:195(backward)
                    127    0.002    0.000   17.413    0.137 __init__.py:68(backward)
                    127   17.407    0.137   17.407    0.137 {method 'run_backward' of 'torch._C._EngineBase' objects}
                  76896    0.216    0.000   14.811    0.000 conv.py:398(forward)
                  76896    0.129    0.000   14.499    0.000 conv.py:390(_conv_forward)
                  76896   14.370    0.000   14.370    0.000 {built-in method conv2d}
                  12700    0.938    0.000    5.363    0.000 optionCritic.py:91(get_action)
                 153235    0.410    0.000    5.361    0.000 linear.py:93(forward)
                 153235    0.158    0.000    4.765    0.000 functional.py:1737(linear)
                 153235    4.569    0.000    4.569    0.000 {built-in method torch._C._nn.linear}
                  12700    0.326    0.000    3.984    0.000 optionCritic.py:80(predict_option_termination)
                  25400    0.346    0.000    2.174    0.000 distribution.py:34(__init__)
                  12700    0.143    0.000    1.788    0.000 categorical.py:115(log_prob)
                 115344    0.132    0.000    1.745    0.000 activation.py:713(forward)
                  12700    0.149    0.000    1.740    0.000 bernoulli.py:34(__init__)
                 115344    0.135    0.000    1.613    0.000 functional.py:1364(leaky_relu)
                  12700    0.189    0.000    1.454    0.000 categorical.py:49(__init__)
                 115344    1.449    0.000    1.449    0.000 {built-in method torch._C._nn.leaky_relu}
                  38208    0.089    0.000    1.364    0.000 optionCritic.py:77(get_Q)
                  25431    0.103    0.000    1.140    0.000 optionCritic.py:88(get_terminations)
                  12700    0.604    0.000    0.892    0.000 constraints.py:398(check)
                  12700    0.118    0.000    0.692    0.000 distribution.py:240(_validate_sample)
                  12700    0.120    0.000    0.613    0.000 bernoulli.py:86(sample)
                  12700    0.610    0.000    0.610    0.000 constraints.py:364(check)
                    127    0.001    0.000    0.529    0.004 game.py:41(step)
                  12471    0.237    0.000    0.514    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                    127    0.001    0.000    0.514    0.004 layers.py:718(step)
                  38100    0.055    0.000    0.511    0.000 utils.py:106(__get__)
                  38448    0.054    0.000    0.505    0.000 activation.py:101(forward)
                  12700    0.249    0.000    0.480    0.000 categorical.py:123(entropy)
                 600522    0.472    0.000    0.472    0.000 module.py:934(__getattr__)
                  88900    0.464    0.000    0.464    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                  38448    0.049    0.000    0.452    0.000 functional.py:1195(relu)
                  12700    0.446    0.000    0.446    0.000 constraints.py:249(check)
                  38162    0.056    0.000    0.442    0.000 tensor.py:525(__rsub__)
                  25400    0.154    0.000    0.438    0.000 functional.py:46(broadcast_tensors)
                  12700    0.099    0.000    0.421    0.000 utils.py:11(broadcast_all)
                  12700    0.016    0.000    0.409    0.000 categorical.py:88(logits)
                  38448    0.042    0.000    0.403    0.000 flatten.py:39(forward)
                  38448    0.395    0.000    0.395    0.000 {built-in method relu}
                  12700    0.017    0.000    0.392    0.000 utils.py:82(probs_to_logits)
                  38162    0.379    0.000    0.379    0.000 {built-in method rsub}
                  38448    0.360    0.000    0.360    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                  25431    0.359    0.000    0.359    0.000 {method 'max' of 'torch._C._TensorBase' objects}
                   1397    0.005    0.000    0.348    0.000 tensor.py:575(__iter__)
                     31    0.006    0.000    0.346    0.011 optionCritic.py:116(critic_loss_fn)
                   1397    0.339    0.000    0.339    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
                  12700    0.089    0.000    0.339    0.000 categorical.py:108(sample)
                  38131    0.337    0.000    0.337    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
                 462216    0.314    0.000    0.314    0.000 {built-in method torch._C._get_tracing_state}
                    127    0.015    0.000    0.311    0.002 layers.py:17(step)
                  38100    0.305    0.000    0.305    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                  12700    0.028    0.000    0.295    0.000 layer.py:98(move)
                  38100    0.287    0.000    0.287    0.000 {method 'all' of 'torch._C._TensorBase' objects}
                1974304    0.284    0.000    0.285    0.000 {built-in method builtins.len}
                  12700    0.282    0.000    0.282    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
                  12471    0.017    0.000    0.277    0.000 <__array_function__ internals>:2(prod)
                  12471    0.016    0.000    0.257    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                    128    0.025    0.000    0.251    0.002 layers.py:684(update)
                  25400    0.242    0.000    0.242    0.000 {built-in method broadcast_tensors}
                  12471    0.025    0.000    0.241    0.000 fromnumeric.py:2912(prod)
                    127    0.019    0.000    0.230    0.002 replaybuffer.py:34(save_option_critic)
                1881724    0.229    0.000    0.229    0.000 {method 'values' of 'collections.OrderedDict' objects}
                  12471    0.061    0.000    0.216    0.000 fromnumeric.py:70(_wrapreduction)
                  12700    0.205    0.000    0.205    0.000 {built-in method bernoulli}
                  12700    0.201    0.000    0.201    0.000 {built-in method log}
                  12700    0.035    0.000    0.174    0.000 utils.py:77(clamp_probs)
                  38193    0.169    0.000    0.169    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
                    127    0.004    0.000    0.158    0.001 optimizer.py:84(wrapper)
                  12700    0.046    0.000    0.152    0.000 layers.py:735(check)
                  12746    0.149    0.000    0.149    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                  12700    0.146    0.000    0.146    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
                    127    0.002    0.000    0.144    0.001 grad_mode.py:24(decorate_context)
                  76262    0.142    0.000    0.142    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                 166671    0.088    0.000    0.141    0.000 {built-in method builtins.isinstance}
                  12700    0.140    0.000    0.140    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
                    127    0.008    0.000    0.139    0.001 rmsprop.py:56(step)
                  12471    0.130    0.000    0.130    0.000 {method 'reduce' of 'numpy.ufunc' objects}
                  25400    0.127    0.000    0.127    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                  12700    0.124    0.000    0.124    0.000 {built-in method clamp}
                    127    0.008    0.000    0.121    0.001 _functional.py:203(rmsprop)
                  12700    0.107    0.000    0.107    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
                  12700    0.097    0.000    0.097    0.000 {built-in method all}
                  12700    0.092    0.000    0.092    0.000 {built-in method multinomial}
                  12700    0.022    0.000    0.088    0.000 layers.py:729(isFree)
                  38462    0.088    0.000    0.088    0.000 {method 'to' of 'torch._C._TensorBase' objects}
                  38245    0.086    0.000    0.086    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                  12853    0.041    0.000    0.085    0.000 grad_mode.py:119(__enter__)
                  38200    0.031    0.000    0.078    0.000 {built-in method builtins.all}
                  25400    0.071    0.000    0.074    0.000 distribution.py:226(_extended_shape)
                  89247    0.065    0.000    0.073    0.000 {built-in method builtins.getattr}
                    768    0.041    0.000    0.071    0.000 layer.py:167(NoRock_update)
                    145    0.002    0.000    0.069    0.000 layers.py:740(restart)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9601821: <Option_critic_tests_0> in cluster <dcc> Done

Job <Option_critic_tests_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Thu Apr 29 21:06:50 2021
Job was executed on host(s) <n-62-31-23>, in queue <hpc>, as user <s183914> in cluster <dcc> at Thu Apr 29 21:06:53 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Apr 29 21:06:53 2021
Terminated at Thu Apr 29 21:07:57 2021
Results reported at Thu Apr 29 21:07:57 2021

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

    CPU time :                                   61.63 sec.
    Max Memory :                                 130 MB
    Average Memory :                             130.00 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               16254.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   69 sec.
    Turnaround time :                            67 sec.

The output (if any) is above this job summary.

