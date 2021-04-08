
# Parameters

    Name :                      causal3_demo-1
    Main :                      teleport
    Level :                     Levels.Causal3
    Hours :                     16.0
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
    Cf convert :                2
    Counterfacts :              10
    Topn :                      7
    Minutes used :              955 minutes.
    Hours used :                15 hours.

# Profiling


      46216268389 function calls (46047633890 primitive calls) in 57310.24 seconds

##    Ordered by: cumulative time
   List reduced from 477 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 57310.239 57310.239 {built-in method builtins.exec}
                      1    1.861    1.861 57310.239 57310.239 <string>:1(<module>)
                      1  203.505  203.505 57308.378 57308.378 main.py:40(teleport)
                6024014   32.007    0.000 19017.074    0.003 agent.py:29(learn)
                6024014  472.865    0.000 15776.709    0.003 learner.py:42(Qlearn)
                3012007   20.221    0.000 15390.770    0.005 game.py:41(step)
                3012007   20.189    0.000 14606.164    0.005 layers.py:710(step)
                3012007  128.804    0.000 11495.894    0.004 agent.py:54(_learn)
                3012007  316.684    0.000 8696.484    0.003 layers.py:17(step)
              301200700  521.287    0.000 8348.145    0.000 layer.py:98(move)
        189714295/21080807  811.855    0.000 7839.914    0.000 module.py:715(_call_impl)
                3012007  101.475    0.000 7474.007    0.002 agent.py:117(_learn)
               15056793   43.026    0.000 7267.215    0.000 network.py:24(forward)
               15056793  204.237    0.000 7113.203    0.000 container.py:115(forward)
                6024014   49.101    0.000 6136.240    0.001 grad_mode.py:23(decorate_context)
                3012007 4434.804    0.001 6059.542    0.002 replaybuffer.py:22(sample_data)
                6024014  225.426    0.000 5997.392    0.001 adam.py:55(step)
                3012007 3407.817    0.001 5979.031    0.002 replaybuffer.py:28(teleporter_save_data)
                3012008  486.514    0.000 5855.679    0.002 layers.py:676(update)
                3012007 2663.180    0.001 5012.432    0.002 agent.py:88(interveen)
                6020772  189.485    0.000 4982.134    0.001 agent.py:49(__call__)
                6024014 1109.236    0.000 4927.453    0.001 functional.py:53(adam)
              301200700  739.196    0.000 4477.392    0.000 layers.py:727(check)
                6024014   42.752    0.000 3892.995    0.001 tensor.py:181(backward)
                6024014   27.941    0.000 3850.243    0.001 __init__.py:68(backward)
                6024014 3653.116    0.001 3653.116    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3012007 1586.413    0.001 3115.015    0.001 agent.py:67(modify)
              301200700  477.922    0.000 2843.166    0.000 layers.py:721(isFree)
               30113586   61.034    0.000 2698.671    0.000 conv.py:422(forward)
               30113586   71.487    0.000 2610.832    0.000 conv.py:414(_conv_forward)
               30113586 2527.618    0.000 2527.618    0.000 {built-in method conv2d}
             2147031719 2003.286    0.000 2365.244    0.000 layer.py:95(isFree)
               39146365   92.788    0.000 2239.708    0.000 linear.py:92(forward)
               39146365  152.209    0.000 2098.372    0.000 functional.py:1669(linear)
              190153064 2061.444    0.000 2061.444    0.000 {built-in method clone}
               24096064 1082.682    0.000 1909.899    0.000 layer.py:167(NoRock_update)
              843265843  480.635    0.000 1706.389    0.000 {built-in method builtins.any}
               27104821 1598.895    0.000 1598.895    0.000 {built-in method cat}
                3012007   55.759    0.000 1514.712    0.001 agent.py:112(__call__)
                9032779   73.615    0.000 1508.145    0.000 agent.py:59(modify_board)
               39146365 1492.205    0.000 1492.205    0.000 {built-in method addmm}
              379512936  900.986    0.000 1491.805    0.000 tensor.py:933(grad)
                3012007   65.752    0.000 1366.427    0.000 replaybuffer.py:18(stacker)
                6024014  124.477    0.000 1289.479    0.000 optimizer.py:167(zero_grad)
              301200700  790.793    0.000 1201.527    0.000 layers.py:240(check)
             4501183444  825.774    0.000 1181.794    0.000 enum.py:646(__hash__)
               12980812 1112.571    0.000 1112.571    0.000 {built-in method tensor}
                3090093   38.582    0.000 1091.592    0.000 layers.py:731(restart)
              322286627  129.233    0.000 1070.913    0.000 {built-in method builtins.all}
              301200700  624.630    0.000 1032.154    0.000 layers.py:280(check)
              108432252 1004.577    0.000 1004.577    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                9032779  983.211    0.000  983.211    0.000 {built-in method torch._C._nn.one_hot}
               54203158   53.462    0.000  969.827    0.000 activation.py:713(forward)
             1214815293  336.802    0.000  965.089    0.000 layers.py:682(<genexpr>)
             2682996363  748.810    0.000  918.248    0.000 layers.py:692(<genexpr>)
               54203158   80.199    0.000  916.365    0.000 functional.py:1292(leaky_relu)
                6024014   11.229    0.000  885.293    0.000 game.py:37(board)
               21085827  125.527    0.000  854.818    0.000 tensor.py:21(wrapped)
               54203158  828.347    0.000  828.347    0.000 {built-in method torch._C._nn.leaky_relu}
              108432252  815.157    0.000  815.157    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              493960742  273.911    0.000  814.629    0.000 overrides.py:1070(has_torch_function)
                3090093   18.844    0.000  778.553    0.000 level.py:8(__init__)
              199185843  585.750    0.000  585.750    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                3012007  340.852    0.000  583.029    0.000 collector.py:53(collect)
              301200800  396.117    0.000  580.421    0.000 layers.py:107(isDone)
                3090093   68.379    0.000  579.876    0.000 levels.py:164(generate)
               54216126  562.807    0.000  562.807    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                6020772  193.263    0.000  544.085    0.000 exploration.py:53(softmaxer)
              913857472  539.381    0.000  539.381    0.000 layer.py:146(elements)
               54216126  528.627    0.000  528.627    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
             5242260868  506.662    0.000  506.662    0.000 layer.py:91(positions)
              301200700  318.494    0.000  495.646    0.000 layers.py:307(check)
              301200700  312.662    0.000  492.423    0.000 layers.py:267(check)
               54216126  470.142    0.000  470.142    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              301200700  299.826    0.000  435.181    0.000 layers.py:42(check)
               54216126  419.006    0.000  419.006    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                6180186   61.750    0.000  418.169    0.000 level.py:41(notUsed)
                6024014   14.256    0.000  378.272    0.000 loss.py:445(forward)
                6024014   46.377    0.000  364.016    0.000 functional.py:2637(mse_loss)
             4501205515  356.024    0.000  356.024    0.000 {built-in method builtins.hash}
                9192193  125.887    0.000  319.803    0.000 random.py:315(sample)
               15060035  304.283    0.000  304.283    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
             1048153074  242.261    0.000  302.733    0.000 overrides.py:1083(<genexpr>)
               54216126  298.072    0.000  298.072    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
        2827849052/2827849050  200.795    0.000  287.972    0.000 {built-in method builtins.len}
              433988020  204.026    0.000  279.894    0.000 layer.py:130(add)
               39146365  271.694    0.000  271.694    0.000 {method 't' of 'torch._C._TensorBase' objects}
               24720744   33.607    0.000  265.248    0.000 layer.py:69(restart)
                3013211  247.484    0.000  247.484    0.000 {method 'ne' of 'torch._C._TensorBase' objects}
              276461677  159.167    0.000  242.873    0.000 layer.py:126(remove)
               18072042  238.610    0.000  238.610    0.000 {built-in method sum}
                3012007   17.692    0.000  208.056    0.000 exploration.py:47(epsilonGreedy)
                6024014  205.341    0.000  205.341    0.000 {built-in method torch._C._nn.mse_loss}
                6024917  188.806    0.000  188.806    0.000 {built-in method max}
             1630456195  185.163    0.000  185.163    0.000 layer.py:203(isBlocking)
              240016844  120.676    0.000  179.167    0.000 random.py:250(_randbelow_with_getrandbits)
                6020772  177.359    0.000  177.359    0.000 {built-in method multinomial}
               30113586   28.079    0.000  176.963    0.000 flatten.py:39(forward)
             2384885656  169.438    0.000  169.438    0.000 layer.py:84(isDead)
                3090093  111.873    0.000  169.069    0.000 level.py:16(<dictcomp>)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-11>
Subject: Job 9501898: <causal3_demo_1> in cluster <dcc> Done

Job <causal3_demo_1> was submitted from host <n-62-30-7> by user <s183905> in cluster <dcc> at Wed Apr  7 16:17:45 2021
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Thu Apr  8 06:49:34 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Apr  8 06:49:34 2021
Terminated at Thu Apr  8 22:44:50 2021
Results reported at Thu Apr  8 22:44:50 2021

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

    CPU time :                                   57147.28 sec.
    Max Memory :                                 2817 MB
    Average Memory :                             2813.01 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13567.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   57316 sec.
    Turnaround time :                            109625 sec.

The output (if any) is above this job summary.

