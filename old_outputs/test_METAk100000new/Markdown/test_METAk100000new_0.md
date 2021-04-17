
# Parameters

    Name :                      test_METAk100000new-0
    Main :                      metateleport
    Level :                     Levels.Causal1
    Hours :                     4.0
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
    Layer rock :                False
    Layer dirt :                False
    Layer diamond1 :            False
    Layer diamond2 :            False
    Layer diamond3 :            False
    Layer diamond4 :            False
    Layer reddoors :            False
    Layer redkeys :             False
    Layer bluedoors :           False
    Layer bluekeys :            False
    K :                         100000.0
    Epsilon cap :               0.1
    Softmax cap :               0.025
    Gamma :                     0.95
    Update :                    10000
    Reset chance :              0.001
    Modified done chance :      0.03
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Minutes used :              235 minutes.
    Hours used :                3 hours.

# Profiling


      5232154067 function calls (5173587568 primitive calls) in 14115.01 seconds

##    Ordered by: cumulative time
   List reduced from 463 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 14115.011 14115.011 {built-in method builtins.exec}
                      1    5.696    5.696 14115.011 14115.011 <string>:1(<module>)
                      1   58.100   58.100 14109.315 14109.315 main.py:14(metateleport)
                1972638    7.800    0.000 5004.004    0.003 agent.py:27(learn)
                1972638  122.915    0.000 4006.606    0.002 learner.py:42(Qlearn)
                1315092   49.520    0.000 3753.337    0.003 agent.py:51(_learn)
                1315092 2528.932    0.002 3029.271    0.002 replaybuffer.py:23(sample_data)
        65637020/7072220  278.419    0.000 2195.582    0.000 module.py:866(_call_impl)
                5099582   14.566    0.000 2041.658    0.000 network.py:24(forward)
                5099582   68.377    0.000 1990.848    0.000 container.py:117(forward)
                1315092 1047.460    0.001 1744.867    0.001 replaybuffer.py:27(teleporter_save_data)
                2469398   67.855    0.000 1639.413    0.001 agent.py:46(__call__)
                1972638   17.846    0.000 1538.492    0.001 optimizer.py:84(wrapper)
                1315092  753.502    0.001 1494.094    0.001 agent.py:81(interveen)
                1972638   10.169    0.000 1459.764    0.001 grad_mode.py:24(decorate_context)
                1972638   62.891    0.000 1428.164    0.001 adam.py:55(step)
                 657546    3.275    0.000 1344.990    0.002 game.py:27(step)
                1972638  293.544    0.000 1293.453    0.001 _functional.py:53(adam)
                 657546   20.008    0.000 1237.320    0.002 agent.py:110(_learn)
                 657546    4.196    0.000 1234.190    0.002 layers.py:475(step)
                1972638    8.877    0.000 1058.856    0.001 tensor.py:195(backward)
                1972638    9.277    0.000 1049.706    0.001 __init__.py:68(backward)
                1972638  998.693    0.001  998.693    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                 657546  600.434    0.001  926.232    0.001 agent.py:114(metamodify)
               10199164   23.713    0.000  739.609    0.000 conv.py:398(forward)
               10199164   15.952    0.000  703.796    0.000 conv.py:390(_conv_forward)
               10199164  687.843    0.000  687.843    0.000 {built-in method conv2d}
                 657547   74.054    0.000  620.273    0.001 layers.py:446(update)
                 657546   60.463    0.000  603.040    0.001 layers.py:18(step)
               65807184  589.372    0.000  589.372    0.000 {built-in method clone}
               13983654   30.677    0.000  559.895    0.000 linear.py:93(forward)
               65754600   70.335    0.000  535.989    0.000 layer.py:76(move)
               13983654   11.620    0.000  513.025    0.000 functional.py:1737(linear)
               13983654  498.831    0.000  498.831    0.000 {built-in method torch._C._nn.linear}
                3784490   34.445    0.000  498.481    0.000 agent.py:55(modify_board)
               11675042  454.917    0.000  454.917    0.000 {built-in method cat}
                1315092   35.286    0.000  397.271    0.000 replaybuffer.py:19(stacker)
                3784490  323.355    0.000  323.355    0.000 {built-in method torch._C._nn.one_hot}
               65754600   45.073    0.000  317.602    0.000 layers.py:486(isFree)
               19083236   16.541    0.000  289.795    0.000 activation.py:713(forward)
                 657546   12.119    0.000  273.737    0.000 agent.py:105(__call__)
               19083236   15.877    0.000  273.254    0.000 functional.py:1364(leaky_relu)
              175770718  243.629    0.000  272.530    0.000 layer.py:73(isFree)
               19083236  254.383    0.000  254.383    0.000 {built-in method torch._C._nn.leaky_relu}
               36822576  250.335    0.000  250.335    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                1972638   40.533    0.000  226.266    0.000 optimizer.py:189(zero_grad)
               36822576  223.111    0.000  223.111    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                1972641  119.262    0.000  196.042    0.000 layer.py:137(NoRock_update)
               65754700   18.094    0.000  181.957    0.000 {built-in method builtins.all}
                3397649  180.726    0.000  180.726    0.000 {built-in method tensor}
              197412381   46.782    0.000  171.564    0.000 layers.py:452(<genexpr>)
                2469398   59.581    0.000  163.331    0.000 exploration.py:53(softmaxer)
               18411288  149.381    0.000  149.381    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                1972638    2.374    0.000  143.767    0.000 game.py:23(board)
                 638960    4.759    0.000  141.202    0.000 layers.py:496(restart)
               68934128  140.210    0.000  140.210    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                 657546   77.504    0.000  132.342    0.000 collector.py:54(collect)
               18411288  129.947    0.000  129.947    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               18411288  121.604    0.000  121.604    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               18411288  120.820    0.000  120.820    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               65754700   81.446    0.000  119.067    0.000 layers.py:110(isDone)
              128879100   90.178    0.000  111.080    0.000 tensor.py:906(grad)
                1315092   39.515    0.000  100.415    0.000 random.py:315(sample)
                 638960    2.757    0.000   95.577    0.000 level.py:8(__init__)
                1972638    3.233    0.000   93.023    0.000 loss.py:527(forward)
                1972638    8.788    0.000   89.789    0.000 functional.py:2898(mse_loss)
               18411288   87.278    0.000   87.278    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                 638960    4.997    0.000   80.412    0.000 levels.py:122(generate)
                1916880   16.587    0.000   70.490    0.000 level.py:41(notUsed)
               65754600   52.401    0.000   68.292    0.000 layers.py:492(check)
                5917914   63.055    0.000   63.055    0.000 {built-in method sum}
        497277987/497277984   47.181    0.000   62.097    0.000 {built-in method builtins.len}
                1972638   54.281    0.000   54.281    0.000 {built-in method torch._C._nn.mse_loss}
                2469398   52.383    0.000   52.383    0.000 {built-in method multinomial}
                3287730    4.803    0.000   50.481    0.000 tensor.py:525(__rsub__)
              157164463   48.729    0.000   48.729    0.000 layer.py:116(elements)
                1972949   48.720    0.000   48.720    0.000 {built-in method max}
               76735899   34.782    0.000   48.361    0.000 layer.py:100(add)
               10199164    7.691    0.000   48.169    0.000 flatten.py:39(forward)
                3287730   44.919    0.000   44.919    0.000 {built-in method rsub}
               67691252   28.804    0.000   42.942    0.000 random.py:250(_randbelow_with_getrandbits)
               55008059   28.555    0.000   42.616    0.000 layer.py:96(remove)
                1315094   41.299    0.000   41.299    0.000 {built-in method nonzero}
               10199164   40.478    0.000   40.478    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                1916880    2.234    0.000   39.976    0.000 layer.py:50(restart)
                1972638    9.514    0.000   39.892    0.000 __init__.py:28(_make_grads)
               53470487   38.571    0.000   38.574    0.000 module.py:934(__getattr__)
                1972638   38.018    0.000   38.018    0.000 {built-in method gather}
                3945276    8.573    0.000   37.641    0.000 profiler.py:615(__enter__)
               66952604   37.288    0.000   37.288    0.000 {built-in method torch._C._get_tracing_state}
              384271938   35.178    0.000   35.178    0.000 layer.py:69(positions)
                2736465   34.948    0.000   34.948    0.000 {method 'long' of 'torch._C._TensorBase' objects}
              120705263   23.567    0.000   34.058    0.000 enum.py:646(__hash__)
                 639060   16.742    0.000   33.929    0.000 layers.py:33(reset)
                4602826   32.768    0.000   32.768    0.000 {built-in method zeros}
                2469644    2.961    0.000   31.166    0.000 functional.py:1553(softmax)
                 657546    3.236    0.000   30.674    0.000 exploration.py:47(epsilonGreedy)
                3945276    5.461    0.000   30.387    0.000 profiler.py:607(__init__)
                3945276   29.067    0.000   29.067    0.000 {built-in method torch._ops.profiler._record_function_enter}
                1972638   28.684    0.000   28.684    0.000 {built-in method ones_like}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-10>
Subject: Job 9457751: <test_METAk100000new_0> in cluster <dcc> Done

Job <test_METAk100000new_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed Mar 24 17:29:15 2021
Job was executed on host(s) <n-62-20-10>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed Mar 24 17:29:16 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed Mar 24 17:29:16 2021
Terminated at Wed Mar 24 21:24:37 2021
Results reported at Wed Mar 24 21:24:37 2021

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

    CPU time :                                   14077.70 sec.
    Max Memory :                                 4873 MB
    Average Memory :                             4262.23 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               3319.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   14183 sec.
    Turnaround time :                            14122 sec.

The output (if any) is above this job summary.

