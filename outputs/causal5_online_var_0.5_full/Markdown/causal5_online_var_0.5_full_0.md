
# Parameters

    Name :                      causal5_online_var_0.5_full-0
    Main :                      graphTrain
    Level :                     Levels.Causal5
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
    Cf convert :                3
    Counterfacts :              2
    Topn :                      5
    Minutes used :              715 minutes.
    Hours used :                11 hours.

# Profiling


      56259632061 function calls (49568180568 primitive calls) in 42902.96 seconds

##    Ordered by: cumulative time
   List reduced from 466 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 42902.958 42902.958 {built-in method builtins.exec}
                      1    0.001    0.001 42902.958 42902.958 <string>:1(<module>)
                      1  137.550  137.550 42902.957 42902.957 allGraphsTrain.py:10(graphTrain)
                 466555  534.048    0.001 14872.627    0.032 allGraphsTrain.py:35(<listcomp>)
                9711651   55.593    0.000 14338.579    0.001 allGraphs.py:127(getInterventions)
                8865686    7.952    0.000 13116.972    0.001 allGraphs.py:107(rightIntervention)
        1149131946/8865686  627.588    0.000 13063.694    0.001 {built-in method builtins.min}
               32717048   15.216    0.000 13045.439    0.000 allGraphs.py:108(<lambda>)
        2289398206/32717048 3794.680    0.000 13030.223    0.000 allGraphs.py:52(expected_moves)
        3396947418/111774826  994.193    0.000 12787.265    0.000 allGraphs.py:56(<genexpr>)
                 466555 4932.618    0.011 12447.452    0.027 allGraphs.py:120(transformNot)
              653181328 8980.414    0.000 8980.414    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                 466555   12.344    0.000 8450.512    0.018 allGraphsTrain.py:29(<listcomp>)
               47122156 1842.045    0.000 8438.186    0.000 allGraphs.py:88(states)
              606522100 5632.898    0.000 5632.898    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
             1149977911  636.048    0.000 4164.662    0.000 allGraphs.py:61(layers_not_in)
            17007348657 2686.098    0.000 4041.548    0.000 enum.py:646(__hash__)
             1149977911 1667.192    0.000 3528.615    0.000 allGraphs.py:62(<listcomp>)
                 466555    2.086    0.000 2412.374    0.005 game.py:41(step)
                 466555    2.632    0.000 2301.340    0.005 layers.py:718(step)
             2289398206 1188.033    0.000 1756.758    0.000 allGraphs.py:37(p)
               14036588 1509.112    0.000 1509.112    0.000 {built-in method tensor}
               12044427    6.856    0.000 1430.676    0.000 game.py:37(board)
                 466555   88.964    0.000 1402.694    0.003 allGraphsTrain.py:37(<listcomp>)
            17007350222 1355.450    0.000 1355.450    0.000 {built-in method builtins.hash}
                 466556   69.781    0.000 1217.937    0.003 layers.py:684(update)
                 466555   40.010    0.000 1077.457    0.002 layers.py:17(step)
                 466555    1.995    0.000 1076.839    0.002 agent.py:29(learn)
                 466555   10.522    0.000 1073.793    0.002 agent.py:117(_learn)
                 466555   32.690    0.000 1063.271    0.002 learner.py:42(Qlearn)
               46655500   77.568    0.000 1032.588    0.000 layer.py:98(move)
               49454830  118.125    0.000  829.108    0.000 tensor.py:21(wrapped)
                 466555   37.263    0.000  785.756    0.002 allGraphsTrain.py:44(<listcomp>)
               48988275  564.013    0.000  564.013    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                1106192   11.142    0.000  558.930    0.001 layers.py:740(restart)
               46655500  131.572    0.000  541.520    0.000 layers.py:735(check)
               46655500  512.793    0.000  512.793    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                 466555  249.180    0.001  470.204    0.001 agent.py:67(modify)
                1106192    5.360    0.000  460.891    0.000 level.py:8(__init__)
        10730765/1399665   48.945    0.000  441.065    0.000 module.py:715(_call_impl)
             2291643836  415.852    0.000  421.068    0.000 {built-in method builtins.max}
                1106192   17.320    0.000  416.829    0.000 levels.py:249(generate)
                 466555    3.273    0.000  409.216    0.001 grad_mode.py:23(decorate_context)
                 933110    2.650    0.000  400.497    0.000 network.py:24(forward)
                 466555   14.586    0.000  399.407    0.001 adam.py:55(step)
                 933110   10.775    0.000  391.058    0.000 container.py:115(forward)
                7189040   67.398    0.000  380.869    0.000 level.py:41(notUsed)
               46655500   83.328    0.000  335.707    0.000 layers.py:729(isFree)
                 466555   72.288    0.000  325.390    0.001 functional.py:53(adam)
              129529443   78.105    0.000  285.919    0.000 {built-in method builtins.any}
                4199004  146.877    0.000  264.871    0.000 layer.py:167(NoRock_update)
                 466555    2.872    0.000  256.634    0.001 tensor.py:181(backward)
                 466555    2.263    0.000  253.761    0.001 __init__.py:68(backward)
              398279170  201.211    0.000  252.379    0.000 layer.py:95(isFree)
                 466555    7.608    0.000  244.600    0.001 agent.py:112(__call__)
                 466555  239.863    0.001  239.863    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                7189040    5.260    0.000  178.519    0.000 level.py:38(elementsIn)
                1399665    6.334    0.000  176.460    0.000 tensor.py:576(__iter__)
                1399665  166.058    0.000  166.058    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               48521720  162.653    0.000  162.653    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                1866220    3.805    0.000  157.043    0.000 conv.py:422(forward)
                1866220    4.825    0.000  151.770    0.000 conv.py:414(_conv_forward)
              455494080  120.960    0.000  149.718    0.000 layers.py:700(<genexpr>)
               96110430   32.546    0.000  148.423    0.000 {built-in method builtins.all}
                1866220  146.222    0.000  146.222    0.000 {built-in method conv2d}
               81180704   41.912    0.000  140.133    0.000 overrides.py:1070(has_torch_function)
                7189040   54.875    0.000  116.035    0.000 level.py:39(<listcomp>)
                1866220    4.643    0.000  115.295    0.000 linear.py:92(forward)
                1866220    8.712    0.000  108.408    0.000 functional.py:1669(linear)
               26127134   63.509    0.000  105.573    0.000 tensor.py:933(grad)
              147454822   40.594    0.000  102.079    0.000 layers.py:690(<genexpr>)
                 466555    8.683    0.000   90.249    0.000 optimizer.py:167(zero_grad)
                9955728    8.904    0.000   83.354    0.000 layer.py:69(restart)
              339064441   82.713    0.000   82.713    0.000 level.py:32(inverse)
                 466555    3.806    0.000   80.273    0.000 agent.py:59(modify_board)
                1866220   77.323    0.000   77.323    0.000 {built-in method addmm}
              711971828   73.721    0.000   73.721    0.000 layer.py:91(positions)
               23329244   43.586    0.000   71.465    0.000 layers.py:349(check)
               23329416   44.002    0.000   71.309    0.000 layers.py:387(check)
                 466555   41.532    0.000   70.934    0.000 collector.py:46(collect)
               23332023   41.950    0.000   69.019    0.000 layers.py:375(check)
               23326045   41.393    0.000   68.803    0.000 layers.py:337(check)
              177362891   67.992    0.000   67.992    0.000 layer.py:146(elements)
                7464880   65.523    0.000   65.523    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                1106292   29.381    0.000   60.339    0.000 layers.py:36(reset)
              213682458   48.125    0.000   57.721    0.000 overrides.py:1083(<genexpr>)
                7189040   35.489    0.000   57.224    0.000 {built-in method _functools.reduce}
              298629914   54.390    0.000   54.390    0.000 enum.py:352(<genexpr>)
                7464880   53.988    0.000   53.988    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                 466555   53.439    0.000   53.439    0.000 {built-in method torch._C._nn.one_hot}
                 466555   35.795    0.000   53.359    0.000 allGraphsTrain.py:43(<listcomp>)
               84921818   36.531    0.000   51.000    0.000 layer.py:130(add)
                2799330    2.918    0.000   49.602    0.000 activation.py:713(forward)
                2799330    4.735    0.000   46.684    0.000 functional.py:1292(leaky_relu)
                 466555   11.855    0.000   44.737    0.000 allGraphs.py:111(transform)
              398279170   42.775    0.000   42.775    0.000 layer.py:203(isBlocking)
        490580249/490580247   34.550    0.000   42.352    0.000 {built-in method builtins.len}
              484406370   41.943    0.000   41.943    0.000 {method 'random' of '_random.Random' objects}
                2799330   41.520    0.000   41.520    0.000 {built-in method torch._C._nn.leaky_relu}
              398435469   40.097    0.000   40.097    0.000 {method 'append' of 'list' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-10>
Subject: Job 9511704: <causal5_online_var_0.5_full_0> in cluster <dcc> Done

Job <causal5_online_var_0.5_full_0> was submitted from host <n-62-27-18> by user <s183905> in cluster <dcc> at Mon Apr 12 21:45:53 2021
Job was executed on host(s) <n-62-20-10>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Tue Apr 13 06:54:20 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue Apr 13 06:54:20 2021
Terminated at Tue Apr 13 18:49:27 2021
Results reported at Tue Apr 13 18:49:27 2021

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

    CPU time :                                   42798.69 sec.
    Max Memory :                                 2080 MB
    Average Memory :                             2079.55 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14304.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   42923 sec.
    Turnaround time :                            75814 sec.

The output (if any) is above this job summary.

