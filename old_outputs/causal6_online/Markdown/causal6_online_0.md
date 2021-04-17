
# Parameters

    Name :                      causal6_online-0
    Main :                      graphTrain
    Level :                     Levels.Causal6
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
    Counterfacts :              1
    Topn :                      7
    Minutes used :              715 minutes.
    Hours used :                11 hours.

# Profiling


      35527591759 function calls (35514075576 primitive calls) in 42904.91 seconds

##    Ordered by: cumulative time
   List reduced from 460 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 42904.907 42904.907 {built-in method builtins.exec}
                      1    0.001    0.001 42904.907 42904.907 <string>:1(<module>)
                      1  165.275  165.275 42904.906 42904.906 allGraphsTrain.py:5(graphTrain)
                 675790 6313.670    0.009 15146.056    0.022 allGraphs.py:220(transformNot)
              810953900 9827.564    0.000 9827.564    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                 675790   17.810    0.000 9807.245    0.015 allGraphsTrain.py:27(<listcomp>)
               68254891 2256.512    0.000 9789.455    0.000 allGraphs.py:141(states)
              743369500 7197.835    0.000 7197.835    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 675790  630.630    0.001 6665.204    0.010 allGraphsTrain.py:33(<listcomp>)
               10724194   64.822    0.000 6034.574    0.001 allGraphs.py:228(getInterventions)
                9982287   61.345    0.000 4740.786    0.000 allGraphs.py:188(rightIntervention)
                 675790    2.450    0.000 4547.347    0.007 game.py:41(step)
                 675790    3.396    0.000 4401.455    0.007 layers.py:710(step)
               13365355  215.278    0.000 4293.947    0.000 allGraphs.py:192(<dictcomp>)
              335796199 1132.599    0.000 3998.151    0.000 allGraphs.py:163(flip_chance)
                 675791  101.700    0.000 2642.461    0.004 layers.py:676(update)
             2501595428 1596.426    0.000 2401.845    0.000 allGraphs.py:157(compress)
             8693798737 1383.744    0.000 2071.017    0.000 enum.py:646(__hash__)
                 675790  128.195    0.000 1942.518    0.003 allGraphsTrain.py:35(<listcomp>)
                 675790   50.590    0.000 1751.797    0.003 layers.py:17(step)
               67579000  113.814    0.000 1695.425    0.000 layer.py:98(move)
                3494131   28.656    0.000 1609.780    0.000 layers.py:731(restart)
               16974791 1545.763    0.000 1545.763    0.000 {built-in method tensor}
                 675790    2.253    0.000 1506.492    0.002 agent.py:29(learn)
                 675790   14.434    0.000 1502.797    0.002 agent.py:117(_learn)
                 675790   43.944    0.000 1488.363    0.002 learner.py:42(Qlearn)
               14103145    8.964    0.000 1449.264    0.000 game.py:37(board)
                3494131   13.345    0.000 1329.970    0.000 level.py:8(__init__)
               71633740  175.496    0.000 1204.449    0.000 tensor.py:21(wrapped)
                3494131   47.667    0.000 1203.933    0.000 levels.py:293(generate)
                 675790   54.842    0.000 1146.151    0.002 allGraphsTrain.py:42(<listcomp>)
               20963172  196.985    0.000 1104.499    0.000 level.py:41(notUsed)
               67579000  177.689    0.000 1059.032    0.000 layers.py:727(check)
               70957950  815.302    0.000  815.302    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
              502141544  231.848    0.000  795.355    0.000 {built-in method builtins.any}
               67579000  757.953    0.000  757.953    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                 675790  393.246    0.001  692.758    0.001 agent.py:67(modify)
             8693800974  687.273    0.000  687.273    0.000 {built-in method builtins.hash}
                 675790    4.236    0.000  594.123    0.001 grad_mode.py:23(decorate_context)
        15543170/2027370   65.064    0.000  591.184    0.000 module.py:715(_call_impl)
                 675790   20.405    0.000  582.286    0.001 adam.py:55(step)
                1351580    3.421    0.000  539.315    0.000 network.py:24(forward)
                1351580   14.308    0.000  527.434    0.000 container.py:115(forward)
               20963172   15.057    0.000  515.432    0.000 level.py:38(elementsIn)
                 675790  106.972    0.000  474.175    0.001 functional.py:53(adam)
               67579000  116.100    0.000  416.928    0.000 layers.py:721(isFree)
                5406328  228.983    0.000  389.249    0.000 layer.py:167(NoRock_update)
                 675790    3.703    0.000  340.866    0.001 tensor.py:181(backward)
                 675790    2.580    0.000  337.163    0.000 __init__.py:68(backward)
               20963172  162.375    0.000  330.841    0.000 level.py:39(<listcomp>)
                 675790  319.307    0.000  319.307    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
              139212840   53.603    0.000  314.543    0.000 {built-in method builtins.all}
                 675790    8.249    0.000  313.758    0.000 agent.py:112(__call__)
              533369432  234.296    0.000  300.828    0.000 layer.py:95(isFree)
               67579000  185.201    0.000  300.491    0.000 layers.py:418(check)
              786569392  180.533    0.000  293.053    0.000 allGraphs.py:192(<genexpr>)
                 675790   56.848    0.000  243.395    0.000 allGraphs.py:209(transform)
                2027370    8.091    0.000  243.189    0.000 tensor.py:576(__iter__)
              267143626   73.824    0.000  241.559    0.000 layers.py:682(<genexpr>)
               27953048   23.094    0.000  241.336    0.000 layer.py:69(restart)
               70282160  241.228    0.000  241.228    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              994356815  236.365    0.000  236.365    0.000 level.py:32(inverse)
                2027370  229.851    0.000  229.851    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
                2703160    4.833    0.000  207.726    0.000 conv.py:422(forward)
              117587594   62.819    0.000  206.669    0.000 overrides.py:1070(has_torch_function)
                2703160    5.505    0.000  201.018    0.000 conv.py:414(_conv_forward)
               67579000  125.039    0.000  195.345    0.000 layers.py:431(check)
                2703160  194.464    0.000  194.464    0.000 {built-in method conv2d}
               67579000  121.267    0.000  192.320    0.000 layers.py:446(check)
              576764721  156.586    0.000  191.851    0.000 layers.py:692(<genexpr>)
               87692399  106.476    0.000  189.424    0.000 allGraphs.py:150(expand)
                3494231   92.775    0.000  184.458    0.000 layers.py:30(reset)
               20963172  105.505    0.000  169.534    0.000 {built-in method _functools.reduce}
              880464434  163.022    0.000  163.022    0.000 enum.py:352(<genexpr>)
               37844294   93.890    0.000  156.214    0.000 tensor.py:933(grad)
                2703160    6.271    0.000  155.264    0.000 linear.py:92(forward)
                2703160   11.302    0.000  145.976    0.000 functional.py:1669(linear)
             1411871270  135.552    0.000  135.552    0.000 layer.py:91(positions)
                 675790   13.523    0.000  134.136    0.000 optimizer.py:167(zero_grad)
                 741907   27.189    0.000  128.166    0.000 allGraphs.py:170(bestIntervention)
               13365355   17.554    0.000  110.237    0.000 allGraphs.py:198(<dictcomp>)
               67579100   69.858    0.000  110.176    0.000 layers.py:451(isDone)
              197936708   77.907    0.000  107.117    0.000 layer.py:130(add)
                 675790    4.925    0.000  105.803    0.000 agent.py:59(modify_board)
                3494131   48.251    0.000  103.769    0.000 level.py:16(<dictcomp>)
                 675790   60.569    0.000  103.713    0.000 collector.py:53(collect)
                2703160  102.987    0.000  102.987    0.000 {built-in method addmm}
              403201723   98.165    0.000   98.165    0.000 layer.py:146(elements)
               10812640   95.615    0.000   95.615    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               67579000   58.288    0.000   88.379    0.000 layers.py:407(check)
               67579000   56.524    0.000   87.245    0.000 layers.py:396(check)
              309512088   69.162    0.000   81.931    0.000 overrides.py:1083(<genexpr>)
        933027984/933027982   69.353    0.000   80.802    0.000 {built-in method builtins.len}
                 675790   54.801    0.000   79.465    0.000 allGraphsTrain.py:41(<listcomp>)
               10812640   79.330    0.000   79.330    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                4054740    3.774    0.000   69.633    0.000 activation.py:713(forward)
                 675790   69.423    0.000   69.423    0.000 {built-in method torch._C._nn.one_hot}
                4054740    6.318    0.000   65.859    0.000 functional.py:1292(leaky_relu)
              733711020   64.029    0.000   64.029    0.000 level.py:39(<lambda>)
                4054740   58.955    0.000   58.955    0.000 {built-in method torch._C._nn.leaky_relu}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-13>
Subject: Job 9507355: <causal6_online_0> in cluster <dcc> Done

Job <causal6_online_0> was submitted from host <n-62-27-21> by user <s183905> in cluster <dcc> at Fri Apr  9 21:48:59 2021
Job was executed on host(s) <n-62-20-13>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Fri Apr  9 22:38:40 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Fri Apr  9 22:38:40 2021
Terminated at Sat Apr 10 10:33:47 2021
Results reported at Sat Apr 10 10:33:47 2021

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

    CPU time :                                   42802.93 sec.
    Max Memory :                                 2090 MB
    Average Memory :                             2089.12 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14294.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   42907 sec.
    Turnaround time :                            45888 sec.

The output (if any) is above this job summary.

