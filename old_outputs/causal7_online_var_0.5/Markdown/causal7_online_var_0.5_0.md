
# Parameters

    Name :                      causal7_online_var_0.5-0
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
    Cf convert :                2
    Counterfacts :              1
    Topn :                      7
    Minutes used :              715 minutes.
    Hours used :                11 hours.

# Profiling


      21513823946 function calls (20741930729 primitive calls) in 42907.71 seconds

##    Ordered by: cumulative time
   List reduced from 465 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 42907.706 42907.706 {built-in method builtins.exec}
                      1    0.001    0.001 42907.706 42907.706 <string>:1(<module>)
                      1  253.286  253.286 42907.704 42907.704 allGraphsTrain.py:10(graphTrain)
                 824422 6323.939    0.008 15943.786    0.019 allGraphs.py:120(transformNot)
              824428992 11359.024    0.000 11359.024    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                 824422   20.927    0.000 10099.399    0.012 allGraphsTrain.py:29(<listcomp>)
               83266723 2218.894    0.000 10078.484    0.000 allGraphs.py:88(states)
              741980200 7043.433    0.000 7043.433    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 824422  927.570    0.001 4422.036    0.005 allGraphsTrain.py:35(<listcomp>)
                 824422    4.063    0.000 4010.278    0.005 game.py:41(step)
                 824422    5.470    0.000 3826.214    0.005 layers.py:712(step)
               17632909   91.493    0.000 3494.466    0.000 allGraphs.py:127(getInterventions)
                 824422  157.745    0.000 2478.580    0.003 allGraphsTrain.py:37(<listcomp>)
               25250704 2253.430    0.000 2253.430    0.000 {built-in method tensor}
                 824423  126.182    0.000 2211.699    0.003 layers.py:678(update)
               21755020   12.956    0.000 2133.849    0.000 game.py:37(board)
                 824422    4.341    0.000 1973.854    0.002 agent.py:29(learn)
                 824422   20.147    0.000 1967.523    0.002 agent.py:117(_learn)
                 824422   59.747    0.000 1947.376    0.002 learner.py:42(Qlearn)
               16766091   14.405    0.000 1679.952    0.000 allGraphs.py:107(rightIntervention)
                 824422   73.742    0.000 1602.616    0.002 layers.py:17(step)
        169524676/16766091  113.707    0.000 1597.720    0.000 {built-in method builtins.min}
               46029838   20.312    0.000 1570.018    0.000 allGraphs.py:108(<lambda>)
        322283261/46029838  481.853    0.000 1549.706    0.000 allGraphs.py:52(expected_moves)
               82442200  142.551    0.000 1520.529    0.000 layer.py:98(move)
               87388732  213.328    0.000 1475.585    0.000 tensor.py:21(wrapped)
                 824422   64.126    0.000 1392.692    0.002 allGraphsTrain.py:44(<listcomp>)
        429012008/102619622  126.876    0.000 1279.103    0.000 allGraphs.py:56(<genexpr>)
                2743823   24.328    0.000 1100.020    0.000 layers.py:734(restart)
               86564310 1004.832    0.000 1004.832    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               82442200  906.926    0.000  906.926    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                 824422  470.946    0.001  878.850    0.001 agent.py:67(modify)
                2743823   12.283    0.000  875.892    0.000 level.py:8(__init__)
        18961706/2473266   90.631    0.000  800.755    0.000 module.py:715(_call_impl)
             3129245996  533.091    0.000  780.232    0.000 enum.py:646(__hash__)
                 824422    6.768    0.000  755.142    0.001 grad_mode.py:23(decorate_context)
                2743823   32.625    0.000  751.601    0.000 levels.py:446(generate)
                 824422   29.073    0.000  736.426    0.001 adam.py:55(step)
                1648844    5.113    0.000  723.833    0.000 network.py:24(forward)
                1648844   19.876    0.000  704.809    0.000 container.py:115(forward)
               13167362  126.635    0.000  684.591    0.000 level.py:41(notUsed)
               82442200  179.174    0.000  678.742    0.000 layers.py:729(check)
                 824422  134.750    0.000  600.981    0.001 functional.py:53(adam)
               82442200  125.431    0.000  554.176    0.000 layers.py:723(isFree)
              170391494  107.913    0.000  502.082    0.000 allGraphs.py:61(layers_not_in)
                 824422    5.436    0.000  470.229    0.001 tensor.py:181(backward)
                 824422    4.108    0.000  464.793    0.001 __init__.py:68(backward)
                 824422   14.537    0.000  446.181    0.001 agent.py:112(__call__)
                 824422  438.878    0.001  438.878    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
              228094572  128.112    0.000  436.307    0.000 {built-in method builtins.any}
                5770961  252.878    0.000  431.288    0.000 layer.py:167(NoRock_update)
              553332032  359.446    0.000  428.745    0.000 layer.py:95(isFree)
              170391494  197.888    0.000  394.168    0.000 allGraphs.py:62(<listcomp>)
                2473266   11.817    0.000  321.867    0.000 tensor.py:576(__iter__)
               13167362   10.093    0.000  319.409    0.000 level.py:38(elementsIn)
              169831032   60.708    0.000  304.297    0.000 {built-in method builtins.all}
                2473266  302.760    0.000  302.760    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               85739888  284.779    0.000  284.779    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                3297688    7.283    0.000  284.686    0.000 conv.py:422(forward)
                3297688    8.971    0.000  274.526    0.000 conv.py:414(_conv_forward)
                3297688  264.228    0.000  264.228    0.000 {built-in method conv2d}
              322283261  171.117    0.000  248.343    0.000 allGraphs.py:37(p)
             3129248713  247.142    0.000  247.142    0.000 {built-in method builtins.hash}
              143449562   74.790    0.000  245.329    0.000 overrides.py:1070(has_torch_function)
              300738860   88.162    0.000  221.550    0.000 layers.py:684(<genexpr>)
              637587816  172.829    0.000  211.793    0.000 layers.py:694(<genexpr>)
                3297688    8.661    0.000  208.224    0.000 linear.py:92(forward)
               13167362  102.641    0.000  204.631    0.000 level.py:39(<listcomp>)
                3297688   15.256    0.000  194.964    0.000 functional.py:1669(linear)
               19206761   17.447    0.000  192.493    0.000 layer.py:69(restart)
               46167686  116.930    0.000  190.092    0.000 tensor.py:933(grad)
                 824422   16.375    0.000  163.533    0.000 optimizer.py:167(zero_grad)
                 824422    8.219    0.000  149.582    0.000 agent.py:59(modify_board)
                2743923   72.953    0.000  145.843    0.000 layers.py:30(reset)
              632203616  140.992    0.000  140.992    0.000 level.py:32(inverse)
                3297688  140.042    0.000  140.042    0.000 {built-in method addmm}
               41221506   81.618    0.000  129.470    0.000 layers.py:596(check)
                 824422   75.771    0.000  128.891    0.000 collector.py:46(collect)
               41225608   79.829    0.000  127.683    0.000 layers.py:626(check)
               41229064   79.729    0.000  127.535    0.000 layers.py:611(check)
               13190752  121.528    0.000  121.528    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              363768258  110.583    0.000  110.583    0.000 layer.py:146(elements)
              572804150  107.871    0.000  107.871    0.000 enum.py:352(<genexpr>)
              177474256   74.796    0.000  105.153    0.000 layer.py:130(add)
                2743823   58.067    0.000  104.732    0.000 level.py:16(<dictcomp>)
               13167362   65.785    0.000  104.685    0.000 {built-in method _functools.reduce}
             1029750624  101.544    0.000  101.544    0.000 layer.py:91(positions)
                 824422   70.309    0.000  100.387    0.000 allGraphsTrain.py:43(<listcomp>)
               13190752   99.948    0.000   99.948    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                 824422   98.401    0.000   98.401    0.000 {built-in method torch._C._nn.one_hot}
              377585544   80.553    0.000   95.813    0.000 overrides.py:1083(<genexpr>)
                4946532    5.849    0.000   89.773    0.000 activation.py:713(forward)
                4946532    9.139    0.000   83.924    0.000 functional.py:1292(leaky_relu)
                 824422   20.794    0.000   81.813    0.000 allGraphs.py:111(transform)
                4946532   73.985    0.000   73.985    0.000 {built-in method torch._C._nn.leaky_relu}
              325623345   67.179    0.000   71.841    0.000 {built-in method builtins.max}
                2473266   71.340    0.000   71.340    0.000 {method 'tolist' of 'torch._C._TensorBase' objects}
               84010795   47.695    0.000   71.001    0.000 layer.py:126(remove)
               36975091   47.088    0.000   69.673    0.000 layers.py:107(isDone)
                6595376   67.835    0.000   67.835    0.000 {method 'add' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-11>
Subject: Job 9511424: <causal7_online_var_0.5_0> in cluster <dcc> Done

Job <causal7_online_var_0.5_0> was submitted from host <n-62-27-18> by user <s183905> in cluster <dcc> at Mon Apr 12 17:14:12 2021
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Mon Apr 12 17:14:15 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Apr 12 17:14:15 2021
Terminated at Tue Apr 13 05:09:28 2021
Results reported at Tue Apr 13 05:09:28 2021

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

    CPU time :                                   42803.52 sec.
    Max Memory :                                 2083 MB
    Average Memory :                             2082.27 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14301.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   42915 sec.
    Turnaround time :                            42916 sec.

The output (if any) is above this job summary.

