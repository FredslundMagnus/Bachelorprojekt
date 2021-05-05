[W NNPACK.cpp:80] Could not initialize NNPACK! Reason: Unsupported hardware.

# Parameters

    Name :                      Coconuts_option_critic-1
    Main :                      option_critic_run
    Level :                     Levels.Coconuts
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


      33535807381 function calls (32482767116 primitive calls) in 258900.40 seconds

##    Ordered by: cumulative time
   List reduced from 437 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.400 258900.400 {built-in method builtins.exec}
                      1    0.293    0.293 258900.400 258900.400 <string>:1(<module>)
                      1 3801.858 3801.858 258900.107 258900.107 optionCritic.py:195(option_critic_run)
        1390762339/342590731 10333.068    0.000 106572.456    0.000 module.py:866(_call_impl)
               37448075 10017.706    0.000 105452.866    0.003 optionCritic.py:143(actor_loss_fn)
              116463512  772.807    0.000 97427.742    0.001 optionCritic.py:70(get_state)
              116463512 2724.443    0.000 94340.951    0.001 container.py:117(forward)
                1497923   11.920    0.000 76586.510    0.051 tensor.py:195(backward)
                1497923   13.856    0.000 76574.311    0.051 __init__.py:68(backward)
                1497923 76522.074    0.051 76522.074    0.051 {method 'run_backward' of 'torch._C._EngineBase' objects}
              232927024  882.133    0.000 56330.876    0.000 conv.py:398(forward)
              232927024  380.824    0.000 55114.726    0.000 conv.py:390(_conv_forward)
              232927024 54733.902    0.000 54733.902    0.000 {built-in method conv2d}
               37448075 3873.945    0.000 23032.489    0.001 optionCritic.py:91(get_action)
              459054243 1565.304    0.000 21583.508    0.000 linear.py:93(forward)
              459054243  604.343    0.000 19400.629    0.000 functional.py:1737(linear)
              459054243 18668.788    0.000 18668.788    0.000 {built-in method torch._C._nn.linear}
                1497923   33.129    0.000 13788.327    0.009 optimizer.py:84(wrapper)
                1497923   17.876    0.000 13657.204    0.009 grad_mode.py:24(decorate_context)
                1497923  105.665    0.000 13602.762    0.009 rmsprop.py:56(step)
                1497923  161.392    0.000 13381.299    0.009 _functional.py:203(rmsprop)
               37448075 1198.756    0.000 12925.906    0.000 optionCritic.py:80(predict_option_termination)
               20970916 10856.415    0.001 10856.415    0.001 {method 'sqrt' of 'torch._C._TensorBase' objects}
               74896150 1094.857    0.000 8453.648    0.000 distribution.py:34(__init__)
              349390536  453.101    0.000 7977.582    0.000 activation.py:713(forward)
               37448075  608.812    0.000 7547.383    0.000 categorical.py:115(log_prob)
              349390536  466.560    0.000 7524.482    0.000 functional.py:1364(leaky_relu)
              349390536 6962.161    0.000 6962.161    0.000 {built-in method torch._C._nn.leaky_relu}
               37448075  874.596    0.000 6803.717    0.000 categorical.py:49(__init__)
              113408514  470.799    0.000 6373.877    0.000 optionCritic.py:77(get_Q)
                 374480   84.971    0.000 6106.016    0.016 optionCritic.py:116(critic_loss_fn)
               75270630  444.051    0.000 5160.062    0.000 optionCritic.py:88(get_terminations)
               37448075  283.123    0.000 4570.026    0.000 bernoulli.py:34(__init__)
               37448075 2812.226    0.000 4235.469    0.000 constraints.py:398(check)
                1497923    8.779    0.000 3622.205    0.002 game.py:41(step)
                1497923   14.639    0.000 3509.316    0.002 layers.py:718(step)
               37448075  467.557    0.000 3205.456    0.000 distribution.py:240(_validate_sample)
              116463512  168.014    0.000 2270.643    0.000 activation.py:101(forward)
               37448075 1079.520    0.000 2227.616    0.000 categorical.py:123(entropy)
                1497923   67.284    0.000 2213.720    0.001 layers.py:17(step)
               37448075 2173.737    0.000 2173.737    0.000 constraints.py:249(check)
               37448075  225.760    0.000 2141.342    0.000 layer.py:98(move)
              116463512  147.398    0.000 2102.630    0.000 functional.py:1195(relu)
               37448075 2020.152    0.000 2020.152    0.000 constraints.py:364(check)
              116463512 1924.134    0.000 1924.134    0.000 {built-in method relu}
              112344225  221.148    0.000 1837.219    0.000 utils.py:106(__get__)
              262136525 1792.937    0.000 1792.937    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
             1407239492 1787.883    0.000 1787.883    0.000 {built-in method torch._C._get_tracing_state}
               37448075  307.206    0.000 1716.653    0.000 bernoulli.py:86(sample)
              113093185  186.830    0.000 1674.546    0.000 tensor.py:525(__rsub__)
             1801644202 1615.777    0.000 1615.929    0.000 module.py:934(__getattr__)
              112344225 1583.982    0.000 1583.982    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
              116463512  111.053    0.000 1564.010    0.000 flatten.py:39(forward)
              112718705 1457.832    0.000 1457.832    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
              113093185 1456.051    0.000 1456.051    0.000 {built-in method rsub}
               37448075   68.791    0.000 1454.729    0.000 categorical.py:88(logits)
              116463512 1452.958    0.000 1452.958    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               37448075  378.057    0.000 1438.218    0.000 categorical.py:108(sample)
               37448075  240.552    0.000 1420.205    0.000 layers.py:735(check)
               37448075   74.682    0.000 1385.938    0.000 utils.py:82(probs_to_logits)
                1497924  141.844    0.000 1274.986    0.001 layers.py:684(update)
               74896150  388.489    0.000 1231.468    0.000 functional.py:46(broadcast_tensors)
               75270630 1213.211    0.000 1213.211    0.000 {method 'max' of 'torch._C._TensorBase' objects}
              112344225 1102.726    0.000 1102.726    0.000 {method 'all' of 'torch._C._TensorBase' objects}
               20970916 1080.484    0.000 1080.484    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
             5997664922 1043.610    0.000 1056.878    0.000 {built-in method builtins.len}
               16477153   46.331    0.000 1046.230    0.000 tensor.py:575(__iter__)
               16477153  965.317    0.000  965.317    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
             5679512868  896.761    0.000  896.761    0.000 {method 'values' of 'collections.OrderedDict' objects}
               37448075  178.524    0.000  870.055    0.000 utils.py:11(broadcast_all)
               37448075  132.629    0.000  842.008    0.000 utils.py:77(clamp_probs)
               37448075  812.772    0.000  812.772    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               74896150  739.164    0.000  739.164    0.000 {built-in method broadcast_tensors}
              113467665  719.243    0.000  719.243    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               37448075  709.378    0.000  709.378    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
                1497923   76.880    0.000  707.208    0.000 replaybuffer.py:34(save_option_critic)
                 374480  524.888    0.001  681.779    0.002 replaybuffer.py:42(sample_option_critic)
               37448075  677.620    0.000  677.620    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
               12232399  305.210    0.000  638.241    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
              225437410  628.270    0.000  628.270    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               37448075  626.532    0.000  626.532    0.000 {built-in method clamp}
               74896150  597.808    0.000  597.808    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               37763404  578.393    0.000  578.393    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               37448075  536.901    0.000  536.901    0.000 {built-in method bernoulli}
               20970916  482.476    0.000  482.476    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               37448075  478.568    0.000  478.568    0.000 {built-in method all}
                1497923   92.198    0.000  477.299    0.000 optimizer.py:189(zero_grad)
               37448075  469.248    0.000  469.248    0.000 {built-in method log}
               37448075  458.841    0.000  458.841    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
               37448075  315.544    0.000  426.309    0.000 layers.py:471(check)
               20970916  414.140    0.000  414.140    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               20970916  386.393    0.000  386.393    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               10485468  248.308    0.000  384.316    0.000 layer.py:151(update)
               37448075  291.906    0.000  384.092    0.000 layers.py:77(check)
               37448075   81.590    0.000  362.332    0.000 layers.py:729(isFree)
                 315353    6.359    0.000  349.660    0.001 layers.py:740(restart)
              494547746  231.306    0.000  340.816    0.000 {built-in method builtins.isinstance}
               37448075  338.535    0.000  338.535    0.000 {built-in method multinomial}
               12232399   19.652    0.000  333.032    0.000 <__array_function__ internals>:2(prod)
               10110982  328.029    0.000  328.029    0.000 {built-in method tensor}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9601882: <Coconuts_option_critic_1> in cluster <dcc> Done

Job <Coconuts_option_critic_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Thu Apr 29 21:41:22 2021
Job was executed on host(s) <n-62-23-21>, in queue <hpc>, as user <s183914> in cluster <dcc> at Thu Apr 29 21:41:24 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Apr 29 21:41:24 2021
Terminated at Sun May  2 21:36:27 2021
Results reported at Sun May  2 21:36:27 2021

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

    CPU time :                                   258896.70 sec.
    Max Memory :                                 869 MB
    Average Memory :                             860.74 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15515.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258963 sec.
    Turnaround time :                            258905 sec.

The output (if any) is above this job summary.

