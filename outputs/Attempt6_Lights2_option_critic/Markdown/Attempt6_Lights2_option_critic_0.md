
# Parameters

    Name :                      Attempt6_Lights2_option_critic-0
    Main :                      option_critic_run
    Level :                     Levels.Causal4
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
    Num :                       0
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              4315 minutes.
    Hours used :                71 hours.

# Profiling


      28356553223 function calls (27528467381 primitive calls) in 258900.85 seconds

##    Ordered by: cumulative time
   List reduced from 439 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.849 258900.849 {built-in method builtins.exec}
                      1    0.360    0.360 258900.849 258900.849 <string>:1(<module>)
                      1 3340.556 3340.556 258900.489 258900.489 optionCritic.py:195(option_critic_run)
                 928347    7.791    0.000 152254.457    0.164 tensor.py:195(backward)
                 928347   10.251    0.000 152246.539    0.164 __init__.py:68(backward)
                 928347 152214.999    0.164 152214.999    0.164 {method 'run_backward' of 'torch._C._EngineBase' objects}
        1097685168/272616783 5382.959    0.000 65309.823    0.000 module.py:866(_call_impl)
               29707104 4695.813    0.000 62569.446    0.002 optionCritic.py:143(actor_loss_fn)
               91674265  426.558    0.000 61072.328    0.001 optionCritic.py:70(get_state)
               91674265 1241.494    0.000 59344.866    0.001 container.py:117(forward)
              183348530  510.667    0.000 37466.272    0.000 conv.py:398(forward)
              183348530  266.033    0.000 36746.935    0.000 conv.py:390(_conv_forward)
              183348530 36480.903    0.000 36480.903    0.000 {built-in method conv2d}
              364291048  879.763    0.000 13455.334    0.000 linear.py:93(forward)
              364291048  363.272    0.000 12201.054    0.000 functional.py:1737(linear)
              364291048 11756.047    0.000 11756.047    0.000 {built-in method torch._C._nn.linear}
               29707104 1758.671    0.000 10423.033    0.000 optionCritic.py:91(get_action)
               29707104  701.798    0.000 8154.058    0.000 optionCritic.py:80(predict_option_termination)
                 928347   22.664    0.000 6724.273    0.007 optimizer.py:84(wrapper)
                 928347   13.066    0.000 6641.116    0.007 grad_mode.py:24(decorate_context)
                 928347   60.027    0.000 6605.922    0.007 adam.py:55(step)
                 928347  374.811    0.000 6484.924    0.007 _functional.py:53(adam)
               59414208  696.150    0.000 4384.680    0.000 distribution.py:34(__init__)
              275022795  288.143    0.000 3915.357    0.000 activation.py:713(forward)
              275022795  293.075    0.000 3627.214    0.000 functional.py:1364(leaky_relu)
               29707104  290.142    0.000 3449.761    0.000 categorical.py:115(log_prob)
               29707104  285.306    0.000 3400.700    0.000 bernoulli.py:34(__init__)
                 232086   41.553    0.000 3386.152    0.015 optionCritic.py:116(critic_loss_fn)
              275022795 3274.253    0.000 3274.253    0.000 {built-in method torch._C._nn.leaky_relu}
                 928347    5.712    0.000 3230.612    0.003 game.py:42(step)
                 928347    8.664    0.000 3148.325    0.003 layers.py:827(step)
               91589120  206.890    0.000 3108.416    0.000 optionCritic.py:77(get_Q)
               29707104  399.397    0.000 2933.740    0.000 categorical.py:49(__init__)
               59646294  219.411    0.000 2392.601    0.000 optionCritic.py:88(get_terminations)
               29707104 1214.175    0.000 1794.237    0.000 constraints.py:398(check)
                 928348   92.530    0.000 1764.422    0.002 layers.py:793(update)
               25993704 1413.078    0.000 1413.078    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               29707104  238.599    0.000 1397.788    0.000 distribution.py:240(_validate_sample)
                 928347   42.704    0.000 1370.786    0.001 layers.py:17(step)
               29707104   93.723    0.000 1323.912    0.000 layer.py:106(move)
               12996852 1261.251    0.000 1261.251    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               29707104  265.315    0.000 1236.433    0.000 bernoulli.py:86(sample)
               29707104 1224.264    0.000 1224.264    0.000 constraints.py:364(check)
               12996852 1167.295    0.000 1167.295    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               91674265  116.893    0.000 1110.407    0.000 activation.py:101(forward)
               91674265  111.723    0.000  993.515    0.000 functional.py:1195(relu)
             1427430886  983.119    0.000  983.187    0.000 module.py:934(__getattr__)
               29707104  495.693    0.000  957.740    0.000 categorical.py:123(entropy)
               29707104  188.809    0.000  939.890    0.000 layers.py:844(check)
                2003667   32.638    0.000  933.193    0.000 layers.py:849(restart)
               29707104  912.821    0.000  912.821    0.000 constraints.py:249(check)
              207949728  884.521    0.000  884.521    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               89585484  109.645    0.000  879.831    0.000 tensor.py:525(__rsub__)
               91674265  865.961    0.000  865.961    0.000 {built-in method relu}
               89121312  118.687    0.000  865.272    0.000 utils.py:106(__get__)
               91674265   94.191    0.000  864.873    0.000 flatten.py:39(forward)
               59414208  310.904    0.000  844.062    0.000 functional.py:46(broadcast_tensors)
               29707104  179.369    0.000  790.031    0.000 utils.py:11(broadcast_all)
               91674265  770.682    0.000  770.682    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               12996852  770.415    0.000  770.415    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               89585484  754.364    0.000  754.364    0.000 {built-in method rsub}
               12996852  748.062    0.000  748.062    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               25993704  744.706    0.000  744.706    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               10211817   24.853    0.000  712.964    0.000 tensor.py:575(__iter__)
               59646294  704.521    0.000  704.521    0.000 {method 'max' of 'torch._C._TensorBase' objects}
             1107896985  697.008    0.000  697.008    0.000 {built-in method torch._C._get_tracing_state}
               29707104  187.605    0.000  675.506    0.000 categorical.py:108(sample)
               10211817  672.151    0.000  672.151    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               89353398  671.118    0.000  671.118    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
                2003667   14.340    0.000  662.444    0.000 level.py:8(__init__)
               29707104   34.483    0.000  656.532    0.000 categorical.py:88(logits)
               29707104   36.647    0.000  622.049    0.000 utils.py:82(probs_to_logits)
               89121312  607.129    0.000  607.129    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
             4825938547  595.732    0.000  602.728    0.000 {built-in method builtins.len}
               89121312  544.240    0.000  544.240    0.000 {method 'all' of 'torch._C._TensorBase' objects}
                2003667   83.461    0.000  543.904    0.000 levels.py:199(generate)
                 232086  432.900    0.002  531.042    0.002 replaybuffer.py:42(sample_option_critic)
             4482414937  518.981    0.000  518.981    0.000 {method 'values' of 'collections.OrderedDict' objects}
               29707104  481.299    0.000  481.299    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
                9283480  312.766    0.000  450.331    0.000 layer.py:159(update)
               59414208  447.011    0.000  447.011    0.000 {built-in method broadcast_tensors}
                 928347   45.724    0.000  404.731    0.000 replaybuffer.py:34(save_option_critic)
                4007334   43.235    0.000  377.442    0.000 level.py:41(notUsed)
               29707104   72.994    0.000  368.136    0.000 utils.py:77(clamp_probs)
               29707104  360.857    0.000  360.857    0.000 {built-in method bernoulli}
               89817570  345.852    0.000  345.852    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               31710740  299.747    0.000  299.747    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               29707104  295.142    0.000  295.142    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
               29707104  293.966    0.000  293.966    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
              398993851  184.823    0.000  283.661    0.000 {built-in method builtins.isinstance}
              178706796  280.760    0.000  280.760    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                 928347   45.225    0.000  280.088    0.000 optimizer.py:189(zero_grad)
              908389339  194.905    0.000  277.603    0.000 enum.py:646(__hash__)
               59414208  252.337    0.000  252.337    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               91126835  245.628    0.000  245.628    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               29707104  245.524    0.000  245.524    0.000 {built-in method clamp}
               29707104   44.944    0.000  245.492    0.000 layers.py:838(isFree)
               20036670   34.316    0.000  230.241    0.000 layer.py:77(restart)
                6266344  226.608    0.000  226.608    0.000 {built-in method tensor}
               29707104  217.266    0.000  217.266    0.000 {built-in method log}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9624144: <Attempt6_Lights2_option_critic_0> in cluster <dcc> Done

Job <Attempt6_Lights2_option_critic_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun May  9 01:22:25 2021
Job was executed on host(s) <n-62-11-62>, in queue <hpc>, as user <s183914> in cluster <dcc> at Sun May  9 01:22:26 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun May  9 01:22:26 2021
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

    CPU time :                                   258271.80 sec.
    Max Memory :                                 1092 MB
    Average Memory :                             1079.83 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15292.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258956 sec.
    Turnaround time :                            258909 sec.

The output (if any) is above this job summary.

