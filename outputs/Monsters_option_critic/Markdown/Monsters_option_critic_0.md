[W NNPACK.cpp:80] Could not initialize NNPACK! Reason: Unsupported hardware.

# Parameters

    Name :                      Monsters_option_critic-0
    Main :                      option_critic_run
    Level :                     Levels.MonsterLevel
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


      35530236692 function calls (34444391843 primitive calls) in 258900.46 seconds

##    Ordered by: cumulative time
   List reduced from 435 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.465 258900.465 {built-in method builtins.exec}
                      1    0.309    0.309 258900.465 258900.465 <string>:1(<module>)
                      1 3992.468 3992.468 258900.156 258900.156 optionCritic.py:195(option_critic_run)
        1434867253/354042511 10545.287    0.000 109057.855    0.000 module.py:866(_call_impl)
               38614675 10187.600    0.000 108112.310    0.003 optionCritic.py:143(actor_loss_fn)
              120091638  817.961    0.000 99649.100    0.001 optionCritic.py:70(get_state)
              120091638 2772.014    0.000 96427.137    0.001 container.py:117(forward)
                1544587   12.015    0.000 78402.110    0.051 tensor.py:195(backward)
                1544587   14.966    0.000 78389.805    0.051 __init__.py:68(backward)
                1544587 78334.772    0.051 78334.772    0.051 {method 'run_backward' of 'torch._C._EngineBase' objects}
              240183276  899.804    0.000 57256.331    0.000 conv.py:398(forward)
              240183276  385.097    0.000 56011.901    0.000 conv.py:390(_conv_forward)
              240183276 55626.805    0.000 55626.805    0.000 {built-in method conv2d}
               38614675 4008.431    0.000 23747.315    0.001 optionCritic.py:91(get_action)
              474134149 1703.727    0.000 22247.923    0.000 linear.py:93(forward)
              474134149  616.850    0.000 19923.549    0.000 functional.py:1737(linear)
              474134149 19174.987    0.000 19174.987    0.000 {built-in method torch._C._nn.linear}
               38614675 1230.621    0.000 13233.251    0.000 optionCritic.py:80(predict_option_termination)
               77229350 1123.555    0.000 8646.879    0.000 distribution.py:34(__init__)
              360274914  484.618    0.000 8289.819    0.000 activation.py:713(forward)
               38614675  631.515    0.000 7811.028    0.000 categorical.py:115(log_prob)
              360274914  468.557    0.000 7805.201    0.000 functional.py:1364(leaky_relu)
              360274914 7234.257    0.000 7234.257    0.000 {built-in method torch._C._nn.leaky_relu}
                1544587   33.475    0.000 7031.780    0.005 optimizer.py:84(wrapper)
               38614675  910.133    0.000 7001.142    0.000 categorical.py:49(__init__)
                1544587   17.110    0.000 6901.066    0.004 grad_mode.py:24(decorate_context)
                1544587  107.252    0.000 6851.663    0.004 rmsprop.py:56(step)
                1544587  167.068    0.000 6628.587    0.004 _functional.py:203(rmsprop)
              117720702  479.141    0.000 6573.668    0.000 optionCritic.py:77(get_Q)
                 386146   87.204    0.000 6113.465    0.016 optionCritic.py:116(critic_loss_fn)
               77615496  462.292    0.000 5298.550    0.000 optionCritic.py:88(get_terminations)
               38614675  284.253    0.000 4657.853    0.000 bernoulli.py:34(__init__)
               21624212 4475.076    0.000 4475.076    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                1544587    9.299    0.000 4409.506    0.003 game.py:41(step)
               38614675 2882.078    0.000 4348.648    0.000 constraints.py:398(check)
                1544587   13.853    0.000 4291.993    0.003 layers.py:718(step)
               38614675  486.598    0.000 3294.991    0.000 distribution.py:240(_validate_sample)
              120091638  175.154    0.000 2366.199    0.000 activation.py:101(forward)
               38614675 1110.537    0.000 2283.977    0.000 categorical.py:123(entropy)
               38614675 2228.364    0.000 2228.364    0.000 constraints.py:249(check)
              120091638  147.372    0.000 2191.044    0.000 functional.py:1195(relu)
                1544588  153.924    0.000 2173.234    0.001 layers.py:684(update)
                1544587   71.207    0.000 2098.855    0.001 layers.py:17(step)
               38614675 2068.315    0.000 2068.315    0.000 constraints.py:364(check)
               38614675  164.161    0.000 2021.070    0.000 layer.py:98(move)
              120091638 2012.880    0.000 2012.880    0.000 {built-in method relu}
              115844025  240.410    0.000 1933.405    0.000 utils.py:106(__get__)
             1451857710 1878.343    0.000 1878.343    0.000 {built-in method torch._C._get_tracing_state}
              270302725 1828.608    0.000 1828.608    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               38614675  335.839    0.000 1778.977    0.000 bernoulli.py:86(sample)
              116616317  182.092    0.000 1692.930    0.000 tensor.py:525(__rsub__)
              120091638  137.909    0.000 1651.637    0.000 flatten.py:39(forward)
              115844025 1634.853    0.000 1634.853    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
             1860107556 1609.501    0.000 1609.656    0.000 module.py:934(__getattr__)
               38614675  211.608    0.000 1566.859    0.000 layers.py:735(check)
               38614675   75.491    0.000 1517.276    0.000 categorical.py:88(logits)
              120091638 1513.728    0.000 1513.728    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              116230171 1506.732    0.000 1506.732    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
              116616317 1478.072    0.000 1478.072    0.000 {built-in method rsub}
               38614675  380.137    0.000 1475.911    0.000 categorical.py:108(sample)
               38614675   76.068    0.000 1441.785    0.000 utils.py:82(probs_to_logits)
               77229350  407.014    0.000 1270.349    0.000 functional.py:46(broadcast_tensors)
               77615496 1218.015    0.000 1218.015    0.000 {method 'max' of 'torch._C._TensorBase' objects}
              115844025 1130.248    0.000 1130.248    0.000 {method 'all' of 'torch._C._TensorBase' objects}
             6081347491 1070.705    0.000 1084.321    0.000 {built-in method builtins.len}
               16990457   48.160    0.000 1059.238    0.000 tensor.py:575(__iter__)
               16990457  974.740    0.000  974.740    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
                1104409   18.358    0.000  970.428    0.001 layers.py:740(restart)
               38614675  174.242    0.000  911.064    0.000 utils.py:11(broadcast_all)
             5859560650  909.076    0.000  909.076    0.000 {method 'values' of 'collections.OrderedDict' objects}
               38614675  524.228    0.000  899.628    0.000 layers.py:538(check)
               38614675  145.966    0.000  883.999    0.000 utils.py:77(clamp_probs)
               38614675  834.103    0.000  834.103    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
                1104409    9.433    0.000  821.285    0.001 level.py:8(__init__)
               77229350  754.657    0.000  754.657    0.000 {built-in method broadcast_tensors}
                1104409  133.827    0.000  750.783    0.001 levels.py:413(generate)
               38614675  738.032    0.000  738.032    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
                1544587   77.319    0.000  734.507    0.000 replaybuffer.py:34(save_option_critic)
              117002463  731.698    0.000  731.698    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               13453716  347.739    0.000  725.131    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               21624212  706.208    0.000  706.208    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                 386146  542.033    0.001  701.927    0.002 replaybuffer.py:42(sample_option_critic)
               38614675  701.913    0.000  701.913    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
              232460342  638.268    0.000  638.268    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               38614675  637.100    0.000  637.100    0.000 {built-in method clamp}
               77229350  617.209    0.000  617.209    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               39719060  603.520    0.000  603.520    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               38614675  560.485    0.000  560.485    0.000 {built-in method bernoulli}
                5522045   72.679    0.000  489.651    0.000 level.py:41(notUsed)
               38614675  487.417    0.000  487.417    0.000 {built-in method all}
                1544587   93.688    0.000  487.289    0.000 optimizer.py:189(zero_grad)
               38614675  481.719    0.000  481.719    0.000 {built-in method log}
               21624212  480.616    0.000  480.616    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               38614675  478.347    0.000  478.347    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
                9267528  308.097    0.000  458.561    0.000 layer.py:151(update)
               38533254   45.465    0.000  427.244    0.000 {built-in method builtins.any}
               21624212  417.550    0.000  417.550    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               21624212  382.069    0.000  382.069    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              266663889  114.611    0.000  382.011    0.000 layers.py:700(<genexpr>)
               13453716   21.580    0.000  377.393    0.000 <__array_function__ internals>:2(prod)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9601884: <Monsters_option_critic_0> in cluster <dcc> Done

Job <Monsters_option_critic_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Thu Apr 29 21:41:23 2021
Job was executed on host(s) <n-62-23-23>, in queue <hpc>, as user <s183914> in cluster <dcc> at Thu Apr 29 21:41:26 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Apr 29 21:41:26 2021
Terminated at Sun May  2 21:36:28 2021
Results reported at Sun May  2 21:36:28 2021

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

    CPU time :                                   258894.31 sec.
    Max Memory :                                 786 MB
    Average Memory :                             768.78 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15598.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258964 sec.
    Turnaround time :                            258905 sec.

The output (if any) is above this job summary.

