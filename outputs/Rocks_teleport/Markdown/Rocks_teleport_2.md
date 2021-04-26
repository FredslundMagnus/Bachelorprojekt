
# Parameters

    Name :                      Rocks_teleport-2
    Main :                      teleport
    Level :                     Levels.Rocks
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


      54862984850 function calls (54660591527 primitive calls) in 86111.11 seconds

##    Ordered by: cumulative time
   List reduced from 470 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86111.113 86111.113 {built-in method builtins.exec}
                      1    1.540    1.540 86111.113 86111.113 <string>:1(<module>)
                      1  335.475  335.475 86109.573 86109.573 main.py:45(teleport)
                3614778   27.389    0.000 28845.290    0.008 game.py:41(step)
                3614778   34.331    0.000 27646.773    0.008 layers.py:718(step)
                7229556   54.612    0.000 26457.929    0.004 agent.py:29(learn)
                7229556  708.496    0.000 21542.196    0.003 learner.py:42(Qlearn)
                3614778  424.731    0.000 17398.582    0.005 layers.py:17(step)
              361477800 1157.039    0.000 16935.084    0.000 layer.py:98(move)
                3614778  246.998    0.000 15886.684    0.004 agent.py:54(_learn)
              361477800 1131.430    0.000 11692.394    0.000 layers.py:735(check)
        227692820/25300508 1169.826    0.000 11522.204    0.000 module.py:715(_call_impl)
               18070952   73.316    0.000 10640.554    0.001 network.py:27(forward)
                3614778  199.049    0.000 10487.788    0.003 agent.py:117(_learn)
               18070952  292.249    0.000 10395.449    0.001 container.py:115(forward)
                3614779  635.264    0.000 10152.994    0.003 layers.py:684(update)
              361477800 7510.994    0.000 8664.836    0.000 layers.py:77(check)
                3614778 6227.912    0.002 8468.231    0.002 replaybuffer.py:22(sample_data)
                7229556   79.102    0.000 7928.028    0.001 grad_mode.py:23(decorate_context)
                7229556  323.413    0.000 7701.334    0.001 adam.py:55(step)
                7226618  320.557    0.000 7366.996    0.001 agent.py:49(__call__)
                3614778 3549.585    0.001 7040.912    0.002 agent.py:88(interveen)
                3614778 3805.167    0.001 6762.764    0.002 replaybuffer.py:28(teleporter_save_data)
                7229556 1427.140    0.000 6264.093    0.001 functional.py:53(adam)
                7229556   66.382    0.000 5399.947    0.001 tensor.py:181(backward)
                7229556   45.844    0.000 5333.565    0.001 __init__.py:68(backward)
                7229556 5022.442    0.001 5022.442    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3614778 2360.898    0.001 4681.632    0.001 agent.py:67(modify)
               36141904   80.638    0.000 4117.971    0.000 conv.py:422(forward)
               36141904  116.285    0.000 4000.100    0.000 conv.py:414(_conv_forward)
               36141904 3867.507    0.000 3867.507    0.000 {built-in method conv2d}
                9929830  106.118    0.000 3851.602    0.000 layers.py:740(restart)
              361477800  388.688    0.000 3331.695    0.000 layers.py:729(isFree)
               18073895 2229.217    0.000 3301.191    0.000 layer.py:151(update)
               46983300  128.487    0.000 3251.436    0.000 linear.py:92(forward)
               46983300  222.649    0.000 3058.326    0.000 functional.py:1669(linear)
             1511417575 2665.807    0.000 2943.008    0.000 layer.py:95(isFree)
                9929830   51.203    0.000 2679.024    0.000 level.py:8(__init__)
              202086716 2379.959    0.000 2379.959    0.000 {built-in method clone}
               10841396  125.629    0.000 2329.304    0.000 agent.py:59(modify_board)
                3614778  101.372    0.000 2257.974    0.001 agent.py:112(__call__)
                9929830  292.402    0.000 2255.075    0.000 levels.py:95(generate)
               46983300 2191.143    0.000 2191.143    0.000 {built-in method addmm}
               28915286 2184.559    0.000 2184.559    0.000 {built-in method cat}
              455462082 1154.487    0.000 1923.706    0.000 tensor.py:933(grad)
                3614778  108.711    0.000 1864.888    0.001 replaybuffer.py:18(stacker)
                7229556  161.189    0.000 1675.151    0.000 optimizer.py:167(zero_grad)
             1005806525  519.864    0.000 1672.714    0.000 {built-in method builtins.any}
               15515994 1551.640    0.000 1551.640    0.000 {built-in method tensor}
               10841396 1519.629    0.000 1519.629    0.000 {built-in method torch._C._nn.one_hot}
               19859660  188.722    0.000 1428.029    0.000 level.py:41(notUsed)
               65054252   83.434    0.000 1358.747    0.000 activation.py:713(forward)
               65054252  126.000    0.000 1275.313    0.000 functional.py:1292(leaky_relu)
              130132008 1258.962    0.000 1258.962    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               25305288  196.365    0.000 1235.547    0.000 tensor.py:21(wrapped)
                7229556   17.420    0.000 1232.565    0.000 game.py:37(board)
              386783188  132.478    0.000 1229.602    0.000 {built-in method builtins.all}
              361477800  867.793    0.000 1214.645    0.000 layers.py:62(check)
             3903664698  812.476    0.000 1188.764    0.000 enum.py:646(__hash__)
               65054252 1138.839    0.000 1138.839    0.000 {built-in method torch._C._nn.leaky_relu}
             1105013325  303.745    0.000 1126.786    0.000 layers.py:690(<genexpr>)
              592816042  355.283    0.000 1072.847    0.000 overrides.py:1070(has_torch_function)
               49649150  130.418    0.000 1046.398    0.000 layer.py:69(restart)
              130132008 1001.197    0.000 1001.197    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
             2756112811  852.680    0.000  852.680    0.000 layer.py:146(elements)
             1365756520  607.094    0.000  838.129    0.000 layer.py:130(add)
                7226618  289.586    0.000  807.397    0.000 exploration.py:53(softmaxer)
              361477900  546.795    0.000  787.000    0.000 layers.py:113(isDone)
              671655857  411.052    0.000  785.388    0.000 layer.py:126(remove)
                3614778  433.132    0.000  759.314    0.000 collector.py:46(collect)
               65066004  742.773    0.000  742.773    0.000 {method 'add' of 'torch._C._TensorBase' objects}
             2109288420  574.735    0.000  731.802    0.000 layers.py:700(<genexpr>)
               13544608  263.185    0.000  717.653    0.000 random.py:315(sample)
               65066004  686.959    0.000  686.959    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              212928112  680.908    0.000  680.908    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               65066004  595.282    0.000  595.282    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                9929930  267.640    0.000  566.398    0.000 layers.py:36(reset)
               19859660   21.639    0.000  558.899    0.000 level.py:38(elementsIn)
                7229556   20.654    0.000  555.967    0.000 loss.py:445(forward)
             5099735132  555.430    0.000  555.430    0.000 layer.py:91(positions)
                7229556   68.571    0.000  535.313    0.000 functional.py:2637(mse_loss)
              546140650  528.902    0.000  528.902    0.000 level.py:32(inverse)
               65066004  526.536    0.000  526.536    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              361477800  284.186    0.000  430.037    0.000 layers.py:23(check)
             1257919950  332.485    0.000  414.589    0.000 overrides.py:1083(<genexpr>)
               18073890  407.699    0.000  407.699    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               65066004  405.385    0.000  405.385    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               46983300  390.806    0.000  390.806    0.000 {method 't' of 'torch._C._TensorBase' objects}
             4222366165  388.143    0.000  388.143    0.000 {method 'append' of 'list' objects}
                3616222  377.957    0.000  377.957    0.000 {method 'ne' of 'torch._C._TensorBase' objects}
             3903691089  376.294    0.000  376.294    0.000 {built-in method builtins.hash}
        2363159506/2363159504  242.871    0.000  361.237    0.000 {built-in method builtins.len}
              361477800  146.339    0.000  356.143    0.000 layers.py:104(<listcomp>)
                9929830  160.078    0.000  347.147    0.000 level.py:16(<dictcomp>)
               19859660  165.171    0.000  339.920    0.000 level.py:39(<listcomp>)
               21688668  333.354    0.000  333.354    0.000 {built-in method sum}
                3614778   25.581    0.000  301.257    0.000 exploration.py:47(epsilonGreedy)
              671655857  300.679    0.000  300.679    0.000 {method 'remove' of 'list' objects}
              429029779  198.954    0.000  300.597    0.000 random.py:250(_randbelow_with_getrandbits)
                7229556  298.352    0.000  298.352    0.000 {built-in method torch._C._nn.mse_loss}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9550919: <Rocks_teleport_2> in cluster <dcc> Done

Job <Rocks_teleport_2> was submitted from host <n-62-30-4> by user <s183905> in cluster <dcc> at Tue Apr 20 16:21:51 2021
Job was executed on host(s) <n-62-20-12>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sun Apr 25 19:20:04 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun Apr 25 19:20:04 2021
Terminated at Mon Apr 26 19:15:21 2021
Results reported at Mon Apr 26 19:15:21 2021

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

    CPU time :                                   85903.57 sec.
    Max Memory :                                 2677 MB
    Average Memory :                             2673.21 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13707.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86118 sec.
    Turnaround time :                            528810 sec.

The output (if any) is above this job summary.

