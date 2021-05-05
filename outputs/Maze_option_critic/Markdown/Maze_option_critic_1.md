[W NNPACK.cpp:80] Could not initialize NNPACK! Reason: Unsupported hardware.

# Parameters

    Name :                      Maze_option_critic-1
    Main :                      option_critic_run
    Level :                     Levels.Maze
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


      32958988719 function calls (31914055671 primitive calls) in 258892.19 seconds

##    Ordered by: cumulative time
   List reduced from 441 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.549 258900.549 {built-in method builtins.exec}
                      1    0.353    0.353 258900.549 258900.549 <string>:1(<module>)
                      1 3930.971 3930.971 258900.195 258900.195 optionCritic.py:195(option_critic_run)
        1380127018/340024927 10561.794    0.000 110637.668    0.000 module.py:866(_call_impl)
               37159775 10091.100    0.000 108854.366    0.003 optionCritic.py:143(actor_loss_fn)
              115566899  760.490    0.000 101291.586    0.001 optionCritic.py:70(get_state)
              115566899 2799.175    0.000 98145.909    0.001 container.py:117(forward)
                1486391   12.071    0.000 81390.314    0.055 tensor.py:195(backward)
                1486391   13.917    0.000 81377.949    0.055 __init__.py:68(backward)
                1486391 81325.753    0.055 81325.753    0.055 {method 'run_backward' of 'torch._C._EngineBase' objects}
              231133798  898.314    0.000 59596.646    0.000 conv.py:398(forward)
              231133798  381.254    0.000 58366.689    0.000 conv.py:390(_conv_forward)
              231133798 57985.435    0.000 57985.435    0.000 {built-in method conv2d}
               37159775 3978.597    0.000 23427.007    0.001 optionCritic.py:91(get_action)
              455591826 1590.892    0.000 21814.405    0.000 linear.py:93(forward)
              455591826  614.257    0.000 19612.797    0.000 functional.py:1737(linear)
              455591826 18865.279    0.000 18865.279    0.000 {built-in method torch._C._nn.linear}
               37159775 1220.247    0.000 13178.238    0.000 optionCritic.py:80(predict_option_termination)
               74319550 1116.040    0.000 8576.030    0.000 distribution.py:34(__init__)
              346700697  445.790    0.000 8105.227    0.000 activation.py:713(forward)
              346700697  455.994    0.000 7659.437    0.000 functional.py:1364(leaky_relu)
               37159775  607.369    0.000 7640.002    0.000 categorical.py:115(log_prob)
              346700697 7108.626    0.000 7108.626    0.000 {built-in method torch._C._nn.leaky_relu}
               37159775  886.174    0.000 6896.605    0.000 categorical.py:49(__init__)
              112607106  459.065    0.000 6473.069    0.000 optionCritic.py:77(get_Q)
                 371597   86.713    0.000 6426.111    0.017 optionCritic.py:116(critic_loss_fn)
               74691147  461.569    0.000 5250.592    0.000 optionCritic.py:88(get_terminations)
               37159775  285.268    0.000 4647.185    0.000 bernoulli.py:34(__init__)
                1486391   33.901    0.000 4286.936    0.003 optimizer.py:84(wrapper)
               37159775 2844.652    0.000 4284.786    0.000 constraints.py:398(check)
                1486391   17.369    0.000 4160.004    0.003 grad_mode.py:24(decorate_context)
                1486391  104.023    0.000 4110.629    0.003 rmsprop.py:56(step)
                1486391  156.979    0.000 3894.147    0.003 _functional.py:203(rmsprop)
               37159775  463.510    0.000 3218.380    0.000 distribution.py:240(_validate_sample)
                1486391    9.125    0.000 3132.989    0.002 game.py:41(step)
                1486391   13.895    0.000 3016.273    0.002 layers.py:718(step)
              115566899  168.649    0.000 2307.782    0.000 activation.py:101(forward)
               37159775 1110.117    0.000 2284.450    0.000 categorical.py:123(entropy)
               37159775 2186.876    0.000 2186.876    0.000 constraints.py:249(check)
              115566899  142.101    0.000 2139.133    0.000 functional.py:1195(relu)
               37159775 2062.338    0.000 2062.338    0.000 constraints.py:364(check)
              115566899 1966.733    0.000 1966.733    0.000 {built-in method relu}
              111479325  226.526    0.000 1880.938    0.000 utils.py:106(__get__)
              260118425 1860.216    0.000 1860.216    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               20809468 1855.796    0.000 1855.796    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
             1396477319 1834.406    0.000 1834.406    0.000 {built-in method torch._C._get_tracing_state}
               37159775  340.594    0.000 1774.657    0.000 bernoulli.py:86(sample)
              112222519  189.975    0.000 1715.183    0.000 tensor.py:525(__rsub__)
              111479325 1624.327    0.000 1624.327    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
             1787989004 1603.894    0.000 1604.045    0.000 module.py:934(__getattr__)
              115566899  119.166    0.000 1603.369    0.000 flatten.py:39(forward)
                1486391   64.696    0.000 1530.105    0.001 layers.py:17(step)
              112222519 1493.076    0.000 1493.076    0.000 {built-in method rsub}
               37159775   72.737    0.000 1490.426    0.000 categorical.py:88(logits)
              115566899 1484.203    0.000 1484.203    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              111850922 1482.335    0.000 1482.335    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
               37159775  381.859    0.000 1466.754    0.000 categorical.py:108(sample)
                1486392  148.456    0.000 1466.361    0.001 layers.py:684(update)
               37159775  107.609    0.000 1460.271    0.000 layer.py:98(move)
               37159775   76.523    0.000 1417.689    0.000 utils.py:82(probs_to_logits)
               74319550  400.708    0.000 1252.459    0.000 functional.py:46(broadcast_tensors)
               74691147 1212.295    0.000 1212.295    0.000 {method 'max' of 'torch._C._TensorBase' objects}
              111479325 1114.400    0.000 1114.400    0.000 {method 'all' of 'torch._C._TensorBase' objects}
             6000213686 1054.779    0.000 1068.046    0.000 {built-in method builtins.len}
               16350301   50.009    0.000 1050.915    0.000 tensor.py:575(__iter__)
               16350301  965.345    0.000  965.345    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
             5636074971  906.303    0.000  906.303    0.000 {method 'values' of 'collections.OrderedDict' objects}
               37159775  204.912    0.000  884.292    0.000 layers.py:735(check)
               37159775  178.308    0.000  883.674    0.000 utils.py:11(broadcast_all)
               37159775  134.529    0.000  868.691    0.000 utils.py:77(clamp_probs)
               37159775  830.187    0.000  830.187    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               13772074  366.279    0.000  765.586    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               74319550  746.294    0.000  746.294    0.000 {built-in method broadcast_tensors}
               37159775  734.162    0.000  734.162    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
              112594116  730.921    0.000  730.921    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
                1486391   76.752    0.000  709.894    0.000 replaybuffer.py:34(save_option_critic)
               37159775  694.103    0.000  694.103    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
                 371597  530.237    0.001  689.852    0.002 replaybuffer.py:42(sample_option_critic)
              223701844  644.493    0.000  644.493    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               37159775  640.358    0.000  640.358    0.000 {built-in method clamp}
               74319550  612.915    0.000  612.915    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               37544362  589.333    0.000  589.333    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               20809468  553.085    0.000  553.085    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               37159775  546.721    0.000  546.721    0.000 {built-in method bernoulli}
               20809468  498.787    0.000  498.787    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               37159775  483.358    0.000  483.358    0.000 {built-in method all}
                1486391   89.566    0.000  473.263    0.000 optimizer.py:189(zero_grad)
               37159775  472.475    0.000  472.475    0.000 {built-in method log}
               37159775  461.334    0.000  461.334    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
               20809468  450.484    0.000  450.484    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                 384611    9.475    0.000  450.484    0.001 layers.py:740(restart)
               37159775   95.493    0.000  404.340    0.000 layers.py:729(isFree)
               13772074   23.848    0.000  399.307    0.000 <__array_function__ internals>:2(prod)
               11891136  238.150    0.000  391.237    0.000 layer.py:167(NoRock_update)
                 384611    5.649    0.000  386.829    0.001 level.py:8(__init__)
               20809468  379.016    0.000  379.016    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               13772074   22.733    0.000  370.799    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                 524048   52.229    0.000  351.536    0.001 levels.py:9(generate)
               13772074   36.638    0.000  348.066    0.000 fromnumeric.py:2912(prod)
              493605827  234.709    0.000  346.789    0.000 {built-in method builtins.isinstance}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9601876: <Maze_option_critic_1> in cluster <dcc> Done

Job <Maze_option_critic_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Thu Apr 29 21:41:17 2021
Job was executed on host(s) <n-62-23-21>, in queue <hpc>, as user <s183914> in cluster <dcc> at Thu Apr 29 21:41:20 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Apr 29 21:41:20 2021
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

    CPU time :                                   258896.66 sec.
    Max Memory :                                 906 MB
    Average Memory :                             897.61 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15478.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258959 sec.
    Turnaround time :                            258906 sec.

The output (if any) is above this job summary.

