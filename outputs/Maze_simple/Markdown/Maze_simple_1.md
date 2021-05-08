
# Parameters

    Name :                      Maze_simple-1
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


      155920011286 function calls (155664070163 primitive calls) in 85862.22 seconds

##    Ordered by: cumulative time
   List reduced from 423 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86102.952 86102.952 {built-in method builtins.exec}
                      1    0.001    0.001 86102.952 86102.952 <string>:1(<module>)
                      1  168.955  168.955 86102.951 86102.951 main.py:67(simple)
               10664198   34.894    0.000 51201.989    0.005 game.py:42(step)
               10664198   48.462    0.000 48888.019    0.005 layers.py:827(step)
               10664198   31.014    0.000 27098.845    0.003 agent.py:29(learn)
               10664198  235.050    0.000 27045.407    0.003 agent.py:117(_learn)
               10664198  705.290    0.000 26810.357    0.003 learner.py:42(Qlearn)
               10664199 1517.591    0.000 26230.470    0.002 layers.py:793(update)
               10664198  803.796    0.000 22546.321    0.002 layers.py:17(step)
             1066419800 1623.944    0.000 21648.613    0.000 layer.py:106(move)
             1066419800 3770.659    0.000 15386.960    0.000 layers.py:844(check)
               15956319  172.215    0.000 12021.471    0.001 layers.py:849(restart)
               10664198   63.884    0.000 11016.232    0.001 grad_mode.py:23(decorate_context)
               10664198  357.767    0.000 10836.114    0.001 adam.py:55(step)
        287933346/31992594 1070.122    0.000 10593.542    0.000 module.py:715(_call_impl)
               15956319  115.471    0.000 10494.235    0.001 level.py:8(__init__)
               21328396   51.559    0.000 9806.468    0.000 network.py:28(forward)
               21328396  257.835    0.000 9624.629    0.000 container.py:115(forward)
               21761437 1290.329    0.000 9526.061    0.000 levels.py:9(generate)
               10664198 1971.871    0.000 8905.883    0.001 functional.py:53(adam)
               10664198   58.763    0.000 6006.680    0.001 tensor.py:181(backward)
               10664198   36.782    0.000 5947.918    0.001 __init__.py:68(backward)
               10664198 5674.630    0.001 5674.630    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               10664198  122.562    0.000 5494.364    0.001 agent.py:112(__call__)
               85313592 2916.476    0.000 5175.634    0.000 layer.py:175(NoRock_update)
             2052898274 1297.451    0.000 4935.442    0.000 {built-in method builtins.any}
             1066419800 2719.406    0.000 4809.703    0.000 layers.py:168(check)
            14387509497 2671.395    0.000 3817.712    0.000 enum.py:646(__hash__)
             1066419800  827.041    0.000 3793.453    0.000 layers.py:838(isFree)
               47868957  403.335    0.000 3526.842    0.000 level.py:41(notUsed)
               42656792   72.553    0.000 3427.612    0.000 conv.py:422(forward)
               42656792   82.169    0.000 3325.459    0.000 conv.py:414(_conv_forward)
               45131504 3247.826    0.000 3247.826    0.000 {built-in method tensor}
               42656792 3228.167    0.000 3228.167    0.000 {built-in method conv2d}
               63985188  140.035    0.000 3226.686    0.000 linear.py:92(forward)
             9454172229 2579.251    0.000 3120.376    0.000 layers.py:809(<genexpr>)
             1066419900  310.362    0.000 3021.694    0.000 {built-in method builtins.all}
               63985188  231.670    0.000 3020.192    0.000 functional.py:1669(linear)
             3031967602 2462.936    0.000 2966.412    0.000 layer.py:103(isFree)
             3346190712  935.673    0.000 2845.670    0.000 layers.py:799(<genexpr>)
              746493890 1701.181    0.000 2829.949    0.000 tensor.py:933(grad)
               21761437 1487.925    0.000 2819.700    0.000 levels.py:75(RFS)
               21328396   20.477    0.000 2570.419    0.000 game.py:38(board)
               10664198  243.093    0.000 2459.170    0.000 optimizer.py:167(zero_grad)
               63985188 2124.792    0.000 2124.792    0.000 {built-in method addmm}
             1066419800 1125.209    0.000 1813.784    0.000 layers.py:141(check)
              213283960 1802.721    0.000 1802.721    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
             1066419900 1176.942    0.000 1797.148    0.000 layers.py:113(isDone)
            18236751277 1656.987    0.000 1656.987    0.000 layer.py:99(positions)
              213283960 1525.307    0.000 1525.307    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
             1066419800  992.818    0.000 1482.622    0.000 layers.py:48(check)
             1066419800  979.198    0.000 1480.164    0.000 layers.py:124(check)
               47868957   41.013    0.000 1471.434    0.000 level.py:38(elementsIn)
             1594234909 1425.813    0.000 1425.813    0.000 level.py:32(inverse)
              917121108  463.985    0.000 1384.839    0.000 overrides.py:1070(has_torch_function)
               85313584   67.968    0.000 1358.891    0.000 activation.py:713(forward)
             3908531521 1324.221    0.000 1324.221    0.000 layer.py:154(elements)
              127650552  168.968    0.000 1312.268    0.000 layer.py:77(restart)
               85313584  114.109    0.000 1290.922    0.000 functional.py:1292(leaky_relu)
               85313584 1165.587    0.000 1165.587    0.000 {built-in method torch._C._nn.leaky_relu}
            14387552246 1146.325    0.000 1146.325    0.000 {built-in method builtins.hash}
             1066419800  749.244    0.000 1114.282    0.000 layers.py:23(check)
              106641980 1024.980    0.000 1024.980    0.000 {method 'add' of 'torch._C._TensorBase' objects}
             1870612409  731.580    0.000 1001.328    0.000 layer.py:138(add)
              106641980  957.389    0.000  957.389    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               47868957  443.867    0.000  915.182    0.000 level.py:39(<listcomp>)
               10664198  532.248    0.000  912.600    0.000 collector.py:46(collect)
              106641980  852.095    0.000  852.095    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               15956419  410.716    0.000  810.621    0.000 layers.py:36(reset)
        11551504320/11551504319  729.598    0.000  794.693    0.000 {built-in method builtins.len}
               21761437  373.484    0.000  792.123    0.000 level.py:16(<dictcomp>)
             9608442398  745.249    0.000  745.249    0.000 {method 'random' of '_random.Random' objects}
              106641980  740.312    0.000  740.312    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
             1305686220  452.711    0.000  681.023    0.000 levels.py:31(<genexpr>)
              930236416  440.969    0.000  641.847    0.000 layer.py:134(remove)
             2994109069  566.019    0.000  566.019    0.000 enum.py:352(<genexpr>)
              106641980  560.969    0.000  560.969    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
             8403708648  541.125    0.000  541.125    0.000 layer.py:92(isDead)
               10664198   15.363    0.000  530.076    0.000 loss.py:445(forward)
               47868957  307.723    0.000  515.239    0.000 {built-in method _functools.reduce}
               10664198   59.579    0.000  514.713    0.000 functional.py:2637(mse_loss)
             1898227404  414.760    0.000  510.587    0.000 overrides.py:1083(<genexpr>)
              380095630  173.362    0.000  491.271    0.000 random.py:285(choice)
             6126493923  485.499    0.000  485.499    0.000 {method 'append' of 'list' objects}
               10664198   36.701    0.000  455.595    0.000 exploration.py:47(epsilonGreedy)
               59479193  176.718    0.000  409.924    0.000 random.py:315(sample)
              521324469  278.593    0.000  399.212    0.000 random.py:250(_randbelow_with_getrandbits)
               63985188  382.019    0.000  382.019    0.000 {method 't' of 'torch._C._TensorBase' objects}
               10664198  317.132    0.000  317.132    0.000 {method 'tolist' of 'torch._C._TensorBase' objects}
             2742725032  312.683    0.000  312.683    0.000 layer.py:211(isBlocking)
               10664198  299.261    0.000  299.261    0.000 {built-in method torch._C._nn.mse_loss}
               21328396  295.122    0.000  295.122    0.000 {built-in method sum}
              106642030  125.921    0.000  286.189    0.000 tensor.py:596(__hash__)
             3199259400  273.857    0.000  273.857    0.000 layer.py:86(check)
               10665264  271.399    0.000  271.399    0.000 {built-in method max}
               85313592  270.430    0.000  270.430    0.000 layer.py:186(<listcomp>)
               85313592  254.782    0.000  254.782    0.000 layer.py:187(<listcomp>)
              326421555  232.905    0.000  232.905    0.000 levels.py:85(<listcomp>)
              326421555  230.194    0.000  230.194    0.000 {method 'intersection_update' of 'set' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9578853: <Maze_simple_1> in cluster <dcc> Done

Job <Maze_simple_1> was submitted from host <n-62-30-3> by user <s183905> in cluster <dcc> at Mon Apr 26 20:44:07 2021
Job was executed on host(s) <n-62-20-10>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Tue May  4 16:52:03 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue May  4 16:52:03 2021
Terminated at Wed May  5 16:47:10 2021
Results reported at Wed May  5 16:47:10 2021

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

    CPU time :                                   85896.12 sec.
    Max Memory :                                 2061 MB
    Average Memory :                             2060.78 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14323.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86108 sec.
    Turnaround time :                            763383 sec.

The output (if any) is above this job summary.

