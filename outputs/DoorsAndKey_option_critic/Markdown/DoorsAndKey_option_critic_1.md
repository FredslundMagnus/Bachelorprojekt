[W NNPACK.cpp:80] Could not initialize NNPACK! Reason: Unsupported hardware.

# Parameters

    Name :                      DoorsAndKey_option_critic-1
    Main :                      option_critic_run
    Level :                     Levels.Causal1
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


      32277261737 function calls (31206130242 primitive calls) in 258900.41 seconds

##    Ordered by: cumulative time
   List reduced from 428 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.413 258900.413 {built-in method builtins.exec}
                      1    0.294    0.294 258900.413 258900.413 <string>:1(<module>)
                      1 3970.349 3970.349 258900.119 258900.119 optionCritic.py:195(option_critic_run)
        1414800221/348621233 10459.040    0.000 108505.841    0.000 module.py:866(_call_impl)
               38091425 10197.250    0.000 107768.845    0.003 optionCritic.py:143(actor_loss_fn)
              118464332  769.410    0.000 99055.302    0.001 optionCritic.py:70(get_state)
              118464332 2847.865    0.000 95886.233    0.001 container.py:117(forward)
                1523657   12.305    0.000 83549.528    0.055 tensor.py:195(backward)
                1523657   14.361    0.000 83536.930    0.055 __init__.py:68(backward)
                1523657 83484.966    0.055 83484.966    0.055 {method 'run_backward' of 'torch._C._EngineBase' objects}
              236928664  912.918    0.000 56723.136    0.000 conv.py:398(forward)
              236928664  381.711    0.000 55474.899    0.000 conv.py:390(_conv_forward)
              236928664 55093.188    0.000 55093.188    0.000 {built-in method conv2d}
               38091425 4058.096    0.000 23847.656    0.001 optionCritic.py:91(get_action)
              467085565 1646.458    0.000 22239.523    0.000 linear.py:93(forward)
              467085565  599.610    0.000 19983.165    0.000 functional.py:1737(linear)
              467085565 19245.166    0.000 19245.166    0.000 {built-in method torch._C._nn.linear}
               38091425 1236.914    0.000 13235.960    0.000 optionCritic.py:80(predict_option_termination)
               76182850 1126.978    0.000 8686.639    0.000 distribution.py:34(__init__)
              355392996  453.054    0.000 8333.809    0.000 activation.py:713(forward)
              355392996  459.385    0.000 7880.755    0.000 functional.py:1364(leaky_relu)
               38091425  639.353    0.000 7821.862    0.000 categorical.py:115(log_prob)
              355392996 7317.575    0.000 7317.575    0.000 {built-in method torch._C._nn.leaky_relu}
               38091425  907.220    0.000 7014.936    0.000 categorical.py:49(__init__)
              115501712  469.042    0.000 6571.331    0.000 optionCritic.py:77(get_Q)
                 380914   86.635    0.000 6046.390    0.016 optionCritic.py:116(critic_loss_fn)
               76563764  460.016    0.000 5307.595    0.000 optionCritic.py:88(get_terminations)
               38091425  290.358    0.000 4663.200    0.000 bernoulli.py:34(__init__)
                1523657   31.514    0.000 4492.764    0.003 optimizer.py:84(wrapper)
               38091425 2913.908    0.000 4373.074    0.000 constraints.py:398(check)
                1523657   16.115    0.000 4366.001    0.003 grad_mode.py:24(decorate_context)
                1523657  104.892    0.000 4319.461    0.003 rmsprop.py:56(step)
                1523657  163.340    0.000 4098.507    0.003 _functional.py:203(rmsprop)
               38091425  487.213    0.000 3304.338    0.000 distribution.py:240(_validate_sample)
              118464332  169.636    0.000 2370.579    0.000 activation.py:101(forward)
               38091425 1115.023    0.000 2301.647    0.000 categorical.py:123(entropy)
                1523657    9.125    0.000 2274.809    0.001 game.py:41(step)
               38091425 2222.803    0.000 2222.803    0.000 constraints.py:249(check)
              118464332  147.776    0.000 2200.942    0.000 functional.py:1195(relu)
                1523657   13.758    0.000 2165.025    0.001 layers.py:718(step)
               21331192 2128.311    0.000 2128.311    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               38091425 2095.050    0.000 2095.050    0.000 constraints.py:364(check)
              118464332 2021.570    0.000 2021.570    0.000 {built-in method relu}
              114274275  224.812    0.000 1903.315    0.000 utils.py:106(__get__)
             1431560448 1893.879    0.000 1893.879    0.000 {built-in method torch._C._get_tracing_state}
              266639975 1844.960    0.000 1844.960    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               38091425  316.939    0.000 1743.407    0.000 bernoulli.py:86(sample)
              115036103  195.887    0.000 1717.913    0.000 tensor.py:525(__rsub__)
              118464332  118.580    0.000 1644.843    0.000 flatten.py:39(forward)
              114274275 1634.497    0.000 1634.497    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
             1833030682 1609.991    0.000 1610.146    0.000 module.py:934(__getattr__)
              118464332 1526.263    0.000 1526.263    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               38091425   74.712    0.000 1511.630    0.000 categorical.py:88(logits)
              114655189 1506.373    0.000 1506.373    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
              115036103 1488.942    0.000 1488.942    0.000 {built-in method rsub}
               38091425  383.830    0.000 1482.142    0.000 categorical.py:108(sample)
               38091425   82.453    0.000 1436.918    0.000 utils.py:82(probs_to_logits)
               76182850  414.040    0.000 1290.941    0.000 functional.py:46(broadcast_tensors)
               76563764 1214.777    0.000 1214.777    0.000 {method 'max' of 'torch._C._TensorBase' objects}
                1523657   67.580    0.000 1137.402    0.001 layers.py:17(step)
              114274275 1114.193    0.000 1114.193    0.000 {method 'all' of 'torch._C._TensorBase' objects}
               38091425  110.701    0.000 1064.466    0.000 layer.py:98(move)
               16760227   46.918    0.000 1038.365    0.000 tensor.py:575(__iter__)
             6080063497 1021.720    0.000 1036.323    0.000 {built-in method builtins.len}
                1523658  141.830    0.000 1007.933    0.001 layers.py:684(update)
               16760227  955.381    0.000  955.381    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
             5777665216  915.819    0.000  915.819    0.000 {method 'values' of 'collections.OrderedDict' objects}
               38091425  166.456    0.000  891.791    0.000 utils.py:11(broadcast_all)
               38091425  136.400    0.000  876.526    0.000 utils.py:77(clamp_probs)
               38091425  835.111    0.000  835.111    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               76182850  769.851    0.000  769.851    0.000 {built-in method broadcast_tensors}
               13787439  366.979    0.000  764.471    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               38091425  740.126    0.000  740.126    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
              115417017  739.305    0.000  739.305    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
                1523657   76.235    0.000  722.783    0.000 replaybuffer.py:34(save_option_critic)
               38091425  709.028    0.000  709.028    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
                 380914  533.768    0.001  694.544    0.002 replaybuffer.py:42(sample_option_critic)
              229310378  658.371    0.000  658.371    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               38091425  645.454    0.000  645.454    0.000 {built-in method clamp}
               76182850  618.442    0.000  618.442    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               38557034  592.288    0.000  592.288    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               21331192  566.967    0.000  566.967    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               38091425  554.418    0.000  554.418    0.000 {built-in method bernoulli}
               38091425  162.354    0.000  534.766    0.000 layers.py:735(check)
               38091425  486.483    0.000  486.483    0.000 {built-in method all}
                1523657   92.837    0.000  484.926    0.000 optimizer.py:189(zero_grad)
               38091425  477.939    0.000  477.939    0.000 {built-in method log}
               38091425  475.596    0.000  475.596    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
               21331192  450.858    0.000  450.858    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               21331192  407.192    0.000  407.192    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               13787439   22.854    0.000  397.491    0.000 <__array_function__ internals>:2(prod)
               21331192  381.838    0.000  381.838    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               13787439   22.358    0.000  369.959    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
               13787439   38.086    0.000  347.600    0.000 fromnumeric.py:2912(prod)
               38091425  346.696    0.000  346.696    0.000 {built-in method multinomial}
               38091425   74.874    0.000  330.344    0.000 layers.py:729(isFree)
               10284688  321.612    0.000  321.612    0.000 {built-in method tensor}
              118464346  314.993    0.000  314.993    0.000 {method 'to' of 'torch._C._TensorBase' objects}
              503043940  219.861    0.000  312.112    0.000 {built-in method builtins.isinstance}
               38091425  309.575    0.000  309.575    0.000 {method 'expand' of 'torch._C._TensorBase' objects}


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
Subject: Job 9601888: <DoorsAndKey_option_critic_1> in cluster <dcc> Exited

Job <DoorsAndKey_option_critic_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Thu Apr 29 21:41:26 2021
Job was executed on host(s) <n-62-23-22>, in queue <hpc>, as user <s183914> in cluster <dcc> at Thu Apr 29 21:41:27 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Apr 29 21:41:27 2021
Terminated at Sun May  2 21:36:30 2021
Results reported at Sun May  2 21:36:30 2021

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

    CPU time :                                   258893.98 sec.
    Max Memory :                                 785 MB
    Average Memory :                             769.06 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15599.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258966 sec.
    Turnaround time :                            258904 sec.

The output (if any) is above this job summary.

