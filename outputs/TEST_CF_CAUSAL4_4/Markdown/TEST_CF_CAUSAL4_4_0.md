
# Parameters

    Name :                      TEST_CF_CAUSAL4_4-0
    Main :                      CFagent
    Level :                     Levels.Causal4
    Hours :                     23.0
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
    Cf convert :                4
    Counterfacts :              1
    Topn :                      7
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      73287008432 function calls (72944078317 primitive calls) in 82514.71 seconds

##    Ordered by: cumulative time
   List reduced from 511 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 82514.713 82514.713 {built-in method builtins.exec}
                      1    4.819    4.819 82514.713 82514.713 <string>:1(<module>)
                      1  258.110  258.110 82509.894 82509.894 main.py:95(CFagent)
               11317152   43.853    0.000 26307.754    0.002 agent.py:29(learn)
               11317147  659.090    0.000 21338.956    0.002 learner.py:42(Qlearn)
                3772384   19.830    0.000 21150.713    0.006 game.py:41(step)
                3772384   21.106    0.000 20298.670    0.005 layers.py:710(step)
                3772384  335.829    0.000 13113.162    0.003 layers.py:17(step)
              376860988 1057.468    0.000 12744.270    0.000 layer.py:98(move)
        384080401/41151977 1452.551    0.000 11909.997    0.000 module.py:866(_call_impl)
               29834830   76.519    0.000 11124.807    0.000 network.py:24(forward)
               29834830  347.876    0.000 10862.480    0.000 container.py:117(forward)
                3772384  810.409    0.000 10551.516    0.003 agent.py:217(counterfact)
                3772384  395.685    0.000 10241.360    0.003 agent.py:54(_learn)
                3772384  393.907    0.000 9390.682    0.002 agent.py:209(_learn)
               11317147   88.624    0.000 8332.170    0.001 optimizer.py:84(wrapper)
               11317147   46.519    0.000 7929.797    0.001 grad_mode.py:24(decorate_context)
               11317147  333.234    0.000 7782.823    0.001 adam.py:55(step)
              376860988 1159.979    0.000 7437.586    0.000 layers.py:727(check)
                3772385  537.870    0.000 7130.241    0.002 layers.py:676(update)
               11317147 1625.796    0.000 7084.684    0.001 _functional.py:53(adam)
                3772384  112.412    0.000 6609.320    0.002 agent.py:117(_learn)
               58900381 5883.582    0.000 5883.582    0.000 {built-in method tensor}
                3772384 4519.977    0.001 5775.845    0.002 replaybuffer.py:22(sample_data)
                9248377  239.498    0.000 5689.433    0.001 agent.py:49(__call__)
               50260014   29.315    0.000 5683.927    0.000 game.py:37(board)
               11317147   43.288    0.000 5555.999    0.000 tensor.py:195(backward)
               11317147   44.675    0.000 5511.073    0.000 __init__.py:68(backward)
               11317147 5253.565    0.000 5253.565    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3772384 3885.004    0.001 4977.092    0.001 replaybuffer.py:49(sample_data)
               75447690 2808.302    0.000 4827.675    0.000 layer.py:151(update)
               59669660  124.844    0.000 4061.354    0.000 conv.py:398(forward)
                3772384 1627.405    0.000 3911.912    0.001 agent.py:88(interveen)
               59669660   84.843    0.000 3875.568    0.000 conv.py:390(_conv_forward)
               59669660 3790.725    0.000 3790.725    0.000 {built-in method conv2d}
                3772384 2147.906    0.001 3776.250    0.001 replaybuffer.py:28(teleporter_save_data)
              376601975  649.918    0.000 3557.991    0.000 layers.py:721(isFree)
               81959722  157.960    0.000 3064.362    0.000 linear.py:93(forward)
             3125678730 2432.162    0.000 2908.073    0.000 layer.py:95(isFree)
               81959722   63.109    0.000 2822.679    0.000 functional.py:1737(linear)
               81959722 2743.690    0.000 2743.690    0.000 {built-in method torch._C._nn.linear}
                3772384 1738.172    0.000 2630.645    0.001 agent.py:67(modify)
                1724543   35.068    0.000 2180.539    0.001 agent.py:172(choose_action)
               54516960 1944.253    0.000 1944.253    0.000 {built-in method cat}
             7322824593 1238.120    0.000 1795.073    0.000 enum.py:646(__hash__)
              111794552   95.746    0.000 1621.425    0.000 activation.py:713(forward)
               13020761   78.146    0.000 1613.250    0.000 agent.py:59(modify_board)
                3772379   66.763    0.000 1612.428    0.000 agent.py:168(__call__)
              377744022  374.172    0.000 1595.029    0.000 {built-in method builtins.any}
              168403403 1589.705    0.000 1589.705    0.000 {built-in method clone}
              111794552   92.240    0.000 1525.678    0.000 functional.py:1364(leaky_relu)
                3772384   62.684    0.000 1522.738    0.000 agent.py:112(__call__)
              111794552 1416.406    0.000 1416.406    0.000 {built-in method torch._C._nn.leaky_relu}
              211253404 1405.427    0.000 1405.427    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              376860988 1029.372    0.000 1350.770    0.000 layers.py:71(check)
              211253404 1228.202    0.000 1228.202    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
             4113688007  995.692    0.000 1220.857    0.000 layers.py:692(<genexpr>)
               11317147  207.066    0.000 1207.623    0.000 optimizer.py:189(zero_grad)
              376860988  770.659    0.000 1193.408    0.000 layers.py:240(check)
              377238500  136.783    0.000 1181.010    0.000 {built-in method builtins.all}
                3266863   41.535    0.000 1150.083    0.000 layers.py:731(restart)
             1186947444 1149.471    0.000 1149.471    0.000 layer.py:146(elements)
              376860988  709.576    0.000 1143.733    0.000 layers.py:280(check)
             1535282657  383.859    0.000 1088.499    0.000 layers.py:682(<genexpr>)
               13020761 1068.123    0.000 1068.123    0.000 {built-in method torch._C._nn.one_hot}
                3772384   82.461    0.000  990.130    0.000 replaybuffer.py:18(stacker)
                3772379   72.148    0.000  836.399    0.000 replaybuffer.py:45(stacker)
                3266863   19.184    0.000  808.214    0.000 level.py:8(__init__)
              105626702  794.265    0.000  794.265    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              376860988  617.264    0.000  793.611    0.000 layers.py:56(check)
             8970792844  781.466    0.000  781.466    0.000 layer.py:91(positions)
              105626702  711.931    0.000  711.931    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                3772384  272.054    0.000  677.708    0.000 replaybuffer.py:55(CF_save_data)
              377238500  438.473    0.000  652.097    0.000 layers.py:107(isDone)
                3266863  105.556    0.000  649.257    0.000 levels.py:199(generate)
              105626702  648.592    0.000  648.592    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              105626702  643.889    0.000  643.889    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
        9226433407/9226433404  567.991    0.000  635.818    0.000 {built-in method builtins.len}
              376860988  409.105    0.000  635.412    0.000 layers.py:307(check)
              376860988  365.315    0.000  570.375    0.000 layers.py:267(check)
                9248377  210.534    0.000  569.002    0.000 exploration.py:53(softmaxer)
              739386998  458.093    0.000  568.696    0.000 tensor.py:906(grad)
               14078494  210.915    0.000  558.517    0.000 random.py:315(sample)
             7322867520  556.961    0.000  556.961    0.000 {built-in method builtins.hash}
                3772384  322.824    0.000  548.293    0.000 collector.py:53(collect)
              376860988  337.889    0.000  494.269    0.000 layers.py:42(check)
              105626702  486.068    0.000  486.068    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               11317147   14.333    0.000  460.699    0.000 loss.py:527(forward)
               11317147   40.492    0.000  446.366    0.000 functional.py:2898(mse_loss)
                6533726   52.145    0.000  441.041    0.000 level.py:41(notUsed)
               11317153  430.866    0.000  430.866    0.000 {built-in method nonzero}
                1724543  353.964    0.000  374.227    0.000 agent.py:183(convert_values)
              185196543  351.878    0.000  351.878    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              323523979  210.430    0.000  297.738    0.000 layer.py:126(remove)
               32668630   43.980    0.000  289.767    0.000 layer.py:69(restart)
               75447690  286.689    0.000  286.689    0.000 layer.py:163(<listcomp>)
              518605879  210.603    0.000  286.528    0.000 layer.py:130(add)
               11317147  275.418    0.000  275.418    0.000 {built-in method torch._C._nn.mse_loss}
              446555465  184.256    0.000  273.188    0.000 random.py:250(_randbelow_with_getrandbits)
               59669660   37.398    0.000  262.695    0.000 flatten.py:39(forward)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-4>
Subject: Job 9505790: <TEST_CF_CAUSAL4_4_0> in cluster <dcc> Done

Job <TEST_CF_CAUSAL4_4_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Fri Apr  9 00:44:40 2021
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Fri Apr  9 00:58:42 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Fri Apr  9 00:58:42 2021
Terminated at Fri Apr  9 23:54:05 2021
Results reported at Fri Apr  9 23:54:05 2021

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

    CPU time :                                   82315.56 sec.
    Max Memory :                                 10496 MB
    Average Memory :                             6890.56 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               5888.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   82522 sec.
    Turnaround time :                            83365 sec.

The output (if any) is above this job summary.

