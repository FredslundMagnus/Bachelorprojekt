
# Parameters

    Name :                      causal2_good_24h-1
    Main :                      teleport
    Level :                     Levels.Causal2
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


      102157185511 function calls (101923598884 primitive calls) in 86115.81 seconds

##    Ordered by: cumulative time
   List reduced from 480 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86115.814 86115.814 {built-in method builtins.exec}
                      1    1.893    1.893 86115.814 86115.814 <string>:1(<module>)
                      1  189.079  189.079 86113.921 86113.921 main.py:43(teleport)
                4171485   16.761    0.000 30657.755    0.007 game.py:27(step)
                4171485   20.514    0.000 29365.656    0.007 layers.py:475(step)
                8342970   29.982    0.000 22294.846    0.003 agent.py:27(learn)
                4171485  325.457    0.000 20247.676    0.005 layers.py:18(step)
              417148500  985.290    0.000 19880.835    0.000 layer.py:76(move)
                8342970  531.400    0.000 18719.218    0.002 learner.py:42(Qlearn)
                4171485  133.504    0.000 13507.540    0.003 agent.py:52(_learn)
              417148500 2234.231    0.000 13497.929    0.000 layers.py:492(check)
                4171485 6941.053    0.002 12370.679    0.003 replaybuffer.py:29(teleporter_save_data)
        262784549/29198933  929.761    0.000 9243.623    0.000 module.py:715(_call_impl)
                4171486  447.015    0.000 9067.675    0.002 layers.py:446(update)
                4171485  110.016    0.000 8739.423    0.002 agent.py:113(_learn)
               20855963   48.706    0.000 8630.609    0.000 network.py:24(forward)
               20855963  224.994    0.000 8467.749    0.000 container.py:115(forward)
                4171485 5285.021    0.001 8131.551    0.002 agent.py:84(interveen)
                8342970   46.607    0.000 7481.527    0.001 grad_mode.py:23(decorate_context)
                8342970  250.714    0.000 7340.971    0.001 adam.py:55(step)
                8342970 1340.217    0.000 5990.825    0.001 functional.py:53(adam)
                4171485 3805.460    0.001 5773.596    0.001 replaybuffer.py:23(sample_data)
                8341508  180.383    0.000 5750.318    0.001 agent.py:47(__call__)
              417148500 1278.993    0.000 4741.835    0.000 layers.py:486(isFree)
                8342970   47.163    0.000 4395.271    0.001 tensor.py:181(backward)
               75086748 2493.529    0.000 4382.512    0.000 layer.py:121(update)
                8342970   26.746    0.000 4348.108    0.001 __init__.py:68(backward)
              450733320 4305.798    0.000 4305.798    0.000 {built-in method clone}
                8342970 4138.873    0.000 4138.873    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
             7273352982 2656.506    0.000 3462.841    0.000 layer.py:73(isFree)
                4171485 1656.218    0.000 3297.924    0.001 agent.py:65(modify)
            14355683657 2278.014    0.000 3253.718    0.000 enum.py:646(__hash__)
               41711926   66.911    0.000 3178.197    0.000 conv.py:422(forward)
               41711926   80.466    0.000 3084.796    0.000 conv.py:414(_conv_forward)
               41711926 2990.712    0.000 2990.712    0.000 {built-in method conv2d}
                9540296  131.604    0.000 2940.837    0.000 layers.py:496(restart)
               54224919  112.416    0.000 2697.202    0.000 linear.py:92(forward)
               54224919  188.139    0.000 2530.629    0.000 functional.py:1669(linear)
               17853628 2045.852    0.000 2045.852    0.000 {built-in method tensor}
                9540296   52.433    0.000 1998.273    0.000 level.py:8(__init__)
               37541903 1972.644    0.000 1972.644    0.000 {built-in method cat}
              525607164 1220.030    0.000 1969.719    0.000 tensor.py:933(grad)
                4171485   51.506    0.000 1819.424    0.000 agent.py:108(__call__)
               54224919 1792.852    0.000 1792.852    0.000 {built-in method addmm}
                9540296  103.406    0.000 1765.312    0.000 levels.py:151(generate)
                8342970   10.090    0.000 1763.112    0.000 game.py:23(board)
               12512993   80.287    0.000 1743.592    0.000 agent.py:57(modify_board)
                8342970  155.903    0.000 1691.329    0.000 optimizer.py:167(zero_grad)
                4171485   75.220    0.000 1682.385    0.000 replaybuffer.py:19(stacker)
               45796264  335.696    0.000 1555.922    0.000 level.py:41(notUsed)
            16669911276 1503.481    0.000 1503.481    0.000 layer.py:69(positions)
              150173460 1203.953    0.000 1203.953    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
             1649471832 1192.811    0.000 1192.811    0.000 layer.py:116(elements)
              463246313 1187.961    0.000 1187.961    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               75080882   60.302    0.000 1182.126    0.000 activation.py:713(forward)
              438008219  141.589    0.000 1159.341    0.000 {built-in method builtins.all}
               12512993 1124.886    0.000 1124.886    0.000 {built-in method torch._C._nn.one_hot}
               75080882   88.010    0.000 1121.824    0.000 functional.py:1292(leaky_relu)
              417148500  697.726    0.000 1105.095    0.000 layers.py:173(check)
             1419182380  330.499    0.000 1051.326    0.000 layers.py:452(<genexpr>)
              417148500  654.812    0.000 1050.678    0.000 layers.py:302(check)
              417148500  666.032    0.000 1049.356    0.000 layers.py:230(check)
              417148500  651.782    0.000 1044.666    0.000 layers.py:216(check)
              417148500  642.290    0.000 1037.299    0.000 layers.py:261(check)
              417148500  646.960    0.000 1026.177    0.000 layers.py:244(check)
               75080882 1024.411    0.000 1024.411    0.000 {built-in method torch._C._nn.leaky_relu}
              675777688  334.333    0.000 1008.071    0.000 overrides.py:1070(has_torch_function)
              150173460 1000.004    0.000 1000.004    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
            14355714080  975.709    0.000  975.709    0.000 {built-in method builtins.hash}
              417148500  643.162    0.000  893.313    0.000 layers.py:76(check)
               20859619  104.248    0.000  775.671    0.000 tensor.py:21(wrapped)
              171725328  111.958    0.000  762.540    0.000 layer.py:50(restart)
               75086730  711.318    0.000  711.318    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                4171485  413.383    0.000  707.059    0.000 collector.py:54(collect)
              417148500  446.121    0.000  686.007    0.000 layers.py:142(check)
               75086730  649.717    0.000  649.717    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              417148600  432.165    0.000  649.552    0.000 layers.py:110(isDone)
              746688548  261.927    0.000  640.383    0.000 {built-in method builtins.any}
              417148500  413.064    0.000  638.041    0.000 layers.py:287(check)
              417148500  401.340    0.000  629.510    0.000 layers.py:328(check)
                8341508  224.738    0.000  603.294    0.000 exploration.py:53(softmaxer)
               45796264   33.956    0.000  582.068    0.000 level.py:38(elementsIn)
               75086730  575.181    0.000  575.181    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
             6063434544  523.415    0.000  523.415    0.000 layer.py:177(isBlocking)
              417148500  323.626    0.000  497.338    0.000 layers.py:63(check)
              417148500  323.719    0.000  496.763    0.000 layers.py:203(check)
              417148500  323.817    0.000  495.248    0.000 layers.py:123(check)
               75086730  491.413    0.000  491.413    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              417148500  309.375    0.000  481.427    0.000 layers.py:47(check)
                9540396  236.881    0.000  474.106    0.000 layers.py:33(reset)
        6142917648/6142917646  355.345    0.000  468.695    0.000 {built-in method builtins.len}
             2198785864  453.723    0.000  453.723    0.000 level.py:32(inverse)
              754395082  299.247    0.000  407.333    0.000 layer.py:100(add)
                8342970   11.207    0.000  391.371    0.000 loss.py:445(forward)
               75086730  390.728    0.000  390.728    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                8342970   44.327    0.000  380.165    0.000 functional.py:2637(mse_loss)
             1426639080  299.514    0.000  373.065    0.000 overrides.py:1083(<genexpr>)
               45796264  182.613    0.000  357.595    0.000 level.py:39(<listcomp>)
               54224919  318.917    0.000  318.917    0.000 {method 't' of 'torch._C._TensorBase' objects}
              421829538  207.710    0.000  302.380    0.000 layer.py:96(remove)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-2>
Subject: Job 9474548: <causal2_good_24h_1> in cluster <dcc> Done

Job <causal2_good_24h_1> was submitted from host <n-62-27-21> by user <s183905> in cluster <dcc> at Sun Mar 28 11:07:13 2021
Job was executed on host(s) <n-62-20-2>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sun Mar 28 11:07:15 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun Mar 28 11:07:15 2021
Terminated at Mon Mar 29 11:02:41 2021
Results reported at Mon Mar 29 11:02:41 2021

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

    CPU time :                                   85897.11 sec.
    Max Memory :                                 2816 MB
    Average Memory :                             2810.27 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13568.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86153 sec.
    Turnaround time :                            86128 sec.

The output (if any) is above this job summary.

