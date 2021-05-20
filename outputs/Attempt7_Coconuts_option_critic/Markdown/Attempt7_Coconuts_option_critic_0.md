[W NNPACK.cpp:80] Could not initialize NNPACK! Reason: Unsupported hardware.

# Parameters

    Name :                      Attempt7_Coconuts_option_critic-0
    Main :                      option_critic_run
    Level :                     Levels.Coconuts
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
    Num :                       0
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              4315 minutes.
    Hours used :                71 hours.

# Profiling


      37602118707 function calls (36542355255 primitive calls) in 258901.21 seconds

##    Ordered by: cumulative time
   List reduced from 437 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258901.210 258901.210 {built-in method builtins.exec}
                      1    0.382    0.382 258901.210 258901.210 <string>:1(<module>)
                      1 4055.573 4055.573 258900.828 258900.828 optionCritic.py:195(option_critic_run)
        1404072110/348170465 10237.100    0.000 108113.113    0.000 module.py:866(_call_impl)
               38018400 9155.563    0.000 107726.163    0.003 optionCritic.py:143(actor_loss_fn)
              117322405  824.158    0.000 98663.382    0.001 optionCritic.py:70(get_state)
              117322405 2819.348    0.000 95448.115    0.001 container.py:117(forward)
                1188075    9.606    0.000 66847.946    0.056 tensor.py:195(backward)
                1188075   10.994    0.000 66838.099    0.056 __init__.py:68(backward)
                1188075 66797.031    0.056 66797.031    0.056 {method 'run_backward' of 'torch._C._EngineBase' objects}
              234644810  915.912    0.000 56868.157    0.000 conv.py:398(forward)
              234644810  402.097    0.000 55621.832    0.000 conv.py:390(_conv_forward)
              234644810 55219.735    0.000 55219.735    0.000 {built-in method conv2d}
               38018400 3943.499    0.000 23570.963    0.001 optionCritic.py:91(get_action)
              465492870 1668.365    0.000 22134.625    0.000 linear.py:93(forward)
                1188075   27.097    0.000 20321.848    0.017 optimizer.py:84(wrapper)
                1188075   14.997    0.000 20213.986    0.017 grad_mode.py:24(decorate_context)
                1188075   81.042    0.000 20171.757    0.017 rmsprop.py:56(step)
                1188075  133.707    0.000 19996.665    0.017 _functional.py:203(rmsprop)
              465492870  598.127    0.000 19844.776    0.000 functional.py:1737(linear)
              465492870 19122.471    0.000 19122.471    0.000 {built-in method torch._C._nn.linear}
               16633044 17568.579    0.001 17568.579    0.001 {method 'sqrt' of 'torch._C._TensorBase' objects}
               38018400 1238.368    0.000 13280.756    0.000 optionCritic.py:80(predict_option_termination)
               76036800 1101.951    0.000 8685.276    0.000 distribution.py:34(__init__)
              351967215  471.478    0.000 8242.093    0.000 activation.py:713(forward)
              351967215  447.340    0.000 7770.614    0.000 functional.py:1364(leaky_relu)
               38018400  617.423    0.000 7734.736    0.000 categorical.py:115(log_prob)
              351967215 7231.398    0.000 7231.398    0.000 {built-in method torch._C._nn.leaky_relu}
               38018400  895.410    0.000 6942.053    0.000 categorical.py:49(__init__)
              116495842  481.463    0.000 6630.975    0.000 optionCritic.py:77(get_Q)
                1188075    8.131    0.000 5350.221    0.005 game.py:42(step)
               76333818  475.813    0.000 5297.328    0.000 optionCritic.py:88(get_terminations)
                1188075   11.698    0.000 5241.994    0.004 layers.py:827(step)
                 297018   68.756    0.000 4876.179    0.016 optionCritic.py:116(critic_loss_fn)
               38018400  277.911    0.000 4697.547    0.000 bernoulli.py:34(__init__)
               38018400 2885.028    0.000 4341.244    0.000 constraints.py:398(check)
               38018400  474.333    0.000 3247.564    0.000 distribution.py:240(_validate_sample)
                1188076  141.493    0.000 3124.722    0.003 layers.py:793(update)
              117322405  171.759    0.000 2350.403    0.000 activation.py:101(forward)
               38018400 1107.426    0.000 2278.215    0.000 categorical.py:123(entropy)
               38018400 2205.248    0.000 2205.248    0.000 constraints.py:249(check)
              117322405  153.360    0.000 2178.644    0.000 functional.py:1195(relu)
               38018400 2127.408    0.000 2127.408    0.000 constraints.py:364(check)
                1188075   63.876    0.000 2099.474    0.002 layers.py:17(step)
                1846642   31.629    0.000 2063.125    0.001 layers.py:849(restart)
               38018400  190.108    0.000 2031.106    0.000 layer.py:106(move)
              117322405 1996.562    0.000 1996.562    0.000 {built-in method relu}
              114055200  212.065    0.000 1900.309    0.000 utils.py:106(__get__)
              266128800 1867.897    0.000 1867.897    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
             1417140935 1852.316    0.000 1852.316    0.000 {built-in method torch._C._get_tracing_state}
                1846642   13.436    0.000 1763.957    0.001 level.py:8(__init__)
               38018400  315.832    0.000 1762.625    0.000 bernoulli.py:86(sample)
              114649236  186.802    0.000 1711.312    0.000 tensor.py:525(__rsub__)
                1846642  114.256    0.000 1641.822    0.001 levels.py:277(generate)
              117322405  128.071    0.000 1638.361    0.000 flatten.py:39(forward)
              114055200 1608.203    0.000 1608.203    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
             1824637138 1603.592    0.000 1603.716    0.000 module.py:934(__getattr__)
               38018400   74.719    0.000 1513.241    0.000 categorical.py:88(logits)
              117322405 1510.290    0.000 1510.290    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              114649236 1491.955    0.000 1491.955    0.000 {built-in method rsub}
              114352218 1486.213    0.000 1486.213    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
               38018400  373.466    0.000 1476.035    0.000 categorical.py:108(sample)
               38018400  236.786    0.000 1458.266    0.000 layers.py:844(check)
               16464726  216.800    0.000 1438.916    0.000 level.py:41(notUsed)
               38018400   75.052    0.000 1438.522    0.000 utils.py:82(probs_to_logits)
               16633044 1390.913    0.000 1390.913    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               76036800  412.465    0.000 1281.684    0.000 functional.py:46(broadcast_tensors)
               76333818 1217.213    0.000 1217.213    0.000 {method 'max' of 'torch._C._TensorBase' objects}
              114055200 1119.789    0.000 1119.789    0.000 {method 'all' of 'torch._C._TensorBase' objects}
             6063507449 1048.293    0.000 1059.285    0.000 {built-in method builtins.len}
               13068825   38.165    0.000 1028.630    0.000 tensor.py:575(__iter__)
               13068825  961.090    0.000  961.090    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               38018400  173.775    0.000  892.260    0.000 utils.py:11(broadcast_all)
               38018400  134.895    0.000  889.589    0.000 utils.py:77(clamp_probs)
             5733610845  859.167    0.000  859.167    0.000 {method 'values' of 'collections.OrderedDict' objects}
               38018400  856.988    0.000  856.988    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               76036800  763.834    0.000  763.834    0.000 {built-in method broadcast_tensors}
               38018400  754.695    0.000  754.695    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
              114946254  747.310    0.000  747.310    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
                1188075   75.796    0.000  737.454    0.001 replaybuffer.py:34(save_option_critic)
               38018400  703.994    0.000  703.994    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
               16464726   18.710    0.000  683.610    0.000 level.py:38(elementsIn)
              228704436  657.374    0.000  657.374    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               38018400  636.711    0.000  636.711    0.000 {built-in method clamp}
               39865006  626.609    0.000  626.609    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               76036800  618.732    0.000  618.732    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                8316532  406.296    0.000  574.809    0.000 layer.py:159(update)
               38018400  554.015    0.000  554.015    0.000 {built-in method bernoulli}
                 297018  421.985    0.001  549.368    0.002 replaybuffer.py:42(sample_option_critic)
               38018400  488.236    0.000  488.236    0.000 {built-in method all}
             1430738407  331.150    0.000  478.316    0.000 enum.py:646(__hash__)
               38018400  473.881    0.000  473.881    0.000 {built-in method log}
               38018400  473.656    0.000  473.656    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
               38018400  350.140    0.000  464.703    0.000 layers.py:471(check)
                8316516  213.009    0.000  446.766    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               16464726  225.137    0.000  424.499    0.000 level.py:39(<listcomp>)
                1188075   73.549    0.000  382.701    0.000 optimizer.py:189(zero_grad)
               38018400  268.107    0.000  355.291    0.000 layers.py:77(check)
               38018400  352.901    0.000  352.901    0.000 {built-in method multinomial}
              500364778  234.710    0.000  331.279    0.000 {built-in method builtins.isinstance}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9632752: <Attempt7_Coconuts_option_critic_0> in cluster <dcc> Done

Job <Attempt7_Coconuts_option_critic_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed May 12 14:11:13 2021
Job was executed on host(s) <n-62-23-26>, in queue <hpc>, as user <s183914> in cluster <dcc> at Sun May 16 23:16:53 2021
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

    CPU time :                                   258896.30 sec.
    Max Memory :                                 864 MB
    Average Memory :                             853.04 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15520.00 MB
    Max Swap :                                   -
    Max Processes :                              5
    Max Threads :                                6
    Run time :                                   259038 sec.
    Turnaround time :                            637270 sec.

The output (if any) is above this job summary.

