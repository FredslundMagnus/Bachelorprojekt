
# Parameters

    Name :                      causal1_good_24h-2
    Main :                      teleport
    Level :                     Levels.Causal1
    Hours :                     24.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Network1 :                  Networks.Teleporter
    K1 :                        5000000
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
    K2 :                        1000000
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
    Layer reddoors :            True
    Layer redkeys :             True
    Layer bluedoors :           True
    Layer bluekeys :            True
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      87651416611 function calls (87448783580 primitive calls) in 86113.03 seconds

##    Ordered by: cumulative time
   List reduced from 480 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86113.027 86113.027 {built-in method builtins.exec}
                      1    1.851    1.851 86113.027 86113.027 <string>:1(<module>)
                      1  175.334  175.334 86111.176 86111.176 main.py:43(teleport)
                3618664   18.682    0.000 26682.459    0.007 game.py:27(step)
                3618664   20.393    0.000 25459.203    0.007 layers.py:475(step)
                7237328   26.937    0.000 24592.973    0.003 agent.py:27(learn)
                7237328  591.034    0.000 21006.575    0.003 learner.py:42(Qlearn)
                3618664  271.545    0.000 17711.473    0.005 layers.py:18(step)
              361866400  841.730    0.000 17409.684    0.000 layer.py:76(move)
                3618664  120.877    0.000 14816.543    0.004 agent.py:52(_learn)
                3618664 7316.587    0.002 13778.154    0.004 replaybuffer.py:29(teleporter_save_data)
              361866400 1922.663    0.000 11857.922    0.000 layers.py:492(check)
                3618664   98.936    0.000 9734.235    0.003 agent.py:113(_learn)
        227961571/25329551  903.104    0.000 9610.441    0.000 module.py:715(_call_impl)
               18092223   45.994    0.000 8992.916    0.000 network.py:24(forward)
                7237328   41.381    0.000 8942.230    0.001 grad_mode.py:23(decorate_context)
                3618664 5925.724    0.002 8879.207    0.002 agent.py:84(interveen)
               18092223  234.861    0.000 8836.753    0.000 container.py:115(forward)
                7237328  239.864    0.000 8820.506    0.001 adam.py:55(step)
                3618665  382.348    0.000 7701.396    0.002 layers.py:446(update)
                7237328 1616.933    0.000 7566.640    0.001 functional.py:53(adam)
                7236231  171.448    0.000 5933.168    0.001 agent.py:47(__call__)
              377992814 5037.019    0.000 5037.019    0.000 {built-in method clone}
                3618664 3155.625    0.001 4993.471    0.001 replaybuffer.py:23(sample_data)
                7237328   45.615    0.000 4798.043    0.001 tensor.py:181(backward)
                7237328   24.256    0.000 4752.429    0.001 __init__.py:68(backward)
                7237328 4544.339    0.001 4544.339    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
              361866400 1086.089    0.000 4134.440    0.000 layers.py:486(isFree)
               65135970 2146.651    0.000 3760.898    0.000 layer.py:121(update)
                3618664 1798.857    0.000 3514.469    0.001 agent.py:65(modify)
               36184446   60.342    0.000 3196.490    0.000 conv.py:422(forward)
               36184446   67.416    0.000 3111.596    0.000 conv.py:414(_conv_forward)
             6189909677 2343.467    0.000 3048.351    0.000 layer.py:73(isFree)
               36184446 3032.439    0.000 3032.439    0.000 {built-in method conv2d}
               47039341  104.009    0.000 2866.271    0.000 linear.py:92(forward)
            12331972189 1999.837    0.000 2829.849    0.000 enum.py:646(__hash__)
               47039341  184.842    0.000 2716.673    0.000 functional.py:1669(linear)
                8586570  125.178    0.000 2435.793    0.000 layers.py:496(restart)
               47039341 1942.566    0.000 1942.566    0.000 {built-in method addmm}
               32566879 1904.900    0.000 1904.900    0.000 {built-in method cat}
              455951718 1223.922    0.000 1896.978    0.000 tensor.py:933(grad)
               15530779 1888.979    0.000 1888.979    0.000 {built-in method tensor}
                3618664   51.046    0.000 1871.499    0.001 agent.py:108(__call__)
                7237328  177.746    0.000 1832.120    0.000 optimizer.py:167(zero_grad)
               10854895   79.787    0.000 1761.035    0.000 agent.py:57(modify_board)
              130271904 1592.444    0.000 1592.444    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                3618664   69.898    0.000 1588.591    0.000 replaybuffer.py:19(stacker)
                7237328   12.549    0.000 1587.245    0.000 game.py:23(board)
                8586570   49.550    0.000 1580.244    0.000 level.py:8(__init__)
              388847709 1523.678    0.000 1523.678    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                8586570   94.999    0.000 1369.424    0.000 levels.py:122(generate)
              130271904 1339.530    0.000 1339.530    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               65131564   51.352    0.000 1316.924    0.000 activation.py:713(forward)
            14516868667 1273.554    0.000 1273.554    0.000 layer.py:69(positions)
               65131564   84.974    0.000 1265.572    0.000 functional.py:1292(leaky_relu)
               33486262  246.387    0.000 1190.323    0.000 level.py:41(notUsed)
               65131564 1172.268    0.000 1172.268    0.000 {built-in method torch._C._nn.leaky_relu}
               10854895 1105.642    0.000 1105.642    0.000 {built-in method torch._C._nn.one_hot}
             1478161289 1024.133    0.000 1024.133    0.000 layer.py:116(elements)
              379961726  121.486    0.000 1007.804    0.000 {built-in method builtins.all}
              361866400  620.303    0.000  974.064    0.000 layers.py:173(check)
              361866400  581.144    0.000  923.647    0.000 layers.py:302(check)
              361866400  564.264    0.000  916.096    0.000 layers.py:230(check)
             1223401500  287.388    0.000  914.890    0.000 layers.py:452(<genexpr>)
              361866400  573.773    0.000  906.261    0.000 layers.py:261(check)
              361866400  565.506    0.000  902.707    0.000 layers.py:244(check)
              361866400  565.006    0.000  902.520    0.000 layers.py:216(check)
              586221604  307.699    0.000  897.178    0.000 overrides.py:1070(has_torch_function)
               65135952  865.549    0.000  865.549    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                3618664  502.489    0.000  840.380    0.000 collector.py:54(collect)
            12331998580  830.016    0.000  830.016    0.000 {built-in method builtins.hash}
              361866400  586.095    0.000  802.594    0.000 layers.py:76(check)
               65135952  778.532    0.000  778.532    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               18095226   94.565    0.000  748.237    0.000 tensor.py:21(wrapped)
               65135952  715.577    0.000  715.577    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              154558260  103.112    0.000  686.734    0.000 layer.py:50(restart)
                7236231  229.192    0.000  640.558    0.000 exploration.py:53(softmaxer)
               65135952  638.174    0.000  638.174    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              361866400  389.074    0.000  597.377    0.000 layers.py:142(check)
              361866500  383.362    0.000  568.367    0.000 layers.py:110(isDone)
              361866400  368.293    0.000  562.517    0.000 layers.py:328(check)
              647735602  227.563    0.000  558.007    0.000 {built-in method builtins.any}
              361866400  357.079    0.000  554.414    0.000 layers.py:287(check)
               65135952  507.718    0.000  507.718    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              361866400  309.468    0.000  463.865    0.000 layers.py:47(check)
              361866400  302.856    0.000  459.399    0.000 layers.py:123(check)
             5156772137  458.851    0.000  458.851    0.000 layer.py:177(isBlocking)
              361866400  288.970    0.000  438.358    0.000 layers.py:63(check)
        5308920042/5308920040  319.647    0.000  430.770    0.000 {built-in method builtins.len}
               33486262   23.830    0.000  423.581    0.000 level.py:38(elementsIn)
              361866400  277.835    0.000  420.618    0.000 layers.py:203(check)
                8586670  205.839    0.000  415.740    0.000 layers.py:33(reset)
                7237328   10.517    0.000  409.046    0.000 loss.py:445(forward)
                7237328   41.135    0.000  398.530    0.000 functional.py:2637(mse_loss)
             1544627621  386.387    0.000  386.387    0.000 level.py:32(inverse)
               47039341  384.857    0.000  384.857    0.000 {method 't' of 'torch._C._TensorBase' objects}
              678083927  262.804    0.000  354.922    0.000 layer.py:100(add)
               21711984  335.578    0.000  335.578    0.000 {built-in method sum}
             1237577052  261.745    0.000  326.004    0.000 overrides.py:1083(<genexpr>)
              356487509  202.211    0.000  281.688    0.000 layer.py:96(remove)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-6>
Subject: Job 9474546: <causal1_good_24h_2> in cluster <dcc> Done

Job <causal1_good_24h_2> was submitted from host <n-62-27-21> by user <s183905> in cluster <dcc> at Sun Mar 28 11:07:12 2021
Job was executed on host(s) <n-62-20-6>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sun Mar 28 11:07:13 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun Mar 28 11:07:13 2021
Terminated at Mon Mar 29 11:02:39 2021
Results reported at Mon Mar 29 11:02:39 2021

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
#BSUB -W 1440
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $LSB_PROJECT_NAME


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   85890.95 sec.
    Max Memory :                                 2820 MB
    Average Memory :                             2802.21 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13564.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86150 sec.
    Turnaround time :                            86127 sec.

The output (if any) is above this job summary.

