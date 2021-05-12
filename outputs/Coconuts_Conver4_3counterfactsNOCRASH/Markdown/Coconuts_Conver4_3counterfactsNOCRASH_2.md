
# Parameters

    Name :                      Coconuts_Conver4_3counterfactsNOCRASH-2
    Main :                      CFagent
    Level :                     Levels.Coconuts
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


      68898521499 function calls (68517759752 primitive calls) in 86121.28 seconds

##    Ordered by: cumulative time
   List reduced from 511 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86121.284 86121.284 {built-in method builtins.exec}
                      1    4.215    4.215 86121.284 86121.284 <string>:1(<module>)
                      1  364.033  364.033 86117.069 86117.069 main.py:80(CFagent)
               10328538   39.379    0.000 23931.803    0.002 agent.py:29(learn)
               10328538  606.227    0.000 19435.375    0.002 learner.py:42(Qlearn)
                3442846   14.120    0.000 18278.783    0.005 game.py:42(step)
                3442846 1366.069    0.000 18086.866    0.005 agent.py:212(counterfact)
                3442846   19.250    0.000 17600.447    0.005 layers.py:827(step)
        423966214/43206158 1600.589    0.000 12999.511    0.000 module.py:866(_call_impl)
               32877620   87.139    0.000 12238.911    0.000 network.py:28(forward)
                3442846  301.725    0.000 12199.850    0.004 layers.py:17(step)
               32877620  388.699    0.000 11948.853    0.000 container.py:117(forward)
              343553763 1210.179    0.000 11869.790    0.000 layer.py:106(move)
                3442846  349.823    0.000 9302.563    0.003 agent.py:54(_learn)
                3442846  346.860    0.000 8532.526    0.002 agent.py:204(_learn)
               97849893 7758.117    0.000 7758.117    0.000 {built-in method tensor}
               89936846   46.838    0.000 7597.836    0.000 game.py:38(board)
               10328538   81.959    0.000 7545.014    0.001 optimizer.py:84(wrapper)
               10328538   44.125    0.000 7174.409    0.001 grad_mode.py:24(decorate_context)
              343553763 1209.354    0.000 7155.525    0.000 layers.py:844(check)
               10328538  296.740    0.000 7039.836    0.001 adam.py:55(step)
               11272112  279.520    0.000 6805.290    0.001 agent.py:49(__call__)
               10328538 1453.902    0.000 6405.384    0.001 _functional.py:53(adam)
                3442846  101.723    0.000 6031.701    0.002 agent.py:117(_learn)
                3442846 4850.543    0.001 5882.092    0.002 replaybuffer.py:22(sample_data)
                3442846 4750.806    0.001 5745.459    0.002 replaybuffer.py:67(sample_data)
                4391278   80.193    0.000 5573.194    0.001 agent.py:176(choose_action)
                3442847  469.798    0.000 5354.285    0.002 layers.py:793(update)
               96399681 2986.209    0.000 5258.696    0.000 layer.py:159(update)
               10328538   39.845    0.000 5086.416    0.000 tensor.py:195(backward)
               10328538   38.570    0.000 5045.202    0.000 __init__.py:68(backward)
               10328538 4814.977    0.000 4814.977    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
               65755240  141.854    0.000 4419.759    0.000 conv.py:398(forward)
               65755240  100.318    0.000 4212.362    0.000 conv.py:390(_conv_forward)
                3442846 2040.093    0.001 4122.702    0.001 agent.py:88(interveen)
                3442846 2343.459    0.001 4118.133    0.001 replaybuffer.py:28(teleporter_save_data)
               65755240 4112.044    0.000 4112.044    0.000 {built-in method conv2d}
               91747168  184.018    0.000 3381.677    0.000 linear.py:93(forward)
               91747168   72.893    0.000 3107.134    0.000 functional.py:1737(linear)
               91747168 3017.950    0.000 3017.950    0.000 {built-in method torch._C._nn.linear}
              343553763  491.018    0.000 2642.128    0.000 layers.py:838(isFree)
                3442846 1533.745    0.000 2343.123    0.001 agent.py:67(modify)
              343553763 1536.608    0.000 2154.991    0.000 layers.py:471(check)
             2245239188 1823.591    0.000 2151.110    0.000 layer.py:103(isFree)
              343553763 1315.151    0.000 1822.835    0.000 layers.py:77(check)
               14714958   86.889    0.000 1785.725    0.000 agent.py:59(modify_board)
              124624788   99.759    0.000 1775.904    0.000 activation.py:713(forward)
               49143418 1755.056    0.000 1755.056    0.000 {built-in method cat}
              124624788   94.959    0.000 1676.144    0.000 functional.py:1364(leaky_relu)
              177053312 1636.225    0.000 1636.225    0.000 {built-in method clone}
                2120108   24.715    0.000 1583.225    0.001 layers.py:849(restart)
              124624788 1562.153    0.000 1562.153    0.000 {built-in method torch._C._nn.leaky_relu}
                3442846   57.449    0.000 1471.394    0.000 agent.py:172(__call__)
             5685470792  990.220    0.000 1429.345    0.000 enum.py:646(__hash__)
                3442846   53.878    0.000 1389.665    0.000 agent.py:112(__call__)
                2120108   13.042    0.000 1352.497    0.001 level.py:8(__init__)
              192799376 1256.926    0.000 1256.926    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                2120108   84.958    0.000 1224.911    0.001 levels.py:277(generate)
             1167579494 1219.897    0.000 1219.897    0.000 layer.py:154(elements)
               14714958 1171.508    0.000 1171.508    0.000 {built-in method torch._C._nn.one_hot}
                4391278  959.907    0.000 1115.321    0.000 agent.py:187(convert_values)
               10328538  202.552    0.000 1114.193    0.000 optimizer.py:189(zero_grad)
              192799376 1114.162    0.000 1114.162    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              352493129  261.147    0.000 1110.939    0.000 {built-in method builtins.any}
               18910163  176.827    0.000 1069.016    0.000 level.py:41(notUsed)
              343553763  700.548    0.000  906.780    0.000 layers.py:62(check)
                3442846  722.746    0.000  884.138    0.000 replaybuffer.py:73(CF_save_data)
             2737316736  699.161    0.000  849.792    0.000 layers.py:809(<genexpr>)
        12038296790/12038296787  715.344    0.000  796.284    0.000 {built-in method builtins.len}
                3442846   65.212    0.000  788.910    0.000 replaybuffer.py:18(stacker)
                3442846   66.623    0.000  761.727    0.000 replaybuffer.py:63(stacker)
               96399688  740.513    0.000  740.513    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               11272112  251.274    0.000  676.515    0.000 exploration.py:53(softmaxer)
             7413866679  651.794    0.000  651.794    0.000 layer.py:99(positions)
               96399688  635.087    0.000  635.087    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               96399688  590.929    0.000  590.929    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               96399688  590.439    0.000  590.439    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              674797900  423.304    0.000  524.900    0.000 tensor.py:906(grad)
               18910163   15.770    0.000  512.478    0.000 level.py:38(elementsIn)
                3442846  286.148    0.000  491.023    0.000 collector.py:46(collect)
                6885692  177.848    0.000  462.735    0.000 random.py:315(sample)
              343553763  299.608    0.000  453.523    0.000 layers.py:48(check)
               96399688  440.115    0.000  440.115    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
             5685510023  439.131    0.000  439.131    0.000 {built-in method builtins.hash}
               10328538   14.338    0.000  418.849    0.000 loss.py:527(forward)
              369364495  293.959    0.000  409.515    0.000 layer.py:134(remove)
               10328538   37.873    0.000  404.510    0.000 functional.py:2898(mse_loss)
              344284700   65.144    0.000  397.476    0.000 {built-in method builtins.all}
              772856139  175.758    0.000  372.546    0.000 layers.py:799(<genexpr>)
              195211116  369.015    0.000  369.015    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              343553763  249.811    0.000  364.012    0.000 layers.py:23(check)
               18910163  166.659    0.000  333.676    0.000 level.py:39(<listcomp>)
               96399681  328.145    0.000  328.145    0.000 layer.py:171(<listcomp>)
               65755240   54.803    0.000  305.303    0.000 flatten.py:39(forward)
              488074977  208.586    0.000  280.268    0.000 layer.py:138(add)
               96399681  277.919    0.000  277.919    0.000 layer.py:172(<listcomp>)
               65755240  250.499    0.000  250.499    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                6885694  250.203    0.000  250.203    0.000 {built-in method nonzero}
               10328538  245.502    0.000  245.502    0.000 {built-in method torch._C._nn.mse_loss}
               10330009  227.860    0.000  227.860    0.000 {built-in method max}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9624183: <Coconuts_Conver4_3counterfactsNOCRASH_2> in cluster <dcc> Done

