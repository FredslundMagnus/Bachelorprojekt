
# Parameters

    Name :                      causal5_online_var_0.5_full_UCB1-0
    Main :                      graphTrain
    Level :                     Levels.Causal5
    Failed actions chance :     0.5
    Hours :                     12.0
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
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                3
    Counterfacts :              2
    Topn :                      5
    Random counterfacts :       False
    Minutes used :              715 minutes.
    Hours used :                11 hours.

# Profiling


      63103211836 function calls (56044783913 primitive calls) in 42911.77 seconds

##    Ordered by: cumulative time
   List reduced from 465 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 42911.768 42911.768 {built-in method builtins.exec}
                      1    0.001    0.001 42911.768 42911.768 <string>:1(<module>)
                      1  141.339  141.339 42911.767 42911.767 allGraphsTrain.py:10(graphTrain)
                 431177  485.966    0.001 17182.945    0.040 allGraphsTrain.py:35(<listcomp>)
                9117075   13.850    0.000 16696.979    0.002 allGraphs.py:158(getInterventions)
                9117075    9.017    0.000 15564.638    0.002 allGraphs.py:133(UCB1)
        1211850604/9117075  701.986    0.000 15510.262    0.002 {built-in method builtins.min}
               33983088   15.747    0.000 15490.532    0.000 allGraphs.py:134(<lambda>)
        2414584133/33983088 4068.968    0.000 15474.785    0.000 allGraphs.py:68(expected_moves_UCB1)
        3583334574/116865148 1067.581    0.000 15189.023    0.000 allGraphs.py:72(<genexpr>)
                 431177 4509.390    0.010 11281.451    0.026 allGraphs.py:146(transformNot)
              603651848 7941.040    0.000 7941.040    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                 431177   11.780    0.000 7631.751    0.018 allGraphsTrain.py:29(<listcomp>)
               43548978 1664.454    0.000 7619.989    0.000 allGraphs.py:110(states)
              560530700 5227.263    0.000 5227.263    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
             1211850604  683.731    0.000 4414.232    0.000 allGraphs.py:83(layers_not_in)
            17811235852 2840.771    0.000 4105.919    0.000 enum.py:646(__hash__)
             1211850604 1807.283    0.000 3730.501    0.000 allGraphs.py:84(<listcomp>)
             2414584133 2174.042    0.000 3442.167    0.000 allGraphs.py:60(UCB1)
                 431177    2.005    0.000 2391.262    0.006 game.py:41(step)
                 431177    2.901    0.000 2288.621    0.005 layers.py:718(step)
               13116800 1400.493    0.000 1400.493    0.000 {built-in method tensor}
               11272961    6.839    0.000 1322.988    0.000 game.py:37(board)
            17811237321 1265.148    0.000 1265.148    0.000 {built-in method builtins.hash}
                 431177   79.757    0.000 1262.279    0.003 allGraphsTrain.py:37(<listcomp>)
                 431178   67.752    0.000 1218.794    0.003 layers.py:684(update)
                9117075   48.311    0.000 1118.491    0.000 allGraphs.py:153(format)
                 431177   41.292    0.000 1063.307    0.002 layers.py:17(step)
                 431177    2.043    0.000 1026.127    0.002 agent.py:29(learn)
                 431177   10.547    0.000 1022.979    0.002 agent.py:117(_learn)
               43117700   74.747    0.000 1017.767    0.000 layer.py:98(move)
                 431177   31.718    0.000 1012.432    0.002 learner.py:42(Qlearn)
               45704762  109.074    0.000  753.084    0.000 tensor.py:21(wrapped)
                 431177   34.166    0.000  709.289    0.002 allGraphsTrain.py:44(<listcomp>)
                1054827   11.079    0.000  533.471    0.001 layers.py:740(restart)
               43117700  123.940    0.000  511.021    0.000 layers.py:735(check)
               45273585  509.562    0.000  509.562    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               43117700  469.765    0.000  469.765    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
             2415877664  468.645    0.000  468.645    0.000 {built-in method builtins.max}
                 431177  235.717    0.001  453.166    0.001 agent.py:67(modify)
             2414255690  440.450    0.000  440.450    0.000 {built-in method math.log}
                1054827    5.389    0.000  439.458    0.000 level.py:8(__init__)
        9917071/1293531   48.238    0.000  433.886    0.000 module.py:715(_call_impl)
                1054827   16.784    0.000  395.261    0.000 levels.py:249(generate)
                 862354    2.701    0.000  392.397    0.000 network.py:24(forward)
                 862354   10.440    0.000  382.786    0.000 container.py:115(forward)
                 431177    3.560    0.000  380.429    0.001 grad_mode.py:23(decorate_context)
                 431177   14.691    0.000  369.977    0.001 adam.py:55(step)
                6856895   64.544    0.000  360.927    0.000 level.py:41(notUsed)
               43117700   83.305    0.000  358.956    0.000 layers.py:729(isFree)
                 431177   67.059    0.000  300.975    0.001 functional.py:53(adam)
              380114242  229.420    0.000  275.651    0.000 layer.py:95(isFree)
              119674968   73.867    0.000  265.817    0.000 {built-in method builtins.any}
             2417705241  258.561    0.000  258.561    0.000 {built-in method math.sqrt}
                3880602  143.948    0.000  256.220    0.000 layer.py:167(NoRock_update)
                 431177    2.889    0.000  253.575    0.001 tensor.py:181(backward)
                 431177    2.228    0.000  250.686    0.001 __init__.py:68(backward)
                 431177    8.310    0.000  248.381    0.001 agent.py:112(__call__)
                 431177  236.674    0.001  236.674    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               88822562   39.891    0.000  193.636    0.000 {built-in method builtins.all}
                1293531    6.411    0.000  172.862    0.000 tensor.py:576(__iter__)
                6856895    5.027    0.000  165.895    0.000 level.py:38(elementsIn)
                1293531  162.367    0.000  162.367    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
                1724708    3.568    0.000  156.626    0.000 conv.py:422(forward)
                1724708    4.663    0.000  151.479    0.000 conv.py:414(_conv_forward)
               44842408  148.901    0.000  148.901    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                1724708  146.120    0.000  146.120    0.000 {built-in method conv2d}
              260455144   73.078    0.000  141.284    0.000 layers.py:690(<genexpr>)
              420629730  115.235    0.000  140.855    0.000 layers.py:700(<genexpr>)
               75024932   38.996    0.000  127.419    0.000 overrides.py:1070(has_torch_function)
                1724708    4.594    0.000  111.924    0.000 linear.py:92(forward)
                6856895   53.239    0.000  107.232    0.000 level.py:39(<listcomp>)
                1724708    8.098    0.000  104.987    0.000 functional.py:1669(linear)
               24145966   57.896    0.000   95.663    0.000 tensor.py:933(grad)
                 431177    8.056    0.000   81.689    0.000 optimizer.py:167(zero_grad)
                 431177    4.217    0.000   80.270    0.000 agent.py:59(modify_board)
                9493443    8.924    0.000   79.774    0.000 layer.py:69(restart)
              323392817   79.770    0.000   79.770    0.000 level.py:32(inverse)
                1724708   75.530    0.000   75.530    0.000 {built-in method addmm}
              166443753   68.066    0.000   68.066    0.000 layer.py:146(elements)
               21557675   43.018    0.000   67.751    0.000 layers.py:337(check)
                 431177   38.721    0.000   66.747    0.000 collector.py:46(collect)
               21556988   42.244    0.000   66.276    0.000 layers.py:387(check)
               21563532   41.491    0.000   66.075    0.000 layers.py:375(check)
              658440227   65.725    0.000   65.725    0.000 layer.py:91(positions)
               21560655   41.181    0.000   65.679    0.000 layers.py:349(check)
                6898832   60.151    0.000   60.151    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                1054927   28.070    0.000   56.058    0.000 layers.py:36(reset)
              284823557   53.678    0.000   53.678    0.000 enum.py:352(<genexpr>)
                6856895   33.478    0.000   53.635    0.000 {built-in method _functools.reduce}
                 431177   53.263    0.000   53.263    0.000 {built-in method torch._C._nn.one_hot}
                 431177   35.656    0.000   51.411    0.000 allGraphsTrain.py:43(<listcomp>)
              197479334   42.942    0.000   50.744    0.000 overrides.py:1083(<genexpr>)
                6898832   49.561    0.000   49.561    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                2587062    3.443    0.000   48.556    0.000 activation.py:713(forward)
               79759730   34.062    0.000   47.100    0.000 layer.py:130(add)
                2587062    5.160    0.000   45.113    0.000 functional.py:1292(leaky_relu)
                 431177   12.479    0.000   43.470    0.000 allGraphs.py:137(transform)
                2587062   39.496    0.000   39.496    0.000 {built-in method torch._C._nn.leaky_relu}
              380114242   38.549    0.000   38.549    0.000 layer.py:203(isBlocking)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-11>
Subject: Job 9512222: <causal5_online_var_0.5_full_UCB1_0> in cluster <dcc> Done

Job <causal5_online_var_0.5_full_UCB1_0> was submitted from host <n-62-30-2> by user <s183905> in cluster <dcc> at Tue Apr 13 11:09:10 2021
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Tue Apr 13 21:35:13 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue Apr 13 21:35:13 2021
Terminated at Wed Apr 14 09:30:35 2021
Results reported at Wed Apr 14 09:30:35 2021

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

    CPU time :                                   42800.94 sec.
    Max Memory :                                 2091 MB
    Average Memory :                             2086.44 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14293.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   42923 sec.
    Turnaround time :                            80485 sec.

The output (if any) is above this job summary.

