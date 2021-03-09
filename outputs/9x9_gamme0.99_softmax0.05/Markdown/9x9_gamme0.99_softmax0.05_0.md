
# Parameters

    Name :                      9x9_gamme0.99_softmax0.05-0
    Main :                      teleport
    Hours :                     10.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Network1 :                  Networks.Teleporter
    Network2 :                  Networks.Mini
    Learner1 :                  Learners.Qlearn
    Learner2 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Exploration2 :              Explorations.epsilonGreedy
    Layer blocks :              True
    Layer goal :                True
    Layer gold :                True
    Layer keys :                True
    Layer door :                True
    Layer holder :              True
    Layer putter :              True
    K :                         200000
    Epsilon cap :               0.2
    Softmax cap :               0.05
    Gamma :                     0.95
    Update :                    10000
    Reset chance :              0.005
    Modified done chance :      0.05
    Miss intervention cost :    -0.2
    Intervention cost :         -0.05
    Replay size :               50000
    Sample size :               50
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      30328837539 function calls (30157878916 primitive calls) in 35686.57 seconds

##    Ordered by: cumulative time
   List reduced from 474 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35709.553 35709.553 {built-in method builtins.exec}
                      1    0.919    0.919 35709.553 35709.553 <string>:1(<module>)
                      1  129.029  129.029 35708.633 35708.633 main.py:10(teleport)
                6106070   21.316    0.000 13296.099    0.002 agent.py:26(learn)
                6106070  358.589    0.000 11157.563    0.002 learner.py:42(Qlearn)
                3053035   11.523    0.000 9198.431    0.003 game.py:21(step)
                3053035   14.414    0.000 8572.643    0.003 layers.py:212(step)
                3053035  109.527    0.000 7957.165    0.003 agent.py:50(_learn)
        192327828/21370216  729.693    0.000 5995.423    0.000 module.py:866(_call_impl)
               15264146   42.968    0.000 5573.900    0.000 network.py:24(forward)
                3053035  209.315    0.000 5546.310    0.002 layers.py:17(step)
               15264146  175.606    0.000 5438.885    0.000 container.py:117(forward)
              305303500  289.073    0.000 5310.603    0.000 layer.py:66(move)
                3053035   95.506    0.000 5306.093    0.002 agent.py:101(_learn)
                6106070   48.988    0.000 4302.123    0.001 optimizer.py:84(wrapper)
                6106070   25.789    0.000 4081.123    0.001 grad_mode.py:24(decorate_context)
                6106070  162.923    0.000 4000.663    0.001 adam.py:55(step)
                6105041  143.080    0.000 3716.298    0.001 agent.py:45(__call__)
                3053035 2185.829    0.001 3696.487    0.001 replaybuffer.py:27(teleporter_save_data)
                6106070  836.355    0.000 3643.968    0.001 _functional.py:53(adam)
                3053035 1808.927    0.001 3640.463    0.001 agent.py:77(interveen)
              305303500  618.796    0.000 3049.969    0.000 layers.py:229(check)
                3053036  263.137    0.000 2992.572    0.001 layers.py:192(update)
                6106070   24.285    0.000 2852.485    0.000 tensor.py:195(backward)
                6106070   23.087    0.000 2827.462    0.000 __init__.py:68(backward)
                6106070 2688.802    0.000 2688.802    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
               30528292   66.868    0.000 2046.927    0.000 conv.py:398(forward)
                3053035 1032.081    0.000 2005.150    0.001 replaybuffer.py:23(sample_data)
               30528292   37.854    0.000 1952.884    0.000 conv.py:390(_conv_forward)
               30528292 1915.030    0.000 1915.030    0.000 {built-in method conv2d}
                3053035 1043.756    0.000 1790.157    0.001 agent.py:59(modify)
              305303500  394.691    0.000 1703.022    0.000 layers.py:223(isFree)
               39686368   77.599    0.000 1518.925    0.000 linear.py:93(forward)
               39686368   32.802    0.000 1407.224    0.000 functional.py:1737(linear)
               39686368 1366.703    0.000 1366.703    0.000 {built-in method torch._C._nn.linear}
             1861769630 1062.699    0.000 1308.331    0.000 layer.py:63(isFree)
              146422285 1281.867    0.000 1281.867    0.000 {built-in method clone}
                3053035   40.677    0.000 1171.662    0.000 agent.py:96(__call__)
                9158076   51.318    0.000 1125.187    0.000 agent.py:54(modify_board)
              305303500  649.433    0.000 1063.988    0.000 layers.py:124(check)
                1572679   15.255    0.000  972.130    0.001 layers.py:233(restart)
               24423251  944.371    0.000  944.371    0.000 {built-in method cat}
               24424288  370.571    0.000  931.197    0.000 layer.py:90(update)
               12897213  890.626    0.000  890.626    0.000 {built-in method tensor}
                1572679    3.294    0.000  827.184    0.001 levels.py:8(__init__)
                1572679   11.750    0.000  823.890    0.001 level.py:8(__init__)
               54950514   42.164    0.000  814.528    0.000 activation.py:713(forward)
                2145265  123.985    0.000  789.734    0.000 levels.py:11(generate)
               54950514   47.873    0.000  772.364    0.000 functional.py:1364(leaky_relu)
                3053035   48.278    0.000  766.336    0.000 replaybuffer.py:19(stacker)
              305303600   79.214    0.000  746.881    0.000 {built-in method builtins.all}
                9158076  744.426    0.000  744.426    0.000 {built-in method torch._C._nn.one_hot}
                6106070    6.832    0.000  721.989    0.000 game.py:17(board)
               54950514  715.917    0.000  715.917    0.000 {built-in method torch._C._nn.leaky_relu}
              109909260  706.001    0.000  706.001    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              927088002  207.433    0.000  702.360    0.000 layers.py:197(<genexpr>)
                6106070  117.361    0.000  654.811    0.000 optimizer.py:189(zero_grad)
             2600413481  453.376    0.000  646.722    0.000 enum.py:646(__hash__)
              109909260  631.684    0.000  631.684    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              305303500  331.836    0.000  512.934    0.000 layers.py:95(check)
              305303600  311.790    0.000  469.469    0.000 layers.py:65(isDone)
                3053035  251.781    0.000  429.579    0.000 collector.py:37(collect)
               54954630  420.509    0.000  420.509    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              824308949  413.472    0.000  413.472    0.000 layer.py:85(elements)
             4696793650  391.390    0.000  391.390    0.000 layer.py:59(positions)
              305303500  258.963    0.000  384.050    0.000 layers.py:50(check)
              305303500  245.566    0.000  377.660    0.000 layers.py:77(check)
                6105041  138.715    0.000  367.176    0.000 exploration.py:53(softmaxer)
               54954630  359.709    0.000  359.709    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               54954630  342.593    0.000  342.593    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               54954630  333.427    0.000  333.427    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              384682464  246.809    0.000  304.117    0.000 tensor.py:906(grad)
              155580361  296.191    0.000  296.191    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                2145265  142.638    0.000  270.835    0.000 levels.py:76(RFS)
               54954630  260.781    0.000  260.781    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                6106070    8.142    0.000  248.166    0.000 loss.py:527(forward)
                8916244   92.564    0.000  241.995    0.000 random.py:315(sample)
                6106070   22.161    0.000  240.023    0.000 functional.py:2898(mse_loss)
              388492807  156.460    0.000  208.561    0.000 layer.py:76(add)
              298373379  135.635    0.000  196.456    0.000 layer.py:72(remove)
             2600435840  193.350    0.000  193.350    0.000 {built-in method builtins.hash}
                4718037   25.081    0.000  188.915    0.000 level.py:41(notUsed)
               18318210  184.822    0.000  184.822    0.000 {built-in method sum}
             1634157060  160.207    0.000  160.207    0.000 layer.py:125(isBlocking)
                6106070  147.342    0.000  147.342    0.000 {built-in method torch._C._nn.mse_loss}
        915222797/915222795  103.688    0.000  145.289    0.000 {built-in method builtins.len}
               30528292   20.642    0.000  137.371    0.000 flatten.py:39(forward)
                6106985  136.568    0.000  136.568    0.000 {built-in method max}
              157138281  133.037    0.000  133.037    0.000 level.py:32(inverse)
                9159105   13.320    0.000  130.467    0.000 tensor.py:525(__rsub__)
               12581432   16.858    0.000  125.414    0.000 layer.py:40(restart)
                3053035   11.990    0.000  124.091    0.000 exploration.py:47(epsilonGreedy)
              204117882   84.893    0.000  123.234    0.000 random.py:250(_randbelow_with_getrandbits)
               30528292  116.729    0.000  116.729    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                6105041  116.246    0.000  116.246    0.000 {built-in method multinomial}
                9159105  114.983    0.000  114.983    0.000 {built-in method rsub}
                6106070   23.786    0.000  110.488    0.000 __init__.py:28(_make_grads)
             1446113283  106.887    0.000  106.887    0.000 {method 'append' of 'list' objects}
               12212140   25.460    0.000  106.339    0.000 profiler.py:615(__enter__)
              195382083  105.385    0.000  105.385    0.000 {built-in method torch._C._get_tracing_state}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-3>
