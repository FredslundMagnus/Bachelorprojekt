
# Parameters

    Name :                      Diamonds3_0.0_UCB1-0
    Main :                      graphTrain
    Level :                     Levels.Causal6
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


      36282327393 function calls (33462740352 primitive calls) in 35709.96 seconds

##    Ordered by: cumulative time
   List reduced from 464 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35709.962 35709.962 {built-in method builtins.exec}
                      1    0.001    0.001 35709.962 35709.962 <string>:1(<module>)
                      1  130.631  130.631 35709.961 35709.961 allGraphsTrain.py:10(graphTrain)
                 579409 4870.159    0.008 11907.823    0.021 allGraphs.py:146(transformNot)
              695295932 7829.354    0.000 7829.354    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                 579409   13.799    0.000 7757.657    0.013 allGraphsTrain.py:29(<listcomp>)
               58520410 1761.326    0.000 7743.905    0.000 allGraphs.py:110(states)
                 579409  506.945    0.001 7106.869    0.012 allGraphsTrain.py:35(<listcomp>)
                9007062   11.563    0.000 6599.924    0.001 allGraphs.py:158(getInterventions)
              637350400 5731.079    0.000 5731.079    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                9007062    7.985    0.000 5640.067    0.001 allGraphs.py:133(UCB1)
        504634816/9007062  276.870    0.000 5592.997    0.001 {built-in method builtins.min}
               34737718   14.394    0.000 5575.598    0.000 allGraphs.py:134(<lambda>)
        1000262570/34737718 1470.513    0.000 5561.204    0.000 allGraphs.py:68(expected_moves_UCB1)
        1461152606/114306734  403.730    0.000 5314.652    0.000 allGraphs.py:72(<genexpr>)
                 579409    1.834    0.000 3698.646    0.006 game.py:41(step)
                 579409    2.538    0.000 3578.582    0.006 layers.py:718(step)
                 579410   80.101    0.000 2057.045    0.004 layers.py:684(update)
             7923038054 1212.812    0.000 1768.889    0.000 enum.py:646(__hash__)
                 579409  104.404    0.000 1577.155    0.003 allGraphsTrain.py:37(<listcomp>)
              504634816  266.897    0.000 1539.833    0.000 allGraphs.py:83(layers_not_in)
                 579409   40.764    0.000 1515.927    0.003 layers.py:17(step)
               57940900   87.032    0.000 1470.334    0.000 layer.py:98(move)
             1000262570  826.158    0.000 1317.570    0.000 allGraphs.py:60(UCB1)
               14370360 1278.096    0.000 1278.096    0.000 {built-in method tensor}
              504634816  610.475    0.000 1272.937    0.000 allGraphs.py:84(<listcomp>)
                2965338   23.588    0.000 1257.731    0.000 layers.py:740(restart)
               11904108    6.962    0.000 1201.273    0.000 game.py:37(board)
                 579409    1.824    0.000 1187.234    0.002 agent.py:29(learn)
                 579409   11.194    0.000 1184.286    0.002 agent.py:117(_learn)
                 579409   34.694    0.000 1173.092    0.002 learner.py:42(Qlearn)
                2965338   11.158    0.000 1038.972    0.000 level.py:8(__init__)
               57940900  190.187    0.000  971.926    0.000 layers.py:735(check)
               61417354  132.342    0.000  953.932    0.000 tensor.py:21(wrapped)
                9007062   42.909    0.000  948.294    0.000 allGraphs.py:153(format)
                2965338   37.209    0.000  930.734    0.000 levels.py:288(generate)
                 579409   40.331    0.000  904.390    0.002 allGraphsTrain.py:44(<listcomp>)
               17793154  155.063    0.000  853.963    0.000 level.py:41(notUsed)
               60837945  656.677    0.000  656.677    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               57940900  623.545    0.000  623.545    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
             7923039971  556.078    0.000  556.078    0.000 {built-in method builtins.hash}
                 579409  315.055    0.001  554.768    0.001 agent.py:67(modify)
                 579409    3.286    0.000  469.543    0.001 grad_mode.py:23(decorate_context)
        13326407/1738227   49.413    0.000  463.487    0.000 module.py:715(_call_impl)
                 579409   15.964    0.000  460.261    0.001 adam.py:55(step)
                1158818    2.790    0.000  423.417    0.000 network.py:27(forward)
                1158818   11.919    0.000  413.845    0.000 container.py:115(forward)
               17793154   11.851    0.000  396.510    0.000 level.py:38(elementsIn)
                 579409   84.537    0.000  378.038    0.001 functional.py:53(adam)
               57940900   94.076    0.000  328.001    0.000 layers.py:729(isFree)
                4635280  181.661    0.000  306.101    0.000 layer.py:167(NoRock_update)
              159269417   87.111    0.000  303.752    0.000 {built-in method builtins.any}
                 579409    2.875    0.000  271.418    0.000 tensor.py:181(backward)
                 579409    1.908    0.000  268.544    0.000 __init__.py:68(backward)
               17793154  124.716    0.000  256.336    0.000 level.py:39(<listcomp>)
                 579409  254.362    0.000  254.362    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                 579409    6.576    0.000  247.382    0.000 agent.py:112(__call__)
               57940900  151.072    0.000  241.609    0.000 layers.py:424(check)
              446501184  181.674    0.000  233.925    0.000 layer.py:95(isFree)
              119358354   42.783    0.000  232.151    0.000 {built-in method builtins.all}
               60258536  196.329    0.000  196.329    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                1738227    6.439    0.000  188.488    0.000 tensor.py:576(__iter__)
               23722704   16.331    0.000  187.677    0.000 layer.py:69(restart)
              843985459  181.712    0.000  181.712    0.000 level.py:32(inverse)
                1738227  177.994    0.000  177.994    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
              246788292   62.827    0.000  174.436    0.000 layers.py:690(<genexpr>)
             1002000797  169.741    0.000  169.741    0.000 {built-in method builtins.max}
             1000208061  167.680    0.000  167.680    0.000 {built-in method math.log}
                2317636    3.870    0.000  164.543    0.000 conv.py:422(forward)
              100817300   48.966    0.000  160.364    0.000 overrides.py:1070(has_torch_function)
                2317636    4.630    0.000  159.264    0.000 conv.py:414(_conv_forward)
                2317636  153.838    0.000  153.838    0.000 {built-in method conv2d}
              494780958  125.002    0.000  153.290    0.000 layers.py:700(<genexpr>)
               57940900   94.612    0.000  149.975    0.000 layers.py:437(check)
               57940900   92.919    0.000  147.648    0.000 layers.py:452(check)
                2965438   72.584    0.000  144.867    0.000 layers.py:36(reset)
               17793154   79.993    0.000  128.322    0.000 {built-in method _functools.reduce}
              747307241  126.712    0.000  126.712    0.000 enum.py:352(<genexpr>)
                2317636    5.117    0.000  121.869    0.000 linear.py:92(forward)
             1339405844  120.786    0.000  120.786    0.000 layer.py:91(positions)
               32446958   70.175    0.000  117.891    0.000 tensor.py:933(grad)
                2317636    8.848    0.000  114.506    0.000 functional.py:1669(linear)
                 579409    9.907    0.000  102.836    0.000 optimizer.py:167(zero_grad)
             1004843468  100.015    0.000  100.015    0.000 {built-in method math.sqrt}
               57941000   61.589    0.000   94.267    0.000 layers.py:113(isDone)
                2965338   45.230    0.000   89.390    0.000 level.py:16(<dictcomp>)
                 579409    3.913    0.000   85.285    0.000 agent.py:59(modify_board)
              168195782   60.737    0.000   83.633    0.000 layer.py:130(add)
                 579409   47.467    0.000   81.643    0.000 collector.py:46(collect)
                2317636   81.113    0.000   81.113    0.000 {built-in method addmm}
              342711232   77.316    0.000   77.316    0.000 layer.py:146(elements)
                9270544   76.013    0.000   76.013    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               57940900   45.106    0.000   69.371    0.000 layers.py:402(check)
               57940900   44.503    0.000   68.642    0.000 layers.py:413(check)
                9270544   63.510    0.000   63.510    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              265369590   53.142    0.000   62.990    0.000 overrides.py:1083(<genexpr>)
               57940900   41.904    0.000   60.019    0.000 layers.py:23(check)
                 579409   39.854    0.000   59.413    0.000 allGraphsTrain.py:43(<listcomp>)
                 579409   56.339    0.000   56.339    0.000 {built-in method torch._C._nn.one_hot}
                3476454    2.772    0.000   54.071    0.000 activation.py:713(forward)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9532027: <Diamonds3_0.0_UCB1_0> in cluster <dcc> Done

Job <Diamonds3_0.0_UCB1_0> was submitted from host <n-62-30-7> by user <s183905> in cluster <dcc> at Sat Apr 17 13:28:43 2021
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Mon Apr 19 15:34:57 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Apr 19 15:34:57 2021
Terminated at Tue Apr 20 01:30:15 2021
Results reported at Tue Apr 20 01:30:15 2021

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

    CPU time :                                   35619.66 sec.
    Max Memory :                                 2074 MB
    Average Memory :                             2070.46 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14310.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35718 sec.
    Turnaround time :                            216092 sec.

The output (if any) is above this job summary.

