
# Parameters

    Name :                      Rock_level_hard_softlow-0
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
    Softmax cap :               0.01
    Gamma :                     0.98
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.2
    Intervention cost :         -0.05
    Replay size :               50000
    Sample size :               50
    Minutes used :              655 minutes.
    Hours used :                10 hours.

# Profiling


      39756886184 function calls (39617665445 primitive calls) in 39312.03 seconds

##    Ordered by: cumulative time
   List reduced from 470 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 39312.030 39312.030 {built-in method builtins.exec}
                      1    0.917    0.917 39312.030 39312.030 <string>:1(<module>)
                      1   96.798   96.798 39311.113 39311.113 main.py:13(teleport)
                2486088    8.854    0.000 16381.495    0.007 game.py:27(step)
                2486088   11.569    0.000 15861.201    0.006 layers.py:373(step)
                2486088  196.705    0.000 10491.076    0.004 layers.py:18(step)
                4972176   16.878    0.000 10451.180    0.002 agent.py:26(learn)
              248608800  478.943    0.000 10273.268    0.000 layer.py:74(move)
                4972176  274.304    0.000 8842.387    0.002 learner.py:42(Qlearn)
              248608800  765.068    0.000 8107.459    0.000 layers.py:390(check)
                2486088   70.172    0.000 6232.069    0.003 agent.py:50(_learn)
                2486089  254.930    0.000 5343.719    0.002 layers.py:344(update)
              248608800 4157.991    0.000 4633.931    0.000 layers.py:76(check)
        156622244/17402516  565.704    0.000 4590.028    0.000 module.py:866(_call_impl)
                2486088 2589.643    0.001 4439.914    0.002 replaybuffer.py:27(teleporter_save_data)
               12430340   33.459    0.000 4257.286    0.000 network.py:24(forward)
                2486088   61.240    0.000 4193.280    0.002 agent.py:101(_learn)
               12430340  132.260    0.000 4151.766    0.000 container.py:117(forward)
                4972176   39.123    0.000 3461.482    0.001 optimizer.py:84(wrapper)
                4972176   20.279    0.000 3285.702    0.001 grad_mode.py:24(decorate_context)
                2486088 1853.265    0.001 3268.246    0.001 agent.py:77(interveen)
                4972176  127.530    0.000 3220.816    0.001 adam.py:55(step)
                4972176  662.927    0.000 2939.076    0.001 _functional.py:53(adam)
                4972076   95.875    0.000 2853.275    0.001 agent.py:45(__call__)
                8581919   77.619    0.000 2378.728    0.000 layers.py:394(restart)
                4972176   21.882    0.000 2305.231    0.000 tensor.py:195(backward)
                4972176   18.120    0.000 2282.657    0.000 __init__.py:68(backward)
                4972176 2174.753    0.000 2174.753    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
               22374801 1334.139    0.000 2001.343    0.000 layer.py:119(update)
                2486088  854.982    0.000 1591.371    0.001 replaybuffer.py:23(sample_data)
               24860680   51.860    0.000 1563.318    0.000 conv.py:398(forward)
                2486088  946.079    0.000 1540.905    0.001 agent.py:59(modify)
              188365956 1540.139    0.000 1540.139    0.000 {built-in method clone}
              248608800  333.063    0.000 1524.683    0.000 layers.py:384(isFree)
                8581919   33.072    0.000 1502.848    0.000 level.py:8(__init__)
               24860680   30.014    0.000 1487.306    0.000 conv.py:390(_conv_forward)
               24860680 1457.292    0.000 1457.292    0.000 {built-in method conv2d}
                8581919  211.386    0.000 1348.397    0.000 levels.py:95(generate)
             1680367430  987.089    0.000 1191.620    0.000 layer.py:71(isFree)
               32318844   62.733    0.000 1157.905    0.000 linear.py:93(forward)
               32318844   25.078    0.000 1066.662    0.000 functional.py:1737(linear)
             4332227927  720.859    0.000 1041.253    0.000 enum.py:646(__hash__)
               32318844 1035.690    0.000 1035.690    0.000 {built-in method torch._C._nn.linear}
                7458164   41.916    0.000  893.800    0.000 agent.py:54(modify_board)
                2486088   28.086    0.000  888.120    0.000 agent.py:96(__call__)
               77237271  107.354    0.000  774.636    0.000 layer.py:48(restart)
               10283334  749.878    0.000  749.878    0.000 {built-in method tensor}
               17163838   98.094    0.000  736.795    0.000 level.py:41(notUsed)
               22374692  711.896    0.000  711.896    0.000 {built-in method cat}
              248608800  390.765    0.000  639.020    0.000 layers.py:216(check)
                4972176    5.083    0.000  625.526    0.000 game.py:23(board)
              248608800  371.728    0.000  615.083    0.000 layers.py:230(check)
              248608900   65.950    0.000  611.205    0.000 {built-in method builtins.all}
               44749184   35.045    0.000  608.220    0.000 activation.py:713(forward)
              248608800  369.713    0.000  607.850    0.000 layers.py:244(check)
                7458164  589.343    0.000  589.343    0.000 {built-in method torch._C._nn.one_hot}
                2486088   42.915    0.000  574.374    0.000 replaybuffer.py:19(stacker)
              746028111  172.490    0.000  574.173    0.000 layers.py:350(<genexpr>)
               44749184   33.185    0.000  573.175    0.000 functional.py:1364(leaky_relu)
               89499168  565.745    0.000  565.745    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               44749184  533.075    0.000  533.075    0.000 {built-in method torch._C._nn.leaky_relu}
               89499168  512.298    0.000  512.298    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                4972176   89.945    0.000  512.239    0.000 optimizer.py:189(zero_grad)
             5732418639  505.243    0.000  505.243    0.000 layer.py:67(positions)
              248608800  331.084    0.000  479.571    0.000 layers.py:63(check)
              943236211  332.966    0.000  445.282    0.000 layer.py:98(add)
             1930417314  442.606    0.000  442.606    0.000 layer.py:114(elements)
               11068007  152.679    0.000  426.217    0.000 random.py:315(sample)
                8582019  209.712    0.000  422.394    0.000 layers.py:33(reset)
              429095950  389.491    0.000  389.491    0.000 level.py:32(inverse)
              248608900  252.123    0.000  382.147    0.000 layers.py:110(isDone)
              195824120  361.854    0.000  361.854    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               44749584  357.474    0.000  357.474    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                2486088  202.173    0.000  344.751    0.000 collector.py:54(collect)
             4332246182  320.397    0.000  320.397    0.000 {built-in method builtins.hash}
              248608800  199.345    0.000  306.502    0.000 layers.py:203(check)
               44749584  289.108    0.000  289.108    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                4972076  107.550    0.000  288.603    0.000 exploration.py:53(softmaxer)
              296899696  138.224    0.000  280.053    0.000 layer.py:94(remove)
               44749584  271.175    0.000  271.175    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               44749584  269.291    0.000  269.291    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              313247142  195.733    0.000  242.462    0.000 tensor.py:906(grad)
              381823698  149.166    0.000  216.079    0.000 random.py:250(_randbelow_with_getrandbits)
        2694247036/2694247034  175.338    0.000  208.766    0.000 {built-in method builtins.len}
               44749584  201.395    0.000  201.395    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                4972176    6.129    0.000  197.152    0.000 loss.py:527(forward)
                4972176   17.710    0.000  191.023    0.000 functional.py:2898(mse_loss)
               17163838   14.062    0.000  190.728    0.000 level.py:38(elementsIn)
             2832658404  182.162    0.000  182.162    0.000 {method 'append' of 'list' objects}
              248608800   73.971    0.000  159.081    0.000 layers.py:99(<listcomp>)
             1680367430  152.928    0.000  152.928    0.000 layer.py:175(isBlocking)
               14916528  148.093    0.000  148.093    0.000 {built-in method sum}
              296899696  118.874    0.000  118.874    0.000 {method 'remove' of 'list' objects}
                4972176  115.922    0.000  115.922    0.000 {built-in method torch._C._nn.mse_loss}
               17163838   54.644    0.000  107.952    0.000 level.py:39(<listcomp>)
               24860680   15.185    0.000  105.491    0.000 flatten.py:39(forward)
                4972921  103.679    0.000  103.679    0.000 {built-in method max}
                7458264    9.654    0.000   99.699    0.000 tensor.py:525(__rsub__)
                8581919   45.981    0.000   98.419    0.000 level.py:16(<dictcomp>)
                4972076   90.838    0.000   90.838    0.000 {built-in method multinomial}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-7>
Subject: Job 9444627: <Rock_level_hard_softlow_0> in cluster <dcc> Done

Job <Rock_level_hard_softlow_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun Mar 21 02:08:58 2021
Job was executed on host(s) <n-62-20-7>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Mar 21 13:04:26 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun Mar 21 13:04:26 2021
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

    CPU time :                                   39293.29 sec.
    Max Memory :                                 2670 MB
    Average Memory :                             2662.94 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               5522.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   39338 sec.
    Turnaround time :                            78647 sec.

The output (if any) is above this job summary.

