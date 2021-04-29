
# Parameters

    Name :                      Coconuts_teleport-1
    Main :                      teleport
    Level :                     Levels.Coconuts
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


      81384673978 function calls (81118257979 primitive calls) in 86104.73 seconds

##    Ordered by: cumulative time
   List reduced from 482 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86104.734 86104.734 {built-in method builtins.exec}
                      1    1.489    1.489 86104.733 86104.733 <string>:1(<module>)
                      1  216.631  216.631 86103.245 86103.245 main.py:45(teleport)
                9534954   33.100    0.000 32829.195    0.003 agent.py:29(learn)
                9534954  779.482    0.000 28104.340    0.003 learner.py:42(Qlearn)
                4767477   19.383    0.000 24565.847    0.005 game.py:41(step)
                4767477   26.531    0.000 23460.242    0.005 layers.py:718(step)
                4767477  156.405    0.000 19750.339    0.004 agent.py:54(_learn)
                4767477  404.253    0.000 15839.371    0.003 layers.py:17(step)
              476747700 1617.072    0.000 15394.071    0.000 layer.py:98(move)
                4767477  129.543    0.000 13022.387    0.003 agent.py:117(_learn)
        299740350/33325362 1196.146    0.000 12733.191    0.000 module.py:715(_call_impl)
                9534954   57.005    0.000 11967.120    0.001 grad_mode.py:23(decorate_context)
               23790408   60.038    0.000 11918.580    0.001 network.py:27(forward)
                9534954  305.943    0.000 11803.054    0.001 adam.py:55(step)
               23790408  295.654    0.000 11723.069    0.000 container.py:115(forward)
                9534954 2164.457    0.000 10184.495    0.001 functional.py:53(adam)
              476747700 1626.241    0.000 9528.777    0.000 layers.py:735(check)
                9487977  215.297    0.000 7805.584    0.001 agent.py:49(__call__)
                4767478  633.614    0.000 7561.263    0.002 layers.py:684(update)
                4767477 3304.580    0.001 7150.299    0.001 agent.py:88(interveen)
                9534954   56.490    0.000 6514.194    0.001 tensor.py:181(backward)
                9534954   33.387    0.000 6457.704    0.001 __init__.py:68(backward)
                4767477 3260.725    0.001 6294.784    0.001 replaybuffer.py:28(teleporter_save_data)
                9534954 6174.761    0.001 6174.761    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                4767477 3627.286    0.001 5810.536    0.001 replaybuffer.py:22(sample_data)
                4767477 2631.180    0.001 5101.687    0.001 agent.py:67(modify)
               47580816   78.094    0.000 4245.376    0.000 conv.py:422(forward)
               47580816   92.166    0.000 4137.761    0.000 conv.py:414(_conv_forward)
               47580816 4030.035    0.000 4030.035    0.000 {built-in method conv2d}
               61836270  131.255    0.000 3797.151    0.000 linear.py:92(forward)
               61836270  237.059    0.000 3606.177    0.000 functional.py:1669(linear)
              476747700  694.642    0.000 3128.901    0.000 layers.py:729(isFree)
              476747700 2028.572    0.000 2888.872    0.000 layers.py:471(check)
               61836270 2589.436    0.000 2589.436    0.000 {built-in method addmm}
              476747700 1833.722    0.000 2533.673    0.000 layers.py:77(check)
              170267519 2461.171    0.000 2461.171    0.000 {built-in method clone}
                4767477   64.000    0.000 2460.817    0.001 agent.py:112(__call__)
              600702156 1564.561    0.000 2448.020    0.000 tensor.py:933(grad)
             3228790926 1984.443    0.000 2434.258    0.000 layer.py:95(isFree)
                9534954  222.496    0.000 2382.192    0.000 optimizer.py:167(zero_grad)
               33372346 1458.467    0.000 2366.618    0.000 layer.py:151(update)
               14255454  102.247    0.000 2348.319    0.000 agent.py:59(modify_board)
             1336926535  666.337    0.000 2310.530    0.000 {built-in method builtins.any}
               38092839 2280.029    0.000 2280.029    0.000 {built-in method cat}
              171629172 2125.485    0.000 2125.485    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
             7604739274 1294.790    0.000 1858.184    0.000 enum.py:646(__hash__)
                4767477   84.863    0.000 1853.599    0.000 replaybuffer.py:18(stacker)
              171629172 1813.593    0.000 1813.593    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               85626678   65.553    0.000 1754.592    0.000 activation.py:713(forward)
               85626678  118.073    0.000 1689.039    0.000 functional.py:1292(leaky_relu)
                2455403   25.314    0.000 1681.887    0.001 layers.py:740(restart)
               85626678 1560.776    0.000 1560.776    0.000 {built-in method torch._C._nn.leaky_relu}
               20358995 1506.925    0.000 1506.925    0.000 {built-in method tensor}
               14255454 1483.548    0.000 1483.548    0.000 {built-in method torch._C._nn.one_hot}
                2455403   13.024    0.000 1423.125    0.001 level.py:8(__init__)
                2455403   93.073    0.000 1276.408    0.001 levels.py:262(generate)
               33375805  173.431    0.000 1261.111    0.000 tensor.py:21(wrapped)
              781727959  418.873    0.000 1208.333    0.000 overrides.py:1070(has_torch_function)
             3794339176  986.232    0.000 1200.791    0.000 layers.py:700(<genexpr>)
              510123605  217.342    0.000 1181.231    0.000 {built-in method builtins.all}
               85814586 1164.383    0.000 1164.383    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                9534954   11.101    0.000 1135.868    0.000 game.py:37(board)
                4767477  674.513    0.000 1135.239    0.000 collector.py:46(collect)
               21897892  191.617    0.000 1102.010    0.000 level.py:41(notUsed)
               85814586 1054.915    0.000 1054.915    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              476747700  761.267    0.000 1026.581    0.000 layers.py:62(check)
             2296490206  575.860    0.000  996.714    0.000 layers.py:690(<genexpr>)
               85814586  971.401    0.000  971.401    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
            10678307648  936.291    0.000  936.291    0.000 layer.py:91(positions)
               85814586  864.176    0.000  864.176    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                9487977  295.481    0.000  832.953    0.000 exploration.py:53(softmaxer)
              184522973  767.275    0.000  767.275    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               85814586  686.525    0.000  686.525    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              476747700  412.355    0.000  620.259    0.000 layers.py:48(check)
             7604773945  563.400    0.000  563.400    0.000 {built-in method builtins.hash}
             1332815372  554.642    0.000  554.642    0.000 layer.py:146(elements)
                9534954   13.468    0.000  549.083    0.000 loss.py:445(forward)
                9534954   55.003    0.000  535.615    0.000 functional.py:2637(mse_loss)
               23837385  525.556    0.000  525.556    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
              476747700  348.526    0.000  509.321    0.000 layers.py:23(check)
               61836270  506.949    0.000  506.949    0.000 {method 't' of 'torch._C._TensorBase' objects}
               21897892   18.123    0.000  498.036    0.000 level.py:38(elementsIn)
        4797298581/4797298579  348.987    0.000  486.413    0.000 {built-in method builtins.len}
               28604862  458.255    0.000  458.255    0.000 {built-in method sum}
             1658667045  351.523    0.000  437.730    0.000 overrides.py:1083(<genexpr>)
              492986908  237.315    0.000  375.912    0.000 layer.py:126(remove)
                9534954  336.081    0.000  336.081    0.000 {built-in method torch._C._nn.mse_loss}
              633701771  244.012    0.000  330.515    0.000 layer.py:130(add)
               47580816   32.234    0.000  325.683    0.000 flatten.py:39(forward)
                4767477  119.795    0.000  321.218    0.000 random.py:315(sample)
               21897892  156.232    0.000  317.281    0.000 level.py:39(<listcomp>)
                4769373  308.107    0.000  308.107    0.000 {method 'ne' of 'torch._C._TensorBase' objects}
             3228790926  302.811    0.000  302.811    0.000 layer.py:203(isBlocking)
                9536378  297.365    0.000  297.365    0.000 {built-in method max}
               47580816  293.448    0.000  293.448    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
             3818749077  290.526    0.000  290.526    0.000 {method 'random' of '_random.Random' objects}
                9487977  269.187    0.000  269.187    0.000 {built-in method multinomial}
              304509723  265.344    0.000  265.344    0.000 {built-in method torch._C._get_tracing_state}
             1009300105  263.224    0.000  263.224    0.000 level.py:32(inverse)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9550921: <Coconuts_teleport_1> in cluster <dcc> Done

Job <Coconuts_teleport_1> was submitted from host <n-62-30-4> by user <s183905> in cluster <dcc> at Tue Apr 20 16:21:52 2021
Job was executed on host(s) <n-62-20-2>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Mon Apr 26 07:08:23 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Apr 26 07:08:23 2021
Terminated at Tue Apr 27 07:03:34 2021
Results reported at Tue Apr 27 07:03:34 2021

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

    CPU time :                                   85895.45 sec.
    Max Memory :                                 2681 MB
    Average Memory :                             2678.44 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13703.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86177 sec.
    Turnaround time :                            571302 sec.

The output (if any) is above this job summary.

