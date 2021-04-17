
# Parameters

    Name :                      Rock_level_hard_misslow-0
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
    Modified done chance :      0.05
    Miss intervention cost :    -0.1
    Intervention cost :         -0.05
    Replay size :               50000
    Sample size :               50
    Minutes used :              655 minutes.
    Hours used :                10 hours.

# Profiling


      39304910450 function calls (39167569575 primitive calls) in 39310.70 seconds

##    Ordered by: cumulative time
   List reduced from 470 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 39310.705 39310.705 {built-in method builtins.exec}
                      1    0.909    0.909 39310.705 39310.705 <string>:1(<module>)
                      1   99.042   99.042 39309.796 39309.796 main.py:13(teleport)
                2452543    8.194    0.000 16037.267    0.007 game.py:27(step)
                2452543   11.621    0.000 15519.609    0.006 layers.py:373(step)
                2452543  188.695    0.000 10728.960    0.004 layers.py:18(step)
              245254300  531.511    0.000 10519.956    0.000 layer.py:74(move)
                4905086   16.688    0.000 10311.945    0.002 agent.py:26(learn)
                4905086  274.717    0.000 8668.676    0.002 learner.py:42(Qlearn)
              245254300  736.255    0.000 8048.468    0.000 layers.py:390(check)
                2452543   79.449    0.000 6164.389    0.003 agent.py:50(_learn)
                2452543 2831.300    0.001 4795.584    0.002 replaybuffer.py:27(teleporter_save_data)
                2452544  250.284    0.000 4764.077    0.002 layers.py:344(update)
              245254300 4070.343    0.000 4666.629    0.000 layers.py:76(check)
        154507453/17167589  555.182    0.000 4637.378    0.000 module.py:866(_call_impl)
               12262503   32.607    0.000 4311.136    0.000 network.py:24(forward)
               12262503  136.989    0.000 4207.723    0.000 container.py:117(forward)
                2452543   69.868    0.000 4119.169    0.002 agent.py:101(_learn)
                2452543 1953.836    0.001 3371.648    0.001 agent.py:77(interveen)
                4905086   38.227    0.000 3345.654    0.001 optimizer.py:84(wrapper)
                4905086   18.950    0.000 3175.138    0.001 grad_mode.py:24(decorate_context)
                4905086  123.920    0.000 3113.452    0.001 adam.py:55(step)
                4904874  105.257    0.000 2871.252    0.001 agent.py:45(__call__)
                4905086  650.154    0.000 2840.090    0.001 _functional.py:53(adam)
                4905086   18.855    0.000 2230.143    0.000 tensor.py:195(backward)
                4905086   18.780    0.000 2210.635    0.000 __init__.py:68(backward)
                4905086 2104.125    0.000 2104.125    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
               22072896 1302.067    0.000 1954.734    0.000 layer.py:119(update)
                6801371   58.072    0.000 1859.884    0.000 layers.py:394(restart)
              245254300  363.192    0.000 1698.453    0.000 layers.py:384(isFree)
                2452543  866.648    0.000 1663.767    0.001 replaybuffer.py:23(sample_data)
              198177728 1619.648    0.000 1619.648    0.000 {built-in method clone}
               24525006   52.371    0.000 1593.739    0.000 conv.py:398(forward)
               24525006   30.969    0.000 1519.548    0.000 conv.py:390(_conv_forward)
                2452543  912.783    0.000 1499.894    0.001 agent.py:59(modify)
               24525006 1488.579    0.000 1488.579    0.000 {built-in method conv2d}
             1922406059 1098.385    0.000 1335.261    0.000 layer.py:71(isFree)
                6801371   26.260    0.000 1179.485    0.000 level.py:8(__init__)
               31882423   63.449    0.000 1169.652    0.000 linear.py:93(forward)
               31882423   24.622    0.000 1078.280    0.000 functional.py:1737(linear)
                6801371  163.090    0.000 1057.385    0.000 levels.py:95(generate)
               31882423 1047.741    0.000 1047.741    0.000 {built-in method torch._C._nn.linear}
             4096988637  673.858    0.000  972.232    0.000 enum.py:646(__hash__)
                2452543   32.013    0.000  894.457    0.000 agent.py:96(__call__)
                7357417   40.789    0.000  878.858    0.000 agent.py:54(modify_board)
               22072675  770.253    0.000  770.253    0.000 {built-in method cat}
               10145783  743.585    0.000  743.585    0.000 {built-in method tensor}
                2452543   40.950    0.000  634.334    0.000 replaybuffer.py:19(stacker)
               44144926   32.014    0.000  625.131    0.000 activation.py:713(forward)
              245254300  382.430    0.000  623.187    0.000 layers.py:216(check)
                4905086    4.689    0.000  618.065    0.000 game.py:23(board)
              245254400   67.279    0.000  605.728    0.000 {built-in method builtins.all}
              245254300  366.720    0.000  604.456    0.000 layers.py:230(check)
               61212339   83.154    0.000  604.164    0.000 layer.py:48(restart)
               44144926   35.393    0.000  593.117    0.000 functional.py:1364(leaky_relu)
              245254300  361.577    0.000  591.869    0.000 layers.py:244(check)
               13602742   76.858    0.000  580.822    0.000 level.py:41(notUsed)
                7357417  579.892    0.000  579.892    0.000 {built-in method torch._C._nn.one_hot}
              757286058  170.282    0.000  566.152    0.000 layers.py:350(<genexpr>)
               44144926  550.916    0.000  550.916    0.000 {built-in method torch._C._nn.leaky_relu}
               88291548  539.039    0.000  539.039    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                4905086   89.762    0.000  500.142    0.000 optimizer.py:189(zero_grad)
               88291548  495.642    0.000  495.642    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
             5722357337  493.629    0.000  493.629    0.000 layer.py:67(positions)
              245254300  307.990    0.000  465.526    0.000 layers.py:63(check)
              937135406  327.482    0.000  441.723    0.000 layer.py:98(add)
             1913665766  434.841    0.000  434.841    0.000 layer.py:114(elements)
              449407897  196.002    0.000  405.976    0.000 layer.py:94(remove)
              205535145  391.556    0.000  391.556    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              245254400  245.321    0.000  374.565    0.000 layers.py:110(isDone)
                9253914  132.088    0.000  371.344    0.000 random.py:315(sample)
                2452543  195.582    0.000  333.674    0.000 collector.py:54(collect)
               44145774  332.315    0.000  332.315    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                6801471  163.763    0.000  330.554    0.000 layers.py:33(reset)
              340068550  309.187    0.000  309.187    0.000 level.py:32(inverse)
              245254300  195.259    0.000  301.522    0.000 layers.py:203(check)
             4097006676  298.377    0.000  298.377    0.000 {built-in method builtins.hash}
                4904874  108.289    0.000  288.489    0.000 exploration.py:53(softmaxer)
               44145774  283.583    0.000  283.583    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               44145774  264.576    0.000  264.576    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               44145774  263.888    0.000  263.888    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              309020472  190.335    0.000  235.663    0.000 tensor.py:906(grad)
              245254300   91.786    0.000  208.542    0.000 layers.py:99(<listcomp>)
        2547956495/2547956493  166.566    0.000  198.643    0.000 {built-in method builtins.len}
               44145774  192.971    0.000  192.971    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                4905086    6.342    0.000  192.099    0.000 loss.py:527(forward)
             2882631346  190.506    0.000  190.506    0.000 {method 'append' of 'list' objects}
                4905086   17.159    0.000  185.756    0.000 functional.py:2898(mse_loss)
              326729303  127.827    0.000  183.665    0.000 random.py:250(_randbelow_with_getrandbits)
             1922406059  182.193    0.000  182.193    0.000 layer.py:175(isBlocking)
              449407897  174.533    0.000  174.533    0.000 {method 'remove' of 'list' objects}
               13602742   10.989    0.000  148.338    0.000 level.py:38(elementsIn)
               14715258  144.720    0.000  144.720    0.000 {built-in method sum}
                4905086  114.055    0.000  114.055    0.000 {built-in method torch._C._nn.mse_loss}
               24525006   17.600    0.000  108.437    0.000 flatten.py:39(forward)
                4905821  106.758    0.000  106.758    0.000 {built-in method max}
                7357629    8.970    0.000  100.273    0.000 tensor.py:525(__rsub__)
               24525006   90.837    0.000   90.837    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                4904874   90.477    0.000   90.477    0.000 {built-in method multinomial}
                7357629   89.644    0.000   89.644    0.000 {built-in method rsub}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-4>
Subject: Job 9444631: <Rock_level_hard_misslow_0> in cluster <dcc> Done

Job <Rock_level_hard_misslow_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun Mar 21 02:08:58 2021
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Mar 21 13:04:27 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun Mar 21 13:04:27 2021
Terminated at Sun Mar 21 23:59:45 2021
Results reported at Sun Mar 21 23:59:45 2021

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

    CPU time :                                   39212.14 sec.
    Max Memory :                                 5733 MB
    Average Memory :                             4245.18 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               2459.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   39318 sec.
    Turnaround time :                            78647 sec.

The output (if any) is above this job summary.

