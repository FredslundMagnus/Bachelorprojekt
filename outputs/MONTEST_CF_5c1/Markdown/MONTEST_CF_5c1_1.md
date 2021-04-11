
# Parameters

    Name :                      MONTEST_CF_5c1-1
    Main :                      CFagent
    Level :                     Levels.MonsterLevel
    Hours :                     22.0
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
    Cf convert :                5
    Counterfacts :              1
    Topn :                      7
    Minutes used :              1315 minutes.
    Hours used :                21 hours.

# Profiling


      63703001888 function calls (63405451505 primitive calls) in 78909.07 seconds

##    Ordered by: cumulative time
   List reduced from 505 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 78909.070 78909.070 {built-in method builtins.exec}
                      1    4.847    4.847 78909.070 78909.070 <string>:1(<module>)
                      1  211.238  211.238 78904.223 78904.223 main.py:95(CFagent)
                8716974   33.270    0.000 22026.805    0.003 agent.py:29(learn)
                2905658   14.112    0.000 21592.561    0.007 game.py:41(step)
                2905658   15.879    0.000 21022.798    0.007 layers.py:710(step)
                8716974  556.771    0.000 17916.429    0.002 learner.py:42(Qlearn)
                2905659  460.729    0.000 11162.889    0.004 layers.py:676(update)
        332029943/34481251 1380.220    0.000 11156.816    0.000 module.py:866(_call_impl)
               25764277   70.030    0.000 10478.607    0.000 network.py:24(forward)
               25764277  329.204    0.000 10236.688    0.000 container.py:117(forward)
                2905658  273.998    0.000 9817.622    0.003 layers.py:17(step)
                2905658 1559.436    0.001 9698.154    0.003 agent.py:217(counterfact)
              279779065  849.454    0.000 9513.522    0.000 layer.py:98(move)
                2905658  324.751    0.000 8555.051    0.003 agent.py:54(_learn)
                2905658  320.579    0.000 7869.580    0.003 agent.py:209(_learn)
                8716974   75.760    0.000 6935.834    0.001 optimizer.py:84(wrapper)
                8716974   40.015    0.000 6600.434    0.001 grad_mode.py:24(decorate_context)
                8716974  277.633    0.000 6475.939    0.001 adam.py:55(step)
                2905658 3544.717    0.001 6211.946    0.002 replaybuffer.py:28(teleporter_save_data)
              279779065  607.010    0.000 6079.678    0.000 layers.py:727(check)
                8716974 1363.243    0.000 5886.128    0.001 _functional.py:53(adam)
                9970233   83.766    0.000 5780.702    0.001 layers.py:731(restart)
                8523614  232.975    0.000 5613.396    0.001 agent.py:49(__call__)
                2905658   90.921    0.000 5551.029    0.002 agent.py:117(_learn)
                9970233   42.142    0.000 4894.936    0.000 level.py:8(__init__)
                8716974   36.535    0.000 4687.725    0.001 tensor.py:195(backward)
                8716974   35.292    0.000 4649.884    0.001 __init__.py:68(backward)
                2905658 3595.673    0.001 4621.060    0.002 replaybuffer.py:22(sample_data)
                9970233  783.843    0.000 4475.453    0.000 levels.py:418(generate)
                2905658 2538.741    0.001 4444.156    0.002 agent.py:88(interveen)
                8716974 4439.361    0.001 4439.361    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2905658 3291.538    0.001 4195.910    0.001 replaybuffer.py:49(sample_data)
              279779065 2231.780    0.000 3950.007    0.000 layers.py:531(check)
                2712373   58.778    0.000 3808.365    0.001 agent.py:172(choose_action)
               51528554  117.078    0.000 3755.972    0.000 conv.py:398(forward)
               34867902 2465.224    0.000 3645.416    0.000 layer.py:151(update)
               51528554   76.556    0.000 3583.485    0.000 conv.py:390(_conv_forward)
               51528554 3506.929    0.000 3506.929    0.000 {built-in method conv2d}
               42657705 3074.805    0.000 3074.805    0.000 {built-in method tensor}
               49851165  474.043    0.000 2925.918    0.000 level.py:41(notUsed)
               35927865   26.025    0.000 2913.846    0.000 game.py:37(board)
               71481515  153.565    0.000 2901.020    0.000 linear.py:93(forward)
              280789397 2754.592    0.000 2754.592    0.000 {built-in method clone}
               71481515   64.528    0.000 2672.620    0.000 functional.py:1737(linear)
               71481515 2592.825    0.000 2592.825    0.000 {built-in method torch._C._nn.linear}
                2905658 1588.570    0.001 2320.801    0.001 agent.py:67(modify)
              289677055  229.609    0.000 2056.122    0.000 {built-in method builtins.any}
              279683417  377.559    0.000 1981.029    0.000 layers.py:721(isFree)
             2001224043  603.240    0.000 1827.308    0.000 layers.py:692(<genexpr>)
             6423361474 1160.487    0.000 1676.594    0.000 enum.py:646(__hash__)
               43391510 1653.625    0.000 1653.625    0.000 {built-in method cat}
                2905658  830.384    0.000 1624.608    0.001 replaybuffer.py:55(CF_save_data)
             1534347890 1339.615    0.000 1603.470    0.000 layer.py:95(isFree)
               97245792   82.220    0.000 1549.416    0.000 activation.py:713(forward)
               11429272   72.019    0.000 1498.839    0.000 agent.py:59(modify_board)
               97245792   86.847    0.000 1467.197    0.000 functional.py:1364(leaky_relu)
               97245792 1363.124    0.000 1363.124    0.000 {built-in method torch._C._nn.leaky_relu}
                2905658   51.900    0.000 1350.501    0.000 agent.py:168(__call__)
                2905658   47.675    0.000 1278.280    0.000 agent.py:112(__call__)
               49851165   42.388    0.000 1261.254    0.000 level.py:38(elementsIn)
              162716848 1147.926    0.000 1147.926    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              286771396  692.912    0.000 1113.224    0.000 layers.py:568(isDead)
                8716974  190.108    0.000 1043.991    0.000 optimizer.py:189(zero_grad)
              162716848 1016.722    0.000 1016.722    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               11429272  982.712    0.000  982.712    0.000 {built-in method torch._C._nn.one_hot}
              279779065  683.236    0.000  962.638    0.000 layers.py:71(check)
               55662481  350.531    0.000  903.369    0.000 random.py:315(sample)
             2126846340  806.773    0.000  806.773    0.000 level.py:32(inverse)
                2905658   55.033    0.000  801.744    0.000 replaybuffer.py:18(stacker)
               49851165  399.465    0.000  799.677    0.000 level.py:39(<listcomp>)
               59821398   78.611    0.000  779.659    0.000 layer.py:69(restart)
             2251182368  747.786    0.000  747.786    0.000 layer.py:146(elements)
                2712373  634.086    0.000  745.757    0.000 agent.py:183(convert_values)
              388936580  147.992    0.000  719.813    0.000 random.py:244(randint)
                2905658   53.117    0.000  689.202    0.000 replaybuffer.py:45(stacker)
              901925843  476.014    0.000  686.149    0.000 random.py:250(_randbelow_with_getrandbits)
               81358424  672.768    0.000  672.768    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              649206950  458.885    0.000  642.281    0.000 layer.py:126(remove)
             1102277063  462.679    0.000  621.618    0.000 layer.py:130(add)
              295124327  610.871    0.000  610.871    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               81358424  591.229    0.000  591.229    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              388936580  241.602    0.000  571.821    0.000 random.py:200(randrange)
                8523614  211.003    0.000  560.569    0.000 exploration.py:53(softmaxer)
                9970333  277.277    0.000  544.203    0.000 layers.py:30(reset)
               81358424  538.597    0.000  538.597    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               81358424  533.275    0.000  533.275    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
             6423394657  516.113    0.000  516.113    0.000 {built-in method builtins.hash}
              569509052  398.452    0.000  494.804    0.000 tensor.py:906(grad)
              279779065  332.375    0.000  483.818    0.000 layers.py:42(check)
             5028410228  474.693    0.000  474.693    0.000 layer.py:91(positions)
                2905658  266.327    0.000  453.238    0.000 collector.py:53(collect)
              279779065  151.507    0.000  441.059    0.000 layers.py:565(<listcomp>)
        4748994953/4748994950  362.712    0.000  422.822    0.000 {built-in method builtins.len}
             2153571782  421.975    0.000  421.975    0.000 enum.py:352(<genexpr>)
               49851165  258.156    0.000  419.189    0.000 {built-in method _functools.reduce}
               81358424  404.623    0.000  404.623    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                8716974   12.266    0.000  382.049    0.000 loss.py:527(forward)
              290565900   67.552    0.000  381.173    0.000 {built-in method builtins.all}
                8716974   34.871    0.000  369.782    0.000 functional.py:2898(mse_loss)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-16>
Subject: Job 9507474: <MONTEST_CF_5c1_1> in cluster <dcc> Done

Job <MONTEST_CF_5c1_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sat Apr 10 02:36:49 2021
Job was executed on host(s) <n-62-20-16>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sat Apr 10 02:46:12 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat Apr 10 02:46:12 2021
Terminated at Sun Apr 11 00:41:26 2021
Results reported at Sun Apr 11 00:41:26 2021

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

    CPU time :                                   78716.60 sec.
    Max Memory :                                 9038 MB
    Average Memory :                             6316.25 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               7346.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   78913 sec.
    Turnaround time :                            79477 sec.

The output (if any) is above this job summary.

