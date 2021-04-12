
# Parameters

    Name :                      causal6_online_var-0
    Main :                      graphTrain
    Level :                     Levels.Causal6
    Hours :                     12.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Network1 :                  Networks.Teleporter
    K1 :                        200000.0
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
    K2 :                        100000.0
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
    Softmax cap :               0.0
    Update :                    10000
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                2
    Counterfacts :              10
    Topn :                      7
    Minutes used :              715 minutes.
    Hours used :                11 hours.

# Profiling


      31720125040 function calls (29151876505 primitive calls) in 42902.87 seconds

##    Ordered by: cumulative time
   List reduced from 464 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 42902.874 42902.874 {built-in method builtins.exec}
                      1    0.002    0.002 42902.874 42902.874 <string>:1(<module>)
                      1  144.223  144.223 42902.872 42902.872 allGraphsTrain.py:5(graphTrain)
                 582038 7314.880    0.013 16534.911    0.028 allGraphs.py:238(transformNot)
                 582038   15.168    0.000 10370.590    0.018 allGraphsTrain.py:24(<listcomp>)
               58785939 2665.395    0.000 10355.441    0.000 allGraphs.py:198(states)
              698450756 9368.451    0.000 9368.451    0.000 {method 'item' of 'torch._C._TensorBase' objects}
              640242300 8196.698    0.000 8196.698    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 582038  637.147    0.001 6047.896    0.010 allGraphsTrain.py:30(<listcomp>)
                9027720   51.704    0.000 5410.749    0.001 allGraphs.py:245(getInterventions)
                8303215    6.706    0.000 4399.294    0.001 allGraphs.py:225(rightIntervention)
        459713257/8303215  240.015    0.000 4356.254    0.001 {built-in method builtins.min}
               31892841   12.795    0.000 4339.971    0.000 allGraphs.py:226(<lambda>)
        911123299/31892841 1299.095    0.000 4327.176    0.000 allGraphs.py:61(expected_moves)
        1330640500/104673608  348.888    0.000 4128.798    0.000 allGraphs.py:65(<genexpr>)
                 582038    2.099    0.000 3361.531    0.006 game.py:41(step)
                 582038    2.873    0.000 3227.085    0.006 layers.py:710(step)
                 582038  153.037    0.000 2041.246    0.004 allGraphsTrain.py:32(<listcomp>)
                 582039   77.067    0.000 1916.202    0.003 layers.py:676(update)
             7360289522 1076.874    0.000 1560.833    0.000 enum.py:646(__hash__)
                 582038    2.025    0.000 1524.641    0.003 agent.py:29(learn)
                 582038   11.869    0.000 1521.428    0.003 agent.py:117(_learn)
                 582038   44.012    0.000 1509.559    0.003 learner.py:42(Qlearn)
               14414942 1351.550    0.000 1351.550    0.000 {built-in method tensor}
              460437762  237.765    0.000 1350.565    0.000 allGraphs.py:70(layers_not_in)
                 582038   38.951    0.000 1304.862    0.002 layers.py:17(step)
               61696028  161.371    0.000 1264.106    0.000 tensor.py:21(wrapped)
               11937911    7.375    0.000 1262.780    0.000 game.py:37(board)
               58203800   86.183    0.000 1261.085    0.000 layer.py:98(move)
                 582038   54.981    0.000 1214.230    0.002 allGraphsTrain.py:39(<listcomp>)
                2825058   20.428    0.000 1170.091    0.000 layers.py:731(restart)
              460437762  552.218    0.000 1112.799    0.000 allGraphs.py:71(<listcomp>)
                2825058   10.010    0.000  967.891    0.000 level.py:8(__init__)
               61113990  934.717    0.000  934.717    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                2825058   34.456    0.000  870.916    0.000 levels.py:293(generate)
               58203800  831.813    0.000  831.813    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               16949232  141.790    0.000  799.019    0.000 level.py:41(notUsed)
               58203800  122.818    0.000  779.847    0.000 layers.py:727(check)
                 582038  397.682    0.001  679.773    0.001 agent.py:67(modify)
                 582038    3.270    0.000  638.469    0.001 grad_mode.py:23(decorate_context)
                 582038   16.221    0.000  628.954    0.001 adam.py:55(step)
              911123299  422.881    0.000  616.544    0.000 allGraphs.py:46(p)
        13386874/1746114   51.470    0.000  548.720    0.000 module.py:715(_call_impl)
                 582038  114.707    0.000  542.171    0.001 functional.py:53(adam)
                1164076    2.880    0.000  502.753    0.000 network.py:24(forward)
                1164076   13.652    0.000  492.998    0.000 container.py:115(forward)
             7360291471  483.959    0.000  483.959    0.000 {built-in method builtins.hash}
               16949232   11.046    0.000  373.017    0.000 level.py:38(elementsIn)
                 582038    3.483    0.000  344.937    0.001 tensor.py:181(backward)
                 582038    1.962    0.000  341.453    0.001 __init__.py:68(backward)
                 582038  325.085    0.001  325.085    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               58203800   84.479    0.000  315.234    0.000 layers.py:721(isFree)
              160145817   85.829    0.000  295.019    0.000 {built-in method builtins.any}
                4656312  172.107    0.000  293.228    0.000 layer.py:167(NoRock_update)
                 582038    7.106    0.000  290.531    0.000 agent.py:112(__call__)
               60531952  284.633    0.000  284.633    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               16949232  116.142    0.000  240.094    0.000 level.py:39(<listcomp>)
              458602720  179.180    0.000  230.755    0.000 layer.py:95(isFree)
               58203800  132.970    0.000  217.561    0.000 layers.py:418(check)
              119899928   37.170    0.000  201.350    0.000 {built-in method builtins.all}
                1746114    6.871    0.000  195.780    0.000 tensor.py:576(__iter__)
                2328152    3.894    0.000  193.978    0.000 conv.py:422(forward)
                2328152    4.716    0.000  188.613    0.000 conv.py:414(_conv_forward)
                1746114  184.325    0.000  184.325    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
                2328152  183.122    0.000  183.122    0.000 {built-in method conv2d}
               22600464   15.800    0.000  174.761    0.000 layer.py:69(restart)
              803961413  171.855    0.000  171.855    0.000 level.py:32(inverse)
              101274746   49.411    0.000  159.400    0.000 overrides.py:1070(has_torch_function)
              913593918  152.035    0.000  156.103    0.000 {built-in method builtins.max}
              191883898   46.522    0.000  149.148    0.000 layers.py:682(<genexpr>)
               58203800   91.836    0.000  148.997    0.000 layers.py:446(check)
              498409578  120.541    0.000  147.724    0.000 layers.py:692(<genexpr>)
                2328152    5.167    0.000  146.485    0.000 linear.py:92(forward)
               58203800   87.405    0.000  140.629    0.000 layers.py:431(check)
                2328152    9.501    0.000  139.066    0.000 functional.py:1669(linear)
                2825158   67.894    0.000  134.359    0.000 layers.py:30(reset)
               32594182   84.884    0.000  132.525    0.000 tensor.py:933(grad)
                 582038   12.126    0.000  128.802    0.000 optimizer.py:167(zero_grad)
               16949232   75.886    0.000  121.877    0.000 {built-in method _functools.reduce}
              711875966  117.450    0.000  117.450    0.000 enum.py:352(<genexpr>)
                9312608  114.078    0.000  114.078    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                 582038   65.760    0.000  110.620    0.000 collector.py:46(collect)
             1228684371  108.106    0.000  108.106    0.000 layer.py:91(positions)
                2328152   99.692    0.000   99.692    0.000 {built-in method addmm}
                 582038    4.465    0.000   97.891    0.000 agent.py:59(modify_board)
                9312608   96.178    0.000   96.178    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               58203900   58.533    0.000   90.204    0.000 layers.py:107(isDone)
                2825058   40.733    0.000   80.499    0.000 level.py:16(<dictcomp>)
              163215528   57.509    0.000   78.887    0.000 layer.py:130(add)
              332929837   73.854    0.000   73.854    0.000 layer.py:146(elements)
                3492228    3.177    0.000   70.069    0.000 activation.py:713(forward)
               58203800   45.240    0.000   69.593    0.000 layers.py:396(check)
                3492228    5.056    0.000   66.891    0.000 functional.py:1292(leaky_relu)
               58203800   42.142    0.000   66.276    0.000 layers.py:407(check)
                 582038   62.633    0.000   62.633    0.000 {built-in method torch._C._nn.one_hot}
                3492228   61.380    0.000   61.380    0.000 {built-in method torch._C._nn.leaky_relu}
                4656304   61.285    0.000   61.285    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              266573672   51.433    0.000   61.108    0.000 overrides.py:1083(<genexpr>)
                 582038   40.840    0.000   59.924    0.000 allGraphsTrain.py:38(<listcomp>)
                4656304   56.073    0.000   56.073    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-2>
