
# Parameters

    Name :                      Diamonds1_0.0_var-1
    Main :                      graphTrain
    Level :                     Levels.Causal2
    Failed actions chance :     0.0
    Hours :                     10.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.var
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


      23105130508 function calls (22512316783 primitive calls) in 35708.33 seconds

##    Ordered by: cumulative time
   List reduced from 463 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35708.328 35708.328 {built-in method builtins.exec}
                      1    0.001    0.001 35708.328 35708.328 <string>:1(<module>)
                      1  175.375  175.375 35708.328 35708.328 allGraphsTrain.py:10(graphTrain)
                 770616 5459.293    0.007 13214.456    0.017 allGraphs.py:146(transformNot)
              770622560 8681.809    0.000 8681.809    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                 770616   17.113    0.000 8326.949    0.011 allGraphsTrain.py:29(<listcomp>)
               77832317 1935.489    0.000 8309.880    0.000 allGraphs.py:110(states)
              693554800 6169.836    0.000 6169.836    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 770616    2.412    0.000 4323.170    0.006 game.py:41(step)
                 770616    3.744    0.000 4171.220    0.005 layers.py:718(step)
                 770616  679.953    0.001 2958.230    0.004 allGraphsTrain.py:35(<listcomp>)
                 770617  107.052    0.000 2417.417    0.003 layers.py:684(update)
               11820028   18.906    0.000 2278.277    0.000 allGraphs.py:158(getInterventions)
                 770616  133.680    0.000 2064.010    0.003 allGraphsTrain.py:37(<listcomp>)
                 770616   53.861    0.000 1745.955    0.002 layers.py:17(step)
               77061600  115.729    0.000 1685.166    0.000 layer.py:98(move)
                 770616    2.234    0.000 1572.868    0.002 agent.py:29(learn)
                 770616   14.864    0.000 1569.086    0.002 agent.py:117(_learn)
                 770616   45.745    0.000 1554.222    0.002 learner.py:42(Qlearn)
               18943441 1503.763    0.000 1503.763    0.000 {built-in method tensor}
                4139976   28.587    0.000 1465.274    0.000 layers.py:740(restart)
               15673109    8.518    0.000 1404.691    0.000 game.py:37(board)
               81685296  176.859    0.000 1255.300    0.000 tensor.py:21(wrapped)
                 770616   53.025    0.000 1188.843    0.002 allGraphsTrain.py:44(<listcomp>)
                4139976   14.253    0.000 1170.063    0.000 level.py:8(__init__)
               11193364    9.704    0.000 1157.627    0.000 allGraphs.py:129(rightIntervention)
        126744864/11193364   77.431    0.000 1107.329    0.000 {built-in method builtins.min}
               11820028   48.146    0.000 1092.374    0.000 allGraphs.py:153(format)
               31839008   12.760    0.000 1089.736    0.000 allGraphs.py:130(<lambda>)
        242296364/31839008  330.665    0.000 1076.976    0.000 allGraphs.py:74(expected_moves)
               77061600  224.566    0.000 1055.968    0.000 layers.py:735(check)
                4139976   41.283    0.000 1026.660    0.000 levels.py:151(generate)
               19871348  171.860    0.000  940.261    0.000 level.py:41(notUsed)
        326008856/74616690   89.805    0.000  903.764    0.000 allGraphs.py:78(<genexpr>)
               80914680  860.529    0.000  860.529    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               77061600  808.299    0.000  808.299    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
             3379498102  538.552    0.000  791.005    0.000 enum.py:646(__hash__)
                 770616  423.709    0.001  742.665    0.001 agent.py:67(modify)
                 770616    4.268    0.000  618.983    0.001 grad_mode.py:23(decorate_context)
        17724168/2311848   65.087    0.000  613.931    0.000 module.py:715(_call_impl)
                 770616   20.958    0.000  606.377    0.001 adam.py:55(step)
                1541232    3.568    0.000  560.611    0.000 network.py:27(forward)
                1541232   14.083    0.000  548.316    0.000 container.py:115(forward)
                 770616  112.652    0.000  497.332    0.001 functional.py:53(adam)
               19871348   13.541    0.000  439.815    0.000 level.py:38(elementsIn)
               77061600  102.932    0.000  401.758    0.000 layers.py:729(isFree)
                5394319  222.557    0.000  372.250    0.000 layer.py:167(NoRock_update)
              211632739  109.506    0.000  370.760    0.000 {built-in method builtins.any}
                 770616    3.890    0.000  364.291    0.000 tensor.py:181(backward)
                 770616    2.495    0.000  360.401    0.000 __init__.py:68(backward)
              127371528   71.118    0.000  346.771    0.000 allGraphs.py:83(layers_not_in)
                 770616  341.745    0.000  341.745    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                 770616    8.975    0.000  328.645    0.000 agent.py:112(__call__)
              530813193  229.855    0.000  298.826    0.000 layer.py:95(isFree)
               19871348  137.902    0.000  284.256    0.000 level.py:39(<listcomp>)
              127371528  134.712    0.000  275.652    0.000 allGraphs.py:84(<listcomp>)
              158746996   50.768    0.000  263.915    0.000 {built-in method builtins.all}
               28979832   21.217    0.000  257.013    0.000 layer.py:69(restart)
                2311848    8.274    0.000  254.795    0.000 tensor.py:576(__iter__)
             3379500659  252.453    0.000  252.453    0.000 {built-in method builtins.hash}
               80144064  249.553    0.000  249.553    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                2311848  241.093    0.000  241.093    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
                3082464    4.812    0.000  219.882    0.000 conv.py:422(forward)
                3082464    6.131    0.000  213.202    0.000 conv.py:414(_conv_forward)
              134087318   64.327    0.000  210.705    0.000 overrides.py:1070(has_torch_function)
                3082464  206.055    0.000  206.055    0.000 {built-in method conv2d}
               77061600  124.707    0.000  205.232    0.000 layers.py:219(check)
                4140076  102.338    0.000  203.977    0.000 layers.py:36(reset)
               77061600  122.524    0.000  202.388    0.000 layers.py:231(check)
              954074240  194.787    0.000  194.787    0.000 level.py:32(inverse)
              254329263   61.681    0.000  194.210    0.000 layers.py:690(<genexpr>)
               77061600  117.399    0.000  193.462    0.000 layers.py:207(check)
              583373792  144.619    0.000  177.505    0.000 layers.py:700(<genexpr>)
              242296364  115.547    0.000  170.370    0.000 allGraphs.py:45(p)
                3082464    6.705    0.000  161.528    0.000 linear.py:92(forward)
               43154550   94.337    0.000  157.306    0.000 tensor.py:933(grad)
                3082464   11.281    0.000  151.860    0.000 functional.py:1669(linear)
              864409157  146.319    0.000  146.319    0.000 enum.py:352(<genexpr>)
               19871348   88.832    0.000  142.018    0.000 {built-in method _functools.reduce}
             1542499507  141.643    0.000  141.643    0.000 layer.py:91(positions)
                 770616   13.008    0.000  136.620    0.000 optimizer.py:167(zero_grad)
               77061700   79.593    0.000  123.287    0.000 layers.py:113(isDone)
                4139976   58.406    0.000  119.846    0.000 level.py:16(<dictcomp>)
              226542711   83.296    0.000  113.931    0.000 layer.py:130(add)
                 770616    5.224    0.000  113.269    0.000 agent.py:59(modify_board)
                3082464  108.443    0.000  108.443    0.000 {built-in method addmm}
                 770616   62.691    0.000  108.017    0.000 collector.py:46(collect)
               12329856   99.674    0.000   99.674    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               77061600   63.533    0.000   98.336    0.000 layers.py:196(check)
              459752753   94.150    0.000   94.150    0.000 layer.py:146(elements)
              352942396   69.797    0.000   83.270    0.000 overrides.py:1083(<genexpr>)
               12329856   83.077    0.000   83.077    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                 770616   51.872    0.000   77.864    0.000 allGraphsTrain.py:43(<listcomp>)
               77061600   51.739    0.000   77.667    0.000 layers.py:23(check)
                 770616   74.785    0.000   74.785    0.000 {built-in method torch._C._nn.one_hot}
                4623696    3.727    0.000   71.988    0.000 activation.py:713(forward)
                4623696    6.059    0.000   68.261    0.000 functional.py:1292(leaky_relu)
                 770616   16.847    0.000   62.701    0.000 allGraphs.py:137(transform)
                4623696   61.619    0.000   61.619    0.000 {built-in method torch._C._nn.leaky_relu}
              751686027   60.319    0.000   60.319    0.000 {method 'append' of 'list' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9532035: <Diamonds1_0.0_var_1> in cluster <dcc> Done

Job <Diamonds1_0.0_var_1> was submitted from host <n-62-30-7> by user <s183905> in cluster <dcc> at Sat Apr 17 13:28:44 2021
Job was executed on host(s) <n-62-20-5>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Tue Apr 20 02:17:20 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue Apr 20 02:17:20 2021
Terminated at Tue Apr 20 12:12:33 2021
Results reported at Tue Apr 20 12:12:33 2021

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

    CPU time :                                   35619.76 sec.
    Max Memory :                                 2062 MB
    Average Memory :                             2061.14 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14322.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35715 sec.
    Turnaround time :                            254629 sec.

The output (if any) is above this job summary.

