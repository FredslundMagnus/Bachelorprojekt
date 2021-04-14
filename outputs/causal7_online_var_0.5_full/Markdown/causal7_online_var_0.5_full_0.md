
# Parameters

    Name :                      causal7_online_var_0.5_full-0
    Main :                      graphTrain
    Level :                     Levels.Causal7
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
    Cf convert :                3
    Counterfacts :              2
    Topn :                      5
    Minutes used :              715 minutes.
    Hours used :                11 hours.

# Profiling


      24197001071 function calls (23362254620 primitive calls) in 42911.95 seconds

##    Ordered by: cumulative time
   List reduced from 466 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 42911.948 42911.948 {built-in method builtins.exec}
                      1    0.001    0.001 42911.948 42911.948 <string>:1(<module>)
                      1  213.402  213.402 42911.947 42911.947 allGraphsTrain.py:10(graphTrain)
                 928950 6654.029    0.007 16059.380    0.017 allGraphs.py:120(transformNot)
              928957824 10486.435    0.000 10486.435    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                 928950   20.777    0.000 10008.340    0.011 allGraphsTrain.py:29(<listcomp>)
               93824051 2337.234    0.000 9987.617    0.000 allGraphs.py:88(states)
              836055400 7406.345    0.000 7406.345    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 928950  849.989    0.001 4578.079    0.005 allGraphsTrain.py:35(<listcomp>)
                 928950    3.294    0.000 3985.388    0.004 game.py:41(step)
                 928950    4.495    0.000 3800.712    0.004 layers.py:718(step)
               21814038  103.162    0.000 3728.090    0.000 allGraphs.py:127(getInterventions)
                 928950  166.517    0.000 2472.045    0.003 allGraphsTrain.py:37(<listcomp>)
               30394096 2443.303    0.000 2443.303    0.000 {built-in method tensor}
               26458789   14.894    0.000 2327.593    0.000 game.py:37(board)
                 928951  126.307    0.000 2225.075    0.002 layers.py:684(update)
                 928950    3.145    0.000 1912.326    0.002 agent.py:29(learn)
                 928950   18.376    0.000 1907.289    0.002 agent.py:117(_learn)
                 928950   57.443    0.000 1888.913    0.002 learner.py:42(Qlearn)
               20847355   16.188    0.000 1711.004    0.000 allGraphs.py:107(rightIntervention)
        185912880/20847355  116.853    0.000 1617.501    0.000 {built-in method builtins.min}
               52489174   22.278    0.000 1587.047    0.000 allGraphs.py:108(<lambda>)
                 928950   66.214    0.000 1566.098    0.002 layers.py:17(step)
        350978405/52489174  486.029    0.000 1564.769    0.000 allGraphs.py:52(expected_moves)
               98468700  218.099    0.000 1521.594    0.000 tensor.py:21(wrapped)
               92895000  137.647    0.000 1491.802    0.000 layer.py:98(move)
                 928950   68.877    0.000 1446.964    0.002 allGraphsTrain.py:44(<listcomp>)
        463554756/110942444  132.149    0.000 1286.364    0.000 allGraphs.py:56(<genexpr>)
                2948785   23.323    0.000 1070.229    0.000 layers.py:740(restart)
               97539750 1039.200    0.000 1039.200    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               92895000  954.821    0.000  954.821    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                2948785   10.767    0.000  856.741    0.000 level.py:8(__init__)
                 928950  463.159    0.000  846.918    0.001 agent.py:67(modify)
             3446551450  551.168    0.000  805.512    0.000 enum.py:646(__hash__)
                 928950    5.285    0.000  752.576    0.001 grad_mode.py:23(decorate_context)
        21365850/2786850   79.008    0.000  749.453    0.000 module.py:715(_call_impl)
                2948785   32.146    0.000  745.533    0.000 levels.py:446(generate)
               92895000  191.704    0.000  737.439    0.000 layers.py:735(check)
                 928950   26.793    0.000  736.654    0.001 adam.py:55(step)
                1857900    4.415    0.000  684.684    0.000 network.py:24(forward)
               14155003  123.043    0.000  679.973    0.000 level.py:41(notUsed)
                1857900   18.604    0.000  669.488    0.000 container.py:115(forward)
                 928950  134.922    0.000  602.288    0.001 functional.py:53(adam)
              186879563  115.059    0.000  515.519    0.000 allGraphs.py:61(layers_not_in)
               92895000  127.751    0.000  483.674    0.000 layers.py:729(isFree)
              257157450  134.030    0.000  468.197    0.000 {built-in method builtins.any}
                 928950    4.799    0.000  438.226    0.000 tensor.py:181(backward)
                 928950    3.092    0.000  433.427    0.000 __init__.py:68(backward)
                 928950  410.862    0.000  410.862    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                6502657  235.591    0.000  405.796    0.000 layer.py:167(NoRock_update)
                 928950   11.270    0.000  401.317    0.000 agent.py:112(__call__)
              186879563  199.285    0.000  400.460    0.000 allGraphs.py:62(<listcomp>)
              613120185  284.331    0.000  355.923    0.000 layer.py:95(isFree)
              191363800   68.456    0.000  351.693    0.000 {built-in method builtins.all}
               14155003    9.622    0.000  321.434    0.000 level.py:38(elementsIn)
               96610800  305.659    0.000  305.659    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                2786850   10.565    0.000  304.301    0.000 tensor.py:576(__iter__)
                2786850  287.232    0.000  287.232    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
                3715800    6.110    0.000  266.288    0.000 conv.py:422(forward)
              392772989  108.004    0.000  258.982    0.000 layers.py:690(<genexpr>)
                3715800    7.139    0.000  257.725    0.000 conv.py:414(_conv_forward)
              161637434   78.065    0.000  256.712    0.000 overrides.py:1070(has_torch_function)
             3446554487  254.345    0.000  254.345    0.000 {built-in method builtins.hash}
                3715800  249.284    0.000  249.284    0.000 {built-in method conv2d}
              350978405  167.561    0.000  246.293    0.000 allGraphs.py:37(p)
              719570520  189.108    0.000  230.737    0.000 layers.py:700(<genexpr>)
               14155003  103.225    0.000  205.448    0.000 level.py:39(<listcomp>)
                3715800    8.081    0.000  197.738    0.000 linear.py:92(forward)
               52021254  115.002    0.000  192.289    0.000 tensor.py:933(grad)
                3715800   14.391    0.000  185.641    0.000 functional.py:1669(linear)
               20641495   15.121    0.000  183.242    0.000 layer.py:69(restart)
                 928950   16.393    0.000  167.096    0.000 optimizer.py:167(zero_grad)
                2948885   72.398    0.000  145.124    0.000 layers.py:36(reset)
              679616219  140.104    0.000  140.104    0.000 level.py:32(inverse)
                 928950    6.639    0.000  137.060    0.000 agent.py:59(modify_board)
                 928950   77.392    0.000  132.282    0.000 collector.py:46(collect)
                3715800  131.357    0.000  131.357    0.000 {built-in method addmm}
               46450456   79.164    0.000  128.953    0.000 layers.py:617(check)
               46449307   78.110    0.000  128.122    0.000 layers.py:632(check)
               46450583   76.504    0.000  126.064    0.000 layers.py:602(check)
               14863200  121.881    0.000  121.881    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
             1279510845  116.907    0.000  116.907    0.000 layer.py:91(positions)
               14155003   66.302    0.000  106.364    0.000 {built-in method _functools.reduce}
              615737858  104.548    0.000  104.548    0.000 enum.py:352(<genexpr>)
              425459368   86.541    0.000  102.838    0.000 overrides.py:1083(<genexpr>)
              398635580  102.574    0.000  102.574    0.000 layer.py:146(elements)
               14863200  101.092    0.000  101.092    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                 928950   66.691    0.000   99.970    0.000 allGraphsTrain.py:43(<listcomp>)
              193985360   71.782    0.000   99.331    0.000 layer.py:130(add)
                2948785   50.092    0.000   93.806    0.000 level.py:16(<dictcomp>)
                 928950   90.443    0.000   90.443    0.000 {built-in method torch._C._nn.one_hot}
                5573700    5.350    0.000   88.277    0.000 activation.py:713(forward)
                5573700    7.495    0.000   82.927    0.000 functional.py:1292(leaky_relu)
               46055868   51.872    0.000   77.734    0.000 layers.py:113(isDone)
                5573700   74.658    0.000   74.658    0.000 {built-in method torch._C._nn.leaky_relu}
                 928950   19.682    0.000   72.938    0.000 allGraphs.py:111(transform)
              354731938   68.766    0.000   72.739    0.000 {built-in method builtins.max}
                7431600   70.035    0.000   70.035    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                2786850   64.898    0.000   64.898    0.000 {method 'tolist' of 'torch._C._TensorBase' objects}
                7431600   64.211    0.000   64.211    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-4>
Subject: Job 9511706: <causal7_online_var_0.5_full_0> in cluster <dcc> Done

Job <causal7_online_var_0.5_full_0> was submitted from host <n-62-27-18> by user <s183905> in cluster <dcc> at Mon Apr 12 21:45:53 2021
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Tue Apr 13 08:12:37 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue Apr 13 08:12:37 2021
Terminated at Tue Apr 13 20:07:57 2021
Results reported at Tue Apr 13 20:07:57 2021

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

    CPU time :                                   42802.84 sec.
    Max Memory :                                 2079 MB
    Average Memory :                             2075.13 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14305.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   42921 sec.
    Turnaround time :                            80524 sec.

The output (if any) is above this job summary.

