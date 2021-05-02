[W NNPACK.cpp:80] Could not initialize NNPACK! Reason: Unsupported hardware.

# Parameters

    Name :                      DoorsAndKey_option_critic-2
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


      31527161700 function calls (30488138037 primitive calls) in 258900.34 seconds

##    Ordered by: cumulative time
   List reduced from 428 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.336 258900.336 {built-in method builtins.exec}
                      1    0.260    0.260 258900.336 258900.336 <string>:1(<module>)
                      1 3842.904 3842.904 258900.075 258900.075 optionCritic.py:195(option_critic_run)
        1372426714/338206708 10114.977    0.000 105636.863    0.000 module.py:866(_call_impl)
               36949625 9887.768    0.000 104818.461    0.003 optionCritic.py:143(actor_loss_fn)
              114913334  743.258    0.000 96496.786    0.001 optionCritic.py:70(get_state)
              114913334 2804.690    0.000 93412.671    0.001 container.py:117(forward)
                1477985   11.658    0.000 80208.223    0.054 tensor.py:195(backward)
                1477985   14.214    0.000 80196.281    0.054 __init__.py:68(backward)
                1477985 80145.008    0.054 80145.008    0.054 {method 'run_backward' of 'torch._C._EngineBase' objects}
              229826668  884.274    0.000 55336.095    0.000 conv.py:398(forward)
              229826668  376.329    0.000 54104.917    0.000 conv.py:390(_conv_forward)
              229826668 53728.588    0.000 53728.588    0.000 {built-in method conv2d}
               36949625 3914.915    0.000 23145.254    0.001 optionCritic.py:91(get_action)
              453120042 1555.518    0.000 21678.646    0.000 linear.py:93(forward)
              453120042  573.806    0.000 19479.877    0.000 functional.py:1737(linear)
              453120042 18786.468    0.000 18786.468    0.000 {built-in method torch._C._nn.linear}
               36949625 1194.733    0.000 12893.621    0.000 optionCritic.py:80(predict_option_termination)
                1477985   32.443    0.000 12491.501    0.008 optimizer.py:84(wrapper)
                1477985   17.266    0.000 12364.447    0.008 grad_mode.py:24(decorate_context)
                1477985  104.430    0.000 12313.740    0.008 rmsprop.py:56(step)
                1477985  161.165    0.000 12096.689    0.008 _functional.py:203(rmsprop)
               20691784 9705.889    0.000 9705.889    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               73899250 1066.983    0.000 8424.661    0.000 distribution.py:34(__init__)
              344740002  426.404    0.000 8026.268    0.000 activation.py:713(forward)
              344740002  436.571    0.000 7599.864    0.000 functional.py:1364(leaky_relu)
               36949625  605.770    0.000 7588.249    0.000 categorical.py:115(log_prob)
              344740002 7069.551    0.000 7069.551    0.000 {built-in method torch._C._nn.leaky_relu}
               36949625  884.869    0.000 6817.645    0.000 categorical.py:49(__init__)
              112075003  457.139    0.000 6342.059    0.000 optionCritic.py:77(get_Q)
                 369496   84.301    0.000 5882.710    0.016 optionCritic.py:116(critic_loss_fn)
               74268746  450.226    0.000 5144.774    0.000 optionCritic.py:88(get_terminations)
               36949625  290.616    0.000 4560.543    0.000 bernoulli.py:34(__init__)
               36949625 2825.564    0.000 4248.818    0.000 constraints.py:398(check)
               36949625  464.534    0.000 3207.331    0.000 distribution.py:240(_validate_sample)
                1477985    8.649    0.000 2341.136    0.002 game.py:41(step)
              114913334  159.595    0.000 2308.506    0.000 activation.py:101(forward)
                1477985   13.312    0.000 2233.744    0.002 layers.py:718(step)
               36949625 1079.271    0.000 2227.209    0.000 categorical.py:123(entropy)
               36949625 2171.987    0.000 2171.987    0.000 constraints.py:249(check)
              114913334  151.678    0.000 2148.911    0.000 functional.py:1195(relu)
               36949625 2041.093    0.000 2041.093    0.000 constraints.py:364(check)
              114913334 1967.737    0.000 1967.737    0.000 {built-in method relu}
              110848875  220.924    0.000 1871.341    0.000 utils.py:106(__get__)
             1388684549 1789.367    0.000 1789.367    0.000 {built-in method torch._C._get_tracing_state}
              258647375 1777.562    0.000 1777.562    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               36949625  307.289    0.000 1719.898    0.000 bernoulli.py:86(sample)
              111587867  175.036    0.000 1655.771    0.000 tensor.py:525(__rsub__)
             1778191565 1628.789    0.000 1628.943    0.000 module.py:934(__getattr__)
              110848875 1595.991    0.000 1595.991    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
              114913334  112.788    0.000 1586.360    0.000 flatten.py:39(forward)
               36949625   72.556    0.000 1476.583    0.000 categorical.py:88(logits)
              114913334 1473.572    0.000 1473.572    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              111218371 1459.437    0.000 1459.437    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
               36949625  387.941    0.000 1456.547    0.000 categorical.py:108(sample)
              111587867 1450.551    0.000 1450.551    0.000 {built-in method rsub}
               36949625   75.440    0.000 1404.027    0.000 utils.py:82(probs_to_logits)
               73899250  382.057    0.000 1237.369    0.000 functional.py:46(broadcast_tensors)
               74268746 1179.947    0.000 1179.947    0.000 {method 'max' of 'torch._C._TensorBase' objects}
                1477985   64.227    0.000 1134.734    0.001 layers.py:17(step)
              110848875 1090.941    0.000 1090.941    0.000 {method 'all' of 'torch._C._TensorBase' objects}
                1477986  144.388    0.000 1079.878    0.001 layers.py:684(update)
               36949625  110.768    0.000 1065.324    0.000 layer.py:98(move)
             5898035858 1035.696    0.000 1048.574    0.000 {built-in method builtins.len}
               16257835   46.616    0.000 1023.220    0.000 tensor.py:575(__iter__)
               20691784 1008.464    0.000 1008.464    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               16257835  941.928    0.000  941.928    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
             5604620190  898.861    0.000  898.861    0.000 {method 'values' of 'collections.OrderedDict' objects}
               36949625  180.476    0.000  878.578    0.000 utils.py:11(broadcast_all)
               36949625  132.963    0.000  853.591    0.000 utils.py:77(clamp_probs)
               36949625  817.165    0.000  817.165    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               73899250  739.259    0.000  739.259    0.000 {built-in method broadcast_tensors}
               36949625  720.627    0.000  720.627    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
              111957363  712.234    0.000  712.234    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
                1477985   74.732    0.000  703.513    0.000 replaybuffer.py:34(save_option_critic)
               36949625  687.570    0.000  687.570    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
               12562650  317.984    0.000  677.551    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                 369496  515.014    0.001  670.484    0.002 replaybuffer.py:42(sample_option_critic)
               36949625  626.857    0.000  626.857    0.000 {built-in method clamp}
              222436742  624.687    0.000  624.687    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               73899250  601.219    0.000  601.219    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               37436761  585.636    0.000  585.636    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               36949625  546.375    0.000  546.375    0.000 {built-in method bernoulli}
               36949625  159.186    0.000  525.340    0.000 layers.py:735(check)
               36949625  474.996    0.000  474.996    0.000 {built-in method log}
               36949625  474.478    0.000  474.478    0.000 {built-in method all}
                1477985   88.213    0.000  468.512    0.000 optimizer.py:189(zero_grad)
               36949625  459.620    0.000  459.620    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
               20691784  439.773    0.000  439.773    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               20691784  396.917    0.000  396.917    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               20691784  384.481    0.000  384.481    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               12562650   21.140    0.000  359.566    0.000 <__array_function__ internals>:2(prod)
               36949625   77.925    0.000  344.089    0.000 layers.py:729(isFree)
               36949625  342.587    0.000  342.587    0.000 {built-in method multinomial}
               12562650   20.237    0.000  334.399    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
              487965017  221.740    0.000  317.416    0.000 {built-in method builtins.isinstance}
                9976402  316.367    0.000  316.367    0.000 {built-in method tensor}
               12562650   37.554    0.000  314.161    0.000 fromnumeric.py:2912(prod)
              114913348  304.740    0.000  304.740    0.000 {method 'to' of 'torch._C._TensorBase' objects}
              111338989  304.598    0.000  304.598    0.000 {method 'item' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9601889: <DoorsAndKey_option_critic_2> in cluster <dcc> Done

Job <DoorsAndKey_option_critic_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Thu Apr 29 21:41:26 2021
Job was executed on host(s) <n-62-23-21>, in queue <hpc>, as user <s183914> in cluster <dcc> at Thu Apr 29 21:41:29 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Apr 29 21:41:29 2021
Terminated at Sun May  2 21:36:31 2021
Results reported at Sun May  2 21:36:31 2021

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

    CPU time :                                   258896.28 sec.
    Max Memory :                                 783 MB
    Average Memory :                             766.48 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15601.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258967 sec.
    Turnaround time :                            258905 sec.

The output (if any) is above this job summary.

