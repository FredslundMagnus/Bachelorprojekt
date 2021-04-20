
# Parameters

    Name :                      Diamonds1_0.0_UCB1-1
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


      18326355242 function calls (17859663515 primitive calls) in 35708.59 seconds

##    Ordered by: cumulative time
   List reduced from 461 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35708.586 35708.586 {built-in method builtins.exec}
                      1    0.001    0.001 35708.586 35708.586 <string>:1(<module>)
                      1  146.665  146.665 35708.585 35708.585 allGraphsTrain.py:10(graphTrain)
                 592480 6324.379    0.011 14247.232    0.024 allGraphs.py:146(transformNot)
                 592480   15.993    0.000 8648.947    0.015 allGraphsTrain.py:29(<listcomp>)
               59840581 2262.607    0.000 8633.002    0.000 allGraphs.py:110(states)
              592485136 8042.390    0.000 8042.390    0.000 {method 'item' of 'torch._C._TensorBase' objects}
              533232400 6925.555    0.000 6925.555    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 592480    2.283    0.000 3396.840    0.006 game.py:41(step)
                 592480    2.897    0.000 3265.606    0.006 layers.py:718(step)
                 592480  658.001    0.001 2620.901    0.004 allGraphsTrain.py:35(<listcomp>)
                 592480  157.518    0.000 2117.196    0.004 allGraphsTrain.py:37(<listcomp>)
                8797175   12.568    0.000 1962.900    0.000 allGraphs.py:158(getInterventions)
                 592481   79.496    0.000 1898.416    0.003 layers.py:684(update)
                 592480    1.858    0.000 1592.344    0.003 agent.py:29(learn)
                 592480   12.136    0.000 1589.358    0.003 agent.py:117(_learn)
                 592480   44.745    0.000 1577.222    0.003 learner.py:42(Qlearn)
                 592480   40.697    0.000 1361.164    0.002 layers.py:17(step)
               59248000   90.520    0.000 1315.146    0.000 layer.py:98(move)
               62802880  159.357    0.000 1295.591    0.000 tensor.py:21(wrapped)
                 592480   55.403    0.000 1242.745    0.002 allGraphsTrain.py:44(<listcomp>)
               14281174 1206.535    0.000 1206.535    0.000 {built-in method tensor}
                3168565   22.572    0.000 1134.324    0.000 layers.py:740(restart)
               11759576    7.346    0.000 1118.839    0.000 game.py:37(board)
                8797175    7.885    0.000 1084.996    0.000 allGraphs.py:133(UCB1)
        99825417/8797175   63.188    0.000 1043.265    0.000 {built-in method builtins.min}
               25059977   10.462    0.000 1028.447    0.000 allGraphs.py:134(<lambda>)
        190853659/25059977  276.641    0.000 1017.984    0.000 allGraphs.py:68(expected_moves_UCB1)
               62210400  957.319    0.000  957.319    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                3168565   11.237    0.000  908.225    0.000 level.py:8(__init__)
               59248000  872.537    0.000  872.537    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                8797175   39.870    0.000  865.337    0.000 allGraphs.py:153(format)
        256821924/58802104   73.778    0.000  852.212    0.000 allGraphs.py:72(<genexpr>)
               59248000  174.368    0.000  831.399    0.000 layers.py:735(check)
                3168565   32.410    0.000  796.481    0.000 levels.py:151(generate)
               15207481  130.639    0.000  728.826    0.000 level.py:41(notUsed)
                 592480  421.885    0.001  711.522    0.001 agent.py:67(modify)
                 592480    3.503    0.000  669.100    0.001 grad_mode.py:23(decorate_context)
                 592480   17.028    0.000  659.083    0.001 adam.py:55(step)
             2578383212  420.813    0.000  627.289    0.000 enum.py:646(__hash__)
        13627040/1777440   54.136    0.000  567.047    0.000 module.py:715(_call_impl)
                 592480  119.666    0.000  566.696    0.001 functional.py:53(adam)
                1184960    3.020    0.000  520.136    0.000 network.py:27(forward)
                1184960   13.049    0.000  509.818    0.000 container.py:115(forward)
                 592480    3.622    0.000  363.788    0.001 tensor.py:181(backward)
                 592480    2.014    0.000  360.167    0.001 __init__.py:68(backward)
               15207481   10.186    0.000  347.251    0.000 level.py:38(elementsIn)
                 592480  343.266    0.001  343.266    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               59248000   83.863    0.000  305.673    0.000 layers.py:729(isFree)
                 592480    7.312    0.000  299.474    0.001 agent.py:112(__call__)
               61617920  295.652    0.000  295.652    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              162726070   84.207    0.000  294.319    0.000 {built-in method builtins.any}
                4147367  170.441    0.000  289.844    0.000 layer.py:167(NoRock_update)
               99825417   58.147    0.000  279.265    0.000 allGraphs.py:83(layers_not_in)
              190853659  168.967    0.000  273.586    0.000 allGraphs.py:60(UCB1)
              122050980   52.179    0.000  234.340    0.000 {built-in method builtins.all}
               15207481  110.796    0.000  228.699    0.000 level.py:39(<listcomp>)
              399401452  172.040    0.000  221.811    0.000 layer.py:95(isFree)
               99825417  106.897    0.000  221.119    0.000 allGraphs.py:84(<listcomp>)
             2578385193  206.476    0.000  206.476    0.000 {built-in method builtins.hash}
                2369920    3.990    0.000  198.624    0.000 conv.py:422(forward)
                1777440    7.081    0.000  196.899    0.000 tensor.py:576(__iter__)
               22179955   15.011    0.000  195.924    0.000 layer.py:69(restart)
                2369920    4.742    0.000  193.108    0.000 conv.py:414(_conv_forward)
                2369920  187.467    0.000  187.467    0.000 {built-in method conv2d}
                1777440  184.911    0.000  184.911    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
              103091654   50.998    0.000  169.999    0.000 overrides.py:1070(has_torch_function)
              345215861   87.031    0.000  164.624    0.000 layers.py:690(<genexpr>)
               59248000   97.779    0.000  161.026    0.000 layers.py:219(check)
               59248000   94.752    0.000  157.871    0.000 layers.py:231(check)
                3168665   76.708    0.000  156.969    0.000 layers.py:36(reset)
               59248000   92.582    0.000  154.328    0.000 layers.py:207(check)
                2369920    5.459    0.000  152.253    0.000 linear.py:92(forward)
              730152302  148.973    0.000  148.973    0.000 level.py:32(inverse)
                2369920    9.380    0.000  144.396    0.000 functional.py:1669(linear)
              448636280  113.856    0.000  140.612    0.000 layers.py:700(<genexpr>)
               33178934   88.134    0.000  140.238    0.000 tensor.py:933(grad)
                 592480   12.439    0.000  134.666    0.000 optimizer.py:167(zero_grad)
                9479680  117.695    0.000  117.695    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                 592480   68.306    0.000  114.599    0.000 collector.py:46(collect)
              661539149  111.257    0.000  111.257    0.000 enum.py:352(<genexpr>)
             1132969031  111.125    0.000  111.125    0.000 layer.py:91(positions)
               15207481   67.389    0.000  108.366    0.000 {built-in method _functools.reduce}
                2369920  104.133    0.000  104.133    0.000 {built-in method addmm}
                9479680  100.172    0.000  100.172    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                 592480    4.882    0.000   99.636    0.000 agent.py:59(modify_board)
                3168565   45.348    0.000   93.114    0.000 level.py:16(<dictcomp>)
              173297003   64.823    0.000   89.534    0.000 layer.py:130(add)
               59248000   49.222    0.000   77.604    0.000 layers.py:196(check)
              351740775   74.542    0.000   74.542    0.000 layer.py:146(elements)
                3554880    3.188    0.000   72.809    0.000 activation.py:713(forward)
                3554880    4.787    0.000   69.621    0.000 functional.py:1292(leaky_relu)
              271356108   57.634    0.000   69.127    0.000 overrides.py:1083(<genexpr>)
                4739840   67.363    0.000   67.363    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                3554880   64.342    0.000   64.342    0.000 {built-in method torch._C._nn.leaky_relu}
                 592480   63.075    0.000   63.075    0.000 {built-in method torch._C._nn.one_hot}
               59248000   40.745    0.000   62.555    0.000 layers.py:23(check)
                 592480   39.894    0.000   60.332    0.000 allGraphsTrain.py:43(<listcomp>)
                4739840   58.324    0.000   58.324    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                4739840   53.754    0.000   53.754    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9532022: <Diamonds1_0.0_UCB1_1> in cluster <dcc> Done

Job <Diamonds1_0.0_UCB1_1> was submitted from host <n-62-30-7> by user <s183905> in cluster <dcc> at Sat Apr 17 13:28:43 2021
Job was executed on host(s) <n-62-20-7>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Mon Apr 19 05:05:30 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Apr 19 05:05:30 2021
Terminated at Mon Apr 19 15:00:43 2021
Results reported at Mon Apr 19 15:00:43 2021

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

    CPU time :                                   35656.63 sec.
    Max Memory :                                 2077 MB
    Average Memory :                             2075.66 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14307.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35716 sec.
    Turnaround time :                            178320 sec.

The output (if any) is above this job summary.

