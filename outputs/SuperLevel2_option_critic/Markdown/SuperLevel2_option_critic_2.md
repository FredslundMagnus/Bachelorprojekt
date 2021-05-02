[W NNPACK.cpp:80] Could not initialize NNPACK! Reason: Unsupported hardware.

# Parameters

    Name :                      SuperLevel2_option_critic-2
    Main :                      option_critic_run
    Level :                     Levels.SuperLevel2
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


      30163932712 function calls (29266992728 primitive calls) in 258900.42 seconds

##    Ordered by: cumulative time
   List reduced from 439 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.417 258900.417 {built-in method builtins.exec}
                      1    0.321    0.321 258900.417 258900.417 <string>:1(<module>)
                      1 3373.301 3373.301 258900.096 258900.096 optionCritic.py:195(option_critic_run)
        1184702072/291909245 8777.618    0.000 111927.637    0.000 module.py:866(_call_impl)
               31896850 8578.468    0.000 105059.715    0.003 optionCritic.py:143(actor_loss_fn)
               99199203  656.799    0.000 103940.338    0.001 optionCritic.py:70(get_state)
               99199203 2366.077    0.000 101286.460    0.001 container.py:117(forward)
                1275874   10.480    0.000 86506.409    0.068 tensor.py:195(backward)
                1275874   13.002    0.000 86495.689    0.068 __init__.py:68(backward)
                1275874 86449.517    0.068 86449.517    0.068 {method 'run_backward' of 'torch._C._EngineBase' objects}
              198398406  779.528    0.000 68194.852    0.000 conv.py:398(forward)
              198398406  339.378    0.000 67124.207    0.000 conv.py:390(_conv_forward)
              198398406 66784.829    0.000 66784.829    0.000 {built-in method conv2d}
               31896850 3390.519    0.000 19903.326    0.001 optionCritic.py:91(get_action)
              391108448 1420.655    0.000 18881.295    0.000 linear.py:93(forward)
              391108448  518.253    0.000 16931.152    0.000 functional.py:1737(linear)
              391108448 16307.952    0.000 16307.952    0.000 {built-in method torch._C._nn.linear}
               31896850 1051.618    0.000 11226.279    0.000 optionCritic.py:80(predict_option_termination)
                 318968   74.075    0.000 7710.143    0.024 optionCritic.py:116(critic_loss_fn)
               63793700  961.586    0.000 7281.610    0.000 distribution.py:34(__init__)
              297597609  377.166    0.000 7043.202    0.000 activation.py:713(forward)
              297597609  396.100    0.000 6666.036    0.000 functional.py:1364(leaky_relu)
               31896850  527.355    0.000 6516.612    0.000 categorical.py:115(log_prob)
              297597609 6190.919    0.000 6190.919    0.000 {built-in method torch._C._nn.leaky_relu}
               31896850  761.655    0.000 5851.562    0.000 categorical.py:49(__init__)
                1275874   27.307    0.000 5793.035    0.005 optimizer.py:84(wrapper)
                1275874   13.483    0.000 5683.635    0.004 grad_mode.py:24(decorate_context)
                1275874   88.012    0.000 5642.524    0.004 rmsprop.py:56(step)
               96700524  392.672    0.000 5529.984    0.000 optionCritic.py:77(get_Q)
                1275874  137.226    0.000 5457.176    0.004 _functional.py:203(rmsprop)
               64112668  387.711    0.000 4477.546    0.000 optionCritic.py:88(get_terminations)
               31896850  255.901    0.000 3972.723    0.000 bernoulli.py:34(__init__)
                1275874    7.427    0.000 3890.432    0.003 game.py:41(step)
                1275874   11.772    0.000 3781.441    0.003 layers.py:718(step)
               31896850 2420.804    0.000 3636.946    0.000 constraints.py:398(check)
               17862230 3549.868    0.000 3549.868    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               31896850  404.552    0.000 2740.928    0.000 distribution.py:240(_validate_sample)
                1275874   57.828    0.000 2701.502    0.002 layers.py:17(step)
               31896850  178.463    0.000 2638.164    0.000 layer.py:98(move)
               99199203  145.199    0.000 1996.427    0.000 activation.py:101(forward)
               31896850  928.799    0.000 1914.899    0.000 categorical.py:123(entropy)
               31896850  288.050    0.000 1876.981    0.000 layers.py:735(check)
               99199203  135.526    0.000 1851.229    0.000 functional.py:1195(relu)
               31896850 1847.499    0.000 1847.499    0.000 constraints.py:249(check)
               31896850 1753.341    0.000 1753.341    0.000 constraints.py:364(check)
               99199203 1690.119    0.000 1690.119    0.000 {built-in method relu}
              223277950 1659.791    0.000 1659.791    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
             1198736686 1620.848    0.000 1620.848    0.000 {built-in method torch._C._get_tracing_state}
               95690550  190.904    0.000 1601.632    0.000 utils.py:106(__get__)
               31896850  271.861    0.000 1496.231    0.000 bernoulli.py:86(sample)
               96328486  161.983    0.000 1447.352    0.000 tensor.py:525(__rsub__)
             1534882580 1377.140    0.000 1377.269    0.000 module.py:934(__getattr__)
               99199203  104.255    0.000 1362.024    0.000 flatten.py:39(forward)
               95690550 1357.283    0.000 1357.283    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
               31896850   63.814    0.000 1265.538    0.000 categorical.py:88(logits)
               99199203 1257.769    0.000 1257.769    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               96328486 1256.404    0.000 1256.404    0.000 {built-in method rsub}
               96009518 1245.397    0.000 1245.397    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
               31896850  321.907    0.000 1240.217    0.000 categorical.py:108(sample)
               31896850   64.151    0.000 1201.724    0.000 utils.py:82(probs_to_logits)
               63793700  337.890    0.000 1073.235    0.000 functional.py:46(broadcast_tensors)
                1275875  121.088    0.000 1063.133    0.001 layers.py:684(update)
               64112668 1036.589    0.000 1036.589    0.000 {method 'max' of 'torch._C._TensorBase' objects}
               95690550  941.730    0.000  941.730    0.000 {method 'all' of 'torch._C._TensorBase' objects}
               14034614   39.340    0.000  926.173    0.000 tensor.py:575(__iter__)
             5253192528  887.752    0.000  899.160    0.000 {built-in method builtins.len}
               14034614  856.534    0.000  856.534    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
             4838007491  765.338    0.000  765.338    0.000 {method 'values' of 'collections.OrderedDict' objects}
               31896850  150.732    0.000  754.828    0.000 utils.py:11(broadcast_all)
               31896850  115.170    0.000  743.697    0.000 utils.py:77(clamp_probs)
               31896850  706.567    0.000  706.567    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               13011959  336.150    0.000  705.225    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               63793700  645.460    0.000  645.460    0.000 {built-in method broadcast_tensors}
               31896850  628.528    0.000  628.528    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
               96647454  617.995    0.000  617.995    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
                1275874   64.897    0.000  614.954    0.000 replaybuffer.py:34(save_option_critic)
               17862230  606.219    0.000  606.219    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                 318968  453.847    0.001  599.626    0.002 replaybuffer.py:42(sample_option_critic)
               31896850  593.910    0.000  593.910    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
              192019036  541.590    0.000  541.590    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               31896850  540.844    0.000  540.844    0.000 {built-in method clamp}
               63793700  513.439    0.000  513.439    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               32268888  510.435    0.000  510.435    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               31896850  110.271    0.000  482.562    0.000 layers.py:729(isFree)
               31896850  471.371    0.000  471.371    0.000 {built-in method bernoulli}
               14034625  287.675    0.000  456.730    0.000 layer.py:151(update)
               31896850  325.568    0.000  433.126    0.000 layers.py:471(check)
               17862230  429.849    0.000  429.849    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                1275874   78.455    0.000  426.752    0.000 optimizer.py:189(zero_grad)
               31896850  407.696    0.000  407.696    0.000 {built-in method all}
               17862230  402.764    0.000  402.764    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               31896850  393.875    0.000  393.875    0.000 {built-in method log}
               31896850  391.145    0.000  391.145    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
              304221408  293.709    0.000  372.291    0.000 layer.py:95(isFree)
               13011959   21.215    0.000  369.075    0.000 <__array_function__ internals>:2(prod)
               13011959   20.936    0.000  343.439    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
               17862230  331.250    0.000  331.250    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               13011959   35.334    0.000  322.503    0.000 fromnumeric.py:2912(prod)
              842790195  217.832    0.000  315.835    0.000 enum.py:646(__hash__)
                8612152  312.839    0.000  312.839    0.000 {built-in method tensor}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9601874: <SuperLevel2_option_critic_2> in cluster <dcc> Done

Job <SuperLevel2_option_critic_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Thu Apr 29 21:41:16 2021
Job was executed on host(s) <n-62-23-22>, in queue <hpc>, as user <s183914> in cluster <dcc> at Thu Apr 29 21:41:19 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Apr 29 21:41:19 2021
Terminated at Sun May  2 21:36:21 2021
Results reported at Sun May  2 21:36:21 2021

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

    CPU time :                                   258886.45 sec.
    Max Memory :                                 1175 MB
    Average Memory :                             1164.04 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15209.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258957 sec.
    Turnaround time :                            258905 sec.

The output (if any) is above this job summary.

