
# Parameters

    Name :                      Attempt2_DoorsAndKey_option_critic-1
    Main :                      option_critic_run
    Level :                     Levels.Causal1
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


      49146710999 function calls (47525185028 primitive calls) in 258900.76 seconds

##    Ordered by: cumulative time
   List reduced from 428 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.757 258900.757 {built-in method builtins.exec}
                      1    0.393    0.393 258900.757 258900.757 <string>:1(<module>)
                      1 6362.379 6362.379 258900.364 258900.364 optionCritic.py:195(option_critic_run)
               57664500 9872.363    0.000 114670.122    0.002 optionCritic.py:143(actor_loss_fn)
        2142135975/528106611 10353.830    0.000 112892.226    0.000 module.py:866(_call_impl)
              179336596  851.949    0.000 105024.382    0.001 optionCritic.py:70(get_state)
              179336596 2307.013    0.000 101600.211    0.001 container.py:117(forward)
                2306580   19.779    0.000 72953.160    0.032 tensor.py:195(backward)
                2306580   24.804    0.000 72933.062    0.032 __init__.py:68(backward)
                2306580 72854.610    0.032 72854.610    0.032 {method 'run_backward' of 'torch._C._EngineBase' objects}
              358673192  992.058    0.000 63247.553    0.000 conv.py:398(forward)
              358673192  579.953    0.000 61845.449    0.000 conv.py:390(_conv_forward)
              358673192 61265.495    0.000 61265.495    0.000 {built-in method conv2d}
              707443207 1663.874    0.000 21954.114    0.000 linear.py:93(forward)
               57664500 3467.532    0.000 20387.146    0.000 optionCritic.py:91(get_action)
              707443207  705.000    0.000 19585.678    0.000 functional.py:1737(linear)
              707443207 18723.287    0.000 18723.287    0.000 {built-in method torch._C._nn.linear}
               57664500 1316.338    0.000 15083.447    0.000 optionCritic.py:80(predict_option_termination)
                2306580   53.472    0.000 8433.682    0.004 optimizer.py:84(wrapper)
                2306580   30.573    0.000 8233.270    0.004 grad_mode.py:24(decorate_context)
              115329000 1306.713    0.000 8230.981    0.000 distribution.py:34(__init__)
                2306580  132.433    0.000 8149.040    0.004 rmsprop.py:56(step)
                2306580  142.882    0.000 7868.093    0.003 _functional.py:203(rmsprop)
              538009788  525.382    0.000 7610.525    0.000 activation.py:713(forward)
              538009788  529.089    0.000 7085.143    0.000 functional.py:1364(leaky_relu)
               57664500  579.903    0.000 6793.465    0.000 categorical.py:115(log_prob)
              538009788 6442.154    0.000 6442.154    0.000 {built-in method torch._C._nn.leaky_relu}
               57664500  519.781    0.000 6158.816    0.000 bernoulli.py:34(__init__)
              175199870  407.842    0.000 5743.821    0.000 optionCritic.py:77(get_Q)
               57664500  778.512    0.000 5705.099    0.000 categorical.py:49(__init__)
                 576645   99.457    0.000 4726.044    0.008 optionCritic.py:116(critic_loss_fn)
              115905645  458.279    0.000 4616.172    0.000 optionCritic.py:88(get_terminations)
               32292114 3906.195    0.000 3906.195    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               57664500 2346.638    0.000 3482.183    0.000 constraints.py:398(check)
                2306580   14.012    0.000 3219.070    0.001 game.py:42(step)
                2306580   22.036    0.000 3083.338    0.001 layers.py:827(step)
               57664500  477.521    0.000 2763.427    0.000 distribution.py:240(_validate_sample)
               32292114 2709.596    0.000 2709.596    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               57664500 2245.805    0.000 2245.805    0.000 constraints.py:364(check)
               57664500  466.972    0.000 2224.975    0.000 bernoulli.py:86(sample)
              179336596  227.517    0.000 2105.610    0.000 activation.py:101(forward)
              179336596  206.301    0.000 1878.094    0.000 functional.py:1195(relu)
               57664500  979.709    0.000 1874.256    0.000 categorical.py:123(entropy)
             2775968314 1856.228    0.000 1856.400    0.000 module.py:934(__getattr__)
               57664500 1795.232    0.000 1795.232    0.000 constraints.py:249(check)
              403651500 1741.322    0.000 1741.322    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              179336596  187.118    0.000 1690.650    0.000 flatten.py:39(forward)
              172993500  236.943    0.000 1677.854    0.000 utils.py:106(__get__)
              174146790  203.249    0.000 1650.484    0.000 tensor.py:525(__rsub__)
              179336596 1640.296    0.000 1640.296    0.000 {built-in method relu}
              115329000  563.970    0.000 1589.874    0.000 functional.py:46(broadcast_tensors)
                2306580   87.242    0.000 1557.107    0.001 layers.py:17(step)
              179336596 1503.532    0.000 1503.532    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                2306581  197.162    0.000 1495.592    0.001 layers.py:793(update)
               25372380   61.741    0.000 1484.579    0.000 tensor.py:575(__iter__)
               57664500  148.771    0.000 1462.395    0.000 layer.py:106(move)
               57664500  326.995    0.000 1437.750    0.000 utils.py:11(broadcast_all)
              174146790 1416.967    0.000 1416.967    0.000 {built-in method rsub}
               25372380 1387.457    0.000 1387.457    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
                 576645 1140.837    0.002 1372.927    0.002 replaybuffer.py:42(sample_option_critic)
               57664500  385.311    0.000 1349.623    0.000 categorical.py:108(sample)
             2167508355 1333.212    0.000 1333.212    0.000 {built-in method torch._C._get_tracing_state}
              115905645 1325.505    0.000 1325.505    0.000 {method 'max' of 'torch._C._TensorBase' objects}
              173570145 1282.495    0.000 1282.495    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
               57664500   70.003    0.000 1266.209    0.000 categorical.py:88(logits)
               57664500   72.296    0.000 1196.206    0.000 utils.py:82(probs_to_logits)
              172993500 1186.583    0.000 1186.583    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
             9205833995 1147.987    0.000 1164.142    0.000 {built-in method builtins.len}
             8747880496 1032.849    0.000 1032.849    0.000 {method 'values' of 'collections.OrderedDict' objects}
              172993500 1023.357    0.000 1023.357    0.000 {method 'all' of 'torch._C._TensorBase' objects}
               57664500  869.392    0.000  869.392    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
              115329000  861.975    0.000  861.975    0.000 {built-in method broadcast_tensors}
                2306580   84.548    0.000  771.896    0.000 replaybuffer.py:34(save_option_critic)
                2306580  111.330    0.000  722.601    0.000 optimizer.py:189(zero_grad)
               57664500  210.641    0.000  700.331    0.000 layers.py:844(check)
               57664500  147.413    0.000  693.657    0.000 utils.py:77(clamp_probs)
              174723435  664.135    0.000  664.135    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               57664500  662.745    0.000  662.745    0.000 {built-in method bernoulli}
               57664500  582.961    0.000  582.961    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
              347140290  552.703    0.000  552.703    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               58717580  549.982    0.000  549.982    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               57664500  546.244    0.000  546.244    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
                1053104   14.553    0.000  515.755    0.000 layers.py:849(restart)
              115329000  501.153    0.000  501.153    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               57664500   90.960    0.000  497.810    0.000 layers.py:838(isFree)
               57664500  473.274    0.000  473.274    0.000 {built-in method clamp}
              761529838  291.181    0.000  471.991    0.000 {built-in method builtins.isinstance}
              174051216  469.110    0.000  469.110    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               32292114  442.720    0.000  442.720    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               57664500  430.253    0.000  430.253    0.000 {built-in method log}
               15569419  429.403    0.000  429.403    0.000 {built-in method tensor}
               57664500  412.084    0.000  412.084    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
              179336610  409.853    0.000  409.853    0.000 {method 'to' of 'torch._C._TensorBase' objects}
              268193608  344.767    0.000  406.849    0.000 layer.py:103(isFree)
                1053104    8.019    0.000  404.456    0.000 level.py:8(__init__)
               13839486  248.331    0.000  403.551    0.000 layer.py:175(NoRock_update)
               32292114  393.167    0.000  393.167    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               57664500  375.690    0.000  375.690    0.000 {built-in method all}
               57664500  344.085    0.000  344.085    0.000 {built-in method multinomial}
                1053104   17.700    0.000  338.925    0.000 levels.py:122(generate)


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
Subject: Job 9606144: <Attempt2_DoorsAndKey_option_critic_1> in cluster <dcc> Exited

Job <Attempt2_DoorsAndKey_option_critic_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon May  3 01:33:13 2021
Job was executed on host(s) <n-62-11-66>, in queue <hpc>, as user <s183914> in cluster <dcc> at Mon May  3 01:33:14 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon May  3 01:33:14 2021
Terminated at Thu May  6 01:28:34 2021
Results reported at Thu May  6 01:28:34 2021

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

    CPU time :                                   258288.23 sec.
    Max Memory :                                 786 MB
    Average Memory :                             763.92 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15598.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258950 sec.
    Turnaround time :                            258921 sec.

The output (if any) is above this job summary.

