
# Parameters

    Name :                      Attempt6_Diamonds3_option_critic-2
    Main :                      option_critic_run
    Level :                     Levels.Causal6
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


      22478653791 function calls (21769480980 primitive calls) in 258900.75 seconds

##    Ordered by: cumulative time
   List reduced from 429 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.745 258900.745 {built-in method builtins.exec}
                      1    0.302    0.302 258900.745 258900.745 <string>:1(<module>)
                      1 2438.482 2438.482 258900.444 258900.444 optionCritic.py:195(option_critic_run)
                 795036    5.792    0.000 179627.895    0.226 tensor.py:195(backward)
                 795036    7.761    0.000 179622.002    0.226 __init__.py:68(backward)
                 795036 179598.735    0.226 179598.735    0.226 {method 'run_backward' of 'torch._C._EngineBase' objects}
        938496990/231908736 4452.634    0.000 49923.801    0.000 module.py:866(_call_impl)
               25441152 3679.097    0.000 49371.380    0.002 optionCritic.py:143(actor_loss_fn)
               78509806  370.079    0.000 46566.571    0.001 optionCritic.py:70(get_state)
               78509806  979.885    0.000 45092.066    0.001 container.py:117(forward)
              157019612  417.270    0.000 28178.753    0.000 conv.py:398(forward)
              157019612  216.502    0.000 27595.327    0.000 conv.py:390(_conv_forward)
              157019612 27378.826    0.000 27378.826    0.000 {built-in method conv2d}
              310418542  726.593    0.000 10092.042    0.000 linear.py:93(forward)
              310418542  289.435    0.000 9070.305    0.000 functional.py:1737(linear)
              310418542 8711.551    0.000 8711.551    0.000 {built-in method torch._C._nn.linear}
               25441152 1454.750    0.000 8678.930    0.000 optionCritic.py:91(get_action)
               25441152  531.664    0.000 6068.176    0.000 optionCritic.py:80(predict_option_termination)
               50882304  507.137    0.000 3400.506    0.000 distribution.py:34(__init__)
                 795036   16.787    0.000 3266.320    0.004 optimizer.py:84(wrapper)
                 795036    8.906    0.000 3203.390    0.004 grad_mode.py:24(decorate_context)
                 795036   46.873    0.000 3178.346    0.004 adam.py:55(step)
              235529418  228.400    0.000 3094.300    0.000 activation.py:713(forward)
                 795036  269.813    0.000 3079.615    0.004 _functional.py:53(adam)
               25441152  248.670    0.000 2898.965    0.000 categorical.py:115(log_prob)
              235529418  243.163    0.000 2865.900    0.000 functional.py:1364(leaky_relu)
              235529418 2574.921    0.000 2574.921    0.000 {built-in method torch._C._nn.leaky_relu}
               76876715  170.675    0.000 2471.522    0.000 optionCritic.py:77(get_Q)
               25441152  328.854    0.000 2440.549    0.000 categorical.py:49(__init__)
               25441152  179.981    0.000 2333.203    0.000 bernoulli.py:34(__init__)
                 198759   30.978    0.000 2084.960    0.010 optionCritic.py:116(critic_loss_fn)
               51081063  182.616    0.000 1918.539    0.000 optionCritic.py:88(get_terminations)
                 795036    4.030    0.000 1663.035    0.002 game.py:42(step)
                 795036    7.323    0.000 1614.414    0.002 layers.py:827(step)
               25441152  997.835    0.000 1486.101    0.000 constraints.py:398(check)
               25441152  207.103    0.000 1178.748    0.000 distribution.py:240(_validate_sample)
                 795036   33.250    0.000  974.383    0.001 layers.py:17(step)
               25441152   64.618    0.000  938.043    0.000 layer.py:106(move)
               25441152  902.771    0.000  902.771    0.000 constraints.py:364(check)
               78509806   97.458    0.000  898.317    0.000 activation.py:101(forward)
               25441152  177.130    0.000  871.290    0.000 bernoulli.py:86(sample)
               78509806   91.459    0.000  800.859    0.000 functional.py:1195(relu)
               25441152  418.192    0.000  799.146    0.000 categorical.py:123(entropy)
             1217770771  796.693    0.000  796.751    0.000 module.py:934(__getattr__)
               25441152  757.188    0.000  757.188    0.000 constraints.py:249(check)
              178088064  738.159    0.000  738.159    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               76323456   98.849    0.000  722.135    0.000 utils.py:106(__get__)
               76720974   94.464    0.000  699.248    0.000 tensor.py:525(__rsub__)
               78509806  696.204    0.000  696.204    0.000 {built-in method relu}
               78509806   72.657    0.000  696.055    0.000 flatten.py:39(forward)
               22260996  653.499    0.000  653.499    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                 795037   69.656    0.000  629.426    0.001 layers.py:793(update)
               78509806  623.398    0.000  623.398    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               50882304  222.566    0.000  621.386    0.000 functional.py:46(broadcast_tensors)
               76720974  591.627    0.000  591.627    0.000 {built-in method rsub}
               25441152  119.778    0.000  586.322    0.000 layers.py:844(check)
               25441152  156.805    0.000  568.050    0.000 categorical.py:108(sample)
               25441152   29.248    0.000  548.672    0.000 categorical.py:88(logits)
               51081063  547.816    0.000  547.816    0.000 {method 'max' of 'torch._C._TensorBase' objects}
              947242386  545.500    0.000  545.500    0.000 {built-in method torch._C._get_tracing_state}
               11130498  543.157    0.000  543.157    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               76522215  533.851    0.000  533.851    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
                8745396   19.392    0.000  520.079    0.000 tensor.py:575(__iter__)
               25441152   33.446    0.000  519.424    0.000 utils.py:82(probs_to_logits)
             4080965867  511.590    0.000  516.975    0.000 {built-in method builtins.len}
               25441152  111.132    0.000  513.671    0.000 utils.py:11(broadcast_all)
               11130498  513.581    0.000  513.581    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               76323456  500.635    0.000  500.635    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                8745396  489.116    0.000  489.116    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
             3832497766  429.392    0.000  429.392    0.000 {method 'values' of 'collections.OrderedDict' objects}
               76323456  424.729    0.000  424.729    0.000 {method 'all' of 'torch._C._TensorBase' objects}
               11130498  378.172    0.000  378.172    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               25441152  374.132    0.000  374.132    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
                 198759  300.171    0.002  371.201    0.002 replaybuffer.py:42(sample_option_critic)
               22260996  361.526    0.000  361.526    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               11130498  355.335    0.000  355.335    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               50882304  330.790    0.000  330.790    0.000 {built-in method broadcast_tensors}
               25441152   63.057    0.000  310.565    0.000 utils.py:77(clamp_probs)
                 795036   34.696    0.000  300.012    0.000 replaybuffer.py:34(save_option_critic)
               76919733  280.884    0.000  280.884    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               25441152  266.885    0.000  266.885    0.000 {built-in method bernoulli}
               25441152  247.507    0.000  247.507    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
               25441152  242.342    0.000  242.342    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
               25441152   56.089    0.000  234.694    0.000 layers.py:838(isFree)
               25596893  230.537    0.000  230.537    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
              153044430  228.996    0.000  228.996    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               50882304  211.423    0.000  211.423    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               76323488   52.977    0.000  205.715    0.000 {built-in method builtins.all}
                 795036   35.930    0.000  203.880    0.000 optimizer.py:189(zero_grad)
               25441152  203.672    0.000  203.672    0.000 {built-in method clamp}
                6360296  111.101    0.000  189.661    0.000 layer.py:175(NoRock_update)
              193369774  147.645    0.000  178.605    0.000 layer.py:103(isFree)
              334834531  118.813    0.000  178.438    0.000 {built-in method builtins.isinstance}
               25441152  178.417    0.000  178.417    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
               25441152  175.413    0.000  175.413    0.000 {built-in method log}
               25441152  165.069    0.000  165.069    0.000 {built-in method all}
               76480818  161.512    0.000  161.512    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               78509820  160.076    0.000  160.076    0.000 {method 'to' of 'torch._C._TensorBase' objects}
              465678341  105.446    0.000  151.169    0.000 enum.py:646(__hash__)
                5366497  149.532    0.000  149.532    0.000 {built-in method tensor}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9624155: <Attempt6_Diamonds3_option_critic_2> in cluster <dcc> Done

Job <Attempt6_Diamonds3_option_critic_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun May  9 01:22:26 2021
Job was executed on host(s) <n-62-11-60>, in queue <hpc>, as user <s183914> in cluster <dcc> at Sun May  9 01:22:27 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun May  9 01:22:27 2021
Terminated at Wed May 12 01:17:35 2021
Results reported at Wed May 12 01:17:35 2021

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

    CPU time :                                   258288.17 sec.
    Max Memory :                                 940 MB
    Average Memory :                             933.94 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15444.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258956 sec.
    Turnaround time :                            258909 sec.

The output (if any) is above this job summary.

