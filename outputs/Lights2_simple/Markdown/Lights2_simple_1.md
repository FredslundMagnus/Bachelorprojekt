
# Parameters

    Name :                      Lights2_simple-1
    Main :                      simple
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


      164099489313 function calls (163874597422 primitive calls) in 86109.20 seconds

##    Ordered by: cumulative time
   List reduced from 419 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86109.200 86109.200 {built-in method builtins.exec}
                      1    0.002    0.002 86109.200 86109.200 <string>:1(<module>)
                      1  153.019  153.019 86109.198 86109.198 main.py:66(simple)
                9370480   31.866    0.000 54634.765    0.006 game.py:41(step)
                9370480   41.765    0.000 52387.549    0.006 layers.py:718(step)
                9370480  760.187    0.000 34371.319    0.004 layers.py:17(step)
              937048000 2301.946    0.000 33530.124    0.000 layer.py:98(move)
                9370480   29.390    0.000 24330.837    0.003 agent.py:29(learn)
                9370480  219.442    0.000 24282.489    0.003 agent.py:117(_learn)
                9370480  636.539    0.000 24063.047    0.003 learner.py:42(Qlearn)
              937048000 4495.665    0.000 21824.723    0.000 layers.py:735(check)
                9370481 1312.706    0.000 17915.286    0.002 layers.py:684(update)
                9370480   58.705    0.000 9792.506    0.001 grad_mode.py:23(decorate_context)
                9370480  323.758    0.000 9624.725    0.001 adam.py:55(step)
        253002960/28111440  949.316    0.000 9445.122    0.000 module.py:715(_call_impl)
               18740960   41.359    0.000 8718.410    0.000 network.py:27(forward)
               18740960  222.736    0.000 8554.430    0.000 container.py:115(forward)
              937048000 1888.969    0.000 7975.063    0.000 layers.py:729(isFree)
                9370480 1757.610    0.000 7914.804    0.001 functional.py:53(adam)
             8659135288 4712.782    0.000 6086.094    0.000 layer.py:95(isFree)
               93704810 3412.374    0.000 5791.383    0.000 layer.py:151(update)
                9370480   52.371    0.000 5509.882    0.001 tensor.py:181(backward)
                9370480   33.496    0.000 5457.510    0.001 __init__.py:68(backward)
                9370480 5201.687    0.001 5201.687    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
             1806037119 1281.199    0.000 4980.547    0.000 {built-in method builtins.any}
                9370480  114.892    0.000 4911.074    0.001 agent.py:112(__call__)
            18761947325 3369.299    0.000 4803.933    0.000 enum.py:646(__hash__)
               11836182  123.083    0.000 4146.663    0.000 layers.py:740(restart)
              937048000 2550.711    0.000 3427.063    0.000 layers.py:77(check)
            10177331098 2644.217    0.000 3247.354    0.000 layers.py:700(<genexpr>)
               39694493 3242.223    0.000 3242.223    0.000 {built-in method tensor}
               37481920   65.079    0.000 3071.260    0.000 conv.py:422(forward)
              937048000 1903.676    0.000 3023.627    0.000 layers.py:286(check)
               37481920   71.722    0.000 2980.197    0.000 conv.py:414(_conv_forward)
               11836182   54.945    0.000 2930.129    0.000 level.py:8(__init__)
               37481920 2895.016    0.000 2895.016    0.000 {built-in method conv2d}
              937048000 1762.978    0.000 2868.012    0.000 layers.py:246(check)
               56222880  123.578    0.000 2865.910    0.000 linear.py:92(forward)
               56222880  201.783    0.000 2685.246    0.000 functional.py:1669(linear)
               18740960   19.785    0.000 2638.536    0.000 game.py:37(board)
              655933630 1478.961    0.000 2477.399    0.000 tensor.py:933(grad)
               11836182  395.379    0.000 2445.531    0.000 levels.py:199(generate)
            24224612095 2236.583    0.000 2236.583    0.000 layer.py:91(positions)
                9370480  200.900    0.000 2154.799    0.000 optimizer.py:167(zero_grad)
              937048100  172.792    0.000 2067.363    0.000 {built-in method builtins.all}
             1882342343  411.281    0.000 2015.968    0.000 layers.py:690(<genexpr>)
               56222880 1897.633    0.000 1897.633    0.000 {built-in method addmm}
               23672364  182.455    0.000 1674.867    0.000 level.py:41(notUsed)
              937048000 1205.522    0.000 1614.738    0.000 layers.py:62(check)
              937048000 1023.706    0.000 1604.253    0.000 layers.py:313(check)
              937048100 1063.099    0.000 1603.334    0.000 layers.py:113(isDone)
              187409600 1601.970    0.000 1601.970    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              937048000 1039.989    0.000 1596.872    0.000 layers.py:273(check)
            18761984914 1434.641    0.000 1434.641    0.000 {built-in method builtins.hash}
              187409600 1341.465    0.000 1341.465    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
             2753962862 1327.269    0.000 1327.269    0.000 layer.py:146(elements)
              937048000  838.980    0.000 1248.658    0.000 layers.py:48(check)
              805861360  408.560    0.000 1215.563    0.000 overrides.py:1070(has_torch_function)
               74963840   64.502    0.000 1196.670    0.000 activation.py:713(forward)
               74963840   95.432    0.000 1132.169    0.000 functional.py:1292(leaky_relu)
              118361820  146.696    0.000 1054.974    0.000 layer.py:69(restart)
              937048000  711.632    0.000 1030.578    0.000 layers.py:23(check)
               74963840 1026.848    0.000 1026.848    0.000 {built-in method torch._C._nn.leaky_relu}
               93704800  897.143    0.000  897.143    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               93704800  861.904    0.000  861.904    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
            10352407026  833.607    0.000  833.607    0.000 {method 'random' of '_random.Random' objects}
                9370480  468.054    0.000  811.732    0.000 collector.py:46(collect)
        11874401425/11874401424  723.318    0.000  782.138    0.000 {built-in method builtins.len}
             6815072534  779.271    0.000  779.271    0.000 layer.py:203(isBlocking)
               93704800  764.382    0.000  764.382    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
             1285149661  520.619    0.000  703.369    0.000 layer.py:130(add)
              481135206  666.970    0.000  666.970    0.000 level.py:32(inverse)
               93704800  665.317    0.000  665.317    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               23672364   22.736    0.000  641.157    0.000 level.py:38(elementsIn)
               11836282  307.971    0.000  614.151    0.000 layers.py:36(reset)
             9252119180  603.137    0.000  603.137    0.000 layer.py:84(isDead)
               93704800  506.554    0.000  506.554    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                9370480   15.261    0.000  499.141    0.000 loss.py:445(forward)
                9370480   52.691    0.000  483.880    0.000 functional.py:2637(mse_loss)
                9370480   37.773    0.000  448.387    0.000 exploration.py:47(epsilonGreedy)
             1667945600  358.620    0.000  445.555    0.000 overrides.py:1083(<genexpr>)
              536485779  279.872    0.000  413.885    0.000 layer.py:126(remove)
               11836182  189.318    0.000  387.852    0.000 level.py:16(<dictcomp>)
               23672364  190.332    0.000  385.511    0.000 level.py:39(<listcomp>)
               56222880  344.421    0.000  344.421    0.000 {method 't' of 'torch._C._TensorBase' objects}
             3994027052  310.308    0.000  310.308    0.000 {method 'append' of 'list' objects}
               93704810  309.856    0.000  309.856    0.000 layer.py:163(<listcomp>)
                9370480  286.639    0.000  286.639    0.000 {method 'tolist' of 'torch._C._TensorBase' objects}
               93704810  285.068    0.000  285.068    0.000 layer.py:164(<listcomp>)
                9370480  281.820    0.000  281.820    0.000 {built-in method torch._C._nn.mse_loss}
               18740960  265.896    0.000  265.896    0.000 {built-in method sum}
             1278309259  253.824    0.000  253.824    0.000 enum.py:352(<genexpr>)
               93704850  112.297    0.000  253.212    0.000 tensor.py:596(__hash__)
                9371417  248.970    0.000  248.970    0.000 {built-in method max}
               23672364  136.168    0.000  232.911    0.000 {built-in method _functools.reduce}
                9370480   43.499    0.000  214.115    0.000 __init__.py:28(_make_grads)
               37481920   32.486    0.000  210.254    0.000 flatten.py:39(forward)
                9370480  208.496    0.000  208.496    0.000 {built-in method gather}
              125545764   82.059    0.000  203.912    0.000 random.py:285(choice)
                9370480   45.518    0.000  192.820    0.000 tensor.py:506(__rsub__)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9578832: <Lights2_simple_1> in cluster <dcc> Done

Job <Lights2_simple_1> was submitted from host <n-62-30-3> by user <s183905> in cluster <dcc> at Mon Apr 26 20:44:04 2021
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Wed Apr 28 12:09:30 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed Apr 28 12:09:30 2021
Terminated at Thu Apr 29 12:04:46 2021
Results reported at Thu Apr 29 12:04:46 2021

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

    CPU time :                                   85901.43 sec.
    Max Memory :                                 2062 MB
    Average Memory :                             2060.70 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14322.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86118 sec.
    Turnaround time :                            228042 sec.

The output (if any) is above this job summary.

