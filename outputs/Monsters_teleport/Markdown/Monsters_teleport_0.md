
# Parameters

    Name :                      Monsters_teleport-0
    Main :                      teleport
    Level :                     Levels.MonsterLevel
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


      83874717688 function calls (83661258805 primitive calls) in 86105.71 seconds

##    Ordered by: cumulative time
   List reduced from 480 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86105.714 86105.714 {built-in method builtins.exec}
                      1    1.476    1.476 86105.714 86105.714 <string>:1(<module>)
                      1  168.829  168.829 86104.238 86104.238 main.py:45(teleport)
                3811782   15.571    0.000 28280.167    0.007 game.py:41(step)
                7623564   27.601    0.000 27518.496    0.004 agent.py:29(learn)
                3811782   18.609    0.000 27424.949    0.007 layers.py:718(step)
                7623564  648.903    0.000 23657.069    0.003 learner.py:42(Qlearn)
                3811782  125.582    0.000 16494.883    0.004 agent.py:54(_learn)
                3811783  561.291    0.000 13904.454    0.004 layers.py:684(update)
                3811782  355.350    0.000 13477.509    0.004 layers.py:17(step)
              381178200 1092.851    0.000 13084.654    0.000 layer.py:98(move)
                3811782  107.902    0.000 10981.574    0.003 agent.py:117(_learn)
        240140186/26682314  963.054    0.000 10608.435    0.000 module.py:715(_call_impl)
                7623564   45.282    0.000 10197.886    0.001 grad_mode.py:23(decorate_context)
                7623564  260.294    0.000 10062.564    0.001 adam.py:55(step)
               19058750   58.234    0.000 9945.768    0.001 network.py:27(forward)
               19058750  255.329    0.000 9769.941    0.001 container.py:115(forward)
                3811782 4913.006    0.001 9554.773    0.003 replaybuffer.py:28(teleporter_save_data)
              381178200 1286.144    0.000 9111.502    0.000 layers.py:735(check)
                7623564 1831.671    0.000 8699.021    0.001 functional.py:53(adam)
                3811782 4876.635    0.001 8109.059    0.002 agent.py:88(interveen)
               12224805   97.371    0.000 6709.089    0.001 layers.py:740(restart)
                7623404  170.511    0.000 6488.160    0.001 agent.py:49(__call__)
               12224805   46.413    0.000 5693.724    0.000 level.py:8(__init__)
                7623564   54.202    0.000 5423.262    0.001 tensor.py:181(backward)
                7623564   27.042    0.000 5369.060    0.001 __init__.py:68(backward)
               12224805  911.708    0.000 5187.441    0.000 levels.py:413(generate)
              381178200 2812.992    0.000 5170.199    0.000 layers.py:538(check)
                7623564 5136.266    0.001 5136.266    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3811782 2594.708    0.001 4643.609    0.001 agent.py:67(modify)
                3811782 2659.942    0.001 4432.315    0.001 replaybuffer.py:22(sample_data)
              248033604 3658.773    0.000 3658.773    0.000 {built-in method clone}
               38117500   65.314    0.000 3520.643    0.000 conv.py:422(forward)
               38117500   75.688    0.000 3431.309    0.000 conv.py:414(_conv_forward)
               61124025  550.234    0.000 3387.863    0.000 level.py:41(notUsed)
               38117500 3342.208    0.000 3342.208    0.000 {built-in method conv2d}
             1067117852  564.808    0.000 3273.224    0.000 {built-in method builtins.any}
               49552686  113.215    0.000 3183.700    0.000 linear.py:92(forward)
               49552686  197.459    0.000 3021.575    0.000 functional.py:1669(linear)
               22870698 1798.913    0.000 2590.051    0.000 layer.py:151(update)
             2607368017  731.873    0.000 2334.007    0.000 layers.py:700(<genexpr>)
             8666242150 1534.469    0.000 2220.303    0.000 enum.py:646(__hash__)
               49552686 2173.392    0.000 2173.392    0.000 {built-in method addmm}
              381178200  474.442    0.000 2101.911    0.000 layers.py:729(isFree)
              480284586 1316.025    0.000 2063.024    0.000 tensor.py:933(grad)
                3811782   50.568    0.000 2050.255    0.001 agent.py:112(__call__)
                7623564  199.520    0.000 2025.475    0.000 optimizer.py:167(zero_grad)
               11435186   86.818    0.000 1937.015    0.000 agent.py:59(modify_board)
               30494096 1867.990    0.000 1867.990    0.000 {built-in method cat}
              137224152 1804.212    0.000 1804.212    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
             2059641260 1297.274    0.000 1627.469    0.000 layer.py:95(isFree)
              137224152 1539.277    0.000 1539.277    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                3811782   67.825    0.000 1503.904    0.000 replaybuffer.py:18(stacker)
               61124025   48.569    0.000 1482.739    0.000 level.py:38(elementsIn)
               68611436   58.471    0.000 1480.529    0.000 activation.py:713(forward)
              377184679  889.961    0.000 1454.261    0.000 layers.py:575(isDead)
               68611436   92.067    0.000 1422.058    0.000 functional.py:1292(leaky_relu)
              381178200  914.368    0.000 1327.306    0.000 layers.py:77(check)
               68611436 1321.470    0.000 1321.470    0.000 {built-in method torch._C._nn.leaky_relu}
              407862982  182.992    0.000 1284.041    0.000 {built-in method builtins.all}
               11435186 1207.797    0.000 1207.797    0.000 {built-in method torch._C._nn.one_hot}
               16343276 1139.513    0.000 1139.513    0.000 {built-in method tensor}
             1548099832  423.867    0.000 1132.496    0.000 layers.py:690(<genexpr>)
              259468790 1119.622    0.000 1119.622    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               68612076 1042.237    0.000 1042.237    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               26684682  149.352    0.000 1037.455    0.000 tensor.py:21(wrapped)
              625133358  346.302    0.000 1015.616    0.000 overrides.py:1070(has_torch_function)
              563409383  179.999    0.000  960.617    0.000 random.py:244(randint)
                3811782  571.238    0.000  954.369    0.000 collector.py:46(collect)
               61124025  463.961    0.000  945.979    0.000 level.py:39(<listcomp>)
             2607812610  919.508    0.000  919.508    0.000 level.py:32(inverse)
               68612076  905.536    0.000  905.536    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               73348830   86.651    0.000  891.834    0.000 layer.py:69(restart)
             8255339876  848.314    0.000  848.314    0.000 layer.py:91(positions)
                7623564    9.301    0.000  836.237    0.000 game.py:37(board)
               68612076  820.680    0.000  820.680    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               64935807  317.139    0.000  807.783    0.000 random.py:315(sample)
              563409383  323.372    0.000  780.618    0.000 random.py:200(randrange)
             1459204293  581.086    0.000  775.963    0.000 layer.py:130(add)
             1026673313  542.627    0.000  762.679    0.000 random.py:250(_randbelow_with_getrandbits)
               68612076  732.858    0.000  732.858    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                7623404  248.377    0.000  694.899    0.000 exploration.py:53(softmaxer)
             8666269981  685.839    0.000  685.839    0.000 {built-in method builtins.hash}
              899801851  430.803    0.000  656.504    0.000 layer.py:126(remove)
              381178300  428.455    0.000  644.400    0.000 layers.py:113(isDone)
               12224905  315.675    0.000  628.003    0.000 layers.py:36(reset)
              381178200  413.074    0.000  627.627    0.000 layers.py:48(check)
              381178200  207.396    0.000  597.843    0.000 layers.py:572(<listcomp>)
             2932025506  595.352    0.000  595.352    0.000 layer.py:146(elements)
               68612076  580.518    0.000  580.518    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               61124025  301.454    0.000  488.191    0.000 {built-in method _functools.reduce}
              381178200  192.636    0.000  482.894    0.000 layers.py:573(<listcomp>)
             2640559334  470.710    0.000  470.710    0.000 enum.py:352(<genexpr>)
                7623564   10.854    0.000  446.320    0.000 loss.py:445(forward)
               19058910  442.086    0.000  442.086    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                7623564   40.148    0.000  435.467    0.000 functional.py:2637(mse_loss)
              381178200  297.099    0.000  433.726    0.000 layers.py:23(check)
               12224805  238.338    0.000  433.316    0.000 level.py:16(<dictcomp>)
               49552686  423.239    0.000  423.239    0.000 {method 't' of 'torch._C._TensorBase' objects}
               22870692  381.112    0.000  381.112    0.000 {built-in method sum}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9550923: <Monsters_teleport_0> in cluster <dcc> Done

Job <Monsters_teleport_0> was submitted from host <n-62-30-4> by user <s183905> in cluster <dcc> at Tue Apr 20 16:21:52 2021
Job was executed on host(s) <n-62-11-13>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Mon Apr 26 07:14:35 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Apr 26 07:14:35 2021
Terminated at Tue Apr 27 07:09:43 2021
Results reported at Tue Apr 27 07:09:43 2021

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

    CPU time :                                   86000.48 sec.
    Max Memory :                                 2674 MB
    Average Memory :                             2671.19 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13710.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86109 sec.
    Turnaround time :                            571671 sec.

The output (if any) is above this job summary.

