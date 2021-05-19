
# Parameters

    Name :                      Attempt7_Lights1_option_critic-1
    Main :                      option_critic_run
    Level :                     Levels.Causal3
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


      54130066657 function calls (52493527104 primitive calls) in 258900.87 seconds

##    Ordered by: cumulative time
   List reduced from 434 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.872 258900.872 {built-in method builtins.exec}
                      1    0.335    0.335 258900.872 258900.872 <string>:1(<module>)
                      1 6123.072 6123.072 258900.537 258900.537 optionCritic.py:195(option_critic_run)
               58709920 9124.705    0.000 118401.738    0.002 optionCritic.py:143(actor_loss_fn)
        2169301951/538725655 10827.558    0.000 116897.734    0.000 module.py:866(_call_impl)
              181175144  851.824    0.000 108420.839    0.001 optionCritic.py:70(get_state)
              181175144 2380.425    0.000 104925.412    0.001 container.py:117(forward)
              362350288 1058.589    0.000 66641.546    0.000 conv.py:398(forward)
                1834685   16.624    0.000 65434.973    0.036 tensor.py:195(backward)
                1834685   21.027    0.000 65418.049    0.036 __init__.py:68(backward)
                1834685 65354.336    0.036 65354.336    0.036 {method 'run_backward' of 'torch._C._EngineBase' objects}
              362350288  544.557    0.000 65155.557    0.000 conv.py:390(_conv_forward)
              362350288 64610.999    0.000 64610.999    0.000 {built-in method conv2d}
               58709920 3843.273    0.000 22975.150    0.000 optionCritic.py:91(get_action)
              719900799 1831.063    0.000 21598.663    0.000 linear.py:93(forward)
              719900799  693.238    0.000 19040.279    0.000 functional.py:1737(linear)
              719900799 18171.496    0.000 18171.496    0.000 {built-in method torch._C._nn.linear}
               58709920 1274.167    0.000 15166.090    0.000 optionCritic.py:80(predict_option_termination)
              117419840 1332.780    0.000 8782.023    0.000 distribution.py:34(__init__)
                1834685   43.537    0.000 8322.824    0.005 optimizer.py:84(wrapper)
                1834685   24.153    0.000 8149.494    0.004 grad_mode.py:24(decorate_context)
                1834685  121.577    0.000 8080.989    0.004 rmsprop.py:56(step)
                1834685  113.248    0.000 7822.781    0.004 _functional.py:203(rmsprop)
               58709920  635.585    0.000 7601.430    0.000 categorical.py:115(log_prob)
              543525432  569.084    0.000 7555.906    0.000 activation.py:713(forward)
              543525432  554.401    0.000 6986.821    0.000 functional.py:1364(leaky_relu)
               58709920  878.386    0.000 6453.925    0.000 categorical.py:49(__init__)
              543525432 6310.578    0.000 6310.578    0.000 {built-in method torch._C._nn.leaky_relu}
              180962080  435.058    0.000 6245.313    0.000 optionCritic.py:77(get_Q)
               58709920  463.558    0.000 5907.010    0.000 bernoulli.py:34(__init__)
                1834685   10.745    0.000 5793.920    0.003 game.py:42(step)
                1834685   18.878    0.000 5652.019    0.003 layers.py:827(step)
              117878511  433.826    0.000 4725.558    0.000 optionCritic.py:88(get_terminations)
               25685584 4154.589    0.000 4154.589    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                 458671   81.443    0.000 3995.471    0.009 optionCritic.py:116(critic_loss_fn)
               58709920 2628.974    0.000 3909.116    0.000 constraints.py:398(check)
                1834686  193.428    0.000 3313.906    0.002 layers.py:793(update)
               58709920  551.834    0.000 3081.371    0.000 distribution.py:240(_validate_sample)
               25685584 2761.018    0.000 2761.018    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                1834685   87.630    0.000 2310.631    0.001 layers.py:17(step)
               58709920  457.743    0.000 2289.076    0.000 bernoulli.py:86(sample)
               58709920 2275.174    0.000 2275.174    0.000 constraints.py:364(check)
              181175144  241.277    0.000 2218.282    0.000 activation.py:101(forward)
               58709920  147.075    0.000 2214.925    0.000 layer.py:106(move)
               58709920 1107.324    0.000 2118.942    0.000 categorical.py:123(entropy)
             2820886240 1981.665    0.000 1981.814    0.000 module.py:934(__getattr__)
              181175144  203.291    0.000 1977.005    0.000 functional.py:1195(relu)
               58709920 1964.572    0.000 1964.572    0.000 constraints.py:249(check)
              176129760  256.916    0.000 1902.748    0.000 utils.py:106(__get__)
                3915014   60.486    0.000 1864.177    0.000 layers.py:849(restart)
              410969440 1826.764    0.000 1826.764    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              181175144  181.625    0.000 1755.742    0.000 flatten.py:39(forward)
              181175144 1740.981    0.000 1740.981    0.000 {built-in method relu}
              177047102  199.636    0.000 1681.880    0.000 tensor.py:525(__rsub__)
              117419840  574.894    0.000 1650.650    0.000 functional.py:46(broadcast_tensors)
              181175144 1574.117    0.000 1574.117    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               58709920  416.939    0.000 1523.933    0.000 categorical.py:108(sample)
               58709920  326.946    0.000 1464.414    0.000 layers.py:844(check)
              177047102 1448.695    0.000 1448.695    0.000 {built-in method rsub}
               58709920   74.770    0.000 1440.844    0.000 categorical.py:88(logits)
             2189483486 1425.890    0.000 1425.890    0.000 {built-in method torch._C._get_tracing_state}
              117878511 1375.622    0.000 1375.622    0.000 {method 'max' of 'torch._C._TensorBase' objects}
               58709920   84.743    0.000 1366.074    0.000 utils.py:82(probs_to_logits)
               20181535   50.721    0.000 1363.272    0.000 tensor.py:575(__iter__)
              176129760 1342.674    0.000 1342.674    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                3915014   29.525    0.000 1339.358    0.000 level.py:8(__init__)
               58709920  263.031    0.000 1332.609    0.000 utils.py:11(broadcast_all)
              176588431 1320.216    0.000 1320.216    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
             9421789122 1287.731    0.000 1302.226    0.000 {built-in method builtins.len}
               20181535 1278.521    0.000 1278.521    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
              176129760 1119.956    0.000 1119.956    0.000 {method 'all' of 'torch._C._TensorBase' objects}
             8858382948 1102.577    0.000 1102.577    0.000 {method 'values' of 'collections.OrderedDict' objects}
                3915014  118.652    0.000 1081.395    0.000 levels.py:164(generate)
               58709920 1048.116    0.000 1048.116    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
                 458671  741.430    0.002  925.072    0.002 replaybuffer.py:42(sample_option_critic)
              117419840  910.393    0.000  910.393    0.000 {built-in method broadcast_tensors}
               58709920  161.372    0.000  803.489    0.000 utils.py:77(clamp_probs)
                1834685   92.092    0.000  801.100    0.000 replaybuffer.py:34(save_option_critic)
                7830028  109.784    0.000  800.046    0.000 level.py:41(notUsed)
               58709920  737.399    0.000  737.399    0.000 {built-in method bernoulli}
              177505773  715.853    0.000  715.853    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               14677488  409.853    0.000  657.183    0.000 layer.py:175(NoRock_update)
               58709920  644.789    0.000  644.789    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
               58709920  642.117    0.000  642.117    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
               62624898  642.109    0.000  642.109    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
              353176862  578.488    0.000  578.488    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
              117419840  569.100    0.000  569.100    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               58709920  534.195    0.000  534.195    0.000 {built-in method clamp}
                1834685   93.830    0.000  527.001    0.000 optimizer.py:189(zero_grad)
               58709920   89.582    0.000  526.796    0.000 layers.py:838(isFree)
             1430385417  357.352    0.000  518.102    0.000 enum.py:646(__hash__)
               58709920  477.842    0.000  477.842    0.000 {built-in method log}
               58709920  464.348    0.000  464.348    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
               31320112   57.848    0.000  448.991    0.000 layer.py:77(restart)
              231863777  360.000    0.000  437.215    0.000 layer.py:103(isFree)
              176129792  142.482    0.000  436.896    0.000 {built-in method builtins.all}
               58709920  432.765    0.000  432.765    0.000 {built-in method all}
              788347929  275.197    0.000  428.342    0.000 {built-in method builtins.isinstance}
              181175158  400.215    0.000  400.215    0.000 {method 'to' of 'torch._C._TensorBase' objects}
               12384127  399.054    0.000  399.054    0.000 {built-in method tensor}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9632732: <Attempt7_Lights1_option_critic_1> in cluster <dcc> Done

Job <Attempt7_Lights1_option_critic_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed May 12 14:11:10 2021
Job was executed on host(s) <n-62-31-1>, in queue <hpc>, as user <s183914> in cluster <dcc> at Sun May 16 23:16:53 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun May 16 23:16:53 2021
Terminated at Wed May 19 23:12:24 2021
Results reported at Wed May 19 23:12:24 2021

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

    CPU time :                                   258290.17 sec.
    Max Memory :                                 945 MB
    Average Memory :                             929.21 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15439.00 MB
    Max Swap :                                   -
    Max Processes :                              5
    Max Threads :                                6
    Run time :                                   258995 sec.
    Turnaround time :                            637274 sec.

The output (if any) is above this job summary.

