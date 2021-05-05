Start
True
True
['main.py', '-name', 'Diamonds4_simple-1', '-hours', '24.0', '-level', 'Levels.Causal7', '-main', 'simple', '-network2', 'Networks.MiniBig']

# Parameters

    Name :                      Diamonds4_simple-1
    Main :                      simple
    Level :                     Levels.Causal7
    Failed actions chance :     0.5
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


      159510564555 function calls (159226773104 primitive calls) in 86110.32 seconds

##    Ordered by: cumulative time
   List reduced from 409 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86110.323 86110.323 {built-in method builtins.exec}
                      1    0.001    0.001 86110.323 86110.323 <string>:1(<module>)
                      1  183.870  183.870 86110.322 86110.322 main.py:71(simple)
               11824629   41.306    0.000 46797.754    0.004 game.py:41(step)
               11824629   55.142    0.000 44419.519    0.004 layers.py:718(step)
               11824629   39.595    0.000 30684.226    0.003 agent.py:29(learn)
               11824629  262.797    0.000 30620.782    0.003 agent.py:117(_learn)
               11824629  774.166    0.000 30357.986    0.003 learner.py:42(Qlearn)
               11824630 1639.349    0.000 25532.983    0.002 layers.py:684(update)
               11824629  926.825    0.000 18761.920    0.002 layers.py:17(step)
             1182462900 1809.145    0.000 17709.862    0.000 layer.py:98(move)
               34519462  263.450    0.000 12942.029    0.000 layers.py:740(restart)
               11824629   71.250    0.000 12532.309    0.001 grad_mode.py:23(decorate_context)
               11824629  418.828    0.000 12329.618    0.001 adam.py:55(step)
        319264983/35473887 1203.659    0.000 11893.114    0.000 module.py:715(_call_impl)
               23649258   55.699    0.000 11029.027    0.000 network.py:27(forward)
               23649258  300.646    0.000 10834.724    0.000 container.py:115(forward)
               34519462  125.374    0.000 10368.498    0.000 level.py:8(__init__)
               11824629 2234.648    0.000 10129.927    0.001 functional.py:53(adam)
             1182462900 2575.952    0.000 9891.367    0.000 layers.py:735(check)
               34519462  392.016    0.000 9130.060    0.000 levels.py:441(generate)
              165690180 1515.957    0.000 8341.824    0.000 level.py:41(notUsed)
               11824629   76.169    0.000 6830.222    0.001 tensor.py:181(backward)
               11824629   40.768    0.000 6754.053    0.001 __init__.py:68(backward)
               11824629 6448.718    0.001 6448.718    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               11824629  136.233    0.000 6190.181    0.001 agent.py:112(__call__)
             1182462900 1332.466    0.000 4897.674    0.000 layers.py:729(isFree)
               82772410 2739.905    0.000 4889.623    0.000 layer.py:167(NoRock_update)
             2259458745 1336.269    0.000 4816.690    0.000 {built-in method builtins.any}
            15829846190 2734.896    0.000 3964.871    0.000 enum.py:646(__hash__)
              165690180  122.804    0.000 3918.490    0.000 level.py:38(elementsIn)
               47298516   82.730    0.000 3855.953    0.000 conv.py:422(forward)
               47298516   93.946    0.000 3741.968    0.000 conv.py:414(_conv_forward)
               70947774  161.352    0.000 3631.519    0.000 linear.py:92(forward)
               47298516 3631.519    0.000 3631.519    0.000 {built-in method conv2d}
             5969611323 2809.505    0.000 3565.209    0.000 layer.py:95(isFree)
               70947774  266.257    0.000 3400.528    0.000 functional.py:1669(linear)
               50008210 3281.322    0.000 3281.322    0.000 {built-in method tensor}
              827724060 1924.474    0.000 3224.193    0.000 tensor.py:933(grad)
             9183548304 2336.335    0.000 2895.094    0.000 layers.py:700(<genexpr>)
               11824629  288.456    0.000 2858.269    0.000 optimizer.py:167(zero_grad)
               23649258   24.638    0.000 2560.540    0.000 game.py:37(board)
              165690180 1267.510    0.000 2547.631    0.000 level.py:39(<listcomp>)
               70947774 2373.060    0.000 2373.060    0.000 {built-in method addmm}
              241636234  181.510    0.000 2225.808    0.000 layer.py:69(restart)
              236492580 2040.450    0.000 2040.450    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               34519562  881.430    0.000 1773.146    0.000 layers.py:36(reset)
             1182463000  331.420    0.000 1762.073    0.000 {built-in method builtins.all}
              591231685 1068.907    0.000 1725.451    0.000 layers.py:602(check)
              236492580 1718.409    0.000 1718.409    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              591214838 1058.536    0.000 1717.179    0.000 layers.py:632(check)
             7955209178 1705.173    0.000 1705.173    0.000 level.py:32(inverse)
              591225939 1047.049    0.000 1692.212    0.000 layers.py:617(check)
             1016918174  532.424    0.000 1586.374    0.000 overrides.py:1070(has_torch_function)
             3067343663  728.789    0.000 1574.443    0.000 layers.py:690(<genexpr>)
               94597032   84.322    0.000 1518.371    0.000 activation.py:713(forward)
               94597032  121.202    0.000 1434.049    0.000 functional.py:1292(leaky_relu)
             7207548607 1306.129    0.000 1306.129    0.000 enum.py:352(<genexpr>)
               94597032 1299.053    0.000 1299.053    0.000 {built-in method torch._C._nn.leaky_relu}
            12450203537 1262.461    0.000 1262.461    0.000 layer.py:91(positions)
              165690180  779.562    0.000 1248.055    0.000 {built-in method _functools.reduce}
              118246290 1238.270    0.000 1238.270    0.000 {method 'add' of 'torch._C._TensorBase' objects}
             3527179860 1230.533    0.000 1230.533    0.000 layer.py:146(elements)
            15829893579 1229.983    0.000 1229.983    0.000 {built-in method builtins.hash}
              118246290 1067.377    0.000 1067.377    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               34519462  492.143    0.000 1030.222    0.000 level.py:16(<dictcomp>)
               11824629  598.593    0.000 1027.167    0.000 collector.py:46(collect)
              118246290  956.469    0.000  956.469    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
             1683569405  642.251    0.000  878.435    0.000 layer.py:130(add)
              118246290  839.697    0.000  839.697    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              591220346  519.640    0.000  798.248    0.000 layers.py:588(check)
             9609719903  747.849    0.000  747.849    0.000 {method 'random' of '_random.Random' objects}
        10479548377/10479548376  644.618    0.000  719.953    0.000 {built-in method builtins.len}
              118246290  665.947    0.000  665.947    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              591220820  436.143    0.000  646.920    0.000 layers.py:23(check)
             5969611323  605.591    0.000  605.591    0.000 layer.py:203(isBlocking)
               11824629   19.613    0.000  577.914    0.000 loss.py:445(forward)
             2104784122  465.105    0.000  577.560    0.000 overrides.py:1083(<genexpr>)
             8035604766  558.759    0.000  558.759    0.000 layer.py:84(isDead)
               11824629   64.579    0.000  558.300    0.000 functional.py:2637(mse_loss)
             1182463000  364.053    0.000  490.616    0.000 layers.py:607(isDone)
               11824629   40.770    0.000  485.415    0.000 exploration.py:47(epsilonGreedy)
             5799156300  468.493    0.000  468.493    0.000 level.py:39(<lambda>)
               70947774  441.188    0.000  441.188    0.000 {method 't' of 'torch._C._TensorBase' objects}
             2830604658  351.359    0.000  351.359    0.000 layer.py:182(grid)
             4554072441  350.945    0.000  350.945    0.000 {method 'append' of 'list' objects}
               11824629  340.051    0.000  340.051    0.000 {method 'tolist' of 'torch._C._TensorBase' objects}
               23649258  330.323    0.000  330.323    0.000 {built-in method sum}
               11824629  321.305    0.000  321.305    0.000 {built-in method torch._C._nn.mse_loss}
              118246340  140.531    0.000  320.139    0.000 tensor.py:596(__hash__)
              418080717  210.039    0.000  311.507    0.000 layer.py:126(remove)
               11825811  297.369    0.000  297.369    0.000 {built-in method max}
               82772410  266.455    0.000  266.455    0.000 layer.py:178(<listcomp>)
               47298516   38.771    0.000  265.061    0.000 flatten.py:39(forward)
              165690180   93.396    0.000  259.489    0.000 random.py:285(choice)
               11824629   49.226    0.000  254.091    0.000 __init__.py:28(_make_grads)
               82772410  248.311    0.000  248.311    0.000 layer.py:179(<listcomp>)
               11824629  244.887    0.000  244.887    0.000 {built-in method gather}
               11824629   55.341    0.000  228.268    0.000 tensor.py:506(__rsub__)
               47298516  226.290    0.000  226.290    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9578844: <Diamonds4_simple_1> in cluster <dcc> Done

Job <Diamonds4_simple_1> was submitted from host <n-62-30-3> by user <s183905> in cluster <dcc> at Mon Apr 26 20:44:06 2021
Job was executed on host(s) <n-62-11-13>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sun May  2 03:08:49 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun May  2 03:08:49 2021
Terminated at Mon May  3 03:04:06 2021
Results reported at Mon May  3 03:04:06 2021

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

    CPU time :                                   86012.51 sec.
    Max Memory :                                 2059 MB
    Average Memory :                             2057.08 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14325.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86117 sec.
    Turnaround time :                            541200 sec.

The output (if any) is above this job summary.

