
# Parameters

    Name :                      Diamonds2_0.0_var-1
    Main :                      graphTrain
    Level :                     Levels.Causal5
    Failed actions chance :     0.0
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


      39998668137 function calls (35809831208 primitive calls) in 35712.13 seconds

##    Ordered by: cumulative time
   List reduced from 466 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35712.134 35712.134 {built-in method builtins.exec}
                      1    0.001    0.001 35712.134 35712.134 <string>:1(<module>)
                      1  156.589  156.589 35712.132 35712.132 allGraphsTrain.py:10(graphTrain)
                 428282 4558.504    0.011 11360.335    0.027 allGraphs.py:146(transformNot)
                 428282  463.066    0.001 9236.325    0.022 allGraphsTrain.py:35(<listcomp>)
                6107422   12.960    0.000 8773.258    0.001 allGraphs.py:158(getInterventions)
                5496135    5.736    0.000 8000.205    0.001 allGraphs.py:129(rightIntervention)
        718717769/5496135  390.640    0.000 7967.022    0.001 {built-in method builtins.min}
               20298319    9.386    0.000 7955.394    0.000 allGraphs.py:130(<lambda>)
              599598824 7947.756    0.000 7947.756    0.000 {method 'item' of 'torch._C._TensorBase' objects}
        1431939403/20298319 2304.256    0.000 7946.008    0.000 allGraphs.py:74(expected_moves)
        2124862718/69454530  613.838    0.000 7795.904    0.000 allGraphs.py:78(<genexpr>)
                 428282   11.816    0.000 7735.232    0.018 allGraphsTrain.py:29(<listcomp>)
               43256583 1708.973    0.000 7723.465    0.000 allGraphs.py:110(states)
              556767200 5321.293    0.000 5321.293    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 428282    2.151    0.000 2792.544    0.007 game.py:41(step)
                 428282    3.046    0.000 2687.514    0.006 layers.py:718(step)
            11299427275 1803.006    0.000 2623.903    0.000 enum.py:646(__hash__)
              719329056  401.113    0.000 2569.353    0.000 allGraphs.py:83(layers_not_in)
              719329056 1017.827    0.000 2168.240    0.000 allGraphs.py:84(<listcomp>)
                 428282   40.735    0.000 1404.174    0.003 layers.py:17(step)
               42828200   73.448    0.000 1359.586    0.000 layer.py:98(move)
                 428282   80.142    0.000 1293.587    0.003 allGraphsTrain.py:37(<listcomp>)
                 428283   68.460    0.000 1276.501    0.003 layers.py:684(update)
                 428282    2.022    0.000 1064.256    0.002 agent.py:29(learn)
               10080529 1061.736    0.000 1061.736    0.000 {built-in method tensor}
                 428282   11.070    0.000 1061.197    0.002 agent.py:117(_learn)
                 428282   32.745    0.000 1050.127    0.002 learner.py:42(Qlearn)
             1431939403  708.844    0.000 1041.829    0.000 allGraphs.py:45(p)
                8248833    5.689    0.000  976.733    0.000 game.py:37(board)
               42828200  175.443    0.000  858.550    0.000 layers.py:735(check)
            11299428712  820.897    0.000  820.897    0.000 {built-in method builtins.hash}
               45397892  110.922    0.000  765.162    0.000 tensor.py:21(wrapped)
                6107422   32.004    0.000  748.340    0.000 allGraphs.py:153(format)
                 428282   33.713    0.000  716.381    0.002 allGraphsTrain.py:44(<listcomp>)
                1312242   13.317    0.000  651.107    0.000 layers.py:740(restart)
                1312242    6.361    0.000  538.457    0.000 level.py:8(__init__)
               44969610  521.116    0.000  521.116    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               42828200  488.433    0.000  488.433    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                1312242   19.826    0.000  484.453    0.000 levels.py:249(generate)
                 428282  254.606    0.001  484.333    0.001 agent.py:67(modify)
        9850486/1284846   50.223    0.000  461.103    0.000 module.py:715(_call_impl)
                8530526   78.655    0.000  443.504    0.000 level.py:41(notUsed)
                 856564    2.964    0.000  417.709    0.000 network.py:27(forward)
                 856564   11.248    0.000  407.536    0.000 container.py:115(forward)
                 428282    3.890    0.000  391.448    0.001 grad_mode.py:23(decorate_context)
                 428282   15.398    0.000  380.216    0.001 adam.py:55(step)
               42828200   79.215    0.000  350.874    0.000 layers.py:729(isFree)
                 428282   69.707    0.000  310.840    0.001 functional.py:53(adam)
              383096160  224.397    0.000  271.659    0.000 layer.py:95(isFree)
                3854547  151.165    0.000  265.146    0.000 layer.py:167(NoRock_update)
                 428282    9.424    0.000  263.068    0.001 agent.py:112(__call__)
                 428282    3.163    0.000  261.708    0.001 tensor.py:181(backward)
                 428282    2.592    0.000  258.545    0.001 __init__.py:68(backward)
              118606953   71.951    0.000  254.594    0.000 {built-in method builtins.any}
             1433835536  249.036    0.000  253.691    0.000 {built-in method builtins.max}
                 428282  243.760    0.001  243.760    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                8530526    6.344    0.000  204.391    0.000 level.py:38(elementsIn)
                1284846    7.228    0.000  183.340    0.000 tensor.py:576(__iter__)
                1284846  171.286    0.000  171.286    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
                1713128    3.771    0.000  169.027    0.000 conv.py:422(forward)
                1713128    5.116    0.000  163.688    0.000 conv.py:414(_conv_forward)
                1713128  157.888    0.000  157.888    0.000 {built-in method conv2d}
               44541328  152.422    0.000  152.422    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               88226192   29.032    0.000  133.857    0.000 {built-in method builtins.all}
              415160580  107.723    0.000  132.213    0.000 layers.py:700(<genexpr>)
                8530526   64.540    0.000  132.042    0.000 level.py:39(<listcomp>)
               42828200   81.712    0.000  128.094    0.000 layers.py:349(check)
               42828200   79.495    0.000  127.060    0.000 layers.py:387(check)
               74521202   39.249    0.000  126.464    0.000 overrides.py:1070(has_torch_function)
                1713128    4.725    0.000  119.687    0.000 linear.py:92(forward)
               42828200   72.970    0.000  116.589    0.000 layers.py:337(check)
               42828200   70.848    0.000  115.149    0.000 layers.py:375(check)
                1713128    8.435    0.000  112.707    0.000 functional.py:1669(linear)
             1044911575  100.565    0.000  100.565    0.000 layer.py:91(positions)
              402326226   97.193    0.000   97.193    0.000 level.py:32(inverse)
               11810178    9.706    0.000   95.438    0.000 layer.py:69(restart)
               23983846   57.732    0.000   95.066    0.000 tensor.py:933(grad)
              133777451   35.114    0.000   93.289    0.000 layers.py:690(<genexpr>)
                 428282    4.518    0.000   85.243    0.000 agent.py:59(modify_board)
                 428282    8.115    0.000   82.189    0.000 optimizer.py:167(zero_grad)
                1713128   81.805    0.000   81.805    0.000 {built-in method addmm}
              188401943   70.099    0.000   70.099    0.000 layer.py:146(elements)
                 428282   39.097    0.000   68.014    0.000 collector.py:46(collect)
                1312342   33.600    0.000   67.563    0.000 layers.py:36(reset)
              354341213   66.705    0.000   66.705    0.000 enum.py:352(<genexpr>)
                8530526   41.109    0.000   66.004    0.000 {built-in method _functools.reduce}
                6852512   61.670    0.000   61.670    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               42828200   38.754    0.000   57.962    0.000 layers.py:364(check)
                 428282   55.895    0.000   55.895    0.000 {built-in method torch._C._nn.one_hot}
               90996030   40.407    0.000   55.624    0.000 layer.py:130(add)
               42828200   35.336    0.000   54.401    0.000 layers.py:326(check)
                 428282   35.822    0.000   51.260    0.000 allGraphsTrain.py:43(<listcomp>)
                6852512   50.691    0.000   50.691    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                 428282   13.752    0.000   50.384    0.000 allGraphs.py:137(transform)
                2569692    3.357    0.000   50.381    0.000 activation.py:713(forward)
              196153424   42.316    0.000   50.104    0.000 overrides.py:1083(<genexpr>)
                2569692    5.326    0.000   47.023    0.000 functional.py:1292(leaky_relu)
               42828200   31.001    0.000   45.782    0.000 layers.py:23(check)
                1312242   20.711    0.000   43.396    0.000 level.py:16(<dictcomp>)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9532038: <Diamonds2_0.0_var_1> in cluster <dcc> Done

Job <Diamonds2_0.0_var_1> was submitted from host <n-62-30-7> by user <s183905> in cluster <dcc> at Sat Apr 17 13:28:45 2021
Job was executed on host(s) <n-62-20-10>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Tue Apr 20 06:00:36 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue Apr 20 06:00:36 2021
Terminated at Tue Apr 20 15:55:57 2021
Results reported at Tue Apr 20 15:55:57 2021

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

    CPU time :                                   35619.89 sec.
    Max Memory :                                 2065 MB
    Average Memory :                             2059.14 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14319.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35722 sec.
    Turnaround time :                            268032 sec.

The output (if any) is above this job summary.

