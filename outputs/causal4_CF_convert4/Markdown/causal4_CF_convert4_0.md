
# Parameters

    Name :                      causal4_CF_convert4-0
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
    Cf convert :                4
    Minutes used :              955 minutes.
    Hours used :                15 hours.

# Profiling


      44489385329 function calls (44240998122 primitive calls) in 57309.36 seconds

##    Ordered by: cumulative time
   List reduced from 508 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 57309.355 57309.355 {built-in method builtins.exec}
                      1    4.655    4.655 57309.355 57309.355 <string>:1(<module>)
                      1  194.391  194.391 57304.700 57304.700 main.py:96(CFagent)
                8271909   31.635    0.000 19089.240    0.002 agent.py:29(learn)
                8271895  480.551    0.000 15470.875    0.002 learner.py:42(Qlearn)
                2757303   13.402    0.000 13152.857    0.005 game.py:35(step)
                2757303   16.224    0.000 12531.599    0.005 layers.py:448(step)
                2757303  243.354    0.000 9217.014    0.003 layers.py:17(step)
              275730300  680.961    0.000 8950.475    0.000 layer.py:84(move)
        278275305/29889789 1075.838    0.000 8600.683    0.000 module.py:866(_call_impl)
               21617894   55.766    0.000 8027.245    0.000 network.py:24(forward)
               21617894  251.398    0.000 7836.646    0.000 container.py:117(forward)
                2757303  292.885    0.000 7442.845    0.003 agent.py:54(_learn)
                2757303  527.379    0.000 7416.503    0.003 agent.py:201(counterfact)
                2757303  289.695    0.000 6819.977    0.002 agent.py:193(_learn)
                8271895   65.047    0.000 6041.883    0.001 optimizer.py:84(wrapper)
                8271895   34.033    0.000 5748.020    0.001 grad_mode.py:24(decorate_context)
                8271895  243.043    0.000 5638.155    0.001 adam.py:55(step)
              275730300  837.308    0.000 5190.195    0.000 layers.py:465(check)
                8271895 1180.201    0.000 5126.265    0.001 _functional.py:53(adam)
                2757303   82.726    0.000 4778.486    0.002 agent.py:115(_learn)
               42692486 4262.265    0.000 4262.265    0.000 {built-in method tensor}
                2757303 3246.597    0.001 4183.583    0.002 replaybuffer.py:22(sample_data)
               36291263   21.183    0.000 4113.003    0.000 game.py:31(board)
                6668868  172.730    0.000 4072.840    0.001 agent.py:49(__call__)
                8271895   32.348    0.000 3999.543    0.000 tensor.py:195(backward)
                8271895   31.445    0.000 3966.104    0.000 __init__.py:68(backward)
                8271895 3783.549    0.000 3783.549    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2757303 2749.791    0.001 3569.210    0.001 replaybuffer.py:49(sample_data)
               55146070 2028.821    0.000 3497.758    0.000 layer.py:129(update)
                2757304  284.568    0.000 3272.710    0.001 layers.py:419(update)
               43235788   94.554    0.000 2929.043    0.000 conv.py:398(forward)
                2757303 1229.850    0.000 2893.636    0.001 agent.py:86(interveen)
                2757303 1623.097    0.001 2856.773    0.001 replaybuffer.py:28(teleporter_save_data)
               43235788   58.912    0.000 2787.323    0.000 conv.py:390(_conv_forward)
               43235788 2728.410    0.000 2728.410    0.000 {built-in method conv2d}
              275580095  462.363    0.000 2633.859    0.000 layers.py:459(isFree)
               59339076  113.477    0.000 2194.494    0.000 linear.py:93(forward)
             2317963875 1836.025    0.000 2171.497    0.000 layer.py:81(isFree)
               59339076   45.514    0.000 2022.598    0.000 functional.py:1737(linear)
               59339076 1964.190    0.000 1964.190    0.000 {built-in method torch._C._nn.linear}
                2757303  993.357    0.000 1682.027    0.001 agent.py:67(modify)
               39756434 1447.039    0.000 1447.039    0.000 {built-in method cat}
                1162539   22.809    0.000 1436.111    0.001 agent.py:168(choose_action)
              125092853 1181.383    0.000 1181.383    0.000 {built-in method clone}
                2757289   48.396    0.000 1175.340    0.000 agent.py:164(__call__)
               80956970   68.810    0.000 1161.428    0.000 activation.py:713(forward)
                9426171   55.078    0.000 1155.636    0.000 agent.py:59(modify_board)
                2757303   45.893    0.000 1118.132    0.000 agent.py:110(__call__)
               80956970   63.625    0.000 1092.619    0.000 functional.py:1364(leaky_relu)
             4438271805  756.995    0.000 1086.568    0.000 enum.py:646(__hash__)
               80956970 1016.602    0.000 1016.602    0.000 {built-in method torch._C._nn.leaky_relu}
              154408688  996.717    0.000  996.717    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                8271895  160.837    0.000  897.171    0.000 optimizer.py:189(zero_grad)
              154408688  891.475    0.000  891.475    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              275730300  550.662    0.000  867.310    0.000 layers.py:270(check)
              836046294  836.368    0.000  836.368    0.000 layer.py:124(elements)
              275730300  485.484    0.000  794.060    0.000 layers.py:233(check)
              275730300  591.669    0.000  762.761    0.000 layers.py:67(check)
                9426171  761.560    0.000  761.560    0.000 {built-in method torch._C._nn.one_hot}
                2757303   63.778    0.000  743.560    0.000 replaybuffer.py:18(stacker)
                2041091   25.600    0.000  662.576    0.000 layers.py:469(restart)
                2757289   59.933    0.000  632.042    0.000 replaybuffer.py:45(stacker)
               77204344  584.437    0.000  584.437    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              275730300  455.908    0.000  576.818    0.000 layers.py:56(check)
               77204344  513.389    0.000  513.389    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
             6091463014  512.560    0.000  512.560    0.000 layer.py:77(positions)
               77204344  470.973    0.000  470.973    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               77204344  469.527    0.000  469.527    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              275730300  290.827    0.000  458.865    0.000 layers.py:294(check)
              275730300  295.311    0.000  451.401    0.000 layers.py:257(check)
        6770384524/6770384521  401.606    0.000  449.601    0.000 {built-in method builtins.len}
                2041091   11.290    0.000  449.553    0.000 level.py:8(__init__)
                2757303  170.443    0.000  446.316    0.000 replaybuffer.py:55(CF_save_data)
              540430492  336.780    0.000  420.835    0.000 tensor.py:906(grad)
                6668868  149.490    0.000  402.988    0.000 exploration.py:53(softmaxer)
                9596788  152.700    0.000  402.042    0.000 random.py:315(sample)
              275730400   68.352    0.000  396.858    0.000 {built-in method builtins.all}
                2757303  234.833    0.000  395.760    0.000 collector.py:54(collect)
              275730300  259.908    0.000  375.993    0.000 layers.py:42(check)
                2041091   66.690    0.000  366.270    0.000 levels.py:199(generate)
              837777509  180.614    0.000  358.311    0.000 layers.py:425(<genexpr>)
               77204344  354.264    0.000  354.264    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                8271895   11.762    0.000  335.277    0.000 loss.py:527(forward)
             4438303308  329.578    0.000  329.578    0.000 {built-in method builtins.hash}
                8271895   30.204    0.000  323.515    0.000 functional.py:2898(mse_loss)
                8271910  310.717    0.000  310.717    0.000 {built-in method nonzero}
              137276313  260.491    0.000  260.491    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                4082182   29.254    0.000  236.697    0.000 level.py:41(notUsed)
                1162539  180.697    0.000  224.899    0.000 agent.py:179(convert_values)
              242185271  149.188    0.000  214.299    0.000 layer.py:104(remove)
               55146070  213.652    0.000  213.652    0.000 layer.py:141(<listcomp>)
              329937375  137.019    0.000  203.049    0.000 random.py:250(_randbelow_with_getrandbits)
                8271895  199.643    0.000  199.643    0.000 {built-in method torch._C._nn.mse_loss}
              363340135  146.800    0.000  199.390    0.000 layer.py:108(add)
               43235788   28.942    0.000  192.579    0.000 flatten.py:39(forward)
                8272836  183.127    0.000  183.127    0.000 {built-in method max}
               20410910   27.718    0.000  181.071    0.000 layer.py:58(restart)
             1867950069  181.017    0.000  181.017    0.000 layer.py:181(isBlocking)
               12191737   15.895    0.000  169.132    0.000 tensor.py:525(__rsub__)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-4>
Subject: Job 9495294: <causal4_CF_convert4_0> in cluster <dcc> Done

Job <causal4_CF_convert4_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon Apr  5 02:37:26 2021
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon Apr  5 10:50:38 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Apr  5 10:50:38 2021
Terminated at Tue Apr  6 02:45:53 2021
Results reported at Tue Apr  6 02:45:53 2021

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

    CPU time :                                   57173.59 sec.
    Max Memory :                                 8432 MB
    Average Memory :                             5845.84 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               7952.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   57431 sec.
    Turnaround time :                            86907 sec.

The output (if any) is above this job summary.

