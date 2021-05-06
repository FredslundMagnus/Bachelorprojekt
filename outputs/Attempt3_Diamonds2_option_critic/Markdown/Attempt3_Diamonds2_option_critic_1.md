[W NNPACK.cpp:80] Could not initialize NNPACK! Reason: Unsupported hardware.

# Parameters

    Name :                      Attempt3_Diamonds2_option_critic-1
    Main :                      option_critic_run
    Level :                     Levels.Causal5
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


      32342138775 function calls (31343684216 primitive calls) in 258901.00 seconds

##    Ordered by: cumulative time
   List reduced from 429 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258901.001 258901.001 {built-in method builtins.exec}
                      1    0.359    0.359 258901.001 258901.001 <string>:1(<module>)
                      1 3343.238 3343.238 258900.642 258900.642 optionCritic.py:195(option_critic_run)
        1325442394/327081592 9299.004    0.000 114489.662    0.000 module.py:866(_call_impl)
               35876125 9115.687    0.000 112130.709    0.003 optionCritic.py:143(actor_loss_fn)
              110928978  704.852    0.000 106018.316    0.001 optionCritic.py:70(get_state)
              110928978 2539.711    0.000 103159.461    0.001 container.py:117(forward)
              221857956  826.360    0.000 68431.733    0.000 conv.py:398(forward)
              221857956  365.241    0.000 67293.810    0.000 conv.py:390(_conv_forward)
              221857956 66928.569    0.000 66928.569    0.000 {built-in method conv2d}
                1435045   10.208    0.000 64211.683    0.045 tensor.py:195(backward)
                1435045   12.255    0.000 64201.204    0.045 __init__.py:68(backward)
                1435045 64154.359    0.045 64154.359    0.045 {method 'run_backward' of 'torch._C._EngineBase' objects}
                1435045   29.372    0.000 25036.028    0.017 optimizer.py:84(wrapper)
                1435045   14.284    0.000 24916.354    0.017 grad_mode.py:24(decorate_context)
                1435045   95.220    0.000 24873.555    0.017 rmsprop.py:56(step)
                1435045  145.194    0.000 24668.033    0.017 _functional.py:203(rmsprop)
               20090612 21813.611    0.001 21813.611    0.001 {method 'sqrt' of 'torch._C._TensorBase' objects}
               35876125 3486.646    0.000 21021.272    0.001 optionCritic.py:91(get_action)
              438010570 1490.104    0.000 19635.784    0.000 linear.py:93(forward)
              438010570  562.351    0.000 17572.556    0.000 functional.py:1737(linear)
              438010570 16893.645    0.000 16893.645    0.000 {built-in method torch._C._nn.linear}
               35876125 1085.733    0.000 11838.213    0.000 optionCritic.py:80(predict_option_termination)
               71752250  990.518    0.000 7698.931    0.000 distribution.py:34(__init__)
              332786934  404.429    0.000 7420.870    0.000 activation.py:713(forward)
              332786934  412.478    0.000 7016.441    0.000 functional.py:1364(leaky_relu)
               35876125  562.209    0.000 6901.142    0.000 categorical.py:115(log_prob)
              332786934 6521.323    0.000 6521.323    0.000 {built-in method torch._C._nn.leaky_relu}
               35876125  812.451    0.000 6206.484    0.000 categorical.py:49(__init__)
              108380735  425.926    0.000 5886.132    0.000 optionCritic.py:77(get_Q)
               71895754  420.958    0.000 4795.443    0.000 optionCritic.py:88(get_terminations)
               35876125  249.635    0.000 4150.282    0.000 bernoulli.py:34(__init__)
               35876125 2543.144    0.000 3865.181    0.000 constraints.py:398(check)
                 143504   31.251    0.000 3298.131    0.023 optionCritic.py:116(critic_loss_fn)
                1435045    8.742    0.000 2963.179    0.002 game.py:42(step)
               35876125  433.336    0.000 2870.738    0.000 distribution.py:240(_validate_sample)
                1435045   14.092    0.000 2856.215    0.002 layers.py:827(step)
              110928978  149.757    0.000 2093.780    0.000 activation.py:101(forward)
               35876125  993.193    0.000 2053.421    0.000 categorical.py:123(entropy)
              110928978  131.693    0.000 1944.023    0.000 functional.py:1195(relu)
               35876125 1917.426    0.000 1917.426    0.000 constraints.py:249(check)
               35876125 1860.787    0.000 1860.787    0.000 constraints.py:364(check)
              110928978 1787.388    0.000 1787.388    0.000 {built-in method relu}
             1341227889 1764.851    0.000 1764.851    0.000 {built-in method torch._C._get_tracing_state}
              107628375  188.959    0.000 1705.785    0.000 utils.py:106(__get__)
               20090612 1698.389    0.000 1698.389    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              251132875 1661.697    0.000 1661.697    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                1435045   57.990    0.000 1598.983    0.001 layers.py:17(step)
               35876125  275.219    0.000 1590.939    0.000 bernoulli.py:86(sample)
               35876125  101.876    0.000 1536.694    0.000 layer.py:106(move)
              107915383  160.012    0.000 1528.527    0.000 tensor.py:525(__rsub__)
             1718574685 1499.435    0.000 1499.437    0.000 module.py:934(__getattr__)
              107628375 1464.439    0.000 1464.439    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
              110928978  107.693    0.000 1458.608    0.000 flatten.py:39(forward)
               35876125   65.981    0.000 1368.905    0.000 categorical.py:88(logits)
              110928978 1350.914    0.000 1350.914    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              107771879 1346.816    0.000 1346.816    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
              107915383 1338.499    0.000 1338.499    0.000 {built-in method rsub}
               35876125  340.817    0.000 1318.214    0.000 categorical.py:108(sample)
               35876125   68.820    0.000 1302.924    0.000 utils.py:82(probs_to_logits)
                1435046  147.358    0.000 1237.331    0.001 layers.py:793(update)
               71752250  356.812    0.000 1145.702    0.000 functional.py:46(broadcast_tensors)
               71895754 1122.003    0.000 1122.003    0.000 {method 'max' of 'torch._C._TensorBase' objects}
               35876125  212.806    0.000 1025.981    0.000 layers.py:844(check)
              107628375 1012.613    0.000 1012.613    0.000 {method 'all' of 'torch._C._TensorBase' objects}
             5809185740  961.198    0.000  971.823    0.000 {built-in method builtins.len}
               15785495   40.575    0.000  956.957    0.000 tensor.py:575(__iter__)
               15785495  883.783    0.000  883.783    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
             5412698554  831.180    0.000  831.180    0.000 {method 'values' of 'collections.OrderedDict' objects}
               35876125  122.921    0.000  803.315    0.000 utils.py:77(clamp_probs)
               35876125  150.035    0.000  798.184    0.000 utils.py:11(broadcast_all)
               35876125  751.927    0.000  751.927    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               71752250  691.203    0.000  691.203    0.000 {built-in method broadcast_tensors}
                1435045   72.220    0.000  680.547    0.000 replaybuffer.py:34(save_option_critic)
               35876125  680.395    0.000  680.395    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
              108058887  660.655    0.000  660.655    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               35876125  640.351    0.000  640.351    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
              215543758  606.718    0.000  606.718    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               35876125  578.652    0.000  578.652    0.000 {built-in method clamp}
               71752250  546.623    0.000  546.623    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               36341477  536.224    0.000  536.224    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               35876125  525.444    0.000  525.444    0.000 {built-in method bernoulli}
                1435045   89.206    0.000  457.242    0.000 optimizer.py:189(zero_grad)
               35876125  440.612    0.000  440.612    0.000 {built-in method all}
               35876125  430.788    0.000  430.788    0.000 {built-in method log}
               35876125  421.504    0.000  421.504    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
               12915414  235.459    0.000  379.672    0.000 layer.py:175(NoRock_update)
                 465377    8.587    0.000  366.708    0.001 layers.py:849(restart)
               20090612  361.279    0.000  361.279    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               20090612  350.951    0.000  350.951    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               35876125   80.266    0.000  327.752    0.000 layers.py:838(isFree)
               35876125  313.870    0.000  313.870    0.000 {built-in method multinomial}
                 465377    3.756    0.000  306.872    0.001 level.py:8(__init__)
               20090612  298.610    0.000  298.610    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              110928992  290.641    0.000  290.641    0.000 {method 'to' of 'torch._C._TensorBase' objects}
              108096621  283.890    0.000  283.890    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                 465377   10.790    0.000  275.387    0.001 levels.py:249(generate)
                9040786  272.535    0.000  272.535    0.000 {built-in method tensor}
               35876125  271.941    0.000  271.941    0.000 {method 'expand' of 'torch._C._TensorBase' objects}
              472436780  179.790    0.000  265.241    0.000 {built-in method builtins.isinstance}


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
Subject: Job 9607847: <Attempt3_Diamonds2_option_critic_1> in cluster <dcc> Exited

Job <Attempt3_Diamonds2_option_critic_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon May  3 13:31:23 2021
Job was executed on host(s) <n-62-23-24>, in queue <hpc>, as user <s183914> in cluster <dcc> at Mon May  3 13:31:24 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon May  3 13:31:24 2021
Terminated at Thu May  6 13:26:32 2021
Results reported at Thu May  6 13:26:32 2021

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

    CPU time :                                   257797.50 sec.
    Max Memory :                                 1029 MB
    Average Memory :                             1001.85 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15355.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258939 sec.
    Turnaround time :                            258909 sec.

The output (if any) is above this job summary.

