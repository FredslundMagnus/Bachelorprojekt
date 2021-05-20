[W NNPACK.cpp:80] Could not initialize NNPACK! Reason: Unsupported hardware.

# Parameters

    Name :                      Attempt8_Diamonds1_option_critic-0
    Main :                      option_critic_run
    Level :                     Levels.Causal2
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


      35446769454 function calls (34353964661 primitive calls) in 258900.95 seconds

##    Ordered by: cumulative time
   List reduced from 427 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.952 258900.952 {built-in method builtins.exec}
                      1    0.344    0.344 258900.952 258900.952 <string>:1(<module>)
                      1 4028.186 4028.186 258900.607 258900.607 optionCritic.py:195(option_critic_run)
        1447497692/358674956 10405.921    0.000 108745.240    0.000 module.py:866(_call_impl)
               39203744 9212.063    0.000 108215.030    0.003 optionCritic.py:143(actor_loss_fn)
              120980304  778.824    0.000 99038.748    0.001 optionCritic.py:70(get_state)
              120980304 2783.653    0.000 95886.233    0.001 container.py:117(forward)
                1225117   10.003    0.000 67604.744    0.055 tensor.py:195(backward)
                1225117   10.865    0.000 67594.511    0.055 __init__.py:68(backward)
                1225117 67552.777    0.055 67552.777    0.055 {method 'run_backward' of 'torch._C._EngineBase' objects}
              241960608  938.138    0.000 57261.822    0.000 conv.py:398(forward)
              241960608  431.949    0.000 55992.563    0.000 conv.py:390(_conv_forward)
              241960608 55560.614    0.000 55560.614    0.000 {built-in method conv2d}
               39203744 4023.944    0.000 24026.811    0.001 optionCritic.py:91(get_action)
              479655260 1695.584    0.000 21979.499    0.000 linear.py:93(forward)
                1225117   27.290    0.000 20707.244    0.017 optimizer.py:84(wrapper)
                1225117   15.464    0.000 20599.534    0.017 grad_mode.py:24(decorate_context)
                1225117   82.153    0.000 20557.421    0.017 rmsprop.py:56(step)
                1225117  136.364    0.000 20381.880    0.017 _functional.py:203(rmsprop)
              479655260  629.766    0.000 19661.494    0.000 functional.py:1737(linear)
              479655260 18914.167    0.000 18914.167    0.000 {built-in method torch._C._nn.linear}
               17151632 17943.143    0.001 17943.143    0.001 {method 'sqrt' of 'torch._C._TensorBase' objects}
               39203744 1227.367    0.000 13177.669    0.000 optionCritic.py:80(predict_option_termination)
               78407488 1123.291    0.000 8708.078    0.000 distribution.py:34(__init__)
              362940912  438.544    0.000 8311.794    0.000 activation.py:713(forward)
               39203744  649.000    0.000 7885.549    0.000 categorical.py:115(log_prob)
              362940912  456.678    0.000 7873.249    0.000 functional.py:1364(leaky_relu)
              362940912 7321.685    0.000 7321.685    0.000 {built-in method torch._C._nn.leaky_relu}
               39203744  910.254    0.000 7065.996    0.000 categorical.py:49(__init__)
              119777141  488.583    0.000 6730.652    0.000 optionCritic.py:77(get_Q)
               78713767  472.068    0.000 5395.698    0.000 optionCritic.py:88(get_terminations)
                 306279   68.497    0.000 4924.585    0.016 optionCritic.py:116(critic_loss_fn)
               39203744  276.958    0.000 4567.795    0.000 bernoulli.py:34(__init__)
               39203744 2919.530    0.000 4402.512    0.000 constraints.py:398(check)
                1225117    7.809    0.000 3341.022    0.003 game.py:42(step)
               39203744  487.424    0.000 3310.048    0.000 distribution.py:240(_validate_sample)
                1225117   12.110    0.000 3244.420    0.003 layers.py:827(step)
              120980304  168.225    0.000 2385.594    0.000 activation.py:101(forward)
               39203744 1139.742    0.000 2334.081    0.000 categorical.py:123(entropy)
               39203744 2233.780    0.000 2233.780    0.000 constraints.py:249(check)
              120980304  153.213    0.000 2217.369    0.000 functional.py:1195(relu)
               39203744 2077.406    0.000 2077.406    0.000 constraints.py:364(check)
              120980304 2036.103    0.000 2036.103    0.000 {built-in method relu}
             1460973979 1951.172    0.000 1951.172    0.000 {built-in method torch._C._get_tracing_state}
              117611232  214.928    0.000 1930.977    0.000 utils.py:106(__get__)
                1225118  141.893    0.000 1872.644    0.002 layers.py:793(update)
              274426208 1858.678    0.000 1858.678    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              118223790  186.060    0.000 1712.465    0.000 tensor.py:525(__rsub__)
               39203744  301.535    0.000 1700.145    0.000 bernoulli.py:86(sample)
              117611232 1644.270    0.000 1644.270    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
              120980304  120.256    0.000 1631.058    0.000 flatten.py:39(forward)
             1880473503 1621.721    0.000 1621.843    0.000 module.py:934(__getattr__)
               39203744   75.253    0.000 1552.075    0.000 categorical.py:88(logits)
              120980304 1510.802    0.000 1510.802    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              117917511 1508.653    0.000 1508.653    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
               39203744  382.685    0.000 1500.448    0.000 categorical.py:108(sample)
              118223790 1494.076    0.000 1494.076    0.000 {built-in method rsub}
               39203744   81.266    0.000 1476.822    0.000 utils.py:82(probs_to_logits)
               17151632 1419.099    0.000 1419.099    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                1225117   61.989    0.000 1353.281    0.001 layers.py:17(step)
               39203744  108.900    0.000 1286.731    0.000 layer.py:106(move)
               78407488  398.688    0.000 1259.469    0.000 functional.py:46(broadcast_tensors)
               78713767 1222.382    0.000 1222.382    0.000 {method 'max' of 'torch._C._TensorBase' objects}
              117611232 1141.514    0.000 1141.514    0.000 {method 'all' of 'torch._C._TensorBase' objects}
             6258571012 1041.662    0.000 1053.321    0.000 {built-in method builtins.len}
               13476287   38.354    0.000  996.509    0.000 tensor.py:575(__iter__)
                1553387   25.978    0.000  993.195    0.001 layers.py:849(restart)
             5910971072  931.118    0.000  931.118    0.000 {method 'values' of 'collections.OrderedDict' objects}
               13476287  928.744    0.000  928.744    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               39203744  137.848    0.000  914.256    0.000 utils.py:77(clamp_probs)
               39203744  200.405    0.000  872.761    0.000 layers.py:844(check)
               39203744  868.058    0.000  868.058    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               39203744  159.037    0.000  846.299    0.000 utils.py:11(broadcast_all)
                1553387   11.690    0.000  807.263    0.001 level.py:8(__init__)
               39203744  776.408    0.000  776.408    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
               78407488  756.381    0.000  756.381    0.000 {built-in method broadcast_tensors}
              118530069  751.925    0.000  751.925    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
                1225117   72.850    0.000  726.691    0.001 replaybuffer.py:34(save_option_critic)
               39203744  717.851    0.000  717.851    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
                1553387   28.836    0.000  703.467    0.000 levels.py:151(generate)
              235835022  671.834    0.000  671.834    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               39203744  655.229    0.000  655.229    0.000 {built-in method clamp}
                7455368  105.428    0.000  646.559    0.000 level.py:41(notUsed)
               78407488  626.948    0.000  626.948    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               40757095  623.600    0.000  623.600    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               39203744  550.143    0.000  550.143    0.000 {built-in method bernoulli}
                 306279  422.516    0.001  549.967    0.002 replaybuffer.py:42(sample_option_critic)
               39203744  501.896    0.000  501.896    0.000 {built-in method all}
               39203744  481.299    0.000  481.299    0.000 {built-in method log}
               39203744  476.620    0.000  476.620    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
                8240107  207.569    0.000  435.169    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                1225117   74.827    0.000  392.392    0.000 optimizer.py:189(zero_grad)
                8575826  230.353    0.000  364.485    0.000 layer.py:175(NoRock_update)
               39203744  357.766    0.000  357.766    0.000 {built-in method multinomial}
              119167064  320.724    0.000  320.724    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               17151632  315.765    0.000  315.765    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                7455368    9.491    0.000  312.569    0.000 level.py:38(elementsIn)
              911525652  219.660    0.000  312.230    0.000 enum.py:646(__hash__)
               39203744  310.010    0.000  310.010    0.000 {method 'expand' of 'torch._C._TensorBase' objects}
              120980318  308.041    0.000  308.041    0.000 {method 'to' of 'torch._C._TensorBase' objects}


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
Subject: Job 9632924: <Attempt8_Diamonds1_option_critic_0> in cluster <dcc> Exited

Job <Attempt8_Diamonds1_option_critic_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed May 12 15:36:14 2021
Job was executed on host(s) <n-62-23-24>, in queue <hpc>, as user <s183914> in cluster <dcc> at Sun May 16 23:16:53 2021
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

    CPU time :                                   258887.83 sec.
    Max Memory :                                 867 MB
    Average Memory :                             856.15 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15517.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   259038 sec.
    Turnaround time :                            632169 sec.

The output (if any) is above this job summary.

