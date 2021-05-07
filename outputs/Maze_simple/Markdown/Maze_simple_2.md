
# Parameters

    Name :                      Maze_simple-2
    Main :                      simple
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
    Cf convert :                3
    Counterfacts :              1
    Topn :                      6
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      152648630726 function calls (152409442179 primitive calls) in 85913.84 seconds

##    Ordered by: cumulative time
   List reduced from 423 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86119.855 86119.855 {built-in method builtins.exec}
                      1    0.001    0.001 86119.854 86119.854 <string>:1(<module>)
                      1  162.368  162.368 86119.854 86119.854 main.py:67(simple)
                9966174   35.334    0.000 46462.952    0.005 game.py:42(step)
                9966174   50.257    0.000 44131.057    0.004 layers.py:827(step)
                9966174   29.883    0.000 31352.672    0.003 agent.py:29(learn)
                9966174  216.653    0.000 31301.083    0.003 agent.py:117(_learn)
                9966174  790.395    0.000 31084.430    0.003 learner.py:42(Qlearn)
                9966175 1320.695    0.000 23449.229    0.002 layers.py:793(update)
                9966174  704.312    0.000 20575.757    0.002 layers.py:17(step)
              996617400 1422.908    0.000 19789.355    0.000 layer.py:106(move)
                9966174   56.749    0.000 13536.015    0.001 grad_mode.py:23(decorate_context)
              996617400 3282.433    0.000 13488.235    0.000 layers.py:844(check)
                9966174  331.913    0.000 13371.169    0.001 adam.py:55(step)
                9966174 2409.811    0.000 11496.535    0.001 functional.py:53(adam)
        269086698/29898522 1031.404    0.000 11368.550    0.000 module.py:715(_call_impl)
               19932348   45.367    0.000 10577.413    0.001 network.py:28(forward)
               14823902  149.726    0.000 10456.690    0.001 layers.py:849(restart)
               19932348  257.981    0.000 10414.756    0.001 container.py:115(forward)
               14823902   96.600    0.000 9124.212    0.001 level.py:8(__init__)
               20215822 1121.882    0.000 8279.449    0.000 levels.py:9(generate)
                9966174   58.171    0.000 6852.160    0.001 tensor.py:181(backward)
                9966174   35.535    0.000 6793.989    0.001 __init__.py:68(backward)
                9966174 6504.444    0.001 6504.444    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                9966174  119.181    0.000 5893.709    0.001 agent.py:112(__call__)
               79729400 2500.221    0.000 4454.800    0.000 layer.py:175(NoRock_update)
             1918614035 1167.138    0.000 4264.193    0.000 {built-in method builtins.any}
              996617400 2406.276    0.000 4220.152    0.000 layers.py:168(check)
              996617400  918.146    0.000 4129.598    0.000 layers.py:838(isFree)
               39864696   65.961    0.000 3666.181    0.000 conv.py:422(forward)
               39864696   73.548    0.000 3572.801    0.000 conv.py:414(_conv_forward)
               59797044  129.340    0.000 3549.639    0.000 linear.py:92(forward)
               39864696 3484.317    0.000 3484.317    0.000 {built-in method conv2d}
              996617500  442.382    0.000 3363.401    0.000 {built-in method builtins.all}
               59797044  224.917    0.000 3363.009    0.000 functional.py:1669(linear)
            13421677713 2303.697    0.000 3341.569    0.000 enum.py:646(__hash__)
               42195841 3219.901    0.000 3219.901    0.000 {built-in method tensor}
             4158720996 2569.759    0.000 3211.452    0.000 layer.py:103(isFree)
               44471706  348.791    0.000 3066.881    0.000 level.py:41(notUsed)
             5074427896 1240.589    0.000 3037.887    0.000 layers.py:799(<genexpr>)
              697632210 1871.436    0.000 2904.040    0.000 tensor.py:933(grad)
                9966174  268.307    0.000 2802.685    0.000 optimizer.py:167(zero_grad)
             8836142382 2148.166    0.000 2631.440    0.000 layers.py:809(<genexpr>)
               19932348   21.367    0.000 2483.285    0.000 game.py:38(board)
               20215822 1283.155    0.000 2448.849    0.000 levels.py:75(RFS)
              199323480 2415.791    0.000 2415.791    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               59797044 2400.477    0.000 2400.477    0.000 {built-in method addmm}
              199323480 2062.423    0.000 2062.423    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              996617400 1014.476    0.000 1596.482    0.000 layers.py:141(check)
              996617500 1027.271    0.000 1584.534    0.000 layers.py:113(isDone)
               79729392   60.057    0.000 1546.669    0.000 activation.py:713(forward)
               79729392   98.107    0.000 1486.612    0.000 functional.py:1292(leaky_relu)
            17580422269 1481.444    0.000 1481.444    0.000 layer.py:99(positions)
               79729392 1378.415    0.000 1378.415    0.000 {built-in method torch._C._nn.leaky_relu}
              996617400  861.091    0.000 1314.812    0.000 layers.py:124(check)
              996617400  876.051    0.000 1296.652    0.000 layers.py:48(check)
               99661740 1290.372    0.000 1290.372    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               44471706   36.066    0.000 1277.979    0.000 level.py:38(elementsIn)
              857091044  433.815    0.000 1263.857    0.000 overrides.py:1070(has_torch_function)
             1481069366 1231.482    0.000 1231.482    0.000 level.py:32(inverse)
               99661740 1191.292    0.000 1191.292    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              118591216  155.614    0.000 1146.164    0.000 layer.py:77(restart)
             3644178002 1140.637    0.000 1140.637    0.000 layer.py:154(elements)
               99661740 1104.393    0.000 1104.393    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                9966174  628.040    0.000 1057.337    0.000 collector.py:46(collect)
            13421717662 1037.879    0.000 1037.879    0.000 {built-in method builtins.hash}
              996617400  674.697    0.000  994.069    0.000 layers.py:23(check)
               99661740  990.858    0.000  990.858    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
             1743909945  627.269    0.000  855.984    0.000 layer.py:138(add)
               44471706  385.572    0.000  783.327    0.000 level.py:39(<listcomp>)
               99661740  781.393    0.000  781.393    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
        10815538417/10815538416  658.220    0.000  724.159    0.000 {built-in method builtins.len}
               14824002  359.431    0.000  703.336    0.000 layers.py:36(reset)
               20215822  330.429    0.000  696.229    0.000 level.py:16(<dictcomp>)
             8979522774  647.945    0.000  647.945    0.000 {method 'random' of '_random.Random' objects}
             1212949320  394.050    0.000  591.215    0.000 levels.py:31(<genexpr>)
              870364591  383.369    0.000  554.867    0.000 layer.py:134(remove)
                9966174   13.034    0.000  545.507    0.000 loss.py:445(forward)
                9966174   54.922    0.000  532.473    0.000 functional.py:2637(mse_loss)
             2781565831  498.700    0.000  498.700    0.000 enum.py:352(<genexpr>)
             7854348784  483.274    0.000  483.274    0.000 layer.py:92(isDead)
               59797044  473.990    0.000  473.990    0.000 {method 't' of 'torch._C._TensorBase' objects}
             1773979132  369.052    0.000  459.739    0.000 overrides.py:1083(<genexpr>)
               44471706  272.526    0.000  458.586    0.000 {built-in method _functools.reduce}
                9966174   34.874    0.000  451.439    0.000 exploration.py:47(epsilonGreedy)
              353100956  155.017    0.000  440.524    0.000 random.py:285(choice)
             5712910172  414.707    0.000  414.707    0.000 {method 'append' of 'list' objects}
               55255546  154.173    0.000  358.114    0.000 random.py:315(sample)
              484306633  248.993    0.000  356.003    0.000 random.py:250(_randbelow_with_getrandbits)
               19932348  341.593    0.000  341.593    0.000 {built-in method sum}
                9966174  334.530    0.000  334.530    0.000 {built-in method torch._C._nn.mse_loss}
             3162103596  327.838    0.000  327.838    0.000 layer.py:211(isBlocking)
                9966174  315.196    0.000  315.196    0.000 {method 'tolist' of 'torch._C._TensorBase' objects}
                9967170  297.322    0.000  297.322    0.000 {built-in method max}
               39864696   27.559    0.000  267.030    0.000 flatten.py:39(forward)
               99661790  117.016    0.000  260.360    0.000 tensor.py:596(__hash__)
                9966174  248.117    0.000  248.117    0.000 {built-in method gather}
                9966174   40.487    0.000  245.145    0.000 __init__.py:28(_make_grads)
               39864696  239.472    0.000  239.472    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               79729400  235.318    0.000  235.318    0.000 layer.py:186(<listcomp>)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9578854: <Maze_simple_2> in cluster <dcc> Done

Job <Maze_simple_2> was submitted from host <n-62-30-3> by user <s183905> in cluster <dcc> at Mon Apr 26 20:44:07 2021
Job was executed on host(s) <n-62-20-3>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Wed May  5 10:35:22 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May  5 10:35:22 2021
Terminated at Thu May  6 10:31:03 2021
Results reported at Thu May  6 10:31:03 2021

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

    CPU time :                                   85895.95 sec.
    Max Memory :                                 2067 MB
    Average Memory :                             2063.67 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14317.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86142 sec.
    Turnaround time :                            827216 sec.

The output (if any) is above this job summary.

