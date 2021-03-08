
# Parameters

    Name :                      keys_door_holder_putter_gold_small-0
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
    Layer holder :              True
    Layer putter :              True
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


      25362101630 function calls (25229266419 primitive calls) in 35690.14 seconds

##    Ordered by: cumulative time
   List reduced from 463 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35705.627 35705.627 {built-in method builtins.exec}
                      1    0.749    0.749 35705.627 35705.627 <string>:1(<module>)
                      1   96.448   96.448 35704.877 35704.877 main.py:10(teleport)
                4744274   16.316    0.000 13429.523    0.003 agent.py:26(learn)
                4744274  317.472    0.000 11502.645    0.002 learner.py:42(Qlearn)
                2372137   73.454    0.000 8025.499    0.003 agent.py:50(_learn)
                2372137    8.553    0.000 7701.923    0.003 game.py:21(step)
                2372137   10.741    0.000 7180.368    0.003 layers.py:212(step)
        149438703/16604503  583.593    0.000 5664.320    0.000 module.py:715(_call_impl)
                2372137   62.551    0.000 5378.556    0.002 agent.py:101(_learn)
               11860229   31.747    0.000 5287.115    0.000 network.py:24(forward)
               11860229  135.497    0.000 5180.789    0.000 container.py:115(forward)
                2372137 2629.871    0.001 4790.033    0.002 replaybuffer.py:27(teleporter_save_data)
                2372137  169.396    0.000 4785.576    0.002 layers.py:17(step)
                4744274   28.771    0.000 4654.795    0.001 grad_mode.py:23(decorate_context)
              237213700  249.003    0.000 4593.748    0.000 layer.py:66(move)
                4744274  157.190    0.000 4572.223    0.001 adam.py:55(step)
                2372137 2425.856    0.001 4159.331    0.002 agent.py:77(interveen)
                4744274  841.713    0.000 3741.930    0.001 functional.py:53(adam)
                4743818   98.247    0.000 3471.534    0.001 agent.py:45(__call__)
                4744274   28.313    0.000 2645.887    0.001 tensor.py:181(backward)
              237213700  506.101    0.000 2630.193    0.000 layers.py:229(check)
                4744274   17.892    0.000 2617.574    0.001 __init__.py:68(backward)
                4744274 2490.649    0.001 2490.649    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2372138  223.358    0.000 2367.914    0.001 layers.py:192(update)
               23720458   43.611    0.000 1896.904    0.000 conv.py:422(forward)
                2372137  816.084    0.000 1876.163    0.001 replaybuffer.py:23(sample_data)
                2372137  866.818    0.000 1850.873    0.001 agent.py:59(modify)
               23720458   47.444    0.000 1837.217    0.000 conv.py:414(_conv_forward)
               23720458 1781.419    0.000 1781.419    0.000 {built-in method conv2d}
              159224019 1735.694    0.000 1735.694    0.000 {built-in method clone}
               30836413   70.981    0.000 1666.603    0.000 linear.py:92(forward)
               30836413  117.201    0.000 1563.847    0.000 functional.py:1669(linear)
              237213700  341.335    0.000 1463.054    0.000 layers.py:223(isFree)
              298889316  723.996    0.000 1202.889    0.000 tensor.py:933(grad)
             1518199853  908.607    0.000 1121.718    0.000 layer.py:63(isFree)
               30836413 1104.138    0.000 1104.138    0.000 {built-in method addmm}
                2372137   27.611    0.000 1087.458    0.000 agent.py:96(__call__)
               18976640 1071.899    0.000 1071.899    0.000 {built-in method cat}
                4744274  105.390    0.000 1053.385    0.000 optimizer.py:167(zero_grad)
                7115955   44.113    0.000 1048.034    0.000 agent.py:54(modify_board)
              237213700  569.893    0.000  938.186    0.000 layers.py:124(check)
                2372137   38.398    0.000  889.454    0.000 replaybuffer.py:19(stacker)
               18977104  309.194    0.000  779.034    0.000 layer.py:90(update)
               85396932  741.320    0.000  741.320    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               10036011  725.718    0.000  725.718    0.000 {built-in method tensor}
               42696642   36.903    0.000  724.992    0.000 activation.py:713(forward)
               42696642   59.956    0.000  688.090    0.000 functional.py:1292(leaky_relu)
                7115955  677.285    0.000  677.285    0.000 {built-in method torch._C._nn.one_hot}
              246703716   75.551    0.000  655.596    0.000 {built-in method builtins.all}
                 983167   10.303    0.000  655.251    0.001 layers.py:233(restart)
               85396932  636.966    0.000  636.966    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              381913727  210.544    0.000  634.510    0.000 overrides.py:1070(has_torch_function)
               42696642  621.908    0.000  621.908    0.000 {built-in method torch._C._nn.leaky_relu}
              727495134  176.811    0.000  602.223    0.000 layers.py:197(<genexpr>)
                4744274    5.598    0.000  569.493    0.000 game.py:17(board)
                 983167    2.077    0.000  555.613    0.001 levels.py:8(__init__)
                 983167    8.088    0.000  553.536    0.001 level.py:8(__init__)
             1998970906  382.352    0.000  549.811    0.000 enum.py:646(__hash__)
                1340942   83.226    0.000  530.601    0.000 levels.py:11(generate)
              166339974  484.321    0.000  484.321    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              237213700  286.419    0.000  443.113    0.000 layers.py:95(check)
               42698466  439.530    0.000  439.530    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                2372137  254.997    0.000  438.535    0.000 collector.py:37(collect)
              422238689  167.578    0.000  404.433    0.000 {built-in method builtins.any}
               42698466  404.361    0.000  404.361    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              237213800  261.904    0.000  398.114    0.000 layers.py:65(isDone)
               42698466  356.926    0.000  356.926    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                4743818  131.925    0.000  355.351    0.000 exploration.py:53(softmaxer)
             3637055468  346.451    0.000  346.451    0.000 layer.py:59(positions)
              638204314  344.171    0.000  344.171    0.000 layer.py:85(elements)
              237213700  224.259    0.000  334.368    0.000 layers.py:50(check)
              237213700  211.008    0.000  327.081    0.000 layers.py:77(check)
               42698466  309.259    0.000  309.259    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                9489916   44.509    0.000  263.941    0.000 tensor.py:21(wrapped)
               42698466  246.287    0.000  246.287    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                4744274    8.937    0.000  244.877    0.000 loss.py:445(forward)
                4744274   26.215    0.000  235.940    0.000 functional.py:2637(mse_loss)
              804153309  187.988    0.000  233.537    0.000 overrides.py:1083(<genexpr>)
               30836413  197.033    0.000  197.033    0.000 {method 't' of 'torch._C._TensorBase' objects}
                6037188   74.092    0.000  194.097    0.000 random.py:315(sample)
              245739339  139.026    0.000  193.604    0.000 layer.py:72(remove)
                1340942   97.469    0.000  184.316    0.000 levels.py:76(RFS)
               14232822  175.438    0.000  175.438    0.000 {built-in method sum}
              300625240  130.558    0.000  175.179    0.000 layer.py:76(add)
             1998988369  167.463    0.000  167.463    0.000 {built-in method builtins.hash}
                7116411   34.498    0.000  149.104    0.000 tensor.py:506(__rsub__)
                4744274  136.909    0.000  136.909    0.000 {built-in method torch._C._nn.mse_loss}
             1329834374  136.665    0.000  136.665    0.000 layer.py:125(isBlocking)
        404948815/404948813   64.557    0.000  133.983    0.000 {built-in method builtins.len}
               23720458   18.489    0.000  133.869    0.000 flatten.py:39(forward)
                2949501   17.128    0.000  129.823    0.000 level.py:41(notUsed)
                7116411  129.282    0.000  129.282    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                4744985  124.442    0.000  124.442    0.000 {built-in method max}
               42698556   54.347    0.000  121.222    0.000 tensor.py:596(__hash__)
              151811788  116.020    0.000  116.020    0.000 {built-in method torch._C._get_tracing_state}
               23720458  115.380    0.000  115.380    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                7116411  114.606    0.000  114.606    0.000 {built-in method rsub}
                4743818  109.282    0.000  109.282    0.000 {built-in method multinomial}
                2372137    9.045    0.000  105.737    0.000 exploration.py:47(epsilonGreedy)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-15>
Subject: Job 9395016: <keys_door_holder_putter_gold_small_0> in cluster <dcc> Done

Job <keys_door_holder_putter_gold_small_0> was submitted from host <n-62-27-20> by user <s183905> in cluster <dcc> at Mon Mar  8 13:46:25 2021
Job was executed on host(s) <n-62-20-15>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Mon Mar  8 14:42:16 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Mar  8 14:42:16 2021
Terminated at Tue Mar  9 00:37:38 2021
Results reported at Tue Mar  9 00:37:38 2021

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

    CPU time :                                   35614.84 sec.
    Max Memory :                                 2393 MB
    Average Memory :                             2391.15 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               5799.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35725 sec.
    Turnaround time :                            39073 sec.

The output (if any) is above this job summary.

