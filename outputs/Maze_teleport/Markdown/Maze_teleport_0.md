
# Parameters

    Name :                      Maze_teleport-0
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


      80286033388 function calls (80004443569 primitive calls) in 86060.13 seconds

##    Ordered by: cumulative time
   List reduced from 487 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86115.990 86115.990 {built-in method builtins.exec}
                      1    1.473    1.473 86115.990 86115.990 <string>:1(<module>)
                      1  219.030  219.030 86114.517 86114.517 main.py:45(teleport)
               10076640   32.322    0.000 34426.962    0.003 agent.py:29(learn)
               10076640  820.332    0.000 29475.923    0.003 learner.py:42(Qlearn)
                5038320   19.868    0.000 22621.094    0.004 game.py:41(step)
                5038320   26.136    0.000 21419.774    0.004 layers.py:718(step)
                5038320  164.830    0.000 20715.210    0.004 agent.py:54(_learn)
                5038320  135.831    0.000 13658.933    0.003 agent.py:117(_learn)
        316810622/35221814 1181.104    0.000 13354.556    0.000 module.py:715(_call_impl)
               10076640   59.454    0.000 12600.917    0.001 grad_mode.py:23(decorate_context)
               25145174   62.566    0.000 12506.989    0.000 network.py:27(forward)
               10076640  315.007    0.000 12431.774    0.001 adam.py:55(step)
               25145174  323.684    0.000 12303.252    0.000 container.py:115(forward)
                5038320  371.307    0.000 11597.951    0.002 layers.py:17(step)
              503832000  766.096    0.000 11184.180    0.000 layer.py:98(move)
               10076640 2279.518    0.000 10751.799    0.001 functional.py:53(adam)
                5038321  662.597    0.000 9760.320    0.002 layers.py:684(update)
               10030214  227.208    0.000 8196.758    0.001 agent.py:49(__call__)
                5038320 3079.725    0.001 7129.507    0.001 agent.py:88(interveen)
               10076640   59.999    0.000 6787.289    0.001 tensor.py:181(backward)
               10076640   33.762    0.000 6727.290    0.001 __init__.py:68(backward)
              503832000 1639.772    0.000 6652.938    0.000 layers.py:735(check)
               10076640 6434.374    0.001 6434.374    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                5038320 3780.782    0.001 6076.152    0.001 replaybuffer.py:22(sample_data)
                5038320 3031.488    0.001 5879.215    0.001 replaybuffer.py:28(teleporter_save_data)
                5038320 2789.668    0.001 5377.716    0.001 agent.py:67(modify)
               50290348   82.898    0.000 4450.610    0.000 conv.py:422(forward)
               50290348   94.260    0.000 4337.405    0.000 conv.py:414(_conv_forward)
               50290348 4226.802    0.000 4226.802    0.000 {built-in method conv2d}
               65358882  137.960    0.000 4001.593    0.000 linear.py:92(forward)
               65358882  243.971    0.000 3802.191    0.000 functional.py:1669(linear)
              503832000  674.199    0.000 3116.823    0.000 layers.py:729(isFree)
                3996214   51.634    0.000 2866.212    0.001 layers.py:740(restart)
               65358882 2741.610    0.000 2741.610    0.000 {built-in method addmm}
             1411495588  743.967    0.000 2627.499    0.000 {built-in method builtins.any}
                5038320   66.693    0.000 2572.926    0.001 agent.py:112(__call__)
              634828374 1630.771    0.000 2551.221    0.000 tensor.py:933(grad)
               40306568 1411.540    0.000 2488.473    0.000 layer.py:167(NoRock_update)
               10076640  228.093    0.000 2487.391    0.000 optimizer.py:167(zero_grad)
                3996214   32.394    0.000 2478.144    0.001 level.py:8(__init__)
               15068534  110.414    0.000 2462.556    0.000 agent.py:59(modify_board)
             3172149554 2020.553    0.000 2442.623    0.000 layer.py:95(isFree)
               40260134 2396.185    0.000 2396.185    0.000 {built-in method cat}
              159893105 2323.530    0.000 2323.530    0.000 {built-in method clone}
              181379520 2258.504    0.000 2258.504    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                5448538  312.203    0.000 2198.972    0.000 levels.py:9(generate)
                5038320   86.167    0.000 1945.239    0.000 replaybuffer.py:18(stacker)
              503832000 1166.182    0.000 1921.343    0.000 layers.py:168(check)
              181379520 1903.743    0.000 1903.743    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               90504056   70.914    0.000 1865.124    0.000 activation.py:713(forward)
               90504056  123.674    0.000 1794.210    0.000 functional.py:1292(leaky_relu)
              539103536  235.729    0.000 1753.523    0.000 {built-in method builtins.all}
               21499259 1667.175    0.000 1667.175    0.000 {built-in method tensor}
               90504056 1658.597    0.000 1658.597    0.000 {built-in method torch._C._nn.leaky_relu}
             2530944380  635.093    0.000 1555.992    0.000 layers.py:690(<genexpr>)
               15068534 1550.350    0.000 1550.350    0.000 {built-in method torch._C._nn.one_hot}
             5537036572  970.799    0.000 1427.608    0.000 enum.py:646(__hash__)
             4498522974 1160.106    0.000 1416.315    0.000 layers.py:700(<genexpr>)
               35271436  183.462    0.000 1335.957    0.000 tensor.py:21(wrapped)
               10076640   10.766    0.000 1276.981    0.000 game.py:37(board)
              826147539  423.134    0.000 1254.001    0.000 overrides.py:1070(has_torch_function)
               90689760 1232.872    0.000 1232.872    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                5038320  712.603    0.000 1192.808    0.000 collector.py:46(collect)
               90689760 1111.460    0.000 1111.460    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               90689760 1022.364    0.000 1022.364    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               90689760  915.785    0.000  915.785    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               10030214  310.117    0.000  877.621    0.000 exploration.py:53(softmaxer)
              503832000  525.897    0.000  843.061    0.000 layers.py:141(check)
              503832100  531.788    0.000  816.420    0.000 layers.py:113(isDone)
             8832032717  778.181    0.000  778.181    0.000 layer.py:91(positions)
               11988642   91.020    0.000  760.517    0.000 level.py:41(notUsed)
              174961639  732.391    0.000  732.391    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               90689760  716.243    0.000  716.243    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                5448538  352.494    0.000  669.254    0.000 levels.py:75(RFS)
              503832000  449.190    0.000  669.060    0.000 layers.py:48(check)
             1620792381  663.410    0.000  663.410    0.000 layer.py:146(elements)
              503832000  427.650    0.000  656.827    0.000 layers.py:124(check)
               10076640   13.515    0.000  574.320    0.000 loss.py:445(forward)
               10076640   56.506    0.000  560.805    0.000 functional.py:2637(mse_loss)
               25191600  558.041    0.000  558.041    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
        5575685065/5575685063  396.330    0.000  541.739    0.000 {built-in method builtins.len}
               65358882  533.618    0.000  533.618    0.000 {method 't' of 'torch._C._TensorBase' objects}
              503832000  339.655    0.000  503.790    0.000 layers.py:23(check)
               30229920  477.036    0.000  477.036    0.000 {built-in method sum}
             1752924393  367.648    0.000  460.768    0.000 overrides.py:1083(<genexpr>)
             5537073187  456.816    0.000  456.816    0.000 {built-in method builtins.hash}
               19931610  169.379    0.000  443.137    0.000 random.py:315(sample)
              771213544  307.195    0.000  417.183    0.000 layer.py:130(add)
              542300316  251.485    0.000  367.577    0.000 layer.py:126(remove)
               50290348   48.645    0.000  360.330    0.000 flatten.py:39(forward)
               10076640  353.211    0.000  353.211    0.000 {built-in method torch._C._nn.mse_loss}
              399242058  335.105    0.000  335.105    0.000 level.py:32(inverse)
             4539526320  334.849    0.000  334.849    0.000 {method 'random' of '_random.Random' objects}
                5040326  331.050    0.000  331.050    0.000 {method 'ne' of 'torch._C._TensorBase' objects}
               31969712   42.490    0.000  326.204    0.000 layer.py:69(restart)
               10078146  314.428    0.000  314.428    0.000 {built-in method max}
               50290348  311.685    0.000  311.685    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               11988642   10.513    0.000  294.603    0.000 level.py:38(elementsIn)
               10030214  285.169    0.000  285.169    0.000 {built-in method multinomial}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9550914: <Maze_teleport_0> in cluster <dcc> Done

Job <Maze_teleport_0> was submitted from host <n-62-30-4> by user <s183905> in cluster <dcc> at Tue Apr 20 16:21:50 2021
Job was executed on host(s) <n-62-20-3>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sun Apr 25 07:09:50 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun Apr 25 07:09:50 2021
Terminated at Mon Apr 26 07:05:14 2021
Results reported at Mon Apr 26 07:05:14 2021

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

    CPU time :                                   85894.98 sec.
    Max Memory :                                 2678 MB
    Average Memory :                             2673.56 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13706.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86124 sec.
    Turnaround time :                            485004 sec.

The output (if any) is above this job summary.