Subject: Job 9395485: <9x9_gamme0.99_softmax0.05_0> in cluster <dcc> Done

Job <9x9_gamme0.99_softmax0.05_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Tue Mar  9 01:14:59 2021
Job was executed on host(s) <n-62-20-3>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Tue Mar  9 03:18:58 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue Mar  9 03:18:58 2021
Terminated at Tue Mar  9 13:14:28 2021
Results reported at Tue Mar  9 13:14:28 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=8G]"
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

    CPU time :                                   35621.77 sec.
    Max Memory :                                 6595 MB
    Average Memory :                             4436.80 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               1597.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35730 sec.
    Turnaround time :                            43169 sec.

The output (if any) is above this job summary.


# Parameters

    Name :                      9x9_gamme0.99_softmax0.05-0
    Main :                      teleport
    Hours :                     10.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Network1 :                  Networks.Teleporter
    Network2 :                  Networks.Mini
    Learner1 :                  Learners.Qlearn
    Learner2 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Exploration2 :              Explorations.epsilonGreedy
    Layer blocks :              True
    Layer goal :                True
    Layer gold :                True
    Layer keys :                True
    Layer door :                True
    Layer holder :              True
    Layer putter :              True
    K :                         200000
    Epsilon cap :               0.2
    Softmax cap :               0.05
    Gamma :                     0.99
    Update :                    10000
    Reset chance :              0.005
    Modified done chance :      0.05
    Miss intervention cost :    -0.2
    Intervention cost :         -0.05
    Replay size :               50000
    Sample size :               50
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      29130388519 function calls (28965486320 primitive calls) in 35683.46 seconds

