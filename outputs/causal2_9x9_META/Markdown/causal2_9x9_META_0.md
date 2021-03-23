
# Parameters

    Name :                      causal2_9x9_META-0
    Main :                      metateleport
    Level :                     Levels.Causal2
    Hours :                     11.0
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
    Layer gold :                False
    Layer keys :                False
    Layer door :                False
    Layer holder :              False
    Layer putter :              False
    Layer rock :                True
    Layer dirt :                True
    Layer diamond1 :            True
    Layer diamond2 :            True
    Layer diamond3 :            True
    Layer diamond4 :            True
    K :                         200000
    Epsilon cap :               0.1
    Softmax cap :               0.02
    Gamma :                     0.98
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.2
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Minutes used :              655 minutes.
    Hours used :                10 hours.

# Profiling


      19496155589 function calls (19376318902 primitive calls) in 39319.82 seconds

##    Ordered by: cumulative time
   List reduced from 471 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 39319.820 39319.820 {built-in method builtins.exec}
                      1    5.137    5.137 39319.819 39319.819 <string>:1(<module>)
                      1   99.273   99.273 39314.682 39314.682 main.py:14(metateleport)
                2605278 6622.714    0.003 11351.531    0.004 replaybuffer.py:27(teleporter_save_data)
                3907917   12.916    0.000 8956.270    0.002 agent.py:27(learn)
                3907917  227.009    0.000 7214.008    0.002 learner.py:42(Qlearn)
                2605278   87.563    0.000 6701.491    0.003 agent.py:51(_learn)
                2605278 4566.746    0.002 6122.416    0.002 agent.py:81(interveen)
                1302639    5.672    0.000 5299.605    0.004 game.py:27(step)
                1302639    7.228    0.000 5024.262    0.004 layers.py:373(step)
                2605278 4042.535    0.002 4863.342    0.002 replaybuffer.py:23(sample_data)
        134163367/14328379  503.038    0.000 4091.496    0.000 module.py:866(_call_impl)
              474565182 3902.592    0.000 3902.592    0.000 {built-in method clone}
               10420462   27.545    0.000 3821.182    0.000 network.py:24(forward)
               10420462  123.112    0.000 3729.727    0.000 container.py:117(forward)
                1302639  103.863    0.000 3581.477    0.003 layers.py:18(step)
              130263900  299.476    0.000 3467.584    0.000 layer.py:74(move)
                5209906  126.199    0.000 3121.151    0.001 agent.py:46(__call__)
                3907917   30.990    0.000 2799.868    0.001 optimizer.py:84(wrapper)
                3907917   16.195    0.000 2660.556    0.001 grad_mode.py:24(decorate_context)
                3907917  109.550    0.000 2610.120    0.001 adam.py:55(step)
                3907917  553.660    0.000 2372.548    0.001 _functional.py:53(adam)
                1302639   35.946    0.000 2232.619    0.002 agent.py:145(_learn)
              130263900  331.898    0.000 1960.695    0.000 layers.py:390(check)
                3907917   14.615    0.000 1853.851    0.000 tensor.py:195(backward)
                3907917   14.781    0.000 1838.708    0.000 __init__.py:68(backward)
                3907917 1752.629    0.000 1752.629    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                1302639  941.582    0.001 1544.921    0.001 agent.py:101(metamodify)
                1302640  134.561    0.000 1424.485    0.001 layers.py:344(update)
               20840924   44.466    0.000 1382.378    0.000 conv.py:398(forward)
               20840924   25.393    0.000 1317.420    0.000 conv.py:390(_conv_forward)
               20840924 1292.026    0.000 1292.026    0.000 {built-in method conv2d}
               28656108   55.635    0.000 1056.533    0.000 linear.py:93(forward)
              130263900  221.727    0.000  989.016    0.000 layers.py:384(isFree)
               28656108   23.123    0.000  972.833    0.000 functional.py:1737(linear)
                7815184   61.465    0.000  947.744    0.000 agent.py:55(modify_board)
               28656108  944.567    0.000  944.567    0.000 {built-in method torch._C._nn.linear}
              481077727  850.153    0.000  850.153    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               11723760  474.036    0.000  816.079    0.000 layer.py:119(update)
               23446852  782.987    0.000  782.987    0.000 {built-in method cat}
             1156356724  628.399    0.000  767.289    0.000 layer.py:71(isFree)
                2605278   46.894    0.000  642.192    0.000 replaybuffer.py:19(stacker)
                7815184  612.813    0.000  612.813    0.000 {built-in method torch._C._nn.one_hot}
               39076570   31.225    0.000  554.816    0.000 activation.py:713(forward)
                6731352  547.564    0.000  547.564    0.000 {built-in method tensor}
               39076570   31.386    0.000  523.591    0.000 functional.py:1364(leaky_relu)
                1302639   20.043    0.000  504.871    0.000 agent.py:140(__call__)
               39076570  486.164    0.000  486.164    0.000 {built-in method torch._C._nn.leaky_relu}
                3907917    5.050    0.000  480.563    0.000 game.py:23(board)
               72947784  453.651    0.000  453.651    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
             1855745209  308.718    0.000  432.372    0.000 enum.py:646(__hash__)
                3907917   74.288    0.000  415.579    0.000 optimizer.py:189(zero_grad)
               72947784  409.483    0.000  409.483    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              130263900  213.898    0.000  335.676    0.000 layers.py:216(check)
              130263900  210.846    0.000  332.178    0.000 layers.py:230(check)
              130263900  210.521    0.000  328.470    0.000 layers.py:244(check)
              130264000   34.040    0.000  323.898    0.000 {built-in method builtins.all}
                5209906  116.192    0.000  311.518    0.000 exploration.py:53(softmaxer)
              398505076   87.609    0.000  303.879    0.000 layers.py:350(<genexpr>)
              130263900  199.791    0.000  276.692    0.000 layers.py:76(check)
               36473892  274.865    0.000  274.865    0.000 {method 'add' of 'torch._C._TensorBase' objects}
             3116127012  257.023    0.000  257.023    0.000 layer.py:67(positions)
                1302639  142.888    0.000  244.872    0.000 collector.py:54(collect)
               36473892  239.204    0.000  239.204    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              305246964  222.854    0.000  222.854    0.000 layer.py:114(elements)
               36473892  217.508    0.000  217.508    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               36473892  216.160    0.000  216.160    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              130264000  138.506    0.000  204.861    0.000 layers.py:110(isDone)
              255317328  160.580    0.000  199.514    0.000 tensor.py:906(grad)
                2605278   66.395    0.000  173.802    0.000 random.py:315(sample)
              130263900  113.416    0.000  168.422    0.000 layers.py:203(check)
               36473892  162.120    0.000  162.120    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              130263900  104.589    0.000  156.107    0.000 layers.py:63(check)
                3907917    4.812    0.000  155.929    0.000 loss.py:527(forward)
                3907917   13.715    0.000  151.117    0.000 functional.py:2898(mse_loss)
        1530093520/1530093517  112.958    0.000  141.692    0.000 {built-in method builtins.len}
             1855760476  123.657    0.000  123.657    0.000 {built-in method builtins.hash}
               11723751  117.899    0.000  117.899    0.000 {built-in method sum}
             1156356724  108.478    0.000  108.478    0.000 layer.py:175(isBlocking)
                 347868    4.242    0.000  100.952    0.000 layers.py:394(restart)
                5209906   97.709    0.000   97.709    0.000 {built-in method multinomial}
              128478292   64.098    0.000   93.918    0.000 layer.py:94(remove)
               20840924   14.462    0.000   93.395    0.000 flatten.py:39(forward)
                3907917   93.294    0.000   93.294    0.000 {built-in method torch._C._nn.mse_loss}
                6513195    8.509    0.000   89.702    0.000 tensor.py:525(__rsub__)
                3908567   86.565    0.000   86.565    0.000 {built-in method max}
              141065493   62.376    0.000   86.164    0.000 layer.py:98(add)
                6513195   79.766    0.000   79.766    0.000 {built-in method rsub}
               20840924   78.933    0.000   78.933    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              131966477   50.199    0.000   74.912    0.000 random.py:250(_randbelow_with_getrandbits)
                2605280   73.913    0.000   73.913    0.000 {built-in method nonzero}
              136769685   71.675    0.000   71.675    0.000 {built-in method torch._C._get_tracing_state}
                 347868    2.335    0.000   70.198    0.000 level.py:8(__init__)
                3907917   14.676    0.000   68.139    0.000 __init__.py:28(_make_grads)
                2606318    6.799    0.000   67.640    0.000 tensor.py:575(__iter__)
              109424605   67.040    0.000   67.046    0.000 module.py:934(__getattr__)
                3907917   66.463    0.000   66.463    0.000 {built-in method gather}
                7815834   14.732    0.000   65.446    0.000 profiler.py:615(__enter__)
                 347868    4.398    0.000   61.875    0.000 levels.py:151(generate)
                5421435   61.577    0.000   61.577    0.000 {method 'long' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-6>
Subject: Job 9452864: <causal2_9x9_META_0> in cluster <dcc> Done

Job <causal2_9x9_META_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Tue Mar 23 02:18:34 2021
Job was executed on host(s) <n-62-20-6>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Tue Mar 23 02:18:36 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue Mar 23 02:18:36 2021
Terminated at Tue Mar 23 13:14:09 2021
Results reported at Tue Mar 23 13:14:09 2021

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

    CPU time :                                   39217.39 sec.
    Max Memory :                                 6081 MB
    Average Memory :                             4966.96 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               2111.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   39448 sec.
    Turnaround time :                            39335 sec.

The output (if any) is above this job summary.

