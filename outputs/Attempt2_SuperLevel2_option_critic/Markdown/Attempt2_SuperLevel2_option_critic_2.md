
# Parameters

    Name :                      Attempt2_SuperLevel2_option_critic-2
    Main :                      option_critic_run
    Level :                     Levels.SuperLevel2
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


      48422349193 function calls (46843600623 primitive calls) in 258893.69 seconds

##    Ordered by: cumulative time
   List reduced from 441 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.629 258900.629 {built-in method builtins.exec}
                      1    0.345    0.345 258900.629 258900.629 <string>:1(<module>)
                      1 6021.884 6021.884 258900.284 258900.284 optionCritic.py:195(option_critic_run)
               56143250 10099.117    0.000 118267.510    0.002 optionCritic.py:143(actor_loss_fn)
        2084976315/513526752 10901.248    0.000 116041.595    0.000 module.py:866(_call_impl)
              174605507  880.612    0.000 108234.846    0.001 optionCritic.py:70(get_state)
              174605507 2400.848    0.000 104673.710    0.001 container.py:117(forward)
                2245730   18.135    0.000 68795.577    0.031 tensor.py:195(backward)
                2245730   21.827    0.000 68777.140    0.031 __init__.py:68(backward)
                2245730 68702.998    0.031 68702.998    0.031 {method 'run_backward' of 'torch._C._EngineBase' objects}
              349211014  986.623    0.000 64876.298    0.000 conv.py:398(forward)
              349211014  546.925    0.000 63429.967    0.000 conv.py:390(_conv_forward)
              349211014 62883.042    0.000 62883.042    0.000 {built-in method conv2d}
              688132259 1667.800    0.000 22785.671    0.000 linear.py:93(forward)
              688132259  679.036    0.000 20323.400    0.000 functional.py:1737(linear)
               56143250 3381.173    0.000 20030.393    0.000 optionCritic.py:91(get_action)
              688132259 19495.222    0.000 19495.222    0.000 {built-in method torch._C._nn.linear}
               56143250 1351.110    0.000 16050.388    0.000 optionCritic.py:80(predict_option_termination)
                2245730   49.898    0.000 8600.925    0.004 optimizer.py:84(wrapper)
              112286500 1422.531    0.000 8590.800    0.000 distribution.py:34(__init__)
                2245730   26.998    0.000 8412.203    0.004 grad_mode.py:24(decorate_context)
                2245730  123.150    0.000 8336.883    0.004 rmsprop.py:56(step)
                2245730  130.350    0.000 8072.412    0.004 _functional.py:203(rmsprop)
              523816521  539.873    0.000 7510.002    0.000 activation.py:713(forward)
               56143250  598.856    0.000 7002.493    0.000 bernoulli.py:34(__init__)
              523816521  576.040    0.000 6970.129    0.000 functional.py:1364(leaky_relu)
               56143250  565.795    0.000 6738.801    0.000 categorical.py:115(log_prob)
              523816521 6274.649    0.000 6274.649    0.000 {built-in method torch._C._nn.leaky_relu}
              169930063  383.200    0.000 5688.075    0.000 optionCritic.py:77(get_Q)
               56143250  762.317    0.000 5572.035    0.000 categorical.py:49(__init__)
                 561432   96.959    0.000 4831.243    0.009 optionCritic.py:116(critic_loss_fn)
              112847932  442.758    0.000 4692.475    0.000 optionCritic.py:88(get_terminations)
               31440214 4135.554    0.000 4135.554    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                2245730   11.643    0.000 3509.378    0.002 game.py:42(step)
               56143250 2284.604    0.000 3390.335    0.000 constraints.py:398(check)
                2245730   22.121    0.000 3366.722    0.001 layers.py:827(step)
               31440214 2855.728    0.000 2855.728    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               56143250  466.897    0.000 2749.591    0.000 distribution.py:240(_validate_sample)
               56143250 2549.998    0.000 2549.998    0.000 constraints.py:364(check)
               56143250  532.445    0.000 2363.160    0.000 bernoulli.py:86(sample)
              174605507  252.589    0.000 2164.824    0.000 activation.py:101(forward)
             2700791799 2053.356    0.000 2053.517    0.000 module.py:934(__getattr__)
              393002750 2035.946    0.000 2035.946    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              174605507  215.485    0.000 1912.235    0.000 functional.py:1195(relu)
                2245730   80.551    0.000 1879.207    0.001 layers.py:17(step)
               56143250  959.904    0.000 1840.337    0.000 categorical.py:123(entropy)
               56143250 1808.984    0.000 1808.984    0.000 constraints.py:249(check)
               56143250  138.414    0.000 1791.207    0.000 layer.py:106(move)
              174605507  277.837    0.000 1787.714    0.000 flatten.py:39(forward)
              112286500  613.032    0.000 1731.675    0.000 functional.py:46(broadcast_tensors)
              169552614  227.007    0.000 1702.125    0.000 tensor.py:525(__rsub__)
              168429750  235.676    0.000 1682.709    0.000 utils.py:106(__get__)
              174605507 1667.263    0.000 1667.263    0.000 {built-in method relu}
               56143250  364.025    0.000 1664.860    0.000 utils.py:11(broadcast_all)
              174605507 1509.877    0.000 1509.877    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                2245731  180.241    0.000 1457.837    0.001 layers.py:793(update)
              169552614 1446.578    0.000 1446.578    0.000 {built-in method rsub}
              112847932 1414.420    0.000 1414.420    0.000 {method 'max' of 'torch._C._TensorBase' objects}
               24703030   60.311    0.000 1348.821    0.000 tensor.py:575(__iter__)
               56143250  369.005    0.000 1316.853    0.000 categorical.py:108(sample)
             2109679345 1294.545    0.000 1294.545    0.000 {built-in method torch._C._get_tracing_state}
              168991182 1293.773    0.000 1293.773    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
               56143250   68.495    0.000 1273.833    0.000 categorical.py:88(logits)
               24703030 1252.396    0.000 1252.396    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               56143250   68.565    0.000 1205.337    0.000 utils.py:82(probs_to_logits)
             9056035563 1144.039    0.000 1160.877    0.000 {built-in method builtins.len}
              168429750 1146.773    0.000 1146.773    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 561432  915.222    0.002 1132.967    0.002 replaybuffer.py:42(sample_option_critic)
               56143250  280.517    0.000 1100.055    0.000 layers.py:844(check)
              168429750 1032.454    0.000 1032.454    0.000 {method 'all' of 'torch._C._TensorBase' objects}
             8514510767 1004.952    0.000 1004.952    0.000 {method 'values' of 'collections.OrderedDict' objects}
              112286500  931.350    0.000  931.350    0.000 {built-in method broadcast_tensors}
               56143250  855.306    0.000  855.306    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
                2245730   86.980    0.000  732.179    0.000 replaybuffer.py:34(save_option_critic)
               56143250  157.334    0.000  704.838    0.000 utils.py:77(clamp_probs)
              170114046  692.323    0.000  692.323    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               56143250  684.267    0.000  684.267    0.000 {built-in method bernoulli}
                2245730  104.173    0.000  617.079    0.000 optimizer.py:189(zero_grad)
               56143250  583.534    0.000  583.534    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
              337982364  570.568    0.000  570.568    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               56143250  547.504    0.000  547.504    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
              744253092  325.510    0.000  543.321    0.000 {built-in method builtins.isinstance}
               56520699  538.302    0.000  538.302    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
              168811713  489.824    0.000  489.824    0.000 {method 'item' of 'torch._C._TensorBase' objects}
              112286500  487.278    0.000  487.278    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               56143250  465.426    0.000  465.426    0.000 {built-in method clamp}
               56143250   80.294    0.000  463.426    0.000 layers.py:838(isFree)
               17965848  274.643    0.000  461.786    0.000 layer.py:175(NoRock_update)
               15158680  435.361    0.000  435.361    0.000 {built-in method tensor}
               56143250  431.935    0.000  431.935    0.000 {built-in method log}
              174605521  408.994    0.000  408.994    0.000 {method 'to' of 'torch._C._TensorBase' objects}
               56143250  402.306    0.000  402.306    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
              235567719  332.777    0.000  383.132    0.000 layer.py:103(isFree)
                 377473    7.668    0.000  374.917    0.001 layers.py:849(restart)
               31440214  369.753    0.000  369.753    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               58389006  198.786    0.000  368.511    0.000 grad_mode.py:119(__enter__)
               56143250  367.334    0.000  367.334    0.000 {built-in method all}
              168429775  135.466    0.000  348.672    0.000 {built-in method builtins.all}
               56143250  340.814    0.000  340.814    0.000 {built-in method multinomial}
                6737194   14.810    0.000  336.042    0.000 game.py:38(board)


