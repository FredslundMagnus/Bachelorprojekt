
# Parameters

    Name :                      teleport_gold-0
    Main :                      teleport
    Hours :                     16.0
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
    Layer gold :                True
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
    Minutes used :              955 minutes.
    Hours used :                15 hours.

# Profiling


      21144562921 function calls (20981083234 primitive calls) in 57291.66 seconds

##    Ordered by: cumulative time
   List reduced from 454 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 57315.948 57315.948 {built-in method builtins.exec}
                      1    0.792    0.792 57315.948 57315.948 <string>:1(<module>)
                      1  115.960  115.960 57315.156 57315.156 main.py:10(teleport)
                5837394   19.044    0.000 19436.755    0.003 agent.py:26(learn)
                2918697  404.343    0.000 17393.915    0.006 collector.py:36(collect)
               14593485 15460.181    0.001 16926.968    0.001 {built-in method builtins.sum}
                5837394  461.653    0.000 16858.726    0.003 learner.py:42(Qlearn)
                2918697   85.308    0.000 11570.181    0.004 agent.py:50(_learn)
                2918697   74.380    0.000 7831.672    0.003 agent.py:101(_learn)
        183836324/20427680  715.628    0.000 7660.273    0.000 module.py:715(_call_impl)
                5837394   32.318    0.000 7222.933    0.001 grad_mode.py:23(decorate_context)
               14590286   35.846    0.000 7180.903    0.000 network.py:24(forward)
                5837394  183.691    0.000 7127.719    0.001 adam.py:55(step)
               14590286  175.464    0.000 7063.330    0.000 container.py:115(forward)
                5837394 1288.938    0.000 6122.875    0.001 functional.py:53(adam)
                2918697   11.338    0.000 5553.912    0.002 game.py:21(step)
                2918697   12.820    0.000 4924.614    0.002 layers.py:212(step)
                5834195  118.238    0.000 4691.323    0.001 agent.py:45(__call__)
                2918697 2035.491    0.001 4379.737    0.002 agent.py:77(interveen)
                2918697 2018.440    0.001 3851.591    0.001 replaybuffer.py:27(teleporter_save_data)
                5837394   35.337    0.000 3820.351    0.001 tensor.py:181(backward)
                5837394   19.167    0.000 3785.014    0.001 __init__.py:68(backward)
                5837394 3618.266    0.001 3618.266    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2918697 1210.992    0.000 2572.086    0.001 agent.py:59(modify)
               29180572   52.466    0.000 2558.766    0.000 conv.py:422(forward)
                2918697  183.987    0.000 2522.119    0.001 layers.py:17(step)
               29180572   58.496    0.000 2488.489    0.000 conv.py:414(_conv_forward)
               29180572 2420.519    0.000 2420.519    0.000 {built-in method conv2d}
                2918698  251.010    0.000 2371.515    0.001 layers.py:192(update)
              291869700  232.046    0.000 2315.123    0.000 layer.py:66(move)
               37933464   83.446    0.000 2305.824    0.000 linear.py:92(forward)
                2918697  955.988    0.000 2265.886    0.001 replaybuffer.py:23(sample_data)
               37933464  139.459    0.000 2186.200    0.000 functional.py:1669(linear)
               37933464 1579.238    0.000 1579.238    0.000 {built-in method addmm}
              367755876  985.080    0.000 1540.740    0.000 tensor.py:933(grad)
               17513348   58.567    0.000 1526.958    0.000 tensor.py:576(__iter__)
                5837394  138.050    0.000 1490.273    0.000 optimizer.py:167(zero_grad)
              107441854 1473.005    0.000 1473.005    0.000 {built-in method clone}
                2918697   36.682    0.000 1433.608    0.000 agent.py:96(__call__)
               17513348 1433.068    0.000 1433.068    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
                8752892   63.169    0.000 1416.494    0.000 agent.py:54(modify_board)
               23346377 1377.018    0.000 1377.018    0.000 {built-in method cat}
              105073092 1287.657    0.000 1287.657    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              291869700  180.629    0.000 1126.272    0.000 layers.py:223(isFree)
                2918697   49.378    0.000 1113.448    0.000 replaybuffer.py:19(stacker)
              105073092 1090.705    0.000 1090.705    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               52523750   42.044    0.000 1043.792    0.000 activation.py:713(forward)
               52523750   64.815    0.000 1001.748    0.000 functional.py:1292(leaky_relu)
              764109657  835.657    0.000  945.642    0.000 layer.py:63(isFree)
               52523750  930.647    0.000  930.647    0.000 {built-in method torch._C._nn.leaky_relu}
                8752892  889.422    0.000  889.422    0.000 {built-in method torch._C._nn.one_hot}
                1467625   11.978    0.000  855.612    0.001 layers.py:233(restart)
               12018081  825.166    0.000  825.166    0.000 {built-in method tensor}
              291869700  299.887    0.000  769.697    0.000 layers.py:229(check)
              469901577  250.327    0.000  727.360    0.000 overrides.py:1070(has_torch_function)
               52536546  707.329    0.000  707.329    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                1467625    2.503    0.000  704.989    0.000 levels.py:8(__init__)
              303545984   83.761    0.000  704.450    0.000 {built-in method builtins.all}
                1467625    6.780    0.000  702.486    0.000 level.py:8(__init__)
                1467625  127.445    0.000  681.456    0.000 levels.py:11(generate)
              881937845  198.510    0.000  646.253    0.000 layers.py:197(<genexpr>)
               52536546  631.250    0.000  631.250    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                5837394    7.021    0.000  626.966    0.000 game.py:17(board)
               52536546  582.568    0.000  582.568    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               52536546  518.866    0.000  518.866    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                5834195  179.950    0.000  499.602    0.000 exploration.py:53(softmaxer)
               11674792  216.097    0.000  497.189    0.000 layer.py:90(update)
              116194746  473.939    0.000  473.939    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              519509830  184.427    0.000  449.884    0.000 {built-in method builtins.any}
               52536546  422.842    0.000  422.842    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              291869800  277.694    0.000  422.553    0.000 layers.py:65(isDone)
              291869700  269.994    0.000  405.493    0.000 layers.py:50(check)
               11676184   52.041    0.000  350.383    0.000 tensor.py:21(wrapped)
                5837394    7.841    0.000  318.791    0.000 loss.py:445(forward)
                5837394   31.391    0.000  310.951    0.000 functional.py:2637(mse_loss)
               37933464  299.921    0.000  299.921    0.000 {method 't' of 'torch._C._TensorBase' objects}
                1467625  150.286    0.000  289.369    0.000 levels.py:76(RFS)
              989412219  211.361    0.000  261.895    0.000 overrides.py:1083(<genexpr>)
                5853947   81.442    0.000  215.806    0.000 random.py:315(sample)
                8756091   42.617    0.000  209.306    0.000 tensor.py:506(__rsub__)
              563390873  206.698    0.000  206.698    0.000 layer.py:85(elements)
               29180572   22.323    0.000  196.242    0.000 flatten.py:39(forward)
                5837394  194.896    0.000  194.896    0.000 {built-in method torch._C._nn.mse_loss}
              687940879  131.456    0.000  186.324    0.000 enum.py:646(__hash__)
                8756091  185.948    0.000  185.948    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
              201349672  181.578    0.000  181.578    0.000 {built-in method torch._C._get_tracing_state}
             2201969044  178.436    0.000  178.436    0.000 layer.py:59(positions)
        502367305/502367303   84.328    0.000  177.630    0.000 {built-in method builtins.len}
                5838268  177.434    0.000  177.434    0.000 {built-in method max}
               29180572  173.919    0.000  173.919    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                8756091  166.688    0.000  166.688    0.000 {built-in method rsub}
                5834195  160.167    0.000  160.167    0.000 {built-in method multinomial}
                5837394  145.482    0.000  145.482    0.000 {built-in method gather}
                5837394   24.563    0.000  142.644    0.000 __init__.py:28(_make_grads)
               52536636   63.551    0.000  139.463    0.000 tensor.py:596(__hash__)
                5870500   12.908    0.000  136.503    0.000 layer.py:40(restart)
              270424444   98.962    0.000  134.645    0.000 layer.py:76(add)
              190194372   79.803    0.000  115.990    0.000 random.py:250(_randbelow_with_getrandbits)
                5837394  113.268    0.000  113.268    0.000 {built-in method ones_like}
                2918698  111.842    0.000  111.842    0.000 {built-in method nonzero}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-2>
Subject: Job 9367048: <teleport_gold_0> in cluster <dcc> Done

Job <teleport_gold_0> was submitted from host <n-62-30-7> by user <s183905> in cluster <dcc> at Sat Mar  6 16:12:40 2021
Job was executed on host(s) <n-62-20-2>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sat Mar  6 16:12:41 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat Mar  6 16:12:41 2021
Terminated at Sun Mar  7 08:08:24 2021
Results reported at Sun Mar  7 08:08:24 2021

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

    CPU time :                                   57122.95 sec.
    Max Memory :                                 2392 MB
    Average Memory :                             2382.05 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               5800.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   57448 sec.
    Turnaround time :                            57344 sec.

The output (if any) is above this job summary.

