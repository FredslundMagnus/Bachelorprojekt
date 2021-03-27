/zhome/ea/9/137501/.lsbatch/1616691068.9465581.shell: line 14:  1022 Killed                  python main.py $LSB_PROJECT_NAME

------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-10>
Subject: Job 9465581: <causal3_9x9_20hoursONLYMOVERepsgreed_0> in cluster <dcc> Exited

Job <causal3_9x9_20hoursONLYMOVERepsgreed_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Thu Mar 25 17:51:08 2021
Job was executed on host(s) <n-62-20-10>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Thu Mar 25 17:51:09 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Mar 25 17:51:09 2021
Terminated at Fri Mar 26 10:26:43 2021
Results reported at Fri Mar 26 10:26:43 2021

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

TERM_MEMLIMIT: job killed after reaching LSF memory usage limit.
Exited with exit code 137.

Resource usage summary:

    CPU time :                                   59590.00 sec.
    Max Memory :                                 8192 MB
    Average Memory :                             5272.51 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               0.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   59840 sec.
    Turnaround time :                            59735 sec.

The output (if any) is above this job summary.


# Parameters

    Name :                      causal3_9x9_20hoursONLYMOVERepsgreed-0
    Main :                      simple
    Level :                     Levels.Causal3
    Hours :                     12.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Network1 :                  Networks.Teleporter
    K1 :                        5000000
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
    K2 :                        5000000.0
    Learner2 :                  Learners.Qlearn
    Exploration2 :              Explorations.epsilonGreedy
    Gamma2 :                    0.98
    Layer blocks :              True
    Layer goal :                True
    Layer gold :                True
    Layer keys :                False
    Layer door :                False
    Layer holder :              False
    Layer putter :              False
    Layer rock :                False
    Layer dirt :                True
    Layer diamond1 :            False
    Layer diamond2 :            False
    Layer diamond3 :            False
    Layer diamond4 :            False
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
    Minutes used :              715 minutes.
    Hours used :                11 hours.

# Profiling


      71578177527 function calls (71420902780 primitive calls) in 42909.13 seconds

