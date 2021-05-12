
# Parameters

    Name :                      Attempt5_Maze_option_critic-0
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


      15394882580 function calls (14889606749 primitive calls) in 258900.33 seconds

##    Ordered by: cumulative time
   List reduced from 442 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258901.981 258901.981 {built-in method builtins.exec}
                      1    0.331    0.331 258901.981 258901.981 <string>:1(<module>)
                      1 1776.155 1776.155 258901.650 258901.650 optionCritic.py:195(option_critic_run)
                 566452    4.872    0.000 198247.475    0.350 tensor.py:195(backward)
                 566452    6.139    0.000 198242.515    0.350 __init__.py:68(backward)
                 566452 198223.535    0.350 198223.535    0.350 {method 'run_backward' of 'torch._C._EngineBase' objects}
               18126464 2943.125    0.000 36226.588    0.002 optionCritic.py:143(actor_loss_fn)
        668631457/165197233 3282.699    0.000 36104.864    0.000 module.py:866(_call_impl)
               55937136  258.997    0.000 33578.388    0.001 optionCritic.py:70(get_state)
               55937136  706.043    0.000 32517.118    0.001 container.py:117(forward)
              111874272  315.765    0.000 20139.777    0.000 conv.py:398(forward)
              111874272  170.539    0.000 19697.894    0.000 conv.py:390(_conv_forward)
              111874272 19527.355    0.000 19527.355    0.000 {built-in method conv2d}
              221134369  538.442    0.000 7303.215    0.000 linear.py:93(forward)
               18126464 1146.322    0.000 6910.488    0.000 optionCritic.py:91(get_action)
              221134369  208.936    0.000 6542.843    0.000 functional.py:1737(linear)
              221134369 6279.900    0.000 6279.900    0.000 {built-in method torch._C._nn.linear}
                 566452   14.455    0.000 4642.057    0.008 optimizer.py:84(wrapper)
                 566452    7.611    0.000 4586.810    0.008 grad_mode.py:24(decorate_context)
                 566452   38.532    0.000 4565.326    0.008 adam.py:55(step)
                 566452  211.507    0.000 4483.949    0.008 _functional.py:53(adam)
               18126464  373.188    0.000 4456.128    0.000 optionCritic.py:80(predict_option_termination)
               36252928  393.537    0.000 2602.492    0.000 distribution.py:34(__init__)
               18126464  192.712    0.000 2304.739    0.000 categorical.py:115(log_prob)
              167811408  166.099    0.000 2281.149    0.000 activation.py:713(forward)
              167811408  166.360    0.000 2115.049    0.000 functional.py:1364(leaky_relu)
               18126464  256.051    0.000 1940.195    0.000 categorical.py:49(__init__)
              167811408 1911.720    0.000 1911.720    0.000 {built-in method torch._C._nn.leaky_relu}
               54739092  134.903    0.000 1845.842    0.000 optionCritic.py:77(get_Q)
               18126464  127.296    0.000 1672.618    0.000 bernoulli.py:34(__init__)
               36394541  129.930    0.000 1432.035    0.000 optionCritic.py:88(get_terminations)
                 141613   22.972    0.000 1415.172    0.010 optionCritic.py:116(critic_loss_fn)
               18126464  795.738    0.000 1187.379    0.000 constraints.py:398(check)
                 566452    3.281    0.000 1166.092    0.002 game.py:42(step)
                 566452    5.725    0.000 1127.669    0.002 layers.py:827(step)
               15860644  991.946    0.000  991.946    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               18126464  168.204    0.000  938.996    0.000 distribution.py:240(_validate_sample)
                7930322  935.638    0.000  935.638    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                7930322  726.436    0.000  726.436    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               55937136   79.113    0.000  679.666    0.000 activation.py:101(forward)
               18126464  132.507    0.000  668.437    0.000 bernoulli.py:86(sample)
                 566452   26.747    0.000  665.131    0.001 layers.py:17(step)
               18126464  648.008    0.000  648.008    0.000 constraints.py:364(check)
               18126464  335.031    0.000  643.312    0.000 categorical.py:123(entropy)
               18126464   46.120    0.000  635.486    0.000 layer.py:106(move)
               18126464  602.331    0.000  602.331    0.000 constraints.py:249(check)
              867541148  601.945    0.000  601.992    0.000 module.py:934(__getattr__)
               55937136   63.757    0.000  600.553    0.000 functional.py:1195(relu)
               54379392   77.482    0.000  580.188    0.000 utils.py:106(__get__)
              126885248  570.167    0.000  570.167    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                7930322  549.864    0.000  549.864    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               15860644  537.507    0.000  537.507    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               55937136   53.894    0.000  530.919    0.000 flatten.py:39(forward)
                7930322  527.509    0.000  527.509    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               55937136  526.119    0.000  526.119    0.000 {built-in method relu}
               54662618   56.825    0.000  493.924    0.000 tensor.py:525(__rsub__)
               55937136  477.025    0.000  477.025    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               36252928  169.316    0.000  471.011    0.000 functional.py:46(broadcast_tensors)
               18126464  128.162    0.000  459.880    0.000 categorical.py:108(sample)
                 566453   58.489    0.000  454.085    0.001 layers.py:793(update)
               18126464   22.306    0.000  441.645    0.000 categorical.py:88(logits)
                6230972   14.740    0.000  436.276    0.000 tensor.py:575(__iter__)
               54662618  427.007    0.000  427.007    0.000 {built-in method rsub}
               18126464   25.354    0.000  419.340    0.000 utils.py:82(probs_to_logits)
              674862429  415.425    0.000  415.425    0.000 {built-in method torch._C._get_tracing_state}
                6230972  412.114    0.000  412.114    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
             2899818855  402.709    0.000  406.928    0.000 {built-in method builtins.len}
               54521005  405.470    0.000  405.470    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
               54379392  404.830    0.000  404.830    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
               36394541  396.603    0.000  396.603    0.000 {method 'max' of 'torch._C._TensorBase' objects}
               18126464   94.076    0.000  385.216    0.000 layers.py:844(check)
               18126464   73.429    0.000  369.757    0.000 utils.py:11(broadcast_all)
             2730462964  331.553    0.000  331.553    0.000 {method 'values' of 'collections.OrderedDict' objects}
               54379392  329.625    0.000  329.625    0.000 {method 'all' of 'torch._C._TensorBase' objects}
               18126464  301.593    0.000  301.593    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
                 141613  233.299    0.002  294.522    0.002 replaybuffer.py:42(sample_option_critic)
               36252928  252.298    0.000  252.298    0.000 {built-in method broadcast_tensors}
               18126464   50.157    0.000  247.459    0.000 utils.py:77(clamp_probs)
                 566452   28.004    0.000  240.450    0.000 replaybuffer.py:34(save_option_critic)
               54804231  209.146    0.000  209.146    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               18126464  199.440    0.000  199.440    0.000 {built-in method bernoulli}
               18126464  197.301    0.000  197.301    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
               18126464  196.500    0.000  196.500    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
               18202938  178.900    0.000  178.900    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
              109042010  172.627    0.000  172.627    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               18126464   31.233    0.000  170.495    0.000 layers.py:838(isFree)
               36252928  170.214    0.000  170.214    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               18126464  163.462    0.000  163.462    0.000 {built-in method clamp}
                 566452   28.112    0.000  161.867    0.000 optimizer.py:189(zero_grad)
                4531624   92.650    0.000  159.330    0.000 layer.py:175(NoRock_update)
               18126464  146.527    0.000  146.527    0.000 {built-in method log}
               18126464  141.216    0.000  141.216    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
               89563566  119.590    0.000  139.262    0.000 layer.py:103(isFree)
               18126464  131.945    0.000  131.945    0.000 {built-in method all}
                3823555  118.650    0.000  118.650    0.000 {built-in method tensor}
              239136468   78.975    0.000  116.919    0.000 {built-in method builtins.isinstance}
               18126464  116.905    0.000  116.905    0.000 {built-in method multinomial}
               55937150  116.557    0.000  116.557    0.000 {method 'to' of 'torch._C._TensorBase' objects}
               18126464   68.768    0.000  114.077    0.000 layers.py:168(check)
               54457029  105.979    0.000  105.979    0.000 {method 'item' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9618613: <Attempt5_Maze_option_critic_0> in cluster <dcc> Done

Job <Attempt5_Maze_option_critic_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Thu May  6 02:11:27 2021
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

    CPU time :                                   258287.39 sec.
    Max Memory :                                 938 MB
    Average Memory :                             923.85 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15446.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258972 sec.
    Turnaround time :                            507455 sec.

The output (if any) is above this job summary.

