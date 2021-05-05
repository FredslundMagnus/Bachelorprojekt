
# Parameters

    Name :                      Lights1_option_critic-1
    Main :                      option_critic_run
    Level :                     Levels.Causal3
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


      51014088812 function calls (49381084743 primitive calls) in 258900.39 seconds

##    Ordered by: cumulative time
   List reduced from 434 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.393 258900.393 {built-in method builtins.exec}
                      1    0.308    0.308 258900.392 258900.392 <string>:1(<module>)
                      1 5760.322 5760.322 258900.085 258900.085 optionCritic.py:195(option_critic_run)
               58072675 9562.683    0.000 114501.103    0.002 optionCritic.py:143(actor_loss_fn)
        2156734747/531280585 10667.791    0.000 113394.039    0.000 module.py:866(_call_impl)
              180606018  835.220    0.000 105281.713    0.001 optionCritic.py:70(get_state)
              180606018 2320.074    0.000 101852.138    0.001 container.py:117(forward)
                2322907   19.345    0.000 74832.724    0.032 tensor.py:195(backward)
                2322907   24.852    0.000 74813.027    0.032 __init__.py:68(backward)
                2322907 74734.894    0.032 74734.894    0.032 {method 'run_backward' of 'torch._C._EngineBase' objects}
              361212036  990.071    0.000 64239.644    0.000 conv.py:398(forward)
              361212036  564.720    0.000 62821.665    0.000 conv.py:390(_conv_forward)
              361212036 62256.945    0.000 62256.945    0.000 {built-in method conv2d}
               58072675 3839.945    0.000 22678.004    0.000 optionCritic.py:91(get_action)
              711886603 1733.255    0.000 20961.983    0.000 linear.py:93(forward)
              711886603  673.879    0.000 18480.163    0.000 functional.py:1737(linear)
              711886603 17640.557    0.000 17640.557    0.000 {built-in method torch._C._nn.linear}
               58072675 1231.671    0.000 14730.295    0.000 optionCritic.py:80(predict_option_termination)
              116145350 1318.902    0.000 8594.169    0.000 distribution.py:34(__init__)
               58072675  654.191    0.000 7536.890    0.000 categorical.py:115(log_prob)
              541818054  527.930    0.000 7522.087    0.000 activation.py:713(forward)
              541818054  564.307    0.000 6994.157    0.000 functional.py:1364(leaky_relu)
               58072675  838.872    0.000 6373.689    0.000 categorical.py:49(__init__)
              541818054 6309.330    0.000 6309.330    0.000 {built-in method torch._C._nn.leaky_relu}
              175875816  413.138    0.000 5917.058    0.000 optionCritic.py:77(get_Q)
               58072675  459.871    0.000 5728.766    0.000 bernoulli.py:34(__init__)
                 580726   92.726    0.000 4848.144    0.008 optionCritic.py:116(critic_loss_fn)
              116726076  423.341    0.000 4627.050    0.000 optionCritic.py:88(get_terminations)
                2322907   11.127    0.000 4220.741    0.002 game.py:41(step)
                2322907   22.171    0.000 4078.970    0.002 layers.py:718(step)
               58072675 2602.625    0.000 3868.695    0.000 constraints.py:398(check)
                2322907   53.009    0.000 3635.532    0.002 optimizer.py:84(wrapper)
                2322907   26.048    0.000 3440.705    0.001 grad_mode.py:24(decorate_context)
                2322907  140.813    0.000 3364.038    0.001 rmsprop.py:56(step)
                2322907  133.018    0.000 3058.583    0.001 _functional.py:203(rmsprop)
               58072675  527.024    0.000 3041.886    0.000 distribution.py:240(_validate_sample)
                2322907   87.846    0.000 2502.470    0.001 layers.py:17(step)
               58072675  154.807    0.000 2405.947    0.000 layer.py:98(move)
               58072675  440.011    0.000 2182.462    0.000 bernoulli.py:86(sample)
               58072675 2176.783    0.000 2176.783    0.000 constraints.py:364(check)
              180606018  230.777    0.000 2170.829    0.000 activation.py:101(forward)
               58072675 1086.533    0.000 2092.575    0.000 categorical.py:123(entropy)
             2793925250 1980.822    0.000 1980.998    0.000 module.py:934(__getattr__)
               58072675 1961.855    0.000 1961.855    0.000 constraints.py:249(check)
              180606018  206.277    0.000 1940.052    0.000 functional.py:1195(relu)
              174218025  259.700    0.000 1889.128    0.000 utils.py:106(__get__)
              406508725 1818.668    0.000 1818.668    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              180606018 1701.520    0.000 1701.520    0.000 {built-in method relu}
              180606018  167.879    0.000 1673.312    0.000 flatten.py:39(forward)
              116145350  567.442    0.000 1620.280    0.000 functional.py:46(broadcast_tensors)
              175379477  197.075    0.000 1616.432    0.000 tensor.py:525(__rsub__)
                2322908  187.719    0.000 1546.017    0.001 layers.py:684(update)
              180606018 1505.434    0.000 1505.434    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               58072675  406.151    0.000 1468.127    0.000 categorical.py:108(sample)
               58072675   72.648    0.000 1430.719    0.000 categorical.py:88(logits)
             2182286724 1418.667    0.000 1418.667    0.000 {built-in method torch._C._get_tracing_state}
               58072675  305.766    0.000 1402.885    0.000 layers.py:735(check)
              175379477 1387.119    0.000 1387.119    0.000 {built-in method rsub}
               25551977   61.021    0.000 1362.513    0.000 tensor.py:575(__iter__)
               58072675   81.108    0.000 1358.071    0.000 utils.py:82(probs_to_logits)
              174798751 1327.579    0.000 1327.579    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
              174218025 1325.387    0.000 1325.387    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
               58072675  263.516    0.000 1308.562    0.000 utils.py:11(broadcast_all)
             9385391713 1282.369    0.000 1299.886    0.000 {built-in method builtins.len}
              116726076 1297.654    0.000 1297.654    0.000 {method 'max' of 'torch._C._TensorBase' objects}
               25551977 1261.903    0.000 1261.903    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
                 580726 1000.159    0.002 1231.037    0.002 replaybuffer.py:42(sample_option_critic)
              174218025 1067.643    0.000 1067.643    0.000 {method 'all' of 'torch._C._TensorBase' objects}
             8807545006 1037.402    0.000 1037.402    0.000 {method 'values' of 'collections.OrderedDict' objects}
               58072675  999.853    0.000  999.853    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               32520692  923.292    0.000  923.292    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              116145350  859.782    0.000  859.782    0.000 {built-in method broadcast_tensors}
               15725512  391.142    0.000  832.038    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               58072675  165.460    0.000  806.793    0.000 utils.py:77(clamp_probs)
                2322907   90.452    0.000  765.546    0.000 replaybuffer.py:34(save_option_critic)
               32520692  758.439    0.000  758.439    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               58072675  123.623    0.000  709.562    0.000 layers.py:729(isFree)
              175960203  699.898    0.000  699.898    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
                2322907  114.989    0.000  679.460    0.000 optimizer.py:189(zero_grad)
               58072675  676.722    0.000  676.722    0.000 {built-in method bernoulli}
               58072675  641.333    0.000  641.333    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
               58072675  638.071    0.000  638.071    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
               58569014  590.778    0.000  590.778    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
              383527855  490.293    0.000  585.939    0.000 layer.py:95(isFree)
              349597502  567.166    0.000  567.166    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
              116145350  548.513    0.000  548.513    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               58072675  536.494    0.000  536.494    0.000 {built-in method clamp}
               18583264  312.472    0.000  527.472    0.000 layer.py:167(NoRock_update)
               32520692  495.510    0.000  495.510    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               58072675  470.170    0.000  470.170    0.000 {built-in method log}
               32520692  460.436    0.000  460.436    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               58072675  451.587    0.000  451.587    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
               15725512   27.335    0.000  440.897    0.000 <__array_function__ internals>:2(prod)
               15679624  438.880    0.000  438.880    0.000 {built-in method tensor}
               58072675  435.553    0.000  435.553    0.000 {built-in method all}
              768905864  275.664    0.000  416.638    0.000 {built-in method builtins.isinstance}
              174218050  120.704    0.000  414.597    0.000 {built-in method builtins.all}
               15725512   26.471    0.000  408.630    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
               15725512   38.520    0.000  382.159    0.000 fromnumeric.py:2912(prod)
              180606032  380.203    0.000  380.203    0.000 {method 'to' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9601852: <Lights1_option_critic_1> in cluster <dcc> Done

Job <Lights1_option_critic_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Thu Apr 29 21:41:02 2021
Job was executed on host(s) <n-62-31-1>, in queue <hpc>, as user <s183914> in cluster <dcc> at Thu Apr 29 21:41:04 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Apr 29 21:41:04 2021
Terminated at Sun May  2 21:36:07 2021
Results reported at Sun May  2 21:36:07 2021

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

    CPU time :                                   258289.86 sec.
    Max Memory :                                 904 MB
    Average Memory :                             887.72 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15480.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258996 sec.
    Turnaround time :                            258905 sec.

The output (if any) is above this job summary.