##    Ordered by: cumulative time
   List reduced from 473 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35705.866 35705.866 {built-in method builtins.exec}
                      1    1.139    1.139 35705.866 35705.866 <string>:1(<module>)
                      1  142.316  142.316 35704.727 35704.727 main.py:10(teleport)
                5890232   22.739    0.000 13808.738    0.002 agent.py:26(learn)
                5890232  372.888    0.000 11584.886    0.002 learner.py:42(Qlearn)
                2945116   11.931    0.000 9440.116    0.003 game.py:21(step)
                2945116   13.931    0.000 8823.058    0.003 layers.py:212(step)
                2945116  117.654    0.000 8263.330    0.003 agent.py:50(_learn)
        185514891/20613703  772.254    0.000 6223.461    0.000 module.py:866(_call_impl)
               14723471   46.450    0.000 5780.542    0.000 network.py:24(forward)
                2945116  216.877    0.000 5719.813    0.002 layers.py:17(step)
               14723471  191.462    0.000 5634.510    0.000 container.py:117(forward)
                2945116  101.191    0.000 5509.387    0.002 agent.py:101(_learn)
              294511600  297.907    0.000 5477.044    0.000 layer.py:66(move)
                5890232   50.550    0.000 4508.741    0.001 optimizer.py:84(wrapper)
                5890232   26.426    0.000 4285.610    0.001 grad_mode.py:24(decorate_context)
                5890232  168.106    0.000 4200.268    0.001 adam.py:55(step)
                5888123  149.910    0.000 3835.078    0.001 agent.py:45(__call__)
                5890232  891.022    0.000 3834.978    0.001 _functional.py:53(adam)
                2945116 1485.423    0.001 3368.257    0.001 agent.py:77(interveen)
              294511600  632.609    0.000 3151.451    0.000 layers.py:229(check)
                2945116 1803.164    0.001 3107.220    0.001 replaybuffer.py:27(teleporter_save_data)
                2945117  277.444    0.000 3068.176    0.001 layers.py:192(update)
                5890232   25.520    0.000 2920.623    0.000 tensor.py:195(backward)
                5890232   24.605    0.000 2894.318    0.000 __init__.py:68(backward)
                5890232 2753.804    0.000 2753.804    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
               29446942   73.380    0.000 2095.307    0.000 conv.py:398(forward)
                2945116 1016.617    0.000 2026.393    0.001 replaybuffer.py:23(sample_data)
               29446942   41.337    0.000 1991.692    0.000 conv.py:390(_conv_forward)
               29446942 1950.355    0.000 1950.355    0.000 {built-in method conv2d}
                2945116 1055.704    0.000 1813.848    0.001 agent.py:59(modify)
              294511600  395.329    0.000 1750.940    0.000 layers.py:223(isFree)
               38280181   85.191    0.000 1576.360    0.000 linear.py:93(forward)
               38280181   34.673    0.000 1453.623    0.000 functional.py:1737(linear)
               38280181 1411.310    0.000 1411.310    0.000 {built-in method torch._C._nn.linear}
             1787169934 1101.350    0.000 1355.611    0.000 layer.py:63(isFree)
                2945116   43.567    0.000 1211.097    0.000 agent.py:96(__call__)
                8833239   55.841    0.000 1143.099    0.000 agent.py:54(modify_board)
              115285202 1111.489    0.000 1111.489    0.000 {built-in method clone}
              294511600  670.607    0.000 1100.094    0.000 layers.py:124(check)
                1488464   15.283    0.000  980.945    0.001 layers.py:233(restart)
               23558819  977.546    0.000  977.546    0.000 {built-in method cat}
               23560936  365.756    0.000  954.604    0.000 layer.py:90(update)
               12445440  869.546    0.000  869.546    0.000 {built-in method tensor}
               53003652   49.186    0.000  847.763    0.000 activation.py:713(forward)
                1488464    3.130    0.000  834.310    0.001 levels.py:8(__init__)
                1488464   12.102    0.000  831.180    0.001 level.py:8(__init__)
               53003652   47.240    0.000  798.576    0.000 functional.py:1364(leaky_relu)
                2945116   52.569    0.000  798.060    0.000 replaybuffer.py:19(stacker)
                2030794  124.838    0.000  797.264    0.000 levels.py:11(generate)
              294511700   92.647    0.000  775.560    0.000 {built-in method builtins.all}
                8833239  748.653    0.000  748.653    0.000 {built-in method torch._C._nn.one_hot}
               53003652  742.040    0.000  742.040    0.000 {built-in method torch._C._nn.leaky_relu}
              106024176  733.941    0.000  733.941    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              891631248  211.372    0.000  715.998    0.000 layers.py:197(<genexpr>)
                5890232    6.182    0.000  698.224    0.000 game.py:17(board)
                5890232  124.528    0.000  680.658    0.000 optimizer.py:189(zero_grad)
             2505308564  477.487    0.000  673.110    0.000 enum.py:646(__hash__)
              106024176  662.777    0.000  662.777    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              294511600  333.079    0.000  522.440    0.000 layers.py:95(check)
              294511700  313.841    0.000  478.793    0.000 layers.py:65(isDone)
                2945116  266.727    0.000  452.522    0.000 collector.py:37(collect)
               53012088  444.821    0.000  444.821    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              788469933  437.352    0.000  437.352    0.000 layer.py:85(elements)
             4535664967  407.281    0.000  407.281    0.000 layer.py:59(positions)
              294511600  273.169    0.000  404.140    0.000 layers.py:50(check)
              294511600  258.424    0.000  396.328    0.000 layers.py:77(check)
               53012088  385.797    0.000  385.797    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                5888123  142.397    0.000  376.463    0.000 exploration.py:53(softmaxer)
               53012088  355.139    0.000  355.139    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               53012088  347.178    0.000  347.178    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              371084670  251.358    0.000  312.175    0.000 tensor.py:906(grad)
                2030794  145.114    0.000  274.528    0.000 levels.py:76(RFS)
               53012088  268.735    0.000  268.735    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              124118441  266.611    0.000  266.611    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                5890232    8.815    0.000  257.696    0.000 loss.py:527(forward)
                5890232   23.451    0.000  248.881    0.000 functional.py:2898(mse_loss)
                8495168   96.713    0.000  247.557    0.000 random.py:315(sample)
              371391007  157.083    0.000  210.940    0.000 layer.py:76(add)
              285799984  140.769    0.000  203.963    0.000 layer.py:72(remove)
             2505330131  195.626    0.000  195.626    0.000 {built-in method builtins.hash}
               17670696  192.234    0.000  192.234    0.000 {built-in method sum}
                4465392   25.363    0.000  189.560    0.000 level.py:41(notUsed)
             1569957427  164.448    0.000  164.448    0.000 layer.py:125(isBlocking)
                5890232  153.853    0.000  153.853    0.000 {built-in method torch._C._nn.mse_loss}
        881945989/881945987  106.304    0.000  149.895    0.000 {built-in method builtins.len}
               29446942   21.674    0.000  141.602    0.000 flatten.py:39(forward)
                5891114  141.524    0.000  141.524    0.000 {built-in method max}
              148731422  133.320    0.000  133.320    0.000 level.py:32(inverse)
                8835348   13.332    0.000  132.254    0.000 tensor.py:525(__rsub__)
              195974118   86.468    0.000  127.197    0.000 random.py:250(_randbelow_with_getrandbits)
               11907712   18.034    0.000  127.111    0.000 layer.py:40(restart)
                2945116   12.494    0.000  124.277    0.000 exploration.py:47(epsilonGreedy)
               29446942  119.928    0.000  119.928    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                5888123  119.437    0.000  119.437    0.000 {built-in method multinomial}
                8835348  116.701    0.000  116.701    0.000 {built-in method rsub}
                5890232   24.063    0.000  110.705    0.000 __init__.py:28(_make_grads)
             1384610766  110.060    0.000  110.060    0.000 {method 'append' of 'list' objects}
                5890232  108.811    0.000  108.811    0.000 {built-in method gather}
              188461183  107.287    0.000  107.287    0.000 {built-in method torch._C._get_tracing_state}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-11-16>
Subject: Job 9395486: <9x9_gamme0.99_softmax0.05_0> in cluster <dcc> Done

Job <9x9_gamme0.99_softmax0.05_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Tue Mar  9 01:14:59 2021
Job was executed on host(s) <n-62-11-16>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Tue Mar  9 03:54:18 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue Mar  9 03:54:18 2021
Terminated at Tue Mar  9 13:49:40 2021
Results reported at Tue Mar  9 13:49:40 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=8G]"
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

    CPU time :                                   35609.93 sec.
    Max Memory :                                 6462 MB
    Average Memory :                             4428.73 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               1730.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35722 sec.
    Turnaround time :                            45281 sec.

The output (if any) is above this job summary.