##    Ordered by: cumulative time
   List reduced from 417 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 42909.133 42909.133 {built-in method builtins.exec}
                      1    0.002    0.002 42909.133 42909.133 <string>:1(<module>)
                      1  103.134  103.134 42909.131 42909.131 main.py:64(simple)
                6553099   22.173    0.000 24846.331    0.004 game.py:27(step)
                6553099   30.401    0.000 23374.586    0.004 layers.py:475(step)
                6553099  485.118    0.000 14635.282    0.002 layers.py:18(step)
              655309900  695.593    0.000 14094.616    0.000 layer.py:76(move)
                6553099   19.904    0.000 13510.533    0.002 agent.py:27(learn)
                6553099  189.528    0.000 13475.306    0.002 agent.py:113(_learn)
                6553099  394.300    0.000 13285.778    0.002 learner.py:42(Qlearn)
              655309900 1680.376    0.000 9791.897    0.000 layers.py:492(check)
                6553100  661.902    0.000 8668.218    0.001 layers.py:446(update)
        176933673/19659297  694.939    0.000 5764.036    0.000 module.py:866(_call_impl)
               13106198   32.420    0.000 5309.441    0.000 network.py:24(forward)
                6553099   52.431    0.000 5196.257    0.001 optimizer.py:84(wrapper)
               13106198  172.293    0.000 5191.750    0.000 container.py:117(forward)
                6553099   29.725    0.000 4959.218    0.001 grad_mode.py:24(decorate_context)
                6553099  190.379    0.000 4868.924    0.001 adam.py:55(step)
                6553099 1014.949    0.000 4443.654    0.001 _functional.py:53(adam)
                6553099   23.684    0.000 3337.014    0.001 tensor.py:195(backward)
                6553099   26.258    0.000 3312.415    0.001 __init__.py:68(backward)
              655309900  702.486    0.000 3209.249    0.000 layers.py:486(isFree)
               58977900 1740.168    0.000 3193.400    0.000 layer.py:137(NoRock_update)
                6553099 3157.793    0.000 3157.793    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                6553099   89.070    0.000 3155.415    0.000 agent.py:108(__call__)
               10909090   94.408    0.000 2907.451    0.000 layers.py:496(restart)
             3100332450 1997.782    0.000 2506.763    0.000 layer.py:73(isFree)
             9784998184 1671.552    0.000 2389.542    0.000 enum.py:646(__hash__)
               29136862 2135.948    0.000 2135.948    0.000 {built-in method tensor}
              655309900 1236.887    0.000 1963.957    0.000 layers.py:302(check)
               26212396   59.572    0.000 1899.743    0.000 conv.py:398(forward)
              655309900 1175.131    0.000 1890.064    0.000 layers.py:261(check)
               10909090   42.745    0.000 1871.179    0.000 level.py:8(__init__)
               26212396   39.446    0.000 1815.098    0.000 conv.py:390(_conv_forward)
               26212396 1775.652    0.000 1775.652    0.000 {built-in method conv2d}
               13106198   11.558    0.000 1675.177    0.000 game.py:23(board)
              655310000  184.959    0.000 1649.271    0.000 {built-in method builtins.all}
               10909090  267.487    0.000 1640.072    0.000 levels.py:163(generate)
             1976408481  467.189    0.000 1541.421    0.000 layers.py:452(<genexpr>)
               39318594   82.775    0.000 1510.812    0.000 linear.py:93(forward)
               39318594   32.576    0.000 1390.548    0.000 functional.py:1737(linear)
               39318594 1349.922    0.000 1349.922    0.000 {built-in method torch._C._nn.linear}
            12073622624 1133.867    0.000 1133.867    0.000 layer.py:69(positions)
              655309900  803.256    0.000 1133.822    0.000 layers.py:63(check)
               21818180  127.419    0.000 1106.777    0.000 level.py:41(notUsed)
              655309900  703.830    0.000 1099.783    0.000 layers.py:328(check)
              655310000  662.020    0.000 1017.399    0.000 layers.py:110(isDone)
              655309900  633.519    0.000 1001.758    0.000 layers.py:287(check)
               98181810  121.794    0.000  910.135    0.000 layer.py:50(restart)
              131061980  859.162    0.000  859.162    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              655309900  566.679    0.000  856.100    0.000 layers.py:47(check)
             2153389907  831.234    0.000  831.234    0.000 layer.py:116(elements)
                6553099  136.417    0.000  786.907    0.000 optimizer.py:189(zero_grad)
              131061980  779.024    0.000  779.024    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               52424792   43.285    0.000  764.830    0.000 activation.py:713(forward)
               52424792   41.913    0.000  721.545    0.000 functional.py:1364(leaky_relu)
             9785024493  717.994    0.000  717.994    0.000 {built-in method builtins.hash}
               52424792  670.588    0.000  670.588    0.000 {built-in method torch._C._nn.leaky_relu}
              453828437  574.112    0.000  574.112    0.000 level.py:32(inverse)
               10909190  274.539    0.000  544.049    0.000 layers.py:33(reset)
             1018818521  388.231    0.000  525.820    0.000 layer.py:100(add)
               65530990  503.757    0.000  503.757    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                6553099  275.029    0.000  476.968    0.000 collector.py:54(collect)
               65530990  443.963    0.000  443.963    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               65530990  414.272    0.000  414.272    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               65530990  410.658    0.000  410.658    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                6553099   26.664    0.000  377.180    0.000 exploration.py:47(epsilonGreedy)
        5890407318/5890407317  350.679    0.000  375.398    0.000 {built-in method builtins.len}
              458716960  298.055    0.000  372.432    0.000 tensor.py:906(grad)
               21818180   17.642    0.000  312.532    0.000 level.py:38(elementsIn)
               65530990  312.449    0.000  312.449    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                6553099    9.943    0.000  281.710    0.000 loss.py:527(forward)
             2471785547  274.070    0.000  274.070    0.000 layer.py:177(isBlocking)
                6553099   25.767    0.000  271.766    0.000 functional.py:2898(mse_loss)
              328378500  162.063    0.000  243.316    0.000 layer.py:96(remove)
             3045005933  223.751    0.000  223.751    0.000 {method 'append' of 'list' objects}
                6553099  206.725    0.000  206.725    0.000 {method 'tolist' of 'torch._C._TensorBase' objects}
               58977900  195.457    0.000  195.457    0.000 layer.py:148(<listcomp>)
               58977900  178.712    0.000  178.712    0.000 layer.py:149(<listcomp>)
               21818180   88.756    0.000  176.865    0.000 level.py:39(<listcomp>)
                6553099  166.718    0.000  166.718    0.000 {built-in method torch._C._nn.mse_loss}
             1965929700  166.037    0.000  166.037    0.000 layer.py:59(check)
               13106198  165.001    0.000  165.001    0.000 {built-in method sum}
                2911366   69.525    0.000  161.058    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               10909090   71.262    0.000  157.597    0.000 level.py:16(<dictcomp>)
                6553754  148.721    0.000  148.721    0.000 {built-in method max}
               21818180   55.433    0.000  135.219    0.000 random.py:315(sample)
               26212396   18.370    0.000  125.298    0.000 flatten.py:39(forward)
                6553099   25.413    0.000  122.568    0.000 __init__.py:28(_make_grads)
                6553099  121.485    0.000  121.485    0.000 {built-in method gather}
               21818180   68.877    0.000  118.025    0.000 {built-in method _functools.reduce}
               13106198   25.918    0.000  114.738    0.000 profiler.py:615(__enter__)
              621818141  114.025    0.000  114.025    0.000 enum.py:352(<genexpr>)
              894554318  108.090    0.000  108.090    0.000 layer.py:152(grid)
               26212396  106.928    0.000  106.928    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              176933673  101.908    0.000  101.908    0.000 {built-in method torch._C._get_tracing_state}
               63472080   39.271    0.000  101.402    0.000 random.py:285(choice)
               13106198   16.536    0.000   99.336    0.000 profiler.py:607(__init__)
              107165877   66.823    0.000   95.028    0.000 random.py:250(_randbelow_with_getrandbits)
                5822732    6.426    0.000   91.532    0.000 <__array_function__ internals>:2(prod)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-11>
Subject: Job 9470147: <causal3_9x9_20hoursONLYMOVERepsgreed_0> in cluster <dcc> Done

Job <causal3_9x9_20hoursONLYMOVERepsgreed_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Fri Mar 26 13:30:13 2021
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Fri Mar 26 13:30:13 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Fri Mar 26 13:30:13 2021
Terminated at Sat Mar 27 01:25:31 2021
Results reported at Sat Mar 27 01:25:31 2021

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

    CPU time :                                   42803.25 sec.
    Max Memory :                                 6754 MB
    Average Memory :                             4594.70 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               9630.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   42936 sec.
    Turnaround time :                            42918 sec.

The output (if any) is above this job summary.

