
# Parameters

    Name :                      Lights1_teleport-0
    Main :                      teleport
    Level :                     Levels.Causal3
    Failed actions chance :     0.0
    Hours :                     24.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.UCB1
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
    Layer greendown :           True
    Layer greenup :             True
    Layer greenstar :           True
    Layer yellowstar :          True
    Layer bluestar :            True
    Layer coconut :             True
    Layer monster :             True
    Layer greencross :          True
    Layer bluecross :           True
    Layer redcross :            True
    Layer purplecross :         True
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                3
    Counterfacts :              1
    Topn :                      6
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      76676120176 function calls (76414096957 primitive calls) in 86117.28 seconds

##    Ordered by: cumulative time
   List reduced from 479 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86117.276 86117.276 {built-in method builtins.exec}
                      1    1.665    1.665 86117.276 86117.276 <string>:1(<module>)
                      1  297.974  297.974 86115.612 86115.612 main.py:45(teleport)
                9362688   42.675    0.000 28916.756    0.003 agent.py:29(learn)
                4681344   29.913    0.000 25504.186    0.005 game.py:41(step)
                4681344   34.429    0.000 24328.764    0.005 layers.py:718(step)
                9362688  708.081    0.000 24164.032    0.003 learner.py:42(Qlearn)
                4681344  189.200    0.000 17442.120    0.004 agent.py:54(_learn)
                4681344  472.416    0.000 15262.214    0.003 layers.py:17(step)
              468134400  793.842    0.000 14743.422    0.000 layer.py:98(move)
        294780528/32758320 1236.325    0.000 11874.854    0.000 module.py:715(_call_impl)
                4681344  153.061    0.000 11410.133    0.002 agent.py:117(_learn)
               23395632   61.279    0.000 11013.189    0.000 network.py:27(forward)
               23395632  305.496    0.000 10793.739    0.000 container.py:115(forward)
                9362688   73.541    0.000 9472.112    0.001 grad_mode.py:23(decorate_context)
                9362688  343.790    0.000 9274.409    0.001 adam.py:55(step)
                4681344 6842.026    0.001 9092.269    0.002 replaybuffer.py:22(sample_data)
                4681345  724.024    0.000 8978.124    0.002 layers.py:684(update)
              468134400 1738.250    0.000 8381.095    0.000 layers.py:735(check)
                9362688 1702.698    0.000 7624.443    0.001 functional.py:53(adam)
                9351600  285.293    0.000 7398.136    0.001 agent.py:49(__call__)
                4681344 3504.099    0.001 7054.073    0.002 agent.py:88(interveen)
                4681344 3682.756    0.001 6579.442    0.001 replaybuffer.py:28(teleporter_save_data)
                9362688   62.298    0.000 5897.960    0.001 tensor.py:181(backward)
                9362688   45.046    0.000 5835.662    0.001 __init__.py:68(backward)
                9362688 5546.936    0.001 5546.936    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                4681344 2494.787    0.001 4813.520    0.001 agent.py:67(modify)
              468134400  902.841    0.000 4765.165    0.000 layers.py:729(isFree)
               46791264   84.845    0.000 4046.381    0.000 conv.py:422(forward)
               46791264  112.717    0.000 3919.787    0.000 conv.py:414(_conv_forward)
             3526396853 3265.420    0.000 3862.324    0.000 layer.py:95(isFree)
               46791264 3788.612    0.000 3788.612    0.000 {built-in method conv2d}
               60824208  138.584    0.000 3410.266    0.000 linear.py:92(forward)
               60824208  236.139    0.000 3194.864    0.000 functional.py:1669(linear)
               37450760 1797.592    0.000 3148.782    0.000 layer.py:167(NoRock_update)
             1309670623  749.686    0.000 2550.009    0.000 {built-in method builtins.any}
              209150428 2361.390    0.000 2361.390    0.000 {built-in method clone}
                4681344   88.092    0.000 2312.924    0.000 agent.py:112(__call__)
              589849398 1381.567    0.000 2303.561    0.000 tensor.py:933(grad)
               60824208 2269.173    0.000 2269.173    0.000 {built-in method addmm}
               37439664 2212.788    0.000 2212.788    0.000 {built-in method cat}
               14032944  114.195    0.000 2209.059    0.000 agent.py:59(modify_board)
                5722241   69.701    0.000 2020.260    0.000 layers.py:740(restart)
                9362688  190.073    0.000 2008.055    0.000 optimizer.py:167(zero_grad)
             7114936698 1329.264    0.000 1935.316    0.000 enum.py:646(__hash__)
              468134400 1231.032    0.000 1894.884    0.000 layers.py:246(check)
                4681344   92.049    0.000 1854.392    0.000 replaybuffer.py:18(stacker)
               19998729 1654.322    0.000 1654.322    0.000 {built-in method tensor}
              468134400  980.681    0.000 1608.430    0.000 layers.py:286(check)
              168528384 1547.489    0.000 1547.489    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               84219840   74.698    0.000 1494.981    0.000 activation.py:713(forward)
                5722241   35.287    0.000 1436.430    0.000 level.py:8(__init__)
               84219840  120.411    0.000 1420.284    0.000 functional.py:1292(leaky_relu)
               14032944 1417.952    0.000 1417.952    0.000 {built-in method torch._C._nn.one_hot}
             4161710331 1076.194    0.000 1326.237    0.000 layers.py:700(<genexpr>)
                9362688   15.570    0.000 1315.183    0.000 game.py:37(board)
               32771826  183.236    0.000 1307.462    0.000 tensor.py:21(wrapped)
               84219840 1288.221    0.000 1288.221    0.000 {built-in method torch._C._nn.leaky_relu}
              168528384 1273.714    0.000 1273.714    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              767708779  415.343    0.000 1260.056    0.000 overrides.py:1070(has_torch_function)
              500906326  111.800    0.000 1175.421    0.000 {built-in method builtins.all}
              961746034  215.418    0.000 1099.928    0.000 layers.py:690(<genexpr>)
                5722241  128.459    0.000 1070.684    0.000 levels.py:164(generate)
                4681344  517.542    0.000  895.279    0.000 collector.py:46(collect)
             1518082281  893.717    0.000  893.717    0.000 layer.py:146(elements)
              468134500  607.400    0.000  879.792    0.000 layers.py:113(isDone)
               84264192  878.331    0.000  878.331    0.000 {method 'add' of 'torch._C._TensorBase' objects}
             9081472206  854.751    0.000  854.751    0.000 layer.py:91(positions)
               84264192  832.806    0.000  832.806    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                9351600  285.360    0.000  803.928    0.000 exploration.py:53(softmaxer)
              468134400  504.756    0.000  798.738    0.000 layers.py:313(check)
               11444482  114.429    0.000  769.778    0.000 level.py:41(notUsed)
              468134400  479.302    0.000  755.174    0.000 layers.py:273(check)
               84264192  721.226    0.000  721.226    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              468134400  465.894    0.000  675.311    0.000 layers.py:48(check)
              223183372  671.081    0.000  671.081    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               84264192  639.941    0.000  639.941    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
             7114970793  606.058    0.000  606.058    0.000 {built-in method builtins.hash}
                9362688   20.702    0.000  580.467    0.000 loss.py:445(forward)
                9362688   70.076    0.000  559.764    0.000 functional.py:2637(mse_loss)
        5374752288/5374752286  392.633    0.000  527.972    0.000 {built-in method builtins.len}
              468134400  344.810    0.000  514.986    0.000 layers.py:23(check)
               16125826  198.066    0.000  510.428    0.000 random.py:315(sample)
               45777928   63.074    0.000  498.037    0.000 layer.py:69(restart)
               84264192  480.443    0.000  480.443    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               23406720  474.963    0.000  474.963    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
              723797283  341.455    0.000  468.179    0.000 layer.py:130(add)
             1629012657  373.704    0.000  466.030    0.000 overrides.py:1083(<genexpr>)
               60824208  412.497    0.000  412.497    0.000 {method 't' of 'torch._C._TensorBase' objects}
              432053546  254.493    0.000  385.196    0.000 layer.py:126(remove)
                4683214  380.324    0.000  380.324    0.000 {method 'ne' of 'torch._C._TensorBase' objects}
               28088064  367.499    0.000  367.499    0.000 {built-in method sum}
             4244212740  353.721    0.000  353.721    0.000 {method 'random' of '_random.Random' objects}
                9362688  316.345    0.000  316.345    0.000 {built-in method torch._C._nn.mse_loss}
             2660221490  311.255    0.000  311.255    0.000 layer.py:203(isBlocking)
                5722241  198.728    0.000  310.079    0.000 level.py:16(<dictcomp>)
               11444482   12.824    0.000  307.278    0.000 level.py:38(elementsIn)
                5722341  149.673    0.000  297.661    0.000 layers.py:36(reset)
                4681344   26.406    0.000  292.490    0.000 exploration.py:47(epsilonGreedy)
                9364091  281.166    0.000  281.166    0.000 {built-in method max}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9550889: <Lights1_teleport_0> in cluster <dcc> Done

Job <Lights1_teleport_0> was submitted from host <n-62-30-4> by user <s183905> in cluster <dcc> at Tue Apr 20 16:21:47 2021
Job was executed on host(s) <n-62-20-12>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Wed Apr 21 05:26:50 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed Apr 21 05:26:50 2021
Terminated at Thu Apr 22 05:22:16 2021
Results reported at Thu Apr 22 05:22:16 2021

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

    CPU time :                                   85888.93 sec.
    Max Memory :                                 2676 MB
    Average Memory :                             2670.26 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13708.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86127 sec.
    Turnaround time :                            133229 sec.

The output (if any) is above this job summary.

