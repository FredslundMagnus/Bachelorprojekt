
# Parameters

    Name :                      Causal4_Conver2-2
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
    Cf convert :                2
    Counterfacts :              1
    Topn :                      3
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      78425533622 function calls (78084119787 primitive calls) in 86113.51 seconds

##    Ordered by: cumulative time
   List reduced from 514 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86113.506 86113.506 {built-in method builtins.exec}
                      1    3.924    3.924 86113.506 86113.506 <string>:1(<module>)
                      1  342.943  342.943 86109.582 86109.582 main.py:79(CFagent)
               10808865   43.651    0.000 24810.007    0.002 agent.py:29(learn)
                3602955   14.954    0.000 21934.138    0.006 game.py:41(step)
                3602955   19.587    0.000 21124.905    0.006 layers.py:718(step)
               10808855  619.085    0.000 20267.106    0.002 learner.py:42(Qlearn)
                3602955  302.853    0.000 13709.531    0.004 layers.py:17(step)
              360278461  980.804    0.000 13378.117    0.000 layer.py:98(move)
        381872996/40460852 1463.156    0.000 11622.523    0.000 module.py:866(_call_impl)
                3602955  956.362    0.000 10927.002    0.003 agent.py:212(counterfact)
               29651997   77.784    0.000 10859.593    0.000 network.py:27(forward)
               29651997  350.512    0.000 10599.136    0.000 container.py:117(forward)
                3602955  332.222    0.000 9623.510    0.003 agent.py:54(_learn)
                3602955  330.842    0.000 8838.255    0.002 agent.py:204(_learn)
              360278461 1587.956    0.000 8301.744    0.000 layers.py:735(check)
               10808855   83.580    0.000 7928.044    0.001 optimizer.py:84(wrapper)
               10808855   45.477    0.000 7539.544    0.001 grad_mode.py:24(decorate_context)
               10808855  309.552    0.000 7395.286    0.001 adam.py:55(step)
                3602956  500.589    0.000 7366.722    0.002 layers.py:684(update)
               10808855 1518.034    0.000 6741.569    0.001 _functional.py:53(adam)
                3602955   95.759    0.000 6282.687    0.002 agent.py:117(_learn)
                3602955 5028.760    0.001 6036.234    0.002 replaybuffer.py:22(sample_data)
               57868576 5885.325    0.000 5885.325    0.000 {built-in method tensor}
                3602955 4826.863    0.001 5813.552    0.002 replaybuffer.py:67(sample_data)
               49600828   28.987    0.000 5694.855    0.000 game.py:37(board)
                9419779  202.753    0.000 5650.500    0.001 agent.py:49(__call__)
               10808855   49.644    0.000 5321.230    0.000 tensor.py:195(backward)
               10808855   43.339    0.000 5270.030    0.000 __init__.py:68(backward)
                3602955 2938.873    0.001 5213.974    0.001 replaybuffer.py:28(teleporter_save_data)
               10808855 5023.979    0.000 5023.979    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3602955 2559.821    0.001 4705.567    0.001 agent.py:88(interveen)
               72059110 2579.898    0.000 4440.270    0.000 layer.py:151(update)
               59303994  125.816    0.000 3915.712    0.000 conv.py:398(forward)
               59303994   77.894    0.000 3728.263    0.000 conv.py:390(_conv_forward)
               59303994 3650.369    0.000 3650.369    0.000 {built-in method conv2d}
              360278461  678.081    0.000 3423.085    0.000 layers.py:729(isFree)
               81750081  157.438    0.000 3006.546    0.000 linear.py:93(forward)
                2217463   41.600    0.000 2810.034    0.001 agent.py:176(choose_action)
               81750081   64.350    0.000 2764.577    0.000 functional.py:1737(linear)
             3182168143 2273.414    0.000 2745.004    0.000 layer.py:95(isFree)
               81750081 2684.752    0.000 2684.752    0.000 {built-in method torch._C._nn.linear}
                3602955 1654.686    0.000 2501.211    0.001 agent.py:67(modify)
              231535275 2161.441    0.000 2161.441    0.000 {built-in method clone}
             6945392635 1191.942    0.000 1709.207    0.000 enum.py:646(__hash__)
               49052234 1650.239    0.000 1650.239    0.000 {built-in method cat}
              359750650  351.982    0.000 1606.629    0.000 {built-in method builtins.any}
               13022734   82.316    0.000 1603.167    0.000 agent.py:59(modify_board)
              111402078   85.485    0.000 1565.616    0.000 activation.py:713(forward)
                3602945   52.840    0.000 1507.198    0.000 agent.py:172(__call__)
              111402078   86.848    0.000 1480.131    0.000 functional.py:1364(leaky_relu)
                4147906   47.351    0.000 1471.598    0.000 layers.py:740(restart)
                3602955   50.926    0.000 1422.221    0.000 agent.py:112(__call__)
              111402078 1374.845    0.000 1374.845    0.000 {built-in method torch._C._nn.leaky_relu}
              360278461  985.100    0.000 1307.956    0.000 layers.py:77(check)
              201765280 1299.190    0.000 1299.190    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                3602955 1003.726    0.000 1291.550    0.000 replaybuffer.py:73(CF_save_data)
             3917624634 1045.623    0.000 1254.647    0.000 layers.py:700(<genexpr>)
              360295600  193.339    0.000 1230.278    0.000 {built-in method builtins.all}
              360278461  752.329    0.000 1207.711    0.000 layers.py:286(check)
               10808855  209.180    0.000 1178.775    0.000 optimizer.py:189(zero_grad)
              201765280 1170.463    0.000 1170.463    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              360278461  675.676    0.000 1128.058    0.000 layers.py:246(check)
             2307196946  604.118    0.000 1077.555    0.000 layers.py:690(<genexpr>)
               13022734 1053.148    0.000 1053.148    0.000 {built-in method torch._C._nn.one_hot}
             1344392085 1050.539    0.000 1050.539    0.000 layer.py:146(elements)
                4147906   23.001    0.000 1042.008    0.000 level.py:8(__init__)
                4147906  133.788    0.000  824.278    0.000 levels.py:199(generate)
              100882640  823.096    0.000  823.096    0.000 {method 'add' of 'torch._C._TensorBase' objects}
             9059315739  787.750    0.000  787.750    0.000 layer.py:91(positions)
                3602955   63.853    0.000  757.492    0.000 replaybuffer.py:18(stacker)
                3602945   63.993    0.000  741.405    0.000 replaybuffer.py:63(stacker)
              360278461  530.006    0.000  705.659    0.000 layers.py:62(check)
        9572723994/9572723991  591.829    0.000  661.479    0.000 {built-in method builtins.len}
              100882640  657.190    0.000  657.190    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              100882640  634.272    0.000  634.272    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              360278461  399.607    0.000  614.467    0.000 layers.py:273(check)
              100882640  613.138    0.000  613.138    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              360278461  378.675    0.000  586.079    0.000 layers.py:313(check)
                9419779  207.272    0.000  565.581    0.000 exploration.py:53(softmaxer)
                8295812   65.295    0.000  561.519    0.000 level.py:41(notUsed)
               15501722  208.364    0.000  545.621    0.000 random.py:315(sample)
              706178564  436.749    0.000  542.755    0.000 tensor.py:906(grad)
                2217463  465.807    0.000  524.607    0.000 agent.py:187(convert_values)
                3602955  304.547    0.000  519.455    0.000 collector.py:46(collect)
             6945433658  517.272    0.000  517.272    0.000 {built-in method builtins.hash}
              100882640  470.607    0.000  470.607    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              248160954  463.304    0.000  463.304    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              360278461  309.566    0.000  460.611    0.000 layers.py:48(check)
               10808855   15.275    0.000  435.036    0.000 loss.py:527(forward)
               10808855   37.967    0.000  419.762    0.000 functional.py:2898(mse_loss)
               41479060   55.719    0.000  369.314    0.000 layer.py:69(restart)
              360278461  256.533    0.000  368.475    0.000 layers.py:23(check)
              368618145  245.348    0.000  343.844    0.000 layer.py:126(remove)
              601744462  236.977    0.000  323.841    0.000 layer.py:130(add)
             3979126783  303.513    0.000  303.513    0.000 {method 'random' of '_random.Random' objects}
              466624333  203.623    0.000  295.177    0.000 random.py:250(_randbelow_with_getrandbits)
               72059110  266.787    0.000  266.787    0.000 layer.py:163(<listcomp>)
               59303994   41.581    0.000  262.866    0.000 flatten.py:39(forward)
               10808855  259.273    0.000  259.273    0.000 {built-in method torch._C._nn.mse_loss}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9579165: <Causal4_Conver2_2> in cluster <dcc> Done

Job <Causal4_Conver2_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Tue Apr 27 02:44:06 2021
Job was executed on host(s) <n-62-20-7>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed Apr 28 08:52:36 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed Apr 28 08:52:36 2021
Terminated at Thu Apr 29 08:47:54 2021
Results reported at Thu Apr 29 08:47:54 2021

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

    CPU time :                                   86098.11 sec.
    Max Memory :                                 3438 MB
    Average Memory :                             3407.09 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               12946.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86120 sec.
    Turnaround time :                            194628 sec.

The output (if any) is above this job summary.

