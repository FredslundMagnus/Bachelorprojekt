
# Parameters

    Name :                      causal2_good-1
    Main :                      teleport
    Level :                     Levels.Causal2
    Hours :                     20.0
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
    Layer keys :                False
    Layer door :                False
    Layer holder :              False
    Layer putter :              False
    Layer rock :                False
    Layer dirt :                False
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
    Minutes used :              1195 minutes.
    Hours used :                19 hours.

# Profiling


      58344833606 function calls (58133567803 primitive calls) in 71710.66 seconds

##    Ordered by: cumulative time
   List reduced from 475 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 71710.665 71710.665 {built-in method builtins.exec}
                      1    2.034    2.034 71710.664 71710.664 <string>:1(<module>)
                      1  178.525  178.525 71708.630 71708.630 main.py:43(teleport)
                7545418   25.904    0.000 21378.070    0.003 agent.py:27(learn)
                7545418  550.871    0.000 18076.934    0.002 learner.py:42(Qlearn)
                3772709   15.570    0.000 16865.373    0.004 game.py:27(step)
                3772709   20.032    0.000 16016.973    0.004 layers.py:475(step)
                3772709 7757.874    0.002 14054.438    0.004 replaybuffer.py:29(teleporter_save_data)
                3772709  395.789    0.000 12895.272    0.003 agent.py:52(_learn)
        237673179/26408387  951.438    0.000 8648.440    0.000 module.py:866(_call_impl)
                3772709 5824.086    0.002 8461.207    0.002 agent.py:84(interveen)
                3772709  107.834    0.000 8441.758    0.002 agent.py:113(_learn)
                3772709  286.221    0.000 8104.391    0.002 layers.py:18(step)
               18862969   53.988    0.000 8059.508    0.000 network.py:24(forward)
               18862969  254.708    0.000 7889.557    0.000 container.py:117(forward)
                3772710  395.766    0.000 7865.961    0.002 layers.py:446(update)
              377270900  457.385    0.000 7786.609    0.000 layer.py:76(move)
                7545418   65.938    0.000 7566.545    0.001 optimizer.py:84(wrapper)
                7545418   35.028    0.000 7259.588    0.001 grad_mode.py:24(decorate_context)
                7545418  207.911    0.000 7157.014    0.001 adam.py:55(step)
                7545418 1487.127    0.000 6707.520    0.001 _functional.py:53(adam)
                7544842  185.947    0.000 5373.143    0.001 agent.py:47(__call__)
              435652336 5051.165    0.000 5051.165    0.000 {built-in method clone}
                7545418   30.833    0.000 4537.719    0.001 tensor.py:195(backward)
                7545418   29.298    0.000 4505.793    0.001 __init__.py:68(backward)
                3772709 3172.203    0.001 4502.911    0.001 replaybuffer.py:23(sample_data)
              377270900  802.073    0.000 4456.933    0.000 layers.py:492(check)
                7545418 4311.491    0.001 4311.491    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               24608563  174.805    0.000 4067.062    0.000 layers.py:496(restart)
                3772709 2224.115    0.001 3348.607    0.001 agent.py:65(modify)
               37725938   83.435    0.000 2914.069    0.000 conv.py:398(forward)
               37725938   48.966    0.000 2793.002    0.000 conv.py:390(_conv_forward)
               37725938 2744.037    0.000 2744.037    0.000 {built-in method conv2d}
              377270900  570.461    0.000 2412.580    0.000 layers.py:486(isFree)
               24608563   84.358    0.000 2349.301    0.000 level.py:8(__init__)
               49043489   98.768    0.000 2236.683    0.000 linear.py:93(forward)
               30181680 1311.233    0.000 2204.722    0.000 layer.py:137(NoRock_update)
               49043489   40.722    0.000 2089.590    0.000 functional.py:1737(linear)
               49043489 2039.545    0.000 2039.545    0.000 {built-in method torch._C._nn.linear}
               24608563  135.926    0.000 1864.404    0.000 levels.py:151(generate)
             2929692541 1467.135    0.000 1842.119    0.000 layer.py:73(isFree)
                3772709   54.726    0.000 1710.425    0.000 agent.py:108(__call__)
               11317551   74.898    0.000 1613.019    0.000 agent.py:57(modify_board)
               49217126  365.415    0.000 1597.619    0.000 level.py:41(notUsed)
             6471327385 1048.336    0.000 1521.076    0.000 enum.py:646(__hash__)
              196868504  121.610    0.000 1483.605    0.000 layer.py:50(restart)
              135817524 1361.206    0.000 1361.206    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              446969887 1344.507    0.000 1344.507    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               33953805 1332.649    0.000 1332.649    0.000 {built-in method cat}
               67906458   51.636    0.000 1255.433    0.000 activation.py:713(forward)
              135817524 1204.632    0.000 1204.632    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               67906458   54.522    0.000 1203.797    0.000 functional.py:1364(leaky_relu)
               16178865 1194.477    0.000 1194.477    0.000 {built-in method tensor}
               24608663  580.363    0.000 1161.660    0.000 layers.py:33(reset)
               67906458 1137.707    0.000 1137.707    0.000 {built-in method torch._C._nn.leaky_relu}
                7545418  172.489    0.000 1074.916    0.000 optimizer.py:189(zero_grad)
                3772709   70.210    0.000 1062.210    0.000 replaybuffer.py:19(stacker)
              377271000  122.004    0.000 1055.372    0.000 {built-in method builtins.all}
               11317551 1032.390    0.000 1032.390    0.000 {built-in method torch._C._nn.one_hot}
             1277077926  325.519    0.000  975.261    0.000 layers.py:452(<genexpr>)
              377270900  593.175    0.000  956.213    0.000 layers.py:302(check)
              377270900  583.364    0.000  936.904    0.000 layers.py:261(check)
                7545418    8.933    0.000  924.255    0.000 game.py:23(board)
                3772709  456.959    0.000  759.079    0.000 collector.py:54(collect)
               67908762  743.577    0.000  743.577    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               67908762  650.141    0.000  650.141    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              377270900  412.351    0.000  630.293    0.000 layers.py:328(check)
               67908762  623.767    0.000  623.767    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               67908762  617.265    0.000  617.265    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               49217126   34.390    0.000  613.824    0.000 level.py:38(elementsIn)
              377271000  403.816    0.000  599.630    0.000 layers.py:110(isDone)
             2438446486  596.411    0.000  596.411    0.000 layer.py:116(elements)
             1201326005  432.682    0.000  594.073    0.000 layer.py:100(add)
              377270900  366.391    0.000  568.829    0.000 layers.py:287(check)
                7544842  204.548    0.000  560.276    0.000 exploration.py:53(softmaxer)
             6095669098  529.265    0.000  529.265    0.000 layer.py:69(positions)
               67908762  486.114    0.000  486.114    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
             6471354928  472.744    0.000  472.744    0.000 {built-in method builtins.hash}
              377270900  299.676    0.000  472.041    0.000 layers.py:47(check)
             2436247737  425.472    0.000  425.472    0.000 level.py:32(inverse)
              475361388  327.804    0.000  403.024    0.000 tensor.py:906(grad)
               49217126  188.169    0.000  377.633    0.000 level.py:39(<listcomp>)
                7545418   11.003    0.000  364.648    0.000 loss.py:527(forward)
                7545418   28.527    0.000  353.645    0.000 functional.py:2898(mse_loss)
               24608563  152.022    0.000  341.721    0.000 level.py:16(<dictcomp>)
               22636254  320.643    0.000  320.643    0.000 {built-in method sum}
        3366006744/3366006742  249.611    0.000  304.501    0.000 {built-in method builtins.len}
                3772709   94.107    0.000  261.120    0.000 random.py:315(sample)
              364631663  168.843    0.000  248.898    0.000 layer.py:96(remove)
             1402688098  243.575    0.000  243.575    0.000 enum.py:352(<genexpr>)
                7545418  231.220    0.000  231.220    0.000 {built-in method torch._C._nn.mse_loss}
             3163669246  226.568    0.000  226.568    0.000 {method 'append' of 'list' objects}
             2017911022  222.637    0.000  222.637    0.000 layer.py:152(grid)
               37725938   28.792    0.000  215.731    0.000 flatten.py:39(forward)
             2200429215  208.831    0.000  208.831    0.000 layer.py:177(isBlocking)
               11318127   15.980    0.000  205.830    0.000 tensor.py:525(__rsub__)
                3772709   16.347    0.000  205.106    0.000 exploration.py:47(epsilonGreedy)
                7546549  202.068    0.000  202.068    0.000 {built-in method max}
               49217126  127.560    0.000  201.801    0.000 {built-in method _functools.reduce}
               11318127  187.016    0.000  187.016    0.000 {built-in method rsub}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-4>
Subject: Job 9474224: <causal2_good_1> in cluster <dcc> Done

Job <causal2_good_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sat Mar 27 17:45:04 2021
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sat Mar 27 17:45:04 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat Mar 27 17:45:04 2021
Terminated at Sun Mar 28 14:40:24 2021
Results reported at Sun Mar 28 14:40:24 2021

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

    CPU time :                                   71527.76 sec.
    Max Memory :                                 7801 MB
    Average Memory :                             5519.40 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               8583.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   71737 sec.
    Turnaround time :                            71720 sec.

The output (if any) is above this job summary.

