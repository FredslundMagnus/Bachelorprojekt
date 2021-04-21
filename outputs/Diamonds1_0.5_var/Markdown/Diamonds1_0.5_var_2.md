
# Parameters

    Name :                      Diamonds1_0.5_var-2
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


      19601510778 function calls (18824125467 primitive calls) in 35702.96 seconds

##    Ordered by: cumulative time
   List reduced from 463 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35702.961 35702.961 {built-in method builtins.exec}
                      1    0.001    0.001 35702.961 35702.961 <string>:1(<module>)
                      1  183.394  183.394 35702.960 35702.960 allGraphsTrain.py:10(graphTrain)
                 687034 5223.739    0.008 13139.435    0.019 allGraphs.py:146(transformNot)
              687039896 9306.639    0.000 9306.639    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                 687034   16.857    0.000 8288.281    0.012 allGraphsTrain.py:29(<listcomp>)
               69390535 1807.388    0.000 8271.437    0.000 allGraphs.py:110(states)
              618331000 5852.288    0.000 5852.288    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 687034  767.958    0.001 3990.374    0.006 allGraphsTrain.py:35(<listcomp>)
                 687034    2.641    0.000 3509.190    0.005 game.py:41(step)
                 687034    3.681    0.000 3362.526    0.005 layers.py:718(step)
               15652006   26.250    0.000 3222.416    0.000 allGraphs.py:158(getInterventions)
                 687034  126.852    0.000 2079.756    0.003 allGraphsTrain.py:37(<listcomp>)
                 687035  103.735    0.000 2023.936    0.003 layers.py:684(update)
               22005789 1892.744    0.000 1892.744    0.000 {built-in method tensor}
               19087177   10.454    0.000 1797.848    0.000 game.py:37(board)
               14649634   13.945    0.000 1655.699    0.000 allGraphs.py:129(rightIntervention)
        167351648/14649634  109.305    0.000 1586.348    0.000 {built-in method builtins.min}
               41790582   18.922    0.000 1561.703    0.000 allGraphs.py:130(<lambda>)
                 687034    3.006    0.000 1548.047    0.002 agent.py:29(learn)
                 687034   14.926    0.000 1543.556    0.002 agent.py:117(_learn)
        320053662/41790582  480.763    0.000 1542.781    0.000 allGraphs.py:74(expected_moves)
                 687034   45.667    0.000 1528.630    0.002 learner.py:42(Qlearn)
               15652006   65.676    0.000 1526.163    0.000 allGraphs.py:153(format)
                 687034   57.724    0.000 1330.489    0.002 layers.py:17(step)
        430965094/98285940  128.903    0.000 1299.683    0.000 allGraphs.py:78(<genexpr>)
               68703400  116.730    0.000 1266.104    0.000 layer.py:98(move)
               72825604  171.444    0.000 1203.385    0.000 tensor.py:21(wrapped)
                 687034   51.712    0.000 1140.707    0.002 allGraphsTrain.py:44(<listcomp>)
                2876049   23.091    0.000 1127.014    0.000 layers.py:740(restart)
                2876049   11.451    0.000  902.765    0.000 level.py:8(__init__)
               72138570  822.982    0.000  822.982    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                2876049   33.967    0.000  784.615    0.000 levels.py:151(generate)
               68703400  776.410    0.000  776.410    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
             3028073946  519.165    0.000  758.803    0.000 enum.py:646(__hash__)
               13807144  130.473    0.000  716.114    0.000 level.py:41(notUsed)
                 687034  393.785    0.001  707.218    0.001 agent.py:67(modify)
        15801782/2061102   65.905    0.000  608.237    0.000 module.py:715(_call_impl)
               68703400  156.041    0.000  605.845    0.000 layers.py:735(check)
                 687034    4.754    0.000  603.739    0.001 grad_mode.py:23(decorate_context)
                 687034   21.764    0.000  589.999    0.001 adam.py:55(step)
                1374068    3.851    0.000  552.604    0.000 network.py:27(forward)
                1374068   15.239    0.000  539.588    0.000 container.py:115(forward)
              168354020  103.397    0.000  491.408    0.000 allGraphs.py:83(layers_not_in)
                 687034  108.665    0.000  483.369    0.001 functional.py:53(adam)
               68703400  104.546    0.000  434.447    0.000 layers.py:729(isFree)
              168354020  189.806    0.000  388.011    0.000 allGraphs.py:84(<listcomp>)
              189493706  106.289    0.000  366.728    0.000 {built-in method builtins.any}
                 687034    4.404    0.000  365.619    0.001 tensor.py:181(backward)
                 687034    2.781    0.000  361.215    0.001 __init__.py:68(backward)
                4809245  204.684    0.000  347.543    0.000 layer.py:167(NoRock_update)
                 687034  342.131    0.000  342.131    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
               13807144   10.589    0.000  338.040    0.000 level.py:38(elementsIn)
                 687034   10.398    0.000  331.721    0.000 agent.py:112(__call__)
              452201425  269.451    0.000  329.901    0.000 layer.py:95(isFree)
                2061102    8.589    0.000  251.204    0.000 tensor.py:576(__iter__)
              320053662  165.143    0.000  241.944    0.000 allGraphs.py:45(p)
               71451536  240.689    0.000  240.689    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
             3028076215  239.638    0.000  239.638    0.000 {built-in method builtins.hash}
                2061102  237.356    0.000  237.356    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
              141529104   42.526    0.000  231.525    0.000 {built-in method builtins.all}
               13807144  108.041    0.000  218.660    0.000 level.py:39(<listcomp>)
                2748136    4.993    0.000  216.002    0.000 conv.py:422(forward)
                2748136    6.730    0.000  208.812    0.000 conv.py:414(_conv_forward)
              119544050   61.613    0.000  201.477    0.000 overrides.py:1070(has_torch_function)
                2748136  201.067    0.000  201.067    0.000 {built-in method conv2d}
               20132343   15.898    0.000  194.104    0.000 layer.py:69(restart)
              526619608  147.566    0.000  180.882    0.000 layers.py:700(<genexpr>)
              171488024   43.976    0.000  171.803    0.000 layers.py:690(<genexpr>)
                2748136    6.584    0.000  157.398    0.000 linear.py:92(forward)
                2876149   75.995    0.000  151.185    0.000 layers.py:36(reset)
               38473958   90.677    0.000  150.635    0.000 tensor.py:933(grad)
                2748136   11.270    0.000  147.691    0.000 functional.py:1669(linear)
              662911387  146.148    0.000  146.148    0.000 level.py:32(inverse)
                 687034   12.455    0.000  130.303    0.000 optimizer.py:167(zero_grad)
               68703500   80.836    0.000  122.380    0.000 layers.py:113(isDone)
                 687034    5.950    0.000  113.653    0.000 agent.py:59(modify_board)
              600596441  112.020    0.000  112.020    0.000 enum.py:352(<genexpr>)
               34351919   68.355    0.000  110.484    0.000 layers.py:231(check)
               13807144   67.269    0.000  108.792    0.000 {built-in method _functools.reduce}
               34344149   65.257    0.000  106.778    0.000 layers.py:207(check)
                2748136  105.732    0.000  105.732    0.000 {built-in method addmm}
                 687034   60.868    0.000  104.290    0.000 collector.py:46(collect)
               34355895   63.009    0.000  103.024    0.000 layers.py:219(check)
                2876049   52.022    0.000   99.457    0.000 level.py:16(<dictcomp>)
               10992544   96.613    0.000   96.613    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              924616549   94.276    0.000   94.276    0.000 layer.py:91(positions)
              168802837   68.135    0.000   93.289    0.000 layer.py:130(add)
              344927916   88.554    0.000   88.554    0.000 layer.py:146(elements)
               10992544   80.123    0.000   80.123    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              314661840   66.818    0.000   79.056    0.000 overrides.py:1083(<genexpr>)
                 687034   51.965    0.000   77.455    0.000 allGraphsTrain.py:43(<listcomp>)
                 687034   75.263    0.000   75.263    0.000 {built-in method torch._C._nn.one_hot}
                4122204    4.094    0.000   70.726    0.000 activation.py:713(forward)
              323117136   64.233    0.000   69.015    0.000 {built-in method builtins.max}
                4122204    6.510    0.000   66.631    0.000 functional.py:1292(leaky_relu)
                 687034   16.415    0.000   61.056    0.000 allGraphs.py:137(transform)
                4122204   59.516    0.000   59.516    0.000 {built-in method torch._C._nn.leaky_relu}
                5496272   56.332    0.000   56.332    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                2061102   54.041    0.000   54.041    0.000 {method 'tolist' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9532011: <Diamonds1_0.5_var_2> in cluster <dcc> Done

Job <Diamonds1_0.5_var_2> was submitted from host <n-62-30-7> by user <s183905> in cluster <dcc> at Sat Apr 17 13:28:41 2021
Job was executed on host(s) <n-62-20-10>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sun Apr 18 09:15:04 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun Apr 18 09:15:04 2021
Terminated at Sun Apr 18 19:10:11 2021
Results reported at Sun Apr 18 19:10:11 2021

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

    CPU time :                                   35588.01 sec.
    Max Memory :                                 2065 MB
    Average Memory :                             2064.11 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14319.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35709 sec.
    Turnaround time :                            106890 sec.

The output (if any) is above this job summary.

