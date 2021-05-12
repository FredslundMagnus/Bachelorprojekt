
# Parameters

    Name :                      Maze_Conver4_3counterfactsNOCRASH-0
    Main :                      CFagent
    Level :                     Levels.Maze
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
    Num :                       0
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      66965353365 function calls (66562893138 primitive calls) in 86074.37 seconds

##    Ordered by: cumulative time
   List reduced from 517 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86117.163 86117.163 {built-in method builtins.exec}
                      1    4.355    4.355 86117.163 86117.163 <string>:1(<module>)
                      1  354.530  354.530 86112.807 86112.807 main.py:80(CFagent)
               10207545   39.894    0.000 23663.604    0.002 agent.py:29(learn)
                3402515 1839.479    0.001 22289.707    0.007 agent.py:212(counterfact)
               10207542  597.345    0.000 19252.878    0.002 learner.py:42(Qlearn)
                3402515   12.557    0.000 15571.339    0.005 game.py:42(step)
                3402515   19.139    0.000 14871.157    0.004 layers.py:827(step)
        447338461/44879925 1645.401    0.000 13587.995    0.000 module.py:866(_call_impl)
               34672383   91.240    0.000 12819.499    0.000 network.py:28(forward)
               34672383  414.295    0.000 12520.965    0.000 container.py:117(forward)
              110798114 9773.385    0.000 9773.385    0.000 {built-in method tensor}
              102973385   52.064    0.000 9618.368    0.000 game.py:38(board)
                3402515  344.679    0.000 9198.532    0.003 agent.py:54(_learn)
                3402515  340.647    0.000 8435.028    0.002 agent.py:204(_learn)
                3402515  284.153    0.000 8301.358    0.002 layers.py:17(step)
              339482307  509.387    0.000 7988.375    0.000 layer.py:106(move)
               10207542   79.978    0.000 7565.198    0.001 optimizer.py:84(wrapper)
               12228643  294.086    0.000 7331.708    0.001 agent.py:49(__call__)
               10207542   41.084    0.000 7200.908    0.001 grad_mode.py:24(decorate_context)
               10207542  288.638    0.000 7069.192    0.001 adam.py:55(step)
                5431171   97.057    0.000 6860.319    0.001 agent.py:176(choose_action)
                3402516  465.947    0.000 6524.509    0.002 layers.py:793(update)
               10207542 1467.895    0.000 6461.214    0.001 _functional.py:53(adam)
                3402515   99.796    0.000 5968.893    0.002 agent.py:117(_learn)
                3402515 4839.244    0.001 5839.515    0.002 replaybuffer.py:22(sample_data)
                3402515 4766.916    0.001 5729.671    0.002 replaybuffer.py:67(sample_data)
              108880472 3013.544    0.000 5571.360    0.000 layer.py:175(NoRock_update)
               10207542   37.721    0.000 4974.056    0.000 tensor.py:195(backward)
               10207542   38.928    0.000 4934.850    0.000 __init__.py:68(backward)
               10207542 4700.996    0.000 4700.996    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
               69344766  139.022    0.000 4644.587    0.000 conv.py:398(forward)
              339482307 1109.911    0.000 4578.283    0.000 layers.py:844(check)
               69344766   90.497    0.000 4441.320    0.000 conv.py:390(_conv_forward)
               69344766 4350.823    0.000 4350.823    0.000 {built-in method conv2d}
                3402515 1633.461    0.000 3671.051    0.001 agent.py:88(interveen)
               97212119  178.630    0.000 3534.878    0.000 linear.py:93(forward)
               97212119   76.191    0.000 3268.738    0.000 functional.py:1737(linear)
                3402515 1831.081    0.001 3233.844    0.001 replaybuffer.py:28(teleporter_save_data)
               97212119 3173.819    0.000 3173.819    0.000 {built-in method torch._C._nn.linear}
              339482307  435.365    0.000 2457.119    0.000 layers.py:838(isFree)
                3402515 1547.609    0.000 2351.557    0.001 agent.py:67(modify)
                3025680   43.251    0.000 2266.646    0.001 layers.py:849(restart)
             2179340898 1716.825    0.000 2021.754    0.000 layer.py:103(isFree)
                3025680   24.413    0.000 1965.164    0.001 level.py:8(__init__)
               15631158   90.529    0.000 1904.345    0.000 agent.py:59(modify_board)
              131884502   99.835    0.000 1894.442    0.000 activation.py:713(forward)
              131884502   98.803    0.000 1794.607    0.000 functional.py:1364(leaky_relu)
                4123963  244.737    0.000 1750.644    0.000 levels.py:9(generate)
               49656293 1748.853    0.000 1748.853    0.000 {built-in method cat}
              131884502 1674.308    0.000 1674.308    0.000 {built-in method torch._C._nn.leaky_relu}
                3402512   55.050    0.000 1438.353    0.000 agent.py:172(__call__)
              144524410 1376.167    0.000 1376.167    0.000 {built-in method clone}
             1303052433 1371.478    0.000 1371.478    0.000 layer.py:154(elements)
                3402515   51.647    0.000 1362.262    0.000 agent.py:112(__call__)
                5431171 1168.560    0.000 1361.295    0.000 agent.py:187(convert_values)
              339482307  815.267    0.000 1340.614    0.000 layers.py:168(check)
              190540780 1275.343    0.000 1275.343    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               15631158 1247.716    0.000 1247.716    0.000 {built-in method torch._C._nn.one_hot}
              347433464  283.221    0.000 1193.933    0.000 {built-in method builtins.any}
              190540780 1123.686    0.000 1123.686    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               10207542  197.491    0.000 1100.243    0.000 optimizer.py:189(zero_grad)
                3402515  840.202    0.000 1056.526    0.000 replaybuffer.py:73(CF_save_data)
             3650925202  678.497    0.000  958.005    0.000 enum.py:646(__hash__)
             3035033280  739.596    0.000  910.712    0.000 layers.py:809(<genexpr>)
              340251600  151.675    0.000  905.269    0.000 {built-in method builtins.all}
        13428906143/13428906140  782.058    0.000  864.654    0.000 {built-in method builtins.len}
             1796076261  438.513    0.000  792.708    0.000 layers.py:799(<genexpr>)
                3402515   58.469    0.000  762.248    0.000 replaybuffer.py:18(stacker)
               95270390  743.861    0.000  743.861    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                3402512   56.024    0.000  731.865    0.000 replaybuffer.py:63(stacker)
               12228643  273.632    0.000  729.689    0.000 exploration.py:53(softmaxer)
               95270390  641.136    0.000  641.136    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                9077040   75.906    0.000  636.537    0.000 level.py:41(notUsed)
               95270390  593.758    0.000  593.758    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               95270390  591.820    0.000  591.820    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              339482307  340.503    0.000  546.852    0.000 layers.py:141(check)
               18078636  208.144    0.000  533.648    0.000 random.py:315(sample)
                4123963  278.339    0.000  520.323    0.000 levels.py:75(RFS)
              666892814  399.295    0.000  497.833    0.000 tensor.py:906(grad)
                3402515  287.548    0.000  489.261    0.000 collector.py:46(collect)
              339482307  327.872    0.000  480.666    0.000 layers.py:48(check)
              339482307  321.218    0.000  475.445    0.000 layers.py:124(check)
             5467775020  472.627    0.000  472.627    0.000 layer.py:99(positions)
               95270390  448.063    0.000  448.063    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               10207542   18.156    0.000  417.281    0.000 loss.py:527(forward)
               10207542   37.111    0.000  399.125    0.000 functional.py:2898(mse_loss)
              108880472  370.557    0.000  370.557    0.000 layer.py:186(<listcomp>)
              339482307  226.382    0.000  341.649    0.000 layers.py:23(check)
              373198405  244.504    0.000  333.883    0.000 layer.py:134(remove)
              163558080  317.209    0.000  317.209    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              108880472  313.685    0.000  313.685    0.000 layer.py:187(<listcomp>)
               69344766   48.116    0.000  307.647    0.000 flatten.py:39(forward)
              543587546  208.955    0.000  295.157    0.000 layer.py:138(add)
             3650963985  279.515    0.000  279.515    0.000 {built-in method builtins.hash}
              444587221  188.938    0.000  277.176    0.000 random.py:250(_randbelow_with_getrandbits)
                9077040    8.915    0.000  262.714    0.000 level.py:38(elementsIn)
               69344766  259.531    0.000  259.531    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              302255617  257.940    0.000  257.940    0.000 level.py:32(inverse)
               24205440   35.080    0.000  250.345    0.000 layer.py:77(restart)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9624178: <Maze_Conver4_3counterfactsNOCRASH_0> in cluster <dcc> Done

