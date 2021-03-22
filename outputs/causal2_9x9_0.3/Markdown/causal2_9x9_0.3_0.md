
# Parameters

    Name :                      causal2_9x9_0.3-0
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


      32268746414 function calls (32164305907 primitive calls) in 35713.10 seconds

##    Ordered by: cumulative time
   List reduced from 459 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35713.103 35713.103 {built-in method builtins.exec}
                      1    0.907    0.907 35713.103 35713.103 <string>:1(<module>)
                      1   75.175   75.175 35712.195 35712.195 main.py:13(teleport)
                3730042   12.328    0.000 9610.556    0.003 agent.py:26(learn)
                1865021    6.533    0.000 8865.759    0.005 game.py:27(step)
                1865021    8.193    0.000 8452.129    0.005 layers.py:373(step)
                3730042  227.944    0.000 8223.995    0.002 learner.py:42(Qlearn)
                1865021 4574.445    0.002 8141.427    0.004 replaybuffer.py:27(teleporter_save_data)
                1865021   53.215    0.000 5740.947    0.003 agent.py:50(_learn)
                1865021  134.256    0.000 4735.635    0.003 layers.py:18(step)
                1865021 3437.061    0.002 4694.045    0.003 agent.py:77(interveen)
              186502100  375.619    0.000 4586.982    0.000 layer.py:74(move)
        117494503/13055007  415.183    0.000 4051.265    0.000 module.py:715(_call_impl)
                1865021   46.345    0.000 3849.397    0.002 agent.py:101(_learn)
                9324965   22.303    0.000 3783.207    0.000 network.py:24(forward)
                9324965   98.367    0.000 3709.085    0.000 container.py:115(forward)
                1865022  182.627    0.000 3696.930    0.002 layers.py:344(update)
                3730042   20.844    0.000 3316.987    0.001 grad_mode.py:23(decorate_context)
                3730042  108.780    0.000 3257.811    0.001 adam.py:55(step)
              299700448 2796.900    0.000 2796.900    0.000 {built-in method clone}
              186502100  477.680    0.000 2783.287    0.000 layers.py:390(check)
                3730042  594.042    0.000 2661.408    0.001 functional.py:53(adam)
                3729902   70.510    0.000 2503.941    0.001 agent.py:45(__call__)
                3730042   21.092    0.000 1900.865    0.001 tensor.py:181(backward)
                3730042   12.592    0.000 1879.773    0.001 __init__.py:68(backward)
                3730042 1787.436    0.000 1787.436    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                6954992   56.213    0.000 1777.433    0.000 layers.py:394(restart)
                1865021  660.394    0.000 1519.831    0.001 replaybuffer.py:23(sample_data)
                1865021  768.579    0.000 1482.435    0.001 agent.py:59(modify)
               18649930   30.219    0.000 1378.912    0.000 conv.py:422(forward)
               18649930   37.019    0.000 1337.726    0.000 conv.py:414(_conv_forward)
               18649930 1294.776    0.000 1294.776    0.000 {built-in method conv2d}
                6954992   25.620    0.000 1261.058    0.000 level.py:8(__init__)
               16785198  755.056    0.000 1187.890    0.000 layer.py:119(update)
               24244853   49.093    0.000 1186.035    0.000 linear.py:92(forward)
              186502100  304.907    0.000 1158.272    0.000 layers.py:384(isFree)
                6954992   70.638    0.000 1138.626    0.000 levels.py:151(generate)
               24244853   83.917    0.000 1114.537    0.000 functional.py:1669(linear)
               33384850  226.301    0.000  992.288    0.000 level.py:41(notUsed)
              234992700  531.284    0.000  873.311    0.000 tensor.py:933(grad)
               16785049  865.602    0.000  865.602    0.000 {built-in method cat}
             1642693772  667.667    0.000  853.366    0.000 layer.py:71(isFree)
               24244853  786.522    0.000  786.522    0.000 {built-in method addmm}
              305295371  786.269    0.000  786.269    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
             3351805750  537.635    0.000  780.223    0.000 enum.py:646(__hash__)
                1865021   20.421    0.000  772.415    0.000 agent.py:96(__call__)
                5594923   32.728    0.000  766.550    0.000 agent.py:54(modify_board)
                3730042   71.454    0.000  756.219    0.000 optimizer.py:167(zero_grad)
                1865021   31.640    0.000  736.119    0.000 replaybuffer.py:19(stacker)
                7734004  586.313    0.000  586.313    0.000 {built-in method tensor}
               67140756  538.991    0.000  538.991    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               33569818   26.055    0.000  513.046    0.000 activation.py:713(forward)
                5594923  495.222    0.000  495.222    0.000 {built-in method torch._C._nn.one_hot}
              193963132   62.471    0.000  488.326    0.000 {built-in method builtins.all}
               33569818   41.755    0.000  486.991    0.000 functional.py:1292(leaky_relu)
                3730042    3.805    0.000  479.547    0.000 game.py:23(board)
              186502100  297.800    0.000  473.870    0.000 layers.py:230(check)
              186502100  294.798    0.000  473.001    0.000 layers.py:216(check)
              186502100  289.536    0.000  466.399    0.000 layers.py:244(check)
              300268581  153.025    0.000  451.383    0.000 overrides.py:1070(has_torch_function)
               67140756  444.655    0.000  444.655    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              613676278  141.247    0.000  442.572    0.000 layers.py:350(<genexpr>)
               33569818  441.255    0.000  441.255    0.000 {built-in method torch._C._nn.leaky_relu}
               62594928   40.404    0.000  441.014    0.000 layer.py:48(restart)
              186502100  287.682    0.000  398.163    0.000 layers.py:76(check)
             4442808113  364.929    0.000  364.929    0.000 layer.py:67(positions)
                6955092  164.831    0.000  336.239    0.000 layers.py:33(reset)
               33384850   20.954    0.000  330.443    0.000 level.py:38(elementsIn)
             1602885487  322.864    0.000  322.864    0.000 level.py:32(inverse)
               33570378  312.342    0.000  312.342    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                1865021  181.480    0.000  311.075    0.000 collector.py:54(collect)
               33570378  283.642    0.000  283.642    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              331973519  114.875    0.000  282.220    0.000 {built-in method builtins.any}
              186502200  185.257    0.000  280.184    0.000 layers.py:110(isDone)
              902587654  275.851    0.000  275.851    0.000 layer.py:114(elements)
                3729902   96.070    0.000  258.927    0.000 exploration.py:53(softmaxer)
               33570378  255.237    0.000  255.237    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
             3351819541  242.591    0.000  242.591    0.000 {built-in method builtins.hash}
              186502100  150.933    0.000  230.608    0.000 layers.py:203(check)
              437971753  164.019    0.000  223.178    0.000 layer.py:98(add)
               33570378  222.759    0.000  222.759    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              186502100  142.118    0.000  217.573    0.000 layers.py:63(check)
               33384850   98.626    0.000  198.551    0.000 level.py:39(<listcomp>)
                7460932   32.312    0.000  192.817    0.000 tensor.py:21(wrapped)
               33570378  175.563    0.000  175.563    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                3730042    4.630    0.000  169.320    0.000 loss.py:445(forward)
              632242575  132.714    0.000  165.036    0.000 overrides.py:1083(<genexpr>)
                3730042   19.147    0.000  164.690    0.000 functional.py:2637(mse_loss)
        1618075786/1618075784  108.125    0.000  157.516    0.000 {built-in method builtins.len}
             1642693772  143.688    0.000  143.688    0.000 layer.py:175(isBlocking)
               24244853  141.127    0.000  141.127    0.000 {method 't' of 'torch._C._TensorBase' objects}
              196213228   86.225    0.000  127.163    0.000 layer.py:94(remove)
               11190126  124.970    0.000  124.970    0.000 {built-in method sum}
                1865021   44.513    0.000  119.966    0.000 random.py:315(sample)
               33384850   69.441    0.000  110.938    0.000 {built-in method _functools.reduce}
              605097635  107.982    0.000  107.982    0.000 enum.py:352(<genexpr>)
                5595063   24.720    0.000  107.797    0.000 tensor.py:506(__rsub__)
               18649930   12.656    0.000   96.338    0.000 flatten.py:39(forward)
                3730042   95.174    0.000   95.174    0.000 {built-in method torch._C._nn.mse_loss}
             1277162646   94.216    0.000   94.216    0.000 {method 'append' of 'list' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-2>
Subject: Job 9447953: <causal2_9x9_0.3_0> in cluster <dcc> Done

Job <causal2_9x9_0.3_0> was submitted from host <n-62-30-1> by user <s183905> in cluster <dcc> at Mon Mar 22 13:28:55 2021
Job was executed on host(s) <n-62-20-2>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Mon Mar 22 13:28:55 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Mar 22 13:28:55 2021
Terminated at Mon Mar 22 23:24:16 2021
Results reported at Mon Mar 22 23:24:16 2021

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

    CPU time :                                   35620.27 sec.
    Max Memory :                                 2448 MB
    Average Memory :                             2440.68 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               5744.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35779 sec.
    Turnaround time :                            35721 sec.

The output (if any) is above this job summary.

