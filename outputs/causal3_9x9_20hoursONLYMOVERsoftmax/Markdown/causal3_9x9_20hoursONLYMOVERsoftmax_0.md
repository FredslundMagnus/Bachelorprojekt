/zhome/ea/9/137501/.lsbatch/1616691068.9465580.shell: line 14: 13716 Killed                  python main.py $LSB_PROJECT_NAME

------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-11>
Subject: Job 9465580: <causal3_9x9_20hoursONLYMOVERsoftmax_0> in cluster <dcc> Exited

Job <causal3_9x9_20hoursONLYMOVERsoftmax_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Thu Mar 25 17:51:08 2021
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Thu Mar 25 17:51:09 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Mar 25 17:51:09 2021
Terminated at Fri Mar 26 11:11:06 2021
Results reported at Fri Mar 26 11:11:06 2021

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

    CPU time :                                   62238.01 sec.
    Max Memory :                                 8192 MB
    Average Memory :                             5184.65 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               0.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   62504 sec.
    Turnaround time :                            62398 sec.

The output (if any) is above this job summary.


# Parameters

    Name :                      causal3_9x9_20hoursONLYMOVERsoftmax-0
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


      69329487117 function calls (69168247594 primitive calls) in 42908.80 seconds

##    Ordered by: cumulative time
   List reduced from 443 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 42908.795 42908.795 {built-in method builtins.exec}
                      1    0.001    0.001 42908.795 42908.795 <string>:1(<module>)
                      1  106.968  106.968 42908.794 42908.794 main.py:64(simple)
                6718298   22.341    0.000 24339.031    0.004 game.py:27(step)
                6718298   35.055    0.000 22809.183    0.003 layers.py:475(step)
                6718298  520.224    0.000 16878.871    0.003 layers.py:18(step)
              671829800  814.504    0.000 16300.787    0.000 layer.py:76(move)
                6718298   22.259    0.000 13897.421    0.002 agent.py:27(learn)
                6718298  194.458    0.000 13860.546    0.002 agent.py:113(_learn)
                6718298  400.527    0.000 13666.088    0.002 learner.py:42(Qlearn)
              671829800 1765.909    0.000 10471.113    0.000 layers.py:492(check)
        181394046/20154894  713.744    0.000 5878.791    0.000 module.py:866(_call_impl)
                6718299  674.970    0.000 5852.435    0.001 layers.py:446(update)
               13436596   34.587    0.000 5426.131    0.000 network.py:24(forward)
                6718298   54.496    0.000 5374.582    0.001 optimizer.py:84(wrapper)
               13436596  175.601    0.000 5305.075    0.000 container.py:117(forward)
                6718298   29.170    0.000 5126.419    0.001 grad_mode.py:24(decorate_context)
                6718298  198.148    0.000 5034.447    0.001 adam.py:55(step)
                6718298 1054.247    0.000 4592.231    0.001 _functional.py:53(adam)
              671829800  993.926    0.000 4346.594    0.000 layers.py:486(isFree)
                6718298   25.651    0.000 3445.337    0.001 tensor.py:195(backward)
                6718298   25.803    0.000 3418.752    0.001 __init__.py:68(backward)
             4641663378 2660.804    0.000 3352.668    0.000 layer.py:73(isFree)
                6718298 3263.649    0.000 3263.649    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                6718298   92.504    0.000 3230.888    0.000 agent.py:108(__call__)
               60464691 1524.340    0.000 2918.281    0.000 layer.py:137(NoRock_update)
             8926601051 1610.849    0.000 2306.464    0.000 enum.py:646(__hash__)
              671829800 1318.738    0.000 2141.100    0.000 layers.py:302(check)
               26886612 2090.564    0.000 2090.564    0.000 {built-in method tensor}
              671829800 1265.487    0.000 2085.261    0.000 layers.py:261(check)
               26873192   60.942    0.000 1941.988    0.000 conv.py:398(forward)
               26873192   34.690    0.000 1854.653    0.000 conv.py:390(_conv_forward)
               26873192 1819.963    0.000 1819.963    0.000 {built-in method conv2d}
               13436596   12.939    0.000 1724.676    0.000 game.py:23(board)
              671829900  184.674    0.000 1711.285    0.000 {built-in method builtins.all}
             2031132816  484.954    0.000 1603.809    0.000 layers.py:452(<genexpr>)
               40309788   81.314    0.000 1535.912    0.000 linear.py:93(forward)
               40309788   32.795    0.000 1415.673    0.000 functional.py:1737(linear)
               40309788 1375.000    0.000 1375.000    0.000 {built-in method torch._C._nn.linear}
              671829800  753.715    0.000 1183.876    0.000 layers.py:328(check)
            12897206301 1164.706    0.000 1164.706    0.000 layer.py:69(positions)
              671829800  812.027    0.000 1113.811    0.000 layers.py:63(check)
              671829800  689.589    0.000 1101.664    0.000 layers.py:287(check)
              671829900  690.498    0.000 1058.236    0.000 layers.py:110(isDone)
              671829800  603.807    0.000  908.309    0.000 layers.py:47(check)
              134365960  898.938    0.000  898.938    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              134365960  811.237    0.000  811.237    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                6718298  137.902    0.000  789.163    0.000 optimizer.py:189(zero_grad)
               53746384   45.750    0.000  786.054    0.000 activation.py:713(forward)
             1314309165  775.465    0.000  775.465    0.000 layer.py:116(elements)
               53746384   46.075    0.000  740.304    0.000 functional.py:1364(leaky_relu)
             8926628000  695.620    0.000  695.620    0.000 {built-in method builtins.hash}
               53746384  684.703    0.000  684.703    0.000 {built-in method torch._C._nn.leaky_relu}
               67182980  510.595    0.000  510.595    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                6718298  286.305    0.000  495.605    0.000 collector.py:54(collect)
               67182980  451.198    0.000  451.198    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               67182980  429.083    0.000  429.083    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               67182980  420.844    0.000  420.844    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                6718298  149.122    0.000  405.055    0.000 exploration.py:53(softmaxer)
              539555630  271.456    0.000  401.541    0.000 layer.py:96(remove)
              470280890  308.353    0.000  384.212    0.000 tensor.py:906(grad)
             3639328193  373.962    0.000  373.962    0.000 layer.py:177(isBlocking)
              597029086  274.475    0.000  365.710    0.000 layer.py:100(add)
        5566336259/5566336258  337.990    0.000  364.510    0.000 {built-in method builtins.len}
               67182980  310.260    0.000  310.260    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                 950946   11.127    0.000  287.889    0.000 layers.py:496(restart)
                6718298    9.368    0.000  283.097    0.000 loss.py:527(forward)
                6718298   24.814    0.000  273.729    0.000 functional.py:2898(mse_loss)
                6718969  224.579    0.000  224.579    0.000 {method 'tolist' of 'torch._C._TensorBase' objects}
               60464691  201.887    0.000  201.887    0.000 layer.py:148(<listcomp>)
                 950946    6.240    0.000  185.704    0.000 level.py:8(__init__)
               60464691  185.166    0.000  185.166    0.000 layer.py:149(<listcomp>)
              113112634   68.420    0.000  174.841    0.000 random.py:285(choice)
             2106359154  172.466    0.000  172.466    0.000 {method 'append' of 'list' objects}
             2015489400  171.183    0.000  171.183    0.000 layer.py:59(check)
                6718298  170.303    0.000  170.303    0.000 {built-in method torch._C._nn.mse_loss}
               13436596  168.518    0.000  168.518    0.000 {built-in method sum}
                 950946   26.409    0.000  159.667    0.000 levels.py:163(generate)
                6718969  151.263    0.000  151.263    0.000 {built-in method max}
                6718298  129.583    0.000  129.583    0.000 {built-in method multinomial}
               26873192   18.333    0.000  128.812    0.000 flatten.py:39(forward)
                6718298  125.968    0.000  125.968    0.000 {built-in method gather}
                6718298   26.404    0.000  123.314    0.000 __init__.py:28(_make_grads)
               13436596   28.490    0.000  121.387    0.000 profiler.py:615(__enter__)
               26873192  110.479    0.000  110.479    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                1901892   14.026    0.000  105.245    0.000 level.py:41(notUsed)
               13436596   18.206    0.000  102.456    0.000 profiler.py:607(__init__)
              181395388   99.626    0.000   99.626    0.000 {built-in method torch._C._get_tracing_state}
              116921472   69.994    0.000   99.482    0.000 random.py:250(_randbelow_with_getrandbits)
               13436596   92.897    0.000   92.897    0.000 {built-in method torch._ops.profiler._record_function_enter}
                6718298   91.125    0.000   91.125    0.000 {built-in method ones_like}
                6718298    8.577    0.000   90.528    0.000 tensor.py:525(__rsub__)
              147820165   89.692    0.000   89.702    0.000 module.py:934(__getattr__)
                8558514   12.670    0.000   88.187    0.000 layer.py:50(restart)
               13436596   84.250    0.000   84.250    0.000 {built-in method zeros}
              539555630   80.984    0.000   80.984    0.000 {method 'remove' of 'list' objects}
                6718298   80.617    0.000   80.617    0.000 {built-in method rsub}
              503992438   79.902    0.000   79.902    0.000 layers.py:331(isBlocking)
                6718969    6.967    0.000   75.308    0.000 functional.py:1553(softmax)
              739012780   68.010    0.000   68.010    0.000 {method 'values' of 'collections.OrderedDict' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-11>
Subject: Job 9470145: <causal3_9x9_20hoursONLYMOVERsoftmax_0> in cluster <dcc> Done

Job <causal3_9x9_20hoursONLYMOVERsoftmax_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Fri Mar 26 13:30:12 2021
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Fri Mar 26 13:30:13 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Fri Mar 26 13:30:13 2021
Terminated at Sat Mar 27 01:25:30 2021
Results reported at Sat Mar 27 01:25:30 2021

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

    CPU time :                                   42792.30 sec.
    Max Memory :                                 6822 MB
    Average Memory :                             4593.48 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               9562.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   42935 sec.
    Turnaround time :                            42918 sec.

The output (if any) is above this job summary.

