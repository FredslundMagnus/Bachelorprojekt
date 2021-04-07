
# Parameters

    Name :                      causal6_demo-1
    Main :                      teleport
    Level :                     Levels.Causal6
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


      60728432588 function calls (60549218341 primitive calls) in 57318.44 seconds

##    Ordered by: cumulative time
   List reduced from 472 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 57318.436 57318.436 {built-in method builtins.exec}
                      1    1.813    1.813 57318.435 57318.435 <string>:1(<module>)
                      1  145.179  145.179 57316.622 57316.622 main.py:40(teleport)
                6400936   22.510    0.000 17045.068    0.003 agent.py:29(learn)
                3200468   12.317    0.000 16115.792    0.005 game.py:39(step)
                3200468   17.537    0.000 15432.093    0.005 layers.py:581(step)
                6400936  409.522    0.000 14333.572    0.002 learner.py:42(Qlearn)
                3200468  102.082    0.000 10314.141    0.003 agent.py:54(_learn)
                3200468 5011.821    0.002 8997.177    0.003 replaybuffer.py:28(teleporter_save_data)
                3200468  242.525    0.000 8073.947    0.003 layers.py:17(step)
              320046800  681.749    0.000 7801.820    0.000 layer.py:92(move)
                3200469  442.295    0.000 7317.847    0.002 layers.py:552(update)
        201615431/22402195  700.135    0.000 6994.378    0.000 module.py:715(_call_impl)
                3200468   84.021    0.000 6696.668    0.002 agent.py:115(_learn)
               16001259   36.917    0.000 6523.410    0.000 network.py:24(forward)
               16001259  172.348    0.000 6396.960    0.000 container.py:115(forward)
                3200468 3821.187    0.001 5971.095    0.002 agent.py:86(interveen)
                6400936   37.397    0.000 5767.592    0.001 grad_mode.py:23(decorate_context)
                6400936  193.958    0.000 5662.821    0.001 adam.py:55(step)
                6400936 1042.748    0.000 4665.712    0.001 functional.py:53(adam)
              320046800  727.783    0.000 4534.780    0.000 layers.py:598(check)
                6399855  136.020    0.000 4355.293    0.001 agent.py:49(__call__)
                3200468 2751.037    0.001 4256.192    0.001 replaybuffer.py:22(sample_data)
                6400936   36.095    0.000 3384.322    0.001 tensor.py:181(backward)
                6400936   20.875    0.000 3348.227    0.001 __init__.py:68(backward)
                6400936 3190.096    0.000 3190.096    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
              328117528 3157.285    0.000 3157.285    0.000 {built-in method clone}
                3200468 1223.076    0.000 2480.465    0.001 agent.py:67(modify)
                6019411   54.134    0.000 2452.210    0.000 layers.py:602(restart)
               32002518   49.926    0.000 2386.055    0.000 conv.py:422(forward)
               32002518   57.745    0.000 2316.475    0.000 conv.py:414(_conv_forward)
               32002518 2248.287    0.000 2248.287    0.000 {built-in method conv2d}
               41602841   82.354    0.000 2050.394    0.000 linear.py:92(forward)
                6019411   26.605    0.000 1981.068    0.000 level.py:8(__init__)
              320046800  493.742    0.000 1956.245    0.000 layers.py:592(isFree)
               41602841  140.793    0.000 1927.535    0.000 functional.py:1669(linear)
                6019411   77.961    0.000 1741.895    0.000 levels.py:293(generate)
               25603752  977.095    0.000 1693.133    0.000 layer.py:163(NoRock_update)
             7165657636 1138.222    0.000 1658.720    0.000 enum.py:646(__hash__)
              886906077  469.617    0.000 1642.287    0.000 {built-in method builtins.any}
               36120395  303.962    0.000 1580.984    0.000 level.py:41(notUsed)
               28803131 1498.222    0.000 1498.222    0.000 {built-in method cat}
              336051036  182.988    0.000 1478.019    0.000 {built-in method builtins.all}
             2501441565 1183.051    0.000 1462.503    0.000 layer.py:89(isFree)
              403259022  860.029    0.000 1436.671    0.000 tensor.py:933(grad)
                3200468   40.013    0.000 1371.851    0.000 agent.py:110(__call__)
               41602841 1366.018    0.000 1366.018    0.000 {built-in method addmm}
                9600323   57.815    0.000 1326.865    0.000 agent.py:59(modify_board)
             2051604358  529.306    0.000 1322.088    0.000 layers.py:558(<genexpr>)
                3200468   58.629    0.000 1283.380    0.000 replaybuffer.py:18(stacker)
              320046800  779.569    0.000 1272.684    0.000 layers.py:418(check)
                6400936  116.136    0.000 1253.364    0.000 optimizer.py:167(zero_grad)
               13772666  978.428    0.000  978.428    0.000 {built-in method tensor}
              115216848  950.867    0.000  950.867    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               57604100   44.390    0.000  897.761    0.000 activation.py:713(forward)
              337717851  882.118    0.000  882.118    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
             2826247401  722.308    0.000  879.711    0.000 layers.py:563(<genexpr>)
                9600323  861.091    0.000  861.091    0.000 {built-in method torch._C._nn.one_hot}
               57604100   68.417    0.000  853.371    0.000 functional.py:1292(leaky_relu)
              320046800  519.854    0.000  824.640    0.000 layers.py:431(check)
              320046800  514.716    0.000  822.508    0.000 layers.py:446(check)
              115216848  780.955    0.000  780.955    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               57604100  778.030    0.000  778.030    0.000 {built-in method torch._C._nn.leaky_relu}
                6400936    7.113    0.000  773.606    0.000 game.py:35(board)
              518473874  255.001    0.000  772.397    0.000 overrides.py:1070(has_torch_function)
               36120395   25.387    0.000  691.774    0.000 level.py:38(elementsIn)
             6361043675  610.676    0.000  610.676    0.000 layer.py:85(positions)
               16004136   78.603    0.000  594.285    0.000 tensor.py:21(wrapped)
                3200468  320.433    0.000  547.319    0.000 collector.py:53(collect)
               57608424  546.640    0.000  546.640    0.000 {method 'add' of 'torch._C._TensorBase' objects}
             7165681075  520.502    0.000  520.502    0.000 {built-in method builtins.hash}
               57608424  506.953    0.000  506.953    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              320046900  311.960    0.000  502.829    0.000 layers.py:436(isDone)
                6399855  166.805    0.000  460.460    0.000 exploration.py:53(softmaxer)
               36120395  215.096    0.000  437.688    0.000 level.py:39(<listcomp>)
             1119238072  437.684    0.000  437.684    0.000 layer.py:142(elements)
               57608424  436.380    0.000  436.380    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              320046800  272.630    0.000  411.673    0.000 layers.py:407(check)
               48155288   38.233    0.000  401.283    0.000 layer.py:64(restart)
              320046800  260.027    0.000  394.055    0.000 layers.py:396(check)
               57608424  386.247    0.000  386.247    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
             1713300907  375.770    0.000  375.770    0.000 level.py:32(inverse)
                6400936   11.434    0.000  302.608    0.000 loss.py:445(forward)
               57608424  298.571    0.000  298.571    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                6019511  146.249    0.000  292.612    0.000 layers.py:30(reset)
                6400936   32.585    0.000  291.175    0.000 functional.py:2637(mse_loss)
             1094554086  232.918    0.000  288.851    0.000 overrides.py:1083(<genexpr>)
        3067876244/3067876242  201.874    0.000  285.023    0.000 {built-in method builtins.len}
              537004980  204.424    0.000  282.306    0.000 layer.py:126(add)
               41602841  243.940    0.000  243.940    0.000 {method 't' of 'torch._C._TensorBase' objects}
               36120395  142.393    0.000  228.698    0.000 {built-in method _functools.reduce}
             2501441565  222.928    0.000  222.928    0.000 layer.py:199(isBlocking)
              322216474  148.370    0.000  219.758    0.000 layer.py:122(remove)
               19202808  219.148    0.000  219.148    0.000 {built-in method sum}
             1306335145  218.728    0.000  218.728    0.000 enum.py:352(<genexpr>)
                3200468   80.244    0.000  216.400    0.000 random.py:315(sample)
                3201746  210.796    0.000  210.796    0.000 {method 'ne' of 'torch._C._TensorBase' objects}
              120004420  139.674    0.000  204.373    0.000 layers.py:107(isDone)
                6019411  118.167    0.000  196.966    0.000 level.py:16(<dictcomp>)
                9601404   47.858    0.000  193.996    0.000 tensor.py:506(__rsub__)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-4>
Subject: Job 9497202: <causal6_demo_1> in cluster <dcc> Done

Job <causal6_demo_1> was submitted from host <n-62-27-19> by user <s183905> in cluster <dcc> at Mon Apr  5 21:09:35 2021
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Wed Apr  7 02:41:12 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed Apr  7 02:41:12 2021
Terminated at Wed Apr  7 18:36:39 2021
Results reported at Wed Apr  7 18:36:39 2021

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

    CPU time :                                   57170.83 sec.
    Max Memory :                                 2816 MB
    Average Memory :                             2809.05 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13568.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   57329 sec.
    Turnaround time :                            163624 sec.

The output (if any) is above this job summary.

