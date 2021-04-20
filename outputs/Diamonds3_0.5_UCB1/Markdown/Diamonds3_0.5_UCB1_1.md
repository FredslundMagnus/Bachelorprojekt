
# Parameters

    Name :                      Diamonds3_0.5_UCB1-1
    Main :                      graphTrain
    Level :                     Levels.Causal6
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


      36360470147 function calls (32893118330 primitive calls) in 35713.26 seconds

##    Ordered by: cumulative time
   List reduced from 463 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35713.260 35713.260 {built-in method builtins.exec}
                      1    0.001    0.001 35713.259 35713.259 <string>:1(<module>)
                      1  139.057  139.057 35713.258 35713.258 allGraphsTrain.py:10(graphTrain)
                 496059 4552.326    0.009 11332.838    0.023 allGraphs.py:146(transformNot)
                 496059  554.343    0.001 9156.501    0.018 allGraphsTrain.py:35(<listcomp>)
               10835660   15.071    0.000 8602.157    0.001 allGraphs.py:158(getInterventions)
              595275268 7876.801    0.000 7876.801    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                 496059   11.846    0.000 7455.265    0.015 allGraphsTrain.py:29(<listcomp>)
               50102060 1637.772    0.000 7443.484    0.000 allGraphs.py:110(states)
               10835660   10.393    0.000 7407.587    0.001 allGraphs.py:133(UCB1)
        620872438/10835660  363.126    0.000 7349.129    0.001 {built-in method builtins.min}
               42222046   19.240    0.000 7327.144    0.000 allGraphs.py:134(<lambda>)
        1230909216/42222046 1915.256    0.000 7307.904    0.000 allGraphs.py:68(expected_moves_UCB1)
        1798723948/140017642  530.815    0.000 6986.697    0.000 allGraphs.py:72(<genexpr>)
              545665400 5253.933    0.000 5253.933    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 496059    2.257    0.000 2828.776    0.006 game.py:41(step)
                 496059    2.846    0.000 2718.108    0.005 layers.py:718(step)
             8608199234 1414.610    0.000 2083.336    0.000 enum.py:646(__hash__)
              620872438  353.229    0.000 2040.278    0.000 allGraphs.py:83(layers_not_in)
             1230909216 1053.910    0.000 1710.827    0.000 allGraphs.py:60(UCB1)
              620872438  804.056    0.000 1687.048    0.000 allGraphs.py:84(<listcomp>)
                 496060   74.353    0.000 1645.013    0.003 layers.py:684(update)
                 496059   92.100    0.000 1497.848    0.003 allGraphsTrain.py:37(<listcomp>)
               15431912 1463.659    0.000 1463.659    0.000 {built-in method tensor}
               13315956    7.694    0.000 1391.979    0.000 game.py:37(board)
               10835660   51.152    0.000 1179.500    0.000 allGraphs.py:153(format)
                 496059    1.787    0.000 1129.289    0.002 agent.py:29(learn)
                 496059   11.009    0.000 1126.342    0.002 agent.py:117(_learn)
                 496059   33.751    0.000 1115.333    0.002 learner.py:42(Qlearn)
                 496059   40.023    0.000 1066.985    0.002 layers.py:17(step)
               49605900   82.804    0.000 1021.859    0.000 layer.py:98(move)
                1908055   17.600    0.000  883.213    0.000 layers.py:740(restart)
               52582254  120.254    0.000  858.540    0.000 tensor.py:21(wrapped)
                 496059   36.591    0.000  811.547    0.002 allGraphsTrain.py:44(<listcomp>)
                1908055    8.074    0.000  727.714    0.000 level.py:8(__init__)
             8608200895  668.725    0.000  668.725    0.000 {built-in method builtins.hash}
                1908055   25.734    0.000  647.880    0.000 levels.py:288(generate)
               11449339  106.956    0.000  594.277    0.000 level.py:41(notUsed)
               52086195  589.407    0.000  589.407    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               49605900  566.186    0.000  566.186    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               49605900  123.207    0.000  517.540    0.000 layers.py:735(check)
                 496059  282.860    0.001  513.393    0.001 agent.py:67(modify)
        11409357/1488177   48.163    0.000  450.840    0.000 module.py:715(_call_impl)
                 496059    3.667    0.000  433.822    0.001 grad_mode.py:23(decorate_context)
                 496059   15.825    0.000  423.854    0.001 adam.py:55(step)
                 992118    2.827    0.000  409.295    0.000 network.py:27(forward)
                 992118   11.233    0.000  399.300    0.000 container.py:115(forward)
                 496059   77.189    0.000  347.200    0.001 functional.py:53(adam)
               49605900   80.666    0.000  340.932    0.000 layers.py:729(isFree)
              136988700   80.463    0.000  283.000    0.000 {built-in method builtins.any}
               11449339    8.396    0.000  275.956    0.000 level.py:38(elementsIn)
                 496059    3.069    0.000  269.366    0.001 tensor.py:181(backward)
                3968480  154.481    0.000  266.918    0.000 layer.py:167(NoRock_update)
                 496059    2.199    0.000  266.297    0.001 __init__.py:68(backward)
              392093039  207.936    0.000  260.266    0.000 layer.py:95(isFree)
                 496059  252.111    0.001  252.111    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                 496059    7.677    0.000  248.472    0.001 agent.py:112(__call__)
              102188254   37.212    0.000  247.585    0.000 {built-in method builtins.all}
             1232397393  227.583    0.000  227.583    0.000 {built-in method builtins.max}
             1230811669  227.249    0.000  227.249    0.000 {built-in method math.log}
              194570871   54.502    0.000  197.652    0.000 layers.py:690(<genexpr>)
                1488177    6.279    0.000  187.547    0.000 tensor.py:576(__iter__)
               11449339   88.095    0.000  178.834    0.000 level.py:39(<listcomp>)
               51590136  178.071    0.000  178.071    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                1488177  177.290    0.000  177.290    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
                1984236    3.957    0.000  161.118    0.000 conv.py:422(forward)
                1984236    4.425    0.000  155.596    0.000 conv.py:414(_conv_forward)
                1984236  150.342    0.000  150.342    0.000 {built-in method conv2d}
              429281505  117.851    0.000  144.699    0.000 layers.py:700(<genexpr>)
               86314400   44.274    0.000  144.692    0.000 overrides.py:1070(has_torch_function)
             1234780276  134.253    0.000  134.253    0.000 {built-in method math.sqrt}
               15264440   11.974    0.000  132.834    0.000 layer.py:69(restart)
              543077588  125.928    0.000  125.928    0.000 level.py:32(inverse)
                1984236    4.993    0.000  116.788    0.000 linear.py:92(forward)
               24805249   66.427    0.000  110.438    0.000 layers.py:424(check)
                1984236    8.418    0.000  109.319    0.000 functional.py:1669(linear)
               27779358   64.892    0.000  108.473    0.000 tensor.py:933(grad)
                1908155   49.210    0.000   99.660    0.000 layers.py:36(reset)
                 496059    8.915    0.000   94.202    0.000 optimizer.py:167(zero_grad)
              480867713   90.516    0.000   90.516    0.000 enum.py:352(<genexpr>)
               11449339   55.151    0.000   88.725    0.000 {built-in method _functools.reduce}
               49606000   54.470    0.000   87.366    0.000 layers.py:442(isDone)
                 496059    3.896    0.000   83.687    0.000 agent.py:59(modify_board)
                1984236   78.012    0.000   78.012    0.000 {built-in method addmm}
              757076332   78.005    0.000   78.005    0.000 layer.py:91(positions)
               24802641   47.610    0.000   77.011    0.000 layers.py:437(check)
                 496059   43.410    0.000   74.853    0.000 collector.py:46(collect)
               24804399   45.250    0.000   73.415    0.000 layers.py:452(check)
                7936944   69.838    0.000   69.838    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              241150760   67.915    0.000   67.915    0.000 layer.py:146(elements)
              117362038   50.336    0.000   67.725    0.000 layer.py:130(add)
                1908055   35.223    0.000   66.538    0.000 level.py:16(<dictcomp>)
              227195290   48.420    0.000   57.469    0.000 overrides.py:1083(<genexpr>)
                7936944   57.185    0.000   57.185    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                 496059   55.668    0.000   55.668    0.000 {built-in method torch._C._nn.one_hot}
                 496059   36.982    0.000   54.887    0.000 allGraphsTrain.py:43(<listcomp>)
                2976354    2.946    0.000   51.614    0.000 activation.py:713(forward)
                2976354    4.841    0.000   48.668    0.000 functional.py:1292(leaky_relu)
                 496059   11.404    0.000   43.512    0.000 allGraphs.py:137(transform)
              392093039   43.434    0.000   43.434    0.000 layer.py:203(isBlocking)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9531989: <Diamonds3_0.5_UCB1_1> in cluster <dcc> Done

Job <Diamonds3_0.5_UCB1_1> was submitted from host <n-62-30-7> by user <s183905> in cluster <dcc> at Sat Apr 17 13:24:03 2021
Job was executed on host(s) <n-62-20-10>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sat Apr 17 23:19:32 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat Apr 17 23:19:32 2021
Terminated at Sun Apr 18 09:14:51 2021
Results reported at Sun Apr 18 09:14:51 2021

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

    CPU time :                                   35619.88 sec.
    Max Memory :                                 2059 MB
    Average Memory :                             2054.31 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14325.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35720 sec.
    Turnaround time :                            71448 sec.

The output (if any) is above this job summary.

