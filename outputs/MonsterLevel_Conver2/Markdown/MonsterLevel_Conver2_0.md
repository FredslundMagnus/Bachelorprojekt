Start
True
True
['main.py', '-name', 'MonsterLevel_Conver2-0', '-hours', '24.0', '-level', 'Levels.MonsterLevel', '-main', 'CFagent', '-CF_convert', '2', '-TopN', '3']

# Parameters

    Name :                      MonsterLevel_Conver2-0
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


      78739840052 function calls (78394044841 primitive calls) in 86108.48 seconds

##    Ordered by: cumulative time
   List reduced from 509 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86108.480 86108.480 {built-in method builtins.exec}
                      1    4.290    4.290 86108.480 86108.480 <string>:1(<module>)
                      1  363.325  363.325 86104.190 86104.190 main.py:84(CFagent)
                3390343   13.401    0.000 23926.128    0.007 game.py:42(step)
                3390343   20.124    0.000 23293.330    0.007 layers.py:827(step)
               10171029   33.963    0.000 23290.177    0.002 agent.py:29(learn)
               10171029  586.116    0.000 18922.887    0.002 learner.py:42(Qlearn)
                3390343  293.402    0.000 11804.721    0.003 layers.py:17(step)
        385910790/40117270 1425.124    0.000 11781.812    0.000 module.py:866(_call_impl)
              337807489  932.282    0.000 11481.788    0.000 layer.py:106(move)
                3390344  497.504    0.000 11441.647    0.003 layers.py:793(update)
               29946241   76.377    0.000 11069.350    0.000 network.py:28(forward)
               29946241  353.946    0.000 10812.376    0.000 container.py:117(forward)
                3390343 1451.149    0.000 9542.302    0.003 agent.py:212(counterfact)
                3390343  344.821    0.000 9045.917    0.003 agent.py:54(_learn)
                3390343  342.294    0.000 8313.388    0.002 agent.py:204(_learn)
              337807489 1043.358    0.000 7686.523    0.000 layers.py:844(check)
               10171029   77.538    0.000 7331.989    0.001 optimizer.py:84(wrapper)
               10171029   40.531    0.000 6978.928    0.001 grad_mode.py:24(decorate_context)
               10171029  274.370    0.000 6848.797    0.001 adam.py:55(step)
               10171029 1442.098    0.000 6244.801    0.001 _functional.py:53(adam)
                9887535  246.653    0.000 5942.758    0.001 agent.py:49(__call__)
                3390343 4920.230    0.001 5904.809    0.002 replaybuffer.py:22(sample_data)
                3390343   98.570    0.000 5877.516    0.002 agent.py:117(_learn)
               10620541   88.171    0.000 5872.754    0.001 layers.py:849(restart)
                3390343 4890.572    0.001 5848.905    0.002 replaybuffer.py:67(sample_data)
                3390343 3093.886    0.001 5369.969    0.002 replaybuffer.py:28(teleporter_save_data)
               10620541   43.562    0.000 5031.388    0.000 level.py:8(__init__)
               10171029   36.986    0.000 4932.337    0.000 tensor.py:195(backward)
               10171029   37.583    0.000 4894.147    0.000 __init__.py:68(backward)
               10171029 4672.574    0.000 4672.574    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3390343 2635.570    0.001 4663.096    0.001 agent.py:88(interveen)
               10620541  745.253    0.000 4563.516    0.000 levels.py:428(generate)
              337807489 2546.861    0.000 4443.040    0.000 layers.py:538(check)
               59892482  122.492    0.000 3975.718    0.000 conv.py:398(forward)
                3106991   60.230    0.000 3879.676    0.001 agent.py:176(choose_action)
               59892482   75.107    0.000 3797.057    0.000 conv.py:390(_conv_forward)
               59892482 3721.950    0.000 3721.950    0.000 {built-in method conv2d}
               40684122 2348.744    0.000 3563.284    0.000 layer.py:159(update)
               48648510 3407.255    0.000 3407.255    0.000 {built-in method tensor}
               40850269   24.596    0.000 3228.819    0.000 game.py:38(board)
               53102705  483.454    0.000 3097.183    0.000 level.py:41(notUsed)
               83058037  158.288    0.000 3095.570    0.000 linear.py:93(forward)
               83058037   64.258    0.000 2860.020    0.000 functional.py:1737(linear)
               83058037 2780.288    0.000 2780.288    0.000 {built-in method torch._C._nn.linear}
                3390343 1687.571    0.000 2491.206    0.001 agent.py:67(modify)
                3390343 1796.270    0.001 2423.181    0.001 replaybuffer.py:73(CF_save_data)
              270275801 2412.228    0.000 2412.228    0.000 {built-in method clone}
              337807489  443.053    0.000 2206.936    0.000 layers.py:838(isFree)
              339015870  241.666    0.000 2185.026    0.000 {built-in method builtins.any}
             2334955348  616.896    0.000 1944.193    0.000 layers.py:809(<genexpr>)
             7738277635 1251.598    0.000 1817.358    0.000 enum.py:646(__hash__)
             1985946527 1470.491    0.000 1763.882    0.000 layer.py:103(isFree)
               47181308 1662.045    0.000 1662.045    0.000 {built-in method cat}
              113004278   81.419    0.000 1633.934    0.000 activation.py:713(forward)
               13277878   81.462    0.000 1630.163    0.000 agent.py:59(modify_board)
              113004278   88.548    0.000 1552.514    0.000 functional.py:1364(leaky_relu)
              113004278 1446.752    0.000 1446.752    0.000 {built-in method torch._C._nn.leaky_relu}
                3390343   55.394    0.000 1428.912    0.000 agent.py:172(__call__)
               53102705   41.313    0.000 1422.968    0.000 level.py:38(elementsIn)
                3390343   52.424    0.000 1362.890    0.000 agent.py:112(__call__)
              189859208 1232.040    0.000 1232.040    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              335625526  754.409    0.000 1208.756    0.000 layers.py:575(isDead)
               10171029  195.740    0.000 1094.407    0.000 optimizer.py:189(zero_grad)
               13277878 1080.756    0.000 1080.756    0.000 {built-in method torch._C._nn.one_hot}
              189859208 1079.178    0.000 1079.178    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              337807489  768.617    0.000 1071.189    0.000 layers.py:77(check)
               53102705  453.305    0.000  916.387    0.000 level.py:39(<listcomp>)
               59883391  346.139    0.000  892.586    0.000 random.py:315(sample)
              494029370  155.232    0.000  785.948    0.000 random.py:244(randint)
             2613206581  782.151    0.000  782.151    0.000 layer.py:154(elements)
             2265574431  764.459    0.000  764.459    0.000 level.py:32(inverse)
                3390343   53.894    0.000  750.358    0.000 replaybuffer.py:18(stacker)
                3390343   55.964    0.000  732.745    0.000 replaybuffer.py:63(stacker)
               63723246   75.713    0.000  732.469    0.000 layer.py:77(restart)
               94929604  716.931    0.000  716.931    0.000 {method 'add' of 'torch._C._TensorBase' objects}
             1070003463  497.749    0.000  715.900    0.000 random.py:250(_randbelow_with_getrandbits)
                3106991  595.458    0.000  680.455    0.000 agent.py:187(convert_values)
             1279636615  470.248    0.000  638.438    0.000 layer.py:138(add)
              494029370  262.291    0.000  630.716    0.000 random.py:200(randrange)
               94929604  627.247    0.000  627.247    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                9887535  222.566    0.000  590.564    0.000 exploration.py:53(softmaxer)
             6774974379  582.464    0.000  582.464    0.000 layer.py:99(positions)
              794523451  379.467    0.000  577.003    0.000 layer.py:134(remove)
               94929604  572.817    0.000  572.817    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
             7738316306  565.767    0.000  565.767    0.000 {built-in method builtins.hash}
               94929604  549.920    0.000  549.920    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              337807489  370.797    0.000  540.809    0.000 layers.py:48(check)
              286944022  538.966    0.000  538.966    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              664507312  422.597    0.000  520.776    0.000 tensor.py:906(grad)
               10620641  256.479    0.000  506.941    0.000 layers.py:36(reset)
                3390343  286.193    0.000  487.961    0.000 collector.py:46(collect)
              337807489  172.638    0.000  487.566    0.000 layers.py:572(<listcomp>)
             2740101614  475.997    0.000  475.997    0.000 enum.py:352(<genexpr>)
        5940183623/5940183620  408.711    0.000  475.313    0.000 {built-in method builtins.len}
               53102705  287.298    0.000  465.268    0.000 {built-in method _functools.reduce}
               94929604  431.580    0.000  431.580    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               10620541  206.112    0.000  401.882    0.000 level.py:16(<dictcomp>)
               10171029   12.386    0.000  401.726    0.000 loss.py:527(forward)
              337807489  154.266    0.000  397.817    0.000 layers.py:573(<listcomp>)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9579181: <MonsterLevel_Conver2_0> in cluster <dcc> Done

Job <MonsterLevel_Conver2_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Tue Apr 27 02:44:08 2021
Job was executed on host(s) <n-62-20-6>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun May  2 20:33:52 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun May  2 20:33:52 2021
Terminated at Mon May  3 20:29:05 2021
Results reported at Mon May  3 20:29:05 2021

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

    CPU time :                                   85905.56 sec.
    Max Memory :                                 9868 MB
    Average Memory :                             6701.47 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               6516.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86114 sec.
    Turnaround time :                            582297 sec.

The output (if any) is above this job summary.

