
# Parameters

    Name :                      MagicalLights2_convert4_TEST-0
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
    Cf convert :                4
    Counterfacts :              1
    Topn :                      3
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      77981691831 function calls (77633221628 primitive calls) in 86110.49 seconds

##    Ordered by: cumulative time
   List reduced from 515 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86110.488 86110.488 {built-in method builtins.exec}
                      1    4.337    4.337 86110.488 86110.488 <string>:1(<module>)
                      1  382.945  382.945 86106.151 86106.151 main.py:79(CFagent)
               11313354   42.626    0.000 27266.241    0.002 agent.py:29(learn)
                3771118   14.985    0.000 22573.714    0.006 game.py:41(step)
               11313352  692.611    0.000 22239.025    0.002 learner.py:42(Qlearn)
                3771118   20.839    0.000 21725.203    0.006 layers.py:718(step)
                3771118  331.793    0.000 14565.122    0.004 layers.py:17(step)
              376853212 1089.493    0.000 14201.213    0.000 layer.py:98(move)
        390077946/41609434 1558.441    0.000 12580.651    0.000 module.py:866(_call_impl)
               30296082   81.058    0.000 11757.904    0.000 network.py:27(forward)
               30296082  392.384    0.000 11484.473    0.000 container.py:117(forward)
                3771118  908.779    0.000 10839.458    0.003 agent.py:212(counterfact)
                3771118  372.372    0.000 10585.130    0.003 agent.py:54(_learn)
                3771118  368.112    0.000 9729.658    0.003 agent.py:204(_learn)
              376853212 1838.518    0.000 9015.931    0.000 layers.py:735(check)
               11313352   94.799    0.000 8827.073    0.001 optimizer.py:84(wrapper)
               11313352   48.181    0.000 8408.496    0.001 grad_mode.py:24(decorate_context)
               11313352  329.696    0.000 8258.047    0.001 adam.py:55(step)
               11313352 1735.581    0.000 7547.752    0.001 _functional.py:53(adam)
                3771119  546.787    0.000 7110.959    0.002 layers.py:684(update)
                3771118  110.524    0.000 6883.174    0.002 agent.py:117(_learn)
                9480787  233.573    0.000 6007.461    0.001 agent.py:49(__call__)
               59511967 5978.225    0.000 5978.225    0.000 {built-in method tensor}
               50874373   32.187    0.000 5775.334    0.000 game.py:37(board)
                3771118 4604.075    0.001 5724.583    0.002 replaybuffer.py:22(sample_data)
               11313352   46.357    0.000 5610.510    0.000 tensor.py:195(backward)
               11313352   43.272    0.000 5562.432    0.000 __init__.py:68(backward)
                3771118 4377.132    0.001 5463.671    0.001 replaybuffer.py:67(sample_data)
               11313352 5301.730    0.000 5301.730    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
               75422370 2634.234    0.000 4554.958    0.000 layer.py:151(update)
               60592164  134.905    0.000 4239.611    0.000 conv.py:398(forward)
               60592164   81.470    0.000 4041.148    0.000 conv.py:390(_conv_forward)
                3771118 1613.293    0.000 3978.581    0.001 agent.py:88(interveen)
               60592164 3959.678    0.000 3959.678    0.000 {built-in method conv2d}
              376853212  667.471    0.000 3364.613    0.000 layers.py:729(isFree)
               83346010  166.140    0.000 3223.365    0.000 linear.py:93(forward)
                3771118 1763.359    0.000 3169.356    0.001 replaybuffer.py:28(teleporter_save_data)
               83346010   70.300    0.000 2973.963    0.000 functional.py:1737(linear)
               83346010 2886.918    0.000 2886.918    0.000 {built-in method torch._C._nn.linear}
             3300077546 2178.415    0.000 2697.142    0.000 layer.py:95(isFree)
                3771118 1771.126    0.000 2695.031    0.001 agent.py:67(modify)
                1959709   39.753    0.000 2646.437    0.001 agent.py:176(choose_action)
             7385891478 1341.508    0.000 1944.542    0.000 enum.py:646(__hash__)
               50963075 1845.431    0.000 1845.431    0.000 {built-in method cat}
              377221770  394.548    0.000 1747.610    0.000 {built-in method builtins.any}
              113642092   87.774    0.000 1721.302    0.000 activation.py:713(forward)
               13251905   87.351    0.000 1702.212    0.000 agent.py:59(modify_board)
                3771116   59.088    0.000 1665.247    0.000 agent.py:172(__call__)
              113642092   96.894    0.000 1633.528    0.000 functional.py:1364(leaky_relu)
                3771118   58.143    0.000 1561.036    0.000 agent.py:112(__call__)
              113642092 1516.613    0.000 1516.613    0.000 {built-in method torch._C._nn.leaky_relu}
              211182568 1490.339    0.000 1490.339    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              376853212 1085.790    0.000 1437.473    0.000 layers.py:77(check)
              141627196 1424.090    0.000 1424.090    0.000 {built-in method clone}
             4107957161 1117.640    0.000 1353.062    0.000 layers.py:700(<genexpr>)
                3661249   47.114    0.000 1324.806    0.000 layers.py:740(restart)
              211182568 1318.344    0.000 1318.344    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               11313352  233.627    0.000 1315.644    0.000 optimizer.py:189(zero_grad)
              376853212  828.466    0.000 1300.820    0.000 layers.py:286(check)
                3771118  992.324    0.000 1261.782    0.000 replaybuffer.py:73(CF_save_data)
              376853212  731.170    0.000 1182.203    0.000 layers.py:246(check)
               13251905 1113.913    0.000 1113.913    0.000 {built-in method torch._C._nn.one_hot}
             1244342635 1051.675    0.000 1051.675    0.000 layer.py:146(elements)
                3661249   20.491    0.000  932.485    0.000 level.py:8(__init__)
             9738496059  895.915    0.000  895.915    0.000 layer.py:91(positions)
              377111900   93.425    0.000  891.629    0.000 {built-in method builtins.all}
              105591284  865.033    0.000  865.033    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                3771118   63.394    0.000  850.851    0.000 replaybuffer.py:18(stacker)
              815564367  183.602    0.000  844.425    0.000 layers.py:690(<genexpr>)
                3771116   67.503    0.000  825.756    0.000 replaybuffer.py:63(stacker)
                3661249  122.353    0.000  753.103    0.000 levels.py:199(generate)
              105591284  743.771    0.000  743.771    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              376853212  539.928    0.000  713.287    0.000 layers.py:62(check)
        10009703753/10009703750  643.687    0.000  712.395    0.000 {built-in method builtins.len}
              105591284  687.242    0.000  687.242    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              105591284  680.047    0.000  680.047    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              377111900  435.847    0.000  650.957    0.000 layers.py:113(isDone)
              376853212  402.187    0.000  629.910    0.000 layers.py:273(check)
              376853212  405.761    0.000  627.407    0.000 layers.py:313(check)
              739139072  494.802    0.000  610.873    0.000 tensor.py:906(grad)
             7385934405  603.041    0.000  603.041    0.000 {built-in method builtins.hash}
                9480787  222.525    0.000  588.140    0.000 exploration.py:53(softmaxer)
                3771118  339.190    0.000  574.212    0.000 collector.py:46(collect)
               14864734  220.759    0.000  573.509    0.000 random.py:315(sample)
              105591284  526.459    0.000  526.459    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                1959709  444.961    0.000  521.715    0.000 agent.py:187(convert_values)
              376853212  348.216    0.000  518.559    0.000 layers.py:48(check)
                7322498   59.582    0.000  512.286    0.000 level.py:41(notUsed)
               11313352   16.547    0.000  474.744    0.000 loss.py:527(forward)
               11313352   42.950    0.000  458.196    0.000 functional.py:2898(mse_loss)
              376853212  279.494    0.000  405.414    0.000 layers.py:23(check)
               36612490   48.200    0.000  332.431    0.000 layer.py:69(restart)
              158650217  330.771    0.000  330.771    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
             4160398785  330.006    0.000  330.006    0.000 {method 'random' of '_random.Random' objects}
              329687447  225.857    0.000  313.617    0.000 layer.py:126(remove)
              547575381  225.189    0.000  304.689    0.000 layer.py:130(add)
               60592164   46.872    0.000  286.188    0.000 flatten.py:39(forward)
              450069375  193.541    0.000  283.093    0.000 random.py:250(_randbelow_with_getrandbits)
               11313352  282.970    0.000  282.970    0.000 {built-in method torch._C._nn.mse_loss}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9572853: <MagicalLights2_convert4_TEST_0> in cluster <dcc> Done

Job <MagicalLights2_convert4_TEST_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon Apr 26 00:55:52 2021
Job was executed on host(s) <n-62-11-15>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon Apr 26 01:09:24 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Apr 26 01:09:24 2021
Terminated at Tue Apr 27 01:04:39 2021
Results reported at Tue Apr 27 01:04:39 2021

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

    CPU time :                                   85900.50 sec.
    Max Memory :                                 10462 MB
    Average Memory :                             6763.61 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               5922.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86115 sec.
    Turnaround time :                            86927 sec.

The output (if any) is above this job summary.

