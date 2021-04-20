
# Parameters

    Name :                      Diamonds1_0.5_UCB1-2
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


      19482169279 function calls (18686426524 primitive calls) in 35710.92 seconds

##    Ordered by: cumulative time
   List reduced from 461 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35710.924 35710.924 {built-in method builtins.exec}
                      1    0.001    0.001 35710.924 35710.924 <string>:1(<module>)
                      1  241.175  241.175 35710.923 35710.923 allGraphsTrain.py:10(graphTrain)
                 646406 5185.949    0.008 12737.644    0.020 allGraphs.py:146(transformNot)
              646411568 8714.892    0.000 8714.892    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                 646406   19.208    0.000 8081.283    0.013 allGraphsTrain.py:29(<listcomp>)
               65287107 1850.050    0.000 8062.088    0.000 allGraphs.py:110(states)
              581765800 5743.835    0.000 5743.835    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 646406  749.831    0.001 4306.592    0.007 allGraphsTrain.py:35(<listcomp>)
               14829486   23.693    0.000 3556.761    0.000 allGraphs.py:158(getInterventions)
                 646406    3.743    0.000 3512.061    0.005 game.py:41(step)
                 646406    5.583    0.000 3343.139    0.005 layers.py:718(step)
               14829486   15.692    0.000 2027.138    0.000 allGraphs.py:133(UCB1)
                 646406  133.382    0.000 2004.671    0.003 allGraphsTrain.py:37(<listcomp>)
                 646407  106.375    0.000 1996.047    0.003 layers.py:684(update)
        171262014/14829486  119.839    0.000 1947.923    0.000 {built-in method builtins.min}
               42514714   19.292    0.000 1920.958    0.000 allGraphs.py:134(<lambda>)
               20809184 1906.873    0.000 1906.873    0.000 {built-in method tensor}
        327694542/42514714  518.304    0.000 1901.666    0.000 allGraphs.py:68(expected_moves_UCB1)
               18061517   13.053    0.000 1801.096    0.000 game.py:37(board)
                 646406    4.125    0.000 1646.390    0.003 agent.py:29(learn)
                 646406   19.877    0.000 1640.418    0.003 agent.py:117(_learn)
                 646406   51.279    0.000 1620.540    0.003 learner.py:42(Qlearn)
        441612356/100410460  139.062    0.000 1595.996    0.000 allGraphs.py:72(<genexpr>)
               14829486   72.476    0.000 1505.931    0.000 allGraphs.py:153(format)
                 646406   62.285    0.000 1335.162    0.002 layers.py:17(step)
               64640600  111.665    0.000 1266.344    0.000 layer.py:98(move)
               68519036  172.307    0.000 1182.243    0.000 tensor.py:21(wrapped)
                2759559   24.768    0.000 1128.660    0.000 layers.py:740(restart)
                 646406   57.019    0.000 1113.898    0.002 allGraphsTrain.py:44(<listcomp>)
                2759559   12.267    0.000  900.691    0.000 level.py:8(__init__)
               67872630  805.065    0.000  805.065    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                 646406  416.102    0.001  773.743    0.001 agent.py:67(modify)
                2759559   32.829    0.000  773.235    0.000 levels.py:151(generate)
             2948886963  519.211    0.000  759.722    0.000 enum.py:646(__hash__)
               64640600  750.350    0.000  750.350    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
        14867338/1939218   76.043    0.000  713.570    0.000 module.py:715(_call_impl)
               13246953  127.754    0.000  705.735    0.000 level.py:41(notUsed)
                1292812    4.913    0.000  645.735    0.000 network.py:27(forward)
                1292812   17.564    0.000  629.541    0.000 container.py:115(forward)
                 646406    5.784    0.000  597.494    0.001 grad_mode.py:23(decorate_context)
               64640600  147.813    0.000  583.858    0.000 layers.py:735(check)
                 646406   23.402    0.000  580.829    0.001 adam.py:55(step)
              171262014  112.527    0.000  526.880    0.000 allGraphs.py:83(layers_not_in)
              327694542  316.430    0.000  503.083    0.000 allGraphs.py:60(UCB1)
                 646406  107.788    0.000  473.262    0.001 functional.py:53(adam)
               64640600  102.883    0.000  456.932    0.000 layers.py:729(isFree)
              171262014  204.978    0.000  414.353    0.000 allGraphs.py:84(<listcomp>)
                 646406    4.768    0.000  399.326    0.001 tensor.py:181(backward)
                 646406   14.910    0.000  398.055    0.001 agent.py:112(__call__)
                 646406    3.727    0.000  394.558    0.001 __init__.py:68(backward)
                4524849  220.059    0.000  372.370    0.000 layer.py:167(NoRock_update)
                 646406  371.589    0.001  371.589    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
              436150004  294.069    0.000  354.049    0.000 layer.py:95(isFree)
              178234356  100.607    0.000  347.660    0.000 {built-in method builtins.any}
               13246953   10.530    0.000  331.330    0.000 level.py:38(elementsIn)
                1939218   12.346    0.000  299.425    0.000 tensor.py:576(__iter__)
                1939218  278.841    0.000  278.841    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
                2585624    5.953    0.000  262.887    0.000 conv.py:422(forward)
                2585624    8.581    0.000  254.515    0.000 conv.py:414(_conv_forward)
                2585624  244.860    0.000  244.860    0.000 {built-in method conv2d}
             2948889104  240.511    0.000  240.511    0.000 {built-in method builtins.hash}
               67226224  238.872    0.000  238.872    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               13246953  106.686    0.000  216.005    0.000 level.py:39(<listcomp>)
              112474778   61.953    0.000  196.978    0.000 overrides.py:1070(has_torch_function)
               19316913   17.275    0.000  196.133    0.000 layer.py:69(restart)
              133159736   43.446    0.000  188.547    0.000 {built-in method builtins.all}
                2585624    7.295    0.000  185.352    0.000 linear.py:92(forward)
                2585624   13.683    0.000  174.406    0.000 functional.py:1669(linear)
              495049128  138.577    0.000  169.763    0.000 layers.py:700(<genexpr>)
               36198790   90.368    0.000  148.953    0.000 tensor.py:933(grad)
                2759659   74.276    0.000  148.129    0.000 layers.py:36(reset)
              636016264  146.633    0.000  146.633    0.000 level.py:32(inverse)
                 646406    7.065    0.000  137.001    0.000 agent.py:59(modify_board)
                 646406   12.488    0.000  128.909    0.000 optimizer.py:167(zero_grad)
              180166537   47.334    0.000  127.706    0.000 layers.py:690(<genexpr>)
                2585624  125.400    0.000  125.400    0.000 {built-in method addmm}
              576235925  110.958    0.000  110.958    0.000 enum.py:352(<genexpr>)
                 646406   62.336    0.000  108.690    0.000 collector.py:46(collect)
                2759559   60.037    0.000  107.629    0.000 level.py:16(<dictcomp>)
               32324501   68.613    0.000  107.406    0.000 layers.py:231(check)
               13246953   65.385    0.000  104.795    0.000 {built-in method _functools.reduce}
               32316817   64.642    0.000  102.157    0.000 layers.py:207(check)
               32323856   62.191    0.000  100.302    0.000 layers.py:219(check)
              328354865   97.341    0.000   97.341    0.000 layer.py:146(elements)
              160751909   67.422    0.000   95.813    0.000 layer.py:130(add)
               10342496   93.847    0.000   93.847    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                 646406   88.752    0.000   88.752    0.000 {built-in method torch._C._nn.one_hot}
                 646406   63.324    0.000   87.801    0.000 allGraphsTrain.py:43(<listcomp>)
              809657550   82.908    0.000   82.908    0.000 layer.py:91(positions)
                3878436    5.279    0.000   77.648    0.000 activation.py:713(forward)
              296054216   64.727    0.000   76.738    0.000 overrides.py:1083(<genexpr>)
               10342496   76.522    0.000   76.522    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                 646406   18.894    0.000   74.627    0.000 allGraphs.py:137(transform)
                3878436    8.147    0.000   72.369    0.000 functional.py:1292(leaky_relu)
              327687804   68.179    0.000   68.179    0.000 {built-in method math.log}
              329633760   67.181    0.000   67.181    0.000 {built-in method builtins.max}
                1939218   65.184    0.000   65.184    0.000 {method 'tolist' of 'torch._C._TensorBase' objects}
                3878436   63.537    0.000   63.537    0.000 {built-in method torch._C._nn.leaky_relu}
                1292812   60.233    0.000   60.233    0.000 {built-in method cat}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9531984: <Diamonds1_0.5_UCB1_2> in cluster <dcc> Done

Job <Diamonds1_0.5_UCB1_2> was submitted from host <n-62-30-7> by user <s183905> in cluster <dcc> at Sat Apr 17 13:24:02 2021
Job was executed on host(s) <n-62-20-10>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sat Apr 17 13:24:03 2021
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

    CPU time :                                   35620.00 sec.
    Max Memory :                                 2064 MB
    Average Memory :                             2041.09 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14320.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35762 sec.
    Turnaround time :                            35729 sec.

The output (if any) is above this job summary.

