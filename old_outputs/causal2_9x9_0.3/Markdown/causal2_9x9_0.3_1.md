
# Parameters

    Name :                      causal2_9x9_0.3-1
    Main :                      teleport
    Level :                     Levels.Causal2
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
    Layer gold :                False
    Layer keys :                False
    Layer door :                False
    Layer holder :              False
    Layer putter :              False
    Layer rock :                True
    Layer dirt :                True
    Layer diamond1 :            True
    Layer diamond2 :            True
    Layer diamond3 :            True
    Layer diamond4 :            True
    K :                         200000
    Epsilon cap :               0.1
    Softmax cap :               0.02
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


      26660890643 function calls (26574095296 primitive calls) in 35711.18 seconds

##    Ordered by: cumulative time
   List reduced from 460 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35711.176 35711.176 {built-in method builtins.exec}
                      1    0.916    0.916 35711.176 35711.176 <string>:1(<module>)
                      1   67.325   67.325 35710.260 35710.260 main.py:13(teleport)
                3099850   11.535    0.000 10307.190    0.003 agent.py:26(learn)
                3099850  242.166    0.000 8952.126    0.003 learner.py:42(Qlearn)
                1549925 4654.585    0.003 8731.802    0.006 replaybuffer.py:27(teleporter_save_data)
                1549925    6.447    0.000 7502.143    0.005 game.py:27(step)
                1549925    7.185    0.000 7123.436    0.005 layers.py:373(step)
                1549925   46.623    0.000 6130.768    0.004 agent.py:50(_learn)
                1549925 3713.716    0.002 4956.460    0.003 agent.py:77(interveen)
                1549925   40.912    0.000 4158.051    0.003 agent.py:101(_learn)
                1549925  107.604    0.000 4067.678    0.003 layers.py:18(step)
        97643689/10849353  386.820    0.000 4038.949    0.000 module.py:715(_call_impl)
              154992500  328.635    0.000 3947.831    0.000 layer.py:74(move)
                3099850   18.358    0.000 3825.289    0.001 grad_mode.py:23(decorate_context)
                7749503   20.111    0.000 3784.006    0.000 network.py:24(forward)
                3099850   98.317    0.000 3772.888    0.001 adam.py:55(step)
                7749503   97.470    0.000 3716.430    0.000 container.py:115(forward)
                3099850  687.946    0.000 3231.550    0.001 functional.py:53(adam)
              241851418 3138.980    0.000 3138.980    0.000 {built-in method clone}
                1549926  155.777    0.000 3039.456    0.002 layers.py:344(update)
                3099728   64.730    0.000 2473.608    0.001 agent.py:45(__call__)
              154992500  404.947    0.000 2369.008    0.000 layers.py:390(check)
                3099850   20.913    0.000 2055.301    0.001 tensor.py:181(backward)
                3099850   11.319    0.000 2034.388    0.001 __init__.py:68(backward)
                3099850 1945.006    0.001 1945.006    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                1549925  804.098    0.001 1513.287    0.001 agent.py:59(modify)
                5639441   45.978    0.000 1450.123    0.000 layers.py:394(restart)
               15499006   25.678    0.000 1337.445    0.000 conv.py:422(forward)
                1549925  539.758    0.000 1307.017    0.001 replaybuffer.py:23(sample_data)
               15499006   31.711    0.000 1302.196    0.000 conv.py:414(_conv_forward)
               15499006 1265.586    0.000 1265.586    0.000 {built-in method conv2d}
               20148659   45.083    0.000 1205.174    0.000 linear.py:92(forward)
               20148659   77.192    0.000 1141.315    0.000 functional.py:1669(linear)
                5639441   22.174    0.000 1028.967    0.000 level.py:8(__init__)
              154992500  261.115    0.000 1014.102    0.000 layers.py:384(isFree)
               13949334  616.668    0.000  973.741    0.000 layer.py:119(update)
              246501071  968.817    0.000  968.817    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                5639441   58.655    0.000  928.020    0.000 levels.py:151(generate)
              195290604  537.489    0.000  833.541    0.000 tensor.py:933(grad)
               20148659  815.367    0.000  815.367    0.000 {built-in method addmm}
               27068964  183.697    0.000  808.483    0.000 level.py:41(notUsed)
               13949203  800.647    0.000  800.647    0.000 {built-in method cat}
                3099850   74.731    0.000  796.546    0.000 optimizer.py:167(zero_grad)
                1549925   19.044    0.000  763.507    0.000 agent.py:96(__call__)
             1363194044  580.167    0.000  752.986    0.000 layer.py:71(isFree)
                4649653   31.342    0.000  737.740    0.000 agent.py:54(modify_board)
             2770980878  460.892    0.000  674.257    0.000 enum.py:646(__hash__)
               55797300  671.897    0.000  671.897    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                1549925   27.754    0.000  662.978    0.000 replaybuffer.py:19(stacker)
               55797300  572.352    0.000  572.352    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               27898162   22.121    0.000  556.089    0.000 activation.py:713(forward)
               27898162   35.876    0.000  533.968    0.000 functional.py:1292(leaky_relu)
                6440010  524.761    0.000  524.761    0.000 {built-in method tensor}
               27898162  494.650    0.000  494.650    0.000 {built-in method torch._C._nn.leaky_relu}
                4649653  461.660    0.000  461.660    0.000 {built-in method torch._C._nn.one_hot}
                3099850    3.635    0.000  414.092    0.000 game.py:23(board)
              161193014   50.152    0.000  409.373    0.000 {built-in method builtins.all}
              154992500  251.732    0.000  407.145    0.000 layers.py:216(check)
              154992500  243.066    0.000  400.152    0.000 layers.py:230(check)
              154992500  240.271    0.000  393.647    0.000 layers.py:244(check)
              249538108  134.572    0.000  388.694    0.000 overrides.py:1070(has_torch_function)
               27898650  383.345    0.000  383.345    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              508320502  117.789    0.000  372.999    0.000 layers.py:350(<genexpr>)
               50754969   34.248    0.000  359.256    0.000 layer.py:48(restart)
                1549925  211.216    0.000  354.772    0.000 collector.py:54(collect)
              154992500  250.287    0.000  345.853    0.000 layers.py:76(check)
               27898650  328.953    0.000  328.953    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
             3692638137  320.909    0.000  320.909    0.000 layer.py:67(positions)
               27898650  303.209    0.000  303.209    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               27898650  274.705    0.000  274.705    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                5639541  136.658    0.000  274.627    0.000 layers.py:33(reset)
               27068964   17.361    0.000  272.070    0.000 level.py:38(elementsIn)
                3099728   95.351    0.000  265.053    0.000 exploration.py:53(softmaxer)
             1299650273  261.963    0.000  261.963    0.000 level.py:32(inverse)
              275886468   97.936    0.000  240.259    0.000 {built-in method builtins.any}
              154992600  154.191    0.000  236.795    0.000 layers.py:110(isDone)
              739400253  227.671    0.000  227.671    0.000 layer.py:114(elements)
               27898650  218.088    0.000  218.088    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
             2770992365  213.367    0.000  213.367    0.000 {built-in method builtins.hash}
              154992500  126.552    0.000  195.776    0.000 layers.py:203(check)
              358559469  139.636    0.000  186.574    0.000 layer.py:98(add)
                6200414   27.817    0.000  184.853    0.000 tensor.py:21(wrapped)
              154992500  117.456    0.000  183.197    0.000 layers.py:63(check)
                3099850    4.155    0.000  167.842    0.000 loss.py:445(forward)
               27068964   81.863    0.000  163.933    0.000 level.py:39(<listcomp>)
                3099850   16.577    0.000  163.687    0.000 functional.py:2637(mse_loss)
               20148659  158.724    0.000  158.724    0.000 {method 't' of 'torch._C._TensorBase' objects}
                9299550  141.491    0.000  141.491    0.000 {built-in method sum}
        1347832663/1347832661   94.725    0.000  140.762    0.000 {built-in method builtins.len}
              525424980  112.153    0.000  140.431    0.000 overrides.py:1083(<genexpr>)
             1363194044  136.022    0.000  136.022    0.000 layer.py:175(isBlocking)
                4649775   22.414    0.000  111.455    0.000 tensor.py:506(__rsub__)
              161753955   73.672    0.000  106.832    0.000 layer.py:94(remove)
                3099850  102.555    0.000  102.555    0.000 {built-in method torch._C._nn.mse_loss}
               15499006   11.055    0.000  101.658    0.000 flatten.py:39(forward)
                1549925   37.646    0.000  101.538    0.000 random.py:315(sample)
                4649775   96.706    0.000   96.706    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                3100313   92.269    0.000   92.269    0.000 {built-in method max}
               27068964   56.351    0.000   90.776    0.000 {built-in method _functools.reduce}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-7>
Subject: Job 9447954: <causal2_9x9_0.3_1> in cluster <dcc> Done

Job <causal2_9x9_0.3_1> was submitted from host <n-62-30-1> by user <s183905> in cluster <dcc> at Mon Mar 22 13:28:55 2021
Job was executed on host(s) <n-62-20-7>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Mon Mar 22 13:28:57 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Mar 22 13:28:57 2021
Terminated at Mon Mar 22 23:24:14 2021
Results reported at Mon Mar 22 23:24:14 2021

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

    CPU time :                                   35682.61 sec.
    Max Memory :                                 2452 MB
    Average Memory :                             2446.49 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               5740.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35778 sec.
    Turnaround time :                            35719 sec.

The output (if any) is above this job summary.

