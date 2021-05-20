[W NNPACK.cpp:80] Could not initialize NNPACK! Reason: Unsupported hardware.

# Parameters

    Name :                      Attempt8_Coconuts_option_critic-2
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
    Num :                       2
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              4315 minutes.
    Hours used :                71 hours.

# Profiling


      30317179320 function calls (29380206602 primitive calls) in 258901.10 seconds

##    Ordered by: cumulative time
   List reduced from 438 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258901.104 258901.104 {built-in method builtins.exec}
                      1    0.436    0.436 258901.103 258901.103 <string>:1(<module>)
                      1 4531.835 4531.835 258900.667 258900.667 optionCritic.py:195(option_critic_run)
        1240105715/306547604 9448.381    0.000 124207.427    0.000 module.py:866(_call_impl)
               33613344 8622.576    0.000 119418.008    0.004 optionCritic.py:143(actor_loss_fn)
              103728679  857.280    0.000 116177.531    0.001 optionCritic.py:70(get_state)
              103728679 2610.098    0.000 112949.123    0.001 container.py:117(forward)
              207457358  856.405    0.000 75927.243    0.000 conv.py:398(forward)
              207457358  465.972    0.000 74725.061    0.000 conv.py:390(_conv_forward)
              207457358 74259.089    0.000 74259.089    0.000 {built-in method conv2d}
                1050417   10.126    0.000 68920.234    0.066 tensor.py:195(backward)
                1050417   11.410    0.000 68909.893    0.066 __init__.py:68(backward)
                1050417 68867.006    0.066 68867.006    0.066 {method 'run_backward' of 'torch._C._EngineBase' objects}
               33613344 3989.087    0.000 23237.592    0.001 optionCritic.py:91(get_action)
              410276283 1483.016    0.000 21357.202    0.000 linear.py:93(forward)
              410276283  541.496    0.000 19265.002    0.000 functional.py:1737(linear)
              410276283 18603.693    0.000 18603.693    0.000 {built-in method torch._C._nn.linear}
               33613344 1166.608    0.000 12984.471    0.000 optionCritic.py:80(predict_option_termination)
               67226688 1131.924    0.000 8386.885    0.000 distribution.py:34(__init__)
               33613344  637.949    0.000 7697.546    0.000 categorical.py:115(log_prob)
              311186037  432.507    0.000 7539.106    0.000 activation.py:713(forward)
              311186037  408.240    0.000 7106.599    0.000 functional.py:1364(leaky_relu)
              311186037 6609.846    0.000 6609.846    0.000 {built-in method torch._C._nn.leaky_relu}
               33613344  854.056    0.000 6607.201    0.000 categorical.py:49(__init__)
                 262604   65.497    0.000 6418.857    0.024 optionCritic.py:116(critic_loss_fn)
              101716289  418.773    0.000 5837.584    0.000 optionCritic.py:77(get_Q)
               33613344  331.952    0.000 4881.927    0.000 bernoulli.py:34(__init__)
               67489292  424.609    0.000 4808.749    0.000 optionCritic.py:88(get_terminations)
               33613344 2746.522    0.000 4126.004    0.000 constraints.py:398(check)
                1050417    8.577    0.000 3304.713    0.003 game.py:42(step)
                1050417   26.162    0.000 3267.859    0.003 optimizer.py:84(wrapper)
                1050417   12.649    0.000 3182.178    0.003 layers.py:827(step)
                1050417   15.104    0.000 3157.733    0.003 grad_mode.py:24(decorate_context)
                1050417   76.842    0.000 3116.424    0.003 rmsprop.py:56(step)
               33613344  482.579    0.000 3103.165    0.000 distribution.py:240(_validate_sample)
                1050417  121.938    0.000 2956.774    0.003 _functional.py:203(rmsprop)
              103728679  193.241    0.000 2307.154    0.000 activation.py:101(forward)
               33613344 1097.774    0.000 2182.384    0.000 categorical.py:123(entropy)
              103728679  171.438    0.000 2113.913    0.000 functional.py:1195(relu)
               33613344 2070.955    0.000 2070.955    0.000 constraints.py:249(check)
               33613344 2045.933    0.000 2045.933    0.000 constraints.py:364(check)
                1050417   59.001    0.000 1986.037    0.002 layers.py:17(step)
              100840032  238.520    0.000 1953.546    0.000 utils.py:106(__get__)
               33613344  157.034    0.000 1922.374    0.000 layer.py:106(move)
              103728679 1914.611    0.000 1914.611    0.000 {built-in method relu}
               33613344  349.935    0.000 1864.937    0.000 bernoulli.py:86(sample)
              235293408 1737.394    0.000 1737.394    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               24524624  817.695    0.000 1704.529    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
             1609378199 1632.699    0.000 1632.807    0.000 module.py:934(__getattr__)
              103728679  152.825    0.000 1624.869    0.000 flatten.py:39(forward)
             1251660302 1622.928    0.000 1622.928    0.000 {built-in method torch._C._get_tracing_state}
               14705832 1593.535    0.000 1593.535    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              101365240  177.422    0.000 1591.357    0.000 tensor.py:525(__rsub__)
               33613344   77.183    0.000 1537.411    0.000 categorical.py:88(logits)
               33613344  410.649    0.000 1483.187    0.000 categorical.py:108(sample)
              103728679 1472.044    0.000 1472.044    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               33613344   86.993    0.000 1460.228    0.000 utils.py:82(probs_to_logits)
              100840032 1449.776    0.000 1449.776    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
               67226688  459.623    0.000 1434.901    0.000 functional.py:46(broadcast_tensors)
              101102636 1405.619    0.000 1405.619    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
              101365240 1383.531    0.000 1383.531    0.000 {built-in method rsub}
               33613344  264.341    0.000 1296.871    0.000 layers.py:844(check)
               67489292 1240.214    0.000 1240.214    0.000 {method 'max' of 'torch._C._TensorBase' objects}
                1050418  133.654    0.000 1177.363    0.001 layers.py:793(update)
               11554587   38.249    0.000 1101.674    0.000 tensor.py:575(__iter__)
              100840032 1057.680    0.000 1057.680    0.000 {method 'all' of 'torch._C._TensorBase' objects}
               11554587 1034.488    0.000 1034.488    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               33613344  212.668    0.000 1031.443    0.000 utils.py:11(broadcast_all)
             5456472687  928.416    0.000  939.427    0.000 {built-in method builtins.len}
               33613344  926.885    0.000  926.885    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               24524624   53.651    0.000  886.834    0.000 <__array_function__ internals>:2(prod)
               33613344  156.885    0.000  877.289    0.000 utils.py:77(clamp_probs)
               67226688  859.271    0.000  859.271    0.000 {built-in method broadcast_tensors}
               24524624   50.988    0.000  823.715    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
               24524624   72.114    0.000  772.727    0.000 fromnumeric.py:2912(prod)
             5064151539  751.520    0.000  751.520    0.000 {method 'values' of 'collections.OrderedDict' objects}
               33613344  720.404    0.000  720.404    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
              101627844  717.281    0.000  717.281    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               24524624  166.422    0.000  700.612    0.000 fromnumeric.py:70(_wrapreduction)
                1050417   70.562    0.000  687.931    0.001 replaybuffer.py:34(save_option_critic)
               33613344  684.471    0.000  684.471    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
               33613344  630.669    0.000  630.669    0.000 {built-in method bernoulli}
                 262604  476.651    0.002  613.419    0.002 replaybuffer.py:42(sample_option_critic)
               33613344  605.885    0.000  605.885    0.000 {built-in method clamp}
              202205272  598.776    0.000  598.776    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               33964393  586.014    0.000  586.014    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               67226688  568.787    0.000  568.787    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               33613344  495.947    0.000  495.947    0.000 {built-in method log}
               33613344  472.590    0.000  472.590    0.000 {built-in method all}
               24524624  466.692    0.000  466.692    0.000 {method 'reduce' of 'numpy.ufunc' objects}
               33613344  464.117    0.000  464.117    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
               10504180  278.090    0.000  437.765    0.000 layer.py:159(update)
               14705832  431.287    0.000  431.287    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               33613344   73.832    0.000  382.309    0.000 layers.py:838(isFree)
               33613344  379.704    0.000  379.704    0.000 {built-in method multinomial}
              103728693  376.809    0.000  376.809    0.000 {method 'to' of 'torch._C._TensorBase' objects}
                1050417   66.941    0.000  373.139    0.000 optimizer.py:189(zero_grad)
              443793980  222.807    0.000  346.410    0.000 {built-in method builtins.isinstance}
                7090318  313.137    0.000  313.137    0.000 {built-in method tensor}
              101193212  312.995    0.000  312.995    0.000 {method 'item' of 'torch._C._TensorBase' objects}


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
Subject: Job 9632941: <Attempt8_Coconuts_option_critic_2> in cluster <dcc> Exited

Job <Attempt8_Coconuts_option_critic_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed May 12 15:36:18 2021
Job was executed on host(s) <n-62-23-21>, in queue <hpc>, as user <s183914> in cluster <dcc> at Sun May 16 23:16:53 2021
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

    CPU time :                                   258895.09 sec.
    Max Memory :                                 868 MB
    Average Memory :                             859.48 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15516.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258978 sec.
    Turnaround time :                            632165 sec.

The output (if any) is above this job summary.

