
# Parameters

    Name :                      Rock_level_hard_modresetlow-0
    Main :                      teleport
    Level :                     Levels.Rocks
    Hours :                     11.0
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
    Modified done chance :      0.02
    Miss intervention cost :    -0.2
    Intervention cost :         -0.05
    Replay size :               50000
    Sample size :               50
    Minutes used :              655 minutes.
    Hours used :                10 hours.

# Profiling


      35724714252 function calls (35595876949 primitive calls) in 39309.92 seconds

##    Ordered by: cumulative time
   List reduced from 470 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 39309.915 39309.915 {built-in method builtins.exec}
                      1    0.899    0.899 39309.915 39309.915 <string>:1(<module>)
                      1   98.517   98.517 39309.015 39309.015 main.py:13(teleport)
                2302291    9.324    0.000 14939.000    0.006 game.py:27(step)
                2302291   11.263    0.000 14399.032    0.006 layers.py:373(step)
                4604582   17.163    0.000 12780.975    0.003 agent.py:26(learn)
                4604582  337.135    0.000 10967.497    0.002 learner.py:42(Qlearn)
                2302291  182.948    0.000 10129.328    0.004 layers.py:18(step)
              230229100  483.196    0.000 9927.401    0.000 layer.py:74(move)
              230229100  734.701    0.000 7630.310    0.000 layers.py:390(check)
                2302291   75.190    0.000 7610.765    0.003 agent.py:50(_learn)
        144944662/16108370  575.201    0.000 5223.449    0.000 module.py:866(_call_impl)
                2302291   66.487    0.000 5144.343    0.002 agent.py:101(_learn)
               11503788   34.214    0.000 4864.424    0.000 network.py:24(forward)
               11503788  151.786    0.000 4761.665    0.000 container.py:117(forward)
                4604582   40.788    0.000 4628.127    0.001 optimizer.py:84(wrapper)
                4604582   18.417    0.000 4439.594    0.001 grad_mode.py:24(decorate_context)
                4604582  124.361    0.000 4378.425    0.001 adam.py:55(step)
              230229100 3871.685    0.000 4369.108    0.000 layers.py:76(check)
                2302292  234.841    0.000 4244.175    0.002 layers.py:344(update)
                4604582  906.702    0.000 4106.440    0.001 _functional.py:53(adam)
                2302291 1839.583    0.001 3345.354    0.001 replaybuffer.py:27(teleporter_save_data)
                4596915  102.639    0.000 3223.546    0.001 agent.py:45(__call__)
                2302291 1422.008    0.001 3012.732    0.001 agent.py:77(interveen)
                4604582   19.302    0.000 2703.402    0.001 tensor.py:195(backward)
                4604582   17.535    0.000 2683.422    0.001 __init__.py:68(backward)
                4604582 2563.594    0.001 2563.594    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2302291 1090.884    0.000 1772.685    0.001 agent.py:59(modify)
               20720628 1146.797    0.000 1746.161    0.000 layer.py:119(update)
               23007576   50.362    0.000 1730.835    0.000 conv.py:398(forward)
               23007576   29.479    0.000 1659.607    0.000 conv.py:390(_conv_forward)
               23007576 1630.128    0.000 1630.128    0.000 {built-in method conv2d}
                2302291  804.728    0.000 1608.838    0.001 replaybuffer.py:23(sample_data)
                5768421   51.932    0.000 1602.915    0.000 layers.py:394(restart)
              230229100  356.919    0.000 1595.534    0.000 layers.py:384(isFree)
               29906782   63.179    0.000 1360.396    0.000 linear.py:93(forward)
               29906782   24.793    0.000 1270.311    0.000 functional.py:1737(linear)
              103711628 1240.781    0.000 1240.781    0.000 {built-in method clone}
               29906782 1239.352    0.000 1239.352    0.000 {built-in method torch._C._nn.linear}
             1804892377 1019.033    0.000 1238.615    0.000 layer.py:71(isFree)
                5768421   24.009    0.000 1021.273    0.000 level.py:8(__init__)
                2302291   31.974    0.000  996.168    0.000 agent.py:96(__call__)
                6899206   43.917    0.000  987.097    0.000 agent.py:54(modify_board)
             3778180195  631.452    0.000  914.004    0.000 enum.py:646(__hash__)
                5768421  141.190    0.000  913.833    0.000 levels.py:95(generate)
               82882476  829.044    0.000  829.044    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               20712952  815.445    0.000  815.445    0.000 {built-in method cat}
               41410570   33.227    0.000  769.970    0.000 activation.py:713(forward)
                9528617  755.139    0.000  755.139    0.000 {built-in method tensor}
               82882476  740.825    0.000  740.825    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               41410570   33.711    0.000  736.743    0.000 functional.py:1364(leaky_relu)
               41410570  695.768    0.000  695.768    0.000 {built-in method torch._C._nn.leaky_relu}
                4604582  106.350    0.000  656.816    0.000 optimizer.py:189(zero_grad)
                2302291   42.534    0.000  650.789    0.000 replaybuffer.py:19(stacker)
                6899206  633.657    0.000  633.657    0.000 {built-in method torch._C._nn.one_hot}
                4604582    4.978    0.000  606.652    0.000 game.py:23(board)
              230229100  366.425    0.000  594.402    0.000 layers.py:216(check)
              230229100  354.473    0.000  584.351    0.000 layers.py:230(check)
              230229100  351.774    0.000  572.981    0.000 layers.py:244(check)
              230229200   61.474    0.000  571.279    0.000 {built-in method builtins.all}
              702264088  161.985    0.000  535.062    0.000 layers.py:350(<genexpr>)
               51915789   71.723    0.000  513.655    0.000 layer.py:48(restart)
               11536842   69.235    0.000  501.270    0.000 level.py:41(notUsed)
             5375459061  475.852    0.000  475.852    0.000 layer.py:67(positions)
                2302291  278.016    0.000  459.791    0.000 collector.py:54(collect)
               41441238  458.010    0.000  458.010    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              230229100  288.135    0.000  430.758    0.000 layers.py:63(check)
               41441238  399.875    0.000  399.875    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
             1620303208  394.227    0.000  394.227    0.000 layer.py:114(elements)
               41441238  384.142    0.000  384.142    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               41441238  375.731    0.000  375.731    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              790830216  275.643    0.000  373.166    0.000 layer.py:98(add)
              230229200  232.221    0.000  352.868    0.000 layers.py:110(isDone)
              110610834  343.157    0.000  343.157    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                4596915  121.169    0.000  335.308    0.000 exploration.py:53(softmaxer)
                8070712  118.356    0.000  332.086    0.000 random.py:315(sample)
              374316873  161.148    0.000  330.482    0.000 layer.py:94(remove)
               41441238  297.086    0.000  297.086    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              230229100  186.970    0.000  287.628    0.000 layers.py:203(check)
             3778197154  282.554    0.000  282.554    0.000 {built-in method builtins.hash}
                5768521  136.497    0.000  278.793    0.000 layers.py:33(reset)
              288421050  262.304    0.000  262.304    0.000 level.py:32(inverse)
              290088720  198.380    0.000  245.294    0.000 tensor.py:906(grad)
                4604582    6.796    0.000  220.996    0.000 loss.py:527(forward)
                4604582   16.028    0.000  214.200    0.000 functional.py:2898(mse_loss)
        2405159174/2405159172  170.343    0.000  204.715    0.000 {built-in method builtins.len}
               13813746  192.225    0.000  192.225    0.000 {built-in method sum}
              230229100   75.887    0.000  167.741    0.000 layers.py:99(<listcomp>)
             1804892377  167.646    0.000  167.646    0.000 layer.py:175(isBlocking)
             2450489055  164.205    0.000  164.205    0.000 {method 'append' of 'list' objects}
              288224838  112.333    0.000  161.676    0.000 random.py:250(_randbelow_with_getrandbits)
                4604582  142.077    0.000  142.077    0.000 {built-in method torch._C._nn.mse_loss}
              374316873  140.375    0.000  140.375    0.000 {method 'remove' of 'list' objects}
               23007576   15.468    0.000  131.656    0.000 flatten.py:39(forward)
               11536842    9.789    0.000  130.780    0.000 level.py:38(elementsIn)
                6906873    9.477    0.000  123.947    0.000 tensor.py:525(__rsub__)
                4605271  123.111    0.000  123.111    0.000 {built-in method max}
               23007576  116.188    0.000  116.188    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                6906873  112.714    0.000  112.714    0.000 {built-in method rsub}
                4596915  107.206    0.000  107.206    0.000 {built-in method multinomial}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-5>
Subject: Job 9444630: <Rock_level_hard_modresetlow_0> in cluster <dcc> Done

Job <Rock_level_hard_modresetlow_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun Mar 21 02:08:58 2021
Job was executed on host(s) <n-62-20-5>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Mar 21 13:04:27 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun Mar 21 13:04:27 2021
Terminated at Sun Mar 21 23:59:43 2021
Results reported at Sun Mar 21 23:59:43 2021

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

    CPU time :                                   39209.71 sec.
    Max Memory :                                 5557 MB
    Average Memory :                             4126.46 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               2635.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   39319 sec.
    Turnaround time :                            78645 sec.

The output (if any) is above this job summary.

