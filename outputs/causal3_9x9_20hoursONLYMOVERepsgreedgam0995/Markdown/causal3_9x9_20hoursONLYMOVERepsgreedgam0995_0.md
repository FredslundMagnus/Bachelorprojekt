
# Parameters

    Name :                      causal3_9x9_20hoursONLYMOVERepsgreedgam0995-0
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


      73268136924 function calls (73108145065 primitive calls) in 42904.63 seconds

##    Ordered by: cumulative time
   List reduced from 417 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 42904.632 42904.632 {built-in method builtins.exec}
                      1    0.001    0.001 42904.632 42904.632 <string>:1(<module>)
                      1  101.158  101.158 42904.631 42904.631 main.py:64(simple)
                6666312   23.323    0.000 24888.404    0.004 game.py:27(step)
                6666312   31.028    0.000 23484.219    0.004 layers.py:475(step)
                6666312  508.424    0.000 14783.951    0.002 layers.py:18(step)
              666631200  734.480    0.000 14216.657    0.000 layer.py:76(move)
                6666312   19.939    0.000 13534.755    0.002 agent.py:27(learn)
                6666312  176.538    0.000 13501.089    0.002 agent.py:113(_learn)
                6666312  392.760    0.000 13324.551    0.002 learner.py:42(Qlearn)
              666631200 1694.134    0.000 9795.936    0.000 layers.py:492(check)
                6666313  659.198    0.000 8629.317    0.001 layers.py:446(update)
        179990424/19998936  691.166    0.000 5680.102    0.000 module.py:866(_call_impl)
                6666312   51.639    0.000 5317.473    0.001 optimizer.py:84(wrapper)
               13332624   32.075    0.000 5239.800    0.000 network.py:24(forward)
               13332624  173.671    0.000 5123.379    0.000 container.py:117(forward)
                6666312   27.371    0.000 5074.678    0.001 grad_mode.py:24(decorate_context)
                6666312  191.132    0.000 4988.735    0.001 adam.py:55(step)
                6666312 1043.713    0.000 4555.678    0.001 _functional.py:53(adam)
                6666312   24.108    0.000 3325.096    0.000 tensor.py:195(backward)
                6666312   24.896    0.000 3299.993    0.000 __init__.py:68(backward)
              666631200  737.109    0.000 3246.476    0.000 layers.py:486(isFree)
                6666312 3149.863    0.000 3149.863    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
               59996817 1716.287    0.000 3147.114    0.000 layer.py:137(NoRock_update)
                6666312   88.076    0.000 3108.464    0.000 agent.py:108(__call__)
               10698233   93.902    0.000 2854.949    0.000 layers.py:496(restart)
             3448265818 1967.322    0.000 2509.367    0.000 layer.py:73(isFree)
             9905887219 1707.114    0.000 2426.239    0.000 enum.py:646(__hash__)
               29610041 2058.708    0.000 2058.708    0.000 {built-in method tensor}
              666631200 1223.637    0.000 1961.085    0.000 layers.py:302(check)
              666631200 1172.926    0.000 1903.761    0.000 layers.py:261(check)
               26665248   59.676    0.000 1873.765    0.000 conv.py:398(forward)
               10698233   42.882    0.000 1837.123    0.000 level.py:8(__init__)
               26665248   31.835    0.000 1788.613    0.000 conv.py:390(_conv_forward)
               26665248 1756.778    0.000 1756.778    0.000 {built-in method conv2d}
              666631300  212.762    0.000 1714.700    0.000 {built-in method builtins.all}
               13332624   11.841    0.000 1624.463    0.000 game.py:23(board)
               10698233  267.142    0.000 1609.045    0.000 levels.py:163(generate)
             2008226014  492.803    0.000 1579.479    0.000 layers.py:452(<genexpr>)
               39997872   80.760    0.000 1484.077    0.000 linear.py:93(forward)
               39997872   32.996    0.000 1364.736    0.000 functional.py:1737(linear)
               39997872 1324.149    0.000 1324.149    0.000 {built-in method torch._C._nn.linear}
            12361937823 1137.421    0.000 1137.421    0.000 layer.py:69(positions)
              666631200  710.651    0.000 1112.660    0.000 layers.py:328(check)
              666631200  787.036    0.000 1086.150    0.000 layers.py:63(check)
               21396466  124.155    0.000 1079.757    0.000 level.py:41(notUsed)
              666631300  661.986    0.000 1031.560    0.000 layers.py:110(isDone)
              666631200  639.038    0.000 1016.064    0.000 layers.py:287(check)
               96284097  127.907    0.000  892.498    0.000 layer.py:50(restart)
              133326240  873.150    0.000  873.150    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              666631200  557.853    0.000  857.006    0.000 layers.py:47(check)
             2210884986  820.761    0.000  820.761    0.000 layer.py:116(elements)
              133326240  807.468    0.000  807.468    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                6666312  136.599    0.000  793.269    0.000 optimizer.py:189(zero_grad)
               53330496   43.798    0.000  757.142    0.000 activation.py:713(forward)
             9905913968  719.130    0.000  719.130    0.000 {built-in method builtins.hash}
               53330496   45.279    0.000  713.344    0.000 functional.py:1364(leaky_relu)
               53330496  658.094    0.000  658.094    0.000 {built-in method torch._C._nn.leaky_relu}
              445054502  556.356    0.000  556.356    0.000 level.py:32(inverse)
             1046499472  395.804    0.000  536.946    0.000 layer.py:100(add)
               10698333  265.117    0.000  528.300    0.000 layers.py:33(reset)
               66663120  517.709    0.000  517.709    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                6666312  281.990    0.000  485.892    0.000 collector.py:54(collect)
               66663120  452.084    0.000  452.084    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               66663120  423.333    0.000  423.333    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               66663120  421.750    0.000  421.750    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              466641870  305.222    0.000  378.698    0.000 tensor.py:906(grad)
        5876065009/5876065008  341.972    0.000  366.736    0.000 {built-in method builtins.len}
                6666312   26.333    0.000  355.142    0.000 exploration.py:47(epsilonGreedy)
               66663120  322.064    0.000  322.064    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               21396466   18.089    0.000  308.199    0.000 level.py:38(elementsIn)
             2737318784  290.065    0.000  290.065    0.000 layer.py:177(isBlocking)
                6666312    8.254    0.000  270.460    0.000 loss.py:527(forward)
              369064145  175.662    0.000  262.970    0.000 layer.py:96(remove)
                6666312   23.938    0.000  262.207    0.000 functional.py:2898(mse_loss)
             3140162248  227.897    0.000  227.897    0.000 {method 'append' of 'list' objects}
               59996817  190.332    0.000  190.332    0.000 layer.py:148(<listcomp>)
                6666312  184.839    0.000  184.839    0.000 {method 'tolist' of 'torch._C._TensorBase' objects}
               59996817  177.244    0.000  177.244    0.000 layer.py:149(<listcomp>)
               21396466   89.029    0.000  175.675    0.000 level.py:39(<listcomp>)
               13332624  167.018    0.000  167.018    0.000 {built-in method sum}
             1999893600  165.076    0.000  165.076    0.000 layer.py:59(check)
                6666312  162.528    0.000  162.528    0.000 {built-in method torch._C._nn.mse_loss}
               10698233   69.920    0.000  155.140    0.000 level.py:16(<dictcomp>)
                6666978  144.397    0.000  144.397    0.000 {built-in method max}
                2931473   60.608    0.000  144.340    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               21396466   55.857    0.000  134.676    0.000 random.py:315(sample)
               26665248   19.296    0.000  125.469    0.000 flatten.py:39(forward)
                6666312   24.481    0.000  119.681    0.000 __init__.py:28(_make_grads)
                6666312  117.332    0.000  117.332    0.000 {built-in method gather}
               13332624   25.345    0.000  114.639    0.000 profiler.py:615(__enter__)
               21396466   67.430    0.000  114.435    0.000 {built-in method _functools.reduce}
              609799292  111.908    0.000  111.908    0.000 enum.py:352(<genexpr>)
               26665248  106.173    0.000  106.173    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              877264044  105.755    0.000  105.755    0.000 layer.py:152(grid)
               13332624   18.932    0.000  103.582    0.000 profiler.py:607(__init__)
              179990424  100.030    0.000  100.030    0.000 {built-in method torch._C._get_tracing_state}
               59807212   36.624    0.000   96.270    0.000 random.py:285(choice)
              102656259   65.706    0.000   92.391    0.000 random.py:250(_randbelow_with_getrandbits)
                6666312   89.814    0.000   89.814    0.000 {built-in method ones_like}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-11-15>
Subject: Job 9470149: <causal3_9x9_20hoursONLYMOVERepsgreedgam0995_0> in cluster <dcc> Done

Job <causal3_9x9_20hoursONLYMOVERepsgreedgam0995_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Fri Mar 26 13:30:13 2021
Job was executed on host(s) <n-62-11-15>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Fri Mar 26 14:20:07 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Fri Mar 26 14:20:07 2021
Terminated at Sat Mar 27 02:15:17 2021
Results reported at Sat Mar 27 02:15:17 2021

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

    CPU time :                                   42793.26 sec.
    Max Memory :                                 6839 MB
    Average Memory :                             4675.14 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               9545.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   42910 sec.
    Turnaround time :                            45904 sec.

The output (if any) is above this job summary.

