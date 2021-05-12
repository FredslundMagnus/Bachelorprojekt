
# Parameters

    Name :                      Maze_Conver4_3counterfactsNOCRASH-1
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
    Num :                       1
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      66473539615 function calls (66075939232 primitive calls) in 86072.52 seconds

##    Ordered by: cumulative time
   List reduced from 518 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86114.276 86114.276 {built-in method builtins.exec}
                      1    4.212    4.212 86114.276 86114.276 <string>:1(<module>)
                      1  340.644  340.644 86110.065 86110.065 main.py:80(CFagent)
               10209165   38.383    0.000 24502.025    0.002 agent.py:29(learn)
                3403055 1806.037    0.001 22158.307    0.007 agent.py:212(counterfact)
               10209164  613.548    0.000 20000.201    0.002 learner.py:42(Qlearn)
                3403055   13.397    0.000 15942.134    0.005 game.py:42(step)
                3403055   18.504    0.000 15240.111    0.004 layers.py:827(step)
        442075432/44476740 1707.542    0.000 13929.083    0.000 module.py:866(_call_impl)
               34267576   96.469    0.000 13136.772    0.000 network.py:28(forward)
               34267576  426.828    0.000 12816.071    0.000 container.py:117(forward)
              109914081 9617.529    0.000 9617.529    0.000 {built-in method tensor}
                3403055  335.988    0.000 9505.427    0.003 agent.py:54(_learn)
              102088658   53.349    0.000 9457.971    0.000 game.py:38(board)
                3403055  333.497    0.000 8737.792    0.003 agent.py:204(_learn)
                3403055  296.734    0.000 8476.260    0.002 layers.py:17(step)
              339573244  553.278    0.000 8148.874    0.000 layer.py:106(move)
               10209164   83.261    0.000 7986.272    0.001 optimizer.py:84(wrapper)
               10209164   41.797    0.000 7605.192    0.001 grad_mode.py:24(decorate_context)
               12025402  295.265    0.000 7468.776    0.001 agent.py:49(__call__)
               10209164  294.491    0.000 7468.666    0.001 adam.py:55(step)
                5226901   97.878    0.000 6851.690    0.001 agent.py:176(choose_action)
               10209164 1549.578    0.000 6837.344    0.001 _functional.py:53(adam)
                3403056  492.200    0.000 6720.847    0.002 layers.py:793(update)
                3403055  102.840    0.000 6198.930    0.002 agent.py:117(_learn)
              108897752 3041.847    0.000 5658.945    0.000 layer.py:175(NoRock_update)
                3403055 4179.342    0.001 5178.955    0.002 replaybuffer.py:22(sample_data)
               10209164   40.276    0.000 5072.231    0.000 tensor.py:195(backward)
               10209164   38.241    0.000 5030.473    0.000 __init__.py:68(backward)
                3403055 4062.389    0.001 5028.564    0.001 replaybuffer.py:67(sample_data)
               10209164 4795.332    0.000 4795.332    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
              339573244 1207.187    0.000 4772.106    0.000 layers.py:844(check)
               68535152  151.036    0.000 4731.853    0.000 conv.py:398(forward)
               68535152   82.261    0.000 4515.956    0.000 conv.py:390(_conv_forward)
               68535152 4433.695    0.000 4433.695    0.000 {built-in method conv2d}
                3403055 1667.389    0.000 3783.126    0.001 agent.py:88(interveen)
               95996618  187.712    0.000 3621.206    0.000 linear.py:93(forward)
               95996618   75.246    0.000 3343.584    0.000 functional.py:1737(linear)
                3403055 1840.648    0.001 3309.842    0.001 replaybuffer.py:28(teleporter_save_data)
               95996618 3248.361    0.000 3248.361    0.000 {built-in method torch._C._nn.linear}
                3403055 1585.023    0.000 2410.251    0.001 agent.py:67(modify)
              339573244  472.143    0.000 2370.346    0.000 layers.py:838(isFree)
                2794183   38.679    0.000 2198.180    0.001 layers.py:849(restart)
               15428457   99.128    0.000 1934.489    0.000 agent.py:59(modify_board)
              130264194  105.714    0.000 1934.302    0.000 activation.py:713(forward)
                2794183   23.236    0.000 1911.898    0.001 level.py:8(__init__)
             2102486363 1606.890    0.000 1898.203    0.000 layer.py:103(isFree)
              130264194  108.941    0.000 1828.588    0.000 functional.py:1364(leaky_relu)
               49459002 1747.220    0.000 1747.220    0.000 {built-in method cat}
                3811016  234.113    0.000 1706.432    0.000 levels.py:9(generate)
              130264194 1699.089    0.000 1699.089    0.000 {built-in method torch._C._nn.leaky_relu}
                3403054   54.854    0.000 1484.343    0.000 agent.py:172(__call__)
              142784820 1429.188    0.000 1429.188    0.000 {built-in method clone}
                3403055   50.893    0.000 1398.746    0.000 agent.py:112(__call__)
             1289367714 1381.184    0.000 1381.184    0.000 layer.py:154(elements)
              339573244  831.940    0.000 1371.362    0.000 layers.py:168(check)
              190571060 1348.294    0.000 1348.294    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                5226901 1150.041    0.000 1340.755    0.000 agent.py:187(convert_values)
              347720581  304.775    0.000 1289.711    0.000 {built-in method builtins.any}
               15428457 1259.565    0.000 1259.565    0.000 {built-in method torch._C._nn.one_hot}
              190571060 1199.567    0.000 1199.567    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               10209164  204.401    0.000 1159.533    0.000 optimizer.py:189(zero_grad)
                3403055  829.570    0.000 1043.397    0.000 replaybuffer.py:73(CF_save_data)
              340305600  178.547    0.000  995.154    0.000 {built-in method builtins.all}
             3037602753  813.460    0.000  984.936    0.000 layers.py:809(<genexpr>)
             3591492707  657.606    0.000  950.603    0.000 enum.py:646(__hash__)
        13411095669/13411095666  825.320    0.000  910.610    0.000 {built-in method builtins.len}
             1862108572  482.129    0.000  857.290    0.000 layers.py:799(<genexpr>)
               95285530  784.778    0.000  784.778    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                3403055   54.817    0.000  754.883    0.000 replaybuffer.py:18(stacker)
               12025402  278.447    0.000  740.126    0.000 exploration.py:53(softmaxer)
                3403054   52.596    0.000  728.435    0.000 replaybuffer.py:63(stacker)
               95285530  673.626    0.000  673.626    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               95285530  629.294    0.000  629.294    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               95285530  628.412    0.000  628.412    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                8382549   74.483    0.000  628.110    0.000 level.py:41(notUsed)
              339573244  378.065    0.000  592.011    0.000 layers.py:141(check)
               17222325  209.474    0.000  545.955    0.000 random.py:315(sample)
              666998794  428.099    0.000  531.876    0.000 tensor.py:906(grad)
                3403055  303.938    0.000  514.361    0.000 collector.py:46(collect)
                3811016  268.556    0.000  504.534    0.000 levels.py:75(RFS)
              339573244  340.189    0.000  501.792    0.000 layers.py:48(check)
             5478758881  495.760    0.000  495.760    0.000 layer.py:99(positions)
               95285530  470.209    0.000  470.209    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              339573244  295.944    0.000  448.374    0.000 layers.py:124(check)
               10209164   14.488    0.000  427.566    0.000 loss.py:527(forward)
               10209164   40.192    0.000  413.078    0.000 functional.py:2898(mse_loss)
              108897752  377.310    0.000  377.310    0.000 layer.py:186(<listcomp>)
              339573244  238.778    0.000  354.931    0.000 layers.py:23(check)
              380150454  262.089    0.000  352.681    0.000 layer.py:134(remove)
              161616331  333.631    0.000  333.631    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              108897752  327.230    0.000  327.230    0.000 layer.py:187(<listcomp>)
               68535152   46.496    0.000  317.113    0.000 flatten.py:39(forward)
              536719332  213.988    0.000  298.553    0.000 layer.py:138(add)
             3591531490  293.003    0.000  293.003    0.000 {built-in method builtins.hash}
              436924212  194.358    0.000  285.902    0.000 random.py:250(_randbelow_with_getrandbits)
               68535152  270.618    0.000  270.618    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                8382549    8.605    0.000  256.311    0.000 level.py:38(elementsIn)
              279178846  254.184    0.000  254.184    0.000 level.py:32(inverse)
               10209164  253.780    0.000  253.780    0.000 {built-in method torch._C._nn.mse_loss}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9624179: <Maze_Conver4_3counterfactsNOCRASH_1> in cluster <dcc> Done

