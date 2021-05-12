
# Parameters

    Name :                      Attempt5_Maze_option_critic-2
    Main :                      option_critic_run
    Level :                     Levels.Maze
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


      15079478002 function calls (14584943512 primitive calls) in 258900.16 seconds

##    Ordered by: cumulative time
   List reduced from 443 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258901.760 258901.760 {built-in method builtins.exec}
                      1    0.337    0.337 258901.760 258901.760 <string>:1(<module>)
                      1 1724.574 1724.574 258901.423 258901.423 optionCritic.py:195(option_critic_run)
                 554410    4.771    0.000 199001.367    0.359 tensor.py:195(backward)
                 554410    5.987    0.000 198996.514    0.359 __init__.py:68(backward)
                 554410 198978.073    0.359 198978.073    0.359 {method 'run_backward' of 'torch._C._EngineBase' objects}
               17741120 2902.109    0.000 35539.808    0.002 optionCritic.py:143(actor_loss_fn)
        654416598/161684715 3150.650    0.000 35485.404    0.000 module.py:866(_call_impl)
               54747987  252.316    0.000 33032.894    0.001 optionCritic.py:70(get_state)
               54747987  710.421    0.000 32002.096    0.001 container.py:117(forward)
              109495974  297.814    0.000 19626.237    0.000 conv.py:398(forward)
              109495974  169.337    0.000 19208.706    0.000 conv.py:390(_conv_forward)
              109495974 19039.369    0.000 19039.369    0.000 {built-in method conv2d}
              216432702  522.711    0.000 7432.534    0.000 linear.py:93(forward)
               17741120 1123.875    0.000 6758.520    0.000 optionCritic.py:91(get_action)
              216432702  202.275    0.000 6694.332    0.000 functional.py:1737(linear)
              216432702 6441.608    0.000 6441.608    0.000 {built-in method torch._C._nn.linear}
                 554410   13.425    0.000 4941.638    0.009 optimizer.py:84(wrapper)
                 554410    7.084    0.000 4889.048    0.009 grad_mode.py:24(decorate_context)
                 554410   38.211    0.000 4868.464    0.009 adam.py:55(step)
                 554410  206.417    0.000 4788.429    0.009 _functional.py:53(adam)
               17741120  361.648    0.000 4315.508    0.000 optionCritic.py:80(predict_option_termination)
               35482240  375.969    0.000 2542.498    0.000 distribution.py:34(__init__)
              164243961  162.488    0.000 2269.401    0.000 activation.py:713(forward)
               17741120  185.439    0.000 2257.308    0.000 categorical.py:115(log_prob)
              164243961  173.547    0.000 2106.913    0.000 functional.py:1364(leaky_relu)
              164243961 1899.960    0.000 1899.960    0.000 {built-in method torch._C._nn.leaky_relu}
               17741120  250.931    0.000 1899.641    0.000 categorical.py:49(__init__)
               53574766  131.259    0.000 1793.493    0.000 optionCritic.py:77(get_Q)
               17741120  124.299    0.000 1639.892    0.000 bernoulli.py:34(__init__)
                 138602   22.844    0.000 1418.518    0.010 optionCritic.py:116(critic_loss_fn)
               35620842  134.377    0.000 1399.370    0.000 optionCritic.py:88(get_terminations)
               17741120  783.214    0.000 1164.460    0.000 constraints.py:398(check)
                 554410    2.736    0.000 1139.233    0.002 game.py:42(step)
                 554410    5.575    0.000 1102.453    0.002 layers.py:827(step)
               15523468 1060.512    0.000 1060.512    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                7761734 1023.640    0.000 1023.640    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               17741120  159.148    0.000  914.897    0.000 distribution.py:240(_validate_sample)
                7761734  747.463    0.000  747.463    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               54747987   72.297    0.000  650.568    0.000 activation.py:101(forward)
                 554410   25.951    0.000  648.868    0.001 layers.py:17(step)
               17741120  638.974    0.000  638.974    0.000 constraints.py:364(check)
               17741120  116.878    0.000  631.325    0.000 bernoulli.py:86(sample)
               17741120  323.930    0.000  623.290    0.000 categorical.py:123(entropy)
               17741120   46.473    0.000  620.359    0.000 layer.py:106(move)
                7761734  596.564    0.000  596.564    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               17741120  588.283    0.000  588.283    0.000 constraints.py:249(check)
              849096452  584.099    0.000  584.146    0.000 module.py:934(__getattr__)
               15523468  580.069    0.000  580.069    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               54747987   60.647    0.000  578.271    0.000 functional.py:1195(relu)
               53223360   76.178    0.000  572.065    0.000 utils.py:106(__get__)
                7761734  570.471    0.000  570.471    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              124187840  565.059    0.000  565.059    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               54747987   53.525    0.000  514.049    0.000 flatten.py:39(forward)
               54747987  508.101    0.000  508.101    0.000 {built-in method relu}
               53500564   56.934    0.000  484.235    0.000 tensor.py:525(__rsub__)
               35482240  163.475    0.000  466.417    0.000 functional.py:46(broadcast_tensors)
               54747987  460.525    0.000  460.525    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                 554411   55.919    0.000  445.342    0.001 layers.py:793(update)
               17741120  121.851    0.000  444.444    0.000 categorical.py:108(sample)
               17741120   22.584    0.000  436.777    0.000 categorical.py:88(logits)
                6098510   14.628    0.000  429.169    0.000 tensor.py:575(__iter__)
               53500564  417.833    0.000  417.833    0.000 {built-in method rsub}
               17741120   24.073    0.000  414.193    0.000 utils.py:82(probs_to_logits)
                6098510  405.040    0.000  405.040    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
              660515108  404.351    0.000  404.351    0.000 {built-in method torch._C._get_tracing_state}
               53223360  393.405    0.000  393.405    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
               35620842  393.004    0.000  393.004    0.000 {method 'max' of 'torch._C._TensorBase' objects}
               53361962  390.074    0.000  390.074    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
             2838061830  378.805    0.000  382.912    0.000 {built-in method builtins.len}
               17741120   93.380    0.000  375.283    0.000 layers.py:844(check)
               17741120   76.448    0.000  369.852    0.000 utils.py:11(broadcast_all)
               53223360  323.778    0.000  323.778    0.000 {method 'all' of 'torch._C._TensorBase' objects}
             2672414379  313.305    0.000  313.305    0.000 {method 'values' of 'collections.OrderedDict' objects}
               17741120  297.835    0.000  297.835    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
                 138602  227.637    0.002  286.295    0.002 replaybuffer.py:42(sample_option_critic)
               17741120   51.578    0.000  248.089    0.000 utils.py:77(clamp_probs)
               35482240  247.555    0.000  247.555    0.000 {built-in method broadcast_tensors}
                 554410   26.533    0.000  237.033    0.000 replaybuffer.py:34(save_option_critic)
               53639166  205.259    0.000  205.259    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               17741120  196.511    0.000  196.511    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
               17741120  193.998    0.000  193.998    0.000 {built-in method bernoulli}
               17741120  192.183    0.000  192.183    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
               17815322  175.115    0.000  175.115    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
              106723924  169.207    0.000  169.207    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               17741120   32.438    0.000  166.241    0.000 layers.py:838(isFree)
               35482240  164.603    0.000  164.603    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               17741120  159.097    0.000  159.097    0.000 {built-in method clamp}
                 554410   27.950    0.000  157.567    0.000 optimizer.py:189(zero_grad)
                4435288   89.900    0.000  154.519    0.000 layer.py:175(NoRock_update)
               17741120  142.031    0.000  142.031    0.000 {built-in method log}
               17741120  140.241    0.000  140.241    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
               87862932  114.287    0.000  133.803    0.000 layer.py:103(isFree)
               17741120  127.190    0.000  127.190    0.000 {built-in method all}
                3742270  116.182    0.000  116.182    0.000 {built-in method tensor}
               17741120  115.522    0.000  115.522    0.000 {built-in method multinomial}
               54748001  112.532    0.000  112.532    0.000 {method 'to' of 'torch._C._TensorBase' objects}
              234047502   74.174    0.000  111.698    0.000 {built-in method builtins.isinstance}
               17741120   66.141    0.000  110.118    0.000 layers.py:168(check)
               53298701  103.912    0.000  103.912    0.000 {method 'item' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9618615: <Attempt5_Maze_option_critic_2> in cluster <dcc> Done

Job <Attempt5_Maze_option_critic_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Thu May  6 02:11:27 2021
Job was executed on host(s) <n-62-31-4>, in queue <hpc>, as user <s183914> in cluster <dcc> at Sat May  8 23:13:45 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat May  8 23:13:45 2021
Terminated at Tue May 11 23:09:02 2021
Results reported at Tue May 11 23:09:02 2021

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

    CPU time :                                   258290.84 sec.
    Max Memory :                                 943 MB
    Average Memory :                             924.08 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15441.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258972 sec.
    Turnaround time :                            507455 sec.

The output (if any) is above this job summary.

