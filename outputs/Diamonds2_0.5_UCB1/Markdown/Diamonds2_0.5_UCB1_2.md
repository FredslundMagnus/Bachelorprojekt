
# Parameters

    Name :                      Diamonds2_0.5_UCB1-2
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


      40899210772 function calls (36368455325 primitive calls) in 35706.91 seconds

##    Ordered by: cumulative time
   List reduced from 464 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35706.915 35706.915 {built-in method builtins.exec}
                      1    0.001    0.001 35706.915 35706.915 <string>:1(<module>)
                      1   82.511   82.511 35706.914 35706.914 allGraphsTrain.py:10(graphTrain)
                 304033  399.258    0.001 11841.972    0.039 allGraphsTrain.py:35(<listcomp>)
                5713632   10.011    0.000 11442.713    0.002 allGraphs.py:158(getInterventions)
                 304033 4978.458    0.016 11200.252    0.037 allGraphs.py:146(transformNot)
                5713632    6.136    0.000 10715.727    0.002 allGraphs.py:133(UCB1)
        777485477/5713632  460.653    0.000 10678.313    0.002 {built-in method builtins.min}
               21484967   10.081    0.000 10664.891    0.000 allGraphs.py:134(<lambda>)
        1549257322/21484967 2766.167    0.000 10654.810    0.000 allGraphs.py:68(expected_moves_UCB1)
        2299544200/74413996  729.562    0.000 10461.786    0.000 allGraphs.py:72(<genexpr>)
                 304033    9.226    0.000 7256.725    0.024 allGraphsTrain.py:29(<listcomp>)
               30707434 1881.742    0.000 7247.527    0.000 allGraphs.py:110(states)
              425649232 6291.185    0.000 6291.185    0.000 {method 'item' of 'torch._C._TensorBase' objects}
              395243500 5655.669    0.000 5655.669    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
              777485477  485.626    0.000 3064.595    0.000 allGraphs.py:83(layers_not_in)
            11483386262 1918.125    0.000 2919.793    0.000 enum.py:646(__hash__)
              777485477 1218.059    0.000 2578.968    0.000 allGraphs.py:84(<listcomp>)
             1549257322 1502.458    0.000 2409.785    0.000 allGraphs.py:60(UCB1)
                 304033    1.194    0.000 1580.198    0.005 game.py:41(step)
                 304033    1.623    0.000 1503.940    0.005 layers.py:718(step)
                 304033   92.019    0.000 1201.359    0.004 allGraphsTrain.py:37(<listcomp>)
            11483387315 1001.668    0.000 1001.668    0.000 {built-in method builtins.hash}
                8543066  916.986    0.000  916.986    0.000 {built-in method tensor}
                 304033    1.124    0.000  890.808    0.003 agent.py:29(learn)
                 304033    6.779    0.000  888.997    0.003 agent.py:117(_learn)
                 304033   25.582    0.000  882.219    0.003 learner.py:42(Qlearn)
                7233798    5.280    0.000  862.069    0.000 game.py:37(board)
                 304034   44.883    0.000  806.421    0.003 layers.py:684(update)
               32227498   90.719    0.000  740.173    0.000 tensor.py:21(wrapped)
                5713632   33.575    0.000  716.975    0.000 allGraphs.py:153(format)
                 304033   31.756    0.000  711.031    0.002 allGraphsTrain.py:44(<listcomp>)
                 304033   23.694    0.000  694.205    0.002 layers.py:17(step)
               30403300   51.594    0.000  667.315    0.000 layer.py:98(move)
               31923465  547.569    0.000  547.569    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               30403300  496.060    0.000  496.060    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                 304033    1.804    0.000  375.784    0.001 grad_mode.py:23(decorate_context)
                 304033    9.724    0.000  370.216    0.001 adam.py:55(step)
               30403300   86.947    0.000  365.275    0.000 layers.py:735(check)
                 304033  201.157    0.001  363.226    0.001 agent.py:67(modify)
                 692102    7.051    0.000  353.958    0.001 layers.py:740(restart)
             1548939569  334.308    0.000  334.308    0.000 {built-in method math.log}
         6992759/912099   30.556    0.000  320.337    0.000 module.py:715(_call_impl)
                 304033   67.262    0.000  317.478    0.001 functional.py:53(adam)
                 692102    3.329    0.000  293.959    0.000 level.py:8(__init__)
                 608066    1.686    0.000  293.571    0.000 network.py:27(forward)
             1550169421  293.331    0.000  293.331    0.000 {built-in method builtins.max}
                 608066    7.459    0.000  287.927    0.000 container.py:115(forward)
                 692102   10.785    0.000  266.471    0.000 levels.py:249(generate)
                4496794   42.939    0.000  244.008    0.000 level.py:41(notUsed)
               30403300   58.163    0.000  202.957    0.000 layers.py:729(isFree)
               84437373   53.505    0.000  198.820    0.000 {built-in method builtins.any}
                 304033    1.803    0.000  198.255    0.001 tensor.py:181(backward)
                 304033    1.087    0.000  196.453    0.001 __init__.py:68(backward)
                 304033  187.032    0.001  187.032    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
             1551371968  171.865    0.000  171.865    0.000 {built-in method math.sqrt}
                 304033    4.193    0.000  170.632    0.001 agent.py:112(__call__)
               31619432  167.558    0.000  167.558    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                2736306   89.947    0.000  164.171    0.000 layer.py:167(NoRock_update)
              266791534  110.599    0.000  144.794    0.000 layer.py:95(isFree)
               62630898   22.588    0.000  120.754    0.000 {built-in method builtins.all}
                4496794    3.317    0.000  114.246    0.000 level.py:38(elementsIn)
                 912099    4.011    0.000  112.651    0.000 tensor.py:576(__iter__)
                1216132    2.303    0.000  112.183    0.000 conv.py:422(forward)
                1216132    2.601    0.000  109.020    0.000 conv.py:414(_conv_forward)
                 912099  105.987    0.000  105.987    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
                1216132  105.945    0.000  105.945    0.000 {built-in method conv2d}
              297112980   84.335    0.000  105.772    0.000 layers.py:700(<genexpr>)
               52901876   28.903    0.000   96.766    0.000 overrides.py:1070(has_torch_function)
              102078070   27.848    0.000   88.175    0.000 layers.py:690(<genexpr>)
                1216132    3.117    0.000   85.924    0.000 linear.py:92(forward)
                1216132    5.629    0.000   81.417    0.000 functional.py:1669(linear)
               17025902   50.902    0.000   80.198    0.000 tensor.py:933(grad)
                 304033    7.059    0.000   76.480    0.000 optimizer.py:167(zero_grad)
                4496794   35.334    0.000   74.923    0.000 level.py:39(<listcomp>)
                4864528   66.552    0.000   66.552    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                 304033   38.175    0.000   64.253    0.000 collector.py:46(collect)
                1216132   58.310    0.000   58.310    0.000 {built-in method addmm}
                4864528   56.350    0.000   56.350    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               30403400   35.314    0.000   55.415    0.000 layers.py:113(isDone)
                 304033    2.566    0.000   55.024    0.000 agent.py:59(modify_board)
              485057096   53.567    0.000   53.567    0.000 layer.py:91(positions)
              212091194   53.173    0.000   53.173    0.000 level.py:32(inverse)
                6228918    4.907    0.000   50.704    0.000 layer.py:69(restart)
               15202492   29.064    0.000   48.380    0.000 layers.py:375(check)
               15198216   28.729    0.000   47.467    0.000 layers.py:387(check)
               15198795   28.472    0.000   47.181    0.000 layers.py:349(check)
               15199683   28.408    0.000   46.695    0.000 layers.py:337(check)
              112189265   40.904    0.000   40.904    0.000 layer.py:146(elements)
                1824198    1.712    0.000   40.864    0.000 activation.py:713(forward)
              139247382   32.656    0.000   39.321    0.000 overrides.py:1083(<genexpr>)
                1824198    2.911    0.000   39.152    0.000 functional.py:1292(leaky_relu)
                 692202   18.909    0.000   38.232    0.000 layers.py:36(reset)
                2432264   36.165    0.000   36.165    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                4496794   22.487    0.000   36.007    0.000 {built-in method _functools.reduce}
                1824198   35.964    0.000   35.964    0.000 {built-in method torch._C._nn.leaky_relu}
                 304033   23.284    0.000   34.970    0.000 allGraphsTrain.py:43(<listcomp>)
              186801821   34.927    0.000   34.927    0.000 enum.py:352(<genexpr>)
                 304033   34.574    0.000   34.574    0.000 {built-in method torch._C._nn.one_hot}
                2432264   32.991    0.000   32.991    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9531987: <Diamonds2_0.5_UCB1_2> in cluster <dcc> Done

Job <Diamonds2_0.5_UCB1_2> was submitted from host <n-62-30-7> by user <s183905> in cluster <dcc> at Sat Apr 17 13:24:03 2021
Job was executed on host(s) <n-62-20-14>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sat Apr 17 13:24:04 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat Apr 17 13:24:04 2021
Terminated at Sat Apr 17 23:19:27 2021
Results reported at Sat Apr 17 23:19:27 2021

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

    CPU time :                                   35617.71 sec.
    Max Memory :                                 2068 MB
    Average Memory :                             2060.61 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14316.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35722 sec.
    Turnaround time :                            35724 sec.

The output (if any) is above this job summary.