Job <Maze_Conver4_3counterfactsNOCRASH_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun May  9 01:29:16 2021
Job was executed on host(s) <n-62-11-14>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun May  9 01:29:17 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun May  9 01:29:17 2021
Terminated at Mon May 10 01:24:37 2021
Results reported at Mon May 10 01:24:37 2021

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

    CPU time :                                   85892.28 sec.
    Max Memory :                                 9725 MB
    Average Memory :                             6502.05 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               6659.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86120 sec.
    Turnaround time :                            86121 sec.

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

    Name :                      Maze_Conver4_3counterfactsNOCRASH-1
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
    Num :                       1
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              0 minutes.
    Hours used :                0 hours.

# Profiling


      254084 function calls (253795 primitive calls) in 8.62 seconds

##    Ordered by: cumulative time
   List reduced from 220 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000    8.624    8.624 {built-in method builtins.exec}
                      1    0.000    0.000    8.624    8.624 <string>:1(<module>)
                      1    0.000    0.000    8.624    8.624 main.py:80(CFagent)
                      3    0.000    0.000    8.512    2.837 agent.py:16(__init__)
                      3    0.000    0.000    8.512    2.837 network.py:37(__init__)
                      1    0.000    0.000    8.495    8.495 agent.py:109(__init__)
                      9    0.000    0.000    8.460    0.940 module.py:573(to)
                  111/9    0.001    0.000    8.459    0.940 module.py:385(_apply)
                     84    0.000    0.000    8.457    0.101 module.py:667(convert)
                     84    8.455    0.101    8.457    0.101 {method 'to' of 'torch._C._TensorBase' objects}
                      1    0.002    0.002    0.104    0.104 game.py:9(__init__)
                      1    0.000    0.000    0.086    0.086 layers.py:793(update)
                    100    0.001    0.000    0.081    0.001 layers.py:849(restart)
                    100    0.001    0.000    0.070    0.001 level.py:8(__init__)
                    141    0.009    0.000    0.064    0.000 levels.py:9(generate)
                      9    0.000    0.000    0.052    0.006 network.py:17(__init__)
                     18    0.000    0.000    0.042    0.002 conv.py:370(__init__)
                     18    0.009    0.000    0.041    0.002 conv.py:66(__init__)
                     42    0.000    0.000    0.036    0.001 init.py:347(kaiming_uniform_)
                     84    0.033    0.000    0.033    0.000 {method 'uniform_' of 'torch._C._TensorBase' objects}
                     18    0.000    0.000    0.031    0.002 conv.py:114(reset_parameters)
                    300    0.003    0.000    0.023    0.000 level.py:41(notUsed)
                    141    0.010    0.000    0.019    0.000 levels.py:75(RFS)
                      1    0.000    0.000    0.013    0.013 agent.py:39(__init__)
                    200    0.006    0.000    0.013    0.000 layers.py:36(reset)
                      1    0.000    0.000    0.011    0.011 layers.py:751(__init__)
                      7    0.000    0.000    0.011    0.002 layers.py:782(add)
                    300    0.000    0.000    0.010    0.000 level.py:38(elementsIn)
                      8    0.001    0.000    0.010    0.001 layer.py:61(__init__)
                  10079    0.009    0.000    0.009    0.000 level.py:32(inverse)
                    800    0.001    0.000    0.009    0.000 layer.py:77(restart)
                      1    0.000    0.000    0.009    0.009 agent.py:158(__init__)
                     24    0.000    0.000    0.007    0.000 linear.py:75(__init__)
                  25836    0.005    0.000    0.007    0.000 enum.py:646(__hash__)
                    300    0.003    0.000    0.006    0.000 level.py:39(<listcomp>)
                     24    0.000    0.000    0.006    0.000 linear.py:86(reset_parameters)
                   9200    0.004    0.000    0.005    0.000 layer.py:138(add)
                    141    0.002    0.000    0.005    0.000 level.py:16(<dictcomp>)
                  21085    0.005    0.000    0.005    0.000 enum.py:352(<genexpr>)
                   8460    0.003    0.000    0.005    0.000 levels.py:31(<genexpr>)
                      1    0.000    0.000    0.004    0.004 game.py:30(<setcomp>)
                     41    0.002    0.000    0.004    0.000 game.py:30(<listcomp>)
                      2    0.004    0.002    0.004    0.002 {built-in method zeros}
                   1698    0.003    0.000    0.004    0.000 module.py:950(__setattr__)
                      8    0.003    0.000    0.004    0.000 layer.py:175(NoRock_update)
                    114    0.001    0.000    0.004    0.000 module.py:250(__init__)
                   2456    0.001    0.000    0.003    0.000 random.py:285(choice)
                    300    0.002    0.000    0.003    0.000 {built-in method _functools.reduce}
                  17056    0.003    0.000    0.003    0.000 layer.py:190(grid)
                      1    0.000    0.000    0.003    0.003 replaybuffer.py:8(__init__)
                      1    0.003    0.003    0.003    0.003 replaybuffer.py:11(<listcomp>)
                   3352    0.002    0.000    0.003    0.000 random.py:250(_randbelow_with_getrandbits)
                    382    0.001    0.000    0.003    0.000 random.py:315(sample)
                  25836    0.002    0.000    0.002    0.000 {built-in method builtins.hash}
                     84    0.002    0.000    0.002    0.000 init.py:268(_calculate_fan_in_and_fan_out)
                  24631    0.002    0.000    0.002    0.000 {method 'append' of 'list' objects}
                     42    0.000    0.000    0.002    0.000 init.py:337(_calculate_correct_fan)
                   2360    0.001    0.000    0.002    0.000 types.py:171(__get__)
                    4/1    0.000    0.000    0.002    0.002 __init__.py:144(_lazy_init)
                   2115    0.002    0.000    0.002    0.000 {method 'intersection_update' of 'set' objects}
                   2115    0.002    0.000    0.002    0.000 levels.py:85(<listcomp>)
                      1    0.001    0.001    0.001    0.001 {built-in method torch._C._cuda_init}
                  11497    0.001    0.000    0.001    0.000 {method 'add' of 'set' objects}
                   6374    0.001    0.000    0.001    0.000 {built-in method builtins.min}
                   5169    0.001    0.000    0.001    0.000 {built-in method builtins.isinstance}
                  12600    0.001    0.000    0.001    0.000 level.py:39(<lambda>)
                    800    0.001    0.000    0.001    0.000 layer.py:147(clear2)
                     33    0.000    0.000    0.001    0.000 activation.py:708(__init__)
                   6374    0.001    0.000    0.001    0.000 {built-in method builtins.max}
                      7    0.000    0.000    0.001    0.000 inspect.py:325(getmembers)
                   9216    0.001    0.000    0.001    0.000 layer.py:154(elements)
                    100    0.000    0.000    0.001    0.000 {built-in method builtins.all}
                    213    0.001    0.000    0.001    0.000 module.py:1338(children)
                    900    0.000    0.000    0.001    0.000 layers.py:799(<genexpr>)
                      9    0.000    0.000    0.001    0.000 container.py:62(__init__)
                      3    0.000    0.000    0.001    0.000 learner.py:16(__init__)
                     18    0.000    0.000    0.001    0.000 flatten.py:34(__init__)
                    272    0.000    0.000    0.001    0.000 {built-in method builtins.hasattr}
                    854    0.000    0.000    0.001    0.000 abc.py:96(__instancecheck__)
                     84    0.000    0.000    0.001    0.000 module.py:322(register_parameter)
                      8    0.000    0.000    0.001    0.000 layer.py:71(<listcomp>)
                   5435    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
                   4512    0.000    0.000    0.000    0.000 {method 'remove' of 'set' objects}
                   1799    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
                      3    0.000    0.000    0.000    0.000 adam.py:34(__init__)
                   2359    0.000    0.000    0.000    0.000 enum.py:659(name)
                      3    0.000    0.000    0.000    0.000 optimizer.py:34(__init__)
                     42    0.000    0.000    0.000    0.000 init.py:112(uniform_)
                    345    0.000    0.000    0.000    0.000 module.py:934(__getattr__)
                    800    0.000    0.000    0.000    0.000 layer.py:142(clear)
                     42    0.000    0.000    0.000    0.000 init.py:12(_no_grad_uniform_)
                   4917    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
                    854    0.000    0.000    0.000    0.000 {built-in method _abc._abc_instancecheck}
                    168    0.000    0.000    0.000    0.000 grad_mode.py:119(__enter__)
                    336    0.000    0.000    0.000    0.000 grad_mode.py:200(__init__)
                     93    0.000    0.000    0.000    0.000 module.py:361(add_module)
              3672/3669    0.000    0.000    0.000    0.000 {built-in method builtins.len}
                    168    0.000    0.000    0.000    0.000 grad_mode.py:123(__exit__)
                     90    0.000    0.000    0.000    0.000 utils.py:9(parse)
                   3352    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9632720: <Maze_Conver4_3counterfactsNOCRASH_1> in cluster <dcc> Done

