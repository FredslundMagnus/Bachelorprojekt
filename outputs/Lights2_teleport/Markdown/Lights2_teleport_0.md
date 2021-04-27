
# Parameters

    Name :                      Lights2_teleport-0
    Main :                      teleport
    Level :                     Levels.Causal4
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


      89155604338 function calls (88900191955 primitive calls) in 86105.61 seconds

##    Ordered by: cumulative time
   List reduced from 484 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86105.611 86105.611 {built-in method builtins.exec}
                      1    1.437    1.437 86105.611 86105.611 <string>:1(<module>)
                      1  196.585  196.585 86104.174 86104.174 main.py:45(teleport)
                9143472   33.478    0.000 32640.653    0.004 agent.py:29(learn)
                9143472  772.430    0.000 28010.294    0.003 learner.py:42(Qlearn)
                4571736   18.080    0.000 26953.629    0.006 game.py:41(step)
                4571736   23.141    0.000 25768.313    0.006 layers.py:718(step)
                4571736  150.645    0.000 19618.917    0.004 agent.py:54(_learn)
                4571736  391.630    0.000 16695.110    0.004 layers.py:17(step)
              457173600 1258.422    0.000 16263.299    0.000 layer.py:98(move)
                4571736  127.034    0.000 12970.085    0.003 agent.py:117(_learn)
        287363037/31951665 1140.201    0.000 12674.144    0.000 module.py:715(_call_impl)
                9143472   56.819    0.000 12069.999    0.001 grad_mode.py:23(decorate_context)
                9143472  319.666    0.000 11909.464    0.001 adam.py:55(step)
               22808193   60.596    0.000 11882.188    0.001 network.py:27(forward)
               22808193  313.660    0.000 11691.460    0.001 container.py:115(forward)
              457173600 2131.301    0.000 10603.636    0.000 layers.py:735(check)
                9143472 2192.622    0.000 10280.522    0.001 functional.py:53(adam)
                4571737  652.575    0.000 9020.646    0.002 layers.py:684(update)
                9092985  201.580    0.000 7747.374    0.001 agent.py:49(__call__)
                4571736 2731.913    0.001 6575.988    0.001 agent.py:88(interveen)
                9143472   56.230    0.000 6343.504    0.001 tensor.py:181(backward)
                9143472   31.736    0.000 6287.274    0.001 __init__.py:68(backward)
                9143472 6009.959    0.001 6009.959    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                4571736 3160.968    0.001 5274.972    0.001 replaybuffer.py:22(sample_data)
                4571736 2634.916    0.001 5154.411    0.001 replaybuffer.py:28(teleporter_save_data)
                4571736 2667.154    0.001 5114.626    0.001 agent.py:67(modify)
               45616386   79.087    0.000 4198.586    0.000 conv.py:422(forward)
               45616386   87.839    0.000 4089.997    0.000 conv.py:414(_conv_forward)
               45616386 3986.865    0.000 3986.865    0.000 {built-in method conv2d}
               59281107  136.066    0.000 3809.625    0.000 linear.py:92(forward)
               59281107  236.329    0.000 3613.781    0.000 functional.py:1669(linear)
              457173600  840.369    0.000 3541.675    0.000 layers.py:729(isFree)
               45717370 1754.576    0.000 2931.984    0.000 layer.py:151(update)
             1280018502  782.415    0.000 2831.205    0.000 {built-in method builtins.any}
             3809097282 2128.101    0.000 2701.307    0.000 layer.py:95(isFree)
               59281107 2586.789    0.000 2586.789    0.000 {built-in method addmm}
              576038790 1553.662    0.000 2445.914    0.000 tensor.py:933(grad)
                4571736   61.017    0.000 2426.161    0.001 agent.py:112(__call__)
                9143472  234.960    0.000 2404.017    0.000 optimizer.py:167(zero_grad)
               13664721  101.987    0.000 2306.654    0.000 agent.py:59(modify_board)
             8941764754 1621.597    0.000 2290.345    0.000 enum.py:646(__hash__)
               36523401 2229.776    0.000 2229.776    0.000 {built-in method cat}
              164582496 2144.181    0.000 2144.181    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              136144767 2053.537    0.000 2053.537    0.000 {built-in method clone}
              164582496 1825.061    0.000 1825.061    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                4571736   76.496    0.000 1794.297    0.000 replaybuffer.py:18(stacker)
               82089300   76.861    0.000 1775.865    0.000 activation.py:713(forward)
               82089300  112.212    0.000 1699.004    0.000 functional.py:1292(leaky_relu)
              457173600 1259.001    0.000 1694.568    0.000 layers.py:77(check)
              489178514  242.600    0.000 1689.292    0.000 {built-in method builtins.all}
               19537352 1676.945    0.000 1676.945    0.000 {built-in method tensor}
             4981188410 1288.795    0.000 1590.527    0.000 layers.py:700(<genexpr>)
               82089300 1576.409    0.000 1576.409    0.000 {built-in method torch._C._nn.leaky_relu}
                4338390   47.180    0.000 1543.545    0.000 layers.py:740(restart)
             2291094184  607.412    0.000 1480.413    0.000 layers.py:690(<genexpr>)
              457173600  913.535    0.000 1466.147    0.000 layers.py:246(check)
               13664721 1445.380    0.000 1445.380    0.000 {built-in method torch._C._nn.one_hot}
              457173600  864.007    0.000 1412.277    0.000 layers.py:286(check)
                9143472   11.682    0.000 1309.072    0.000 game.py:37(board)
               32004814  180.330    0.000 1240.548    0.000 tensor.py:21(wrapped)
              749615140  412.755    0.000 1221.362    0.000 overrides.py:1070(has_torch_function)
               82291248 1179.901    0.000 1179.901    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                4571736  682.585    0.000 1143.985    0.000 collector.py:46(collect)
            11776565734 1111.169    0.000 1111.169    0.000 layer.py:91(positions)
                4338390   22.517    0.000 1100.609    0.000 level.py:8(__init__)
               82291248 1068.607    0.000 1068.607    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               82291248  970.514    0.000  970.514    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                4338390  137.353    0.000  875.874    0.000 levels.py:199(generate)
               82291248  872.188    0.000  872.188    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                9092985  293.984    0.000  831.656    0.000 exploration.py:53(softmaxer)
              457173600  587.011    0.000  817.033    0.000 layers.py:62(check)
              457173600  520.673    0.000  803.342    0.000 layers.py:273(check)
              457173700  503.627    0.000  778.562    0.000 layers.py:113(isDone)
              457173600  484.230    0.000  754.718    0.000 layers.py:313(check)
               82291248  691.213    0.000  691.213    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
             1413652653  675.146    0.000  675.146    0.000 layer.py:146(elements)
             8941798057  668.754    0.000  668.754    0.000 {built-in method builtins.hash}
              149809488  663.367    0.000  663.367    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                8676780   69.992    0.000  598.573    0.000 level.py:41(notUsed)
              457173600  392.627    0.000  589.333    0.000 layers.py:48(check)
        6183472426/6183472424  433.918    0.000  576.051    0.000 {built-in method builtins.len}
                9143472   13.746    0.000  535.668    0.000 loss.py:445(forward)
               22858680  529.109    0.000  529.109    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                9143472   48.771    0.000  521.921    0.000 functional.py:2637(mse_loss)
               59281107  510.481    0.000  510.481    0.000 {method 't' of 'torch._C._TensorBase' objects}
              457173600  336.815    0.000  491.642    0.000 layers.py:23(check)
               27430416  456.142    0.000  456.142    0.000 {built-in method sum}
             1590515292  362.836    0.000  452.158    0.000 overrides.py:1083(<genexpr>)
             5046496506  404.548    0.000  404.548    0.000 {method 'random' of '_random.Random' objects}
               43383900   54.093    0.000  381.099    0.000 layer.py:69(restart)
               13248516  143.056    0.000  379.041    0.000 random.py:315(sample)
              662104002  267.509    0.000  362.441    0.000 layer.py:130(add)
                9143472  331.208    0.000  331.208    0.000 {built-in method torch._C._nn.mse_loss}
               45616386   33.377    0.000  328.297    0.000 flatten.py:39(forward)
              401843847  211.724    0.000  308.219    0.000 layer.py:126(remove)
             4528353100  301.732    0.000  301.732    0.000 layer.py:84(isDead)
                9144838  297.028    0.000  297.028    0.000 {built-in method max}
             2980395461  296.005    0.000  296.005    0.000 layer.py:203(isBlocking)
               45616386  294.920    0.000  294.920    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9550892: <Lights2_teleport_0> in cluster <dcc> Done

Job <Lights2_teleport_0> was submitted from host <n-62-30-4> by user <s183905> in cluster <dcc> at Tue Apr 20 16:21:47 2021
Job was executed on host(s) <n-62-11-14>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Wed Apr 21 07:25:21 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed Apr 21 07:25:21 2021
Terminated at Thu Apr 22 07:20:31 2021
Results reported at Thu Apr 22 07:20:31 2021

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

    CPU time :                                   85893.81 sec.
    Max Memory :                                 2680 MB
    Average Memory :                             2676.97 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13704.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86109 sec.
    Turnaround time :                            140324 sec.

The output (if any) is above this job summary.

