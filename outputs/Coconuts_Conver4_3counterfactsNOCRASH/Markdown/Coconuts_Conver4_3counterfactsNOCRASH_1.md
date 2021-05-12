
# Parameters

    Name :                      Coconuts_Conver4_3counterfactsNOCRASH-1
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
    Num :                       1
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      62968931874 function calls (62628223379 primitive calls) in 86121.50 seconds

##    Ordered by: cumulative time
   List reduced from 511 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86121.502 86121.502 {built-in method builtins.exec}
                      1    4.927    4.927 86121.501 86121.501 <string>:1(<module>)
                      1  364.348  364.348 86116.574 86116.574 main.py:80(CFagent)
                9320088   38.110    0.000 23411.359    0.003 agent.py:29(learn)
                9320084  592.053    0.000 18952.187    0.002 learner.py:42(Qlearn)
                3106696   14.613    0.000 17992.525    0.006 game.py:42(step)
                3106696   21.790    0.000 17334.536    0.006 layers.py:827(step)
                3106696 1353.310    0.000 17309.162    0.006 agent.py:212(counterfact)
        379454687/38747883 1582.777    0.000 12512.002    0.000 module.py:866(_call_impl)
                3106696  298.530    0.000 11752.890    0.004 layers.py:17(step)
               29427799   81.760    0.000 11749.039    0.000 network.py:28(forward)
               29427799  388.438    0.000 11467.927    0.000 container.py:117(forward)
              309983824 1181.298    0.000 11427.348    0.000 layer.py:106(move)
                3106696  363.583    0.000 9117.307    0.003 agent.py:54(_learn)
                3106696  353.096    0.000 8320.316    0.003 agent.py:204(_learn)
                9320084   84.557    0.000 7313.321    0.001 optimizer.py:84(wrapper)
               87808687 7309.325    0.000 7309.325    0.000 {built-in method tensor}
               80637035   45.109    0.000 7148.842    0.000 game.py:38(board)
                9320084   43.620    0.000 6942.307    0.001 grad_mode.py:24(decorate_context)
              309983824 1163.248    0.000 6865.728    0.000 layers.py:844(check)
                9320084  301.009    0.000 6801.218    0.001 adam.py:55(step)
               10052397  274.559    0.000 6566.424    0.001 agent.py:49(__call__)
                3106696 5551.302    0.002 6559.908    0.002 replaybuffer.py:22(sample_data)
                9320084 1409.027    0.000 6170.437    0.001 _functional.py:53(adam)
                3106696 5208.961    0.002 6168.305    0.002 replaybuffer.py:67(sample_data)
                3106696   97.974    0.000 5914.118    0.002 agent.py:117(_learn)
                3106697  471.474    0.000 5532.058    0.002 layers.py:793(update)
               86987481 2996.780    0.000 5256.296    0.000 layer.py:159(update)
                3841930   78.016    0.000 5222.085    0.001 agent.py:176(choose_action)
                9320084   39.834    0.000 5010.017    0.001 tensor.py:195(backward)
                9320084   41.516    0.000 4968.815    0.001 __init__.py:68(backward)
                9320084 4735.184    0.001 4735.184    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3106696 2646.638    0.001 4510.914    0.001 replaybuffer.py:28(teleporter_save_data)
                3106696 2303.625    0.001 4327.066    0.001 agent.py:88(interveen)
               58855598  135.051    0.000 4250.237    0.000 conv.py:398(forward)
               58855598   85.836    0.000 4051.178    0.000 conv.py:390(_conv_forward)
               58855598 3965.342    0.000 3965.342    0.000 {built-in method conv2d}
               82070005  168.984    0.000 3217.692    0.000 linear.py:93(forward)
               82070005   68.368    0.000 2962.118    0.000 functional.py:1737(linear)
               82070005 2877.835    0.000 2877.835    0.000 {built-in method torch._C._nn.linear}
              309983824  456.305    0.000 2585.182    0.000 layers.py:838(isFree)
                3106696 1526.008    0.000 2331.453    0.001 agent.py:67(modify)
             2025411212 1821.913    0.000 2128.877    0.000 layer.py:103(isFree)
              309983824 1479.588    0.000 2067.574    0.000 layers.py:471(check)
              309983824 1278.068    0.000 1755.242    0.000 layers.py:77(check)
               13159093   89.168    0.000 1740.824    0.000 agent.py:59(modify_board)
              170547052 1696.499    0.000 1696.499    0.000 {built-in method clone}
              111497804   91.852    0.000 1692.392    0.000 activation.py:713(forward)
               44226033 1680.382    0.000 1680.382    0.000 {built-in method cat}
              111497804   94.444    0.000 1600.540    0.000 functional.py:1364(leaky_relu)
              111497804 1487.526    0.000 1487.526    0.000 {built-in method torch._C._nn.leaky_relu}
                3106692   57.270    0.000 1443.621    0.000 agent.py:172(__call__)
                1780437   23.833    0.000 1424.676    0.001 layers.py:849(restart)
             5344233334  984.847    0.000 1419.232    0.000 enum.py:646(__hash__)
                3106696   54.096    0.000 1343.588    0.000 agent.py:112(__call__)
             1040237272 1225.135    0.000 1225.135    0.000 layer.py:154(elements)
                1780437   11.488    0.000 1217.026    0.001 level.py:8(__init__)
              173974896 1216.647    0.000 1216.647    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               13159093 1142.366    0.000 1142.366    0.000 {built-in method torch._C._nn.one_hot}
                1780437   75.625    0.000 1100.766    0.001 levels.py:277(generate)
              318209350  259.040    0.000 1092.994    0.000 {built-in method builtins.any}
              173974896 1069.623    0.000 1069.623    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                9320084  197.129    0.000 1065.248    0.000 optimizer.py:189(zero_grad)
                3841930  908.535    0.000 1054.389    0.000 agent.py:187(convert_values)
               15880681  160.322    0.000  960.446    0.000 level.py:41(notUsed)
                3106696  708.975    0.000  859.719    0.000 replaybuffer.py:73(CF_save_data)
              309983824  657.482    0.000  845.924    0.000 layers.py:62(check)
             2471114104  677.976    0.000  833.954    0.000 layers.py:809(<genexpr>)
              310669700   65.010    0.000  770.124    0.000 {built-in method builtins.all}
        10981148445/10981148442  690.595    0.000  768.276    0.000 {built-in method builtins.len}
                3106696   63.978    0.000  762.092    0.000 replaybuffer.py:18(stacker)
              664411423  159.534    0.000  745.650    0.000 layers.py:799(<genexpr>)
                3106692   63.799    0.000  725.365    0.000 replaybuffer.py:63(stacker)
               86987448  699.045    0.000  699.045    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               10052397  245.449    0.000  667.149    0.000 exploration.py:53(softmaxer)
             7245742281  658.806    0.000  658.806    0.000 layer.py:99(positions)
               86987448  614.112    0.000  614.112    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              310669700  394.427    0.000  574.571    0.000 layers.py:113(isDone)
               86987448  571.902    0.000  571.902    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               86987448  568.609    0.000  568.609    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              608912220  411.920    0.000  508.306    0.000 tensor.py:906(grad)
                3106696  277.438    0.000  473.317    0.000 collector.py:46(collect)
                6213392  181.710    0.000  469.090    0.000 random.py:315(sample)
               15880681   13.103    0.000  463.661    0.000 level.py:38(elementsIn)
              309983824  307.159    0.000  452.567    0.000 layers.py:48(check)
             5344268757  434.392    0.000  434.392    0.000 {built-in method builtins.hash}
                9320084   15.335    0.000  432.549    0.000 loss.py:527(forward)
                9320084   42.858    0.000  417.214    0.000 functional.py:2898(mse_loss)
               86987448  416.871    0.000  416.871    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              335179243  274.103    0.000  389.811    0.000 layer.py:134(remove)
              186812837  382.720    0.000  382.720    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              309983824  239.540    0.000  346.547    0.000 layers.py:23(check)
               86987481  326.538    0.000  326.538    0.000 layer.py:171(<listcomp>)
               15880681  149.209    0.000  301.167    0.000 level.py:39(<listcomp>)
               58855598   43.560    0.000  280.704    0.000 flatten.py:39(forward)
               86987481  268.838    0.000  268.838    0.000 layer.py:172(<listcomp>)
                6213394  252.451    0.000  252.451    0.000 {built-in method nonzero}
                9320084  251.146    0.000  251.146    0.000 {built-in method torch._C._nn.mse_loss}
              433740201  180.015    0.000  250.713    0.000 layer.py:138(add)
               58855598  237.144    0.000  237.144    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9624182: <Coconuts_Conver4_3counterfactsNOCRASH_1> in cluster <dcc> Done

