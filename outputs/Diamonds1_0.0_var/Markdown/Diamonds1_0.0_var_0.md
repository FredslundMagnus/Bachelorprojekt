
# Parameters

    Name :                      Diamonds1_0.0_var-0
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


      16148694991 function calls (15758146376 primitive calls) in 35710.05 seconds

##    Ordered by: cumulative time
   List reduced from 464 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35710.051 35710.051 {built-in method builtins.exec}
                      1    0.001    0.001 35710.051 35710.051 <string>:1(<module>)
                      1  145.889  145.889 35710.050 35710.050 allGraphsTrain.py:10(graphTrain)
                 541777 6384.229    0.012 14312.982    0.026 allGraphs.py:146(transformNot)
                 541777   16.169    0.000 8671.935    0.016 allGraphsTrain.py:29(<listcomp>)
               54719578 2267.465    0.000 8655.793    0.000 allGraphs.py:110(states)
              541781728 7993.000    0.000 7993.000    0.000 {method 'item' of 'torch._C._TensorBase' objects}
              487599700 7000.169    0.000 7000.169    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 541777    2.091    0.000 3509.960    0.006 game.py:41(step)
                 541777    2.759    0.000 3383.112    0.006 layers.py:718(step)
                 541777  658.317    0.001 2382.680    0.004 allGraphsTrain.py:35(<listcomp>)
                 541777  159.790    0.000 2141.879    0.004 allGraphsTrain.py:37(<listcomp>)
                 541778   81.112    0.000 1962.733    0.004 layers.py:684(update)
                8034590   15.974    0.000 1724.362    0.000 allGraphs.py:158(getInterventions)
                 541777    2.110    0.000 1592.774    0.003 agent.py:29(learn)
                 541777   12.057    0.000 1589.470    0.003 agent.py:117(_learn)
                 541777   45.135    0.000 1577.413    0.003 learner.py:42(Qlearn)
                 541777   41.586    0.000 1414.492    0.003 layers.py:17(step)
               54177700   93.965    0.000 1367.102    0.000 layer.py:98(move)
               57428362  159.932    0.000 1316.401    0.000 tensor.py:21(wrapped)
                 541777   56.063    0.000 1262.279    0.002 allGraphsTrain.py:44(<listcomp>)
               13052118 1141.097    0.000 1141.097    0.000 {built-in method tensor}
                2764887   22.457    0.000 1121.259    0.000 layers.py:740(restart)
               10743476    7.323    0.000 1052.941    0.000 game.py:37(board)
               56886585  974.108    0.000  974.108    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                2764887   10.642    0.000  897.867    0.000 level.py:8(__init__)
               54177700  890.571    0.000  890.571    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                7332947    7.208    0.000  879.380    0.000 allGraphs.py:129(rightIntervention)
               54177700  183.919    0.000  863.442    0.000 layers.py:735(check)
        83281237/7332947   57.272    0.000  840.847    0.000 {built-in method builtins.min}
               20860799    9.830    0.000  826.940    0.000 allGraphs.py:130(<lambda>)
                8034590   40.548    0.000  817.887    0.000 allGraphs.py:153(format)
        159229527/20860799  251.433    0.000  817.110    0.000 allGraphs.py:74(expected_moves)
                2764887   32.332    0.000  787.852    0.000 levels.py:151(generate)
               13272307  128.782    0.000  720.899    0.000 level.py:41(notUsed)
                 541777  419.347    0.001  711.023    0.001 agent.py:67(modify)
        214317018/48921344   66.783    0.000  685.747    0.000 allGraphs.py:78(<genexpr>)
                 541777    3.632    0.000  671.807    0.001 grad_mode.py:23(decorate_context)
                 541777   17.091    0.000  661.764    0.001 adam.py:55(step)
             2288712137  420.902    0.000  629.600    0.000 enum.py:646(__hash__)
        12460871/1625331   55.694    0.000  570.943    0.000 module.py:715(_call_impl)
                 541777  120.520    0.000  568.591    0.001 functional.py:53(adam)
                1083554    3.115    0.000  522.846    0.000 network.py:27(forward)
                1083554   13.188    0.000  512.125    0.000 container.py:115(forward)
                 541777    3.189    0.000  355.452    0.001 tensor.py:181(backward)
                 541777    2.170    0.000  352.263    0.001 __init__.py:68(backward)
               13272307   10.037    0.000  343.068    0.000 level.py:38(elementsIn)
                 541777  334.853    0.001  334.853    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               54177700   82.245    0.000  319.598    0.000 layers.py:729(isFree)
              148932908   86.072    0.000  309.540    0.000 {built-in method builtins.any}
                 541777    7.665    0.000  301.641    0.001 agent.py:112(__call__)
               56344808  299.102    0.000  299.102    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                3792446  173.555    0.000  294.391    0.000 layer.py:167(NoRock_update)
              111606162   54.743    0.000  291.926    0.000 {built-in method builtins.all}
               83982880   53.893    0.000  263.098    0.000 allGraphs.py:83(layers_not_in)
              364645600  185.423    0.000  237.353    0.000 layer.py:95(isFree)
               13272307  107.263    0.000  225.440    0.000 level.py:39(<listcomp>)
              331237215   97.731    0.000  219.287    0.000 layers.py:690(<genexpr>)
               83982880  102.491    0.000  209.205    0.000 allGraphs.py:84(<listcomp>)
             2288713958  208.698    0.000  208.698    0.000 {built-in method builtins.hash}
                2167108    4.077    0.000  200.508    0.000 conv.py:422(forward)
                1625331    6.993    0.000  199.757    0.000 tensor.py:576(__iter__)
                2167108    4.617    0.000  194.956    0.000 conv.py:414(_conv_forward)
               19354209   14.869    0.000  193.573    0.000 layer.py:69(restart)
                2167108  189.361    0.000  189.361    0.000 {built-in method conv2d}
                1625331  187.988    0.000  187.988    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               94269332   52.908    0.000  173.032    0.000 overrides.py:1070(has_torch_function)
               54177700   96.900    0.000  165.131    0.000 layers.py:231(check)
               54177700   97.156    0.000  163.725    0.000 layers.py:207(check)
               54177700   95.454    0.000  161.366    0.000 layers.py:219(check)
                2764987   75.488    0.000  155.413    0.000 layers.py:36(reset)
              411303304  122.273    0.000  152.892    0.000 layers.py:700(<genexpr>)
                2167108    5.220    0.000  151.660    0.000 linear.py:92(forward)
              637234064  147.590    0.000  147.590    0.000 level.py:32(inverse)
                2167108    9.344    0.000  143.913    0.000 functional.py:1669(linear)
               30339566   90.005    0.000  142.890    0.000 tensor.py:933(grad)
                 541777   12.480    0.000  137.256    0.000 optimizer.py:167(zero_grad)
              159229527   90.690    0.000  131.893    0.000 allGraphs.py:45(p)
             1083886037  125.663    0.000  125.663    0.000 layer.py:91(positions)
                8668432  118.867    0.000  118.867    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                 541777   68.645    0.000  115.133    0.000 collector.py:46(collect)
              577340477  110.276    0.000  110.276    0.000 enum.py:352(<genexpr>)
               13272307   66.989    0.000  107.591    0.000 {built-in method _functools.reduce}
                2167108  103.604    0.000  103.604    0.000 {built-in method addmm}
               54177800   64.289    0.000  101.906    0.000 layers.py:113(isDone)
                8668432  100.649    0.000  100.649    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                 541777    4.420    0.000   98.554    0.000 agent.py:59(modify_board)
                2764887   45.088    0.000   92.095    0.000 level.py:16(<dictcomp>)
              153496541   64.516    0.000   89.475    0.000 layer.py:130(add)
               54177700   49.833    0.000   79.530    0.000 layers.py:196(check)
              311828614   74.688    0.000   74.688    0.000 layer.py:146(elements)
                3250662    3.006    0.000   72.767    0.000 activation.py:713(forward)
              248134134   58.810    0.000   70.196    0.000 overrides.py:1083(<genexpr>)
                3250662    5.194    0.000   69.761    0.000 functional.py:1292(leaky_relu)
               54177700   42.442    0.000   64.940    0.000 layers.py:23(check)
                4334216   64.819    0.000   64.819    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                3250662   64.092    0.000   64.092    0.000 {built-in method torch._C._nn.leaky_relu}
                 541777   62.180    0.000   62.180    0.000 {built-in method torch._C._nn.one_hot}
                 541777   40.544    0.000   61.994    0.000 allGraphsTrain.py:43(<listcomp>)
                4334216   59.363    0.000   59.363    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9532034: <Diamonds1_0.0_var_0> in cluster <dcc> Done

Job <Diamonds1_0.0_var_0> was submitted from host <n-62-30-7> by user <s183905> in cluster <dcc> at Sat Apr 17 13:28:44 2021
Job was executed on host(s) <n-62-20-16>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Tue Apr 20 01:50:53 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue Apr 20 01:50:53 2021
Terminated at Tue Apr 20 11:46:09 2021
Results reported at Tue Apr 20 11:46:09 2021

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

    CPU time :                                   35618.53 sec.
    Max Memory :                                 2079 MB
    Average Memory :                             2076.23 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14305.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35716 sec.
    Turnaround time :                            253045 sec.

The output (if any) is above this job summary.

