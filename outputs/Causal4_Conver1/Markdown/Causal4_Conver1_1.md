
# Parameters

    Name :                      Causal4_Conver1-1
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


      68153635013 function calls (67858557078 primitive calls) in 86115.07 seconds

##    Ordered by: cumulative time
   List reduced from 513 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86115.075 86115.075 {built-in method builtins.exec}
                      1    4.346    4.346 86115.075 86115.075 <string>:1(<module>)
                      1  328.379  328.379 86110.728 86110.728 main.py:79(CFagent)
                9258480   32.613    0.000 27590.923    0.003 agent.py:29(learn)
                9258480  686.822    0.000 22989.214    0.002 learner.py:42(Qlearn)
                3086160   14.691    0.000 18692.303    0.006 game.py:41(step)
                3086160   17.643    0.000 17923.036    0.006 layers.py:718(step)
        329953131/34876887 1334.387    0.000 12143.088    0.000 module.py:866(_call_impl)
                3086160  257.087    0.000 11491.402    0.004 layers.py:17(step)
               25618407   69.895    0.000 11409.209    0.000 network.py:27(forward)
              308572085  790.825    0.000 11209.394    0.000 layer.py:98(move)
               25618407  373.048    0.000 11185.418    0.000 container.py:117(forward)
                3086160 1266.672    0.000 10890.064    0.004 agent.py:212(counterfact)
                3086160  318.134    0.000 10645.881    0.003 agent.py:54(_learn)
                3086160  314.261    0.000 9865.018    0.003 agent.py:204(_learn)
                9258480   82.922    0.000 9745.174    0.001 optimizer.py:84(wrapper)
                9258480   36.934    0.000 9367.553    0.001 grad_mode.py:24(decorate_context)
                9258480  265.639    0.000 9241.950    0.001 adam.py:55(step)
                9258480 1900.256    0.000 8685.101    0.001 _functional.py:53(adam)
                3086160   92.442    0.000 7028.776    0.002 agent.py:117(_learn)
              308572085 1322.511    0.000 6934.831    0.000 layers.py:735(check)
                3086161  421.159    0.000 6389.753    0.002 layers.py:684(update)
                8178587  217.446    0.000 5908.667    0.001 agent.py:49(__call__)
                3086160 3151.948    0.001 5856.779    0.002 replaybuffer.py:28(teleporter_save_data)
                9258480   37.530    0.000 5730.941    0.001 tensor.py:195(backward)
                9258480   36.526    0.000 5692.078    0.001 __init__.py:68(backward)
               50845671 5490.372    0.000 5490.372    0.000 {built-in method tensor}
                9258480 5451.350    0.001 5451.350    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3086160 4381.366    0.001 5384.389    0.002 replaybuffer.py:22(sample_data)
               43719862   27.524    0.000 5285.207    0.000 game.py:37(board)
                3086160 2942.267    0.001 5167.732    0.002 agent.py:88(interveen)
                3086160 4173.694    0.001 5142.050    0.002 replaybuffer.py:67(sample_data)
               51236814  112.983    0.000 4045.868    0.000 conv.py:398(forward)
               61723210 2360.447    0.000 3933.697    0.000 layer.py:151(update)
               51236814   66.471    0.000 3880.666    0.000 conv.py:390(_conv_forward)
               51236814 3814.195    0.000 3814.195    0.000 {built-in method conv2d}
               70682901  144.144    0.000 3232.967    0.000 linear.py:93(forward)
               70682901   56.333    0.000 3019.641    0.000 functional.py:1737(linear)
               70682901 2949.176    0.000 2949.176    0.000 {built-in method torch._C._nn.linear}
                2009020   43.858    0.000 2925.606    0.001 agent.py:176(choose_action)
              308572085  582.677    0.000 2925.183    0.000 layers.py:729(isFree)
                3086160 1829.476    0.001 2724.459    0.001 agent.py:67(modify)
              199285820 2574.957    0.000 2574.957    0.000 {built-in method clone}
             2884981617 1918.098    0.000 2342.506    0.000 layer.py:95(isFree)
               96301308   78.458    0.000 1792.115    0.000 activation.py:713(forward)
              172824960 1784.033    0.000 1784.033    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               42126347 1733.488    0.000 1733.488    0.000 {built-in method cat}
               96301308   75.991    0.000 1713.657    0.000 functional.py:1364(leaky_relu)
                3086160 1269.381    0.000 1692.717    0.001 replaybuffer.py:73(CF_save_data)
               11264747   75.651    0.000 1637.935    0.000 agent.py:59(modify_board)
               96301308 1620.423    0.000 1620.423    0.000 {built-in method torch._C._nn.leaky_relu}
                4676925   52.352    0.000 1569.676    0.000 layers.py:740(restart)
              172824960 1566.167    0.000 1566.167    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                3086160   55.596    0.000 1552.722    0.001 agent.py:172(__call__)
             6119843743 1018.514    0.000 1463.509    0.000 enum.py:646(__hash__)
                3086160   54.446    0.000 1454.644    0.000 agent.py:112(__call__)
                9258480  212.468    0.000 1330.164    0.000 optimizer.py:189(zero_grad)
              307025336  295.281    0.000 1289.443    0.000 {built-in method builtins.any}
                4676925   24.501    0.000 1104.464    0.000 level.py:8(__init__)
              308572085  816.385    0.000 1085.075    0.000 layers.py:77(check)
               11264747 1047.784    0.000 1047.784    0.000 {built-in method torch._C._nn.one_hot}
              308572085  623.916    0.000  996.720    0.000 layers.py:286(check)
             3343330925  817.005    0.000  994.162    0.000 layers.py:700(<genexpr>)
               86412480  974.546    0.000  974.546    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              308572085  571.889    0.000  948.998    0.000 layers.py:246(check)
                4676925  144.643    0.000  897.417    0.000 levels.py:199(generate)
             1287424559  890.851    0.000  890.851    0.000 layer.py:146(elements)
              308616100  143.650    0.000  884.125    0.000 {built-in method builtins.all}
               86412480  837.589    0.000  837.589    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               86412480  802.725    0.000  802.725    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               86412480  794.634    0.000  794.634    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                3086160   61.805    0.000  789.116    0.000 replaybuffer.py:18(stacker)
             1728244996  422.476    0.000  775.509    0.000 layers.py:690(<genexpr>)
                3086160   60.072    0.000  761.480    0.000 replaybuffer.py:63(stacker)
             7774271222  667.540    0.000  667.540    0.000 layer.py:91(positions)
              213636727  639.072    0.000  639.072    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                3086160  380.905    0.000  630.170    0.000 collector.py:46(collect)
               86412480  617.609    0.000  617.609    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                9353850   70.953    0.000  613.288    0.000 level.py:41(notUsed)
                8178587  223.156    0.000  606.215    0.000 exploration.py:53(softmaxer)
              308572085  452.835    0.000  599.785    0.000 layers.py:62(check)
        8170773333/8170773330  522.531    0.000  582.594    0.000 {built-in method builtins.len}
              308572085  334.680    0.000  509.853    0.000 layers.py:313(check)
              308572085  313.056    0.000  483.370    0.000 layers.py:273(check)
              604887444  382.195    0.000  478.081    0.000 tensor.py:906(grad)
               15526170  181.181    0.000  476.032    0.000 random.py:315(sample)
             6119878942  445.001    0.000  445.001    0.000 {built-in method builtins.hash}
                9258480   13.618    0.000  444.872    0.000 loss.py:527(forward)
                9258480   33.159    0.000  431.253    0.000 functional.py:2898(mse_loss)
                2009020  430.938    0.000  430.938    0.000 agent.py:187(convert_values)
              308572085  267.152    0.000  400.401    0.000 layers.py:48(check)
               46769250   57.853    0.000  398.107    0.000 layer.py:69(restart)
              316477667  255.951    0.000  340.181    0.000 layer.py:126(remove)
              308572085  215.451    0.000  314.478    0.000 layers.py:23(check)
              583939163  221.310    0.000  303.558    0.000 layer.py:130(add)
               51236814   38.017    0.000  300.257    0.000 flatten.py:39(forward)
                9258480  283.985    0.000  283.985    0.000 {built-in method torch._C._nn.mse_loss}
               18516960  266.535    0.000  266.535    0.000 {built-in method sum}
                6172322  262.617    0.000  262.617    0.000 {built-in method nonzero}
               51236814  262.240    0.000  262.240    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9579161: <Causal4_Conver1_1> in cluster <dcc> Done

Job <Causal4_Conver1_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Tue Apr 27 02:44:06 2021
Job was executed on host(s) <n-62-20-2>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed Apr 28 08:26:29 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed Apr 28 08:26:29 2021
Terminated at Thu Apr 29 08:21:53 2021
Results reported at Thu Apr 29 08:21:53 2021

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

    CPU time :                                   85900.95 sec.
    Max Memory :                                 9064 MB
    Average Memory :                             6267.19 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               7320.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86124 sec.
    Turnaround time :                            193067 sec.

The output (if any) is above this job summary.

