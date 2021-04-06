
# Parameters

    Name :                      causal3_CF_convert1_2-0
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
    Cf convert :                1
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      55004505764 function calls (54685910845 primitive calls) in 86110.19 seconds

##    Ordered by: cumulative time
   List reduced from 493 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86110.193 86110.193 {built-in method builtins.exec}
                      1    4.875    4.875 86110.193 86110.193 <string>:1(<module>)
                      1  227.974  227.974 86105.318 86105.318 main.py:96(CFagent)
                9842403   38.084    0.000 29905.674    0.003 agent.py:29(learn)
                9842400  683.300    0.000 24813.571    0.003 learner.py:42(Qlearn)
                3280801   15.485    0.000 14645.668    0.004 game.py:35(step)
                3280801   18.868    0.000 13905.299    0.004 layers.py:448(step)
        356078664/37485436 1367.177    0.000 13516.390    0.000 module.py:715(_call_impl)
               27643036   63.476    0.000 12727.057    0.000 network.py:24(forward)
               27643036  327.575    0.000 12492.909    0.000 container.py:115(forward)
                3280801  115.904    0.000 11569.087    0.004 agent.py:54(_learn)
                3280801  115.120    0.000 10702.525    0.003 agent.py:196(_learn)
                3280801 1285.876    0.000 10695.753    0.003 agent.py:204(counterfact)
                9842400   60.220    0.000 10063.749    0.001 grad_mode.py:23(decorate_context)
                9842400  334.450    0.000 9892.324    0.001 adam.py:55(step)
                3280801  293.775    0.000 8863.106    0.003 layers.py:17(step)
              327746756  536.726    0.000 8534.437    0.000 layer.py:84(move)
                9842400 1823.010    0.000 8107.522    0.001 functional.py:53(adam)
                3280801 4257.198    0.001 7874.114    0.002 replaybuffer.py:28(teleporter_save_data)
                3280801   94.324    0.000 7575.069    0.002 agent.py:115(_learn)
                8899091  214.541    0.000 6599.831    0.001 agent.py:49(__call__)
                9842400   58.686    0.000 5844.982    0.001 tensor.py:181(backward)
                9842400   34.831    0.000 5786.296    0.001 __init__.py:68(backward)
                3280801 3312.435    0.001 5751.316    0.002 agent.py:86(interveen)
                3280801 3990.693    0.001 5663.087    0.002 replaybuffer.py:22(sample_data)
                9842400 5522.686    0.001 5522.686    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3280802  365.294    0.000 4994.881    0.002 layers.py:419(update)
                3280801 3308.056    0.001 4789.470    0.001 replaybuffer.py:49(sample_data)
              327746756  755.011    0.000 4584.569    0.000 layers.py:465(check)
               55286072   95.520    0.000 4537.921    0.000 conv.py:422(forward)
               55286072  106.198    0.000 4402.972    0.000 conv.py:414(_conv_forward)
               48772777 4383.776    0.000 4383.776    0.000 {built-in method tensor}
               55286072 4277.045    0.000 4277.045    0.000 {built-in method conv2d}
               41215604   27.748    0.000 4172.809    0.000 game.py:31(board)
               76367506  167.831    0.000 4082.739    0.000 linear.py:92(forward)
               76367506  285.422    0.000 3834.232    0.000 functional.py:1669(linear)
               52492824 2097.023    0.000 3624.174    0.000 layer.py:145(NoRock_update)
                2339946   51.537    0.000 3564.567    0.002 agent.py:168(choose_action)
              288893671 3289.175    0.000 3289.175    0.000 {built-in method clone}
              327721103  544.176    0.000 2883.849    0.000 layers.py:459(isFree)
               48268688 2873.927    0.000 2873.927    0.000 {built-in method cat}
                3280801 1358.469    0.000 2774.932    0.001 agent.py:67(modify)
               76367506 2705.067    0.000 2705.067    0.000 {built-in method addmm}
              643036870 1589.472    0.000 2600.214    0.000 tensor.py:933(grad)
             2502249512 1942.341    0.000 2339.672    0.000 layer.py:81(isFree)
                9842400  195.990    0.000 2224.046    0.000 optimizer.py:167(zero_grad)
                6067649   60.269    0.000 1825.234    0.000 layers.py:469(restart)
               12179892   88.419    0.000 1816.791    0.000 agent.py:59(modify_board)
              104010542   91.878    0.000 1762.205    0.000 activation.py:713(forward)
                3280798   49.395    0.000 1694.016    0.001 agent.py:164(__call__)
              104010542  136.173    0.000 1670.327    0.000 functional.py:1292(leaky_relu)
              183724796 1652.190    0.000 1652.190    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                3280801   48.982    0.000 1588.679    0.000 agent.py:110(__call__)
              104010542 1519.527    0.000 1519.527    0.000 {built-in method torch._C._nn.leaky_relu}
                3280801   77.010    0.000 1427.307    0.000 replaybuffer.py:18(stacker)
              835632994  460.571    0.000 1375.799    0.000 overrides.py:1070(has_torch_function)
              183724796 1343.880    0.000 1343.880    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                3280801  555.020    0.000 1241.741    0.000 replaybuffer.py:55(CF_save_data)
                6067649   30.158    0.000 1241.726    0.000 level.py:8(__init__)
                3280798   58.930    0.000 1239.756    0.000 replaybuffer.py:45(stacker)
             4810165742  873.304    0.000 1238.223    0.000 enum.py:646(__hash__)
              327746756  760.186    0.000 1202.379    0.000 layers.py:233(check)
               12179892 1156.767    0.000 1156.767    0.000 {built-in method torch._C._nn.one_hot}
               24366969  140.296    0.000 1080.149    0.000 tensor.py:21(wrapped)
              327746756  626.812    0.000 1057.001    0.000 layers.py:270(check)
                6067649  127.483    0.000  989.326    0.000 levels.py:164(generate)
               91862398  949.714    0.000  949.714    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              304354361  900.808    0.000  900.808    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               91862398  876.641    0.000  876.641    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              934966102  358.487    0.000  872.089    0.000 {built-in method builtins.any}
             1351352164  864.107    0.000  864.107    0.000 layer.py:124(elements)
              352447169  137.353    0.000  837.816    0.000 {built-in method builtins.all}
               91862398  764.643    0.000  764.643    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
             1254254050  327.605    0.000  723.216    0.000 layers.py:425(<genexpr>)
               12135298  102.518    0.000  689.940    0.000 level.py:41(notUsed)
                8899091  254.092    0.000  682.291    0.000 exploration.py:53(softmaxer)
               91862398  671.222    0.000  671.222    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                3280801  366.573    0.000  625.682    0.000 collector.py:54(collect)
               18696900  225.036    0.000  593.714    0.000 random.py:315(sample)
                2339946  420.087    0.000  589.384    0.000 agent.py:179(convert_values)
        6038341001/6038340998  410.928    0.000  536.496    0.000 {built-in method builtins.len}
              327746756  333.801    0.000  526.425    0.000 layers.py:257(check)
              327746756  325.779    0.000  515.094    0.000 layers.py:294(check)
               91862398  509.798    0.000  509.798    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
             5443393217  509.593    0.000  509.593    0.000 layer.py:77(positions)
             1771999574  408.928    0.000  506.881    0.000 overrides.py:1083(<genexpr>)
               48541192   64.546    0.000  505.986    0.000 layer.py:58(restart)
                9842400   16.042    0.000  504.308    0.000 loss.py:445(forward)
               76367506  498.484    0.000  498.484    0.000 {method 't' of 'torch._C._TensorBase' objects}
                9842400   56.281    0.000  488.266    0.000 functional.py:2637(mse_loss)
              327746756  297.051    0.000  441.196    0.000 layers.py:42(check)
                6563377  430.566    0.000  430.566    0.000 {method 'ne' of 'torch._C._TensorBase' objects}
                9842404  420.761    0.000  420.761    0.000 {built-in method nonzero}
              323232490  302.302    0.000  394.238    0.000 layer.py:104(remove)
             4810203181  364.927    0.000  364.927    0.000 {built-in method builtins.hash}
              625881922  264.313    0.000  362.687    0.000 layer.py:108(add)
              459259610  217.663    0.000  321.116    0.000 random.py:250(_randbelow_with_getrandbits)
                6067749  163.151    0.000  320.858    0.000 layers.py:30(reset)
               55286072   46.186    0.000  313.252    0.000 flatten.py:39(forward)
                9842400  285.561    0.000  285.561    0.000 {built-in method torch._C._nn.mse_loss}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-14>
Subject: Job 9496012: <causal3_CF_convert1_2_0> in cluster <dcc> Done

Job <causal3_CF_convert1_2_0> was submitted from host <n-62-27-19> by user <s183905> in cluster <dcc> at Mon Apr  5 20:05:17 2021
Job was executed on host(s) <n-62-20-14>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Mon Apr  5 20:36:22 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Apr  5 20:36:22 2021
Terminated at Tue Apr  6 20:31:35 2021
Results reported at Tue Apr  6 20:31:35 2021

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

    CPU time :                                   85886.50 sec.
    Max Memory :                                 3430 MB
    Average Memory :                             3349.49 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               12954.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86113 sec.
    Turnaround time :                            87978 sec.

The output (if any) is above this job summary.

