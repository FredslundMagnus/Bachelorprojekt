[W NNPACK.cpp:80] Could not initialize NNPACK! Reason: Unsupported hardware.

# Parameters

    Name :                      Attempt8_Lights1_option_critic-2
    Main :                      option_critic_run
    Level :                     Levels.Causal3
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


      41997779480 function calls (40722658788 primitive calls) in 258900.92 seconds

##    Ordered by: cumulative time
   List reduced from 433 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.916 258900.916 {built-in method builtins.exec}
                      1    0.263    0.263 258900.916 258900.916 <string>:1(<module>)
                      1 3380.773 3380.773 258900.653 258900.653 optionCritic.py:195(option_critic_run)
        1689805312/419330977 10372.177    0.000 110220.640    0.000 module.py:866(_call_impl)
               45744224 9073.603    0.000 109166.971    0.002 optionCritic.py:143(actor_loss_fn)
              141163815  766.240    0.000 100601.744    0.001 optionCritic.py:70(get_state)
              141163815 2819.035    0.000 97465.748    0.001 container.py:117(forward)
                1429507    6.254    0.000 65426.871    0.046 tensor.py:195(backward)
                1429507    8.176    0.000 65420.355    0.046 __init__.py:68(backward)
                1429507 65383.860    0.046 65383.860    0.046 {method 'run_backward' of 'torch._C._EngineBase' objects}
              282327630  940.659    0.000 59415.873    0.000 conv.py:398(forward)
              282327630  404.652    0.000 58151.110    0.000 conv.py:390(_conv_forward)
              282327630 57746.458    0.000 57746.458    0.000 {built-in method conv2d}
               45744224 3919.017    0.000 23700.843    0.001 optionCritic.py:91(get_action)
                1429507   17.269    0.000 22659.968    0.016 optimizer.py:84(wrapper)
                1429507    9.831    0.000 22590.851    0.016 grad_mode.py:24(decorate_context)
                1429507   74.033    0.000 22563.771    0.016 rmsprop.py:56(step)
                1429507  124.765    0.000 22402.951    0.016 _functional.py:203(rmsprop)
              560494792 1688.613    0.000 21443.051    0.000 linear.py:93(forward)
               20013092 19910.148    0.001 19910.148    0.001 {method 'sqrt' of 'torch._C._TensorBase' objects}
              560494792  623.077    0.000 19135.624    0.000 functional.py:1737(linear)
              560494792 18382.244    0.000 18382.244    0.000 {built-in method torch._C._nn.linear}
               45744224 1212.966    0.000 12909.069    0.000 optionCritic.py:80(predict_option_termination)
               91488448 1082.905    0.000 8580.423    0.000 distribution.py:34(__init__)
              423491445  432.446    0.000 8254.952    0.000 activation.py:713(forward)
              423491445  474.886    0.000 7822.506    0.000 functional.py:1364(leaky_relu)
               45744224  629.806    0.000 7800.532    0.000 categorical.py:115(log_prob)
              423491445 7250.646    0.000 7250.646    0.000 {built-in method torch._C._nn.leaky_relu}
               45744224  895.702    0.000 6991.971    0.000 categorical.py:49(__init__)
              140577114  483.784    0.000 6691.858    0.000 optionCritic.py:77(get_Q)
               91845824  471.210    0.000 5330.231    0.000 optionCritic.py:88(get_terminations)
                 357376   66.339    0.000 5178.186    0.014 optionCritic.py:116(critic_loss_fn)
               45744224  253.331    0.000 4421.768    0.000 bernoulli.py:34(__init__)
               45744224 2878.852    0.000 4360.953    0.000 constraints.py:398(check)
                1429507    6.770    0.000 3790.687    0.003 game.py:42(step)
                1429507    9.987    0.000 3695.106    0.003 layers.py:827(step)
               45744224  482.701    0.000 3282.484    0.000 distribution.py:240(_validate_sample)
              141163815  164.907    0.000 2344.763    0.000 activation.py:101(forward)
               45744224 1117.009    0.000 2304.406    0.000 categorical.py:123(entropy)
               45744224 2214.065    0.000 2214.065    0.000 constraints.py:249(check)
              141163815  141.563    0.000 2179.857    0.000 functional.py:1195(relu)
                1429508  140.248    0.000 2142.612    0.001 layers.py:793(update)
               45744224 2048.487    0.000 2048.487    0.000 constraints.py:364(check)
              141163815 2008.195    0.000 2008.195    0.000 {built-in method relu}
              137232672  214.003    0.000 1914.073    0.000 utils.py:106(__get__)
             1705529889 1885.803    0.000 1885.803    0.000 {built-in method torch._C._get_tracing_state}
              320209568 1853.164    0.000 1853.164    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              137947424  184.730    0.000 1701.559    0.000 tensor.py:525(__rsub__)
               45744224  280.453    0.000 1641.458    0.000 bernoulli.py:86(sample)
              141163815  114.909    0.000 1637.299    0.000 flatten.py:39(forward)
              137232672 1635.361    0.000 1635.361    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
             2196650164 1622.829    0.000 1622.947    0.000 module.py:934(__getattr__)
               20013092 1544.090    0.000 1544.090    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                1429507   59.001    0.000 1537.334    0.001 layers.py:17(step)
               45744224   75.642    0.000 1534.432    0.000 categorical.py:88(logits)
              141163815 1522.390    0.000 1522.390    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               45744224  384.086    0.000 1493.371    0.000 categorical.py:108(sample)
              137590048 1486.139    0.000 1486.139    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
              137947424 1485.175    0.000 1485.175    0.000 {built-in method rsub}
               45744224  103.125    0.000 1473.149    0.000 layer.py:106(move)
               45744224   79.815    0.000 1458.790    0.000 utils.py:82(probs_to_logits)
               91488448  386.477    0.000 1228.063    0.000 functional.py:46(broadcast_tensors)
               91845824 1217.288    0.000 1217.288    0.000 {method 'max' of 'torch._C._TensorBase' objects}
              137232672 1138.338    0.000 1138.338    0.000 {method 'all' of 'torch._C._TensorBase' objects}
                2629722   35.553    0.000 1100.827    0.000 layers.py:849(restart)
             7335467052 1069.327    0.000 1079.216    0.000 {built-in method builtins.len}
               45744224  226.012    0.000 1000.458    0.000 layers.py:844(check)
             6900385063  920.346    0.000  920.346    0.000 {method 'values' of 'collections.OrderedDict' objects}
               45744224  136.713    0.000  900.794    0.000 utils.py:77(clamp_probs)
               15724577   35.696    0.000  872.635    0.000 tensor.py:575(__iter__)
               45744224  839.717    0.000  839.717    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               15724577  808.556    0.000  808.556    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               45744224  147.066    0.000  803.698    0.000 utils.py:11(broadcast_all)
                2629722   16.276    0.000  794.765    0.000 level.py:8(__init__)
               45744224  764.081    0.000  764.081    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
              138304800  746.398    0.000  746.398    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               91488448  735.790    0.000  735.790    0.000 {built-in method broadcast_tensors}
                1429507   72.250    0.000  713.167    0.000 replaybuffer.py:34(save_option_critic)
               45744224  707.308    0.000  707.308    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
              275180096  676.414    0.000  676.414    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               45744224  648.439    0.000  648.439    0.000 {built-in method clamp}
                2629722   73.003    0.000  645.162    0.000 levels.py:164(generate)
               91488448  626.740    0.000  626.740    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               48373914  619.894    0.000  619.894    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                 357376  430.252    0.001  556.027    0.002 replaybuffer.py:42(sample_option_critic)
               45744224  536.428    0.000  536.428    0.000 {built-in method bernoulli}
               45744224  501.626    0.000  501.626    0.000 {built-in method all}
                5259444   62.034    0.000  480.298    0.000 level.py:41(notUsed)
               45744224  478.181    0.000  478.181    0.000 {built-in method log}
               45744224  473.363    0.000  473.363    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
               11436064  269.788    0.000  433.807    0.000 layer.py:175(NoRock_update)
               45744224  348.958    0.000  348.958    0.000 {built-in method multinomial}
              137232704   87.840    0.000  343.502    0.000 {built-in method builtins.all}
                1429507   68.258    0.000  340.856    0.000 optimizer.py:189(zero_grad)
             1075845645  230.225    0.000  329.648    0.000 enum.py:646(__hash__)
              139865251  326.891    0.000  326.891    0.000 {method 'item' of 'torch._C._TensorBase' objects}
              141163829  315.940    0.000  315.940    0.000 {method 'to' of 'torch._C._TensorBase' objects}
                6643817  151.291    0.000  313.814    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               45744224   68.474    0.000  310.994    0.000 layers.py:838(isFree)
               45744224  307.463    0.000  307.463    0.000 {method 'expand' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9632920: <Attempt8_Lights1_option_critic_2> in cluster <dcc> Done

Job <Attempt8_Lights1_option_critic_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed May 12 15:36:14 2021
Job was executed on host(s) <n-62-23-25>, in queue <hpc>, as user <s183914> in cluster <dcc> at Sun May 16 23:16:53 2021
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

    CPU time :                                   258895.22 sec.
    Max Memory :                                 934 MB
    Average Memory :                             924.04 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15450.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   259038 sec.
    Turnaround time :                            632169 sec.

The output (if any) is above this job summary.

