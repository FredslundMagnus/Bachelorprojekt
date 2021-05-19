[W NNPACK.cpp:80] Could not initialize NNPACK! Reason: Unsupported hardware.
Traceback (most recent call last):
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils/debug.py", line 71, in __init__
    cProfile.run(
  File "/appl/python/3.8.4/lib/python3.8/cProfile.py", line 16, in run
    return _pyprofile._Utils(Profile).run(statement, filename, sort)
  File "/appl/python/3.8.4/lib/python3.8/profile.py", line 57, in run
    self._show(prof, filename, sort)
  File "/appl/python/3.8.4/lib/python3.8/profile.py", line 70, in _show
    prof.dump_stats(filename)
  File "/appl/python/3.8.4/lib/python3.8/cProfile.py", line 48, in dump_stats
    marshal.dump(self.stats, f)
OSError: [Errno 116] Stale file handle


# Parameters

    Name :                      Attempt7_Diamonds1_option_critic-2
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
    Num :                       2
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              4315 minutes.
    Hours used :                71 hours.

# Profiling


      35474833504 function calls (34338717498 primitive calls) in 258901.15 seconds

##    Ordered by: cumulative time
   List reduced from 430 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258901.145 258901.145 {built-in method builtins.exec}
                      1    0.382    0.382 258901.145 258901.145 <string>:1(<module>)
                      1 4412.341 4412.341 258900.763 258900.763 optionCritic.py:195(option_critic_run)
        1503707327/371731328 10863.877    0.000 115944.302    0.000 module.py:866(_call_impl)
               40757504 9790.478    0.000 115664.500    0.003 optionCritic.py:143(actor_loss_fn)
              125775111  822.185    0.000 105785.845    0.001 optionCritic.py:70(get_state)
              125775111 3032.367    0.000 102441.555    0.001 container.py:117(forward)
                1273672   10.034    0.000 71854.289    0.056 tensor.py:195(backward)
                1273672   12.097    0.000 71844.018    0.056 __init__.py:68(backward)
                1273672 71799.191    0.056 71799.191    0.056 {method 'run_backward' of 'torch._C._EngineBase' objects}
              251550222  986.220    0.000 60974.625    0.000 conv.py:398(forward)
              251550222  423.339    0.000 59629.528    0.000 conv.py:390(_conv_forward)
              251550222 59206.189    0.000 59206.189    0.000 {built-in method conv2d}
               40757504 4396.335    0.000 25717.290    0.001 optionCritic.py:91(get_action)
              497506439 1766.720    0.000 23726.092    0.000 linear.py:93(forward)
              497506439  624.156    0.000 21281.866    0.000 functional.py:1737(linear)
              497506439 20521.666    0.000 20521.666    0.000 {built-in method torch._C._nn.linear}
               40757504 1319.241    0.000 14291.335    0.000 optionCritic.py:80(predict_option_termination)
               81515008 1218.819    0.000 9326.174    0.000 distribution.py:34(__init__)
              377325333  481.384    0.000 8891.140    0.000 activation.py:713(forward)
              377325333  480.600    0.000 8409.756    0.000 functional.py:1364(leaky_relu)
               40757504  678.047    0.000 8394.055    0.000 categorical.py:115(log_prob)
              377325333 7827.943    0.000 7827.943    0.000 {built-in method torch._C._nn.leaky_relu}
               40757504  976.862    0.000 7521.756    0.000 categorical.py:49(__init__)
              123365287  515.510    0.000 7050.727    0.000 optionCritic.py:77(get_Q)
               81833426  505.237    0.000 5741.708    0.000 optionCritic.py:88(get_terminations)
                 318418   74.029    0.000 5234.918    0.016 optionCritic.py:116(critic_loss_fn)
               40757504  314.419    0.000 5071.245    0.000 bernoulli.py:34(__init__)
               40757504 3103.491    0.000 4687.413    0.000 constraints.py:398(check)
                1273672   26.458    0.000 4420.313    0.003 optimizer.py:84(wrapper)
                1273672   12.875    0.000 4312.748    0.003 grad_mode.py:24(decorate_context)
                1273672   87.516    0.000 4272.925    0.003 rmsprop.py:56(step)
                1273672  134.746    0.000 4083.447    0.003 _functional.py:203(rmsprop)
               40757504  525.184    0.000 3491.514    0.000 distribution.py:240(_validate_sample)
                1273672    7.870    0.000 2777.743    0.002 game.py:42(step)
                1273672   11.603    0.000 2675.204    0.002 layers.py:827(step)
              125775111  178.950    0.000 2566.390    0.000 activation.py:101(forward)
               17831402 2512.336    0.000 2512.336    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               40757504 1211.862    0.000 2488.170    0.000 categorical.py:123(entropy)
              125775111  173.208    0.000 2387.439    0.000 functional.py:1195(relu)
               40757504 2353.102    0.000 2353.102    0.000 constraints.py:249(check)
               40757504 2239.146    0.000 2239.146    0.000 constraints.py:364(check)
              125775111 2182.956    0.000 2182.956    0.000 {built-in method relu}
              122272512  227.036    0.000 2080.645    0.000 utils.py:106(__get__)
              285302528 2002.989    0.000 2002.989    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
             1517717719 1999.582    0.000 1999.582    0.000 {built-in method torch._C._get_tracing_state}
               40757504  344.844    0.000 1885.057    0.000 bernoulli.py:86(sample)
              122909348  199.489    0.000 1841.240    0.000 tensor.py:525(__rsub__)
              122272512 1761.955    0.000 1761.955    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
             1951525299 1761.511    0.000 1761.638    0.000 module.py:934(__getattr__)
              125775111  126.327    0.000 1737.609    0.000 flatten.py:39(forward)
               40757504   83.968    0.000 1675.089    0.000 categorical.py:88(logits)
              122590930 1636.896    0.000 1636.896    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
              125775111 1611.282    0.000 1611.282    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              122909348 1607.603    0.000 1607.603    0.000 {built-in method rsub}
               40757504  417.829    0.000 1607.139    0.000 categorical.py:108(sample)
               40757504   92.294    0.000 1591.121    0.000 utils.py:82(probs_to_logits)
                1273672   65.189    0.000 1526.610    0.001 layers.py:17(step)
               40757504  114.211    0.000 1456.676    0.000 layer.py:106(move)
               81515008  456.199    0.000 1405.216    0.000 functional.py:46(broadcast_tensors)
               26054561  643.318    0.000 1362.423    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               81833426 1315.463    0.000 1315.463    0.000 {method 'max' of 'torch._C._TensorBase' objects}
              122272512 1197.529    0.000 1197.529    0.000 {method 'all' of 'torch._C._TensorBase' objects}
                1273673  137.568    0.000 1130.698    0.001 layers.py:793(update)
             6498221565 1118.821    0.000 1130.086    0.000 {built-in method builtins.len}
               14010392   41.218    0.000 1084.404    0.000 tensor.py:575(__iter__)
               14010392 1012.492    0.000 1012.492    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               40757504  194.413    0.000  988.438    0.000 utils.py:11(broadcast_all)
               40757504  145.715    0.000  970.511    0.000 utils.py:77(clamp_probs)
             6140604419  963.844    0.000  963.844    0.000 {method 'values' of 'collections.OrderedDict' objects}
               40757504  941.223    0.000  941.223    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               40757504  191.500    0.000  888.711    0.000 layers.py:844(check)
               81515008  831.586    0.000  831.586    0.000 {built-in method broadcast_tensors}
               40757504  824.796    0.000  824.796    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
              123227766  806.658    0.000  806.658    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
                1273672   79.689    0.000  777.620    0.001 replaybuffer.py:34(save_option_critic)
               40757504  764.406    0.000  764.406    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
               26054561   43.399    0.000  719.105    0.000 <__array_function__ internals>:2(prod)
              245181860  707.989    0.000  707.989    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               40757504  696.605    0.000  696.605    0.000 {built-in method clamp}
               26054561   40.049    0.000  666.433    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
               81515008  660.589    0.000  660.589    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               41213443  645.482    0.000  645.482    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               26054561   64.411    0.000  626.384    0.000 fromnumeric.py:2912(prod)
               40757504  601.148    0.000  601.148    0.000 {built-in method bernoulli}
                 318418  453.783    0.001  589.607    0.002 replaybuffer.py:42(sample_option_critic)
               26054561  150.134    0.000  561.972    0.000 fromnumeric.py:70(_wrapreduction)
               40757504  530.199    0.000  530.199    0.000 {built-in method all}
               40757504  528.316    0.000  528.316    0.000 {built-in method log}
               17831402  523.587    0.000  523.587    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               40757504  512.881    0.000  512.881    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
                1273672   76.211    0.000  406.114    0.000 optimizer.py:189(zero_grad)
               40757504  385.929    0.000  385.929    0.000 {built-in method multinomial}
               40757504   88.068    0.000  359.261    0.000 layers.py:838(isFree)
              536414386  241.656    0.000  347.933    0.000 {built-in method builtins.isinstance}
               26054561  344.461    0.000  344.461    0.000 {method 'reduce' of 'numpy.ufunc' objects}
              122731028  340.642    0.000  340.642    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                8915711  206.708    0.000  338.735    0.000 layer.py:175(NoRock_update)
              125775125  337.208    0.000  337.208    0.000 {method 'to' of 'torch._C._TensorBase' objects}
               17831402  326.565    0.000  326.565    0.000 {method 'add_' of 'torch._C._TensorBase' objects}


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
Subject: Job 9632739: <Attempt7_Diamonds1_option_critic_2> in cluster <dcc> Exited

Job <Attempt7_Diamonds1_option_critic_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed May 12 14:11:11 2021
Job was executed on host(s) <n-62-23-28>, in queue <hpc>, as user <s183914> in cluster <dcc> at Sun May 16 23:16:53 2021
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

    CPU time :                                   258889.97 sec.
    Max Memory :                                 864 MB
    Average Memory :                             852.30 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15520.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   259038 sec.
    Turnaround time :                            637272 sec.

The output (if any) is above this job summary.

