[W NNPACK.cpp:80] Could not initialize NNPACK! Reason: Unsupported hardware.

# Parameters

    Name :                      Monsters_option_critic-1
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


      35551185831 function calls (34458878980 primitive calls) in 258900.53 seconds

##    Ordered by: cumulative time
   List reduced from 434 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.531 258900.531 {built-in method builtins.exec}
                      1    0.318    0.318 258900.531 258900.531 <string>:1(<module>)
                      1 4090.565 4090.565 258900.213 258900.213 optionCritic.py:195(option_critic_run)
        1443397719/356140875 10977.800    0.000 111273.842    0.000 module.py:866(_call_impl)
               38844475 10392.220    0.000 110504.504    0.003 optionCritic.py:143(actor_loss_fn)
              120806316  796.153    0.000 101454.077    0.001 optionCritic.py:70(get_state)
              120806316 2901.674    0.000 98204.032    0.001 container.py:117(forward)
                1553779   12.027    0.000 77554.085    0.050 tensor.py:195(backward)
                1553779   14.750    0.000 77541.769    0.050 __init__.py:68(backward)
                1553779 77487.270    0.050 77487.270    0.050 {method 'run_backward' of 'torch._C._EngineBase' objects}
              241612632  932.118    0.000 57920.161    0.000 conv.py:398(forward)
              241612632  407.001    0.000 56632.080    0.000 conv.py:390(_conv_forward)
              241612632 56225.079    0.000 56225.079    0.000 {built-in method conv2d}
               38844475 4114.049    0.000 24346.702    0.001 optionCritic.py:91(get_action)
              476947191 1669.927    0.000 22891.940    0.000 linear.py:93(forward)
              476947191  654.936    0.000 20566.272    0.000 functional.py:1737(linear)
              476947191 19772.280    0.000 19772.280    0.000 {built-in method torch._C._nn.linear}
               38844475 1276.327    0.000 13730.834    0.000 optionCritic.py:80(predict_option_termination)
               77688950 1161.382    0.000 8967.803    0.000 distribution.py:34(__init__)
              362418948  442.273    0.000 8480.778    0.000 activation.py:713(forward)
              362418948  515.915    0.000 8038.505    0.000 functional.py:1364(leaky_relu)
               38844475  642.945    0.000 7989.385    0.000 categorical.py:115(log_prob)
              362418948 7423.455    0.000 7423.455    0.000 {built-in method torch._C._nn.leaky_relu}
               38844475  927.270    0.000 7196.644    0.000 categorical.py:49(__init__)
              118412690  551.253    0.000 6905.337    0.000 optionCritic.py:77(get_Q)
                 388444   88.020    0.000 6165.043    0.016 optionCritic.py:116(critic_loss_fn)
               78077394  476.743    0.000 5480.822    0.000 optionCritic.py:88(get_terminations)
               38844475  295.935    0.000 4848.772    0.000 bernoulli.py:34(__init__)
               38844475 3004.310    0.000 4495.847    0.000 constraints.py:398(check)
                1553779    9.382    0.000 4362.303    0.003 game.py:41(step)
                1553779   13.521    0.000 4243.272    0.003 layers.py:718(step)
                1553779   34.027    0.000 4066.273    0.003 optimizer.py:84(wrapper)
                1553779   16.135    0.000 3933.548    0.003 grad_mode.py:24(decorate_context)
                1553779  110.975    0.000 3883.341    0.002 rmsprop.py:56(step)
                1553779  165.136    0.000 3650.907    0.002 _functional.py:203(rmsprop)
               38844475  498.076    0.000 3389.396    0.000 distribution.py:240(_validate_sample)
              120806316  170.296    0.000 2420.214    0.000 activation.py:101(forward)
               38844475 1134.463    0.000 2331.641    0.000 categorical.py:123(entropy)
               38844475 2296.919    0.000 2296.919    0.000 constraints.py:249(check)
              120806316  153.874    0.000 2249.918    0.000 functional.py:1195(relu)
               38844475 2180.115    0.000 2180.115    0.000 constraints.py:364(check)
                1553780  155.137    0.000 2113.617    0.001 layers.py:684(update)
                1553779   70.444    0.000 2110.019    0.001 layers.py:17(step)
              120806316 2065.086    0.000 2065.086    0.000 {built-in method relu}
               38844475  162.434    0.000 2034.306    0.000 layer.py:98(move)
              116533425  228.708    0.000 1947.578    0.000 utils.py:106(__get__)
             1460489288 1928.181    0.000 1928.181    0.000 {built-in method torch._C._get_tracing_state}
              271911325 1873.066    0.000 1873.066    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               38844475  325.915    0.000 1810.079    0.000 bernoulli.py:86(sample)
              117310313  197.960    0.000 1764.488    0.000 tensor.py:525(__rsub__)
             1871151512 1718.282    0.000 1718.441    0.000 module.py:934(__getattr__)
               21752900 1678.501    0.000 1678.501    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              120806316  118.230    0.000 1671.823    0.000 flatten.py:39(forward)
              116533425 1665.106    0.000 1665.106    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
               38844475  216.538    0.000 1588.258    0.000 layers.py:735(check)
              120806316 1553.593    0.000 1553.593    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              116921869 1551.596    0.000 1551.596    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
               38844475   75.155    0.000 1544.336    0.000 categorical.py:88(logits)
              117310313 1532.744    0.000 1532.744    0.000 {built-in method rsub}
               38844475  395.142    0.000 1516.312    0.000 categorical.py:108(sample)
               38844475   80.179    0.000 1469.181    0.000 utils.py:82(probs_to_logits)
               77688950  419.818    0.000 1310.838    0.000 functional.py:46(broadcast_tensors)
               78077394 1247.433    0.000 1247.433    0.000 {method 'max' of 'torch._C._TensorBase' objects}
              116533425 1147.743    0.000 1147.743    0.000 {method 'all' of 'torch._C._TensorBase' objects}
             6117015355 1074.230    0.000 1088.374    0.000 {built-in method builtins.len}
               17091569   48.833    0.000 1077.049    0.000 tensor.py:575(__iter__)
               17091569  991.879    0.000  991.879    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
                1102402   19.022    0.000  968.631    0.001 layers.py:740(restart)
             5894397192  942.958    0.000  942.958    0.000 {method 'values' of 'collections.OrderedDict' objects}
               38844475  183.325    0.000  929.807    0.000 utils.py:11(broadcast_all)
               38844475  540.378    0.000  918.017    0.000 layers.py:538(check)
               38844475  140.554    0.000  894.323    0.000 utils.py:77(clamp_probs)
               38844475  856.880    0.000  856.880    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
                1102402    9.003    0.000  820.966    0.001 level.py:8(__init__)
               77688950  782.099    0.000  782.099    0.000 {built-in method broadcast_tensors}
               13801028  367.091    0.000  763.465    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
              117698757  756.864    0.000  756.864    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               38844475  753.770    0.000  753.770    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
                1553779   80.475    0.000  751.983    0.000 replaybuffer.py:34(save_option_critic)
                1102402  133.774    0.000  751.726    0.001 levels.py:413(generate)
               38844475  714.048    0.000  714.048    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
                 388444  552.313    0.001  712.160    0.002 replaybuffer.py:42(sample_option_critic)
              233843738  649.845    0.000  649.845    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               38844475  649.608    0.000  649.608    0.000 {built-in method clamp}
               77688950  629.241    0.000  629.241    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               39946852  617.478    0.000  617.478    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               38844475  567.215    0.000  567.215    0.000 {built-in method bernoulli}
               21752900  552.237    0.000  552.237    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                1553779  100.802    0.000  508.934    0.000 optimizer.py:189(zero_grad)
               38844475  502.938    0.000  502.938    0.000 {built-in method all}
               38844475  494.679    0.000  494.679    0.000 {built-in method log}
                5512010   71.931    0.000  490.541    0.000 level.py:41(notUsed)
               38844475  478.441    0.000  478.441    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
               21752900  464.868    0.000  464.868    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                9322680  305.935    0.000  453.733    0.000 layer.py:151(update)
               38762513   45.307    0.000  420.494    0.000 {built-in method builtins.any}
               21752900  402.728    0.000  402.728    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               13801028   22.601    0.000  396.373    0.000 <__array_function__ internals>:2(prod)
               21752900  387.437    0.000  387.437    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              268276346  116.712    0.000  375.422    0.000 layers.py:700(<genexpr>)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9601885: <Monsters_option_critic_1> in cluster <dcc> Done

Job <Monsters_option_critic_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Thu Apr 29 21:41:24 2021
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

    CPU time :                                   258894.17 sec.
    Max Memory :                                 784 MB
    Average Memory :                             771.54 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15600.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258964 sec.
    Turnaround time :                            258904 sec.

The output (if any) is above this job summary.

