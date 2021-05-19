[W NNPACK.cpp:80] Could not initialize NNPACK! Reason: Unsupported hardware.

# Parameters

    Name :                      Attempt8_Monsters_option_critic-2
    Main :                      option_critic_run
    Level :                     Levels.MonsterLevel
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


      39139272163 function calls (37943006035 primitive calls) in 258900.95 seconds

##    Ordered by: cumulative time
   List reduced from 435 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.951 258900.951 {built-in method builtins.exec}
                      1    0.330    0.330 258900.951 258900.951 <string>:1(<module>)
                      1 4339.226 4339.226 258900.620 258900.620 optionCritic.py:195(option_critic_run)
               42915360 9778.210    0.000 115221.355    0.003 optionCritic.py:143(actor_loss_fn)
        1583852031/391944960 11174.116    0.000 115215.881    0.000 module.py:866(_call_impl)
              132434119  852.191    0.000 104974.514    0.001 optionCritic.py:70(get_state)
              132434119 3086.309    0.000 101560.456    0.001 container.py:117(forward)
                1341105   10.279    0.000 71165.847    0.053 tensor.py:195(backward)
                1341105   12.482    0.000 71155.317    0.053 __init__.py:68(backward)
                1341105 71110.233    0.053 71110.233    0.053 {method 'run_backward' of 'torch._C._EngineBase' objects}
              264868238  984.967    0.000 60128.963    0.000 conv.py:398(forward)
              264868238  405.316    0.000 58804.291    0.000 conv.py:390(_conv_forward)
              264868238 58398.975    0.000 58398.975    0.000 {built-in method conv2d}
               42915360 4411.834    0.000 25846.305    0.001 optionCritic.py:91(get_action)
              524379079 1788.112    0.000 23258.439    0.000 linear.py:93(forward)
              524379079  603.257    0.000 20814.608    0.000 functional.py:1737(linear)
              524379079 20078.652    0.000 20078.652    0.000 {built-in method torch._C._nn.linear}
               42915360 1313.796    0.000 13952.231    0.000 optionCritic.py:80(predict_option_termination)
               85830720 1176.293    0.000 9292.634    0.000 distribution.py:34(__init__)
              397302357  543.376    0.000 9011.054    0.000 activation.py:713(forward)
              397302357  461.677    0.000 8467.678    0.000 functional.py:1364(leaky_relu)
               42915360  667.257    0.000 8406.387    0.000 categorical.py:115(log_prob)
              397302357 7897.993    0.000 7897.993    0.000 {built-in method torch._C._nn.leaky_relu}
               42915360  979.498    0.000 7598.887    0.000 categorical.py:49(__init__)
              130429485  524.961    0.000 7133.510    0.000 optionCritic.py:77(get_Q)
               86165996  511.624    0.000 5755.371    0.000 optionCritic.py:88(get_terminations)
                 335276   72.258    0.000 5100.361    0.015 optionCritic.py:116(critic_loss_fn)
               42915360  274.172    0.000 4788.642    0.000 bernoulli.py:34(__init__)
               42915360 3134.293    0.000 4740.953    0.000 constraints.py:398(check)
                1341105    8.950    0.000 4524.446    0.003 game.py:42(step)
                1341105   26.844    0.000 4432.309    0.003 optimizer.py:84(wrapper)
                1341105   11.859    0.000 4420.953    0.003 layers.py:827(step)
                1341105   12.923    0.000 4326.737    0.003 grad_mode.py:24(decorate_context)
                1341105   88.327    0.000 4287.131    0.003 rmsprop.py:56(step)
                1341105  135.618    0.000 4097.563    0.003 _functional.py:203(rmsprop)
               42915360  515.135    0.000 3527.524    0.000 distribution.py:240(_validate_sample)
              132434119  172.883    0.000 2551.614    0.000 activation.py:101(forward)
               18775464 2541.408    0.000 2541.408    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               42915360 1211.869    0.000 2500.510    0.000 categorical.py:123(entropy)
               42915360 2386.564    0.000 2386.564    0.000 constraints.py:249(check)
              132434119  166.033    0.000 2378.732    0.000 functional.py:1195(relu)
                1341105   71.096    0.000 2303.328    0.002 layers.py:17(step)
               42915360  183.155    0.000 2227.251    0.000 layer.py:106(move)
               42915360 2207.704    0.000 2207.704    0.000 constraints.py:364(check)
              132434119 2182.017    0.000 2182.017    0.000 {built-in method relu}
                1341106  146.059    0.000 2098.981    0.002 layers.py:793(update)
              128746080  231.482    0.000 2072.701    0.000 utils.py:106(__get__)
              300407520 2032.009    0.000 2032.009    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
             1598604186 2014.341    0.000 2014.341    0.000 {built-in method torch._C._get_tracing_state}
              129416632  191.933    0.000 1842.866    0.000 tensor.py:525(__rsub__)
               42915360  317.023    0.000 1787.297    0.000 bernoulli.py:86(sample)
              128746080 1774.066    0.000 1774.066    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
              132434119  123.863    0.000 1773.036    0.000 flatten.py:39(forward)
             2056444717 1715.518    0.000 1715.646    0.000 module.py:934(__getattr__)
               42915360   79.637    0.000 1661.667    0.000 categorical.py:88(logits)
              132434119 1649.173    0.000 1649.173    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               42915360  216.122    0.000 1632.568    0.000 layers.py:844(check)
              129081356 1619.527    0.000 1619.527    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
              129416632 1616.265    0.000 1616.265    0.000 {built-in method rsub}
               42915360  408.797    0.000 1614.571    0.000 categorical.py:108(sample)
               42915360   85.604    0.000 1582.030    0.000 utils.py:82(probs_to_logits)
               85830720  417.167    0.000 1334.037    0.000 functional.py:46(broadcast_tensors)
               26627993  633.573    0.000 1329.700    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               86165996 1304.272    0.000 1304.272    0.000 {method 'max' of 'torch._C._TensorBase' objects}
              128746080 1206.421    0.000 1206.421    0.000 {method 'all' of 'torch._C._TensorBase' objects}
             6671716305 1165.716    0.000 1176.857    0.000 {built-in method builtins.len}
               14752155   39.568    0.000 1052.442    0.000 tensor.py:575(__iter__)
             6467842243  985.707    0.000  985.707    0.000 {method 'values' of 'collections.OrderedDict' objects}
               14752155  982.275    0.000  982.275    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               42915360  144.480    0.000  973.069    0.000 utils.py:77(clamp_probs)
               42915360  567.993    0.000  955.530    0.000 layers.py:538(check)
               42915360  945.139    0.000  945.139    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
                1012884   17.640    0.000  898.554    0.001 layers.py:849(restart)
               42915360  159.195    0.000  889.091    0.000 utils.py:11(broadcast_all)
               42915360  828.589    0.000  828.589    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
               85830720  807.832    0.000  807.832    0.000 {built-in method broadcast_tensors}
              129751908  800.368    0.000  800.368    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
                1341105   77.067    0.000  776.846    0.001 replaybuffer.py:34(save_option_critic)
                1012884    8.058    0.000  768.097    0.001 level.py:8(__init__)
               42915360  766.085    0.000  766.085    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
              258162712  723.170    0.000  723.170    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               42915360  707.837    0.000  707.837    0.000 {built-in method clamp}
                1012884  119.510    0.000  697.363    0.001 levels.py:428(generate)
               26627993   42.534    0.000  696.127    0.000 <__array_function__ internals>:2(prod)
               85830720  677.604    0.000  677.604    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               43928213  645.663    0.000  645.663    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               26627993   39.702    0.000  644.071    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
               26627993   60.162    0.000  604.370    0.000 fromnumeric.py:2912(prod)
                 335276  454.700    0.001  587.269    0.002 replaybuffer.py:42(sample_option_critic)
               42915360  574.910    0.000  574.910    0.000 {built-in method bernoulli}
               26627993  139.115    0.000  544.208    0.000 fromnumeric.py:70(_wrapreduction)
               42915360  540.189    0.000  540.189    0.000 {built-in method all}
               18775464  524.400    0.000  524.400    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               42915360  523.358    0.000  523.358    0.000 {built-in method log}
               42915360  515.846    0.000  515.846    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
                5064420   68.431    0.000  462.096    0.000 level.py:41(notUsed)
                8046636  300.870    0.000  450.488    0.000 layer.py:159(update)
               42826601   46.080    0.000  423.772    0.000 {built-in method builtins.any}
                1341105   77.658    0.000  417.637    0.000 optimizer.py:189(zero_grad)
               42915360  382.265    0.000  382.265    0.000 {built-in method multinomial}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9632944: <Attempt8_Monsters_option_critic_2> in cluster <dcc> Done

Job <Attempt8_Monsters_option_critic_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed May 12 15:36:18 2021
Job was executed on host(s) <n-62-23-21>, in queue <hpc>, as user <s183914> in cluster <dcc> at Sun May 16 23:16:53 2021
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

    CPU time :                                   258890.91 sec.
    Max Memory :                                 785 MB
    Average Memory :                             772.69 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15599.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258978 sec.
    Turnaround time :                            632165 sec.

The output (if any) is above this job summary.

