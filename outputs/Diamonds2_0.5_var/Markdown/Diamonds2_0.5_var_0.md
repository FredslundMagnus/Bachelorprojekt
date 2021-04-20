
# Parameters

    Name :                      Diamonds2_0.5_var-0
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


      38118346497 function calls (33686211550 primitive calls) in 35703.72 seconds

##    Ordered by: cumulative time
   List reduced from 467 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35703.722 35703.722 {built-in method builtins.exec}
                      1    0.001    0.001 35703.722 35703.722 <string>:1(<module>)
                      1   91.795   91.795 35703.722 35703.722 allGraphsTrain.py:10(graphTrain)
                 347159 5421.912    0.016 12104.637    0.035 allGraphs.py:146(transformNot)
                 347159  427.482    0.001 9939.371    0.029 allGraphsTrain.py:35(<listcomp>)
                6830104   13.974    0.000 9511.890    0.001 allGraphs.py:158(getInterventions)
                5842221    6.008    0.000 8656.130    0.001 allGraphs.py:129(rightIntervention)
        760880962/5842221  462.827    0.000 8620.564    0.001 {built-in method builtins.min}
               21538918   10.684    0.000 8606.835    0.000 allGraphs.py:130(<lambda>)
        1515919703/21538918 2521.437    0.000 8596.151    0.000 allGraphs.py:74(expected_moves)
        2249419526/73647668  729.214    0.000 8435.807    0.000 allGraphs.py:78(<genexpr>)
                 347159    9.885    0.000 7810.078    0.022 allGraphsTrain.py:29(<listcomp>)
               35063160 2036.657    0.000 7800.226    0.000 allGraphs.py:110(states)
              486025976 6650.907    0.000 6650.907    0.000 {method 'item' of 'torch._C._TensorBase' objects}
              451307300 6170.211    0.000 6170.211    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
              761868845  451.879    0.000 2691.847    0.000 allGraphs.py:83(layers_not_in)
            11325551615 1746.442    0.000 2551.602    0.000 enum.py:646(__hash__)
              761868845 1066.384    0.000 2239.968    0.000 allGraphs.py:84(<listcomp>)
                 347159    1.310    0.000 1678.438    0.005 game.py:41(step)
                 347159    1.735    0.000 1593.555    0.005 layers.py:718(step)
                 347159   97.300    0.000 1286.795    0.004 allGraphsTrain.py:37(<listcomp>)
             1515919703  772.928    0.000 1129.652    0.000 allGraphs.py:45(p)
               10056675 1050.522    0.000 1050.522    0.000 {built-in method tensor}
                8565900    5.558    0.000  989.068    0.000 game.py:37(board)
                 347159    1.325    0.000  983.681    0.003 agent.py:29(learn)
                 347159    7.454    0.000  981.613    0.003 agent.py:117(_learn)
                 347159   28.352    0.000  974.160    0.003 learner.py:42(Qlearn)
                 347160   48.955    0.000  854.371    0.002 layers.py:684(update)
                6830104   37.160    0.000  825.608    0.000 allGraphs.py:153(format)
            11325552796  805.160    0.000  805.160    0.000 {built-in method builtins.hash}
               36798854   99.322    0.000  804.109    0.000 tensor.py:21(wrapped)
                 347159   37.411    0.000  773.945    0.002 allGraphsTrain.py:44(<listcomp>)
                 347159   27.069    0.000  735.542    0.002 layers.py:17(step)
               34715900   56.822    0.000  704.752    0.000 layer.py:98(move)
               36451695  598.397    0.000  598.397    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               34715900  539.016    0.000  539.016    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                 347159    2.168    0.000  414.755    0.001 grad_mode.py:23(decorate_context)
                 347159   11.099    0.000  408.594    0.001 adam.py:55(step)
                 347159  220.810    0.001  399.655    0.001 agent.py:67(modify)
                 794022    7.356    0.000  382.842    0.000 layers.py:740(restart)
               34715900   94.808    0.000  381.560    0.000 layers.py:735(check)
                 347159   74.322    0.000  352.069    0.001 functional.py:53(adam)
        7984657/1041477   32.720    0.000  350.260    0.000 module.py:715(_call_impl)
                 694318    1.941    0.000  321.203    0.000 network.py:27(forward)
                 794022    3.570    0.000  318.899    0.000 level.py:8(__init__)
                 694318    8.399    0.000  314.997    0.000 container.py:115(forward)
                 794022   11.943    0.000  288.732    0.000 levels.py:249(generate)
             1517949063  272.479    0.000  278.531    0.000 {built-in method builtins.max}
                5160106   46.978    0.000  264.372    0.000 level.py:41(notUsed)
                 347159    2.267    0.000  223.552    0.001 tensor.py:181(backward)
                 347159    1.186    0.000  221.285    0.001 __init__.py:68(backward)
               34715900   58.395    0.000  215.825    0.000 layers.py:729(isFree)
                 347159  210.886    0.001  210.886    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               96410733   57.737    0.000  204.986    0.000 {built-in method builtins.any}
                 347159    4.597    0.000  186.579    0.001 agent.py:112(__call__)
               36104536  181.320    0.000  181.320    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                3124440  100.005    0.000  178.872    0.000 layer.py:167(NoRock_update)
              293122926  120.931    0.000  157.430    0.000 layer.py:95(isFree)
                1388636    2.472    0.000  124.011    0.000 conv.py:422(forward)
                1041477    4.365    0.000  122.990    0.000 tensor.py:576(__iter__)
                5160106    3.791    0.000  122.373    0.000 level.py:38(elementsIn)
                1388636    2.871    0.000  120.607    0.000 conv.py:414(_conv_forward)
                1388636  117.244    0.000  117.244    0.000 {built-in method conv2d}
                1041477  115.668    0.000  115.668    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               71514854   28.019    0.000  115.613    0.000 {built-in method builtins.all}
              339219780   88.258    0.000  107.935    0.000 layers.py:700(<genexpr>)
               60405800   31.948    0.000  102.276    0.000 overrides.py:1070(has_torch_function)
                1388636    3.408    0.000   93.676    0.000 linear.py:92(forward)
                1388636    5.926    0.000   88.807    0.000 functional.py:1669(linear)
               19440958   53.993    0.000   84.808    0.000 tensor.py:933(grad)
                 347159    8.159    0.000   82.793    0.000 optimizer.py:167(zero_grad)
                5160106   39.225    0.000   79.182    0.000 level.py:39(<listcomp>)
              152818609   40.243    0.000   78.664    0.000 layers.py:690(<genexpr>)
                5554544   72.862    0.000   72.862    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                 347159   42.192    0.000   71.002    0.000 collector.py:46(collect)
                1388636   63.980    0.000   63.980    0.000 {built-in method addmm}
                5554544   61.868    0.000   61.868    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                 347159    2.884    0.000   60.737    0.000 agent.py:59(modify_board)
              243371040   57.271    0.000   57.271    0.000 level.py:32(inverse)
                7146198    5.340    0.000   54.247    0.000 layer.py:69(restart)
               17355583   31.420    0.000   51.160    0.000 layers.py:349(check)
              520657910   50.797    0.000   50.797    0.000 layer.py:91(positions)
               17359076   30.281    0.000   49.673    0.000 layers.py:337(check)
               17358478   29.711    0.000   48.573    0.000 layers.py:387(check)
               17360727   28.786    0.000   47.316    0.000 layers.py:375(check)
              129744662   45.069    0.000   45.069    0.000 layer.py:146(elements)
                2082954    1.915    0.000   44.632    0.000 activation.py:713(forward)
                2082954    3.005    0.000   42.716    0.000 functional.py:1292(leaky_relu)
                2777272   42.248    0.000   42.248    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                 794122   20.368    0.000   40.796    0.000 layers.py:36(reset)
                2082954   39.422    0.000   39.422    0.000 {built-in method torch._C._nn.leaky_relu}
                5160106   24.584    0.000   39.400    0.000 {built-in method _functools.reduce}
              214350173   39.257    0.000   39.257    0.000 enum.py:352(<genexpr>)
              158999090   32.747    0.000   39.082    0.000 overrides.py:1083(<genexpr>)
                 347159   38.166    0.000   38.166    0.000 {built-in method torch._C._nn.one_hot}
                 347159   25.353    0.000   37.529    0.000 allGraphsTrain.py:43(<listcomp>)
                2777272   36.467    0.000   36.467    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                2777272   33.610    0.000   33.610    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               62067881   23.982    0.000   32.699    0.000 layer.py:130(add)
                 347159    8.245    0.000   31.152    0.000 allGraphs.py:137(transform)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9532012: <Diamonds2_0.5_var_0> in cluster <dcc> Done

Job <Diamonds2_0.5_var_0> was submitted from host <n-62-30-7> by user <s183905> in cluster <dcc> at Sat Apr 17 13:28:41 2021
Job was executed on host(s) <n-62-11-13>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sun Apr 18 09:49:17 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun Apr 18 09:49:17 2021
Terminated at Sun Apr 18 19:44:23 2021
Results reported at Sun Apr 18 19:44:23 2021

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

    CPU time :                                   35636.93 sec.
    Max Memory :                                 2067 MB
    Average Memory :                             2059.70 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14317.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35706 sec.
    Turnaround time :                            108942 sec.

The output (if any) is above this job summary.

