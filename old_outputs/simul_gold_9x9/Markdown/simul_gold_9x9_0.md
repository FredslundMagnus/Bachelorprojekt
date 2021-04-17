
# Parameters

    Name :                      simul_gold_9x9-0
    Main :                      simulation
    Level :                     Levels.Causal1
    Hours :                     4.0
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
    Layer rock :                False
    Layer dirt :                False
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
    Minutes used :              235 minutes.
    Hours used :                3 hours.

# Profiling


      7426683904 function calls (7398146799 primitive calls) in 14084.83 seconds

##    Ordered by: cumulative time
   List reduced from 450 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 14107.284 14107.284 {built-in method builtins.exec}
                      1    0.913    0.913 14107.284 14107.284 <string>:1(<module>)
                      1   35.303   35.303 14106.371 14106.371 main.py:47(simulation)
                 792672   20.454    0.000 3837.654    0.005 simulator.py:51(learn)
                 792672  202.860    0.000 3817.201    0.005 simulator.py:28(learn)
                 792672 1838.628    0.002 3488.864    0.004 replaybuffer.py:27(teleporter_save_data)
                 792672    3.196    0.000 2491.325    0.003 game.py:27(step)
                 792672    4.168    0.000 2325.965    0.003 layers.py:295(step)
                 792672 1494.598    0.002 2202.794    0.003 agent.py:77(interveen)
        33292055/4756019  148.746    0.000 1572.206    0.000 module.py:715(_call_impl)
                 792672   85.040    0.000 1481.739    0.002 layers.py:266(update)
                1585344    8.949    0.000 1470.679    0.001 grad_mode.py:23(decorate_context)
                1585344   41.143    0.000 1443.587    0.001 adam.py:55(step)
                3170675   37.072    0.000 1418.248    0.000 container.py:115(forward)
               87599172 1273.450    0.000 1273.450    0.000 {built-in method clone}
                1585344  262.243    0.000 1229.965    0.001 functional.py:53(adam)
                1988256   16.399    0.000  848.294    0.000 layers.py:316(restart)
                 792672   59.759    0.000  834.998    0.001 layers.py:18(step)
                1585331    4.009    0.000  832.708    0.001 network.py:24(forward)
                 792672  426.138    0.001  827.487    0.001 agent.py:59(modify)
                1585344   10.168    0.000  791.451    0.000 tensor.py:181(backward)
                1585344    5.424    0.000  781.283    0.000 __init__.py:68(backward)
               79267200   91.535    0.000  768.269    0.000 layer.py:70(move)
                1585344  732.981    0.000  732.981    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                 792672  277.740    0.000  707.384    0.001 replaybuffer.py:23(sample_data)
                 792659   22.339    0.000  696.294    0.001 agent.py:45(__call__)
                1988256    7.965    0.000  675.552    0.000 level.py:8(__init__)
                1988256  113.027    0.000  644.877    0.000 levels.py:9(generate)
                6341350   11.480    0.000  585.241    0.000 conv.py:422(forward)
                6341350   13.145    0.000  569.508    0.000 conv.py:414(_conv_forward)
                6341350  553.745    0.000  553.745    0.000 {built-in method conv2d}
                7926707  481.782    0.000  481.782    0.000 {built-in method cat}
                 792672   16.848    0.000  441.352    0.001 agent.py:96(__call__)
               89977175  399.836    0.000  399.836    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                5548665   13.205    0.000  381.142    0.000 linear.py:92(forward)
                 792672   14.818    0.000  372.158    0.000 replaybuffer.py:19(stacker)
                5548665   23.857    0.000  361.677    0.000 functional.py:1669(linear)
               79267200   69.580    0.000  350.879    0.000 layers.py:306(isFree)
               66584460  207.940    0.000  321.058    0.000 tensor.py:933(grad)
                 792672    2.544    0.000  315.389    0.000 simulator.py:25(RDforward)
                 792672    3.012    0.000  305.705    0.000 simulator.py:22(boardforward)
                1585344   28.986    0.000  305.423    0.000 optimizer.py:167(zero_grad)
                3170688  182.989    0.000  296.421    0.000 layer.py:132(NoRock_update)
              291945732  236.000    0.000  281.299    0.000 layer.py:67(isFree)
                1585331   11.637    0.000  275.472    0.000 agent.py:54(modify_board)
                1988256  140.432    0.000  267.195    0.000 levels.py:75(RFS)
                2378003  260.912    0.000  260.912    0.000 {built-in method torch._C._nn.one_hot}
                5548665  260.813    0.000  260.813    0.000 {built-in method addmm}
               19024128  257.919    0.000  257.919    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               79267200   89.062    0.000  235.534    0.000 layers.py:312(check)
               84023390   28.923    0.000  226.245    0.000 {built-in method builtins.all}
               19024128  217.488    0.000  217.488    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                9512012    8.841    0.000  211.413    0.000 activation.py:713(forward)
                3328730  205.658    0.000  205.658    0.000 {built-in method tensor}
              241656569   60.991    0.000  203.451    0.000 layers.py:272(<genexpr>)
                9512012   13.700    0.000  202.572    0.000 functional.py:1292(leaky_relu)
                9512012  187.611    0.000  187.611    0.000 {built-in method torch._C._nn.leaky_relu}
                4756190   27.796    0.000  166.191    0.000 tensor.py:21(wrapped)
                7953024   15.662    0.000  153.061    0.000 layer.py:44(restart)
               86401378   52.550    0.000  152.563    0.000 overrides.py:1070(has_torch_function)
                1585344    1.745    0.000  144.391    0.000 game.py:23(board)
                9512064  142.720    0.000  142.720    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               79267200   88.005    0.000  134.071    0.000 layers.py:110(isDone)
               79267200   81.102    0.000  126.597    0.000 layers.py:47(check)
                9512064  125.131    0.000  125.131    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                9512064  116.413    0.000  116.413    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                9512064  104.660    0.000  104.660    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                1988256   53.192    0.000  104.517    0.000 layers.py:33(reset)
                1585344    2.470    0.000   98.776    0.000 loss.py:445(forward)
                1585344    8.401    0.000   96.306    0.000 functional.py:2637(mse_loss)
              180246924   70.173    0.000   95.906    0.000 layer.py:94(add)
               95120732   38.943    0.000   94.846    0.000 {built-in method builtins.any}
                3963360   94.614    0.000   94.614    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                1988256   13.787    0.000   89.988    0.000 level.py:41(notUsed)
                4769184   34.546    0.000   87.788    0.000 random.py:315(sample)
                9512064   84.251    0.000   84.251    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              281806286   58.969    0.000   84.168    0.000 enum.py:646(__hash__)
              364924639   75.213    0.000   75.213    0.000 layer.py:110(elements)
                 792659   26.364    0.000   73.737    0.000 exploration.py:53(softmaxer)
               97424544   66.466    0.000   66.466    0.000 level.py:32(inverse)
                1585344   65.046    0.000   65.046    0.000 {built-in method torch._C._nn.mse_loss}
              119295360   43.009    0.000   65.022    0.000 levels.py:31(<genexpr>)
              627751500   60.406    0.000   60.406    0.000 layer.py:63(positions)
               81625245   39.738    0.000   57.525    0.000 random.py:250(_randbelow_with_getrandbits)
              183107532   44.114    0.000   54.772    0.000 overrides.py:1083(<genexpr>)
               76574320   35.730    0.000   53.587    0.000 layer.py:90(remove)
        428040477/428040476   35.055    0.000   49.477    0.000 {built-in method builtins.len}
                5548665   49.294    0.000   49.294    0.000 {method 't' of 'torch._C._TensorBase' objects}
                2378016   48.605    0.000   48.605    0.000 {built-in method sum}
                6341350   45.708    0.000   45.708    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              563758451   44.533    0.000   44.533    0.000 {method 'append' of 'list' objects}
                5548678    4.385    0.000   43.310    0.000 flatten.py:39(forward)
               31812096   15.171    0.000   42.936    0.000 random.py:285(choice)
                1585344    7.292    0.000   41.267    0.000 __init__.py:28(_make_grads)
                 792672    3.210    0.000   38.430    0.000 exploration.py:47(epsilonGreedy)
               34084885   34.532    0.000   34.532    0.000 {built-in method torch._C._get_tracing_state}
                1585344   32.560    0.000   32.560    0.000 {built-in method ones_like}
                 792673   32.271    0.000   32.271    0.000 {built-in method nonzero}
                1743189   31.903    0.000   31.903    0.000 {method 'long' of 'torch._C._TensorBase' objects}
              194716813   31.889    0.000   31.889    0.000 {method 'add' of 'set' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-13>
Subject: Job 9434611: <simul_gold_9x9_0> in cluster <dcc> Done

Job <simul_gold_9x9_0> was submitted from host <n-62-30-8> by user <s183905> in cluster <dcc> at Thu Mar 18 20:16:27 2021
Job was executed on host(s) <n-62-20-13>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Thu Mar 18 20:16:28 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Mar 18 20:16:28 2021
Terminated at Fri Mar 19 00:11:41 2021
Results reported at Fri Mar 19 00:11:41 2021

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

    CPU time :                                   14070.78 sec.
    Max Memory :                                 2435 MB
    Average Memory :                             2431.08 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               5757.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   14158 sec.
    Turnaround time :                            14114 sec.

The output (if any) is above this job summary.

