
# Parameters

    Name :                      SuperLevel1_simple-2
    Main :                      simple
    Level :                     Levels.SuperLevel
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
    Network2 :                  Networks.MiniBig
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
    Cf convert :                3
    Counterfacts :              1
    Topn :                      6
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      190964268969 function calls (190765164542 primitive calls) in 86123.69 seconds

##    Ordered by: cumulative time
   List reduced from 423 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86123.686 86123.686 {built-in method builtins.exec}
                      1    0.001    0.001 86123.686 86123.686 <string>:1(<module>)
                      1  122.889  122.889 86123.685 86123.685 main.py:67(simple)
                8296003   26.228    0.000 60247.695    0.007 game.py:42(step)
                8296003   37.244    0.000 58137.349    0.007 layers.py:827(step)
                8296003  681.370    0.000 41827.504    0.005 layers.py:17(step)
              829600300 2480.102    0.000 41072.779    0.000 layer.py:106(move)
              829600300 5111.666    0.000 29969.731    0.000 layers.py:844(check)
                8296003   24.907    0.000 19695.812    0.002 agent.py:29(learn)
                8296003  175.742    0.000 19654.228    0.002 agent.py:117(_learn)
                8296003  508.344    0.000 19478.487    0.002 learner.py:42(Qlearn)
                8296004 1100.917    0.000 16226.399    0.002 layers.py:793(update)
                8296003   46.889    0.000 7993.802    0.001 grad_mode.py:23(decorate_context)
                8296003  261.567    0.000 7860.338    0.001 adam.py:55(step)
        223992081/24888009  776.190    0.000 7827.620    0.000 module.py:715(_call_impl)
               16592006   38.212    0.000 7261.430    0.000 network.py:28(forward)
              829600300 1700.030    0.000 7242.980    0.000 layers.py:838(isFree)
               16592006  181.783    0.000 7134.282    0.000 container.py:115(forward)
              829600300 4725.881    0.000 6678.996    0.000 layers.py:471(check)
                8296003 1432.345    0.000 6450.854    0.001 functional.py:53(adam)
            25313038912 4081.503    0.000 5919.901    0.000 enum.py:646(__hash__)
             8954382212 4103.418    0.000 5542.951    0.000 layer.py:103(isFree)
              107848052 3072.308    0.000 5462.318    0.000 layer.py:159(update)
             1598813163 1243.860    0.000 5281.852    0.000 {built-in method builtins.any}
              829600300 3230.022    0.000 4502.250    0.000 layers.py:77(check)
                8296003   43.810    0.000 4343.675    0.001 tensor.py:181(backward)
                8296003   24.691    0.000 4299.865    0.001 __init__.py:68(backward)
                8296003 4103.624    0.000 4103.624    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                8296003   90.939    0.000 4083.458    0.000 agent.py:112(__call__)
            11465843200 3000.904    0.000 3660.525    0.000 layers.py:809(<genexpr>)
               35179012 3194.336    0.000 3194.336    0.000 {built-in method tensor}
              829600400  394.532    0.000 3005.354    0.000 {built-in method builtins.all}
             4622957462 1223.377    0.000 2708.907    0.000 layers.py:799(<genexpr>)
               16592006   16.932    0.000 2684.488    0.000 game.py:38(board)
            29535580974 2666.021    0.000 2666.021    0.000 layer.py:99(positions)
               33184012   53.686    0.000 2575.794    0.000 conv.py:422(forward)
               33184012   60.694    0.000 2502.313    0.000 conv.py:414(_conv_forward)
               33184012 2430.897    0.000 2430.897    0.000 {built-in method conv2d}
               49776018  106.373    0.000 2390.916    0.000 linear.py:92(forward)
              829600300 1489.385    0.000 2350.097    0.000 layers.py:286(check)
              829600300 1386.845    0.000 2245.174    0.000 layers.py:246(check)
               49776018  171.462    0.000 2238.556    0.000 functional.py:1669(linear)
              580720240 1230.745    0.000 2060.878    0.000 tensor.py:933(grad)
            25313072181 1838.404    0.000 1838.404    0.000 {built-in method builtins.hash}
                8296003  166.396    0.000 1789.256    0.000 optimizer.py:167(zero_grad)
               10611600  108.944    0.000 1706.897    0.000 layers.py:849(restart)
               49776018 1573.832    0.000 1573.832    0.000 {built-in method addmm}
              829600300  889.607    0.000 1429.595    0.000 layers.py:141(check)
              829600300  864.206    0.000 1342.179    0.000 layers.py:313(check)
              165920060 1318.985    0.000 1318.985    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
             2385102685 1311.198    0.000 1311.198    0.000 layer.py:154(elements)
              829600300  857.205    0.000 1308.897    0.000 layers.py:273(check)
              829600300  807.441    0.000 1161.263    0.000 layers.py:62(check)
              165920060 1104.906    0.000 1104.906    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              829600300  708.023    0.000 1053.264    0.000 layers.py:124(check)
              640452977  670.376    0.000 1021.120    0.000 layers.py:113(isDone)
              713456338  343.223    0.000 1019.594    0.000 overrides.py:1070(has_torch_function)
               66368024   50.396    0.000  990.514    0.000 activation.py:713(forward)
              829600300  654.229    0.000  989.917    0.000 layers.py:48(check)
               66368024   79.529    0.000  940.118    0.000 functional.py:1292(leaky_relu)
            11654535003  872.254    0.000  872.254    0.000 {method 'random' of '_random.Random' objects}
               66368024  852.115    0.000  852.115    0.000 {built-in method torch._C._nn.leaky_relu}
              829600300  575.771    0.000  851.531    0.000 layers.py:23(check)
              137950800  126.593    0.000  844.423    0.000 layer.py:77(restart)
             6958713019  836.130    0.000  836.130    0.000 layer.py:211(isBlocking)
               82960030  729.447    0.000  729.447    0.000 {method 'add' of 'torch._C._TensorBase' objects}
        12358078015/12358078014  675.444    0.000  722.395    0.000 {built-in method builtins.len}
               10611600   45.604    0.000  713.755    0.000 level.py:8(__init__)
               82960030  692.262    0.000  692.262    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                8296003  387.374    0.000  663.604    0.000 collector.py:46(collect)
               82960030  610.838    0.000  610.838    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
             9827865600  604.549    0.000  604.549    0.000 layer.py:92(isDead)
             1086316071  405.541    0.000  549.078    0.000 layer.py:138(add)
               82960030  539.339    0.000  539.339    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               10611700  256.323    0.000  508.219    0.000 layers.py:36(reset)
             1659200600  488.739    0.000  488.739    0.000 {method 'union' of 'set' objects}
               82960030  418.766    0.000  418.766    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              507385048  248.831    0.000  379.678    0.000 layer.py:134(remove)
                8296003    9.517    0.000  375.879    0.000 loss.py:445(forward)
             1476688694  299.313    0.000  372.312    0.000 overrides.py:1083(<genexpr>)
                8296003   40.918    0.000  366.362    0.000 functional.py:2637(mse_loss)
               10611600  167.909    0.000  350.422    0.000 level.py:16(<dictcomp>)
                8296003   27.306    0.000  328.381    0.000 exploration.py:47(epsilonGreedy)
              107848052  314.477    0.000  314.477    0.000 layer.py:171(<listcomp>)
              829600400  232.467    0.000  311.072    0.000 layers.py:52(isDone)
              107848052  296.625    0.000  296.625    0.000 layer.py:172(<listcomp>)
               49776018  285.510    0.000  285.510    0.000 {method 't' of 'torch._C._TensorBase' objects}
               10611600  179.433    0.000  279.684    0.000 levels.py:316(generate)
             3357866972  244.096    0.000  244.096    0.000 {method 'append' of 'list' objects}
                8296003  226.097    0.000  226.097    0.000 {method 'tolist' of 'torch._C._TensorBase' objects}
               16592006  214.203    0.000  214.203    0.000 {built-in method sum}
                8296003  213.884    0.000  213.884    0.000 {built-in method torch._C._nn.mse_loss}
               82960080   90.222    0.000  207.626    0.000 tensor.py:596(__hash__)
                8296832  196.181    0.000  196.181    0.000 {built-in method max}
               33184012   23.840    0.000  168.160    0.000 flatten.py:39(forward)
                8296003   29.549    0.000  164.464    0.000 __init__.py:28(_make_grads)
                8296003  161.989    0.000  161.989    0.000 {built-in method gather}
              223992081  149.609    0.000  149.609    0.000 {built-in method torch._C._get_tracing_state}
             1659200600  149.240    0.000  149.240    0.000 layer.py:86(check)
                8296003   34.004    0.000  149.108    0.000 tensor.py:506(__rsub__)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9578848: <SuperLevel1_simple_2> in cluster <dcc> Done

Job <SuperLevel1_simple_2> was submitted from host <n-62-30-3> by user <s183905> in cluster <dcc> at Mon Apr 26 20:44:06 2021
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Mon May  3 12:23:52 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon May  3 12:23:52 2021
Terminated at Tue May  4 12:19:27 2021
Results reported at Tue May  4 12:19:27 2021

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

    CPU time :                                   85899.46 sec.
    Max Memory :                                 2066 MB
    Average Memory :                             2062.98 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14318.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86136 sec.
    Turnaround time :                            660921 sec.

The output (if any) is above this job summary.

