Start
True
True
['main.py', '-name', 'MonsterLevel_Conver2-1', '-hours', '24.0', '-level', 'Levels.MonsterLevel', '-main', 'CFagent', '-CF_convert', '2', '-TopN', '3']

# Parameters

    Name :                      MonsterLevel_Conver2-1
    Main :                      CFagent
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
    Cf convert :                2
    Counterfacts :              1
    Topn :                      3
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      78726199069 function calls (78384628658 primitive calls) in 86113.49 seconds

##    Ordered by: cumulative time
   List reduced from 508 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86113.486 86113.486 {built-in method builtins.exec}
                      1    4.280    4.280 86113.486 86113.486 <string>:1(<module>)
                      1  376.730  376.730 86109.207 86109.207 main.py:84(CFagent)
                3346089   14.518    0.000 24704.269    0.007 game.py:42(step)
                3346089   18.793    0.000 24077.341    0.007 layers.py:827(step)
               10038267   35.413    0.000 23157.707    0.002 agent.py:29(learn)
               10038267  580.714    0.000 18795.540    0.002 learner.py:42(Qlearn)
                3346089  301.289    0.000 12087.646    0.004 layers.py:17(step)
                3346090  495.117    0.000 11943.580    0.004 layers.py:793(update)
              333432329  953.636    0.000 11757.370    0.000 layer.py:106(move)
        381186410/39617690 1435.761    0.000 11726.435    0.000 module.py:866(_call_impl)
               29579423   74.327    0.000 11011.905    0.000 network.py:28(forward)
               29579423  354.521    0.000 10760.803    0.000 container.py:117(forward)
                3346089 1461.428    0.000 9502.822    0.003 agent.py:212(counterfact)
                3346089  343.034    0.000 8987.617    0.003 agent.py:54(_learn)
                3346089  340.737    0.000 8272.828    0.002 agent.py:204(_learn)
              333432329 1109.760    0.000 7905.037    0.000 layers.py:844(check)
               10038267   80.205    0.000 7306.070    0.001 optimizer.py:84(wrapper)
               10038267   41.496    0.000 6949.845    0.001 grad_mode.py:24(decorate_context)
               10038267  285.983    0.000 6819.876    0.001 adam.py:55(step)
               10038267 1430.745    0.000 6199.735    0.001 _functional.py:53(adam)
               10551847   90.843    0.000 5984.515    0.001 layers.py:849(restart)
                9770515  253.909    0.000 5922.575    0.001 agent.py:49(__call__)
                3346089  102.103    0.000 5842.210    0.002 agent.py:117(_learn)
                3346089 4710.752    0.001 5709.449    0.002 replaybuffer.py:22(sample_data)
                3346089 4693.349    0.001 5665.566    0.002 replaybuffer.py:67(sample_data)
                3346089 3056.371    0.001 5275.431    0.002 replaybuffer.py:28(teleporter_save_data)
               10551847   43.548    0.000 5131.844    0.000 level.py:8(__init__)
               10038267   39.368    0.000 4859.672    0.000 tensor.py:195(backward)
               10038267   36.066    0.000 4818.975    0.000 __init__.py:68(backward)
               10551847  764.777    0.000 4649.915    0.000 levels.py:428(generate)
               10038267 4596.003    0.000 4596.003    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3346089 2574.572    0.001 4590.810    0.001 agent.py:88(interveen)
              333432329 2571.369    0.000 4529.264    0.000 layers.py:538(check)
               59158846  122.295    0.000 3972.096    0.000 conv.py:398(forward)
                3078463   62.711    0.000 3855.479    0.001 agent.py:176(choose_action)
               59158846   74.846    0.000 3789.065    0.000 conv.py:390(_conv_forward)
               59158846 3714.219    0.000 3714.219    0.000 {built-in method conv2d}
               40153074 2360.080    0.000 3586.424    0.000 layer.py:159(update)
               48099004 3359.577    0.000 3359.577    0.000 {built-in method tensor}
               40399020   24.475    0.000 3185.460    0.000 game.py:38(board)
               52759235  484.707    0.000 3146.268    0.000 level.py:41(notUsed)
               82046091  160.623    0.000 3047.590    0.000 linear.py:93(forward)
               82046091   63.182    0.000 2806.358    0.000 functional.py:1737(linear)
               82046091 2727.501    0.000 2727.501    0.000 {built-in method torch._C._nn.linear}
                3346089 1666.146    0.000 2451.944    0.001 agent.py:67(modify)
                3346089 1788.870    0.001 2413.205    0.001 replaybuffer.py:73(CF_save_data)
              265208358 2340.402    0.000 2340.402    0.000 {built-in method clone}
              333432329  454.158    0.000 2228.135    0.000 layers.py:838(isFree)
              334801206  242.947    0.000 2180.118    0.000 {built-in method builtins.any}
             2297991923  610.103    0.000 1938.035    0.000 layers.py:809(<genexpr>)
             7963378960 1333.743    0.000 1933.692    0.000 enum.py:646(__hash__)
             1918505476 1486.573    0.000 1773.977    0.000 layer.py:103(isFree)
               46577494 1682.948    0.000 1682.948    0.000 {built-in method cat}
              111625514   88.993    0.000 1627.784    0.000 activation.py:713(forward)
               13116604   81.053    0.000 1608.991    0.000 agent.py:59(modify_board)
              111625514   86.584    0.000 1538.790    0.000 functional.py:1364(leaky_relu)
               52759235   43.384    0.000 1463.434    0.000 level.py:38(elementsIn)
              111625514 1434.198    0.000 1434.198    0.000 {built-in method torch._C._nn.leaky_relu}
                3346089   57.639    0.000 1429.459    0.000 agent.py:172(__call__)
                3346089   51.073    0.000 1348.634    0.000 agent.py:112(__call__)
              187380984 1221.950    0.000 1221.950    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              331455116  749.323    0.000 1206.533    0.000 layers.py:575(isDead)
               10038267  198.027    0.000 1103.792    0.000 optimizer.py:189(zero_grad)
              333432329  789.498    0.000 1097.592    0.000 layers.py:77(check)
              187380984 1063.841    0.000 1063.841    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               13116604 1061.464    0.000 1061.464    0.000 {built-in method torch._C._nn.one_hot}
               52759235  474.758    0.000  949.134    0.000 level.py:39(<listcomp>)
               59451413  351.504    0.000  903.874    0.000 random.py:315(sample)
             2583389224  798.326    0.000  798.326    0.000 layer.py:154(elements)
              488003226  151.215    0.000  797.618    0.000 random.py:244(randint)
             2250913287  768.687    0.000  768.687    0.000 level.py:32(inverse)
              334609000   70.673    0.000  766.017    0.000 {built-in method builtins.all}
                3346089   57.327    0.000  764.704    0.000 replaybuffer.py:18(stacker)
                3346089   56.337    0.000  745.534    0.000 replaybuffer.py:63(stacker)
               63311082   76.671    0.000  740.673    0.000 layer.py:77(restart)
             1058019352  513.003    0.000  737.306    0.000 random.py:250(_randbelow_with_getrandbits)
              721683912  170.868    0.000  735.668    0.000 layers.py:799(<genexpr>)
               93690492  712.951    0.000  712.951    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                3078463  577.636    0.000  658.666    0.000 agent.py:187(convert_values)
             1265138218  485.168    0.000  650.733    0.000 layer.py:138(add)
              488003226  266.216    0.000  646.404    0.000 random.py:200(randrange)
             7252071271  642.918    0.000  642.918    0.000 layer.py:99(positions)
               93690492  624.896    0.000  624.896    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
             7963417071  599.955    0.000  599.955    0.000 {built-in method builtins.hash}
              782253679  393.896    0.000  599.733    0.000 layer.py:134(remove)
                9770515  221.240    0.000  587.481    0.000 exploration.py:53(softmaxer)
              333432329  394.855    0.000  580.324    0.000 layers.py:48(check)
               93690492  570.696    0.000  570.696    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              334609000  382.618    0.000  555.328    0.000 layers.py:113(isDone)
              281671051  552.673    0.000  552.673    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               93690492  549.570    0.000  549.570    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              655833528  422.576    0.000  520.605    0.000 tensor.py:906(grad)
              333432329  186.960    0.000  518.872    0.000 layers.py:572(<listcomp>)
               10551947  258.674    0.000  514.243    0.000 layers.py:36(reset)
                3346089  282.124    0.000  482.207    0.000 collector.py:46(collect)
             2722378562  482.058    0.000  482.058    0.000 enum.py:352(<genexpr>)
        5667556834/5667556831  407.544    0.000  471.304    0.000 {built-in method builtins.len}
               52759235  291.158    0.000  470.916    0.000 {built-in method _functools.reduce}
               93690492  436.959    0.000  436.959    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9579182: <MonsterLevel_Conver2_1> in cluster <dcc> Done

Job <MonsterLevel_Conver2_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Tue Apr 27 02:44:09 2021
Job was executed on host(s) <n-62-20-5>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun May  2 20:38:20 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun May  2 20:38:20 2021
Terminated at Mon May  3 20:33:40 2021
Results reported at Mon May  3 20:33:40 2021

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

    CPU time :                                   85901.98 sec.
    Max Memory :                                 9783 MB
    Average Memory :                             6587.28 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               6601.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86121 sec.
    Turnaround time :                            582571 sec.

The output (if any) is above this job summary.

