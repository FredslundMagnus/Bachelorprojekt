
# Parameters

    Name :                      Causal3_Conver4_3counterfactsNOCRASH-0
    Main :                      CFagent
    Level :                     Levels.Causal3
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


      57750940200 function calls (57404025165 primitive calls) in 86123.20 seconds

##    Ordered by: cumulative time
   List reduced from 510 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86123.204 86123.204 {built-in method builtins.exec}
                      1    3.883    3.883 86123.204 86123.204 <string>:1(<module>)
                      1  273.743  273.743 86119.321 86119.321 main.py:80(CFagent)
                8152755   29.758    0.000 24510.521    0.003 agent.py:29(learn)
                2717585 2457.721    0.001 22471.892    0.008 agent.py:212(counterfact)
                8152755  606.265    0.000 20545.021    0.003 learner.py:42(Qlearn)
        384881406/37968062 1551.257    0.000 13814.499    0.000 module.py:866(_call_impl)
                2717585   12.598    0.000 13401.115    0.005 game.py:42(step)
               29815307   84.380    0.000 13099.185    0.000 network.py:28(forward)
               29815307  406.427    0.000 12829.231    0.000 container.py:117(forward)
                2717585   16.839    0.000 12789.017    0.005 layers.py:827(step)
                2717585  261.276    0.000 9437.069    0.003 agent.py:54(_learn)
                2717585  259.365    0.000 8752.569    0.003 agent.py:204(_learn)
                8152755   70.259    0.000 8702.094    0.001 optimizer.py:84(wrapper)
               93580475 8670.460    0.000 8670.460    0.000 {built-in method tensor}
               87267230   53.623    0.000 8521.726    0.000 game.py:38(board)
                8152755   33.446    0.000 8370.435    0.001 grad_mode.py:24(decorate_context)
                8152755  237.187    0.000 8256.673    0.001 adam.py:55(step)
                5397001  111.864    0.000 8222.810    0.002 agent.py:176(choose_action)
                2717585  225.613    0.000 7800.632    0.003 layers.py:17(step)
                8152755 1675.599    0.000 7753.924    0.001 _functional.py:53(adam)
               10830381  253.255    0.000 7627.467    0.001 agent.py:49(__call__)
              271331627  426.431    0.000 7552.533    0.000 layer.py:106(move)
                2717585   74.358    0.000 6274.275    0.002 agent.py:117(_learn)
                2717585 3099.351    0.001 5769.632    0.002 replaybuffer.py:28(teleporter_save_data)
                8152755   42.903    0.000 5242.707    0.001 tensor.py:195(backward)
                8152755   32.031    0.000 5198.498    0.001 __init__.py:68(backward)
                8152755 4983.923    0.001 4983.923    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2717586  384.377    0.000 4950.253    0.002 layers.py:793(update)
                2717585 2897.310    0.001 4817.080    0.002 agent.py:88(interveen)
               59630614  126.972    0.000 4561.118    0.000 conv.py:398(forward)
                2717585 3619.169    0.001 4475.401    0.002 replaybuffer.py:22(sample_data)
               86962712 2360.236    0.000 4417.051    0.000 layer.py:175(NoRock_update)
              271331627  927.900    0.000 4395.584    0.000 layers.py:844(check)
               59630614   78.384    0.000 4378.277    0.000 conv.py:390(_conv_forward)
                2717585 3513.003    0.001 4352.742    0.002 replaybuffer.py:67(sample_data)
               59630614 4299.893    0.000 4299.893    0.000 {built-in method conv2d}
               84010751  166.550    0.000 3738.887    0.000 linear.py:93(forward)
               84010751   65.698    0.000 3495.540    0.000 functional.py:1737(linear)
               84010751 3412.425    0.000 3412.425    0.000 {built-in method torch._C._nn.linear}
              195074985 2473.028    0.000 2473.028    0.000 {built-in method clone}
                2717585 1594.722    0.001 2379.960    0.001 agent.py:67(modify)
              271331627  414.813    0.000 2329.208    0.000 layers.py:838(isFree)
              113826058   87.829    0.000 2069.021    0.000 activation.py:713(forward)
              113826058   89.715    0.000 1981.192    0.000 functional.py:1364(leaky_relu)
               13547966   89.487    0.000 1930.490    0.000 agent.py:59(modify_board)
             1908575128 1594.777    0.000 1914.395    0.000 layer.py:103(isFree)
              113826058 1871.289    0.000 1871.289    0.000 {built-in method torch._C._nn.leaky_relu}
                5397001 1476.142    0.000 1726.544    0.000 agent.py:187(convert_values)
               40723816 1611.982    0.000 1611.982    0.000 {built-in method cat}
              152184760 1586.102    0.000 1586.102    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              152184760 1391.900    0.000 1391.900    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                2717585 1047.046    0.000 1388.449    0.001 replaybuffer.py:73(CF_save_data)
                2717585   44.247    0.000 1347.582    0.000 agent.py:172(__call__)
                2717585   42.621    0.000 1275.410    0.000 agent.py:112(__call__)
               13547966 1230.849    0.000 1230.849    0.000 {built-in method torch._C._nn.one_hot}
                3737748   37.364    0.000 1229.692    0.000 layers.py:849(restart)
                8152755  193.285    0.000 1206.506    0.000 optimizer.py:189(zero_grad)
             1064631020 1092.731    0.000 1092.731    0.000 layer.py:154(elements)
             4123069314  733.016    0.000 1046.428    0.000 enum.py:646(__hash__)
              271758600  158.178    0.000 1007.628    0.000 {built-in method builtins.all}
              276173606  227.198    0.000  957.199    0.000 {built-in method builtins.any}
              271331627  573.218    0.000  918.329    0.000 layers.py:246(check)
                3737748   18.958    0.000  898.150    0.000 level.py:8(__init__)
               76092380  895.034    0.000  895.034    0.000 {method 'add' of 'torch._C._TensorBase' objects}
             1885321634  480.574    0.000  881.439    0.000 layers.py:799(<genexpr>)
              271331627  500.427    0.000  836.917    0.000 layers.py:286(check)
               10830381  288.975    0.000  796.579    0.000 exploration.py:53(softmaxer)
        10960641081/10960641078  668.166    0.000  745.384    0.000 {built-in method builtins.len}
               76092380  741.745    0.000  741.745    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
             2412187668  602.625    0.000  730.002    0.000 layers.py:809(<genexpr>)
               76092380  721.453    0.000  721.453    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               76092380  719.955    0.000  719.955    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                3737748   77.203    0.000  690.919    0.000 levels.py:164(generate)
                2717585   53.649    0.000  666.797    0.000 replaybuffer.py:18(stacker)
                2717585   52.572    0.000  654.098    0.000 replaybuffer.py:63(stacker)
              211340536  625.176    0.000  625.176    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                2717585  337.435    0.000  560.802    0.000 collector.py:46(collect)
               76092380  557.591    0.000  557.591    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                7475496   70.687    0.000  512.835    0.000 level.py:41(notUsed)
              271331627  289.209    0.000  455.830    0.000 layers.py:313(check)
             5097134949  441.862    0.000  441.862    0.000 layer.py:99(positions)
              532646744  355.524    0.000  440.876    0.000 tensor.py:906(grad)
               12910666  164.693    0.000  435.419    0.000 random.py:315(sample)
              271331627  265.372    0.000  415.745    0.000 layers.py:273(check)
                8152755   11.597    0.000  397.931    0.000 loss.py:527(forward)
                8152755   30.440    0.000  386.334    0.000 functional.py:2898(mse_loss)
              271331627  234.755    0.000  353.897    0.000 layers.py:48(check)
               59630614   41.339    0.000  346.466    0.000 flatten.py:39(forward)
             4123100369  313.417    0.000  313.417    0.000 {built-in method builtins.hash}
               59630614  305.127    0.000  305.127    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               86962712  302.194    0.000  302.194    0.000 layer.py:186(<listcomp>)
               22546397  296.131    0.000  296.131    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               29901984   35.713    0.000  284.264    0.000 layer.py:77(restart)
              271331627  186.784    0.000  274.283    0.000 layers.py:23(check)
              395715743  271.252    0.000  271.252    0.000 {built-in method torch._C._get_tracing_state}
               10830381  260.066    0.000  260.066    0.000 {built-in method multinomial}
                8152755  253.846    0.000  253.846    0.000 {built-in method torch._C._nn.mse_loss}
               86962712  253.369    0.000  253.369    0.000 layer.py:187(<listcomp>)
               13549756   21.339    0.000  242.959    0.000 tensor.py:525(__rsub__)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9624187: <Causal3_Conver4_3counterfactsNOCRASH_0> in cluster <dcc> Done