Job <Maze_Conver4_3counterfactsNOCRASH_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun May  9 01:29:16 2021
Job was executed on host(s) <n-62-20-2>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun May  9 01:29:17 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun May  9 01:29:17 2021
Terminated at Mon May 10 01:24:43 2021
Results reported at Mon May 10 01:24:43 2021

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

    CPU time :                                   85899.08 sec.
    Max Memory :                                 9622 MB
    Average Memory :                             6420.00 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               6762.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86160 sec.
    Turnaround time :                            86127 sec.

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

    Name :                      Maze_Conver4_3counterfactsNOCRASH-0
    Main :                      CFagent
    Level :                     Levels.Maze
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
    Num :                       0
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              0 minutes.
    Hours used :                0 hours.

# Profiling


      244335 function calls (244046 primitive calls) in 13.79 seconds

##    Ordered by: cumulative time
   List reduced from 220 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000   13.796   13.796 {built-in method builtins.exec}
                      1    0.000    0.000   13.796   13.796 <string>:1(<module>)
                      1    0.000    0.000   13.796   13.796 main.py:80(CFagent)
                      3    0.000    0.000   13.690    4.563 agent.py:16(__init__)
                      3    0.000    0.000   13.690    4.563 network.py:37(__init__)
                      1    0.000    0.000   13.674   13.674 agent.py:109(__init__)
                      9    0.000    0.000   13.562    1.507 module.py:573(to)
                  111/9    0.001    0.000   13.562    1.507 module.py:385(_apply)
                     84    0.000    0.000   13.559    0.161 module.py:667(convert)
                     84   13.556    0.161   13.559    0.161 {method 'to' of 'torch._C._TensorBase' objects}
                      9    0.000    0.000    0.128    0.014 network.py:17(__init__)
                     18    0.000    0.000    0.116    0.006 conv.py:370(__init__)
                     18    0.013    0.001    0.116    0.006 conv.py:66(__init__)
                     42    0.000    0.000    0.106    0.003 init.py:347(kaiming_uniform_)
                     18    0.000    0.000    0.101    0.006 conv.py:114(reset_parameters)
                      1    0.002    0.002    0.098    0.098 game.py:9(__init__)
                     84    0.084    0.001    0.084    0.001 {method 'uniform_' of 'torch._C._TensorBase' objects}
                      1    0.000    0.000    0.081    0.081 layers.py:793(update)
                    100    0.001    0.000    0.076    0.001 layers.py:849(restart)
                    100    0.001    0.000    0.066    0.001 level.py:8(__init__)
                    127    0.008    0.000    0.061    0.000 levels.py:9(generate)
                    300    0.003    0.000    0.024    0.000 level.py:41(notUsed)
                     84    0.021    0.000    0.022    0.000 init.py:268(_calculate_fan_in_and_fan_out)
                     42    0.000    0.000    0.021    0.001 init.py:337(_calculate_correct_fan)
                    127    0.009    0.000    0.017    0.000 levels.py:75(RFS)
                      1    0.000    0.000    0.013    0.013 agent.py:39(__init__)
                    200    0.006    0.000    0.011    0.000 layers.py:36(reset)
                    300    0.000    0.000    0.010    0.000 level.py:38(elementsIn)
                   9813    0.009    0.000    0.009    0.000 level.py:32(inverse)
                      1    0.000    0.000    0.009    0.009 layers.py:751(__init__)
                    800    0.001    0.000    0.009    0.000 layer.py:77(restart)
                      1    0.000    0.000    0.009    0.009 agent.py:158(__init__)
                      7    0.000    0.000    0.009    0.001 layers.py:782(add)
                     24    0.000    0.000    0.008    0.000 linear.py:75(__init__)
                      8    0.001    0.000    0.008    0.001 layer.py:61(__init__)
                  24786    0.005    0.000    0.007    0.000 enum.py:646(__hash__)
                    300    0.003    0.000    0.006    0.000 level.py:39(<listcomp>)
                     24    0.000    0.000    0.006    0.000 linear.py:86(reset_parameters)
                      1    0.000    0.000    0.005    0.005 game.py:30(<setcomp>)
                   9200    0.004    0.000    0.005    0.000 layer.py:138(add)
                     41    0.002    0.000    0.005    0.000 game.py:30(<listcomp>)
                  20483    0.005    0.000    0.005    0.000 enum.py:352(<genexpr>)
                    127    0.002    0.000    0.004    0.000 level.py:16(<dictcomp>)
                      2    0.004    0.002    0.004    0.002 {built-in method zeros}
                   1698    0.003    0.000    0.004    0.000 module.py:950(__setattr__)
                   7620    0.003    0.000    0.004    0.000 levels.py:31(<genexpr>)
                      8    0.003    0.000    0.004    0.000 layer.py:175(NoRock_update)
                    114    0.001    0.000    0.004    0.000 module.py:250(__init__)
                    300    0.002    0.000    0.003    0.000 {built-in method _functools.reduce}
                   2232    0.001    0.000    0.003    0.000 random.py:285(choice)
                      1    0.000    0.000    0.003    0.003 replaybuffer.py:8(__init__)
                      1    0.003    0.003    0.003    0.003 replaybuffer.py:11(<listcomp>)
                    4/1    0.000    0.000    0.003    0.003 __init__.py:144(_lazy_init)
                    354    0.001    0.000    0.003    0.000 random.py:315(sample)
                  17056    0.003    0.000    0.003    0.000 layer.py:190(grid)
                   3099    0.002    0.000    0.002    0.000 random.py:250(_randbelow_with_getrandbits)
                      1    0.002    0.002    0.002    0.002 {built-in method torch._C._cuda_init}
                  24786    0.002    0.000    0.002    0.000 {built-in method builtins.hash}
                  24127    0.002    0.000    0.002    0.000 {method 'append' of 'list' objects}
                   2360    0.001    0.000    0.002    0.000 types.py:171(__get__)
                   1905    0.001    0.000    0.001    0.000 {method 'intersection_update' of 'set' objects}
                   5113    0.001    0.000    0.001    0.000 {built-in method builtins.isinstance}
                  12600    0.001    0.000    0.001    0.000 level.py:39(<lambda>)
                   1905    0.001    0.000    0.001    0.000 levels.py:85(<listcomp>)
                     33    0.000    0.000    0.001    0.000 activation.py:708(__init__)
                  10447    0.001    0.000    0.001    0.000 {method 'add' of 'set' objects}
                   5694    0.001    0.000    0.001    0.000 {built-in method builtins.min}
                    800    0.001    0.000    0.001    0.000 layer.py:147(clear2)
                   9216    0.001    0.000    0.001    0.000 layer.py:154(elements)
                   5694    0.001    0.000    0.001    0.000 {built-in method builtins.max}
                    100    0.000    0.000    0.001    0.000 {built-in method builtins.all}
                      7    0.000    0.000    0.001    0.000 inspect.py:325(getmembers)
                    213    0.000    0.000    0.001    0.000 module.py:1338(children)
                      9    0.000    0.000    0.001    0.000 container.py:62(__init__)
                    900    0.000    0.000    0.001    0.000 layers.py:799(<genexpr>)
                    213    0.000    0.000    0.001    0.000 module.py:1347(named_children)
                     18    0.000    0.000    0.001    0.000 flatten.py:34(__init__)
                    272    0.000    0.000    0.001    0.000 {built-in method builtins.hasattr}
                      3    0.000    0.000    0.001    0.000 learner.py:16(__init__)
                     84    0.000    0.000    0.001    0.000 module.py:322(register_parameter)
                    798    0.000    0.000    0.001    0.000 abc.py:96(__instancecheck__)
                     42    0.000    0.000    0.001    0.000 init.py:112(uniform_)
                   4917    0.001    0.000    0.001    0.000 {method 'get' of 'dict' objects}
                    407    0.000    0.000    0.000    0.000 {method 'items' of 'collections.OrderedDict' objects}
                    345    0.000    0.000    0.000    0.000 module.py:934(__getattr__)
                   1799    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
                     42    0.000    0.000    0.000    0.000 init.py:12(_no_grad_uniform_)
                   2359    0.000    0.000    0.000    0.000 enum.py:659(name)
                      3    0.000    0.000    0.000    0.000 adam.py:34(__init__)
                   4966    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
                      3    0.000    0.000    0.000    0.000 optimizer.py:34(__init__)
                   4064    0.000    0.000    0.000    0.000 {method 'remove' of 'set' objects}
                      8    0.000    0.000    0.000    0.000 layer.py:71(<listcomp>)
                    168    0.000    0.000    0.000    0.000 grad_mode.py:119(__enter__)
                     93    0.000    0.000    0.000    0.000 module.py:361(add_module)
                    336    0.000    0.000    0.000    0.000 grad_mode.py:200(__init__)
                    168    0.000    0.000    0.000    0.000 grad_mode.py:123(__exit__)
                    798    0.000    0.000    0.000    0.000 {built-in method _abc._abc_instancecheck}
                     90    0.000    0.000    0.000    0.000 utils.py:9(parse)
                     84    0.000    0.000    0.000    0.000 parameter.py:23(__new__)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9632719: <Maze_Conver4_3counterfactsNOCRASH_0> in cluster <dcc> Done

