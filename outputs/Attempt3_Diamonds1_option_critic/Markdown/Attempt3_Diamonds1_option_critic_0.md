[W NNPACK.cpp:80] Could not initialize NNPACK! Reason: Unsupported hardware.

# Parameters

    Name :                      Attempt3_Diamonds1_option_critic-0
    Main :                      option_critic_run
    Level :                     Levels.Causal2
    Failed actions chance :     0
    Use model :                 True
    Depth :                     3
    Model explore :             1000000
    Samples :                   5
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
    Minutes used :              4315 minutes.
    Hours used :                71 hours.

# Profiling


      32742732890 function calls (31694957687 primitive calls) in 258900.89 seconds

##    Ordered by: cumulative time
   List reduced from 433 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.885 258900.885 {built-in method builtins.exec}
                      1    0.322    0.322 258900.885 258900.885 <string>:1(<module>)
                      1 3729.653 3729.653 258900.563 258900.563 optionCritic.py:195(option_critic_run)
               37648300 9750.495    0.000 106592.630    0.003 optionCritic.py:143(actor_loss_fn)
        1390620290/342943394 9969.946    0.000 104678.040    0.000 module.py:866(_call_impl)
              116408544  845.369    0.000 95810.166    0.001 optionCritic.py:70(get_state)
              116408544 2814.861    0.000 92702.352    0.001 container.py:117(forward)
                1505932   11.257    0.000 66747.098    0.044 tensor.py:195(backward)
                1505932   13.216    0.000 66735.547    0.044 __init__.py:68(backward)
                1505932 66685.190    0.044 66685.190    0.044 {method 'run_backward' of 'torch._C._EngineBase' objects}
              232817088  891.290    0.000 55692.421    0.000 conv.py:398(forward)
              232817088  376.242    0.000 54491.913    0.000 conv.py:390(_conv_forward)
              232817088 54115.672    0.000 54115.672    0.000 {built-in method conv2d}
                1505932   32.206    0.000 28689.982    0.019 optimizer.py:84(wrapper)
                1505932   17.662    0.000 28559.058    0.019 grad_mode.py:24(decorate_context)
                1505932  106.947    0.000 28509.155    0.019 rmsprop.py:56(step)
                1505932  162.172    0.000 28274.507    0.019 _functional.py:203(rmsprop)
               21083030 25070.383    0.001 25070.383    0.001 {method 'sqrt' of 'torch._C._TensorBase' objects}
               37648300 3753.741    0.000 22469.552    0.001 optionCritic.py:91(get_action)
              459351938 1558.562    0.000 20912.326    0.000 linear.py:93(forward)
              459351938  562.666    0.000 18776.907    0.000 functional.py:1737(linear)
              459351938 18100.056    0.000 18100.056    0.000 {built-in method torch._C._nn.linear}
               37648300 1158.888    0.000 12596.041    0.000 optionCritic.py:80(predict_option_termination)
               75296600 1054.078    0.000 8226.958    0.000 distribution.py:34(__init__)
              349225632  415.667    0.000 7799.914    0.000 activation.py:713(forward)
              349225632  424.781    0.000 7384.247    0.000 functional.py:1364(leaky_relu)
               37648300  609.076    0.000 7360.827    0.000 categorical.py:115(log_prob)
              349225632 6869.606    0.000 6869.606    0.000 {built-in method torch._C._nn.leaky_relu}
               37648300  870.885    0.000 6624.105    0.000 categorical.py:49(__init__)
              113439357  462.913    0.000 6217.453    0.000 optionCritic.py:77(get_Q)
               75447193  451.785    0.000 5086.724    0.000 optionCritic.py:88(get_terminations)
               37648300  266.369    0.000 4446.320    0.000 bernoulli.py:34(__init__)
               37648300 2721.219    0.000 4130.447    0.000 constraints.py:398(check)
               37648300  460.981    0.000 3061.769    0.000 distribution.py:240(_validate_sample)
                1505932    8.931    0.000 2897.503    0.002 game.py:42(step)
                1505932   14.252    0.000 2784.149    0.002 layers.py:827(step)
                 150593   33.644    0.000 2523.666    0.017 optionCritic.py:116(critic_loss_fn)
              116408544  152.369    0.000 2214.368    0.000 activation.py:101(forward)
               37648300 1057.363    0.000 2196.832    0.000 categorical.py:123(entropy)
              116408544  141.295    0.000 2062.000    0.000 functional.py:1195(relu)
               37648300 2048.666    0.000 2048.666    0.000 constraints.py:249(check)
               37648300 1987.589    0.000 1987.589    0.000 constraints.py:364(check)
               21083030 1951.536    0.000 1951.536    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              116408544 1892.381    0.000 1892.381    0.000 {built-in method relu}
              112944900  201.990    0.000 1817.083    0.000 utils.py:106(__get__)
             1407185542 1784.251    0.000 1784.251    0.000 {built-in method torch._C._get_tracing_state}
                1505932   64.891    0.000 1777.918    0.001 layers.py:17(step)
              263538100 1730.889    0.000 1730.889    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               37648300  117.978    0.000 1707.597    0.000 layer.py:106(move)
               37648300  304.234    0.000 1680.662    0.000 bernoulli.py:86(sample)
              113246086  181.977    0.000 1638.249    0.000 tensor.py:525(__rsub__)
              112944900 1561.219    0.000 1561.219    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
             1802582019 1521.035    0.000 1521.038    0.000 module.py:934(__getattr__)
              116408544  112.891    0.000 1520.980    0.000 flatten.py:39(forward)
               37648300   76.146    0.000 1457.477    0.000 categorical.py:88(logits)
              113246086 1424.300    0.000 1424.300    0.000 {built-in method rsub}
              113095493 1424.223    0.000 1424.223    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
              116408544 1408.089    0.000 1408.089    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               37648300  365.826    0.000 1402.152    0.000 categorical.py:108(sample)
               37648300   76.006    0.000 1381.331    0.000 utils.py:82(probs_to_logits)
               75296600  385.146    0.000 1220.947    0.000 functional.py:46(broadcast_tensors)
               75447193 1186.717    0.000 1186.717    0.000 {method 'max' of 'torch._C._TensorBase' objects}
              112944900 1074.138    0.000 1074.138    0.000 {method 'all' of 'torch._C._TensorBase' objects}
             6050167785 1042.045    0.000 1053.780    0.000 {built-in method builtins.len}
               37648300  222.467    0.000 1050.336    0.000 layers.py:844(check)
               16565252   43.957    0.000 1004.086    0.000 tensor.py:575(__iter__)
                1505933  152.655    0.000  985.667    0.001 layers.py:793(update)
               16565252  926.175    0.000  926.175    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               37648300  170.205    0.000  856.936    0.000 utils.py:11(broadcast_all)
               37648300  134.298    0.000  856.315    0.000 utils.py:77(clamp_probs)
             5678889704  854.843    0.000  854.843    0.000 {method 'values' of 'collections.OrderedDict' objects}
               37648300  809.597    0.000  809.597    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               75296600  733.280    0.000  733.280    0.000 {built-in method broadcast_tensors}
               37648300  722.017    0.000  722.017    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
                1505932   76.401    0.000  719.967    0.000 replaybuffer.py:34(save_option_critic)
              113396679  691.504    0.000  691.504    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               37648300  672.793    0.000  672.793    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
              226190986  642.715    0.000  642.715    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               37648300  622.463    0.000  622.463    0.000 {built-in method clamp}
               75296600  576.149    0.000  576.149    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               37841571  556.265    0.000  556.265    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               37648300  550.034    0.000  550.034    0.000 {built-in method bernoulli}
                1505932   95.318    0.000  497.858    0.000 optimizer.py:189(zero_grad)
               37648300  473.972    0.000  473.972    0.000 {built-in method all}
               37648300  449.010    0.000  449.010    0.000 {built-in method log}
               37648300   92.434    0.000  448.581    0.000 layers.py:838(isFree)
               37648300  448.438    0.000  448.438    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
               21083030  394.090    0.000  394.090    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               21083030  381.091    0.000  381.091    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              288755900  289.494    0.000  356.147    0.000 layer.py:103(isFree)
               12047464  215.361    0.000  354.987    0.000 layer.py:175(NoRock_update)
               37648300  334.066    0.000  334.066    0.000 {built-in method multinomial}
               21083030  315.235    0.000  315.235    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              116408558  309.513    0.000  309.513    0.000 {method 'to' of 'torch._C._TensorBase' objects}
              113141205  297.548    0.000  297.548    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                9487375  292.939    0.000  292.939    0.000 {built-in method tensor}
               37648300  287.837    0.000  287.837    0.000 {method 'expand' of 'torch._C._TensorBase' objects}
              496546816  196.470    0.000  286.710    0.000 {built-in method builtins.isinstance}
              112944925   74.098    0.000  276.851    0.000 {built-in method builtins.all}
                 150593  202.598    0.001  267.074    0.002 replaybuffer.py:42(sample_option_critic)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9607843: <Attempt3_Diamonds1_option_critic_0> in cluster <dcc> Done

Job <Attempt3_Diamonds1_option_critic_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon May  3 13:31:22 2021
Job was executed on host(s) <n-62-23-21>, in queue <hpc>, as user <s183914> in cluster <dcc> at Mon May  3 13:31:24 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon May  3 13:31:24 2021
Terminated at Thu May  6 13:26:32 2021
Results reported at Thu May  6 13:26:32 2021

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

    CPU time :                                   258896.94 sec.
    Max Memory :                                 861 MB
    Average Memory :                             840.77 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15523.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258938 sec.
    Turnaround time :                            258910 sec.

The output (if any) is above this job summary.

