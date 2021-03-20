
# Parameters

    Name :                      causal1_9x9-1
    Main :                      teleport
    Level :                     Levels.Causal1
    Hours :                     12.0
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
    Minutes used :              715 minutes.
    Hours used :                11 hours.

# Profiling


      22745948310 function calls (22639016791 primitive calls) in 42907.53 seconds

##    Ordered by: cumulative time
   List reduced from 458 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 42907.531 42907.531 {built-in method builtins.exec}
                      1    0.955    0.955 42907.531 42907.531 <string>:1(<module>)
                      1   83.717   83.717 42906.576 42906.576 main.py:13(teleport)
                3818996   14.771    0.000 13769.204    0.004 agent.py:26(learn)
                3818996  330.133    0.000 11965.091    0.003 learner.py:42(Qlearn)
                1909498 5667.316    0.003 10735.985    0.006 replaybuffer.py:27(teleporter_save_data)
                1909498   60.372    0.000 8195.689    0.004 agent.py:50(_learn)
                1909498    7.991    0.000 6639.537    0.003 game.py:27(step)
                1909498 4572.256    0.002 6232.610    0.003 agent.py:77(interveen)
                1909498   10.037    0.000 6210.097    0.003 layers.py:295(step)
                1909498   52.384    0.000 5550.638    0.003 agent.py:101(_learn)
        120296879/13366371  507.822    0.000 5419.844    0.000 module.py:715(_call_impl)
                3818996   24.045    0.000 5134.511    0.001 grad_mode.py:23(decorate_context)
                9547375   27.049    0.000 5077.902    0.001 network.py:24(forward)
                3818996  130.371    0.000 5067.522    0.001 adam.py:55(step)
                9547375  134.350    0.000 4988.755    0.001 container.py:115(forward)
                3818996  929.374    0.000 4339.553    0.001 functional.py:53(adam)
              270102656 3905.731    0.000 3905.731    0.000 {built-in method clone}
                3818881   84.594    0.000 3304.305    0.001 agent.py:45(__call__)
                1909499  205.096    0.000 3182.152    0.002 layers.py:266(update)
                1909498  151.629    0.000 3006.110    0.002 layers.py:18(step)
              190949800  249.385    0.000 2836.165    0.000 layer.py:70(move)
                3818996   24.447    0.000 2689.774    0.001 tensor.py:181(backward)
                3818996   13.602    0.000 2665.327    0.001 __init__.py:68(backward)
                3818996 2547.063    0.001 2547.063    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                1909498 1057.522    0.001 2010.860    0.001 agent.py:59(modify)
               19094750   36.398    0.000 1778.573    0.000 conv.py:422(forward)
               19094750   38.497    0.000 1729.545    0.000 conv.py:414(_conv_forward)
                1909498  694.156    0.000 1715.950    0.001 replaybuffer.py:23(sample_data)
               19094750 1683.335    0.000 1683.335    0.000 {built-in method conv2d}
               24823129   63.069    0.000 1628.840    0.000 linear.py:92(forward)
               24823129  106.425    0.000 1539.538    0.000 functional.py:1669(linear)
                6072726   45.239    0.000 1469.692    0.000 layers.py:316(restart)
              190949800  346.611    0.000 1283.900    0.000 layers.py:312(check)
              275831035 1209.980    0.000 1209.980    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              240596802  720.930    0.000 1123.322    0.000 tensor.py:933(grad)
               24823129 1098.884    0.000 1098.884    0.000 {built-in method addmm}
                3818996  104.156    0.000 1076.141    0.000 optimizer.py:167(zero_grad)
               17185367 1068.064    0.000 1068.064    0.000 {built-in method cat}
              190949800  258.612    0.000 1063.950    0.000 layers.py:306(isFree)
                1909498   25.749    0.000 1038.318    0.001 agent.py:96(__call__)
                6072726   24.479    0.000  986.660    0.000 level.py:8(__init__)
                5728379   43.252    0.000  984.361    0.000 agent.py:54(modify_board)
               68741928  904.566    0.000  904.566    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                6072726   71.240    0.000  891.020    0.000 levels.py:122(generate)
               11456994  525.768    0.000  882.943    0.000 layer.py:132(NoRock_update)
                1909498   34.571    0.000  881.627    0.000 replaybuffer.py:19(stacker)
             1099767133  635.692    0.000  805.338    0.000 layer.py:67(isFree)
               68741928  772.717    0.000  772.717    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               23683199  171.683    0.000  754.969    0.000 level.py:41(notUsed)
               34370504   30.939    0.000  747.783    0.000 activation.py:713(forward)
               34370504   49.686    0.000  716.844    0.000 functional.py:1292(leaky_relu)
               34370504  662.608    0.000  662.608    0.000 {built-in method torch._C._nn.leaky_relu}
                5728379  613.451    0.000  613.451    0.000 {built-in method torch._C._nn.one_hot}
                8090619  567.563    0.000  567.563    0.000 {built-in method tensor}
              198588696   67.852    0.000  556.082    0.000 {built-in method builtins.all}
              307429400  182.589    0.000  526.027    0.000 overrides.py:1070(has_torch_function)
              599637014  158.518    0.000  507.448    0.000 layers.py:272(<genexpr>)
               34370964  498.943    0.000  498.943    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                1909498  284.893    0.000  478.265    0.000 collector.py:54(collect)
               34370964  444.811    0.000  444.811    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               36436356   34.313    0.000  423.427    0.000 layer.py:44(restart)
                3818996    4.356    0.000  415.640    0.000 game.py:23(board)
               34370964  411.762    0.000  411.762    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
             1390767364  270.096    0.000  397.788    0.000 enum.py:646(__hash__)
               34370964  365.845    0.000  365.845    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              190949800  224.181    0.000  357.228    0.000 layers.py:142(check)
                3818881  125.194    0.000  349.226    0.000 exploration.py:53(softmaxer)
                6072826  164.531    0.000  329.610    0.000 layers.py:33(reset)
              190949900  213.514    0.000  327.250    0.000 layers.py:110(isDone)
              339890522  133.328    0.000  325.065    0.000 {built-in method builtins.any}
             1092435303  300.445    0.000  300.445    0.000 level.py:32(inverse)
               34370964  294.259    0.000  294.259    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              190949800  170.921    0.000  267.719    0.000 layers.py:123(check)
              190949800  168.456    0.000  262.199    0.000 layers.py:47(check)
                7638796   38.641    0.000  250.819    0.000 tensor.py:21(wrapped)
              417108653  171.477    0.000  235.021    0.000 layer.py:94(add)
                3818996    5.239    0.000  225.984    0.000 loss.py:445(forward)
              851318568  223.861    0.000  223.861    0.000 layer.py:110(elements)
                3818996   22.622    0.000  220.745    0.000 functional.py:2637(mse_loss)
               24823129  215.523    0.000  215.523    0.000 {method 't' of 'torch._C._TensorBase' objects}
               23683199   18.118    0.000  211.411    0.000 level.py:38(elementsIn)
             2156857039  210.409    0.000  210.409    0.000 layer.py:63(positions)
               11456988  190.585    0.000  190.585    0.000 {built-in method sum}
              647320344  152.565    0.000  189.100    0.000 overrides.py:1083(<genexpr>)
        1460895298/1460895296  118.574    0.000  180.389    0.000 {built-in method builtins.len}
                5728494   31.951    0.000  150.028    0.000 tensor.py:506(__rsub__)
               19094750   14.485    0.000  139.348    0.000 flatten.py:39(forward)
                3818996  138.025    0.000  138.025    0.000 {built-in method torch._C._nn.mse_loss}
              189459107   92.617    0.000  137.057    0.000 layer.py:90(remove)
                1909498   50.561    0.000  136.568    0.000 random.py:315(sample)
                5728494  131.268    0.000  131.268    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
             1390781443  127.694    0.000  127.694    0.000 {built-in method builtins.hash}
               19094750  124.863    0.000  124.863    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                3819567  124.722    0.000  124.722    0.000 {built-in method max}
               23683199   62.112    0.000  122.500    0.000 level.py:39(<listcomp>)
              122207139  119.262    0.000  119.262    0.000 {built-in method torch._C._get_tracing_state}
                5728494  118.077    0.000  118.077    0.000 {built-in method rsub}
                3818881  112.081    0.000  112.081    0.000 {built-in method multinomial}
             1242767471  103.654    0.000  103.654    0.000 {method 'append' of 'list' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-14>
Subject: Job 9434609: <causal1_9x9_1> in cluster <dcc> Done

Job <causal1_9x9_1> was submitted from host <n-62-30-8> by user <s183905> in cluster <dcc> at Thu Mar 18 20:16:26 2021
Job was executed on host(s) <n-62-20-14>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Thu Mar 18 20:16:28 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Mar 18 20:16:28 2021
Terminated at Fri Mar 19 08:11:41 2021
Results reported at Fri Mar 19 08:11:41 2021

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

    CPU time :                                   42800.80 sec.
    Max Memory :                                 2447 MB
    Average Memory :                             2444.63 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               5745.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   42959 sec.
    Turnaround time :                            42915 sec.

The output (if any) is above this job summary.

