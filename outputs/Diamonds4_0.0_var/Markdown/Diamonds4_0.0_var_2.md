
# Parameters

    Name :                      Diamonds4_0.0_var-2
    Main :                      graphTrain
    Level :                     Levels.Causal7
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
    Counterfacts :              1
    Topn :                      6
    Random counterfacts :       False
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      15334699610 function calls (15010330835 primitive calls) in 35712.80 seconds

##    Ordered by: cumulative time
   List reduced from 466 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35712.797 35712.797 {built-in method builtins.exec}
                      1    0.001    0.001 35712.797 35712.797 <string>:1(<module>)
                      1  149.308  149.308 35712.796 35712.796 allGraphsTrain.py:10(graphTrain)
                 580375 6521.543    0.011 14562.558    0.025 allGraphs.py:146(transformNot)
                 580375   17.159    0.000 8872.886    0.015 allGraphsTrain.py:29(<listcomp>)
               58617976 2345.129    0.000 8855.801    0.000 allGraphs.py:110(states)
              580380040 8084.032    0.000 8084.032    0.000 {method 'item' of 'torch._C._TensorBase' objects}
              522337900 7143.714    0.000 7143.714    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 580375    2.195    0.000 3088.616    0.005 game.py:41(step)
                 580375    2.835    0.000 2957.407    0.005 layers.py:718(step)
                 580375  673.435    0.001 2244.226    0.004 allGraphsTrain.py:35(<listcomp>)
                 580375  164.619    0.000 2177.939    0.004 allGraphsTrain.py:37(<listcomp>)
                 580375    1.968    0.000 1622.131    0.003 agent.py:29(learn)
                 580375   12.461    0.000 1618.904    0.003 agent.py:117(_learn)
                 580375   46.721    0.000 1606.443    0.003 learner.py:42(Qlearn)
                8502232   16.461    0.000 1570.791    0.000 allGraphs.py:158(getInterventions)
                 580376   82.930    0.000 1547.588    0.003 layers.py:684(update)
                 580375   44.677    0.000 1403.749    0.002 layers.py:17(step)
               58037500   96.085    0.000 1353.991    0.000 layer.py:98(move)
               61519750  163.747    0.000 1343.187    0.000 tensor.py:21(wrapped)
                 580375   59.277    0.000 1290.377    0.002 allGraphsTrain.py:44(<listcomp>)
               13874357 1174.399    0.000 1174.399    0.000 {built-in method tensor}
               11404108    7.242    0.000 1084.818    0.000 game.py:37(board)
               60939375 1002.123    0.000 1002.123    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               58037500  908.865    0.000  908.865    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                2235550   17.832    0.000  849.893    0.000 layers.py:740(restart)
                8502232   41.774    0.000  837.923    0.000 allGraphs.py:153(format)
               58037500  178.023    0.000  836.878    0.000 layers.py:735(check)
                7835097    7.848    0.000  706.409    0.000 allGraphs.py:129(rightIntervention)
                 580375  403.078    0.001  700.235    0.001 agent.py:67(modify)
                 580375    3.461    0.000  686.279    0.001 grad_mode.py:23(decorate_context)
                2235550    8.593    0.000  679.660    0.000 level.py:8(__init__)
                 580375   18.492    0.000  676.059    0.001 adam.py:55(step)
        71049919/7835097   52.744    0.000  667.630    0.000 {built-in method builtins.min}
               19906271    9.372    0.000  653.148    0.000 allGraphs.py:130(<lambda>)
        134264741/19906271  201.799    0.000  643.776    0.000 allGraphs.py:74(expected_moves)
                2235550   25.427    0.000  593.661    0.000 levels.py:441(generate)
                 580375  123.516    0.000  582.131    0.001 functional.py:53(adam)
        13348625/1741125   55.284    0.000  580.193    0.000 module.py:715(_call_impl)
               10732141   99.158    0.000  542.145    0.000 level.py:41(notUsed)
                1160750    3.077    0.000  531.961    0.000 network.py:27(forward)
        177573292/42385692   56.399    0.000  528.759    0.000 allGraphs.py:78(<genexpr>)
                1160750   13.561    0.000  521.773    0.000 container.py:115(forward)
             2079259059  355.789    0.000  513.459    0.000 enum.py:646(__hash__)
                 580375    3.307    0.000  361.865    0.001 tensor.py:181(backward)
                 580375    1.989    0.000  358.558    0.001 __init__.py:68(backward)
                 580375  341.364    0.001  341.364    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               58037500   88.135    0.000  332.341    0.000 layers.py:729(isFree)
                 580375    7.649    0.000  306.624    0.001 agent.py:112(__call__)
               60359000  304.624    0.000  304.624    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              160269685   86.855    0.000  293.380    0.000 {built-in method builtins.any}
                4062632  158.347    0.000  271.143    0.000 layer.py:167(NoRock_update)
               10732141    8.319    0.000  254.736    0.000 level.py:38(elementsIn)
              401373256  189.314    0.000  244.206    0.000 layer.py:95(isFree)
               71717054   44.712    0.000  209.375    0.000 allGraphs.py:83(layers_not_in)
                2321500    3.998    0.000  204.691    0.000 conv.py:422(forward)
                1741125    7.373    0.000  204.130    0.000 tensor.py:576(__iter__)
                2321500    4.573    0.000  199.129    0.000 conv.py:414(_conv_forward)
                2321500  193.751    0.000  193.751    0.000 {built-in method conv2d}
                1741125  191.880    0.000  191.880    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
              119557350   41.983    0.000  179.675    0.000 {built-in method builtins.all}
              100985384   52.330    0.000  170.114    0.000 overrides.py:1070(has_torch_function)
               10732141   81.587    0.000  165.013    0.000 level.py:39(<listcomp>)
               71717054   82.362    0.000  164.664    0.000 allGraphs.py:84(<listcomp>)
               58037500  100.913    0.000  164.289    0.000 layers.py:602(check)
               58037500   99.283    0.000  162.636    0.000 layers.py:632(check)
             2079261008  157.670    0.000  157.670    0.000 {built-in method builtins.hash}
                2321500    5.763    0.000  154.776    0.000 linear.py:92(forward)
               58037500   94.780    0.000  154.760    0.000 layers.py:617(check)
               15648850   12.380    0.000  146.919    0.000 layer.py:69(restart)
                2321500    9.631    0.000  146.581    0.000 functional.py:1669(linear)
               32501054   89.160    0.000  140.511    0.000 tensor.py:933(grad)
              446416400  113.160    0.000  140.118    0.000 layers.py:700(<genexpr>)
                 580375   13.788    0.000  137.992    0.000 optimizer.py:167(zero_grad)
              185128889   47.474    0.000  122.599    0.000 layers.py:690(<genexpr>)
                9286000  121.640    0.000  121.640    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                 580375   70.100    0.000  117.887    0.000 collector.py:46(collect)
                2235650   57.980    0.000  115.979    0.000 layers.py:36(reset)
              515273222  111.960    0.000  111.960    0.000 level.py:32(inverse)
             1148379486  109.426    0.000  109.426    0.000 layer.py:91(positions)
                2321500  105.747    0.000  105.747    0.000 {built-in method addmm}
                9286000  103.582    0.000  103.582    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                 580375    4.564    0.000  101.127    0.000 agent.py:59(modify_board)
              134264741   67.953    0.000   99.033    0.000 allGraphs.py:45(p)
              466838369   82.681    0.000   82.681    0.000 enum.py:352(<genexpr>)
               10732141   50.671    0.000   81.405    0.000 {built-in method _functools.reduce}
                3482250    3.297    0.000   74.121    0.000 activation.py:713(forward)
               58037500   46.410    0.000   73.555    0.000 layers.py:588(check)
              137865819   53.966    0.000   73.545    0.000 layer.py:130(add)
                2235550   37.009    0.000   72.034    0.000 level.py:16(<dictcomp>)
                3482250    5.008    0.000   70.824    0.000 functional.py:1292(leaky_relu)
              281636263   68.871    0.000   68.871    0.000 layer.py:146(elements)
                4643000   66.539    0.000   66.539    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              265812018   55.593    0.000   66.036    0.000 overrides.py:1083(<genexpr>)
                3482250   65.336    0.000   65.336    0.000 {built-in method torch._C._nn.leaky_relu}
                 580375   63.962    0.000   63.962    0.000 {built-in method torch._C._nn.one_hot}
                 580375   42.449    0.000   62.909    0.000 allGraphsTrain.py:43(<listcomp>)
               58037500   41.676    0.000   61.156    0.000 layers.py:23(check)
                4643000   60.117    0.000   60.117    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                4643000   55.234    0.000   55.234    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9532045: <Diamonds4_0.0_var_2> in cluster <dcc> Done

Job <Diamonds4_0.0_var_2> was submitted from host <n-62-30-7> by user <s183905> in cluster <dcc> at Sat Apr 17 13:28:46 2021
Job was executed on host(s) <n-62-11-16>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Wed Apr 21 03:14:13 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed Apr 21 03:14:13 2021
Terminated at Wed Apr 21 13:09:36 2021
Results reported at Wed Apr 21 13:09:36 2021

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

    CPU time :                                   35617.85 sec.
    Max Memory :                                 2061 MB
    Average Memory :                             2053.82 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14323.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35723 sec.
    Turnaround time :                            344450 sec.

The output (if any) is above this job summary.

