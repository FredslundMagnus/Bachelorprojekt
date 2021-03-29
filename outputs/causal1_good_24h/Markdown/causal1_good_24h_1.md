
# Parameters

    Name :                      causal1_good_24h-1
    Main :                      teleport
    Level :                     Levels.Causal1
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


      99739994864 function calls (99510559209 primitive calls) in 86113.99 seconds

##    Ordered by: cumulative time
   List reduced from 480 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86113.992 86113.992 {built-in method builtins.exec}
                      1    2.039    2.039 86113.992 86113.992 <string>:1(<module>)
                      1  190.189  190.189 86111.953 86111.953 main.py:43(teleport)
                4097371   18.107    0.000 31254.772    0.008 game.py:27(step)
                4097371   21.201    0.000 29973.712    0.007 layers.py:475(step)
                8194742   30.437    0.000 22290.151    0.003 agent.py:27(learn)
                4097371  345.827    0.000 20821.074    0.005 layers.py:18(step)
              409737100  991.103    0.000 20440.127    0.000 layer.py:76(move)
                8194742  522.753    0.000 18730.690    0.002 learner.py:42(Qlearn)
              409737100 2192.164    0.000 13637.812    0.000 layers.py:492(check)
                4097371  134.610    0.000 13491.624    0.003 agent.py:52(_learn)
                4097371 6711.124    0.002 11978.088    0.003 replaybuffer.py:29(teleporter_save_data)
        258114730/28680086  955.361    0.000 9268.490    0.000 module.py:715(_call_impl)
                4097372  446.231    0.000 9101.887    0.002 layers.py:446(update)
                4097371  109.422    0.000 8750.444    0.002 agent.py:113(_learn)
               20485344   49.934    0.000 8652.167    0.000 network.py:24(forward)
               20485344  232.568    0.000 8483.473    0.000 container.py:115(forward)
                4097371 5107.446    0.001 7945.322    0.002 agent.py:84(interveen)
                8194742   49.918    0.000 7458.707    0.001 grad_mode.py:23(decorate_context)
                8194742  254.490    0.000 7308.709    0.001 adam.py:55(step)
                8194742 1334.590    0.000 5994.753    0.001 functional.py:53(adam)
                4097371 3860.941    0.001 5803.842    0.001 replaybuffer.py:23(sample_data)
                8193231  180.319    0.000 5734.734    0.001 agent.py:47(__call__)
              409737100 1521.480    0.000 5148.239    0.000 layers.py:486(isFree)
                8194742   56.193    0.000 4487.651    0.001 tensor.py:181(backward)
                8194742   29.328    0.000 4431.459    0.001 __init__.py:68(backward)
               73752696 2513.975    0.000 4396.273    0.000 layer.py:121(update)
                8194742 4227.190    0.001 4227.190    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
              429668414 4175.330    0.000 4175.330    0.000 {built-in method clone}
             7007208597 2719.791    0.000 3626.760    0.000 layer.py:73(isFree)
            14026896941 2294.067    0.000 3313.176    0.000 enum.py:646(__hash__)
                4097371 1652.503    0.000 3276.536    0.001 agent.py:65(modify)
               40970688   67.696    0.000 3134.441    0.000 conv.py:422(forward)
               40970688   76.028    0.000 3039.758    0.000 conv.py:414(_conv_forward)
               10205136  138.960    0.000 2953.388    0.000 layers.py:496(restart)
               40970688 2950.311    0.000 2950.311    0.000 {built-in method conv2d}
               53261290  112.818    0.000 2713.047    0.000 linear.py:92(forward)
               53261290  193.653    0.000 2546.861    0.000 functional.py:1669(linear)
               17544472 2023.786    0.000 2023.786    0.000 {built-in method tensor}
               36874828 1941.891    0.000 1941.891    0.000 {built-in method cat}
               10205136   59.136    0.000 1919.984    0.000 level.py:8(__init__)
              516268800 1145.189    0.000 1898.513    0.000 tensor.py:933(grad)
                4097371   51.194    0.000 1817.298    0.000 agent.py:108(__call__)
               53261290 1789.634    0.000 1789.634    0.000 {built-in method addmm}
                8194742   11.455    0.000 1744.048    0.000 game.py:23(board)
               12290602   81.709    0.000 1718.250    0.000 agent.py:57(modify_board)
               10205136  112.602    0.000 1660.969    0.000 levels.py:122(generate)
                4097371   75.695    0.000 1657.547    0.000 replaybuffer.py:19(stacker)
                8194742  157.650    0.000 1647.463    0.000 optimizer.py:167(zero_grad)
            16440770569 1476.675    0.000 1476.675    0.000 layer.py:69(positions)
               39800640  295.378    0.000 1447.267    0.000 level.py:41(notUsed)
             1710878589 1204.600    0.000 1204.600    0.000 layer.py:116(elements)
              147505356 1200.618    0.000 1200.618    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               73746634   64.113    0.000 1190.722    0.000 activation.py:713(forward)
              430226089  140.053    0.000 1173.771    0.000 {built-in method builtins.all}
              441959016 1160.164    0.000 1160.164    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               73746634  100.883    0.000 1126.609    0.000 functional.py:1292(leaky_relu)
               12290602 1104.115    0.000 1104.115    0.000 {built-in method torch._C._nn.one_hot}
              409737100  698.801    0.000 1100.840    0.000 layers.py:173(check)
             1393004698  338.645    0.000 1066.655    0.000 layers.py:452(<genexpr>)
              409737100  663.832    0.000 1060.443    0.000 layers.py:302(check)
              409737100  647.535    0.000 1051.805    0.000 layers.py:230(check)
              409737100  651.497    0.000 1040.332    0.000 layers.py:261(check)
              409737100  648.283    0.000 1035.526    0.000 layers.py:244(check)
              409737100  640.243    0.000 1029.887    0.000 layers.py:216(check)
            14026926788 1019.115    0.000 1019.115    0.000 {built-in method builtins.hash}
              663770928  341.866    0.000 1016.355    0.000 overrides.py:1070(has_torch_function)
               73746634 1016.268    0.000 1016.268    0.000 {built-in method torch._C._nn.leaky_relu}
              147505356  980.639    0.000  980.639    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              409737100  698.102    0.000  954.458    0.000 layers.py:76(check)
              183692448  129.561    0.000  841.052    0.000 layer.py:50(restart)
               20488889  102.736    0.000  764.798    0.000 tensor.py:21(wrapped)
               73752678  754.491    0.000  754.491    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              409737100  461.814    0.000  709.565    0.000 layers.py:142(check)
                4097371  405.130    0.000  695.626    0.000 collector.py:54(collect)
              409737200  444.461    0.000  658.353    0.000 layers.py:110(isDone)
              409737100  427.037    0.000  656.900    0.000 layers.py:328(check)
               73752678  643.293    0.000  643.293    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              733421703  260.248    0.000  640.942    0.000 {built-in method builtins.any}
              409737100  409.623    0.000  639.234    0.000 layers.py:287(check)
             5837799163  619.203    0.000  619.203    0.000 layer.py:177(isBlocking)
                8193231  215.650    0.000  585.947    0.000 exploration.py:53(softmaxer)
               73752678  573.238    0.000  573.238    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              409737100  352.454    0.000  532.762    0.000 layers.py:47(check)
              409737100  344.540    0.000  530.697    0.000 layers.py:123(check)
               39800640   28.665    0.000  517.838    0.000 level.py:38(elementsIn)
               10205236  250.631    0.000  506.299    0.000 layers.py:33(reset)
              409737100  323.775    0.000  492.917    0.000 layers.py:63(check)
               73752678  487.976    0.000  487.976    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              409737100  316.544    0.000  484.143    0.000 layers.py:203(check)
             1835885147  470.892    0.000  470.892    0.000 level.py:32(inverse)
        6003927928/6003927926  349.373    0.000  463.452    0.000 {built-in method builtins.len}
              786612928  322.443    0.000  430.433    0.000 layer.py:100(add)
                8194742   13.128    0.000  393.899    0.000 loss.py:445(forward)
               73752678  382.418    0.000  382.418    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                8194742   44.154    0.000  380.771    0.000 functional.py:2637(mse_loss)
             1401291216  303.888    0.000  375.082    0.000 overrides.py:1083(<genexpr>)
               53261290  329.359    0.000  329.359    0.000 {method 't' of 'torch._C._TensorBase' objects}
               39800640  159.907    0.000  315.168    0.000 level.py:39(<listcomp>)
              404440566  217.089    0.000  310.260    0.000 layer.py:96(remove)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-7>
Subject: Job 9474545: <causal1_good_24h_1> in cluster <dcc> Done

Job <causal1_good_24h_1> was submitted from host <n-62-27-21> by user <s183905> in cluster <dcc> at Sun Mar 28 11:07:12 2021
Job was executed on host(s) <n-62-20-7>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sun Mar 28 11:07:13 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun Mar 28 11:07:13 2021
Terminated at Mon Mar 29 11:02:39 2021
Results reported at Mon Mar 29 11:02:39 2021

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

    CPU time :                                   86075.45 sec.
    Max Memory :                                 2821 MB
    Average Memory :                             2815.81 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13563.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86150 sec.
    Turnaround time :                            86127 sec.

The output (if any) is above this job summary.

