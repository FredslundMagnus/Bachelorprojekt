
# Parameters

    Name :                      CFv2TESTCAU4cf1-0
    Main :                      CFagentv2
    Level :                     Levels.Causal4
    Failed actions chance :     0.0
    Hours :                     16.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Network1 :                  Networks.Teleporter
    K1 :                        500000
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
    K2 :                        100000
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
    Cf convert :                3
    Counterfacts :              1
    Topn :                      5
    Minutes used :              955 minutes.
    Hours used :                15 hours.

# Profiling


      48352098656 function calls (48164658826 primitive calls) in 57309.69 seconds

##    Ordered by: cumulative time
   List reduced from 528 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 57309.693 57309.693 {built-in method builtins.exec}
                      1    5.557    5.557 57309.693 57309.693 <string>:1(<module>)
                      1  177.537  177.537 57304.136 57304.136 main.py:103(CFagentv2)
                6570642   23.523    0.000 15181.363    0.002 agent.py:29(learn)
                2190214   10.961    0.000 13631.316    0.006 game.py:41(step)
                2190214   12.970    0.000 13121.838    0.006 layers.py:719(step)
                6567896  386.545    0.000 12281.230    0.002 learner.py:42(Qlearn)
                2190214  198.223    0.000 8283.231    0.004 layers.py:17(step)
              218716102  590.347    0.000 8067.214    0.000 layer.py:98(move)
        213655277/26217159  842.020    0.000 6901.901    0.000 module.py:866(_call_impl)
               17459049  206.198    0.000 6196.446    0.000 container.py:117(forward)
                2190214  228.463    0.000 5903.636    0.003 agent.py:54(_learn)
                8758110   70.063    0.000 5837.937    0.001 optimizer.py:84(wrapper)
               15240780   41.244    0.000 5743.367    0.000 network.py:24(forward)
                2190214  861.386    0.000 5673.583    0.003 agent.py:236(counterfact2)
                8758110   35.098    0.000 5524.590    0.001 grad_mode.py:24(decorate_context)
                2190214  223.462    0.000 5435.490    0.002 agent.py:202(_learn)
                8758110  243.392    0.000 5409.503    0.001 adam.py:55(step)
              218716102  954.042    0.000 5040.747    0.000 layers.py:736(check)
                8758110 1127.228    0.000 4906.459    0.001 _functional.py:53(adam)
                2190215  326.128    0.000 4803.827    0.002 layers.py:685(update)
                2190214 4126.215    0.002 4623.771    0.002 replaybuffer.py:85(sample_data)
                8758110   33.915    0.000 4040.634    0.000 tensor.py:195(backward)
                8758110   31.851    0.000 4005.550    0.000 __init__.py:68(backward)
                8758110 3810.187    0.000 3810.187    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2190214   64.922    0.000 3805.612    0.002 agent.py:117(_learn)
                2190214 2950.316    0.001 3600.324    0.002 replaybuffer.py:22(sample_data)
                2190214   38.838    0.000 3490.653    0.002 simulator.py:50(learn)
               33978945 3472.852    0.000 3472.852    0.000 {built-in method tensor}
                2190214  227.614    0.000 3451.814    0.002 simulator.py:23(learn)
               29116123   16.309    0.000 3357.088    0.000 game.py:37(board)
                2190214 2679.324    0.001 3302.967    0.002 replaybuffer.py:52(sample_data)
               43804290 1721.313    0.000 2921.572    0.000 layer.py:151(update)
                4267147  111.300    0.000 2667.735    0.001 agent.py:49(__call__)
               37136367   81.605    0.000 2503.212    0.000 conv.py:398(forward)
               37136367   54.347    0.000 2381.396    0.000 conv.py:390(_conv_forward)
               37136367 2327.049    0.000 2327.049    0.000 {built-in method conv2d}
              218716102  349.515    0.000 2055.109    0.000 layers.py:730(isFree)
                2190214  600.711    0.000 1876.633    0.001 agent.py:88(interveen)
             1602907325 1461.332    0.000 1705.594    0.000 layer.py:95(isFree)
               41341912   82.314    0.000 1578.510    0.000 linear.py:93(forward)
                2190214 1020.131    0.000 1546.719    0.001 agent.py:67(modify)
               41341912   31.520    0.000 1453.357    0.000 functional.py:1737(linear)
               41341912 1414.132    0.000 1414.132    0.000 {built-in method torch._C._nn.linear}
               37134682 1373.550    0.000 1373.550    0.000 {built-in method cat}
                2190214  617.927    0.000 1106.505    0.001 replaybuffer.py:28(teleporter_save_data)
             4413931135  736.423    0.000 1050.570    0.000 enum.py:646(__hash__)
                2832816   34.745    0.000 1002.120    0.000 layers.py:741(restart)
              148879632  961.812    0.000  961.812    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                2187468   41.706    0.000  958.107    0.000 agent.py:171(__call__)
              219021500  126.034    0.000  930.113    0.000 {built-in method builtins.all}
              218378899  215.429    0.000  928.680    0.000 {built-in method builtins.any}
               61019230   48.513    0.000  902.614    0.000 activation.py:713(forward)
                2190214   38.309    0.000  896.901    0.000 agent.py:112(__call__)
                8758110  152.877    0.000  864.245    0.000 optimizer.py:189(zero_grad)
               61019230   49.723    0.000  854.101    0.000 functional.py:1364(leaky_relu)
              148879632  840.717    0.000  840.717    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
             1533798916  365.005    0.000  829.915    0.000 layers.py:691(<genexpr>)
              218716102  619.616    0.000  810.339    0.000 layers.py:78(check)
                6457361   37.920    0.000  798.516    0.000 agent.py:59(modify_board)
               61019230  794.320    0.000  794.320    0.000 {built-in method torch._C._nn.leaky_relu}
                2190214  618.769    0.000  793.670    0.000 replaybuffer.py:58(CF_save_data)
                8675630  728.998    0.000  728.998    0.000 {built-in method torch._C._nn.one_hot}
             2378075524  584.355    0.000  713.250    0.000 layers.py:701(<genexpr>)
                2832816   16.626    0.000  709.755    0.000 level.py:8(__init__)
              771269104  699.391    0.000  699.391    0.000 layer.py:146(elements)
              218716102  454.640    0.000  698.202    0.000 layers.py:247(check)
               64773298  640.127    0.000  640.127    0.000 {built-in method clone}
              218716102  392.696    0.000  633.727    0.000 layers.py:287(check)
                2218269    9.046    0.000  624.457    0.000 simulator.py:20(boardforward)
                2190214  494.881    0.000  598.664    0.000 replaybuffer.py:91(simulator_save_data)
                2832816  105.712    0.000  578.376    0.000 levels.py:199(generate)
               74439816  570.084    0.000  570.084    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              218716102  408.498    0.000  499.646    0.000 layers.py:63(check)
                2190214   34.939    0.000  495.687    0.000 replaybuffer.py:18(stacker)
             5589671757  491.846    0.000  491.846    0.000 layer.py:91(positions)
               74439816  491.325    0.000  491.325    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               12236274  186.290    0.000  479.717    0.000 random.py:315(sample)
                2187468   35.170    0.000  476.559    0.000 replaybuffer.py:48(stacker)
               74439816  450.242    0.000  450.242    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               74439816  446.670    0.000  446.670    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              521078802  323.062    0.000  400.096    0.000 tensor.py:906(grad)
              219021500  273.478    0.000  398.705    0.000 layers.py:114(isDone)
        5808323569/5808323565  355.634    0.000  393.550    0.000 {built-in method builtins.len}
                5665632   43.061    0.000  387.674    0.000 level.py:41(notUsed)
              218716102  246.972    0.000  372.538    0.000 layers.py:314(check)
                8758110   10.904    0.000  361.866    0.000 loss.py:527(forward)
               32907725  357.431    0.000  357.431    0.000 {method 'item' of 'torch._C._TensorBase' objects}
              218716102  232.907    0.000  354.306    0.000 layers.py:274(check)
                8758110   32.039    0.000  350.962    0.000 functional.py:2898(mse_loss)
                2190214   30.075    0.000  346.240    0.000 replaybuffer.py:81(stacker)
               74439816  341.586    0.000  341.586    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
             4413956366  314.151    0.000  314.151    0.000 {built-in method builtins.hash}
                2190214  185.582    0.000  304.906    0.000 collector.py:46(collect)
              218716102  203.710    0.000  295.917    0.000 layers.py:49(check)
                4267147   99.976    0.000  280.336    0.000 exploration.py:53(softmaxer)
               28328160   35.205    0.000  248.784    0.000 layer.py:69(restart)
                2190214   44.289    0.000  245.023    0.000 agent.py:277(counterfact_check)
                7185930  235.173    0.000  235.173    0.000 {built-in method nonzero}
              342103744  180.010    0.000  231.599    0.000 layer.py:130(add)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-3>
Subject: Job 9511603: <CFv2TESTCAU4cf1_0> in cluster <dcc> Done

Job <CFv2TESTCAU4cf1_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon Apr 12 20:13:41 2021
Job was executed on host(s) <n-62-20-3>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon Apr 12 21:08:00 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Apr 12 21:08:00 2021
Terminated at Tue Apr 13 13:03:15 2021
Results reported at Tue Apr 13 13:03:15 2021

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

    CPU time :                                   57175.32 sec.
    Max Memory :                                 9237 MB
    Average Memory :                             6474.31 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               7147.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   57316 sec.
    Turnaround time :                            60574 sec.

The output (if any) is above this job summary.