Traceback (most recent call last):
  File "main.py", line 239, in <module>
    run(Defaults)
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/auxillaries.py", line 133, in run
    (serverRun if isServer else Defaults.main).__call__(getvals(Defaults))
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils/server.py", line 37, in serverRun
    profilingStats()
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils/debug.py", line 62, in profilingStats
    os.remove('stats')
FileNotFoundError: [Errno 2] No such file or directory: 'stats'

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9606133: <Attempt2_SuperLevel2_option_critic_2> in cluster <dcc> Exited

Job <Attempt2_SuperLevel2_option_critic_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon May  3 01:33:11 2021
Job was executed on host(s) <n-62-11-69>, in queue <hpc>, as user <s183914> in cluster <dcc> at Mon May  3 01:33:12 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon May  3 01:33:12 2021
Terminated at Thu May  6 01:28:32 2021
Results reported at Thu May  6 01:28:32 2021

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

Exited with exit code 1.

Resource usage summary:

    CPU time :                                   258283.33 sec.
    Max Memory :                                 1179 MB
    Average Memory :                             1167.56 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15205.00 MB
    Max Swap :                                   -
    Max Processes :                              6
    Max Threads :                                7
    Run time :                                   258948 sec.
    Turnaround time :                            258921 sec.

The output (if any) is above this job summary.