Job <Coconuts_Conver4_3counterfactsNOCRASH_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun May  9 01:29:17 2021
Job was executed on host(s) <n-62-20-2>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon May 10 01:24:44 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon May 10 01:24:44 2021
Terminated at Tue May 11 01:20:22 2021
Results reported at Tue May 11 01:20:22 2021

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

    CPU time :                                   85898.09 sec.
    Max Memory :                                 9616 MB
    Average Memory :                             6346.76 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               6768.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86139 sec.
    Turnaround time :                            172265 sec.

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

    Name :                      Coconuts_Conver4_3counterfactsNOCRASH-2
    Main :                      CFagent
    Level :                     Levels.Coconuts
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


      331696 function calls (331423 primitive calls) in 8.55 seconds

##    Ordered by: cumulative time
   List reduced from 209 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000    8.549    8.549 {built-in method builtins.exec}
                      1    0.000    0.000    8.549    8.549 <string>:1(<module>)
                      1    0.000    0.000    8.549    8.549 main.py:80(CFagent)
                      3    0.000    0.000    8.443    2.814 agent.py:16(__init__)
                      3    0.000    0.000    8.443    2.814 network.py:37(__init__)
                      1    0.000    0.000    8.426    8.426 agent.py:109(__init__)
                      9    0.000    0.000    8.388    0.932 module.py:573(to)
                  111/9    0.001    0.000    8.388    0.932 module.py:385(_apply)
                     84    0.000    0.000    8.387    0.100 module.py:667(convert)
                     84    8.384    0.100    8.386    0.100 {method 'to' of 'torch._C._TensorBase' objects}
                      1    0.002    0.002    0.098    0.098 game.py:9(__init__)
                      1    0.000    0.000    0.083    0.083 layers.py:793(update)
                    100    0.001    0.000    0.076    0.001 layers.py:849(restart)
                    100    0.000    0.000    0.065    0.001 level.py:8(__init__)
                    100    0.004    0.000    0.061    0.001 levels.py:277(generate)
                      9    0.000    0.000    0.054    0.006 network.py:17(__init__)
                    886    0.009    0.000    0.053    0.000 level.py:41(notUsed)
                     18    0.000    0.000    0.043    0.002 conv.py:370(__init__)
                     18    0.009    0.000    0.043    0.002 conv.py:66(__init__)
                     42    0.000    0.000    0.038    0.001 init.py:347(kaiming_uniform_)
                     84    0.035    0.000    0.035    0.000 {method 'uniform_' of 'torch._C._TensorBase' objects}
                     18    0.000    0.000    0.032    0.002 conv.py:114(reset_parameters)
                    886    0.001    0.000    0.026    0.000 level.py:38(elementsIn)
                    886    0.008    0.000    0.017    0.000 level.py:39(<listcomp>)
                      1    0.000    0.000    0.013    0.013 agent.py:39(__init__)
                  48858    0.008    0.000    0.012    0.000 enum.py:646(__hash__)
                  40874    0.011    0.000    0.011    0.000 level.py:32(inverse)
                    200    0.005    0.000    0.011    0.000 layers.py:36(reset)
                    700    0.001    0.000    0.010    0.000 layer.py:77(restart)
                      1    0.000    0.000    0.009    0.009 agent.py:158(__init__)
                  44477    0.009    0.000    0.009    0.000 enum.py:352(<genexpr>)
                      1    0.000    0.000    0.009    0.009 layers.py:751(__init__)
                      6    0.000    0.000    0.008    0.001 layers.py:782(add)
                    886    0.005    0.000    0.008    0.000 {built-in method _functools.reduce}
                     24    0.000    0.000    0.008    0.000 linear.py:75(__init__)
                      7    0.000    0.000    0.007    0.001 layer.py:61(__init__)
                      7    0.005    0.001    0.007    0.001 layer.py:159(update)
                     24    0.000    0.000    0.006    0.000 linear.py:86(reset_parameters)
                  11300    0.004    0.000    0.006    0.000 layer.py:138(add)
                      2    0.004    0.002    0.004    0.002 {built-in method zeros}
                      1    0.000    0.000    0.004    0.004 game.py:30(<setcomp>)
                     41    0.002    0.000    0.004    0.000 game.py:30(<listcomp>)
                   1698    0.002    0.000    0.004    0.000 module.py:950(__setattr__)
                  48858    0.004    0.000    0.004    0.000 {built-in method builtins.hash}
                    100    0.001    0.000    0.003    0.000 level.py:16(<dictcomp>)
                    114    0.001    0.000    0.003    0.000 module.py:250(__init__)
                  37212    0.003    0.000    0.003    0.000 level.py:39(<lambda>)
                      1    0.000    0.000    0.003    0.003 replaybuffer.py:8(__init__)
                      1    0.003    0.003    0.003    0.003 replaybuffer.py:11(<listcomp>)
                  16974    0.003    0.000    0.003    0.000 layer.py:190(grid)
                    4/1    0.000    0.000    0.002    0.002 __init__.py:144(_lazy_init)
                     84    0.002    0.000    0.002    0.000 init.py:268(_calculate_fan_in_and_fan_out)
                      1    0.002    0.002    0.002    0.002 {built-in method torch._C._cuda_init}
                  27805    0.002    0.000    0.002    0.000 {method 'append' of 'list' objects}
                     42    0.000    0.000    0.002    0.000 init.py:337(_calculate_correct_fan)
                   2275    0.001    0.000    0.001    0.000 types.py:171(__get__)
                  11314    0.001    0.000    0.001    0.000 layer.py:154(elements)
                    686    0.000    0.000    0.001    0.000 random.py:244(randint)
                     33    0.000    0.000    0.001    0.000 activation.py:708(__init__)
                    700    0.001    0.000    0.001    0.000 layer.py:147(clear2)
                    686    0.000    0.000    0.001    0.000 random.py:200(randrange)
                    886    0.001    0.000    0.001    0.000 random.py:250(_randbelow_with_getrandbits)
                     18    0.000    0.000    0.001    0.000 flatten.py:34(__init__)
                      6    0.000    0.000    0.001    0.000 inspect.py:325(getmembers)
                      9    0.000    0.000    0.001    0.000 container.py:62(__init__)
                   4339    0.001    0.000    0.001    0.000 {built-in method builtins.isinstance}
                    100    0.000    0.000    0.001    0.000 {built-in method builtins.all}
                    800    0.000    0.000    0.001    0.000 layers.py:799(<genexpr>)
                    272    0.000    0.000    0.001    0.000 {built-in method builtins.hasattr}
                      3    0.000    0.000    0.001    0.000 learner.py:16(__init__)
                     18    0.000    0.000    0.001    0.000 utils.py:21(_reverse_repeat_tuple)
                     84    0.000    0.000    0.000    0.000 module.py:322(register_parameter)
                   1035    0.000    0.000    0.000    0.000 enum.py:351(__iter__)
                     42    0.000    0.000    0.000    0.000 init.py:112(uniform_)
                    886    0.000    0.000    0.000    0.000 enum.py:354(__len__)
                     42    0.000    0.000    0.000    0.000 init.py:12(_no_grad_uniform_)
                   1799    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
                    345    0.000    0.000    0.000    0.000 module.py:934(__getattr__)
                      3    0.000    0.000    0.000    0.000 adam.py:34(__init__)
                   4917    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
                      3    0.000    0.000    0.000    0.000 optimizer.py:34(__init__)
                   2274    0.000    0.000    0.000    0.000 enum.py:659(name)
                      7    0.000    0.000    0.000    0.000 layer.py:71(<listcomp>)
                     93    0.000    0.000    0.000    0.000 module.py:361(add_module)
                    336    0.000    0.000    0.000    0.000 grad_mode.py:200(__init__)
                    168    0.000    0.000    0.000    0.000 grad_mode.py:119(__enter__)
                    200    0.000    0.000    0.000    0.000 random.py:285(choice)
                    168    0.000    0.000    0.000    0.000 grad_mode.py:123(__exit__)
                     90    0.000    0.000    0.000    0.000 utils.py:9(parse)
                    213    0.000    0.000    0.000    0.000 module.py:1338(children)
                     84    0.000    0.000    0.000    0.000 parameter.py:23(__new__)
                    700    0.000    0.000    0.000    0.000 layer.py:142(clear)
                      1    0.000    0.000    0.000    0.000 agent.py:167(<listcomp>)
                    168    0.000    0.000    0.000    0.000 grad_mode.py:114(__init__)
                     84    0.000    0.000    0.000    0.000 module.py:389(compute_should_use_set_data)
                      1    0.000    0.000    0.000    0.000 layers.py:467(__init__)
                     31    0.000    0.000    0.000    0.000 module.py:1240(parameters)
                      1    0.000    0.000    0.000    0.000 layers.py:73(__init__)
                     84    0.000    0.000    0.000    0.000 {built-in method _make_subclass}
                     31    0.000    0.000    0.000    0.000 module.py:1264(named_parameters)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9632724: <Coconuts_Conver4_3counterfactsNOCRASH_2> in cluster <dcc> Done

