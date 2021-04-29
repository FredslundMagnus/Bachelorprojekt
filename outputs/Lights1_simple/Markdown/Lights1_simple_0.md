
# Parameters

    Name :                      Lights1_simple-0
    Main :                      simple
    Level :                     Levels.Causal3
    Failed actions chance :     0.0
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
    Network2 :                  Networks.MiniBig
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
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                3
    Counterfacts :              1
    Topn :                      6
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      156003082792 function calls (155757865997 primitive calls) in 86118.20 seconds

##    Ordered by: cumulative time
   List reduced from 415 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86118.199 86118.199 {built-in method builtins.exec}
                      1    0.001    0.001 86118.199 86118.199 <string>:1(<module>)
                      1  156.126  156.126 86118.198 86118.198 main.py:66(simple)
               10217351   35.178    0.000 45730.886    0.004 game.py:41(step)
               10217351   46.773    0.000 43396.418    0.004 layers.py:718(step)
               10217351   30.217    0.000 31996.375    0.003 agent.py:29(learn)
               10217351  225.171    0.000 31946.169    0.003 agent.py:117(_learn)
               10217351  799.313    0.000 31720.998    0.003 learner.py:42(Qlearn)
               10217351  713.006    0.000 22777.988    0.002 layers.py:17(step)
             1021735100 1406.041    0.000 21974.109    0.000 layer.py:98(move)
               10217352 1312.365    0.000 20514.690    0.002 layers.py:684(update)
             1021735100 3306.424    0.000 15732.864    0.000 layers.py:735(check)
               10217351   56.032    0.000 13880.223    0.001 grad_mode.py:23(decorate_context)
               10217351  339.466    0.000 13713.418    0.001 adam.py:55(step)
               10217351 2486.640    0.000 11801.577    0.001 functional.py:53(adam)
        275868477/30652053 1026.170    0.000 11545.042    0.000 module.py:715(_call_impl)
               20434702   45.789    0.000 10735.695    0.001 network.py:27(forward)
               20434702  260.988    0.000 10572.685    0.001 container.py:115(forward)
               28544634  220.390    0.000 7990.641    0.000 layers.py:740(restart)
               10217351   56.431    0.000 6984.376    0.001 tensor.py:181(backward)
               10217351   34.814    0.000 6927.945    0.001 __init__.py:68(backward)
               10217351 6635.098    0.001 6635.098    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               10217351  122.339    0.000 5966.172    0.001 agent.py:112(__call__)
               28544634  103.389    0.000 5647.068    0.000 level.py:8(__init__)
               81738816 2596.700    0.000 4669.120    0.000 layer.py:167(NoRock_update)
               28544634  497.372    0.000 4648.460    0.000 levels.py:164(generate)
            17485641769 2993.245    0.000 4407.000    0.000 enum.py:646(__hash__)
             1953621641 1148.422    0.000 4385.321    0.000 {built-in method builtins.any}
             1021735100  817.752    0.000 3900.002    0.000 layers.py:729(isFree)
               40869404   68.311    0.000 3704.768    0.000 conv.py:422(forward)
               40869404   76.558    0.000 3611.828    0.000 conv.py:414(_conv_forward)
               61304106  131.518    0.000 3591.092    0.000 linear.py:92(forward)
               40869404 3521.455    0.000 3521.455    0.000 {built-in method conv2d}
               57089268  455.835    0.000 3424.446    0.000 level.py:41(notUsed)
               61304106  223.632    0.000 3402.482    0.000 functional.py:1669(linear)
               43254758 3230.104    0.000 3230.104    0.000 {built-in method tensor}
             3609523839 2482.270    0.000 3082.250    0.000 layer.py:95(isFree)
             1021735100 1860.027    0.000 3067.154    0.000 layers.py:286(check)
              715214600 1855.283    0.000 2934.768    0.000 tensor.py:933(grad)
             1021735100 1744.893    0.000 2930.619    0.000 layers.py:246(check)
               10217351  251.686    0.000 2825.525    0.000 optimizer.py:167(zero_grad)
             8938715094 2214.661    0.000 2743.405    0.000 layers.py:700(<genexpr>)
             1021735200  453.643    0.000 2597.430    0.000 {built-in method builtins.all}
               20434702   20.262    0.000 2486.148    0.000 game.py:37(board)
              204347020 2475.621    0.000 2475.621    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               61304106 2430.363    0.000 2430.363    0.000 {built-in method addmm}
             5319849624 1298.069    0.000 2266.452    0.000 layers.py:690(<genexpr>)
              204347020 2117.358    0.000 2117.358    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              228357072  229.618    0.000 2043.973    0.000 layer.py:69(restart)
             1021735100 1035.835    0.000 1667.053    0.000 layers.py:313(check)
            17117212817 1617.666    0.000 1617.666    0.000 layer.py:91(positions)
               81738808   71.005    0.000 1604.463    0.000 activation.py:713(forward)
             1021735100  974.258    0.000 1587.995    0.000 layers.py:273(check)
               81738808  105.196    0.000 1533.458    0.000 functional.py:1292(leaky_relu)
               81738808 1417.837    0.000 1417.837    0.000 {built-in method torch._C._nn.leaky_relu}
            17485682718 1413.762    0.000 1413.762    0.000 {built-in method builtins.hash}
               57089268   46.994    0.000 1403.084    0.000 level.py:38(elementsIn)
               28544734  684.360    0.000 1381.408    0.000 layers.py:36(reset)
              102173510 1336.960    0.000 1336.960    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              878692266  453.417    0.000 1312.119    0.000 overrides.py:1070(has_torch_function)
             1021735100  838.532    0.000 1305.809    0.000 layers.py:48(check)
              102173510 1225.828    0.000 1225.828    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
             3918591532 1174.025    0.000 1174.025    0.000 layer.py:146(elements)
             1872645345 1163.766    0.000 1163.766    0.000 level.py:32(inverse)
              102173510 1129.975    0.000 1129.975    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               10217351  633.150    0.000 1070.890    0.000 collector.py:46(collect)
             1021735100  703.287    0.000 1047.479    0.000 layers.py:23(check)
              102173510  998.957    0.000  998.957    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
             1880138148  680.730    0.000  938.261    0.000 layer.py:130(add)
               57089268  418.097    0.000  877.240    0.000 level.py:39(<listcomp>)
               28544634  377.401    0.000  820.755    0.000 level.py:16(<dictcomp>)
              102173510  802.674    0.000  802.674    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
        10963107259/10963107258  720.972    0.000  787.703    0.000 {built-in method builtins.len}
             9337139930  730.105    0.000  730.105    0.000 {method 'random' of '_random.Random' objects}
               10217351   16.551    0.000  561.670    0.000 loss.py:445(forward)
             3082822003  553.902    0.000  553.902    0.000 enum.py:352(<genexpr>)
               10217351   51.953    0.000  545.119    0.000 functional.py:2637(mse_loss)
             7945524528  528.744    0.000  528.744    0.000 layer.py:84(isDead)
               57089268  192.530    0.000  495.848    0.000 random.py:315(sample)
             1818688638  386.832    0.000  487.174    0.000 overrides.py:1083(<genexpr>)
               61304106  479.849    0.000  479.849    0.000 {method 't' of 'torch._C._TensorBase' objects}
               57089268  287.616    0.000  478.849    0.000 {built-in method _functools.reduce}
               10217351   35.280    0.000  451.180    0.000 exploration.py:47(epsilonGreedy)
             5248369174  393.189    0.000  393.189    0.000 {method 'append' of 'list' objects}
             1021735200  283.592    0.000  391.371    0.000 layers.py:52(isDone)
              211042848  231.145    0.000  361.749    0.000 layers.py:113(isDone)
               20434702  348.611    0.000  348.611    0.000 {built-in method sum}
               10217351  344.049    0.000  344.049    0.000 {built-in method torch._C._nn.mse_loss}
               10217351  317.601    0.000  317.601    0.000 {method 'tolist' of 'torch._C._TensorBase' objects}
             2842390015  316.492    0.000  316.492    0.000 layer.py:203(isBlocking)
               10218372  298.780    0.000  298.780    0.000 {built-in method max}
              411277268  193.373    0.000  297.671    0.000 layer.py:126(remove)
             2340668844  276.070    0.000  276.070    0.000 layer.py:182(grid)
               40869404   28.159    0.000  273.132    0.000 flatten.py:39(forward)
              102173560  121.720    0.000  271.410    0.000 tensor.py:596(__hash__)
              355796910  185.694    0.000  269.537    0.000 random.py:250(_randbelow_with_getrandbits)
               10217351  257.668    0.000  257.668    0.000 {built-in method gather}
               10217351   41.367    0.000  249.212    0.000 __init__.py:28(_make_grads)
               40869404  244.973    0.000  244.973    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               81738816  242.622    0.000  242.622    0.000 layer.py:178(<listcomp>)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9578828: <Lights1_simple_0> in cluster <dcc> Done

Job <Lights1_simple_0> was submitted from host <n-62-30-3> by user <s183905> in cluster <dcc> at Mon Apr 26 20:44:03 2021
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Tue Apr 27 09:34:35 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue Apr 27 09:34:35 2021
Terminated at Wed Apr 28 09:30:03 2021
Results reported at Wed Apr 28 09:30:03 2021

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

    CPU time :                                   85896.44 sec.
    Max Memory :                                 2062 MB
    Average Memory :                             2059.28 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14322.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86130 sec.
    Turnaround time :                            132360 sec.

The output (if any) is above this job summary.