Job <Maze_Conver4_3counterfactsNOCRASH_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed May 12 14:11:08 2021
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed May 12 15:11:39 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 12 15:11:39 2021
Terminated at Wed May 12 15:11:53 2021
Results reported at Wed May 12 15:11:53 2021

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

    CPU time :                                   5.87 sec.
    Max Memory :                                 2001 MB
    Average Memory :                             2001.00 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14383.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                7
    Run time :                                   15 sec.
    Turnaround time :                            3645 sec.

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

    Name :                      Maze_Conver4_3counterfactsNOCRASH-1
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
    Num :                       1
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              0 minutes.
    Hours used :                0 hours.

# Profiling


      245807 function calls (245518 primitive calls) in 4.53 seconds

##    Ordered by: cumulative time
   List reduced from 220 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000    4.530    4.530 {built-in method builtins.exec}
                      1    0.000    0.000    4.529    4.529 <string>:1(<module>)
                      1    0.000    0.000    4.529    4.529 main.py:80(CFagent)
                      3    0.000    0.000    4.431    1.477 agent.py:16(__init__)
                      3    0.000    0.000    4.430    1.477 network.py:37(__init__)
                      1    0.000    0.000    4.413    4.413 agent.py:109(__init__)
                      9    0.000    0.000    4.402    0.489 module.py:573(to)
                  111/9    0.001    0.000    4.402    0.489 module.py:385(_apply)
                     84    0.000    0.000    4.399    0.052 module.py:667(convert)
                     84    4.397    0.052    4.399    0.052 {method 'to' of 'torch._C._TensorBase' objects}
                      1    0.002    0.002    0.094    0.094 game.py:9(__init__)
                      1    0.000    0.000    0.080    0.080 layers.py:793(update)
                    100    0.001    0.000    0.075    0.001 layers.py:849(restart)
                    100    0.001    0.000    0.064    0.001 level.py:8(__init__)
                    129    0.008    0.000    0.059    0.000 levels.py:9(generate)
                      9    0.000    0.000    0.028    0.003 network.py:17(__init__)
                    300    0.003    0.000    0.023    0.000 level.py:41(notUsed)
                     18    0.000    0.000    0.019    0.001 conv.py:370(__init__)
                     18    0.010    0.001    0.019    0.001 conv.py:66(__init__)
                    129    0.009    0.000    0.017    0.000 levels.py:75(RFS)
                     42    0.000    0.000    0.012    0.000 init.py:347(kaiming_uniform_)
                    200    0.006    0.000    0.012    0.000 layers.py:36(reset)
                      1    0.000    0.000    0.010    0.010 agent.py:158(__init__)
                     84    0.010    0.000    0.010    0.000 {method 'uniform_' of 'torch._C._TensorBase' objects}
                      1    0.000    0.000    0.010    0.010 layers.py:751(__init__)
                    300    0.000    0.000    0.010    0.000 level.py:38(elementsIn)
                      7    0.000    0.000    0.009    0.001 layers.py:782(add)
                   9851    0.009    0.000    0.009    0.000 level.py:32(inverse)
                    800    0.001    0.000    0.009    0.000 layer.py:77(restart)
                      8    0.001    0.000    0.009    0.001 layer.py:61(__init__)
                      1    0.000    0.000    0.008    0.008 agent.py:39(__init__)
                     18    0.000    0.000    0.008    0.000 conv.py:114(reset_parameters)
                     24    0.000    0.000    0.007    0.000 linear.py:75(__init__)
                  24936    0.004    0.000    0.006    0.000 enum.py:646(__hash__)
                    300    0.003    0.000    0.006    0.000 level.py:39(<listcomp>)
                     24    0.000    0.000    0.005    0.000 linear.py:86(reset_parameters)
                   9200    0.004    0.000    0.005    0.000 layer.py:138(add)
                    129    0.002    0.000    0.004    0.000 level.py:16(<dictcomp>)
                   7740    0.003    0.000    0.004    0.000 levels.py:31(<genexpr>)
                  20569    0.004    0.000    0.004    0.000 enum.py:352(<genexpr>)
                      8    0.003    0.000    0.004    0.000 layer.py:175(NoRock_update)
                   1698    0.002    0.000    0.003    0.000 module.py:950(__setattr__)
                    300    0.002    0.000    0.003    0.000 {built-in method _functools.reduce}
                      1    0.000    0.000    0.003    0.003 replaybuffer.py:8(__init__)
                      1    0.003    0.003    0.003    0.003 replaybuffer.py:11(<listcomp>)
                    114    0.001    0.000    0.003    0.000 module.py:250(__init__)
                   2264    0.001    0.000    0.003    0.000 random.py:285(choice)
                      1    0.000    0.000    0.003    0.003 game.py:30(<setcomp>)
                     41    0.001    0.000    0.003    0.000 game.py:30(<listcomp>)
                  17056    0.003    0.000    0.003    0.000 layer.py:190(grid)
                    358    0.001    0.000    0.002    0.000 random.py:315(sample)
                   3131    0.002    0.000    0.002    0.000 random.py:250(_randbelow_with_getrandbits)
                    4/1    0.000    0.000    0.002    0.002 __init__.py:144(_lazy_init)
                      1    0.002    0.002    0.002    0.002 {built-in method torch._C._cuda_init}
                     84    0.002    0.000    0.002    0.000 init.py:268(_calculate_fan_in_and_fan_out)
                  24936    0.002    0.000    0.002    0.000 {built-in method builtins.hash}
                     42    0.000    0.000    0.002    0.000 init.py:337(_calculate_correct_fan)
                  24199    0.002    0.000    0.002    0.000 {method 'append' of 'list' objects}
                   1935    0.001    0.000    0.001    0.000 {method 'intersection_update' of 'set' objects}
                   1935    0.001    0.000    0.001    0.000 levels.py:85(<listcomp>)
                  12600    0.001    0.000    0.001    0.000 level.py:39(<lambda>)
                   5121    0.001    0.000    0.001    0.000 {built-in method builtins.isinstance}
                   5834    0.001    0.000    0.001    0.000 {built-in method builtins.min}
                  10597    0.001    0.000    0.001    0.000 {method 'add' of 'set' objects}
                   2360    0.001    0.000    0.001    0.000 types.py:171(__get__)
                    800    0.001    0.000    0.001    0.000 layer.py:147(clear2)
                   9216    0.001    0.000    0.001    0.000 layer.py:154(elements)
                   5834    0.001    0.000    0.001    0.000 {built-in method builtins.max}
                     33    0.000    0.000    0.001    0.000 activation.py:708(__init__)
                    100    0.000    0.000    0.001    0.000 {built-in method builtins.all}
                    213    0.001    0.000    0.001    0.000 module.py:1338(children)
                      7    0.000    0.000    0.001    0.000 inspect.py:325(getmembers)
                    900    0.000    0.000    0.001    0.000 layers.py:799(<genexpr>)
                      9    0.000    0.000    0.001    0.000 container.py:62(__init__)
                      3    0.000    0.000    0.001    0.000 learner.py:16(__init__)
                    806    0.000    0.000    0.001    0.000 abc.py:96(__instancecheck__)
                     18    0.000    0.000    0.001    0.000 flatten.py:34(__init__)
                    272    0.000    0.000    0.000    0.000 {built-in method builtins.hasattr}
                     84    0.000    0.000    0.000    0.000 module.py:322(register_parameter)
                      3    0.000    0.000    0.000    0.000 adam.py:34(__init__)
                   4992    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
                      3    0.000    0.000    0.000    0.000 optimizer.py:34(__init__)
                   4128    0.000    0.000    0.000    0.000 {method 'remove' of 'set' objects}
                     42    0.000    0.000    0.000    0.000 init.py:112(uniform_)
                    806    0.000    0.000    0.000    0.000 {built-in method _abc._abc_instancecheck}
                      8    0.000    0.000    0.000    0.000 layer.py:71(<listcomp>)
                    345    0.000    0.000    0.000    0.000 module.py:934(__getattr__)
                     42    0.000    0.000    0.000    0.000 init.py:12(_no_grad_uniform_)
                    168    0.000    0.000    0.000    0.000 grad_mode.py:119(__enter__)
                   4917    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
                    336    0.000    0.000    0.000    0.000 grad_mode.py:200(__init__)
                     93    0.000    0.000    0.000    0.000 module.py:361(add_module)
                     90    0.000    0.000    0.000    0.000 utils.py:9(parse)
                      1    0.000    0.000    0.000    0.000 agent.py:167(<listcomp>)
                      1    0.000    0.000    0.000    0.000 layers.py:134(__init__)
              3156/3153    0.000    0.000    0.000    0.000 {built-in method builtins.len}
                   2359    0.000    0.000    0.000    0.000 enum.py:659(name)
                    168    0.000    0.000    0.000    0.000 grad_mode.py:123(__exit__)
                   3131    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
                   1799    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9632763: <Maze_Conver4_3counterfactsNOCRASH_1> in cluster <dcc> Done

Job <Maze_Conver4_3counterfactsNOCRASH_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed May 12 14:13:38 2021
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed May 12 15:13:28 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 12 15:13:28 2021
Terminated at Wed May 12 15:13:41 2021
Results reported at Wed May 12 15:13:41 2021

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

    CPU time :                                   5.13 sec.
    Max Memory :                                 4 MB
    Average Memory :                             4.00 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               16380.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                5
    Run time :                                   14 sec.
    Turnaround time :                            3603 sec.

The output (if any) is above this job summary.

