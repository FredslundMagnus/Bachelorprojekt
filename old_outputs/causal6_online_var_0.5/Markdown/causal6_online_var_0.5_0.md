
# Parameters

    Name :                      causal6_online_var_0.5-0
    Main :                      graphTrain
    Level :                     Levels.Causal6
    Failed actions chance :     0.5
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


      41054144378 function calls (36888869963 primitive calls) in 42908.44 seconds

##    Ordered by: cumulative time
   List reduced from 464 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 42908.442 42908.442 {built-in method builtins.exec}
                      1    0.001    0.001 42908.442 42908.442 <string>:1(<module>)
                      1  180.031  180.031 42908.442 42908.442 allGraphsTrain.py:10(graphTrain)
                 607868 5535.734    0.009 14059.504    0.023 allGraphs.py:120(transformNot)
              729446956 10177.417    0.000 10177.417    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                 607868  697.989    0.001 9807.495    0.016 allGraphsTrain.py:35(<listcomp>)
                 607868   15.187    0.000 9270.311    0.015 allGraphsTrain.py:29(<listcomp>)
               61394769 1995.759    0.000 9255.171    0.000 allGraphs.py:88(states)
               12549179   67.979    0.000 9109.506    0.001 allGraphs.py:127(getInterventions)
               11540696   10.349    0.000 7647.952    0.001 allGraphs.py:107(rightIntervention)
        742100465/11540696  414.519    0.000 7584.937    0.001 {built-in method builtins.min}
               46740905   20.757    0.000 7561.573    0.000 allGraphs.py:108(<lambda>)
        1472660234/46740905 2231.376    0.000 7540.816    0.000 allGraphs.py:52(expected_moves)
        2156479098/159841524  611.283    0.000 7227.389    0.000 allGraphs.py:56(<genexpr>)
              668655300 6301.384    0.000 6301.384    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 607868    2.808    0.000 3573.383    0.006 game.py:41(step)
                 607868    3.691    0.000 3431.420    0.006 layers.py:712(step)
            10388724478 1636.001    0.000 2399.050    0.000 enum.py:646(__hash__)
              743108948  409.186    0.000 2355.165    0.000 allGraphs.py:61(layers_not_in)
                 607869   93.988    0.000 2115.923    0.003 layers.py:678(update)
              743108948  948.288    0.000 1945.979    0.000 allGraphs.py:62(<listcomp>)
                 607868  114.575    0.000 1837.187    0.003 allGraphsTrain.py:37(<listcomp>)
               18174791 1810.772    0.000 1810.772    0.000 {built-in method tensor}
               15588520    8.702    0.000 1720.238    0.000 game.py:37(board)
                 607868    2.687    0.000 1430.985    0.002 agent.py:29(learn)
                 607868   14.463    0.000 1426.881    0.002 agent.py:117(_learn)
                 607868   43.416    0.000 1412.417    0.002 learner.py:42(Qlearn)
                 607868   52.419    0.000 1307.252    0.002 layers.py:17(step)
               60786800  100.432    0.000 1249.230    0.000 layer.py:98(move)
                2531044   23.123    0.000 1170.412    0.000 layers.py:734(restart)
             1472660234  740.601    0.000 1085.175    0.000 allGraphs.py:37(p)
               64434008  154.674    0.000 1067.043    0.000 tensor.py:21(wrapped)
                 607868   45.991    0.000 1006.210    0.002 allGraphsTrain.py:44(<listcomp>)
                2531044   11.092    0.000  962.167    0.000 level.py:8(__init__)
                2531044   34.935    0.000  858.463    0.000 levels.py:293(generate)
               15186138  138.782    0.000  786.005    0.000 level.py:41(notUsed)
            10388726491  763.050    0.000  763.050    0.000 {built-in method builtins.hash}
               63826140  724.521    0.000  724.521    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               60786800  669.753    0.000  669.753    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                 607868  356.278    0.001  653.117    0.001 agent.py:67(modify)
               60786800  149.496    0.000  608.276    0.000 layers.py:729(check)
        13980964/1823604   64.329    0.000  580.720    0.000 module.py:715(_call_impl)
                 607868    4.617    0.000  546.098    0.001 grad_mode.py:23(decorate_context)
                 607868   21.582    0.000  532.531    0.001 adam.py:55(step)
                1215736    3.569    0.000  524.893    0.000 network.py:24(forward)
                1215736   14.420    0.000  511.673    0.000 container.py:115(forward)
               60786800   97.680    0.000  439.214    0.000 layers.py:723(isFree)
                 607868   95.838    0.000  433.881    0.001 functional.py:53(adam)
               15186138   10.925    0.000  366.907    0.000 level.py:38(elementsIn)
                4862952  202.903    0.000  348.526    0.000 layer.py:167(NoRock_update)
              167672231   99.344    0.000  347.502    0.000 {built-in method builtins.any}
                 607868    3.895    0.000  344.667    0.001 tensor.py:181(backward)
              482192503  280.925    0.000  341.534    0.000 layer.py:95(isFree)
                 607868    2.959    0.000  340.772    0.001 __init__.py:68(backward)
                 607868   10.449    0.000  323.987    0.001 agent.py:112(__call__)
                 607868  321.955    0.001  321.955    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
              125220908   44.201    0.000  293.396    0.000 {built-in method builtins.all}
             1475492321  258.609    0.000  265.455    0.000 {built-in method builtins.max}
               15186138  119.102    0.000  236.531    0.000 level.py:39(<listcomp>)
                1823604    8.499    0.000  234.738    0.000 tensor.py:576(__iter__)
              209641632   61.296    0.000  232.601    0.000 layers.py:684(<genexpr>)
                1823604  221.020    0.000  221.020    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               63218272  213.754    0.000  213.754    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                2431472    5.034    0.000  206.852    0.000 conv.py:422(forward)
                2431472    6.171    0.000  199.714    0.000 conv.py:414(_conv_forward)
                2431472  192.571    0.000  192.571    0.000 {built-in method conv2d}
              105769166   55.725    0.000  180.646    0.000 overrides.py:1070(has_torch_function)
               20248352   16.518    0.000  178.348    0.000 layer.py:69(restart)
              524302704  144.920    0.000  176.837    0.000 layers.py:694(<genexpr>)
              720329104  170.389    0.000  170.389    0.000 level.py:32(inverse)
                2431472    6.372    0.000  149.149    0.000 linear.py:92(forward)
                2431472   11.190    0.000  139.731    0.000 functional.py:1669(linear)
               30393207   85.174    0.000  137.754    0.000 layers.py:418(check)
               34040662   81.588    0.000  136.384    0.000 tensor.py:933(grad)
                2531144   65.751    0.000  131.543    0.000 layers.py:30(reset)
               15186138   74.368    0.000  119.451    0.000 {built-in method _functools.reduce}
                 607868   11.608    0.000  117.083    0.000 optimizer.py:167(zero_grad)
              637820078  116.348    0.000  116.348    0.000 enum.py:352(<genexpr>)
               60786900   72.005    0.000  114.160    0.000 layers.py:436(isDone)
                 607868    5.157    0.000  108.688    0.000 agent.py:59(modify_board)
                2431472  100.076    0.000  100.076    0.000 {built-in method addmm}
               30401438   60.639    0.000   95.513    0.000 layers.py:431(check)
                 607868   55.416    0.000   94.588    0.000 collector.py:46(collect)
               30390760   59.068    0.000   94.193    0.000 layers.py:446(check)
              312941065   90.184    0.000   90.184    0.000 layer.py:146(elements)
              864386472   88.038    0.000   88.038    0.000 layer.py:91(positions)
              152867649   63.637    0.000   87.006    0.000 layer.py:130(add)
                9725888   86.860    0.000   86.860    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                2531044   45.415    0.000   85.605    0.000 level.py:16(<dictcomp>)
                9725888   72.259    0.000   72.259    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                 607868   72.099    0.000   72.099    0.000 {built-in method torch._C._nn.one_hot}
                 607868   48.999    0.000   71.155    0.000 allGraphsTrain.py:43(<listcomp>)
              278403812   59.854    0.000   70.869    0.000 overrides.py:1083(<genexpr>)
                3647208    4.450    0.000   65.817    0.000 activation.py:713(forward)
                3647208    6.654    0.000   61.367    0.000 functional.py:1292(leaky_relu)
                 607868   15.365    0.000   58.503    0.000 allGraphs.py:111(transform)
                3647208   54.128    0.000   54.128    0.000 {built-in method torch._C._nn.leaky_relu}
                1823604   50.917    0.000   50.917    0.000 {method 'tolist' of 'torch._C._TensorBase' objects}
              482192503   49.899    0.000   49.899    0.000 layer.py:203(isBlocking)
                4862944   49.381    0.000   49.381    0.000 {method 'add' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-10>
Subject: Job 9511308: <causal6_online_var_0.5_0> in cluster <dcc> Done

Job <causal6_online_var_0.5_0> was submitted from host <n-62-27-21> by user <s183905> in cluster <dcc> at Mon Apr 12 16:10:31 2021
Job was executed on host(s) <n-62-20-10>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Mon Apr 12 16:29:34 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Apr 12 16:29:34 2021
Terminated at Tue Apr 13 04:24:48 2021
Results reported at Tue Apr 13 04:24:48 2021

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

    CPU time :                                   42799.68 sec.
    Max Memory :                                 2075 MB
    Average Memory :                             2073.62 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14309.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   42916 sec.
    Turnaround time :                            44057 sec.

The output (if any) is above this job summary.

