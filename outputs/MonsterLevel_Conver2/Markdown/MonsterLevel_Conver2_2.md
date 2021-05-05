
# Parameters

    Name :                      MonsterLevel_Conver2-2
    Main :                      CFagent
    Level :                     Levels.MonsterLevel
    Failed actions chance :     0
    Use model :                 True
    Depth :                     3
    Model explore :             1000000
    Samples :                   5
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
    Layer super1 :              True
    Layer super2 :              True
    Layer super3 :              True
    Layer super4 :              True
    Layer super5 :              True
    Layer super6 :              True
    Layer super7 :              True
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                2
    Counterfacts :              1
    Topn :                      3
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      77886303345 function calls (77549166134 primitive calls) in 86120.18 seconds

##    Ordered by: cumulative time
   List reduced from 508 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86120.175 86120.175 {built-in method builtins.exec}
                      1    4.184    4.184 86120.175 86120.175 <string>:1(<module>)
                      1  316.137  316.137 86115.991 86115.991 main.py:80(CFagent)
                3298009   14.284    0.000 24964.538    0.008 game.py:42(step)
                3298009   18.723    0.000 24345.587    0.007 layers.py:827(step)
                9894027   38.031    0.000 23794.889    0.002 agent.py:29(learn)
                9894027  600.897    0.000 19541.066    0.002 learner.py:42(Qlearn)
                3298010  509.756    0.000 12335.529    0.004 layers.py:793(update)
                3298009  312.458    0.000 11966.376    0.004 layers.py:17(step)
        376223510/39087990 1462.461    0.000 11822.899    0.000 module.py:866(_call_impl)
              328551519  963.266    0.000 11623.682    0.000 layer.py:106(move)
               29193963   79.686    0.000 11091.668    0.000 network.py:28(forward)
               29193963  368.777    0.000 10829.896    0.000 container.py:117(forward)
                3298009 1493.732    0.000 9497.039    0.003 agent.py:212(counterfact)
                3298009  299.807    0.000 9201.419    0.003 agent.py:54(_learn)
                3298009  296.457    0.000 8481.746    0.003 agent.py:204(_learn)
              328551519 1086.251    0.000 7880.447    0.000 layers.py:844(check)
                9894027   85.787    0.000 7673.974    0.001 optimizer.py:84(wrapper)
                9894027   45.194    0.000 7294.335    0.001 grad_mode.py:24(decorate_context)
                9894027  281.487    0.000 7155.433    0.001 adam.py:55(step)
                9894027 1494.401    0.000 6541.510    0.001 _functional.py:53(adam)
               10660151   90.263    0.000 6261.004    0.001 layers.py:849(restart)
                3298009   89.864    0.000 6053.273    0.002 agent.py:117(_learn)
                9649923  215.768    0.000 5965.637    0.001 agent.py:49(__call__)
                3298009 3086.102    0.001 5470.224    0.002 replaybuffer.py:28(teleporter_save_data)
               10660151   43.011    0.000 5371.422    0.001 level.py:8(__init__)
                9894027   45.364    0.000 5152.471    0.001 tensor.py:195(backward)
                9894027   37.323    0.000 5105.880    0.001 __init__.py:68(backward)
                3298009 4100.452    0.001 5032.329    0.002 replaybuffer.py:22(sample_data)
                3298009 4079.480    0.001 5000.760    0.002 replaybuffer.py:67(sample_data)
                9894027 4879.511    0.000 4879.511    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
               10660151  796.179    0.000 4853.439    0.000 levels.py:428(generate)
                3298009 2712.057    0.001 4743.557    0.001 agent.py:88(interveen)
              328551519 2549.061    0.000 4534.481    0.000 layers.py:538(check)
               58387926  125.046    0.000 3960.866    0.000 conv.py:398(forward)
                3053995   61.242    0.000 3925.549    0.001 agent.py:176(choose_action)
               58387926   74.679    0.000 3778.906    0.000 conv.py:390(_conv_forward)
               58387926 3704.227    0.000 3704.227    0.000 {built-in method conv2d}
               39576114 2268.270    0.000 3487.269    0.000 layer.py:159(update)
               47692018 3325.153    0.000 3325.153    0.000 {built-in method tensor}
               53300755  513.287    0.000 3285.543    0.000 level.py:41(notUsed)
               40098212   25.741    0.000 3150.532    0.000 game.py:38(board)
               80985871  162.998    0.000 3102.894    0.000 linear.py:93(forward)
               80985871   64.100    0.000 2862.030    0.000 functional.py:1737(linear)
               80985871 2782.783    0.000 2782.783    0.000 {built-in method torch._C._nn.linear}
                3298009 1718.421    0.001 2516.960    0.001 agent.py:67(modify)
              269343913 2515.478    0.000 2515.478    0.000 {built-in method clone}
                3298009 1829.135    0.001 2488.952    0.001 replaybuffer.py:73(CF_save_data)
              329701786  267.551    0.000 2257.468    0.000 {built-in method builtins.any}
              328551519  442.243    0.000 2107.782    0.000 layers.py:838(isFree)
             7944345899 1370.245    0.000 1998.254    0.000 enum.py:646(__hash__)
             2255774724  627.044    0.000 1990.831    0.000 layers.py:809(<genexpr>)
             1931238982 1363.995    0.000 1665.539    0.000 layer.py:103(isFree)
               12947932   78.414    0.000 1642.201    0.000 agent.py:59(modify_board)
              110179834   86.079    0.000 1605.027    0.000 activation.py:713(forward)
               45928022 1582.855    0.000 1582.855    0.000 {built-in method cat}
              110179834   89.982    0.000 1518.948    0.000 functional.py:1364(leaky_relu)
               53300755   44.007    0.000 1512.236    0.000 level.py:38(elementsIn)
                3298009   47.273    0.000 1422.737    0.000 agent.py:172(__call__)
              110179834 1411.267    0.000 1411.267    0.000 {built-in method torch._C._nn.leaky_relu}
                3298009   48.011    0.000 1350.715    0.000 agent.py:112(__call__)
              184688504 1266.438    0.000 1266.438    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              326403776  760.915    0.000 1236.144    0.000 layers.py:575(isDead)
                9894027  202.173    0.000 1147.034    0.000 optimizer.py:189(zero_grad)
              184688504 1125.504    0.000 1125.504    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               12947932 1079.393    0.000 1079.393    0.000 {built-in method torch._C._nn.one_hot}
              328551519  766.041    0.000 1077.872    0.000 layers.py:77(check)
               53300755  478.810    0.000  976.038    0.000 level.py:39(<listcomp>)
               59896773  361.552    0.000  933.902    0.000 random.py:315(sample)
              481052136  170.616    0.000  846.186    0.000 random.py:244(randint)
             2274022815  806.990    0.000  806.990    0.000 level.py:32(inverse)
               92344252  795.080    0.000  795.080    0.000 {method 'add' of 'torch._C._TensorBase' objects}
             2570856077  794.410    0.000  794.410    0.000 layer.py:154(elements)
              329801000   84.657    0.000  785.534    0.000 {built-in method builtins.all}
               63960906   77.138    0.000  777.352    0.000 layer.py:77(restart)
             1048669359  526.870    0.000  754.167    0.000 random.py:250(_randbelow_with_getrandbits)
              693253588  170.786    0.000  744.314    0.000 layers.py:799(<genexpr>)
                3298009   51.945    0.000  698.051    0.000 replaybuffer.py:18(stacker)
                3298009   53.346    0.000  688.943    0.000 replaybuffer.py:63(stacker)
                3053995  597.848    0.000  680.663    0.000 agent.py:187(convert_values)
              481052136  289.698    0.000  675.570    0.000 random.py:200(randrange)
             7144853009  670.827    0.000  670.827    0.000 layer.py:99(positions)
             1259634374  488.896    0.000  661.350    0.000 layer.py:138(add)
               92344252  645.930    0.000  645.930    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
             7944383450  628.016    0.000  628.016    0.000 {built-in method builtins.hash}
               92344252  604.732    0.000  604.732    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                9649923  225.271    0.000  598.351    0.000 exploration.py:53(softmaxer)
              772623372  389.997    0.000  591.213    0.000 layer.py:134(remove)
               92344252  582.516    0.000  582.516    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              285589854  581.678    0.000  581.678    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              328551519  376.915    0.000  566.832    0.000 layers.py:48(check)
              329801000  378.757    0.000  565.340    0.000 layers.py:113(isDone)
               10660251  271.805    0.000  542.975    0.000 layers.py:36(reset)
              646409848  422.731    0.000  523.373    0.000 tensor.py:906(grad)
                3298009  297.918    0.000  506.126    0.000 collector.py:46(collect)
             2750320994  506.109    0.000  506.109    0.000 enum.py:352(<genexpr>)
              328551519  178.128    0.000  498.754    0.000 layers.py:572(<listcomp>)
               53300755  304.185    0.000  492.191    0.000 {built-in method _functools.reduce}
        5325087856/5325087853  404.231    0.000  470.386    0.000 {built-in method builtins.len}
               92344252  462.404    0.000  462.404    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9579183: <MonsterLevel_Conver2_2> in cluster <dcc> Done

Job <MonsterLevel_Conver2_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Tue Apr 27 02:44:09 2021
Job was executed on host(s) <n-62-11-13>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon May  3 03:04:07 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon May  3 03:04:07 2021
Terminated at Tue May  4 02:59:35 2021
Results reported at Tue May  4 02:59:35 2021

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

    CPU time :                                   86034.51 sec.
    Max Memory :                                 3452 MB
    Average Memory :                             3445.20 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               12932.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86127 sec.
    Turnaround time :                            605726 sec.

The output (if any) is above this job summary.

