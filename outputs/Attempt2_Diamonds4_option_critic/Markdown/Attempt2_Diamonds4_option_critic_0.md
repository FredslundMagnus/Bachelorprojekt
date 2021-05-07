
# Parameters

    Name :                      Attempt2_Diamonds4_option_critic-0
    Main :                      option_critic_run
    Level :                     Levels.Causal7
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


      54499058975 function calls (52769920893 primitive calls) in 258900.59 seconds

##    Ordered by: cumulative time
   List reduced from 429 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.586 258900.586 {built-in method builtins.exec}
                      1    0.298    0.298 258900.586 258900.586 <string>:1(<module>)
                      1 5730.383 5730.383 258900.288 258900.288 optionCritic.py:195(option_critic_run)
               61491375 9847.426    0.000 115458.611    0.002 optionCritic.py:143(actor_loss_fn)
        2284402815/563259240 10786.017    0.000 113706.642    0.000 module.py:866(_call_impl)
              191238175  897.833    0.000 105601.787    0.001 optionCritic.py:70(get_state)
              191238175 2481.162    0.000 102029.523    0.001 container.py:117(forward)
                2459655   19.524    0.000 71339.363    0.029 tensor.py:195(backward)
                2459655   24.611    0.000 71319.501    0.029 __init__.py:68(backward)
                2459655 71242.116    0.029 71242.116    0.029 {method 'run_backward' of 'torch._C._EngineBase' objects}
              382476350 1048.461    0.000 63845.444    0.000 conv.py:398(forward)
              382476350  538.856    0.000 62377.323    0.000 conv.py:390(_conv_forward)
              382476350 61838.467    0.000 61838.467    0.000 {built-in method conv2d}
              754497415 1769.386    0.000 21290.408    0.000 linear.py:93(forward)
               61491375 3570.025    0.000 21166.887    0.000 optionCritic.py:91(get_action)
              754497415  709.300    0.000 18814.703    0.000 functional.py:1737(linear)
              754497415 17944.110    0.000 17944.110    0.000 {built-in method torch._C._nn.linear}
               61491375 1264.330    0.000 14832.411    0.000 optionCritic.py:80(predict_option_termination)
                2459655   50.483    0.000 9080.102    0.004 optimizer.py:84(wrapper)
                2459655   29.011    0.000 8888.372    0.004 grad_mode.py:24(decorate_context)
                2459655  131.412    0.000 8808.334    0.004 rmsprop.py:56(step)
                2459655  136.220    0.000 8524.428    0.003 _functional.py:203(rmsprop)
              122982750 1262.932    0.000 8256.665    0.000 distribution.py:34(__init__)
              573714525  550.503    0.000 7664.667    0.000 activation.py:713(forward)
              573714525  593.743    0.000 7114.164    0.000 functional.py:1364(leaky_relu)
               61491375  603.060    0.000 7095.815    0.000 categorical.py:115(log_prob)
              573714525 6399.887    0.000 6399.887    0.000 {built-in method torch._C._nn.leaky_relu}
              186932027  407.820    0.000 5949.809    0.000 optionCritic.py:77(get_Q)
               61491375  796.022    0.000 5919.055    0.000 categorical.py:49(__init__)
               61491375  439.997    0.000 5750.172    0.000 bernoulli.py:34(__init__)
                 614913   94.370    0.000 4665.703    0.008 optionCritic.py:116(critic_loss_fn)
              123597663  422.123    0.000 4625.184    0.000 optionCritic.py:88(get_terminations)
               34435164 4426.519    0.000 4426.519    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                2459655   12.355    0.000 4026.799    0.002 game.py:42(step)
                2459655   21.890    0.000 3890.541    0.002 layers.py:827(step)
               61491375 2430.521    0.000 3608.343    0.000 constraints.py:398(check)
               34435164 3032.941    0.000 3032.941    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               61491375  507.448    0.000 2904.856    0.000 distribution.py:240(_validate_sample)
               61491375 2202.717    0.000 2202.717    0.000 constraints.py:364(check)
               61491375  437.668    0.000 2179.368    0.000 bernoulli.py:86(sample)
              191238175  243.438    0.000 2162.796    0.000 activation.py:101(forward)
                2459655   85.953    0.000 2109.171    0.001 layers.py:17(step)
               61491375  155.416    0.000 2015.569    0.000 layer.py:106(move)
               61491375 1015.936    0.000 1965.340    0.000 categorical.py:123(entropy)
              191238175  210.111    0.000 1919.358    0.000 functional.py:1195(relu)
             2960509341 1889.208    0.000 1889.384    0.000 module.py:934(__getattr__)
               61491375 1873.397    0.000 1873.397    0.000 constraints.py:249(check)
              430439625 1780.076    0.000 1780.076    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              184474125  243.288    0.000 1759.622    0.000 utils.py:106(__get__)
                2459656  194.215    0.000 1751.219    0.001 layers.py:793(update)
              191238175  177.037    0.000 1704.124    0.000 flatten.py:39(forward)
              191238175 1675.976    0.000 1675.976    0.000 {built-in method relu}
              185703951  206.348    0.000 1668.494    0.000 tensor.py:525(__rsub__)
              122982750  524.121    0.000 1530.259    0.000 functional.py:46(broadcast_tensors)
              191238175 1527.086    0.000 1527.086    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              185703951 1432.859    0.000 1432.859    0.000 {built-in method rsub}
               61491375  387.580    0.000 1400.109    0.000 categorical.py:108(sample)
               27056205   59.551    0.000 1367.247    0.000 tensor.py:575(__iter__)
              123597663 1340.643    0.000 1340.643    0.000 {method 'max' of 'torch._C._TensorBase' objects}
               61491375   73.106    0.000 1332.080    0.000 categorical.py:88(logits)
             2311459020 1331.056    0.000 1331.056    0.000 {built-in method torch._C._get_tracing_state}
               61491375  272.408    0.000 1297.149    0.000 utils.py:11(broadcast_all)
              185089038 1281.287    0.000 1281.287    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
               27056205 1271.086    0.000 1271.086    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               61491375   77.807    0.000 1258.974    0.000 utils.py:82(probs_to_logits)
             9882512953 1236.268    0.000 1252.869    0.000 {built-in method builtins.len}
              184474125 1237.922    0.000 1237.922    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
               61491375  263.221    0.000 1206.995    0.000 layers.py:844(check)
                 614913  947.172    0.002 1165.611    0.002 replaybuffer.py:42(sample_option_critic)
             9328849435 1094.334    0.000 1094.334    0.000 {method 'values' of 'collections.OrderedDict' objects}
              184474125 1041.835    0.000 1041.835    0.000 {method 'all' of 'torch._C._TensorBase' objects}
               61491375  871.840    0.000  871.840    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
              122982750  848.838    0.000  848.838    0.000 {built-in method broadcast_tensors}
                2459655   85.488    0.000  741.497    0.000 replaybuffer.py:34(save_option_critic)
               61491375  156.533    0.000  733.659    0.000 utils.py:77(clamp_probs)
              186318864  678.334    0.000  678.334    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               61491375  672.101    0.000  672.101    0.000 {built-in method bernoulli}
                1228102   16.527    0.000  660.598    0.001 layers.py:849(restart)
                2459655  109.052    0.000  636.070    0.000 optimizer.py:189(zero_grad)
               61491375  616.773    0.000  616.773    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
               62719451  592.263    0.000  592.263    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               61491375  577.125    0.000  577.125    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
              370178076  557.219    0.000  557.219    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                1228102    8.738    0.000  533.660    0.000 level.py:8(__init__)
               61491375  124.797    0.000  532.646    0.000 layers.py:838(isFree)
              122982750  527.372    0.000  527.372    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               61491375  505.587    0.000  505.587    0.000 {built-in method clamp}
                1228102   19.308    0.000  460.222    0.000 levels.py:456(generate)
               17217592  277.496    0.000  455.668    0.000 layer.py:175(NoRock_update)
               61491375  447.509    0.000  447.509    0.000 {built-in method log}
              812068461  265.160    0.000  428.674    0.000 {built-in method builtins.isinstance}
                5895058   74.610    0.000  420.896    0.000 level.py:41(notUsed)
               61491375  420.222    0.000  420.222    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
              191238189  419.737    0.000  419.737    0.000 {method 'to' of 'torch._C._TensorBase' objects}
              185707143  414.224    0.000  414.224    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               16602673  410.106    0.000  410.106    0.000 {built-in method tensor}
              409100255  341.739    0.000  407.849    0.000 layer.py:103(isFree)
               61491375  398.772    0.000  398.772    0.000 {built-in method all}
               61491375  359.861    0.000  359.861    0.000 {built-in method multinomial}
             1052523753  233.546    0.000  350.727    0.000 enum.py:646(__hash__)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9606125: <Attempt2_Diamonds4_option_critic_0> in cluster <dcc> Done

Job <Attempt2_Diamonds4_option_critic_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon May  3 01:33:09 2021
Job was executed on host(s) <n-62-11-60>, in queue <hpc>, as user <s183914> in cluster <dcc> at Mon May  3 01:33:11 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon May  3 01:33:11 2021
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

Successfully completed.

Resource usage summary:

    CPU time :                                   258289.66 sec.
    Max Memory :                                 869 MB
    Average Memory :                             845.26 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15515.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258943 sec.
    Turnaround time :                            258919 sec.

The output (if any) is above this job summary.

