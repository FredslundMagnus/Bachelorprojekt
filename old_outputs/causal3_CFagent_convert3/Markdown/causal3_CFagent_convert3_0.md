
# Parameters

    Name :                      causal3_CFagent_convert3-0
    Main :                      CFagent
    Level :                     Levels.Causal3
    Hours :                     13.0
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
    Cf convert :                2
    Minutes used :              775 minutes.
    Hours used :                12 hours.

# Profiling


      28138767335 function calls (27954483660 primitive calls) in 46520.25 seconds

##    Ordered by: cumulative time
   List reduced from 489 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 46520.255 46520.255 {built-in method builtins.exec}
                      1    4.690    4.690 46520.255 46520.255 <string>:1(<module>)
                      1  148.207  148.207 46515.565 46515.565 main.py:96(CFagent)
                6097329   23.690    0.000 18210.450    0.003 agent.py:28(learn)
                6097329  456.348    0.000 15155.051    0.002 learner.py:42(Qlearn)
                2032443   11.194    0.000 7693.048    0.004 game.py:36(step)
        206413626/22131642  835.654    0.000 7572.828    0.000 module.py:866(_call_impl)
                2032443   13.222    0.000 7227.828    0.004 layers.py:594(step)
               16034313   44.107    0.000 7097.304    0.000 network.py:24(forward)
                2032443  218.755    0.000 7037.094    0.003 agent.py:53(_learn)
               16034313  224.905    0.000 6952.617    0.000 container.py:117(forward)
                2032443  214.296    0.000 6507.108    0.003 agent.py:189(_learn)
                6097329   53.548    0.000 6392.318    0.001 optimizer.py:84(wrapper)
                6097329   25.833    0.000 6141.850    0.001 grad_mode.py:24(decorate_context)
                6097329  188.526    0.000 6056.784    0.001 adam.py:55(step)
                6097329 1252.692    0.000 5667.947    0.001 _functional.py:53(adam)
                2032443  180.070    0.000 4958.531    0.002 layers.py:18(step)
              203061070  242.864    0.000 4760.523    0.000 layer.py:82(move)
                2032443  416.803    0.000 4721.442    0.002 agent.py:197(counterfact)
                2032443   61.176    0.000 4628.449    0.002 agent.py:114(_learn)
                6097329   25.211    0.000 3816.448    0.001 tensor.py:195(backward)
                6097329   23.679    0.000 3790.268    0.001 __init__.py:68(backward)
                2032443 1943.232    0.001 3640.137    0.002 replaybuffer.py:28(teleporter_save_data)
                6097329 3629.462    0.001 3629.462    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                4967300  136.336    0.000 3584.432    0.001 agent.py:48(__call__)
                2032443 2314.920    0.001 3057.539    0.002 replaybuffer.py:22(sample_data)
                2032443 1537.080    0.001 2989.209    0.001 agent.py:85(interveen)
              203061070  436.849    0.000 2670.549    0.000 layers.py:611(check)
               32068626   71.766    0.000 2516.533    0.000 conv.py:398(forward)
               28486029 2483.266    0.000 2483.266    0.000 {built-in method tensor}
                2032443 1821.027    0.001 2467.499    0.001 replaybuffer.py:49(sample_data)
               32068626   45.444    0.000 2412.132    0.000 conv.py:390(_conv_forward)
               32068626 2366.688    0.000 2366.688    0.000 {built-in method conv2d}
               22859755   16.737    0.000 2310.038    0.000 game.py:32(board)
                2032444  214.483    0.000 2236.814    0.001 layers.py:565(update)
               44038053   87.805    0.000 2007.976    0.000 linear.py:93(forward)
               32519096 1081.032    0.000 1939.751    0.000 layer.py:143(NoRock_update)
               44038053   36.963    0.000 1876.889    0.000 functional.py:1737(linear)
               44038053 1831.127    0.000 1831.127    0.000 {built-in method torch._C._nn.linear}
              202973994  273.980    0.000 1638.416    0.000 layers.py:605(isFree)
                2032443  934.331    0.000 1557.195    0.001 agent.py:66(modify)
              117644004 1536.708    0.000 1536.708    0.000 {built-in method clone}
             1335019344 1166.132    0.000 1364.436    0.000 layer.py:79(isFree)
               29356616 1190.046    0.000 1190.046    0.000 {built-in method cat}
                 904798    8.677    0.000 1177.165    0.001 agent.py:167(choose_action)
              113816808 1153.662    0.000 1153.662    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               60072366   47.081    0.000 1118.070    0.000 activation.py:713(forward)
               60072366   49.895    0.000 1070.989    0.000 functional.py:1364(leaky_relu)
                2032443   37.864    0.000 1019.761    0.001 agent.py:163(__call__)
              113816808 1012.755    0.000 1012.755    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               60072366 1009.958    0.000 1009.958    0.000 {built-in method torch._C._nn.leaky_relu}
                6999743   45.608    0.000 1001.212    0.000 agent.py:58(modify_board)
                2032443   36.761    0.000  962.962    0.000 agent.py:109(__call__)
                6097329  144.390    0.000  891.717    0.000 optimizer.py:189(zero_grad)
              203061070  417.398    0.000  652.672    0.000 layers.py:303(check)
             2647463858  448.130    0.000  642.770    0.000 enum.py:646(__hash__)
                6999743  639.920    0.000  639.920    0.000 {built-in method torch._C._nn.one_hot}
               56908404  633.815    0.000  633.815    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                2032443   51.391    0.000  597.861    0.000 replaybuffer.py:18(stacker)
              203061070  358.693    0.000  590.542    0.000 layers.py:262(check)
               56908404  556.148    0.000  556.148    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              203244400   56.388    0.000  524.728    0.000 {built-in method builtins.all}
               56908404  524.097    0.000  524.097    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               56908404  518.180    0.000  518.180    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                2032443   45.638    0.000  508.437    0.000 replaybuffer.py:45(stacker)
              571653080  498.164    0.000  498.164    0.000 layer.py:122(elements)
              620164383  142.103    0.000  491.004    0.000 layers.py:571(<genexpr>)
                1630528   18.915    0.000  467.035    0.000 layers.py:615(restart)
                2032443  167.643    0.000  439.636    0.000 replaybuffer.py:55(CF_save_data)
                2032443  251.907    0.000  416.520    0.000 collector.py:54(collect)
               56908404  405.303    0.000  405.303    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              126676190  385.163    0.000  385.163    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                4967300  136.949    0.000  377.720    0.000 exploration.py:53(softmaxer)
              203061070  225.690    0.000  352.604    0.000 layers.py:329(check)
              398358912  268.440    0.000  332.741    0.000 tensor.py:906(grad)
              203244400  225.194    0.000  329.722    0.000 layers.py:111(isDone)
              203061070  203.977    0.000  319.798    0.000 layers.py:288(check)
                1630528    9.449    0.000  317.839    0.000 level.py:8(__init__)
             3510721309  306.557    0.000  306.557    0.000 layer.py:75(positions)
                7325942  114.191    0.000  306.415    0.000 random.py:315(sample)
        3914995813/3914995810  258.556    0.000  298.685    0.000 {built-in method builtins.len}
                6097329    8.878    0.000  292.513    0.000 loss.py:527(forward)
                6097329   23.360    0.000  283.636    0.000 functional.py:2898(mse_loss)
                6097330  270.183    0.000  270.183    0.000 {built-in method nonzero}
              203061070  181.264    0.000  267.597    0.000 layers.py:47(check)
                1630528   35.125    0.000  252.944    0.000 levels.py:164(generate)
                2937241   15.748    0.000  244.369    0.000 exploration.py:47(epsilonGreedy)
             2647487297  194.645    0.000  194.645    0.000 {built-in method builtins.hash}
                6097329  186.418    0.000  186.418    0.000 {built-in method torch._C._nn.mse_loss}
               32068626   23.306    0.000  183.784    0.000 flatten.py:39(forward)
               12194658  174.305    0.000  174.305    0.000 {built-in method sum}
                3261056   27.969    0.000  174.180    0.000 level.py:41(notUsed)
                6098118  170.594    0.000  170.594    0.000 {built-in method max}
               32068626  160.479    0.000  160.479    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              171093801  106.154    0.000  152.662    0.000 layer.py:102(remove)
              248439445  102.409    0.000  152.342    0.000 random.py:250(_randbelow_with_getrandbits)
                8129772   12.718    0.000  149.201    0.000 tensor.py:525(__rsub__)
              211384302  143.422    0.000  143.422    0.000 {built-in method torch._C._get_tracing_state}
              253679125  102.355    0.000  139.953    0.000 layer.py:106(add)
                8129772  134.419    0.000  134.419    0.000 {built-in method rsub}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-4>
Subject: Job 9493322: <causal3_CFagent_convert3_0> in cluster <dcc> Done

Job <causal3_CFagent_convert3_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Fri Apr  2 22:10:09 2021
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sat Apr  3 11:06:50 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat Apr  3 11:06:50 2021
Terminated at Sun Apr  4 00:02:18 2021
Results reported at Sun Apr  4 00:02:18 2021

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

    CPU time :                                   46393.26 sec.
    Max Memory :                                 7089 MB
    Average Memory :                             5208.98 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               9295.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   46528 sec.
    Turnaround time :                            93129 sec.

The output (if any) is above this job summary.