Job <Causal3_Conver4_3counterfactsNOCRASH_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun May  9 01:29:17 2021
Job was executed on host(s) <n-62-20-7>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Tue May 11 02:45:03 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue May 11 02:45:03 2021
Terminated at Wed May 12 02:40:38 2021
Results reported at Wed May 12 02:40:38 2021

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

    CPU time :                                   86088.32 sec.
    Max Memory :                                 3438 MB
    Average Memory :                             3404.50 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               12946.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86137 sec.
    Turnaround time :                            263481 sec.

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

    Name :                      Causal3_Conver4_3counterfactsNOCRASH-0
    Main :                      CFagent
    Level :                     Levels.Causal3
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


      158906 function calls (158617 primitive calls) in 5.45 seconds

##    Ordered by: cumulative time
   List reduced from 207 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000    5.448    5.448 {built-in method builtins.exec}
                      1    0.000    0.000    5.448    5.448 <string>:1(<module>)
                      1    0.000    0.000    5.448    5.448 main.py:80(CFagent)
                      3    0.000    0.000    5.394    1.798 agent.py:16(__init__)
                      3    0.000    0.000    5.393    1.798 network.py:37(__init__)
                      1    0.000    0.000    5.376    5.376 agent.py:109(__init__)
                      9    0.000    0.000    5.353    0.595 module.py:573(to)
                  111/9    0.001    0.000    5.353    0.595 module.py:385(_apply)
                     84    0.000    0.000    5.351    0.064 module.py:667(convert)
                     84    5.349    0.064    5.351    0.064 {method 'to' of 'torch._C._TensorBase' objects}
                      1    0.002    0.002    0.050    0.050 game.py:9(__init__)
                      9    0.000    0.000    0.040    0.004 network.py:17(__init__)
                      1    0.000    0.000    0.037    0.037 layers.py:793(update)
                    100    0.001    0.000    0.033    0.000 layers.py:849(restart)
                     42    0.000    0.000    0.030    0.001 init.py:347(kaiming_uniform_)
                     18    0.000    0.000    0.029    0.002 conv.py:370(__init__)
                     18    0.002    0.000    0.029    0.002 conv.py:66(__init__)
                     84    0.028    0.000    0.028    0.000 {method 'uniform_' of 'torch._C._TensorBase' objects}
                     18    0.000    0.000    0.025    0.001 conv.py:114(reset_parameters)
                    100    0.000    0.000    0.023    0.000 level.py:8(__init__)
                    100    0.002    0.000    0.019    0.000 levels.py:164(generate)
                    200    0.002    0.000    0.015    0.000 level.py:41(notUsed)
                    200    0.006    0.000    0.011    0.000 layers.py:36(reset)
                      1    0.000    0.000    0.009    0.009 agent.py:158(__init__)
                      1    0.000    0.000    0.009    0.009 layers.py:751(__init__)
                      7    0.000    0.000    0.009    0.001 layers.py:782(add)
                      1    0.000    0.000    0.009    0.009 agent.py:39(__init__)
                    800    0.001    0.000    0.008    0.000 layer.py:77(restart)
                      8    0.001    0.000    0.008    0.001 layer.py:61(__init__)
                     24    0.000    0.000    0.008    0.000 linear.py:75(__init__)
                    200    0.000    0.000    0.006    0.000 level.py:38(elementsIn)
                     24    0.000    0.000    0.006    0.000 linear.py:86(reset_parameters)
                   6539    0.005    0.000    0.005    0.000 level.py:32(inverse)
                   8357    0.003    0.000    0.004    0.000 layer.py:138(add)
                  17218    0.003    0.000    0.004    0.000 enum.py:646(__hash__)
                    200    0.002    0.000    0.004    0.000 level.py:39(<listcomp>)
                   1698    0.002    0.000    0.004    0.000 module.py:950(__setattr__)
                    100    0.001    0.000    0.003    0.000 level.py:16(<dictcomp>)
                      8    0.002    0.000    0.003    0.000 layer.py:175(NoRock_update)
                    114    0.001    0.000    0.003    0.000 module.py:250(__init__)
                      1    0.000    0.000    0.003    0.003 replaybuffer.py:8(__init__)
                      1    0.003    0.003    0.003    0.003 replaybuffer.py:11(<listcomp>)
                  15022    0.003    0.000    0.003    0.000 enum.py:352(<genexpr>)
                  17056    0.003    0.000    0.003    0.000 layer.py:190(grid)
                      1    0.000    0.000    0.002    0.002 game.py:30(<setcomp>)
                     41    0.001    0.000    0.002    0.000 game.py:30(<listcomp>)
                    200    0.001    0.000    0.002    0.000 {built-in method _functools.reduce}
                     84    0.002    0.000    0.002    0.000 init.py:268(_calculate_fan_in_and_fan_out)
                    200    0.001    0.000    0.002    0.000 random.py:315(sample)
                     42    0.000    0.000    0.002    0.000 init.py:337(_calculate_correct_fan)
                    4/1    0.000    0.000    0.002    0.002 __init__.py:144(_lazy_init)
                  17218    0.001    0.000    0.001    0.000 {built-in method builtins.hash}
                      1    0.001    0.001    0.001    0.001 {built-in method torch._C._cuda_init}
                  19026    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
                     33    0.000    0.000    0.001    0.000 activation.py:708(__init__)
                    800    0.001    0.000    0.001    0.000 layer.py:147(clear2)
                   4805    0.001    0.000    0.001    0.000 {built-in method builtins.isinstance}
                   2360    0.001    0.000    0.001    0.000 types.py:171(__get__)
                   8373    0.001    0.000    0.001    0.000 layer.py:154(elements)
                   8400    0.001    0.000    0.001    0.000 level.py:39(<lambda>)
                    213    0.000    0.000    0.001    0.000 module.py:1338(children)
                      7    0.000    0.000    0.001    0.000 inspect.py:325(getmembers)
                    851    0.001    0.000    0.001    0.000 random.py:250(_randbelow_with_getrandbits)
                    213    0.001    0.000    0.001    0.000 module.py:1347(named_children)
                    100    0.000    0.000    0.001    0.000 {built-in method builtins.all}
                      9    0.000    0.000    0.001    0.000 container.py:62(__init__)
                      3    0.000    0.000    0.001    0.000 learner.py:16(__init__)
                     18    0.000    0.000    0.001    0.000 flatten.py:34(__init__)
                    900    0.000    0.000    0.001    0.000 layers.py:799(<genexpr>)
                    272    0.000    0.000    0.001    0.000 {built-in method builtins.hasattr}
                     84    0.000    0.000    0.000    0.000 module.py:322(register_parameter)
                      3    0.000    0.000    0.000    0.000 adam.py:34(__init__)
                    345    0.000    0.000    0.000    0.000 module.py:934(__getattr__)
                     42    0.000    0.000    0.000    0.000 init.py:112(uniform_)
                   4917    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
                      3    0.000    0.000    0.000    0.000 optimizer.py:34(__init__)
                    490    0.000    0.000    0.000    0.000 abc.py:96(__instancecheck__)
                     42    0.000    0.000    0.000    0.000 init.py:12(_no_grad_uniform_)
                      8    0.000    0.000    0.000    0.000 layer.py:71(<listcomp>)
                     93    0.000    0.000    0.000    0.000 module.py:361(add_module)
                    336    0.000    0.000    0.000    0.000 grad_mode.py:200(__init__)
                    168    0.000    0.000    0.000    0.000 grad_mode.py:119(__enter__)
                      1    0.000    0.000    0.000    0.000 layers.py:266(__init__)
                    168    0.000    0.000    0.000    0.000 grad_mode.py:123(__exit__)
                    800    0.000    0.000    0.000    0.000 layer.py:142(clear)
                     90    0.000    0.000    0.000    0.000 utils.py:9(parse)
                      1    0.000    0.000    0.000    0.000 agent.py:167(<listcomp>)
                    490    0.000    0.000    0.000    0.000 {built-in method _abc._abc_instancecheck}
                     84    0.000    0.000    0.000    0.000 parameter.py:23(__new__)
                      1    0.000    0.000    0.000    0.000 layers.py:306(__init__)
                   2359    0.000    0.000    0.000    0.000 enum.py:659(name)
                    168    0.000    0.000    0.000    0.000 grad_mode.py:114(__init__)
                     31    0.000    0.000    0.000    0.000 module.py:1240(parameters)
                   1799    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
                     31    0.000    0.000    0.000    0.000 module.py:1264(named_parameters)
                     84    0.000    0.000    0.000    0.000 module.py:389(compute_should_use_set_data)
                     84    0.000    0.000    0.000    0.000 {built-in method _make_subclass}
                     31    0.000    0.000    0.000    0.000 module.py:1227(_named_members)
                   1422    0.000    0.000    0.000    0.000 {method 'add' of 'set' objects}
                      2    0.000    0.000    0.000    0.000 {built-in method zeros}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9632728: <Causal3_Conver4_3counterfactsNOCRASH_0> in cluster <dcc> Done

