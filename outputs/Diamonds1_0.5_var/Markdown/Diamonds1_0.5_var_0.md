
# Parameters

    Name :                      Diamonds1_0.5_var-0
    Main :                      graphTrain
    Level :                     Levels.Causal2
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


      20590661778 function calls (19782503233 primitive calls) in 35710.40 seconds

##    Ordered by: cumulative time
   List reduced from 464 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35710.401 35710.401 {built-in method builtins.exec}
                      1    0.002    0.002 35710.401 35710.401 <string>:1(<module>)
                      1  187.994  187.994 35710.399 35710.399 allGraphsTrain.py:10(graphTrain)
                 710357 5155.691    0.007 13087.025    0.018 allGraphs.py:146(transformNot)
              710363080 9283.618    0.000 9283.618    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                 710357   16.458    0.000 8304.935    0.012 allGraphsTrain.py:29(<listcomp>)
               71746158 1825.331    0.000 8288.527    0.000 allGraphs.py:110(states)
              639321700 5880.334    0.000 5880.334    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 710357  766.516    0.001 3986.952    0.006 allGraphsTrain.py:35(<listcomp>)
                 710357    2.643    0.000 3513.624    0.005 game.py:41(step)
                 710357    3.830    0.000 3363.748    0.005 layers.py:718(step)
               16114417   25.460    0.000 3220.436    0.000 allGraphs.py:158(getInterventions)
                 710357  125.462    0.000 2067.095    0.003 allGraphsTrain.py:37(<listcomp>)
                 710358  102.345    0.000 2058.800    0.003 layers.py:684(update)
               22682407 1906.902    0.000 1906.902    0.000 {built-in method tensor}
               19666203   10.233    0.000 1810.606    0.000 game.py:37(board)
               15201987   13.829    0.000 1649.240    0.000 allGraphs.py:129(rightIntervention)
        173935015/15201987  108.228    0.000 1578.738    0.000 {built-in method builtins.min}
                 710357    2.515    0.000 1566.242    0.002 agent.py:29(learn)
                 710357   15.351    0.000 1562.130    0.002 agent.py:117(_learn)
               43385741   18.157    0.000 1554.799    0.000 allGraphs.py:130(<lambda>)
                 710357   46.230    0.000 1546.779    0.002 learner.py:42(Qlearn)
        332668043/43385741  475.945    0.000 1536.642    0.000 allGraphs.py:74(expected_moves)
               16114417   65.107    0.000 1532.232    0.000 allGraphs.py:153(format)
                 710357   54.576    0.000 1296.639    0.002 layers.py:17(step)
        448015330/102079638  128.961    0.000 1292.642    0.000 allGraphs.py:78(<genexpr>)
               71035700  113.266    0.000 1235.286    0.000 layer.py:98(move)
               75297842  171.818    0.000 1197.545    0.000 tensor.py:21(wrapped)
                 710357   53.798    0.000 1134.532    0.002 allGraphsTrain.py:44(<listcomp>)
                2967691   23.031    0.000 1118.092    0.000 layers.py:740(restart)
                2967691   11.481    0.000  894.433    0.000 level.py:8(__init__)
               74587485  815.843    0.000  815.843    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                2967691   31.896    0.000  776.205    0.000 levels.py:151(generate)
               71035700  772.249    0.000  772.249    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
             3138077861  528.411    0.000  768.750    0.000 enum.py:646(__hash__)
                 710357  400.121    0.001  721.891    0.001 agent.py:67(modify)
               14244636  129.463    0.000  709.434    0.000 level.py:41(notUsed)
        16338211/2131071   65.651    0.000  626.814    0.000 module.py:715(_call_impl)
                 710357    4.822    0.000  600.700    0.001 grad_mode.py:23(decorate_context)
               71035700  154.952    0.000  596.371    0.000 layers.py:735(check)
                 710357   21.037    0.000  586.749    0.001 adam.py:55(step)
                1420714    3.853    0.000  569.427    0.000 network.py:27(forward)
                1420714   15.591    0.000  556.256    0.000 container.py:115(forward)
              174847445   99.866    0.000  494.644    0.000 allGraphs.py:83(layers_not_in)
                 710357  107.115    0.000  479.868    0.001 functional.py:53(adam)
               71035700  102.163    0.000  418.062    0.000 layers.py:729(isFree)
              174847445  191.988    0.000  394.778    0.000 allGraphs.py:84(<listcomp>)
                 710357    4.055    0.000  372.383    0.001 tensor.py:181(backward)
                 710357    2.950    0.000  368.328    0.001 __init__.py:68(backward)
              195932504  106.035    0.000  359.603    0.000 {built-in method builtins.any}
                 710357  348.621    0.000  348.621    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                4972506  202.240    0.000  344.494    0.000 layer.py:167(NoRock_update)
                 710357   10.229    0.000  341.883    0.000 agent.py:112(__call__)
               14244636   10.082    0.000  331.596    0.000 level.py:38(elementsIn)
              491130323  252.619    0.000  315.900    0.000 layer.py:95(isFree)
              146333642   54.186    0.000  288.716    0.000 {built-in method builtins.all}
                2131071    8.607    0.000  252.061    0.000 tensor.py:576(__iter__)
             3138080226  240.340    0.000  240.340    0.000 {built-in method builtins.hash}
               73877128  239.615    0.000  239.615    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                2131071  237.580    0.000  237.580    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
              332668043  160.544    0.000  236.732    0.000 allGraphs.py:45(p)
                2841428    5.291    0.000  225.009    0.000 conv.py:422(forward)
                2841428    6.398    0.000  217.572    0.000 conv.py:414(_conv_forward)
              308232772   81.186    0.000  216.822    0.000 layers.py:690(<genexpr>)
               14244636  104.390    0.000  215.262    0.000 level.py:39(<listcomp>)
                2841428  210.154    0.000  210.154    0.000 {built-in method conv2d}
              123602252   61.274    0.000  201.942    0.000 overrides.py:1070(has_torch_function)
               20773837   16.426    0.000  193.562    0.000 layer.py:69(restart)
              544544872  139.446    0.000  173.483    0.000 layers.py:700(<genexpr>)
                2841428    7.162    0.000  164.866    0.000 linear.py:92(forward)
                2841428   11.850    0.000  154.549    0.000 functional.py:1669(linear)
               39780046   93.283    0.000  153.523    0.000 tensor.py:933(grad)
                2967791   75.989    0.000  150.606    0.000 layers.py:36(reset)
              683919610  146.930    0.000  146.930    0.000 level.py:32(inverse)
                 710357   12.929    0.000  132.673    0.000 optimizer.py:167(zero_grad)
               71035800   78.929    0.000  120.843    0.000 layers.py:113(isDone)
                 710357    5.483    0.000  117.071    0.000 agent.py:59(modify_board)
              619645265  112.117    0.000  112.117    0.000 enum.py:352(<genexpr>)
                2841428  110.665    0.000  110.665    0.000 {built-in method addmm}
               14244636   66.346    0.000  106.252    0.000 {built-in method _functools.reduce}
               35519578   64.911    0.000  105.603    0.000 layers.py:231(check)
               35510237   64.552    0.000  105.222    0.000 layers.py:219(check)
                 710357   60.386    0.000  104.185    0.000 collector.py:46(collect)
               35519818   61.056    0.000  100.066    0.000 layers.py:207(check)
                2967691   51.560    0.000   99.284    0.000 level.py:16(<dictcomp>)
               11365712   96.616    0.000   96.616    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              174130071   66.988    0.000   92.355    0.000 layer.py:130(add)
              955819627   91.862    0.000   91.862    0.000 layer.py:91(positions)
              355840939   88.016    0.000   88.016    0.000 layer.py:146(elements)
               11365712   79.717    0.000   79.717    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              325343774   67.115    0.000   79.602    0.000 overrides.py:1083(<genexpr>)
                 710357   77.873    0.000   77.873    0.000 {built-in method torch._C._nn.one_hot}
                 710357   51.349    0.000   76.648    0.000 allGraphsTrain.py:43(<listcomp>)
                4262142    4.378    0.000   71.366    0.000 activation.py:713(forward)
              335711544   62.837    0.000   67.252    0.000 {built-in method builtins.max}
                4262142    6.392    0.000   66.988    0.000 functional.py:1292(leaky_relu)
                 710357   15.431    0.000   61.002    0.000 allGraphs.py:137(transform)
                4262142   60.001    0.000   60.001    0.000 {built-in method torch._C._nn.leaky_relu}
                2131071   56.214    0.000   56.214    0.000 {method 'tolist' of 'torch._C._TensorBase' objects}
                5682856   55.347    0.000   55.347    0.000 {method 'add' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9532009: <Diamonds1_0.5_var_0> in cluster <dcc> Done

Job <Diamonds1_0.5_var_0> was submitted from host <n-62-30-7> by user <s183905> in cluster <dcc> at Sat Apr 17 13:28:41 2021
Job was executed on host(s) <n-62-20-12>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sun Apr 18 09:14:50 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun Apr 18 09:14:50 2021
Terminated at Sun Apr 18 19:10:08 2021
Results reported at Sun Apr 18 19:10:08 2021

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

    CPU time :                                   35621.25 sec.
    Max Memory :                                 2060 MB
    Average Memory :                             2055.91 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14324.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35718 sec.
    Turnaround time :                            106887 sec.

The output (if any) is above this job summary.

