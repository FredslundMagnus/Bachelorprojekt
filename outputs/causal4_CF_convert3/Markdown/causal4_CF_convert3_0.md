
# Parameters

    Name :                      causal4_CF_convert3-0
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
    Cf convert :                3
    Minutes used :              955 minutes.
    Hours used :                15 hours.

# Profiling


      39809483987 function calls (39586252336 primitive calls) in 57316.77 seconds

##    Ordered by: cumulative time
   List reduced from 508 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 57316.774 57316.774 {built-in method builtins.exec}
                      1    5.212    5.212 57316.774 57316.774 <string>:1(<module>)
                      1  198.213  198.213 57311.563 57311.563 main.py:96(CFagent)
                7363200   29.569    0.000 18405.188    0.002 agent.py:29(learn)
                7363197  467.092    0.000 14849.051    0.002 learner.py:42(Qlearn)
                2454400   13.020    0.000 13005.239    0.005 game.py:35(step)
                2454400   17.098    0.000 12417.950    0.005 layers.py:448(step)
                2454400  237.363    0.000 9109.374    0.004 layers.py:17(step)
              245054226  669.249    0.000 8846.046    0.000 layer.py:84(move)
        250013787/26783827 1051.576    0.000 8327.352    0.000 module.py:866(_call_impl)
               19420630   51.266    0.000 7759.097    0.000 network.py:24(forward)
               19420630  261.860    0.000 7574.267    0.000 container.py:117(forward)
                2454400  592.909    0.000 7253.814    0.003 agent.py:201(counterfact)
                2454400  299.923    0.000 7210.441    0.003 agent.py:54(_learn)
                2454400  293.212    0.000 6548.249    0.003 agent.py:193(_learn)
                7363197   65.978    0.000 5751.055    0.001 optimizer.py:84(wrapper)
                7363197   35.289    0.000 5459.934    0.001 grad_mode.py:24(decorate_context)
                7363197  244.112    0.000 5347.998    0.001 adam.py:55(step)
              245054226  794.668    0.000 5028.934    0.000 layers.py:465(check)
                7363197 1124.545    0.000 4846.075    0.001 _functional.py:53(adam)
                2454400   74.205    0.000 4599.381    0.002 agent.py:115(_learn)
                2454400 3497.205    0.001 4408.706    0.002 replaybuffer.py:22(sample_data)
                6026851  178.218    0.000 4031.337    0.001 agent.py:49(__call__)
               38320751 4002.147    0.000 4002.147    0.000 {built-in method tensor}
                7363197   30.842    0.000 3891.186    0.001 tensor.py:195(backward)
                7363197   32.168    0.000 3859.244    0.001 __init__.py:68(backward)
               32587806   20.741    0.000 3856.068    0.000 game.py:31(board)
                2454400 2938.328    0.001 3722.765    0.002 replaybuffer.py:49(sample_data)
                7363197 3676.839    0.000 3676.839    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
               49088010 2051.617    0.000 3549.358    0.000 layer.py:129(update)
                2454400 1971.923    0.001 3362.943    0.001 replaybuffer.py:28(teleporter_save_data)
                2454401  278.767    0.000 3265.258    0.001 layers.py:419(update)
                2454400 1458.753    0.001 3067.232    0.001 agent.py:86(interveen)
               38841260   86.505    0.000 2809.990    0.000 conv.py:398(forward)
              244989767  489.464    0.000 2700.018    0.000 layers.py:459(isFree)
               38841260   59.383    0.000 2678.321    0.000 conv.py:390(_conv_forward)
               38841260 2618.938    0.000 2618.938    0.000 {built-in method conv2d}
             2149523726 1855.484    0.000 2210.554    0.000 layer.py:81(isFree)
               53353090  108.679    0.000 2118.160    0.000 linear.py:93(forward)
               53353090   44.758    0.000 1950.443    0.000 functional.py:1737(linear)
               53353090 1895.106    0.000 1895.106    0.000 {built-in method torch._C._nn.linear}
                2454400  998.582    0.000 1667.653    0.001 agent.py:67(modify)
               35479636 1386.501    0.000 1386.501    0.000 {built-in method cat}
                1121785   24.743    0.000 1333.337    0.001 agent.py:168(choose_action)
              130697075 1308.651    0.000 1308.651    0.000 {built-in method clone}
                8481251   58.242    0.000 1141.208    0.000 agent.py:59(modify_board)
                2454397   49.906    0.000 1132.819    0.000 agent.py:164(__call__)
               72773720   59.457    0.000 1116.274    0.000 activation.py:713(forward)
                2454400   47.972    0.000 1075.760    0.000 agent.py:110(__call__)
               72773720   62.224    0.000 1056.817    0.000 functional.py:1364(leaky_relu)
             3981535838  715.788    0.000 1022.015    0.000 enum.py:646(__hash__)
               72773720  982.800    0.000  982.800    0.000 {built-in method torch._C._nn.leaky_relu}
              137446340  946.317    0.000  946.317    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              245054226  593.792    0.000  895.354    0.000 layers.py:233(check)
              773733808  876.863    0.000  876.863    0.000 layer.py:124(elements)
                7363197  152.601    0.000  835.077    0.000 optimizer.py:189(zero_grad)
              137446340  833.524    0.000  833.524    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              245054226  485.571    0.000  790.099    0.000 layers.py:270(check)
                8481251  755.149    0.000  755.149    0.000 {built-in method torch._C._nn.one_hot}
              245054226  574.292    0.000  737.365    0.000 layers.py:67(check)
                2454400   60.953    0.000  716.690    0.000 replaybuffer.py:18(stacker)
                2013223   28.439    0.000  713.190    0.000 layers.py:469(restart)
                2454397   56.201    0.000  596.628    0.000 replaybuffer.py:45(stacker)
              245054226  451.064    0.000  568.029    0.000 layers.py:56(check)
               68723170  546.168    0.000  546.168    0.000 {method 'add' of 'torch._C._TensorBase' objects}
             5458531654  506.452    0.000  506.452    0.000 layer.py:77(positions)
               68723170  490.773    0.000  490.773    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                2013223   12.651    0.000  484.294    0.000 level.py:8(__init__)
                2454400  192.436    0.000  476.982    0.000 replaybuffer.py:55(CF_save_data)
               68723170  443.856    0.000  443.856    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               68723170  442.047    0.000  442.047    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
        5975973578/5975973575  394.724    0.000  441.992    0.000 {built-in method builtins.len}
                6026851  148.592    0.000  417.294    0.000 exploration.py:53(softmaxer)
              245054226  267.965    0.000  416.122    0.000 layers.py:257(check)
                8935246  153.957    0.000  408.842    0.000 random.py:315(sample)
              481062274  321.296    0.000  398.439    0.000 tensor.py:906(grad)
                2013223   72.413    0.000  393.434    0.000 levels.py:199(generate)
              245054226  252.764    0.000  391.466    0.000 layers.py:294(check)
                2454400  222.214    0.000  376.040    0.000 collector.py:54(collect)
              245054226  254.689    0.000  368.364    0.000 layers.py:42(check)
              245440100   57.395    0.000  356.761    0.000 {built-in method builtins.all}
                7363197   11.610    0.000  338.478    0.000 loss.py:527(forward)
              620144227  143.675    0.000  327.133    0.000 layers.py:425(<genexpr>)
                7363197   31.584    0.000  326.867    0.000 functional.py:2898(mse_loss)
               68723170  325.437    0.000  325.437    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                7363201  313.657    0.000  313.657    0.000 {built-in method nonzero}
             3981563981  306.233    0.000  306.233    0.000 {built-in method builtins.hash}
              141632723  290.669    0.000  290.669    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                4026446   31.266    0.000  252.042    0.000 level.py:41(notUsed)
              220397941  161.549    0.000  233.829    0.000 layer.py:104(remove)
              338304839  151.568    0.000  211.144    0.000 layer.py:108(add)
               49088010  210.246    0.000  210.246    0.000 layer.py:141(<listcomp>)
              298995329  139.450    0.000  205.526    0.000 random.py:250(_randbelow_with_getrandbits)
             1741654251  202.290    0.000  202.290    0.000 layer.py:181(isBlocking)
                7363197  199.603    0.000  199.603    0.000 {built-in method torch._C._nn.mse_loss}
               20132230   29.116    0.000  193.519    0.000 layer.py:58(restart)
               38841260   29.223    0.000  186.176    0.000 flatten.py:39(forward)
                7364044  179.995    0.000  179.995    0.000 {built-in method max}
               10939382   17.930    0.000  169.878    0.000 tensor.py:525(__rsub__)
               14726400  161.447    0.000  161.447    0.000 {built-in method sum}


Traceback (most recent call last):
  File "main.py", line 185, in <module>
    run(Defaults)
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/auxillaries.py", line 132, in run
    (serverRun if isServer else Defaults.main).__call__(getvals(Defaults))
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils/server.py", line 36, in serverRun
    profilingStats()
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils/debug.py", line 62, in profilingStats
    os.remove('stats')
FileNotFoundError: [Errno 2] No such file or directory: 'stats'

------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-10>
Subject: Job 9495293: <causal4_CF_convert3_0> in cluster <dcc> Exited

Job <causal4_CF_convert3_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon Apr  5 02:37:26 2021
Job was executed on host(s) <n-62-20-10>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon Apr  5 02:37:27 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Apr  5 02:37:27 2021
Terminated at Mon Apr  5 18:32:54 2021
Results reported at Mon Apr  5 18:32:54 2021

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

Exited with exit code 1.

Resource usage summary:

    CPU time :                                   57170.19 sec.
    Max Memory :                                 7952 MB
    Average Memory :                             5626.27 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               8432.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   57342 sec.
    Turnaround time :                            57328 sec.

The output (if any) is above this job summary.

