
# Parameters

    Name :                      MonsterLevel_Conver4_3counterfactsNOCRASH-2
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
    Cf convert :                4
    Counterfacts :              3
    Topn :                      5
    Random counterfacts :       False
    Num :                       2
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      66506665829 function calls (66135541806 primitive calls) in 86119.82 seconds

##    Ordered by: cumulative time
   List reduced from 508 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86119.818 86119.818 {built-in method builtins.exec}
                      1    4.342    4.342 86119.818 86119.818 <string>:1(<module>)
                      1  283.280  283.280 86115.476 86115.476 main.py:80(CFagent)
                2514378 3816.477    0.002 23289.261    0.009 agent.py:212(counterfact)
                2514378   10.787    0.000 20370.267    0.008 game.py:42(step)
                2514378   15.177    0.000 19876.265    0.008 layers.py:827(step)
                7543134   29.684    0.000 18884.614    0.003 agent.py:29(learn)
                7543134  473.410    0.000 15389.173    0.002 learner.py:42(Qlearn)
        410430453/39308121 1645.399    0.000 13379.473    0.000 module.py:866(_call_impl)
               31764987   86.024    0.000 12707.386    0.000 network.py:28(forward)
               31764987  402.668    0.000 12413.720    0.000 container.py:117(forward)
                2514379  403.219    0.000 10455.074    0.004 layers.py:793(update)
                7082200  143.509    0.000 9591.588    0.001 agent.py:176(choose_action)
                2514378  241.180    0.000 9385.625    0.004 layers.py:17(step)
              247572031  766.243    0.000 9120.026    0.000 layer.py:106(move)
               12110897  321.971    0.000 7809.873    0.001 agent.py:49(__call__)
                2514378  269.836    0.000 7331.266    0.003 agent.py:54(_learn)
                2514378  267.344    0.000 6735.572    0.003 agent.py:204(_learn)
               89434421 6645.667    0.000 6645.667    0.000 {built-in method tensor}
               83569235   50.138    0.000 6530.171    0.000 game.py:38(board)
              247572031  839.027    0.000 6157.022    0.000 layers.py:844(check)
                7543134   64.980    0.000 6055.723    0.001 optimizer.py:84(wrapper)
                7543134   32.344    0.000 5765.333    0.001 grad_mode.py:24(decorate_context)
                7543134  230.093    0.000 5662.453    0.001 adam.py:55(step)
                8733234   75.457    0.000 5387.301    0.001 layers.py:849(restart)
                7543134 1175.243    0.000 5165.484    0.001 _functional.py:53(adam)
                2514378   77.463    0.000 4770.680    0.002 agent.py:117(_learn)
               60345066 2949.120    0.000 4683.214    0.000 layer.py:159(update)
                8733234   36.677    0.000 4617.008    0.001 level.py:8(__init__)
                2514378 3789.203    0.002 4565.783    0.002 replaybuffer.py:22(sample_data)
                2514378 3779.145    0.002 4537.769    0.002 replaybuffer.py:67(sample_data)
               63529974  137.076    0.000 4528.223    0.000 conv.py:398(forward)
                2514378 2520.198    0.001 4434.092    0.002 replaybuffer.py:28(teleporter_save_data)
               63529974   95.491    0.000 4327.485    0.000 conv.py:390(_conv_forward)
               63529974 4231.994    0.000 4231.994    0.000 {built-in method conv2d}
                8733234  677.196    0.000 4195.175    0.000 levels.py:428(generate)
                7543134   31.460    0.000 3960.959    0.001 tensor.py:195(backward)
                7543134   29.405    0.000 3928.466    0.001 __init__.py:68(backward)
                2514378 2168.880    0.001 3787.995    0.002 agent.py:88(interveen)
                7543134 3748.705    0.000 3748.705    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
               90266205  193.340    0.000 3556.232    0.000 linear.py:93(forward)
              247572031 1972.274    0.000 3509.846    0.000 layers.py:538(check)
               90266205   77.180    0.000 3274.756    0.000 functional.py:1737(linear)
               90266205 3179.436    0.000 3179.436    0.000 {built-in method torch._C._nn.linear}
               43666170  447.895    0.000 2857.167    0.000 level.py:41(notUsed)
                2514378 1546.548    0.001 2108.278    0.001 replaybuffer.py:73(CF_save_data)
              209649796 2054.749    0.000 2054.749    0.000 {built-in method clone}
                2514378 1385.728    0.001 2021.413    0.001 agent.py:67(modify)
               14625275   90.149    0.000 1895.532    0.000 agent.py:59(modify_board)
              122031192   97.271    0.000 1876.627    0.000 activation.py:713(forward)
              255944242  210.203    0.000 1807.483    0.000 {built-in method builtins.any}
                7082200 1532.596    0.000 1802.414    0.000 agent.py:187(convert_values)
              122031192  100.165    0.000 1779.356    0.000 functional.py:1364(leaky_relu)
              247572031  333.538    0.000 1665.178    0.000 layers.py:838(isFree)
              122031192 1659.179    0.000 1659.179    0.000 {built-in method torch._C._nn.leaky_relu}
             6240353798 1126.352    0.000 1631.922    0.000 enum.py:646(__hash__)
             1733111320  517.676    0.000 1598.019    0.000 layers.py:809(<genexpr>)
               39769055 1458.911    0.000 1458.911    0.000 {built-in method cat}
             1328465616 1119.215    0.000 1331.640    0.000 layer.py:103(isFree)
               43666170   37.577    0.000 1312.347    0.000 level.py:38(elementsIn)
               14625275 1236.946    0.000 1236.946    0.000 {built-in method torch._C._nn.one_hot}
                2514378   42.882    0.000 1144.965    0.000 agent.py:172(__call__)
                2514378   40.157    0.000 1096.326    0.000 agent.py:112(__call__)
              140805168 1012.412    0.000 1012.412    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
             2059307132  991.465    0.000  991.465    0.000 layer.py:154(elements)
              248401109  615.194    0.000  981.119    0.000 layers.py:575(isDead)
              140805168  901.834    0.000  901.834    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              247572031  637.902    0.000  896.342    0.000 layers.py:77(check)
                7543134  160.489    0.000  888.290    0.000 optimizer.py:189(zero_grad)
               43666170  416.101    0.000  843.363    0.000 level.py:39(<listcomp>)
               12110897  292.845    0.000  780.692    0.000 exploration.py:53(softmaxer)
               48694926  302.434    0.000  777.931    0.000 random.py:315(sample)
              251437900   87.257    0.000  776.532    0.000 {built-in method builtins.all}
              812491758  239.839    0.000  722.930    0.000 layers.py:799(<genexpr>)
             1862971362  700.630    0.000  700.630    0.000 level.py:32(inverse)
               52399404   68.103    0.000  675.847    0.000 layer.py:77(restart)
              355367848  129.387    0.000  657.058    0.000 random.py:244(randint)
        8193627797/8193627794  575.351    0.000  649.702    0.000 {built-in method builtins.len}
              584212047  467.540    0.000  633.581    0.000 layer.py:134(remove)
              801631502  424.342    0.000  613.379    0.000 random.py:250(_randbelow_with_getrandbits)
               70402584  592.085    0.000  592.085    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                2514378   44.273    0.000  585.543    0.000 replaybuffer.py:18(stacker)
                2514378   45.887    0.000  571.930    0.000 replaybuffer.py:63(stacker)
               52527233  570.288    0.000  570.288    0.000 {method 'item' of 'torch._C._TensorBase' objects}
              980167059  402.953    0.000  545.565    0.000 layer.py:138(add)
              355367848  217.999    0.000  527.671    0.000 random.py:200(randrange)
             5356505091  521.855    0.000  521.855    0.000 layer.py:99(positions)
               70402584  512.006    0.000  512.006    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
             6240382613  505.576    0.000  505.576    0.000 {built-in method builtins.hash}
                8733334  242.485    0.000  478.335    0.000 layers.py:36(reset)
               70402584  476.831    0.000  476.831    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               70402584  476.711    0.000  476.711    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              226789449  470.170    0.000  470.170    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              251437900  303.232    0.000  443.844    0.000 layers.py:113(isDone)
             2253176408  442.026    0.000  442.026    0.000 enum.py:352(<genexpr>)
               43666170  267.909    0.000  431.406    0.000 {built-in method _functools.reduce}
              247572031  292.609    0.000  428.474    0.000 layers.py:48(check)
              492818172  337.867    0.000  419.347    0.000 tensor.py:906(grad)
              247572031  140.375    0.000  396.435    0.000 layers.py:572(<listcomp>)
                2514378  227.754    0.000  389.144    0.000 collector.py:46(collect)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9624186: <MonsterLevel_Conver4_3counterfactsNOCRASH_2> in cluster <dcc> Done

Job <MonsterLevel_Conver4_3counterfactsNOCRASH_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun May  9 01:29:17 2021
Job was executed on host(s) <n-62-20-14>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon May 10 17:27:26 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon May 10 17:27:26 2021
Terminated at Tue May 11 17:22:56 2021
Results reported at Tue May 11 17:22:56 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
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

python main.py $MYARGS


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   85866.36 sec.
    Max Memory :                                 8214 MB
    Average Memory :                             5839.27 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               8170.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86130 sec.
    Turnaround time :                            230019 sec.

The output (if any) is above this job summary.

