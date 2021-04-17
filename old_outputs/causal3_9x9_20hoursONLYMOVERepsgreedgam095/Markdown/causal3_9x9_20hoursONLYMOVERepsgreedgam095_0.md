
# Parameters

    Name :                      causal3_9x9_20hoursONLYMOVERepsgreedgam095-0
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


      76161583175 function calls (75994304892 primitive calls) in 42911.79 seconds

##    Ordered by: cumulative time
   List reduced from 417 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 42911.786 42911.786 {built-in method builtins.exec}
                      1    0.001    0.001 42911.786 42911.786 <string>:1(<module>)
                      1   99.782   99.782 42911.785 42911.785 main.py:64(simple)
                6969913   23.113    0.000 24902.827    0.004 game.py:27(step)
                6969913   30.122    0.000 23491.382    0.003 layers.py:475(step)
                6969913  488.323    0.000 14781.167    0.002 layers.py:18(step)
              696991300  684.164    0.000 14238.077    0.000 layer.py:76(move)
                6969913   19.588    0.000 13528.249    0.002 agent.py:27(learn)
                6969913  148.894    0.000 13496.188    0.002 agent.py:113(_learn)
                6969913  386.263    0.000 13347.294    0.002 learner.py:42(Qlearn)
              696991300 1732.655    0.000 9808.917    0.000 layers.py:492(check)
                6969914  649.999    0.000 8641.240    0.001 layers.py:446(update)
        188187651/20909739  687.578    0.000 5609.904    0.000 module.py:866(_call_impl)
                6969913   54.222    0.000 5318.041    0.001 optimizer.py:84(wrapper)
               13939826   31.205    0.000 5168.401    0.000 network.py:24(forward)
                6969913   28.288    0.000 5068.932    0.001 grad_mode.py:24(decorate_context)
               13939826  163.966    0.000 5052.554    0.000 container.py:117(forward)
                6969913  195.194    0.000 4979.709    0.001 adam.py:55(step)
                6969913 1017.215    0.000 4546.910    0.001 _functional.py:53(adam)
                6969913   28.993    0.000 3409.505    0.000 tensor.py:195(backward)
                6969913   24.969    0.000 3379.520    0.000 __init__.py:68(backward)
              696991300  738.241    0.000 3344.572    0.000 layers.py:486(isFree)
                6969913 3229.795    0.000 3229.795    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
               62729226 1729.666    0.000 3192.392    0.000 layer.py:137(NoRock_update)
                6969913   77.080    0.000 3058.963    0.000 agent.py:108(__call__)
               11478175   91.942    0.000 2881.029    0.000 layers.py:496(restart)
             3346244256 2120.159    0.000 2606.330    0.000 layer.py:73(isFree)
            10393714567 1687.228    0.000 2397.502    0.000 enum.py:646(__hash__)
               30887984 2138.123    0.000 2138.123    0.000 {built-in method tensor}
              696991300 1221.720    0.000 1947.162    0.000 layers.py:302(check)
              696991300 1159.753    0.000 1874.799    0.000 layers.py:261(check)
               27879652   64.435    0.000 1865.491    0.000 conv.py:398(forward)
               11478175   42.778    0.000 1864.555    0.000 level.py:8(__init__)
               27879652   36.589    0.000 1775.809    0.000 conv.py:390(_conv_forward)
               27879652 1739.220    0.000 1739.220    0.000 {built-in method conv2d}
               13939826   12.378    0.000 1723.163    0.000 game.py:23(board)
              696991400  181.914    0.000 1666.616    0.000 {built-in method builtins.all}
               11478175  262.888    0.000 1633.798    0.000 levels.py:163(generate)
             2097411876  467.466    0.000 1561.052    0.000 layers.py:452(<genexpr>)
               41819478   78.512    0.000 1449.137    0.000 linear.py:93(forward)
               41819478   32.040    0.000 1334.188    0.000 functional.py:1737(linear)
               41819478 1294.486    0.000 1294.486    0.000 {built-in method torch._C._nn.linear}
              696991300  820.483    0.000 1111.130    0.000 layers.py:63(check)
              696991300  712.428    0.000 1107.248    0.000 layers.py:328(check)
               22956350  126.350    0.000 1104.986    0.000 level.py:41(notUsed)
            12854480843 1070.440    0.000 1070.440    0.000 layer.py:69(positions)
              696991400  681.879    0.000 1037.061    0.000 layers.py:110(isDone)
              696991300  654.468    0.000 1024.171    0.000 layers.py:287(check)
              103303575  117.863    0.000  893.459    0.000 layer.py:50(restart)
              139398260  872.287    0.000  872.287    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
             2289288627  849.906    0.000  849.906    0.000 layer.py:116(elements)
              696991300  553.284    0.000  844.890    0.000 layers.py:47(check)
              139398260  795.640    0.000  795.640    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                6969913  136.973    0.000  781.570    0.000 optimizer.py:189(zero_grad)
               55759304   42.583    0.000  746.704    0.000 activation.py:713(forward)
            10393742516  710.278    0.000  710.278    0.000 {built-in method builtins.hash}
               55759304   43.087    0.000  704.121    0.000 functional.py:1364(leaky_relu)
               55759304  651.551    0.000  651.551    0.000 {built-in method torch._C._nn.leaky_relu}
              477492984  569.416    0.000  569.416    0.000 level.py:32(inverse)
               69699130  544.847    0.000  544.847    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               11478275  270.279    0.000  536.548    0.000 layers.py:33(reset)
             1083062341  384.917    0.000  523.601    0.000 layer.py:100(add)
                6969913  279.542    0.000  480.098    0.000 collector.py:54(collect)
               69699130  454.887    0.000  454.887    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               69699130  424.590    0.000  424.590    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               69699130  421.865    0.000  421.865    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              487893940  301.903    0.000  375.014    0.000 tensor.py:906(grad)
        6244263771/6244263770  344.946    0.000  369.442    0.000 {built-in method builtins.len}
                6969913   25.357    0.000  354.833    0.000 exploration.py:47(epsilonGreedy)
               22956350   17.506    0.000  316.150    0.000 level.py:38(elementsIn)
               69699130  312.033    0.000  312.033    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                6969913    8.143    0.000  274.876    0.000 loss.py:527(forward)
             2668576932  266.861    0.000  266.861    0.000 layer.py:177(isBlocking)
                6969913   25.553    0.000  266.733    0.000 functional.py:2898(mse_loss)
              356671588  160.314    0.000  243.662    0.000 layer.py:96(remove)
             3241033240  223.838    0.000  223.838    0.000 {method 'append' of 'list' objects}
               62729226  189.607    0.000  189.607    0.000 layer.py:148(<listcomp>)
               22956350   89.938    0.000  178.438    0.000 level.py:39(<listcomp>)
               62729226  176.918    0.000  176.918    0.000 layer.py:149(<listcomp>)
             2090973900  166.862    0.000  166.862    0.000 layer.py:59(check)
                6969913  164.846    0.000  164.846    0.000 {built-in method torch._C._nn.mse_loss}
               13939826  164.199    0.000  164.199    0.000 {built-in method sum}
                6969913  162.618    0.000  162.618    0.000 {method 'tolist' of 'torch._C._TensorBase' objects}
               11478175   71.662    0.000  158.632    0.000 level.py:16(<dictcomp>)
                2994412   60.034    0.000  141.630    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                6970609  140.502    0.000  140.502    0.000 {built-in method max}
               22956350   55.819    0.000  135.770    0.000 random.py:315(sample)
               27879652   18.637    0.000  120.744    0.000 flatten.py:39(forward)
               22956350   70.490    0.000  120.206    0.000 {built-in method _functools.reduce}
                6969913   24.166    0.000  119.115    0.000 __init__.py:28(_make_grads)
               13939826   25.618    0.000  116.299    0.000 profiler.py:615(__enter__)
              654255986  115.501    0.000  115.501    0.000 enum.py:352(<genexpr>)
                6969913  115.491    0.000  115.491    0.000 {built-in method gather}
              941219288  106.747    0.000  106.747    0.000 layer.py:152(grid)
               13939826   17.757    0.000  102.989    0.000 profiler.py:607(__init__)
               27879652  102.107    0.000  102.107    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               67860504   39.283    0.000  100.274    0.000 random.py:285(choice)
              188187651   98.434    0.000   98.434    0.000 {built-in method torch._C._get_tracing_state}
              113833565   66.023    0.000   93.937    0.000 random.py:250(_randbelow_with_getrandbits)
               13939826   90.680    0.000   90.680    0.000 {built-in method torch._ops.profiler._record_function_enter}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-7>
Subject: Job 9470151: <causal3_9x9_20hoursONLYMOVERepsgreedgam095_0> in cluster <dcc> Done

Job <causal3_9x9_20hoursONLYMOVERepsgreedgam095_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Fri Mar 26 13:30:13 2021
Job was executed on host(s) <n-62-20-7>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sat Mar 27 01:25:31 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat Mar 27 01:25:31 2021
Terminated at Sat Mar 27 13:20:50 2021
Results reported at Sat Mar 27 13:20:50 2021

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

    CPU time :                                   42896.77 sec.
    Max Memory :                                 2325 MB
    Average Memory :                             2319.89 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14059.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   42952 sec.
    Turnaround time :                            85837 sec.

The output (if any) is above this job summary.