Subject: Job 9509263: <causal6_online_var_0> in cluster <dcc> Done

Job <causal6_online_var_0> was submitted from host <n-62-27-21> by user <s183905> in cluster <dcc> at Mon Apr 12 00:14:18 2021
Job was executed on host(s) <n-62-20-2>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Mon Apr 12 00:14:19 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Apr 12 00:14:19 2021
Terminated at Mon Apr 12 12:09:28 2021
Results reported at Mon Apr 12 12:09:28 2021

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

    CPU time :                                   42800.39 sec.
    Max Memory :                                 2087 MB
    Average Memory :                             2086.88 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14297.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   42910 sec.
    Turnaround time :                            42910 sec.

The output (if any) is above this job summary.


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-15>
Subject: Job 9509321: <causal6_online_var_0> in cluster <dcc> Exited

Job <causal6_online_var_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon Apr 12 04:00:46 2021
Job was executed on host(s) <n-62-20-15>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon Apr 12 04:00:48 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Apr 12 04:00:48 2021
Terminated at Mon Apr 12 15:56:31 2021
Results reported at Mon Apr 12 15:56:31 2021

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

Exited with exit code 120.

Resource usage summary:

    CPU time :                                   42801.91 sec.
    Max Memory :                                 2842 MB
    Average Memory :                             2577.61 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13542.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   42913 sec.
    Turnaround time :                            42945 sec.

The output (if any) is above this job summary.

