
# Parameters

    Name :                      Diamonds1_simple-0
    Main :                      simple
    Level :                     Levels.Causal2
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
    Network2 :                  Networks.MiniBig
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


      189571564736 function calls (189345609685 primitive calls) in 86119.00 seconds

##    Ordered by: cumulative time
   List reduced from 407 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86118.995 86118.995 {built-in method builtins.exec}
                      1    0.001    0.001 86118.995 86118.995 <string>:1(<module>)
                      1  140.949  140.949 86118.994 86118.994 main.py:66(simple)
                9414779   30.253    0.000 55427.723    0.006 game.py:41(step)
                9414779   42.784    0.000 53462.534    0.006 layers.py:718(step)
                9414780 1340.979    0.000 30893.709    0.003 layers.py:684(update)
                9414779   26.256    0.000 23948.747    0.003 agent.py:29(learn)
                9414779  206.373    0.000 23904.898    0.003 agent.py:117(_learn)
                9414779  614.585    0.000 23698.526    0.003 learner.py:42(Qlearn)
                9414779  689.497    0.000 22472.883    0.002 layers.py:17(step)
              941477900 1539.811    0.000 21703.276    0.000 layer.py:98(move)
               45832480  365.288    0.000 17491.924    0.000 layers.py:740(restart)
               45832480  165.079    0.000 13944.002    0.000 level.py:8(__init__)
              941477900 2832.048    0.000 13633.814    0.000 layers.py:735(check)
               45832480  514.315    0.000 12287.381    0.000 levels.py:151(generate)
              219998810 2038.076    0.000 11248.520    0.000 level.py:41(notUsed)
                9414779   53.740    0.000 9777.580    0.001 grad_mode.py:23(decorate_context)
                9414779  314.216    0.000 9627.330    0.001 adam.py:55(step)
        254199033/28244337  924.491    0.000 9280.179    0.000 module.py:715(_call_impl)
               18829558   39.641    0.000 8596.231    0.000 network.py:27(forward)
               18829558  226.995    0.000 8450.082    0.000 container.py:115(forward)
                9414779 1775.021    0.000 7909.419    0.001 functional.py:53(adam)
            21817760297 3743.866    0.000 5441.956    0.000 enum.py:646(__hash__)
                9414779   49.869    0.000 5309.958    0.001 tensor.py:181(backward)
              219998810  155.237    0.000 5308.850    0.000 level.py:38(elementsIn)
                9414779   30.546    0.000 5260.089    0.001 __init__.py:68(backward)
              941477900 1349.585    0.000 5074.168    0.000 layers.py:729(isFree)
                9414779 5023.817    0.001 5023.817    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                9414779  105.244    0.000 4795.740    0.001 agent.py:112(__call__)
               65903460 2823.581    0.000 4735.438    0.000 layer.py:167(NoRock_update)
             1780634827 1072.814    0.000 3890.681    0.000 {built-in method builtins.any}
              941478000  537.685    0.000 3840.862    0.000 {built-in method builtins.all}
             6423099650 2942.710    0.000 3724.583    0.000 layer.py:95(isFree)
              219998810 1689.698    0.000 3445.727    0.000 level.py:39(<listcomp>)
             5754255109 1536.246    0.000 3418.068    0.000 layers.py:690(<genexpr>)
              320827360  246.683    0.000 3070.350    0.000 layer.py:69(restart)
               37659116   65.233    0.000 3007.566    0.000 conv.py:422(forward)
               37659116   70.713    0.000 2918.114    0.000 conv.py:414(_conv_forward)
               56488674  125.768    0.000 2846.982    0.000 linear.py:92(forward)
               37659116 2831.551    0.000 2831.551    0.000 {built-in method conv2d}
              941477900 1687.146    0.000 2701.217    0.000 layers.py:207(check)
               39882459 2699.126    0.000 2699.126    0.000 {built-in method tensor}
               56488674  205.181    0.000 2664.154    0.000 functional.py:1669(linear)
              941477900 1618.395    0.000 2629.874    0.000 layers.py:219(check)
              941477900 1618.665    0.000 2608.311    0.000 layers.py:231(check)
              659034560 1511.469    0.000 2514.112    0.000 tensor.py:933(grad)
               45832580 1217.243    0.000 2439.821    0.000 layers.py:36(reset)
             7165164160 1917.458    0.000 2355.538    0.000 layers.py:700(<genexpr>)
            10562682123 2289.902    0.000 2289.902    0.000 level.py:32(inverse)
                9414779  205.161    0.000 2169.232    0.000 optimizer.py:167(zero_grad)
               18829558   16.380    0.000 2091.801    0.000 game.py:37(board)
               56488674 1873.996    0.000 1873.996    0.000 {built-in method addmm}
             9569927935 1758.875    0.000 1758.875    0.000 enum.py:352(<genexpr>)
              219998810 1068.840    0.000 1707.886    0.000 {built-in method _functools.reduce}
            21817798046 1698.097    0.000 1698.097    0.000 {built-in method builtins.hash}
            17900463650 1694.274    0.000 1694.274    0.000 layer.py:91(positions)
              941478000 1028.143    0.000 1596.013    0.000 layers.py:113(isDone)
              188295580 1589.373    0.000 1589.373    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
             2594670140 1031.238    0.000 1423.023    0.000 layer.py:130(add)
               45832480  649.781    0.000 1383.186    0.000 level.py:16(<dictcomp>)
              188295580 1328.015    0.000 1328.015    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              809671074  408.684    0.000 1227.661    0.000 overrides.py:1070(has_torch_function)
             5275756903 1190.809    0.000 1190.809    0.000 layer.py:146(elements)
               75318232   63.555    0.000 1188.352    0.000 activation.py:713(forward)
              941477900  760.061    0.000 1177.109    0.000 layers.py:196(check)
               75318232   98.203    0.000 1124.797    0.000 functional.py:1292(leaky_relu)
               75318232 1016.970    0.000 1016.970    0.000 {built-in method torch._C._nn.leaky_relu}
              941477900  671.223    0.000  998.215    0.000 layers.py:23(check)
               94147790  916.316    0.000  916.316    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               94147790  855.342    0.000  855.342    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                9414779  461.323    0.000  799.242    0.000 collector.py:46(collect)
               94147790  760.931    0.000  760.931    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              989264179  454.126    0.000  680.275    0.000 layer.py:126(remove)
               94147790  660.565    0.000  660.565    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
        9132579787/9132579786  595.617    0.000  654.375    0.000 {built-in method builtins.len}
             7699958350  639.046    0.000  639.046    0.000 level.py:39(<lambda>)
             7724567899  624.582    0.000  624.582    0.000 {method 'random' of '_random.Random' objects}
             6423099650  618.221    0.000  618.221    0.000 layer.py:203(isBlocking)
             6878841963  556.551    0.000  556.551    0.000 {method 'append' of 'list' objects}
               94147790  495.642    0.000  495.642    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
             3758272134  470.032    0.000  470.032    0.000 layer.py:182(grid)
                9414779   12.187    0.000  466.190    0.000 loss.py:445(forward)
             1675830822  369.130    0.000  456.244    0.000 overrides.py:1083(<genexpr>)
                9414779   52.876    0.000  454.003    0.000 functional.py:2637(mse_loss)
             6269518640  438.080    0.000  438.080    0.000 layer.py:84(isDead)
                9414779   36.454    0.000  402.471    0.000 exploration.py:47(epsilonGreedy)
              219998810  119.137    0.000  342.006    0.000 random.py:285(choice)
               56488674  339.810    0.000  339.810    0.000 {method 't' of 'torch._C._TensorBase' objects}
                9414779  283.921    0.000  283.921    0.000 {method 'tolist' of 'torch._C._TensorBase' objects}
                9414779  263.728    0.000  263.728    0.000 {built-in method torch._C._nn.mse_loss}
               18829558  261.365    0.000  261.365    0.000 {built-in method sum}
             3809491277  260.055    0.000  260.055    0.000 layer.py:81(isDone)
               94147840  111.966    0.000  255.218    0.000 tensor.py:596(__hash__)
                9415720  241.764    0.000  241.764    0.000 {built-in method max}
              320827360  228.760    0.000  228.760    0.000 layer.py:139(clear2)
               65903460  211.268    0.000  211.268    0.000 layer.py:178(<listcomp>)
               37659116   25.754    0.000  200.687    0.000 flatten.py:39(forward)
              219998810  139.904    0.000  200.328    0.000 random.py:250(_randbelow_with_getrandbits)
               65903460  199.919    0.000  199.919    0.000 layer.py:179(<listcomp>)
                9414779  199.129    0.000  199.129    0.000 {built-in method gather}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9578834: <Diamonds1_simple_0> in cluster <dcc> Done

Job <Diamonds1_simple_0> was submitted from host <n-62-30-3> by user <s183905> in cluster <dcc> at Mon Apr 26 20:44:04 2021
Job was executed on host(s) <n-62-20-10>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Thu Apr 29 14:27:13 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Apr 29 14:27:13 2021
Terminated at Fri Apr 30 14:22:52 2021
Results reported at Fri Apr 30 14:22:52 2021

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

    CPU time :                                   85769.56 sec.
    Max Memory :                                 2063 MB
    Average Memory :                             2059.73 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14321.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86163 sec.
    Turnaround time :                            322728 sec.

The output (if any) is above this job summary.

