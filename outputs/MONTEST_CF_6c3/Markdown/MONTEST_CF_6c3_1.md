
# Parameters

    Name :                      MONTEST_CF_6c3-1
    Main :                      CFagent
    Level :                     Levels.MonsterLevel
    Hours :                     22.0
    Batch :                     100
    Width :                     9
    Height :                    9
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
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                6
    Counterfacts :              3
    Topn :                      7
    Minutes used :              1315 minutes.
    Hours used :                21 hours.

# Profiling


      57364344246 function calls (57018912287 primitive calls) in 78915.02 seconds

##    Ordered by: cumulative time
   List reduced from 505 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 78915.015 78915.015 {built-in method builtins.exec}
                      1    4.739    4.739 78915.015 78915.015 <string>:1(<module>)
                      1  169.744  169.744 78910.277 78910.277 main.py:95(CFagent)
                2323879 4073.789    0.002 23102.257    0.010 agent.py:217(counterfact)
                2323879   11.285    0.000 17649.162    0.008 game.py:41(step)
                6971637   26.471    0.000 17418.917    0.002 agent.py:29(learn)
                2323879   13.555    0.000 17192.531    0.007 layers.py:710(step)
                6971637  439.532    0.000 14190.620    0.002 learner.py:42(Qlearn)
        381962387/36532119 1518.384    0.000 12394.735    0.000 module.py:866(_call_impl)
               29560482   81.029    0.000 11782.169    0.000 network.py:24(forward)
               29560482  373.524    0.000 11510.369    0.000 container.py:117(forward)
                2323880  369.519    0.000 9671.135    0.004 layers.py:676(update)
                6646695  132.957    0.000 9035.163    0.001 agent.py:172(choose_action)
                2323879  219.581    0.000 7488.390    0.003 layers.py:17(step)
               11294392  297.076    0.000 7244.824    0.001 agent.py:49(__call__)
              210781238  651.176    0.000 7242.594    0.000 layer.py:98(move)
                2323879  247.290    0.000 6763.743    0.003 agent.py:54(_learn)
               86787067 6458.560    0.000 6458.560    0.000 {built-in method tensor}
               81341753   51.034    0.000 6356.427    0.000 game.py:37(board)
                2323879  245.439    0.000 6222.777    0.003 agent.py:209(_learn)
                6971637   60.107    0.000 5528.926    0.001 optimizer.py:84(wrapper)
                9405830   80.216    0.000 5444.770    0.001 layers.py:731(restart)
                6971637   31.763    0.000 5262.875    0.001 grad_mode.py:24(decorate_context)
                6971637  218.850    0.000 5166.394    0.001 adam.py:55(step)
                2323879 2892.792    0.001 5063.139    0.002 replaybuffer.py:28(teleporter_save_data)
                6971637 1081.695    0.000 4698.474    0.001 _functional.py:53(adam)
                9405830   38.922    0.000 4627.448    0.000 level.py:8(__init__)
              210781238  471.154    0.000 4626.645    0.000 layers.py:727(check)
               55773102 2861.989    0.000 4479.084    0.000 layer.py:151(update)
                2323879   72.086    0.000 4388.526    0.002 agent.py:117(_learn)
                9405830  737.619    0.000 4241.149    0.000 levels.py:418(generate)
               59120964  133.004    0.000 4195.631    0.000 conv.py:398(forward)
               59120964   80.558    0.000 4004.122    0.000 conv.py:390(_conv_forward)
               59120964 3923.564    0.000 3923.564    0.000 {built-in method conv2d}
                6971637   28.600    0.000 3712.170    0.001 tensor.py:195(backward)
                6971637   29.822    0.000 3682.481    0.001 __init__.py:68(backward)
                2323879 2873.909    0.001 3666.646    0.002 replaybuffer.py:22(sample_data)
                2323879 2082.935    0.001 3572.892    0.002 agent.py:88(interveen)
                6971637 3509.942    0.001 3509.942    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2323879 2660.976    0.001 3364.262    0.001 replaybuffer.py:49(sample_data)
               84033688  177.173    0.000 3277.146    0.000 linear.py:93(forward)
               84033688   70.356    0.000 3018.058    0.000 functional.py:1737(linear)
              210781238 1715.420    0.000 2976.828    0.000 layers.py:531(check)
               84033688 2931.027    0.000 2931.027    0.000 {built-in method torch._C._nn.linear}
               47029150  443.593    0.000 2778.841    0.000 level.py:41(notUsed)
              238141708 2304.683    0.000 2304.683    0.000 {built-in method clone}
                2323879 1281.164    0.001 1863.546    0.001 agent.py:67(modify)
                6646695 1521.366    0.000 1774.543    0.000 agent.py:183(convert_values)
               13618271   85.508    0.000 1757.255    0.000 agent.py:59(modify_board)
              113594170   89.207    0.000 1750.505    0.000 activation.py:713(forward)
              113594170   96.921    0.000 1661.299    0.000 functional.py:1364(leaky_relu)
              234749777  187.481    0.000 1636.007    0.000 {built-in method builtins.any}
              113594170 1545.026    0.000 1545.026    0.000 {built-in method torch._C._nn.leaky_relu}
              210675693  286.814    0.000 1515.482    0.000 layers.py:721(isFree)
                2323879  762.965    0.000 1473.136    0.001 replaybuffer.py:55(CF_save_data)
             5520730029 1001.120    0.000 1456.735    0.000 enum.py:646(__hash__)
             1575263097  465.721    0.000 1449.138    0.000 layers.py:692(<genexpr>)
               39180940 1414.881    0.000 1414.881    0.000 {built-in method cat}
             1237058740 1021.503    0.000 1228.669    0.000 layer.py:95(isFree)
               47029150   38.621    0.000 1209.653    0.000 level.py:38(elementsIn)
               13618271 1146.989    0.000 1146.989    0.000 {built-in method torch._C._nn.one_hot}
                2323879   40.458    0.000 1061.627    0.000 agent.py:168(__call__)
                2323879   37.431    0.000 1014.893    0.000 agent.py:112(__call__)
             1934944875  936.505    0.000  936.505    0.000 layer.py:146(elements)
              130137224  906.678    0.000  906.678    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              227778139  558.000    0.000  895.409    0.000 layers.py:568(isDead)
              130137224  819.544    0.000  819.544    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                6971637  145.185    0.000  819.325    0.000 optimizer.py:189(zero_grad)
               51676908  304.059    0.000  787.153    0.000 random.py:315(sample)
               47029150  378.500    0.000  769.101    0.000 level.py:39(<listcomp>)
             2006441535  766.452    0.000  766.452    0.000 level.py:32(inverse)
              210781238  534.901    0.000  757.278    0.000 layers.py:71(check)
               11294392  269.799    0.000  720.887    0.000 exploration.py:53(softmaxer)
               56434980   74.113    0.000  716.355    0.000 layer.py:69(restart)
              497615957  531.980    0.000  678.902    0.000 layer.py:126(remove)
               56554281  616.746    0.000  616.746    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                2323879   44.636    0.000  614.849    0.000 replaybuffer.py:18(stacker)
              733737262  386.827    0.000  558.837    0.000 random.py:250(_randbelow_with_getrandbits)
        6658476627/6658476624  480.927    0.000  550.054    0.000 {built-in method builtins.len}
               65068612  545.072    0.000  545.072    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              291527501  105.772    0.000  544.100    0.000 random.py:244(randint)
                2323879   43.370    0.000  531.644    0.000 replaybuffer.py:45(stacker)
              254083858  508.365    0.000  508.365    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              921292570  371.738    0.000  505.335    0.000 layer.py:130(add)
                9405930  250.156    0.000  498.348    0.000 layers.py:30(reset)
               65068612  467.508    0.000  467.508    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
             5520756716  455.619    0.000  455.619    0.000 {built-in method builtins.hash}
              291527501  187.945    0.000  438.328    0.000 random.py:200(randrange)
               65068612  432.473    0.000  432.473    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               65068612  427.382    0.000  427.382    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               47029150  247.263    0.000  401.931    0.000 {built-in method _functools.reduce}
             2031660734  392.392    0.000  392.392    0.000 enum.py:352(<genexpr>)
              455480368  309.557    0.000  388.651    0.000 tensor.py:906(grad)
             3897239270  374.395    0.000  374.395    0.000 layer.py:91(positions)
              210781238  250.624    0.000  368.233    0.000 layers.py:42(check)
                2323879  214.999    0.000  363.861    0.000 collector.py:53(collect)
              232388000   59.562    0.000  338.525    0.000 {built-in method builtins.all}
              210781238  116.990    0.000  330.356    0.000 layers.py:565(<listcomp>)
                9405830  164.331    0.000  324.972    0.000 level.py:16(<dictcomp>)
               65068612  324.259    0.000  324.259    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-13>
Subject: Job 9507484: <MONTEST_CF_6c3_1> in cluster <dcc> Done

Job <MONTEST_CF_6c3_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sat Apr 10 02:36:50 2021
Job was executed on host(s) <n-62-20-13>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Apr 11 05:46:08 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun Apr 11 05:46:08 2021
Terminated at Mon Apr 12 03:41:29 2021
Results reported at Mon Apr 12 03:41:29 2021

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

    CPU time :                                   78722.89 sec.
    Max Memory :                                 7952 MB
    Average Memory :                             5756.83 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               8432.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   78922 sec.
    Turnaround time :                            176679 sec.

The output (if any) is above this job summary.

