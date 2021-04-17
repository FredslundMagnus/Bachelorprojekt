
# Parameters

    Name :                      cococonuts_teleport-0
    Main :                      teleport
    Level :                     Levels.Coconuts
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
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                2
    Counterfacts :              1
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      94266902195 function calls (93921256076 primitive calls) in 86110.96 seconds

##    Ordered by: cumulative time
   List reduced from 493 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86110.959 86110.959 {built-in method builtins.exec}
                      1    2.028    2.028 86110.959 86110.959 <string>:1(<module>)
                      1  280.095  280.095 86108.930 86108.930 main.py:40(teleport)
                6200457   26.232    0.000 31626.627    0.005 game.py:41(step)
                6200457   30.874    0.000 30405.282    0.005 layers.py:710(step)
               12400914   44.101    0.000 27452.653    0.002 agent.py:29(learn)
               12400914  723.422    0.000 22650.079    0.002 learner.py:42(Qlearn)
                6200457  519.400    0.000 20607.786    0.003 layers.py:17(step)
              620045700 2126.062    0.000 20038.382    0.000 layer.py:98(move)
                6200457  653.264    0.000 16670.084    0.003 agent.py:54(_learn)
              620045700 1543.330    0.000 12272.632    0.000 layers.py:727(check)
        388916600/43271492 1442.879    0.000 11974.106    0.000 module.py:866(_call_impl)
               30870578   87.705    0.000 11109.531    0.000 network.py:24(forward)
               30870578  344.243    0.000 10833.716    0.000 container.py:117(forward)
                6200457  184.099    0.000 10710.078    0.002 agent.py:117(_learn)
                6200458  818.533    0.000 9720.107    0.002 layers.py:676(update)
               12400914  101.331    0.000 8698.417    0.001 optimizer.py:84(wrapper)
               12400914   51.330    0.000 8246.684    0.001 grad_mode.py:24(decorate_context)
               12400914  331.779    0.000 8081.755    0.001 adam.py:55(step)
               12269207  286.347    0.000 7447.687    0.001 agent.py:49(__call__)
                6200457 5363.562    0.001 7412.510    0.001 replaybuffer.py:22(sample_data)
               12400914 1689.295    0.000 7358.791    0.001 _functional.py:53(adam)
               12400914   48.697    0.000 5935.504    0.000 tensor.py:195(backward)
                6200457 2321.261    0.000 5905.344    0.001 agent.py:88(interveen)
               12400914   48.215    0.000 5885.067    0.000 __init__.py:68(backward)
               12400914 5605.087    0.000 5605.087    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                6200457 3082.943    0.000 5332.777    0.001 replaybuffer.py:28(teleporter_save_data)
              620045700 3608.868    0.000 4957.967    0.000 layers.py:464(check)
              620045700  801.920    0.000 4210.373    0.000 layers.py:721(isFree)
                6200457 2730.730    0.000 4174.290    0.001 agent.py:67(modify)
               61741156  134.003    0.000 4127.924    0.000 conv.py:398(forward)
               61741156   79.397    0.000 3934.629    0.000 conv.py:390(_conv_forward)
               61741156 3855.233    0.000 3855.233    0.000 {built-in method conv2d}
              620045700 2527.973    0.000 3464.861    0.000 layers.py:71(check)
             4025189396 2803.711    0.000 3408.453    0.000 layer.py:95(isFree)
               43403206 1980.860    0.000 3204.443    0.000 layer.py:151(update)
               80210820  156.036    0.000 3002.936    0.000 linear.py:93(forward)
               80210820   68.696    0.000 2771.477    0.000 functional.py:1737(linear)
               80210820 2686.928    0.000 2686.928    0.000 {built-in method torch._C._nn.linear}
                2910550   33.570    0.000 2621.340    0.001 layers.py:731(restart)
            11099954348 1797.472    0.000 2582.448    0.000 enum.py:646(__hash__)
                6200457   85.882    0.000 2391.424    0.000 agent.py:112(__call__)
                2910550   14.726    0.000 2299.763    0.001 level.py:8(__init__)
               18469664  117.181    0.000 2279.789    0.000 agent.py:59(modify_board)
                2910550  132.501    0.000 2125.959    0.001 levels.py:262(generate)
              617135251  462.733    0.000 1990.249    0.000 {built-in method builtins.any}
              220138872 1950.234    0.000 1950.234    0.000 {built-in method clone}
               55672406 1934.349    0.000 1934.349    0.000 {built-in method cat}
               36025931  303.389    0.000 1868.069    0.000 level.py:41(notUsed)
               26384773 1717.812    0.000 1717.812    0.000 {built-in method tensor}
                6200457  114.134    0.000 1604.761    0.000 replaybuffer.py:18(stacker)
              111081398   88.886    0.000 1603.457    0.000 activation.py:713(forward)
             4937082000 1263.540    0.000 1527.516    0.000 layers.py:692(<genexpr>)
              111081398   92.692    0.000 1514.571    0.000 functional.py:1364(leaky_relu)
               18469664 1503.494    0.000 1503.494    0.000 {built-in method torch._C._nn.one_hot}
              223216452 1421.585    0.000 1421.585    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              111081398 1403.498    0.000 1403.498    0.000 {built-in method torch._C._nn.leaky_relu}
              620045700 1045.133    0.000 1385.873    0.000 layers.py:56(check)
               12400914   13.316    0.000 1364.846    0.000 game.py:37(board)
               12400914  231.516    0.000 1290.908    0.000 optimizer.py:189(zero_grad)
              223216452 1277.053    0.000 1277.053    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
            12489958310 1062.530    0.000 1062.530    0.000 layer.py:91(positions)
                6200457  515.556    0.000  877.183    0.000 collector.py:53(collect)
              111608226  847.872    0.000  847.872    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              620045800  145.595    0.000  844.789    0.000 {built-in method builtins.all}
               36025931   34.470    0.000  834.236    0.000 level.py:38(elementsIn)
            11099999387  784.984    0.000  784.984    0.000 {built-in method builtins.hash}
              620045700  522.833    0.000  779.189    0.000 layers.py:42(check)
             1698893156  388.446    0.000  773.234    0.000 layers.py:682(<genexpr>)
               12269207  282.357    0.000  749.870    0.000 exploration.py:53(softmaxer)
             1655652372  746.672    0.000  746.672    0.000 layer.py:146(elements)
              111608226  744.452    0.000  744.452    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              111608226  680.337    0.000  680.337    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              111608226  671.326    0.000  671.326    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              781257636  489.791    0.000  605.712    0.000 tensor.py:906(grad)
               36025931  268.086    0.000  529.818    0.000 level.py:39(<listcomp>)
               12400914   17.222    0.000  511.718    0.000 loss.py:527(forward)
              111608226  508.182    0.000  508.182    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               12400914   46.191    0.000  494.496    0.000 functional.py:2898(mse_loss)
        6012966663/6012966661  413.439    0.000  492.876    0.000 {built-in method builtins.len}
             1607192550  479.192    0.000  479.192    0.000 level.py:32(inverse)
              613328650  303.083    0.000  476.920    0.000 layer.py:126(remove)
              238608536  456.052    0.000  456.052    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              784884446  323.887    0.000  433.951    0.000 layer.py:130(add)
                6200457  157.212    0.000  432.453    0.000 random.py:315(sample)
             4025189396  420.723    0.000  420.723    0.000 layer.py:203(isBlocking)
               37202742  378.022    0.000  378.022    0.000 {built-in method sum}
             1240091400  372.561    0.000  372.561    0.000 {method 'union' of 'set' objects}
               12400914  302.645    0.000  302.645    0.000 {built-in method torch._C._nn.mse_loss}
                6200457   26.506    0.000  292.776    0.000 exploration.py:47(epsilonGreedy)
               61741156   44.889    0.000  281.405    0.000 flatten.py:39(forward)
               20373850   39.963    0.000  281.266    0.000 layer.py:69(restart)
               12402760  275.692    0.000  275.692    0.000 {built-in method max}
               36025931  165.902    0.000  269.948    0.000 {built-in method _functools.reduce}
             1401714806  245.762    0.000  245.762    0.000 enum.py:352(<genexpr>)
               61741156  236.516    0.000  236.516    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               12269207  235.967    0.000  235.967    0.000 {built-in method multinomial}
              620045800  176.027    0.000  233.914    0.000 layers.py:46(isDone)
             2896286968  224.607    0.000  224.607    0.000 {method 'append' of 'list' objects}
               12400914   48.324    0.000  221.751    0.000 __init__.py:28(_make_grads)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-3>
Subject: Job 9501864: <cococonuts_teleport_0> in cluster <dcc> Done

Job <cococonuts_teleport_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed Apr  7 15:46:07 2021
Job was executed on host(s) <n-62-20-3>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed Apr  7 17:20:38 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed Apr  7 17:20:38 2021
Terminated at Thu Apr  8 17:15:57 2021
Results reported at Thu Apr  8 17:15:57 2021

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

    CPU time :                                   85903.45 sec.
    Max Memory :                                 11053 MB
    Average Memory :                             6905.92 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               5331.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86119 sec.
    Turnaround time :                            91790 sec.

The output (if any) is above this job summary.

