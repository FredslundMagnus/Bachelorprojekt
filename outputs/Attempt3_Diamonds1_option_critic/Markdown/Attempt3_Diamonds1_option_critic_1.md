[W NNPACK.cpp:80] Could not initialize NNPACK! Reason: Unsupported hardware.

# Parameters

    Name :                      Attempt3_Diamonds1_option_critic-1
    Main :                      option_critic_run
    Level :                     Levels.Causal2
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


      34161636313 function calls (33125925848 primitive calls) in 258900.89 seconds

##    Ordered by: cumulative time
   List reduced from 426 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.890 258900.890 {built-in method builtins.exec}
                      1    0.315    0.315 258900.890 258900.890 <string>:1(<module>)
                      1 3901.879 3901.879 258900.575 258900.575 optionCritic.py:195(option_critic_run)
               37214800 10027.010    0.000 107910.801    0.003 optionCritic.py:143(actor_loss_fn)
        1375992733/340379275 10270.102    0.000 105245.144    0.000 module.py:866(_call_impl)
              115068162  774.358    0.000 95952.729    0.001 optionCritic.py:70(get_state)
              115068162 2837.469    0.000 92845.369    0.001 container.py:117(forward)
                1488592   12.474    0.000 74814.266    0.050 tensor.py:195(backward)
                1488592   14.633    0.000 74801.495    0.050 __init__.py:68(backward)
                1488592 74747.894    0.050 74747.894    0.050 {method 'run_backward' of 'torch._C._EngineBase' objects}
              230136324  895.373    0.000 54349.042    0.000 conv.py:398(forward)
              230136324  393.660    0.000 53127.672    0.000 conv.py:390(_conv_forward)
              230136324 52734.011    0.000 52734.011    0.000 {built-in method conv2d}
               37214800 3914.454    0.000 23162.067    0.001 optionCritic.py:91(get_action)
              455447437 1579.297    0.000 22010.079    0.000 linear.py:93(forward)
              455447437  577.444    0.000 19802.933    0.000 functional.py:1737(linear)
              455447437 19108.664    0.000 19108.664    0.000 {built-in method torch._C._nn.linear}
                1488592   33.620    0.000 16743.165    0.011 optimizer.py:84(wrapper)
                1488592   17.633    0.000 16603.795    0.011 grad_mode.py:24(decorate_context)
                1488592  102.484    0.000 16554.330    0.011 rmsprop.py:56(step)
                1488592  162.369    0.000 16335.138    0.011 _functional.py:203(rmsprop)
               20840270 13762.947    0.001 13762.947    0.001 {method 'sqrt' of 'torch._C._TensorBase' objects}
               37214800 1215.526    0.000 13378.700    0.000 optionCritic.py:80(predict_option_termination)
               74429600 1115.454    0.000 8586.749    0.000 distribution.py:34(__init__)
              345204486  492.159    0.000 8106.849    0.000 activation.py:713(forward)
              345204486  455.996    0.000 7614.691    0.000 functional.py:1364(leaky_relu)
               37214800  619.869    0.000 7569.878    0.000 categorical.py:115(log_prob)
              345204486 7073.288    0.000 7073.288    0.000 {built-in method torch._C._nn.leaky_relu}
               37214800  888.618    0.000 6827.019    0.000 categorical.py:49(__init__)
              113517854  471.710    0.000 6486.211    0.000 optionCritic.py:77(get_Q)
               74578459  467.873    0.000 5242.013    0.000 optionCritic.py:88(get_terminations)
               37214800  313.572    0.000 4859.492    0.000 bernoulli.py:34(__init__)
               37214800 2792.709    0.000 4246.633    0.000 constraints.py:398(check)
                1488592    9.720    0.000 3420.457    0.002 game.py:42(step)
                1488592   15.801    0.000 3296.009    0.002 layers.py:827(step)
               37214800  472.543    0.000 3145.321    0.000 distribution.py:240(_validate_sample)
                 148859   34.498    0.000 2439.623    0.016 optionCritic.py:116(critic_loss_fn)
              115068162  164.116    0.000 2317.465    0.000 activation.py:101(forward)
               37214800 1087.987    0.000 2255.822    0.000 categorical.py:123(entropy)
              115068162  145.823    0.000 2153.349    0.000 functional.py:1195(relu)
               37214800 2110.618    0.000 2110.618    0.000 constraints.py:364(check)
               37214800 2103.670    0.000 2103.670    0.000 constraints.py:249(check)
              115068162 1979.902    0.000 1979.902    0.000 {built-in method relu}
                1488593  158.250    0.000 1914.846    0.001 layers.py:793(update)
              111644400  210.306    0.000 1880.190    0.000 utils.py:106(__get__)
               37214800  331.350    0.000 1845.778    0.000 bernoulli.py:86(sample)
             1392367245 1842.725    0.000 1842.725    0.000 {built-in method torch._C._get_tracing_state}
              260503600 1779.993    0.000 1779.993    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              111942118  181.455    0.000 1705.974    0.000 tensor.py:525(__rsub__)
             1785980318 1619.435    0.000 1619.438    0.000 module.py:934(__getattr__)
              111644400 1618.681    0.000 1618.681    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
              115068162  114.796    0.000 1566.851    0.000 flatten.py:39(forward)
               37214800   76.760    0.000 1503.384    0.000 categorical.py:88(logits)
              111942118 1491.760    0.000 1491.760    0.000 {built-in method rsub}
              111793259 1476.528    0.000 1476.528    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
              115068162 1452.054    0.000 1452.054    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               37214800  367.969    0.000 1430.516    0.000 categorical.py:108(sample)
               37214800   76.767    0.000 1426.624    0.000 utils.py:82(probs_to_logits)
                1488592   63.559    0.000 1358.733    0.001 layers.py:17(step)
               74429600  420.298    0.000 1319.871    0.000 functional.py:46(broadcast_tensors)
               37214800  108.428    0.000 1290.755    0.000 layer.py:106(move)
               74578459 1271.366    0.000 1271.366    0.000 {method 'max' of 'torch._C._TensorBase' objects}
               20840270 1250.551    0.000 1250.551    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              111644400 1134.443    0.000 1134.443    0.000 {method 'all' of 'torch._C._TensorBase' objects}
               16374512   44.827    0.000 1074.523    0.000 tensor.py:575(__iter__)
             5957770674 1009.775    0.000 1022.007    0.000 {built-in method builtins.len}
                1575761   27.041    0.000 1015.917    0.001 layers.py:849(restart)
               16374512  993.865    0.000  993.865    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               37214800  200.733    0.000  985.058    0.000 utils.py:11(broadcast_all)
               37214800  134.406    0.000  882.040    0.000 utils.py:77(clamp_probs)
             5619039094  874.971    0.000  874.971    0.000 {method 'values' of 'collections.OrderedDict' objects}
               37214800  187.977    0.000  845.585    0.000 layers.py:844(check)
               37214800  835.679    0.000  835.679    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
                1575761   12.741    0.000  823.226    0.001 level.py:8(__init__)
               74429600  789.003    0.000  789.003    0.000 {built-in method broadcast_tensors}
               37214800  747.634    0.000  747.634    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
                1488592   77.276    0.000  735.505    0.000 replaybuffer.py:34(save_option_critic)
              112090977  731.082    0.000  731.082    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
                1575761   29.360    0.000  715.283    0.000 levels.py:151(generate)
               37214800  690.712    0.000  690.712    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
                7563340  104.867    0.000  656.513    0.000 level.py:41(notUsed)
              223586518  656.289    0.000  656.289    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               37214800  638.840    0.000  638.840    0.000 {built-in method clamp}
               38790536  625.252    0.000  625.252    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               37214800  619.063    0.000  619.063    0.000 {built-in method bernoulli}
               74429600  588.859    0.000  588.859    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                8702971  248.037    0.000  510.434    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               37214800  484.465    0.000  484.465    0.000 {built-in method all}
                1488592   92.747    0.000  484.291    0.000 optimizer.py:189(zero_grad)
               37214800  467.818    0.000  467.818    0.000 {built-in method log}
               37214800  464.207    0.000  464.207    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
               20840270  413.127    0.000  413.127    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               20840270  399.546    0.000  399.546    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               10420151  224.708    0.000  356.579    0.000 layer.py:175(NoRock_update)
               20840270  346.598    0.000  346.598    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               37214800  344.066    0.000  344.066    0.000 {built-in method multinomial}
              490064976  213.125    0.000  319.302    0.000 {built-in method builtins.isinstance}
              113223136  317.594    0.000  317.594    0.000 {method 'item' of 'torch._C._TensorBase' objects}
              115068176  317.177    0.000  317.177    0.000 {method 'to' of 'torch._C._TensorBase' objects}
                7563340    9.733    0.000  316.382    0.000 level.py:38(elementsIn)


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
Subject: Job 9607844: <Attempt3_Diamonds1_option_critic_1> in cluster <dcc> Exited

Job <Attempt3_Diamonds1_option_critic_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon May  3 13:31:23 2021
Job was executed on host(s) <n-62-23-21>, in queue <hpc>, as user <s183914> in cluster <dcc> at Mon May  3 13:31:24 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon May  3 13:31:24 2021
Terminated at Thu May  6 13:26:33 2021
Results reported at Thu May  6 13:26:33 2021

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

    CPU time :                                   258897.00 sec.
    Max Memory :                                 866 MB
    Average Memory :                             849.53 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15518.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258938 sec.
    Turnaround time :                            258910 sec.

The output (if any) is above this job summary.

