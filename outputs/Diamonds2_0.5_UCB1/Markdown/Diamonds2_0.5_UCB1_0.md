
# Parameters

    Name :                      Diamonds2_0.5_UCB1-0
    Main :                      graphTrain
    Level :                     Levels.Causal5
    Failed actions chance :     0.5
    Hours :                     10.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.UCB1
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
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                3
    Counterfacts :              2
    Topn :                      5
    Random counterfacts :       False
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      49588310906 function calls (44029910613 primitive calls) in 35710.81 seconds

##    Ordered by: cumulative time
   List reduced from 464 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35710.808 35710.808 {built-in method builtins.exec}
                      1    0.001    0.001 35710.808 35710.808 <string>:1(<module>)
                      1  133.927  133.927 35710.807 35710.807 allGraphsTrain.py:10(graphTrain)
                 343596  412.041    0.001 14082.870    0.041 allGraphsTrain.py:35(<listcomp>)
                7054433   12.421    0.000 13670.828    0.002 allGraphs.py:158(getInterventions)
                7054433    7.870    0.000 12728.614    0.002 allGraphs.py:133(UCB1)
        954011552/7054433  572.919    0.000 12682.315    0.002 {built-in method builtins.min}
               26453966   13.087    0.000 12665.468    0.000 allGraphs.py:134(<lambda>)
        1900968671/26453966 3319.230    0.000 12652.381    0.000 allGraphs.py:68(expected_moves_UCB1)
        2821471824/91415658  890.551    0.000 12416.517    0.000 allGraphs.py:72(<genexpr>)
                 343596 3851.164    0.011 9492.134    0.028 allGraphs.py:146(transformNot)
              481037744 6513.816    0.000 6513.816    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                 343596   10.763    0.000 6388.783    0.019 allGraphsTrain.py:29(<listcomp>)
               34703297 1419.022    0.000 6378.074    0.000 allGraphs.py:110(states)
              446675400 4442.141    0.000 4442.141    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
              954011552  589.858    0.000 3611.191    0.000 allGraphs.py:83(layers_not_in)
            14028273883 2300.982    0.000 3359.921    0.000 enum.py:646(__hash__)
              954011552 1445.858    0.000 3021.333    0.000 allGraphs.py:84(<listcomp>)
             1900968671 1790.203    0.000 2819.278    0.000 allGraphs.py:60(UCB1)
                 343596    2.133    0.000 1920.805    0.006 game.py:41(step)
                 343596    2.880    0.000 1824.809    0.005 layers.py:718(step)
               10247999 1189.444    0.000 1189.444    0.000 {built-in method tensor}
                8772414    7.717    0.000 1115.090    0.000 game.py:37(board)
                 343596   70.007    0.000 1072.770    0.003 allGraphsTrain.py:37(<listcomp>)
            14028275064 1058.939    0.000 1058.939    0.000 {built-in method builtins.hash}
                 343597   56.110    0.000  960.072    0.003 layers.py:684(update)
                7054433   43.177    0.000  929.793    0.000 allGraphs.py:153(format)
                 343596    2.299    0.000  882.467    0.003 agent.py:29(learn)
                 343596   10.441    0.000  879.206    0.003 agent.py:117(_learn)
                 343596   27.929    0.000  868.764    0.003 learner.py:42(Qlearn)
                 343596   34.266    0.000  858.477    0.002 layers.py:17(step)
               34359600   61.165    0.000  820.789    0.000 layer.py:98(move)
               36421176   89.887    0.000  631.761    0.000 tensor.py:21(wrapped)
                 343596   28.560    0.000  593.325    0.002 allGraphsTrain.py:44(<listcomp>)
                 835810    9.884    0.000  435.909    0.001 layers.py:740(restart)
               36077580  432.629    0.000  432.629    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               34359600   98.669    0.000  414.365    0.000 layers.py:735(check)
               34359600  404.532    0.000  404.532    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                 343596  205.589    0.001  395.938    0.001 agent.py:67(modify)
        7902708/1030788   41.771    0.000  383.509    0.000 module.py:715(_call_impl)
             1901999459  365.411    0.000  365.411    0.000 {built-in method builtins.max}
                 835810    5.016    0.000  358.534    0.000 level.py:8(__init__)
             1900738892  356.393    0.000  356.393    0.000 {built-in method math.log}
                 687192    2.773    0.000  346.426    0.001 network.py:27(forward)
                 687192    9.814    0.000  337.273    0.000 container.py:115(forward)
                 343596    3.316    0.000  320.634    0.001 grad_mode.py:23(decorate_context)
                 835810   13.612    0.000  320.428    0.000 levels.py:249(generate)
                 343596   12.638    0.000  311.375    0.001 adam.py:55(step)
                5432588   52.335    0.000  292.346    0.000 level.py:41(notUsed)
               34359600   67.758    0.000  285.187    0.000 layers.py:729(isFree)
                 343596   57.418    0.000  254.546    0.001 functional.py:53(adam)
                3092373  123.314    0.000  217.514    0.000 layer.py:167(NoRock_update)
              302806194  180.265    0.000  217.428    0.000 layer.py:95(isFree)
                 343596    8.314    0.000  216.730    0.001 agent.py:112(__call__)
                 343596    2.492    0.000  215.249    0.001 tensor.py:181(backward)
                 343596    1.952    0.000  212.757    0.001 __init__.py:68(backward)
             1903487795  212.095    0.000  212.095    0.000 {built-in method math.sqrt}
               95371305   59.620    0.000  211.507    0.000 {built-in method builtins.any}
                 343596  200.460    0.001  200.460    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                1030788    6.785    0.000  157.498    0.000 tensor.py:576(__iter__)
                1030788  146.324    0.000  146.324    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
                1374384    3.191    0.000  140.107    0.000 conv.py:422(forward)
                1374384    4.808    0.000  135.602    0.000 conv.py:414(_conv_forward)
                5432588    4.167    0.000  135.564    0.000 level.py:38(elementsIn)
                1374384  130.200    0.000  130.200    0.000 {built-in method conv2d}
               35733984  127.414    0.000  127.414    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               70780876   25.649    0.000  118.272    0.000 {built-in method builtins.all}
              335238900   90.242    0.000  110.978    0.000 layers.py:700(<genexpr>)
               59785838   31.945    0.000  103.875    0.000 overrides.py:1070(has_torch_function)
                1374384    3.963    0.000   99.063    0.000 linear.py:92(forward)
                1374384    7.156    0.000   93.189    0.000 functional.py:1669(linear)
                5432588   43.626    0.000   87.757    0.000 level.py:39(<listcomp>)
              121576997   33.367    0.000   82.921    0.000 layers.py:690(<genexpr>)
               19241430   46.626    0.000   77.221    0.000 tensor.py:933(grad)
                 343596    3.972    0.000   72.096    0.000 agent.py:59(modify_board)
                 343596    6.802    0.000   67.468    0.000 optimizer.py:167(zero_grad)
                1374384   66.909    0.000   66.909    0.000 {built-in method addmm}
                7522290    6.656    0.000   64.951    0.000 layer.py:69(restart)
              256220094   63.882    0.000   63.882    0.000 level.py:32(inverse)
                 343596   33.692    0.000   58.549    0.000 collector.py:46(collect)
              132168827   57.395    0.000   57.395    0.000 layer.py:146(elements)
               17178425   36.589    0.000   56.447    0.000 layers.py:349(check)
               17179540   34.458    0.000   54.591    0.000 layers.py:387(check)
              523851298   54.302    0.000   54.302    0.000 layer.py:91(positions)
               17180044   34.501    0.000   53.955    0.000 layers.py:375(check)
               17183623   32.858    0.000   52.701    0.000 layers.py:337(check)
                5497536   50.528    0.000   50.528    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                 343596   46.880    0.000   46.880    0.000 {built-in method torch._C._nn.one_hot}
                 343596   33.606    0.000   46.639    0.000 allGraphsTrain.py:43(<listcomp>)
                 835910   22.871    0.000   45.541    0.000 layers.py:36(reset)
                5432588   27.178    0.000   43.640    0.000 {built-in method _functools.reduce}
              225663893   42.907    0.000   42.907    0.000 enum.py:352(<genexpr>)
                 343596   11.721    0.000   42.360    0.000 allGraphs.py:137(transform)
                2061576    3.101    0.000   42.224    0.000 activation.py:713(forward)
                5497536   41.420    0.000   41.420    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              157367236   34.202    0.000   40.632    0.000 overrides.py:1083(<genexpr>)
               63326205   27.927    0.000   39.219    0.000 layer.py:130(add)
                2061576    4.746    0.000   39.123    0.000 functional.py:1292(leaky_relu)
                1030788   34.961    0.000   34.961    0.000 {method 'tolist' of 'torch._C._TensorBase' objects}
                2061576   34.012    0.000   34.012    0.000 {built-in method torch._C._nn.leaky_relu}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9531985: <Diamonds2_0.5_UCB1_0> in cluster <dcc> Done

Job <Diamonds2_0.5_UCB1_0> was submitted from host <n-62-30-7> by user <s183905> in cluster <dcc> at Sat Apr 17 13:24:03 2021
Job was executed on host(s) <n-62-20-10>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sat Apr 17 13:24:04 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat Apr 17 13:24:04 2021
Terminated at Sat Apr 17 23:19:30 2021
Results reported at Sat Apr 17 23:19:30 2021

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
#BSUB -W 720
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $LSB_PROJECT_NAME


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   35616.67 sec.
    Max Memory :                                 2064 MB
    Average Memory :                             2056.71 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14320.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35762 sec.
    Turnaround time :                            35727 sec.

The output (if any) is above this job summary.

