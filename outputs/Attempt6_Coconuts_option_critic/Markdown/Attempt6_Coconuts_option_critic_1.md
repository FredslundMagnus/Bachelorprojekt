
# Parameters

    Name :                      Attempt6_Coconuts_option_critic-1
    Main :                      option_critic_run
    Level :                     Levels.Coconuts
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
    Num :                       1
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              4315 minutes.
    Hours used :                71 hours.

# Profiling


      27226081127 function calls (26477599881 primitive calls) in 258901.42 seconds

##    Ordered by: cumulative time
   List reduced from 438 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258901.416 258901.416 {built-in method builtins.exec}
                      1    0.358    0.358 258901.416 258901.416 <string>:1(<module>)
                      1 3025.697 3025.697 258901.058 258901.058 optionCritic.py:195(option_critic_run)
                 839104    7.100    0.000 163261.232    0.195 tensor.py:195(backward)
                 839104    9.483    0.000 163254.012    0.195 __init__.py:68(backward)
                 839104 163224.429    0.195 163224.429    0.195 {method 'run_backward' of 'torch._C._EngineBase' objects}
        991901945/246148256 4914.198    0.000 57771.004    0.000 module.py:866(_call_impl)
               26851328 4199.659    0.000 55759.742    0.002 optionCritic.py:143(actor_loss_fn)
               82861521  411.690    0.000 53995.402    0.001 optionCritic.py:70(get_state)
               82861521 1108.006    0.000 52369.387    0.001 container.py:117(forward)
              165723042  468.855    0.000 31994.892    0.000 conv.py:398(forward)
              165723042  297.519    0.000 31341.321    0.000 conv.py:390(_conv_forward)
              165723042 31043.802    0.000 31043.802    0.000 {built-in method conv2d}
              329009777  808.305    0.000 12859.858    0.000 linear.py:93(forward)
              329009777  314.560    0.000 11723.959    0.000 functional.py:1737(linear)
              329009777 11336.926    0.000 11336.926    0.000 {built-in method torch._C._nn.linear}
               26851328 1607.306    0.000 9456.697    0.000 optionCritic.py:91(get_action)
               26851328  621.657    0.000 7381.685    0.000 optionCritic.py:80(predict_option_termination)
                 839104   20.726    0.000 6025.450    0.007 optimizer.py:84(wrapper)
                 839104   11.735    0.000 5948.419    0.007 grad_mode.py:24(decorate_context)
                 839104   52.753    0.000 5915.970    0.007 adam.py:55(step)
                 839104  332.556    0.000 5807.030    0.007 _functional.py:53(adam)
               53702656  655.011    0.000 3969.306    0.000 distribution.py:34(__init__)
              248584563  255.671    0.000 3446.592    0.000 activation.py:713(forward)
                 839104    5.910    0.000 3400.654    0.004 game.py:42(step)
                 839104    8.607    0.000 3329.846    0.004 layers.py:827(step)
              248584563  254.501    0.000 3190.921    0.000 functional.py:1364(leaky_relu)
               26851328  268.370    0.000 3125.826    0.000 categorical.py:115(log_prob)
               26851328  248.530    0.000 3074.917    0.000 bernoulli.py:34(__init__)
                 209776   37.310    0.000 2894.311    0.014 optionCritic.py:116(critic_loss_fn)
              248584563 2884.193    0.000 2884.193    0.000 {built-in method torch._C._nn.leaky_relu}
               82522975  196.527    0.000 2786.767    0.000 optionCritic.py:77(get_Q)
               26851328  358.317    0.000 2656.606    0.000 categorical.py:49(__init__)
               53912432  204.833    0.000 2174.393    0.000 optionCritic.py:88(get_terminations)
                 839105   81.415    0.000 2053.546    0.002 layers.py:793(update)
               26851328 1089.081    0.000 1618.963    0.000 constraints.py:398(check)
                1549472   21.584    0.000 1455.016    0.001 layers.py:849(restart)
               23494900 1271.095    0.000 1271.095    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               26851328  219.726    0.000 1264.404    0.000 distribution.py:240(_validate_sample)
                 839104   38.858    0.000 1263.690    0.002 layers.py:17(step)
                1549472   10.755    0.000 1240.923    0.001 level.py:8(__init__)
               26851328  103.199    0.000 1221.542    0.000 layer.py:106(move)
                1549472   76.714    0.000 1148.379    0.001 levels.py:277(generate)
               11747450 1145.132    0.000 1145.132    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               26851328  251.357    0.000 1136.462    0.000 bernoulli.py:86(sample)
               26851328 1109.489    0.000 1109.489    0.000 constraints.py:364(check)
               11747450 1022.373    0.000 1022.373    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               13815526  165.628    0.000 1004.008    0.000 level.py:41(notUsed)
               82861521  109.488    0.000  997.098    0.000 activation.py:101(forward)
               82861521   96.156    0.000  887.610    0.000 functional.py:1195(relu)
             1289425693  878.181    0.000  878.243    0.000 module.py:934(__getattr__)
               26851328  451.952    0.000  872.181    0.000 categorical.py:123(entropy)
               26851328  133.039    0.000  847.583    0.000 layers.py:844(check)
              187959296  827.335    0.000  827.335    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               26851328  823.277    0.000  823.277    0.000 constraints.py:249(check)
               80973536  102.811    0.000  784.292    0.000 tensor.py:525(__rsub__)
               80553984  105.182    0.000  778.467    0.000 utils.py:106(__get__)
               82861521  777.316    0.000  777.316    0.000 {built-in method relu}
               82861521   81.480    0.000  774.958    0.000 flatten.py:39(forward)
               53702656  286.606    0.000  773.654    0.000 functional.py:46(broadcast_tensors)
               26851328  158.197    0.000  716.408    0.000 utils.py:11(broadcast_all)
               82861521  693.478    0.000  693.478    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               11747450  687.051    0.000  687.051    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                9230144   23.902    0.000  673.892    0.000 tensor.py:575(__iter__)
               23494900  673.053    0.000  673.053    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               11747450  669.994    0.000  669.994    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               80973536  667.462    0.000  667.462    0.000 {built-in method rsub}
               53912432  640.296    0.000  640.296    0.000 {method 'max' of 'torch._C._TensorBase' objects}
                9230144  635.405    0.000  635.405    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
             1001132089  629.426    0.000  629.426    0.000 {built-in method torch._C._get_tracing_state}
               26851328  171.712    0.000  616.848    0.000 categorical.py:108(sample)
               80763760  601.845    0.000  601.845    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
               26851328   31.879    0.000  592.559    0.000 categorical.py:88(logits)
               26851328   38.134    0.000  560.680    0.000 utils.py:82(probs_to_logits)
               80553984  554.264    0.000  554.264    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
             4270463377  535.713    0.000  542.662    0.000 {built-in method builtins.len}
               80553984  492.100    0.000  492.100    0.000 {method 'all' of 'torch._C._TensorBase' objects}
               13815526   13.297    0.000  482.495    0.000 level.py:38(elementsIn)
                 209776  392.435    0.002  475.824    0.002 replaybuffer.py:42(sample_option_critic)
             4050469301  451.534    0.000  451.534    0.000 {method 'values' of 'collections.OrderedDict' objects}
               26851328  424.104    0.000  424.104    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               53702656  410.668    0.000  410.668    0.000 {built-in method broadcast_tensors}
                 839104   41.579    0.000  370.095    0.000 replaybuffer.py:34(save_option_critic)
                5873735  249.052    0.000  348.744    0.000 layer.py:159(update)
               26851328  331.039    0.000  331.039    0.000 {built-in method bernoulli}
             1097955471  231.499    0.000  330.821    0.000 enum.py:646(__hash__)
               26851328   64.913    0.000  329.331    0.000 utils.py:77(clamp_probs)
               13815526  157.011    0.000  318.319    0.000 level.py:39(<listcomp>)
               81183312  316.083    0.000  316.083    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               28400767  271.978    0.000  271.978    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               26851328  264.418    0.000  264.418    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
               26851328  262.745    0.000  262.745    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
              161527520  255.887    0.000  255.887    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               26851328  185.455    0.000  252.949    0.000 layers.py:471(check)
                 839104   40.396    0.000  249.570    0.000 optimizer.py:189(zero_grad)
              353393879  148.198    0.000  234.403    0.000 {built-in method builtins.isinstance}
               53702656  231.490    0.000  231.490    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               26851328  223.722    0.000  223.722    0.000 {built-in method clamp}
               82105132  222.588    0.000  222.588    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               26851328   42.784    0.000  219.865    0.000 layers.py:838(isFree)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9624169: <Attempt6_Coconuts_option_critic_1> in cluster <dcc> Done

Job <Attempt6_Coconuts_option_critic_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun May  9 01:22:29 2021
Job was executed on host(s) <n-62-11-62>, in queue <hpc>, as user <s183914> in cluster <dcc> at Sun May  9 01:22:30 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun May  9 01:22:30 2021
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

    CPU time :                                   258287.98 sec.
    Max Memory :                                 863 MB
    Average Memory :                             852.83 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15521.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258956 sec.
    Turnaround time :                            258905 sec.

The output (if any) is above this job summary.