Job <Coconuts_Conver4_3counterfactsNOCRASH_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed May 12 14:11:09 2021
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed May 12 15:12:27 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 12 15:12:27 2021
Terminated at Wed May 12 15:12:41 2021
Results reported at Wed May 12 15:12:41 2021

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

    CPU time :                                   5.76 sec.
    Max Memory :                                 2290 MB
    Average Memory :                             1578.67 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14094.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                7
    Run time :                                   15 sec.
    Turnaround time :                            3692 sec.

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

    Name :                      Coconuts_Conver4_3counterfactsNOCRASH-2
    Main :                      CFagent
    Level :                     Levels.Coconuts
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

Traceback (most recent call last):
  File "main.py", line 268, in <module>
    run(Defaults)
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/auxillaries.py", line 133, in run
    (serverRun if isServer else Defaults.main).__call__(getvals(Defaults))
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils/server.py", line 37, in serverRun
    profilingStats()
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils/debug.py", line 59, in profilingStats
    p = Stats('stats')
  File "/appl/python/3.8.4/lib/python3.8/pstats.py", line 96, in __init__
    self.init(arg)
  File "/appl/python/3.8.4/lib/python3.8/pstats.py", line 110, in init
    self.load_stats(arg)
  File "/appl/python/3.8.4/lib/python3.8/pstats.py", line 124, in load_stats
    self.stats = marshal.load(f)
EOFError: EOF read where object expected

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9632767: <Coconuts_Conver4_3counterfactsNOCRASH_2> in cluster <dcc> Exited

Job <Coconuts_Conver4_3counterfactsNOCRASH_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed May 12 14:13:39 2021
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed May 12 15:13:57 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 12 15:13:57 2021
Terminated at Wed May 12 15:14:03 2021
Results reported at Wed May 12 15:14:03 2021

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

Exited with exit code 1.

Resource usage summary:

    CPU time :                                   4.72 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   8 sec.
    Turnaround time :                            3624 sec.

The output (if any) is above this job summary.

