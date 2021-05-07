
# Parameters

    Name :                      Attempt2_Diamonds3_option_critic-2
    Main :                      option_critic_run
    Level :                     Levels.Causal6
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


      54363589547 function calls (52640750475 primitive calls) in 258900.67 seconds

##    Ordered by: cumulative time
   List reduced from 429 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.671 258900.671 {built-in method builtins.exec}
                      1    0.311    0.311 258900.671 258900.671 <string>:1(<module>)
                      1 5816.796 5816.796 258900.360 258900.360 optionCritic.py:195(option_critic_run)
               61267375 9977.562    0.000 117060.370    0.002 optionCritic.py:143(actor_loss_fn)
        2275382321/560508506 10640.695    0.000 115368.733    0.000 module.py:866(_call_impl)
              190541535  896.760    0.000 107300.966    0.001 optionCritic.py:70(get_state)
              190541535 2462.133    0.000 103663.584    0.001 container.py:117(forward)
                2450695   18.700    0.000 69306.601    0.028 tensor.py:195(backward)
                2450695   23.824    0.000 69287.575    0.028 __init__.py:68(backward)
                2450695 69210.727    0.028 69210.727    0.028 {method 'run_backward' of 'torch._C._EngineBase' objects}
              381083070 1036.118    0.000 65245.092    0.000 conv.py:398(forward)
              381083070  566.283    0.000 63797.453    0.000 conv.py:390(_conv_forward)
              381083070 63231.169    0.000 63231.169    0.000 {built-in method conv2d}
              751050041 1738.374    0.000 21561.895    0.000 linear.py:93(forward)
               61267375 3676.976    0.000 21555.244    0.000 optionCritic.py:91(get_action)
              751050041  724.929    0.000 19124.898    0.000 functional.py:1737(linear)
              751050041 18243.849    0.000 18243.849    0.000 {built-in method torch._C._nn.linear}
               61267375 1315.032    0.000 15057.837    0.000 optionCritic.py:80(predict_option_termination)
              122534750 1290.235    0.000 8444.213    0.000 distribution.py:34(__init__)
                2450695   50.773    0.000 8256.657    0.003 optimizer.py:84(wrapper)
                2450695   26.994    0.000 8063.514    0.003 grad_mode.py:24(decorate_context)
                2450695  130.781    0.000 7986.389    0.003 rmsprop.py:56(step)
              571624605  557.679    0.000 7707.950    0.000 activation.py:713(forward)
                2450695  140.311    0.000 7703.049    0.003 _functional.py:203(rmsprop)
               61267375  611.163    0.000 7174.308    0.000 categorical.py:115(log_prob)
              571624605  577.442    0.000 7150.271    0.000 functional.py:1364(leaky_relu)
              571624605 6453.508    0.000 6453.508    0.000 {built-in method torch._C._nn.leaky_relu}
               61267375  837.920    0.000 6066.734    0.000 categorical.py:49(__init__)
               61267375  471.734    0.000 5946.652    0.000 bernoulli.py:34(__init__)
              185552173  408.515    0.000 5940.096    0.000 optionCritic.py:77(get_Q)
                 612673   96.337    0.000 4860.567    0.008 optionCritic.py:116(critic_loss_fn)
              123147423  429.526    0.000 4693.955    0.000 optionCritic.py:88(get_terminations)
                2450695   11.647    0.000 4095.147    0.002 game.py:42(step)
                2450695   23.519    0.000 3953.126    0.002 layers.py:827(step)
               34309724 3902.115    0.000 3902.115    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               61267375 2489.651    0.000 3682.229    0.000 constraints.py:398(check)
               61267375  529.062    0.000 2918.514    0.000 distribution.py:240(_validate_sample)
               34309724 2704.201    0.000 2704.201    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                2450695   86.488    0.000 2322.556    0.001 layers.py:17(step)
               61267375 2258.707    0.000 2258.707    0.000 constraints.py:364(check)
               61267375  151.768    0.000 2228.082    0.000 layer.py:106(move)
              190541535  238.157    0.000 2210.166    0.000 activation.py:101(forward)
               61267375  419.589    0.000 2141.651    0.000 bernoulli.py:86(sample)
               61267375 1028.260    0.000 1979.075    0.000 categorical.py:123(entropy)
              190541535  206.203    0.000 1972.009    0.000 functional.py:1195(relu)
              428871625 1898.529    0.000 1898.529    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
             2947628129 1889.216    0.000 1889.387    0.000 module.py:934(__getattr__)
               61267375 1873.369    0.000 1873.369    0.000 constraints.py:249(check)
              183802125  246.072    0.000 1778.526    0.000 utils.py:106(__get__)
              190541535  180.446    0.000 1738.370    0.000 flatten.py:39(forward)
              190541535 1735.370    0.000 1735.370    0.000 {built-in method relu}
              185027471  200.166    0.000 1673.633    0.000 tensor.py:525(__rsub__)
                2450696  196.761    0.000 1598.604    0.001 layers.py:793(update)
              122534750  544.103    0.000 1562.994    0.000 functional.py:46(broadcast_tensors)
              190541535 1557.925    0.000 1557.925    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               61267375  307.337    0.000 1445.643    0.000 layers.py:844(check)
              185027471 1443.501    0.000 1443.501    0.000 {built-in method rsub}
             2302339966 1406.421    0.000 1406.421    0.000 {built-in method torch._C._get_tracing_state}
              123147423 1405.719    0.000 1405.719    0.000 {method 'max' of 'torch._C._TensorBase' objects}
               61267375  397.822    0.000 1405.695    0.000 categorical.py:108(sample)
               26957645   60.696    0.000 1364.707    0.000 tensor.py:575(__iter__)
               61267375   73.019    0.000 1345.185    0.000 categorical.py:88(logits)
               61267375  280.448    0.000 1332.016    0.000 utils.py:11(broadcast_all)
              184414798 1315.111    0.000 1315.111    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
               61267375   72.997    0.000 1272.166    0.000 utils.py:82(probs_to_logits)
               26957645 1266.236    0.000 1266.236    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
              183802125 1245.322    0.000 1245.322    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
             9904894871 1225.586    0.000 1242.350    0.000 {built-in method builtins.len}
                 612673  957.624    0.002 1182.501    0.002 replaybuffer.py:42(sample_option_critic)
             9292070819 1072.302    0.000 1072.302    0.000 {method 'values' of 'collections.OrderedDict' objects}
              183802125 1055.036    0.000 1055.036    0.000 {method 'all' of 'torch._C._TensorBase' objects}
               61267375  896.123    0.000  896.123    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
              122534750  866.945    0.000  866.945    0.000 {built-in method broadcast_tensors}
                2450695   88.532    0.000  755.333    0.000 replaybuffer.py:34(save_option_critic)
               61267375  167.594    0.000  743.488    0.000 utils.py:77(clamp_probs)
              185640144  694.028    0.000  694.028    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               61267375  682.816    0.000  682.816    0.000 {built-in method bernoulli}
                2450695  109.548    0.000  645.064    0.000 optimizer.py:189(zero_grad)
               61267375  629.975    0.000  629.975    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
               61792077  590.704    0.000  590.704    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               61267375  575.893    0.000  575.893    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
              368829596  569.736    0.000  569.736    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
              122534750  522.097    0.000  522.097    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               61267375  107.787    0.000  507.336    0.000 layers.py:838(isFree)
               61267375  503.727    0.000  503.727    0.000 {built-in method clamp}
               19605568  289.643    0.000  487.469    0.000 layer.py:175(NoRock_update)
              809110312  276.908    0.000  473.932    0.000 {built-in method builtins.isinstance}
               61267375  455.681    0.000  455.681    0.000 {built-in method log}
               61267375  436.084    0.000  436.084    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
               16542193  432.552    0.000  432.552    0.000 {built-in method tensor}
              184331751  432.257    0.000  432.257    0.000 {method 'item' of 'torch._C._TensorBase' objects}
              190541549  430.877    0.000  430.877    0.000 {method 'to' of 'torch._C._TensorBase' objects}
              183802150  127.703    0.000  424.059    0.000 {built-in method builtins.all}
              367235086  338.243    0.000  399.549    0.000 layer.py:103(isFree)
               61267375  395.447    0.000  395.447    0.000 {built-in method all}
               61267375  361.189    0.000  361.189    0.000 {built-in method multinomial}
             1108825962  241.489    0.000  358.303    0.000 enum.py:646(__hash__)
               34309724  350.707    0.000  350.707    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               61267375  208.919    0.000  340.024    0.000 layers.py:424(check)
                 524726    8.725    0.000  339.273    0.001 layers.py:849(restart)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9606124: <Attempt2_Diamonds3_option_critic_2> in cluster <dcc> Done

Job <Attempt2_Diamonds3_option_critic_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon May  3 01:33:09 2021
Job was executed on host(s) <n-62-11-60>, in queue <hpc>, as user <s183914> in cluster <dcc> at Mon May  3 01:33:11 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon May  3 01:33:11 2021
Terminated at Thu May  6 01:28:26 2021
Results reported at Thu May  6 01:28:26 2021

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

    CPU time :                                   258288.77 sec.
    Max Memory :                                 902 MB
    Average Memory :                             888.65 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15482.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258942 sec.
    Turnaround time :                            258917 sec.

The output (if any) is above this job summary.

