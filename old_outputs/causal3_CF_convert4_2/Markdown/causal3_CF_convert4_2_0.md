
# Parameters

    Name :                      causal3_CF_convert4_2-0
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
    Cf convert :                4
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      50632843920 function calls (50340314621 primitive calls) in 86117.28 seconds

##    Ordered by: cumulative time
   List reduced from 494 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86117.280 86117.280 {built-in method builtins.exec}
                      1    4.418    4.418 86117.280 86117.280 <string>:1(<module>)
                      1  226.319  226.319 86112.862 86112.862 main.py:96(CFagent)
                9245037   38.654    0.000 33041.767    0.004 agent.py:29(learn)
                9245034  753.809    0.000 27822.589    0.003 learner.py:42(Qlearn)
        327177169/34649561 1261.039    0.000 13832.038    0.000 module.py:715(_call_impl)
               25404527   60.129    0.000 13044.771    0.001 network.py:24(forward)
               25404527  338.661    0.000 12837.982    0.001 container.py:115(forward)
                3081679  109.585    0.000 12726.364    0.004 agent.py:54(_learn)
                3081679   16.035    0.000 12667.618    0.004 game.py:35(step)
                3081679   20.058    0.000 11912.228    0.004 layers.py:448(step)
                3081679  110.182    0.000 11859.807    0.004 agent.py:196(_learn)
                9245034   55.949    0.000 11852.090    0.001 grad_mode.py:23(decorate_context)
                9245034  318.472    0.000 11691.002    0.001 adam.py:55(step)
                9245034 2152.040    0.000 10078.238    0.001 functional.py:53(adam)
                3081679 1010.284    0.000 9633.548    0.003 agent.py:204(counterfact)
                3081679   89.442    0.000 8396.907    0.003 agent.py:115(_learn)
                3081679 4251.163    0.001 8222.008    0.003 replaybuffer.py:28(teleporter_save_data)
                3081679  264.174    0.000 7814.337    0.003 layers.py:17(step)
              308073055  455.539    0.000 7525.796    0.000 layer.py:84(move)
                8078377  204.209    0.000 6639.761    0.001 agent.py:49(__call__)
                9245034   59.103    0.000 6493.036    0.001 tensor.py:181(backward)
                9245034   33.745    0.000 6433.934    0.001 __init__.py:68(backward)
                9245034 6160.701    0.001 6160.701    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3081679 3482.985    0.001 6021.728    0.002 agent.py:86(interveen)
                3081679 3648.277    0.001 5252.630    0.002 replaybuffer.py:22(sample_data)
               50809054   82.152    0.000 4573.690    0.000 conv.py:422(forward)
               50809054   99.406    0.000 4455.806    0.000 conv.py:414(_conv_forward)
                3081679 2942.279    0.001 4353.567    0.001 replaybuffer.py:49(sample_data)
               50809054 4338.976    0.000 4338.976    0.000 {built-in method conv2d}
               70050223  146.898    0.000 4253.424    0.000 linear.py:92(forward)
               43813416 4095.052    0.000 4095.052    0.000 {built-in method tensor}
                3081680  327.236    0.000 4049.486    0.001 layers.py:419(update)
              308073055  662.926    0.000 4047.222    0.000 layers.py:465(check)
               70050223  258.964    0.000 4033.915    0.000 functional.py:1669(linear)
               36697013   29.028    0.000 3864.271    0.000 game.py:31(board)
                1917761   47.452    0.000 3501.154    0.002 agent.py:168(choose_action)
              238221232 3466.449    0.000 3466.449    0.000 {built-in method clone}
               49306872 1703.874    0.000 3050.326    0.000 layer.py:145(NoRock_update)
                3081679 1432.557    0.000 2934.995    0.001 agent.py:67(modify)
               70050223 2886.954    0.000 2886.954    0.000 {built-in method addmm}
               45058510 2805.370    0.000 2805.370    0.000 {built-in method cat}
              308071070  454.048    0.000 2595.864    0.000 layers.py:459(isFree)
              604008958 1549.075    0.000 2440.327    0.000 tensor.py:933(grad)
                9245034  226.314    0.000 2378.452    0.000 optimizer.py:167(zero_grad)
             2273817311 1800.323    0.000 2141.816    0.000 layer.py:81(isFree)
              172573964 2134.845    0.000 2134.845    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               95454750   75.689    0.000 1920.921    0.000 activation.py:713(forward)
               95454750  118.087    0.000 1845.232    0.000 functional.py:1292(leaky_relu)
               11160056   80.681    0.000 1823.735    0.000 agent.py:59(modify_board)
              172573964 1771.682    0.000 1771.682    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                3081676   52.446    0.000 1770.862    0.001 agent.py:164(__call__)
               95454750 1715.381    0.000 1715.381    0.000 {built-in method torch._C._nn.leaky_relu}
                3081679   53.040    0.000 1645.741    0.001 agent.py:110(__call__)
                3081679   79.458    0.000 1387.946    0.000 replaybuffer.py:18(stacker)
              782673173  415.310    0.000 1204.385    0.000 overrides.py:1070(has_torch_function)
                3081676   57.168    0.000 1200.924    0.000 replaybuffer.py:45(stacker)
               86286982 1145.222    0.000 1145.222    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               11160056 1140.874    0.000 1140.874    0.000 {built-in method torch._C._nn.one_hot}
                3962462   40.020    0.000 1116.941    0.000 layers.py:469(restart)
             4514017328  749.617    0.000 1081.472    0.000 enum.py:646(__hash__)
              308073055  688.708    0.000 1070.459    0.000 layers.py:233(check)
                3081679  433.555    0.000 1054.248    0.000 replaybuffer.py:55(CF_save_data)
               86286982 1046.563    0.000 1046.563    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               22327677  128.881    0.000 1045.432    0.000 tensor.py:21(wrapped)
              252462964 1039.773    0.000 1039.773    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               86286982  947.584    0.000  947.584    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              308073055  558.077    0.000  938.088    0.000 layers.py:270(check)
              330495677  121.949    0.000  931.457    0.000 {built-in method builtins.all}
               86286982  853.431    0.000  853.431    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
             1256842922  291.672    0.000  829.768    0.000 layers.py:425(<genexpr>)
                1917761  519.402    0.000  785.329    0.000 agent.py:179(convert_values)
             1080062061  771.172    0.000  771.172    0.000 layer.py:124(elements)
                3962462   19.913    0.000  766.903    0.000 level.py:8(__init__)
              874295144  310.450    0.000  753.965    0.000 {built-in method builtins.any}
                3081679  440.532    0.000  736.549    0.000 collector.py:54(collect)
                8078377  256.479    0.000  714.206    0.000 exploration.py:53(softmaxer)
               86286982  666.273    0.000  666.273    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                3962462   79.867    0.000  592.815    0.000 levels.py:164(generate)
               70050223  582.936    0.000  582.936    0.000 {method 't' of 'torch._C._TensorBase' objects}
                9245034   13.103    0.000  521.338    0.000 loss.py:445(forward)
                9245034   50.262    0.000  508.234    0.000 functional.py:2637(mse_loss)
              308168000  335.493    0.000  489.629    0.000 layers.py:100(isDone)
               14088282  184.300    0.000  489.473    0.000 random.py:315(sample)
        5715030700/5715030697  359.854    0.000  478.215    0.000 {built-in method builtins.len}
              308073055  284.305    0.000  454.147    0.000 layers.py:257(check)
              308073055  282.693    0.000  450.429    0.000 layers.py:294(check)
             5389342446  443.684    0.000  443.684    0.000 layer.py:77(positions)
                9245038  439.846    0.000  439.846    0.000 {built-in method nonzero}
             1657723439  351.046    0.000  437.117    0.000 overrides.py:1083(<genexpr>)
                6164969  410.565    0.000  410.565    0.000 {method 'ne' of 'torch._C._TensorBase' objects}
                7924924   62.821    0.000  409.447    0.000 level.py:41(notUsed)
              308073055  274.106    0.000  399.055    0.000 layers.py:42(check)
               50809054   42.879    0.000  353.383    0.000 flatten.py:39(forward)
               14244474   66.255    0.000  344.127    0.000 tensor.py:506(__rsub__)
             4514052527  331.862    0.000  331.862    0.000 {built-in method builtins.hash}
                9245034  317.919    0.000  317.919    0.000 {built-in method torch._C._nn.mse_loss}
               50809054  310.504    0.000  310.504    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               31699696   38.046    0.000  300.075    0.000 layer.py:58(restart)
               18490074  294.276    0.000  294.276    0.000 {built-in method sum}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-2>
Subject: Job 9496015: <causal3_CF_convert4_2_0> in cluster <dcc> Done

Job <causal3_CF_convert4_2_0> was submitted from host <n-62-27-19> by user <s183905> in cluster <dcc> at Mon Apr  5 20:05:18 2021
Job was executed on host(s) <n-62-20-2>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Mon Apr  5 20:43:59 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Apr  5 20:43:59 2021
Terminated at Tue Apr  6 20:39:23 2021
Results reported at Tue Apr  6 20:39:23 2021

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

    CPU time :                                   85899.17 sec.
    Max Memory :                                 3410 MB
    Average Memory :                             3352.85 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               12974.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86125 sec.
    Turnaround time :                            88445 sec.

The output (if any) is above this job summary.

