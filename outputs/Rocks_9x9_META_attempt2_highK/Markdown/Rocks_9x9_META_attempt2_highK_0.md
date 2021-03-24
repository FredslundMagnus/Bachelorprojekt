
# Parameters

    Name :                      Rocks_9x9_META_attempt2_highK-0
    Main :                      metateleport
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
    Layer gold :                True
    Layer keys :                False
    Layer door :                False
    Layer holder :              False
    Layer putter :              False
    Layer rock :                True
    Layer dirt :                True
    Layer diamond1 :            False
    Layer diamond2 :            False
    Layer diamond3 :            False
    Layer diamond4 :            False
    Layer reddoors :            False
    Layer redkeys :             False
    Layer bluedoors :           False
    Layer bluekeys :            False
    K :                         500000.0
    Epsilon cap :               0.1
    Softmax cap :               0.025
    Gamma :                     0.98
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.03
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Minutes used :              655 minutes.
    Hours used :                10 hours.

# Profiling


      17867562129 function calls (17723733894 primitive calls) in 39315.51 seconds

##    Ordered by: cumulative time
   List reduced from 467 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 39315.508 39315.508 {built-in method builtins.exec}
                      1    5.715    5.715 39315.508 39315.508 <string>:1(<module>)
                      1  145.632  145.632 39309.793 39309.793 main.py:14(metateleport)
                4695582   21.816    0.000 12194.971    0.003 agent.py:27(learn)
                4695582  305.098    0.000 9741.142    0.002 learner.py:42(Qlearn)
                3130388  116.179    0.000 9122.120    0.003 agent.py:51(_learn)
                1565194    9.080    0.000 8757.401    0.006 game.py:27(step)
                1565194   11.402    0.000 8424.604    0.005 layers.py:475(step)
                3130388 6214.757    0.002 7386.660    0.002 replaybuffer.py:23(sample_data)
                1565194  149.160    0.000 6068.689    0.004 layers.py:18(step)
              156519400  431.607    0.000 5905.209    0.000 layer.py:76(move)
        161029394/17202858  694.651    0.000 5483.447    0.000 module.py:866(_call_impl)
               12507276   38.326    0.000 5093.973    0.000 network.py:24(forward)
               12507276  172.928    0.000 4966.131    0.000 container.py:117(forward)
                6246500  182.622    0.000 4229.069    0.001 agent.py:46(__call__)
              156519400  349.959    0.000 3857.308    0.000 layers.py:492(check)
                4695582   44.716    0.000 3685.879    0.001 optimizer.py:84(wrapper)
                3130388 2164.967    0.001 3644.025    0.001 replaybuffer.py:27(teleporter_save_data)
                3130388 1599.335    0.001 3613.018    0.001 agent.py:81(interveen)
                4695582   25.170    0.000 3492.348    0.001 grad_mode.py:24(decorate_context)
                4695582  156.283    0.000 3413.239    0.001 adam.py:55(step)
                4695582  711.457    0.000 3083.713    0.001 _functional.py:53(adam)
                1565194   48.043    0.000 3038.443    0.002 agent.py:146(_learn)
              156519400 2623.487    0.000 2809.255    0.000 layers.py:76(check)
                4695582   20.695    0.000 2623.124    0.001 tensor.py:195(backward)
                4695582   23.443    0.000 2601.678    0.001 __init__.py:68(backward)
                4695582 2476.055    0.001 2476.055    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                1565195  188.837    0.000 2327.830    0.001 layers.py:446(update)
                1565194 1446.449    0.001 2253.049    0.001 agent.py:101(metamodify)
               25014552   60.318    0.000 1840.538    0.000 conv.py:398(forward)
               25014552   39.607    0.000 1750.336    0.000 conv.py:390(_conv_forward)
               25014552 1710.730    0.000 1710.730    0.000 {built-in method conv2d}
               34391440   74.833    0.000 1397.320    0.000 linear.py:93(forward)
              156519400  188.259    0.000 1389.078    0.000 layers.py:486(isFree)
               34391440   29.549    0.000 1283.334    0.000 functional.py:1737(linear)
                9376888   87.021    0.000 1267.331    0.000 agent.py:55(modify_board)
              133368286 1267.178    0.000 1267.178    0.000 {built-in method clone}
               34391440 1247.489    0.000 1247.489    0.000 {built-in method torch._C._nn.linear}
              841471589 1072.005    0.000 1200.819    0.000 layer.py:73(isFree)
               28159216 1089.845    0.000 1089.845    0.000 {built-in method cat}
                9391170  616.090    0.000  977.770    0.000 layer.py:121(update)
                3130388   67.909    0.000  922.211    0.000 replaybuffer.py:19(stacker)
                9376888  823.950    0.000  823.950    0.000 {built-in method torch._C._nn.one_hot}
               46898716   40.883    0.000  725.422    0.000 activation.py:713(forward)
               46898716   39.674    0.000  684.539    0.000 functional.py:1364(leaky_relu)
                1565194   29.166    0.000  667.951    0.000 agent.py:141(__call__)
                1911027   20.522    0.000  659.263    0.000 layers.py:496(restart)
               46898716  636.860    0.000  636.860    0.000 {built-in method torch._C._nn.leaky_relu}
                8193416  601.568    0.000  601.568    0.000 {built-in method tensor}
               87650864  590.781    0.000  590.781    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                4695582  101.808    0.000  543.893    0.000 optimizer.py:189(zero_grad)
               87650864  528.953    0.000  528.953    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                4695582    6.257    0.000  506.344    0.000 game.py:23(board)
              156519500   43.907    0.000  434.254    0.000 {built-in method builtins.all}
              156519400  340.981    0.000  432.973    0.000 layers.py:63(check)
                1911027   10.652    0.000  430.002    0.000 level.py:8(__init__)
                6246500  153.683    0.000  423.850    0.000 exploration.py:53(softmaxer)
              469788488  113.736    0.000  409.346    0.000 layers.py:452(<genexpr>)
                1911027   56.580    0.000  378.846    0.000 levels.py:95(generate)
               43825432  351.816    0.000  351.816    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                1565194  186.409    0.000  317.739    0.000 collector.py:54(collect)
               43825432  312.672    0.000  312.672    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                5041415  115.644    0.000  307.086    0.000 random.py:315(sample)
              141179980  291.633    0.000  291.633    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               43825432  289.816    0.000  289.816    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               43825432  286.216    0.000  286.216    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              156519500  195.868    0.000  281.558    0.000 layers.py:110(isDone)
              978205845  190.470    0.000  270.635    0.000 enum.py:646(__hash__)
              306778108  216.254    0.000  265.572    0.000 tensor.py:906(grad)
              627820743  252.652    0.000  252.652    0.000 layer.py:116(elements)
                4695582    8.507    0.000  231.984    0.000 loss.py:527(forward)
                3822054   29.666    0.000  226.966    0.000 level.py:41(notUsed)
              156519400  150.020    0.000  224.056    0.000 layers.py:47(check)
                4695582   22.488    0.000  223.477    0.000 functional.py:2898(mse_loss)
             2286781794  209.256    0.000  209.256    0.000 layer.py:69(positions)
               43825432  206.565    0.000  206.565    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               11466162   25.431    0.000  204.692    0.000 layer.py:50(restart)
              304758095  128.264    0.000  175.475    0.000 layer.py:100(add)
        1428561421/1428561418  129.238    0.000  167.017    0.000 {built-in method builtins.len}
              163975149   91.988    0.000  156.800    0.000 layer.py:96(remove)
               14086746  151.914    0.000  151.914    0.000 {built-in method sum}
                6246500  136.926    0.000  136.926    0.000 {built-in method multinomial}
                4695582  133.883    0.000  133.883    0.000 {built-in method torch._C._nn.mse_loss}
              204335007   86.744    0.000  128.511    0.000 random.py:250(_randbelow_with_getrandbits)
                7825970   12.668    0.000  126.202    0.000 tensor.py:525(__rsub__)
               25014552   21.201    0.000  122.039    0.000 flatten.py:39(forward)
                4696361  121.768    0.000  121.768    0.000 {built-in method max}
                1911127   51.724    0.000  119.943    0.000 layers.py:33(reset)
              105106485  118.803    0.000  118.803    0.000 level.py:32(inverse)
                7825970  111.585    0.000  111.585    0.000 {built-in method rsub}
               25014552  100.838    0.000  100.838    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                3130390  100.528    0.000  100.528    0.000 {built-in method nonzero}
                4695582   21.394    0.000   97.508    0.000 __init__.py:28(_make_grads)
              131331263   96.529    0.000   96.537    0.000 module.py:934(__getattr__)
                9391164   21.346    0.000   93.038    0.000 profiler.py:615(__enter__)
              164161028   92.967    0.000   92.967    0.000 {built-in method torch._C._get_tracing_state}
                4695582   92.061    0.000   92.061    0.000 {built-in method gather}
             1091010031   91.221    0.000   91.221    0.000 {method 'append' of 'list' objects}
              841471589   89.726    0.000   89.726    0.000 layer.py:177(isBlocking)
                6619488   88.010    0.000   88.010    0.000 {method 'long' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-12>
Subject: Job 9455326: <Rocks_9x9_META_attempt2_highK_0> in cluster <dcc> Done

Job <Rocks_9x9_META_attempt2_highK_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed Mar 24 02:22:06 2021
Job was executed on host(s) <n-62-20-12>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed Mar 24 02:29:07 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed Mar 24 02:29:07 2021
Terminated at Wed Mar 24 13:24:31 2021
Results reported at Wed Mar 24 13:24:31 2021

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

    CPU time :                                   39218.34 sec.
    Max Memory :                                 6570 MB
    Average Memory :                             5111.31 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               1622.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   39325 sec.
    Turnaround time :                            39745 sec.

The output (if any) is above this job summary.

