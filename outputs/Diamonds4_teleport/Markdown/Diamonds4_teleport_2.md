
# Parameters

    Name :                      Diamonds4_teleport-2
    Main :                      teleport
    Level :                     Levels.Causal7
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


      69309478687 function calls (69083622616 primitive calls) in 86113.34 seconds

##    Ordered by: cumulative time
   List reduced from 474 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86113.338 86113.338 {built-in method builtins.exec}
                      1    1.663    1.663 86113.338 86113.338 <string>:1(<module>)
                      1  284.608  284.608 86111.675 86111.675 main.py:45(teleport)
                8066802   44.241    0.000 26400.974    0.003 agent.py:29(learn)
                8066802  668.276    0.000 21843.703    0.003 learner.py:42(Qlearn)
                4033401   23.562    0.000 21659.492    0.005 game.py:41(step)
                4033401   34.740    0.000 20622.256    0.005 layers.py:718(step)
                4033401  186.086    0.000 15846.053    0.004 agent.py:54(_learn)
                4033401 6746.321    0.002 11909.555    0.003 replaybuffer.py:28(teleporter_save_data)
                4033401  407.325    0.000 11229.207    0.003 layers.py:17(step)
        254087584/28232524 1114.577    0.000 10954.990    0.000 module.py:715(_call_impl)
              403340100  693.421    0.000 10780.419    0.000 layer.py:98(move)
                4033401  154.860    0.000 10485.903    0.003 agent.py:117(_learn)
               20165722   60.266    0.000 10134.840    0.001 network.py:27(forward)
               20165722  290.754    0.000 9926.808    0.000 container.py:115(forward)
                4033401 6138.328    0.002 9384.840    0.002 agent.py:88(interveen)
                4033402  648.985    0.000 9305.805    0.002 layers.py:684(update)
                4033401 6483.524    0.002 8527.429    0.002 replaybuffer.py:22(sample_data)
                8066802   71.791    0.000 8325.536    0.001 grad_mode.py:23(decorate_context)
                8066802  305.546    0.000 8127.724    0.001 adam.py:55(step)
                8065519  273.609    0.000 6918.953    0.001 agent.py:49(__call__)
                8066802 1515.907    0.000 6682.040    0.001 functional.py:53(adam)
              403340100 1292.403    0.000 6313.820    0.000 layers.py:735(check)
                8066802   60.886    0.000 5472.860    0.001 tensor.py:181(backward)
                8066802   46.841    0.000 5411.974    0.001 __init__.py:68(backward)
                8066802 5126.656    0.001 5126.656    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                4033401 2333.782    0.001 4506.599    0.001 agent.py:67(modify)
              372274047 4074.758    0.000 4074.758    0.000 {built-in method clone}
               40331444   85.638    0.000 3791.896    0.000 conv.py:422(forward)
               40331444  100.445    0.000 3669.260    0.000 conv.py:414(_conv_forward)
               40331444 3552.008    0.000 3552.008    0.000 {built-in method conv2d}
                7708086   84.179    0.000 3290.555    0.000 layers.py:740(restart)
               52430364  130.169    0.000 3136.809    0.000 linear.py:92(forward)
              403340100  621.629    0.000 3021.430    0.000 layers.py:729(isFree)
               52430364  214.469    0.000 2939.386    0.000 functional.py:1669(linear)
                7708086   43.553    0.000 2609.638    0.000 level.py:8(__init__)
               28233814 1497.860    0.000 2548.305    0.000 layer.py:167(NoRock_update)
             2746772514 2005.624    0.000 2399.801    0.000 layer.py:95(isFree)
                7708086   96.238    0.000 2173.690    0.000 levels.py:441(generate)
               12098920  116.499    0.000 2142.987    0.000 agent.py:59(modify_board)
                4033401   83.317    0.000 2102.293    0.001 agent.py:112(__call__)
               52430364 2100.817    0.000 2100.817    0.000 {built-in method addmm}
             1125671456  613.241    0.000 2089.577    0.000 {built-in method builtins.any}
               32265925 2007.219    0.000 2007.219    0.000 {built-in method cat}
              508208580 1201.376    0.000 1994.120    0.000 tensor.py:933(grad)
               36996140  367.485    0.000 1978.031    0.000 level.py:41(notUsed)
             6616363414 1239.724    0.000 1803.489    0.000 enum.py:646(__hash__)
                8066802  166.026    0.000 1728.836    0.000 optimizer.py:167(zero_grad)
                4033401   86.612    0.000 1673.221    0.000 replaybuffer.py:18(stacker)
               17275794 1442.650    0.000 1442.650    0.000 {built-in method tensor}
               12098920 1383.393    0.000 1383.393    0.000 {built-in method torch._C._nn.one_hot}
               72596086   74.195    0.000 1332.906    0.000 activation.py:713(forward)
              145202436 1326.027    0.000 1326.027    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              403340100  830.579    0.000 1299.330    0.000 layers.py:632(check)
              431576127  139.696    0.000 1276.722    0.000 {built-in method builtins.all}
               72596086  109.020    0.000 1258.711    0.000 functional.py:1292(leaky_relu)
              403340100  784.480    0.000 1240.413    0.000 layers.py:602(check)
               28235927  167.560    0.000 1199.120    0.000 tensor.py:21(wrapped)
              403340100  711.270    0.000 1190.163    0.000 layers.py:617(check)
             1248864589  331.065    0.000 1168.947    0.000 layers.py:690(<genexpr>)
              384372967 1144.761    0.000 1144.761    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               72596086 1139.490    0.000 1139.490    0.000 {built-in method torch._C._nn.leaky_relu}
                8066802   15.173    0.000 1138.236    0.000 game.py:37(board)
              145202436 1084.102    0.000 1084.102    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              661475373  357.917    0.000 1080.648    0.000 overrides.py:1070(has_torch_function)
             3165056912  871.603    0.000 1066.920    0.000 layers.py:700(<genexpr>)
               36996140   29.593    0.000  924.357    0.000 level.py:38(elementsIn)
             7680337699  807.845    0.000  807.845    0.000 layer.py:91(positions)
              403340200  530.618    0.000  787.971    0.000 layers.py:113(isDone)
                4033401  449.415    0.000  782.400    0.000 collector.py:46(collect)
               72601218  771.266    0.000  771.266    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                8065519  261.711    0.000  764.026    0.000 exploration.py:53(softmaxer)
               72601218  736.918    0.000  736.918    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
             1397264306  699.338    0.000  699.338    0.000 layer.py:146(elements)
               72601218  651.812    0.000  651.812    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               36996140  293.743    0.000  603.412    0.000 level.py:39(<listcomp>)
               53956602   52.556    0.000  576.687    0.000 layer.py:69(restart)
               72601218  572.389    0.000  572.389    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
             6616392829  563.770    0.000  563.770    0.000 {built-in method builtins.hash}
                8066802   24.085    0.000  548.297    0.000 loss.py:445(forward)
              403340100  341.809    0.000  539.878    0.000 layers.py:588(check)
                8066802   67.889    0.000  524.213    0.000 functional.py:2637(mse_loss)
              403340100  301.370    0.000  449.131    0.000 layers.py:23(check)
        4273028602/4273028600  325.467    0.000  441.575    0.000 {built-in method builtins.len}
              674230161  315.824    0.000  441.538    0.000 layer.py:130(add)
               20167005  424.764    0.000  424.764    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                7708186  208.084    0.000  419.587    0.000 layers.py:36(reset)
             1776285550  413.954    0.000  413.954    0.000 level.py:32(inverse)
               72601218  409.285    0.000  409.285    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
             1403616231  324.529    0.000  402.909    0.000 overrides.py:1083(<genexpr>)
               52430364  381.238    0.000  381.238    0.000 {method 't' of 'torch._C._TensorBase' objects}
                7708086  223.479    0.000  367.806    0.000 level.py:16(<dictcomp>)
                4035013  364.240    0.000  364.240    0.000 {method 'ne' of 'torch._C._TensorBase' objects}
                4033401  135.993    0.000  362.965    0.000 random.py:315(sample)
              410869538  237.031    0.000  352.893    0.000 layer.py:126(remove)
               24200406  334.344    0.000  334.344    0.000 {built-in method sum}
             2746772514  319.194    0.000  319.194    0.000 layer.py:203(isBlocking)
             1609353626  309.617    0.000  309.617    0.000 enum.py:352(<genexpr>)
                8066802  299.742    0.000  299.742    0.000 {built-in method torch._C._nn.mse_loss}
               36996140  182.552    0.000  291.352    0.000 {built-in method _functools.reduce}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9550907: <Diamonds4_teleport_2> in cluster <dcc> Done

Job <Diamonds4_teleport_2> was submitted from host <n-62-30-4> by user <s183905> in cluster <dcc> at Tue Apr 20 16:21:49 2021
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Fri Apr 23 17:50:14 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Fri Apr 23 17:50:14 2021
Terminated at Sat Apr 24 17:45:34 2021
Results reported at Sat Apr 24 17:45:34 2021

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

    CPU time :                                   85903.70 sec.
    Max Memory :                                 2676 MB
    Average Memory :                             2671.91 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13708.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86121 sec.
    Turnaround time :                            350625 sec.

The output (if any) is above this job summary.

