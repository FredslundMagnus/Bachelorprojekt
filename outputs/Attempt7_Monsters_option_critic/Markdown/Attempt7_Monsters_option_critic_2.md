[W NNPACK.cpp:80] Could not initialize NNPACK! Reason: Unsupported hardware.

# Parameters

    Name :                      Attempt7_Monsters_option_critic-2
    Main :                      option_critic_run
    Level :                     Levels.MonsterLevel
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


      36542295960 function calls (35405191969 primitive calls) in 258901.05 seconds

##    Ordered by: cumulative time
   List reduced from 430 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258901.048 258901.048 {built-in method builtins.exec}
                      1    0.361    0.361 258901.048 258901.048 <string>:1(<module>)
                      1 4236.694 4236.694 258900.687 258900.687 optionCritic.py:195(option_critic_run)
        1505720710/372759976 10610.856    0.000 113114.071    0.000 module.py:866(_call_impl)
               40792960 9586.176    0.000 112606.728    0.003 optionCritic.py:143(actor_loss_fn)
              125884526  809.590    0.000 103207.677    0.001 optionCritic.py:70(get_state)
              125884526 2967.903    0.000 99921.162    0.001 container.py:117(forward)
                1274780   10.106    0.000 70626.632    0.055 tensor.py:195(backward)
                1274780   11.217    0.000 70616.288    0.055 __init__.py:68(backward)
                1274780 70573.455    0.055 70573.455    0.055 {method 'run_backward' of 'torch._C._EngineBase' objects}
              251769052  954.204    0.000 59897.901    0.000 conv.py:398(forward)
              251769052  413.698    0.000 58596.626    0.000 conv.py:390(_conv_forward)
              251769052 58182.928    0.000 58182.928    0.000 {built-in method conv2d}
               40792960 4238.137    0.000 25080.501    0.001 optionCritic.py:91(get_action)
              498644502 1731.503    0.000 22859.355    0.000 linear.py:93(forward)
              498644502  628.144    0.000 20471.434    0.000 functional.py:1737(linear)
              498644502 19715.356    0.000 19715.356    0.000 {built-in method torch._C._nn.linear}
               40792960 1266.874    0.000 13740.957    0.000 optionCritic.py:80(predict_option_termination)
                1274780   26.288    0.000 10030.888    0.008 optimizer.py:84(wrapper)
                1274780   13.355    0.000 9926.239    0.008 grad_mode.py:24(decorate_context)
                1274780   83.517    0.000 9886.487    0.008 rmsprop.py:56(step)
                1274780  133.985    0.000 9703.278    0.008 _functional.py:203(rmsprop)
               81585920 1172.944    0.000 9135.593    0.000 distribution.py:34(__init__)
              377653578  472.196    0.000 8600.167    0.000 activation.py:713(forward)
               40792960  646.193    0.000 8187.988    0.000 categorical.py:115(log_prob)
              377653578  470.870    0.000 8127.971    0.000 functional.py:1364(leaky_relu)
               17846914 7828.595    0.000 7828.595    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              377653578 7553.223    0.000 7553.223    0.000 {built-in method torch._C._nn.leaky_relu}
               40792960  949.888    0.000 7400.449    0.000 categorical.py:49(__init__)
              124177875  496.710    0.000 6887.261    0.000 optionCritic.py:77(get_Q)
               81904615  484.042    0.000 5548.398    0.000 optionCritic.py:88(get_terminations)
                 318695   71.769    0.000 5172.073    0.016 optionCritic.py:116(critic_loss_fn)
               40792960  288.809    0.000 4811.348    0.000 bernoulli.py:34(__init__)
               40792960 3050.695    0.000 4621.625    0.000 constraints.py:398(check)
               40792960  505.328    0.000 3445.896    0.000 distribution.py:240(_validate_sample)
                1274780    8.333    0.000 3268.543    0.003 game.py:42(step)
                1274780   12.230    0.000 3167.927    0.002 layers.py:827(step)
              125884526  174.806    0.000 2456.027    0.000 activation.py:101(forward)
               40792960 1176.579    0.000 2427.245    0.000 categorical.py:123(entropy)
               40792960 2327.479    0.000 2327.479    0.000 constraints.py:249(check)
              125884526  160.838    0.000 2281.221    0.000 functional.py:1195(relu)
               40792960 2181.556    0.000 2181.556    0.000 constraints.py:364(check)
              125884526 2087.997    0.000 2087.997    0.000 {built-in method relu}
              122378880  227.372    0.000 2015.923    0.000 utils.py:106(__get__)
              285550720 1939.711    0.000 1939.711    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
             1519743290 1922.511    0.000 1922.511    0.000 {built-in method torch._C._get_tracing_state}
              123016270  194.673    0.000 1816.346    0.000 tensor.py:525(__rsub__)
               40792960  319.075    0.000 1811.060    0.000 bernoulli.py:86(sample)
              122378880 1730.264    0.000 1730.264    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
              125884526  120.403    0.000 1701.201    0.000 flatten.py:39(forward)
             1955338775 1689.025    0.000 1689.152    0.000 module.py:934(__getattr__)
                1274781  140.098    0.000 1615.864    0.001 layers.py:793(update)
               40792960   77.783    0.000 1612.888    0.000 categorical.py:88(logits)
              123016270 1586.040    0.000 1586.040    0.000 {built-in method rsub}
              125884526 1580.799    0.000 1580.799    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              122697575 1567.963    0.000 1567.963    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
               40792960  398.017    0.000 1565.062    0.000 categorical.py:108(sample)
               40792960   84.720    0.000 1535.104    0.000 utils.py:82(probs_to_logits)
                1274780   65.284    0.000 1533.676    0.001 layers.py:17(step)
               40792960  110.942    0.000 1463.522    0.000 layer.py:106(move)
               81585920  409.374    0.000 1307.996    0.000 functional.py:46(broadcast_tensors)
               81904615 1295.721    0.000 1295.721    0.000 {method 'max' of 'torch._C._TensorBase' objects}
              122378880 1194.740    0.000 1194.740    0.000 {method 'all' of 'torch._C._TensorBase' objects}
               22278948  528.540    0.000 1123.902    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
             6509020700 1105.781    0.000 1116.684    0.000 {built-in method builtins.len}
               14022580   38.888    0.000 1052.805    0.000 tensor.py:575(__iter__)
               14022580  983.429    0.000  983.429    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               40792960  141.605    0.000  945.469    0.000 utils.py:77(clamp_probs)
             6148767366  934.638    0.000  934.638    0.000 {method 'values' of 'collections.OrderedDict' objects}
               40792960  197.082    0.000  913.043    0.000 layers.py:844(check)
               40792960  905.935    0.000  905.935    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               40792960  173.373    0.000  883.301    0.000 utils.py:11(broadcast_all)
               17846914  833.206    0.000  833.206    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               40792960  803.864    0.000  803.864    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
              123334965  792.014    0.000  792.014    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               81585920  787.781    0.000  787.781    0.000 {built-in method broadcast_tensors}
                1274780   78.539    0.000  763.188    0.001 replaybuffer.py:34(save_option_critic)
                1161639   19.092    0.000  752.659    0.001 layers.py:849(restart)
               40792960  750.814    0.000  750.814    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
              245395150  699.684    0.000  699.684    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               40792960  683.666    0.000  683.666    0.000 {built-in method clamp}
               81585920  656.233    0.000  656.233    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               41954565  629.468    0.000  629.468    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                1161639    8.849    0.000  609.484    0.001 level.py:8(__init__)
               22278948   36.123    0.000  595.362    0.000 <__array_function__ internals>:2(prod)
               40792960  579.645    0.000  579.645    0.000 {built-in method bernoulli}
                 318695  443.021    0.001  576.297    0.002 replaybuffer.py:42(sample_option_critic)
               22278948   34.786    0.000  551.362    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
               40792960  532.588    0.000  532.588    0.000 {built-in method all}
                1161639   20.960    0.000  531.579    0.000 levels.py:456(generate)
               22278948   55.169    0.000  516.576    0.000 fromnumeric.py:2912(prod)
               40792960  504.915    0.000  504.915    0.000 {built-in method log}
               40792960  502.791    0.000  502.791    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
                5576238   77.504    0.000  489.704    0.000 level.py:41(notUsed)
               22278948  119.972    0.000  461.406    0.000 fromnumeric.py:70(_wrapreduction)
                1274780   75.663    0.000  398.134    0.000 optimizer.py:189(zero_grad)
               40792960  375.544    0.000  375.544    0.000 {built-in method multinomial}
                8923467  225.726    0.000  363.205    0.000 layer.py:175(NoRock_update)
               40792960   91.489    0.000  352.874    0.000 layers.py:838(isFree)
              123543064  330.057    0.000  330.057    0.000 {method 'item' of 'torch._C._TensorBase' objects}


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
Subject: Job 9632757: <Attempt7_Monsters_option_critic_2> in cluster <dcc> Exited

Job <Attempt7_Monsters_option_critic_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed May 12 14:11:14 2021
Job was executed on host(s) <n-62-23-25>, in queue <hpc>, as user <s183914> in cluster <dcc> at Sun May 16 23:16:52 2021
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

    CPU time :                                   258848.17 sec.
    Max Memory :                                 794 MB
    Average Memory :                             781.93 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15590.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   259038 sec.
    Turnaround time :                            637269 sec.

The output (if any) is above this job summary.

