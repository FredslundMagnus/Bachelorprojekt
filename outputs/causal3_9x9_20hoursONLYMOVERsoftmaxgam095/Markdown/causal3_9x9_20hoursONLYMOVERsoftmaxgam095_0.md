
# Parameters

    Name :                      causal3_9x9_20hoursONLYMOVERsoftmaxgam095-0
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
    Exploration2 :              Explorations.softmaxer
    Gamma2 :                    0.95
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


      75560165657 function calls (75384419862 primitive calls) in 42909.18 seconds

##    Ordered by: cumulative time
   List reduced from 443 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 42909.177 42909.177 {built-in method builtins.exec}
                      1    0.001    0.001 42909.177 42909.177 <string>:1(<module>)
                      1  109.014  109.014 42909.175 42909.175 main.py:64(simple)
                7322726   24.697    0.000 23922.709    0.003 game.py:27(step)
                7322726   34.647    0.000 22365.452    0.003 layers.py:475(step)
                7322726  500.764    0.000 16540.423    0.002 layers.py:18(step)
              732272600  802.598    0.000 15982.466    0.000 layer.py:76(move)
                7322726   21.451    0.000 14177.253    0.002 agent.py:27(learn)
                7322726  191.176    0.000 14139.797    0.002 agent.py:113(_learn)
                7322726  411.398    0.000 13948.621    0.002 learner.py:42(Qlearn)
              732272600 1714.889    0.000 10272.546    0.000 layers.py:492(check)
        197713602/21968178  723.180    0.000 5974.820    0.000 module.py:866(_call_impl)
                7322727  657.112    0.000 5749.043    0.001 layers.py:446(update)
               14645452   33.345    0.000 5509.524    0.000 network.py:24(forward)
                7322726   55.507    0.000 5493.388    0.001 optimizer.py:84(wrapper)
               14645452  175.938    0.000 5388.421    0.000 container.py:117(forward)
                7322726   28.517    0.000 5234.871    0.001 grad_mode.py:24(decorate_context)
                7322726  198.038    0.000 5141.116    0.001 adam.py:55(step)
                7322726 1066.662    0.000 4694.433    0.001 _functional.py:53(adam)
              732272600 1005.054    0.000 4260.808    0.000 layers.py:486(isFree)
                7322726   26.173    0.000 3541.870    0.000 tensor.py:195(backward)
                7322726   26.965    0.000 3514.759    0.000 __init__.py:68(backward)
                7322726 3355.283    0.000 3355.283    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                7322726   89.825    0.000 3307.532    0.000 agent.py:108(__call__)
             5077077349 2557.091    0.000 3255.754    0.000 layer.py:73(isFree)
               65904543 1483.014    0.000 2872.552    0.000 layer.py:137(NoRock_update)
             9723251811 1585.566    0.000 2263.141    0.000 enum.py:646(__hash__)
               29305544 2173.795    0.000 2173.795    0.000 {built-in method tensor}
              732272600 1315.802    0.000 2137.138    0.000 layers.py:302(check)
              732272600 1235.310    0.000 2043.755    0.000 layers.py:261(check)
               29290904   61.568    0.000 2005.361    0.000 conv.py:398(forward)
               29290904   34.658    0.000 1918.148    0.000 conv.py:390(_conv_forward)
               29290904 1883.490    0.000 1883.490    0.000 {built-in method conv2d}
               14645452   13.724    0.000 1821.563    0.000 game.py:23(board)
              732272700  184.817    0.000 1699.163    0.000 {built-in method builtins.all}
             2207059376  480.255    0.000 1591.902    0.000 layers.py:452(<genexpr>)
               43936356   81.628    0.000 1550.786    0.000 linear.py:93(forward)
               43936356   31.816    0.000 1431.239    0.000 functional.py:1737(linear)
               43936356 1391.799    0.000 1391.799    0.000 {built-in method torch._C._nn.linear}
              732272600  744.279    0.000 1167.270    0.000 layers.py:328(check)
            14062889339 1139.353    0.000 1139.353    0.000 layer.py:69(positions)
              732272600  784.567    0.000 1079.144    0.000 layers.py:63(check)
              732272600  672.493    0.000 1073.418    0.000 layers.py:287(check)
              732272700  693.997    0.000 1050.250    0.000 layers.py:110(isDone)
              146454520  910.455    0.000  910.455    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              732272600  589.623    0.000  879.309    0.000 layers.py:47(check)
              146454520  833.919    0.000  833.919    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                7322726  141.470    0.000  817.923    0.000 optimizer.py:189(zero_grad)
               58581808   44.062    0.000  785.259    0.000 activation.py:713(forward)
             1429991021  767.724    0.000  767.724    0.000 layer.py:116(elements)
               58581808   43.045    0.000  741.198    0.000 functional.py:1364(leaky_relu)
               58581808  688.638    0.000  688.638    0.000 {built-in method torch._C._nn.leaky_relu}
             9723281200  677.581    0.000  677.581    0.000 {built-in method builtins.hash}
               73227260  530.268    0.000  530.268    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                7322726  294.049    0.000  505.821    0.000 collector.py:54(collect)
               73227260  469.054    0.000  469.054    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               73227260  435.870    0.000  435.870    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               73227260  431.414    0.000  431.414    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                7322726  155.206    0.000  414.083    0.000 exploration.py:53(softmaxer)
              590726793  262.819    0.000  392.647    0.000 layer.py:96(remove)
              512590850  315.437    0.000  391.770    0.000 tensor.py:906(grad)
             3980602496  377.501    0.000  377.501    0.000 layer.py:177(isBlocking)
        6061166002/6061166001  341.441    0.000  367.005    0.000 {built-in method builtins.len}
              649446852  256.480    0.000  349.850    0.000 layer.py:100(add)
               73227260  327.233    0.000  327.233    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                7322726    9.000    0.000  285.994    0.000 loss.py:527(forward)
                7322726   24.234    0.000  276.994    0.000 functional.py:2898(mse_loss)
                 971284   10.437    0.000  259.204    0.000 layers.py:496(restart)
                7323458  213.167    0.000  213.167    0.000 {method 'tolist' of 'torch._C._TensorBase' objects}
               65904543  200.378    0.000  200.378    0.000 layer.py:148(<listcomp>)
               65904543  186.098    0.000  186.098    0.000 layer.py:149(<listcomp>)
             2196817800  177.622    0.000  177.622    0.000 layer.py:59(check)
              124367996   68.718    0.000  177.305    0.000 random.py:285(choice)
             2293839153  176.837    0.000  176.837    0.000 {method 'append' of 'list' objects}
               14645452  173.686    0.000  173.686    0.000 {built-in method sum}
                7322726  172.392    0.000  172.392    0.000 {built-in method torch._C._nn.mse_loss}
                 971284    4.724    0.000  166.926    0.000 level.py:8(__init__)
                7323458  153.159    0.000  153.159    0.000 {built-in method max}
                 971284   23.435    0.000  144.836    0.000 levels.py:163(generate)
                7322726  132.132    0.000  132.132    0.000 {built-in method multinomial}
               29290904   18.024    0.000  131.729    0.000 flatten.py:39(forward)
                7322726   26.063    0.000  126.573    0.000 __init__.py:28(_make_grads)
                7322726  123.553    0.000  123.553    0.000 {built-in method gather}
               14645452   28.295    0.000  123.138    0.000 profiler.py:615(__enter__)
               29290904  113.705    0.000  113.705    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               14645452   18.410    0.000  108.902    0.000 profiler.py:607(__init__)
              128258275   71.651    0.000  101.116    0.000 random.py:250(_randbelow_with_getrandbits)
              197715066   99.897    0.000   99.897    0.000 {built-in method torch._C._get_tracing_state}
                1942568   12.332    0.000   96.512    0.000 level.py:41(notUsed)
               14645452   94.840    0.000   94.840    0.000 {built-in method torch._ops.profiler._record_function_enter}
                7322726   94.834    0.000   94.834    0.000 {built-in method ones_like}
                7322726    8.725    0.000   93.158    0.000 tensor.py:525(__rsub__)
               14645452   90.492    0.000   90.492    0.000 {built-in method zeros}
              161119167   88.717    0.000   88.728    0.000 module.py:934(__getattr__)
                7322726   83.082    0.000   83.082    0.000 {built-in method rsub}
              551169301   82.608    0.000   82.608    0.000 layers.py:331(isBlocking)
              590726793   79.283    0.000   79.283    0.000 {method 'remove' of 'list' objects}
                8741556   10.835    0.000   79.078    0.000 layer.py:50(restart)
                7323458    6.987    0.000   77.131    0.000 functional.py:1553(softmax)
              805499860   69.760    0.000   69.760    0.000 {method 'values' of 'collections.OrderedDict' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-2>
Subject: Job 9470150: <causal3_9x9_20hoursONLYMOVERsoftmaxgam095_0> in cluster <dcc> Done

Job <causal3_9x9_20hoursONLYMOVERsoftmaxgam095_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Fri Mar 26 13:30:13 2021
Job was executed on host(s) <n-62-20-2>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Fri Mar 26 14:34:00 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Fri Mar 26 14:34:00 2021
Terminated at Sat Mar 27 02:29:17 2021
Results reported at Sat Mar 27 02:29:17 2021

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

    CPU time :                                   42802.02 sec.
    Max Memory :                                 7259 MB
    Average Memory :                             4816.87 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               9125.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   42916 sec.
    Turnaround time :                            46744 sec.

The output (if any) is above this job summary.