Job <Causal3_Conver4_3counterfactsNOCRASH_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed May 12 14:11:09 2021
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed May 12 15:12:59 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 12 15:12:59 2021
Terminated at Wed May 12 15:13:12 2021
Results reported at Wed May 12 15:13:12 2021

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

    CPU time :                                   5.09 sec.
    Max Memory :                                 4 MB
    Average Memory :                             4.00 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               16380.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                5
    Run time :                                   15 sec.
    Turnaround time :                            3723 sec.

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

    Name :                      Causal3_Conver4_3counterfactsNOCRASH-0
    Main :                      CFagent
    Level :                     Levels.Causal3
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


Traceback (most recent call last):
  File "main.py", line 268, in <module>
    run(Defaults)
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/auxillaries.py", line 133, in run
    (serverRun if isServer else Defaults.main).__call__(getvals(Defaults))
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils/server.py", line 37, in serverRun
    profilingStats()
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils/debug.py", line 62, in profilingStats
    os.remove('stats')
FileNotFoundError: [Errno 2] No such file or directory: 'stats'

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9632771: <Causal3_Conver4_3counterfactsNOCRASH_0> in cluster <dcc> Exited

Job <Causal3_Conver4_3counterfactsNOCRASH_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed May 12 14:13:39 2021
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed May 12 15:14:26 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 12 15:14:26 2021
Terminated at Wed May 12 15:14:32 2021
Results reported at Wed May 12 15:14:32 2021

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

    CPU time :                                   4.65 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   8 sec.
    Turnaround time :                            3653 sec.

The output (if any) is above this job summary.

