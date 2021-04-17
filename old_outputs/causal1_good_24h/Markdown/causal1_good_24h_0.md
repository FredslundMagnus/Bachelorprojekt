
# Parameters

    Name :                      causal1_good_24h-0
    Main :                      teleport
    Level :                     Levels.Causal1
    Hours :                     24.0
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
    Layer keys :                True
    Layer door :                True
    Layer holder :              True
    Layer putter :              True
    Layer rock :                True
    Layer dirt :                True
    Layer diamond1 :            True
    Layer diamond2 :            True
    Layer diamond3 :            True
    Layer diamond4 :            True
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
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      103484600544 function calls (103247220421 primitive calls) in 86112.84 seconds

##    Ordered by: cumulative time
   List reduced from 481 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86112.842 86112.842 {built-in method builtins.exec}
                      1    1.941    1.941 86112.842 86112.842 <string>:1(<module>)
                      1  190.852  190.852 86110.901 86110.901 main.py:43(teleport)
                4239274   16.551    0.000 31356.630    0.007 game.py:27(step)
                4239274   23.247    0.000 30059.037    0.007 layers.py:475(step)
                8478548   29.188    0.000 22260.927    0.003 agent.py:27(learn)
                4239274  324.733    0.000 20647.402    0.005 layers.py:18(step)
              423927400  966.207    0.000 20286.820    0.000 layer.py:76(move)
                8478548  528.341    0.000 18685.084    0.002 learner.py:42(Qlearn)
              423927400 2197.058    0.000 13776.334    0.000 layers.py:492(check)
                4239274  133.377    0.000 13481.160    0.003 agent.py:52(_learn)
                4239274 6639.481    0.002 11879.188    0.003 replaybuffer.py:29(teleporter_save_data)
                4239275  460.319    0.000 9357.469    0.002 layers.py:446(update)
        267052344/29673232  989.884    0.000 9315.132    0.000 module.py:715(_call_impl)
                4239274  108.982    0.000 8732.459    0.002 agent.py:113(_learn)
               21194684   49.724    0.000 8686.488    0.000 network.py:24(forward)
               21194684  232.394    0.000 8508.139    0.000 container.py:115(forward)
                4239274 5089.623    0.001 7953.059    0.002 agent.py:84(interveen)
                8478548   48.684    0.000 7456.469    0.001 grad_mode.py:23(decorate_context)
                8478548  251.801    0.000 7319.516    0.001 adam.py:55(step)
                8478548 1339.855    0.000 5986.441    0.001 functional.py:53(adam)
                8476862  177.259    0.000 5767.245    0.001 agent.py:47(__call__)
                4239274 3766.328    0.001 5738.506    0.001 replaybuffer.py:23(sample_data)
              423927400 1304.247    0.000 4892.127    0.000 layers.py:486(isFree)
               76306950 2582.969    0.000 4492.889    0.000 layer.py:121(update)
                8478548   46.446    0.000 4366.159    0.001 tensor.py:181(backward)
                8478548   28.443    0.000 4319.713    0.001 __init__.py:68(backward)
              434001734 4185.793    0.000 4185.793    0.000 {built-in method clone}
                8478548 4109.575    0.000 4109.575    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
             7273960653 2738.708    0.000 3587.879    0.000 layer.py:73(isFree)
            14546455155 2359.962    0.000 3373.089    0.000 enum.py:646(__hash__)
                4239274 1669.657    0.000 3322.813    0.001 agent.py:65(modify)
               42389368   65.775    0.000 3153.100    0.000 conv.py:422(forward)
               42389368   79.140    0.000 3059.432    0.000 conv.py:414(_conv_forward)
               10803312  145.171    0.000 3056.948    0.000 layers.py:496(restart)
               42389368 2966.563    0.000 2966.563    0.000 {built-in method conv2d}
               55105504  109.727    0.000 2714.094    0.000 linear.py:92(forward)
               55105504  192.031    0.000 2551.272    0.000 functional.py:1669(linear)
               18139770 2057.048    0.000 2057.048    0.000 {built-in method tensor}
               10803312   63.463    0.000 1995.591    0.000 level.py:8(__init__)
               38151780 1974.962    0.000 1974.962    0.000 {built-in method cat}
              534148578 1161.873    0.000 1929.398    0.000 tensor.py:933(grad)
                4239274   50.730    0.000 1829.672    0.000 agent.py:108(__call__)
               55105504 1800.342    0.000 1800.342    0.000 {built-in method addmm}
                8478548    9.796    0.000 1776.190    0.000 game.py:23(board)
               12716136   85.249    0.000 1755.247    0.000 agent.py:57(modify_board)
               10803312  119.362    0.000 1728.437    0.000 levels.py:122(generate)
                4239274   71.787    0.000 1682.138    0.000 replaybuffer.py:19(stacker)
                8478548  161.338    0.000 1678.649    0.000 optimizer.py:167(zero_grad)
               42133791  307.138    0.000 1502.657    0.000 level.py:41(notUsed)
            17015699568 1486.636    0.000 1486.636    0.000 layer.py:69(positions)
             1791969991 1216.549    0.000 1216.549    0.000 layer.py:116(elements)
              445126082  145.108    0.000 1207.833    0.000 {built-in method builtins.all}
              152613864 1202.216    0.000 1202.216    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               76300188   57.202    0.000 1181.348    0.000 activation.py:713(forward)
               12716136 1130.812    0.000 1130.812    0.000 {built-in method torch._C._nn.one_hot}
              446717870 1124.814    0.000 1124.814    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               76300188   98.714    0.000 1124.145    0.000 functional.py:1292(leaky_relu)
             1445906180  354.022    0.000 1097.027    0.000 layers.py:452(<genexpr>)
              423927400  697.932    0.000 1092.778    0.000 layers.py:261(check)
              423927400  686.743    0.000 1087.520    0.000 layers.py:173(check)
              423927400  684.529    0.000 1086.960    0.000 layers.py:302(check)
              423927400  668.914    0.000 1077.580    0.000 layers.py:230(check)
              423927400  665.956    0.000 1073.436    0.000 layers.py:216(check)
              686758839  347.037    0.000 1033.855    0.000 overrides.py:1070(has_torch_function)
              423927400  635.691    0.000 1026.631    0.000 layers.py:244(check)
               76300188 1015.439    0.000 1015.439    0.000 {built-in method torch._C._nn.leaky_relu}
            14546486010 1013.132    0.000 1013.132    0.000 {built-in method builtins.hash}
              152613864 1012.243    0.000 1012.243    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              423927400  685.401    0.000  938.824    0.000 layers.py:76(check)
              194459616  129.005    0.000  861.028    0.000 layer.py:50(restart)
               21198582  103.744    0.000  779.926    0.000 tensor.py:21(wrapped)
              423927400  454.896    0.000  708.351    0.000 layers.py:142(check)
                4239274  411.832    0.000  704.541    0.000 collector.py:54(collect)
               76306932  700.741    0.000  700.741    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              423927500  455.397    0.000  673.201    0.000 layers.py:110(isDone)
              423927400  414.004    0.000  653.746    0.000 layers.py:287(check)
              758821440  265.357    0.000  650.152    0.000 {built-in method builtins.any}
               76306932  643.012    0.000  643.012    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              423927400  409.442    0.000  642.806    0.000 layers.py:328(check)
                8476862  218.685    0.000  592.376    0.000 exploration.py:53(softmaxer)
               76306932  576.846    0.000  576.846    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
             6060194359  565.896    0.000  565.896    0.000 layer.py:177(isBlocking)
              423927400  368.119    0.000  551.245    0.000 layers.py:123(check)
               42133791   30.059    0.000  540.730    0.000 level.py:38(elementsIn)
              423927400  354.144    0.000  533.954    0.000 layers.py:47(check)
               10803412  257.183    0.000  519.361    0.000 layers.py:33(reset)
              423927400  328.007    0.000  497.491    0.000 layers.py:63(check)
               76306932  491.608    0.000  491.608    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
             1943521057  486.703    0.000  486.703    0.000 level.py:32(inverse)
              423927400  317.778    0.000  484.707    0.000 layers.py:203(check)
        6201083462/6201083460  360.336    0.000  472.667    0.000 {built-in method builtins.len}
              824917496  312.673    0.000  423.969    0.000 layer.py:100(add)
                8478548   11.011    0.000  399.286    0.000 loss.py:445(forward)
               76306932  393.736    0.000  393.736    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                8478548   44.164    0.000  388.275    0.000 functional.py:2637(mse_loss)
             1449820917  307.068    0.000  379.297    0.000 overrides.py:1083(<genexpr>)
               42133791  164.280    0.000  329.312    0.000 level.py:39(<listcomp>)
               55105504  323.278    0.000  323.278    0.000 {method 't' of 'torch._C._TensorBase' objects}
              420329880  214.302    0.000  309.680    0.000 layer.py:96(remove)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-6>
Subject: Job 9474544: <causal1_good_24h_0> in cluster <dcc> Done

Job <causal1_good_24h_0> was submitted from host <n-62-27-21> by user <s183905> in cluster <dcc> at Sun Mar 28 11:07:12 2021
Job was executed on host(s) <n-62-20-6>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sun Mar 28 11:07:13 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun Mar 28 11:07:13 2021
Terminated at Mon Mar 29 11:02:38 2021
Results reported at Mon Mar 29 11:02:38 2021

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

    CPU time :                                   85901.67 sec.
    Max Memory :                                 2821 MB
    Average Memory :                             2815.53 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13563.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86150 sec.
    Turnaround time :                            86126 sec.

The output (if any) is above this job summary.

