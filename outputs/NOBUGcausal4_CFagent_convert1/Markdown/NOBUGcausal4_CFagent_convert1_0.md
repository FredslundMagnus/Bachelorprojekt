
# Parameters

    Name :                      NOBUGcausal4_CFagent_convert1-0
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
    Cf convert :                1
    Minutes used :              955 minutes.
    Hours used :                15 hours.

# Profiling


      37414640462 function calls (37205511439 primitive calls) in 57308.42 seconds

##    Ordered by: cumulative time
   List reduced from 492 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 57308.416 57308.416 {built-in method builtins.exec}
                      1    4.646    4.646 57308.416 57308.416 <string>:1(<module>)
                      1  148.777  148.777 57303.770 57303.770 main.py:96(CFagent)
                7051908   27.194    0.000 21795.914    0.003 agent.py:28(learn)
                7051908  536.020    0.000 18270.031    0.003 learner.py:42(Qlearn)
                2350636   10.634    0.000 11186.705    0.005 game.py:36(step)
                2350636   12.650    0.000 10607.936    0.005 layers.py:594(step)
        234390063/25262731  970.581    0.000 8865.585    0.000 module.py:866(_call_impl)
                2350636  226.719    0.000 8383.994    0.004 agent.py:53(_learn)
               18210823   51.738    0.000 8289.504    0.000 network.py:24(forward)
               18210823  260.947    0.000 8122.474    0.000 container.py:117(forward)
                2350636  223.973    0.000 7783.457    0.003 agent.py:191(_learn)
                7051908   62.198    0.000 7776.350    0.001 optimizer.py:84(wrapper)
                2350636  207.873    0.000 7627.942    0.003 layers.py:18(step)
                7051908   30.952    0.000 7473.315    0.001 grad_mode.py:24(decorate_context)
              234962184  527.714    0.000 7399.611    0.000 layer.py:82(move)
                7051908  210.619    0.000 7373.502    0.001 adam.py:55(step)
                7051908 1525.304    0.000 6925.654    0.001 _functional.py:53(adam)
                2350636  538.917    0.000 6303.097    0.003 agent.py:199(counterfact)
                2350636   66.394    0.000 5585.058    0.002 agent.py:114(_learn)
                7051908   38.390    0.000 4602.969    0.001 tensor.py:195(backward)
                7051908   29.466    0.000 4563.497    0.001 __init__.py:68(backward)
              234962184  714.985    0.000 4507.512    0.000 layers.py:611(check)
                7051908 4370.494    0.001 4370.494    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2350636 2245.340    0.001 4272.504    0.002 replaybuffer.py:28(teleporter_save_data)
                5577006  136.482    0.000 4121.963    0.001 agent.py:48(__call__)
               36329329 3796.731    0.000 3796.731    0.000 {built-in method tensor}
               30823700   20.799    0.000 3633.048    0.000 game.py:32(board)
                2350636 1820.534    0.001 3553.738    0.002 agent.py:85(interveen)
                2350636 2342.392    0.001 3169.440    0.001 replaybuffer.py:22(sample_data)
                2350637  250.162    0.000 2948.637    0.001 layers.py:565(update)
               36421646   89.594    0.000 2910.719    0.000 conv.py:398(forward)
               36421646   52.014    0.000 2784.660    0.000 conv.py:390(_conv_forward)
               36421646 2732.646    0.000 2732.646    0.000 {built-in method conv2d}
               47012730 1502.182    0.000 2699.918    0.000 layer.py:127(update)
                2350636 1917.741    0.001 2658.005    0.001 replaybuffer.py:49(sample_data)
               49931197  109.738    0.000 2358.524    0.000 linear.py:93(forward)
               49931197   43.372    0.000 2198.787    0.000 functional.py:1737(linear)
               49931197 2144.385    0.000 2144.385    0.000 {built-in method torch._C._nn.linear}
              234952623  398.129    0.000 2043.678    0.000 layers.py:605(isFree)
                2350636 1078.513    0.000 1826.088    0.001 agent.py:66(modify)
              135790693 1822.162    0.000 1822.162    0.000 {built-in method clone}
             1859550669 1342.559    0.000 1645.549    0.000 layer.py:79(isFree)
              131635616 1391.226    0.000 1391.226    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               33784638 1345.957    0.000 1345.957    0.000 {built-in method cat}
               68142020   57.583    0.000 1315.217    0.000 activation.py:713(forward)
               68142020   64.066    0.000 1257.634    0.000 functional.py:1364(leaky_relu)
              131635616 1227.586    0.000 1227.586    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                2350636   37.026    0.000 1204.418    0.001 agent.py:163(__call__)
               68142020 1180.220    0.000 1180.220    0.000 {built-in method torch._C._nn.leaky_relu}
                7927642   61.109    0.000 1169.578    0.000 agent.py:58(modify_board)
                2350636   36.423    0.000 1134.201    0.000 agent.py:109(__call__)
                 880637    8.833    0.000 1088.737    0.001 agent.py:167(choose_action)
                7051908  175.079    0.000 1079.848    0.000 optimizer.py:189(zero_grad)
             3763306401  665.320    0.000  947.481    0.000 enum.py:646(__hash__)
               65817808  802.554    0.000  802.554    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              234962184  492.264    0.000  777.352    0.000 layers.py:303(check)
                7927642  735.297    0.000  735.297    0.000 {built-in method torch._C._nn.one_hot}
              234962184  439.219    0.000  720.787    0.000 layers.py:262(check)
               65817808  676.667    0.000  676.667    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              234962184  523.923    0.000  674.762    0.000 layers.py:76(check)
              701787288  665.649    0.000  665.649    0.000 layer.py:122(elements)
                2350636   54.695    0.000  660.434    0.000 replaybuffer.py:18(stacker)
               65817808  641.627    0.000  641.627    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               65817808  640.085    0.000  640.085    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              235063700   77.581    0.000  630.746    0.000 {built-in method builtins.all}
              713554151  175.066    0.000  580.630    0.000 layers.py:571(<genexpr>)
                2350636   49.890    0.000  577.123    0.000 replaybuffer.py:45(stacker)
                1735433   19.609    0.000  572.434    0.000 layers.py:615(restart)
             5638851006  519.941    0.000  519.941    0.000 layer.py:75(positions)
                2350636  302.102    0.000  498.204    0.000 collector.py:54(collect)
               65817808  489.876    0.000  489.876    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                2350636  176.895    0.000  484.055    0.000 replaybuffer.py:55(CF_save_data)
              234962184  359.043    0.000  462.155    0.000 layers.py:63(check)
              146068971  459.295    0.000  459.295    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                5577006  155.269    0.000  427.284    0.000 exploration.py:53(softmaxer)
              234962184  266.365    0.000  410.441    0.000 layers.py:329(check)
              460724740  317.942    0.000  394.176    0.000 tensor.py:906(grad)
        5124078187/5124078184  345.430    0.000  391.396    0.000 {built-in method builtins.len}
                1735433    9.036    0.000  388.226    0.000 level.py:8(__init__)
              235063700  257.040    0.000  385.069    0.000 layers.py:111(isDone)
              234962184  239.319    0.000  372.760    0.000 layers.py:288(check)
                7051908   11.648    0.000  361.115    0.000 loss.py:527(forward)
                7051908   29.919    0.000  349.467    0.000 functional.py:2898(mse_loss)
                8172138  129.690    0.000  344.631    0.000 random.py:315(sample)
                1735433   54.360    0.000  314.811    0.000 levels.py:199(generate)
                7051909  314.392    0.000  314.392    0.000 {built-in method nonzero}
              234962184  209.562    0.000  313.934    0.000 layers.py:47(check)
             3763333424  282.166    0.000  282.166    0.000 {built-in method builtins.hash}
                7051908  228.223    0.000  228.223    0.000 {built-in method torch._C._nn.mse_loss}
               36421646   28.084    0.000  222.153    0.000 flatten.py:39(forward)
               14103816  208.721    0.000  208.721    0.000 {built-in method sum}
                3470866   25.275    0.000  208.078    0.000 level.py:41(notUsed)
                7052700  199.312    0.000  199.312    0.000 {built-in method max}
               36421646  194.069    0.000  194.069    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              194697536  136.467    0.000  189.410    0.000 layer.py:102(remove)
               47012730  181.972    0.000  181.972    0.000 layer.py:139(<listcomp>)
              283958910  121.381    0.000  178.711    0.000 random.py:250(_randbelow_with_getrandbits)
                9402544   15.027    0.000  178.128    0.000 tensor.py:525(__rsub__)
              239973086  173.808    0.000  173.808    0.000 {built-in method torch._C._get_tracing_state}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-11-13>
Subject: Job 9494242: <NOBUGcausal4_CFagent_convert1_0> in cluster <dcc> Done

Job <NOBUGcausal4_CFagent_convert1_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun Apr  4 02:59:53 2021
Job was executed on host(s) <n-62-11-13>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Apr  4 18:55:25 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun Apr  4 18:55:25 2021
Terminated at Mon Apr  5 10:50:36 2021
Results reported at Mon Apr  5 10:50:36 2021

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

    CPU time :                                   57266.38 sec.
    Max Memory :                                 3574 MB
    Average Memory :                             3498.32 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               12810.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   57312 sec.
    Turnaround time :                            114643 sec.

The output (if any) is above this job summary.

