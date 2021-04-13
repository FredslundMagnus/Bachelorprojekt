
# Parameters

    Name :                      causal6_online_var_0.5_full-0
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
    Cf convert :                3
    Counterfacts :              2
    Topn :                      5
    Minutes used :              715 minutes.
    Hours used :                11 hours.

# Profiling


      39749533448 function calls (35760846035 primitive calls) in 42908.80 seconds

##    Ordered by: cumulative time
   List reduced from 465 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 42908.801 42908.801 {built-in method builtins.exec}
                      1    0.001    0.001 42908.801 42908.801 <string>:1(<module>)
                      1  184.663  184.663 42908.799 42908.799 allGraphsTrain.py:10(graphTrain)
                 612249 5684.881    0.009 14224.936    0.023 allGraphs.py:120(transformNot)
              734704196 10070.706    0.000 10070.706    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                 612249  701.116    0.001 9685.737    0.016 allGraphsTrain.py:35(<listcomp>)
                 612249   16.290    0.000 9298.063    0.015 allGraphsTrain.py:29(<listcomp>)
               61837250 2020.921    0.000 9281.788    0.000 allGraphs.py:88(states)
               13751585   74.971    0.000 8984.621    0.001 allGraphs.py:127(getInterventions)
               12770326   11.278    0.000 7388.051    0.001 allGraphs.py:107(rightIntervention)
        714702237/12770326  407.429    0.000 7318.527    0.001 {built-in method builtins.min}
               49259425   21.789    0.000 7293.622    0.000 allGraphs.py:108(<lambda>)
        1416634148/49259425 2161.342    0.000 7271.834    0.000 allGraphs.py:52(expected_moves)
        2069306634/162171218  596.921    0.000 6941.494    0.000 allGraphs.py:56(<genexpr>)
              673474400 6417.427    0.000 6417.427    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 612249    2.904    0.000 3450.781    0.006 game.py:41(step)
                 612249    3.889    0.000 3308.883    0.005 layers.py:718(step)
             9941553437 1595.796    0.000 2292.945    0.000 enum.py:646(__hash__)
              715683496  408.828    0.000 2256.969    0.000 allGraphs.py:61(layers_not_in)
                 612250   97.356    0.000 1972.415    0.003 layers.py:684(update)
               19417362 1936.365    0.000 1936.365    0.000 {built-in method tensor}
              715683496  893.032    0.000 1848.140    0.000 allGraphs.py:62(<listcomp>)
               16812831    9.569    0.000 1845.705    0.000 game.py:37(board)
                 612249  117.428    0.000 1844.824    0.003 allGraphsTrain.py:37(<listcomp>)
                 612249    3.006    0.000 1444.720    0.002 agent.py:29(learn)
                 612249   14.502    0.000 1440.243    0.002 agent.py:117(_learn)
                 612249   43.935    0.000 1425.741    0.002 learner.py:42(Qlearn)
                 612249   52.616    0.000 1327.993    0.002 layers.py:17(step)
               61224900  102.630    0.000 1269.788    0.000 layer.py:98(move)
               64898394  156.350    0.000 1078.844    0.000 tensor.py:21(wrapped)
                2316225   20.976    0.000 1072.985    0.000 layers.py:740(restart)
             1416634148  715.613    0.000 1052.634    0.000 allGraphs.py:37(p)
                 612249   47.754    0.000 1018.375    0.002 allGraphsTrain.py:44(<listcomp>)
                2316225   10.475    0.000  882.083    0.000 level.py:8(__init__)
                2316225   31.986    0.000  783.183    0.000 levels.py:293(generate)
               64286145  733.981    0.000  733.981    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               13898054  128.071    0.000  716.708    0.000 level.py:41(notUsed)
             9941555482  697.149    0.000  697.149    0.000 {built-in method builtins.hash}
               61224900  675.101    0.000  675.101    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                 612249  356.630    0.001  658.409    0.001 agent.py:67(modify)
               61224900  152.196    0.000  635.625    0.000 layers.py:735(check)
        14081727/1836747   63.953    0.000  590.424    0.000 module.py:715(_call_impl)
                 612249    4.706    0.000  547.128    0.001 grad_mode.py:23(decorate_context)
                1224498    3.530    0.000  534.341    0.000 network.py:24(forward)
                 612249   20.987    0.000  533.336    0.001 adam.py:55(step)
                1224498   15.534    0.000  521.377    0.000 container.py:115(forward)
                 612249   97.638    0.000  436.243    0.001 functional.py:53(adam)
               61224900   96.048    0.000  428.741    0.000 layers.py:729(isFree)
                 612249    3.937    0.000  350.478    0.001 tensor.py:181(backward)
                 612249    2.973    0.000  346.541    0.001 __init__.py:68(backward)
              169113730   97.875    0.000  345.723    0.000 {built-in method builtins.any}
                4898000  199.853    0.000  344.976    0.000 layer.py:167(NoRock_update)
               13898054   10.131    0.000  333.667    0.000 level.py:38(elementsIn)
              469633924  273.757    0.000  332.694    0.000 layer.py:95(isFree)
                 612249   11.009    0.000  331.802    0.001 agent.py:112(__call__)
                 612249  327.695    0.001  327.695    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
             1419452154  248.226    0.000  254.256    0.000 {built-in method builtins.max}
              126123394   43.736    0.000  248.942    0.000 {built-in method builtins.all}
                1836747    8.469    0.000  233.962    0.000 tensor.py:576(__iter__)
                1836747  220.028    0.000  220.028    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               63673896  216.270    0.000  216.270    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               13898054  105.124    0.000  213.470    0.000 level.py:39(<listcomp>)
                2448996    4.870    0.000  210.315    0.000 conv.py:422(forward)
                2448996    6.222    0.000  203.307    0.000 conv.py:414(_conv_forward)
                2448996  196.126    0.000  196.126    0.000 {built-in method conv2d}
              211175892   57.794    0.000  187.987    0.000 layers.py:690(<genexpr>)
              106531460   54.701    0.000  179.269    0.000 overrides.py:1070(has_torch_function)
              530178975  143.208    0.000  175.853    0.000 layers.py:700(<genexpr>)
               18529800   15.467    0.000  163.448    0.000 layer.py:69(restart)
              659228170  155.556    0.000  155.556    0.000 level.py:32(inverse)
                2448996    6.538    0.000  153.837    0.000 linear.py:92(forward)
                2448996   11.356    0.000  144.128    0.000 functional.py:1669(linear)
               30610308   85.368    0.000  138.748    0.000 layers.py:424(check)
               34285998   82.310    0.000  135.848    0.000 tensor.py:933(grad)
                2316325   60.582    0.000  121.367    0.000 layers.py:36(reset)
                 612249   11.962    0.000  118.500    0.000 optimizer.py:167(zero_grad)
                 612249    5.994    0.000  110.875    0.000 agent.py:59(modify_board)
               61225000   72.991    0.000  110.532    0.000 layers.py:113(isDone)
               13898054   68.404    0.000  110.066    0.000 {built-in method _functools.reduce}
              583715570  105.321    0.000  105.321    0.000 enum.py:352(<genexpr>)
                2448996  103.534    0.000  103.534    0.000 {built-in method addmm}
                 612249   56.403    0.000   95.908    0.000 collector.py:46(collect)
               30611696   58.012    0.000   91.881    0.000 layers.py:452(check)
               30613814   56.674    0.000   91.000    0.000 layers.py:437(check)
              924778005   90.563    0.000   90.563    0.000 layer.py:91(positions)
              296352212   89.950    0.000   89.950    0.000 layer.py:146(elements)
                9795984   87.126    0.000   87.126    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              144204035   59.418    0.000   82.341    0.000 layer.py:130(add)
                2316225   45.332    0.000   82.190    0.000 level.py:16(<dictcomp>)
                 612249   73.394    0.000   73.394    0.000 {built-in method torch._C._nn.one_hot}
                9795984   72.107    0.000   72.107    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              280410310   60.383    0.000   71.524    0.000 overrides.py:1083(<genexpr>)
                 612249   47.953    0.000   70.119    0.000 allGraphsTrain.py:43(<listcomp>)
                3673494    4.104    0.000   66.454    0.000 activation.py:713(forward)
                3673494    6.584    0.000   62.350    0.000 functional.py:1292(leaky_relu)
                 612249   15.412    0.000   58.298    0.000 allGraphs.py:111(transform)
                3673494   55.219    0.000   55.219    0.000 {built-in method torch._C._nn.leaky_relu}
                1836747   51.203    0.000   51.203    0.000 {method 'tolist' of 'torch._C._TensorBase' objects}
               61005878   33.360    0.000   49.582    0.000 layer.py:126(remove)
                4897992   49.486    0.000   49.486    0.000 {method 'add' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-12>
Subject: Job 9511705: <causal6_online_var_0.5_full_0> in cluster <dcc> Done

Job <causal6_online_var_0.5_full_0> was submitted from host <n-62-27-18> by user <s183905> in cluster <dcc> at Mon Apr 12 21:45:53 2021
Job was executed on host(s) <n-62-20-12>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Tue Apr 13 07:29:44 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue Apr 13 07:29:44 2021
Terminated at Tue Apr 13 19:25:01 2021
Results reported at Tue Apr 13 19:25:01 2021

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

    CPU time :                                   42804.23 sec.
    Max Memory :                                 2092 MB
    Average Memory :                             2087.63 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14292.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   42917 sec.
    Turnaround time :                            77948 sec.

The output (if any) is above this job summary.

