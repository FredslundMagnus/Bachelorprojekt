
# Parameters

    Name :                      Causal4_Cf_convert5_TopN3-0
    Main :                      CFagent
    Level :                     Levels.Causal4
    Failed actions chance :     0.0
    Hours :                     24.0
    Batch :                     100
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
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                5
    Counterfacts :              1
    Topn :                      3
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      67467941863 function calls (67179201788 primitive calls) in 86110.83 seconds

##    Ordered by: cumulative time
   List reduced from 514 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86110.832 86110.832 {built-in method builtins.exec}
                      1    5.211    5.211 86110.832 86110.832 <string>:1(<module>)
                      1  436.082  436.082 86105.621 86105.621 main.py:79(CFagent)
                9488106   50.731    0.000 25254.649    0.003 agent.py:29(learn)
                3162702   18.235    0.000 21636.773    0.007 game.py:41(step)
                3162702   23.232    0.000 20811.048    0.007 layers.py:718(step)
                9488105  659.159    0.000 20278.365    0.002 learner.py:42(Qlearn)
                3162702  327.381    0.000 13716.501    0.004 layers.py:17(step)
              316025383  986.315    0.000 13360.592    0.000 layer.py:98(move)
        323342255/34603871 1479.869    0.000 11424.398    0.000 module.py:866(_call_impl)
               25115766   87.189    0.000 10602.880    0.000 network.py:27(forward)
               25115766  369.012    0.000 10317.746    0.000 container.py:117(forward)
                3162702  409.087    0.000 9842.565    0.003 agent.py:54(_learn)
                3162702  795.038    0.000 9781.104    0.003 agent.py:210(counterfact)
                3162702  399.709    0.000 8887.909    0.003 agent.py:202(_learn)
                3162702 7179.945    0.002 8298.721    0.003 replaybuffer.py:22(sample_data)
              316025383 1548.893    0.000 8119.761    0.000 layers.py:735(check)
                3162702 6708.042    0.002 7762.368    0.002 replaybuffer.py:67(sample_data)
                9488105  107.340    0.000 7698.166    0.001 optimizer.py:84(wrapper)
                9488105   56.725    0.000 7263.835    0.001 grad_mode.py:24(decorate_context)
                9488105  341.649    0.000 7084.810    0.001 adam.py:55(step)
                3162703  491.653    0.000 7034.953    0.002 layers.py:684(update)
                3162702  114.484    0.000 6449.043    0.002 agent.py:117(_learn)
                9488105 1472.528    0.000 6391.108    0.001 _functional.py:53(adam)
                7807243  267.259    0.000 5600.733    0.001 agent.py:49(__call__)
                9488105   47.002    0.000 5410.507    0.001 tensor.py:195(backward)
                9488105   52.118    0.000 5362.081    0.001 __init__.py:68(backward)
               49441458 5295.378    0.000 5295.378    0.000 {built-in method tensor}
               42145748   29.762    0.000 5100.317    0.000 game.py:37(board)
                9488105 5083.600    0.001 5083.600    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               63254050 2913.382    0.000 5005.446    0.000 layer.py:151(update)
               50231532  123.726    0.000 3841.409    0.000 conv.py:398(forward)
                3162702 1575.666    0.000 3762.037    0.001 agent.py:88(interveen)
               50231532   86.365    0.000 3654.507    0.000 conv.py:390(_conv_forward)
              316025383  658.858    0.000 3575.550    0.000 layers.py:729(isFree)
               50231532 3568.142    0.000 3568.142    0.000 {built-in method conv2d}
                3162702 1759.843    0.001 3047.363    0.001 replaybuffer.py:28(teleporter_save_data)
             2725704897 2462.653    0.000 2916.692    0.000 layer.py:95(isFree)
               69021894  147.021    0.000 2873.860    0.000 linear.py:93(forward)
               69021894   65.659    0.000 2644.208    0.000 functional.py:1737(linear)
               69021894 2563.766    0.000 2563.766    0.000 {built-in method torch._C._nn.linear}
                3162702 1653.384    0.001 2559.573    0.001 agent.py:67(modify)
                1495015   35.650    0.000 2099.008    0.001 agent.py:175(choose_action)
               42596960 1757.108    0.000 1757.108    0.000 {built-in method cat}
               10969945   89.887    0.000 1610.549    0.000 agent.py:59(modify_board)
             5852300703 1088.782    0.000 1576.380    0.000 enum.py:646(__hash__)
                3162701   70.914    0.000 1572.816    0.000 agent.py:171(__call__)
               94137660   92.767    0.000 1497.595    0.000 activation.py:713(forward)
              316734693  337.348    0.000 1466.256    0.000 {built-in method builtins.any}
                3162702   67.224    0.000 1409.610    0.000 agent.py:112(__call__)
               94137660   83.458    0.000 1404.828    0.000 functional.py:1364(leaky_relu)
               94137660 1305.400    0.000 1305.400    0.000 {built-in method torch._C._nn.leaky_relu}
              996995626 1292.128    0.000 1292.128    0.000 layer.py:146(elements)
              316025383  994.040    0.000 1288.511    0.000 layers.py:77(check)
              120831584 1282.380    0.000 1282.380    0.000 {built-in method clone}
              177111292 1241.629    0.000 1241.629    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              316025383  825.045    0.000 1234.887    0.000 layers.py:286(check)
              316270300  224.603    0.000 1212.904    0.000 {built-in method builtins.all}
             3449291890  929.246    0.000 1128.908    0.000 layers.py:700(<genexpr>)
                9488105  211.100    0.000 1127.706    0.000 optimizer.py:189(zero_grad)
                3162702  878.167    0.000 1098.838    0.000 replaybuffer.py:73(CF_save_data)
              177111292 1091.138    0.000 1091.138    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                2698310   39.026    0.000 1078.794    0.000 layers.py:740(restart)
               10969945 1059.101    0.000 1059.101    0.000 {built-in method torch._C._nn.one_hot}
              316025383  642.273    0.000 1041.389    0.000 layers.py:246(check)
             2589310283  690.461    0.000 1026.551    0.000 layers.py:690(<genexpr>)
                3162702   69.587    0.000  838.585    0.000 replaybuffer.py:18(stacker)
                3162701   72.542    0.000  788.883    0.000 replaybuffer.py:63(stacker)
              316025383  612.027    0.000  762.746    0.000 layers.py:62(check)
                2698310   19.182    0.000  761.483    0.000 level.py:8(__init__)
               88555646  726.711    0.000  726.711    0.000 {method 'add' of 'torch._C._TensorBase' objects}
             7586422215  721.799    0.000  721.799    0.000 layer.py:91(positions)
               88555646  639.284    0.000  639.284    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
        8328490976/8328490973  557.162    0.000  622.999    0.000 {built-in method builtins.len}
               88555646  599.508    0.000  599.508    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               88555646  594.465    0.000  594.465    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                2698310   98.104    0.000  593.041    0.000 levels.py:199(generate)
               11722024  224.951    0.000  584.443    0.000 random.py:315(sample)
                7807243  203.049    0.000  583.768    0.000 exploration.py:53(softmaxer)
              316025383  361.000    0.000  561.842    0.000 layers.py:273(check)
              619889606  429.517    0.000  534.269    0.000 tensor.py:906(grad)
              316025383  336.764    0.000  529.441    0.000 layers.py:313(check)
                9488105   21.918    0.000  494.321    0.000 loss.py:527(forward)
                3162702  286.083    0.000  491.316    0.000 collector.py:46(collect)
             5852336798  487.606    0.000  487.606    0.000 {built-in method builtins.hash}
              316025383  329.425    0.000  477.044    0.000 layers.py:48(check)
                9488105   54.783    0.000  472.403    0.000 functional.py:2898(mse_loss)
               88555646  438.549    0.000  438.549    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                5396620   47.244    0.000  396.903    0.000 level.py:41(notUsed)
              316025383  244.788    0.000  358.552    0.000 layers.py:23(check)
                1495015  317.847    0.000  337.333    0.000 agent.py:186(convert_values)
              273036522  210.188    0.000  295.235    0.000 layer.py:126(remove)
              134964230  289.381    0.000  289.381    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               63254050  286.040    0.000  286.040    0.000 layer.py:163(<listcomp>)
             3487781662  286.015    0.000  286.015    0.000 {method 'random' of '_random.Random' objects}
              435792797  201.218    0.000  281.795    0.000 layer.py:130(add)
                9488105  279.083    0.000  279.083    0.000 {built-in method torch._C._nn.mse_loss}
                6325406  278.278    0.000  278.278    0.000 {built-in method nonzero}
              374487804  179.697    0.000  270.605    0.000 random.py:250(_randbelow_with_getrandbits)
               26983100   39.940    0.000  268.884    0.000 layer.py:69(restart)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9551821: <Causal4_Cf_convert5_TopN3_0> in cluster <dcc> Done

Job <Causal4_Cf_convert5_TopN3_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed Apr 21 03:20:32 2021
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Fri Apr 23 06:35:43 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Fri Apr 23 06:35:43 2021
Terminated at Sat Apr 24 06:30:59 2021
Results reported at Sat Apr 24 06:30:59 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=16G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 1440
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $LSB_PROJECT_NAME


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   85906.89 sec.
    Max Memory :                                 9242 MB
    Average Memory :                             6269.34 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               7142.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86117 sec.
    Turnaround time :                            270627 sec.

The output (if any) is above this job summary.

