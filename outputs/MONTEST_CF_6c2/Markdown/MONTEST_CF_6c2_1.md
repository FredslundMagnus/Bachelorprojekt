
# Parameters

    Name :                      MONTEST_CF_6c2-1
    Main :                      CFagent
    Level :                     Levels.MonsterLevel
    Hours :                     22.0
    Batch :                     100
    Width :                     9
    Height :                    9
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
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                6
    Counterfacts :              2
    Topn :                      7
    Minutes used :              1315 minutes.
    Hours used :                21 hours.

# Profiling


      54626566162 function calls (54342182891 primitive calls) in 78913.72 seconds

##    Ordered by: cumulative time
   List reduced from 505 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 78913.717 78913.717 {built-in method builtins.exec}
                      1    5.871    5.871 78913.717 78913.717 <string>:1(<module>)
                      1  246.228  246.228 78907.846 78907.846 main.py:95(CFagent)
                6804972   42.832    0.000 19692.703    0.003 agent.py:29(learn)
                2268324   16.617    0.000 18593.602    0.008 game.py:41(step)
                2268324   18.805    0.000 18023.429    0.008 layers.py:710(step)
                2268324 2895.710    0.001 16833.583    0.007 agent.py:217(counterfact)
                6804972  533.041    0.000 15664.242    0.002 learner.py:42(Qlearn)
        315641125/31259545 1483.568    0.000 11637.738    0.000 module.py:866(_call_impl)
               24454573   86.376    0.000 10904.455    0.000 network.py:24(forward)
               24454573  358.317    0.000 10622.581    0.000 container.py:117(forward)
                2268325  390.611    0.000 10027.673    0.004 layers.py:676(update)
                2268324  237.092    0.000 7947.912    0.004 layers.py:17(step)
              212132476  686.170    0.000 7689.442    0.000 layer.py:98(move)
                2268324  353.612    0.000 7647.753    0.003 agent.py:54(_learn)
                2268324  349.249    0.000 6864.151    0.003 agent.py:209(_learn)
                8824767  351.473    0.000 6622.949    0.001 agent.py:49(__call__)
                4288186  108.566    0.000 6549.969    0.002 agent.py:172(choose_action)
                6804972   88.009    0.000 5766.251    0.001 optimizer.py:84(wrapper)
                6804972   47.255    0.000 5402.133    0.001 grad_mode.py:24(decorate_context)
                2268324 3126.285    0.001 5267.317    0.002 replaybuffer.py:28(teleporter_save_data)
                6804972  259.681    0.000 5254.008    0.001 adam.py:55(step)
                2268324   97.450    0.000 5119.688    0.002 agent.py:117(_learn)
                8499623   83.294    0.000 4905.077    0.001 layers.py:731(restart)
              212132476  489.015    0.000 4861.629    0.000 layers.py:727(check)
                2268324 3840.416    0.002 4840.475    0.002 replaybuffer.py:22(sample_data)
                6804972 1106.817    0.000 4735.249    0.001 _functional.py:53(adam)
               58366476 4621.303    0.000 4621.303    0.000 {built-in method tensor}
               53043960   40.275    0.000 4490.903    0.000 game.py:37(board)
               40829838 2833.855    0.000 4455.969    0.000 layer.py:151(update)
                2268324 3459.662    0.002 4317.085    0.002 replaybuffer.py:49(sample_data)
                6804972   43.144    0.000 4287.732    0.001 tensor.py:195(backward)
                6804972   44.835    0.000 4243.537    0.001 __init__.py:68(backward)
                8499623   39.200    0.000 4134.221    0.000 level.py:8(__init__)
                6804972 4012.810    0.001 4012.810    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               48909146  122.831    0.000 3990.519    0.000 conv.py:398(forward)
               48909146   85.887    0.000 3808.693    0.000 conv.py:390(_conv_forward)
                2268324 2175.166    0.001 3795.471    0.002 agent.py:88(interveen)
                8499623  652.707    0.000 3742.454    0.000 levels.py:418(generate)
               48909146 3722.806    0.000 3722.806    0.000 {built-in method conv2d}
              212132476 1843.446    0.000 3135.860    0.000 layers.py:531(check)
               68827071  151.654    0.000 2992.904    0.000 linear.py:93(forward)
               68827071   64.342    0.000 2761.506    0.000 functional.py:1737(linear)
               68827071 2681.737    0.000 2681.737    0.000 {built-in method torch._C._nn.linear}
               42498115  396.668    0.000 2436.808    0.000 level.py:41(notUsed)
              224393207 2260.295    0.000 2260.295    0.000 {built-in method clone}
                2268324 1421.805    0.001 2165.659    0.001 agent.py:67(modify)
               11093091   96.780    0.000 1745.287    0.000 agent.py:59(modify_board)
              212035731  263.695    0.000 1667.572    0.000 layers.py:721(isFree)
               36044655 1655.897    0.000 1655.897    0.000 {built-in method cat}
              227831294  180.084    0.000 1603.484    0.000 {built-in method builtins.any}
               93281644   87.721    0.000 1547.283    0.000 activation.py:713(forward)
                2268324  794.527    0.000 1518.864    0.001 replaybuffer.py:55(CF_save_data)
               93281644   87.364    0.000 1459.562    0.000 functional.py:1364(leaky_relu)
             1543215443  449.262    0.000 1424.047    0.000 layers.py:692(<genexpr>)
             1132961091 1219.383    0.000 1403.877    0.000 layer.py:95(isFree)
             5416918584  954.743    0.000 1368.175    0.000 enum.py:646(__hash__)
               93281644 1356.091    0.000 1356.091    0.000 {built-in method torch._C._nn.leaky_relu}
                4288186 1115.590    0.000 1317.717    0.000 agent.py:183(convert_values)
                2268324   57.654    0.000 1238.775    0.001 agent.py:168(__call__)
               11093091 1148.584    0.000 1148.584    0.000 {built-in method torch._C._nn.one_hot}
             1826071405 1085.907    0.000 1085.907    0.000 layer.py:146(elements)
                2268324   56.391    0.000 1081.200    0.000 agent.py:112(__call__)
               42498115   35.299    0.000 1045.918    0.000 level.py:38(elementsIn)
              226832500  118.033    0.000  936.202    0.000 {built-in method builtins.all}
              127026144  895.086    0.000  895.086    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              223294645  572.574    0.000  888.930    0.000 layers.py:568(isDead)
             1175977585  347.350    0.000  848.486    0.000 layers.py:682(<genexpr>)
                6804972  160.312    0.000  822.261    0.000 optimizer.py:189(zero_grad)
               47034763  318.209    0.000  811.040    0.000 random.py:315(sample)
              127026144  796.062    0.000  796.062    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                2268324   60.407    0.000  791.648    0.000 replaybuffer.py:18(stacker)
              212132476  556.628    0.000  771.384    0.000 layers.py:71(check)
                8824767  243.327    0.000  709.385    0.000 exploration.py:53(softmaxer)
             1813159014  678.996    0.000  678.996    0.000 level.py:32(inverse)
               50997738   67.182    0.000  669.418    0.000 layer.py:69(restart)
               42498115  327.112    0.000  660.149    0.000 level.py:39(<listcomp>)
                2268324   56.782    0.000  659.478    0.000 replaybuffer.py:45(stacker)
              495717586  468.023    0.000  616.065    0.000 layer.py:126(remove)
              297157767  113.220    0.000  549.108    0.000 random.py:244(randint)
              713600944  373.642    0.000  548.423    0.000 random.py:250(_randbelow_with_getrandbits)
               63513072  534.089    0.000  534.089    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              881436163  377.555    0.000  510.268    0.000 layer.py:130(add)
              237754622  494.298    0.000  494.298    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               63513072  490.406    0.000  490.406    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                8499723  225.093    0.000  454.517    0.000 layers.py:30(reset)
               63513072  450.516    0.000  450.516    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               63513072  441.130    0.000  441.130    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              297157767  181.819    0.000  435.888    0.000 random.py:200(randrange)
              226832500  305.334    0.000  431.780    0.000 layers.py:107(isDone)
               34097134  423.543    0.000  423.543    0.000 {method 'item' of 'torch._C._TensorBase' objects}
        4880954875/4880954872  357.424    0.000  423.381    0.000 {built-in method builtins.len}
                6804972   17.262    0.000  413.961    0.000 loss.py:527(forward)
             5416944599  413.437    0.000  413.437    0.000 {built-in method builtins.hash}
              212132476  288.980    0.000  405.416    0.000 layers.py:42(check)
             4241054918  398.465    0.000  398.465    0.000 layer.py:91(positions)
                6804972   46.156    0.000  396.699    0.000 functional.py:2898(mse_loss)
              444591588  313.971    0.000  385.904    0.000 tensor.py:906(grad)
                2268324  213.656    0.000  367.121    0.000 collector.py:53(collect)
                6804973  353.301    0.000  353.301    0.000 {built-in method nonzero}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-10>
Subject: Job 9507482: <MONTEST_CF_6c2_1> in cluster <dcc> Done

Job <MONTEST_CF_6c2_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sat Apr 10 02:36:50 2021
Job was executed on host(s) <n-62-20-10>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Apr 11 03:29:06 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun Apr 11 03:29:06 2021
Terminated at Mon Apr 12 01:24:27 2021
Results reported at Mon Apr 12 01:24:27 2021

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

    CPU time :                                   78717.41 sec.
    Max Memory :                                 7865 MB
    Average Memory :                             5696.81 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               8519.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   78922 sec.
    Turnaround time :                            168457 sec.

The output (if any) is above this job summary.