Job <Coconuts_Conver4_3counterfactsNOCRASH_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun May  9 01:29:16 2021
Job was executed on host(s) <n-62-20-10>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon May 10 01:24:41 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon May 10 01:24:41 2021
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

    CPU time :                                   85906.95 sec.
    Max Memory :                                 8982 MB
    Average Memory :                             6121.17 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               7402.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86141 sec.
    Turnaround time :                            172266 sec.

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

    Name :                      Coconuts_Conver4_3counterfactsNOCRASH-1
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
    Num :                       1
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              0 minutes.
    Hours used :                0 hours.

# Profiling


      325183 function calls (324910 primitive calls) in 7.82 seconds

##    Ordered by: cumulative time
   List reduced from 209 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000    7.818    7.818 {built-in method builtins.exec}
                      1    0.000    0.000    7.818    7.818 <string>:1(<module>)
                      1    0.000    0.000    7.818    7.818 main.py:80(CFagent)
                      3    0.000    0.000    7.710    2.570 agent.py:16(__init__)
                      3    0.000    0.000    7.709    2.570 network.py:37(__init__)
                      1    0.000    0.000    7.693    7.693 agent.py:109(__init__)
                      9    0.000    0.000    7.658    0.851 module.py:573(to)
                  111/9    0.001    0.000    7.658    0.851 module.py:385(_apply)
                     84    0.000    0.000    7.656    0.091 module.py:667(convert)
                     84    7.653    0.091    7.656    0.091 {method 'to' of 'torch._C._TensorBase' objects}
                      1    0.002    0.002    0.099    0.099 game.py:9(__init__)
                      1    0.000    0.000    0.082    0.082 layers.py:793(update)
                    100    0.001    0.000    0.074    0.001 layers.py:849(restart)
                    100    0.000    0.000    0.064    0.001 level.py:8(__init__)
                    100    0.004    0.000    0.060    0.001 levels.py:277(generate)
                    856    0.009    0.000    0.052    0.000 level.py:41(notUsed)
                      9    0.000    0.000    0.052    0.006 network.py:17(__init__)
                     18    0.000    0.000    0.041    0.002 conv.py:370(__init__)
                     18    0.009    0.000    0.041    0.002 conv.py:66(__init__)
                     42    0.000    0.000    0.036    0.001 init.py:347(kaiming_uniform_)
                     84    0.033    0.000    0.033    0.000 {method 'uniform_' of 'torch._C._TensorBase' objects}
                     18    0.000    0.000    0.031    0.002 conv.py:114(reset_parameters)
                    856    0.001    0.000    0.025    0.000 level.py:38(elementsIn)
                    856    0.009    0.000    0.017    0.000 level.py:39(<listcomp>)
                      1    0.000    0.000    0.014    0.014 agent.py:39(__init__)
                    200    0.006    0.000    0.012    0.000 layers.py:36(reset)
                  47583    0.008    0.000    0.011    0.000 enum.py:646(__hash__)
                  39610    0.011    0.000    0.011    0.000 level.py:32(inverse)
                    700    0.001    0.000    0.010    0.000 layer.py:77(restart)
                      1    0.000    0.000    0.009    0.009 agent.py:158(__init__)
                      1    0.000    0.000    0.009    0.009 layers.py:751(__init__)
                      6    0.000    0.000    0.009    0.001 layers.py:782(add)
                  43187    0.009    0.000    0.009    0.000 enum.py:352(<genexpr>)
                    856    0.005    0.000    0.008    0.000 {built-in method _functools.reduce}
                      7    0.001    0.000    0.008    0.001 layer.py:61(__init__)
                     24    0.000    0.000    0.007    0.000 linear.py:75(__init__)
                      7    0.005    0.001    0.007    0.001 layer.py:159(update)
                     24    0.000    0.000    0.006    0.000 linear.py:86(reset_parameters)
                  11300    0.004    0.000    0.006    0.000 layer.py:138(add)
                      1    0.000    0.000    0.006    0.006 game.py:30(<setcomp>)
                     41    0.002    0.000    0.005    0.000 game.py:30(<listcomp>)
                      2    0.005    0.003    0.005    0.003 {built-in method zeros}
                   1698    0.002    0.000    0.004    0.000 module.py:950(__setattr__)
                  47583    0.004    0.000    0.004    0.000 {built-in method builtins.hash}
                    100    0.001    0.000    0.003    0.000 level.py:16(<dictcomp>)
                    114    0.001    0.000    0.003    0.000 module.py:250(__init__)
                  35952    0.003    0.000    0.003    0.000 level.py:39(<lambda>)
                    4/1    0.000    0.000    0.003    0.003 __init__.py:144(_lazy_init)
                      1    0.000    0.000    0.003    0.003 replaybuffer.py:8(__init__)
                      1    0.003    0.003    0.003    0.003 replaybuffer.py:11(<listcomp>)
                      1    0.003    0.003    0.003    0.003 {built-in method torch._C._cuda_init}
                  16974    0.003    0.000    0.003    0.000 layer.py:190(grid)
                     84    0.002    0.000    0.002    0.000 init.py:268(_calculate_fan_in_and_fan_out)
                   2275    0.001    0.000    0.002    0.000 types.py:171(__get__)
                  27805    0.002    0.000    0.002    0.000 {method 'append' of 'list' objects}
                     42    0.000    0.000    0.002    0.000 init.py:337(_calculate_correct_fan)
                    656    0.000    0.000    0.001    0.000 random.py:244(randint)
                  11314    0.001    0.000    0.001    0.000 layer.py:154(elements)
                     33    0.000    0.000    0.001    0.000 activation.py:708(__init__)
                    700    0.001    0.000    0.001    0.000 layer.py:147(clear2)
                    656    0.000    0.000    0.001    0.000 random.py:200(randrange)
                    856    0.001    0.000    0.001    0.000 random.py:250(_randbelow_with_getrandbits)
                      6    0.000    0.000    0.001    0.000 inspect.py:325(getmembers)
                     18    0.000    0.000    0.001    0.000 flatten.py:34(__init__)
                    100    0.000    0.000    0.001    0.000 {built-in method builtins.all}
                      9    0.000    0.000    0.001    0.000 container.py:62(__init__)
                   4339    0.000    0.000    0.001    0.000 {built-in method builtins.isinstance}
                      3    0.000    0.000    0.001    0.000 learner.py:16(__init__)
                    800    0.000    0.000    0.001    0.000 layers.py:799(<genexpr>)
                   1005    0.001    0.000    0.001    0.000 enum.py:351(__iter__)
                     18    0.000    0.000    0.001    0.000 utils.py:21(_reverse_repeat_tuple)
                   1799    0.001    0.000    0.001    0.000 {method 'split' of 'str' objects}
                    272    0.000    0.000    0.001    0.000 {built-in method builtins.hasattr}
                   2274    0.001    0.000    0.001    0.000 enum.py:659(name)
                     84    0.000    0.000    0.000    0.000 module.py:322(register_parameter)
                      3    0.000    0.000    0.000    0.000 adam.py:34(__init__)
                     42    0.000    0.000    0.000    0.000 init.py:112(uniform_)
                   4917    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
                      3    0.000    0.000    0.000    0.000 optimizer.py:34(__init__)
                    345    0.000    0.000    0.000    0.000 module.py:934(__getattr__)
                    856    0.000    0.000    0.000    0.000 enum.py:354(__len__)
                     42    0.000    0.000    0.000    0.000 init.py:12(_no_grad_uniform_)
                      7    0.000    0.000    0.000    0.000 layer.py:71(<listcomp>)
                    200    0.000    0.000    0.000    0.000 random.py:285(choice)
                     93    0.000    0.000    0.000    0.000 module.py:361(add_module)
                    168    0.000    0.000    0.000    0.000 grad_mode.py:119(__enter__)
                    336    0.000    0.000    0.000    0.000 grad_mode.py:200(__init__)
                    168    0.000    0.000    0.000    0.000 grad_mode.py:123(__exit__)
                     90    0.000    0.000    0.000    0.000 utils.py:9(parse)
                    213    0.000    0.000    0.000    0.000 module.py:1338(children)
                      1    0.000    0.000    0.000    0.000 layers.py:73(__init__)
                    700    0.000    0.000    0.000    0.000 layer.py:142(clear)
                      1    0.000    0.000    0.000    0.000 agent.py:167(<listcomp>)
                     84    0.000    0.000    0.000    0.000 parameter.py:23(__new__)
                      1    0.000    0.000    0.000    0.000 layers.py:467(__init__)
                     84    0.000    0.000    0.000    0.000 module.py:389(compute_should_use_set_data)
                    168    0.000    0.000    0.000    0.000 grad_mode.py:114(__init__)
                     31    0.000    0.000    0.000    0.000 module.py:1240(parameters)
                     31    0.000    0.000    0.000    0.000 module.py:1264(named_parameters)
                     84    0.000    0.000    0.000    0.000 {built-in method _make_subclass}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9632723: <Coconuts_Conver4_3counterfactsNOCRASH_1> in cluster <dcc> Done

