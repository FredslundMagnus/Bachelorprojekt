
# Parameters

    Name :                      Causal4_Cf_convert1_TopN6-0
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


      81421226020 function calls (81064666761 primitive calls) in 86116.67 seconds

##    Ordered by: cumulative time
   List reduced from 513 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86116.671 86116.671 {built-in method builtins.exec}
                      1    3.933    3.933 86116.671 86116.671 <string>:1(<module>)
                      1  353.874  353.874 86112.738 86112.738 main.py:79(CFagent)
               11463573   42.844    0.000 26158.595    0.002 agent.py:29(learn)
                3821191   15.771    0.000 22709.290    0.006 game.py:41(step)
                3821191   20.645    0.000 21857.338    0.006 layers.py:718(step)
               11463572  671.694    0.000 21396.301    0.002 learner.py:42(Qlearn)
                3821191  329.054    0.000 14509.911    0.004 layers.py:17(step)
              382098586 1022.993    0.000 14148.523    0.000 layer.py:98(move)
        399008001/42450433 1491.658    0.000 12009.164    0.000 module.py:866(_call_impl)
               30986861   81.410    0.000 11214.926    0.000 network.py:27(forward)
               30986861  364.818    0.000 10946.504    0.000 container.py:117(forward)
                3821191  922.548    0.000 10841.495    0.003 agent.py:210(counterfact)
                3821191  348.079    0.000 10136.018    0.003 agent.py:54(_learn)
                3821191  345.647    0.000 9322.474    0.002 agent.py:202(_learn)
              382098586 1699.224    0.000 8760.866    0.000 layers.py:735(check)
               11463572   91.011    0.000 8384.431    0.001 optimizer.py:84(wrapper)
               11463572   47.288    0.000 7964.590    0.001 grad_mode.py:24(decorate_context)
               11463572  326.044    0.000 7818.675    0.001 adam.py:55(step)
                3821192  522.798    0.000 7295.871    0.002 layers.py:684(update)
               11463572 1608.029    0.000 7120.854    0.001 _functional.py:53(adam)
                3821191   99.741    0.000 6634.180    0.002 agent.py:117(_learn)
                3821191 5332.185    0.001 6393.494    0.002 replaybuffer.py:22(sample_data)
                3821191 5125.403    0.001 6165.746    0.002 replaybuffer.py:67(sample_data)
               60742753 6093.719    0.000 6093.719    0.000 {built-in method tensor}
               51995258   31.645    0.000 5895.408    0.000 game.py:37(board)
                9751369  207.418    0.000 5789.875    0.001 agent.py:49(__call__)
               11463572   52.049    0.000 5607.064    0.000 tensor.py:195(backward)
               11463572   41.777    0.000 5553.369    0.000 __init__.py:68(backward)
               11463572 5300.816    0.000 5300.816    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
               76423830 2640.852    0.000 4598.530    0.000 layer.py:151(update)
               61973722  129.207    0.000 4052.389    0.000 conv.py:398(forward)
               61973722   81.774    0.000 3860.489    0.000 conv.py:390(_conv_forward)
                3821191 1599.776    0.000 3838.097    0.001 agent.py:88(interveen)
               61973722 3778.715    0.000 3778.715    0.000 {built-in method conv2d}
              382098586  678.143    0.000 3648.786    0.000 layers.py:729(isFree)
               85318201  162.369    0.000 3094.703    0.000 linear.py:93(forward)
                3821191 1740.960    0.000 3085.852    0.001 replaybuffer.py:28(teleporter_save_data)
             3406612726 2423.398    0.000 2970.643    0.000 layer.py:95(isFree)
               85318201   69.273    0.000 2847.858    0.000 functional.py:1737(linear)
               85318201 2762.886    0.000 2762.886    0.000 {built-in method torch._C._nn.linear}
                3821191 1722.924    0.000 2616.334    0.001 agent.py:67(modify)
                2129539   41.440    0.000 2552.641    0.001 agent.py:175(choose_action)
             7198101436 1261.062    0.000 1818.733    0.000 enum.py:646(__hash__)
               51784465 1731.169    0.000 1731.169    0.000 {built-in method cat}
               13572560   77.302    0.000 1654.816    0.000 agent.py:59(modify_board)
              381928965  367.974    0.000 1643.628    0.000 {built-in method builtins.any}
              116305062   94.233    0.000 1625.023    0.000 activation.py:713(forward)
                3821190   55.400    0.000 1580.004    0.000 agent.py:171(__call__)
              116305062   92.643    0.000 1530.790    0.000 functional.py:1364(leaky_relu)
                3821191   52.774    0.000 1493.435    0.000 agent.py:112(__call__)
              116305062 1419.440    0.000 1419.440    0.000 {built-in method torch._C._nn.leaky_relu}
                4011427   45.855    0.000 1407.769    0.000 layers.py:740(restart)
              382098586 1043.430    0.000 1386.678    0.000 layers.py:77(check)
              147704407 1385.748    0.000 1385.748    0.000 {built-in method clone}
              213986676 1376.588    0.000 1376.588    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              382098586  823.316    0.000 1288.150    0.000 layers.py:246(check)
                3821191 1003.052    0.000 1277.112    0.000 replaybuffer.py:73(CF_save_data)
             4159185503 1055.610    0.000 1275.654    0.000 layers.py:700(<genexpr>)
               11463572  221.511    0.000 1249.848    0.000 optimizer.py:189(zero_grad)
              213986676 1238.432    0.000 1238.432    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              382098586  687.018    0.000 1145.251    0.000 layers.py:286(check)
             1320506261 1106.525    0.000 1106.525    0.000 layer.py:146(elements)
               13572560 1094.611    0.000 1094.611    0.000 {built-in method torch._C._nn.one_hot}
              382119200  196.240    0.000 1076.640    0.000 {built-in method builtins.all}
                4011427   22.774    0.000  999.047    0.000 level.py:8(__init__)
             2387876589  591.742    0.000  922.478    0.000 layers.py:690(<genexpr>)
              106993338  869.908    0.000  869.908    0.000 {method 'add' of 'torch._C._TensorBase' objects}
             9268528982  834.325    0.000  834.325    0.000 layer.py:91(positions)
                3821191   68.937    0.000  797.777    0.000 replaybuffer.py:18(stacker)
                4011427  128.216    0.000  791.359    0.000 levels.py:199(generate)
                3821190   66.656    0.000  780.164    0.000 replaybuffer.py:63(stacker)
              382098586  590.479    0.000  769.564    0.000 layers.py:62(check)
              106993338  691.814    0.000  691.814    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
        10091888767/10091888764  615.325    0.000  683.041    0.000 {built-in method builtins.len}
              106993338  660.880    0.000  660.880    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              106993338  647.803    0.000  647.803    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              382098586  383.262    0.000  615.099    0.000 layers.py:313(check)
              748953450  478.925    0.000  591.495    0.000 tensor.py:906(grad)
                9751369  219.676    0.000  585.410    0.000 exploration.py:53(softmaxer)
              382098586  363.646    0.000  585.057    0.000 layers.py:273(check)
               15665236  218.239    0.000  570.560    0.000 random.py:315(sample)
             7198144923  557.678    0.000  557.678    0.000 {built-in method builtins.hash}
                3821191  326.491    0.000  554.343    0.000 collector.py:46(collect)
                8022854   64.540    0.000  538.306    0.000 level.py:41(notUsed)
              382098586  347.272    0.000  516.607    0.000 layers.py:48(check)
              106993338  493.933    0.000  493.933    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               11463572   16.314    0.000  463.510    0.000 loss.py:527(forward)
               11463572   42.475    0.000  447.196    0.000 functional.py:2898(mse_loss)
              382098586  267.429    0.000  392.721    0.000 layers.py:23(check)
                2129539  374.284    0.000  374.284    0.000 agent.py:186(convert_values)
               40114270   51.635    0.000  349.920    0.000 layer.py:69(restart)
             4218960432  328.515    0.000  328.515    0.000 {method 'random' of '_random.Random' objects}
             2774295352  319.001    0.000  319.001    0.000 layer.py:203(isBlocking)
              585051442  229.837    0.000  313.450    0.000 layer.py:130(add)
              348068155  220.561    0.000  310.668    0.000 layer.py:126(remove)
              165098157  310.304    0.000  310.304    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              462197572  192.712    0.000  281.884    0.000 random.py:250(_randbelow_with_getrandbits)
               76423830  279.249    0.000  279.249    0.000 layer.py:163(<listcomp>)
                7642384  273.582    0.000  273.582    0.000 {built-in method nonzero}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9533955: <Causal4_Cf_convert1_TopN6_0> in cluster <dcc> Done

Job <Causal4_Cf_convert1_TopN6_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun Apr 18 20:20:06 2021
Job was executed on host(s) <n-62-20-7>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Apr 18 20:20:08 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun Apr 18 20:20:08 2021
Terminated at Mon Apr 19 20:15:38 2021
Results reported at Mon Apr 19 20:15:38 2021

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

    CPU time :                                   86101.39 sec.
    Max Memory :                                 3451 MB
    Average Memory :                             3415.44 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               12933.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86174 sec.
    Turnaround time :                            86132 sec.

The output (if any) is above this job summary.

