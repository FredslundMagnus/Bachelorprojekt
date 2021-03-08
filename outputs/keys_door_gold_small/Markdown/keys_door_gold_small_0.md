
# Parameters

    Name :                      keys_door_gold_small-0
    Main :                      teleport
    Hours :                     10.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Network1 :                  Networks.Teleporter
    Network2 :                  Networks.Mini
    Learner1 :                  Learners.Qlearn
    Learner2 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Exploration2 :              Explorations.epsilonGreedy
    Layer blocks :              True
    Layer goal :                True
    Layer gold :                True
    Layer keys :                True
    Layer door :                True
    Layer holder :              False
    Layer putter :              False
    K :                         200000
    Epsilon cap :               0.2
    Softmax cap :               0.03
    Gamma :                     0.98
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.2
    Intervention cost :         -0.05
    Replay size :               50000
    Sample size :               50
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      21944899651 function calls (21813639596 primitive calls) in 35682.73 seconds

##    Ordered by: cumulative time
   List reduced from 459 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35710.613 35710.613 {built-in method builtins.exec}
                      1    1.042    1.042 35710.613 35710.613 <string>:1(<module>)
                      1  130.356  130.356 35709.571 35709.571 main.py:10(teleport)
                4688006   17.767    0.000 13392.867    0.003 agent.py:26(learn)
                4688006  324.238    0.000 11399.082    0.002 learner.py:42(Qlearn)
                2344003   88.515    0.000 8003.492    0.003 agent.py:50(_learn)
                2344003    9.998    0.000 6943.155    0.003 game.py:21(step)
                2344003   12.065    0.000 6445.039    0.003 layers.py:212(step)
        147666638/16407594  606.371    0.000 5708.828    0.000 module.py:715(_call_impl)
                2344003   77.898    0.000 5362.274    0.002 agent.py:101(_learn)
               11719588   31.277    0.000 5324.101    0.000 network.py:24(forward)
               11719588  144.923    0.000 5221.019    0.000 container.py:115(forward)
                2344003 2894.617    0.001 5011.648    0.002 replaybuffer.py:27(teleporter_save_data)
                4688006   29.360    0.000 4513.561    0.001 grad_mode.py:23(decorate_context)
                4688006  157.289    0.000 4428.799    0.001 adam.py:55(step)
                2344003 2567.056    0.001 4301.290    0.002 agent.py:77(interveen)
                2344003  183.594    0.000 3711.195    0.002 layers.py:17(step)
                4688006  814.950    0.000 3630.445    0.001 functional.py:53(adam)
                4687579  120.356    0.000 3508.040    0.001 agent.py:45(__call__)
              234400300  250.471    0.000 3504.249    0.000 layer.py:66(move)
                2344004  226.403    0.000 2701.308    0.001 layers.py:192(update)
                4688006   29.978    0.000 2682.907    0.001 tensor.py:181(backward)
                4688006   19.399    0.000 2652.929    0.001 __init__.py:68(backward)
                4688006 2523.811    0.001 2523.811    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2344003 1088.996    0.000 2223.830    0.001 replaybuffer.py:23(sample_data)
                2344003  915.696    0.000 1914.075    0.001 agent.py:59(modify)
               23439176   41.973    0.000 1899.963    0.000 conv.py:422(forward)
               23439176   51.219    0.000 1841.169    0.000 conv.py:414(_conv_forward)
               23439176 1781.157    0.000 1781.157    0.000 {built-in method conv2d}
              159658026 1696.817    0.000 1696.817    0.000 {built-in method clone}
               30470758   69.131    0.000 1671.493    0.000 linear.py:92(forward)
               30470758  119.419    0.000 1569.674    0.000 functional.py:1669(linear)
              234400300  390.712    0.000 1548.167    0.000 layers.py:229(check)
              234400300  272.624    0.000 1453.359    0.000 layers.py:223(isFree)
             1142001868  998.429    0.000 1180.735    0.000 layer.py:63(isFree)
              295344432  681.878    0.000 1141.839    0.000 tensor.py:933(grad)
               18751597 1135.354    0.000 1135.354    0.000 {built-in method cat}
                2344003   34.254    0.000 1109.948    0.000 agent.py:96(__call__)
               30470758 1104.389    0.000 1104.389    0.000 {built-in method addmm}
                7031582   44.962    0.000 1057.112    0.000 agent.py:54(modify_board)
                1849287   16.798    0.000 1020.760    0.001 layers.py:233(restart)
                4688006   98.232    0.000 1003.857    0.000 optimizer.py:167(zero_grad)
                2344003   44.624    0.000  961.277    0.000 replaybuffer.py:19(stacker)
                1849287    3.913    0.000  851.346    0.000 levels.py:8(__init__)
                1849287   14.168    0.000  847.433    0.000 level.py:8(__init__)
                2522398  148.899    0.000  807.174    0.000 levels.py:11(generate)
               14064024  296.068    0.000  744.754    0.000 layer.py:90(update)
               42190346   37.302    0.000  737.366    0.000 activation.py:713(forward)
               84384108  715.018    0.000  715.018    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               42190346   61.139    0.000  700.065    0.000 functional.py:1292(leaky_relu)
                7031582  688.261    0.000  688.261    0.000 {built-in method torch._C._nn.one_hot}
                9916860  669.195    0.000  669.195    0.000 {built-in method tensor}
              243777512   72.900    0.000  655.039    0.000 {built-in method builtins.all}
               42190346  632.949    0.000  632.949    0.000 {built-in method torch._C._nn.leaky_relu}
               84384108  616.430    0.000  616.430    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              377383978  206.007    0.000  612.682    0.000 overrides.py:1070(has_torch_function)
              717165255  175.362    0.000  603.612    0.000 layers.py:197(<genexpr>)
                4688006    5.729    0.000  510.364    0.000 game.py:17(board)
              166689608  475.986    0.000  475.986    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              234400300  283.541    0.000  435.503    0.000 layers.py:95(check)
               42192054  432.834    0.000  432.834    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                2344003  252.481    0.000  430.739    0.000 collector.py:37(collect)
              234400400  271.416    0.000  405.642    0.000 layers.py:65(isDone)
               42192054  392.295    0.000  392.295    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              417230749  158.059    0.000  387.108    0.000 {built-in method builtins.any}
                4687579  130.530    0.000  360.707    0.000 exploration.py:53(softmaxer)
             1314758016  253.435    0.000  355.207    0.000 enum.py:646(__hash__)
               42192054  348.629    0.000  348.629    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              595723019  347.692    0.000  347.692    0.000 layer.py:85(elements)
              234400300  230.835    0.000  339.750    0.000 layers.py:50(check)
                2522398  175.542    0.000  332.081    0.000 levels.py:76(RFS)
              234400300  208.504    0.000  324.625    0.000 layers.py:77(check)
               42192054  299.141    0.000  299.141    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                9377112   44.046    0.000  266.169    0.000 tensor.py:21(wrapped)
             2616532897  260.809    0.000  260.809    0.000 layer.py:59(positions)
                4688006    7.509    0.000  248.101    0.000 loss.py:445(forward)
                4688006   28.584    0.000  240.592    0.000 functional.py:2637(mse_loss)
               42192054  236.676    0.000  236.676    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              794615358  182.520    0.000  225.807    0.000 overrides.py:1083(<genexpr>)
                9238086   85.906    0.000  218.908    0.000 random.py:315(sample)
               30470758  202.677    0.000  202.677    0.000 {method 't' of 'torch._C._TensorBase' objects}
               14064018  171.811    0.000  171.811    0.000 {built-in method sum}
              284669242  123.798    0.000  166.097    0.000 layer.py:76(add)
                7032009   34.013    0.000  149.846    0.000 tensor.py:506(__rsub__)
               11095722   18.497    0.000  148.550    0.000 layer.py:40(restart)
              185442160  100.861    0.000  145.932    0.000 layer.py:72(remove)
                4688006  139.042    0.000  139.042    0.000 {built-in method torch._C._nn.mse_loss}
               23439176   17.771    0.000  132.515    0.000 flatten.py:39(forward)
        419568581/419568579   63.141    0.000  129.719    0.000 {built-in method builtins.len}
                4688708  129.232    0.000  129.232    0.000 {built-in method max}
                7032009  128.633    0.000  128.633    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               42192144   52.774    0.000  118.344    0.000 tensor.py:596(__hash__)
                2344003   10.186    0.000  116.995    0.000 exploration.py:47(epsilonGreedy)
              173984979   79.848    0.000  115.965    0.000 random.py:250(_randbelow_with_getrandbits)
                7032009  115.834    0.000  115.834    0.000 {built-in method rsub}
               23439176  114.744    0.000  114.744    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                4687579  113.762    0.000  113.762    0.000 {built-in method multinomial}
              150011577  111.633    0.000  111.633    0.000 {built-in method torch._C._get_tracing_state}
                4688006   20.968    0.000  105.590    0.000 __init__.py:28(_make_grads)
              954312178  102.981    0.000  102.981    0.000 layer.py:125(isBlocking)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-11>
Subject: Job 9395014: <keys_door_gold_small_0> in cluster <dcc> Done

Job <keys_door_gold_small_0> was submitted from host <n-62-27-20> by user <s183905> in cluster <dcc> at Mon Mar  8 13:46:25 2021
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Mon Mar  8 13:59:22 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Mar  8 13:59:22 2021
Terminated at Mon Mar  8 23:54:50 2021
Results reported at Mon Mar  8 23:54:50 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=8G]"
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

    CPU time :                                   35622.59 sec.
    Max Memory :                                 2381 MB
    Average Memory :                             2373.91 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               5811.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35729 sec.
    Turnaround time :                            36505 sec.

The output (if any) is above this job summary.

