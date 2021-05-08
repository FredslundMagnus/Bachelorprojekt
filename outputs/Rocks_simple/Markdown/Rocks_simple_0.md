
# Parameters

    Name :                      Rocks_simple-0
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


      128894274580 function calls (128691885401 primitive calls) in 86102.91 seconds

##    Ordered by: cumulative time
   List reduced from 409 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86102.907 86102.907 {built-in method builtins.exec}
                      1    0.001    0.001 86102.907 86102.907 <string>:1(<module>)
                      1  137.303  137.303 86102.905 86102.905 main.py:67(simple)
                8432867   32.041    0.000 52757.240    0.006 game.py:42(step)
                8432867   40.034    0.000 51005.846    0.006 layers.py:827(step)
                8432867  670.074    0.000 29018.309    0.003 layers.py:17(step)
              843286700 2039.563    0.000 28279.803    0.000 layer.py:106(move)
                8432867   24.206    0.000 26587.505    0.003 agent.py:29(learn)
                8432867  186.017    0.000 26546.804    0.003 agent.py:117(_learn)
                8432867  657.347    0.000 26360.786    0.003 learner.py:42(Qlearn)
                8432868 1154.294    0.000 21901.748    0.003 layers.py:793(update)
              843286700 2286.963    0.000 20960.884    0.000 layers.py:844(check)
              843286700 13015.966    0.000 15519.417    0.000 layers.py:77(check)
                8432867   47.791    0.000 11487.505    0.001 grad_mode.py:23(decorate_context)
                8432867  285.207    0.000 11347.457    0.001 adam.py:55(step)
               29838584  203.265    0.000 9894.064    0.000 layers.py:849(restart)
                8432867 2060.278    0.000 9749.883    0.001 functional.py:53(adam)
        227687409/25298601  864.171    0.000 9567.637    0.000 module.py:715(_call_impl)
               16865734   39.376    0.000 8899.667    0.001 network.py:28(forward)
               16865734  216.983    0.000 8763.677    0.001 container.py:115(forward)
               29838584   96.072    0.000 7181.299    0.000 level.py:8(__init__)
               29838584  767.453    0.000 6070.794    0.000 levels.py:95(generate)
                8432867   51.995    0.000 5826.699    0.001 tensor.py:181(backward)
                8432867   27.944    0.000 5774.703    0.001 __init__.py:68(backward)
               42164340 4119.354    0.000 5663.719    0.000 layer.py:159(update)
                8432867 5532.962    0.001 5532.962    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                8432867  102.279    0.000 4953.514    0.001 agent.py:112(__call__)
               59677168  491.033    0.000 4028.719    0.000 level.py:41(notUsed)
              843286700  794.243    0.000 4011.385    0.000 layers.py:838(isFree)
             3559751740 2692.355    0.000 3217.142    0.000 layer.py:103(isFree)
               33731468   59.444    0.000 3063.132    0.000 conv.py:422(forward)
               50597202  119.125    0.000 2991.615    0.000 linear.py:92(forward)
               33731468   64.563    0.000 2982.154    0.000 conv.py:414(_conv_forward)
               33731468 2906.215    0.000 2906.215    0.000 {built-in method conv2d}
              843286800  374.724    0.000 2834.960    0.000 {built-in method builtins.all}
               50597202  183.503    0.000 2823.403    0.000 functional.py:1669(linear)
             1606137795  785.009    0.000 2699.177    0.000 {built-in method builtins.any}
            10728109549 1828.411    0.000 2653.598    0.000 enum.py:646(__hash__)
             4240439757 1037.182    0.000 2560.162    0.000 layers.py:799(<genexpr>)
              590300720 1598.791    0.000 2474.298    0.000 tensor.py:933(grad)
              149192920  317.537    0.000 2459.895    0.000 layer.py:77(restart)
                8432867  229.423    0.000 2385.652    0.000 optimizer.py:167(zero_grad)
               35756248 2277.838    0.000 2277.838    0.000 {built-in method tensor}
              168657340 2045.597    0.000 2045.597    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               50597202 2028.407    0.000 2028.407    0.000 {built-in method addmm}
             3955212452 1362.950    0.000 1838.433    0.000 layer.py:138(add)
              843286700 1150.704    0.000 1812.863    0.000 layers.py:62(check)
              168657340 1749.008    0.000 1749.008    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               59677168   48.769    0.000 1709.998    0.000 level.py:38(elementsIn)
               16865734   18.758    0.000 1661.035    0.000 game.py:38(board)
             1867557516  774.644    0.000 1582.104    0.000 layer.py:134(remove)
             4880689296 1244.969    0.000 1520.878    0.000 layers.py:809(<genexpr>)
               29838684  690.209    0.000 1382.359    0.000 layers.py:36(reset)
              843286800  884.868    0.000 1356.358    0.000 layers.py:113(isDone)
             1641122120 1311.581    0.000 1311.581    0.000 level.py:32(inverse)
               67462936   59.284    0.000 1310.763    0.000 activation.py:713(forward)
               67462936   84.243    0.000 1251.479    0.000 functional.py:1292(leaky_relu)
             7953777000 1203.598    0.000 1203.598    0.000 layer.py:154(elements)
               67462936 1158.944    0.000 1158.944    0.000 {built-in method torch._C._nn.leaky_relu}
               84328670 1095.256    0.000 1095.256    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              725226642  371.073    0.000 1076.007    0.000 overrides.py:1070(has_torch_function)
               59677168  525.330    0.000 1043.114    0.000 level.py:39(<listcomp>)
            11886822122 1035.409    0.000 1035.409    0.000 layer.py:99(positions)
               84328670 1004.895    0.000 1004.895    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               29838584  420.241    0.000  961.444    0.000 level.py:16(<dictcomp>)
               84328670  931.386    0.000  931.386    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                8432867  533.198    0.000  898.801    0.000 collector.py:46(collect)
              843286700  587.043    0.000  874.084    0.000 layers.py:23(check)
               84328670  836.938    0.000  836.938    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
            10728143378  825.192    0.000  825.192    0.000 {built-in method builtins.hash}
               29838584  282.991    0.000  821.089    0.000 random.py:315(sample)
              843286700  334.274    0.000  792.041    0.000 layers.py:104(<listcomp>)
            11670225338  756.679    0.000  756.679    0.000 {method 'append' of 'list' objects}
             3849179334  727.982    0.000  727.982    0.000 enum.py:352(<genexpr>)
             1867557516  663.045    0.000  663.045    0.000 {method 'remove' of 'list' objects}
               84328670  660.396    0.000  660.396    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               59677168  368.039    0.000  618.115    0.000 {built-in method _functools.reduce}
                8432867   11.010    0.000  465.803    0.000 loss.py:445(forward)
                8432867   42.926    0.000  454.793    0.000 functional.py:2637(mse_loss)
              745964600  303.138    0.000  436.519    0.000 random.py:250(_randbelow_with_getrandbits)
             5068153067  398.254    0.000  398.254    0.000 {method 'random' of '_random.Random' objects}
               50597202  394.139    0.000  394.139    0.000 {method 't' of 'torch._C._TensorBase' objects}
                8432867   32.604    0.000  388.812    0.000 exploration.py:47(epsilonGreedy)
             1501050486  310.263    0.000  388.176    0.000 overrides.py:1083(<genexpr>)
        4220354131/4220354130  321.072    0.000  377.349    0.000 {built-in method builtins.len}
             3559751740  349.692    0.000  349.692    0.000 layer.py:211(isBlocking)
               16865734  291.179    0.000  291.179    0.000 {built-in method sum}
                8432867  281.985    0.000  281.985    0.000 {built-in method torch._C._nn.mse_loss}
             2446772498  279.587    0.000  279.587    0.000 layer.py:190(grid)
             4067241080  275.908    0.000  275.908    0.000 layer.py:92(isDead)
                8432867  267.582    0.000  267.582    0.000 {method 'tolist' of 'torch._C._TensorBase' objects}
                8433710  251.400    0.000  251.400    0.000 {built-in method max}
             2506441056  250.076    0.000  250.076    0.000 level.py:39(<lambda>)
               33731468   24.897    0.000  226.397    0.000 flatten.py:39(forward)
               84328720   99.732    0.000  223.487    0.000 tensor.py:596(__hash__)
                8432867  210.950    0.000  210.950    0.000 {built-in method gather}
                8432867   36.315    0.000  206.950    0.000 __init__.py:28(_make_grads)
               33731468  201.500    0.000  201.500    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                8432867   42.738    0.000  197.648    0.000 tensor.py:506(__rsub__)
              227687409  197.574    0.000  197.574    0.000 {built-in method torch._C._get_tracing_state}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9578855: <Rocks_simple_0> in cluster <dcc> Done

Job <Rocks_simple_0> was submitted from host <n-62-30-3> by user <s183905> in cluster <dcc> at Mon Apr 26 20:44:07 2021
Job was executed on host(s) <n-62-20-2>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Wed May  5 17:15:38 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May  5 17:15:38 2021
Terminated at Thu May  6 17:10:50 2021
Results reported at Thu May  6 17:10:50 2021

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

    CPU time :                                   85896.49 sec.
    Max Memory :                                 2076 MB
    Average Memory :                             2075.23 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14308.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86113 sec.
    Turnaround time :                            851203 sec.

The output (if any) is above this job summary.

