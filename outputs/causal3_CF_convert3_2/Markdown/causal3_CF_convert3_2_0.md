
# Parameters

    Name :                      causal3_CF_convert3_2-0
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
    Cf convert :                3
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      49543889748 function calls (49258776921 primitive calls) in 86113.95 seconds

##    Ordered by: cumulative time
   List reduced from 494 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86113.948 86113.948 {built-in method builtins.exec}
                      1    4.433    4.433 86113.948 86113.948 <string>:1(<module>)
                      1  220.652  220.652 86109.515 86109.515 main.py:96(CFagent)
                8917692   36.876    0.000 32021.130    0.004 agent.py:29(learn)
                8917677  728.990    0.000 26972.041    0.003 learner.py:42(Qlearn)
        318778929/33667793 1248.576    0.000 13562.678    0.000 module.py:715(_call_impl)
               24750116   59.792    0.000 12792.225    0.001 network.py:24(forward)
                2972564   16.841    0.000 12626.605    0.004 game.py:35(step)
               24750116  335.638    0.000 12590.490    0.001 container.py:115(forward)
                2972564  105.372    0.000 12328.826    0.004 agent.py:54(_learn)
                2972564   18.294    0.000 11896.841    0.004 layers.py:448(step)
                8917677   54.842    0.000 11521.446    0.001 grad_mode.py:23(decorate_context)
                2972564  106.884    0.000 11497.183    0.004 agent.py:196(_learn)
                8917677  305.227    0.000 11365.056    0.001 adam.py:55(step)
                2972564 1113.436    0.000 9823.094    0.003 agent.py:204(counterfact)
                8917677 2121.464    0.000 9812.894    0.001 functional.py:53(adam)
                2972564 4714.288    0.002 9137.971    0.003 replaybuffer.py:28(teleporter_save_data)
                2972564   86.386    0.000 8135.598    0.003 agent.py:115(_learn)
                2972564  263.490    0.000 7790.909    0.003 layers.py:17(step)
              297247790  448.618    0.000 7496.957    0.000 layer.py:84(move)
                7915195  199.111    0.000 6521.179    0.001 agent.py:49(__call__)
                2972564 3859.866    0.001 6316.601    0.002 agent.py:86(interveen)
                8917677   55.158    0.000 6284.491    0.001 tensor.py:181(backward)
                8917677   30.546    0.000 6229.334    0.001 __init__.py:68(backward)
                8917677 5970.119    0.001 5970.119    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2972564 3576.847    0.001 5110.120    0.002 replaybuffer.py:22(sample_data)
               49500232   82.136    0.000 4502.203    0.000 conv.py:422(forward)
               49500232  110.142    0.000 4383.767    0.000 conv.py:414(_conv_forward)
               49500232 4256.255    0.000 4256.255    0.000 {built-in method conv2d}
                2972564 2904.476    0.001 4254.386    0.001 replaybuffer.py:49(sample_data)
               68305220  148.353    0.000 4147.296    0.000 linear.py:92(forward)
                2972565  315.536    0.000 4060.365    0.001 layers.py:419(update)
              297247790  685.585    0.000 4056.038    0.000 layers.py:465(check)
               42886469 4032.316    0.000 4032.316    0.000 {built-in method tensor}
               68305220  255.654    0.000 3926.431    0.000 functional.py:1669(linear)
              264292718 3857.289    0.000 3857.289    0.000 {built-in method clone}
               36009502   25.865    0.000 3806.957    0.000 game.py:31(board)
                1972131   49.091    0.000 3513.851    0.002 agent.py:168(choose_action)
               47561032 1757.557    0.000 3067.833    0.000 layer.py:145(NoRock_update)
                2972564 1410.851    0.000 2860.652    0.001 agent.py:67(modify)
               68305220 2798.648    0.000 2798.648    0.000 {built-in method addmm}
               43585888 2692.956    0.000 2692.956    0.000 {built-in method cat}
              297237886  459.563    0.000 2566.290    0.000 layers.py:459(isFree)
              582621578 1498.761    0.000 2350.078    0.000 tensor.py:933(grad)
                8917677  211.777    0.000 2286.108    0.000 optimizer.py:167(zero_grad)
             2184876921 1778.596    0.000 2106.727    0.000 layer.py:81(isFree)
              166463284 2072.665    0.000 2072.665    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               93055336   73.338    0.000 1894.942    0.000 activation.py:713(forward)
               93055336  123.729    0.000 1821.604    0.000 functional.py:1292(leaky_relu)
               10887759   76.939    0.000 1775.282    0.000 agent.py:59(modify_board)
              166463284 1725.751    0.000 1725.751    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                2972549   49.654    0.000 1722.954    0.001 agent.py:164(__call__)
               93055336 1686.340    0.000 1686.340    0.000 {built-in method torch._C._nn.leaky_relu}
                2972564   52.130    0.000 1595.414    0.001 agent.py:110(__call__)
                2972564   75.083    0.000 1328.915    0.000 replaybuffer.py:18(stacker)
                4311732   44.345    0.000 1215.636    0.000 layers.py:469(restart)
              755939504  401.989    0.000 1159.317    0.000 overrides.py:1070(has_torch_function)
                2972549   55.368    0.000 1149.765    0.000 replaybuffer.py:45(stacker)
              278153026 1126.430    0.000 1126.430    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                2972564  469.259    0.000 1119.326    0.000 replaybuffer.py:55(CF_save_data)
               83231642 1113.357    0.000 1113.357    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               10887759 1112.798    0.000 1112.798    0.000 {built-in method torch._C._nn.one_hot}
              297247790  676.574    0.000 1050.842    0.000 layers.py:233(check)
             4285336474  726.198    0.000 1035.056    0.000 enum.py:646(__hash__)
               21781715  125.088    0.000 1015.977    0.000 tensor.py:21(wrapped)
               83231642 1014.585    0.000 1014.585    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              297247790  565.548    0.000  944.950    0.000 layers.py:270(check)
               83231642  913.512    0.000  913.512    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              319038215  134.154    0.000  892.702    0.000 {built-in method builtins.all}
               83231642  826.172    0.000  826.172    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                4311732   21.635    0.000  825.454    0.000 level.py:8(__init__)
             1445936815  333.940    0.000  777.137    0.000 layers.py:425(<genexpr>)
             1100348133  756.264    0.000  756.264    0.000 layer.py:124(elements)
              845052643  299.601    0.000  725.488    0.000 {built-in method builtins.any}
                2972564  426.373    0.000  715.355    0.000 collector.py:54(collect)
                1972131  467.556    0.000  708.433    0.000 agent.py:179(convert_values)
                7915195  246.995    0.000  696.231    0.000 exploration.py:53(softmaxer)
               83231642  646.485    0.000  646.485    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                4311732   85.168    0.000  642.483    0.000 levels.py:164(generate)
               68305220  573.284    0.000  573.284    0.000 {method 't' of 'torch._C._TensorBase' objects}
                8917677   12.944    0.000  502.469    0.000 loss.py:445(forward)
                8917677   47.236    0.000  489.525    0.000 functional.py:2637(mse_loss)
               14568592  179.737    0.000  472.224    0.000 random.py:315(sample)
        5503618837/5503618834  346.200    0.000  460.756    0.000 {built-in method builtins.len}
             5110164001  451.868    0.000  451.868    0.000 layer.py:77(positions)
              297247790  287.242    0.000  451.619    0.000 layers.py:294(check)
                8623464   69.114    0.000  445.451    0.000 level.py:41(notUsed)
              297247790  280.064    0.000  441.222    0.000 layers.py:257(check)
                8917693  426.364    0.000  426.364    0.000 {built-in method nonzero}
             1601965152  338.369    0.000  420.011    0.000 overrides.py:1083(<genexpr>)
              297247790  277.337    0.000  407.151    0.000 layers.py:42(check)
                5946695  389.071    0.000  389.071    0.000 {method 'ne' of 'torch._C._TensorBase' objects}
               49500232   36.981    0.000  340.168    0.000 flatten.py:39(forward)
               34493856   43.286    0.000  334.578    0.000 layer.py:58(restart)
               13862372   64.861    0.000  331.280    0.000 tensor.py:506(__rsub__)
             4285370441  308.864    0.000  308.864    0.000 {built-in method builtins.hash}
                8917677  308.532    0.000  308.532    0.000 {built-in method torch._C._nn.mse_loss}
               49500232  303.187    0.000  303.187    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              288589472  222.189    0.000  301.188    0.000 layer.py:104(remove)
               17835384  288.192    0.000  288.192    0.000 {built-in method sum}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-5>
Subject: Job 9496014: <causal3_CF_convert3_2_0> in cluster <dcc> Done

Job <causal3_CF_convert3_2_0> was submitted from host <n-62-27-19> by user <s183905> in cluster <dcc> at Mon Apr  5 20:05:18 2021
Job was executed on host(s) <n-62-20-5>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Mon Apr  5 20:41:48 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Apr  5 20:41:48 2021
Terminated at Tue Apr  6 20:37:07 2021
Results reported at Tue Apr  6 20:37:07 2021

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

    CPU time :                                   85898.12 sec.
    Max Memory :                                 3410 MB
    Average Memory :                             3362.22 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               12974.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86121 sec.
    Turnaround time :                            88309 sec.

The output (if any) is above this job summary.

