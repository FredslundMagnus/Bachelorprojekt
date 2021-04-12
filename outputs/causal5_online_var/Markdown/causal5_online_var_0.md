
# Parameters

    Name :                      causal5_online_var-0
    Main :                      graphTrain
    Level :                     Levels.Causal5
    Hours :                     12.0
    Batch :                     100
    Width :                     9
    Height :                    9
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
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                2
    Counterfacts :              10
    Topn :                      7
    Minutes used :              715 minutes.
    Hours used :                11 hours.

# Profiling


      44144818483 function calls (39467207806 primitive calls) in 42911.94 seconds

##    Ordered by: cumulative time
   List reduced from 465 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 42911.938 42911.938 {built-in method builtins.exec}
                      1    0.001    0.001 42911.938 42911.938 <string>:1(<module>)
                      1  117.609  117.609 42911.936 42911.936 allGraphsTrain.py:5(graphTrain)
                 466951 6843.123    0.015 15401.076    0.033 allGraphs.py:238(transformNot)
                 466951   12.338    0.000 9993.293    0.021 allGraphsTrain.py:24(<listcomp>)
               47162152 2567.562    0.000 9981.016    0.000 allGraphs.py:198(states)
                 466951  519.235    0.001 9651.493    0.021 allGraphsTrain.py:30(<listcomp>)
                6835452   39.797    0.000 9132.258    0.001 allGraphs.py:245(getInterventions)
              653735728 8720.606    0.000 8720.606    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                6193908    5.145    0.000 8296.655    0.001 allGraphs.py:225(rightIntervention)
        802769650/6193908  405.070    0.000 8261.016    0.001 {built-in method builtins.min}
               22822246    9.500    0.000 8248.478    0.000 allGraphs.py:226(<lambda>)
        1599345392/22822246 2411.159    0.000 8238.978    0.000 allGraphs.py:61(expected_moves)
        2373098888/77926502  631.422    0.000 8086.420    0.000 allGraphs.py:65(<genexpr>)
              607036900 7757.316    0.000 7757.316    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
            12619423341 1792.498    0.000 2648.874    0.000 enum.py:646(__hash__)
              803411194  422.922    0.000 2643.081    0.000 allGraphs.py:70(layers_not_in)
                 466951    1.697    0.000 2581.894    0.006 game.py:41(step)
                 466951    2.120    0.000 2470.667    0.005 layers.py:710(step)
              803411194 1076.224    0.000 2220.159    0.000 allGraphs.py:71(<listcomp>)
                 466951  124.159    0.000 1643.211    0.004 allGraphsTrain.py:32(<listcomp>)
                 466952   62.357    0.000 1321.625    0.003 layers.py:676(update)
                 466951    1.547    0.000 1222.161    0.003 agent.py:29(learn)
                 466951    9.474    0.000 1219.710    0.003 agent.py:117(_learn)
                 466951   35.142    0.000 1210.235    0.003 learner.py:42(Qlearn)
                 466951   32.504    0.000 1144.507    0.002 layers.py:17(step)
               11163676 1136.948    0.000 1136.948    0.000 {built-in method tensor}
               46695100   72.163    0.000 1107.770    0.000 layer.py:98(move)
             1599345392  751.272    0.000 1095.830    0.000 allGraphs.py:46(p)
                9170208    5.986    0.000 1056.983    0.000 game.py:37(board)
               49496806  124.548    0.000  997.901    0.000 tensor.py:21(wrapped)
                 466951   44.097    0.000  958.113    0.002 allGraphsTrain.py:39(<listcomp>)
            12619424906  856.377    0.000  856.377    0.000 {built-in method builtins.hash}
               49029855  737.843    0.000  737.843    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               46695100  111.571    0.000  693.931    0.000 layers.py:727(check)
               46695100  674.638    0.000  674.638    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                1453141   11.761    0.000  648.586    0.000 layers.py:731(restart)
                1453141    5.507    0.000  539.476    0.000 level.py:8(__init__)
                 466951  291.097    0.001  516.499    0.001 agent.py:67(modify)
                 466951    2.597    0.000  510.108    0.001 grad_mode.py:23(decorate_context)
                 466951   13.514    0.000  502.620    0.001 adam.py:55(step)
                1453141   20.064    0.000  490.953    0.000 levels.py:249(generate)
                9443084   80.340    0.000  449.383    0.000 level.py:41(notUsed)
        10739873/1400853   43.138    0.000  443.362    0.000 module.py:715(_call_impl)
                 466951   91.652    0.000  431.971    0.001 functional.py:53(adam)
                 933902    2.338    0.000  405.969    0.000 network.py:24(forward)
                 933902   10.931    0.000  397.935    0.000 container.py:115(forward)
               46695100   77.629    0.000  277.665    0.000 layers.py:721(isFree)
                 466951    2.662    0.000  275.016    0.001 tensor.py:181(backward)
             1601387789  268.950    0.000  272.717    0.000 {built-in method builtins.max}
                 466951    1.549    0.000  272.354    0.001 __init__.py:68(backward)
              129293374   73.452    0.000  264.155    0.000 {built-in method builtins.any}
                 466951  259.056    0.001  259.056    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                 466951    5.749    0.000  234.503    0.001 agent.py:112(__call__)
                4202568  132.305    0.000  234.292    0.000 layer.py:167(NoRock_update)
               48562904  226.704    0.000  226.704    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               96192006   40.598    0.000  211.252    0.000 {built-in method builtins.all}
                9443084    6.026    0.000  206.809    0.000 level.py:38(elementsIn)
              405776622  157.727    0.000  200.036    0.000 layer.py:95(isFree)
              287107073   70.904    0.000  158.102    0.000 layers.py:682(<genexpr>)
                1400853    6.070    0.000  156.831    0.000 tensor.py:576(__iter__)
                1867804    3.130    0.000  155.399    0.000 conv.py:422(forward)
                1867804    3.423    0.000  151.094    0.000 conv.py:414(_conv_forward)
                1867804  147.046    0.000  147.046    0.000 {built-in method conv2d}
                1400853  147.013    0.000  147.013    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
              452420590  114.719    0.000  139.890    0.000 layers.py:692(<genexpr>)
                9443084   65.252    0.000  132.200    0.000 level.py:39(<listcomp>)
               81249608   39.605    0.000  128.745    0.000 overrides.py:1070(has_torch_function)
                1867804    4.422    0.000  118.524    0.000 linear.py:92(forward)
               46695100   73.383    0.000  118.379    0.000 layers.py:331(check)
               46695100   72.025    0.000  118.335    0.000 layers.py:343(check)
               46695100   70.498    0.000  114.837    0.000 layers.py:369(check)
               46695100   71.560    0.000  114.736    0.000 layers.py:381(check)
                1867804    7.714    0.000  112.188    0.000 functional.py:1669(linear)
               26149310   68.705    0.000  108.062    0.000 tensor.py:933(grad)
                 466951    9.857    0.000  104.175    0.000 optimizer.py:167(zero_grad)
              445374763   99.120    0.000   99.120    0.000 level.py:32(inverse)
               13078269    8.981    0.000   93.298    0.000 layer.py:69(restart)
             1074686022   92.231    0.000   92.231    0.000 layer.py:91(positions)
                7471216   91.015    0.000   91.015    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                 466951   52.582    0.000   88.858    0.000 collector.py:46(collect)
                1867804   80.171    0.000   80.171    0.000 {built-in method addmm}
                 466951    3.706    0.000   77.653    0.000 agent.py:59(modify_board)
                7471216   76.541    0.000   76.541    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               46695200   47.772    0.000   73.948    0.000 layers.py:107(isDone)
                1453241   35.043    0.000   70.102    0.000 layers.py:30(reset)
                9443084   42.653    0.000   68.583    0.000 {built-in method _functools.reduce}
              392265662   65.406    0.000   65.406    0.000 enum.py:352(<genexpr>)
              207425086   59.364    0.000   59.364    0.000 layer.py:146(elements)
                2801706    2.522    0.000   56.283    0.000 activation.py:713(forward)
                2801706    3.931    0.000   53.761    0.000 functional.py:1292(leaky_relu)
               46695100   34.153    0.000   52.729    0.000 layers.py:358(check)
               46695100   33.240    0.000   52.011    0.000 layers.py:320(check)
              213863826   42.567    0.000   50.519    0.000 overrides.py:1083(<genexpr>)
              100228683   36.479    0.000   49.628    0.000 layer.py:130(add)
                2801706   49.473    0.000   49.473    0.000 {built-in method torch._C._nn.leaky_relu}
                 466951   49.242    0.000   49.242    0.000 {built-in method torch._C._nn.one_hot}
                3735608   48.967    0.000   48.967    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                 466951   32.611    0.000   48.186    0.000 allGraphsTrain.py:38(<listcomp>)
                3735608   44.849    0.000   44.849    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-4>
Subject: Job 9509262: <causal5_online_var_0> in cluster <dcc> Done

Job <causal5_online_var_0> was submitted from host <n-62-27-21> by user <s183905> in cluster <dcc> at Mon Apr 12 00:14:17 2021
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Mon Apr 12 00:14:19 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Apr 12 00:14:19 2021
Terminated at Mon Apr 12 12:09:40 2021
Results reported at Mon Apr 12 12:09:40 2021

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
#BSUB -W 1440
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $LSB_PROJECT_NAME


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   42798.90 sec.
    Max Memory :                                 2088 MB
    Average Memory :                             2069.45 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14296.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   42923 sec.
    Turnaround time :                            42923 sec.

The output (if any) is above this job summary.

