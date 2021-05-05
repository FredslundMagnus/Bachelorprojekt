
# Parameters

    Name :                      Causal4_Conver4-0
    Main :                      CFagent
    Level :                     Levels.Causal4
    Failed actions chance :     0
    Use model :                 True
    Depth :                     3
    Model explore :             1000000
    Samples :                   5
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
    Cf convert :                4
    Counterfacts :              1
    Topn :                      3
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      68792368505 function calls (68486229658 primitive calls) in 86123.86 seconds

##    Ordered by: cumulative time
   List reduced from 515 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86123.863 86123.863 {built-in method builtins.exec}
                      1    4.366    4.366 86123.863 86123.863 <string>:1(<module>)
                      1  356.788  356.788 86119.497 86119.497 main.py:80(CFagent)
               10002099   34.624    0.000 30106.218    0.003 agent.py:29(learn)
               10002095  755.195    0.000 25100.461    0.003 learner.py:42(Qlearn)
                3334033   16.376    0.000 19166.245    0.006 game.py:42(step)
                3334033   19.446    0.000 18333.656    0.005 layers.py:827(step)
        342762025/36624869 1389.737    0.000 12759.086    0.000 module.py:866(_call_impl)
                3334033  271.211    0.000 12309.093    0.004 layers.py:17(step)
              332913397  874.501    0.000 12008.984    0.000 layer.py:106(move)
               26622774   73.149    0.000 11959.986    0.000 network.py:28(forward)
               26622774  376.146    0.000 11706.265    0.000 container.py:117(forward)
                3334033  343.236    0.000 11618.219    0.003 agent.py:54(_learn)
                3334033  340.447    0.000 10764.192    0.003 agent.py:204(_learn)
               10002095   85.056    0.000 10590.162    0.001 optimizer.py:84(wrapper)
                3334033  920.463    0.000 10222.584    0.003 agent.py:212(counterfact)
               10002095   42.064    0.000 10178.075    0.001 grad_mode.py:24(decorate_context)
               10002095  291.248    0.000 10043.222    0.001 adam.py:55(step)
               10002095 2061.248    0.000 9417.878    0.001 _functional.py:53(adam)
                3334033  101.116    0.000 7668.167    0.002 agent.py:117(_learn)
              332913397 1462.546    0.000 7472.248    0.000 layers.py:844(check)
               10002095   41.235    0.000 6276.257    0.001 tensor.py:195(backward)
               10002095   38.429    0.000 6233.680    0.001 __init__.py:68(backward)
                8301927  223.591    0.000 6046.826    0.001 agent.py:49(__call__)
                3334034  474.816    0.000 5978.634    0.002 layers.py:793(update)
               10002095 5973.548    0.001 5973.548    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3334033 4676.446    0.001 5766.284    0.002 replaybuffer.py:22(sample_data)
               52436416 5601.902    0.000 5601.902    0.000 {built-in method tensor}
                3334033 4476.164    0.001 5525.223    0.002 replaybuffer.py:67(sample_data)
               44762005   32.233    0.000 5380.697    0.000 game.py:38(board)
                3334033 1860.159    0.001 4269.795    0.001 agent.py:88(interveen)
               53245548  116.176    0.000 4235.456    0.000 conv.py:398(forward)
               53245548   68.071    0.000 4066.575    0.000 conv.py:390(_conv_forward)
               66680670 2337.769    0.000 4008.866    0.000 layer.py:159(update)
               53245548 3998.504    0.000 3998.504    0.000 {built-in method conv2d}
                3334033 1935.046    0.001 3609.885    0.001 replaybuffer.py:28(teleporter_save_data)
               73200256  146.592    0.000 3409.128    0.000 linear.py:93(forward)
               73200256   59.385    0.000 3191.782    0.000 functional.py:1737(linear)
               73200256 3117.985    0.000 3117.985    0.000 {built-in method torch._C._nn.linear}
              332913397  597.672    0.000 3068.976    0.000 layers.py:838(isFree)
                3334033 1891.488    0.001 2868.595    0.001 agent.py:67(modify)
                1650690   37.609    0.000 2591.517    0.002 agent.py:176(choose_action)
             2901656571 2003.431    0.000 2471.304    0.000 layer.py:103(isFree)
              186705768 1934.993    0.000 1934.993    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               99823030   75.853    0.000 1874.797    0.000 activation.py:713(forward)
               44976270 1861.034    0.000 1861.034    0.000 {built-in method cat}
               99823030   83.252    0.000 1798.944    0.000 functional.py:1364(leaky_relu)
               11635960   80.307    0.000 1701.567    0.000 agent.py:59(modify_board)
              186705768 1699.337    0.000 1699.337    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               99823030 1698.957    0.000 1698.957    0.000 {built-in method torch._C._nn.leaky_relu}
                3334029   59.212    0.000 1689.407    0.001 agent.py:172(__call__)
              124381236 1636.767    0.000 1636.767    0.000 {built-in method clone}
             6575154276 1108.233    0.000 1595.204    0.000 enum.py:646(__hash__)
                3334033   55.514    0.000 1581.749    0.000 agent.py:112(__call__)
               10002095  231.048    0.000 1467.928    0.000 optimizer.py:189(zero_grad)
              333634514  318.980    0.000 1401.016    0.000 {built-in method builtins.any}
                3334033 1046.913    0.000 1345.602    0.000 replaybuffer.py:73(CF_save_data)
              332913397  883.800    0.000 1188.435    0.000 layers.py:77(check)
                3102920   35.281    0.000 1124.051    0.000 layers.py:849(restart)
               11635960 1085.397    0.000 1085.397    0.000 {built-in method torch._C._nn.one_hot}
             3633305280  886.876    0.000 1082.035    0.000 layers.py:809(<genexpr>)
              332913397  695.346    0.000 1073.780    0.000 layers.py:246(check)
               93352884 1052.314    0.000 1052.314    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              332913397  611.303    0.000  996.490    0.000 layers.py:286(check)
             1071818244  925.152    0.000  925.152    0.000 layer.py:154(elements)
               93352884  917.859    0.000  917.859    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               93352884  872.308    0.000  872.308    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                3334033   64.163    0.000  854.448    0.000 replaybuffer.py:18(stacker)
               93352884  852.329    0.000  852.329    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                3334029   63.014    0.000  823.083    0.000 replaybuffer.py:63(stacker)
                3102920   16.606    0.000  808.504    0.000 level.py:8(__init__)
             8550354219  786.548    0.000  786.548    0.000 layer.py:99(positions)
              333403400   59.961    0.000  728.213    0.000 {built-in method builtins.all}
              692866835  146.252    0.000  707.384    0.000 layers.py:799(<genexpr>)
                3334033  419.204    0.000  694.621    0.000 collector.py:46(collect)
               93352884  679.601    0.000  679.601    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              332913397  502.544    0.000  645.511    0.000 layers.py:62(check)
                3102920   98.912    0.000  642.887    0.000 levels.py:199(generate)
                8301927  226.489    0.000  623.281    0.000 exploration.py:53(softmaxer)
        8839951155/8839951152  556.912    0.000  620.911    0.000 {built-in method builtins.len}
              333403400  372.609    0.000  554.918    0.000 layers.py:113(isDone)
              653470272  443.978    0.000  547.244    0.000 tensor.py:906(grad)
                1650690  441.942    0.000  524.668    0.000 agent.py:187(convert_values)
              332913397  328.076    0.000  516.622    0.000 layers.py:273(check)
              332913397  325.601    0.000  514.600    0.000 layers.py:313(check)
               10002095   15.421    0.000  500.056    0.000 loss.py:527(forward)
               12873906  187.643    0.000  496.291    0.000 random.py:315(sample)
             6575192275  486.978    0.000  486.978    0.000 {built-in method builtins.hash}
               10002095   40.096    0.000  484.635    0.000 functional.py:2898(mse_loss)
                6205840   51.144    0.000  448.802    0.000 level.py:41(notUsed)
              139351225  442.824    0.000  442.824    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              332913397  291.283    0.000  427.788    0.000 layers.py:48(check)
              332913397  232.229    0.000  343.461    0.000 layers.py:23(check)
               10002095  317.810    0.000  317.810    0.000 {built-in method torch._C._nn.mse_loss}
               53245548   37.625    0.000  315.271    0.000 flatten.py:39(forward)
               20004198  295.174    0.000  295.174    0.000 {built-in method sum}
                6668068  286.389    0.000  286.389    0.000 {built-in method nonzero}
               10003258  278.464    0.000  278.464    0.000 {built-in method max}
               53245548  277.646    0.000  277.646    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
             3675180063  277.141    0.000  277.141    0.000 {method 'random' of '_random.Random' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9606153: <Causal4_Conver4_0> in cluster <dcc> Done

Job <Causal4_Conver4_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon May  3 01:44:21 2021
Job was executed on host(s) <n-62-20-3>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Tue May  4 04:59:49 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue May  4 04:59:49 2021
Terminated at Wed May  5 04:55:23 2021
Results reported at Wed May  5 04:55:23 2021

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

    CPU time :                                   85901.04 sec.
    Max Memory :                                 9454 MB
    Average Memory :                             6283.29 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               6930.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86136 sec.
    Turnaround time :                            184262 sec.

The output (if any) is above this job summary.