Job <Maze_Conver4_3counterfactsNOCRASH_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed May 12 14:11:08 2021
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed May 12 15:11:05 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 12 15:11:05 2021
Terminated at Wed May 12 15:11:37 2021
Results reported at Wed May 12 15:11:37 2021

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

    CPU time :                                   7.02 sec.
    Max Memory :                                 69 MB
    Average Memory :                             69.00 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               16315.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                5
    Run time :                                   32 sec.
    Turnaround time :                            3629 sec.

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

    Name :                      Maze_Conver4_3counterfactsNOCRASH-0
    Main :                      CFagent
    Level :                     Levels.Maze
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
    Num :                       0
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              0 minutes.
    Hours used :                0 hours.

# Profiling


      249067 function calls (248778 primitive calls) in 4.56 seconds

##    Ordered by: cumulative time
   List reduced from 220 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000    4.563    4.563 {built-in method builtins.exec}
                      1    0.000    0.000    4.563    4.563 <string>:1(<module>)
                      1    0.000    0.000    4.563    4.563 main.py:80(CFagent)
                      3    0.000    0.000    4.462    1.487 agent.py:16(__init__)
                      3    0.000    0.000    4.461    1.487 network.py:37(__init__)
                      1    0.000    0.000    4.441    4.441 agent.py:109(__init__)
                      9    0.000    0.000    4.435    0.493 module.py:573(to)
                  111/9    0.001    0.000    4.435    0.493 module.py:385(_apply)
                     84    0.000    0.000    4.433    0.053 module.py:667(convert)
                     84    4.430    0.053    4.433    0.053 {method 'to' of 'torch._C._TensorBase' objects}
                      1    0.002    0.002    0.097    0.097 game.py:9(__init__)
                      1    0.000    0.000    0.083    0.083 layers.py:793(update)
                    100    0.001    0.000    0.078    0.001 layers.py:849(restart)
                    100    0.001    0.000    0.067    0.001 level.py:8(__init__)
                    134    0.008    0.000    0.061    0.000 levels.py:9(generate)
                      9    0.000    0.000    0.026    0.003 network.py:17(__init__)
                    300    0.003    0.000    0.023    0.000 level.py:41(notUsed)
                    134    0.010    0.000    0.018    0.000 levels.py:75(RFS)
                     18    0.000    0.000    0.016    0.001 conv.py:370(__init__)
                     18    0.006    0.000    0.015    0.001 conv.py:66(__init__)
                     42    0.000    0.000    0.013    0.000 init.py:347(kaiming_uniform_)
                    200    0.006    0.000    0.012    0.000 layers.py:36(reset)
                      1    0.000    0.000    0.011    0.011 agent.py:158(__init__)
                      1    0.000    0.000    0.011    0.011 agent.py:39(__init__)
                     84    0.010    0.000    0.010    0.000 {method 'uniform_' of 'torch._C._TensorBase' objects}
                    300    0.000    0.000    0.010    0.000 level.py:38(elementsIn)
                      1    0.000    0.000    0.010    0.010 layers.py:751(__init__)
                   9946    0.009    0.000    0.009    0.000 level.py:32(inverse)
                      7    0.000    0.000    0.009    0.001 layers.py:782(add)
                    800    0.001    0.000    0.009    0.000 layer.py:77(restart)
                      8    0.001    0.000    0.008    0.001 layer.py:61(__init__)
                     18    0.000    0.000    0.008    0.000 conv.py:114(reset_parameters)
                     24    0.000    0.000    0.007    0.000 linear.py:75(__init__)
                  25311    0.005    0.000    0.007    0.000 enum.py:646(__hash__)
                    300    0.003    0.000    0.006    0.000 level.py:39(<listcomp>)
                     24    0.000    0.000    0.006    0.000 linear.py:86(reset_parameters)
                   9200    0.004    0.000    0.005    0.000 layer.py:138(add)
                    134    0.002    0.000    0.005    0.000 level.py:16(<dictcomp>)
                  20784    0.004    0.000    0.004    0.000 enum.py:352(<genexpr>)
                   8040    0.003    0.000    0.004    0.000 levels.py:31(<genexpr>)
                      8    0.003    0.000    0.004    0.000 layer.py:175(NoRock_update)
                   1698    0.002    0.000    0.004    0.000 module.py:950(__setattr__)
                    300    0.002    0.000    0.003    0.000 {built-in method _functools.reduce}
                   2344    0.001    0.000    0.003    0.000 random.py:285(choice)
                      1    0.000    0.000    0.003    0.003 game.py:30(<setcomp>)
                    114    0.001    0.000    0.003    0.000 module.py:250(__init__)
                      1    0.000    0.000    0.003    0.003 replaybuffer.py:8(__init__)
                      1    0.003    0.003    0.003    0.003 replaybuffer.py:11(<listcomp>)
                     41    0.001    0.000    0.003    0.000 game.py:30(<listcomp>)
                  17056    0.003    0.000    0.003    0.000 layer.py:190(grid)
                    368    0.001    0.000    0.003    0.000 random.py:315(sample)
                   3228    0.002    0.000    0.003    0.000 random.py:250(_randbelow_with_getrandbits)
                    4/1    0.000    0.000    0.002    0.002 __init__.py:144(_lazy_init)
                      1    0.002    0.002    0.002    0.002 {built-in method torch._C._cuda_init}
                  25311    0.002    0.000    0.002    0.000 {built-in method builtins.hash}
                     84    0.002    0.000    0.002    0.000 init.py:268(_calculate_fan_in_and_fan_out)
                  24379    0.002    0.000    0.002    0.000 {method 'append' of 'list' objects}
                     42    0.000    0.000    0.002    0.000 init.py:337(_calculate_correct_fan)
                   2010    0.002    0.000    0.002    0.000 {method 'intersection_update' of 'set' objects}
                   2010    0.001    0.000    0.001    0.000 levels.py:85(<listcomp>)
                  12600    0.001    0.000    0.001    0.000 level.py:39(<lambda>)
                   5141    0.001    0.000    0.001    0.000 {built-in method builtins.isinstance}
                   2360    0.001    0.000    0.001    0.000 types.py:171(__get__)
                  10972    0.001    0.000    0.001    0.000 {method 'add' of 'set' objects}
                   6032    0.001    0.000    0.001    0.000 {built-in method builtins.min}
                    800    0.001    0.000    0.001    0.000 layer.py:147(clear2)
                   9216    0.001    0.000    0.001    0.000 layer.py:154(elements)
                   6032    0.001    0.000    0.001    0.000 {built-in method builtins.max}
                     33    0.000    0.000    0.001    0.000 activation.py:708(__init__)
                    100    0.000    0.000    0.001    0.000 {built-in method builtins.all}
                    213    0.001    0.000    0.001    0.000 module.py:1338(children)
                    900    0.000    0.000    0.001    0.000 layers.py:799(<genexpr>)
                      7    0.000    0.000    0.001    0.000 inspect.py:325(getmembers)
                      9    0.000    0.000    0.001    0.000 container.py:62(__init__)
                      3    0.000    0.000    0.001    0.000 learner.py:16(__init__)
                    826    0.000    0.000    0.001    0.000 abc.py:96(__instancecheck__)
                    272    0.000    0.000    0.001    0.000 {built-in method builtins.hasattr}
                     18    0.000    0.000    0.001    0.000 flatten.py:34(__init__)
                     84    0.000    0.000    0.000    0.000 module.py:322(register_parameter)
                   5157    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
                      3    0.000    0.000    0.000    0.000 adam.py:34(__init__)
                      3    0.000    0.000    0.000    0.000 optimizer.py:34(__init__)
                   4288    0.000    0.000    0.000    0.000 {method 'remove' of 'set' objects}
                    345    0.000    0.000    0.000    0.000 module.py:934(__getattr__)
                    826    0.000    0.000    0.000    0.000 {built-in method _abc._abc_instancecheck}
                     42    0.000    0.000    0.000    0.000 init.py:112(uniform_)
                      8    0.000    0.000    0.000    0.000 layer.py:71(<listcomp>)
                   4917    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
                     42    0.000    0.000    0.000    0.000 init.py:12(_no_grad_uniform_)
                    168    0.000    0.000    0.000    0.000 grad_mode.py:119(__enter__)
                     93    0.000    0.000    0.000    0.000 module.py:361(add_module)
                    336    0.000    0.000    0.000    0.000 grad_mode.py:200(__init__)
                   2359    0.000    0.000    0.000    0.000 enum.py:659(name)
                    800    0.000    0.000    0.000    0.000 layer.py:142(clear)
              3246/3243    0.000    0.000    0.000    0.000 {built-in method builtins.len}
                    168    0.000    0.000    0.000    0.000 grad_mode.py:123(__exit__)
                   3228    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
                     90    0.000    0.000    0.000    0.000 utils.py:9(parse)
                   1799    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
                      1    0.000    0.000    0.000    0.000 agent.py:167(<listcomp>)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9632762: <Maze_Conver4_3counterfactsNOCRASH_0> in cluster <dcc> Done

Job <Maze_Conver4_3counterfactsNOCRASH_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed May 12 14:13:38 2021
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed May 12 15:13:27 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 12 15:13:27 2021
Terminated at Wed May 12 15:13:36 2021
Results reported at Wed May 12 15:13:36 2021

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

    CPU time :                                   5.14 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   9 sec.
    Turnaround time :                            3598 sec.

The output (if any) is above this job summary.

