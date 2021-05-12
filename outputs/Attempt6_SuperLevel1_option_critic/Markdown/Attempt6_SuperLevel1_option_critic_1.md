
# Parameters

    Name :                      Attempt6_SuperLevel1_option_critic-1
    Main :                      option_critic_run
    Level :                     Levels.SuperLevel
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


      35305614563 function calls (34280198755 primitive calls) in 258900.76 seconds

##    Ordered by: cumulative time
   List reduced from 444 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.756 258900.756 {built-in method builtins.exec}
                      1    0.359    0.359 258900.756 258900.756 <string>:1(<module>)
                      1 3879.344 3879.344 258900.397 258900.397 optionCritic.py:195(option_critic_run)
                1149569    9.465    0.000 136151.293    0.118 tensor.py:195(backward)
                1149569   13.103    0.000 136141.666    0.118 __init__.py:68(backward)
                1149569 136103.194    0.118 136103.194    0.118 {method 'run_backward' of 'torch._C._EngineBase' objects}
        1358517857/336838406 6461.428    0.000 75753.643    0.000 module.py:866(_call_impl)
               36786208 5431.743    0.000 74899.883    0.002 optionCritic.py:143(actor_loss_fn)
              113519939  527.089    0.000 70747.664    0.001 optionCritic.py:70(get_state)
              113519939 1540.963    0.000 68653.636    0.001 container.py:117(forward)
              227039878  601.792    0.000 43317.045    0.000 conv.py:398(forward)
              227039878  336.281    0.000 42471.941    0.000 conv.py:390(_conv_forward)
              227039878 42135.660    0.000 42135.660    0.000 {built-in method conv2d}
              450358345 1039.853    0.000 15054.842    0.000 linear.py:93(forward)
              450358345  423.332    0.000 13576.237    0.000 functional.py:1737(linear)
              450358345 13055.288    0.000 13055.288    0.000 {built-in method torch._C._nn.linear}
               36786208 2153.049    0.000 12796.879    0.000 optionCritic.py:91(get_action)
               36786208  772.605    0.000 9049.302    0.000 optionCritic.py:80(predict_option_termination)
                1149569   26.583    0.000 5961.682    0.005 optimizer.py:84(wrapper)
                1149569   15.121    0.000 5862.236    0.005 grad_mode.py:24(decorate_context)
                1149569   72.639    0.000 5819.767    0.005 adam.py:55(step)
                1149569  436.696    0.000 5671.144    0.005 _functional.py:53(adam)
               73572416  787.986    0.000 5063.794    0.000 distribution.py:34(__init__)
              340559817  345.243    0.000 4774.597    0.000 activation.py:713(forward)
              340559817  356.323    0.000 4429.354    0.000 functional.py:1364(leaky_relu)
               36786208  358.452    0.000 4244.845    0.000 categorical.py:115(log_prob)
                1149569    6.423    0.000 4148.943    0.004 game.py:42(step)
                1149569   10.615    0.000 4051.635    0.004 layers.py:827(step)
              340559817 3992.000    0.000 3992.000    0.000 {built-in method torch._C._nn.leaky_relu}
              112672451  253.241    0.000 3686.846    0.000 optionCritic.py:77(get_Q)
               36786208  488.675    0.000 3600.145    0.000 categorical.py:49(__init__)
               36786208  291.877    0.000 3573.056    0.000 bernoulli.py:34(__init__)
                 287392   48.910    0.000 3089.030    0.011 optionCritic.py:116(critic_loss_fn)
               73859808  258.780    0.000 2842.438    0.000 optionCritic.py:88(get_terminations)
                1149569   55.448    0.000 2590.790    0.002 layers.py:17(step)
               36786208  160.737    0.000 2530.961    0.000 layer.py:106(move)
               36786208 1476.541    0.000 2188.671    0.000 constraints.py:398(check)
               36786208  329.351    0.000 1929.278    0.000 layers.py:844(check)
               36786208  296.516    0.000 1722.807    0.000 distribution.py:240(_validate_sample)
                1149570  106.871    0.000 1444.893    0.001 layers.py:793(update)
               36786208 1351.791    0.000 1351.791    0.000 constraints.py:364(check)
               36786208  266.119    0.000 1341.720    0.000 bernoulli.py:86(sample)
              113519939  140.353    0.000 1326.028    0.000 activation.py:101(forward)
               32187920 1229.890    0.000 1229.890    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              113519939  133.343    0.000 1185.675    0.000 functional.py:1195(relu)
               36786208  612.956    0.000 1181.302    0.000 categorical.py:123(entropy)
             1765356763 1160.914    0.000 1160.997    0.000 module.py:934(__getattr__)
               36786208 1121.065    0.000 1121.065    0.000 constraints.py:249(check)
              110358624  143.326    0.000 1066.747    0.000 utils.py:106(__get__)
              113519939  106.311    0.000 1040.709    0.000 flatten.py:39(forward)
              257503456 1040.609    0.000 1040.609    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              113519939 1032.770    0.000 1032.770    0.000 {built-in method relu}
               16093960 1031.500    0.000 1031.500    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              110933408  124.274    0.000 1026.914    0.000 tensor.py:525(__rsub__)
               16093960 1019.156    0.000 1019.156    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               73572416  332.779    0.000  936.177    0.000 functional.py:46(broadcast_tensors)
              113519939  934.398    0.000  934.398    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              110933408  884.041    0.000  884.041    0.000 {built-in method rsub}
               36786208  224.379    0.000  830.831    0.000 categorical.py:108(sample)
               12645259   29.936    0.000  818.490    0.000 tensor.py:575(__iter__)
               73859808  810.541    0.000  810.541    0.000 {method 'max' of 'torch._C._TensorBase' objects}
               36786208   41.060    0.000  810.394    0.000 categorical.py:88(logits)
              110646016  809.333    0.000  809.333    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
             1371163116  805.865    0.000  805.865    0.000 {built-in method torch._C._get_tracing_state}
               36786208  173.930    0.000  801.911    0.000 utils.py:11(broadcast_all)
               12645259  769.642    0.000  769.642    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               36786208   45.734    0.000  769.333    0.000 utils.py:82(probs_to_logits)
             6043069402  742.132    0.000  750.895    0.000 {built-in method builtins.len}
              110358624  750.162    0.000  750.162    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
               16093960  657.951    0.000  657.951    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                 287392  526.825    0.002  652.113    0.002 replaybuffer.py:42(sample_option_critic)
               16093960  645.133    0.000  645.133    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               32187920  644.262    0.000  644.262    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              110358624  630.012    0.000  630.012    0.000 {method 'all' of 'torch._C._TensorBase' objects}
             5547591367  628.742    0.000  628.742    0.000 {method 'values' of 'collections.OrderedDict' objects}
               36786208  573.588    0.000  573.588    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               14944410  350.217    0.000  550.214    0.000 layer.py:159(update)
               73572416  507.726    0.000  507.726    0.000 {built-in method broadcast_tensors}
                1149569   54.014    0.000  481.746    0.000 replaybuffer.py:34(save_option_critic)
               36786208  354.318    0.000  477.672    0.000 layers.py:471(check)
               36786208   98.521    0.000  459.520    0.000 utils.py:77(clamp_probs)
                1739076   33.991    0.000  425.197    0.000 layers.py:849(restart)
               36786208  411.568    0.000  411.568    0.000 {built-in method bernoulli}
              111220800  406.307    0.000  406.307    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
             1220712200  265.922    0.000  379.211    0.000 enum.py:646(__hash__)
               38525251  369.843    0.000  369.843    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               36786208   66.678    0.000  369.531    0.000 layers.py:838(isFree)
               36786208  360.998    0.000  360.998    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
               36786208  358.650    0.000  358.650    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
                1149569   55.266    0.000  348.442    0.000 optimizer.py:189(zero_grad)
              221292032  338.493    0.000  338.493    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               73572416  311.413    0.000  311.413    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
              205401686  252.423    0.000  302.852    0.000 layer.py:103(isFree)
               36786208  300.690    0.000  300.690    0.000 {built-in method clamp}
                4790054  140.284    0.000  290.618    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                7759594  275.001    0.000  275.001    0.000 {built-in method tensor}
               36786208  196.192    0.000  270.013    0.000 layers.py:77(check)
               36786208  264.080    0.000  264.080    0.000 {built-in method log}
               36786208  261.249    0.000  261.249    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
               35047164   55.785    0.000  250.914    0.000 {built-in method builtins.any}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9624160: <Attempt6_SuperLevel1_option_critic_1> in cluster <dcc> Done

Job <Attempt6_SuperLevel1_option_critic_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun May  9 01:22:27 2021
Job was executed on host(s) <n-62-11-63>, in queue <hpc>, as user <s183914> in cluster <dcc> at Sun May  9 01:22:28 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun May  9 01:22:28 2021
Terminated at Wed May 12 01:17:35 2021
Results reported at Wed May 12 01:17:35 2021

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

    CPU time :                                   258268.28 sec.
    Max Memory :                                 1311 MB
    Average Memory :                             1283.64 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15073.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258957 sec.
    Turnaround time :                            258908 sec.

The output (if any) is above this job summary.

