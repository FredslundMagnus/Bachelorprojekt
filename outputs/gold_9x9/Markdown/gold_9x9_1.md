
# Parameters

    Name :                      gold_9x9-1
    Main :                      teleport
    Hours :                     24.0
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
    Layer keys :                False
    Layer door :                False
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
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      48521657202 function calls (48242167443 primitive calls) in 86000.17 seconds

##    Ordered by: cumulative time
   List reduced from 460 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86110.804 86110.804 {built-in method builtins.exec}
                      1    0.757    0.757 86110.804 86110.804 <string>:1(<module>)
                      1  199.260  199.260 86110.046 86110.046 main.py:10(teleport)
                9981888   34.152    0.000 32841.774    0.003 agent.py:26(learn)
                9981888  787.019    0.000 28508.552    0.003 learner.py:42(Qlearn)
                4990944  144.229    0.000 19552.153    0.004 agent.py:50(_learn)
                4990944 8114.727    0.002 15346.239    0.003 replaybuffer.py:27(teleporter_save_data)
                4990944   20.682    0.000 13428.534    0.003 game.py:25(step)
                4990944  128.681    0.000 13236.162    0.003 agent.py:101(_learn)
        314425013/34936265 1202.042    0.000 12917.231    0.000 module.py:715(_call_impl)
                4990944   26.278    0.000 12441.179    0.002 layers.py:295(step)
                9981888   60.064    0.000 12215.097    0.001 grad_mode.py:23(decorate_context)
               24954377   62.918    0.000 12096.164    0.000 network.py:24(forward)
                9981888  317.531    0.000 12048.661    0.001 adam.py:55(step)
               24954377  304.093    0.000 11889.018    0.000 container.py:115(forward)
                4990944 7842.010    0.002 11789.052    0.002 agent.py:77(interveen)
                9981888 2194.331    0.000 10324.446    0.001 functional.py:53(adam)
                9981545  200.049    0.000 7897.099    0.001 agent.py:45(__call__)
                4990945  488.966    0.000 7647.652    0.002 layers.py:266(update)
                9981888   60.870    0.000 6440.089    0.001 tensor.py:181(backward)
                9981888   34.072    0.000 6379.220    0.001 __init__.py:68(backward)
                9981888 6094.139    0.001 6094.139    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
              423090573 5633.032    0.000 5633.032    0.000 {built-in method clone}
                4990944  347.450    0.000 4737.890    0.001 layers.py:19(step)
                4990944 2358.731    0.000 4654.659    0.001 agent.py:59(modify)
              499094400  536.619    0.000 4347.182    0.000 layer.py:70(move)
               49908754   81.741    0.000 4273.740    0.000 conv.py:422(forward)
               49908754   92.329    0.000 4159.789    0.000 conv.py:414(_conv_forward)
               10734128   81.961    0.000 4144.916    0.000 layers.py:316(restart)
               49908754 4049.582    0.000 4049.582    0.000 {built-in method conv2d}
               64881243  152.325    0.000 3903.404    0.000 linear.py:92(forward)
                4990944 1614.145    0.000 3825.477    0.001 replaybuffer.py:23(sample_data)
               64881243  244.999    0.000 3685.642    0.000 functional.py:1669(linear)
               10734128   15.119    0.000 3304.890    0.000 levels.py:8(__init__)
               10734128   38.593    0.000 3289.770    0.000 level.py:8(__init__)
               10734128  540.448    0.000 3139.032    0.000 levels.py:11(generate)
               64881243 2641.208    0.000 2641.208    0.000 {built-in method addmm}
              628858998 1703.542    0.000 2637.195    0.000 tensor.py:933(grad)
                9981888  241.715    0.000 2531.648    0.000 optimizer.py:167(zero_grad)
                4990944   60.257    0.000 2465.930    0.000 agent.py:96(__call__)
               14972489  101.810    0.000 2380.360    0.000 agent.py:54(modify_board)
               39927209 2323.604    0.000 2323.604    0.000 {built-in method cat}
              179673984 2149.923    0.000 2149.923    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              499094400  391.805    0.000 1975.760    0.000 layers.py:306(isFree)
                4990944   82.576    0.000 1879.951    0.000 replaybuffer.py:19(stacker)
              179673984 1845.614    0.000 1845.614    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               89835620   70.963    0.000 1764.934    0.000 activation.py:713(forward)
              438063062 1747.821    0.000 1747.821    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               89835620  115.462    0.000 1693.971    0.000 functional.py:1292(leaky_relu)
               19963780  991.688    0.000 1608.623    0.000 layer.py:132(NoRock_update)
             1798279053 1336.683    0.000 1583.955    0.000 layer.py:67(isFree)
               89835620 1567.738    0.000 1567.738    0.000 {built-in method torch._C._nn.leaky_relu}
               14972489 1494.242    0.000 1494.242    0.000 {built-in method torch._C._nn.one_hot}
              499094400  497.065    0.000 1323.213    0.000 layers.py:312(check)
               10734128  696.467    0.000 1320.008    0.000 levels.py:77(RFS)
               21043077 1249.190    0.000 1249.190    0.000 {built-in method tensor}
              519060392  146.271    0.000 1244.371    0.000 {built-in method builtins.all}
              803542217  420.960    0.000 1227.472    0.000 overrides.py:1070(has_torch_function)
               89836992 1192.479    0.000 1192.479    0.000 {method 'add' of 'torch._C._TensorBase' objects}
             1518632257  340.297    0.000 1138.945    0.000 layers.py:272(<genexpr>)
                4990944  680.724    0.000 1138.004    0.000 collector.py:37(collect)
               89836992 1051.958    0.000 1051.958    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               89836992  985.176    0.000  985.176    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                9981888   11.194    0.000  890.419    0.000 game.py:21(board)
               89836992  876.820    0.000  876.820    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                9981545  303.895    0.000  845.234    0.000 exploration.py:53(softmaxer)
              888387237  310.024    0.000  761.884    0.000 {built-in method builtins.any}
              499094500  492.981    0.000  754.082    0.000 layers.py:111(isDone)
               42936512   72.957    0.000  742.435    0.000 layer.py:44(restart)
              499094400  463.662    0.000  716.967    0.000 layers.py:48(check)
               89836992  701.189    0.000  701.189    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               19965892   92.708    0.000  602.445    0.000 tensor.py:21(wrapped)
                9981888   14.768    0.000  545.082    0.000 loss.py:445(forward)
                9981888   51.722    0.000  530.315    0.000 functional.py:2637(mse_loss)
               64881243  515.616    0.000  515.616    0.000 {method 't' of 'torch._C._TensorBase' objects}
               10734228  256.907    0.000  505.734    0.000 layers.py:34(reset)
             1023441791  367.534    0.000  499.803    0.000 layer.py:94(add)
               26459200  189.346    0.000  479.408    0.000 random.py:315(sample)
               29945664  451.456    0.000  451.456    0.000 {built-in method sum}
             1691930571  357.189    0.000  445.221    0.000 overrides.py:1083(<genexpr>)
             1663704840  314.215    0.000  444.692    0.000 enum.py:646(__hash__)
               10734128   67.225    0.000  432.953    0.000 level.py:41(notUsed)
             2076984223  403.353    0.000  403.353    0.000 layer.py:110(elements)
        2947466265/2947466263  242.739    0.000  387.901    0.000 {built-in method builtins.len}
               14972832   73.868    0.000  358.968    0.000 tensor.py:506(__rsub__)
             3937456679  340.579    0.000  340.579    0.000 layer.py:63(positions)
               49908754   36.130    0.000  333.416    0.000 flatten.py:39(forward)
                9981888  330.785    0.000  330.785    0.000 {built-in method torch._C._nn.mse_loss}
              525972272  320.249    0.000  320.249    0.000 level.py:32(inverse)
               14972832  313.503    0.000  313.503    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
              644047680  208.218    0.000  312.757    0.000 levels.py:33(<genexpr>)
              476265500  209.057    0.000  306.388    0.000 random.py:250(_randbelow_with_getrandbits)
              462571487  202.834    0.000  300.442    0.000 layer.py:90(remove)
               49908754  297.286    0.000  297.286    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                9983385  296.746    0.000  296.746    0.000 {built-in method max}
               14972832  285.100    0.000  285.100    0.000 {built-in method rsub}
                9981545  273.560    0.000  273.560    0.000 {built-in method multinomial}
              319417953  272.993    0.000  272.993    0.000 {built-in method torch._C._get_tracing_state}
             3387357724  245.109    0.000  245.109    0.000 {method 'append' of 'list' objects}
                9981888  244.658    0.000  244.658    0.000 {built-in method gather}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-6>
Subject: Job 9418586: <gold_9x9_1> in cluster <dcc> Done

Job <gold_9x9_1> was submitted from host <n-62-30-2> by user <s183905> in cluster <dcc> at Tue Mar 16 21:35:11 2021
Job was executed on host(s) <n-62-20-6>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Tue Mar 16 21:35:12 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue Mar 16 21:35:12 2021
Terminated at Wed Mar 17 21:30:36 2021
Results reported at Wed Mar 17 21:30:36 2021

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

    CPU time :                                   85890.68 sec.
    Max Memory :                                 2389 MB
    Average Memory :                             2384.33 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               5803.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86140 sec.
    Turnaround time :                            86125 sec.

The output (if any) is above this job summary.

