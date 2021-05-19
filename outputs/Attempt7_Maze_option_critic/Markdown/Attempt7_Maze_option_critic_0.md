[W NNPACK.cpp:80] Could not initialize NNPACK! Reason: Unsupported hardware.

# Parameters

    Name :                      Attempt7_Maze_option_critic-0
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


      36022895928 function calls (34879706148 primitive calls) in 258901.08 seconds

##    Ordered by: cumulative time
   List reduced from 429 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258901.075 258901.075 {built-in method builtins.exec}
                      1    0.368    0.368 258901.075 258901.075 <string>:1(<module>)
                      1 4330.729 4330.729 258900.707 258900.707 optionCritic.py:195(option_critic_run)
        1513338595/374314822 10814.265    0.000 114919.742    0.000 module.py:866(_call_impl)
               41011264 9807.002    0.000 114682.739    0.003 optionCritic.py:143(actor_loss_fn)
              126558197  854.282    0.000 104876.197    0.001 optionCritic.py:70(get_state)
              126558197 2985.081    0.000 101479.234    0.001 container.py:117(forward)
                1281602   10.969    0.000 70542.654    0.055 tensor.py:195(backward)
                1281602   12.210    0.000 70531.429    0.055 __init__.py:68(backward)
                1281602 70486.321    0.055 70486.321    0.055 {method 'run_backward' of 'torch._C._EngineBase' objects}
              253116394  975.736    0.000 60655.495    0.000 conv.py:398(forward)
              253116394  429.542    0.000 59335.137    0.000 conv.py:390(_conv_forward)
              253116394 58905.595    0.000 58905.595    0.000 {built-in method conv2d}
               41011264 4361.703    0.000 25686.239    0.001 optionCritic.py:91(get_action)
              500873019 1757.713    0.000 23303.966    0.000 linear.py:93(forward)
              500873019  645.773    0.000 20913.598    0.000 functional.py:1737(linear)
              500873019 20139.579    0.000 20139.579    0.000 {built-in method torch._C._nn.linear}
               41011264 1286.704    0.000 14040.206    0.000 optionCritic.py:80(predict_option_termination)
               82022528 1189.072    0.000 9320.416    0.000 distribution.py:34(__init__)
              379674591  497.836    0.000 8773.544    0.000 activation.py:713(forward)
               41011264  700.955    0.000 8415.385    0.000 categorical.py:115(log_prob)
              379674591  464.839    0.000 8275.708    0.000 functional.py:1364(leaky_relu)
              379674591 7709.578    0.000 7709.578    0.000 {built-in method torch._C._nn.leaky_relu}
               41011264  968.701    0.000 7542.623    0.000 categorical.py:49(__init__)
                1281602   26.260    0.000 7096.406    0.006 optimizer.py:84(wrapper)
              124402433  508.887    0.000 7009.108    0.000 optionCritic.py:77(get_Q)
                1281602   13.414    0.000 6987.573    0.005 grad_mode.py:24(decorate_context)
                1281602   87.606    0.000 6947.847    0.005 rmsprop.py:56(step)
                1281602  137.013    0.000 6760.898    0.005 _functional.py:203(rmsprop)
               82342928  492.614    0.000 5666.452    0.000 optionCritic.py:88(get_terminations)
                 320400   73.594    0.000 5220.703    0.016 optionCritic.py:116(critic_loss_fn)
               17942422 5038.720    0.000 5038.720    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               41011264  295.310    0.000 4949.232    0.000 bernoulli.py:34(__init__)
               41011264 3115.489    0.000 4714.667    0.000 constraints.py:398(check)
               41011264  512.247    0.000 3504.163    0.000 distribution.py:240(_validate_sample)
                1281602    8.429    0.000 2932.845    0.002 game.py:42(step)
                1281602   12.477    0.000 2832.037    0.002 layers.py:827(step)
              126558197  177.229    0.000 2506.268    0.000 activation.py:101(forward)
               41011264 1201.540    0.000 2480.797    0.000 categorical.py:123(entropy)
               41011264 2368.273    0.000 2368.273    0.000 constraints.py:249(check)
              126558197  156.024    0.000 2329.038    0.000 functional.py:1195(relu)
               41011264 2241.685    0.000 2241.685    0.000 constraints.py:364(check)
              126558197 2142.153    0.000 2142.153    0.000 {built-in method relu}
              123033792  231.773    0.000 2057.153    0.000 utils.py:106(__get__)
             1527436217 2010.576    0.000 2010.576    0.000 {built-in method torch._C._get_tracing_state}
              287078848 1984.762    0.000 1984.762    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               41011264  322.290    0.000 1844.688    0.000 bernoulli.py:86(sample)
              123674592  191.572    0.000 1843.722    0.000 tensor.py:525(__rsub__)
              123033792 1760.821    0.000 1760.821    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
              126558197  118.965    0.000 1729.127    0.000 flatten.py:39(forward)
             1964482857 1680.542    0.000 1680.669    0.000 module.py:934(__getattr__)
               41011264   81.989    0.000 1646.267    0.000 categorical.py:88(logits)
              123674592 1615.165    0.000 1615.165    0.000 {built-in method rsub}
              126558197 1610.162    0.000 1610.162    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              123354192 1600.179    0.000 1600.179    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
               41011264  404.825    0.000 1592.615    0.000 categorical.py:108(sample)
               41011264   84.444    0.000 1564.278    0.000 utils.py:82(probs_to_logits)
                1281602   64.198    0.000 1545.296    0.001 layers.py:17(step)
               41011264  116.247    0.000 1476.262    0.000 layer.py:106(move)
               82022528  436.715    0.000 1394.466    0.000 functional.py:46(broadcast_tensors)
               82342928 1325.438    0.000 1325.438    0.000 {method 'max' of 'torch._C._TensorBase' objects}
                1281603  135.996    0.000 1268.070    0.001 layers.py:793(update)
               24728524  597.152    0.000 1253.908    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
              123033792 1211.719    0.000 1211.719    0.000 {method 'all' of 'torch._C._TensorBase' objects}
             6540794561 1132.945    0.000 1144.287    0.000 {built-in method builtins.len}
               14097622   39.657    0.000 1060.981    0.000 tensor.py:575(__iter__)
               14097622  990.663    0.000  990.663    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               41011264  144.324    0.000  964.093    0.000 utils.py:77(clamp_probs)
               41011264  181.776    0.000  952.104    0.000 utils.py:11(broadcast_all)
             6179912577  942.530    0.000  942.530    0.000 {method 'values' of 'collections.OrderedDict' objects}
               41011264  930.575    0.000  930.575    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               41011264  200.009    0.000  910.105    0.000 layers.py:844(check)
               41011264  819.769    0.000  819.769    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
               82022528  812.343    0.000  812.343    0.000 {built-in method broadcast_tensors}
              123994992  802.463    0.000  802.463    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
                1281602   78.603    0.000  769.181    0.001 replaybuffer.py:34(save_option_critic)
               41011264  768.827    0.000  768.827    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
              246708384  711.067    0.000  711.067    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               41011264  702.217    0.000  702.217    0.000 {built-in method clamp}
               17942422  672.818    0.000  672.818    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               82022528  669.021    0.000  669.021    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               24728524   40.669    0.000  656.756    0.000 <__array_function__ internals>:2(prod)
               41739105  652.758    0.000  652.758    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               24728524   37.875    0.000  607.683    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
               41011264  599.561    0.000  599.561    0.000 {built-in method bernoulli}
                 320400  450.840    0.001  584.512    0.002 replaybuffer.py:42(sample_option_critic)
               24728524   57.379    0.000  569.808    0.000 fromnumeric.py:2912(prod)
               41011264  539.129    0.000  539.129    0.000 {built-in method all}
               41011264  515.741    0.000  515.741    0.000 {built-in method log}
               41011264  514.760    0.000  514.760    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
               24728524  136.035    0.000  512.429    0.000 fromnumeric.py:70(_wrapreduction)
                 727877   11.872    0.000  471.479    0.001 layers.py:849(restart)
                1281602   77.090    0.000  410.587    0.000 optimizer.py:189(zero_grad)
                 727877    6.191    0.000  382.780    0.001 level.py:8(__init__)
               41011264  379.871    0.000  379.871    0.000 {built-in method multinomial}
               41011264   89.649    0.000  356.738    0.000 layers.py:838(isFree)
                8971221  212.880    0.000  345.439    0.000 layer.py:175(NoRock_update)
              126558211  335.393    0.000  335.393    0.000 {method 'to' of 'torch._C._TensorBase' objects}
                 727877   13.327    0.000  333.143    0.000 levels.py:456(generate)
              123764226  331.427    0.000  331.427    0.000 {method 'item' of 'torch._C._TensorBase' objects}


Traceback (most recent call last):
  File "main.py", line 268, in <module>
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
Subject: Job 9632749: <Attempt7_Maze_option_critic_0> in cluster <dcc> Exited

Job <Attempt7_Maze_option_critic_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed May 12 14:11:13 2021
Job was executed on host(s) <n-62-23-27>, in queue <hpc>, as user <s183914> in cluster <dcc> at Sun May 16 23:16:53 2021
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

Exited with exit code 1.

Resource usage summary:

    CPU time :                                   258891.89 sec.
    Max Memory :                                 944 MB
    Average Memory :                             931.20 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15440.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   259038 sec.
    Turnaround time :                            637270 sec.

The output (if any) is above this job summary.

