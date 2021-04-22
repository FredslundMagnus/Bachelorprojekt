
# Parameters

    Name :                      Causal4_Cf_convert1_TopN3-1
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
    Topn :                      3
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      73499695785 function calls (73167942594 primitive calls) in 86110.52 seconds

##    Ordered by: cumulative time
   List reduced from 513 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86110.522 86110.522 {built-in method builtins.exec}
                      1    4.413    4.413 86110.522 86110.522 <string>:1(<module>)
                      1  378.954  378.954 86106.109 86106.109 main.py:79(CFagent)
               10591980   37.263    0.000 26322.510    0.002 agent.py:29(learn)
                3530660   14.088    0.000 22470.748    0.006 game.py:41(step)
                3530660   20.070    0.000 21656.762    0.006 layers.py:718(step)
               10591975  662.136    0.000 21426.892    0.002 learner.py:42(Qlearn)
                3530660  323.390    0.000 14607.904    0.004 layers.py:17(step)
              352739643 1061.527    0.000 14253.666    0.000 layer.py:98(move)
        371166320/39414820 1514.069    0.000 12340.136    0.000 module.py:866(_call_impl)
               28822845   78.763    0.000 11553.314    0.000 network.py:27(forward)
               28822845  361.063    0.000 11271.181    0.000 container.py:117(forward)
                3530660  987.808    0.000 10860.396    0.003 agent.py:210(counterfact)
                3530660  374.156    0.000 10234.782    0.003 agent.py:54(_learn)
                3530660  368.874    0.000 9390.629    0.003 agent.py:202(_learn)
              352739643 1720.288    0.000 8872.072    0.000 layers.py:735(check)
               10591975   90.710    0.000 8438.630    0.001 optimizer.py:84(wrapper)
               10591975   45.276    0.000 8039.157    0.001 grad_mode.py:24(decorate_context)
               10591975  325.991    0.000 7891.173    0.001 adam.py:55(step)
               10591975 1638.291    0.000 7198.829    0.001 _functional.py:53(adam)
                3530661  520.286    0.000 6999.846    0.002 layers.py:684(update)
                3530660  108.517    0.000 6636.671    0.002 agent.py:117(_learn)
                3530660 5058.853    0.001 6151.241    0.002 replaybuffer.py:22(sample_data)
                9107733  233.676    0.000 5975.133    0.001 agent.py:49(__call__)
                3530660 4839.244    0.001 5895.613    0.002 replaybuffer.py:67(sample_data)
               56526873 5738.976    0.000 5738.976    0.000 {built-in method tensor}
               48420253   31.752    0.000 5538.415    0.000 game.py:37(board)
               10591975   43.793    0.000 5495.171    0.001 tensor.py:195(backward)
               10591975   40.499    0.000 5449.888    0.001 __init__.py:68(backward)
               10591975 5198.180    0.000 5198.180    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
               70613210 2758.831    0.000 4699.782    0.000 layer.py:151(update)
               57645690  134.197    0.000 4193.223    0.000 conv.py:398(forward)
               57645690   79.683    0.000 3993.003    0.000 conv.py:390(_conv_forward)
                3530660 1698.960    0.000 3992.903    0.001 agent.py:88(interveen)
               57645690 3913.319    0.000 3913.319    0.000 {built-in method conv2d}
              352739643  758.528    0.000 3609.829    0.000 layers.py:729(isFree)
                3530660 1879.967    0.001 3365.482    0.001 replaybuffer.py:28(teleporter_save_data)
               79407215  165.116    0.000 3173.554    0.000 linear.py:93(forward)
               79407215   67.130    0.000 2922.996    0.000 functional.py:1737(linear)
             3291355156 2315.934    0.000 2851.301    0.000 layer.py:95(isFree)
               79407215 2839.306    0.000 2839.306    0.000 {built-in method torch._C._nn.linear}
                2061822   43.143    0.000 2701.760    0.001 agent.py:175(choose_action)
                3530660 1761.818    0.000 2662.313    0.001 agent.py:67(modify)
             6741985266 1306.913    0.000 1850.500    0.000 enum.py:646(__hash__)
               47944968 1789.063    0.000 1789.063    0.000 {built-in method cat}
              108230060   93.906    0.000 1693.870    0.000 activation.py:713(forward)
              352606249  374.524    0.000 1679.888    0.000 {built-in method builtins.any}
               12638393   81.411    0.000 1672.545    0.000 agent.py:59(modify_board)
                3530655   58.863    0.000 1610.524    0.000 agent.py:171(__call__)
              108230060   91.853    0.000 1599.964    0.000 functional.py:1364(leaky_relu)
              144605415 1524.928    0.000 1524.928    0.000 {built-in method clone}
                3990512   47.737    0.000 1514.697    0.000 layers.py:740(restart)
                3530660   55.747    0.000 1509.513    0.000 agent.py:112(__call__)
              108230060 1489.432    0.000 1489.432    0.000 {built-in method torch._C._nn.leaky_relu}
              197716860 1409.151    0.000 1409.151    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              352739643 1032.198    0.000 1366.703    0.000 layers.py:77(check)
                3530660 1059.534    0.000 1360.935    0.000 replaybuffer.py:73(CF_save_data)
             3839831468 1086.182    0.000 1305.364    0.000 layers.py:700(<genexpr>)
              197716860 1253.777    0.000 1253.777    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              352739643  783.381    0.000 1246.095    0.000 layers.py:246(check)
               10591975  220.339    0.000 1237.763    0.000 optimizer.py:189(zero_grad)
              352739643  710.346    0.000 1151.916    0.000 layers.py:286(check)
               12638393 1096.802    0.000 1096.802    0.000 {built-in method torch._C._nn.one_hot}
             1253898272 1077.119    0.000 1077.119    0.000 layer.py:146(elements)
                3990512   22.458    0.000 1064.474    0.000 level.py:8(__init__)
                3990512  136.128    0.000  860.007    0.000 levels.py:199(generate)
               98858430  830.254    0.000  830.254    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                3530660   63.654    0.000  825.309    0.000 replaybuffer.py:18(stacker)
             8708214126  819.287    0.000  819.287    0.000 layer.py:91(positions)
                3530655   66.088    0.000  797.827    0.000 replaybuffer.py:63(stacker)
              352739643  587.562    0.000  767.621    0.000 layers.py:62(check)
        9373615603/9373615600  640.813    0.000  708.917    0.000 {built-in method builtins.len}
               98858430  708.917    0.000  708.917    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               98858430  668.725    0.000  668.725    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               98858430  662.100    0.000  662.100    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              352739643  426.798    0.000  660.046    0.000 layers.py:313(check)
              352739643  413.131    0.000  643.283    0.000 layers.py:273(check)
              353066100   85.548    0.000  603.854    0.000 {built-in method builtins.all}
                9107733  219.239    0.000  592.582    0.000 exploration.py:53(softmaxer)
                7981024   67.633    0.000  587.179    0.000 level.py:41(notUsed)
               15042344  218.580    0.000  578.634    0.000 random.py:315(sample)
              692009094  458.753    0.000  572.567    0.000 tensor.py:906(grad)
              890319230  225.404    0.000  563.255    0.000 layers.py:690(<genexpr>)
                3530660  322.844    0.000  548.231    0.000 collector.py:46(collect)
             6742025505  543.595    0.000  543.595    0.000 {built-in method builtins.hash}
              352739643  362.438    0.000  530.291    0.000 layers.py:48(check)
               98858430  493.802    0.000  493.802    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               10591975   15.084    0.000  455.628    0.000 loss.py:527(forward)
               10591975   39.468    0.000  440.544    0.000 functional.py:2898(mse_loss)
              352739643  297.648    0.000  425.556    0.000 layers.py:23(check)
               39905120   56.047    0.000  388.515    0.000 layer.py:69(restart)
                2061822  385.845    0.000  385.845    0.000 agent.py:186(convert_values)
              160774463  338.424    0.000  338.424    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
             3895964626  327.333    0.000  327.333    0.000 {method 'random' of '_random.Random' objects}
              557572685  241.327    0.000  326.287    0.000 layer.py:130(add)
              320924238  234.550    0.000  323.118    0.000 layer.py:126(remove)
              429114794  198.880    0.000  290.876    0.000 random.py:250(_randbelow_with_getrandbits)
             2590472625  290.785    0.000  290.785    0.000 layer.py:203(isBlocking)
               57645690   40.763    0.000  280.807    0.000 flatten.py:39(forward)
               10591975  274.791    0.000  274.791    0.000 {built-in method torch._C._nn.mse_loss}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9551810: <Causal4_Cf_convert1_TopN3_1> in cluster <dcc> Done

Job <Causal4_Cf_convert1_TopN3_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed Apr 21 03:20:30 2021
Job was executed on host(s) <n-62-20-16>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed Apr 21 03:41:13 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed Apr 21 03:41:13 2021
Terminated at Thu Apr 22 03:36:29 2021
Results reported at Thu Apr 22 03:36:29 2021

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

    CPU time :                                   85894.20 sec.
    Max Memory :                                 9975 MB
    Average Memory :                             6577.48 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               6409.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86115 sec.
    Turnaround time :                            87359 sec.

The output (if any) is above this job summary.

