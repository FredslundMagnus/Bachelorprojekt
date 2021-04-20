
# Parameters

    Name :                      Causal4_Cf_convert1_TopN6-1
    Main :                      CFagent
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
    Cf convert :                1
    Counterfacts :              1
    Topn :                      6
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      78212996520 function calls (77863344561 primitive calls) in 86113.29 seconds

##    Ordered by: cumulative time
   List reduced from 514 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86113.293 86113.293 {built-in method builtins.exec}
                      1    4.296    4.296 86113.293 86113.293 <string>:1(<module>)
                      1  379.475  379.475 86108.996 86108.996 main.py:79(CFagent)
               11340708   41.690    0.000 27363.448    0.002 agent.py:29(learn)
                3780236   15.037    0.000 22723.320    0.006 game.py:41(step)
               11340706  692.598    0.000 22342.327    0.002 learner.py:42(Qlearn)
                3780236   21.257    0.000 21872.294    0.006 layers.py:718(step)
                3780236  361.482    0.000 14990.279    0.004 layers.py:17(step)
              378023600 1123.312    0.000 14596.368    0.000 layer.py:98(move)
        391388575/41738307 1542.197    0.000 12557.837    0.000 module.py:866(_call_impl)
               30397601   83.728    0.000 11735.466    0.000 network.py:27(forward)
               30397601  384.618    0.000 11458.181    0.000 container.py:117(forward)
                3780236  880.625    0.000 10628.321    0.003 agent.py:210(counterfact)
                3780236  373.533    0.000 10621.360    0.003 agent.py:54(_learn)
                3780236  372.267    0.000 9758.664    0.003 agent.py:202(_learn)
              378023600 1818.970    0.000 9033.586    0.000 layers.py:735(check)
               11340706   95.101    0.000 8912.089    0.001 optimizer.py:84(wrapper)
               11340706   47.522    0.000 8484.125    0.001 grad_mode.py:24(decorate_context)
               11340706  337.462    0.000 8333.275    0.001 adam.py:55(step)
               11340706 1751.384    0.000 7616.154    0.001 _functional.py:53(adam)
                3780236  112.166    0.000 6917.743    0.002 agent.py:117(_learn)
                3780237  546.376    0.000 6832.275    0.002 layers.py:684(update)
                9515990  236.003    0.000 6008.025    0.001 agent.py:49(__call__)
               59624092 5960.329    0.000 5960.329    0.000 {built-in method tensor}
               50966329   32.146    0.000 5756.180    0.000 game.py:37(board)
                3780236 4592.819    0.001 5707.964    0.002 replaybuffer.py:22(sample_data)
               11340706   44.420    0.000 5648.549    0.000 tensor.py:195(backward)
               11340706   46.002    0.000 5602.469    0.000 __init__.py:68(backward)
                3780236 4460.365    0.001 5543.740    0.001 replaybuffer.py:67(sample_data)
               11340706 5332.292    0.000 5332.292    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
               75604730 2649.231    0.000 4589.350    0.000 layer.py:151(update)
               60795202  134.251    0.000 4244.702    0.000 conv.py:398(forward)
               60795202   87.339    0.000 4050.113    0.000 conv.py:390(_conv_forward)
               60795202 3962.775    0.000 3962.775    0.000 {built-in method conv2d}
                3780236 1582.428    0.000 3944.910    0.001 agent.py:88(interveen)
              378023600  776.940    0.000 3707.263    0.000 layers.py:729(isFree)
               83632331  168.857    0.000 3209.329    0.000 linear.py:93(forward)
                3780236 1715.981    0.000 3094.343    0.001 replaybuffer.py:28(teleporter_save_data)
               83632331   70.843    0.000 2958.506    0.000 functional.py:1737(linear)
             3637268332 2364.451    0.000 2930.323    0.000 layer.py:95(isFree)
               83632331 2871.950    0.000 2871.950    0.000 {built-in method torch._C._nn.linear}
                3780236 1787.264    0.000 2713.850    0.001 agent.py:67(modify)
                1980435   41.174    0.000 2509.870    0.001 agent.py:175(choose_action)
             7074107839 1317.047    0.000 1842.249    0.000 enum.py:646(__hash__)
               51098576 1825.949    0.000 1825.949    0.000 {built-in method cat}
              114029932   91.416    0.000 1734.124    0.000 activation.py:713(forward)
               13296226   84.223    0.000 1702.086    0.000 agent.py:59(modify_board)
              378180875  381.164    0.000 1696.153    0.000 {built-in method builtins.any}
                3780234   59.189    0.000 1658.014    0.000 agent.py:171(__call__)
              114029932   96.260    0.000 1642.707    0.000 functional.py:1364(leaky_relu)
                3780236   57.055    0.000 1551.888    0.000 agent.py:112(__call__)
              114029932 1527.810    0.000 1527.810    0.000 {built-in method torch._C._nn.leaky_relu}
              211693176 1480.110    0.000 1480.110    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              378023600 1104.373    0.000 1447.304    0.000 layers.py:77(check)
              139960617 1400.126    0.000 1400.126    0.000 {built-in method clone}
              211693176 1325.606    0.000 1325.606    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                3623062   45.481    0.000 1324.319    0.000 layers.py:740(restart)
             4118407018 1088.113    0.000 1314.989    0.000 layers.py:700(<genexpr>)
               11340706  235.530    0.000 1303.945    0.000 optimizer.py:189(zero_grad)
              378023600  809.426    0.000 1271.612    0.000 layers.py:286(check)
                3780236  987.518    0.000 1254.049    0.000 replaybuffer.py:73(CF_save_data)
              378023600  716.803    0.000 1161.075    0.000 layers.py:246(check)
               13296226 1118.471    0.000 1118.471    0.000 {built-in method torch._C._nn.one_hot}
             1248362691 1068.642    0.000 1068.642    0.000 layer.py:146(elements)
                3623062   20.212    0.000  933.335    0.000 level.py:8(__init__)
              105846588  870.721    0.000  870.721    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                3780236   65.251    0.000  841.436    0.000 replaybuffer.py:18(stacker)
             9261706529  838.693    0.000  838.693    0.000 layer.py:91(positions)
                3780234   66.587    0.000  818.371    0.000 replaybuffer.py:63(stacker)
                3623062  121.242    0.000  753.028    0.000 levels.py:199(generate)
              105846588  747.423    0.000  747.423    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              378023600  569.362    0.000  742.293    0.000 layers.py:62(check)
        9980007356/9980007353  647.648    0.000  716.800    0.000 {built-in method builtins.len}
              105846588  710.471    0.000  710.471    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              105846588  700.537    0.000  700.537    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              378023600  419.251    0.000  646.033    0.000 layers.py:273(check)
              378023600  406.907    0.000  636.290    0.000 layers.py:313(check)
              378023700  114.454    0.000  628.896    0.000 {built-in method builtins.all}
                9515990  222.754    0.000  597.925    0.000 exploration.py:53(softmaxer)
              740926200  481.805    0.000  595.975    0.000 tensor.py:906(grad)
               14806596  219.008    0.000  582.528    0.000 random.py:315(sample)
                3780236  342.853    0.000  579.444    0.000 collector.py:46(collect)
             1131128839  275.752    0.000  558.504    0.000 layers.py:690(<genexpr>)
              378023600  361.768    0.000  535.314    0.000 layers.py:48(check)
              105846588  525.566    0.000  525.566    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
             7074150878  525.210    0.000  525.210    0.000 {built-in method builtins.hash}
                7246124   60.258    0.000  512.518    0.000 level.py:41(notUsed)
               11340706   16.178    0.000  476.786    0.000 loss.py:527(forward)
               11340706   43.429    0.000  460.608    0.000 functional.py:2898(mse_loss)
              378023600  288.686    0.000  420.286    0.000 layers.py:23(check)
                1980435  363.986    0.000  363.986    0.000 agent.py:186(convert_values)
               36230620   49.584    0.000  333.166    0.000 layer.py:69(restart)
             4172909022  326.100    0.000  326.100    0.000 {method 'random' of '_random.Random' objects}
              157037077  324.460    0.000  324.460    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
             2892386109  303.589    0.000  303.589    0.000 layer.py:203(isBlocking)
              549512424  220.689    0.000  303.417    0.000 layer.py:130(add)
              332076557  208.649    0.000  295.718    0.000 layer.py:126(remove)
              448609963  199.404    0.000  290.049    0.000 random.py:250(_randbelow_with_getrandbits)
               60795202   43.911    0.000  283.641    0.000 flatten.py:39(forward)
               11340706  283.602    0.000  283.602    0.000 {built-in method torch._C._nn.mse_loss}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9533956: <Causal4_Cf_convert1_TopN6_1> in cluster <dcc> Done

Job <Causal4_Cf_convert1_TopN6_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun Apr 18 20:20:07 2021
Job was executed on host(s) <n-62-11-14>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Apr 18 20:20:08 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun Apr 18 20:20:08 2021
Terminated at Mon Apr 19 20:15:36 2021
Results reported at Mon Apr 19 20:15:36 2021

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

    CPU time :                                   85893.99 sec.
    Max Memory :                                 10454 MB
    Average Memory :                             6753.77 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               5930.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86128 sec.
    Turnaround time :                            86129 sec.

The output (if any) is above this job summary.

