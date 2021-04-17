
# Parameters

    Name :                      causal3_CF_convert0_2-0
    Main :                      CFagent
    Level :                     Levels.Causal3
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
    Cf convert :                0
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      47137155777 function calls (46869974246 primitive calls) in 86116.22 seconds

##    Ordered by: cumulative time
   List reduced from 493 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86116.220 86116.220 {built-in method builtins.exec}
                      1    4.868    4.868 86116.220 86116.220 <string>:1(<module>)
                      1  213.766  213.766 86111.352 86111.352 main.py:96(CFagent)
                8381901   32.702    0.000 32683.961    0.004 agent.py:29(learn)
                8381901  750.393    0.000 27589.525    0.003 learner.py:42(Qlearn)
        298758050/31578210 1277.374    0.000 13781.341    0.000 module.py:715(_call_impl)
               23196309   59.866    0.000 13004.450    0.001 network.py:24(forward)
               23196309  335.732    0.000 12801.777    0.001 container.py:115(forward)
                2793967   13.803    0.000 12591.859    0.005 game.py:35(step)
                2793967  105.519    0.000 12570.709    0.004 agent.py:54(_learn)
                2793967   19.239    0.000 11884.505    0.004 layers.py:448(step)
                8381901   55.114    0.000 11809.432    0.001 grad_mode.py:23(decorate_context)
                2793967  104.252    0.000 11728.179    0.004 agent.py:196(_learn)
                8381901  301.391    0.000 11655.424    0.001 adam.py:55(step)
                8381901 2152.139    0.000 10047.908    0.001 functional.py:53(adam)
                2793967 1114.951    0.000 9518.646    0.003 agent.py:204(counterfact)
                2793967 4678.017    0.002 9058.592    0.003 replaybuffer.py:28(teleporter_save_data)
                2793967   86.135    0.000 8333.599    0.003 agent.py:115(_learn)
                2793967  251.699    0.000 7576.685    0.003 layers.py:17(step)
              279396612  459.981    0.000 7298.354    0.000 layer.py:84(move)
                7406165  198.278    0.000 6620.686    0.001 agent.py:49(__call__)
                8381901   53.477    0.000 6375.328    0.001 tensor.py:181(backward)
                2793967 3853.751    0.001 6363.442    0.002 agent.py:86(interveen)
                8381901   33.097    0.000 6321.850    0.001 __init__.py:68(backward)
                8381901 6055.873    0.001 6055.873    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2793967 3275.837    0.001 4855.728    0.002 replaybuffer.py:22(sample_data)
               46392618   81.857    0.000 4511.689    0.000 conv.py:422(forward)
               46392618   90.367    0.000 4394.706    0.000 conv.py:414(_conv_forward)
               46392618 4284.906    0.000 4284.906    0.000 {built-in method conv2d}
                2793968  317.795    0.000 4263.297    0.002 layers.py:419(update)
               64000993  150.493    0.000 4240.175    0.000 linear.py:92(forward)
                2793967 2764.536    0.001 4157.025    0.001 replaybuffer.py:49(sample_data)
               64000993  262.380    0.000 4016.708    0.000 functional.py:1669(linear)
              279396612  654.290    0.000 3980.450    0.000 layers.py:465(check)
               40284848 3858.243    0.000 3858.243    0.000 {built-in method tensor}
              240852266 3810.650    0.000 3810.650    0.000 {built-in method clone}
               33802690   25.283    0.000 3629.725    0.000 game.py:31(board)
                1820309   46.961    0.000 3444.173    0.002 agent.py:168(choose_action)
               44703480 1688.923    0.000 2985.597    0.000 layer.py:145(NoRock_update)
                2793967 1424.423    0.001 2894.128    0.001 agent.py:67(modify)
               64000993 2865.008    0.000 2865.008    0.000 {built-in method addmm}
               40933769 2780.569    0.000 2780.569    0.000 {built-in method cat}
              547617616 1572.239    0.000 2457.477    0.000 tensor.py:933(grad)
              279382191  433.293    0.000 2434.051    0.000 layers.py:459(isFree)
                8381901  222.043    0.000 2379.620    0.000 optimizer.py:167(zero_grad)
              156462152 2124.806    0.000 2124.806    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
             2022853596 1665.897    0.000 2000.757    0.000 layer.py:81(isFree)
               87197302   76.152    0.000 1944.932    0.000 activation.py:713(forward)
               87197302  128.476    0.000 1868.780    0.000 functional.py:1292(leaky_relu)
               10200132   76.810    0.000 1798.529    0.000 agent.py:59(modify_board)
              156462152 1773.755    0.000 1773.755    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                2793967   48.119    0.000 1746.252    0.001 agent.py:164(__call__)
               87197302 1728.982    0.000 1728.982    0.000 {built-in method torch._C._nn.leaky_relu}
                2793967   47.385    0.000 1614.196    0.001 agent.py:110(__call__)
                2793967   76.122    0.000 1370.180    0.000 replaybuffer.py:18(stacker)
                4042714   44.725    0.000 1246.141    0.000 layers.py:469(restart)
              710255509  407.685    0.000 1202.889    0.000 overrides.py:1070(has_torch_function)
                2793967   55.117    0.000 1185.386    0.000 replaybuffer.py:45(stacker)
               78231076 1143.624    0.000 1143.624    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              253846365 1137.869    0.000 1137.869    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                2793967  474.749    0.000 1130.287    0.000 replaybuffer.py:55(CF_save_data)
               10200132 1120.790    0.000 1120.790    0.000 {built-in method torch._C._nn.one_hot}
              299803224  168.432    0.000 1071.782    0.000 {built-in method builtins.all}
             4031570014  746.489    0.000 1065.283    0.000 enum.py:646(__hash__)
               78231076 1040.225    0.000 1040.225    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               20406424  126.718    0.000  999.713    0.000 tensor.py:21(wrapped)
              279396612  604.889    0.000  975.880    0.000 layers.py:233(check)
               78231076  939.429    0.000  939.429    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
             1671878274  441.960    0.000  924.442    0.000 layers.py:425(<genexpr>)
              279396612  547.138    0.000  915.822    0.000 layers.py:270(check)
                4042714   21.281    0.000  851.591    0.000 level.py:8(__init__)
               78231076  849.023    0.000  849.023    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              793814272  312.904    0.000  760.292    0.000 {built-in method builtins.any}
                2793967  434.955    0.000  731.134    0.000 collector.py:54(collect)
             1026417994  726.563    0.000  726.563    0.000 layer.py:124(elements)
                7406165  251.999    0.000  703.689    0.000 exploration.py:53(softmaxer)
                4042714   87.846    0.000  667.465    0.000 levels.py:164(generate)
               78231076  665.856    0.000  665.856    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                1820309  455.273    0.000  643.883    0.000 agent.py:179(convert_values)
               64000993  582.441    0.000  582.441    0.000 {method 't' of 'torch._C._TensorBase' objects}
                8381901   15.494    0.000  515.731    0.000 loss.py:445(forward)
                8381901   48.985    0.000  500.237    0.000 functional.py:2637(mse_loss)
              279396612  321.721    0.000  497.351    0.000 layers.py:257(check)
               13673362  185.637    0.000  488.023    0.000 random.py:315(sample)
        5223619488/5223619485  368.846    0.000  486.180    0.000 {built-in method builtins.len}
              279396612  305.045    0.000  482.399    0.000 layers.py:294(check)
                8085428   71.543    0.000  464.439    0.000 level.py:41(notUsed)
             1504917695  354.052    0.000  441.782    0.000 overrides.py:1083(<genexpr>)
             4831830128  436.981    0.000  436.981    0.000 layer.py:77(positions)
                8381902  425.065    0.000  425.065    0.000 {built-in method nonzero}
              279396612  259.255    0.000  385.212    0.000 layers.py:42(check)
                5589414  376.633    0.000  376.633    0.000 {method 'ne' of 'torch._C._TensorBase' objects}
               46392618   33.114    0.000  345.574    0.000 flatten.py:39(forward)
               32341712   41.842    0.000  338.523    0.000 layer.py:58(restart)
             4031601965  318.800    0.000  318.800    0.000 {built-in method builtins.hash}
                8381901  317.064    0.000  317.064    0.000 {built-in method torch._C._nn.mse_loss}
               46392618  312.459    0.000  312.459    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              166100626  208.739    0.000  305.768    0.000 layers.py:100(isDone)
               11175868   56.870    0.000  295.229    0.000 tensor.py:506(__rsub__)
               16763802  293.486    0.000  293.486    0.000 {built-in method sum}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-13>
Subject: Job 9496011: <causal3_CF_convert0_2_0> in cluster <dcc> Done

Job <causal3_CF_convert0_2_0> was submitted from host <n-62-27-19> by user <s183905> in cluster <dcc> at Mon Apr  5 20:05:17 2021
Job was executed on host(s) <n-62-20-13>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Mon Apr  5 20:31:15 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Apr  5 20:31:15 2021
Terminated at Tue Apr  6 20:26:44 2021
Results reported at Tue Apr  6 20:26:44 2021

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

    CPU time :                                   85899.87 sec.
    Max Memory :                                 3401 MB
    Average Memory :                             3342.34 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               12983.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86128 sec.
    Turnaround time :                            87687 sec.

The output (if any) is above this job summary.

