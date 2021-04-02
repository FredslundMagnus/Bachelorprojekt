
# Parameters

    Name :                      causal5_test-1
    Main :                      teleport
    Level :                     Levels.Causal5
    Hours :                     6.0
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
    Layer reddoors :            True
    Layer redkeys :             True
    Layer bluedoors :           True
    Layer bluekeys :            True
    Layer pink1 :               True
    Layer pink2 :               True
    Layer pink3 :               True
    Layer brown1 :              True
    Layer brown2 :              True
    Layer brown3 :              True
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Minutes used :              358 minutes.
    Hours used :                5 hours.

# Profiling


      17808558919 function calls (17738367004 primitive calls) in 21483.40 seconds

##    Ordered by: cumulative time
   List reduced from 459 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 21483.402 21483.402 {built-in method builtins.exec}
                      1    1.862    1.862 21483.402 21483.402 <string>:1(<module>)
                      1   66.626   66.626 21481.540 21481.540 main.py:42(teleport)
                2507184    9.938    0.000 7149.517    0.003 agent.py:27(learn)
                2507184  172.750    0.000 5984.268    0.002 learner.py:42(Qlearn)
                1253592    5.680    0.000 5328.505    0.004 game.py:36(step)
                1253592    7.630    0.000 5032.924    0.004 layers.py:594(step)
                1253592   44.114    0.000 4342.920    0.003 agent.py:52(_learn)
                1253592  106.460    0.000 3414.933    0.003 layers.py:18(step)
              125359200  164.488    0.000 3296.936    0.000 layer.py:82(move)
        78965194/8774290  305.508    0.000 2947.875    0.000 module.py:715(_call_impl)
                1253592   34.616    0.000 2791.716    0.002 agent.py:113(_learn)
                6267106   15.821    0.000 2750.356    0.000 network.py:24(forward)
                6267106   71.348    0.000 2696.183    0.000 container.py:115(forward)
                1253592 1494.274    0.001 2635.070    0.002 replaybuffer.py:28(teleporter_save_data)
                2507184   15.512    0.000 2385.510    0.001 grad_mode.py:23(decorate_context)
                2507184   81.513    0.000 2341.796    0.001 adam.py:55(step)
              125359200  321.744    0.000 2067.468    0.000 layers.py:611(check)
                1253592 1418.642    0.001 2058.420    0.002 replaybuffer.py:22(sample_data)
                1253592 1159.857    0.001 2057.304    0.002 agent.py:84(interveen)
                2507184  430.859    0.000 1923.688    0.001 functional.py:53(adam)
                2506330   61.293    0.000 1839.541    0.001 agent.py:47(__call__)
                1253593  135.055    0.000 1598.646    0.001 layers.py:565(update)
                2507184   15.396    0.000 1421.789    0.001 tensor.py:181(backward)
                2507184    9.361    0.000 1406.393    0.001 __init__.py:68(backward)
                2507184 1338.893    0.001 1338.893    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                1253592  474.135    0.000 1006.166    0.001 agent.py:65(modify)
               12534212   20.920    0.000 1000.160    0.000 conv.py:422(forward)
               12534212   25.093    0.000  969.696    0.000 conv.py:414(_conv_forward)
               12534212  939.215    0.000  939.215    0.000 {built-in method conv2d}
               86968416  913.369    0.000  913.369    0.000 {built-in method clone}
              125359200  211.226    0.000  897.464    0.000 layers.py:605(isFree)
               16294134   35.953    0.000  864.557    0.000 linear.py:92(forward)
               11282337  460.937    0.000  810.080    0.000 layer.py:143(NoRock_update)
               16294134   60.861    0.000  809.733    0.000 functional.py:1669(linear)
             1059677728  566.228    0.000  686.238    0.000 layer.py:79(isFree)
               11281474  630.446    0.000  630.446    0.000 {built-in method cat}
                1253592   17.850    0.000  603.541    0.000 agent.py:108(__call__)
              157952646  361.952    0.000  600.602    0.000 tensor.py:933(grad)
               16294134  572.115    0.000  572.115    0.000 {built-in method addmm}
                3759922   26.447    0.000  559.388    0.000 agent.py:57(modify_board)
                1253592   27.166    0.000  543.017    0.000 replaybuffer.py:18(stacker)
                2507184   49.408    0.000  521.050    0.000 optimizer.py:167(zero_grad)
             2005111520  368.384    0.000  516.289    0.000 enum.py:646(__hash__)
                5589272  437.626    0.000  437.626    0.000 {built-in method tensor}
               45129312  388.269    0.000  388.269    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               22561240   19.088    0.000  373.307    0.000 activation.py:713(forward)
                3759922  362.273    0.000  362.273    0.000 {built-in method torch._C._nn.one_hot}
               22561240   29.367    0.000  354.219    0.000 functional.py:1292(leaky_relu)
              125359200  215.532    0.000  349.572    0.000 layers.py:357(check)
              125359200  212.480    0.000  343.579    0.000 layers.py:371(check)
              125359200  214.836    0.000  343.332    0.000 layers.py:401(check)
                2507184    2.908    0.000  341.596    0.000 game.py:32(board)
              125359200  209.891    0.000  340.641    0.000 layers.py:415(check)
              131628246   39.971    0.000  338.869    0.000 {built-in method builtins.all}
               22561240  321.810    0.000  321.810    0.000 {built-in method torch._C._nn.leaky_relu}
               45129312  320.846    0.000  320.846    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              203080222  106.150    0.000  318.916    0.000 overrides.py:1070(has_torch_function)
              382848699   89.466    0.000  309.228    0.000 layers.py:571(<genexpr>)
                 584262    8.072    0.000  271.985    0.000 layers.py:615(restart)
                6268946   32.448    0.000  260.428    0.000 tensor.py:21(wrapped)
               90728338  257.158    0.000  257.158    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
             2750664551  251.630    0.000  251.630    0.000 layer.py:75(positions)
                1253592  132.515    0.000  227.870    0.000 collector.py:54(collect)
               22564656  224.039    0.000  224.039    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                 584262    4.126    0.000  216.001    0.000 level.py:8(__init__)
              300586455  215.240    0.000  215.240    0.000 layer.py:122(elements)
               22564656  212.923    0.000  212.923    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              125359300  140.314    0.000  208.096    0.000 layers.py:111(isDone)
              224388725   81.846    0.000  202.496    0.000 {built-in method builtins.any}
                1253646  201.214    0.000  201.215    0.000 {method 'to' of 'torch._C._TensorBase' objects}
                2506330   69.251    0.000  193.819    0.000 exploration.py:53(softmaxer)
                 584262    9.923    0.000  182.623    0.000 levels.py:247(generate)
               22564656  182.484    0.000  182.484    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                      2    0.000    0.000  180.661   90.331 agent.py:14(__init__)
                      2    0.000    0.000  180.661   90.330 network.py:33(__init__)
                      1    0.000    0.000  180.652  180.652 agent.py:105(__init__)
                      6    0.000    0.000  179.600   29.933 module.py:529(to)
                   72/6    0.001    0.000  179.600   29.933 module.py:357(_apply)
                     54    0.000    0.000  179.598    3.326 module.py:607(convert)
              125359200  117.099    0.000  177.863    0.000 layers.py:344(check)
                3797038   32.982    0.000  162.601    0.000 level.py:41(notUsed)
              125359200  105.964    0.000  160.002    0.000 layers.py:388(check)
               22564656  158.406    0.000  158.406    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
             2005120919  147.906    0.000  147.906    0.000 {built-in method builtins.hash}
                2507184    3.753    0.000  129.847    0.000 loss.py:445(forward)
                2507184   14.782    0.000  126.095    0.000 functional.py:2637(mse_loss)
        1333038128/1333038126   87.228    0.000  122.222    0.000 {built-in method builtins.len}
               22564656  120.958    0.000  120.958    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              428723274   95.597    0.000  118.887    0.000 overrides.py:1083(<genexpr>)
               16294134  105.646    0.000  105.646    0.000 {method 't' of 'torch._C._TensorBase' objects}
                1254092   99.139    0.000   99.139    0.000 {method 'ne' of 'torch._C._TensorBase' objects}
             1059677728   99.007    0.000   99.007    0.000 layer.py:183(isBlocking)
                1253592   35.622    0.000   94.588    0.000 random.py:315(sample)
                1253592    6.509    0.000   94.453    0.000 exploration.py:47(epsilonGreedy)
              118925598   63.579    0.000   93.676    0.000 layer.py:102(remove)
                7521552   91.726    0.000   91.726    0.000 {built-in method sum}
              139286438   63.419    0.000   87.466    0.000 layer.py:106(add)
                3760776   17.340    0.000   79.164    0.000 tensor.py:506(__rsub__)
                2507184   73.325    0.000   73.325    0.000 {built-in method torch._C._nn.mse_loss}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-10>
Subject: Job 9492735: <causal5_test_1> in cluster <dcc> Done

Job <causal5_test_1> was submitted from host <n-62-27-19> by user <s183905> in cluster <dcc> at Fri Apr  2 14:23:06 2021
Job was executed on host(s) <n-62-20-10>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Fri Apr  2 14:23:08 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Fri Apr  2 14:23:08 2021
Terminated at Fri Apr  2 20:23:44 2021
Results reported at Fri Apr  2 20:23:44 2021

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

    CPU time :                                   21252.95 sec.
    Max Memory :                                 2812 MB
    Average Memory :                             2756.98 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13572.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   21640 sec.
    Turnaround time :                            21638 sec.

The output (if any) is above this job summary.

