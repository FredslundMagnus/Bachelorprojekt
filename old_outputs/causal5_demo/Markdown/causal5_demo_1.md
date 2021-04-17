
# Parameters

    Name :                      causal5_demo-1
    Main :                      teleport
    Level :                     Levels.Causal5
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


      54651654624 function calls (54483431897 primitive calls) in 57306.74 seconds

##    Ordered by: cumulative time
   List reduced from 473 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 57306.738 57306.738 {built-in method builtins.exec}
                      1    1.866    1.866 57306.738 57306.738 <string>:1(<module>)
                      1  139.259  139.259 57304.872 57304.872 main.py:40(teleport)
                6008416   22.379    0.000 17485.648    0.003 agent.py:29(learn)
                3004208   13.095    0.000 15953.835    0.005 game.py:39(step)
                3004208   16.424    0.000 15261.430    0.005 layers.py:581(step)
                6008416  416.000    0.000 14726.639    0.002 learner.py:42(Qlearn)
                3004208  103.757    0.000 10569.335    0.004 agent.py:54(_learn)
                3004208  242.489    0.000 8994.122    0.003 layers.py:17(step)
                3004208 4861.393    0.002 8764.278    0.003 replaybuffer.py:28(teleporter_save_data)
              300420800  733.836    0.000 8725.414    0.000 layer.py:92(move)
        189250011/21028295  750.854    0.000 7245.688    0.000 module.py:715(_call_impl)
                3004208   84.063    0.000 6882.223    0.002 agent.py:115(_learn)
               15019879   37.460    0.000 6771.280    0.000 network.py:24(forward)
               15019879  182.793    0.000 6641.110    0.000 container.py:115(forward)
                3004209  447.179    0.000 6228.356    0.002 layers.py:552(update)
                3004208 3713.806    0.001 5929.225    0.002 agent.py:86(interveen)
                6008416   37.909    0.000 5912.814    0.001 grad_mode.py:23(decorate_context)
                6008416  206.551    0.000 5803.870    0.001 adam.py:55(step)
              300420800  838.557    0.000 5156.707    0.000 layers.py:598(check)
                6008416 1067.303    0.000 4749.525    0.001 functional.py:53(adam)
                6007255  135.984    0.000 4466.392    0.001 agent.py:49(__call__)
                3004208 2672.584    0.001 4200.681    0.001 replaybuffer.py:22(sample_data)
                6008416   38.328    0.000 3454.977    0.001 tensor.py:181(backward)
                6008416   22.438    0.000 3416.649    0.001 __init__.py:68(backward)
                6008416 3254.627    0.001 3254.627    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
              291506980 3091.650    0.000 3091.650    0.000 {built-in method clone}
                3004208 1187.992    0.000 2465.402    0.001 agent.py:67(modify)
               30039758   51.781    0.000 2445.432    0.000 conv.py:422(forward)
               30039758   59.170    0.000 2372.848    0.000 conv.py:414(_conv_forward)
               30039758 2302.622    0.000 2302.622    0.000 {built-in method conv2d}
              300420800  586.122    0.000 2180.703    0.000 layers.py:592(isFree)
               39051221   93.097    0.000 2131.150    0.000 linear.py:92(forward)
               39051221  150.016    0.000 1996.305    0.000 functional.py:1669(linear)
               27037881 1018.171    0.000 1801.298    0.000 layer.py:163(NoRock_update)
              834815658  515.706    0.000 1796.544    0.000 {built-in method builtins.any}
                3352843   39.849    0.000 1663.402    0.000 layers.py:602(restart)
             2608961616 1263.304    0.000 1594.581    0.000 layer.py:89(isFree)
             6033185990 1072.519    0.000 1542.119    0.000 enum.py:646(__hash__)
               27036711 1522.812    0.000 1522.812    0.000 {built-in method cat}
              378530262  913.447    0.000 1517.780    0.000 tensor.py:933(grad)
                3004208   39.035    0.000 1424.016    0.000 agent.py:110(__call__)
               39051221 1410.499    0.000 1410.499    0.000 {built-in method addmm}
                3352843   18.296    0.000 1355.901    0.000 level.py:8(__init__)
                9011463   61.853    0.000 1339.529    0.000 agent.py:59(modify_board)
                6008416  128.925    0.000 1316.561    0.000 optimizer.py:167(zero_grad)
                3004208   58.550    0.000 1297.287    0.000 replaybuffer.py:18(stacker)
                3352843   54.318    0.000 1191.724    0.000 levels.py:249(generate)
               21795310  205.155    0.000 1079.717    0.000 level.py:41(notUsed)
               12948944  995.878    0.000  995.878    0.000 {built-in method tensor}
             2970680570  804.990    0.000  977.161    0.000 layers.py:563(<genexpr>)
              108151488  960.142    0.000  960.142    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               54071100   46.250    0.000  923.538    0.000 activation.py:713(forward)
              315443730  159.182    0.000  922.048    0.000 {built-in method builtins.all}
              300420800  574.039    0.000  897.259    0.000 layers.py:331(check)
               54071100   72.621    0.000  877.288    0.000 functional.py:1292(leaky_relu)
              300420800  561.784    0.000  876.168    0.000 layers.py:381(check)
              300518443  872.740    0.000  872.740    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                9011463  857.205    0.000  857.205    0.000 {built-in method torch._C._nn.one_hot}
              300420800  536.673    0.000  847.539    0.000 layers.py:343(check)
              300420800  522.676    0.000  834.440    0.000 layers.py:369(check)
              486679547  269.996    0.000  807.699    0.000 overrides.py:1070(has_torch_function)
               54071100  796.890    0.000  796.890    0.000 {built-in method torch._C._nn.leaky_relu}
              108151488  794.088    0.000  794.088    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
             1493847491  421.161    0.000  790.337    0.000 layers.py:558(<genexpr>)
                6008416    7.880    0.000  788.377    0.000 game.py:35(board)
             6351168050  623.606    0.000  623.606    0.000 layer.py:85(positions)
               15022830   81.883    0.000  598.821    0.000 tensor.py:21(wrapped)
                3004208  326.701    0.000  560.153    0.000 collector.py:53(collect)
               54075744  554.310    0.000  554.310    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               54075744  509.499    0.000  509.499    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               21795310   16.741    0.000  474.002    0.000 level.py:38(elementsIn)
             6033207989  469.604    0.000  469.604    0.000 {built-in method builtins.hash}
              886078314  464.212    0.000  464.212    0.000 layer.py:142(elements)
                6007255  170.948    0.000  463.518    0.000 exploration.py:53(softmaxer)
               54075744  451.864    0.000  451.864    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               54075744  396.964    0.000  396.964    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              300420800  257.368    0.000  396.514    0.000 layers.py:358(check)
              300420800  249.158    0.000  383.668    0.000 layers.py:320(check)
                6008416    8.330    0.000  307.845    0.000 loss.py:445(forward)
        3166458800/3166458798  218.439    0.000  305.453    0.000 {built-in method builtins.len}
               54075744  300.666    0.000  300.666    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                6008416   33.661    0.000  299.515    0.000 functional.py:2637(mse_loss)
             1027432545  241.636    0.000  299.396    0.000 overrides.py:1083(<genexpr>)
               21795310  146.763    0.000  297.967    0.000 level.py:39(<listcomp>)
             2608961616  279.597    0.000  279.597    0.000 layer.py:199(isBlocking)
               30175587   26.097    0.000  256.365    0.000 layer.py:64(restart)
               39051221  255.854    0.000  255.854    0.000 {method 't' of 'torch._C._TensorBase' objects}
             1027938260  255.657    0.000  255.657    0.000 level.py:32(inverse)
              417657088  177.215    0.000  246.095    0.000 layer.py:126(add)
               18025248  225.440    0.000  225.440    0.000 {built-in method sum}
                3004208   82.811    0.000  225.283    0.000 random.py:315(sample)
              301992199  151.718    0.000  225.188    0.000 layer.py:122(remove)
                3005408  211.353    0.000  211.353    0.000 {method 'ne' of 'torch._C._TensorBase' objects}
                9012624   44.842    0.000  193.928    0.000 tensor.py:506(__rsub__)
                3352943   93.736    0.000  185.303    0.000 layers.py:30(reset)
                6008416  173.341    0.000  173.341    0.000 {built-in method torch._C._nn.mse_loss}
             2673612513  172.171    0.000  172.171    0.000 layer.py:78(isDead)
               30039758   21.607    0.000  169.395    0.000 flatten.py:39(forward)
                9012624  167.634    0.000  167.634    0.000 {method 'eq' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-16>
Subject: Job 9497200: <causal5_demo_1> in cluster <dcc> Done

Job <causal5_demo_1> was submitted from host <n-62-27-19> by user <s183905> in cluster <dcc> at Mon Apr  5 21:09:35 2021
Job was executed on host(s) <n-62-20-16>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Tue Apr  6 23:33:13 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue Apr  6 23:33:13 2021
Terminated at Wed Apr  7 15:28:23 2021
Results reported at Wed Apr  7 15:28:23 2021

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

    CPU time :                                   57166.52 sec.
    Max Memory :                                 2812 MB
    Average Memory :                             2808.00 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13572.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   57310 sec.
    Turnaround time :                            152328 sec.

The output (if any) is above this job summary.

