
# Parameters

    Name :                      causal3_good-1
    Main :                      teleport
    Level :                     Levels.Causal3
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


      55122335757 function calls (54863496962 primitive calls) in 71708.20 seconds

##    Ordered by: cumulative time
   List reduced from 475 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 71708.204 71708.204 {built-in method builtins.exec}
                      1    1.939    1.939 71708.204 71708.204 <string>:1(<module>)
                      1  210.945  210.945 71706.264 71706.264 main.py:43(teleport)
                9250978   32.548    0.000 27455.785    0.003 agent.py:27(learn)
                9250978  712.261    0.000 23280.328    0.003 learner.py:42(Qlearn)
                4625489   20.111    0.000 17332.549    0.004 game.py:27(step)
                4625489  478.181    0.000 16514.837    0.004 agent.py:52(_learn)
                4625489   24.158    0.000 16287.989    0.004 layers.py:475(step)
        291200407/32362623 1242.996    0.000 11141.659    0.000 module.py:866(_call_impl)
                4625489  140.544    0.000 10889.375    0.002 agent.py:113(_learn)
                4625489  372.495    0.000 10790.455    0.002 layers.py:18(step)
               23111645   69.233    0.000 10380.261    0.000 network.py:24(forward)
              462548900  588.723    0.000 10377.500    0.000 layer.py:76(move)
               23111645  337.699    0.000 10161.146    0.000 container.py:117(forward)
                9250978   84.074    0.000 9813.575    0.001 optimizer.py:84(wrapper)
                9250978   40.222    0.000 9421.137    0.001 grad_mode.py:24(decorate_context)
                9250978  267.430    0.000 9288.186    0.001 adam.py:55(step)
                9250978 1939.420    0.000 8706.045    0.001 _functional.py:53(adam)
                4625489 4097.034    0.001 7605.573    0.002 replaybuffer.py:29(teleporter_save_data)
                9235178  228.221    0.000 6843.671    0.001 agent.py:47(__call__)
                4625489 3223.053    0.001 6588.047    0.001 agent.py:84(interveen)
              462548900 1058.713    0.000 6177.016    0.000 layers.py:492(check)
                9250978   38.848    0.000 5742.474    0.001 tensor.py:195(backward)
                9250978   37.721    0.000 5702.208    0.001 __init__.py:68(backward)
                9250978 5450.713    0.001 5450.713    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                4625490  489.576    0.000 5443.020    0.001 layers.py:446(update)
                4625489 3580.045    0.001 5242.650    0.001 replaybuffer.py:23(sample_data)
               46223290  107.962    0.000 3711.827    0.000 conv.py:398(forward)
                4625489 2126.580    0.000 3567.580    0.001 agent.py:65(modify)
               46223290   74.478    0.000 3555.319    0.000 conv.py:390(_conv_forward)
               46223290 3480.841    0.000 3480.841    0.000 {built-in method conv2d}
              462548900  691.738    0.000 3106.637    0.000 layers.py:486(isFree)
               60083957  133.125    0.000 2875.881    0.000 linear.py:93(forward)
              228809566 2872.389    0.000 2872.389    0.000 {built-in method clone}
               60083957   52.178    0.000 2681.531    0.000 functional.py:1737(linear)
               60083957 2615.646    0.000 2615.646    0.000 {built-in method torch._C._nn.linear}
             3133851974 1943.224    0.000 2414.899    0.000 layer.py:73(isFree)
               37003920 1257.794    0.000 2229.581    0.000 layer.py:137(NoRock_update)
                4625489   69.685    0.000 2179.309    0.000 agent.py:108(__call__)
               13860667  104.496    0.000 2044.552    0.000 agent.py:57(modify_board)
              166517604 1759.107    0.000 1759.107    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               41613601 1677.463    0.000 1677.463    0.000 {built-in method cat}
               83195602   77.283    0.000 1625.334    0.000 activation.py:713(forward)
              166517604 1551.879    0.000 1551.879    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               83195602   71.599    0.000 1548.051    0.000 functional.py:1364(leaky_relu)
             6110355905 1050.287    0.000 1506.562    0.000 enum.py:646(__hash__)
              462548900  917.546    0.000 1482.694    0.000 layers.py:302(check)
               19763400 1463.651    0.000 1463.651    0.000 {built-in method tensor}
               83195602 1461.342    0.000 1461.342    0.000 {built-in method torch._C._nn.leaky_relu}
              462548900  844.734    0.000 1386.777    0.000 layers.py:261(check)
                9250978  223.580    0.000 1386.472    0.000 optimizer.py:189(zero_grad)
                5187209   47.670    0.000 1336.604    0.000 layers.py:496(restart)
                4625489   87.186    0.000 1323.627    0.000 replaybuffer.py:19(stacker)
               13860667 1286.355    0.000 1286.355    0.000 {built-in method torch._C._nn.one_hot}
              462549000  151.967    0.000 1207.395    0.000 {built-in method builtins.all}
                9250978   10.464    0.000 1130.832    0.000 game.py:23(board)
             1406318610  334.330    0.000 1109.459    0.000 layers.py:452(<genexpr>)
                4625489  591.090    0.000  979.219    0.000 collector.py:54(collect)
               83258802  962.763    0.000  962.763    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                5187209   24.826    0.000  871.395    0.000 level.py:8(__init__)
               83258802  847.174    0.000  847.174    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               83258802  818.591    0.000  818.591    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              242670233  801.936    0.000  801.936    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               83258802  799.087    0.000  799.087    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              462548900  498.811    0.000  784.699    0.000 layers.py:328(check)
                5187209  102.270    0.000  748.475    0.000 levels.py:163(generate)
              462548900  463.699    0.000  734.603    0.000 layers.py:287(check)
              462549000  488.028    0.000  732.977    0.000 layers.py:110(isDone)
             7964452455  715.225    0.000  715.225    0.000 layer.py:69(positions)
                9235178  259.107    0.000  707.876    0.000 exploration.py:53(softmaxer)
               83258802  621.285    0.000  621.285    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              462548900  403.198    0.000  607.870    0.000 layers.py:47(check)
             1423434597  594.198    0.000  594.198    0.000 layer.py:116(elements)
              582811668  428.362    0.000  524.785    0.000 tensor.py:906(grad)
               10374418   77.453    0.000  501.129    0.000 level.py:41(notUsed)
                9250978   12.502    0.000  471.596    0.000 loss.py:527(forward)
                9250978   37.627    0.000  459.094    0.000 functional.py:2898(mse_loss)
             6110389568  456.281    0.000  456.281    0.000 {built-in method builtins.hash}
               14999907  162.591    0.000  433.494    0.000 random.py:315(sample)
               27752934  410.851    0.000  410.851    0.000 {built-in method sum}
        4363310308/4363310306  338.354    0.000  410.837    0.000 {built-in method builtins.len}
               41497672   48.433    0.000  403.556    0.000 layer.py:50(restart)
              676442067  278.407    0.000  377.371    0.000 layer.py:100(add)
              411765400  207.471    0.000  306.181    0.000 layer.py:96(remove)
                9250978  300.106    0.000  300.106    0.000 {built-in method torch._C._nn.mse_loss}
               46223290   32.105    0.000  281.358    0.000 flatten.py:39(forward)
               13876467   23.670    0.000  265.208    0.000 tensor.py:525(__rsub__)
                9252363  262.027    0.000  262.027    0.000 {built-in method max}
                5187309  132.197    0.000  261.043    0.000 layers.py:33(reset)
               46223290  249.253    0.000  249.253    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
             2363324115  243.340    0.000  243.340    0.000 layer.py:177(isBlocking)
                4625489   20.436    0.000  240.579    0.000 exploration.py:47(epsilonGreedy)
              355232871  164.778    0.000  239.378    0.000 random.py:250(_randbelow_with_getrandbits)
               13876467  237.678    0.000  237.678    0.000 {built-in method rsub}
                9235178  229.561    0.000  229.561    0.000 {built-in method multinomial}
              340300796  225.505    0.000  225.505    0.000 level.py:32(inverse)
              295827742  216.134    0.000  216.134    0.000 {built-in method torch._C._get_tracing_state}
                9250978  210.808    0.000  210.808    0.000 {built-in method gather}
                9250978   39.974    0.000  205.867    0.000 __init__.py:28(_make_grads)
               18501956   44.060    0.000  202.452    0.000 profiler.py:615(__enter__)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-11-15>
Subject: Job 9474226: <causal3_good_1> in cluster <dcc> Done

Job <causal3_good_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sat Mar 27 17:45:04 2021
Job was executed on host(s) <n-62-11-15>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sat Mar 27 17:45:06 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat Mar 27 17:45:06 2021
Terminated at Sun Mar 28 14:40:19 2021
Results reported at Sun Mar 28 14:40:19 2021

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

    CPU time :                                   71531.59 sec.
    Max Memory :                                 8918 MB
    Average Memory :                             5992.61 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               7466.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   71746 sec.
    Turnaround time :                            71715 sec.

The output (if any) is above this job summary.

