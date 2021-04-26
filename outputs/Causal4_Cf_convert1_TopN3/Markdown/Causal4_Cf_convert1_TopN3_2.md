
# Parameters

    Name :                      Causal4_Cf_convert1_TopN3-2
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


      66684369034 function calls (66390035275 primitive calls) in 86109.38 seconds

##    Ordered by: cumulative time
   List reduced from 513 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86109.383 86109.383 {built-in method builtins.exec}
                      1    4.240    4.240 86109.383 86109.383 <string>:1(<module>)
                      1  334.565  334.565 86105.144 86105.144 main.py:79(CFagent)
                9100959   33.022    0.000 27250.009    0.003 agent.py:29(learn)
                9100953  680.696    0.000 22702.961    0.002 learner.py:42(Qlearn)
                3033653   13.054    0.000 18587.117    0.006 game.py:41(step)
                3033653   18.382    0.000 17831.167    0.006 layers.py:718(step)
        328971911/34639843 1335.627    0.000 12115.668    0.000 module.py:866(_call_impl)
                3033653  248.595    0.000 11454.364    0.004 layers.py:17(step)
               25538890   80.354    0.000 11384.544    0.000 network.py:27(forward)
                3033653 1448.334    0.000 11308.952    0.004 agent.py:210(counterfact)
              303294399  788.783    0.000 11182.009    0.000 layer.py:98(move)
               25538890  344.831    0.000 11141.210    0.000 container.py:117(forward)
                3033653  317.435    0.000 10515.791    0.003 agent.py:54(_learn)
                3033653  314.950    0.000 9745.511    0.003 agent.py:202(_learn)
                9100953   79.468    0.000 9629.983    0.001 optimizer.py:84(wrapper)
                9100953   37.562    0.000 9258.064    0.001 grad_mode.py:24(decorate_context)
                9100953  270.583    0.000 9131.568    0.001 adam.py:55(step)
                9100953 1866.568    0.000 8571.202    0.001 _functional.py:53(adam)
              303294399 1315.936    0.000 6944.325    0.000 layers.py:735(check)
                3033653   90.924    0.000 6937.333    0.002 agent.py:117(_learn)
                3033654  426.406    0.000 6334.517    0.002 layers.py:684(update)
                3033653 3206.546    0.001 5990.418    0.002 replaybuffer.py:28(teleporter_save_data)
                8217409  220.249    0.000 5943.930    0.001 agent.py:49(__call__)
                9100953   39.055    0.000 5639.363    0.001 tensor.py:195(backward)
                9100953   33.946    0.000 5598.956    0.001 __init__.py:68(backward)
               51135374 5464.180    0.000 5464.180    0.000 {built-in method tensor}
                9100953 5361.595    0.001 5361.595    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               44123319   29.411    0.000 5262.563    0.000 game.py:37(board)
                3033653 4226.108    0.001 5227.541    0.002 replaybuffer.py:22(sample_data)
                3033653 2987.286    0.001 5177.752    0.002 agent.py:88(interveen)
                3033653 4034.770    0.001 5004.610    0.002 replaybuffer.py:67(sample_data)
               51077780  110.545    0.000 4024.288    0.000 conv.py:398(forward)
               60673070 2386.532    0.000 3946.559    0.000 layer.py:151(update)
               51077780   69.236    0.000 3863.882    0.000 conv.py:390(_conv_forward)
               51077780 3794.646    0.000 3794.646    0.000 {built-in method conv2d}
               70549364  147.198    0.000 3249.152    0.000 linear.py:93(forward)
                2153228   48.251    0.000 3128.850    0.001 agent.py:175(choose_action)
               70549364   58.179    0.000 3035.389    0.000 functional.py:1737(linear)
               70549364 2962.917    0.000 2962.917    0.000 {built-in method torch._C._nn.linear}
              303294399  565.802    0.000 2897.174    0.000 layers.py:729(isFree)
                3033653 1832.929    0.001 2722.353    0.001 agent.py:67(modify)
              207403896 2692.578    0.000 2692.578    0.000 {built-in method clone}
             2900751952 1885.775    0.000 2331.372    0.000 layer.py:95(isFree)
                3033653 1407.404    0.000 1904.137    0.001 replaybuffer.py:73(CF_save_data)
                5566259   59.622    0.000 1876.861    0.000 layers.py:740(restart)
               96088254   73.714    0.000 1798.949    0.000 activation.py:713(forward)
              169884448 1777.345    0.000 1777.345    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               41587562 1739.705    0.000 1739.705    0.000 {built-in method cat}
               96088254   80.097    0.000 1725.235    0.000 functional.py:1364(leaky_relu)
               11251062   80.319    0.000 1645.435    0.000 agent.py:59(modify_board)
               96088254 1629.287    0.000 1629.287    0.000 {built-in method torch._C._nn.leaky_relu}
              169884448 1545.992    0.000 1545.992    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                3033647   53.792    0.000 1530.644    0.001 agent.py:171(__call__)
             6126105336 1058.633    0.000 1507.990    0.000 enum.py:646(__hash__)
                3033653   50.564    0.000 1434.776    0.000 agent.py:112(__call__)
                9100953  214.596    0.000 1338.097    0.000 optimizer.py:189(zero_grad)
                5566259   28.469    0.000 1319.455    0.000 level.py:8(__init__)
              300832795  286.839    0.000 1232.659    0.000 {built-in method builtins.any}
              303294399  822.121    0.000 1084.291    0.000 layers.py:77(check)
                5566259  169.632    0.000 1072.089    0.000 levels.py:199(generate)
               11251062 1048.924    0.000 1048.924    0.000 {built-in method torch._C._nn.one_hot}
              303294399  622.226    0.000 1001.769    0.000 layers.py:246(check)
               84942224  954.918    0.000  954.918    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              303294399  571.374    0.000  950.276    0.000 layers.py:286(check)
             3275790551  779.986    0.000  945.821    0.000 layers.py:700(<genexpr>)
             1389489902  895.800    0.000  895.800    0.000 layer.py:146(elements)
               84942224  824.482    0.000  824.482    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               84942224  792.428    0.000  792.428    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                3033653   59.919    0.000  789.232    0.000 replaybuffer.py:18(stacker)
               84942224  784.585    0.000  784.585    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                3033647   61.303    0.000  764.456    0.000 replaybuffer.py:63(stacker)
               11132518   83.664    0.000  735.710    0.000 level.py:41(notUsed)
              221688605  668.306    0.000  668.306    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
             7490905496  633.501    0.000  633.501    0.000 layer.py:91(positions)
                3033653  376.398    0.000  624.627    0.000 collector.py:46(collect)
              303294399  470.956    0.000  622.413    0.000 layers.py:62(check)
                8217409  224.745    0.000  612.242    0.000 exploration.py:53(softmaxer)
               84942224  610.904    0.000  610.904    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
        7938683222/7938683219  509.075    0.000  570.106    0.000 {built-in method builtins.len}
              303365400   93.687    0.000  559.675    0.000 {built-in method builtins.all}
              303294399  330.554    0.000  503.721    0.000 layers.py:273(check)
             1087971064  262.332    0.000  501.414    0.000 layers.py:690(<genexpr>)
              594595652  395.700    0.000  488.171    0.000 tensor.py:906(grad)
              303294399  306.996    0.000  486.332    0.000 layers.py:313(check)
               17199824  186.383    0.000  485.137    0.000 random.py:315(sample)
               55662590   67.472    0.000  480.326    0.000 layer.py:69(restart)
             6126139975  449.363    0.000  449.363    0.000 {built-in method builtins.hash}
                2153228  448.790    0.000  448.790    0.000 agent.py:186(convert_values)
                9100953   12.890    0.000  439.769    0.000 loss.py:527(forward)
                9100953   34.532    0.000  426.879    0.000 functional.py:2898(mse_loss)
              303294399  261.167    0.000  389.019    0.000 layers.py:48(check)
              316423538  277.480    0.000  359.400    0.000 layer.py:126(remove)
              636502365  241.126    0.000  327.047    0.000 layer.py:130(add)
              303294399  213.686    0.000  312.259    0.000 layers.py:23(check)
               51077780   36.959    0.000  298.785    0.000 flatten.py:39(forward)
              226271228  294.116    0.000  294.116    0.000 level.py:32(inverse)
               11132518   11.402    0.000  280.523    0.000 level.py:38(elementsIn)
                9100953  279.592    0.000  279.592    0.000 {built-in method torch._C._nn.mse_loss}
                5566359  137.454    0.000  272.710    0.000 layers.py:36(reset)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9551811: <Causal4_Cf_convert1_TopN3_2> in cluster <dcc> Done

Job <Causal4_Cf_convert1_TopN3_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed Apr 21 03:20:30 2021
Job was executed on host(s) <n-62-20-3>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed Apr 21 03:48:03 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed Apr 21 03:48:03 2021
Terminated at Thu Apr 22 03:43:17 2021
Results reported at Thu Apr 22 03:43:17 2021

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

    CPU time :                                   85896.18 sec.
    Max Memory :                                 8833 MB
    Average Memory :                             6275.61 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               7551.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86116 sec.
    Turnaround time :                            87767 sec.

The output (if any) is above this job summary.

