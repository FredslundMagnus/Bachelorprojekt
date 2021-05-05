
# Parameters

    Name :                      Attempt2_Lights1_option_critic-0
    Main :                      option_critic_run
    Level :                     Levels.Causal3
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


      48596401182 function calls (47029933088 primitive calls) in 258900.71 seconds

##    Ordered by: cumulative time
   List reduced from 433 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.714 258900.714 {built-in method builtins.exec}
                      1    0.332    0.332 258900.714 258900.714 <string>:1(<module>)
                      1 5741.791 5741.791 258900.381 258900.381 optionCritic.py:195(option_critic_run)
               55706525 9665.377    0.000 115448.585    0.002 optionCritic.py:143(actor_loss_fn)
        2068723478/509497841 10401.710    0.000 114425.407    0.000 module.py:866(_call_impl)
              173247293  831.389    0.000 106343.756    0.001 optionCritic.py:70(get_state)
              173247293 2297.379    0.000 102957.562    0.001 container.py:117(forward)
                2228261   17.654    0.000 68356.036    0.031 tensor.py:195(backward)
                2228261   23.461    0.000 68338.047    0.031 __init__.py:68(backward)
                2228261 68259.642    0.031 68259.642    0.031 {method 'run_backward' of 'torch._C._EngineBase' objects}
              346494586 1036.895    0.000 65326.932    0.000 conv.py:398(forward)
              346494586  544.262    0.000 63865.251    0.000 conv.py:390(_conv_forward)
              346494586 63320.989    0.000 63320.989    0.000 {built-in method conv2d}
               55706525 3656.452    0.000 21912.325    0.000 optionCritic.py:91(get_action)
              682745134 1731.558    0.000 21426.382    0.000 linear.py:93(forward)
              682745134  664.375    0.000 18979.809    0.000 functional.py:1737(linear)
              682745134 18156.402    0.000 18156.402    0.000 {built-in method torch._C._nn.linear}
               55706525 1279.056    0.000 15137.512    0.000 optionCritic.py:80(predict_option_termination)
                2228261   51.604    0.000 10286.979    0.005 optimizer.py:84(wrapper)
                2228261   27.511    0.000 10096.586    0.005 grad_mode.py:24(decorate_context)
                2228261  141.426    0.000 10018.025    0.004 rmsprop.py:56(step)
                2228261  137.734    0.000 9711.190    0.004 _functional.py:203(rmsprop)
              111413050 1376.647    0.000 8763.082    0.000 distribution.py:34(__init__)
              519741879  531.806    0.000 7422.631    0.000 activation.py:713(forward)
               55706525  600.268    0.000 7301.180    0.000 categorical.py:115(log_prob)
              519741879  546.021    0.000 6890.825    0.000 functional.py:1364(leaky_relu)
              519741879 6234.250    0.000 6234.250    0.000 {built-in method torch._C._nn.leaky_relu}
               55706525  808.456    0.000 6180.874    0.000 categorical.py:49(__init__)
               55706525  489.192    0.000 6174.811    0.000 bernoulli.py:34(__init__)
              168573908  406.250    0.000 5869.378    0.000 optionCritic.py:77(get_Q)
               31195648 5132.254    0.000 5132.254    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                 557065   94.181    0.000 4904.699    0.009 optionCritic.py:116(critic_loss_fn)
              111970115  417.664    0.000 4586.992    0.000 optionCritic.py:88(get_terminations)
                2228261   12.050    0.000 4185.260    0.002 game.py:42(step)
                2228261   21.775    0.000 4040.735    0.002 layers.py:827(step)
               55706525 2561.603    0.000 3793.231    0.000 constraints.py:398(check)
               31195648 3417.384    0.000 3417.384    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               55706525  524.616    0.000 2993.489    0.000 distribution.py:240(_validate_sample)
                2228261   87.397    0.000 2518.423    0.001 layers.py:17(step)
               55706525  162.323    0.000 2422.177    0.000 layer.py:106(move)
               55706525 2324.468    0.000 2324.468    0.000 constraints.py:364(check)
               55706525  443.435    0.000 2260.187    0.000 bernoulli.py:86(sample)
              173247293  239.312    0.000 2130.323    0.000 activation.py:101(forward)
               55706525 1050.400    0.000 2033.125    0.000 categorical.py:123(entropy)
               55706525 1930.978    0.000 1930.978    0.000 constraints.py:249(check)
             2679680070 1921.735    0.000 1921.923    0.000 module.py:934(__getattr__)
              173247293  203.319    0.000 1891.011    0.000 functional.py:1195(relu)
              389945675 1856.611    0.000 1856.611    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              167119575  254.249    0.000 1820.711    0.000 utils.py:106(__get__)
              173247293  179.801    0.000 1681.491    0.000 flatten.py:39(forward)
              173247293 1657.325    0.000 1657.325    0.000 {built-in method relu}
              168233705  204.846    0.000 1632.822    0.000 tensor.py:525(__rsub__)
              111413050  562.338    0.000 1609.138    0.000 functional.py:46(broadcast_tensors)
              173247293 1501.690    0.000 1501.690    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                2228262  205.689    0.000 1492.203    0.001 layers.py:793(update)
               55706525  323.076    0.000 1462.683    0.000 layers.py:844(check)
               55706525  399.027    0.000 1425.945    0.000 categorical.py:108(sample)
              168233705 1395.369    0.000 1395.369    0.000 {built-in method rsub}
             2093234349 1390.876    0.000 1390.876    0.000 {built-in method torch._C._get_tracing_state}
               55706525  292.269    0.000 1382.397    0.000 utils.py:11(broadcast_all)
               24510871   61.546    0.000 1378.410    0.000 tensor.py:575(__iter__)
               55706525   74.578    0.000 1371.935    0.000 categorical.py:88(logits)
              111970115 1370.199    0.000 1370.199    0.000 {method 'max' of 'torch._C._TensorBase' objects}
               55706525   76.604    0.000 1297.357    0.000 utils.py:82(probs_to_logits)
              167119575 1291.168    0.000 1291.168    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
               24510871 1279.083    0.000 1279.083    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
              167676640 1274.962    0.000 1274.962    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
             9002204273 1221.581    0.000 1238.514    0.000 {built-in method builtins.len}
                 557065  942.747    0.002 1168.854    0.002 replaybuffer.py:42(sample_option_critic)
              167119575 1107.308    0.000 1107.308    0.000 {method 'all' of 'torch._C._TensorBase' objects}
             8448141205 1022.756    0.000 1022.756    0.000 {method 'values' of 'collections.OrderedDict' objects}
               55706525  963.762    0.000  963.762    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
              111413050  871.769    0.000  871.769    0.000 {built-in method broadcast_tensors}
                2228261   92.195    0.000  777.510    0.000 replaybuffer.py:34(save_option_critic)
               55706525  155.109    0.000  755.070    0.000 utils.py:77(clamp_probs)
              168790770  694.587    0.000  694.587    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               55706525  692.968    0.000  692.968    0.000 {built-in method bernoulli}
               55706525  122.957    0.000  669.150    0.000 layers.py:838(isFree)
                2228261  108.559    0.000  654.276    0.000 optimizer.py:189(zero_grad)
               55706525  643.501    0.000  643.501    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
               55706525  599.960    0.000  599.960    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
              335353280  568.221    0.000  568.221    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               56046728  550.145    0.000  550.145    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
              335444365  453.772    0.000  546.194    0.000 layer.py:103(isFree)
              111413050  534.974    0.000  534.974    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               55706525  516.143    0.000  516.143    0.000 {built-in method clamp}
               17826096  304.794    0.000  515.726    0.000 layer.py:175(NoRock_update)
               55706525  465.683    0.000  465.683    0.000 {built-in method log}
              737033546  286.238    0.000  461.120    0.000 {built-in method builtins.isinstance}
               55706525  444.554    0.000  444.554    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
               15040765  444.277    0.000  444.277    0.000 {built-in method tensor}
              167119600  125.739    0.000  423.378    0.000 {built-in method builtins.all}
               55706525  409.447    0.000  409.447    0.000 {built-in method all}
               31195648  389.982    0.000  389.982    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              173247307  382.178    0.000  382.178    0.000 {method 'to' of 'torch._C._TensorBase' objects}
               55706525  358.579    0.000  358.579    0.000 {built-in method multinomial}
               31195648  347.800    0.000  347.800    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              167464258  341.176    0.000  341.176    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               57934812  171.587    0.000  339.671    0.000 grad_mode.py:119(__enter__)
                6684787   12.853    0.000  336.317    0.000 game.py:38(board)


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
Subject: Job 9606110: <Attempt2_Lights1_option_critic_0> in cluster <dcc> Exited

Job <Attempt2_Lights1_option_critic_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon May  3 01:33:07 2021
Job was executed on host(s) <n-62-31-1>, in queue <hpc>, as user <s183914> in cluster <dcc> at Mon May  3 01:33:08 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon May  3 01:33:08 2021
Terminated at Thu May  6 01:28:28 2021
Results reported at Thu May  6 01:28:28 2021

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

    CPU time :                                   258291.42 sec.
    Max Memory :                                 903 MB
    Average Memory :                             891.73 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15481.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258951 sec.
    Turnaround time :                            258921 sec.

The output (if any) is above this job summary.

