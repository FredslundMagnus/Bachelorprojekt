
# Parameters

    Name :                      Diamonds1_0.0_UCB1-0
    Main :                      graphTrain
    Level :                     Levels.Causal2
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


      16715800658 function calls (16292375795 primitive calls) in 35706.67 seconds

##    Ordered by: cumulative time
   List reduced from 462 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35706.668 35706.668 {built-in method builtins.exec}
                      1    0.001    0.001 35706.668 35706.668 <string>:1(<module>)
                      1  144.981  144.981 35706.667 35706.667 allGraphsTrain.py:10(graphTrain)
                 539471 6406.640    0.012 14307.515    0.027 allGraphs.py:146(transformNot)
                 539471   15.826    0.000 8644.075    0.016 allGraphsTrain.py:29(<listcomp>)
               54486672 2276.174    0.000 8628.275    0.000 allGraphs.py:110(states)
              539475712 8005.191    0.000 8005.191    0.000 {method 'item' of 'torch._C._TensorBase' objects}
              485524300 6927.517    0.000 6927.517    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 539471    2.053    0.000 3395.653    0.006 game.py:41(step)
                 539471    2.760    0.000 3269.820    0.006 layers.py:718(step)
                 539471  658.130    0.001 2571.807    0.005 allGraphsTrain.py:35(<listcomp>)
                 539471  160.547    0.000 2144.177    0.004 allGraphsTrain.py:37(<listcomp>)
                7987153   12.720    0.000 1913.677    0.000 allGraphs.py:158(getInterventions)
                 539472   80.901    0.000 1910.802    0.004 layers.py:684(update)
                 539471    1.852    0.000 1572.137    0.003 agent.py:29(learn)
                 539471   12.042    0.000 1569.122    0.003 agent.py:117(_learn)
                 539471   45.316    0.000 1557.081    0.003 learner.py:42(Qlearn)
                 539471   40.831    0.000 1353.161    0.003 layers.py:17(step)
               53947100   90.635    0.000 1307.164    0.000 layer.py:98(move)
               57183926  157.742    0.000 1300.447    0.000 tensor.py:21(wrapped)
                 539471   57.008    0.000 1248.857    0.002 allGraphsTrain.py:44(<listcomp>)
               12982611 1136.645    0.000 1136.645    0.000 {built-in method tensor}
                2871473   22.621    0.000 1128.609    0.000 layers.py:740(restart)
                7987153    7.910    0.000 1085.063    0.000 allGraphs.py:133(UCB1)
               10684509    7.180    0.000 1049.214    0.000 game.py:37(board)
        90567490/7987153   65.820    0.000 1043.019    0.000 {built-in method builtins.min}
               22740368   10.474    0.000 1027.909    0.000 allGraphs.py:134(<lambda>)
        173147827/22740368  272.165    0.000 1017.435    0.000 allGraphs.py:68(expected_moves_UCB1)
               56644455  968.117    0.000  968.117    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                2871473   10.907    0.000  905.032    0.000 level.py:8(__init__)
               53947100  887.153    0.000  887.153    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
        232987796/53340532   74.653    0.000  852.681    0.000 allGraphs.py:72(<genexpr>)
               53947100  174.749    0.000  819.746    0.000 layers.py:735(check)
                7987153   40.208    0.000  815.894    0.000 allGraphs.py:153(format)
                2871473   32.261    0.000  792.991    0.000 levels.py:151(generate)
               13783383  130.870    0.000  726.622    0.000 level.py:41(notUsed)
                 539471  420.853    0.001  709.326    0.001 agent.py:67(modify)
                 539471    3.322    0.000  662.602    0.001 grad_mode.py:23(decorate_context)
                 539471   16.850    0.000  652.798    0.001 adam.py:55(step)
             2374353904  420.532    0.000  610.154    0.000 enum.py:646(__hash__)
        12407833/1618413   53.600    0.000  565.402    0.000 module.py:715(_call_impl)
                 539471  119.542    0.000  563.030    0.001 functional.py:53(adam)
                1078942    3.261    0.000  518.363    0.000 network.py:27(forward)
                1078942   13.636    0.000  508.160    0.000 container.py:115(forward)
                 539471    3.155    0.000  353.485    0.001 tensor.py:181(backward)
                 539471    1.975    0.000  350.331    0.001 __init__.py:68(backward)
               13783383   10.072    0.000  342.931    0.000 level.py:38(elementsIn)
                 539471  333.620    0.001  333.620    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               53947100   90.252    0.000  310.143    0.000 layers.py:729(isFree)
               56104984  303.173    0.000  303.173    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                 539471    7.254    0.000  298.961    0.001 agent.py:112(__call__)
              148180642   84.738    0.000  289.825    0.000 {built-in method builtins.any}
                3776304  170.128    0.000  285.158    0.000 layer.py:167(NoRock_update)
               90567490   58.615    0.000  281.141    0.000 allGraphs.py:83(layers_not_in)
              173147827  169.377    0.000  272.389    0.000 allGraphs.py:60(UCB1)
              111131126   48.477    0.000  253.487    0.000 {built-in method builtins.all}
               90567490  111.238    0.000  222.526    0.000 allGraphs.py:84(<listcomp>)
               13783383  111.404    0.000  222.509    0.000 level.py:39(<listcomp>)
              368820048  172.547    0.000  219.891    0.000 layer.py:95(isFree)
                1618413    7.101    0.000  200.217    0.000 tensor.py:576(__iter__)
                2157884    4.008    0.000  198.370    0.000 conv.py:422(forward)
               20100311   16.180    0.000  193.803    0.000 layer.py:69(restart)
                2157884    4.402    0.000  192.882    0.000 conv.py:414(_conv_forward)
             2374355693  189.622    0.000  189.622    0.000 {built-in method builtins.hash}
              278817451   78.052    0.000  188.602    0.000 layers.py:690(<genexpr>)
                1618413  188.490    0.000  188.490    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
                2157884  187.552    0.000  187.552    0.000 {built-in method conv2d}
               93868088   50.877    0.000  165.308    0.000 overrides.py:1070(has_torch_function)
               53947100   95.678    0.000  157.352    0.000 layers.py:231(check)
               53947100   95.081    0.000  155.274    0.000 layers.py:207(check)
                2871573   76.668    0.000  153.618    0.000 layers.py:36(reset)
               53947100   92.475    0.000  152.112    0.000 layers.py:219(check)
                2157884    5.830    0.000  151.626    0.000 linear.py:92(forward)
              661773304  148.119    0.000  148.119    0.000 level.py:32(inverse)
                2157884    9.453    0.000  143.390    0.000 functional.py:1669(linear)
              408605816  113.839    0.000  139.812    0.000 layers.py:700(<genexpr>)
               30210430   86.440    0.000  136.229    0.000 tensor.py:933(grad)
                 539471   12.463    0.000  132.067    0.000 optimizer.py:167(zero_grad)
                8631536  117.827    0.000  117.827    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              599576309  114.689    0.000  114.689    0.000 enum.py:352(<genexpr>)
                 539471   67.944    0.000  113.845    0.000 collector.py:46(collect)
             1079611260  111.073    0.000  111.073    0.000 layer.py:91(positions)
               13783383   68.699    0.000  110.350    0.000 {built-in method _functools.reduce}
                2157884  103.498    0.000  103.498    0.000 {built-in method addmm}
                8631536   99.876    0.000   99.876    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                 539471    4.500    0.000   98.005    0.000 agent.py:59(modify_board)
               53947200   62.715    0.000   96.580    0.000 layers.py:113(isDone)
                2871473   46.806    0.000   94.165    0.000 level.py:16(<dictcomp>)
              157418406   63.317    0.000   86.853    0.000 layer.py:130(add)
               53947100   49.415    0.000   76.176    0.000 layers.py:196(check)
                3236826    3.106    0.000   72.258    0.000 activation.py:713(forward)
              319527842   71.866    0.000   71.866    0.000 layer.py:146(elements)
                3236826    5.118    0.000   69.152    0.000 functional.py:1292(leaky_relu)
              247077986   54.560    0.000   64.903    0.000 overrides.py:1083(<genexpr>)
                4315768   64.415    0.000   64.415    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                3236826   63.574    0.000   63.574    0.000 {built-in method torch._C._nn.leaky_relu}
                 539471   61.952    0.000   61.952    0.000 {built-in method torch._C._nn.one_hot}
               53947100   41.270    0.000   61.715    0.000 layers.py:23(check)
                 539471   40.546    0.000   60.802    0.000 allGraphsTrain.py:43(<listcomp>)
                4315768   58.124    0.000   58.124    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9532021: <Diamonds1_0.0_UCB1_0> in cluster <dcc> Done

Job <Diamonds1_0.0_UCB1_0> was submitted from host <n-62-30-7> by user <s183905> in cluster <dcc> at Sat Apr 17 13:28:43 2021
Job was executed on host(s) <n-62-20-13>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Mon Apr 19 05:05:28 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Apr 19 05:05:28 2021
Terminated at Mon Apr 19 15:00:40 2021
Results reported at Mon Apr 19 15:00:40 2021

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

    CPU time :                                   35618.38 sec.
    Max Memory :                                 2065 MB
    Average Memory :                             2064.11 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14319.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35787 sec.
    Turnaround time :                            178317 sec.

The output (if any) is above this job summary.

