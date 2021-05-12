
# Parameters

    Name :                      Monsters_simple-0
    Main :                      simple
    Level :                     Levels.MonsterLevel
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
    Num :                       0
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      156328143623 function calls (156123778020 primitive calls) in 86112.90 seconds

##    Ordered by: cumulative time
   List reduced from 417 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86112.900 86112.900 {built-in method builtins.exec}
                      1    0.001    0.001 86112.900 86112.900 <string>:1(<module>)
                      1  131.886  131.886 86112.899 86112.899 main.py:67(simple)
                8515218   31.744    0.000 52434.847    0.006 game.py:42(step)
                8515218   39.562    0.000 50599.585    0.006 layers.py:827(step)
                8515218  681.491    0.000 26998.532    0.003 layers.py:17(step)
                8515218   26.102    0.000 26788.158    0.003 agent.py:29(learn)
                8515218  189.165    0.000 26745.326    0.003 agent.py:117(_learn)
                8515218  671.741    0.000 26556.161    0.003 learner.py:42(Qlearn)
              851521800 2147.099    0.000 26243.307    0.000 layer.py:106(move)
                8515219 1129.798    0.000 23512.840    0.003 layers.py:793(update)
              851521800 2608.552    0.000 18420.627    0.000 layers.py:844(check)
                8515218   48.794    0.000 11602.899    0.001 grad_mode.py:23(decorate_context)
                8515218  281.021    0.000 11458.777    0.001 adam.py:55(step)
              851521800 5606.147    0.000 10448.045    0.000 layers.py:538(check)
               18356590  132.481    0.000 10003.354    0.001 layers.py:849(restart)
                8515218 2085.733    0.000 9894.764    0.001 functional.py:53(adam)
        229910886/25545654  863.170    0.000 9659.718    0.000 module.py:715(_call_impl)
               17030436   38.565    0.000 8981.919    0.001 network.py:28(forward)
               17030436  223.710    0.000 8845.493    0.001 container.py:115(forward)
               18356590   67.413    0.000 8580.876    0.000 level.py:8(__init__)
               18356590 1274.105    0.000 7835.303    0.000 levels.py:428(generate)
             1642235374  877.720    0.000 6145.974    0.000 {built-in method builtins.any}
                8515218   48.234    0.000 5880.420    0.001 tensor.py:181(backward)
                8515218   28.640    0.000 5832.186    0.001 __init__.py:68(backward)
                8515218 5587.695    0.001 5587.695    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               91782950  816.453    0.000 5320.306    0.000 level.py:41(notUsed)
                8515218  103.200    0.000 4992.035    0.001 agent.py:112(__call__)
             5866715134 1589.794    0.000 4881.794    0.000 layers.py:809(<genexpr>)
               51091314 3248.935    0.000 4749.759    0.000 layer.py:159(update)
              851521800  989.961    0.000 4145.578    0.000 layers.py:838(isFree)
            17048920455 2831.199    0.000 4045.807    0.000 enum.py:646(__hash__)
             4541457040 2485.714    0.000 3155.616    0.000 layer.py:103(isFree)
               34060872   54.890    0.000 3101.465    0.000 conv.py:422(forward)
               34060872   64.628    0.000 3025.390    0.000 conv.py:414(_conv_forward)
               51091308  107.546    0.000 3004.174    0.000 linear.py:92(forward)
              841804801 1842.914    0.000 2977.722    0.000 layers.py:575(isDead)
               34060872 2949.664    0.000 2949.664    0.000 {built-in method conv2d}
               51091308  181.839    0.000 2848.176    0.000 functional.py:1669(linear)
              851521800 1868.383    0.000 2694.503    0.000 layers.py:77(check)
               91782950   67.141    0.000 2456.433    0.000 level.py:38(elementsIn)
               36099683 2438.699    0.000 2438.699    0.000 {built-in method tensor}
              596065290 1539.642    0.000 2413.984    0.000 tensor.py:933(grad)
                8515218  214.428    0.000 2338.856    0.000 optimizer.py:167(zero_grad)
              170304360 2065.846    0.000 2065.846    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               51091308 2044.123    0.000 2044.123    0.000 {built-in method addmm}
             1238923441  384.456    0.000 1946.362    0.000 random.py:244(randint)
              851521900  180.513    0.000 1819.930    0.000 {built-in method builtins.all}
               17030436   18.004    0.000 1815.041    0.000 game.py:38(board)
              170304360 1779.134    0.000 1779.134    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
             1887298220  437.661    0.000 1744.430    0.000 layers.py:799(<genexpr>)
            18334180361 1650.112    0.000 1650.112    0.000 layer.py:99(positions)
               91782950  781.638    0.000 1576.779    0.000 level.py:39(<listcomp>)
             1238923441  649.579    0.000 1561.906    0.000 random.py:200(randrange)
             2807299261 1035.385    0.000 1394.964    0.000 layer.py:138(add)
               68121744   54.067    0.000 1332.135    0.000 activation.py:713(forward)
             1977672146  849.220    0.000 1314.211    0.000 layer.py:134(remove)
             3915875607 1296.978    0.000 1296.978    0.000 level.py:32(inverse)
               68121744   86.352    0.000 1278.068    0.000 functional.py:1292(leaky_relu)
              851521900  846.889    0.000 1277.672    0.000 layers.py:113(isDone)
              110139540  126.064    0.000 1254.616    0.000 layer.py:77(restart)
              851521800  440.452    0.000 1247.200    0.000 layers.py:572(<listcomp>)
              851521800  815.639    0.000 1233.706    0.000 layers.py:48(check)
            17048954604 1214.613    0.000 1214.613    0.000 {built-in method builtins.hash}
               68121744 1183.420    0.000 1183.420    0.000 {built-in method torch._C._nn.leaky_relu}
             1648301370  835.422    0.000 1182.890    0.000 random.py:250(_randbelow_with_getrandbits)
               85152180 1120.306    0.000 1120.306    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              732308828  374.660    0.000 1068.200    0.000 overrides.py:1070(has_torch_function)
             5668766800 1055.189    0.000 1055.189    0.000 layer.py:154(elements)
               85152180 1027.863    0.000 1027.863    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              851521800  398.265    0.000 1012.223    0.000 layers.py:573(<listcomp>)
               85152180  941.244    0.000  941.244    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                8515218  537.993    0.000  909.915    0.000 collector.py:46(collect)
              851521800  610.725    0.000  894.888    0.000 layers.py:23(check)
               18356690  447.996    0.000  887.804    0.000 layers.py:36(reset)
               85152180  848.433    0.000  848.433    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
             4736002261  830.747    0.000  830.747    0.000 enum.py:352(<genexpr>)
               91782950  501.898    0.000  812.513    0.000 {built-in method _functools.reduce}
               91782950  305.839    0.000  771.805    0.000 random.py:315(sample)
               85152180  666.435    0.000  666.435    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               18356590  310.919    0.000  640.937    0.000 level.py:16(<dictcomp>)
             8318355105  585.170    0.000  585.170    0.000 {method 'append' of 'list' objects}
                8515218   12.011    0.000  471.677    0.000 loss.py:445(forward)
             5969167818  469.062    0.000  469.062    0.000 {method 'random' of '_random.Random' objects}
             4541457040  467.114    0.000  467.114    0.000 layer.py:211(isBlocking)
                8515218   42.841    0.000  459.666    0.000 functional.py:2637(mse_loss)
        5489640834/5489640833  391.073    0.000  447.577    0.000 {built-in method builtins.len}
               51091308  401.251    0.000  401.251    0.000 {method 't' of 'torch._C._TensorBase' objects}
                8515218   29.741    0.000  382.724    0.000 exploration.py:47(epsilonGreedy)
             1515708964  305.444    0.000  382.237    0.000 overrides.py:1083(<genexpr>)
             4183105532  314.278    0.000  314.278    0.000 layer.py:92(isDead)
             3854883900  310.615    0.000  310.615    0.000 level.py:39(<lambda>)
             1977672146  303.002    0.000  303.002    0.000 {method 'remove' of 'list' objects}
               17030436  295.168    0.000  295.168    0.000 {built-in method sum}
                8515218  291.204    0.000  291.204    0.000 {built-in method torch._C._nn.mse_loss}
                8515218  267.801    0.000  267.801    0.000 {method 'tolist' of 'torch._C._TensorBase' objects}
                8516069  251.021    0.000  251.021    0.000 {built-in method max}
               34060872   27.716    0.000  231.639    0.000 flatten.py:39(forward)
               85152230   98.196    0.000  220.089    0.000 tensor.py:596(__hash__)
             2634151752  214.672    0.000  214.672    0.000 {method 'getrandbits' of '_random.Random' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9623997: <Monsters_simple_0> in cluster <dcc> Done

Job <Monsters_simple_0> was submitted from host <n-62-30-2> by user <s183905> in cluster <dcc> at Sat May  8 23:34:13 2021
Job was executed on host(s) <n-62-20-5>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sat May  8 23:34:14 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat May  8 23:34:14 2021
Terminated at Sun May  9 23:29:43 2021
Results reported at Sun May  9 23:29:43 2021

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

    CPU time :                                   85895.37 sec.
    Max Memory :                                 2066 MB
    Average Memory :                             2062.99 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14318.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86172 sec.
    Turnaround time :                            86130 sec.

The output (if any) is above this job summary.

