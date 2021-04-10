
# Parameters

    Name :                      TEST_CF_CAUSAL4_6c2-0
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
    Cf convert :                6
    Counterfacts :              2
    Topn :                      7
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      61428720722 function calls (61127411899 primitive calls) in 82510.28 seconds

##    Ordered by: cumulative time
   List reduced from 512 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 82510.282 82510.282 {built-in method builtins.exec}
                      1    5.361    5.361 82510.282 82510.282 <string>:1(<module>)
                      1  271.875  271.875 82504.921 82504.921 main.py:95(CFagent)
                8823945   45.448    0.000 23257.358    0.003 agent.py:29(learn)
                8823944  604.553    0.000 18680.327    0.002 learner.py:42(Qlearn)
                2941315   17.674    0.000 18044.752    0.006 game.py:41(step)
                2941315 1460.254    0.000 17704.581    0.006 agent.py:217(counterfact)
                2941315   20.309    0.000 17290.598    0.006 layers.py:710(step)
        336220442/34913310 1453.963    0.000 11652.679    0.000 module.py:866(_call_impl)
                2941315  289.438    0.000 11172.266    0.004 layers.py:17(step)
               26089366   76.744    0.000 10870.710    0.000 network.py:24(forward)
              292900517  876.290    0.000 10851.372    0.000 layer.py:98(move)
               26089366  366.168    0.000 10600.866    0.000 container.py:117(forward)
                2941315  384.019    0.000 9097.852    0.003 agent.py:54(_learn)
               79517511 8650.297    0.000 8650.297    0.000 {built-in method tensor}
               72709196   41.248    0.000 8483.780    0.000 game.py:37(board)
                2941315  376.676    0.000 8204.785    0.003 agent.py:209(_learn)
                8823944   93.200    0.000 7144.610    0.001 optimizer.py:84(wrapper)
                8823944   51.656    0.000 6748.397    0.001 grad_mode.py:24(decorate_context)
                8823944  313.474    0.000 6590.017    0.001 adam.py:55(step)
              292900517  934.057    0.000 6158.387    0.000 layers.py:727(check)
               88239460 3511.890    0.000 6131.943    0.000 layer.py:151(update)
                8628987  287.995    0.000 6066.954    0.001 agent.py:49(__call__)
                2941316  450.630    0.000 6066.557    0.002 layers.py:676(update)
                8823944 1375.030    0.000 5950.189    0.001 _functional.py:53(adam)
                2941315   99.991    0.000 5884.955    0.002 agent.py:117(_learn)
                2941315 4663.508    0.002 5819.830    0.002 replaybuffer.py:22(sample_data)
                2941315 3994.877    0.001 4982.944    0.002 replaybuffer.py:49(sample_data)
                8823944   42.359    0.000 4960.635    0.001 tensor.py:195(backward)
                8823944   48.949    0.000 4916.920    0.001 __init__.py:68(backward)
                8823944 4668.326    0.001 4668.326    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               52178732  126.356    0.000 3978.440    0.000 conv.py:398(forward)
                2753806   61.649    0.000 3922.067    0.001 agent.py:172(choose_action)
               52178732   92.691    0.000 3790.647    0.000 conv.py:390(_conv_forward)
               52178732 3697.955    0.000 3697.955    0.000 {built-in method conv2d}
                2941315 2164.358    0.001 3692.026    0.001 replaybuffer.py:28(teleporter_save_data)
                2941315 1600.419    0.001 3629.806    0.001 agent.py:88(interveen)
              292573532  555.341    0.000 3231.555    0.000 layers.py:721(isFree)
               72385468  153.132    0.000 2971.029    0.000 linear.py:93(forward)
               72385468   62.801    0.000 2735.775    0.000 functional.py:1737(linear)
             2592747716 2259.706    0.000 2676.215    0.000 layer.py:95(isFree)
               72385468 2657.074    0.000 2657.074    0.000 {built-in method torch._C._nn.linear}
                2941315 1523.392    0.001 2342.571    0.001 agent.py:67(modify)
               43924762 1788.929    0.000 1788.929    0.000 {built-in method cat}
               11570302   93.154    0.000 1649.606    0.000 agent.py:59(modify_board)
               98474834   87.072    0.000 1551.171    0.000 activation.py:713(forward)
              987244900 1539.684    0.000 1539.684    0.000 layer.py:146(elements)
              142549992 1469.696    0.000 1469.696    0.000 {built-in method clone}
               98474834   89.634    0.000 1464.098    0.000 functional.py:1364(leaky_relu)
                2941314   65.364    0.000 1439.589    0.000 agent.py:168(__call__)
             5469750434  985.987    0.000 1401.801    0.000 enum.py:646(__hash__)
              297391001  311.733    0.000 1372.162    0.000 {built-in method builtins.any}
               98474834 1357.973    0.000 1357.973    0.000 {built-in method torch._C._nn.leaky_relu}
                2941315   63.135    0.000 1322.357    0.000 agent.py:112(__call__)
              164713620 1160.850    0.000 1160.850    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              292900517  888.568    0.000 1158.062    0.000 layers.py:71(check)
               11570302 1083.272    0.000 1083.272    0.000 {built-in method torch._C._nn.one_hot}
              292900517  710.141    0.000 1077.856    0.000 layers.py:280(check)
             3206592070  883.291    0.000 1060.430    0.000 layers.py:692(<genexpr>)
              164713620 1022.062    0.000 1022.062    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                8823944  187.483    0.000 1021.024    0.000 optimizer.py:189(zero_grad)
                2623230   35.744    0.000 1012.115    0.000 layers.py:731(restart)
                2941315   78.350    0.000  905.265    0.000 replaybuffer.py:18(stacker)
              294131600  153.895    0.000  882.571    0.000 {built-in method builtins.all}
              292900517  535.926    0.000  879.418    0.000 layers.py:240(check)
                2753806  655.957    0.000  772.543    0.000 agent.py:183(convert_values)
             1707007764  445.339    0.000  764.454    0.000 layers.py:682(<genexpr>)
                2941314   73.196    0.000  750.048    0.000 replaybuffer.py:45(stacker)
                2623230   17.312    0.000  716.249    0.000 level.py:8(__init__)
        10274636980/10274636977  634.603    0.000  709.434    0.000 {built-in method builtins.len}
              292900517  537.303    0.000  672.313    0.000 layers.py:56(check)
               82356810  670.782    0.000  670.782    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                2941315  256.910    0.000  630.264    0.000 replaybuffer.py:55(CF_save_data)
                8628987  221.869    0.000  628.880    0.000 exploration.py:53(softmaxer)
             6551073373  611.359    0.000  611.359    0.000 layer.py:91(positions)
               82356810  603.441    0.000  603.441    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                2623230   91.980    0.000  566.892    0.000 levels.py:199(generate)
               82356810  552.623    0.000  552.623    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               82356810  542.517    0.000  542.517    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               11129090  203.244    0.000  525.039    0.000 random.py:315(sample)
              576497754  398.570    0.000  491.342    0.000 tensor.py:906(grad)
              292900517  299.153    0.000  478.443    0.000 layers.py:267(check)
              292900517  299.930    0.000  471.689    0.000 layers.py:307(check)
                2941315  271.215    0.000  465.944    0.000 collector.py:53(collect)
                8823944   18.817    0.000  459.160    0.000 loss.py:527(forward)
                8823944   49.039    0.000  440.342    0.000 functional.py:2898(mse_loss)
             5469784065  415.820    0.000  415.820    0.000 {built-in method builtins.hash}
              292900517  282.242    0.000  407.353    0.000 layers.py:42(check)
                8823946  401.328    0.000  401.328    0.000 {built-in method nonzero}
               82356810  398.983    0.000  398.983    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                5246460   45.440    0.000  383.254    0.000 level.py:41(notUsed)
               88239460  364.260    0.000  364.260    0.000 layer.py:163(<listcomp>)
              157061608  334.527    0.000  334.527    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              250008385  221.699    0.000  303.175    0.000 layer.py:126(remove)
               88239460  271.132    0.000  271.132    0.000 layer.py:164(<listcomp>)
                8823944  255.901    0.000  255.901    0.000 {built-in method torch._C._nn.mse_loss}
               52178732   42.055    0.000  253.947    0.000 flatten.py:39(forward)
               26232300   37.779    0.000  251.263    0.000 layer.py:69(restart)
              348588638  166.220    0.000  248.838    0.000 random.py:250(_randbelow_with_getrandbits)
              405828942  174.554    0.000  248.525    0.000 layer.py:130(add)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-10>
Subject: Job 9505792: <TEST_CF_CAUSAL4_6c2_0> in cluster <dcc> Done

Job <TEST_CF_CAUSAL4_6c2_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Fri Apr  9 00:44:40 2021
Job was executed on host(s) <n-62-20-10>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Fri Apr  9 01:55:25 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Fri Apr  9 01:55:25 2021
Terminated at Sat Apr 10 00:50:42 2021
Results reported at Sat Apr 10 00:50:42 2021

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

    CPU time :                                   82304.02 sec.
    Max Memory :                                 8748 MB
    Average Memory :                             5999.86 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               7636.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   82518 sec.
    Turnaround time :                            86762 sec.

The output (if any) is above this job summary.

