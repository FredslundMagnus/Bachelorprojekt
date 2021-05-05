[W NNPACK.cpp:80] Could not initialize NNPACK! Reason: Unsupported hardware.

# Parameters

    Name :                      SuperLevel1_option_critic-2
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


      30804681622 function calls (29908724425 primitive calls) in 258900.80 seconds

##    Ordered by: cumulative time
   List reduced from 443 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.802 258900.802 {built-in method builtins.exec}
                      1    0.341    0.341 258900.802 258900.802 <string>:1(<module>)
                      1 3377.206 3377.206 258900.461 258900.461 optionCritic.py:195(option_critic_run)
        1183442579/291627989 8883.508    0.000 112322.842    0.000 module.py:866(_call_impl)
               31861900 8725.846    0.000 105626.754    0.003 optionCritic.py:143(actor_loss_fn)
               99090510  654.328    0.000 104217.565    0.001 optionCritic.py:70(get_state)
               99090510 2425.700    0.000 101527.296    0.001 container.py:117(forward)
                1274476   10.657    0.000 87211.352    0.068 tensor.py:195(backward)
                1274476   11.779    0.000 87200.437    0.068 __init__.py:68(backward)
                1274476 87155.109    0.068 87155.109    0.068 {method 'run_backward' of 'torch._C._EngineBase' objects}
              198181020  776.713    0.000 68226.925    0.000 conv.py:398(forward)
              198181020  332.718    0.000 67156.765    0.000 conv.py:390(_conv_forward)
              198181020 66824.048    0.000 66824.048    0.000 {built-in method conv2d}
               31861900 3432.319    0.000 20112.201    0.001 optionCritic.py:91(get_action)
              390718499 1395.017    0.000 19080.818    0.000 linear.py:93(forward)
              390718499  498.895    0.000 17135.499    0.000 functional.py:1737(linear)
              390718499 16531.352    0.000 16531.352    0.000 {built-in method torch._C._nn.linear}
               31861900 1041.322    0.000 11379.195    0.000 optionCritic.py:80(predict_option_termination)
                 318619   75.353    0.000 7737.716    0.024 optionCritic.py:116(critic_loss_fn)
               63723800  967.930    0.000 7401.585    0.000 distribution.py:34(__init__)
              297271530  385.265    0.000 7048.086    0.000 activation.py:713(forward)
              297271530  376.050    0.000 6662.821    0.000 functional.py:1364(leaky_relu)
               31861900  527.150    0.000 6557.457    0.000 categorical.py:115(log_prob)
              297271530 6203.751    0.000 6203.751    0.000 {built-in method torch._C._nn.leaky_relu}
               31861900  762.868    0.000 5925.764    0.000 categorical.py:49(__init__)
               96633160  400.145    0.000 5621.869    0.000 optionCritic.py:77(get_Q)
               64042419  399.482    0.000 4553.037    0.000 optionCritic.py:88(get_terminations)
                1274476    8.464    0.000 4337.961    0.003 game.py:41(step)
                1274476   11.428    0.000 4222.916    0.003 layers.py:718(step)
               31861900  255.498    0.000 4071.938    0.000 bernoulli.py:34(__init__)
                1274476   28.591    0.000 3762.723    0.003 optimizer.py:84(wrapper)
               31861900 2456.592    0.000 3700.011    0.000 constraints.py:398(check)
                1274476   13.425    0.000 3649.448    0.003 grad_mode.py:24(decorate_context)
                1274476   91.422    0.000 3607.915    0.003 rmsprop.py:56(step)
                1274476  137.530    0.000 3420.181    0.003 _functional.py:203(rmsprop)
                1274476   57.412    0.000 2975.754    0.002 layers.py:17(step)
               31861900  199.494    0.000 2914.038    0.000 layer.py:98(move)
               31861900  404.902    0.000 2772.768    0.000 distribution.py:240(_validate_sample)
               31861900  354.198    0.000 2077.603    0.000 layers.py:735(check)
               99090510  149.530    0.000 2008.585    0.000 activation.py:101(forward)
               31861900  956.175    0.000 1953.341    0.000 categorical.py:123(entropy)
               31861900 1876.627    0.000 1876.627    0.000 constraints.py:249(check)
               99090510  127.679    0.000 1859.055    0.000 functional.py:1195(relu)
               31861900 1790.418    0.000 1790.418    0.000 constraints.py:364(check)
               99090510 1706.231    0.000 1706.231    0.000 {built-in method relu}
               95585700  186.121    0.000 1601.893    0.000 utils.py:106(__get__)
             1197461815 1580.032    0.000 1580.032    0.000 {built-in method torch._C._get_tracing_state}
               17842658 1549.178    0.000 1549.178    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              223033300 1542.953    0.000 1542.953    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               31861900  281.003    0.000 1513.156    0.000 bernoulli.py:86(sample)
               96222938  154.517    0.000 1466.750    0.000 tensor.py:525(__rsub__)
             1533316572 1401.179    0.000 1401.310    0.000 module.py:934(__getattr__)
               95585700 1381.853    0.000 1381.853    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
               99090510   98.152    0.000 1362.395    0.000 flatten.py:39(forward)
               96222938 1285.165    0.000 1285.165    0.000 {built-in method rsub}
               95904319 1279.474    0.000 1279.474    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
               31861900   63.127    0.000 1275.688    0.000 categorical.py:88(logits)
               99090510 1264.243    0.000 1264.243    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               31861900  331.293    0.000 1253.917    0.000 categorical.py:108(sample)
                1274477  129.503    0.000 1230.631    0.001 layers.py:684(update)
               31861900   64.693    0.000 1212.561    0.000 utils.py:82(probs_to_logits)
               63723800  356.718    0.000 1111.529    0.000 functional.py:46(broadcast_tensors)
               64042419 1050.348    0.000 1050.348    0.000 {method 'max' of 'torch._C._TensorBase' objects}
               95585700  960.508    0.000  960.508    0.000 {method 'all' of 'torch._C._TensorBase' objects}
             5304978783  914.214    0.000  925.960    0.000 {built-in method builtins.len}
               14019236   41.719    0.000  914.977    0.000 tensor.py:575(__iter__)
               14019236  842.966    0.000  842.966    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               31861900  160.485    0.000  801.452    0.000 utils.py:11(broadcast_all)
             4832860826  756.601    0.000  756.601    0.000 {method 'values' of 'collections.OrderedDict' objects}
               31861900  114.844    0.000  740.133    0.000 utils.py:77(clamp_probs)
               13212868  341.486    0.000  718.819    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               31861900  708.336    0.000  708.336    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               63723800  647.663    0.000  647.663    0.000 {built-in method broadcast_tensors}
               31861900  625.289    0.000  625.289    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
               96541557  616.943    0.000  616.943    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
                1274476   64.705    0.000  613.483    0.000 replaybuffer.py:34(save_option_critic)
                 318619  447.496    0.001  595.591    0.002 replaybuffer.py:42(sample_option_critic)
               31861900  594.999    0.000  594.999    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
              191808638  548.902    0.000  548.902    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               31861900  546.886    0.000  546.886    0.000 {built-in method clamp}
               31861900  122.153    0.000  525.142    0.000 layers.py:729(isFree)
               16568201  327.896    0.000  521.647    0.000 layer.py:151(update)
               63723800  515.051    0.000  515.051    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               32272122  508.726    0.000  508.726    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               17842658  497.880    0.000  497.880    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               31861900  360.755    0.000  482.043    0.000 layers.py:471(check)
               31861900  473.585    0.000  473.585    0.000 {built-in method bernoulli}
               17842658  461.335    0.000  461.335    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               17842658  439.294    0.000  439.294    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                1274476   80.816    0.000  435.285    0.000 optimizer.py:189(zero_grad)
               31861900  420.021    0.000  420.021    0.000 {built-in method all}
               31861900  407.735    0.000  407.735    0.000 {built-in method log}
              345401174  319.285    0.000  402.990    0.000 layer.py:95(isFree)
               31861900  398.256    0.000  398.256    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
               13212868   21.690    0.000  377.333    0.000 <__array_function__ internals>:2(prod)
              987933722  255.702    0.000  367.536    0.000 enum.py:646(__hash__)
               13212868   21.996    0.000  351.142    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
               17842658  334.963    0.000  334.963    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               31861900  250.461    0.000  332.080    0.000 layers.py:77(check)
                8602717  331.090    0.000  331.090    0.000 {built-in method tensor}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9601871: <SuperLevel1_option_critic_2> in cluster <dcc> Done

Job <SuperLevel1_option_critic_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Thu Apr 29 21:41:14 2021
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

Successfully completed.

Resource usage summary:

    CPU time :                                   258896.50 sec.
    Max Memory :                                 1331 MB
    Average Memory :                             1320.24 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15053.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258959 sec.
    Turnaround time :                            258909 sec.

The output (if any) is above this job summary.

