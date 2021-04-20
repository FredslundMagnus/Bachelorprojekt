
# Parameters

    Name :                      Diamonds1_0.5_UCB1-1
    Main :                      graphTrain
    Level :                     Levels.Causal2
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


      20813804701 function calls (19963694058 primitive calls) in 35711.09 seconds

##    Ordered by: cumulative time
   List reduced from 461 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35711.090 35711.090 {built-in method builtins.exec}
                      1    0.001    0.001 35711.090 35711.090 <string>:1(<module>)
                      1  173.087  173.087 35711.089 35711.089 allGraphsTrain.py:10(graphTrain)
                 685900 5178.871    0.008 12997.487    0.019 allGraphs.py:146(transformNot)
              685905880 9117.380    0.000 9117.380    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                 685900   16.966    0.000 8218.705    0.012 allGraphsTrain.py:29(<listcomp>)
               69276001 1808.928    0.000 8201.789    0.000 allGraphs.py:110(states)
              617310400 5853.035    0.000 5853.035    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 685900  753.970    0.001 4425.087    0.006 allGraphsTrain.py:35(<listcomp>)
               15859295   20.975    0.000 3671.117    0.000 allGraphs.py:158(getInterventions)
                 685900    2.546    0.000 3391.702    0.005 game.py:41(step)
                 685900    3.797    0.000 3247.403    0.005 layers.py:718(step)
               15859295   15.205    0.000 2096.445    0.000 allGraphs.py:133(UCB1)
                 685900  128.636    0.000 2056.038    0.003 allGraphsTrain.py:37(<listcomp>)
        183022748/15859295  121.449    0.000 2020.163    0.000 {built-in method builtins.min}
               45469082   20.567    0.000 1993.956    0.000 allGraphs.py:134(<lambda>)
                 685901   99.321    0.000 1981.281    0.003 layers.py:684(update)
        350186201/45469082  527.568    0.000 1973.389    0.000 allGraphs.py:68(expected_moves_UCB1)
               22202362 1910.535    0.000 1910.535    0.000 {built-in method tensor}
               19288796   11.060    0.000 1818.792    0.000 game.py:37(board)
        471880572/107368884  144.574    0.000 1663.525    0.000 allGraphs.py:72(<genexpr>)
               15859295   66.795    0.000 1553.696    0.000 allGraphs.py:153(format)
                 685900    2.412    0.000 1527.029    0.002 agent.py:29(learn)
                 685900   14.543    0.000 1523.125    0.002 agent.py:117(_learn)
                 685900   44.160    0.000 1508.582    0.002 learner.py:42(Qlearn)
                 685900   52.188    0.000 1258.311    0.002 layers.py:17(step)
               68590000  110.035    0.000 1199.888    0.000 layer.py:98(move)
               72705400  169.472    0.000 1185.958    0.000 tensor.py:21(wrapped)
                2950293   23.652    0.000 1133.372    0.000 layers.py:740(restart)
                 685900   50.826    0.000 1120.927    0.002 allGraphsTrain.py:44(<listcomp>)
                2950293   11.494    0.000  908.550    0.000 level.py:8(__init__)
               72019500  805.223    0.000  805.223    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                2950293   32.700    0.000  793.675    0.000 levels.py:151(generate)
             3147408632  544.936    0.000  792.014    0.000 enum.py:646(__hash__)
               68590000  774.277    0.000  774.277    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               14164317  131.307    0.000  726.007    0.000 level.py:41(notUsed)
                 685900  392.306    0.001  705.396    0.001 agent.py:67(modify)
        15775700/2057700   65.367    0.000  597.842    0.000 module.py:715(_call_impl)
                 685900    4.288    0.000  591.903    0.001 grad_mode.py:23(decorate_context)
               68590000  152.770    0.000  587.207    0.000 layers.py:735(check)
                 685900   20.918    0.000  579.499    0.001 adam.py:55(step)
              183022748  114.843    0.000  550.186    0.000 allGraphs.py:83(layers_not_in)
                1371800    3.641    0.000  542.689    0.000 network.py:27(forward)
                1371800   14.913    0.000  529.707    0.000 container.py:115(forward)
              350186201  328.141    0.000  519.763    0.000 allGraphs.py:60(UCB1)
                 685900  106.598    0.000  474.397    0.001 functional.py:53(adam)
              183022748  213.417    0.000  435.343    0.000 allGraphs.py:84(<listcomp>)
               68590000  101.218    0.000  398.219    0.000 layers.py:729(isFree)
              189101942  104.381    0.000  363.641    0.000 {built-in method builtins.any}
                 685900    3.865    0.000  361.243    0.001 tensor.py:181(backward)
                 685900    2.643    0.000  357.378    0.001 __init__.py:68(backward)
               14164317   10.452    0.000  341.811    0.000 level.py:38(elementsIn)
                 685900  338.538    0.000  338.538    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                4801307  198.849    0.000  337.682    0.000 layer.py:167(NoRock_update)
                 685900    8.959    0.000  323.255    0.000 agent.py:112(__call__)
              474347571  237.540    0.000  297.002    0.000 layer.py:95(isFree)
             3147410901  247.078    0.000  247.078    0.000 {built-in method builtins.hash}
                2057700    7.848    0.000  240.729    0.000 tensor.py:576(__iter__)
               71333600  239.658    0.000  239.658    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                2057700  227.718    0.000  227.718    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               14164317  107.898    0.000  221.788    0.000 level.py:39(<listcomp>)
                2743600    4.911    0.000  211.498    0.000 conv.py:422(forward)
                2743600    6.241    0.000  204.541    0.000 conv.py:414(_conv_forward)
              119346734   62.454    0.000  202.815    0.000 overrides.py:1070(has_torch_function)
              141295500   47.390    0.000  202.421    0.000 {built-in method builtins.all}
                2743600  197.175    0.000  197.175    0.000 {built-in method conv2d}
               20652051   16.016    0.000  193.948    0.000 layer.py:69(restart)
              525118456  147.655    0.000  179.164    0.000 layers.py:700(<genexpr>)
                2743600    6.655    0.000  155.853    0.000 linear.py:92(forward)
                2950393   76.078    0.000  152.237    0.000 layers.py:36(reset)
               38410454   90.568    0.000  150.583    0.000 tensor.py:933(grad)
              680059223  148.384    0.000  148.384    0.000 level.py:32(inverse)
                2743600   11.088    0.000  146.100    0.000 functional.py:1669(linear)
              211949706   57.901    0.000  137.654    0.000 layers.py:690(<genexpr>)
                 685900   13.046    0.000  130.613    0.000 optimizer.py:167(zero_grad)
              616127453  115.411    0.000  115.411    0.000 enum.py:352(<genexpr>)
                 685900    5.459    0.000  112.008    0.000 agent.py:59(modify_board)
               14164317   68.277    0.000  109.571    0.000 {built-in method _functools.reduce}
                2743600  104.281    0.000  104.281    0.000 {built-in method addmm}
               34302971   64.322    0.000  103.798    0.000 layers.py:231(check)
                 685900   60.116    0.000  103.466    0.000 collector.py:46(collect)
               34295381   63.173    0.000  102.164    0.000 layers.py:219(check)
               34287535   61.841    0.000  100.353    0.000 layers.py:207(check)
                2950293   47.429    0.000   95.927    0.000 level.py:16(<dictcomp>)
               10974400   94.439    0.000   94.439    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              171384464   66.559    0.000   91.765    0.000 layer.py:130(add)
              350026484   85.710    0.000   85.710    0.000 layer.py:146(elements)
              859020104   82.651    0.000   82.651    0.000 layer.py:91(positions)
              314142468   67.082    0.000   79.617    0.000 overrides.py:1083(<genexpr>)
               10974400   79.048    0.000   79.048    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                 685900   74.205    0.000   74.205    0.000 {built-in method torch._C._nn.one_hot}
                 685900   49.465    0.000   74.104    0.000 allGraphsTrain.py:43(<listcomp>)
              352243901   70.678    0.000   70.678    0.000 {built-in method builtins.max}
                4115400    3.841    0.000   69.403    0.000 activation.py:713(forward)
              350180696   68.911    0.000   68.911    0.000 {built-in method math.log}
                4115400    6.265    0.000   65.562    0.000 functional.py:1292(leaky_relu)
                4115400   58.712    0.000   58.712    0.000 {built-in method torch._C._nn.leaky_relu}
                 685900   15.202    0.000   58.490    0.000 allGraphs.py:137(transform)
                5487200   55.233    0.000   55.233    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                2057700   52.700    0.000   52.700    0.000 {method 'tolist' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9531983: <Diamonds1_0.5_UCB1_1> in cluster <dcc> Done

Job <Diamonds1_0.5_UCB1_1> was submitted from host <n-62-30-7> by user <s183905> in cluster <dcc> at Sat Apr 17 13:24:02 2021
Job was executed on host(s) <n-62-20-12>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sat Apr 17 13:24:03 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat Apr 17 13:24:03 2021
Terminated at Sat Apr 17 23:19:31 2021
Results reported at Sat Apr 17 23:19:31 2021

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

    CPU time :                                   35621.34 sec.
    Max Memory :                                 2070 MB
    Average Memory :                             2062.52 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14314.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35763 sec.
    Turnaround time :                            35729 sec.

The output (if any) is above this job summary.

