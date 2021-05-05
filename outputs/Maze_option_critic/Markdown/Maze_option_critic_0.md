[W NNPACK.cpp:80] Could not initialize NNPACK! Reason: Unsupported hardware.

# Parameters

    Name :                      Maze_option_critic-0
    Main :                      option_critic_run
    Level :                     Levels.Maze
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


      32972305262 function calls (31915945164 primitive calls) in 258890.93 seconds

##    Ordered by: cumulative time
   List reduced from 442 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.498 258900.498 {built-in method builtins.exec}
                      1    0.327    0.327 258900.498 258900.498 <string>:1(<module>)
                      1 3934.004 3934.004 258900.171 258900.171 optionCritic.py:195(option_critic_run)
        1395263934/343788093 10335.070    0.000 111185.451    0.000 module.py:866(_call_impl)
               37566125 10080.284    0.000 109285.946    0.003 optionCritic.py:143(actor_loss_fn)
              116830649  779.454    0.000 101836.289    0.001 optionCritic.py:70(get_state)
              116830649 2764.404    0.000 98673.600    0.001 container.py:117(forward)
                1502645   11.820    0.000 81437.136    0.054 tensor.py:195(backward)
                1502645   13.252    0.000 81425.049    0.054 __init__.py:68(backward)
                1502645 81374.159    0.054 81374.159    0.054 {method 'run_backward' of 'torch._C._EngineBase' objects}
              233661298  902.606    0.000 60124.592    0.000 conv.py:398(forward)
              233661298  393.599    0.000 58885.233    0.000 conv.py:390(_conv_forward)
              233661298 58491.634    0.000 58491.634    0.000 {built-in method conv2d}
               37566125 3998.382    0.000 23479.356    0.001 optionCritic.py:91(get_action)
              460618742 1651.951    0.000 21978.578    0.000 linear.py:93(forward)
              460618742  583.530    0.000 19695.130    0.000 functional.py:1737(linear)
              460618742 18986.254    0.000 18986.254    0.000 {built-in method torch._C._nn.linear}
               37566125 1247.215    0.000 13079.599    0.000 optionCritic.py:80(predict_option_termination)
               75132250 1101.823    0.000 8471.385    0.000 distribution.py:34(__init__)
              350491947  436.087    0.000 8186.718    0.000 activation.py:713(forward)
              350491947  445.169    0.000 7750.631    0.000 functional.py:1364(leaky_relu)
               37566125  628.330    0.000 7713.577    0.000 categorical.py:115(log_prob)
              350491947 7213.313    0.000 7213.313    0.000 {built-in method torch._C._nn.leaky_relu}
               37566125  907.118    0.000 6869.877    0.000 categorical.py:49(__init__)
              113883408  467.697    0.000 6492.365    0.000 optionCritic.py:77(get_Q)
                 375661   86.671    0.000 6479.815    0.017 optionCritic.py:116(critic_loss_fn)
               75507911  467.251    0.000 5281.487    0.000 optionCritic.py:88(get_terminations)
               37566125  290.483    0.000 4552.681    0.000 bernoulli.py:34(__init__)
               37566125 2827.763    0.000 4252.140    0.000 constraints.py:398(check)
                1502645   30.557    0.000 3847.787    0.003 optimizer.py:84(wrapper)
                1502645   14.899    0.000 3724.558    0.002 grad_mode.py:24(decorate_context)
                1502645  106.056    0.000 3678.407    0.002 rmsprop.py:56(step)
                1502645  156.323    0.000 3454.420    0.002 _functional.py:203(rmsprop)
               37566125  479.672    0.000 3260.363    0.000 distribution.py:240(_validate_sample)
                1502645    9.957    0.000 2985.797    0.002 game.py:41(step)
                1502645   13.668    0.000 2868.697    0.002 layers.py:718(step)
              116830649  162.282    0.000 2312.324    0.000 activation.py:101(forward)
               37566125 1096.527    0.000 2256.853    0.000 categorical.py:123(entropy)
               37566125 2196.119    0.000 2196.119    0.000 constraints.py:249(check)
              116830649  140.361    0.000 2150.041    0.000 functional.py:1195(relu)
               37566125 2037.365    0.000 2037.365    0.000 constraints.py:364(check)
              116830649 1981.036    0.000 1981.036    0.000 {built-in method relu}
              112698375  225.413    0.000 1885.270    0.000 utils.py:106(__get__)
              262962875 1877.118    0.000 1877.118    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
             1411793029 1856.283    0.000 1856.283    0.000 {built-in method torch._C._get_tracing_state}
               37566125  327.134    0.000 1751.233    0.000 bernoulli.py:86(sample)
              113449697  205.500    0.000 1699.039    0.000 tensor.py:525(__rsub__)
             1807675834 1632.204    0.000 1632.357    0.000 module.py:934(__getattr__)
              116830649  112.732    0.000 1606.437    0.000 flatten.py:39(forward)
              112698375 1602.915    0.000 1602.915    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
               37566125   76.561    0.000 1494.325    0.000 categorical.py:88(logits)
              116830649 1493.705    0.000 1493.705    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              113074036 1479.058    0.000 1479.058    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
               37566125  390.438    0.000 1477.025    0.000 categorical.py:108(sample)
              113449697 1459.634    0.000 1459.634    0.000 {built-in method rsub}
               21037024 1457.109    0.000 1457.109    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                1502645   64.192    0.000 1437.689    0.001 layers.py:17(step)
               37566125   76.584    0.000 1417.763    0.000 utils.py:82(probs_to_logits)
                1502646  140.687    0.000 1411.380    0.001 layers.py:684(update)
               37566125  111.328    0.000 1368.113    0.000 layer.py:98(move)
               75132250  404.194    0.000 1252.346    0.000 functional.py:46(broadcast_tensors)
               75507911 1206.329    0.000 1206.329    0.000 {method 'max' of 'torch._C._TensorBase' objects}
              112698375 1105.904    0.000 1105.904    0.000 {method 'all' of 'torch._C._TensorBase' objects}
             6069919759 1042.770    0.000 1055.742    0.000 {built-in method builtins.len}
               16529095   46.885    0.000 1050.074    0.000 tensor.py:575(__iter__)
               16529095  967.757    0.000  967.757    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
             5697886385  923.537    0.000  923.537    0.000 {method 'values' of 'collections.OrderedDict' objects}
               37566125  218.111    0.000  913.481    0.000 layers.py:735(check)
               37566125  138.070    0.000  872.189    0.000 utils.py:77(clamp_probs)
               37566125  169.201    0.000  865.515    0.000 utils.py:11(broadcast_all)
               37566125  832.969    0.000  832.969    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               13820601  364.717    0.000  762.514    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               75132250  741.083    0.000  741.083    0.000 {built-in method broadcast_tensors}
               37566125  734.119    0.000  734.119    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
              113825358  723.253    0.000  723.253    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
                1502645   76.579    0.000  713.756    0.000 replaybuffer.py:34(save_option_critic)
               37566125  697.657    0.000  697.657    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
                 375661  533.809    0.001  693.972    0.002 replaybuffer.py:42(sample_option_critic)
              226148072  644.337    0.000  644.337    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               37566125  633.607    0.000  633.607    0.000 {built-in method clamp}
               75132250  615.318    0.000  615.318    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               37999836  590.371    0.000  590.371    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               37566125  547.824    0.000  547.824    0.000 {built-in method bernoulli}
               21037024  528.348    0.000  528.348    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                 433735   10.212    0.000  505.586    0.001 layers.py:740(restart)
               21037024  500.852    0.000  500.852    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                1502645   91.718    0.000  485.920    0.000 optimizer.py:189(zero_grad)
               37566125  471.414    0.000  471.414    0.000 {built-in method all}
               37566125  468.990    0.000  468.990    0.000 {built-in method log}
               37566125  460.332    0.000  460.332    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
               21037024  435.799    0.000  435.799    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                 433735    6.657    0.000  433.931    0.001 level.py:8(__init__)
               12021168  244.191    0.000  397.968    0.000 layer.py:167(NoRock_update)
               13820601   22.907    0.000  397.797    0.000 <__array_function__ internals>:2(prod)
                 591360   58.612    0.000  394.405    0.001 levels.py:9(generate)
               21037024  375.990    0.000  375.990    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               13820601   22.837    0.000  370.402    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
               13820601   35.860    0.000  347.564    0.000 fromnumeric.py:2912(prod)
               10142857  341.883    0.000  341.883    0.000 {built-in method tensor}
               37566125  341.873    0.000  341.873    0.000 {built-in method multinomial}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9601875: <Maze_option_critic_0> in cluster <dcc> Done

Job <Maze_option_critic_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Thu Apr 29 21:41:17 2021
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

    CPU time :                                   258873.48 sec.
    Max Memory :                                 901 MB
    Average Memory :                             892.46 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15483.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258957 sec.
    Turnaround time :                            258904 sec.

The output (if any) is above this job summary.

