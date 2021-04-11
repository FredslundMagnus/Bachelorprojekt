
# Parameters

    Name :                      MONTEST_CF_5c1-0
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
    Cf convert :                5
    Counterfacts :              1
    Topn :                      7
    Minutes used :              1315 minutes.
    Hours used :                21 hours.

# Profiling


      58874060971 function calls (58598177540 primitive calls) in 78919.26 seconds

##    Ordered by: cumulative time
   List reduced from 506 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 78919.260 78919.260 {built-in method builtins.exec}
                      1    4.665    4.665 78919.259 78919.259 <string>:1(<module>)
                      1  209.893  209.893 78914.595 78914.595 main.py:95(CFagent)
                8090010   32.222    0.000 24267.322    0.003 agent.py:29(learn)
                8090010  602.957    0.000 20176.594    0.002 learner.py:42(Qlearn)
                2696670   14.537    0.000 18195.792    0.007 game.py:41(step)
                2696670   18.185    0.000 17625.167    0.007 layers.py:710(step)
        307860785/31979045 1275.511    0.000 11340.790    0.000 module.py:866(_call_impl)
               23889035   66.600    0.000 10665.467    0.000 network.py:24(forward)
               23889035  326.114    0.000 10443.371    0.000 container.py:117(forward)
                2696670 1658.552    0.001 9750.927    0.004 agent.py:217(counterfact)
                2696670  289.741    0.000 9365.790    0.003 agent.py:54(_learn)
                2696671  391.757    0.000 9208.811    0.003 layers.py:676(update)
                2696670  287.274    0.000 8692.858    0.003 agent.py:209(_learn)
                8090010   67.842    0.000 8462.814    0.001 optimizer.py:84(wrapper)
                2696670  240.569    0.000 8373.522    0.003 layers.py:17(step)
                8090010   34.235    0.000 8134.229    0.001 grad_mode.py:24(decorate_context)
              259504794  725.776    0.000 8106.952    0.000 layer.py:98(move)
                8090010  240.855    0.000 8021.013    0.001 adam.py:55(step)
                8090010 1656.908    0.000 7520.714    0.001 _functional.py:53(adam)
                2696670 3822.419    0.001 7104.961    0.003 replaybuffer.py:28(teleporter_save_data)
                2696670   83.786    0.000 6159.439    0.002 agent.py:117(_learn)
                7899473  222.102    0.000 5707.111    0.001 agent.py:49(__call__)
              259504794  513.361    0.000 5145.923    0.000 layers.py:727(check)
                8090010   34.550    0.000 5111.697    0.001 tensor.py:195(backward)
                8090010   30.867    0.000 5075.903    0.001 __init__.py:68(backward)
                2696670 2952.855    0.001 4889.017    0.002 agent.py:88(interveen)
                8090010 4865.994    0.001 4865.994    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                9175619   71.692    0.000 4714.037    0.001 layers.py:731(restart)
                2696670 3295.922    0.001 4254.704    0.002 replaybuffer.py:22(sample_data)
                9175619   36.333    0.000 3993.206    0.000 level.py:8(__init__)
                2506212   59.113    0.000 3913.928    0.002 agent.py:172(choose_action)
                2696670 2997.102    0.001 3850.921    0.001 replaybuffer.py:49(sample_data)
               47778070  105.070    0.000 3772.141    0.000 conv.py:398(forward)
                9175619  640.148    0.000 3651.134    0.000 levels.py:418(generate)
               47778070   66.100    0.000 3619.732    0.000 conv.py:390(_conv_forward)
               47778070 3553.633    0.000 3553.633    0.000 {built-in method conv2d}
              259504794 1943.768    0.000 3336.692    0.000 layers.py:531(check)
              262026959 3324.725    0.000 3324.725    0.000 {built-in method clone}
               32360046 2133.304    0.000 3153.686    0.000 layer.py:151(update)
               66273765  135.499    0.000 3038.012    0.000 linear.py:93(forward)
               39523222 3003.220    0.000 3003.220    0.000 {built-in method tensor}
               66273765   53.169    0.000 2838.329    0.000 functional.py:1737(linear)
               33255185   26.002    0.000 2828.908    0.000 game.py:37(board)
               66273765 2770.998    0.000 2770.998    0.000 {built-in method torch._C._nn.linear}
                2696670 1739.525    0.001 2516.443    0.001 agent.py:67(modify)
               45878095  393.801    0.000 2390.092    0.000 level.py:41(notUsed)
                2696670  872.046    0.000 1795.801    0.001 replaybuffer.py:55(CF_save_data)
              259423047  295.718    0.000 1737.232    0.000 layers.py:721(isFree)
              268893254  188.483    0.000 1694.376    0.000 {built-in method builtins.any}
               90162800   74.578    0.000 1681.468    0.000 activation.py:713(forward)
               40259513 1632.747    0.000 1632.747    0.000 {built-in method cat}
               90162800   74.912    0.000 1606.890    0.000 functional.py:1364(leaky_relu)
               10596143   75.234    0.000 1538.090    0.000 agent.py:59(modify_board)
              151013520 1538.064    0.000 1538.064    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               90162800 1516.312    0.000 1516.312    0.000 {built-in method torch._C._nn.leaky_relu}
             1851965877  478.232    0.000 1506.544    0.000 layers.py:692(<genexpr>)
             1425356534 1230.662    0.000 1441.514    0.000 layer.py:95(isFree)
                2696670   52.285    0.000 1372.479    0.001 agent.py:168(__call__)
             5932970763  943.403    0.000 1363.829    0.000 enum.py:646(__hash__)
              151013520 1349.082    0.000 1349.082    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                2696670   49.709    0.000 1296.285    0.000 agent.py:112(__call__)
                8090010  184.657    0.000 1161.392    0.000 optimizer.py:189(zero_grad)
               45878095   34.548    0.000 1028.518    0.000 level.py:38(elementsIn)
               10596143  985.490    0.000  985.490    0.000 {built-in method torch._C._nn.one_hot}
              266196583  588.670    0.000  933.991    0.000 layers.py:568(isDead)
               75506760  836.861    0.000  836.861    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              259504794  583.765    0.000  810.401    0.000 layers.py:71(check)
              275319772  807.306    0.000  807.306    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                2506212  675.171    0.000  800.840    0.000 agent.py:183(convert_values)
                2696670   50.763    0.000  772.704    0.000 replaybuffer.py:18(stacker)
               51271435  287.453    0.000  743.268    0.000 random.py:315(sample)
               75506760  733.706    0.000  733.706    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               75506760  692.916    0.000  692.916    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               75506760  691.681    0.000  691.681    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                2696670   49.427    0.000  673.114    0.000 replaybuffer.py:45(stacker)
             1957351308  662.231    0.000  662.231    0.000 level.py:32(inverse)
             2081402661  661.563    0.000  661.563    0.000 layer.py:146(elements)
               45878095  323.963    0.000  650.095    0.000 level.py:39(<listcomp>)
               55053714   63.539    0.000  631.333    0.000 layer.py:69(restart)
                7899473  215.248    0.000  589.247    0.000 exploration.py:53(softmaxer)
              601765250  416.020    0.000  572.357    0.000 layer.py:126(remove)
              360405777  114.162    0.000  570.780    0.000 random.py:244(randint)
                2696670  333.548    0.000  551.452    0.000 collector.py:53(collect)
              834770815  380.210    0.000  549.317    0.000 random.py:250(_randbelow_with_getrandbits)
               75506760  536.095    0.000  536.095    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
             1018940773  374.828    0.000  507.774    0.000 layer.py:130(add)
              360405777  192.697    0.000  456.617    0.000 random.py:200(randrange)
                9175719  221.328    0.000  438.988    0.000 layers.py:30(reset)
              528547404  342.782    0.000  425.743    0.000 tensor.py:906(grad)
              259504794  294.717    0.000  422.357    0.000 layers.py:42(check)
             5933001594  420.431    0.000  420.431    0.000 {built-in method builtins.hash}
                8090010   13.130    0.000  392.410    0.000 loss.py:527(forward)
             4664118629  384.581    0.000  384.581    0.000 layer.py:91(positions)
                8090010   29.821    0.000  379.280    0.000 functional.py:2898(mse_loss)
              259504794  128.591    0.000  367.838    0.000 layers.py:565(<listcomp>)
        4219129272/4219129269  309.660    0.000  364.724    0.000 {built-in method builtins.len}
                8090011  360.341    0.000  360.341    0.000 {built-in method nonzero}
              269667100   60.850    0.000  349.301    0.000 {built-in method builtins.all}
               45878095  211.146    0.000  343.874    0.000 {built-in method _functools.reduce}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-5>
Subject: Job 9507473: <MONTEST_CF_5c1_0> in cluster <dcc> Done

Job <MONTEST_CF_5c1_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sat Apr 10 02:36:49 2021
Job was executed on host(s) <n-62-20-5>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sat Apr 10 02:43:11 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat Apr 10 02:43:11 2021
Terminated at Sun Apr 11 00:38:41 2021
Results reported at Sun Apr 11 00:38:41 2021

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

    CPU time :                                   78717.58 sec.
    Max Memory :                                 8616 MB
    Average Memory :                             6112.07 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               7768.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   78932 sec.
    Turnaround time :                            79312 sec.

The output (if any) is above this job summary.

