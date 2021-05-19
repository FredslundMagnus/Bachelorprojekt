[W NNPACK.cpp:80] Could not initialize NNPACK! Reason: Unsupported hardware.

# Parameters

    Name :                      Attempt7_Lights2_option_critic-1
    Main :                      option_critic_run
    Level :                     Levels.Causal4
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
    Num :                       1
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              4315 minutes.
    Hours used :                71 hours.

# Profiling


      29468743093 function calls (28573431537 primitive calls) in 258901.27 seconds

##    Ordered by: cumulative time
   List reduced from 438 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258901.273 258901.273 {built-in method builtins.exec}
                      1    0.443    0.443 258901.273 258901.273 <string>:1(<module>)
                      1 4315.191 4315.191 258900.829 258900.829 optionCritic.py:195(option_critic_run)
        1185802792/293753743 9290.978    0.000 119497.505    0.000 module.py:866(_call_impl)
               32118784 8255.107    0.000 114831.808    0.004 optionCritic.py:143(actor_loss_fn)
               99116561  842.042    0.000 111632.320    0.001 optionCritic.py:70(get_state)
               99116561 2548.926    0.000 108492.349    0.001 container.py:117(forward)
              198233122  845.678    0.000 72662.364    0.000 conv.py:398(forward)
              198233122  439.290    0.000 71477.164    0.000 conv.py:390(_conv_forward)
              198233122 71037.874    0.000 71037.874    0.000 {built-in method conv2d}
                1003712    9.504    0.000 66081.844    0.066 tensor.py:195(backward)
                1003712   12.130    0.000 66072.154    0.066 __init__.py:68(backward)
                1003712 66028.944    0.066 66028.944    0.066 {method 'run_backward' of 'torch._C._EngineBase' objects}
               32118784 3692.225    0.000 21930.194    0.001 optionCritic.py:91(get_action)
              392870304 1436.468    0.000 20589.242    0.000 linear.py:93(forward)
              392870304  509.535    0.000 18565.487    0.000 functional.py:1737(linear)
              392870304 17945.228    0.000 17945.228    0.000 {built-in method torch._C._nn.linear}
                1003712   25.949    0.000 14063.334    0.014 optimizer.py:84(wrapper)
                1003712   14.589    0.000 13956.594    0.014 grad_mode.py:24(decorate_context)
                1003712   74.695    0.000 13914.389    0.014 rmsprop.py:56(step)
                1003712  143.279    0.000 13760.276    0.014 _functional.py:203(rmsprop)
               32118784 1141.321    0.000 12640.583    0.000 optionCritic.py:80(predict_option_termination)
               14051962 11712.664    0.001 11712.664    0.001 {method 'sqrt' of 'torch._C._TensorBase' objects}
               64237568 1108.615    0.000 8025.064    0.000 distribution.py:34(__init__)
               32118784  611.658    0.000 7314.030    0.000 categorical.py:115(log_prob)
              297349683  417.358    0.000 7252.228    0.000 activation.py:713(forward)
              297349683  424.403    0.000 6834.871    0.000 functional.py:1364(leaky_relu)
              297349683 6328.116    0.000 6328.116    0.000 {built-in method torch._C._nn.leaky_relu}
               32118784  814.512    0.000 6280.124    0.000 categorical.py:49(__init__)
                 250928   62.814    0.000 6135.483    0.024 optionCritic.py:116(critic_loss_fn)
               98029902  413.480    0.000 5724.482    0.000 optionCritic.py:77(get_Q)
               32118784  320.130    0.000 4749.842    0.000 bernoulli.py:34(__init__)
               64488496  413.452    0.000 4637.450    0.000 optionCritic.py:88(get_terminations)
               32118784 2600.873    0.000 3915.710    0.000 constraints.py:398(check)
                1003712    9.463    0.000 3734.272    0.004 game.py:42(step)
                1003712   11.253    0.000 3613.667    0.004 layers.py:827(step)
               32118784  463.979    0.000 2956.233    0.000 distribution.py:240(_validate_sample)
               99116561  212.373    0.000 2258.052    0.000 activation.py:101(forward)
               32118784 1022.887    0.000 2054.985    0.000 categorical.py:123(entropy)
               99116561  177.416    0.000 2045.679    0.000 functional.py:1195(relu)
               32118784 1978.052    0.000 1978.052    0.000 constraints.py:249(check)
               32118784 1954.783    0.000 1954.783    0.000 constraints.py:364(check)
                1003712   58.325    0.000 1926.447    0.002 layers.py:17(step)
               96356352  232.180    0.000 1873.151    0.000 utils.py:106(__get__)
               32118784  141.871    0.000 1863.007    0.000 layer.py:106(move)
               99116561 1842.560    0.000 1842.560    0.000 {built-in method relu}
               32118784  354.987    0.000 1822.349    0.000 bernoulli.py:86(sample)
              224831488 1681.822    0.000 1681.822    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                1003713  131.408    0.000 1670.086    0.002 layers.py:793(update)
             1196843624 1588.626    0.000 1588.626    0.000 {built-in method torch._C._get_tracing_state}
             1540328704 1570.152    0.000 1570.258    0.000 module.py:934(__getattr__)
               96858208  200.039    0.000 1568.411    0.000 tensor.py:525(__rsub__)
               99116561  141.139    0.000 1541.480    0.000 flatten.py:39(forward)
               32118784   70.183    0.000 1462.775    0.000 categorical.py:88(logits)
               99116561 1400.340    0.000 1400.340    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               32118784   87.067    0.000 1392.592    0.000 utils.py:82(probs_to_logits)
               96356352 1391.322    0.000 1391.322    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
               32118784  371.436    0.000 1384.751    0.000 categorical.py:108(sample)
               64237568  429.181    0.000 1349.434    0.000 functional.py:46(broadcast_tensors)
               96858208 1339.238    0.000 1339.238    0.000 {built-in method rsub}
               96607280 1331.611    0.000 1331.611    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
               32118784  266.299    0.000 1297.549    0.000 layers.py:844(check)
               64488496 1185.571    0.000 1185.571    0.000 {method 'max' of 'torch._C._TensorBase' objects}
               11040832   39.644    0.000 1060.182    0.000 tensor.py:575(__iter__)
               32118784  211.140    0.000 1016.772    0.000 utils.py:11(broadcast_all)
               96356352 1014.923    0.000 1014.923    0.000 {method 'all' of 'torch._C._TensorBase' objects}
               14051962 1008.754    0.000 1008.754    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               11040832  991.722    0.000  991.722    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
             5218046775  915.467    0.000  926.428    0.000 {built-in method builtins.len}
               32118784  869.440    0.000  869.440    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               32118784  147.870    0.000  842.800    0.000 utils.py:77(clamp_probs)
               64237568  805.050    0.000  805.050    0.000 {built-in method broadcast_tensors}
             4842327729  768.382    0.000  768.382    0.000 {method 'values' of 'collections.OrderedDict' objects}
                1171726   33.583    0.000  725.191    0.001 layers.py:849(restart)
               32118784  694.930    0.000  694.930    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
               97109136  684.204    0.000  684.204    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               12716330  316.176    0.000  668.333    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                1003712   69.708    0.000  667.005    0.001 replaybuffer.py:34(save_option_critic)
               32118784  643.640    0.000  643.640    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
               32118784  600.659    0.000  600.659    0.000 {built-in method bernoulli}
                 250928  457.255    0.002  588.810    0.002 replaybuffer.py:42(sample_option_critic)
               33290478  582.492    0.000  582.492    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
              193214560  576.659    0.000  576.659    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               32118784  572.013    0.000  572.013    0.000 {built-in method clamp}
               64237568  541.085    0.000  541.085    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               10037130  350.427    0.000  534.589    0.000 layer.py:159(update)
                1171726   13.145    0.000  502.007    0.000 level.py:8(__init__)
               32118784  462.725    0.000  462.725    0.000 {built-in method log}
               32118784  452.312    0.000  452.312    0.000 {built-in method all}
               32118784  437.786    0.000  437.786    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
                1171726   69.873    0.000  411.545    0.000 levels.py:199(generate)
                1003712   67.150    0.000  359.120    0.000 optimizer.py:189(zero_grad)
               32118784  354.385    0.000  354.385    0.000 {built-in method multinomial}
               12716330   21.514    0.000  352.157    0.000 <__array_function__ internals>:2(prod)
              427406458  219.895    0.000  350.154    0.000 {built-in method builtins.isinstance}
               99116575  348.075    0.000  348.075    0.000 {method 'to' of 'torch._C._TensorBase' objects}
               32118784   73.500    0.000  347.393    0.000 layers.py:838(isFree)
               14051962  333.427    0.000  333.427    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               12716330   19.446    0.000  326.014    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
               14051962  307.731    0.000  307.731    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}


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
Subject: Job 9632735: <Attempt7_Lights2_option_critic_1> in cluster <dcc> Exited

Job <Attempt7_Lights2_option_critic_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed May 12 14:11:10 2021
Job was executed on host(s) <n-62-23-29>, in queue <hpc>, as user <s183914> in cluster <dcc> at Sun May 16 23:16:53 2021
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

    CPU time :                                   258857.72 sec.
    Max Memory :                                 1093 MB
    Average Memory :                             1086.23 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15291.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   259038 sec.
    Turnaround time :                            637273 sec.

The output (if any) is above this job summary.

