
# Parameters

    Name :                      Diamonds2_0.0_UCB1-0
    Main :                      graphTrain
    Level :                     Levels.Causal5
    Failed actions chance :     0.0
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


      50200818361 function calls (45137422516 primitive calls) in 35708.90 seconds

##    Ordered by: cumulative time
   List reduced from 464 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35708.895 35708.895 {built-in method builtins.exec}
                      1    0.001    0.001 35708.895 35708.895 <string>:1(<module>)
                      1  102.757  102.757 35708.894 35708.894 allGraphsTrain.py:10(graphTrain)
                 440820  386.607    0.001 11416.449    0.026 allGraphsTrain.py:35(<listcomp>)
                6577014    9.382    0.000 11029.842    0.002 allGraphs.py:158(getInterventions)
                 440820 4351.367    0.010 10567.475    0.024 allGraphs.py:146(transformNot)
                6577014    6.137    0.000 10260.915    0.002 allGraphs.py:133(UCB1)
        868981442/6577014  463.428    0.000 10224.028    0.002 {built-in method builtins.min}
               24462474   10.708    0.000 10211.564    0.000 allGraphs.py:134(<lambda>)
        1731385870/24462474 2685.116    0.000 10200.856    0.000 allGraphs.py:68(expected_moves_UCB1)
        2569327824/84076586  715.182    0.000 10011.352    0.000 allGraphs.py:72(<genexpr>)
                 440820   10.615    0.000 7096.586    0.016 allGraphsTrain.py:29(<listcomp>)
               44522921 1614.684    0.000 7086.020    0.000 allGraphs.py:110(states)
              617152120 6943.471    0.000 6943.471    0.000 {method 'item' of 'torch._C._TensorBase' objects}
              573066600 5141.628    0.000 5141.628    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
            13482774219 1999.263    0.000 2902.961    0.000 enum.py:646(__hash__)
              868981442  456.603    0.000 2893.543    0.000 allGraphs.py:83(layers_not_in)
                 440820    1.409    0.000 2628.861    0.006 game.py:41(step)
                 440820    1.924    0.000 2533.852    0.006 layers.py:718(step)
              868981442 1156.073    0.000 2436.940    0.000 allGraphs.py:84(<listcomp>)
             1731385870 1431.288    0.000 2267.667    0.000 allGraphs.py:60(UCB1)
                 440821   58.446    0.000 1296.567    0.003 layers.py:684(update)
                 440820   30.656    0.000 1233.102    0.003 layers.py:17(step)
               44082000   67.891    0.000 1198.552    0.000 layer.py:98(move)
                 440820   76.573    0.000 1189.806    0.003 allGraphsTrain.py:37(<listcomp>)
               10664993 1040.367    0.000 1040.367    0.000 {built-in method tensor}
                8781115    5.172    0.000  973.945    0.000 game.py:37(board)
                 440820    1.601    0.000  907.117    0.002 agent.py:29(learn)
                 440820    8.564    0.000  904.628    0.002 agent.py:117(_learn)
            13482775720  903.699    0.000  903.699    0.000 {built-in method builtins.hash}
                 440820   26.525    0.000  896.064    0.002 learner.py:42(Qlearn)
               44082000  160.648    0.000  801.331    0.000 layers.py:735(check)
                6577014   30.520    0.000  759.545    0.000 allGraphs.py:153(format)
               46726920  103.797    0.000  726.888    0.000 tensor.py:21(wrapped)
                 440820   31.496    0.000  689.984    0.002 allGraphsTrain.py:44(<listcomp>)
                1458753   12.673    0.000  662.564    0.000 layers.py:740(restart)
                1458753    5.987    0.000  551.060    0.000 level.py:8(__init__)
                1458753   19.735    0.000  499.600    0.000 levels.py:249(generate)
               46286100  494.772    0.000  494.772    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               44082000  468.376    0.000  468.376    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                9481918   80.574    0.000  458.398    0.000 level.py:41(notUsed)
                 440820  222.278    0.001  404.705    0.001 agent.py:67(modify)
                 440820    2.514    0.000  358.343    0.001 grad_mode.py:23(decorate_context)
        10138860/1322460   37.141    0.000  355.286    0.000 module.py:715(_call_impl)
                 440820   12.274    0.000  351.073    0.001 adam.py:55(step)
                 881640    2.205    0.000  324.668    0.000 network.py:27(forward)
                 881640    8.965    0.000  317.526    0.000 container.py:115(forward)
             1732708330  297.238    0.000  297.238    0.000 {built-in method builtins.max}
             1731183533  288.915    0.000  288.915    0.000 {built-in method math.log}
                 440820   63.832    0.000  286.257    0.001 functional.py:53(adam)
               44082000   75.579    0.000  266.832    0.000 layers.py:729(isFree)
              121971082   71.083    0.000  255.046    0.000 {built-in method builtins.any}
                3967389  130.343    0.000  227.094    0.000 layer.py:167(NoRock_update)
                9481918    6.368    0.000  213.630    0.000 level.py:38(elementsIn)
                 440820    2.247    0.000  205.170    0.000 tensor.py:181(backward)
                 440820    1.417    0.000  202.923    0.000 __init__.py:68(backward)
                 440820  192.288    0.000  192.288    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
              387976232  147.308    0.000  191.252    0.000 layer.py:95(isFree)
                 440820    5.481    0.000  190.814    0.000 agent.py:112(__call__)
               90809020   36.351    0.000  189.840    0.000 {built-in method builtins.all}
             1734710228  166.183    0.000  166.183    0.000 {built-in method math.sqrt}
               45845280  146.922    0.000  146.922    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                1322460    4.990    0.000  143.197    0.000 tensor.py:576(__iter__)
              229031141   60.948    0.000  142.428    0.000 layers.py:690(<genexpr>)
                9481918   68.406    0.000  138.182    0.000 level.py:39(<listcomp>)
                1322460  135.008    0.000  135.008    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
              426233470  110.195    0.000  134.171    0.000 layers.py:700(<genexpr>)
                1763280    2.973    0.000  126.676    0.000 conv.py:422(forward)
               76702814   37.617    0.000  125.507    0.000 overrides.py:1070(has_torch_function)
                1763280    3.427    0.000  122.603    0.000 conv.py:414(_conv_forward)
                1763280  118.566    0.000  118.566    0.000 {built-in method conv2d}
               44082000   72.000    0.000  115.379    0.000 layers.py:349(check)
               44082000   70.037    0.000  113.437    0.000 layers.py:375(check)
               44082000   69.292    0.000  112.771    0.000 layers.py:387(check)
               44082000   68.051    0.000  110.192    0.000 layers.py:337(check)
             1102877210  100.687    0.000  100.687    0.000 layer.py:91(positions)
              447201533   99.143    0.000   99.143    0.000 level.py:32(inverse)
               13128777    9.504    0.000   94.768    0.000 layer.py:69(restart)
               24685974   56.836    0.000   94.440    0.000 tensor.py:933(grad)
                1763280    3.991    0.000   93.573    0.000 linear.py:92(forward)
                1763280    6.764    0.000   87.802    0.000 functional.py:1669(linear)
                 440820    7.649    0.000   81.030    0.000 optimizer.py:167(zero_grad)
               44082100   45.946    0.000   71.092    0.000 layers.py:113(isDone)
                1458853   35.573    0.000   70.899    0.000 layers.py:36(reset)
                9481918   42.906    0.000   69.080    0.000 {built-in method _functools.reduce}
              393865721   67.737    0.000   67.737    0.000 enum.py:352(<genexpr>)
                 440820    3.103    0.000   64.906    0.000 agent.py:59(modify_board)
                 440820   36.620    0.000   62.822    0.000 collector.py:46(collect)
                1763280   62.203    0.000   62.203    0.000 {built-in method addmm}
                7053120   57.569    0.000   57.569    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              202601444   56.191    0.000   56.191    0.000 layer.py:146(elements)
               44082000   35.909    0.000   55.200    0.000 layers.py:326(check)
               44082000   34.276    0.000   53.264    0.000 layers.py:364(check)
              201895828   41.809    0.000   49.524    0.000 overrides.py:1083(<genexpr>)
               98056772   35.945    0.000   49.168    0.000 layer.py:130(add)
                7053120   48.496    0.000   48.496    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                 440820   31.194    0.000   46.240    0.000 allGraphsTrain.py:43(<listcomp>)
               44082000   29.572    0.000   44.206    0.000 layers.py:23(check)
                 440820   42.778    0.000   42.778    0.000 {built-in method torch._C._nn.one_hot}
                2644920    2.285    0.000   41.927    0.000 activation.py:713(forward)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9532024: <Diamonds2_0.0_UCB1_0> in cluster <dcc> Done

Job <Diamonds2_0.0_UCB1_0> was submitted from host <n-62-30-7> by user <s183905> in cluster <dcc> at Sat Apr 17 13:28:43 2021
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Mon Apr 19 05:39:41 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Apr 19 05:39:41 2021
Terminated at Mon Apr 19 15:34:57 2021
Results reported at Mon Apr 19 15:34:57 2021

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

    CPU time :                                   35619.71 sec.
    Max Memory :                                 2068 MB
    Average Memory :                             2065.78 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14316.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35717 sec.
    Turnaround time :                            180374 sec.

The output (if any) is above this job summary.

