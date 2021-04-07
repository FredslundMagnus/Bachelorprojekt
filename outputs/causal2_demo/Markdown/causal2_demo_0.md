
# Parameters

    Name :                      causal2_demo-0
    Main :                      teleport
    Level :                     Levels.Causal2
    Hours :                     16.0
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
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                2
    Minutes used :              955 minutes.
    Hours used :                15 hours.

# Profiling


      49501575777 function calls (49328915342 primitive calls) in 57309.92 seconds

##    Ordered by: cumulative time
   List reduced from 471 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 57309.925 57309.925 {built-in method builtins.exec}
                      1    1.881    1.881 57309.925 57309.925 <string>:1(<module>)
                      1  144.196  144.196 57308.044 57308.044 main.py:40(teleport)
                6166816   22.602    0.000 17846.712    0.003 agent.py:29(learn)
                6166816  428.388    0.000 15029.623    0.002 learner.py:42(Qlearn)
                3083408   12.378    0.000 14258.964    0.005 game.py:39(step)
                3083408   16.685    0.000 13599.998    0.004 layers.py:581(step)
                3083408  105.356    0.000 10792.919    0.004 agent.py:54(_learn)
                3083408 5317.266    0.002 9559.656    0.003 replaybuffer.py:28(teleporter_save_data)
        194242328/21582904  731.666    0.000 7354.758    0.000 module.py:715(_call_impl)
                3083408  252.572    0.000 7326.163    0.002 layers.py:17(step)
              308340800  728.586    0.000 7041.529    0.000 layer.py:92(move)
                3083408   87.554    0.000 7019.065    0.002 agent.py:115(_learn)
               15416088   38.851    0.000 6870.712    0.000 network.py:24(forward)
               15416088  179.820    0.000 6739.270    0.000 container.py:115(forward)
                3083408 4057.383    0.001 6307.811    0.002 agent.py:86(interveen)
                3083409  455.871    0.000 6233.759    0.002 layers.py:552(update)
                6166816   38.758    0.000 6051.818    0.001 grad_mode.py:23(decorate_context)
                6166816  201.489    0.000 5943.180    0.001 adam.py:55(step)
                6166816 1089.829    0.000 4878.882    0.001 functional.py:53(adam)
                6165864  138.796    0.000 4549.605    0.001 agent.py:49(__call__)
                3083408 2682.422    0.001 4244.936    0.001 replaybuffer.py:22(sample_data)
              308340800  652.491    0.000 3787.172    0.000 layers.py:598(check)
                6166816   36.400    0.000 3532.269    0.001 tensor.py:181(backward)
                6166816   21.489    0.000 3495.869    0.001 __init__.py:68(backward)
              320466772 3355.673    0.000 3355.673    0.000 {built-in method clone}
                6166816 3332.024    0.001 3332.024    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3083408 1280.764    0.000 2588.557    0.001 agent.py:67(modify)
               30832176   54.614    0.000 2506.865    0.000 conv.py:422(forward)
               30832176   61.279    0.000 2431.473    0.000 conv.py:414(_conv_forward)
               30832176 2359.298    0.000 2359.298    0.000 {built-in method conv2d}
                5858592   53.449    0.000 2261.381    0.000 layers.py:602(restart)
               40081448   90.501    0.000 2168.041    0.000 linear.py:92(forward)
               40081448  152.764    0.000 2036.584    0.000 functional.py:1669(linear)
              308340800  478.292    0.000 1867.926    0.000 layers.py:592(isFree)
                5858592   26.924    0.000 1776.048    0.000 level.py:8(__init__)
               21583863  919.439    0.000 1586.453    0.000 layer.py:163(NoRock_update)
              854407931  479.416    0.000 1583.748    0.000 {built-in method builtins.any}
               27749720 1563.539    0.000 1563.539    0.000 {built-in method cat}
              388509462  926.656    0.000 1544.014    0.000 tensor.py:933(grad)
                5858592   71.322    0.000 1524.632    0.000 levels.py:151(generate)
                3083408   39.965    0.000 1444.997    0.000 agent.py:110(__call__)
               40081448 1435.407    0.000 1435.407    0.000 {built-in method addmm}
             2123834291 1133.261    0.000 1389.634    0.000 layer.py:89(isFree)
             5475670673  964.699    0.000 1387.828    0.000 enum.py:646(__hash__)
               28117035  272.404    0.000 1379.406    0.000 level.py:41(notUsed)
                9249272   61.497    0.000 1374.451    0.000 agent.py:59(modify_board)
                3083408   59.960    0.000 1332.633    0.000 replaybuffer.py:18(stacker)
                6166816  124.636    0.000 1329.040    0.000 optimizer.py:167(zero_grad)
              111002688  993.789    0.000  993.789    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              329716044  944.266    0.000  944.266    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               55497536   46.592    0.000  940.880    0.000 activation.py:713(forward)
               13281193  915.311    0.000  915.311    0.000 {built-in method tensor}
              308340800  570.019    0.000  906.127    0.000 layers.py:213(check)
               55497536   73.207    0.000  894.288    0.000 functional.py:1292(leaky_relu)
                9249272  882.903    0.000  882.903    0.000 {built-in method torch._C._nn.one_hot}
              308340800  549.494    0.000  871.050    0.000 layers.py:225(check)
              308340800  536.369    0.000  864.971    0.000 layers.py:201(check)
              499510542  269.578    0.000  826.148    0.000 overrides.py:1070(has_torch_function)
               55497536  813.577    0.000  813.577    0.000 {built-in method torch._C._nn.leaky_relu}
              111002688  813.106    0.000  813.106    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
             2419858464  643.399    0.000  787.912    0.000 layers.py:563(<genexpr>)
              323759714   77.599    0.000  766.581    0.000 {built-in method builtins.all}
              659564502  155.409    0.000  719.116    0.000 layers.py:558(<genexpr>)
                6166816    7.013    0.000  700.406    0.000 game.py:35(board)
               15418814   82.513    0.000  612.504    0.000 tensor.py:21(wrapped)
               28117035   22.372    0.000  609.395    0.000 level.py:38(elementsIn)
               55501344  572.064    0.000  572.064    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                3083408  332.428    0.000  571.732    0.000 collector.py:53(collect)
              308340900  371.517    0.000  556.938    0.000 layers.py:107(isDone)
             5236135289  530.970    0.000  530.970    0.000 layer.py:85(positions)
               55501344  526.053    0.000  526.053    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                6165864  176.403    0.000  475.875    0.000 exploration.py:53(softmaxer)
               55501344  460.655    0.000  460.655    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
             5475693248  423.133    0.000  423.133    0.000 {built-in method builtins.hash}
               41010144   36.290    0.000  416.965    0.000 layer.py:64(restart)
              308340800  272.469    0.000  410.902    0.000 layers.py:190(check)
             1062186376  410.149    0.000  410.149    0.000 layer.py:142(elements)
               55501344  407.009    0.000  407.009    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               28117035  191.501    0.000  386.279    0.000 level.py:39(<listcomp>)
                5858692  159.390    0.000  317.611    0.000 layers.py:30(reset)
                6166816    9.578    0.000  313.507    0.000 loss.py:445(forward)
             1054520730  248.225    0.000  312.307    0.000 overrides.py:1083(<genexpr>)
             1349977919  310.826    0.000  310.826    0.000 level.py:32(inverse)
               55501344  304.535    0.000  304.535    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                6166816   33.255    0.000  303.929    0.000 functional.py:2637(mse_loss)
              512418876  214.667    0.000  299.884    0.000 layer.py:126(add)
        2655980803/2655980801  194.549    0.000  281.551    0.000 {built-in method builtins.len}
               40081448  262.743    0.000  262.743    0.000 {method 't' of 'torch._C._TensorBase' objects}
               18500448  232.487    0.000  232.487    0.000 {built-in method sum}
              308268583  155.129    0.000  232.120    0.000 layer.py:122(remove)
                3083408   82.609    0.000  224.411    0.000 random.py:315(sample)
                3084640  214.565    0.000  214.565    0.000 {method 'ne' of 'torch._C._TensorBase' objects}
                5858592  123.909    0.000  209.292    0.000 level.py:16(<dictcomp>)
             2123834291  202.964    0.000  202.964    0.000 layer.py:199(isBlocking)
             1053245565  202.948    0.000  202.948    0.000 enum.py:352(<genexpr>)
               28117035  125.648    0.000  200.744    0.000 {built-in method _functools.reduce}
                9250224   46.454    0.000  198.167    0.000 tensor.py:506(__rsub__)
                6166816  177.251    0.000  177.251    0.000 {built-in method torch._C._nn.mse_loss}
                9250224  173.804    0.000  173.804    0.000 {method 'eq' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-14>
Subject: Job 9497197: <causal2_demo_0> in cluster <dcc> Done

Job <causal2_demo_0> was submitted from host <n-62-27-19> by user <s183905> in cluster <dcc> at Mon Apr  5 21:09:34 2021
Job was executed on host(s) <n-62-20-14>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Tue Apr  6 22:38:37 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue Apr  6 22:38:37 2021
Terminated at Wed Apr  7 14:33:53 2021
Results reported at Wed Apr  7 14:33:53 2021

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

    CPU time :                                   57157.01 sec.
    Max Memory :                                 2811 MB
    Average Memory :                             2807.27 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13573.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   57317 sec.
    Turnaround time :                            149059 sec.

The output (if any) is above this job summary.

