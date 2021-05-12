
# Parameters

    Name :                      MonsterLevel_Conver4_3counterfactsNOCRASH-1
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
    Num :                       1
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      59414505042 function calls (59077569867 primitive calls) in 86109.52 seconds

##    Ordered by: cumulative time
   List reduced from 508 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86109.518 86109.518 {built-in method builtins.exec}
                      1    4.041    4.041 86109.518 86109.518 <string>:1(<module>)
                      1  260.794  260.794 86105.476 86105.476 main.py:80(CFagent)
                2274356 4266.330    0.002 23805.607    0.010 agent.py:212(counterfact)
                6823068   26.346    0.000 21437.924    0.003 agent.py:29(learn)
                6823068  536.021    0.000 17875.924    0.003 learner.py:42(Qlearn)
                2274356   10.162    0.000 17460.873    0.008 game.py:42(step)
                2274356   13.713    0.000 16978.746    0.007 layers.py:827(step)
        372592461/35658977 1539.022    0.000 14123.194    0.000 module.py:866(_call_impl)
               28835909   83.974    0.000 13464.285    0.000 network.py:28(forward)
               28835909  426.735    0.000 13196.814    0.000 container.py:117(forward)
                6457723  140.952    0.000 10248.504    0.002 agent.py:176(choose_action)
                2274357  360.571    0.000 8759.738    0.004 layers.py:793(update)
                2274356  252.737    0.000 8258.570    0.004 agent.py:54(_learn)
               11006406  307.307    0.000 8210.032    0.001 agent.py:49(__call__)
                2274356  211.431    0.000 8188.682    0.004 layers.py:17(step)
              223786834  656.118    0.000 7956.088    0.000 layer.py:106(move)
                2274356  251.548    0.000 7672.153    0.003 agent.py:204(_learn)
                6823068   61.873    0.000 7622.670    0.001 optimizer.py:84(wrapper)
                6823068   29.330    0.000 7331.036    0.001 grad_mode.py:24(decorate_context)
                6823068  200.828    0.000 7236.466    0.001 adam.py:55(step)
                6823068 1490.020    0.000 6809.023    0.001 _functional.py:53(adam)
               81625112 6354.715    0.000 6354.715    0.000 {built-in method tensor}
               76288620   52.745    0.000 6232.681    0.000 game.py:38(board)
                2274356   72.546    0.000 5467.309    0.002 agent.py:117(_learn)
              223786834  754.031    0.000 5400.255    0.000 layers.py:844(check)
                2274356 2710.407    0.001 5070.438    0.002 replaybuffer.py:28(teleporter_save_data)
                8114667   67.994    0.000 4755.453    0.001 layers.py:849(restart)
               57671818  128.951    0.000 4669.872    0.000 conv.py:398(forward)
               57671818   70.885    0.000 4486.849    0.000 conv.py:390(_conv_forward)
               57671818 4415.964    0.000 4415.964    0.000 {built-in method conv2d}
                6823068   28.102    0.000 4402.348    0.001 tensor.py:195(backward)
                6823068   26.929    0.000 4373.224    0.001 __init__.py:68(backward)
                2274356 2513.428    0.001 4214.701    0.002 agent.py:88(interveen)
                6823068 4188.110    0.001 4188.110    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                8114667   33.830    0.000 4073.200    0.001 level.py:8(__init__)
               54584538 2574.722    0.000 4033.199    0.000 layer.py:159(update)
               81959015  168.235    0.000 3882.413    0.000 linear.py:93(forward)
                8114667  607.242    0.000 3703.454    0.000 levels.py:428(generate)
                2274356 2854.829    0.001 3641.417    0.002 replaybuffer.py:22(sample_data)
               81959015   68.203    0.000 3637.969    0.000 functional.py:1737(linear)
                2274356 2829.935    0.001 3594.141    0.002 replaybuffer.py:67(sample_data)
               81959015 3552.597    0.000 3552.597    0.000 {built-in method torch._C._nn.linear}
              223786834 1736.709    0.000 3070.925    0.000 layers.py:538(check)
               40573335  383.573    0.000 2495.042    0.000 level.py:41(notUsed)
              187791602 2486.846    0.000 2486.846    0.000 {built-in method clone}
                2274356 1733.746    0.001 2444.360    0.001 replaybuffer.py:73(CF_save_data)
                2274356 1543.910    0.001 2230.476    0.001 agent.py:67(modify)
              110794924   84.898    0.000 2171.070    0.000 activation.py:713(forward)
              110794924   91.901    0.000 2086.172    0.000 functional.py:1364(leaky_relu)
                6457723 1691.205    0.000 2002.642    0.000 agent.py:187(convert_values)
               13280762   90.904    0.000 1979.333    0.000 agent.py:59(modify_board)
              110794924 1974.389    0.000 1974.389    0.000 {built-in method torch._C._nn.leaky_relu}
               36024322 1573.675    0.000 1573.675    0.000 {built-in method cat}
              231689293  184.149    0.000 1562.395    0.000 {built-in method builtins.any}
              223786834  313.319    0.000 1453.350    0.000 layers.py:838(isFree)
              127363936 1395.567    0.000 1395.567    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
             5522089914  956.219    0.000 1389.334    0.000 enum.py:646(__hash__)
             1568518389  440.960    0.000 1378.924    0.000 layers.py:809(<genexpr>)
               13280762 1255.323    0.000 1255.323    0.000 {built-in method torch._C._nn.one_hot}
              127363936 1224.991    0.000 1224.991    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                2274356   41.138    0.000 1197.713    0.001 agent.py:172(__call__)
               40573335   33.593    0.000 1149.454    0.000 level.py:38(elementsIn)
             1281456116  921.120    0.000 1140.031    0.000 layer.py:103(isFree)
                2274356   38.318    0.000 1123.877    0.000 agent.py:112(__call__)
                6823068  165.935    0.000 1045.478    0.000 optimizer.py:189(zero_grad)
              224866226  531.456    0.000  854.532    0.000 layers.py:575(isDead)
               11006406  307.315    0.000  846.312    0.000 exploration.py:53(softmaxer)
             1873081688  829.566    0.000  829.566    0.000 layer.py:154(elements)
              223786834  554.792    0.000  770.970    0.000 layers.py:77(check)
               63681968  758.802    0.000  758.802    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               40573335  368.540    0.000  745.380    0.000 level.py:39(<listcomp>)
               45122047  265.621    0.000  682.538    0.000 random.py:315(sample)
              203346720  659.462    0.000  659.462    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               63681968  654.729    0.000  654.729    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               63681968  633.142    0.000  633.142    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               63681968  631.962    0.000  631.962    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                2274356   40.176    0.000  621.606    0.000 replaybuffer.py:18(stacker)
               48803966  620.841    0.000  620.841    0.000 {method 'item' of 'torch._C._TensorBase' objects}
             1731029610  614.134    0.000  614.134    0.000 level.py:32(inverse)
                2274356   40.778    0.000  603.846    0.000 replaybuffer.py:63(stacker)
               48688002   60.191    0.000  597.379    0.000 layer.py:77(restart)
        7388821866/7388821863  519.732    0.000  589.118    0.000 {built-in method builtins.len}
              523101756  445.082    0.000  587.152    0.000 layer.py:134(remove)
              321065014  110.528    0.000  574.064    0.000 random.py:244(randint)
              729526292  372.092    0.000  531.050    0.000 random.py:250(_randbelow_with_getrandbits)
                2274356  298.180    0.000  493.552    0.000 collector.py:46(collect)
               63681968  486.602    0.000  486.602    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              891964918  344.162    0.000  466.012    0.000 layer.py:138(add)
             4477903316  464.524    0.000  464.524    0.000 layer.py:99(positions)
              321065014  197.626    0.000  463.535    0.000 random.py:200(randrange)
             5522116041  433.119    0.000  433.119    0.000 {built-in method builtins.hash}
                8114767  210.440    0.000  418.318    0.000 layers.py:36(reset)
              223786834  249.428    0.000  386.631    0.000 layers.py:48(check)
             2093586122  385.781    0.000  385.781    0.000 enum.py:352(<genexpr>)
              445773860  299.721    0.000  373.401    0.000 tensor.py:906(grad)
               40573335  230.006    0.000  370.481    0.000 {built-in method _functools.reduce}
               57671818   37.519    0.000  349.191    0.000 flatten.py:39(forward)
                6823068    9.673    0.000  345.969    0.000 loss.py:527(forward)
              223786834  123.866    0.000  344.103    0.000 layers.py:572(<listcomp>)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9624185: <MonsterLevel_Conver4_3counterfactsNOCRASH_1> in cluster <dcc> Done

