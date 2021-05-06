
# Parameters

    Name :                      Attempt3_Coconuts_option_critic-0
    Main :                      option_critic_run
    Level :                     Levels.Coconuts
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


      39300748835 function calls (38077948476 primitive calls) in 258900.87 seconds

##    Ordered by: cumulative time
   List reduced from 438 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.866 258900.866 {built-in method builtins.exec}
                      1    0.332    0.332 258900.865 258900.865 <string>:1(<module>)
                      1 4260.420 4260.420 258900.534 258900.534 optionCritic.py:195(option_critic_run)
               43937250 8431.683    0.000 101484.025    0.002 optionCritic.py:143(actor_loss_fn)
        1623240275/400554473 9964.397    0.000 99610.778    0.000 module.py:866(_call_impl)
              135853978  731.338    0.000 91460.021    0.001 optionCritic.py:70(get_state)
              135853978 2405.862    0.000 88494.413    0.001 container.py:117(forward)
                1757490   11.738    0.000 63839.702    0.036 tensor.py:195(backward)
                1757490   16.108    0.000 63827.654    0.036 __init__.py:68(backward)
                1757490 63772.622    0.036 63772.622    0.036 {method 'run_backward' of 'torch._C._EngineBase' objects}
              271707956  902.042    0.000 53682.145    0.000 conv.py:398(forward)
              271707956  574.185    0.000 52442.866    0.000 conv.py:390(_conv_forward)
              271707956 51868.682    0.000 51868.682    0.000 {built-in method conv2d}
                1757490   38.427    0.000 37659.817    0.021 optimizer.py:84(wrapper)
                1757490   24.433    0.000 37516.977    0.021 grad_mode.py:24(decorate_context)
                1757490  109.536    0.000 37449.144    0.021 rmsprop.py:56(step)
                1757490  136.229    0.000 37217.331    0.021 _functional.py:203(rmsprop)
               24604842 33637.927    0.001 33637.927    0.001 {method 'sqrt' of 'torch._C._TensorBase' objects}
               43937250 3610.457    0.000 21100.320    0.000 optionCritic.py:91(get_action)
              536408451 1576.106    0.000 19157.327    0.000 linear.py:93(forward)
              536408451  685.310    0.000 16995.084    0.000 functional.py:1737(linear)
              536408451 16191.194    0.000 16191.194    0.000 {built-in method torch._C._nn.linear}
               43937250 1160.924    0.000 13056.958    0.000 optionCritic.py:80(predict_option_termination)
               87874500 1193.047    0.000 7698.895    0.000 distribution.py:34(__init__)
              407561934  494.225    0.000 7350.034    0.000 activation.py:713(forward)
               43937250  602.853    0.000 7046.355    0.000 categorical.py:115(log_prob)
              407561934  511.053    0.000 6855.809    0.000 functional.py:1364(leaky_relu)
              407561934 6249.480    0.000 6249.480    0.000 {built-in method torch._C._nn.leaky_relu}
               43937250  793.848    0.000 5930.442    0.000 categorical.py:49(__init__)
              132712996  442.160    0.000 5782.840    0.000 optionCritic.py:77(get_Q)
               43937250  349.932    0.000 4716.136    0.000 bernoulli.py:34(__init__)
               88050249  444.320    0.000 4424.383    0.000 optionCritic.py:88(get_terminations)
                1757490   10.461    0.000 4252.171    0.002 game.py:42(step)
                1757490   17.490    0.000 4132.250    0.002 layers.py:827(step)
               43937250 2402.277    0.000 3572.777    0.000 constraints.py:398(check)
               43937250  499.755    0.000 2796.899    0.000 distribution.py:240(_validate_sample)
                1757490   74.756    0.000 2518.975    0.001 layers.py:17(step)
               43937250  253.082    0.000 2437.692    0.000 layer.py:106(move)
               24604842 2384.424    0.000 2384.424    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              135853978  185.940    0.000 2027.292    0.000 activation.py:101(forward)
                 175749   31.311    0.000 1981.279    0.011 optionCritic.py:116(critic_loss_fn)
               43937250  957.515    0.000 1952.247    0.000 categorical.py:123(entropy)
               43937250 1909.083    0.000 1909.083    0.000 constraints.py:364(check)
              135853978  175.675    0.000 1841.352    0.000 functional.py:1195(relu)
              131811750  237.219    0.000 1832.617    0.000 utils.py:106(__get__)
               43937250  350.182    0.000 1799.278    0.000 bernoulli.py:86(sample)
               43937250 1775.413    0.000 1775.413    0.000 constraints.py:249(check)
              135853978 1641.407    0.000 1641.407    0.000 {built-in method relu}
             2104666410 1641.211    0.000 1641.214    0.000 module.py:934(__getattr__)
                1757491  161.937    0.000 1587.974    0.001 layers.py:793(update)
               43937250  263.913    0.000 1529.801    0.000 layers.py:844(check)
              307560750 1526.022    0.000 1526.022    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              135853978  149.593    0.000 1481.519    0.000 flatten.py:39(forward)
              132163248  192.880    0.000 1461.309    0.000 tensor.py:525(__rsub__)
               43937250   76.541    0.000 1414.333    0.000 categorical.py:88(logits)
             1642572665 1404.144    0.000 1404.144    0.000 {built-in method torch._C._get_tracing_state}
               43937250  372.468    0.000 1388.526    0.000 categorical.py:108(sample)
               43937250   81.715    0.000 1337.793    0.000 utils.py:82(probs_to_logits)
               87874500  468.965    0.000 1332.788    0.000 functional.py:46(broadcast_tensors)
              135853978 1331.926    0.000 1331.926    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              131811750 1296.709    0.000 1296.709    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
              132163248 1240.783    0.000 1240.783    0.000 {built-in method rsub}
              131987499 1191.829    0.000 1191.829    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
             6995491099 1122.338    0.000 1136.463    0.000 {built-in method builtins.len}
               88050249 1111.839    0.000 1111.839    0.000 {method 'max' of 'torch._C._TensorBase' objects}
               19332390   49.229    0.000 1088.906    0.000 tensor.py:575(__iter__)
               19332390 1008.659    0.000 1008.659    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               43937250  201.206    0.000  995.950    0.000 utils.py:11(broadcast_all)
              131811750  927.843    0.000  927.843    0.000 {method 'all' of 'torch._C._TensorBase' objects}
             6628815078  921.752    0.000  921.752    0.000 {method 'values' of 'collections.OrderedDict' objects}
               43937250  160.019    0.000  841.188    0.000 utils.py:77(clamp_probs)
               43937250  809.646    0.000  809.646    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               87874500  738.550    0.000  738.550    0.000 {built-in method broadcast_tensors}
               43937250  681.170    0.000  681.170    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
                1757490   77.627    0.000  656.643    0.000 replaybuffer.py:34(save_option_critic)
               43937250  633.517    0.000  633.517    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
                 549772   10.143    0.000  625.890    0.001 layers.py:849(restart)
              132338997  592.964    0.000  592.964    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               44486998  547.664    0.000  547.664    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               87874500  543.705    0.000  543.705    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               43937250  540.514    0.000  540.514    0.000 {built-in method clamp}
               43937250  538.046    0.000  538.046    0.000 {built-in method bernoulli}
                 549772    4.616    0.000  532.510    0.001 level.py:8(__init__)
              263974998  525.620    0.000  525.620    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                1757490   90.736    0.000  503.531    0.000 optimizer.py:189(zero_grad)
               43937250  102.171    0.000  502.417    0.000 layers.py:838(isFree)
                 549772   33.948    0.000  493.390    0.001 levels.py:277(generate)
               43937250  350.517    0.000  481.747    0.000 layers.py:471(check)
               12302437  303.632    0.000  466.284    0.000 layer.py:159(update)
                4903140   71.299    0.000  431.428    0.000 level.py:41(notUsed)
               24604842  424.862    0.000  424.862    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               43937250  415.523    0.000  415.523    0.000 {built-in method all}
               43937250  414.889    0.000  414.889    0.000 {built-in method log}
              270689608  326.218    0.000  400.246    0.000 layer.py:103(isFree)
               43937250  386.130    0.000  386.130    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
               43937250  275.375    0.000  374.243    0.000 layers.py:77(check)
                 175749  288.198    0.002  360.335    0.002 replaybuffer.py:42(sample_option_critic)
               43937250  334.608    0.000  334.608    0.000 {built-in method multinomial}
              578589735  224.708    0.000  328.170    0.000 {built-in method builtins.isinstance}
              132365036  326.397    0.000  326.397    0.000 {method 'item' of 'torch._C._TensorBase' objects}


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
Subject: Job 9607864: <Attempt3_Coconuts_option_critic_0> in cluster <dcc> Exited

Job <Attempt3_Coconuts_option_critic_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon May  3 13:31:26 2021
Job was executed on host(s) <n-62-21-97>, in queue <hpc>, as user <s183914> in cluster <dcc> at Mon May  3 13:31:28 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon May  3 13:31:28 2021
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

    CPU time :                                   258918.34 sec.
    Max Memory :                                 866 MB
    Average Memory :                             844.63 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15518.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258926 sec.
    Turnaround time :                            258907 sec.

The output (if any) is above this job summary.

