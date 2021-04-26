
# Parameters

    Name :                      MagicalLights2_convert3-1
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
    Cf convert :                3
    Counterfacts :              1
    Topn :                      1
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      51605677086 function calls (51339107531 primitive calls) in 86113.65 seconds

##    Ordered by: cumulative time
   List reduced from 514 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86113.649 86113.649 {built-in method builtins.exec}
                      1    4.087    4.087 86113.649 86113.649 <string>:1(<module>)
                      1  283.562  283.562 86109.562 86109.562 main.py:79(CFagent)
                7710924   28.562    0.000 24003.375    0.003 agent.py:29(learn)
                7710909  597.225    0.000 20044.336    0.003 learner.py:42(Qlearn)
                2570308 5209.039    0.002 18555.173    0.007 agent.py:210(counterfact)
                2570308   13.724    0.000 14361.309    0.006 game.py:41(step)
                2570308   15.780    0.000 13723.180    0.005 layers.py:718(step)
                2570309  411.678    0.000 13424.193    0.005 layers.py:684(update)
        297349531/30781667 1259.073    0.000 11386.994    0.000 module.py:866(_call_impl)
               23070758   68.200    0.000 10732.916    0.000 network.py:27(forward)
               23070758  343.722    0.000 10518.677    0.000 container.py:117(forward)
                2570308  262.174    0.000 9250.081    0.004 agent.py:54(_learn)
                2570308  260.130    0.000 8587.139    0.003 agent.py:202(_learn)
                7710909   72.617    0.000 8554.973    0.001 optimizer.py:84(wrapper)
                7710909   33.223    0.000 8227.413    0.001 grad_mode.py:24(decorate_context)
                7710909  228.673    0.000 8119.651    0.001 adam.py:55(step)
               23188646  217.033    0.000 7802.511    0.000 layers.py:740(restart)
                7710909 1673.988    0.000 7630.514    0.001 _functional.py:53(adam)
               62560419 6825.743    0.000 6825.743    0.000 {built-in method tensor}
               56571707   42.301    0.000 6668.616    0.000 game.py:37(board)
                2570308 4189.846    0.002 6125.829    0.002 replaybuffer.py:73(CF_save_data)
                2570308   79.486    0.000 6120.674    0.002 agent.py:117(_learn)
                7679876  212.432    0.000 5761.309    0.001 agent.py:49(__call__)
                2570308 2997.653    0.001 5630.689    0.002 replaybuffer.py:28(teleporter_save_data)
               23188646   97.417    0.000 5450.272    0.000 level.py:8(__init__)
               51406170 3466.097    0.000 5026.467    0.000 layer.py:151(update)
                7710909   31.819    0.000 4925.967    0.001 tensor.py:195(backward)
                7710909   29.858    0.000 4892.869    0.001 __init__.py:68(backward)
                2570308 2822.271    0.001 4762.439    0.002 agent.py:88(interveen)
                7710909 4684.110    0.001 4684.110    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               23188646  733.726    0.000 4594.237    0.000 levels.py:199(generate)
                2570308 3133.366    0.001 3969.228    0.002 replaybuffer.py:22(sample_data)
                2539372   61.520    0.000 3926.733    0.002 agent.py:175(choose_action)
                2570308 3101.258    0.001 3924.393    0.002 replaybuffer.py:67(sample_data)
               46141516  105.649    0.000 3754.186    0.000 conv.py:398(forward)
              280587446 3718.199    0.000 3718.199    0.000 {built-in method clone}
               46141516   59.846    0.000 3601.582    0.000 conv.py:390(_conv_forward)
               46141516 3541.736    0.000 3541.736    0.000 {built-in method conv2d}
               46377292  333.158    0.000 3156.914    0.000 level.py:41(notUsed)
               64071658  136.931    0.000 3061.293    0.000 linear.py:93(forward)
               64071658   53.211    0.000 2859.522    0.000 functional.py:1737(linear)
               64071658 2792.394    0.000 2792.394    0.000 {built-in method torch._C._nn.linear}
                2570308 1433.370    0.001 2205.628    0.001 agent.py:67(modify)
              231886460  285.969    0.000 2059.969    0.000 layer.py:69(restart)
               87142416   74.102    0.000 1718.320    0.000 activation.py:713(forward)
               87142416   73.968    0.000 1644.218    0.000 functional.py:1364(leaky_relu)
              143936948 1573.863    0.000 1573.863    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               87142416 1554.364    0.000 1554.364    0.000 {built-in method torch._C._nn.leaky_relu}
               10250184   71.139    0.000 1538.482    0.000 agent.py:59(modify_board)
               35953189 1500.950    0.000 1500.950    0.000 {built-in method cat}
              143936948 1374.502    0.000 1374.502    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                2570293   45.750    0.000 1348.541    0.001 agent.py:171(__call__)
              942622055 1278.815    0.000 1278.815    0.000 level.py:32(inverse)
                2570308   41.240    0.000 1256.574    0.000 agent.py:112(__call__)
               46377292   40.787    0.000 1207.508    0.000 level.py:38(elementsIn)
                7710909  185.474    0.000 1182.559    0.000 optimizer.py:189(zero_grad)
               23188746  581.312    0.000 1167.769    0.000 layers.py:36(reset)
              236412563  252.949    0.000 1099.384    0.000 {built-in method builtins.any}
              257030900  175.176    0.000 1095.417    0.000 {built-in method builtins.all}
             4314009847  722.690    0.000 1045.671    0.000 enum.py:646(__hash__)
               10250184  980.284    0.000  980.284    0.000 {built-in method torch._C._nn.one_hot}
             3058617547  958.343    0.000  958.343    0.000 layer.py:146(elements)
             1780809196  476.811    0.000  953.234    0.000 layers.py:690(<genexpr>)
              293407923  913.208    0.000  913.208    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
             2572264794  697.284    0.000  846.436    0.000 layers.py:700(<genexpr>)
               71968474  843.645    0.000  843.645    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               46377292  359.451    0.000  731.823    0.000 level.py:39(<listcomp>)
               71968474  730.530    0.000  730.530    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               71968474  708.395    0.000  708.395    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
             1477911267  517.691    0.000  703.580    0.000 layer.py:130(add)
               71968474  703.018    0.000  703.018    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               23188646  317.917    0.000  686.653    0.000 level.py:16(<dictcomp>)
               51517908  262.864    0.000  677.799    0.000 random.py:315(sample)
                2539372  617.487    0.000  657.430    0.000 agent.py:186(convert_values)
                2570308   44.113    0.000  650.033    0.000 replaybuffer.py:18(stacker)
                2570293   46.972    0.000  642.877    0.000 replaybuffer.py:63(stacker)
                7679876  219.220    0.000  591.598    0.000 exploration.py:53(softmaxer)
               26849162  568.908    0.000  588.508    0.000 layer.py:126(remove)
               46470245  565.317    0.000  565.317    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                2570308  332.650    0.000  550.859    0.000 collector.py:46(collect)
               71968474  546.152    0.000  546.152    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
        6419895455/6419895452  440.066    0.000  495.412    0.000 {built-in method builtins.len}
             2504375366  470.532    0.000  470.532    0.000 enum.py:352(<genexpr>)
               46377292  255.982    0.000  434.898    0.000 {built-in method _functools.reduce}
              503779402  345.916    0.000  434.516    0.000 tensor.py:906(grad)
                7710909   12.937    0.000  387.950    0.000 loss.py:527(forward)
                7710909   28.884    0.000  375.013    0.000 functional.py:2898(mse_loss)
             4314039334  322.987    0.000  322.987    0.000 {built-in method builtins.hash}
              257030900  182.806    0.000  296.016    0.000 layers.py:113(isDone)
             4175282133  289.533    0.000  289.533    0.000 {method 'append' of 'list' objects}
              422514514  198.997    0.000  289.088    0.000 random.py:250(_randbelow_with_getrandbits)
               46141516   31.490    0.000  278.057    0.000 flatten.py:39(forward)
                2570308   67.590    0.000  263.705    0.000 layers.py:17(step)
                7710909  249.395    0.000  249.395    0.000 {built-in method torch._C._nn.mse_loss}
               46141516  246.567    0.000  246.567    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
             1901477992  242.010    0.000  242.010    0.000 layer.py:182(grid)
               15421848  232.107    0.000  232.107    0.000 {built-in method sum}
                5140618  226.418    0.000  226.418    0.000 {built-in method nonzero}
                7711933  220.336    0.000  220.336    0.000 {built-in method max}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9571369: <MagicalLights2_convert3_1> in cluster <dcc> Done

Job <MagicalLights2_convert3_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sat Apr 24 18:36:26 2021
Job was executed on host(s) <n-62-11-16>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sat Apr 24 18:36:28 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat Apr 24 18:36:28 2021
Terminated at Sun Apr 25 18:31:53 2021
Results reported at Sun Apr 25 18:31:53 2021

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

    CPU time :                                   85901.87 sec.
    Max Memory :                                 8349 MB
    Average Memory :                             5835.09 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               8035.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86125 sec.
    Turnaround time :                            86127 sec.

The output (if any) is above this job summary.

