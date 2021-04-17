
# Parameters

    Name :                      cococonuts_CF_conver4-0
    Main :                      CFagent
    Level :                     Levels.Coconuts
    Hours :                     24.0
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
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      64298727489 function calls (63981473086 primitive calls) in 86110.63 seconds

##    Ordered by: cumulative time
   List reduced from 508 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86110.633 86110.633 {built-in method builtins.exec}
                      1    5.947    5.947 86110.633 86110.633 <string>:1(<module>)
                      1  323.301  323.301 86104.686 86104.686 main.py:94(CFagent)
               10870839   57.951    0.000 28303.700    0.003 agent.py:29(learn)
               10870829  734.550    0.000 22771.930    0.002 learner.py:42(Qlearn)
                3623613   23.585    0.000 22220.219    0.006 game.py:41(step)
                3623613   24.259    0.000 21406.744    0.006 layers.py:710(step)
                3623613  376.537    0.000 14179.134    0.004 layers.py:17(step)
              361921103 1393.520    0.000 13770.113    0.000 layer.py:98(move)
        355769138/38516426 1563.510    0.000 12358.945    0.000 module.py:866(_call_impl)
               27645597   78.629    0.000 11458.334    0.000 network.py:24(forward)
               27645597  381.656    0.000 11174.631    0.000 container.py:117(forward)
                3623613  451.428    0.000 11050.230    0.003 agent.py:54(_learn)
                3623613  443.215    0.000 10003.804    0.003 agent.py:208(_learn)
               10870829  111.860    0.000 8689.338    0.001 optimizer.py:84(wrapper)
               10870829   70.253    0.000 8225.974    0.001 grad_mode.py:24(decorate_context)
              361921103  939.517    0.000 8186.460    0.000 layers.py:727(check)
               10870829  378.268    0.000 8030.580    0.001 adam.py:55(step)
               10870829 1675.987    0.000 7254.218    0.001 _functional.py:53(adam)
                3623613  122.319    0.000 7162.069    0.002 agent.py:117(_learn)
                3623614  565.472    0.000 7161.653    0.002 layers.py:676(update)
                3623613  509.558    0.000 7074.512    0.002 agent.py:216(counterfact)
                3623613 5666.845    0.002 7056.214    0.002 replaybuffer.py:22(sample_data)
                3623613 4977.771    0.001 6171.469    0.002 replaybuffer.py:49(sample_data)
               10870829   51.365    0.000 6072.659    0.001 tensor.py:195(backward)
               10870829   55.417    0.000 6019.719    0.001 __init__.py:68(backward)
                8376915  276.579    0.000 5870.206    0.001 agent.py:49(__call__)
               10870829 5722.440    0.001 5722.440    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3623613 2725.342    0.001 4656.541    0.001 replaybuffer.py:28(teleporter_save_data)
                3623613 2020.104    0.001 4468.649    0.001 agent.py:88(interveen)
               50730589 2508.091    0.000 4217.412    0.000 layer.py:151(update)
               55291194  130.696    0.000 4172.111    0.000 conv.py:398(forward)
               55291194   94.185    0.000 3968.692    0.000 conv.py:390(_conv_forward)
               55291194 3874.507    0.000 3874.507    0.000 {built-in method conv2d}
               43782199 3577.447    0.000 3577.447    0.000 {built-in method tensor}
               35469135   27.996    0.000 3359.438    0.000 game.py:37(board)
              361772909  515.224    0.000 3259.720    0.000 layers.py:721(isFree)
              361921103 2295.952    0.000 3145.387    0.000 layers.py:464(check)
               75689565  160.048    0.000 3116.555    0.000 linear.py:93(forward)
               75689565   65.485    0.000 2862.433    0.000 functional.py:1737(linear)
                3623613 1825.782    0.001 2803.487    0.001 agent.py:67(modify)
               75689565 2780.749    0.000 2780.749    0.000 {built-in method torch._C._nn.linear}
             2256531600 2405.792    0.000 2744.496    0.000 layer.py:95(isFree)
              361921103 1829.602    0.000 2432.486    0.000 layers.py:71(check)
               51860221 2074.522    0.000 2074.522    0.000 {built-in method cat}
              173782917 1758.868    0.000 1758.868    0.000 {built-in method clone}
                3623603   79.702    0.000 1755.861    0.000 agent.py:167(__call__)
             6804408883 1242.813    0.000 1749.165    0.000 enum.py:646(__hash__)
               12000528   88.404    0.000 1683.598    0.000 agent.py:59(modify_board)
                1705981   23.725    0.000 1654.252    0.001 layers.py:731(restart)
              103335162   92.872    0.000 1640.361    0.000 activation.py:713(forward)
                3623613   76.100    0.000 1610.443    0.000 agent.py:112(__call__)
                1150637   28.179    0.000 1591.661    0.001 agent.py:171(choose_action)
              103335162   94.820    0.000 1547.489    0.000 functional.py:1364(leaky_relu)
                1705981   10.456    0.000 1446.659    0.001 level.py:8(__init__)
              103335162 1435.156    0.000 1435.156    0.000 {built-in method torch._C._nn.leaky_relu}
              202922128 1405.489    0.000 1405.489    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                1705981   83.824    0.000 1341.589    0.001 levels.py:262(generate)
              364279033  309.578    0.000 1261.723    0.000 {built-in method builtins.any}
              202922128 1253.422    0.000 1253.422    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               10870829  229.974    0.000 1249.996    0.000 optimizer.py:189(zero_grad)
              362361400  143.305    0.000 1230.942    0.000 {built-in method builtins.all}
               21114928  196.543    0.000 1178.313    0.000 level.py:41(notUsed)
             1465004472  384.138    0.000 1133.190    0.000 layers.py:682(<genexpr>)
               12000528 1115.876    0.000 1115.876    0.000 {built-in method torch._C._nn.one_hot}
                3623613   91.260    0.000 1082.641    0.000 replaybuffer.py:18(stacker)
             1015072556 1049.050    0.000 1049.050    0.000 layer.py:146(elements)
              361921103  834.815    0.000 1040.157    0.000 layers.py:56(check)
             2885243352  779.185    0.000  952.146    0.000 layers.py:692(<genexpr>)
                3623603   88.798    0.000  902.808    0.000 replaybuffer.py:45(stacker)
              101461064  816.511    0.000  816.511    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              101461064  736.998    0.000  736.998    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
             7712503042  719.777    0.000  719.777    0.000 layer.py:91(positions)
              362361400  474.011    0.000  692.537    0.000 layers.py:107(isDone)
              101461064  677.155    0.000  677.155    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              101461064  659.248    0.000  659.248    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                8376915  218.286    0.000  616.554    0.000 exploration.py:53(softmaxer)
              710227532  478.539    0.000  596.418    0.000 tensor.py:906(grad)
                7247226  226.656    0.000  584.880    0.000 random.py:315(sample)
                3623613  333.512    0.000  566.790    0.000 collector.py:53(collect)
               10870829   21.795    0.000  549.613    0.000 loss.py:527(forward)
              361921103  373.613    0.000  537.152    0.000 layers.py:42(check)
        6629888507/6629888504  466.084    0.000  535.859    0.000 {built-in method builtins.len}
               10870829   63.569    0.000  527.818    0.000 functional.py:2898(mse_loss)
                3623613  177.086    0.000  527.423    0.000 replaybuffer.py:55(CF_save_data)
               21114928   18.848    0.000  525.978    0.000 level.py:38(elementsIn)
             6804450130  506.360    0.000  506.360    0.000 {built-in method builtins.hash}
              101461064  491.651    0.000  491.651    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               10870840  479.830    0.000  479.830    0.000 {built-in method nonzero}
              189407048  399.954    0.000  399.954    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              356452996  240.469    0.000  362.402    0.000 layer.py:126(remove)
               21114928  168.945    0.000  336.411    0.000 level.py:39(<listcomp>)
               10870829  309.246    0.000  309.246    0.000 {built-in method torch._C._nn.mse_loss}
              941981443  302.099    0.000  302.099    0.000 level.py:32(inverse)
              457071567  207.001    0.000  286.487    0.000 layer.py:130(add)
               10872028  280.197    0.000  280.197    0.000 {built-in method max}
               55291194   43.897    0.000  272.008    0.000 flatten.py:39(forward)
                1150637  246.979    0.000  261.811    0.000 agent.py:182(convert_values)
              387305524  173.387    0.000  261.048    0.000 random.py:250(_randbelow_with_getrandbits)
               21741678  246.117    0.000  246.117    0.000 {built-in method sum}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-11>
Subject: Job 9501861: <cococonuts_CF_conver4_0> in cluster <dcc> Done

Job <cococonuts_CF_conver4_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed Apr  7 15:46:06 2021
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed Apr  7 16:52:15 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed Apr  7 16:52:15 2021
Terminated at Thu Apr  8 16:47:31 2021
Results reported at Thu Apr  8 16:47:31 2021

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

    CPU time :                                   85901.18 sec.
    Max Memory :                                 10175 MB
    Average Memory :                             6692.30 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               6209.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86117 sec.
    Turnaround time :                            90085 sec.

The output (if any) is above this job summary.

