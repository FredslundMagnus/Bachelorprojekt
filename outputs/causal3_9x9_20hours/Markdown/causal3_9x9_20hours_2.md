
# Parameters

    Name :                      causal3_9x9_20hours-2
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
    Minutes used :              1195 minutes.
    Hours used :                19 hours.

# Profiling


      68414303583 function calls (68118868956 primitive calls) in 71709.72 seconds

##    Ordered by: cumulative time
   List reduced from 475 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 71709.716 71709.716 {built-in method builtins.exec}
                      1    1.808    1.808 71709.716 71709.716 <string>:1(<module>)
                      1  213.884  213.884 71707.907 71707.907 main.py:43(teleport)
               10557108   37.024    0.000 23605.159    0.002 agent.py:27(learn)
                5278554   20.724    0.000 22016.027    0.004 game.py:27(step)
                5278554   28.713    0.000 20920.711    0.004 layers.py:475(step)
               10557108  603.664    0.000 20001.797    0.002 learner.py:42(Qlearn)
                5278554  156.292    0.000 14089.243    0.003 agent.py:52(_learn)
                5278554  433.882    0.000 14041.901    0.003 layers.py:18(step)
              527855400  693.863    0.000 13560.594    0.000 layer.py:76(move)
        332369710/36936094 1284.797    0.000 10330.803    0.000 module.py:866(_call_impl)
               26378986   73.820    0.000 9595.047    0.000 network.py:24(forward)
                5278554  134.300    0.000 9459.269    0.002 agent.py:112(_learn)
               26378986  320.451    0.000 9354.633    0.000 container.py:117(forward)
              527855400 1420.190    0.000 8330.934    0.000 layers.py:492(check)
               10557108   89.791    0.000 7839.685    0.001 optimizer.py:84(wrapper)
               10557108   44.265    0.000 7443.061    0.001 grad_mode.py:24(decorate_context)
               10557108  283.086    0.000 7302.762    0.001 adam.py:55(step)
                5278554 4139.960    0.001 7260.636    0.001 replaybuffer.py:27(teleporter_save_data)
                5278555  560.403    0.000 6815.869    0.001 layers.py:446(update)
               10557108 1518.841    0.000 6674.532    0.001 _functional.py:53(adam)
               10543324  215.750    0.000 6377.696    0.001 agent.py:47(__call__)
                5278554 3105.266    0.001 6255.494    0.001 agent.py:83(interveen)
                5278554 4034.490    0.001 5653.709    0.001 replaybuffer.py:23(sample_data)
               10557108   48.733    0.000 5221.939    0.000 tensor.py:195(backward)
               10557108   42.865    0.000 5171.762    0.000 __init__.py:68(backward)
               10557108 4925.874    0.000 4925.874    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
              527855400  898.417    0.000 3935.235    0.000 layers.py:486(isFree)
               52757972  121.593    0.000 3500.922    0.000 conv.py:398(forward)
               52757972   65.449    0.000 3327.428    0.000 conv.py:390(_conv_forward)
               52757972 3261.979    0.000 3261.979    0.000 {built-in method conv2d}
                5278554 1927.467    0.000 3243.007    0.001 agent.py:64(modify)
             4173113389 2422.786    0.000 3036.818    0.000 layer.py:73(isFree)
               47506995 1540.233    0.000 2803.986    0.000 layer.py:137(NoRock_update)
              300054462 2629.870    0.000 2629.870    0.000 {built-in method clone}
               68579850  140.598    0.000 2599.273    0.000 linear.py:93(forward)
               68579850   57.424    0.000 2393.344    0.000 functional.py:1737(linear)
               68579850 2322.671    0.000 2322.671    0.000 {built-in method torch._C._nn.linear}
                5278554   63.466    0.000 2051.112    0.000 agent.py:107(__call__)
               15821878   99.772    0.000 1954.621    0.000 agent.py:56(modify_board)
             7671795335 1385.629    0.000 1927.234    0.000 enum.py:646(__hash__)
                6519025   67.078    0.000 1838.840    0.000 layers.py:496(restart)
              527855400 1059.580    0.000 1720.384    0.000 layers.py:302(check)
              527855400  969.184    0.000 1622.115    0.000 layers.py:261(check)
               22509144 1600.244    0.000 1600.244    0.000 {built-in method tensor}
               47493202 1552.786    0.000 1552.786    0.000 {built-in method cat}
              527855500  175.451    0.000 1402.966    0.000 {built-in method builtins.all}
               94958836   77.054    0.000 1375.481    0.000 activation.py:713(forward)
               10557108   11.273    0.000 1306.030    0.000 game.py:23(board)
               94958836   79.468    0.000 1298.428    0.000 functional.py:1364(leaky_relu)
             1621839626  395.298    0.000 1289.761    0.000 layers.py:452(<genexpr>)
              190027944 1280.717    0.000 1280.717    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               15821878 1272.903    0.000 1272.903    0.000 {built-in method torch._C._nn.one_hot}
                5278554   90.733    0.000 1244.944    0.000 replaybuffer.py:19(stacker)
               94958836 1203.772    0.000 1203.772    0.000 {built-in method torch._C._nn.leaky_relu}
               10557108  218.990    0.000 1197.885    0.000 optimizer.py:189(zero_grad)
                6519025   32.976    0.000 1174.780    0.000 level.py:8(__init__)
              190027944 1154.121    0.000 1154.121    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                6519025  165.416    0.000 1019.074    0.000 levels.py:163(generate)
              527855400  668.222    0.000  947.333    0.000 layers.py:63(check)
              527855400  605.040    0.000  934.723    0.000 layers.py:328(check)
            10260643170  921.393    0.000  921.393    0.000 layer.py:69(positions)
              527855400  546.789    0.000  853.559    0.000 layers.py:287(check)
              527855500  556.810    0.000  845.728    0.000 layers.py:110(isDone)
               95013972  807.891    0.000  807.891    0.000 {method 'add' of 'torch._C._TensorBase' objects}
             1908218440  801.934    0.000  801.934    0.000 layer.py:116(elements)
                5278554  455.757    0.000  775.166    0.000 collector.py:54(collect)
              527855400  463.286    0.000  698.480    0.000 layers.py:47(check)
               13038050   85.198    0.000  683.311    0.000 level.py:41(notUsed)
               95013972  655.380    0.000  655.380    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               10543324  238.118    0.000  637.286    0.000 exploration.py:53(softmaxer)
              315876340  617.096    0.000  617.096    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               95013972  616.184    0.000  616.184    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               95013972  615.242    0.000  615.242    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               58671225   77.704    0.000  577.273    0.000 layer.py:50(restart)
              665097858  449.328    0.000  555.587    0.000 tensor.py:906(grad)
             7671833678  541.612    0.000  541.612    0.000 {built-in method builtins.hash}
              909204669  377.659    0.000  508.972    0.000 layer.py:100(add)
               95013972  470.358    0.000  470.358    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               18316604  173.903    0.000  455.211    0.000 random.py:315(sample)
               10557108   13.321    0.000  434.867    0.000 loss.py:527(forward)
        5035726358/5035726356  359.222    0.000  434.196    0.000 {built-in method builtins.len}
               10557108   38.266    0.000  421.546    0.000 functional.py:2898(mse_loss)
              550072846  265.401    0.000  407.680    0.000 layer.py:96(remove)
              271197087  342.439    0.000  342.439    0.000 level.py:32(inverse)
                6519125  167.914    0.000  334.225    0.000 layers.py:33(reset)
               31671324  331.985    0.000  331.985    0.000 {built-in method sum}
             3250254792  330.724    0.000  330.724    0.000 layer.py:177(isBlocking)
              398045094  187.500    0.000  272.778    0.000 random.py:250(_randbelow_with_getrandbits)
               10557108  254.221    0.000  254.221    0.000 {built-in method torch._C._nn.mse_loss}
               52757972   36.947    0.000  239.256    0.000 flatten.py:39(forward)
             3060217789  238.457    0.000  238.457    0.000 {method 'append' of 'list' objects}
                5278554   20.665    0.000  238.280    0.000 exploration.py:47(epsilonGreedy)
               10558689  227.469    0.000  227.469    0.000 {built-in method max}
               15835662   22.222    0.000  223.606    0.000 tensor.py:525(__rsub__)
               10543324  203.406    0.000  203.406    0.000 {built-in method multinomial}
               52757972  202.309    0.000  202.309    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               13038050   12.407    0.000  200.209    0.000 level.py:38(elementsIn)
               15835662  197.691    0.000  197.691    0.000 {built-in method rsub}
               10557108   42.341    0.000  194.067    0.000 __init__.py:28(_make_grads)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-11-13>
Subject: Job 9464473: <causal3_9x9_20hours_2> in cluster <dcc> Done

Job <causal3_9x9_20hours_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Thu Mar 25 15:24:45 2021
Job was executed on host(s) <n-62-11-13>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Thu Mar 25 15:24:46 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Mar 25 15:24:46 2021
Terminated at Fri Mar 26 11:20:03 2021
Results reported at Fri Mar 26 11:20:03 2021

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

    CPU time :                                   71643.30 sec.
    Max Memory :                                 3028 MB
    Average Memory :                             3024.71 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               5164.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   71716 sec.
    Turnaround time :                            71718 sec.

The output (if any) is above this job summary.

