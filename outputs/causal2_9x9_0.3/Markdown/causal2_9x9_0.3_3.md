
# Parameters

    Name :                      causal2_9x9_0.3-3
    Main :                      teleport
    Level :                     Levels.Causal2
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
    Layer gold :                False
    Layer keys :                False
    Layer door :                False
    Layer holder :              False
    Layer putter :              False
    Layer rock :                True
    Layer dirt :                True
    Layer diamond1 :            True
    Layer diamond2 :            True
    Layer diamond3 :            True
    Layer diamond4 :            True
    K :                         200000
    Epsilon cap :               0.1
    Softmax cap :               0.02
    Gamma :                     0.98
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.2
    Intervention cost :         -0.05
    Replay size :               50000
    Sample size :               50
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      26612067679 function calls (26525312416 primitive calls) in 35711.20 seconds

##    Ordered by: cumulative time
   List reduced from 459 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35711.200 35711.200 {built-in method builtins.exec}
                      1    0.916    0.916 35711.200 35711.200 <string>:1(<module>)
                      1   65.627   65.627 35710.284 35710.284 main.py:13(teleport)
                3098424   11.302    0.000 10255.086    0.003 agent.py:26(learn)
                3098424  243.436    0.000 8896.296    0.003 learner.py:42(Qlearn)
                1549212 4656.580    0.003 8756.944    0.006 replaybuffer.py:27(teleporter_save_data)
                1549212    6.273    0.000 7468.508    0.005 game.py:27(step)
                1549212    7.377    0.000 7086.670    0.005 layers.py:373(step)
                1549212   45.875    0.000 6106.436    0.004 agent.py:50(_learn)
                1549212 3741.643    0.002 4992.674    0.003 agent.py:77(interveen)
                1549212   40.449    0.000 4130.789    0.003 agent.py:101(_learn)
        97598601/10844349  385.200    0.000 4068.375    0.000 module.py:715(_call_impl)
                1549212  109.191    0.000 4038.391    0.003 layers.py:18(step)
              154921200  330.241    0.000 3916.442    0.000 layer.py:74(move)
                7745925   20.342    0.000 3807.976    0.000 network.py:24(forward)
                3098424   17.810    0.000 3791.105    0.001 grad_mode.py:23(decorate_context)
                7745925   97.017    0.000 3744.271    0.000 container.py:115(forward)
                3098424   97.096    0.000 3739.809    0.001 adam.py:55(step)
                3098424  681.393    0.000 3199.353    0.001 functional.py:53(adam)
              240532266 3161.951    0.000 3161.951    0.000 {built-in method clone}
                1549213  160.809    0.000 3031.724    0.002 layers.py:344(update)
                3098289   65.425    0.000 2486.963    0.001 agent.py:45(__call__)
              154921200  400.789    0.000 2343.569    0.000 layers.py:390(check)
                3098424   19.054    0.000 2011.973    0.001 tensor.py:181(backward)
                3098424   10.134    0.000 1992.919    0.001 __init__.py:68(backward)
                3098424 1905.128    0.001 1905.128    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                1549212  810.421    0.001 1527.313    0.001 agent.py:59(modify)
                5602804   45.865    0.000 1437.770    0.000 layers.py:394(restart)
               15491850   25.956    0.000 1344.651    0.000 conv.py:422(forward)
                1549212  541.823    0.000 1311.744    0.001 replaybuffer.py:23(sample_data)
               15491850   29.318    0.000 1309.338    0.000 conv.py:414(_conv_forward)
               15491850 1275.065    0.000 1275.065    0.000 {built-in method conv2d}
               20139351   45.265    0.000 1219.654    0.000 linear.py:92(forward)
               20139351   78.597    0.000 1155.644    0.000 functional.py:1669(linear)
                5602804   21.107    0.000 1018.724    0.000 level.py:8(__init__)
              154921200  270.632    0.000 1015.544    0.000 layers.py:384(isFree)
              245179767  969.692    0.000  969.692    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               13942917  612.750    0.000  967.388    0.000 layer.py:119(update)
                5602804   58.050    0.000  920.292    0.000 levels.py:151(generate)
              195200766  537.399    0.000  831.904    0.000 tensor.py:933(grad)
               20139351  824.670    0.000  824.670    0.000 {built-in method addmm}
               13942773  805.254    0.000  805.254    0.000 {built-in method cat}
               26894689  183.227    0.000  802.383    0.000 level.py:41(notUsed)
                3098424   77.268    0.000  797.241    0.000 optimizer.py:167(zero_grad)
                1549212   18.823    0.000  771.658    0.000 agent.py:96(__call__)
             1362180344  585.718    0.000  744.912    0.000 layer.py:71(isFree)
                4647501   32.025    0.000  743.603    0.000 agent.py:54(modify_board)
               55771632  667.642    0.000  667.642    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                1549212   27.148    0.000  666.030    0.000 replaybuffer.py:19(stacker)
             2765574322  458.238    0.000  660.731    0.000 enum.py:646(__hash__)
               55771632  569.110    0.000  569.110    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               27885276   21.979    0.000  559.712    0.000 activation.py:713(forward)
               27885276   36.707    0.000  537.733    0.000 functional.py:1292(leaky_relu)
                6438592  528.403    0.000  528.403    0.000 {built-in method tensor}
               27885276  497.360    0.000  497.360    0.000 {built-in method torch._C._nn.leaky_relu}
                4647501  465.101    0.000  465.101    0.000 {built-in method torch._C._nn.one_hot}
                3098424    3.563    0.000  417.522    0.000 game.py:23(board)
              161118872   51.272    0.000  416.281    0.000 {built-in method builtins.all}
              154921200  246.757    0.000  399.577    0.000 layers.py:216(check)
              154921200  243.449    0.000  397.611    0.000 layers.py:230(check)
              154921200  246.613    0.000  397.163    0.000 layers.py:244(check)
              249423286  136.240    0.000  387.745    0.000 overrides.py:1070(has_torch_function)
              508540403  120.784    0.000  378.437    0.000 layers.py:350(<genexpr>)
               27885816  367.790    0.000  367.790    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               50425236   32.540    0.000  357.310    0.000 layer.py:48(restart)
                1549212  211.486    0.000  353.239    0.000 collector.py:54(collect)
              154921200  239.941    0.000  333.646    0.000 layers.py:76(check)
               27885816  328.524    0.000  328.524    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
             3690431912  324.257    0.000  324.257    0.000 layer.py:67(positions)
               27885816  304.295    0.000  304.295    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                5602904  136.921    0.000  272.871    0.000 layers.py:33(reset)
               27885816  271.983    0.000  271.983    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               26894689   17.526    0.000  268.796    0.000 level.py:38(elementsIn)
                3098289   95.794    0.000  266.340    0.000 exploration.py:53(softmaxer)
             1291279919  260.752    0.000  260.752    0.000 level.py:32(inverse)
              154921300  155.867    0.000  239.728    0.000 layers.py:110(isDone)
              275759486   98.045    0.000  238.138    0.000 {built-in method builtins.any}
              736499785  224.085    0.000  224.085    0.000 layer.py:114(elements)
               27885816  218.505    0.000  218.505    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
             2765585809  202.495    0.000  202.495    0.000 {built-in method builtins.hash}
              154921200  125.795    0.000  195.278    0.000 layers.py:203(check)
                6197572   29.378    0.000  188.990    0.000 tensor.py:21(wrapped)
              154921200  116.918    0.000  181.908    0.000 layers.py:63(check)
              357095010  131.456    0.000  177.518    0.000 layer.py:98(add)
                3098424    4.382    0.000  171.179    0.000 loss.py:445(forward)
                3098424   16.558    0.000  166.797    0.000 functional.py:2637(mse_loss)
               20139351  162.862    0.000  162.862    0.000 {method 't' of 'torch._C._TensorBase' objects}
               26894689   79.874    0.000  160.774    0.000 level.py:39(<listcomp>)
        1346852722/1346852720   94.874    0.000  141.018    0.000 {built-in method builtins.len}
                9295272  140.368    0.000  140.368    0.000 {built-in method sum}
              525183186  111.253    0.000  138.180    0.000 overrides.py:1083(<genexpr>)
             1362180344  121.362    0.000  121.362    0.000 layer.py:175(isBlocking)
                4647636   23.122    0.000  111.973    0.000 tensor.py:506(__rsub__)
              161709331   73.511    0.000  106.979    0.000 layer.py:94(remove)
                3098424  103.355    0.000  103.355    0.000 {built-in method torch._C._nn.mse_loss}
               15491850   10.955    0.000  103.285    0.000 flatten.py:39(forward)
                1549212   37.679    0.000  100.986    0.000 random.py:315(sample)
                4647636   98.460    0.000   98.460    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                3098887   93.111    0.000   93.111    0.000 {built-in method max}
               15491850   92.330    0.000   92.330    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}


Traceback (most recent call last):
  File "main.py", line 111, in <module>
    run(Defaults)
  File "/zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/auxillaries.py", line 132, in run
    (serverRun if isServer else Defaults.main).__call__(getvals(Defaults))
  File "/zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils/server.py", line 36, in serverRun
    profilingStats()
  File "/zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils/debug.py", line 62, in profilingStats
    os.remove('stats')
FileNotFoundError: [Errno 2] No such file or directory: 'stats'

------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-5>
Subject: Job 9447956: <causal2_9x9_0.3_3> in cluster <dcc> Exited

Job <causal2_9x9_0.3_3> was submitted from host <n-62-30-1> by user <s183905> in cluster <dcc> at Mon Mar 22 13:28:55 2021
Job was executed on host(s) <n-62-20-5>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Mon Mar 22 13:28:57 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Mar 22 13:28:57 2021
Terminated at Mon Mar 22 23:24:14 2021
Results reported at Mon Mar 22 23:24:14 2021

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

Exited with exit code 1.

Resource usage summary:

    CPU time :                                   35617.66 sec.
    Max Memory :                                 2450 MB
    Average Memory :                             2444.38 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               5742.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35778 sec.
    Turnaround time :                            35719 sec.

The output (if any) is above this job summary.

