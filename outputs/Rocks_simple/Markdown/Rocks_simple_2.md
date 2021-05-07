
# Parameters

    Name :                      Rocks_simple-2
    Main :                      simple
    Level :                     Levels.Rocks
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


      140591570530 function calls (140373295463 primitive calls) in 86114.33 seconds

##    Ordered by: cumulative time
   List reduced from 408 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86114.333 86114.333 {built-in method builtins.exec}
                      1    0.001    0.001 86114.333 86114.333 <string>:1(<module>)
                      1  132.162  132.162 86114.332 86114.332 main.py:67(simple)
                9094779   28.688    0.000 58037.394    0.006 game.py:42(step)
                9094779   38.529    0.000 56378.919    0.006 layers.py:827(step)
                9094779  725.227    0.000 32269.560    0.004 layers.py:17(step)
              909477900 2252.152    0.000 31469.093    0.000 layer.py:106(move)
                9094780 1216.466    0.000 24019.222    0.003 layers.py:793(update)
              909477900 2527.440    0.000 22884.646    0.000 layers.py:844(check)
                9094779   23.956    0.000 22003.085    0.002 agent.py:29(learn)
                9094779  191.339    0.000 21962.125    0.002 agent.py:117(_learn)
                9094779  562.998    0.000 21770.786    0.002 learner.py:42(Qlearn)
              909477900 14145.840    0.000 16917.258    0.000 layers.py:77(check)
               32297109  231.356    0.000 10676.864    0.000 layers.py:849(restart)
                9094779   53.202    0.000 8892.767    0.001 grad_mode.py:23(decorate_context)
                9094779  284.132    0.000 8744.392    0.001 adam.py:55(step)
        245559033/27284337  844.754    0.000 8547.889    0.000 module.py:715(_call_impl)
               18189558   38.021    0.000 7918.266    0.000 network.py:28(forward)
               18189558  202.117    0.000 7778.239    0.000 container.py:115(forward)
               32297109  100.843    0.000 7648.060    0.000 level.py:8(__init__)
                9094779 1586.043    0.000 7202.687    0.001 functional.py:53(adam)
               32297109  780.151    0.000 6471.262    0.000 levels.py:95(generate)
               45473900 4507.613    0.000 6240.843    0.000 layer.py:159(update)
                9094779   54.391    0.000 5010.929    0.001 tensor.py:181(backward)
                9094779   28.474    0.000 4956.538    0.001 __init__.py:68(backward)
              909477900  960.667    0.000 4927.411    0.000 layers.py:838(isFree)
                9094779 4736.335    0.001 4736.335    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                9094779   99.279    0.000 4420.432    0.000 agent.py:112(__call__)
               64594218  521.958    0.000 4301.452    0.000 level.py:41(notUsed)
             4079253366 3338.231    0.000 3966.744    0.000 layer.py:103(isFree)
              909478000  405.684    0.000 3146.627    0.000 {built-in method builtins.all}
             1732090198  859.747    0.000 3092.313    0.000 {built-in method builtins.any}
            11591756290 1980.654    0.000 2888.082    0.000 enum.py:646(__hash__)
             4573427884 1177.837    0.000 2846.016    0.000 layers.py:799(<genexpr>)
               36379116   57.512    0.000 2805.690    0.000 conv.py:422(forward)
              161485545  372.303    0.000 2743.369    0.000 layer.py:77(restart)
               36379116   66.059    0.000 2725.669    0.000 conv.py:414(_conv_forward)
               36379116 2647.374    0.000 2647.374    0.000 {built-in method conv2d}
               54568674  111.564    0.000 2603.580    0.000 linear.py:92(forward)
               54568674  183.674    0.000 2441.628    0.000 functional.py:1669(linear)
              636634560 1359.247    0.000 2260.292    0.000 tensor.py:933(grad)
               38536776 2200.632    0.000 2200.632    0.000 {built-in method tensor}
             4280167749 1485.641    0.000 2006.776    0.000 layer.py:138(add)
                9094779  186.705    0.000 1960.955    0.000 optimizer.py:167(zero_grad)
              909477900 1226.651    0.000 1936.272    0.000 layers.py:62(check)
               64594218   53.372    0.000 1830.754    0.000 level.py:38(elementsIn)
             5263085346 1517.923    0.000 1821.191    0.000 layers.py:809(<genexpr>)
             2020135698  873.188    0.000 1781.173    0.000 layer.py:134(remove)
               54568674 1717.405    0.000 1717.405    0.000 {built-in method addmm}
               18189558   17.313    0.000 1666.865    0.000 game.py:38(board)
               32297209  791.205    0.000 1574.949    0.000 layers.py:36(reset)
              909478000  968.675    0.000 1489.170    0.000 layers.py:113(isDone)
              181895580 1446.875    0.000 1446.875    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
             1776340995 1436.357    0.000 1436.357    0.000 level.py:32(inverse)
             8606517803 1321.338    0.000 1321.338    0.000 layer.py:154(elements)
              181895580 1230.485    0.000 1230.485    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
            12937085724 1121.023    0.000 1121.023    0.000 layer.py:99(positions)
               64594218  550.872    0.000 1110.409    0.000 level.py:39(<listcomp>)
              782151074  372.844    0.000 1108.074    0.000 overrides.py:1070(has_torch_function)
               72758232   54.939    0.000 1088.563    0.000 activation.py:713(forward)
               72758232   88.020    0.000 1033.624    0.000 functional.py:1292(leaky_relu)
               32297109  448.329    0.000 1017.196    0.000 level.py:16(<dictcomp>)
              909477900  668.011    0.000  979.377    0.000 layers.py:23(check)
               72758232  936.042    0.000  936.042    0.000 {built-in method torch._C._nn.leaky_relu}
            11591792759  907.434    0.000  907.434    0.000 {built-in method builtins.hash}
               32297109  310.766    0.000  895.835    0.000 random.py:315(sample)
              909477900  389.250    0.000  894.409    0.000 layers.py:104(<listcomp>)
               90947790  871.848    0.000  871.848    0.000 {method 'add' of 'torch._C._TensorBase' objects}
            12626945293  827.667    0.000  827.667    0.000 {method 'append' of 'list' objects}
               90947790  763.896    0.000  763.896    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
             2020135698  747.356    0.000  747.356    0.000 {method 'remove' of 'list' objects}
                9094779  427.854    0.000  737.632    0.000 collector.py:46(collect)
             4166329059  722.273    0.000  722.273    0.000 enum.py:352(<genexpr>)
               90947790  685.088    0.000  685.088    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               64594218  398.891    0.000  666.973    0.000 {built-in method _functools.reduce}
               90947790  592.038    0.000  592.038    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              807427725  334.920    0.000  478.801    0.000 random.py:250(_randbelow_with_getrandbits)
               90947790  456.391    0.000  456.391    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
             5465962179  440.650    0.000  440.650    0.000 {method 'random' of '_random.Random' objects}
             4079253366  428.499    0.000  428.499    0.000 layer.py:211(isBlocking)
        5336096270/5336096269  373.191    0.000  426.084    0.000 {built-in method builtins.len}
                9094779   11.832    0.000  422.644    0.000 loss.py:445(forward)
                9094779   48.079    0.000  410.812    0.000 functional.py:2637(mse_loss)
             1618870822  327.366    0.000  405.470    0.000 overrides.py:1083(<genexpr>)
                9094779   29.937    0.000  358.865    0.000 exploration.py:47(epsilonGreedy)
               54568674  314.043    0.000  314.043    0.000 {method 't' of 'torch._C._TensorBase' objects}
             2648371548  304.894    0.000  304.894    0.000 layer.py:190(grid)
             4385904455  303.267    0.000  303.267    0.000 layer.py:92(isDead)
             2712957156  268.082    0.000  268.082    0.000 level.py:39(<lambda>)
                9094779  254.189    0.000  254.189    0.000 {method 'tolist' of 'torch._C._TensorBase' objects}
               18189558  240.575    0.000  240.575    0.000 {built-in method sum}
                9094779  235.831    0.000  235.831    0.000 {built-in method torch._C._nn.mse_loss}
               90947840   99.551    0.000  225.737    0.000 tensor.py:596(__hash__)
                9095688  216.199    0.000  216.199    0.000 {built-in method max}
                9094779   34.969    0.000  184.452    0.000 __init__.py:28(_make_grads)
               36379116   25.103    0.000  184.264    0.000 flatten.py:39(forward)
             2754471884  179.009    0.000  179.009    0.000 layer.py:89(isDone)
                9094779  178.262    0.000  178.262    0.000 {built-in method gather}
             1818955800  169.559    0.000  169.559    0.000 layer.py:86(check)
                9094779   41.190    0.000  168.937    0.000 tensor.py:506(__rsub__)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9578857: <Rocks_simple_2> in cluster <dcc> Done

Job <Rocks_simple_2> was submitted from host <n-62-30-3> by user <s183905> in cluster <dcc> at Mon Apr 26 20:44:07 2021
Job was executed on host(s) <n-62-20-7>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Wed May  5 17:39:17 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May  5 17:39:17 2021
Terminated at Thu May  6 17:34:42 2021
Results reported at Thu May  6 17:34:42 2021

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

    CPU time :                                   86054.04 sec.
    Max Memory :                                 2063 MB
    Average Memory :                             2060.19 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14321.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86125 sec.
    Turnaround time :                            852635 sec.

The output (if any) is above this job summary.