Job <MonsterLevel_Conver4_3counterfactsNOCRASH_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun May  9 01:29:17 2021
Job was executed on host(s) <n-62-11-16>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon May 10 02:31:07 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon May 10 02:31:07 2021
Terminated at Tue May 11 02:26:20 2021
Results reported at Tue May 11 02:26:20 2021

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

    CPU time :                                   85900.38 sec.
    Max Memory :                                 7719 MB
    Average Memory :                             5587.68 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               8665.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86113 sec.
    Turnaround time :                            176223 sec.

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

    Name :                      MonsterLevel_Conver4_3counterfactsNOCRASH-1
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
    Num :                       1
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              0 minutes.
    Hours used :                0 hours.

# Profiling


      247320 function calls (247031 primitive calls) in 7.98 seconds

##    Ordered by: cumulative time
   List reduced from 208 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000    7.980    7.980 {built-in method builtins.exec}
                      1    0.000    0.000    7.980    7.980 <string>:1(<module>)
                      1    0.000    0.000    7.979    7.979 main.py:80(CFagent)
                      3    0.000    0.000    7.862    2.621 agent.py:16(__init__)
                      3    0.000    0.000    7.862    2.621 network.py:37(__init__)
                      1    0.000    0.000    7.846    7.846 agent.py:109(__init__)
                      9    0.000    0.000    7.812    0.868 module.py:573(to)
                  111/9    0.001    0.000    7.812    0.868 module.py:385(_apply)
                     84    0.000    0.000    7.810    0.093 module.py:667(convert)
                     84    7.808    0.093    7.810    0.093 {method 'to' of 'torch._C._TensorBase' objects}
                      1    0.002    0.002    0.110    0.110 game.py:9(__init__)
                      1    0.000    0.000    0.091    0.091 layers.py:793(update)
                    100    0.001    0.000    0.085    0.001 layers.py:849(restart)
                    100    0.000    0.000    0.076    0.001 level.py:8(__init__)
                    100    0.008    0.000    0.072    0.001 levels.py:428(generate)
                    500    0.005    0.000    0.057    0.000 level.py:41(notUsed)
                      9    0.000    0.000    0.049    0.005 network.py:17(__init__)
                     18    0.000    0.000    0.039    0.002 conv.py:370(__init__)
                     18    0.009    0.000    0.039    0.002 conv.py:66(__init__)
                     42    0.000    0.000    0.033    0.001 init.py:347(kaiming_uniform_)
                  21306    0.032    0.000    0.032    0.000 level.py:32(inverse)
                     84    0.031    0.000    0.031    0.000 {method 'uniform_' of 'torch._C._TensorBase' objects}
                     18    0.000    0.000    0.029    0.002 conv.py:114(reset_parameters)
                    500    0.000    0.000    0.015    0.000 level.py:38(elementsIn)
                      1    0.000    0.000    0.013    0.013 agent.py:39(__init__)
                    200    0.006    0.000    0.012    0.000 layers.py:36(reset)
                      1    0.000    0.000    0.012    0.012 layers.py:751(__init__)
                      5    0.000    0.000    0.011    0.002 layers.py:782(add)
                    500    0.005    0.000    0.010    0.000 level.py:39(<listcomp>)
                  39049    0.006    0.000    0.009    0.000 enum.py:646(__hash__)
                      6    0.000    0.000    0.009    0.001 layer.py:61(__init__)
                      1    0.000    0.000    0.009    0.009 agent.py:158(__init__)
                    600    0.001    0.000    0.008    0.000 layer.py:77(restart)
                     24    0.000    0.000    0.007    0.000 linear.py:75(__init__)
                  27836    0.006    0.000    0.006    0.000 enum.py:352(<genexpr>)
                     24    0.000    0.000    0.005    0.000 linear.py:86(reset_parameters)
                      6    0.004    0.001    0.005    0.001 layer.py:159(update)
                      1    0.000    0.000    0.005    0.005 game.py:30(<setcomp>)
                    500    0.003    0.000    0.005    0.000 {built-in method _functools.reduce}
                    500    0.002    0.000    0.005    0.000 random.py:315(sample)
                     41    0.002    0.000    0.005    0.000 game.py:30(<listcomp>)
                   7998    0.003    0.000    0.005    0.000 layer.py:138(add)
                   1698    0.003    0.000    0.004    0.000 module.py:950(__setattr__)
                      2    0.004    0.002    0.004    0.002 {built-in method zeros}
                    114    0.001    0.000    0.004    0.000 module.py:250(__init__)
                    100    0.001    0.000    0.003    0.000 level.py:16(<dictcomp>)
                  39049    0.003    0.000    0.003    0.000 {built-in method builtins.hash}
                  16892    0.003    0.000    0.003    0.000 layer.py:190(grid)
                      1    0.000    0.000    0.003    0.003 replaybuffer.py:8(__init__)
                      1    0.003    0.003    0.003    0.003 replaybuffer.py:11(<listcomp>)
                    4/1    0.000    0.000    0.002    0.002 __init__.py:144(_lazy_init)
                      1    0.002    0.002    0.002    0.002 {built-in method torch._C._cuda_init}
                     84    0.002    0.000    0.002    0.000 init.py:268(_calculate_fan_in_and_fan_out)
                      1    0.002    0.002    0.002    0.002 layers.py:529(__init__)
                  21000    0.002    0.000    0.002    0.000 level.py:39(<lambda>)
                     42    0.000    0.000    0.002    0.000 init.py:337(_calculate_correct_fan)
                   2190    0.001    0.000    0.002    0.000 types.py:171(__get__)
                   2236    0.001    0.000    0.002    0.000 random.py:250(_randbelow_with_getrandbits)
                     33    0.000    0.000    0.002    0.000 activation.py:708(__init__)
                   5273    0.001    0.000    0.001    0.000 {built-in method builtins.isinstance}
                  17849    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
                    600    0.001    0.000    0.001    0.000 layer.py:147(clear2)
                      9    0.000    0.000    0.001    0.000 container.py:62(__init__)
                   8010    0.001    0.000    0.001    0.000 layer.py:154(elements)
                    100    0.000    0.000    0.001    0.000 {built-in method builtins.all}
                   1090    0.000    0.000    0.001    0.000 abc.py:96(__instancecheck__)
                      5    0.000    0.000    0.001    0.000 inspect.py:325(getmembers)
                    700    0.000    0.000    0.001    0.000 layers.py:799(<genexpr>)
                      3    0.000    0.000    0.001    0.000 learner.py:16(__init__)
                     18    0.000    0.000    0.001    0.000 flatten.py:34(__init__)
                    272    0.000    0.000    0.001    0.000 {built-in method builtins.hasattr}
                   1799    0.001    0.000    0.001    0.000 {method 'split' of 'str' objects}
                     84    0.000    0.000    0.000    0.000 module.py:322(register_parameter)
                   2189    0.000    0.000    0.000    0.000 enum.py:659(name)
                   1090    0.000    0.000    0.000    0.000 {built-in method _abc._abc_instancecheck}
                    648    0.000    0.000    0.000    0.000 enum.py:351(__iter__)
                     42    0.000    0.000    0.000    0.000 init.py:112(uniform_)
                      3    0.000    0.000    0.000    0.000 adam.py:34(__init__)
                      3    0.000    0.000    0.000    0.000 optimizer.py:34(__init__)
                     42    0.000    0.000    0.000    0.000 init.py:12(_no_grad_uniform_)
                    345    0.000    0.000    0.000    0.000 module.py:934(__getattr__)
                   4917    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
                      6    0.000    0.000    0.000    0.000 layer.py:71(<listcomp>)
                    168    0.000    0.000    0.000    0.000 grad_mode.py:119(__enter__)
                     93    0.000    0.000    0.000    0.000 module.py:361(add_module)
                    168    0.000    0.000    0.000    0.000 grad_mode.py:123(__exit__)
                    336    0.000    0.000    0.000    0.000 grad_mode.py:200(__init__)
                   3556    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
                     90    0.000    0.000    0.000    0.000 utils.py:9(parse)
                     84    0.000    0.000    0.000    0.000 parameter.py:23(__new__)
                    213    0.000    0.000    0.000    0.000 module.py:1338(children)
                    600    0.000    0.000    0.000    0.000 layer.py:142(clear)
                      1    0.000    0.000    0.000    0.000 agent.py:167(<listcomp>)
                    168    0.000    0.000    0.000    0.000 grad_mode.py:114(__init__)
                     84    0.000    0.000    0.000    0.000 {built-in method _make_subclass}
                      1    0.000    0.000    0.000    0.000 layers.py:73(__init__)
                    500    0.000    0.000    0.000    0.000 enum.py:354(__len__)
                     84    0.000    0.000    0.000    0.000 module.py:389(compute_should_use_set_data)
                     31    0.000    0.000    0.000    0.000 module.py:1240(parameters)
                     31    0.000    0.000    0.000    0.000 module.py:1264(named_parameters)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9632726: <MonsterLevel_Conver4_3counterfactsNOCRASH_1> in cluster <dcc> Done

