
# Parameters

    Name :                      teleport_short-0
    Main :                      teleport
    Hours :                     3.0
    Batch :                     100
    Width :                     11
    Height :                    11
    Network1 :                  Networks.Teleporter
    Network2 :                  Networks.Mini
    Learner1 :                  Learners.Qlearn
    Learner2 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Exploration2 :              Explorations.epsilonGreedy
    Layer blocks :              True
    Layer goal :                True
    Layer gold :                False
    Layer keys :                False
    Layer door :                False
    Layer holder :              False
    Layer putter :              False
    K :                         100000
    Epsilon cap :               0.1
    Softmax cap :               0.02
    Gamma :                     0.95
    Update :                    10000
    Reset chance :              0.005
    Modified done chance :      0.05
    Miss intervention cost :    -0.2
    Intervention cost :         -0.1
    Replay size :               50000
    Sample size :               50
    Minutes used :              175 minutes.
    Hours used :                2 hours.

# Profiling


      5103319792 function calls (5064614885 primitive calls) in 10501.48 seconds

##    Ordered by: cumulative time
   List reduced from 446 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 10513.319 10513.319 {built-in method builtins.exec}
                      1    0.690    0.690 10513.319 10513.319 <string>:1(<module>)
                      1   26.578   26.578 10512.629 10512.629 main.py:10(teleport)
                1382006    4.372    0.000 3585.741    0.003 agent.py:26(learn)
                1382006   85.794    0.000 3066.680    0.002 learner.py:42(Qlearn)
                 691003   68.047    0.000 2603.412    0.004 collector.py:36(collect)
                3455015 2185.420    0.001 2522.621    0.001 {built-in method builtins.sum}
                 691003   20.496    0.000 2140.331    0.003 agent.py:50(_learn)
        43523595/4836283  155.191    0.000 1513.255    0.000 module.py:715(_call_impl)
                 691003   17.944    0.000 1437.284    0.002 agent.py:101(_learn)
                3454277    8.550    0.000 1412.842    0.000 network.py:24(forward)
                3454277   35.430    0.000 1385.531    0.000 container.py:115(forward)
                 691003    2.259    0.000 1317.318    0.002 game.py:21(step)
                1382006    7.944    0.000 1237.692    0.001 grad_mode.py:23(decorate_context)
                1382006   40.547    0.000 1214.486    0.001 adam.py:55(step)
                 691003    2.781    0.000 1194.810    0.002 layers.py:212(step)
                1382006  222.588    0.000  994.011    0.001 functional.py:53(adam)
                1381268   26.897    0.000  929.101    0.001 agent.py:45(__call__)
                 691003  385.432    0.001  849.486    0.001 agent.py:77(interveen)
                 691003  410.755    0.001  741.135    0.001 replaybuffer.py:27(teleporter_save_data)
                 691004   59.515    0.000  722.732    0.001 layers.py:192(update)
                1382006    7.930    0.000  702.843    0.001 tensor.py:181(backward)
                1382006    4.316    0.000  694.913    0.001 __init__.py:68(backward)
                1382006  661.612    0.000  661.612    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                 691003  225.750    0.000  518.224    0.001 replaybuffer.py:23(sample_data)
                 691003  244.240    0.000  514.131    0.001 agent.py:59(modify)
                6908554   11.463    0.000  510.160    0.000 conv.py:422(forward)
                6908554   13.178    0.000  494.500    0.000 conv.py:414(_conv_forward)
                6908554  478.797    0.000  478.797    0.000 {built-in method conv2d}
                 691003   42.816    0.000  465.038    0.001 layers.py:17(step)
                8980825   19.551    0.000  448.806    0.000 linear.py:92(forward)
                8980825   31.462    0.000  420.497    0.000 functional.py:1669(linear)
               69100300   55.798    0.000  415.705    0.000 layer.py:66(move)
                 736982    5.089    0.000  355.652    0.000 layers.py:233(restart)
                4146294   12.299    0.000  349.661    0.000 tensor.py:576(__iter__)
                4146294  330.628    0.000  330.628    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               87066432  195.577    0.000  325.303    0.000 tensor.py:933(grad)
                8980825  295.842    0.000  295.842    0.000 {built-in method addmm}
                5527286  294.702    0.000  294.702    0.000 {built-in method cat}
                 691003    7.913    0.000  287.048    0.000 agent.py:96(__call__)
                2072271   11.901    0.000  286.733    0.000 agent.py:54(modify_board)
                1382006   25.673    0.000  283.194    0.000 optimizer.py:167(zero_grad)
                 736982    1.123    0.000  282.840    0.000 levels.py:8(__init__)
                 736982    2.610    0.000  281.718    0.000 level.py:8(__init__)
                 736982   57.944    0.000  272.533    0.000 levels.py:11(generate)
               26705796  269.911    0.000  269.911    0.000 {built-in method clone}
               69100300   38.978    0.000  248.246    0.000 layers.py:223(isFree)
                 691003   10.907    0.000  246.557    0.000 replaybuffer.py:19(stacker)
              150876140  185.086    0.000  209.268    0.000 layer.py:63(isFree)
               24876108  198.605    0.000  198.605    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               12435102   10.736    0.000  193.588    0.000 activation.py:713(forward)
                2072271  188.059    0.000  188.059    0.000 {built-in method torch._C._nn.one_hot}
               12435102   16.028    0.000  182.852    0.000 functional.py:1292(leaky_relu)
              111249625   57.379    0.000  172.144    0.000 overrides.py:1070(has_torch_function)
               71864762   19.830    0.000  171.915    0.000 {built-in method builtins.all}
               24876108  168.070    0.000  168.070    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               12435102  165.270    0.000  165.270    0.000 {built-in method torch._C._nn.leaky_relu}
                2876092  159.787    0.000  159.787    0.000 {built-in method tensor}
              207694641   45.902    0.000  157.923    0.000 layers.py:197(<genexpr>)
                 736982   73.629    0.000  142.439    0.000 levels.py:76(RFS)
                2073012   62.809    0.000  121.175    0.000 layer.py:90(update)
                1382006    1.395    0.000  120.253    0.000 game.py:17(board)
               12438054  115.957    0.000  115.957    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              122994463   44.894    0.000  109.175    0.000 {built-in method builtins.any}
               69100400   69.848    0.000  106.771    0.000 layers.py:65(isDone)
               12438054  105.307    0.000  105.307    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               12438054   95.645    0.000   95.645    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                1381268   35.331    0.000   94.500    0.000 exploration.py:53(softmaxer)
               12438054   84.104    0.000   84.104    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               28778067   80.273    0.000   80.273    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                2764362   12.064    0.000   71.359    0.000 tensor.py:21(wrapped)
                2210946    5.761    0.000   66.800    0.000 layer.py:40(restart)
               12438054   66.475    0.000   66.475    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                1382006    1.938    0.000   64.900    0.000 loss.py:445(forward)
               69100300   49.317    0.000   63.544    0.000 layers.py:229(check)
              234244299   51.535    0.000   63.436    0.000 overrides.py:1083(<genexpr>)
                1382006    7.283    0.000   62.962    0.000 functional.py:2637(mse_loss)
                8980825   53.842    0.000   53.842    0.000 {method 't' of 'torch._C._TensorBase' objects}
                1427985   19.296    0.000   50.875    0.000 random.py:315(sample)
                 737082   24.960    0.000   47.383    0.000 layers.py:37(reset)
               95428588   34.512    0.000   46.192    0.000 layer.py:76(add)
              194395938   44.839    0.000   44.839    0.000 layer.py:85(elements)
                2073009    9.412    0.000   40.662    0.000 tensor.py:506(__rsub__)
        128368210/128368208   17.803    0.000   37.703    0.000 {built-in method builtins.len}
                1382006   36.248    0.000   36.248    0.000 {built-in method torch._C._nn.mse_loss}
                2073009   34.973    0.000   34.973    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                6908554    4.735    0.000   34.738    0.000 flatten.py:39(forward)
               54497171   23.050    0.000   33.693    0.000 random.py:250(_randbelow_with_getrandbits)
               70750272   22.337    0.000   33.545    0.000 levels.py:33(<genexpr>)
                1382213   33.427    0.000   33.427    0.000 {built-in method max}
              386733161   33.359    0.000   33.359    0.000 layer.py:59(positions)
               47669889   32.686    0.000   32.686    0.000 {built-in method torch._C._get_tracing_state}
               12438144   13.972    0.000   32.429    0.000 tensor.py:596(__hash__)
                2073009   31.250    0.000   31.250    0.000 {built-in method rsub}
              111845359   21.046    0.000   30.465    0.000 enum.py:646(__hash__)
                6908554   30.002    0.000   30.002    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                1381268   29.363    0.000   29.363    0.000 {built-in method multinomial}
                1382006    5.175    0.000   27.880    0.000 __init__.py:28(_make_grads)
                1382006   27.196    0.000   27.196    0.000 {built-in method gather}
               40887920   18.128    0.000   26.281    0.000 layer.py:72(remove)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-5>
Subject: Job 9367046: <teleport_short_0> in cluster <dcc> Done

Job <teleport_short_0> was submitted from host <n-62-30-7> by user <s183905> in cluster <dcc> at Sat Mar  6 16:12:39 2021
Job was executed on host(s) <n-62-20-5>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sat Mar  6 16:12:41 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat Mar  6 16:12:41 2021
Terminated at Sat Mar  6 19:08:20 2021
Results reported at Sat Mar  6 19:08:20 2021

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

    CPU time :                                   10480.52 sec.
    Max Memory :                                 2389 MB
    Average Memory :                             2357.37 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               5803.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   10644 sec.
    Turnaround time :                            10541 sec.

The output (if any) is above this job summary.

