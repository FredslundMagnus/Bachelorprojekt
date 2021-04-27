
# Parameters

    Name :                      Maze_teleport-2
    Main :                      teleport
    Level :                     Levels.Maze
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


      74623247202 function calls (74352307675 primitive calls) in 86054.50 seconds

##    Ordered by: cumulative time
   List reduced from 486 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86111.392 86111.392 {built-in method builtins.exec}
                      1    1.759    1.759 86111.391 86111.391 <string>:1(<module>)
                      1  327.717  327.717 86109.632 86109.632 main.py:45(teleport)
                9723548   53.360    0.000 31436.801    0.003 agent.py:29(learn)
                9723548  772.698    0.000 26037.380    0.003 learner.py:42(Qlearn)
                4861774   32.303    0.000 25781.485    0.005 game.py:41(step)
                4861774   37.567    0.000 24470.250    0.005 layers.py:718(step)
                4861774  224.611    0.000 18898.620    0.004 agent.py:54(_learn)
                4861774  504.364    0.000 13695.650    0.003 layers.py:17(step)
              486177400  823.729    0.000 13141.716    0.000 layer.py:98(move)
        304860865/33922349 1345.457    0.000 12950.781    0.000 module.py:715(_call_impl)
                4861774  182.642    0.000 12457.681    0.003 agent.py:117(_learn)
               24198801   67.987    0.000 11969.760    0.000 network.py:27(forward)
               24198801  362.050    0.000 11726.576    0.000 container.py:115(forward)
                4861775  775.986    0.000 10676.155    0.002 layers.py:684(update)
                9723548   85.933    0.000 9926.667    0.001 grad_mode.py:23(decorate_context)
                9723548  371.298    0.000 9691.867    0.001 adam.py:55(step)
                4861774 7063.863    0.001 9458.581    0.002 replaybuffer.py:22(sample_data)
                9613479  305.487    0.000 8124.786    0.001 agent.py:49(__call__)
                9723548 1799.276    0.000 7927.568    0.001 functional.py:53(adam)
              486177400 1753.855    0.000 7424.742    0.000 layers.py:735(check)
                9723548   71.701    0.000 6524.403    0.001 tensor.py:181(backward)
                9723548   54.921    0.000 6452.703    0.001 __init__.py:68(backward)
                9723548 6119.167    0.001 6119.167    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                4861774 2159.711    0.000 5943.371    0.001 agent.py:88(interveen)
                4861774 2571.348    0.001 5173.231    0.001 agent.py:67(modify)
               48397602   90.890    0.000 4483.423    0.000 conv.py:422(forward)
               48397602  117.457    0.000 4337.348    0.000 conv.py:414(_conv_forward)
               48397602 4198.689    0.000 4198.689    0.000 {built-in method conv2d}
              486177400  680.400    0.000 4144.357    0.000 layers.py:729(isFree)
                4861774 2151.851    0.000 3894.317    0.001 replaybuffer.py:28(teleporter_save_data)
               62872855  144.862    0.000 3680.297    0.000 linear.py:92(forward)
             2940085332 2996.275    0.000 3463.958    0.000 layer.py:95(isFree)
               62872855  253.619    0.000 3457.143    0.000 functional.py:1669(linear)
               38894200 1874.833    0.000 3325.903    0.000 layer.py:167(NoRock_update)
                3663110   59.874    0.000 3006.540    0.001 layers.py:740(restart)
             1361838010  771.753    0.000 2695.736    0.000 {built-in method builtins.any}
                3663110   36.542    0.000 2589.122    0.001 level.py:8(__init__)
               14475253  128.962    0.000 2514.211    0.000 agent.py:59(modify_board)
               62872855 2472.208    0.000 2472.208    0.000 {built-in method addmm}
                4861774   94.259    0.000 2448.518    0.001 agent.py:112(__call__)
              612583578 1496.372    0.000 2444.281    0.000 tensor.py:933(grad)
               38784123 2350.969    0.000 2350.969    0.000 {built-in method cat}
                4995491  328.237    0.000 2259.846    0.000 levels.py:9(generate)
              486177400 1352.072    0.000 2168.472    0.000 layers.py:168(check)
                9723548  205.362    0.000 2118.498    0.000 optimizer.py:167(zero_grad)
                4861774  102.058    0.000 1951.343    0.000 replaybuffer.py:18(stacker)
               20758070 1837.433    0.000 1837.433    0.000 {built-in method tensor}
               14475253 1626.260    0.000 1626.260    0.000 {built-in method torch._C._nn.one_hot}
              175023864 1585.792    0.000 1585.792    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               87071656   87.966    0.000 1567.672    0.000 activation.py:713(forward)
             5316649583 1034.173    0.000 1520.982    0.000 enum.py:646(__hash__)
              520213674  163.250    0.000 1513.856    0.000 {built-in method builtins.all}
               87071656  135.447    0.000 1479.706    0.000 functional.py:1292(leaky_relu)
                9723548   19.742    0.000 1476.838    0.000 game.py:37(board)
              123211838 1462.589    0.000 1462.589    0.000 {built-in method clone}
             4342629510 1163.274    0.000 1436.619    0.000 layers.py:700(<genexpr>)
               34036174  201.248    0.000 1431.854    0.000 tensor.py:21(wrapped)
             1468359084  385.196    0.000 1390.124    0.000 layers.py:690(<genexpr>)
               87071656 1332.253    0.000 1332.253    0.000 {built-in method torch._C._nn.leaky_relu}
              175023864 1296.226    0.000 1296.226    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              797003668  431.483    0.000 1292.099    0.000 overrides.py:1070(has_torch_function)
             1484056978  975.876    0.000  975.876    0.000 layer.py:146(elements)
              486177500  655.009    0.000  964.139    0.000 layers.py:113(isDone)
                4861774  540.883    0.000  936.235    0.000 collector.py:46(collect)
               87511932  905.609    0.000  905.609    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                9613479  304.806    0.000  905.387    0.000 exploration.py:53(softmaxer)
               87511932  884.312    0.000  884.312    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              486177400  541.613    0.000  860.023    0.000 layers.py:141(check)
             8493931625  854.993    0.000  854.993    0.000 layer.py:91(positions)
              486177400  588.234    0.000  826.026    0.000 layers.py:48(check)
              486177400  546.911    0.000  818.216    0.000 layers.py:124(check)
               10989330   95.293    0.000  771.961    0.000 level.py:41(notUsed)
               87511932  756.325    0.000  756.325    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                4995491  363.065    0.000  683.929    0.000 levels.py:75(RFS)
               87511932  671.818    0.000  671.818    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                9723548   22.311    0.000  653.059    0.000 loss.py:445(forward)
                9723548   80.034    0.000  630.747    0.000 functional.py:2637(mse_loss)
        5385510804/5385510802  409.252    0.000  550.838    0.000 {built-in method builtins.len}
               18515866  212.017    0.000  546.977    0.000 random.py:315(sample)
              486177400  365.065    0.000  544.448    0.000 layers.py:23(check)
               24308870  502.526    0.000  502.526    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               87511932  497.462    0.000  497.462    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
             5316684974  486.816    0.000  486.816    0.000 {built-in method builtins.hash}
             1690915404  384.923    0.000  478.191    0.000 overrides.py:1083(<genexpr>)
              703821058  341.812    0.000  473.173    0.000 layer.py:130(add)
              137687091  448.214    0.000  448.214    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               62872855  444.032    0.000  444.032    0.000 {method 't' of 'torch._C._TensorBase' objects}
                4863696  439.509    0.000  439.509    0.000 {method 'ne' of 'torch._C._TensorBase' objects}
              490954858  286.873    0.000  419.339    0.000 layer.py:126(remove)
               29170644  393.321    0.000  393.321    0.000 {built-in method sum}
             4380458374  367.144    0.000  367.144    0.000 {method 'random' of '_random.Random' objects}
                9723548  355.433    0.000  355.433    0.000 {built-in method torch._C._nn.mse_loss}
               29304880   48.311    0.000  347.387    0.000 layer.py:69(restart)
              365984469  340.685    0.000  340.685    0.000 level.py:32(inverse)
                9724995  312.844    0.000  312.844    0.000 {built-in method max}
                4861774   28.682    0.000  309.460    0.000 exploration.py:47(epsilonGreedy)
               10989330   11.624    0.000  299.583    0.000 level.py:38(elementsIn)
                9613479  299.027    0.000  299.027    0.000 {built-in method multinomial}
             2584886284  295.764    0.000  295.764    0.000 layer.py:203(isBlocking)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9550916: <Maze_teleport_2> in cluster <dcc> Done

Job <Maze_teleport_2> was submitted from host <n-62-30-4> by user <s183905> in cluster <dcc> at Tue Apr 20 16:21:51 2021
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sun Apr 25 07:13:35 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun Apr 25 07:13:35 2021
Terminated at Mon Apr 26 07:08:53 2021
Results reported at Mon Apr 26 07:08:53 2021

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

    CPU time :                                   85903.01 sec.
    Max Memory :                                 2680 MB
    Average Memory :                             2677.17 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13704.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86222 sec.
    Turnaround time :                            485222 sec.

The output (if any) is above this job summary.

