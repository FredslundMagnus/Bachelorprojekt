
# Parameters

    Name :                      Diamonds2_convert4-0
    Main :                      CFagent
    Level :                     Levels.Causal5
    Failed actions chance :     0
    Use model :                 False
    Depth :                     1
    Model explore :             100000
    Samples :                   5
    Hours :                     24.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.UCB1
    Network1 :                  Networks.Teleporter
    K1 :                        2000000.0
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
    Topn :                      2
    Random counterfacts :       False
    Num :                       0
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      68876610606 function calls (68574729635 primitive calls) in 86119.75 seconds

##    Ordered by: cumulative time
   List reduced from 506 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86119.752 86119.752 {built-in method builtins.exec}
                      1    5.016    5.016 86119.752 86119.752 <string>:1(<module>)
                      1  387.349  387.349 86114.736 86114.736 main.py:80(CFagent)
                9275025   37.446    0.000 23171.438    0.002 agent.py:29(learn)
                3091675   15.379    0.000 18810.807    0.006 game.py:42(step)
                9275025  588.708    0.000 18782.856    0.002 learner.py:42(Qlearn)
                3091675   21.889    0.000 18103.957    0.006 layers.py:827(step)
        337341470/35462190 1417.284    0.000 11166.403    0.000 module.py:866(_call_impl)
               26187165   73.137    0.000 10447.131    0.000 network.py:28(forward)
                3091675  295.467    0.000 10289.390    0.003 layers.py:17(step)
                3091675 1125.555    0.000 10273.545    0.003 agent.py:212(counterfact)
               26187165  348.551    0.000 10193.103    0.000 container.py:117(forward)
              308855809  535.373    0.000 9966.799    0.000 layer.py:106(move)
                3091675  348.600    0.000 9025.935    0.003 agent.py:54(_learn)
                3091675  344.310    0.000 8230.596    0.003 agent.py:204(_learn)
                3091676  476.237    0.000 7761.134    0.003 layers.py:793(update)
                9275025   83.420    0.000 7347.352    0.001 optimizer.py:84(wrapper)
                3091675 6336.424    0.002 7346.960    0.002 replaybuffer.py:22(sample_data)
                3091675 4272.873    0.001 7268.811    0.002 replaybuffer.py:28(teleporter_save_data)
                9275025   45.294    0.000 6991.953    0.001 grad_mode.py:24(decorate_context)
                3091675 6016.673    0.002 6977.386    0.002 replaybuffer.py:67(sample_data)
                9275025  302.464    0.000 6857.843    0.001 adam.py:55(step)
              308855809 1273.410    0.000 6314.334    0.000 layers.py:844(check)
                9275025 1431.262    0.000 6229.857    0.001 _functional.py:53(adam)
                3091675   98.354    0.000 5854.419    0.002 agent.py:117(_learn)
                3091675 3600.378    0.001 5605.090    0.002 agent.py:88(interveen)
                8455008  242.364    0.000 5565.794    0.001 agent.py:49(__call__)
                9275025   37.520    0.000 4866.405    0.001 tensor.py:195(backward)
                9275025   42.370    0.000 4827.529    0.001 __init__.py:68(backward)
               48589626 4701.055    0.000 4701.055    0.000 {built-in method tensor}
                9275025 4601.840    0.000 4601.840    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
               41449983   27.189    0.000 4522.660    0.000 game.py:38(board)
               55650159 2127.407    0.000 3785.130    0.000 layer.py:175(NoRock_update)
               52374330  116.251    0.000 3755.991    0.000 conv.py:398(forward)
               52374330   80.189    0.000 3580.475    0.000 conv.py:390(_conv_forward)
               52374330 3500.287    0.000 3500.287    0.000 {built-in method conv2d}
                2273782   48.063    0.000 3213.620    0.001 agent.py:176(choose_action)
                5167782   63.377    0.000 2906.124    0.001 layers.py:849(restart)
               72378145  141.805    0.000 2858.784    0.000 linear.py:93(forward)
              286250330 2796.635    0.000 2796.635    0.000 {built-in method clone}
               72378145   60.686    0.000 2635.965    0.000 functional.py:1737(linear)
              308855809  601.509    0.000 2576.325    0.000 layers.py:838(isFree)
               72378145 2560.970    0.000 2560.970    0.000 {built-in method torch._C._nn.linear}
                5167782   28.131    0.000 2435.038    0.000 level.py:8(__init__)
                3091675 1602.676    0.001 2391.766    0.001 agent.py:67(modify)
                5167782   83.832    0.000 2148.773    0.000 levels.py:249(generate)
               33589218  339.175    0.000 1980.571    0.000 level.py:41(notUsed)
             2717716137 1644.290    0.000 1974.815    0.000 layer.py:103(isFree)
             6581752236 1162.627    0.000 1672.566    0.000 enum.py:646(__hash__)
               42463433 1629.810    0.000 1629.810    0.000 {built-in method cat}
                3091675 1200.069    0.000 1560.000    0.001 replaybuffer.py:73(CF_save_data)
               11546683   75.720    0.000 1539.228    0.000 agent.py:59(modify_board)
               98565310   89.666    0.000 1513.424    0.000 activation.py:713(forward)
               98565310   85.079    0.000 1423.758    0.000 functional.py:1364(leaky_relu)
                3091675   60.508    0.000 1421.533    0.000 agent.py:172(__call__)
                3091675   55.552    0.000 1334.154    0.000 agent.py:112(__call__)
               98565310 1322.026    0.000 1322.026    0.000 {built-in method torch._C._nn.leaky_relu}
              307091494  304.779    0.000 1316.293    0.000 {built-in method builtins.any}
              173133800 1229.610    0.000 1229.610    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              173133800 1077.386    0.000 1077.386    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                9275025  194.696    0.000 1064.041    0.000 optimizer.py:189(zero_grad)
               11546683 1018.473    0.000 1018.473    0.000 {built-in method torch._C._nn.one_hot}
             3039998180  833.408    0.000 1011.514    0.000 layers.py:809(<genexpr>)
              309167600  140.864    0.000  989.868    0.000 {built-in method builtins.all}
             1101164643  983.600    0.000  983.600    0.000 layer.py:154(elements)
               33589218   26.654    0.000  963.565    0.000 level.py:38(elementsIn)
              308855809  603.034    0.000  935.298    0.000 layers.py:337(check)
              308855809  585.236    0.000  920.821    0.000 layers.py:375(check)
              308855809  567.587    0.000  900.219    0.000 layers.py:349(check)
             1495718034  425.779    0.000  887.686    0.000 layers.py:799(<genexpr>)
              308855809  560.473    0.000  885.204    0.000 layers.py:387(check)
                3091675   62.815    0.000  758.968    0.000 replaybuffer.py:18(stacker)
                3091675   61.471    0.000  722.281    0.000 replaybuffer.py:63(stacker)
               86566900  710.581    0.000  710.581    0.000 {method 'add' of 'torch._C._TensorBase' objects}
             7204226149  684.633    0.000  684.633    0.000 layer.py:99(positions)
                2273782  583.692    0.000  676.901    0.000 agent.py:187(convert_values)
               33589218  307.031    0.000  625.625    0.000 level.py:39(<listcomp>)
               86566900  614.534    0.000  614.534    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              300888688  598.333    0.000  598.333    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               86566900  578.607    0.000  578.607    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
        7673224404/7673224401  515.366    0.000  575.627    0.000 {built-in method builtins.len}
                8455008  212.042    0.000  567.107    0.000 exploration.py:53(softmaxer)
               86566900  565.492    0.000  565.492    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
             6581787547  509.945    0.000  509.945    0.000 {built-in method builtins.hash}
              605968384  404.251    0.000  501.519    0.000 tensor.py:906(grad)
                6183350  182.619    0.000  478.964    0.000 random.py:315(sample)
                3091675  279.287    0.000  474.146    0.000 collector.py:46(collect)
               86566900  418.611    0.000  418.611    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                9275025   14.462    0.000  412.715    0.000 loss.py:527(forward)
                9275025   40.735    0.000  398.253    0.000 functional.py:2898(mse_loss)
              308855809  257.057    0.000  396.968    0.000 layers.py:326(check)
              308855809  254.716    0.000  394.261    0.000 layers.py:364(check)
               46510038   41.931    0.000  392.231    0.000 layer.py:77(restart)
             1584185985  391.080    0.000  391.080    0.000 level.py:32(inverse)
              308855809  223.257    0.000  329.444    0.000 layers.py:23(check)
              497486227  217.066    0.000  312.898    0.000 layer.py:138(add)
             1666553165  312.543    0.000  312.543    0.000 enum.py:352(<genexpr>)
               33589218  193.700    0.000  311.286    0.000 {built-in method _functools.reduce}
             2717716137  276.041    0.000  276.041    0.000 layer.py:211(isBlocking)
                5167882  136.942    0.000  275.351    0.000 layers.py:36(reset)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9678088: <Diamonds2_convert4_0> in cluster <dcc> Done

Job <Diamonds2_convert4_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Fri May 21 19:42:39 2021
Job was executed on host(s) <n-62-20-10>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun May 23 20:23:20 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun May 23 20:23:20 2021
Terminated at Mon May 24 20:18:50 2021
Results reported at Mon May 24 20:18:50 2021

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

    CPU time :                                   85907.23 sec.
    Max Memory :                                 9280 MB
    Average Memory :                             6399.38 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               7104.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86132 sec.
    Turnaround time :                            261371 sec.

The output (if any) is above this job summary.

