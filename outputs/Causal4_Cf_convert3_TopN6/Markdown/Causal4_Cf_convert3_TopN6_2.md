
# Parameters

    Name :                      Causal4_Cf_convert3_TopN6-2
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
    Cf convert :                3
    Counterfacts :              1
    Topn :                      6
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      63259532071 function calls (62973127356 primitive calls) in 86110.72 seconds

##    Ordered by: cumulative time
   List reduced from 513 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86110.719 86110.719 {built-in method builtins.exec}
                      1    4.437    4.437 86110.719 86110.719 <string>:1(<module>)
                      1  351.881  351.881 86106.282 86106.282 main.py:79(CFagent)
                9323391   37.466    0.000 30515.049    0.003 agent.py:29(learn)
                9323390  760.966    0.000 25474.520    0.003 learner.py:42(Qlearn)
                3107797   15.128    0.000 19107.836    0.006 game.py:41(step)
                3107797   21.375    0.000 18304.095    0.006 layers.py:718(step)
        320629265/34226241 1412.598    0.000 12927.361    0.000 module.py:866(_call_impl)
                3107797  283.967    0.000 12499.339    0.004 layers.py:17(step)
              310522397  901.574    0.000 12187.277    0.000 layer.py:98(move)
               24902851   74.521    0.000 12120.929    0.000 network.py:27(forward)
               24902851  378.732    0.000 11877.106    0.000 container.py:117(forward)
                3107797  343.588    0.000 11770.023    0.004 agent.py:54(_learn)
                3107797  339.237    0.000 10904.608    0.004 agent.py:202(_learn)
                9323390   84.640    0.000 10825.362    0.001 optimizer.py:84(wrapper)
                9323390   41.970    0.000 10418.835    0.001 grad_mode.py:24(decorate_context)
                9323390  295.109    0.000 10282.713    0.001 adam.py:55(step)
                3107797  948.701    0.000 10072.254    0.003 agent.py:210(counterfact)
                9323390 2115.846    0.000 9653.956    0.001 _functional.py:53(adam)
                3107797  101.841    0.000 7781.240    0.003 agent.py:117(_learn)
              310522397 1528.139    0.000 7568.397    0.000 layers.py:735(check)
                9323390   41.020    0.000 6310.185    0.001 tensor.py:195(backward)
                9323390   36.960    0.000 6267.611    0.001 __init__.py:68(backward)
                7783831  222.198    0.000 6138.485    0.001 agent.py:49(__call__)
                9323390 6005.314    0.001 6005.314    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3107798  466.246    0.000 5757.008    0.002 layers.py:684(update)
                3107797 4374.436    0.001 5461.969    0.002 replaybuffer.py:22(sample_data)
               48978509 5332.582    0.000 5332.582    0.000 {built-in method tensor}
                3107797 4174.609    0.001 5225.172    0.002 replaybuffer.py:67(sample_data)
               41804297   29.834    0.000 5106.842    0.000 game.py:37(board)
                3107797 1964.039    0.001 4402.445    0.001 agent.py:88(interveen)
               49805702  120.395    0.000 4265.069    0.000 conv.py:398(forward)
               62155950 2380.357    0.000 4106.900    0.000 layer.py:151(update)
               49805702   71.968    0.000 4091.025    0.000 conv.py:390(_conv_forward)
               49805702 4019.057    0.000 4019.057    0.000 {built-in method conv2d}
                3107797 2014.341    0.001 3796.810    0.001 replaybuffer.py:28(teleporter_save_data)
               68492959  151.443    0.000 3452.323    0.000 linear.py:93(forward)
               68492959   64.559    0.000 3229.193    0.000 functional.py:1737(linear)
               68492959 3148.609    0.000 3148.609    0.000 {built-in method torch._C._nn.linear}
              310522397  663.102    0.000 3098.271    0.000 layers.py:729(isFree)
                3107797 1931.530    0.001 2915.497    0.001 agent.py:67(modify)
                1580037   39.802    0.000 2585.448    0.002 agent.py:175(choose_action)
             2781219696 2001.874    0.000 2435.170    0.000 layer.py:95(isFree)
              174036612 1977.781    0.000 1977.781    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               93395810   80.222    0.000 1928.484    0.000 activation.py:713(forward)
               41969593 1857.728    0.000 1857.728    0.000 {built-in method cat}
               93395810   86.874    0.000 1848.262    0.000 functional.py:1364(leaky_relu)
               93395810 1743.810    0.000 1743.810    0.000 {built-in method torch._C._nn.leaky_relu}
              174036612 1743.422    0.000 1743.422    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              119919079 1734.100    0.000 1734.100    0.000 {built-in method clone}
               10891628   81.376    0.000 1714.773    0.000 agent.py:59(modify_board)
                3107796   58.075    0.000 1702.621    0.001 agent.py:171(__call__)
                3107797   55.322    0.000 1596.678    0.001 agent.py:112(__call__)
             5800944270 1085.272    0.000 1541.392    0.000 enum.py:646(__hash__)
                9323390  247.140    0.000 1523.548    0.000 optimizer.py:189(zero_grad)
              310956900  332.363    0.000 1437.193    0.000 {built-in method builtins.any}
                3107797 1071.111    0.000 1380.252    0.000 replaybuffer.py:73(CF_save_data)
              310522397  903.576    0.000 1204.556    0.000 layers.py:77(check)
                2930698   37.802    0.000 1126.172    0.000 layers.py:740(restart)
             3386340122  912.006    0.000 1104.830    0.000 layers.py:700(<genexpr>)
              310522397  697.603    0.000 1089.940    0.000 layers.py:286(check)
               10891628 1088.089    0.000 1088.089    0.000 {built-in method torch._C._nn.one_hot}
               87018306 1073.641    0.000 1073.641    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              310522397  590.779    0.000  966.794    0.000 layers.py:246(check)
             1009817811  962.861    0.000  962.861    0.000 layer.py:146(elements)
               87018306  930.211    0.000  930.211    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               87018306  897.956    0.000  897.956    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               87018306  885.643    0.000  885.643    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                3107797   64.986    0.000  846.555    0.000 replaybuffer.py:18(stacker)
                3107796   64.601    0.000  819.092    0.000 replaybuffer.py:63(stacker)
                2930698   17.193    0.000  793.614    0.000 level.py:8(__init__)
                3107797  426.782    0.000  704.001    0.000 collector.py:46(collect)
             7458453886  702.185    0.000  702.185    0.000 layer.py:91(positions)
               87018306  689.296    0.000  689.296    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              310522397  502.486    0.000  658.229    0.000 layers.py:62(check)
        8223532446/8223532443  579.340    0.000  645.492    0.000 {built-in method builtins.len}
                2930698  103.597    0.000  640.851    0.000 levels.py:199(generate)
                7783831  232.114    0.000  633.175    0.000 exploration.py:53(softmaxer)
              609128226  462.900    0.000  569.482    0.000 tensor.py:906(grad)
              310522397  326.862    0.000  514.394    0.000 layers.py:313(check)
               12076990  191.854    0.000  508.541    0.000 random.py:315(sample)
                9323390   16.349    0.000  501.953    0.000 loss.py:527(forward)
              310522397  310.262    0.000  494.512    0.000 layers.py:273(check)
                9323390   38.392    0.000  485.604    0.000 functional.py:2898(mse_loss)
              133918503  464.251    0.000  464.251    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
             5800979693  456.126    0.000  456.126    0.000 {built-in method builtins.hash}
              310522397  301.956    0.000  447.929    0.000 layers.py:48(check)
                1580037  414.670    0.000  440.352    0.000 agent.py:186(convert_values)
                5861396   51.818    0.000  436.421    0.000 level.py:41(notUsed)
              310779800   71.136    0.000  424.796    0.000 {built-in method builtins.all}
              738230554  181.612    0.000  394.604    0.000 layers.py:690(<genexpr>)
              310522397  236.793    0.000  345.244    0.000 layers.py:23(check)
                9323390  320.294    0.000  320.294    0.000 {built-in method torch._C._nn.mse_loss}
               49805702   38.557    0.000  318.965    0.000 flatten.py:39(forward)
               18646782  294.956    0.000  294.956    0.000 {built-in method sum}
             3427903561  294.325    0.000  294.325    0.000 {method 'random' of '_random.Random' objects}
                6215596  286.486    0.000  286.486    0.000 {built-in method nonzero}
               29306980   43.834    0.000  284.376    0.000 layer.py:69(restart)
              268085100  203.292    0.000  281.343    0.000 layer.py:126(remove)
               49805702  280.409    0.000  280.409    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9533963: <Causal4_Cf_convert3_TopN6_2> in cluster <dcc> Done

Job <Causal4_Cf_convert3_TopN6_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun Apr 18 20:20:08 2021
Job was executed on host(s) <n-62-20-13>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon Apr 19 21:45:29 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Apr 19 21:45:29 2021
Terminated at Tue Apr 20 21:40:45 2021
Results reported at Tue Apr 20 21:40:45 2021

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

    CPU time :                                   85903.49 sec.
    Max Memory :                                 9118 MB
    Average Memory :                             6159.61 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               7266.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86116 sec.
    Turnaround time :                            177637 sec.

The output (if any) is above this job summary.