Job <Coconuts_Conver4_3counterfactsNOCRASH_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed May 12 14:11:09 2021
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed May 12 15:12:11 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 12 15:12:11 2021
Terminated at Wed May 12 15:12:23 2021
Results reported at Wed May 12 15:12:23 2021

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

    CPU time :                                   5.42 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   13 sec.
    Turnaround time :                            3674 sec.

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

    Name :                      Coconuts_Conver4_3counterfactsNOCRASH-1
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
    Num :                       1
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              0 minutes.
    Hours used :                0 hours.

# Profiling


      326986 function calls (326713 primitive calls) in 3.61 seconds

##    Ordered by: cumulative time
   List reduced from 209 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000    3.606    3.606 {built-in method builtins.exec}
                      1    0.000    0.000    3.606    3.606 <string>:1(<module>)
                      1    0.000    0.000    3.606    3.606 main.py:80(CFagent)
                      3    0.000    0.000    3.508    1.169 agent.py:16(__init__)
                      3    0.000    0.000    3.508    1.169 network.py:37(__init__)
                      1    0.000    0.000    3.492    3.492 agent.py:109(__init__)
                      9    0.000    0.000    3.491    0.388 module.py:573(to)
                  111/9    0.001    0.000    3.491    0.388 module.py:385(_apply)
                     84    0.000    0.000    3.490    0.042 module.py:667(convert)
                     84    3.489    0.042    3.490    0.042 {method 'to' of 'torch._C._TensorBase' objects}
                      1    0.002    0.002    0.094    0.094 game.py:9(__init__)
                      1    0.000    0.000    0.082    0.082 layers.py:793(update)
                    100    0.001    0.000    0.075    0.001 layers.py:849(restart)
                    100    0.000    0.000    0.064    0.001 level.py:8(__init__)
                    100    0.004    0.000    0.060    0.001 levels.py:277(generate)
                    865    0.009    0.000    0.053    0.000 level.py:41(notUsed)
                    865    0.001    0.000    0.026    0.000 level.py:38(elementsIn)
                    865    0.009    0.000    0.017    0.000 level.py:39(<listcomp>)
                      9    0.000    0.000    0.016    0.002 network.py:17(__init__)
                  47966    0.008    0.000    0.011    0.000 enum.py:646(__hash__)
                  40020    0.011    0.000    0.011    0.000 level.py:32(inverse)
                    200    0.005    0.000    0.010    0.000 layers.py:36(reset)
                    700    0.001    0.000    0.010    0.000 layer.py:77(restart)
                      1    0.000    0.000    0.009    0.009 agent.py:158(__init__)
                     42    0.000    0.000    0.009    0.000 init.py:347(kaiming_uniform_)
                      1    0.000    0.000    0.008    0.008 agent.py:39(__init__)
                  43574    0.008    0.000    0.008    0.000 enum.py:352(<genexpr>)
                    865    0.005    0.000    0.008    0.000 {built-in method _functools.reduce}
                     84    0.008    0.000    0.008    0.000 {method 'uniform_' of 'torch._C._TensorBase' objects}
                      1    0.000    0.000    0.008    0.008 layers.py:751(__init__)
                     18    0.000    0.000    0.007    0.000 conv.py:370(__init__)
                      6    0.000    0.000    0.007    0.001 layers.py:782(add)
                     18    0.001    0.000    0.007    0.000 conv.py:66(__init__)
                      7    0.006    0.001    0.007    0.001 layer.py:159(update)
                      7    0.000    0.000    0.006    0.001 layer.py:61(__init__)
                     24    0.000    0.000    0.006    0.000 linear.py:75(__init__)
                  11300    0.004    0.000    0.005    0.000 layer.py:138(add)
                     24    0.000    0.000    0.005    0.000 linear.py:86(reset_parameters)
                     18    0.000    0.000    0.005    0.000 conv.py:114(reset_parameters)
                  47966    0.003    0.000    0.003    0.000 {built-in method builtins.hash}
                    100    0.001    0.000    0.003    0.000 level.py:16(<dictcomp>)
                   1698    0.002    0.000    0.003    0.000 module.py:950(__setattr__)
                  36330    0.003    0.000    0.003    0.000 level.py:39(<lambda>)
                    114    0.001    0.000    0.003    0.000 module.py:250(__init__)
                      1    0.000    0.000    0.003    0.003 replaybuffer.py:8(__init__)
                      1    0.003    0.003    0.003    0.003 replaybuffer.py:11(<listcomp>)
                  16974    0.002    0.000    0.002    0.000 layer.py:190(grid)
                      1    0.000    0.000    0.002    0.002 game.py:30(<setcomp>)
                     41    0.001    0.000    0.002    0.000 game.py:30(<listcomp>)
                  27805    0.002    0.000    0.002    0.000 {method 'append' of 'list' objects}
                  11314    0.001    0.000    0.001    0.000 layer.py:154(elements)
                    665    0.000    0.000    0.001    0.000 random.py:244(randint)
                     33    0.000    0.000    0.001    0.000 activation.py:708(__init__)
                    4/1    0.000    0.000    0.001    0.001 __init__.py:144(_lazy_init)
                    700    0.001    0.000    0.001    0.000 layer.py:147(clear2)
                    665    0.000    0.000    0.001    0.000 random.py:200(randrange)
                      1    0.001    0.001    0.001    0.001 {built-in method torch._C._cuda_init}
                   2275    0.001    0.000    0.001    0.000 types.py:171(__get__)
                    865    0.000    0.000    0.001    0.000 random.py:250(_randbelow_with_getrandbits)
                    100    0.000    0.000    0.001    0.000 {built-in method builtins.all}
                     84    0.001    0.000    0.001    0.000 init.py:268(_calculate_fan_in_and_fan_out)
                     18    0.000    0.000    0.001    0.000 flatten.py:34(__init__)
                   4339    0.000    0.000    0.001    0.000 {built-in method builtins.isinstance}
                      9    0.000    0.000    0.001    0.000 container.py:62(__init__)
                      6    0.000    0.000    0.001    0.000 inspect.py:325(getmembers)
                      3    0.000    0.000    0.001    0.000 learner.py:16(__init__)
                    800    0.000    0.000    0.001    0.000 layers.py:799(<genexpr>)
                     18    0.001    0.000    0.001    0.000 utils.py:21(_reverse_repeat_tuple)
                     42    0.000    0.000    0.001    0.000 init.py:337(_calculate_correct_fan)
                    272    0.000    0.000    0.000    0.000 {built-in method builtins.hasattr}
                   1014    0.000    0.000    0.000    0.000 enum.py:351(__iter__)
                     84    0.000    0.000    0.000    0.000 module.py:322(register_parameter)
                      3    0.000    0.000    0.000    0.000 adam.py:34(__init__)
                      3    0.000    0.000    0.000    0.000 optimizer.py:34(__init__)
                   4917    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
                    865    0.000    0.000    0.000    0.000 enum.py:354(__len__)
                    345    0.000    0.000    0.000    0.000 module.py:934(__getattr__)
                     42    0.000    0.000    0.000    0.000 init.py:112(uniform_)
                    200    0.000    0.000    0.000    0.000 random.py:285(choice)
                     42    0.000    0.000    0.000    0.000 init.py:12(_no_grad_uniform_)
                     93    0.000    0.000    0.000    0.000 module.py:361(add_module)
                    168    0.000    0.000    0.000    0.000 grad_mode.py:119(__enter__)
                     90    0.000    0.000    0.000    0.000 utils.py:9(parse)
                    336    0.000    0.000    0.000    0.000 grad_mode.py:200(__init__)
                    168    0.000    0.000    0.000    0.000 grad_mode.py:123(__exit__)
                    213    0.000    0.000    0.000    0.000 module.py:1338(children)
                      7    0.000    0.000    0.000    0.000 layer.py:71(<listcomp>)
                      1    0.000    0.000    0.000    0.000 agent.py:167(<listcomp>)
                     84    0.000    0.000    0.000    0.000 module.py:389(compute_should_use_set_data)
                     84    0.000    0.000    0.000    0.000 parameter.py:23(__new__)
                    700    0.000    0.000    0.000    0.000 layer.py:142(clear)
                    168    0.000    0.000    0.000    0.000 grad_mode.py:114(__init__)
                     31    0.000    0.000    0.000    0.000 module.py:1240(parameters)
                      1    0.000    0.000    0.000    0.000 layers.py:467(__init__)
                   2274    0.000    0.000    0.000    0.000 enum.py:659(name)
                     31    0.000    0.000    0.000    0.000 module.py:1264(named_parameters)
                   1799    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
                     31    0.000    0.000    0.000    0.000 module.py:1227(_named_members)
                      1    0.000    0.000    0.000    0.000 layers.py:73(__init__)
                      2    0.000    0.000    0.000    0.000 {built-in method zeros}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9632766: <Coconuts_Conver4_3counterfactsNOCRASH_1> in cluster <dcc> Done

Job <Coconuts_Conver4_3counterfactsNOCRASH_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed May 12 14:13:38 2021
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed May 12 15:13:57 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 12 15:13:57 2021
Terminated at Wed May 12 15:14:10 2021
Results reported at Wed May 12 15:14:10 2021

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

    CPU time :                                   4.76 sec.
    Max Memory :                                 4 MB
    Average Memory :                             4.00 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               16380.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                5
    Run time :                                   8 sec.
    Turnaround time :                            3632 sec.

The output (if any) is above this job summary.

