
# Parameters

    Name :                      MONTEST_CF_6c1-1
    Main :                      CFagent
    Level :                     Levels.MonsterLevel
    Hours :                     22.0
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
    Cf convert :                6
    Counterfacts :              1
    Topn :                      7
    Minutes used :              1315 minutes.
    Hours used :                21 hours.

# Profiling


      54520344686 function calls (54266591963 primitive calls) in 78909.05 seconds

##    Ordered by: cumulative time
   List reduced from 505 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 78909.045 78909.045 {built-in method builtins.exec}
                      1    4.826    4.826 78909.045 78909.045 <string>:1(<module>)
                      1  190.982  190.982 78904.219 78904.219 main.py:95(CFagent)
                7436643   29.424    0.000 24495.257    0.003 agent.py:29(learn)
                7436643  612.127    0.000 20435.942    0.003 learner.py:42(Qlearn)
                2478881   13.343    0.000 18597.628    0.008 game.py:41(step)
                2478881   14.871    0.000 18047.137    0.007 layers.py:710(step)
        283159888/29408856 1283.626    0.000 11451.893    0.000 module.py:866(_call_impl)
               21972213   65.310    0.000 10782.798    0.000 network.py:24(forward)
               21972213  348.742    0.000 10566.193    0.000 container.py:117(forward)
                2478881 1667.143    0.001 9588.867    0.004 agent.py:217(counterfact)
                2478882  396.797    0.000 9556.347    0.004 layers.py:676(update)
                2478881  275.934    0.000 9446.598    0.004 agent.py:54(_learn)
                2478881  272.605    0.000 8763.092    0.004 agent.py:209(_learn)
                7436643   70.560    0.000 8662.019    0.001 optimizer.py:84(wrapper)
                2478881  234.183    0.000 8454.306    0.003 layers.py:17(step)
                7436643   34.868    0.000 8336.310    0.001 grad_mode.py:24(decorate_context)
                7436643  245.602    0.000 8226.802    0.001 adam.py:55(step)
              239712233  742.447    0.000 8192.226    0.000 layer.py:98(move)
                7436643 1708.429    0.000 7712.286    0.001 _functional.py:53(adam)
                2478881 3819.063    0.002 7148.569    0.003 replaybuffer.py:28(teleporter_save_data)
                2478881   80.328    0.000 6239.118    0.003 agent.py:117(_learn)
                7267750  212.163    0.000 5730.506    0.001 agent.py:49(__call__)
              239712233  525.531    0.000 5302.073    0.000 layers.py:727(check)
                7436643   33.210    0.000 5076.374    0.001 tensor.py:195(backward)
                7436643   31.962    0.000 5041.644    0.001 __init__.py:68(backward)
                8555980   74.268    0.000 4974.790    0.001 layers.py:731(restart)
                2478881 2981.254    0.001 4930.334    0.002 agent.py:88(interveen)
                7436643 4826.921    0.001 4826.921    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                8555980   38.263    0.000 4230.235    0.000 level.py:8(__init__)
                2310058   57.414    0.000 3969.394    0.002 agent.py:172(choose_action)
                2478881 2975.051    0.001 3914.487    0.002 replaybuffer.py:22(sample_data)
                8555980  688.225    0.000 3871.852    0.000 levels.py:418(generate)
               43944426  105.022    0.000 3746.438    0.000 conv.py:398(forward)
               43944426   67.682    0.000 3594.291    0.000 conv.py:390(_conv_forward)
                2478881 2743.579    0.001 3581.350    0.001 replaybuffer.py:49(sample_data)
               43944426 3526.609    0.000 3526.609    0.000 {built-in method conv2d}
              239712233 1986.695    0.000 3450.558    0.000 layers.py:531(check)
              239057458 3367.022    0.000 3367.022    0.000 {built-in method clone}
               60958877  144.971    0.000 3063.655    0.000 linear.py:93(forward)
               29746578 2007.635    0.000 2982.539    0.000 layer.py:151(update)
               36483993 2854.953    0.000 2854.953    0.000 {built-in method tensor}
               60958877   58.414    0.000 2853.645    0.000 functional.py:1737(linear)
               60958877 2781.037    0.000 2781.037    0.000 {built-in method torch._C._nn.linear}
               30697083   25.078    0.000 2679.562    0.000 game.py:37(board)
                2478881 1767.184    0.001 2551.118    0.001 agent.py:67(modify)
               42779900  408.250    0.000 2525.949    0.000 level.py:41(notUsed)
                2478881  890.840    0.000 1840.696    0.001 replaybuffer.py:55(CF_save_data)
              247398613  197.286    0.000 1744.679    0.000 {built-in method builtins.any}
               82931090   73.344    0.000 1736.496    0.000 activation.py:713(forward)
               82931090   81.040    0.000 1663.151    0.000 functional.py:1364(leaky_relu)
              239668240  303.284    0.000 1651.797    0.000 layers.py:721(isFree)
               37014322 1602.518    0.000 1602.518    0.000 {built-in method cat}
              138817336 1569.679    0.000 1569.679    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               82931090 1564.494    0.000 1564.494    0.000 {built-in method torch._C._nn.leaky_relu}
             1686500562  481.838    0.000 1548.105    0.000 layers.py:692(<genexpr>)
                9746631   68.960    0.000 1514.403    0.000 agent.py:59(modify_board)
             5527262404  990.521    0.000 1434.167    0.000 enum.py:646(__hash__)
                2478881   48.547    0.000 1376.789    0.001 agent.py:168(__call__)
              138817336 1375.080    0.000 1375.080    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
             1343376186 1138.298    0.000 1348.513    0.000 layer.py:95(isFree)
                2478881   46.345    0.000 1296.495    0.001 agent.py:112(__call__)
                7436643  201.187    0.000 1210.784    0.000 optimizer.py:189(zero_grad)
               42779900   36.256    0.000 1091.564    0.000 level.py:38(elementsIn)
              244919731  609.285    0.000  977.161    0.000 layers.py:568(isDead)
                9746631  958.790    0.000  958.790    0.000 {built-in method torch._C._nn.one_hot}
               69408668  860.491    0.000  860.491    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              251282970  839.612    0.000  839.612    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                2310058  705.115    0.000  833.640    0.000 agent.py:183(convert_values)
              239712233  593.570    0.000  832.848    0.000 layers.py:71(check)
               47737662  300.829    0.000  775.710    0.000 random.py:315(sample)
               69408668  754.562    0.000  754.562    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                2478881   48.325    0.000  749.109    0.000 replaybuffer.py:18(stacker)
               69408668  711.540    0.000  711.540    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               69408668  708.102    0.000  708.102    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               42779900  348.958    0.000  695.173    0.000 level.py:39(<listcomp>)
             1825172571  695.021    0.000  695.021    0.000 level.py:32(inverse)
                2478881   46.752    0.000  653.013    0.000 replaybuffer.py:45(stacker)
               51335880   68.424    0.000  651.787    0.000 layer.py:69(restart)
             1937812774  642.213    0.000  642.213    0.000 layer.py:146(elements)
              342285799  125.393    0.000  616.460    0.000 random.py:244(randint)
                7267750  216.349    0.000  592.804    0.000 exploration.py:53(softmaxer)
              781047000  405.347    0.000  583.149    0.000 random.py:250(_randbelow_with_getrandbits)
                2478881  337.599    0.000  559.659    0.000 collector.py:53(collect)
              558995924  395.978    0.000  549.957    0.000 layer.py:126(remove)
               69408668  544.524    0.000  544.524    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              949278784  383.162    0.000  518.090    0.000 layer.py:130(add)
              342285799  207.856    0.000  491.067    0.000 random.py:200(randrange)
              247888200   85.277    0.000  464.283    0.000 {built-in method builtins.all}
                8556080  228.998    0.000  452.054    0.000 layers.py:30(reset)
              485860760  358.954    0.000  449.380    0.000 tensor.py:906(grad)
             5527290771  443.652    0.000  443.652    0.000 {built-in method builtins.hash}
              239712233  292.688    0.000  429.968    0.000 layers.py:42(check)
             4320194418  418.302    0.000  418.302    0.000 layer.py:91(positions)
              823786064  230.152    0.000  412.101    0.000 layers.py:682(<genexpr>)
                7436643   11.482    0.000  394.863    0.000 loss.py:527(forward)
                7436643   30.077    0.000  383.381    0.000 functional.py:2898(mse_loss)
              239712233  130.505    0.000  371.457    0.000 layers.py:565(<listcomp>)
             1848093134  363.237    0.000  363.237    0.000 enum.py:352(<genexpr>)
               42779900  221.499    0.000  360.135    0.000 {built-in method _functools.reduce}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-14>
Subject: Job 9507480: <MONTEST_CF_6c1_1> in cluster <dcc> Done

Job <MONTEST_CF_6c1_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sat Apr 10 02:36:50 2021
Job was executed on host(s) <n-62-20-14>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Apr 11 01:45:15 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun Apr 11 01:45:15 2021
Terminated at Sun Apr 11 23:40:28 2021
Results reported at Sun Apr 11 23:40:28 2021

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

    CPU time :                                   78718.35 sec.
    Max Memory :                                 8248 MB
    Average Memory :                             5937.08 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               8136.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   78913 sec.
    Turnaround time :                            162218 sec.

The output (if any) is above this job summary.

