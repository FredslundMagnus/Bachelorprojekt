
# Parameters

    Name :                      Coconuts_simple-1
    Main :                      simple
    Level :                     Levels.Coconuts
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


      171009704996 function calls (170812961761 primitive calls) in 86102.96 seconds

##    Ordered by: cumulative time
   List reduced from 417 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86102.959 86102.959 {built-in method builtins.exec}
                      1    0.001    0.001 86102.959 86102.959 <string>:1(<module>)
                      1  143.646  143.646 86102.958 86102.958 main.py:67(simple)
                8197620   30.143    0.000 58099.079    0.007 game.py:42(step)
                8197620   39.422    0.000 56302.943    0.007 layers.py:827(step)
                8197621 1188.278    0.000 29882.673    0.004 layers.py:793(update)
                8197620  734.583    0.000 26327.863    0.003 layers.py:17(step)
              819762000 2232.752    0.000 25520.793    0.000 layer.py:106(move)
                8197620   29.433    0.000 21769.363    0.003 agent.py:29(learn)
                8197620  194.122    0.000 21722.163    0.003 agent.py:117(_learn)
                8197620  579.674    0.000 21528.040    0.003 learner.py:42(Qlearn)
               24530626  218.764    0.000 18661.370    0.001 layers.py:849(restart)
              819762000 3101.196    0.000 18563.963    0.000 layers.py:844(check)
               24530626   98.808    0.000 16020.652    0.001 level.py:8(__init__)
               24530626  984.375    0.000 14952.335    0.001 levels.py:277(generate)
              218766783 2118.716    0.000 13117.904    0.000 level.py:41(notUsed)
                8197620   54.124    0.000 8716.121    0.001 grad_mode.py:23(decorate_context)
        221335740/24592860  877.139    0.000 8633.852    0.000 module.py:715(_call_impl)
                8197620  285.822    0.000 8563.497    0.001 adam.py:55(step)
               16395240   38.986    0.000 7982.590    0.000 network.py:28(forward)
               16395240  217.661    0.000 7840.700    0.000 container.py:115(forward)
                8197620 1560.679    0.000 7008.301    0.001 functional.py:53(adam)
              218766783  170.463    0.000 6352.115    0.000 level.py:38(elementsIn)
              819762000 4123.426    0.000 5796.841    0.000 layers.py:471(check)
            22537026725 3852.144    0.000 5600.505    0.000 enum.py:646(__hash__)
               57383347 3532.845    0.000 5308.826    0.000 layer.py:159(update)
                8197620   49.630    0.000 4832.310    0.001 tensor.py:181(backward)
                8197620   31.469    0.000 4782.680    0.001 __init__.py:68(backward)
              819762000 3278.681    0.000 4568.286    0.000 layers.py:77(check)
                8197620 4558.103    0.001 4558.103    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                8197620  103.015    0.000 4467.103    0.001 agent.py:112(__call__)
              218766783 2038.310    0.000 4127.713    0.000 level.py:39(<listcomp>)
              819762000  875.157    0.000 3530.300    0.000 layers.py:838(isFree)
             1565807835  945.114    0.000 3493.732    0.000 {built-in method builtins.any}
               32790480   58.011    0.000 2790.789    0.000 conv.py:422(forward)
            10083175040 2744.233    0.000 2744.233    0.000 level.py:32(inverse)
               32790480   69.247    0.000 2709.796    0.000 conv.py:414(_conv_forward)
             3110176250 2143.899    0.000 2655.144    0.000 layer.py:103(isFree)
               49185720  113.440    0.000 2632.906    0.000 linear.py:92(forward)
               32790480 2628.702    0.000 2628.702    0.000 {built-in method conv2d}
               49185720  190.264    0.000 2468.042    0.000 functional.py:1669(linear)
               34765698 2450.100    0.000 2450.100    0.000 {built-in method tensor}
              819762000 1857.072    0.000 2402.177    0.000 layers.py:62(check)
              171714382  319.371    0.000 2360.938    0.000 layer.py:77(restart)
              573833430 1364.838    0.000 2273.787    0.000 tensor.py:933(grad)
             6361851792 1768.766    0.000 2134.075    0.000 layers.py:809(<genexpr>)
              218766783 1274.285    0.000 2053.939    0.000 {built-in method _functools.reduce}
                8197620  190.532    0.000 1962.470    0.000 optimizer.py:167(zero_grad)
            10461790671 1929.253    0.000 1929.253    0.000 enum.py:352(<genexpr>)
               16395240   20.851    0.000 1909.630    0.000 game.py:38(board)
            22537059594 1748.367    0.000 1748.367    0.000 {built-in method builtins.hash}
               49185720 1730.578    0.000 1730.578    0.000 {built-in method addmm}
              819762100  312.566    0.000 1595.972    0.000 {built-in method builtins.all}
            15904982201 1521.210    0.000 1521.210    0.000 layer.py:99(positions)
              163952400 1412.801    0.000 1412.801    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
             3326113357  869.600    0.000 1383.259    0.000 layers.py:799(<genexpr>)
               24530726  640.194    0.000 1297.701    0.000 layers.py:36(reset)
              163952400 1187.741    0.000 1187.741    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
             2276751021  869.138    0.000 1160.985    0.000 layer.py:138(add)
              819762000  770.512    0.000 1160.110    0.000 layers.py:48(check)
             4664531864 1155.463    0.000 1155.463    0.000 layer.py:154(elements)
              704995400  382.856    0.000 1121.308    0.000 overrides.py:1070(has_torch_function)
               65580960   54.843    0.000 1090.218    0.000 activation.py:713(forward)
               65580960   88.373    0.000 1035.374    0.000 functional.py:1292(leaky_relu)
               65580960  937.953    0.000  937.953    0.000 {built-in method torch._C._nn.leaky_relu}
              819762000  627.343    0.000  914.695    0.000 layers.py:23(check)
               24530626  423.634    0.000  903.433    0.000 level.py:16(<dictcomp>)
               81976200  797.900    0.000  797.900    0.000 {method 'add' of 'torch._C._TensorBase' objects}
             9188204886  779.654    0.000  779.654    0.000 level.py:39(<lambda>)
               81976200  755.436    0.000  755.436    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                8197620  423.917    0.000  731.141    0.000 collector.py:46(collect)
               81976200  674.223    0.000  674.223    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               81976200  594.441    0.000  594.441    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
        7291218399/7291218398  497.627    0.000  550.773    0.000 {built-in method builtins.len}
             6566293620  536.119    0.000  536.119    0.000 {method 'random' of '_random.Random' objects}
             6596666293  458.084    0.000  458.084    0.000 {method 'append' of 'list' objects}
               81976200  449.163    0.000  449.163    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                8197620   12.485    0.000  443.669    0.000 loss.py:445(forward)
                8197620   53.965    0.000  431.185    0.000 functional.py:2637(mse_loss)
             1459176520  331.913    0.000  408.886    0.000 overrides.py:1083(<genexpr>)
             1639524000  401.480    0.000  401.480    0.000 {method 'union' of 'set' objects}
              423010927  227.452    0.000  400.619    0.000 layer.py:134(remove)
                8197620   31.652    0.000  384.946    0.000 exploration.py:47(epsilonGreedy)
             3110176250  356.828    0.000  356.828    0.000 layer.py:211(isBlocking)
              819762100  250.788    0.000  341.743    0.000 layers.py:508(isDone)
              169705531   68.104    0.000  320.877    0.000 random.py:244(randint)
               49185720  317.771    0.000  317.771    0.000 {method 't' of 'torch._C._TensorBase' objects}
             4771388844  307.673    0.000  307.673    0.000 layer.py:92(isDead)
             2011520106  282.829    0.000  282.829    0.000 layer.py:190(grid)
                8197620  256.273    0.000  256.273    0.000 {method 'tolist' of 'torch._C._TensorBase' objects}
              169705531  107.658    0.000  252.773    0.000 random.py:200(randrange)
                8197620  246.798    0.000  246.798    0.000 {built-in method torch._C._nn.mse_loss}
               16395240  237.085    0.000  237.085    0.000 {built-in method sum}
               81976250  101.806    0.000  230.114    0.000 tensor.py:596(__hash__)
                8198439  225.070    0.000  225.070    0.000 {built-in method max}
              218766783  140.105    0.000  202.450    0.000 random.py:250(_randbelow_with_getrandbits)
               57383347  197.596    0.000  197.596    0.000 layer.py:171(<listcomp>)
                8197620   35.151    0.000  185.707    0.000 __init__.py:28(_make_grads)
               32790480   24.866    0.000  184.027    0.000 flatten.py:39(forward)
                8197620  183.873    0.000  183.873    0.000 {built-in method gather}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9578859: <Coconuts_simple_1> in cluster <dcc> Done

Job <Coconuts_simple_1> was submitted from host <n-62-30-3> by user <s183905> in cluster <dcc> at Mon Apr 26 20:44:08 2021
Job was executed on host(s) <n-62-20-10>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Thu May  6 18:30:16 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu May  6 18:30:16 2021
Terminated at Fri May  7 18:25:24 2021
Results reported at Fri May  7 18:25:24 2021

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

    CPU time :                                   85895.77 sec.
    Max Memory :                                 2061 MB
    Average Memory :                             2059.47 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14323.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86109 sec.
    Turnaround time :                            942076 sec.

The output (if any) is above this job summary.

