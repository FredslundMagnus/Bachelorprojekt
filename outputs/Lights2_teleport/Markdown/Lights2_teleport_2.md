
# Parameters

    Name :                      Lights2_teleport-2
    Main :                      teleport
    Level :                     Levels.Causal4
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


      87962941760 function calls (87707040949 primitive calls) in 86105.41 seconds

##    Ordered by: cumulative time
   List reduced from 483 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86105.415 86105.415 {built-in method builtins.exec}
                      1    1.606    1.606 86105.414 86105.414 <string>:1(<module>)
                      1  295.180  295.180 86103.808 86103.808 main.py:45(teleport)
                4582337   29.385    0.000 30822.086    0.007 game.py:41(step)
                4582337   35.743    0.000 29575.959    0.006 layers.py:718(step)
                9164674   46.175    0.000 27989.066    0.003 agent.py:29(learn)
                9164674  690.947    0.000 23373.142    0.003 learner.py:42(Qlearn)
                4582337  464.115    0.000 19354.537    0.004 layers.py:17(step)
              458233700 1393.936    0.000 18847.388    0.000 layer.py:98(move)
                4582337  180.372    0.000 16887.666    0.004 agent.py:54(_learn)
              458233700 2154.978    0.000 11561.634    0.000 layers.py:735(check)
        287916903/32017103 1208.924    0.000 11428.047    0.000 module.py:715(_call_impl)
                4582337  144.342    0.000 11030.158    0.002 agent.py:117(_learn)
               22852429   65.013    0.000 10591.882    0.000 network.py:27(forward)
               22852429  297.612    0.000 10367.596    0.000 container.py:115(forward)
                4582338  706.769    0.000 10132.073    0.002 layers.py:684(update)
                9164674   75.403    0.000 9123.512    0.001 grad_mode.py:23(decorate_context)
                9164674  340.167    0.000 8922.894    0.001 adam.py:55(step)
                4582337 6606.704    0.001 8779.821    0.002 replaybuffer.py:22(sample_data)
                9164674 1641.094    0.000 7272.657    0.001 functional.py:53(adam)
                9105418  268.519    0.000 7120.292    0.001 agent.py:49(__call__)
                9164674   59.373    0.000 5708.390    0.001 tensor.py:181(backward)
                9164674   42.641    0.000 5649.017    0.001 __init__.py:68(backward)
                4582337 2261.931    0.000 5640.113    0.001 agent.py:88(interveen)
                9164674 5366.772    0.001 5366.772    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
              458233700  893.656    0.000 4939.063    0.000 layers.py:729(isFree)
                4582337 2374.716    0.001 4639.642    0.001 agent.py:67(modify)
                4582337 2311.066    0.001 4159.072    0.001 replaybuffer.py:28(teleporter_save_data)
               45823380 2430.777    0.000 4057.920    0.000 layer.py:151(update)
             3808168736 3378.912    0.000 4045.407    0.000 layer.py:95(isFree)
               45704858   87.617    0.000 3882.615    0.000 conv.py:422(forward)
               45704858  107.414    0.000 3755.962    0.000 conv.py:414(_conv_forward)
               45704858 3630.274    0.000 3630.274    0.000 {built-in method conv2d}
               59392613  137.058    0.000 3280.413    0.000 linear.py:92(forward)
               59392613  225.394    0.000 3071.929    0.000 functional.py:1669(linear)
             1282975542  789.885    0.000 2952.355    0.000 {built-in method builtins.any}
              577374516 1398.070    0.000 2313.233    0.000 tensor.py:933(grad)
             8551141487 1571.493    0.000 2273.888    0.000 enum.py:646(__hash__)
                4582337   83.237    0.000 2207.017    0.000 agent.py:112(__call__)
               59392613 2174.651    0.000 2174.651    0.000 {built-in method addmm}
               13687755  108.662    0.000 2152.868    0.000 agent.py:59(modify_board)
               36599440 2130.324    0.000 2130.324    0.000 {built-in method cat}
                9164674  190.684    0.000 1992.026    0.000 optimizer.py:167(zero_grad)
              458233700 1442.553    0.000 1866.878    0.000 layers.py:77(check)
               19581428 1796.098    0.000 1796.098    0.000 {built-in method tensor}
                4582337   94.107    0.000 1784.925    0.000 replaybuffer.py:18(stacker)
              458233700 1169.113    0.000 1753.704    0.000 layers.py:286(check)
                4307580   58.223    0.000 1729.282    0.000 layers.py:740(restart)
             4993188420 1422.607    0.000 1697.002    0.000 layers.py:700(<genexpr>)
              458233700  943.884    0.000 1538.755    0.000 layers.py:246(check)
              132203504 1534.732    0.000 1534.732    0.000 {built-in method clone}
                9164674   18.376    0.000 1467.493    0.000 game.py:37(board)
              164964132 1463.112    0.000 1463.112    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               82245042   78.497    0.000 1412.902    0.000 activation.py:713(forward)
               13687755 1388.510    0.000 1388.510    0.000 {built-in method torch._C._nn.one_hot}
               82245042  109.919    0.000 1334.404    0.000 functional.py:1292(leaky_relu)
              490312785  246.940    0.000 1304.914    0.000 {built-in method builtins.all}
               32078985  184.991    0.000 1256.155    0.000 tensor.py:21(wrapped)
              751327360  428.542    0.000 1247.350    0.000 overrides.py:1070(has_torch_function)
                4307580   28.605    0.000 1226.850    0.000 level.py:8(__init__)
               82245042 1213.294    0.000 1213.294    0.000 {built-in method torch._C._nn.leaky_relu}
              164964132 1205.453    0.000 1205.453    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
             2489851880  682.932    0.000 1091.607    0.000 layers.py:690(<genexpr>)
             1411333527 1076.650    0.000 1076.650    0.000 layer.py:146(elements)
              458233700  851.637    0.000 1069.302    0.000 layers.py:62(check)
            11012926469 1024.509    0.000 1024.509    0.000 layer.py:91(positions)
                4307580  155.193    0.000  940.794    0.000 levels.py:199(generate)
                4582337  500.764    0.000  865.304    0.000 collector.py:46(collect)
               82482066  839.794    0.000  839.794    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               82482066  788.783    0.000  788.783    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                9105418  268.345    0.000  772.414    0.000 exploration.py:53(softmaxer)
              458233700  493.120    0.000  769.894    0.000 layers.py:273(check)
              458233700  478.461    0.000  755.530    0.000 layers.py:313(check)
             8551174862  702.402    0.000  702.402    0.000 {built-in method builtins.hash}
               82482066  698.158    0.000  698.158    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              458233700  477.459    0.000  683.379    0.000 layers.py:48(check)
                8615160   77.388    0.000  634.285    0.000 level.py:41(notUsed)
               82482066  610.120    0.000  610.120    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                9164674   20.563    0.000  561.647    0.000 loss.py:445(forward)
        6094800548/6094800546  423.253    0.000  555.989    0.000 {built-in method builtins.len}
                9164674   70.042    0.000  541.084    0.000 functional.py:2637(mse_loss)
              458233700  344.298    0.000  509.590    0.000 layers.py:23(check)
              145891259  460.040    0.000  460.040    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
             1594125408  368.003    0.000  458.128    0.000 overrides.py:1083(<genexpr>)
               82482066  456.248    0.000  456.248    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               13197497  176.010    0.000  455.922    0.000 random.py:315(sample)
               22911685  450.206    0.000  450.206    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               43075800   61.939    0.000  429.374    0.000 layer.py:69(restart)
             5058075777  421.358    0.000  421.358    0.000 {method 'random' of '_random.Random' objects}
              660810011  301.987    0.000  410.970    0.000 layer.py:130(add)
               59392613  400.872    0.000  400.872    0.000 {method 't' of 'torch._C._TensorBase' objects}
             3064775941  378.571    0.000  378.571    0.000 layer.py:203(isBlocking)
                4584157  359.514    0.000  359.514    0.000 {method 'ne' of 'torch._C._TensorBase' objects}
               27494022  355.846    0.000  355.846    0.000 {built-in method sum}
              401426752  238.104    0.000  354.469    0.000 layer.py:126(remove)
                9164674  306.858    0.000  306.858    0.000 {built-in method torch._C._nn.mse_loss}
                4582337   25.884    0.000  283.464    0.000 exploration.py:47(epsilonGreedy)
             4539262200  274.395    0.000  274.395    0.000 layer.py:84(isDead)
                9166042  266.872    0.000  266.872    0.000 {built-in method max}
               45704858   38.940    0.000  260.934    0.000 flatten.py:39(forward)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9550895: <Lights2_teleport_2> in cluster <dcc> Done

Job <Lights2_teleport_2> was submitted from host <n-62-30-4> by user <s183905> in cluster <dcc> at Tue Apr 20 16:21:48 2021
Job was executed on host(s) <n-62-20-12>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Wed Apr 21 14:05:31 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed Apr 21 14:05:31 2021
Terminated at Thu Apr 22 14:00:41 2021
Results reported at Thu Apr 22 14:00:41 2021

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

    CPU time :                                   85900.94 sec.
    Max Memory :                                 2682 MB
    Average Memory :                             2679.47 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13702.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86111 sec.
    Turnaround time :                            164333 sec.

The output (if any) is above this job summary.

