
# Parameters

    Name :                      Coconuts_simple-2
    Main :                      simple
    Level :                     Levels.Coconuts
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


      174338303011 function calls (174141032448 primitive calls) in 86116.02 seconds

##    Ordered by: cumulative time
   List reduced from 417 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86116.024 86116.024 {built-in method builtins.exec}
                      1    0.001    0.001 86116.024 86116.024 <string>:1(<module>)
                      1  130.553  130.553 86116.023 86116.023 main.py:67(simple)
                8219592   32.393    0.000 53542.065    0.007 game.py:42(step)
                8219592   41.615    0.000 51685.554    0.006 layers.py:827(step)
                8219593 1092.257    0.000 27402.188    0.003 layers.py:793(update)
                8219592   26.428    0.000 25837.786    0.003 agent.py:29(learn)
                8219592  180.673    0.000 25794.872    0.003 agent.py:117(_learn)
                8219592  646.126    0.000 25614.199    0.003 learner.py:42(Qlearn)
                8219592  651.906    0.000 24194.107    0.003 layers.py:17(step)
              821959200 1996.515    0.000 23473.672    0.000 layer.py:106(move)
               24579706  189.195    0.000 16885.268    0.001 layers.py:849(restart)
              821959200 2905.362    0.000 16686.776    0.000 layers.py:844(check)
               24579706   85.881    0.000 14522.659    0.001 level.py:8(__init__)
               24579706  894.973    0.000 13576.544    0.001 levels.py:277(generate)
              219215478 1931.514    0.000 11916.218    0.000 level.py:41(notUsed)
                8219592   48.634    0.000 11138.681    0.001 grad_mode.py:23(decorate_context)
                8219592  271.300    0.000 11004.031    0.001 adam.py:55(step)
                8219592 1984.580    0.000 9458.369    0.001 functional.py:53(adam)
        221928984/24658776  850.554    0.000 9330.765    0.000 module.py:715(_call_impl)
               16439184   38.203    0.000 8675.720    0.001 network.py:28(forward)
               16439184  215.740    0.000 8540.739    0.001 container.py:115(forward)
              219215478  149.560    0.000 5727.141    0.000 level.py:38(elementsIn)
                8219592   46.872    0.000 5677.113    0.001 tensor.py:181(backward)
                8219592   29.099    0.000 5630.241    0.001 __init__.py:68(backward)
                8219592 5394.245    0.001 5394.245    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
            23379279826 3617.295    0.000 5252.589    0.000 enum.py:646(__hash__)
              821959200 3528.996    0.000 5016.022    0.000 layers.py:471(check)
                8219592   99.122    0.000 4830.734    0.001 agent.py:112(__call__)
               57537151 3118.881    0.000 4746.157    0.000 layer.py:159(update)
              821959200 3104.664    0.000 4289.740    0.000 layers.py:77(check)
              821959200  907.285    0.000 3727.315    0.000 layers.py:838(isFree)
              219215478 1836.703    0.000 3710.122    0.000 level.py:39(<listcomp>)
             1570021323  875.153    0.000 3258.190    0.000 {built-in method builtins.any}
               32878368   56.658    0.000 2994.947    0.000 conv.py:422(forward)
               32878368   60.410    0.000 2915.860    0.000 conv.py:414(_conv_forward)
               49317552  108.067    0.000 2903.841    0.000 linear.py:92(forward)
               32878368 2843.365    0.000 2843.365    0.000 {built-in method conv2d}
             3980742142 2172.673    0.000 2820.030    0.000 layer.py:103(isFree)
               49317552  180.649    0.000 2748.474    0.000 functional.py:1669(linear)
               34859755 2513.636    0.000 2513.636    0.000 {built-in method tensor}
            10103828283 2500.677    0.000 2500.677    0.000 level.py:32(inverse)
              575371470 1549.425    0.000 2396.292    0.000 tensor.py:933(grad)
                8219592  216.256    0.000 2308.230    0.000 optimizer.py:167(zero_grad)
              172057942  295.397    0.000 2121.790    0.000 layer.py:77(restart)
              821959200 1572.412    0.000 2082.201    0.000 layers.py:62(check)
             6379036752 1641.831    0.000 2008.212    0.000 layers.py:809(<genexpr>)
              164391840 1984.867    0.000 1984.867    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               49317552 1970.260    0.000 1970.260    0.000 {built-in method addmm}
               16439184   17.522    0.000 1906.743    0.000 game.py:38(board)
              219215478 1156.036    0.000 1867.458    0.000 {built-in method _functools.reduce}
            10483194996 1782.306    0.000 1782.306    0.000 enum.py:352(<genexpr>)
              821959300  148.541    0.000 1737.680    0.000 {built-in method builtins.all}
              164391840 1700.711    0.000 1700.711    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
             1677794753  357.548    0.000 1691.152    0.000 layers.py:799(<genexpr>)
            23379312775 1635.300    0.000 1635.300    0.000 {built-in method builtins.hash}
            18375392790 1601.472    0.000 1601.472    0.000 layer.py:99(positions)
              821959300  862.479    0.000 1325.515    0.000 layers.py:113(isDone)
               65756736   50.526    0.000 1272.808    0.000 activation.py:713(forward)
               65756736   82.404    0.000 1222.282    0.000 functional.py:1292(leaky_relu)
               24579806  590.162    0.000 1195.210    0.000 layers.py:36(reset)
               65756736 1131.906    0.000 1131.906    0.000 {built-in method torch._C._nn.leaky_relu}
               82195920 1066.186    0.000 1066.186    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              706884992  356.882    0.000 1030.170    0.000 overrides.py:1070(has_torch_function)
             2281712375  762.595    0.000 1027.819    0.000 layer.py:138(add)
             4674735905 1027.708    0.000 1027.708    0.000 layer.py:154(elements)
              821959200  649.350    0.000  993.909    0.000 layers.py:48(check)
               82195920  973.498    0.000  973.498    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               82195920  908.671    0.000  908.671    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                8219592  516.845    0.000  870.238    0.000 collector.py:46(collect)
              821959200  557.635    0.000  817.492    0.000 layers.py:23(check)
               82195920  814.349    0.000  814.349    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               24579706  377.155    0.000  803.732    0.000 level.py:16(<dictcomp>)
             9207050076  711.422    0.000  711.422    0.000 level.py:39(<lambda>)
               82195920  647.388    0.000  647.388    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
        7805766727/7805766726  484.587    0.000  538.998    0.000 {built-in method builtins.len}
             6583893192  507.429    0.000  507.429    0.000 {method 'random' of '_random.Random' objects}
                8219592   10.592    0.000  448.855    0.000 loss.py:445(forward)
                8219592   42.958    0.000  438.262    0.000 functional.py:2637(mse_loss)
             3980742142  435.441    0.000  435.441    0.000 layer.py:211(isBlocking)
             6611916353  420.934    0.000  420.934    0.000 {method 'append' of 'list' objects}
               49317552  387.978    0.000  387.978    0.000 {method 't' of 'torch._C._TensorBase' objects}
                8219592   30.135    0.000  372.894    0.000 exploration.py:47(epsilonGreedy)
             1463087536  295.339    0.000  369.734    0.000 overrides.py:1083(<genexpr>)
              424812605  209.614    0.000  369.233    0.000 layer.py:134(remove)
             1643918400  367.239    0.000  367.239    0.000 {method 'union' of 'set' objects}
             4784277564  307.786    0.000  307.786    0.000 layer.py:92(isDead)
              170056066   62.759    0.000  293.898    0.000 random.py:244(randint)
               16439184  280.499    0.000  280.499    0.000 {built-in method sum}
                8219592  276.137    0.000  276.137    0.000 {built-in method torch._C._nn.mse_loss}
                8219592  258.253    0.000  258.253    0.000 {method 'tolist' of 'torch._C._TensorBase' objects}
             2015544666  253.266    0.000  253.266    0.000 layer.py:190(grid)
                8220413  244.455    0.000  244.455    0.000 {built-in method max}
              170056066   99.586    0.000  231.139    0.000 random.py:200(randrange)
               32878368   23.568    0.000  222.518    0.000 flatten.py:39(forward)
               82195970   98.842    0.000  215.593    0.000 tensor.py:596(__hash__)
                8219592  204.585    0.000  204.585    0.000 {built-in method gather}
                8219592   33.161    0.000  199.999    0.000 __init__.py:28(_make_grads)
               32878368  198.950    0.000  198.950    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              221928984  191.336    0.000  191.336    0.000 {built-in method torch._C._get_tracing_state}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9578860: <Coconuts_simple_2> in cluster <dcc> Done

Job <Coconuts_simple_2> was submitted from host <n-62-30-3> by user <s183905> in cluster <dcc> at Mon Apr 26 20:44:08 2021
Job was executed on host(s) <n-62-20-3>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Thu May  6 20:48:52 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu May  6 20:48:52 2021
Terminated at Fri May  7 20:44:59 2021
Results reported at Fri May  7 20:44:59 2021

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

    CPU time :                                   85895.94 sec.
    Max Memory :                                 2067 MB
    Average Memory :                             2063.95 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14317.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86168 sec.
    Turnaround time :                            950451 sec.

The output (if any) is above this job summary.

