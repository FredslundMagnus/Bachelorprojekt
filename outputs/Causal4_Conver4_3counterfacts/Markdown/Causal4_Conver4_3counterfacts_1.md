
# Parameters

    Name :                      Causal4_Conver4_3counterfacts-1
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
    Counterfacts :              3
    Topn :                      5
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      71353200690 function calls (70993167139 primitive calls) in 86109.46 seconds

##    Ordered by: cumulative time
   List reduced from 514 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86109.455 86109.455 {built-in method builtins.exec}
                      1    4.335    4.335 86109.455 86109.455 <string>:1(<module>)
                      1  300.129  300.129 86105.120 86105.120 main.py:80(CFagent)
                2907354 2281.116    0.001 25421.883    0.009 agent.py:212(counterfact)
                8722062   29.049    0.000 20134.106    0.002 agent.py:29(learn)
                2907354   13.208    0.000 17559.684    0.006 game.py:42(step)
                2907354   18.735    0.000 16910.209    0.006 layers.py:827(step)
                8722061  510.926    0.000 16388.844    0.002 learner.py:42(Qlearn)
        399725694/39693834 1475.433    0.000 12136.042    0.000 module.py:866(_call_impl)
              115329323 12041.241    0.000 12041.241    0.000 {built-in method tensor}
              108596430   54.042    0.000 11916.398    0.000 game.py:38(board)
               30971773   76.256    0.000 11472.681    0.000 network.py:28(forward)
               30971773  364.172    0.000 11214.720    0.000 container.py:117(forward)
                2907354  246.807    0.000 10972.073    0.004 layers.py:17(step)
              290101274  793.011    0.000 10699.885    0.000 layer.py:106(move)
                2907354  290.230    0.000 7828.372    0.003 agent.py:54(_learn)
                2907354  287.082    0.000 7173.013    0.002 agent.py:204(_learn)
                5311549   93.630    0.000 6775.684    0.001 agent.py:176(choose_action)
               11123456  269.495    0.000 6687.375    0.001 agent.py:49(__call__)
              290101274 1320.187    0.000 6627.578    0.000 layers.py:844(check)
                8722061   69.268    0.000 6426.818    0.001 optimizer.py:84(wrapper)
              116294150 3479.638    0.000 6215.699    0.000 layer.py:159(update)
                8722061   35.278    0.000 6112.342    0.001 grad_mode.py:24(decorate_context)
                8722061  238.966    0.000 6001.465    0.001 adam.py:55(step)
                2907355  416.877    0.000 5897.103    0.002 layers.py:793(update)
                8722061 1240.348    0.000 5480.864    0.001 _functional.py:53(adam)
                2907354   83.963    0.000 5085.699    0.002 agent.py:117(_learn)
                2907354 4229.514    0.001 5077.605    0.002 replaybuffer.py:22(sample_data)
                2907354 4102.141    0.001 4918.230    0.002 replaybuffer.py:67(sample_data)
                8722061   31.729    0.000 4215.919    0.000 tensor.py:195(backward)
                8722061   31.036    0.000 4183.083    0.000 __init__.py:68(backward)
               61943546  127.283    0.000 4149.530    0.000 conv.py:398(forward)
                8722061 3992.747    0.000 3992.747    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
               61943546   74.233    0.000 3965.037    0.000 conv.py:390(_conv_forward)
               61943546 3890.803    0.000 3890.803    0.000 {built-in method conv2d}
                2907354 2183.816    0.001 3863.471    0.001 replaybuffer.py:28(teleporter_save_data)
                2907354 1901.031    0.001 3656.317    0.001 agent.py:88(interveen)
               87100611  163.756    0.000 3185.136    0.000 linear.py:93(forward)
               87100611   63.244    0.000 2939.561    0.000 functional.py:1737(linear)
               87100611 2861.367    0.000 2861.367    0.000 {built-in method torch._C._nn.linear}
              290101274  547.363    0.000 2754.632    0.000 layers.py:838(isFree)
             2588211745 1824.533    0.000 2207.269    0.000 layer.py:103(isFree)
                2907354 1349.317    0.000 2041.092    0.001 agent.py:67(modify)
               14030810   88.514    0.000 1714.769    0.000 agent.py:59(modify_board)
              118072384   85.451    0.000 1694.659    0.000 activation.py:713(forward)
              118072384   85.290    0.000 1609.208    0.000 functional.py:1364(leaky_relu)
              170906483 1602.216    0.000 1602.216    0.000 {built-in method clone}
              118072384 1504.891    0.000 1504.891    0.000 {built-in method torch._C._nn.leaky_relu}
               43104345 1487.076    0.000 1487.076    0.000 {built-in method cat}
             1189368244 1433.966    0.000 1433.966    0.000 layer.py:154(elements)
             5856166313  988.626    0.000 1414.109    0.000 enum.py:646(__hash__)
                5311549 1180.297    0.000 1370.630    0.000 agent.py:187(convert_values)
                3416593   43.003    0.000 1244.479    0.000 layers.py:849(restart)
              296040968  285.517    0.000 1240.539    0.000 {built-in method builtins.any}
                2907353   47.178    0.000 1225.494    0.000 agent.py:172(__call__)
                2907354   44.414    0.000 1174.843    0.000 agent.py:112(__call__)
               14030810 1129.581    0.000 1129.581    0.000 {built-in method torch._C._nn.one_hot}
              162811804 1066.414    0.000 1066.414    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              290101274  800.996    0.000 1061.343    0.000 layers.py:77(check)
                2907354  828.361    0.000 1061.183    0.000 replaybuffer.py:73(CF_save_data)
              290735500  130.793    0.000 1045.305    0.000 {built-in method builtins.all}
              290101274  637.665    0.000  986.203    0.000 layers.py:286(check)
             3160507977  780.603    0.000  955.021    0.000 layers.py:809(<genexpr>)
              162811804  954.287    0.000  954.287    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                8722061  164.682    0.000  952.368    0.000 optimizer.py:189(zero_grad)
             1549924400  387.533    0.000  949.011    0.000 layers.py:799(<genexpr>)
                3416593   17.641    0.000  894.332    0.000 level.py:8(__init__)
        13914951858/13914951855  794.976    0.000  867.260    0.000 {built-in method builtins.len}
              290101274  518.584    0.000  857.270    0.000 layers.py:246(check)
                3416593  108.922    0.000  716.660    0.000 levels.py:199(generate)
             7546709009  679.096    0.000  679.096    0.000 layer.py:99(positions)
               11123456  245.676    0.000  659.209    0.000 exploration.py:53(softmaxer)
                2907354   52.868    0.000  646.680    0.000 replaybuffer.py:18(stacker)
               81405902  632.853    0.000  632.853    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                2907353   53.083    0.000  622.350    0.000 replaybuffer.py:63(stacker)
              290101274  429.053    0.000  565.293    0.000 layers.py:62(check)
               81405902  560.096    0.000  560.096    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               81405902  510.450    0.000  510.450    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                6833186   56.861    0.000  504.389    0.000 level.py:41(notUsed)
               81405902  495.374    0.000  495.374    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              290735500  327.218    0.000  491.488    0.000 layers.py:113(isDone)
              290101274  283.163    0.000  448.245    0.000 layers.py:273(check)
              290101274  281.916    0.000  445.311    0.000 layers.py:313(check)
              569841398  354.336    0.000  438.577    0.000 tensor.py:906(grad)
               12647894  165.917    0.000  434.296    0.000 random.py:315(sample)
             5856199496  425.489    0.000  425.489    0.000 {built-in method builtins.hash}
                2907354  250.239    0.000  425.146    0.000 collector.py:46(collect)
              116294150  409.508    0.000  409.508    0.000 layer.py:171(<listcomp>)
               81405902  389.524    0.000  389.524    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              290101274  248.721    0.000  385.919    0.000 layers.py:48(check)
              187844646  371.926    0.000  371.926    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                8722061   11.203    0.000  349.307    0.000 loss.py:527(forward)
              286840135  264.246    0.000  342.092    0.000 layer.py:134(remove)
              116294150  340.060    0.000  340.060    0.000 layer.py:172(<listcomp>)
                8722061   30.076    0.000  338.104    0.000 functional.py:2898(mse_loss)
               34165930   43.348    0.000  296.747    0.000 layer.py:77(restart)
              290101274  197.247    0.000  293.119    0.000 layers.py:23(check)
               61943546   39.814    0.000  272.483    0.000 flatten.py:39(forward)
              479663109  183.805    0.000  255.352    0.000 layer.py:138(add)
               87220600  247.944    0.000  247.944    0.000 agent.py:232(<listcomp>)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9618556: <Causal4_Conver4_3counterfacts_1> in cluster <dcc> Done

Job <Causal4_Conver4_3counterfacts_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Thu May  6 00:28:49 2021
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Thu May  6 06:20:48 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu May  6 06:20:48 2021
Terminated at Fri May  7 06:16:20 2021
Results reported at Fri May  7 06:16:20 2021

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

    CPU time :                                   85906.93 sec.
    Max Memory :                                 8762 MB
    Average Memory :                             6064.25 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               7622.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86179 sec.
    Turnaround time :                            107251 sec.

The output (if any) is above this job summary.

