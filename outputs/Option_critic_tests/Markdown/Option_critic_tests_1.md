
# Parameters

    Name :                      Option_critic_tests-1
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


      10027520 function calls (9697016 primitive calls) in 60.82 seconds

##    Ordered by: cumulative time
   List reduced from 429 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000   60.817   60.817 {built-in method builtins.exec}
                      1    0.041    0.041   60.817   60.817 <string>:1(<module>)
                      1    1.678    1.678   60.775   60.775 optionCritic.py:195(option_critic_run)
                  12100    2.502    0.000   28.015    0.002 optionCritic.py:143(actor_loss_fn)
          439067/109370    2.424    0.000   26.518    0.000 module.py:866(_call_impl)
                  36633    0.181    0.000   24.593    0.001 optionCritic.py:70(get_state)
                  36633    0.551    0.000   23.825    0.001 container.py:117(forward)
                    121    0.001    0.000   17.531    0.145 tensor.py:195(backward)
                    121    0.002    0.000   17.530    0.145 __init__.py:68(backward)
                    121   17.523    0.145   17.523    0.145 {method 'run_backward' of 'torch._C._EngineBase' objects}
                  73266    0.218    0.000   14.717    0.000 conv.py:398(forward)
                  73266    0.133    0.000   14.404    0.000 conv.py:390(_conv_forward)
                  73266   14.271    0.000   14.271    0.000 {built-in method conv2d}
                 146003    0.399    0.000    5.376    0.000 linear.py:93(forward)
                  12100    0.945    0.000    5.350    0.000 optionCritic.py:91(get_action)
                 146003    0.151    0.000    4.806    0.000 functional.py:1737(linear)
                 146003    4.620    0.000    4.620    0.000 {built-in method torch._C._nn.linear}
                  12100    0.320    0.000    4.011    0.000 optionCritic.py:80(predict_option_termination)
                  24200    0.337    0.000    2.164    0.000 distribution.py:34(__init__)
                  12100    0.140    0.000    1.756    0.000 categorical.py:115(log_prob)
                  12100    0.153    0.000    1.728    0.000 bernoulli.py:34(__init__)
                 109899    0.127    0.000    1.713    0.000 activation.py:713(forward)
                 109899    0.130    0.000    1.586    0.000 functional.py:1364(leaky_relu)
                  12100    0.203    0.000    1.462    0.000 categorical.py:49(__init__)
                 109899    1.430    0.000    1.430    0.000 {built-in method torch._C._nn.leaky_relu}
                  36407    0.091    0.000    1.357    0.000 optionCritic.py:77(get_Q)
                  24230    0.103    0.000    1.115    0.000 optionCritic.py:88(get_terminations)
                  12100    0.602    0.000    0.887    0.000 constraints.py:398(check)
                  12100    0.115    0.000    0.676    0.000 distribution.py:240(_validate_sample)
                  12100    0.141    0.000    0.651    0.000 bernoulli.py:86(sample)
                  12100    0.612    0.000    0.612    0.000 constraints.py:364(check)
                    121    0.001    0.000    0.548    0.005 game.py:41(step)
                    121    0.002    0.000    0.532    0.004 layers.py:718(step)
                  11851    0.247    0.000    0.521    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                  36633    0.052    0.000    0.501    0.000 activation.py:101(forward)
                  36300    0.058    0.000    0.494    0.000 utils.py:106(__get__)
                  12100    0.245    0.000    0.468    0.000 categorical.py:123(entropy)
                  84700    0.463    0.000    0.463    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                 572181    0.457    0.000    0.457    0.000 module.py:934(__getattr__)
                  36633    0.049    0.000    0.449    0.000 functional.py:1195(relu)
                  24200    0.154    0.000    0.443    0.000 functional.py:46(broadcast_tensors)
                  12100    0.437    0.000    0.437    0.000 constraints.py:249(check)
                  12100    0.096    0.000    0.423    0.000 utils.py:11(broadcast_all)
                  36360    0.054    0.000    0.418    0.000 tensor.py:525(__rsub__)
                  36633    0.045    0.000    0.403    0.000 flatten.py:39(forward)
                  36633    0.393    0.000    0.393    0.000 {built-in method relu}
                  12100    0.017    0.000    0.392    0.000 categorical.py:88(logits)
                  12100    0.017    0.000    0.375    0.000 utils.py:82(probs_to_logits)
                   1331    0.006    0.000    0.368    0.000 tensor.py:575(__iter__)
                   1331    0.359    0.000    0.359    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
                  36633    0.358    0.000    0.358    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                  36360    0.357    0.000    0.357    0.000 {built-in method rsub}
                  24230    0.352    0.000    0.352    0.000 {method 'max' of 'torch._C._TensorBase' objects}
                     30    0.006    0.000    0.350    0.012 optionCritic.py:116(critic_loss_fn)
                  12100    0.090    0.000    0.342    0.000 categorical.py:108(sample)
                  36330    0.318    0.000    0.318    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
                    121    0.015    0.000    0.307    0.003 layers.py:17(step)
                 440398    0.307    0.000    0.307    0.000 {built-in method torch._C._get_tracing_state}
                  36300    0.302    0.000    0.302    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                  12100    0.298    0.000    0.298    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
                  12100    0.028    0.000    0.291    0.000 layer.py:98(move)
                  36300    0.286    0.000    0.286    0.000 {method 'all' of 'torch._C._TensorBase' objects}
                  11851    0.017    0.000    0.274    0.000 <__array_function__ internals>:2(prod)
                    122    0.024    0.000    0.272    0.002 layers.py:684(update)
                1881147    0.267    0.000    0.268    0.000 {built-in method builtins.len}
                  11851    0.016    0.000    0.253    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                  24200    0.246    0.000    0.246    0.000 {built-in method broadcast_tensors}
                  11851    0.024    0.000    0.237    0.000 fromnumeric.py:2912(prod)
                    121    0.020    0.000    0.225    0.002 replaybuffer.py:34(save_option_critic)
                1792901    0.224    0.000    0.224    0.000 {method 'values' of 'collections.OrderedDict' objects}
                  11851    0.060    0.000    0.213    0.000 fromnumeric.py:70(_wrapreduction)
                  12100    0.205    0.000    0.205    0.000 {built-in method bernoulli}
                  12100    0.183    0.000    0.183    0.000 {built-in method log}
                  36390    0.179    0.000    0.179    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
                  12100    0.035    0.000    0.175    0.000 utils.py:77(clamp_probs)
                    121    0.004    0.000    0.164    0.001 optimizer.py:84(wrapper)
                  12147    0.153    0.000    0.153    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                  12100    0.045    0.000    0.149    0.000 layers.py:735(check)
                    121    0.002    0.000    0.148    0.001 grad_mode.py:24(decorate_context)
                  12100    0.148    0.000    0.148    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
                    121    0.008    0.000    0.143    0.001 rmsprop.py:56(step)
                  12100    0.140    0.000    0.140    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
                  72660    0.140    0.000    0.140    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                  24200    0.129    0.000    0.129    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                  11851    0.128    0.000    0.128    0.000 {method 'reduce' of 'numpy.ufunc' objects}
                 158845    0.075    0.000    0.125    0.000 {built-in method builtins.isinstance}
                    121    0.008    0.000    0.125    0.001 _functional.py:203(rmsprop)
                  12100    0.118    0.000    0.118    0.000 {built-in method clamp}
                  12100    0.105    0.000    0.105    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
                  36400    0.032    0.000    0.101    0.000 {built-in method builtins.all}
                  12100    0.095    0.000    0.095    0.000 {built-in method all}
                  12100    0.093    0.000    0.093    0.000 {built-in method multinomial}
                  12247    0.044    0.000    0.089    0.000 grad_mode.py:119(__enter__)
                  36446    0.088    0.000    0.088    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                  12100    0.021    0.000    0.088    0.000 layers.py:729(isFree)
                  36647    0.084    0.000    0.084    0.000 {method 'to' of 'torch._C._TensorBase' objects}
                  24200    0.076    0.000    0.079    0.000 distribution.py:226(_extended_shape)
                  85027    0.068    0.000    0.076    0.000 {built-in method builtins.getattr}
                    146    0.002    0.000    0.070    0.000 layers.py:740(restart)
                  12100    0.070    0.000    0.070    0.000 {method 'expand' of 'torch._C._TensorBase' objects}


Traceback (most recent call last):
  File "main.py", line 227, in <module>
    run(Defaults)
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/auxillaries.py", line 132, in run
    (serverRun if isServer else Defaults.main).__call__(getvals(Defaults))
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils/server.py", line 37, in serverRun
    profilingStats()
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils/debug.py", line 62, in profilingStats
    os.remove('stats')
FileNotFoundError: [Errno 2] No such file or directory: 'stats'

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9601822: <Option_critic_tests_1> in cluster <dcc> Exited

Job <Option_critic_tests_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Thu Apr 29 21:06:51 2021
Job was executed on host(s) <n-62-31-1>, in queue <hpc>, as user <s183914> in cluster <dcc> at Thu Apr 29 21:06:53 2021
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

Exited with exit code 1.

Resource usage summary:

    CPU time :                                   61.61 sec.
    Max Memory :                                 126 MB
    Average Memory :                             126.00 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               16258.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   130 sec.
    Turnaround time :                            66 sec.

The output (if any) is above this job summary.

