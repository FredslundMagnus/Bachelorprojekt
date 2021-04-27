
# Parameters

    Name :                      Diamonds4_teleport-1
    Main :                      teleport
    Level :                     Levels.Causal7
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


      86419122241 function calls (86139473390 primitive calls) in 86105.84 seconds

##    Ordered by: cumulative time
   List reduced from 474 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86105.836 86105.836 {built-in method builtins.exec}
                      1    1.544    1.544 86105.836 86105.836 <string>:1(<module>)
                      1  211.323  211.323 86104.292 86104.292 main.py:45(teleport)
                9988190   35.041    0.000 26540.601    0.003 agent.py:29(learn)
                4994095   19.134    0.000 22509.516    0.005 game.py:41(step)
                9988190  634.688    0.000 22346.035    0.002 learner.py:42(Qlearn)
                4994095   24.032    0.000 21489.059    0.004 layers.py:718(step)
                4994095  156.601    0.000 16032.159    0.003 agent.py:54(_learn)
                4994095 7202.790    0.001 12990.798    0.003 replaybuffer.py:28(teleporter_save_data)
                4994095  367.860    0.000 11725.643    0.002 layers.py:17(step)
              499409500  781.796    0.000 11314.826    0.000 layer.py:98(move)
        314604715/34956875 1106.683    0.000 11016.384    0.000 module.py:715(_call_impl)
                4994095  131.284    0.000 10456.201    0.002 agent.py:117(_learn)
               24968685   60.053    0.000 10287.818    0.000 network.py:27(forward)
               24968685  270.159    0.000 10090.044    0.000 container.py:115(forward)
                4994095 6479.082    0.001 9858.476    0.002 agent.py:88(interveen)
                4994096  671.313    0.000 9705.956    0.002 layers.py:684(update)
                9988190   58.069    0.000 8967.553    0.001 grad_mode.py:23(decorate_context)
                9988190  301.937    0.000 8804.114    0.001 adam.py:55(step)
                9988190 1647.264    0.000 7254.692    0.001 functional.py:53(adam)
              499409500 1465.025    0.000 6974.788    0.000 layers.py:735(check)
                9986400  201.449    0.000 6814.982    0.001 agent.py:49(__call__)
                4994095 3785.976    0.001 5885.522    0.001 replaybuffer.py:22(sample_data)
                9988190   52.239    0.000 5262.862    0.001 tensor.py:181(backward)
                9988190   33.368    0.000 5210.623    0.001 __init__.py:68(backward)
                9988190 4959.755    0.000 4959.755    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
              468338545 4597.575    0.000 4597.575    0.000 {built-in method clone}
                4994095 2436.390    0.000 4567.048    0.001 agent.py:67(modify)
               10387494   91.362    0.000 3843.034    0.000 layers.py:740(restart)
               49937370   78.439    0.000 3771.780    0.000 conv.py:422(forward)
               49937370   94.943    0.000 3661.098    0.000 conv.py:414(_conv_forward)
               49937370 3548.084    0.000 3548.084    0.000 {built-in method conv2d}
               64917865  134.974    0.000 3217.517    0.000 linear.py:92(forward)
               10387494   44.180    0.000 3070.056    0.000 level.py:8(__init__)
               64917865  223.569    0.000 3018.662    0.000 functional.py:1669(linear)
              499409500  728.255    0.000 2798.385    0.000 layers.py:729(isFree)
               10387494  112.137    0.000 2616.433    0.000 levels.py:441(generate)
               49857690  442.322    0.000 2387.644    0.000 level.py:41(notUsed)
               34958672 1368.952    0.000 2329.204    0.000 layer.py:167(NoRock_update)
             1392944202  692.949    0.000 2320.596    0.000 {built-in method builtins.any}
              629256024 1339.040    0.000 2226.674    0.000 tensor.py:933(grad)
                4994095   60.841    0.000 2158.559    0.000 agent.py:112(__call__)
               64917865 2138.584    0.000 2138.584    0.000 {built-in method addmm}
               39950970 2107.539    0.000 2107.539    0.000 {built-in method cat}
               14980495   97.027    0.000 2084.792    0.000 agent.py:59(modify_board)
             3437003324 1670.846    0.000 2070.130    0.000 layer.py:95(isFree)
             8216058217 1370.041    0.000 2016.162    0.000 enum.py:646(__hash__)
                9988190  191.623    0.000 1959.827    0.000 optimizer.py:167(zero_grad)
                4994095   75.661    0.000 1753.985    0.000 replaybuffer.py:18(stacker)
              179787420 1458.012    0.000 1458.012    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               21312484 1422.590    0.000 1422.590    0.000 {built-in method tensor}
               89886550   73.939    0.000 1405.333    0.000 activation.py:713(forward)
              499409500  862.553    0.000 1390.485    0.000 layers.py:602(check)
              499409500  844.990    0.000 1364.274    0.000 layers.py:632(check)
               14980495 1349.787    0.000 1349.787    0.000 {built-in method torch._C._nn.one_hot}
               89886550  112.428    0.000 1331.394    0.000 functional.py:1292(leaky_relu)
              499409500  795.471    0.000 1299.400    0.000 layers.py:617(check)
              483319040 1273.144    0.000 1273.144    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              819027850  401.730    0.000 1217.635    0.000 overrides.py:1070(has_torch_function)
               89886550 1208.468    0.000 1208.468    0.000 {built-in method torch._C._nn.leaky_relu}
              179787420 1204.833    0.000 1204.833    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              534370759  144.502    0.000 1178.752    0.000 {built-in method builtins.all}
             3912176848  944.312    0.000 1167.460    0.000 layers.py:700(<genexpr>)
               34961159  172.271    0.000 1166.569    0.000 tensor.py:21(wrapped)
               49857690   35.783    0.000 1121.995    0.000 level.py:38(elementsIn)
                9988190   10.154    0.000 1111.601    0.000 game.py:37(board)
             1383996515  323.643    0.000 1070.948    0.000 layers.py:690(<genexpr>)
             9500535730  862.576    0.000  862.576    0.000 layer.py:91(positions)
               89893710  853.484    0.000  853.484    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                4994095  492.626    0.000  850.933    0.000 collector.py:46(collect)
               89893710  781.929    0.000  781.929    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               49857690  357.278    0.000  727.057    0.000 level.py:39(<listcomp>)
                9986400  264.072    0.000  711.136    0.000 exploration.py:53(softmaxer)
               89893710  686.348    0.000  686.348    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               72712458   55.254    0.000  657.753    0.000 layer.py:69(restart)
             8216094544  646.127    0.000  646.127    0.000 {built-in method builtins.hash}
              499409500  388.518    0.000  609.341    0.000 layers.py:588(check)
               89893710  600.482    0.000  600.482    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
             1793491606  589.903    0.000  589.903    0.000 layer.py:146(elements)
              331261192  360.038    0.000  545.354    0.000 layers.py:113(isDone)
              499409500  339.972    0.000  503.985    0.000 layers.py:23(check)
               10387594  250.695    0.000  502.952    0.000 layers.py:36(reset)
        5283541622/5283541620  362.164    0.000  491.291    0.000 {built-in method builtins.len}
             2393795749  489.788    0.000  489.788    0.000 level.py:32(inverse)
                9988190   13.563    0.000  468.958    0.000 loss.py:445(forward)
               89893710  467.008    0.000  467.008    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              866954404  332.931    0.000  459.089    0.000 layer.py:130(add)
                9988190   50.472    0.000  455.395    0.000 functional.py:2637(mse_loss)
             1737933726  367.735    0.000  453.895    0.000 overrides.py:1083(<genexpr>)
               24970475  437.844    0.000  437.844    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               10387494  216.325    0.000  383.849    0.000 level.py:16(<dictcomp>)
               64917865  383.132    0.000  383.132    0.000 {method 't' of 'torch._C._TensorBase' objects}
             2168828114  374.202    0.000  374.202    0.000 enum.py:352(<genexpr>)
               49857690  222.577    0.000  359.156    0.000 {built-in method _functools.reduce}
              512206371  238.790    0.000  354.235    0.000 layer.py:126(remove)
               29964570  347.128    0.000  347.128    0.000 {built-in method sum}
                4994095  125.151    0.000  337.366    0.000 random.py:315(sample)
             3437003324  316.864    0.000  316.864    0.000 layer.py:203(isBlocking)
                4996091  307.696    0.000  307.696    0.000 {method 'ne' of 'torch._C._TensorBase' objects}
             4041820071  304.056    0.000  304.056    0.000 {method 'random' of '_random.Random' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9550906: <Diamonds4_teleport_1> in cluster <dcc> Done

Job <Diamonds4_teleport_1> was submitted from host <n-62-30-4> by user <s183905> in cluster <dcc> at Tue Apr 20 16:21:49 2021
Job was executed on host(s) <n-62-20-2>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Fri Apr 23 17:42:55 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Fri Apr 23 17:42:55 2021
Terminated at Sat Apr 24 17:38:05 2021
Results reported at Sat Apr 24 17:38:05 2021

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

    CPU time :                                   85898.98 sec.
    Max Memory :                                 2683 MB
    Average Memory :                             2680.66 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13701.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86111 sec.
    Turnaround time :                            350176 sec.

The output (if any) is above this job summary.

