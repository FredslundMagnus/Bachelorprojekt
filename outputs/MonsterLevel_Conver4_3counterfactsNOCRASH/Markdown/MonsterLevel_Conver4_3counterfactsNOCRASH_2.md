
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

Traceback (most recent call last):
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils/debug.py", line 71, in __init__
    cProfile.run(
  File "/appl/python/3.8.4/lib/python3.8/cProfile.py", line 16, in run
    return _pyprofile._Utils(Profile).run(statement, filename, sort)
  File "/appl/python/3.8.4/lib/python3.8/profile.py", line 53, in run
    prof.run(statement)
  File "/appl/python/3.8.4/lib/python3.8/cProfile.py", line 95, in run
    return self.runctx(cmd, dict, dict)
  File "/appl/python/3.8.4/lib/python3.8/cProfile.py", line 100, in runctx
    exec(cmd, globals, locals)
  File "<string>", line 2, in <module>
  File "main.py", line 85, in CFagent
    CFagent = CFAgent(env, **defaults)
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/agent.py", line 171, in __init__
    if a != b:
NameError: name 'a' is not defined


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
    Minutes used :              0 minutes.
    Hours used :                0 hours.

# Profiling


      246198 function calls (245909 primitive calls) in 5.22 seconds

##    Ordered by: cumulative time
   List reduced from 208 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000    5.224    5.224 {built-in method builtins.exec}
                      1    0.000    0.000    5.224    5.224 <string>:1(<module>)
                      1    0.000    0.000    5.224    5.224 main.py:80(CFagent)
                      3    0.000    0.000    5.122    1.707 agent.py:16(__init__)
                      3    0.000    0.000    5.121    1.707 network.py:37(__init__)
                      1    0.000    0.000    5.104    5.104 agent.py:109(__init__)
                      9    0.000    0.000    5.104    0.567 module.py:573(to)
                  111/9    0.001    0.000    5.104    0.567 module.py:385(_apply)
                     84    0.000    0.000    5.102    0.061 module.py:667(convert)
                     84    5.090    0.061    5.102    0.061 {method 'to' of 'torch._C._TensorBase' objects}
                      1    0.002    0.002    0.098    0.098 game.py:9(__init__)
                      1    0.000    0.000    0.085    0.085 layers.py:793(update)
                    100    0.001    0.000    0.079    0.001 layers.py:849(restart)
                    100    0.000    0.000    0.071    0.001 level.py:8(__init__)
                    100    0.008    0.000    0.067    0.001 levels.py:428(generate)
                    500    0.005    0.000    0.052    0.000 level.py:41(notUsed)
                  21348    0.028    0.000    0.028    0.000 level.py:32(inverse)
                      9    0.000    0.000    0.018    0.002 network.py:17(__init__)
                    500    0.000    0.000    0.015    0.000 level.py:38(elementsIn)
                    4/1    0.000    0.000    0.012    0.012 __init__.py:144(_lazy_init)
                      1    0.012    0.012    0.012    0.012 {built-in method torch._C._cuda_init}
                    200    0.005    0.000    0.011    0.000 layers.py:36(reset)
                    500    0.005    0.000    0.010    0.000 level.py:39(<listcomp>)
                     42    0.000    0.000    0.010    0.000 init.py:347(kaiming_uniform_)
                      1    0.000    0.000    0.009    0.009 layers.py:751(__init__)
                      1    0.000    0.000    0.009    0.009 agent.py:158(__init__)
                      1    0.000    0.000    0.009    0.009 agent.py:39(__init__)
                  38507    0.006    0.000    0.009    0.000 enum.py:646(__hash__)
                      5    0.000    0.000    0.009    0.002 layers.py:782(add)
                     84    0.009    0.000    0.009    0.000 {method 'uniform_' of 'torch._C._TensorBase' objects}
                    600    0.001    0.000    0.008    0.000 layer.py:77(restart)
                     24    0.000    0.000    0.007    0.000 linear.py:75(__init__)
                     18    0.000    0.000    0.007    0.000 conv.py:370(__init__)
                      6    0.000    0.000    0.007    0.001 layer.py:61(__init__)
                     18    0.001    0.000    0.007    0.000 conv.py:66(__init__)
                     24    0.000    0.000    0.006    0.000 linear.py:86(reset_parameters)
                  27836    0.005    0.000    0.005    0.000 enum.py:352(<genexpr>)
                      6    0.004    0.001    0.005    0.001 layer.py:159(update)
                     18    0.000    0.000    0.005    0.000 conv.py:114(reset_parameters)
                    500    0.003    0.000    0.005    0.000 {built-in method _functools.reduce}
                    500    0.002    0.000    0.005    0.000 random.py:315(sample)
                   1698    0.003    0.000    0.004    0.000 module.py:950(__setattr__)
                   7984    0.003    0.000    0.004    0.000 layer.py:138(add)
                    114    0.001    0.000    0.004    0.000 module.py:250(__init__)
                    100    0.001    0.000    0.003    0.000 level.py:16(<dictcomp>)
                  38507    0.003    0.000    0.003    0.000 {built-in method builtins.hash}
                      1    0.000    0.000    0.003    0.003 replaybuffer.py:8(__init__)
                      1    0.003    0.003    0.003    0.003 replaybuffer.py:11(<listcomp>)
                  16892    0.002    0.000    0.002    0.000 layer.py:190(grid)
                      1    0.000    0.000    0.002    0.002 game.py:30(<setcomp>)
                     41    0.001    0.000    0.002    0.000 game.py:30(<listcomp>)
                      1    0.002    0.002    0.002    0.002 layers.py:529(__init__)
                  21000    0.002    0.000    0.002    0.000 level.py:39(<lambda>)
                   2227    0.001    0.000    0.002    0.000 random.py:250(_randbelow_with_getrandbits)
                     33    0.000    0.000    0.002    0.000 activation.py:708(__init__)
                   5273    0.001    0.000    0.001    0.000 {built-in method builtins.isinstance}
                  17807    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
                      9    0.000    0.000    0.001    0.000 container.py:62(__init__)
                    600    0.001    0.000    0.001    0.000 layer.py:147(clear2)
                   7996    0.001    0.000    0.001    0.000 layer.py:154(elements)
                   2190    0.001    0.000    0.001    0.000 types.py:171(__get__)
                   1090    0.000    0.000    0.001    0.000 abc.py:96(__instancecheck__)
                     84    0.001    0.000    0.001    0.000 init.py:268(_calculate_fan_in_and_fan_out)
                      3    0.000    0.000    0.001    0.000 learner.py:16(__init__)
                    100    0.000    0.000    0.001    0.000 {built-in method builtins.all}
                      5    0.000    0.000    0.001    0.000 inspect.py:325(getmembers)
                     42    0.000    0.000    0.001    0.000 init.py:337(_calculate_correct_fan)
                    272    0.000    0.000    0.001    0.000 {built-in method builtins.hasattr}
                     18    0.000    0.000    0.000    0.000 flatten.py:34(__init__)
                    700    0.000    0.000    0.000    0.000 layers.py:799(<genexpr>)
                     84    0.000    0.000    0.000    0.000 module.py:322(register_parameter)
                   1090    0.000    0.000    0.000    0.000 {built-in method _abc._abc_instancecheck}
                      3    0.000    0.000    0.000    0.000 adam.py:34(__init__)
                      3    0.000    0.000    0.000    0.000 optimizer.py:34(__init__)
                   4917    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
                    345    0.000    0.000    0.000    0.000 module.py:934(__getattr__)
                     42    0.000    0.000    0.000    0.000 init.py:112(uniform_)
                     42    0.000    0.000    0.000    0.000 init.py:12(_no_grad_uniform_)
                   3564    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
                    168    0.000    0.000    0.000    0.000 grad_mode.py:119(__enter__)
                    648    0.000    0.000    0.000    0.000 enum.py:351(__iter__)
                     93    0.000    0.000    0.000    0.000 module.py:361(add_module)
                     90    0.000    0.000    0.000    0.000 utils.py:9(parse)
                    336    0.000    0.000    0.000    0.000 grad_mode.py:200(__init__)
                    213    0.000    0.000    0.000    0.000 module.py:1338(children)
                    168    0.000    0.000    0.000    0.000 grad_mode.py:123(__exit__)
                      1    0.000    0.000    0.000    0.000 agent.py:167(<listcomp>)
                      6    0.000    0.000    0.000    0.000 layer.py:71(<listcomp>)
                     84    0.000    0.000    0.000    0.000 parameter.py:23(__new__)
                    500    0.000    0.000    0.000    0.000 enum.py:354(__len__)
                     84    0.000    0.000    0.000    0.000 module.py:389(compute_should_use_set_data)
                    600    0.000    0.000    0.000    0.000 layer.py:142(clear)
                   1799    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
                   2189    0.000    0.000    0.000    0.000 enum.py:659(name)
                     31    0.000    0.000    0.000    0.000 module.py:1240(parameters)
                    168    0.000    0.000    0.000    0.000 grad_mode.py:114(__init__)
                     31    0.000    0.000    0.000    0.000 module.py:1264(named_parameters)
                      2    0.000    0.000    0.000    0.000 {built-in method zeros}
                      1    0.000    0.000    0.000    0.000 layers.py:73(__init__)
                     31    0.000    0.000    0.000    0.000 module.py:1227(_named_members)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9632727: <MonsterLevel_Conver4_3counterfactsNOCRASH_2> in cluster <dcc> Done

Job <MonsterLevel_Conver4_3counterfactsNOCRASH_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed May 12 14:11:09 2021
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed May 12 15:12:58 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 12 15:12:58 2021
Terminated at Wed May 12 15:13:08 2021
Results reported at Wed May 12 15:13:08 2021

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

    CPU time :                                   5.19 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   11 sec.
    Turnaround time :                            3719 sec.

The output (if any) is above this job summary.

Traceback (most recent call last):
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils/debug.py", line 71, in __init__
    cProfile.run(
  File "/appl/python/3.8.4/lib/python3.8/cProfile.py", line 16, in run
    return _pyprofile._Utils(Profile).run(statement, filename, sort)
  File "/appl/python/3.8.4/lib/python3.8/profile.py", line 53, in run
    prof.run(statement)
  File "/appl/python/3.8.4/lib/python3.8/cProfile.py", line 95, in run
    return self.runctx(cmd, dict, dict)
  File "/appl/python/3.8.4/lib/python3.8/cProfile.py", line 100, in runctx
    exec(cmd, globals, locals)
  File "<string>", line 2, in <module>
  File "main.py", line 85, in CFagent
    CFagent = CFAgent(env, **defaults)
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/agent.py", line 171, in __init__
    if a != b:
NameError: name 'a' is not defined


# Parameters

    Name :                      MonsterLevel_Conver4_3counterfactsNOCRASH-2
    Main :                      CFagent
    Level :                     Levels.MonsterLevel
    Failed actions chance :     0
    Use model :                 True
    Depth :                     3
    Model explore :             1000000
    Samples :                   5
    Hours :                     0.0
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
    Minutes used :              0 minutes.
    Hours used :                0 hours.

# Profiling


      158537 function calls (158248 primitive calls) in 3.52 seconds

##    Ordered by: cumulative time
   List reduced from 207 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000    3.523    3.523 {built-in method builtins.exec}
                      1    0.000    0.000    3.523    3.523 <string>:1(<module>)
                      1    0.000    0.000    3.523    3.523 main.py:80(CFagent)
                      3    0.000    0.000    3.468    1.156 agent.py:16(__init__)
                      3    0.000    0.000    3.467    1.156 network.py:37(__init__)
                      1    0.000    0.000    3.450    3.450 agent.py:109(__init__)
                      9    0.000    0.000    3.445    0.383 module.py:573(to)
                  111/9    0.001    0.000    3.445    0.383 module.py:385(_apply)
                     84    0.000    0.000    3.441    0.041 module.py:667(convert)
                     84    3.426    0.041    3.441    0.041 {method 'to' of 'torch._C._TensorBase' objects}
                      1    0.002    0.002    0.052    0.052 game.py:9(__init__)
                      1    0.000    0.000    0.039    0.039 layers.py:793(update)
                    100    0.001    0.000    0.035    0.000 layers.py:849(restart)
                    100    0.000    0.000    0.024    0.000 level.py:8(__init__)
                      9    0.000    0.000    0.022    0.002 network.py:17(__init__)
                    100    0.002    0.000    0.020    0.000 levels.py:164(generate)
                    4/1    0.000    0.000    0.016    0.016 __init__.py:144(_lazy_init)
                      1    0.016    0.016    0.016    0.016 {built-in method torch._C._cuda_init}
                    200    0.002    0.000    0.015    0.000 level.py:41(notUsed)
                     42    0.000    0.000    0.012    0.000 init.py:347(kaiming_uniform_)
                     84    0.010    0.000    0.010    0.000 {method 'uniform_' of 'torch._C._TensorBase' objects}
                    200    0.005    0.000    0.010    0.000 layers.py:36(reset)
                      1    0.000    0.000    0.010    0.010 agent.py:39(__init__)
                    800    0.001    0.000    0.010    0.000 layer.py:77(restart)
                     18    0.000    0.000    0.009    0.001 conv.py:370(__init__)
                     18    0.001    0.000    0.009    0.000 conv.py:66(__init__)
                     24    0.000    0.000    0.009    0.000 linear.py:75(__init__)
                      1    0.000    0.000    0.009    0.009 agent.py:158(__init__)
                      1    0.000    0.000    0.008    0.008 layers.py:751(__init__)
                      7    0.000    0.000    0.008    0.001 layers.py:782(add)
                     24    0.000    0.000    0.007    0.000 linear.py:86(reset_parameters)
                      8    0.000    0.000    0.007    0.001 layer.py:61(__init__)
                    200    0.000    0.000    0.006    0.000 level.py:38(elementsIn)
                     18    0.000    0.000    0.006    0.000 conv.py:114(reset_parameters)
                   1698    0.003    0.000    0.005    0.000 module.py:950(__setattr__)
                   6556    0.005    0.000    0.005    0.000 level.py:32(inverse)
                    114    0.001    0.000    0.004    0.000 module.py:250(__init__)
                  17216    0.003    0.000    0.004    0.000 enum.py:646(__hash__)
                    200    0.002    0.000    0.004    0.000 level.py:39(<listcomp>)
                   8355    0.003    0.000    0.004    0.000 layer.py:138(add)
                    100    0.001    0.000    0.003    0.000 level.py:16(<dictcomp>)
                      8    0.002    0.000    0.003    0.000 layer.py:175(NoRock_update)
                  15022    0.003    0.000    0.003    0.000 enum.py:352(<genexpr>)
                    800    0.003    0.000    0.003    0.000 layer.py:147(clear2)
                      1    0.000    0.000    0.003    0.003 replaybuffer.py:8(__init__)
                      1    0.003    0.003    0.003    0.003 replaybuffer.py:11(<listcomp>)
                  17056    0.002    0.000    0.002    0.000 layer.py:190(grid)
                      1    0.000    0.000    0.002    0.002 game.py:30(<setcomp>)
                    200    0.001    0.000    0.002    0.000 {built-in method _functools.reduce}
                     41    0.001    0.000    0.002    0.000 game.py:30(<listcomp>)
                    200    0.001    0.000    0.002    0.000 random.py:315(sample)
                     33    0.000    0.000    0.001    0.000 activation.py:708(__init__)
                  17216    0.001    0.000    0.001    0.000 {built-in method builtins.hash}
                  19020    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
                   4805    0.001    0.000    0.001    0.000 {built-in method builtins.isinstance}
                      9    0.000    0.000    0.001    0.000 container.py:62(__init__)
                     84    0.001    0.000    0.001    0.000 init.py:268(_calculate_fan_in_and_fan_out)
                   8371    0.001    0.000    0.001    0.000 layer.py:154(elements)
                   2360    0.001    0.000    0.001    0.000 types.py:171(__get__)
                    213    0.000    0.000    0.001    0.000 module.py:1338(children)
                   8400    0.001    0.000    0.001    0.000 level.py:39(<lambda>)
                    272    0.000    0.000    0.001    0.000 {built-in method builtins.hasattr}
                     18    0.000    0.000    0.001    0.000 flatten.py:34(__init__)
                     42    0.000    0.000    0.001    0.000 init.py:337(_calculate_correct_fan)
                     84    0.000    0.000    0.001    0.000 module.py:322(register_parameter)
                    100    0.000    0.000    0.001    0.000 {built-in method builtins.all}
                    213    0.001    0.000    0.001    0.000 module.py:1347(named_children)
                     93    0.000    0.000    0.001    0.000 module.py:361(add_module)
                    833    0.000    0.000    0.001    0.000 random.py:250(_randbelow_with_getrandbits)
                      7    0.000    0.000    0.001    0.000 inspect.py:325(getmembers)
                      3    0.000    0.000    0.001    0.000 learner.py:16(__init__)
                    900    0.000    0.000    0.001    0.000 layers.py:799(<genexpr>)
                    345    0.000    0.000    0.001    0.000 module.py:934(__getattr__)
                   4917    0.001    0.000    0.001    0.000 {method 'get' of 'dict' objects}
                     42    0.000    0.000    0.001    0.000 init.py:112(uniform_)
                     42    0.000    0.000    0.000    0.000 init.py:12(_no_grad_uniform_)
                    168    0.000    0.000    0.000    0.000 grad_mode.py:119(__enter__)
                    336    0.000    0.000    0.000    0.000 grad_mode.py:200(__init__)
                      3    0.000    0.000    0.000    0.000 adam.py:34(__init__)
                    168    0.000    0.000    0.000    0.000 grad_mode.py:123(__exit__)
                    490    0.000    0.000    0.000    0.000 abc.py:96(__instancecheck__)
                      3    0.000    0.000    0.000    0.000 optimizer.py:34(__init__)
                     90    0.000    0.000    0.000    0.000 utils.py:9(parse)
                     84    0.000    0.000    0.000    0.000 module.py:389(compute_should_use_set_data)
                     84    0.000    0.000    0.000    0.000 parameter.py:23(__new__)
                    350    0.000    0.000    0.000    0.000 enum.py:351(__iter__)
                      8    0.000    0.000    0.000    0.000 layer.py:71(<listcomp>)
                    168    0.000    0.000    0.000    0.000 grad_mode.py:114(__init__)
                    490    0.000    0.000    0.000    0.000 {built-in method _abc._abc_instancecheck}
                      1    0.000    0.000    0.000    0.000 agent.py:167(<listcomp>)
                    800    0.000    0.000    0.000    0.000 layer.py:142(clear)
                     84    0.000    0.000    0.000    0.000 {built-in method _make_subclass}
                     31    0.000    0.000    0.000    0.000 module.py:1240(parameters)
                     31    0.000    0.000    0.000    0.000 module.py:1264(named_parameters)
                   2359    0.000    0.000    0.000    0.000 enum.py:659(name)
                   1799    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
                     31    0.000    0.000    0.000    0.000 module.py:1227(_named_members)
                     84    0.000    0.000    0.000    0.000 tensor.py:906(grad)
                      1    0.000    0.000    0.000    0.000 layers.py:306(__init__)
                   1422    0.000    0.000    0.000    0.000 {method 'add' of 'set' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9632770: <MonsterLevel_Conver4_3counterfactsNOCRASH_2> in cluster <dcc> Done

Job <MonsterLevel_Conver4_3counterfactsNOCRASH_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed May 12 14:13:39 2021
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed May 12 15:14:25 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 12 15:14:25 2021
Terminated at Wed May 12 15:14:39 2021
Results reported at Wed May 12 15:14:39 2021

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

    CPU time :                                   4.78 sec.
    Max Memory :                                 4 MB
    Average Memory :                             4.00 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               16380.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                5
    Run time :                                   8 sec.
    Turnaround time :                            3660 sec.

The output (if any) is above this job summary.

