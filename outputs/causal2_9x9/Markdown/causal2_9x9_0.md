
# Parameters

    Name :                      causal2_9x9-0
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


      29839268702 function calls (29737541223 primitive calls) in 35709.14 seconds

##    Ordered by: cumulative time
   List reduced from 460 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35709.135 35709.135 {built-in method builtins.exec}
                      1    0.933    0.933 35709.135 35709.135 <string>:1(<module>)
                      1   75.634   75.634 35708.202 35708.202 main.py:13(teleport)
                3633152   13.179    0.000 9798.526    0.003 agent.py:26(learn)
                1816576    6.618    0.000 8626.287    0.005 game.py:27(step)
                3633152  236.852    0.000 8391.280    0.002 learner.py:42(Qlearn)
                1816576    9.197    0.000 8218.550    0.005 layers.py:373(step)
                1816576 4515.985    0.002 8164.133    0.004 replaybuffer.py:27(teleporter_save_data)
                1816576   53.007    0.000 5855.020    0.003 agent.py:50(_learn)
                1816576  143.978    0.000 4913.476    0.003 layers.py:18(step)
                1816576 3474.199    0.002 4755.361    0.003 agent.py:77(interveen)
              181657600  399.718    0.000 4753.901    0.000 layer.py:74(move)
        114442351/12715883  431.706    0.000 4152.408    0.000 module.py:715(_call_impl)
                1816576   46.394    0.000 3923.473    0.002 agent.py:101(_learn)
                9082731   23.271    0.000 3879.931    0.000 network.py:24(forward)
                9082731  105.788    0.000 3803.319    0.000 container.py:115(forward)
                3633152   21.141    0.000 3388.167    0.001 grad_mode.py:23(decorate_context)
                3633152  120.837    0.000 3326.542    0.001 adam.py:55(step)
                1816577  189.432    0.000 3285.059    0.002 layers.py:344(update)
              181657600  497.761    0.000 2863.069    0.000 layers.py:390(check)
              287020148 2854.164    0.000 2854.164    0.000 {built-in method clone}
                3633152  613.288    0.000 2717.027    0.001 functional.py:53(adam)
                3633003   70.563    0.000 2548.283    0.001 agent.py:45(__call__)
                3633152   20.558    0.000 1920.982    0.001 tensor.py:181(backward)
                3633152   13.640    0.000 1900.424    0.001 __init__.py:68(backward)
                3633152 1807.123    0.000 1807.123    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                1816576  643.636    0.000 1497.094    0.001 replaybuffer.py:23(sample_data)
                1816576  733.611    0.000 1454.538    0.001 agent.py:59(modify)
                4700784   42.102    0.000 1427.314    0.000 layers.py:394(restart)
               18165462   31.020    0.000 1399.752    0.000 conv.py:422(forward)
               18165462   35.262    0.000 1356.916    0.000 conv.py:414(_conv_forward)
               18165462 1315.549    0.000 1315.549    0.000 {built-in method conv2d}
               23615041   51.971    0.000 1216.997    0.000 linear.py:92(forward)
              181657600  316.896    0.000 1196.128    0.000 layers.py:384(isFree)
               23615041   89.643    0.000 1141.796    0.000 functional.py:1669(linear)
               16349193  683.463    0.000 1108.023    0.000 layer.py:119(update)
                4700784   19.472    0.000 1051.069    0.000 level.py:8(__init__)
                4700784   58.139    0.000  961.324    0.000 levels.py:151(generate)
             1597353568  685.155    0.000  879.231    0.000 layer.py:71(isFree)
              228888630  530.952    0.000  876.226    0.000 tensor.py:933(grad)
               16349035  862.307    0.000  862.307    0.000 {built-in method cat}
               26323949  192.509    0.000  842.413    0.000 level.py:41(notUsed)
              292469727  811.358    0.000  811.358    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               23615041  799.877    0.000  799.877    0.000 {built-in method addmm}
                1816576   21.345    0.000  791.073    0.000 agent.py:96(__call__)
                5449579   37.529    0.000  773.323    0.000 agent.py:54(modify_board)
                3633152   80.604    0.000  771.697    0.000 optimizer.py:167(zero_grad)
             3090606495  527.728    0.000  757.498    0.000 enum.py:646(__hash__)
                1816576   30.307    0.000  728.717    0.000 replaybuffer.py:19(stacker)
                7535482  572.511    0.000  572.511    0.000 {built-in method tensor}
               65396736  536.458    0.000  536.458    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               32697772   26.661    0.000  530.631    0.000 activation.py:713(forward)
               32697772   42.458    0.000  503.970    0.000 functional.py:1292(leaky_relu)
              188924846   70.449    0.000  498.938    0.000 {built-in method builtins.all}
              181657600  304.615    0.000  494.945    0.000 layers.py:216(check)
                5449579  493.438    0.000  493.438    0.000 {built-in method torch._C._nn.one_hot}
              181657600  295.780    0.000  482.229    0.000 layers.py:230(check)
              181657600  297.310    0.000  475.790    0.000 layers.py:244(check)
                3633152    3.819    0.000  463.249    0.000 game.py:23(board)
               32697772  457.380    0.000  457.380    0.000 {built-in method torch._C._nn.leaky_relu}
              292468912  154.034    0.000  456.829    0.000 overrides.py:1070(has_torch_function)
               65396736  452.907    0.000  452.907    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              582387828  140.902    0.000  445.030    0.000 layers.py:350(<genexpr>)
              181657600  300.551    0.000  412.702    0.000 layers.py:76(check)
             4324302351  387.378    0.000  387.378    0.000 layer.py:67(positions)
               32698368  323.429    0.000  323.429    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               42307056   31.122    0.000  319.911    0.000 layer.py:48(restart)
                1816576  186.437    0.000  318.518    0.000 collector.py:54(collect)
               32698368  291.221    0.000  291.221    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              323350258  118.324    0.000  287.107    0.000 {built-in method builtins.any}
              181657700  189.063    0.000  285.307    0.000 layers.py:110(isDone)
             1254806493  278.345    0.000  278.345    0.000 level.py:32(inverse)
               26323949   18.627    0.000  277.887    0.000 level.py:38(elementsIn)
              735466943  265.678    0.000  265.678    0.000 layer.py:114(elements)
               32698368  263.055    0.000  263.055    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                3633003   96.921    0.000  261.930    0.000 exploration.py:53(softmaxer)
                4700884  120.355    0.000  241.622    0.000 layers.py:33(reset)
              181657600  153.641    0.000  235.727    0.000 layers.py:203(check)
             3090619926  229.772    0.000  229.772    0.000 {built-in method builtins.hash}
               32698368  227.133    0.000  227.133    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              181657600  141.865    0.000  218.845    0.000 layers.py:63(check)
              353714233  149.832    0.000  200.218    0.000 layer.py:98(add)
                7267146   32.704    0.000  195.509    0.000 tensor.py:21(wrapped)
               32698368  180.299    0.000  180.299    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                3633152    4.536    0.000  172.267    0.000 loss.py:445(forward)
                3633152   18.977    0.000  167.731    0.000 functional.py:2637(mse_loss)
               26323949   83.974    0.000  166.950    0.000 level.py:39(<listcomp>)
              615819648  134.239    0.000  166.391    0.000 overrides.py:1083(<genexpr>)
        1568850659/1568850657  109.505    0.000  159.991    0.000 {built-in method builtins.len}
             1597353568  149.721    0.000  149.721    0.000 layer.py:175(isBlocking)
               23615041  147.407    0.000  147.407    0.000 {method 't' of 'torch._C._TensorBase' objects}
              192863096   94.982    0.000  139.086    0.000 layer.py:94(remove)
               10899456  126.666    0.000  126.666    0.000 {built-in method sum}
                1816576   45.051    0.000  121.519    0.000 random.py:315(sample)
                5449728   24.913    0.000  108.194    0.000 tensor.py:506(__rsub__)
               18165462   13.495    0.000   99.500    0.000 flatten.py:39(forward)
                3633152   97.887    0.000   97.887    0.000 {built-in method torch._C._nn.mse_loss}
                5449728   94.817    0.000   94.817    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               26323949   57.820    0.000   92.310    0.000 {built-in method _functools.reduce}
                3633696   91.355    0.000   91.355    0.000 {built-in method max}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-11-15>
Subject: Job 9447206: <causal2_9x9_0> in cluster <dcc> Done

Job <causal2_9x9_0> was submitted from host <n-62-27-21> by user <s183905> in cluster <dcc> at Sun Mar 21 22:24:33 2021
Job was executed on host(s) <n-62-11-15>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sun Mar 21 22:24:33 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun Mar 21 22:24:33 2021
Terminated at Mon Mar 22 08:19:58 2021
Results reported at Mon Mar 22 08:19:58 2021

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

    CPU time :                                   35614.80 sec.
    Max Memory :                                 2445 MB
    Average Memory :                             2435.99 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               5747.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35734 sec.
    Turnaround time :                            35725 sec.

The output (if any) is above this job summary.

