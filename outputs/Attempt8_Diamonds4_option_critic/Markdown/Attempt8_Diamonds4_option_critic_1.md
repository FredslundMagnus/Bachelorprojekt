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

    Name :                      Attempt8_Diamonds4_option_critic-1
    Main :                      option_critic_run
    Level :                     Levels.Causal7
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


      37171206000 function calls (36013767082 primitive calls) in 258901.15 seconds

##    Ordered by: cumulative time
   List reduced from 437 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258901.149 258901.149 {built-in method builtins.exec}
                      1    0.370    0.370 258901.149 258901.149 <string>:1(<module>)
                      1 4346.555 4346.555 258900.779 258900.779 optionCritic.py:195(option_critic_run)
        1532001993/378780432 10905.749    0.000 115535.787    0.000 module.py:866(_call_impl)
               41522464 9865.458    0.000 115193.009    0.003 optionCritic.py:143(actor_loss_fn)
              128135729  822.600    0.000 105411.020    0.001 optionCritic.py:70(get_state)
              128135729 2993.276    0.000 102045.476    0.001 container.py:117(forward)
                1297577   10.845    0.000 72102.098    0.056 tensor.py:195(backward)
                1297577   11.777    0.000 72090.981    0.056 __init__.py:68(backward)
                1297577 72046.896    0.056 72046.896    0.056 {method 'run_backward' of 'torch._C._EngineBase' objects}
              256271458 1008.362    0.000 61118.562    0.000 conv.py:398(forward)
              256271458  407.714    0.000 59748.205    0.000 conv.py:390(_conv_forward)
              256271458 59340.491    0.000 59340.491    0.000 {built-in method conv2d}
               41522464 4418.327    0.000 25801.092    0.001 optionCritic.py:91(get_action)
              506916161 1814.894    0.000 23315.970    0.000 linear.py:93(forward)
              506916161  643.839    0.000 20827.786    0.000 functional.py:1737(linear)
              506916161 20053.797    0.000 20053.797    0.000 {built-in method torch._C._nn.linear}
               41522464 1301.844    0.000 13967.289    0.000 optionCritic.py:80(predict_option_termination)
               83044928 1179.351    0.000 9322.405    0.000 distribution.py:34(__init__)
              384407187  454.995    0.000 8802.610    0.000 activation.py:713(forward)
               41522464  671.655    0.000 8407.554    0.000 categorical.py:115(log_prob)
              384407187  456.880    0.000 8347.615    0.000 functional.py:1364(leaky_relu)
              384407187 7793.037    0.000 7793.037    0.000 {built-in method torch._C._nn.leaky_relu}
               41522464  981.889    0.000 7580.117    0.000 categorical.py:49(__init__)
              125752917  517.092    0.000 7023.904    0.000 optionCritic.py:77(get_Q)
               83369322  499.333    0.000 5694.174    0.000 optionCritic.py:88(get_terminations)
                 324394   73.982    0.000 5274.972    0.016 optionCritic.py:116(critic_loss_fn)
               41522464  292.676    0.000 4874.946    0.000 bernoulli.py:34(__init__)
               41522464 3137.828    0.000 4731.905    0.000 constraints.py:398(check)
                1297577    7.679    0.000 3932.873    0.003 game.py:42(step)
                1297577   12.972    0.000 3829.427    0.003 layers.py:827(step)
                1297577   26.743    0.000 3668.106    0.003 optimizer.py:84(wrapper)
                1297577   12.272    0.000 3560.397    0.003 grad_mode.py:24(decorate_context)
               41522464  520.627    0.000 3527.406    0.000 distribution.py:240(_validate_sample)
                1297577   88.724    0.000 3523.238    0.003 rmsprop.py:56(step)
                1297577  139.629    0.000 3332.560    0.003 _functional.py:203(rmsprop)
              128135729  185.525    0.000 2510.242    0.000 activation.py:101(forward)
               41522464 1219.172    0.000 2491.676    0.000 categorical.py:123(entropy)
               41522464 2375.508    0.000 2375.508    0.000 constraints.py:249(check)
              128135729  166.290    0.000 2324.717    0.000 functional.py:1195(relu)
                1297577   69.589    0.000 2304.548    0.002 layers.py:17(step)
               41522464  218.818    0.000 2230.070    0.000 layer.py:106(move)
               41522464 2226.920    0.000 2226.920    0.000 constraints.py:364(check)
              128135729 2127.897    0.000 2127.897    0.000 {built-in method relu}
              124567392  229.729    0.000 2059.082    0.000 utils.py:106(__get__)
              290657248 2006.697    0.000 2006.697    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
             1546275340 1997.681    0.000 1997.681    0.000 {built-in method torch._C._get_tracing_state}
              125216180  195.757    0.000 1841.573    0.000 tensor.py:525(__rsub__)
               18166072 1801.965    0.000 1801.965    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               41522464  310.167    0.000 1800.596    0.000 bernoulli.py:86(sample)
              124567392 1759.359    0.000 1759.359    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
             1988369333 1738.804    0.000 1738.929    0.000 module.py:934(__getattr__)
              128135729  122.615    0.000 1737.926    0.000 flatten.py:39(forward)
               41522464   81.884    0.000 1651.541    0.000 categorical.py:88(logits)
              128135729 1615.311    0.000 1615.311    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               41522464  410.708    0.000 1614.725    0.000 categorical.py:108(sample)
              125216180 1609.782    0.000 1609.782    0.000 {built-in method rsub}
              124891786 1609.610    0.000 1609.610    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
               41522464   86.633    0.000 1569.657    0.000 utils.py:82(probs_to_logits)
               41522464  251.252    0.000 1555.946    0.000 layers.py:844(check)
                1297578  134.826    0.000 1505.504    0.001 layers.py:793(update)
               27092561  657.050    0.000 1379.923    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               83044928  424.952    0.000 1362.412    0.000 functional.py:46(broadcast_tensors)
               83369322 1315.664    0.000 1315.664    0.000 {method 'max' of 'torch._C._TensorBase' objects}
              124567392 1229.071    0.000 1229.071    0.000 {method 'all' of 'torch._C._TensorBase' objects}
             6609266608 1110.695    0.000 1121.758    0.000 {built-in method builtins.len}
               14273347   39.466    0.000 1067.536    0.000 tensor.py:575(__iter__)
               14273347  996.316    0.000  996.316    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
             6256143701  981.443    0.000  981.443    0.000 {method 'values' of 'collections.OrderedDict' objects}
               41522464  145.558    0.000  968.514    0.000 utils.py:77(clamp_probs)
               41522464  924.641    0.000  924.641    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               41522464  167.842    0.000  903.215    0.000 utils.py:11(broadcast_all)
               41522464  822.956    0.000  822.956    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
               83044928  806.957    0.000  806.957    0.000 {built-in method broadcast_tensors}
              125540574  802.836    0.000  802.836    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
                1297577   81.449    0.000  794.234    0.001 replaybuffer.py:34(save_option_critic)
               41522464  763.524    0.000  763.524    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
               27092561   45.210    0.000  722.872    0.000 <__array_function__ internals>:2(prod)
              249783572  719.642    0.000  719.642    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               41522464  695.218    0.000  695.218    0.000 {built-in method clamp}
               83044928  675.248    0.000  675.248    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               27092561   40.391    0.000  668.464    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
               42059201  643.227    0.000  643.227    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               27092561   65.761    0.000  628.073    0.000 fromnumeric.py:2912(prod)
                 536769   10.140    0.000  617.446    0.001 layers.py:849(restart)
               41522464  588.172    0.000  588.172    0.000 {built-in method bernoulli}
                 324394  449.529    0.001  584.314    0.002 replaybuffer.py:42(sample_option_critic)
               27092561  142.519    0.000  562.312    0.000 fromnumeric.py:70(_wrapreduction)
               41522464  538.750    0.000  538.750    0.000 {built-in method all}
                 536769    4.480    0.000  528.899    0.001 level.py:8(__init__)
               41522464  514.510    0.000  514.510    0.000 {built-in method log}
               41522464  513.332    0.000  513.332    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
                 536769   34.951    0.000  490.179    0.001 levels.py:277(generate)
               18166072  482.539    0.000  482.539    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               41522464  356.985    0.000  477.173    0.000 layers.py:471(check)
                4786662   65.376    0.000  428.130    0.000 level.py:41(notUsed)
               41522464  326.846    0.000  425.087    0.000 layers.py:77(check)
                9083046  277.332    0.000  420.807    0.000 layer.py:159(update)
                1297577   79.083    0.000  415.877    0.000 optimizer.py:189(zero_grad)
               41522464  385.748    0.000  385.748    0.000 {built-in method multinomial}


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
Subject: Job 9632934: <Attempt8_Diamonds4_option_critic_1> in cluster <dcc> Exited

Job <Attempt8_Diamonds4_option_critic_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed May 12 15:36:16 2021
Job was executed on host(s) <n-62-23-22>, in queue <hpc>, as user <s183914> in cluster <dcc> at Sun May 16 23:16:52 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun May 16 23:16:52 2021
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

    CPU time :                                   258863.25 sec.
    Max Memory :                                 864 MB
    Average Memory :                             854.85 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15520.00 MB
    Max Swap :                                   -
    Max Processes :                              5
    Max Threads :                                6
    Run time :                                   258978 sec.
    Turnaround time :                            632167 sec.

The output (if any) is above this job summary.

