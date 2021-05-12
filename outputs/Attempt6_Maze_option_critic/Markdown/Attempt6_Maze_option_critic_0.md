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

    Name :                      Attempt6_Maze_option_critic-0
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


      53387576833 function calls (51723055156 primitive calls) in 258900.80 seconds

##    Ordered by: cumulative time
   List reduced from 435 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.802 258900.802 {built-in method builtins.exec}
                      1    0.360    0.360 258900.802 258900.802 <string>:1(<module>)
                      1 6500.592 6500.592 258900.441 258900.441 optionCritic.py:195(option_critic_run)
               59713760 9372.142    0.000 120687.497    0.002 optionCritic.py:143(actor_loss_fn)
        2203368556/544912186 10841.997    0.000 117904.516    0.000 module.py:866(_call_impl)
              184272930  907.756    0.000 109776.351    0.001 optionCritic.py:70(get_state)
              184272930 2493.634    0.000 106180.666    0.001 container.py:117(forward)
                1866055   15.353    0.000 68521.501    0.037 tensor.py:195(backward)
                1866055   19.624    0.000 68505.886    0.037 __init__.py:68(backward)
                1866055 68442.586    0.037 68442.586    0.037 {method 'run_backward' of 'torch._C._EngineBase' objects}
              368545860  971.847    0.000 64986.559    0.000 conv.py:398(forward)
              368545860  545.643    0.000 63587.767    0.000 conv.py:390(_conv_forward)
              368545860 63042.124    0.000 63042.124    0.000 {built-in method conv2d}
              729185116 1732.251    0.000 24279.103    0.000 linear.py:93(forward)
              729185116  682.696    0.000 21775.577    0.000 functional.py:1737(linear)
               59713760 3540.098    0.000 21000.910    0.000 optionCritic.py:91(get_action)
              729185116 20925.056    0.000 20925.056    0.000 {built-in method torch._C._nn.linear}
               59713760 1354.556    0.000 16036.816    0.000 optionCritic.py:80(predict_option_termination)
              119427520 1376.548    0.000 8661.460    0.000 distribution.py:34(__init__)
              552818790  569.312    0.000 7707.035    0.000 activation.py:713(forward)
              552818790  557.507    0.000 7137.722    0.000 functional.py:1364(leaky_relu)
               59713760  590.705    0.000 6986.526    0.000 categorical.py:115(log_prob)
               59713760  549.566    0.000 6597.960    0.000 bernoulli.py:34(__init__)
              552818790 6455.404    0.000 6455.404    0.000 {built-in method torch._C._nn.leaky_relu}
              181031463  407.477    0.000 5995.049    0.000 optionCritic.py:77(get_Q)
               59713760  798.371    0.000 5875.158    0.000 categorical.py:49(__init__)
                1866055   10.785    0.000 5160.174    0.003 game.py:42(step)
                1866055   17.732    0.000 5018.554    0.003 layers.py:827(step)
                1866055   43.689    0.000 4747.180    0.003 optimizer.py:84(wrapper)
              119894033  432.745    0.000 4734.672    0.000 optionCritic.py:88(get_terminations)
                1866055   24.299    0.000 4587.195    0.002 grad_mode.py:24(decorate_context)
                1866055  116.721    0.000 4517.932    0.002 adam.py:55(step)
                1866055  675.195    0.000 4276.602    0.002 _functional.py:53(adam)
                 466513   82.430    0.000 3841.334    0.008 optionCritic.py:116(critic_loss_fn)
               59713760 2396.387    0.000 3580.765    0.000 constraints.py:398(check)
               59713760  483.125    0.000 2823.113    0.000 distribution.py:240(_validate_sample)
                1866055   89.813    0.000 2817.296    0.002 layers.py:17(step)
               59713760  233.188    0.000 2719.888    0.000 layer.py:106(move)
               59713760  536.106    0.000 2510.682    0.000 bernoulli.py:86(sample)
               59713760 2401.014    0.000 2401.014    0.000 constraints.py:364(check)
              184272930  242.723    0.000 2219.375    0.000 activation.py:101(forward)
                1866056  175.972    0.000 2174.215    0.001 layers.py:793(update)
             2860044311 2002.674    0.000 2002.809    0.000 module.py:934(__getattr__)
              184272930  219.680    0.000 1976.652    0.000 functional.py:1195(relu)
               59713760 1019.561    0.000 1950.764    0.000 categorical.py:123(entropy)
               59713760  255.391    0.000 1949.997    0.000 layers.py:844(check)
              417996320 1837.732    0.000 1837.732    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               59713760 1837.303    0.000 1837.303    0.000 constraints.py:249(check)
              180074306  244.430    0.000 1779.072    0.000 tensor.py:525(__rsub__)
              179141280  234.454    0.000 1738.833    0.000 utils.py:106(__get__)
              184272930  182.643    0.000 1736.957    0.000 flatten.py:39(forward)
              184272930 1724.953    0.000 1724.953    0.000 {built-in method relu}
              119427520  637.972    0.000 1707.629    0.000 functional.py:46(broadcast_tensors)
              184272930 1554.314    0.000 1554.314    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               59713760  330.744    0.000 1526.755    0.000 utils.py:11(broadcast_all)
              180074306 1502.900    0.000 1502.900    0.000 {built-in method rsub}
               20526605   49.660    0.000 1477.924    0.000 tensor.py:575(__iter__)
              119894033 1415.155    0.000 1415.155    0.000 {method 'max' of 'torch._C._TensorBase' objects}
               20526605 1398.473    0.000 1398.473    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               59713760  381.503    0.000 1380.366    0.000 categorical.py:108(sample)
               59713760   68.457    0.000 1325.375    0.000 categorical.py:88(logits)
              179607793 1320.485    0.000 1320.485    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
             2223895161 1313.305    0.000 1313.305    0.000 {built-in method torch._C._get_tracing_state}
               59713760   75.956    0.000 1256.918    0.000 utils.py:82(probs_to_logits)
              179141280 1230.811    0.000 1230.811    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
             9415867050 1197.360    0.000 1211.824    0.000 {built-in method builtins.len}
               59713760  651.580    0.000 1137.380    0.000 layers.py:538(check)
              179141280 1087.197    0.000 1087.197    0.000 {method 'all' of 'torch._C._TensorBase' objects}
                 466513  881.375    0.002 1062.817    0.002 replaybuffer.py:42(sample_option_critic)
             8997747154 1002.949    0.000 1002.949    0.000 {method 'values' of 'collections.OrderedDict' objects}
               52249528  994.364    0.000  994.364    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               59713760  936.780    0.000  936.780    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
              119427520  891.650    0.000  891.650    0.000 {built-in method broadcast_tensors}
                1866055   89.951    0.000  799.912    0.000 replaybuffer.py:34(save_option_critic)
               59713760  151.249    0.000  743.221    0.000 utils.py:77(clamp_probs)
                 957189   16.257    0.000  735.049    0.001 layers.py:849(restart)
               59713760  723.075    0.000  723.075    0.000 {built-in method bernoulli}
              180540819  693.435    0.000  693.435    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
                 957189    8.277    0.000  624.247    0.001 level.py:8(__init__)
               26124764  601.014    0.000  601.014    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               59713760  592.392    0.000  592.392    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
               59713760  591.972    0.000  591.972    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
              359215586  579.771    0.000  579.771    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               60670917  574.531    0.000  574.531    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                 957189   89.708    0.000  560.253    0.001 levels.py:428(generate)
                1866055   90.709    0.000  547.897    0.000 optimizer.py:189(zero_grad)
               26124764  545.334    0.000  545.334    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               11196336  372.949    0.000  543.370    0.000 layer.py:159(update)
              119427520  518.315    0.000  518.315    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               59589286   60.058    0.000  509.942    0.000 {built-in method builtins.any}
              795471282  324.248    0.000  504.035    0.000 {built-in method builtins.isinstance}
               26124764  499.394    0.000  499.394    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               59713760  491.690    0.000  491.690    0.000 {built-in method clamp}
               52249528  480.090    0.000  480.090    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               26124764  470.251    0.000  470.251    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              416292319  147.245    0.000  450.008    0.000 layers.py:809(<genexpr>)
              180102200  449.374    0.000  449.374    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               59713760  437.741    0.000  437.741    0.000 {built-in method log}
               59713760  435.960    0.000  435.960    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
              184272944  425.125    0.000  425.125    0.000 {method 'to' of 'torch._C._TensorBase' objects}


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
Subject: Job 9624165: <Attempt6_Maze_option_critic_0> in cluster <dcc> Exited

Job <Attempt6_Maze_option_critic_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun May  9 01:22:28 2021
Job was executed on host(s) <n-62-11-61>, in queue <hpc>, as user <s183914> in cluster <dcc> at Sun May  9 01:22:29 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun May  9 01:22:29 2021
Terminated at Wed May 12 01:17:34 2021
Results reported at Wed May 12 01:17:34 2021

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

    CPU time :                                   258289.70 sec.
    Max Memory :                                 950 MB
    Average Memory :                             932.64 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15434.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258956 sec.
    Turnaround time :                            258906 sec.

The output (if any) is above this job summary.

