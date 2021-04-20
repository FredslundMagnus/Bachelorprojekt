
# Parameters

    Name :                      Diamonds2_0.5_var-1
    Main :                      graphTrain
    Level :                     Levels.Causal5
    Failed actions chance :     0.5
    Hours :                     10.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.var
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


      48333152298 function calls (42643111221 primitive calls) in 35702.88 seconds

##    Ordered by: cumulative time
   List reduced from 466 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35702.880 35702.880 {built-in method builtins.exec}
                      1    0.001    0.001 35702.880 35702.880 <string>:1(<module>)
                      1  100.336  100.336 35702.879 35702.879 allGraphsTrain.py:10(graphTrain)
                 410012  405.737    0.001 12412.818    0.030 allGraphsTrain.py:35(<listcomp>)
                8349102   15.619    0.000 12007.081    0.001 allGraphs.py:158(getInterventions)
                7440176    7.461    0.000 11020.445    0.001 allGraphs.py:129(rightIntervention)
        976848092/7440176  602.773    0.000 10977.366    0.001 {built-in method builtins.min}
               27543870   13.566    0.000 10960.172    0.000 allGraphs.py:130(<lambda>)
        1946256008/27543870 3224.709    0.000 10946.605    0.000 allGraphs.py:74(expected_moves)
        2888120054/94399654  913.680    0.000 10742.778    0.000 allGraphs.py:78(<genexpr>)
                 410012 4339.854    0.011 10321.275    0.025 allGraphs.py:146(transformNot)
                 410012   11.268    0.000 6990.900    0.017 allGraphsTrain.py:29(<listcomp>)
               41411313 1630.877    0.000 6979.650    0.000 allGraphs.py:110(states)
              574020680 6632.414    0.000 6632.414    0.000 {method 'item' of 'torch._C._TensorBase' objects}
              533016200 5078.830    0.000 5078.830    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
              977757018  571.043    0.000 3435.290    0.000 allGraphs.py:83(layers_not_in)
            14509282539 2249.646    0.000 3210.460    0.000 enum.py:646(__hash__)
              977757018 1381.935    0.000 2864.247    0.000 allGraphs.py:84(<listcomp>)
                 410012    1.420    0.000 2050.065    0.005 game.py:41(step)
                 410012    2.050    0.000 1959.873    0.005 layers.py:718(step)
             1946256008  989.610    0.000 1429.274    0.000 allGraphs.py:45(p)
               12154041 1204.688    0.000 1204.688    0.000 {built-in method tensor}
                 410012   78.289    0.000 1177.694    0.003 allGraphsTrain.py:37(<listcomp>)
               10399163    6.077    0.000 1140.674    0.000 game.py:37(board)
                 410013   58.569    0.000 1068.100    0.003 layers.py:684(update)
            14509283944  960.814    0.000  960.814    0.000 {built-in method builtins.hash}
                8349102   40.696    0.000  956.137    0.000 allGraphs.py:153(format)
                 410012    1.292    0.000  903.729    0.002 agent.py:29(learn)
                 410012    8.567    0.000  901.544    0.002 agent.py:117(_learn)
                 410012   26.076    0.000  892.977    0.002 learner.py:42(Qlearn)
                 410012   33.865    0.000  887.504    0.002 layers.py:17(step)
               41001200   69.043    0.000  849.730    0.000 layer.py:98(move)
               43461272  100.571    0.000  718.800    0.000 tensor.py:21(wrapped)
                 410012   33.664    0.000  685.361    0.002 allGraphsTrain.py:44(<listcomp>)
               43051260  495.691    0.000  495.691    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                 974503    8.908    0.000  473.428    0.000 layers.py:740(restart)
               41001200  461.668    0.000  461.668    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               41001200  114.302    0.000  458.305    0.000 layers.py:735(check)
                 974503    4.148    0.000  393.499    0.000 level.py:8(__init__)
                 410012  209.839    0.001  388.426    0.001 agent.py:67(modify)
                 410012    2.448    0.000  358.994    0.001 grad_mode.py:23(decorate_context)
                 974503   14.812    0.000  356.641    0.000 levels.py:249(generate)
                 410012   12.412    0.000  351.906    0.001 adam.py:55(step)
        9430276/1230036   36.893    0.000  347.754    0.000 module.py:715(_call_impl)
             1948394970  339.230    0.000  344.795    0.000 {built-in method builtins.max}
                6334103   58.526    0.000  326.473    0.000 level.py:41(notUsed)
                 820024    2.227    0.000  318.097    0.000 network.py:27(forward)
                 820024    8.396    0.000  310.626    0.000 container.py:115(forward)
                 410012   64.589    0.000  289.917    0.001 functional.py:53(adam)
               41001200   72.120    0.000  260.951    0.000 layers.py:729(isFree)
              113829092   68.997    0.000  245.841    0.000 {built-in method builtins.any}
                3690117  117.356    0.000  210.893    0.000 layer.py:167(NoRock_update)
                 410012    2.554    0.000  209.181    0.001 tensor.py:181(backward)
                 410012    1.443    0.000  206.627    0.001 __init__.py:68(backward)
                 410012  196.065    0.000  196.065    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
              365193777  146.270    0.000  188.831    0.000 layer.py:95(isFree)
                 410012    4.923    0.000  186.184    0.000 agent.py:112(__call__)
               84462572   33.076    0.000  170.116    0.000 {built-in method builtins.all}
                6334103    4.893    0.000  151.105    0.000 level.py:38(elementsIn)
               42641248  148.048    0.000  148.048    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                1230036    4.924    0.000  141.458    0.000 tensor.py:576(__iter__)
                1230036  133.517    0.000  133.517    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
              400267970  105.191    0.000  130.211    0.000 layers.py:700(<genexpr>)
              175372023   46.623    0.000  126.209    0.000 layers.py:690(<genexpr>)
                1640048    3.023    0.000  123.994    0.000 conv.py:422(forward)
                1640048    3.140    0.000  119.799    0.000 conv.py:414(_conv_forward)
               71342222   36.417    0.000  118.399    0.000 overrides.py:1070(has_torch_function)
                1640048  116.068    0.000  116.068    0.000 {built-in method conv2d}
                6334103   48.574    0.000   97.949    0.000 level.py:39(<listcomp>)
                1640048    3.928    0.000   91.523    0.000 linear.py:92(forward)
               22960726   53.404    0.000   88.741    0.000 tensor.py:933(grad)
                1640048    6.826    0.000   85.924    0.000 functional.py:1669(linear)
                 410012    7.786    0.000   78.032    0.000 optimizer.py:167(zero_grad)
               41001300   45.898    0.000   71.155    0.000 layers.py:113(isDone)
              298738175   70.246    0.000   70.246    0.000 level.py:32(inverse)
                8770527    7.079    0.000   68.175    0.000 layer.py:69(restart)
              655025344   63.606    0.000   63.606    0.000 layer.py:91(positions)
                 410012    3.086    0.000   63.219    0.000 agent.py:59(modify_board)
                 410012   35.997    0.000   62.044    0.000 collector.py:46(collect)
                1640048   60.674    0.000   60.674    0.000 {built-in method addmm}
               20497416   36.126    0.000   59.336    0.000 layers.py:387(check)
               20501777   36.027    0.000   58.993    0.000 layers.py:337(check)
               20493130   35.086    0.000   58.098    0.000 layers.py:349(check)
                6560192   57.796    0.000   57.796    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               20498010   34.837    0.000   57.411    0.000 layers.py:375(check)
              156012004   53.448    0.000   53.448    0.000 layer.py:146(elements)
                 974603   25.679    0.000   50.575    0.000 layers.py:36(reset)
              263111381   48.322    0.000   48.322    0.000 enum.py:352(<genexpr>)
                6560192   48.279    0.000   48.279    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                6334103   30.130    0.000   48.264    0.000 {built-in method _functools.reduce}
              187785764   39.077    0.000   46.359    0.000 overrides.py:1083(<genexpr>)
                 410012   30.231    0.000   44.520    0.000 allGraphsTrain.py:43(<listcomp>)
                 410012   41.321    0.000   41.321    0.000 {built-in method torch._C._nn.one_hot}
                2460072    2.256    0.000   40.896    0.000 activation.py:713(forward)
               74705576   29.963    0.000   40.448    0.000 layer.py:130(add)
                2460072    3.286    0.000   38.640    0.000 functional.py:1292(leaky_relu)
                3280096   36.208    0.000   36.208    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              365193777   35.087    0.000   35.087    0.000 layer.py:203(isBlocking)
                2460072   35.014    0.000   35.014    0.000 {built-in method torch._C._nn.leaky_relu}
              425485844   33.842    0.000   33.842    0.000 {method 'random' of '_random.Random' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9532013: <Diamonds2_0.5_var_1> in cluster <dcc> Done

Job <Diamonds2_0.5_var_1> was submitted from host <n-62-30-7> by user <s183905> in cluster <dcc> at Sat Apr 17 13:28:41 2021
Job was executed on host(s) <n-62-11-13>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sun Apr 18 09:49:18 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun Apr 18 09:49:18 2021
Terminated at Sun Apr 18 19:44:24 2021
Results reported at Sun Apr 18 19:44:24 2021

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

    CPU time :                                   35638.58 sec.
    Max Memory :                                 2060 MB
    Average Memory :                             2059.70 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14324.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35706 sec.
    Turnaround time :                            108943 sec.

The output (if any) is above this job summary.

