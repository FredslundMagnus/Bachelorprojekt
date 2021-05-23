
# Parameters

    Name :                      Diamonds2_convert2-0
    Main :                      CFagent
    Level :                     Levels.Causal5
    Failed actions chance :     0
    Use model :                 False
    Depth :                     1
    Model explore :             100000
    Samples :                   5
    Hours :                     24.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.UCB1
    Network1 :                  Networks.Teleporter
    K1 :                        2000000.0
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
    Layer super1 :              True
    Layer super2 :              True
    Layer super3 :              True
    Layer super4 :              True
    Layer super5 :              True
    Layer super6 :              True
    Layer super7 :              True
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                2
    Counterfacts :              1
    Topn :                      2
    Random counterfacts :       False
    Num :                       0
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      67010615425 function calls (66715629050 primitive calls) in 86115.72 seconds

##    Ordered by: cumulative time
   List reduced from 506 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86115.722 86115.722 {built-in method builtins.exec}
                      1    5.466    5.466 86115.722 86115.722 <string>:1(<module>)
                      1  394.794  394.794 86110.256 86110.256 main.py:80(CFagent)
                9066555   43.922    0.000 23980.777    0.003 agent.py:29(learn)
                9066554  617.550    0.000 19310.405    0.002 learner.py:42(Qlearn)
                3022185   16.102    0.000 18612.308    0.006 game.py:42(step)
                3022185   21.121    0.000 17885.726    0.006 layers.py:827(step)
        329640690/34656006 1421.852    0.000 11492.865    0.000 module.py:866(_call_impl)
               25589452   77.672    0.000 10712.880    0.000 network.py:28(forward)
               25589452  351.179    0.000 10452.801    0.000 container.py:117(forward)
                3022185 1115.304    0.000 10273.184    0.003 agent.py:212(counterfact)
                3022185  308.510    0.000 10211.776    0.003 layers.py:17(step)
              301820106  521.153    0.000 9876.163    0.000 layer.py:106(move)
                3022185  385.092    0.000 9345.169    0.003 agent.py:54(_learn)
                3022185  376.184    0.000 8496.211    0.003 agent.py:204(_learn)
                3022186  473.629    0.000 7620.414    0.003 layers.py:793(update)
                9066554   92.226    0.000 7384.466    0.001 optimizer.py:84(wrapper)
                3022185 4213.235    0.001 7156.395    0.002 replaybuffer.py:28(teleporter_save_data)
                9066554   48.688    0.000 6982.528    0.001 grad_mode.py:24(decorate_context)
                3022185 5882.509    0.002 6951.853    0.002 replaybuffer.py:22(sample_data)
                9066554  303.863    0.000 6830.491    0.001 adam.py:55(step)
                3022185 5711.477    0.002 6726.968    0.002 replaybuffer.py:67(sample_data)
                9066554 1424.984    0.000 6203.582    0.001 _functional.py:53(adam)
              301820106 1258.144    0.000 6189.856    0.000 layers.py:844(check)
                3022185   95.973    0.000 6073.893    0.002 agent.py:117(_learn)
                8260363  253.472    0.000 5804.161    0.001 agent.py:49(__call__)
                3022185 3543.294    0.001 5607.784    0.002 agent.py:88(interveen)
                9066554   39.989    0.000 5162.849    0.001 tensor.py:195(backward)
                9066554   45.657    0.000 5121.516    0.001 __init__.py:68(backward)
                9066554 4868.053    0.001 4868.053    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               47501450 4669.790    0.000 4669.790    0.000 {built-in method tensor}
               40516679   27.512    0.000 4488.414    0.000 game.py:38(board)
               51178904  119.062    0.000 3916.684    0.000 conv.py:398(forward)
               54399339 2180.287    0.000 3878.899    0.000 layer.py:175(NoRock_update)
               51178904   82.056    0.000 3738.849    0.000 conv.py:390(_conv_forward)
               51178904 3656.793    0.000 3656.793    0.000 {built-in method conv2d}
                2218166   50.819    0.000 3198.972    0.001 agent.py:176(choose_action)
               70723986  147.940    0.000 2939.435    0.000 linear.py:93(forward)
                5054481   67.562    0.000 2900.007    0.001 layers.py:849(restart)
              278536735 2753.509    0.000 2753.509    0.000 {built-in method clone}
               70723986   60.319    0.000 2712.094    0.000 functional.py:1737(linear)
               70723986 2637.139    0.000 2637.139    0.000 {built-in method torch._C._nn.linear}
              301820106  607.638    0.000 2616.063    0.000 layers.py:838(isFree)
                3022185 1639.283    0.001 2472.205    0.001 agent.py:67(modify)
                5054481   30.362    0.000 2428.713    0.000 level.py:8(__init__)
                5054481   85.615    0.000 2136.616    0.000 levels.py:249(generate)
             2695575556 1683.887    0.000 2008.425    0.000 layer.py:103(isFree)
               32855703  336.316    0.000 1965.409    0.000 level.py:41(notUsed)
               41504393 1716.784    0.000 1716.784    0.000 {built-in method cat}
             6431007278 1151.526    0.000 1631.318    0.000 enum.py:646(__hash__)
               11282548   86.699    0.000 1626.269    0.000 agent.py:59(modify_board)
                3022185 1217.827    0.000 1580.267    0.001 replaybuffer.py:73(CF_save_data)
               96313438   89.325    0.000 1539.895    0.000 activation.py:713(forward)
                3022184   62.817    0.000 1495.695    0.000 agent.py:172(__call__)
               96313438   83.253    0.000 1450.570    0.000 functional.py:1364(leaky_relu)
                3022185   60.599    0.000 1358.387    0.000 agent.py:112(__call__)
               96313438 1351.688    0.000 1351.688    0.000 {built-in method torch._C._nn.leaky_relu}
              300186305  298.047    0.000 1285.165    0.000 {built-in method builtins.any}
              169242340 1212.111    0.000 1212.111    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               11282548 1076.472    0.000 1076.472    0.000 {built-in method torch._C._nn.one_hot}
              169242340 1070.177    0.000 1070.177    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                9066554  193.411    0.000 1057.722    0.000 optimizer.py:189(zero_grad)
             1075851653 1013.527    0.000 1013.527    0.000 layer.py:154(elements)
             2971641190  807.727    0.000  987.118    0.000 layers.py:809(<genexpr>)
               32855703   26.183    0.000  960.047    0.000 level.py:38(elementsIn)
              301820106  600.946    0.000  928.451    0.000 layers.py:349(check)
              301820106  582.670    0.000  902.874    0.000 layers.py:375(check)
              302218600  121.141    0.000  864.135    0.000 {built-in method builtins.all}
              301820106  546.602    0.000  861.436    0.000 layers.py:387(check)
              301820106  513.663    0.000  827.217    0.000 layers.py:337(check)
                3022185   65.855    0.000  805.710    0.000 replaybuffer.py:18(stacker)
             1279682403  349.315    0.000  781.782    0.000 layers.py:799(<genexpr>)
                3022184   64.991    0.000  767.065    0.000 replaybuffer.py:63(stacker)
               84621170  700.863    0.000  700.863    0.000 {method 'add' of 'torch._C._TensorBase' objects}
             7031184368  670.143    0.000  670.143    0.000 layer.py:99(positions)
               32855703  312.238    0.000  625.601    0.000 level.py:39(<listcomp>)
                2218166  549.341    0.000  617.011    0.000 agent.py:187(convert_values)
               84621170  615.574    0.000  615.574    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                8260363  213.779    0.000  602.993    0.000 exploration.py:53(softmaxer)
              292841467  586.608    0.000  586.608    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               84621170  580.547    0.000  580.547    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
        7499415820/7499415817  518.807    0.000  579.550    0.000 {built-in method builtins.len}
               84621170  576.688    0.000  576.688    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                6044370  185.129    0.000  499.786    0.000 random.py:315(sample)
              592348274  395.836    0.000  493.421    0.000 tensor.py:906(grad)
             6431041805  479.799    0.000  479.799    0.000 {built-in method builtins.hash}
                3022185  278.798    0.000  478.421    0.000 collector.py:46(collect)
                9066554   16.124    0.000  462.028    0.000 loss.py:527(forward)
                9066554   46.790    0.000  445.904    0.000 functional.py:2898(mse_loss)
               84621170  418.791    0.000  418.791    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              301820106  281.226    0.000  417.489    0.000 layers.py:326(check)
               45490329   43.763    0.000  388.724    0.000 layer.py:77(restart)
              301820106  252.106    0.000  386.628    0.000 layers.py:364(check)
             1549583944  383.996    0.000  383.996    0.000 level.py:32(inverse)
              301820106  219.177    0.000  329.388    0.000 layers.py:23(check)
              486019702  212.648    0.000  310.948    0.000 layer.py:138(add)
             1630140077  309.165    0.000  309.165    0.000 enum.py:352(<genexpr>)
               32855703  191.614    0.000  308.264    0.000 {built-in method _functools.reduce}
             2695575556  271.632    0.000  271.632    0.000 layer.py:211(isBlocking)
                5054581  135.195    0.000  271.041    0.000 layers.py:36(reset)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9678085: <Diamonds2_convert2_0> in cluster <dcc> Done

Job <Diamonds2_convert2_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Fri May 21 19:42:39 2021
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sat May 22 18:56:16 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat May 22 18:56:16 2021
Terminated at Sun May 23 18:51:40 2021
Results reported at Sun May 23 18:51:40 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
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

python main.py $MYARGS


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   85782.48 sec.
    Max Memory :                                 9138 MB
    Average Memory :                             6303.53 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               7246.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86124 sec.
    Turnaround time :                            169741 sec.

The output (if any) is above this job summary.

