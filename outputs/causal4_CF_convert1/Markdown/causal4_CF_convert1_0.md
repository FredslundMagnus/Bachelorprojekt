
# Parameters

    Name :                      causal4_CF_convert1-0
    Main :                      CFagent
    Level :                     Levels.Causal4
    Hours :                     16.0
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
    Layer reddoor :             True
    Layer redkeys :             True
    Layer bluedoor :            True
    Layer bluekeys :            True
    Layer pink1 :               True
    Layer pink2 :               True
    Layer pink3 :               True
    Layer brown1 :              True
    Layer brown2 :              True
    Layer brown3 :              True
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                1
    Minutes used :              955 minutes.
    Hours used :                15 hours.

# Profiling


      45696790494 function calls (45457309367 primitive calls) in 57313.17 seconds

##    Ordered by: cumulative time
   List reduced from 507 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 57313.169 57313.169 {built-in method builtins.exec}
                      1    4.620    4.620 57313.169 57313.169 <string>:1(<module>)
                      1  165.367  165.367 57308.549 57308.549 main.py:96(CFagent)
                7743846   28.626    0.000 18656.433    0.002 agent.py:29(learn)
                7743845  470.620    0.000 15218.312    0.002 learner.py:42(Qlearn)
                2581282   12.120    0.000 13425.790    0.005 game.py:35(step)
                2581282   14.677    0.000 12843.977    0.005 layers.py:448(step)
                2581282  234.216    0.000 8758.093    0.003 layers.py:17(step)
        268040328/28560892 1077.285    0.000 8623.157    0.000 module.py:866(_call_impl)
              258128200  658.389    0.000 8500.267    0.000 layer.py:84(move)
               20817047   55.982    0.000 8054.005    0.000 network.py:24(forward)
               20817047  266.259    0.000 7862.921    0.000 container.py:117(forward)
                2581282  662.395    0.000 7356.793    0.003 agent.py:201(counterfact)
                2581282  257.017    0.000 7247.708    0.003 agent.py:54(_learn)
                2581282  253.662    0.000 6652.737    0.003 agent.py:193(_learn)
                7743845   64.659    0.000 6044.999    0.001 optimizer.py:84(wrapper)
                7743845   34.076    0.000 5757.678    0.001 grad_mode.py:24(decorate_context)
                7743845  226.326    0.000 5653.113    0.001 adam.py:55(step)
                7743845 1201.506    0.000 5162.874    0.001 _functional.py:53(adam)
              258128200  827.541    0.000 4992.873    0.000 layers.py:465(check)
                2581282   77.093    0.000 4712.081    0.002 agent.py:115(_learn)
                6535160  164.894    0.000 4135.143    0.001 agent.py:49(__call__)
               41119357 4093.228    0.000 4093.228    0.000 {built-in method tensor}
                2581283  277.506    0.000 4050.692    0.002 layers.py:419(update)
                2581282 2233.899    0.001 3966.188    0.002 replaybuffer.py:28(teleporter_save_data)
               35106917   21.462    0.000 3950.487    0.000 game.py:31(board)
                7743845   30.951    0.000 3864.835    0.000 tensor.py:195(backward)
                7743845   28.884    0.000 3832.844    0.000 __init__.py:68(backward)
                7743845 3652.975    0.000 3652.975    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2581282 2653.821    0.001 3510.397    0.001 replaybuffer.py:22(sample_data)
                2581282 1659.084    0.001 3283.556    0.001 agent.py:86(interveen)
               51625650 1890.770    0.000 3242.033    0.000 layer.py:129(update)
                2581282 2227.664    0.001 2981.735    0.001 replaybuffer.py:49(sample_data)
               41634094   92.299    0.000 2896.357    0.000 conv.py:398(forward)
               41634094   62.199    0.000 2761.211    0.000 conv.py:390(_conv_forward)
               41634094 2699.012    0.000 2699.012    0.000 {built-in method conv2d}
              258091709  484.288    0.000 2418.744    0.000 layers.py:459(isFree)
               57288577  113.529    0.000 2210.241    0.000 linear.py:93(forward)
               57288577   46.984    0.000 2038.904    0.000 functional.py:1737(linear)
               57288577 1980.606    0.000 1980.606    0.000 {built-in method torch._C._nn.linear}
             2371178866 1567.240    0.000 1934.456    0.000 layer.py:81(isFree)
                2581282  983.771    0.000 1651.007    0.001 agent.py:67(modify)
              168111990 1631.588    0.000 1631.588    0.000 {built-in method clone}
                1375479   26.439    0.000 1491.167    0.001 agent.py:168(choose_action)
               37510539 1333.535    0.000 1333.535    0.000 {built-in method cat}
               78105624   64.868    0.000 1180.112    0.000 activation.py:713(forward)
                9116442   59.082    0.000 1159.191    0.000 agent.py:59(modify_board)
                2581281   41.137    0.000 1134.061    0.000 agent.py:164(__call__)
             4496353902  790.699    0.000 1129.804    0.000 enum.py:646(__hash__)
               78105624   65.797    0.000 1115.244    0.000 functional.py:1364(leaky_relu)
                2581282   39.266    0.000 1076.527    0.000 agent.py:110(__call__)
               78105624 1036.786    0.000 1036.786    0.000 {built-in method torch._C._nn.leaky_relu}
              258128300  150.883    0.000 1026.061    0.000 {built-in method builtins.all}
              144551772  995.584    0.000  995.584    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
             1557537730  398.929    0.000  906.943    0.000 layers.py:425(<genexpr>)
                2756058   30.854    0.000  904.442    0.000 layers.py:469(restart)
              144551772  899.749    0.000  899.749    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                7743845  155.926    0.000  879.858    0.000 optimizer.py:189(zero_grad)
              258128200  521.171    0.000  845.049    0.000 layers.py:233(check)
              258128200  485.737    0.000  810.382    0.000 layers.py:270(check)
                9116442  758.574    0.000  758.574    0.000 {built-in method torch._C._nn.one_hot}
              258128200  583.707    0.000  751.622    0.000 layers.py:67(check)
              918629594  748.335    0.000  748.335    0.000 layer.py:124(elements)
                2581282   57.901    0.000  670.189    0.000 replaybuffer.py:18(stacker)
                2756058   14.866    0.000  612.086    0.000 level.py:8(__init__)
               72275886  595.029    0.000  595.029    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                2581281   53.568    0.000  573.871    0.000 replaybuffer.py:45(stacker)
             6216115965  569.298    0.000  569.298    0.000 layer.py:77(positions)
                2581282  228.764    0.000  549.328    0.000 replaybuffer.py:55(CF_save_data)
               72275886  518.753    0.000  518.753    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              258128200  383.028    0.000  509.149    0.000 layers.py:56(check)
                2756058   90.324    0.000  507.003    0.000 levels.py:199(generate)
               72275886  466.539    0.000  466.539    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               72275886  465.578    0.000  465.578    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
        6245169124/6245169121  396.168    0.000  447.925    0.000 {built-in method builtins.len}
              258128200  283.397    0.000  438.088    0.000 layers.py:294(check)
              258128300  292.558    0.000  433.649    0.000 layers.py:100(isDone)
              505931286  336.328    0.000  417.533    0.000 tensor.py:906(grad)
              258128200  261.178    0.000  409.176    0.000 layers.py:257(check)
                6535160  152.367    0.000  407.570    0.000 exploration.py:53(softmaxer)
               10674680  150.015    0.000  400.082    0.000 random.py:315(sample)
                2581282  234.309    0.000  396.009    0.000 collector.py:54(collect)
              179809713  351.732    0.000  351.732    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               72275886  346.909    0.000  346.909    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
             4496383501  339.111    0.000  339.111    0.000 {built-in method builtins.hash}
              258128200  225.957    0.000  338.384    0.000 layers.py:42(check)
                5512116   40.317    0.000  328.811    0.000 level.py:41(notUsed)
                7743845   10.533    0.000  328.796    0.000 loss.py:527(forward)
                7743845   28.881    0.000  318.263    0.000 functional.py:2898(mse_loss)
                7743847  299.097    0.000  299.097    0.000 {built-in method nonzero}
               27560580   38.844    0.000  252.451    0.000 layer.py:58(restart)
              251869500  175.128    0.000  245.285    0.000 layer.py:104(remove)
              408697390  164.053    0.000  225.166    0.000 layer.py:108(add)
              331485047  147.121    0.000  215.683    0.000 random.py:250(_randbelow_with_getrandbits)
               51625650  197.248    0.000  197.248    0.000 layer.py:141(<listcomp>)
               41634094   27.151    0.000  193.724    0.000 flatten.py:39(forward)
                7743845  193.702    0.000  193.702    0.000 {built-in method torch._C._nn.mse_loss}
             1859808229  185.250    0.000  185.250    0.000 layer.py:181(isBlocking)
                7744756  179.220    0.000  179.220    0.000 {built-in method max}
               15487692  166.858    0.000  166.858    0.000 {built-in method sum}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-11-16>
Subject: Job 9495291: <causal4_CF_convert1_0> in cluster <dcc> Done

Job <causal4_CF_convert1_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon Apr  5 02:37:26 2021
Job was executed on host(s) <n-62-11-16>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon Apr  5 02:37:27 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Apr  5 02:37:27 2021
Terminated at Mon Apr  5 18:32:49 2021
Results reported at Mon Apr  5 18:32:49 2021

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

    CPU time :                                   57165.54 sec.
    Max Memory :                                 8182 MB
    Average Memory :                             5777.79 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               8202.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   57351 sec.
    Turnaround time :                            57323 sec.

The output (if any) is above this job summary.

