
# Parameters

    Name :                      Attempt6_Diamonds2_option_critic-2
    Main :                      option_critic_run
    Level :                     Levels.Causal5
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


      32150201481 function calls (31213220771 primitive calls) in 258900.71 seconds

##    Ordered by: cumulative time
   List reduced from 430 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.710 258900.710 {built-in method builtins.exec}
                      1    0.303    0.303 258900.710 258900.710 <string>:1(<module>)
                      1 3247.677 3247.677 258900.407 258900.407 optionCritic.py:195(option_critic_run)
                1050426    7.830    0.000 153226.114    0.146 tensor.py:195(backward)
                1050426    9.815    0.000 153218.147    0.146 __init__.py:68(backward)
                1050426 153187.249    0.146 153187.249    0.146 {method 'run_backward' of 'torch._C._EngineBase' objects}
        1241217099/307650996 5754.708    0.000 65331.328    0.000 module.py:866(_call_impl)
               33613632 4892.178    0.000 65296.309    0.002 optionCritic.py:143(actor_loss_fn)
              103729567  491.544    0.000 60839.850    0.001 optionCritic.py:70(get_state)
              103729567 1341.631    0.000 58903.106    0.001 container.py:117(forward)
              207459134  556.522    0.000 36889.040    0.000 conv.py:398(forward)
              207459134  302.644    0.000 36106.918    0.000 conv.py:390(_conv_forward)
              207459134 35804.274    0.000 35804.274    0.000 {built-in method conv2d}
              411380563  990.524    0.000 12945.820    0.000 linear.py:93(forward)
               33613632 1924.092    0.000 11569.167    0.000 optionCritic.py:91(get_action)
              411380563  387.058    0.000 11555.204    0.000 functional.py:1737(linear)
              411380563 11075.808    0.000 11075.808    0.000 {built-in method torch._C._nn.linear}
               33613632  695.379    0.000 8124.890    0.000 optionCritic.py:80(predict_option_termination)
                1050426   23.827    0.000 4692.269    0.004 optimizer.py:84(wrapper)
                1050426   12.033    0.000 4606.179    0.004 grad_mode.py:24(decorate_context)
                1050426   62.168    0.000 4572.345    0.004 adam.py:55(step)
               67227264  713.281    0.000 4554.037    0.000 distribution.py:34(__init__)
                1050426  360.262    0.000 4442.599    0.004 _functional.py:53(adam)
              311188701  309.550    0.000 4218.784    0.000 activation.py:713(forward)
              311188701  334.048    0.000 3909.234    0.000 functional.py:1364(leaky_relu)
               33613632  329.854    0.000 3871.202    0.000 categorical.py:115(log_prob)
              311188701 3510.238    0.000 3510.238    0.000 {built-in method torch._C._nn.leaky_relu}
              102817927  244.999    0.000 3354.268    0.000 optionCritic.py:77(get_Q)
               33613632  439.492    0.000 3242.278    0.000 categorical.py:49(__init__)
               33613632  248.845    0.000 3151.339    0.000 bernoulli.py:34(__init__)
                1050426    5.985    0.000 3026.321    0.003 game.py:42(step)
                1050426    8.960    0.000 2952.553    0.003 layers.py:827(step)
               67489870  238.159    0.000 2561.688    0.000 optionCritic.py:88(get_terminations)
                 262606   41.350    0.000 2509.119    0.010 optionCritic.py:116(critic_loss_fn)
               33613632 1325.031    0.000 1971.596    0.000 constraints.py:398(check)
                1050427   93.935    0.000 1661.837    0.002 layers.py:793(update)
               33613632  272.957    0.000 1561.203    0.000 distribution.py:240(_validate_sample)
                1050426   45.768    0.000 1277.052    0.001 layers.py:17(step)
               33613632   79.002    0.000 1227.193    0.000 layer.py:106(move)
               33613632 1225.278    0.000 1225.278    0.000 constraints.py:364(check)
              103729567  133.493    0.000 1218.335    0.000 activation.py:101(forward)
               33613632  231.322    0.000 1166.014    0.000 bernoulli.py:86(sample)
              103729567  110.618    0.000 1084.842    0.000 functional.py:1195(relu)
               33613632  555.046    0.000 1072.600    0.000 categorical.py:123(entropy)
             1612694279 1070.755    0.000 1070.831    0.000 module.py:934(__getattr__)
               33613632 1008.713    0.000 1008.713    0.000 constraints.py:249(check)
              100840896  130.411    0.000  967.469    0.000 utils.py:106(__get__)
               29411916  964.414    0.000  964.414    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              103729567  956.669    0.000  956.669    0.000 {built-in method relu}
                1451852   20.531    0.000  953.261    0.001 layers.py:849(restart)
              103729567  100.794    0.000  949.885    0.000 flatten.py:39(forward)
              235295424  931.862    0.000  931.862    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              101366108  106.906    0.000  923.788    0.000 tensor.py:525(__rsub__)
               33613632  184.754    0.000  851.208    0.000 layers.py:844(check)
              103729567  849.091    0.000  849.091    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               67227264  298.850    0.000  846.222    0.000 functional.py:46(broadcast_tensors)
              101366108  799.588    0.000  799.588    0.000 {built-in method rsub}
                1451852    9.530    0.000  798.521    0.001 level.py:8(__init__)
               14705958  793.775    0.000  793.775    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               14705958  761.399    0.000  761.399    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               33613632  208.215    0.000  757.686    0.000 categorical.py:108(sample)
               33613632   37.813    0.000  736.441    0.000 categorical.py:88(logits)
               67489870  730.133    0.000  730.133    0.000 {method 'max' of 'torch._C._TensorBase' objects}
              101103502  722.360    0.000  722.360    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
             1252771785  721.290    0.000  721.290    0.000 {built-in method torch._C._get_tracing_state}
                1451852   28.366    0.000  716.038    0.000 levels.py:249(generate)
               33613632   43.277    0.000  698.628    0.000 utils.py:82(probs_to_logits)
               33613632  144.402    0.000  693.946    0.000 utils.py:11(broadcast_all)
               11554686   25.917    0.000  692.086    0.000 tensor.py:575(__iter__)
             5438213688  669.347    0.000  676.667    0.000 {built-in method builtins.len}
              100840896  671.110    0.000  671.110    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                9438107  113.432    0.000  657.706    0.000 level.py:41(notUsed)
               11554686  649.986    0.000  649.986    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
              100840896  565.098    0.000  565.098    0.000 {method 'all' of 'torch._C._TensorBase' objects}
             5068597963  560.468    0.000  560.468    0.000 {method 'values' of 'collections.OrderedDict' objects}
               14705958  526.040    0.000  526.040    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               29411916  517.446    0.000  517.446    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               14705958  513.809    0.000  513.809    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               33613632  512.265    0.000  512.265    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
                 262606  402.181    0.002  499.751    0.002 replaybuffer.py:42(sample_option_critic)
               67227264  461.411    0.000  461.411    0.000 {built-in method broadcast_tensors}
               33613632   84.262    0.000  410.598    0.000 utils.py:77(clamp_probs)
                1050426   46.972    0.000  403.873    0.000 replaybuffer.py:34(save_option_critic)
              101628714  369.267    0.000  369.267    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               33613632  364.034    0.000  364.034    0.000 {built-in method bernoulli}
               33613632  334.015    0.000  334.015    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
               35065451  330.969    0.000  330.969    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               33613632  326.336    0.000  326.336    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
             1062522419  218.914    0.000  320.408    0.000 enum.py:646(__hash__)
                9438107    9.131    0.000  318.467    0.000 level.py:38(elementsIn)
              202207004  316.959    0.000  316.959    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                9453843  183.475    0.000  305.588    0.000 layer.py:175(NoRock_update)
               67227264  281.237    0.000  281.237    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               33613632  277.693    0.000  277.693    0.000 {built-in method clamp}
                1050426   49.328    0.000  273.551    0.000 optimizer.py:189(zero_grad)
               33613632   55.722    0.000  245.880    0.000 layers.py:838(isFree)
               33613632  244.753    0.000  244.753    0.000 {built-in method log}
               33613632  237.025    0.000  237.025    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
              103729581  219.133    0.000  219.133    0.000 {method 'to' of 'torch._C._TensorBase' objects}
              100840928   65.452    0.000  216.771    0.000 {built-in method builtins.all}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9624152: <Attempt6_Diamonds2_option_critic_2> in cluster <dcc> Done

Job <Attempt6_Diamonds2_option_critic_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun May  9 01:22:26 2021
Job was executed on host(s) <n-62-11-60>, in queue <hpc>, as user <s183914> in cluster <dcc> at Sun May  9 01:22:27 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun May  9 01:22:27 2021
Terminated at Wed May 12 01:17:34 2021
Results reported at Wed May 12 01:17:34 2021

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

    CPU time :                                   258289.59 sec.
    Max Memory :                                 1014 MB
    Average Memory :                             1004.41 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15370.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258956 sec.
    Turnaround time :                            258908 sec.

The output (if any) is above this job summary.

