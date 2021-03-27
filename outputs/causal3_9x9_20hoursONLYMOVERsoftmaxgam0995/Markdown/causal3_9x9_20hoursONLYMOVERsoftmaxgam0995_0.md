/zhome/ea/9/137501/.lsbatch/1616691068.9465582.shell: line 14: 14268 Killed                  python main.py $LSB_PROJECT_NAME

------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-12>
Subject: Job 9465582: <causal3_9x9_20hoursONLYMOVERsoftmaxgam0995_0> in cluster <dcc> Exited

Job <causal3_9x9_20hoursONLYMOVERsoftmaxgam0995_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Thu Mar 25 17:51:08 2021
Job was executed on host(s) <n-62-20-12>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Thu Mar 25 18:36:59 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Mar 25 18:36:59 2021
Terminated at Fri Mar 26 11:09:56 2021
Results reported at Fri Mar 26 11:09:56 2021

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

    CPU time :                                   59423.50 sec.
    Max Memory :                                 8192 MB
    Average Memory :                             5102.49 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               0.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   59577 sec.
    Turnaround time :                            62328 sec.

The output (if any) is above this job summary.


# Parameters

    Name :                      causal3_9x9_20hoursONLYMOVERsoftmaxgam0995-0
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
    Gamma2 :                    0.995
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


      60204363454 function calls (60064344683 primitive calls) in 42904.56 seconds

