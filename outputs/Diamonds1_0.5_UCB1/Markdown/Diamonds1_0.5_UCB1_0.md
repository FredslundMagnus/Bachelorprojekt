
# Parameters

    Name :                      Diamonds1_0.5_UCB1-0
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


      21814246069 function calls (20919973656 primitive calls) in 35706.26 seconds

##    Ordered by: cumulative time
   List reduced from 462 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35706.256 35706.256 {built-in method builtins.exec}
                      1    0.001    0.001 35706.256 35706.256 <string>:1(<module>)
                      1  167.724  167.724 35706.256 35706.256 allGraphsTrain.py:10(graphTrain)
                 719080 5428.605    0.008 12882.625    0.018 allGraphs.py:146(transformNot)
              719086152 8283.352    0.000 8283.352    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                 719080   18.672    0.000 8098.652    0.011 allGraphsTrain.py:29(<listcomp>)
               72627181 1905.575    0.000 8080.002    0.000 allGraphs.py:110(states)
              647172400 6029.969    0.000 6029.969    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 719080  695.779    0.001 4511.206    0.006 allGraphsTrain.py:35(<listcomp>)
               16712575   23.131    0.000 3815.427    0.000 allGraphs.py:158(getInterventions)
                 719080    2.643    0.000 3453.761    0.005 game.py:41(step)
                 719080    3.277    0.000 3308.427    0.005 layers.py:718(step)
               16712575   16.069    0.000 2222.908    0.000 allGraphs.py:133(UCB1)
        192590068/16712575  143.370    0.000 2142.604    0.000 {built-in method builtins.min}
               47888918   22.515    0.000 2112.007    0.000 allGraphs.py:134(<lambda>)
        368467561/47888918  571.745    0.000 2089.492    0.000 allGraphs.py:68(expected_moves_UCB1)
                 719080  133.611    0.000 2034.116    0.003 allGraphsTrain.py:37(<listcomp>)
                 719081  102.616    0.000 2021.099    0.003 layers.py:684(update)
               23360508 1922.994    0.000 1922.994    0.000 {built-in method tensor}
               20307976   11.668    0.000 1829.619    0.000 game.py:37(board)
        496456136/113021842  165.013    0.000 1758.332    0.000 allGraphs.py:72(<genexpr>)
               16712575   71.904    0.000 1569.389    0.000 allGraphs.py:153(format)
                 719080    2.575    0.000 1568.372    0.002 agent.py:29(learn)
                 719080   15.295    0.000 1564.247    0.002 agent.py:117(_learn)
                 719080   45.124    0.000 1548.952    0.002 learner.py:42(Qlearn)
                 719080   56.621    0.000 1280.092    0.002 layers.py:17(step)
               76222480  175.958    0.000 1245.067    0.000 tensor.py:21(wrapped)
               71908000  115.256    0.000 1216.804    0.000 layer.py:98(move)
                 719080   57.861    0.000 1186.559    0.002 allGraphsTrain.py:44(<listcomp>)
                3106376   23.652    0.000 1173.912    0.000 layers.py:740(restart)
                3106376   11.526    0.000  940.132    0.000 level.py:8(__init__)
               75503400  855.481    0.000  855.481    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                3106376   35.686    0.000  823.050    0.000 levels.py:151(generate)
             3309362980  566.188    0.000  816.271    0.000 enum.py:646(__hash__)
               71908000  799.662    0.000  799.662    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               14911583  137.508    0.000  750.805    0.000 level.py:41(notUsed)
                 719080  393.771    0.001  702.193    0.001 agent.py:67(modify)
                 719080    4.296    0.000  618.253    0.001 grad_mode.py:23(decorate_context)
               71908000  157.800    0.000  609.875    0.000 layers.py:735(check)
                 719080   21.452    0.000  606.050    0.001 adam.py:55(step)
        16538840/2157240   63.642    0.000  604.248    0.000 module.py:715(_call_impl)
              192590068  120.549    0.000  568.811    0.000 allGraphs.py:83(layers_not_in)
                1438160    3.867    0.000  552.297    0.000 network.py:27(forward)
                1438160   15.258    0.000  539.778    0.000 container.py:115(forward)
              368467561  338.758    0.000  536.719    0.000 allGraphs.py:60(UCB1)
                 719080  110.704    0.000  498.329    0.001 functional.py:53(adam)
              192590068  221.541    0.000  448.262    0.000 allGraphs.py:84(<listcomp>)
               71908000  106.603    0.000  384.299    0.000 layers.py:729(isFree)
                 719080    4.622    0.000  364.989    0.001 tensor.py:181(backward)
              198236259  107.702    0.000  362.942    0.000 {built-in method builtins.any}
                 719080    2.480    0.000  360.367    0.001 __init__.py:68(backward)
               14911583   10.972    0.000  353.458    0.000 level.py:38(elementsIn)
                5033567  202.831    0.000  345.714    0.000 layer.py:167(NoRock_update)
                 719080  342.217    0.000  342.217    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                 719080    8.494    0.000  321.123    0.000 agent.py:112(__call__)
              491748840  219.244    0.000  277.697    0.000 layer.py:95(isFree)
               74784320  256.435    0.000  256.435    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
             3309365345  250.083    0.000  250.083    0.000 {built-in method builtins.hash}
                2157240    8.623    0.000  245.545    0.000 tensor.py:576(__iter__)
                2157240  231.581    0.000  231.581    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               14911583  113.549    0.000  229.704    0.000 level.py:39(<listcomp>)
                2876320    4.937    0.000  214.901    0.000 conv.py:422(forward)
                2876320    5.429    0.000  208.160    0.000 conv.py:414(_conv_forward)
              125120054   62.811    0.000  207.646    0.000 overrides.py:1070(has_torch_function)
               21744632   16.928    0.000  202.400    0.000 layer.py:69(restart)
                2876320  201.715    0.000  201.715    0.000 {built-in method conv2d}
              148130580   48.375    0.000  196.319    0.000 {built-in method builtins.all}
              550413792  140.453    0.000  173.198    0.000 layers.py:700(<genexpr>)
                3106476   80.276    0.000  159.143    0.000 layers.py:36(reset)
                2876320    6.739    0.000  158.665    0.000 linear.py:92(forward)
               40268534   93.040    0.000  154.972    0.000 tensor.py:933(grad)
              715942113  153.517    0.000  153.517    0.000 level.py:32(inverse)
                2876320   11.337    0.000  149.017    0.000 functional.py:1669(linear)
                 719080   13.686    0.000  136.773    0.000 optimizer.py:167(zero_grad)
              200842107   48.435    0.000  128.398    0.000 layers.py:690(<genexpr>)
              648648017  115.693    0.000  115.693    0.000 enum.py:352(<genexpr>)
               14911583   70.703    0.000  112.782    0.000 {built-in method _functools.reduce}
               35955316   66.502    0.000  108.905    0.000 layers.py:231(check)
                 719080    5.158    0.000  108.728    0.000 agent.py:59(modify_board)
                 719080   61.747    0.000  106.752    0.000 collector.py:46(collect)
                2876320  105.705    0.000  105.705    0.000 {built-in method addmm}
               35955847   64.721    0.000  105.558    0.000 layers.py:219(check)
               35951952   63.374    0.000  104.014    0.000 layers.py:207(check)
               11505280   99.444    0.000   99.444    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                3106376   49.650    0.000   98.131    0.000 level.py:16(<dictcomp>)
              180423235   69.093    0.000   94.524    0.000 layer.py:130(add)
              368440391   87.999    0.000   87.999    0.000 layer.py:146(elements)
              900988498   87.137    0.000   87.137    0.000 layer.py:91(positions)
               11505280   82.784    0.000   82.784    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              329338908   68.653    0.000   81.547    0.000 overrides.py:1083(<genexpr>)
                 719080   53.363    0.000   78.781    0.000 allGraphsTrain.py:43(<listcomp>)
              370624801   71.632    0.000   71.632    0.000 {built-in method builtins.max}
                4314480    3.981    0.000   71.556    0.000 activation.py:713(forward)
                 719080   71.136    0.000   71.136    0.000 {built-in method torch._C._nn.one_hot}
              368460091   69.758    0.000   69.758    0.000 {built-in method math.log}
                4314480    5.957    0.000   67.575    0.000 functional.py:1292(leaky_relu)
                5752640   62.616    0.000   62.616    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                4314480   61.036    0.000   61.036    0.000 {built-in method torch._C._nn.leaky_relu}
                 719080   15.944    0.000   57.403    0.000 allGraphs.py:137(transform)
                5752640   53.387    0.000   53.387    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9531982: <Diamonds1_0.5_UCB1_0> in cluster <dcc> Done

Job <Diamonds1_0.5_UCB1_0> was submitted from host <n-62-30-7> by user <s183905> in cluster <dcc> at Sat Apr 17 13:24:02 2021
Job was executed on host(s) <n-62-11-13>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sat Apr 17 13:24:03 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat Apr 17 13:24:03 2021
Terminated at Sat Apr 17 23:19:26 2021
Results reported at Sat Apr 17 23:19:26 2021

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

    CPU time :                                   35640.48 sec.
    Max Memory :                                 2069 MB
    Average Memory :                             2061.64 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14315.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35723 sec.
    Turnaround time :                            35724 sec.

The output (if any) is above this job summary.

