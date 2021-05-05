[W NNPACK.cpp:80] Could not initialize NNPACK! Reason: Unsupported hardware.

# Parameters

    Name :                      SuperLevel1_option_critic-1
    Main :                      option_critic_run
    Level :                     Levels.SuperLevel
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


      30968750181 function calls (30073399475 primitive calls) in 258900.78 seconds

##    Ordered by: cumulative time
   List reduced from 443 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.781 258900.781 {built-in method builtins.exec}
                      1    0.338    0.338 258900.781 258900.781 <string>:1(<module>)
                      1 3320.405 3320.405 258900.443 258900.443 optionCritic.py:195(option_critic_run)
        1182580322/291369623 8897.764    0.000 111503.292    0.000 module.py:866(_call_impl)
               31840325 8564.295    0.000 104701.635    0.003 optionCritic.py:143(actor_loss_fn)
               99023411  678.462    0.000 103605.560    0.001 optionCritic.py:70(get_state)
               99023411 2427.144    0.000 100919.811    0.001 container.py:117(forward)
                1273613   10.572    0.000 82608.385    0.065 tensor.py:195(backward)
                1273613   11.307    0.000 82597.562    0.065 __init__.py:68(backward)
                1273613 82553.577    0.065 82553.577    0.065 {method 'run_backward' of 'torch._C._EngineBase' objects}
              198046822  747.193    0.000 67640.349    0.000 conv.py:398(forward)
              198046822  330.741    0.000 66606.460    0.000 conv.py:390(_conv_forward)
              198046822 66275.719    0.000 66275.719    0.000 {built-in method conv2d}
               31840325 3350.280    0.000 19769.267    0.001 optionCritic.py:91(get_action)
              390393034 1362.444    0.000 18837.777    0.000 linear.py:93(forward)
              390393034  504.178    0.000 16942.571    0.000 functional.py:1737(linear)
              390393034 16331.807    0.000 16331.807    0.000 {built-in method torch._C._nn.linear}
               31840325 1025.891    0.000 11184.178    0.000 optionCritic.py:80(predict_option_termination)
                1273613   27.557    0.000 10025.323    0.008 optimizer.py:84(wrapper)
                1273613   14.128    0.000 9913.705    0.008 grad_mode.py:24(decorate_context)
                1273613   91.827    0.000 9871.673    0.008 rmsprop.py:56(step)
                1273613  137.254    0.000 9684.050    0.008 _functional.py:203(rmsprop)
                 318403   73.452    0.000 7701.123    0.024 optionCritic.py:116(critic_loss_fn)
               17830576 7518.343    0.000 7518.343    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               63680650  920.782    0.000 7285.492    0.000 distribution.py:34(__init__)
              297070233  519.862    0.000 7132.291    0.000 activation.py:713(forward)
              297070233  391.178    0.000 6612.429    0.000 functional.py:1364(leaky_relu)
               31840325  513.346    0.000 6459.475    0.000 categorical.py:115(log_prob)
              297070233 6138.565    0.000 6138.565    0.000 {built-in method torch._C._nn.leaky_relu}
               31840325  749.334    0.000 5827.747    0.000 categorical.py:49(__init__)
               96506834  385.430    0.000 5496.996    0.000 optionCritic.py:77(get_Q)
               63999053  384.074    0.000 4474.131    0.000 optionCritic.py:88(get_terminations)
                1273613    7.494    0.000 4351.885    0.003 game.py:41(step)
                1273613   11.166    0.000 4238.649    0.003 layers.py:718(step)
               31840325  244.619    0.000 3996.908    0.000 bernoulli.py:34(__init__)
               31840325 2422.814    0.000 3649.820    0.000 constraints.py:398(check)
                1273613   56.660    0.000 2961.236    0.002 layers.py:17(step)
               31840325  189.509    0.000 2900.174    0.000 layer.py:98(move)
               31840325  394.104    0.000 2733.283    0.000 distribution.py:240(_validate_sample)
               31840325  355.037    0.000 2073.594    0.000 layers.py:735(check)
               99023411  144.239    0.000 1990.850    0.000 activation.py:101(forward)
               31840325  940.143    0.000 1925.110    0.000 categorical.py:123(entropy)
               31840325 1858.520    0.000 1858.520    0.000 constraints.py:249(check)
               99023411  135.679    0.000 1846.612    0.000 functional.py:1195(relu)
               31840325 1770.510    0.000 1770.510    0.000 constraints.py:364(check)
               99023411 1685.252    0.000 1685.252    0.000 {built-in method relu}
               95520975  182.899    0.000 1581.324    0.000 utils.py:106(__get__)
              222882275 1526.993    0.000 1526.993    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
             1196590065 1521.886    0.000 1521.886    0.000 {built-in method torch._C._get_tracing_state}
               31840325  265.737    0.000 1493.486    0.000 bernoulli.py:86(sample)
               96157781  156.415    0.000 1442.627    0.000 tensor.py:525(__rsub__)
             1532095626 1387.247    0.000 1387.376    0.000 module.py:934(__getattr__)
               95520975 1364.349    0.000 1364.349    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
               99023411   99.799    0.000 1356.422    0.000 flatten.py:39(forward)
               95839378 1262.548    0.000 1262.548    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
                1273614  130.142    0.000 1261.008    0.001 layers.py:684(update)
               96157781 1260.106    0.000 1260.106    0.000 {built-in method rsub}
               31840325   62.477    0.000 1258.939    0.000 categorical.py:88(logits)
               99023411 1256.622    0.000 1256.622    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               31840325  317.737    0.000 1231.097    0.000 categorical.py:108(sample)
               31840325   64.203    0.000 1196.462    0.000 utils.py:82(probs_to_logits)
               63680650  341.965    0.000 1066.297    0.000 functional.py:46(broadcast_tensors)
               63999053 1033.652    0.000 1033.652    0.000 {method 'max' of 'torch._C._TensorBase' objects}
               95520975  946.942    0.000  946.942    0.000 {method 'all' of 'torch._C._TensorBase' objects}
             5295040865  919.198    0.000  930.693    0.000 {built-in method builtins.len}
               14009743   39.498    0.000  906.977    0.000 tensor.py:575(__iter__)
               17830576  845.264    0.000  845.264    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               14009743  838.194    0.000  838.194    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               31840325  164.386    0.000  768.332    0.000 utils.py:11(broadcast_all)
             4829344699  742.691    0.000  742.691    0.000 {method 'values' of 'collections.OrderedDict' objects}
               31840325  114.344    0.000  732.085    0.000 utils.py:77(clamp_probs)
               31840325  700.609    0.000  700.609    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               12592328  315.801    0.000  666.711    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               63680650  633.896    0.000  633.896    0.000 {built-in method broadcast_tensors}
               31840325  617.741    0.000  617.741    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
               96476184  615.569    0.000  615.569    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
                1273613   63.944    0.000  613.069    0.000 replaybuffer.py:34(save_option_critic)
                 318403  450.599    0.001  599.473    0.002 replaybuffer.py:42(sample_option_critic)
               31840325  589.423    0.000  589.423    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
               31840325  536.755    0.000  536.755    0.000 {built-in method clamp}
              191678756  533.204    0.000  533.204    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               31840325  124.482    0.000  531.440    0.000 layers.py:729(isFree)
               32189378  511.466    0.000  511.466    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               63680650  509.979    0.000  509.979    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               16556982  315.644    0.000  508.110    0.000 layer.py:151(update)
               31840325  359.671    0.000  481.538    0.000 layers.py:471(check)
               31840325  477.918    0.000  477.918    0.000 {built-in method bernoulli}
               17830576  452.012    0.000  452.012    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                1273613   78.633    0.000  424.672    0.000 optimizer.py:189(zero_grad)
               31840325  409.902    0.000  409.902    0.000 {built-in method all}
              342113568  318.553    0.000  406.958    0.000 layer.py:95(isFree)
               31840325  400.174    0.000  400.174    0.000 {built-in method log}
               17830576  394.389    0.000  394.389    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               31840325  394.008    0.000  394.008    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
              978259785  252.206    0.000  360.134    0.000 enum.py:646(__hash__)
               12592328   20.642    0.000  350.910    0.000 <__array_function__ internals>:2(prod)
               31840325  255.880    0.000  338.102    0.000 layers.py:77(check)
               17830576  336.788    0.000  336.788    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                8596891  330.360    0.000  330.360    0.000 {built-in method tensor}
               12592328   19.724    0.000  326.242    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}


Traceback (most recent call last):
  File "main.py", line 227, in <module>
    
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/auxillaries.py", line 132, in run
    enablePrint()
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils/server.py", line 37, in serverRun
    profilingStats()
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils/debug.py", line 62, in profilingStats
    os.remove('stats')
FileNotFoundError: [Errno 2] No such file or directory: 'stats'

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9601870: <SuperLevel1_option_critic_1> in cluster <dcc> Exited

Job <SuperLevel1_option_critic_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Thu Apr 29 21:41:14 2021
Job was executed on host(s) <n-62-23-21>, in queue <hpc>, as user <s183914> in cluster <dcc> at Thu Apr 29 21:41:16 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Apr 29 21:41:16 2021
Terminated at Sun May  2 21:36:23 2021
Results reported at Sun May  2 21:36:23 2021

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

Exited with exit code 1.

Resource usage summary:

    CPU time :                                   258864.36 sec.
    Max Memory :                                 1334 MB
    Average Memory :                             1326.84 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15050.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258959 sec.
    Turnaround time :                            258909 sec.

The output (if any) is above this job summary.