##    Ordered by: cumulative time
   List reduced from 443 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 42904.563 42904.563 {built-in method builtins.exec}
                      1    0.001    0.001 42904.563 42904.563 <string>:1(<module>)
                      1  101.392  101.392 42904.562 42904.562 main.py:64(simple)
                5834100   23.236    0.000 21408.995    0.004 game.py:27(step)
                5834100   30.791    0.000 19997.690    0.003 layers.py:475(step)
                5834100   18.394    0.000 16581.367    0.003 agent.py:27(learn)
                5834100  166.666    0.000 16549.228    0.003 agent.py:113(_learn)
                5834100  459.030    0.000 16382.562    0.003 learner.py:42(Qlearn)
                5834100  454.628    0.000 14766.652    0.003 layers.py:18(step)
              583410000  728.565    0.000 14260.704    0.000 layer.py:76(move)
              583410000 1516.191    0.000 9114.457    0.000 layers.py:492(check)
                5834100   51.207    0.000 7039.598    0.001 optimizer.py:84(wrapper)
                5834100   25.959    0.000 6785.757    0.001 grad_mode.py:24(decorate_context)
                5834100  183.918    0.000 6699.038    0.001 adam.py:55(step)
        157520700/17502300  690.838    0.000 6298.180    0.000 module.py:866(_call_impl)
                5834100 1385.271    0.000 6290.499    0.001 _functional.py:53(adam)
               11668200   34.663    0.000 5830.999    0.000 network.py:24(forward)
               11668200  191.858    0.000 5718.977    0.000 container.py:117(forward)
                5834101  587.430    0.000 5162.470    0.001 layers.py:446(update)
                5834100   23.777    0.000 3966.301    0.001 tensor.py:195(backward)
                5834100   23.350    0.000 3941.540    0.001 __init__.py:68(backward)
              583410000  875.439    0.000 3837.214    0.000 layers.py:486(isFree)
                5834100 3782.089    0.001 3782.089    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                5834100   85.430    0.000 3485.949    0.001 agent.py:108(__call__)
             4036788389 2349.205    0.000 2961.775    0.000 layer.py:73(isFree)
               52506909 1340.145    0.000 2584.290    0.000 layer.py:137(NoRock_update)
               23336400   56.694    0.000 2017.161    0.000 conv.py:398(forward)
             7749540933 1403.200    0.000 1984.939    0.000 enum.py:646(__hash__)
               23336400   31.746    0.000 1936.776    0.000 conv.py:390(_conv_forward)
               23336400 1905.030    0.000 1905.030    0.000 {built-in method conv2d}
               23348060 1892.849    0.000 1892.849    0.000 {built-in method tensor}
              583410000 1165.661    0.000 1885.988    0.000 layers.py:302(check)
              583410000 1107.300    0.000 1823.300    0.000 layers.py:261(check)
               35004600   79.109    0.000 1693.108    0.000 linear.py:93(forward)
               35004600   31.487    0.000 1579.470    0.000 functional.py:1737(linear)
               35004600 1540.367    0.000 1540.367    0.000 {built-in method torch._C._nn.linear}
              583410100  173.535    0.000 1517.199    0.000 {built-in method builtins.all}
               11668200   12.643    0.000 1516.938    0.000 game.py:23(board)
             1762567316  425.069    0.000 1414.796    0.000 layers.py:452(<genexpr>)
              116682000 1286.723    0.000 1286.723    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              116682000 1142.934    0.000 1142.934    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
            11201421988 1045.741    0.000 1045.741    0.000 layer.py:69(positions)
              583410000  654.373    0.000 1031.239    0.000 layers.py:328(check)
                5834100  161.324    0.000  992.435    0.000 optimizer.py:189(zero_grad)
              583410000  718.377    0.000  986.890    0.000 layers.py:63(check)
              583410100  612.313    0.000  938.042    0.000 layers.py:110(isDone)
              583410000  583.626    0.000  930.853    0.000 layers.py:287(check)
               46672800   39.993    0.000  920.785    0.000 activation.py:713(forward)
               46672800   43.085    0.000  880.792    0.000 functional.py:1364(leaky_relu)
               46672800  828.609    0.000  828.609    0.000 {built-in method torch._C._nn.leaky_relu}
              583410000  517.320    0.000  784.461    0.000 layers.py:47(check)
             1140439010  688.333    0.000  688.333    0.000 layer.py:116(elements)
               58341000  687.259    0.000  687.259    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               58341000  603.204    0.000  603.204    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                5834100  356.464    0.000  594.636    0.000 collector.py:54(collect)
               58341000  586.896    0.000  586.896    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
             7749564362  581.743    0.000  581.743    0.000 {built-in method builtins.hash}
               58341000  579.416    0.000  579.416    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               58341000  447.966    0.000  447.966    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                5834100  160.197    0.000  445.565    0.000 exploration.py:53(softmaxer)
              408387030  306.132    0.000  377.536    0.000 tensor.py:906(grad)
              469449777  237.482    0.000  355.289    0.000 layer.py:96(remove)
        4831691789/4831691788  312.664    0.000  337.706    0.000 {built-in method builtins.len}
             3165079699  329.420    0.000  329.420    0.000 layer.py:177(isBlocking)
              518002366  230.921    0.000  311.068    0.000 layer.py:100(add)
                5834100    8.685    0.000  306.147    0.000 loss.py:527(forward)
                5834100   23.733    0.000  297.462    0.000 functional.py:2898(mse_loss)
                 803309    9.430    0.000  239.354    0.000 layers.py:496(restart)
                5834683  201.685    0.000  201.685    0.000 {method 'tolist' of 'torch._C._TensorBase' objects}
               11668200  199.938    0.000  199.938    0.000 {built-in method sum}
                5834100  196.283    0.000  196.283    0.000 {built-in method torch._C._nn.mse_loss}
               52506909  179.879    0.000  179.879    0.000 layer.py:148(<listcomp>)
               52506909  168.020    0.000  168.020    0.000 layer.py:149(<listcomp>)
                5834683  166.233    0.000  166.233    0.000 {built-in method max}
               98590520   60.435    0.000  157.588    0.000 random.py:285(choice)
             1750230000  155.536    0.000  155.536    0.000 layer.py:59(check)
             1828431622  154.524    0.000  154.524    0.000 {method 'append' of 'list' objects}
                 803309    4.336    0.000  154.174    0.000 level.py:8(__init__)
               23336400   17.779    0.000  152.356    0.000 flatten.py:39(forward)
                5834100  143.840    0.000  143.840    0.000 {built-in method multinomial}
                5834100  136.939    0.000  136.939    0.000 {built-in method gather}
               23336400  134.577    0.000  134.577    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                 803309   21.599    0.000  133.737    0.000 levels.py:163(generate)
               11668200   29.002    0.000  130.924    0.000 profiler.py:615(__enter__)
                5834100   23.561    0.000  130.873    0.000 __init__.py:28(_make_grads)
              157521866  119.797    0.000  119.797    0.000 {built-in method torch._C._get_tracing_state}
               11668200   21.707    0.000  115.619    0.000 profiler.py:607(__init__)
                5834100    8.798    0.000  108.525    0.000 tensor.py:525(__rsub__)
                5834100  102.081    0.000  102.081    0.000 {built-in method ones_like}
               11668200  101.922    0.000  101.922    0.000 {built-in method torch._ops.profiler._record_function_enter}
                5834100   98.299    0.000   98.299    0.000 {built-in method rsub}
               11668200   93.913    0.000   93.913    0.000 {built-in method zeros}
              101807937   63.931    0.000   90.724    0.000 random.py:250(_randbelow_with_getrandbits)
                1606618   11.128    0.000   89.018    0.000 level.py:41(notUsed)
                5834683    7.076    0.000   88.207    0.000 functional.py:1553(softmax)
                5834683   80.109    0.000   80.109    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
              128365521   78.629    0.000   78.639    0.000 module.py:934(__getattr__)
               11668200   73.637    0.000   73.637    0.000 {method 'view' of 'torch._C._TensorBase' objects}
                7229781   10.141    0.000   73.271    0.000 layer.py:50(restart)
              469449777   73.228    0.000   73.228    0.000 {method 'remove' of 'list' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-14>
Subject: Job 9470148: <causal3_9x9_20hoursONLYMOVERsoftmaxgam0995_0> in cluster <dcc> Done

Job <causal3_9x9_20hoursONLYMOVERsoftmaxgam0995_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Fri Mar 26 13:30:13 2021
Job was executed on host(s) <n-62-20-14>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Fri Mar 26 13:51:26 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Fri Mar 26 13:51:26 2021
Terminated at Sat Mar 27 01:46:35 2021
Results reported at Sat Mar 27 01:46:35 2021

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

    CPU time :                                   42800.93 sec.
    Max Memory :                                 6266 MB
    Average Memory :                             4345.37 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               10118.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   42911 sec.
    Turnaround time :                            44182 sec.

The output (if any) is above this job summary.

