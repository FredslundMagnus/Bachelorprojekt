
# Parameters

    Name :                      causal2_online_var_0.5-0
    Main :                      graphTrain
    Level :                     Levels.Causal2
    Failed actions chance :     0.5
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
    Counterfacts :              1
    Topn :                      7
    Minutes used :              715 minutes.
    Hours used :                11 hours.

# Profiling


      24488239521 function calls (23492575680 primitive calls) in 42906.09 seconds

##    Ordered by: cumulative time
   List reduced from 462 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 42906.090 42906.090 {built-in method builtins.exec}
                      1    0.001    0.001 42906.090 42906.090 <string>:1(<module>)
                      1  240.740  240.740 42906.088 42906.088 allGraphsTrain.py:10(graphTrain)
                 813532 6215.372    0.008 15581.425    0.019 allGraphs.py:120(transformNot)
              813538904 11047.003    0.000 11047.003    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                 813532   20.300    0.000 9823.436    0.012 allGraphsTrain.py:29(<listcomp>)
               82166833 2160.675    0.000 9803.148    0.000 allGraphs.py:88(states)
              732179200 6870.500    0.000 6870.500    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 813532  897.875    0.001 4718.579    0.006 allGraphsTrain.py:35(<listcomp>)
                 813532    3.937    0.000 4494.309    0.006 game.py:41(step)
                 813532    5.952    0.000 4312.124    0.005 layers.py:712(step)
               17064293   88.410    0.000 3820.704    0.000 allGraphs.py:127(getInterventions)
                 813533  130.697    0.000 2713.070    0.003 layers.py:678(update)
                 813532  151.087    0.000 2413.550    0.003 allGraphsTrain.py:37(<listcomp>)
               24582259 2188.881    0.000 2188.881    0.000 {built-in method tensor}
               21131954   11.712    0.000 2071.702    0.000 game.py:37(board)
               16129100   14.090    0.000 2064.007    0.000 allGraphs.py:107(rightIntervention)
        210437982/16129100  135.416    0.000 1985.348    0.000 {built-in method builtins.min}
               48982394   21.274    0.000 1956.980    0.000 allGraphs.py:108(<lambda>)
                 813532    4.041    0.000 1936.657    0.002 agent.py:29(learn)
        404746864/48982394  607.754    0.000 1935.707    0.000 allGraphs.py:52(expected_moves)
                 813532   19.294    0.000 1930.584    0.002 agent.py:117(_learn)
                 813532   59.765    0.000 1911.290    0.002 learner.py:42(Qlearn)
        550073352/120753886  157.948    0.000 1643.188    0.000 allGraphs.py:56(<genexpr>)
                 813532   72.299    0.000 1587.032    0.002 layers.py:17(step)
               81353200  140.285    0.000 1506.955    0.000 layer.py:98(move)
                3747275   30.923    0.000 1476.713    0.000 layers.py:734(restart)
               86234392  213.413    0.000 1460.533    0.000 tensor.py:21(wrapped)
                 813532   67.179    0.000 1380.636    0.002 allGraphsTrain.py:44(<listcomp>)
                3747275   15.847    0.000 1176.848    0.000 level.py:8(__init__)
                3747275   43.640    0.000 1025.705    0.000 levels.py:151(generate)
               85420860  991.656    0.000  991.656    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               17987821  169.728    0.000  935.906    0.000 level.py:41(notUsed)
             3782943028  640.059    0.000  931.073    0.000 enum.py:646(__hash__)
                 813532  486.463    0.001  890.495    0.001 agent.py:67(modify)
               81353200  886.231    0.000  886.231    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
        18711236/2440596   87.508    0.000  793.587    0.000 module.py:715(_call_impl)
                 813532    6.610    0.000  730.173    0.001 grad_mode.py:23(decorate_context)
                1627064    4.766    0.000  716.560    0.000 network.py:24(forward)
                 813532   27.686    0.000  711.217    0.001 adam.py:55(step)
                1627064   19.656    0.000  699.581    0.000 container.py:115(forward)
               81353200  184.758    0.000  671.462    0.000 layers.py:729(check)
              211373175  126.007    0.000  606.130    0.000 allGraphs.py:61(layers_not_in)
                 813532  129.749    0.000  581.376    0.001 functional.py:53(adam)
               81353200  129.882    0.000  557.551    0.000 layers.py:723(isFree)
              211373175  238.177    0.000  480.123    0.000 allGraphs.py:62(<listcomp>)
                 813532    5.494    0.000  469.191    0.001 tensor.py:181(backward)
                 813532    4.048    0.000  463.697    0.001 __init__.py:68(backward)
               17987821   13.580    0.000  441.004    0.000 level.py:38(elementsIn)
                 813532   13.775    0.000  439.749    0.001 agent.py:112(__call__)
              224041920  126.549    0.000  439.161    0.000 {built-in method builtins.any}
                 813532  437.864    0.001  437.864    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                5694731  258.385    0.000  436.817    0.000 layer.py:167(NoRock_update)
              542438440  356.877    0.000  427.669    0.000 layer.py:95(isFree)
              167587692   76.894    0.000  414.800    0.000 {built-in method builtins.all}
              496402453  138.080    0.000  315.704    0.000 layers.py:684(<genexpr>)
                2440596   10.781    0.000  308.071    0.000 tensor.py:576(__iter__)
              404746864  212.541    0.000  307.729    0.000 allGraphs.py:37(p)
             3782945713  291.014    0.000  291.014    0.000 {built-in method builtins.hash}
                2440596  290.382    0.000  290.382    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               17987821  141.184    0.000  284.253    0.000 level.py:39(<listcomp>)
                3254128    6.894    0.000  283.514    0.000 conv.py:422(forward)
               84607328  280.669    0.000  280.669    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                3254128    8.169    0.000  273.627    0.000 conv.py:414(_conv_forward)
                3254128  264.004    0.000  264.004    0.000 {built-in method conv2d}
               26230925   21.740    0.000  259.552    0.000 layer.py:69(restart)
              141554702   74.382    0.000  242.551    0.000 overrides.py:1070(has_torch_function)
              620848200  177.225    0.000  215.727    0.000 layers.py:694(<genexpr>)
                3254128    8.835    0.000  205.530    0.000 linear.py:92(forward)
                3747375   99.858    0.000  200.323    0.000 layers.py:30(reset)
              863639735  194.250    0.000  194.250    0.000 level.py:32(inverse)
                3254128   14.516    0.000  192.230    0.000 functional.py:1669(linear)
               45557846  108.979    0.000  180.934    0.000 tensor.py:933(grad)
                 813532   15.295    0.000  155.602    0.000 optimizer.py:167(zero_grad)
               81353300  102.119    0.000  152.701    0.000 layers.py:107(isDone)
                 813532    7.021    0.000  147.343    0.000 agent.py:59(modify_board)
              782464946  144.296    0.000  144.296    0.000 enum.py:352(<genexpr>)
               17987821   89.749    0.000  143.170    0.000 {built-in method _functools.reduce}
                3254128  138.118    0.000  138.118    0.000 {built-in method addmm}
                 813532   74.859    0.000  127.822    0.000 collector.py:46(collect)
               40678707   79.571    0.000  126.111    0.000 layers.py:213(check)
                3747275   63.929    0.000  125.879    0.000 level.py:16(<dictcomp>)
               40678278   78.163    0.000  125.208    0.000 layers.py:225(check)
               40686035   76.589    0.000  123.016    0.000 layers.py:201(check)
              213850229   87.217    0.000  122.541    0.000 layer.py:130(add)
               13016512  116.221    0.000  116.221    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              435357940  113.730    0.000  113.730    0.000 layer.py:146(elements)
             1015289969  101.384    0.000  101.384    0.000 layer.py:91(positions)
                 813532   69.762    0.000  100.194    0.000 allGraphsTrain.py:43(<listcomp>)
                 813532   97.953    0.000   97.953    0.000 {built-in method torch._C._nn.one_hot}
              372597924   80.533    0.000   96.214    0.000 overrides.py:1083(<genexpr>)
               13016512   95.346    0.000   95.346    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                4881192    5.854    0.000   89.552    0.000 activation.py:713(forward)
              408122653   79.717    0.000   84.719    0.000 {built-in method builtins.max}
                4881192    8.907    0.000   83.698    0.000 functional.py:1292(leaky_relu)
                 813532   20.619    0.000   79.547    0.000 allGraphs.py:111(transform)
                4881192   73.998    0.000   73.998    0.000 {built-in method torch._C._nn.leaky_relu}
                2440596   69.028    0.000   69.028    0.000 {method 'tolist' of 'torch._C._TensorBase' objects}
                6508256   66.913    0.000   66.913    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              731171429   66.884    0.000   66.884    0.000 {method 'append' of 'list' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-12>
Subject: Job 9511306: <causal2_online_var_0.5_0> in cluster <dcc> Done

Job <causal2_online_var_0.5_0> was submitted from host <n-62-27-21> by user <s183905> in cluster <dcc> at Mon Apr 12 16:10:31 2021
Job was executed on host(s) <n-62-20-12>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Mon Apr 12 16:25:23 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Apr 12 16:25:23 2021
Terminated at Tue Apr 13 04:20:36 2021
Results reported at Tue Apr 13 04:20:36 2021

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

    CPU time :                                   42795.95 sec.
    Max Memory :                                 2085 MB
    Average Memory :                             2084.59 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14299.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   42914 sec.
    Turnaround time :                            43805 sec.

The output (if any) is above this job summary.

