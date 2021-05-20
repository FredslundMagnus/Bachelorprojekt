[W NNPACK.cpp:80] Could not initialize NNPACK! Reason: Unsupported hardware.

# Parameters

    Name :                      Attempt7_DoorsAndKey_option_critic-2
    Main :                      option_critic_run
    Level :                     Levels.Causal1
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


      40509426412 function calls (39285387646 primitive calls) in 258901.02 seconds

##    Ordered by: cumulative time
   List reduced from 428 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258901.024 258901.024 {built-in method builtins.exec}
                      1    0.302    0.302 258901.024 258901.024 <string>:1(<module>)
                      1 4023.063 4023.063 258900.721 258900.721 optionCritic.py:195(option_critic_run)
        1620986258/401407949 10579.386    0.000 113565.204    0.000 module.py:866(_call_impl)
               43911680 9434.904    0.000 112662.201    0.003 optionCritic.py:143(actor_loss_fn)
              135508701  803.661    0.000 103728.561    0.001 optionCritic.py:70(get_state)
              135508701 2923.315    0.000 100441.489    0.001 container.py:117(forward)
                1372240    9.289    0.000 69126.961    0.050 tensor.py:195(backward)
                1372240   10.822    0.000 69117.420    0.050 __init__.py:68(backward)
                1372240 69075.593    0.050 69075.593    0.050 {method 'run_backward' of 'torch._C._EngineBase' objects}
              271017402  963.101    0.000 61188.661    0.000 conv.py:398(forward)
              271017402  441.974    0.000 59886.002    0.000 conv.py:390(_conv_forward)
              271017402 59444.028    0.000 59444.028    0.000 {built-in method conv2d}
               43911680 4162.691    0.000 24752.016    0.001 optionCritic.py:91(get_action)
              536916650 1744.667    0.000 22189.433    0.000 linear.py:93(forward)
              536916650  617.246    0.000 19807.529    0.000 functional.py:1737(linear)
              536916650 19059.261    0.000 19059.261    0.000 {built-in method torch._C._nn.linear}
               43911680 1258.571    0.000 13321.531    0.000 optionCritic.py:80(predict_option_termination)
                1372240   23.617    0.000 12132.872    0.009 optimizer.py:84(wrapper)
                1372240   11.388    0.000 12040.900    0.009 grad_mode.py:24(decorate_context)
                1372240   84.326    0.000 12007.726    0.009 rmsprop.py:56(step)
                1372240  131.754    0.000 11828.414    0.009 _functional.py:203(rmsprop)
               19211354 9883.967    0.001 9883.967    0.001 {method 'sqrt' of 'torch._C._TensorBase' objects}
               87823360 1121.892    0.000 8918.995    0.000 distribution.py:34(__init__)
              406526103  443.983    0.000 8513.861    0.000 activation.py:713(forward)
               43911680  639.323    0.000 8104.210    0.000 categorical.py:115(log_prob)
              406526103  456.156    0.000 8069.878    0.000 functional.py:1364(leaky_relu)
              406526103 7515.637    0.000 7515.637    0.000 {built-in method torch._C._nn.leaky_relu}
               43911680  940.014    0.000 7299.298    0.000 categorical.py:49(__init__)
              133821148  498.241    0.000 6865.313    0.000 optionCritic.py:77(get_Q)
               88166420  489.834    0.000 5521.311    0.000 optionCritic.py:88(get_terminations)
                 343060   69.083    0.000 5286.692    0.015 optionCritic.py:116(critic_loss_fn)
               43911680  259.483    0.000 4571.770    0.000 bernoulli.py:34(__init__)
               43911680 3023.987    0.000 4562.938    0.000 constraints.py:398(check)
                1372240    7.467    0.000 3743.001    0.003 game.py:42(step)
                1372240   11.924    0.000 3644.093    0.003 layers.py:827(step)
               43911680  501.720    0.000 3408.332    0.000 distribution.py:240(_validate_sample)
              135508701  181.818    0.000 2446.618    0.000 activation.py:101(forward)
               43911680 1161.210    0.000 2397.449    0.000 categorical.py:123(entropy)
               43911680 2303.581    0.000 2303.581    0.000 constraints.py:249(check)
              135508701  157.935    0.000 2264.800    0.000 functional.py:1195(relu)
               43911680 2123.936    0.000 2123.936    0.000 constraints.py:364(check)
              135508701 2075.144    0.000 2075.144    0.000 {built-in method relu}
              131735040  241.429    0.000 2006.433    0.000 utils.py:106(__get__)
             1636080898 1956.821    0.000 1956.821    0.000 {built-in method torch._C._get_tracing_state}
                1372241  142.173    0.000 1956.683    0.001 layers.py:793(update)
              307381760 1914.793    0.000 1914.793    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              132421160  185.848    0.000 1746.066    0.000 tensor.py:525(__rsub__)
              131735040 1697.714    0.000 1697.714    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
               43911680  290.771    0.000 1693.575    0.000 bernoulli.py:86(sample)
              135508701  120.444    0.000 1681.120    0.000 flatten.py:39(forward)
             2105277872 1673.097    0.000 1673.221    0.000 module.py:934(__getattr__)
                1372240   64.640    0.000 1669.465    0.001 layers.py:17(step)
               43911680  116.969    0.000 1599.344    0.000 layer.py:106(move)
               43911680   78.641    0.000 1593.334    0.000 categorical.py:88(logits)
              135508701 1560.676    0.000 1560.676    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              132078100 1558.397    0.000 1558.397    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
               43911680  396.300    0.000 1539.269    0.000 categorical.py:108(sample)
              132421160 1525.848    0.000 1525.848    0.000 {built-in method rsub}
               43911680   84.128    0.000 1514.693    0.000 utils.py:82(probs_to_logits)
               87823360  401.632    0.000 1269.766    0.000 functional.py:46(broadcast_tensors)
               88166420 1256.106    0.000 1256.106    0.000 {method 'max' of 'torch._C._TensorBase' objects}
              131735040 1153.953    0.000 1153.953    0.000 {method 'all' of 'torch._C._TensorBase' objects}
             7054548078 1096.516    0.000 1106.836    0.000 {built-in method builtins.len}
               43911680  228.319    0.000 1098.465    0.000 layers.py:844(check)
                1400022   23.148    0.000 1014.003    0.001 layers.py:849(restart)
               21777950  468.525    0.000  992.257    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               19211354  949.955    0.000  949.955    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               43911680  139.304    0.000  933.234    0.000 utils.py:77(clamp_probs)
               15094640   35.830    0.000  929.858    0.000 tensor.py:575(__iter__)
             6619453733  929.759    0.000  929.759    0.000 {method 'values' of 'collections.OrderedDict' objects}
               43911680  894.100    0.000  894.100    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               15094640  865.250    0.000  865.250    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
                1400022    9.740    0.000  847.917    0.001 level.py:8(__init__)
               43911680  154.512    0.000  826.787    0.000 utils.py:11(broadcast_all)
               43911680  793.930    0.000  793.930    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
              132764220  772.001    0.000  772.001    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               87823360  761.678    0.000  761.678    0.000 {built-in method broadcast_tensors}
                1400022   28.773    0.000  759.335    0.001 levels.py:303(generate)
                1372240   74.084    0.000  735.336    0.001 replaybuffer.py:34(save_option_critic)
               43911680  731.195    0.000  731.195    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
                8399030  108.513    0.000  701.534    0.000 level.py:41(notUsed)
              264156200  683.779    0.000  683.779    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               43911680  679.659    0.000  679.659    0.000 {built-in method clamp}
               87823360  639.924    0.000  639.924    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               45311668  623.459    0.000  623.459    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                 343060  435.223    0.001  566.684    0.002 replaybuffer.py:42(sample_option_critic)
               43911680  553.066    0.000  553.066    0.000 {built-in method bernoulli}
               21777950   32.429    0.000  523.732    0.000 <__array_function__ internals>:2(prod)
               43911680  518.227    0.000  518.227    0.000 {built-in method all}
               43911680  497.708    0.000  497.708    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
               43911680  497.331    0.000  497.331    0.000 {built-in method log}
               21777950   29.320    0.000  484.615    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
               21777950   45.545    0.000  455.295    0.000 fromnumeric.py:2912(prod)
               21777950  105.180    0.000  409.750    0.000 fromnumeric.py:70(_wrapreduction)
                1372240   73.713    0.000  402.626    0.000 optimizer.py:189(zero_grad)
               10977928  247.279    0.000  401.098    0.000 layer.py:175(NoRock_update)
               43911680  366.445    0.000  366.445    0.000 {built-in method multinomial}
             1132485797  251.835    0.000  361.913    0.000 enum.py:646(__hash__)
                8399030    9.809    0.000  339.219    0.000 level.py:38(elementsIn)


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
Subject: Job 9632760: <Attempt7_DoorsAndKey_option_critic_2> in cluster <dcc> Exited

Job <Attempt7_DoorsAndKey_option_critic_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed May 12 14:11:15 2021
Job was executed on host(s) <n-62-23-25>, in queue <hpc>, as user <s183914> in cluster <dcc> at Sun May 16 23:16:53 2021
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

    CPU time :                                   258896.05 sec.
    Max Memory :                                 788 MB
    Average Memory :                             774.02 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15596.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   259038 sec.
    Turnaround time :                            637268 sec.

The output (if any) is above this job summary.

