
# Parameters

    Name :                      Diamonds2_0.0_UCB1-1
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


      39409493804 function calls (35469112269 primitive calls) in 35708.27 seconds

##    Ordered by: cumulative time
   List reduced from 465 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35708.270 35708.270 {built-in method builtins.exec}
                      1    0.001    0.001 35708.270 35708.270 <string>:1(<module>)
                      1   94.951   94.951 35708.269 35708.269 allGraphsTrain.py:10(graphTrain)
                 371379 5447.279    0.015 12298.172    0.033 allGraphs.py:146(transformNot)
                 371379  422.251    0.001 9081.331    0.024 allGraphsTrain.py:35(<listcomp>)
                5085082    8.110    0.000 8659.080    0.002 allGraphs.py:158(getInterventions)
                5085082    4.809    0.000 8026.317    0.002 allGraphs.py:133(UCB1)
        676077034/5085082  355.239    0.000 7997.439    0.002 {built-in method builtins.min}
                 371379    9.956    0.000 7989.553    0.022 allGraphsTrain.py:29(<listcomp>)
               18953516    7.975    0.000 7986.497    0.000 allGraphs.py:134(<lambda>)
               37509380 2047.809    0.000 7979.651    0.000 allGraphs.py:110(states)
        1347068986/18953516 2074.338    0.000 7978.522    0.000 allGraphs.py:68(expected_moves_UCB1)
        1999107422/65261272  546.995    0.000 7830.480    0.000 allGraphs.py:72(<genexpr>)
              519934168 6981.135    0.000 6981.135    0.000 {method 'item' of 'torch._C._TensorBase' objects}
              482793300 6208.162    0.000 6208.162    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
            10528512055 1590.866    0.000 2316.418    0.000 enum.py:646(__hash__)
              676077034  356.176    0.000 2291.163    0.000 allGraphs.py:83(layers_not_in)
                 371379    1.250    0.000 2105.925    0.006 game.py:41(step)
                 371379    1.723    0.000 2016.488    0.005 layers.py:718(step)
              676077034  911.278    0.000 1934.987    0.000 allGraphs.py:84(<listcomp>)
             1347068986 1111.156    0.000 1790.943    0.000 allGraphs.py:60(UCB1)
                 371379   97.557    0.000 1317.725    0.004 allGraphsTrain.py:37(<listcomp>)
                 371379   25.885    0.000 1046.530    0.003 layers.py:17(step)
               37137900   57.407    0.000 1017.660    0.000 layer.py:98(move)
                 371379    1.191    0.000  978.424    0.003 agent.py:29(learn)
                 371379    7.487    0.000  976.509    0.003 agent.py:117(_learn)
                 371379   28.246    0.000  969.022    0.003 learner.py:42(Qlearn)
                 371380   48.617    0.000  966.311    0.003 layers.py:684(update)
                8534420  881.974    0.000  881.974    0.000 {built-in method tensor}
                6941978    4.495    0.000  816.555    0.000 game.py:37(board)
               39366174   96.594    0.000  800.328    0.000 tensor.py:21(wrapped)
                 371379   34.155    0.000  766.898    0.002 allGraphsTrain.py:44(<listcomp>)
            10528513332  725.553    0.000  725.553    0.000 {built-in method builtins.hash}
               37137900  134.872    0.000  686.412    0.000 layers.py:735(check)
                5085082   27.032    0.000  624.653    0.000 allGraphs.py:153(format)
               38994795  595.842    0.000  595.842    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               37137900  544.140    0.000  544.140    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                1137406    9.752    0.000  512.049    0.000 layers.py:740(restart)
                1137406    4.538    0.000  426.270    0.000 level.py:8(__init__)
                 371379  234.324    0.001  416.078    0.001 agent.py:67(modify)
                 371379    2.093    0.000  411.020    0.001 grad_mode.py:23(decorate_context)
                 371379   10.712    0.000  404.941    0.001 adam.py:55(step)
                1137406   15.709    0.000  386.607    0.000 levels.py:249(generate)
                7392501   61.932    0.000  354.364    0.000 level.py:41(notUsed)
        8541717/1114137   32.808    0.000  352.705    0.000 module.py:715(_call_impl)
                 371379   73.737    0.000  348.814    0.001 functional.py:53(adam)
                 742758    1.876    0.000  323.151    0.000 network.py:27(forward)
                 742758    8.292    0.000  317.032    0.000 container.py:115(forward)
             1346851895  248.080    0.000  248.080    0.000 {built-in method math.log}
             1348183123  227.628    0.000  227.628    0.000 {built-in method builtins.max}
               37137900   62.751    0.000  221.841    0.000 layers.py:729(isFree)
                 371379    2.070    0.000  221.033    0.001 tensor.py:181(backward)
                 371379    1.318    0.000  218.963    0.001 __init__.py:68(backward)
                 371379  208.258    0.001  208.258    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
              102848949   57.541    0.000  204.859    0.000 {built-in method builtins.any}
                 371379    4.573    0.000  187.885    0.001 agent.py:112(__call__)
                3342420  103.455    0.000  182.898    0.000 layer.py:167(NoRock_update)
               38623416  181.954    0.000  181.954    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                7392501    4.904    0.000  165.592    0.000 level.py:38(elementsIn)
              327190752  121.728    0.000  159.090    0.000 layer.py:95(isFree)
             1349823062  129.651    0.000  129.651    0.000 {built-in method math.sqrt}
                1485516    2.617    0.000  125.116    0.000 conv.py:422(forward)
                1114137    4.506    0.000  124.499    0.000 tensor.py:576(__iter__)
                1485516    2.772    0.000  121.624    0.000 conv.py:414(_conv_forward)
                1485516  118.362    0.000  118.362    0.000 {built-in method conv2d}
                1114137  116.999    0.000  116.999    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
                7392501   53.340    0.000  108.191    0.000 level.py:39(<listcomp>)
              360005940   87.322    0.000  106.886    0.000 layers.py:700(<genexpr>)
               64620080   31.306    0.000  102.770    0.000 overrides.py:1070(has_torch_function)
               37137900   65.719    0.000  101.601    0.000 layers.py:337(check)
               37137900   62.329    0.000   99.527    0.000 layers.py:387(check)
               76504174   21.665    0.000   96.774    0.000 {built-in method builtins.all}
               37137900   58.926    0.000   96.101    0.000 layers.py:375(check)
               37137900   58.412    0.000   95.790    0.000 layers.py:349(check)
                1485516    3.380    0.000   94.258    0.000 linear.py:92(forward)
                1485516    5.785    0.000   89.484    0.000 functional.py:1669(linear)
               20797278   54.037    0.000   84.801    0.000 tensor.py:933(grad)
                 371379    7.676    0.000   81.898    0.000 optimizer.py:167(zero_grad)
              903299095   77.996    0.000   77.996    0.000 layer.py:91(positions)
              348658332   76.549    0.000   76.549    0.000 level.py:32(inverse)
                5942064   73.353    0.000   73.353    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               10236654    6.938    0.000   72.787    0.000 layer.py:69(restart)
                 371379   42.261    0.000   71.212    0.000 collector.py:46(collect)
               99444808   22.352    0.000   65.276    0.000 layers.py:690(<genexpr>)
                1485516   64.668    0.000   64.668    0.000 {built-in method addmm}
                 371379    2.739    0.000   62.556    0.000 agent.py:59(modify_board)
                5942064   61.971    0.000   61.971    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                1137506   27.475    0.000   54.892    0.000 layers.py:36(reset)
                7392501   32.701    0.000   52.496    0.000 {built-in method _functools.reduce}
              307078217   52.343    0.000   52.343    0.000 enum.py:352(<genexpr>)
              162728497   45.851    0.000   45.851    0.000 layer.py:146(elements)
               37137900   29.656    0.000   45.254    0.000 layers.py:326(check)
                2228274    1.991    0.000   45.129    0.000 activation.py:713(forward)
               37137900   29.111    0.000   44.526    0.000 layers.py:364(check)
                2228274    3.246    0.000   43.138    0.000 functional.py:1292(leaky_relu)
              170091850   33.768    0.000   40.210    0.000 overrides.py:1083(<genexpr>)
                2971032   39.884    0.000   39.884    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                 371379   39.801    0.000   39.801    0.000 {built-in method torch._C._nn.one_hot}
                2228274   39.611    0.000   39.611    0.000 {built-in method torch._C._nn.leaky_relu}
               78580477   28.620    0.000   39.052    0.000 layer.py:130(add)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9532025: <Diamonds2_0.0_UCB1_1> in cluster <dcc> Done

Job <Diamonds2_0.0_UCB1_1> was submitted from host <n-62-30-7> by user <s183905> in cluster <dcc> at Sat Apr 17 13:28:43 2021
Job was executed on host(s) <n-62-20-3>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Mon Apr 19 05:39:41 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Apr 19 05:39:41 2021
Terminated at Mon Apr 19 15:34:55 2021
Results reported at Mon Apr 19 15:34:55 2021

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

    CPU time :                                   35618.10 sec.
    Max Memory :                                 2066 MB
    Average Memory :                             2065.89 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14318.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35715 sec.
    Turnaround time :                            180372 sec.

The output (if any) is above this job summary.

