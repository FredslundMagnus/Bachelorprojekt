
# Parameters

    Name :                      Rocks_simple-1
    Main :                      simple
    Level :                     Levels.Rocks
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


      115979833714 function calls (115798190831 primitive calls) in 86121.81 seconds

##    Ordered by: cumulative time
   List reduced from 408 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86121.811 86121.811 {built-in method builtins.exec}
                      1    0.001    0.001 86121.811 86121.811 <string>:1(<module>)
                      1  128.869  128.869 86121.810 86121.810 main.py:67(simple)
                7568438   28.972    0.000 53327.847    0.007 game.py:42(step)
                7568438   36.911    0.000 51686.056    0.007 layers.py:827(step)
                7568438  666.218    0.000 29648.064    0.004 layers.py:17(step)
              756843800 2088.420    0.000 28910.321    0.000 layer.py:106(move)
                7568438   25.532    0.000 26229.186    0.003 agent.py:29(learn)
                7568438  180.974    0.000 26186.559    0.003 agent.py:117(_learn)
                7568438  652.558    0.000 26005.585    0.003 learner.py:42(Qlearn)
                7568439 1160.158    0.000 21955.163    0.003 layers.py:793(update)
              756843800 2323.324    0.000 21196.713    0.000 layers.py:844(check)
              756843800 12993.768    0.000 15669.176    0.000 layers.py:77(check)
                7568438   45.407    0.000 11399.540    0.002 grad_mode.py:23(decorate_context)
                7568438  284.605    0.000 11266.013    0.001 adam.py:55(step)
               26542779  193.471    0.000 9810.569    0.000 layers.py:849(restart)
                7568438 2046.366    0.000 9678.154    0.001 functional.py:53(adam)
        204347826/22705314  854.396    0.000 9354.218    0.000 module.py:715(_call_impl)
               15136876   36.634    0.000 8700.088    0.001 network.py:28(forward)
               15136876  214.057    0.000 8566.857    0.001 container.py:115(forward)
               26542779   93.017    0.000 7089.110    0.000 level.py:8(__init__)
               26542779  730.118    0.000 5997.073    0.000 levels.py:95(generate)
               37842195 4148.602    0.000 5721.973    0.000 layer.py:159(update)
                7568438   46.634    0.000 5710.268    0.001 tensor.py:181(backward)
                7568438   26.614    0.000 5663.634    0.001 __init__.py:68(backward)
                7568438 5429.543    0.001 5429.543    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                7568438   96.911    0.000 4835.254    0.001 agent.py:112(__call__)
              756843800  855.307    0.000 4275.590    0.000 layers.py:838(isFree)
               53085558  482.308    0.000 3997.057    0.000 level.py:41(notUsed)
             3246919892 2844.041    0.000 3420.283    0.000 layer.py:103(isFree)
               30273752   55.468    0.000 2965.809    0.000 conv.py:422(forward)
               45410628  110.257    0.000 2920.741    0.000 linear.py:92(forward)
              756843900  372.283    0.000 2916.168    0.000 {built-in method builtins.all}
               30273752   61.084    0.000 2889.350    0.000 conv.py:414(_conv_forward)
               30273752 2816.847    0.000 2816.847    0.000 {built-in method conv2d}
             9588919903 1967.774    0.000 2806.004    0.000 enum.py:646(__hash__)
               45410628  180.299    0.000 2762.957    0.000 functional.py:1669(linear)
             1441734374  787.354    0.000 2688.820    0.000 {built-in method builtins.any}
             3805389822 1097.947    0.000 2643.188    0.000 layers.py:799(<genexpr>)
              132713895  310.603    0.000 2478.019    0.000 layer.py:77(restart)
              529790690 1586.344    0.000 2464.235    0.000 tensor.py:933(grad)
                7568438  225.593    0.000 2373.996    0.000 optimizer.py:167(zero_grad)
               32120794 2117.466    0.000 2117.466    0.000 {built-in method tensor}
              151368760 2042.413    0.000 2042.413    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               45410628 1983.649    0.000 1983.649    0.000 {built-in method addmm}
              756843800 1151.388    0.000 1874.461    0.000 layers.py:62(check)
             3514212179 1387.870    0.000 1864.459    0.000 layer.py:138(add)
              151368760 1738.525    0.000 1738.525    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
             1655468722  865.875    0.000 1713.329    0.000 layer.py:134(remove)
               53085558   48.531    0.000 1699.699    0.000 level.py:38(elementsIn)
               15136876   16.987    0.000 1518.710    0.000 game.py:38(board)
             4381806726 1204.286    0.000 1508.595    0.000 layers.py:809(<genexpr>)
               26542879  708.382    0.000 1427.515    0.000 layers.py:36(reset)
              756843900  888.692    0.000 1374.643    0.000 layers.py:113(isDone)
             1459852845 1340.633    0.000 1340.633    0.000 level.py:32(inverse)
               60547504   54.134    0.000 1294.710    0.000 activation.py:713(forward)
               60547504   82.537    0.000 1240.576    0.000 functional.py:1292(leaky_relu)
             7067856880 1191.751    0.000 1191.751    0.000 layer.py:154(elements)
               60547504 1149.313    0.000 1149.313    0.000 {built-in method torch._C._nn.leaky_relu}
               75684380 1087.487    0.000 1087.487    0.000 {method 'add' of 'torch._C._TensorBase' objects}
            10762265127 1079.972    0.000 1079.972    0.000 layer.py:99(positions)
              650885748  367.407    0.000 1069.128    0.000 overrides.py:1070(has_torch_function)
               53085558  518.663    0.000 1037.455    0.000 level.py:39(<listcomp>)
               75684380  990.395    0.000  990.395    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               26542779  419.336    0.000  946.860    0.000 level.py:16(<dictcomp>)
               75684380  917.620    0.000  917.620    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                7568438  524.930    0.000  877.953    0.000 collector.py:46(collect)
              756843800  582.353    0.000  865.137    0.000 layers.py:23(check)
             9588950252  838.235    0.000  838.235    0.000 {built-in method builtins.hash}
               75684380  827.397    0.000  827.397    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               26542779  282.917    0.000  817.482    0.000 random.py:315(sample)
              756843800  331.866    0.000  798.578    0.000 layers.py:104(<listcomp>)
            10370547850  760.433    0.000  760.433    0.000 {method 'append' of 'list' objects}
             1655468722  703.611    0.000  703.611    0.000 {method 'remove' of 'list' objects}
             3424020489  670.187    0.000  670.187    0.000 enum.py:352(<genexpr>)
               75684380  655.143    0.000  655.143    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               53085558  366.897    0.000  613.713    0.000 {built-in method _functools.reduce}
                7568438   16.654    0.000  458.063    0.000 loss.py:445(forward)
                7568438   44.567    0.000  441.408    0.000 functional.py:2637(mse_loss)
              663569475  303.057    0.000  437.493    0.000 random.py:250(_randbelow_with_getrandbits)
        4351797732/4351797731  349.169    0.000  403.130    0.000 {built-in method builtins.len}
             4548631238  395.458    0.000  395.458    0.000 {method 'random' of '_random.Random' objects}
               45410628  387.780    0.000  387.780    0.000 {method 't' of 'torch._C._TensorBase' objects}
             1347182124  313.590    0.000  387.573    0.000 overrides.py:1083(<genexpr>)
             3246919892  383.603    0.000  383.603    0.000 layer.py:211(isBlocking)
                7568438   30.986    0.000  374.613    0.000 exploration.py:47(epsilonGreedy)
             3651505605  304.309    0.000  304.309    0.000 layer.py:92(isDead)
               15136876  280.507    0.000  280.507    0.000 {built-in method sum}
             2176516488  278.377    0.000  278.377    0.000 layer.py:190(grid)
                7568438  277.757    0.000  277.757    0.000 {built-in method torch._C._nn.mse_loss}
                7568438  255.015    0.000  255.015    0.000 {method 'tolist' of 'torch._C._TensorBase' objects}
                7569194  249.677    0.000  249.677    0.000 {built-in method max}
             2229593436  246.816    0.000  246.816    0.000 level.py:39(<lambda>)
               30273752   24.335    0.000  225.014    0.000 flatten.py:39(forward)
               75684430   98.737    0.000  221.147    0.000 tensor.py:596(__hash__)
                7568438  206.148    0.000  206.148    0.000 {built-in method gather}
                7568438   34.418    0.000  200.930    0.000 __init__.py:28(_make_grads)
               30273752  200.679    0.000  200.679    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              204347826  193.849    0.000  193.849    0.000 {built-in method torch._C._get_tracing_state}
                7568438   37.187    0.000  188.155    0.000 tensor.py:506(__rsub__)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9578856: <Rocks_simple_1> in cluster <dcc> Done

Job <Rocks_simple_1> was submitted from host <n-62-30-3> by user <s183905> in cluster <dcc> at Mon Apr 26 20:44:07 2021
Job was executed on host(s) <n-62-20-14>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Wed May  5 17:22:44 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May  5 17:22:44 2021
Terminated at Thu May  6 17:18:30 2021
Results reported at Thu May  6 17:18:30 2021

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

    CPU time :                                   85897.08 sec.
    Max Memory :                                 2065 MB
    Average Memory :                             2061.89 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14319.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86145 sec.
    Turnaround time :                            851663 sec.

The output (if any) is above this job summary.