Job <MonsterLevel_Conver4_3counterfactsNOCRASH_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed May 12 14:11:09 2021
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed May 12 15:12:44 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 12 15:12:44 2021
Terminated at Wed May 12 15:12:56 2021
Results reported at Wed May 12 15:12:56 2021

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

    CPU time :                                   5.36 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   12 sec.
    Turnaround time :                            3707 sec.

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

    Name :                      MonsterLevel_Conver4_3counterfactsNOCRASH-1
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
    Num :                       1
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              0 minutes.
    Hours used :                0 hours.

# Profiling


      247446 function calls (247157 primitive calls) in 3.51 seconds

##    Ordered by: cumulative time
   List reduced from 208 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000    3.511    3.511 {built-in method builtins.exec}
                      1    0.000    0.000    3.511    3.511 <string>:1(<module>)
                      1    0.000    0.000    3.511    3.511 main.py:80(CFagent)
                      3    0.000    0.000    3.407    1.136 agent.py:16(__init__)
                      3    0.000    0.000    3.406    1.135 network.py:37(__init__)
                      1    0.000    0.000    3.390    3.390 agent.py:109(__init__)
                      9    0.000    0.000    3.389    0.377 module.py:573(to)
                  111/9    0.001    0.000    3.389    0.377 module.py:385(_apply)
                     84    0.000    0.000    3.388    0.040 module.py:667(convert)
                     84    3.386    0.040    3.387    0.040 {method 'to' of 'torch._C._TensorBase' objects}
                      1    0.002    0.002    0.101    0.101 game.py:9(__init__)
                      1    0.000    0.000    0.088    0.088 layers.py:793(update)
                    100    0.001    0.000    0.082    0.001 layers.py:849(restart)
                    100    0.000    0.000    0.073    0.001 level.py:8(__init__)
                    100    0.008    0.000    0.069    0.001 levels.py:428(generate)
                    500    0.005    0.000    0.054    0.000 level.py:41(notUsed)
                  21285    0.030    0.000    0.030    0.000 level.py:32(inverse)
                      9    0.000    0.000    0.017    0.002 network.py:17(__init__)
                    500    0.000    0.000    0.015    0.000 level.py:38(elementsIn)
                    200    0.005    0.000    0.010    0.000 layers.py:36(reset)
                    500    0.005    0.000    0.010    0.000 level.py:39(<listcomp>)
                      1    0.000    0.000    0.009    0.009 agent.py:158(__init__)
                  38944    0.006    0.000    0.009    0.000 enum.py:646(__hash__)
                     42    0.000    0.000    0.009    0.000 init.py:347(kaiming_uniform_)
                      1    0.000    0.000    0.009    0.009 layers.py:751(__init__)
                      1    0.000    0.000    0.009    0.009 agent.py:39(__init__)
                      5    0.000    0.000    0.009    0.002 layers.py:782(add)
                     84    0.008    0.000    0.008    0.000 {method 'uniform_' of 'torch._C._TensorBase' objects}
                    600    0.001    0.000    0.008    0.000 layer.py:77(restart)
                     18    0.000    0.000    0.007    0.000 conv.py:370(__init__)
                     24    0.000    0.000    0.006    0.000 linear.py:75(__init__)
                     18    0.001    0.000    0.006    0.000 conv.py:66(__init__)
                      6    0.000    0.000    0.006    0.001 layer.py:61(__init__)
                  27836    0.005    0.000    0.005    0.000 enum.py:352(<genexpr>)
                     24    0.000    0.000    0.005    0.000 linear.py:86(reset_parameters)
                      6    0.004    0.001    0.005    0.001 layer.py:159(update)
                    500    0.003    0.000    0.005    0.000 {built-in method _functools.reduce}
                     18    0.000    0.000    0.005    0.000 conv.py:114(reset_parameters)
                    500    0.002    0.000    0.005    0.000 random.py:315(sample)
                   1698    0.003    0.000    0.004    0.000 module.py:950(__setattr__)
                   8005    0.003    0.000    0.004    0.000 layer.py:138(add)
                    114    0.001    0.000    0.004    0.000 module.py:250(__init__)
                    100    0.001    0.000    0.003    0.000 level.py:16(<dictcomp>)
                      1    0.000    0.000    0.003    0.003 replaybuffer.py:8(__init__)
                      1    0.003    0.003    0.003    0.003 replaybuffer.py:11(<listcomp>)
                  38944    0.003    0.000    0.003    0.000 {built-in method builtins.hash}
                  16892    0.002    0.000    0.002    0.000 layer.py:190(grid)
                      1    0.000    0.000    0.002    0.002 game.py:30(<setcomp>)
                     41    0.001    0.000    0.002    0.000 game.py:30(<listcomp>)
                      1    0.002    0.002    0.002    0.002 layers.py:529(__init__)
                    4/1    0.000    0.000    0.002    0.002 __init__.py:144(_lazy_init)
                  21000    0.002    0.000    0.002    0.000 level.py:39(<lambda>)
                      1    0.002    0.002    0.002    0.002 {built-in method torch._C._cuda_init}
                   2232    0.001    0.000    0.002    0.000 random.py:250(_randbelow_with_getrandbits)
                     33    0.000    0.000    0.001    0.000 activation.py:708(__init__)
                   5273    0.001    0.000    0.001    0.000 {built-in method builtins.isinstance}
                  17870    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
                      9    0.000    0.000    0.001    0.000 container.py:62(__init__)
                    600    0.001    0.000    0.001    0.000 layer.py:147(clear2)
                   8017    0.001    0.000    0.001    0.000 layer.py:154(elements)
                   2190    0.001    0.000    0.001    0.000 types.py:171(__get__)
                     84    0.001    0.000    0.001    0.000 init.py:268(_calculate_fan_in_and_fan_out)
                   1090    0.000    0.000    0.001    0.000 abc.py:96(__instancecheck__)
                    100    0.000    0.000    0.001    0.000 {built-in method builtins.all}
                      3    0.000    0.000    0.001    0.000 learner.py:16(__init__)
                     42    0.000    0.000    0.001    0.000 init.py:337(_calculate_correct_fan)
                      5    0.000    0.000    0.001    0.000 inspect.py:325(getmembers)
                     18    0.000    0.000    0.001    0.000 flatten.py:34(__init__)
                    272    0.000    0.000    0.000    0.000 {built-in method builtins.hasattr}
                    700    0.000    0.000    0.000    0.000 layers.py:799(<genexpr>)
                     84    0.000    0.000    0.000    0.000 module.py:322(register_parameter)
                      3    0.000    0.000    0.000    0.000 adam.py:34(__init__)
                   1090    0.000    0.000    0.000    0.000 {built-in method _abc._abc_instancecheck}
                      3    0.000    0.000    0.000    0.000 optimizer.py:34(__init__)
                     42    0.000    0.000    0.000    0.000 init.py:112(uniform_)
                   4917    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
                    345    0.000    0.000    0.000    0.000 module.py:934(__getattr__)
                     42    0.000    0.000    0.000    0.000 init.py:12(_no_grad_uniform_)
                    168    0.000    0.000    0.000    0.000 grad_mode.py:119(__enter__)
                    648    0.000    0.000    0.000    0.000 enum.py:351(__iter__)
                   3586    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
                    336    0.000    0.000    0.000    0.000 grad_mode.py:200(__init__)
                     93    0.000    0.000    0.000    0.000 module.py:361(add_module)
                    213    0.000    0.000    0.000    0.000 module.py:1338(children)
                    168    0.000    0.000    0.000    0.000 grad_mode.py:123(__exit__)
                      1    0.000    0.000    0.000    0.000 agent.py:167(<listcomp>)
                     90    0.000    0.000    0.000    0.000 utils.py:9(parse)
                      6    0.000    0.000    0.000    0.000 layer.py:71(<listcomp>)
                    500    0.000    0.000    0.000    0.000 enum.py:354(__len__)
                     84    0.000    0.000    0.000    0.000 parameter.py:23(__new__)
                      1    0.000    0.000    0.000    0.000 layers.py:73(__init__)
                     84    0.000    0.000    0.000    0.000 module.py:389(compute_should_use_set_data)
                   1799    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
                   2189    0.000    0.000    0.000    0.000 enum.py:659(name)
                    168    0.000    0.000    0.000    0.000 grad_mode.py:114(__init__)
                     31    0.000    0.000    0.000    0.000 module.py:1240(parameters)
                      2    0.000    0.000    0.000    0.000 {built-in method zeros}
                    600    0.000    0.000    0.000    0.000 layer.py:142(clear)
                     31    0.000    0.000    0.000    0.000 module.py:1264(named_parameters)
                     31    0.000    0.000    0.000    0.000 module.py:1227(_named_members)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9632769: <MonsterLevel_Conver4_3counterfactsNOCRASH_1> in cluster <dcc> Done

Job <MonsterLevel_Conver4_3counterfactsNOCRASH_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed May 12 14:13:39 2021
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed May 12 15:14:11 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 12 15:14:11 2021
Terminated at Wed May 12 15:14:17 2021
Results reported at Wed May 12 15:14:17 2021

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

    CPU time :                                   4.69 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   7 sec.
    Turnaround time :                            3638 sec.

The output (if any) is above this job summary.

