
# Parameters

    Name :                      Coconuts_Conver4_3counterfactsNOCRASH_2-2
    Main :                      Load_Cfagent
    Level :                     Levels.Coconuts
    Failed actions chance :     0
    Use model :                 True
    Depth :                     3
    Model explore :             1000000
    Samples :                   5
    Hours :                     11.0
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
    Num :                       2
    Load name :                 Coconuts_Conver4_3counterfactsNOCRASH
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      64593394299 function calls (64224671034 primitive calls) in 86110.69 seconds

##    Ordered by: cumulative time
   List reduced from 433 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86110.689 86110.689 {built-in method builtins.exec}
                      1    4.215    4.215 86110.689 86110.689 <string>:1(<module>)
                      1  367.808  367.808 86106.474 86106.474 main.py:109(Load_Cfagent)
                9266340   33.273    0.000 23191.684    0.003 agent.py:29(learn)
                3088780 1802.418    0.001 19828.602    0.006 agent.py:212(counterfact)
                9266340  578.259    0.000 18765.009    0.002 learner.py:42(Qlearn)
                3088780   14.046    0.000 18129.191    0.006 game.py:42(step)
                3088780   19.378    0.000 17482.809    0.006 layers.py:827(step)
        409743081/41022637 1722.782    0.000 13555.118    0.000 module.py:866(_call_impl)
               31756297   87.622    0.000 12808.487    0.000 network.py:28(forward)
               31756297  399.096    0.000 12501.700    0.000 container.py:117(forward)
                3088780  284.629    0.000 11710.096    0.004 layers.py:17(step)
              308068975 1135.877    0.000 11398.834    0.000 layer.py:106(move)
                3088780  381.814    0.000 9025.608    0.003 agent.py:54(_learn)
                3088780  380.725    0.000 8294.157    0.003 agent.py:204(_learn)
               90867777 7619.034    0.000 7619.034    0.000 {built-in method tensor}
               84054878   50.630    0.000 7478.081    0.000 game.py:38(board)
               11237809  304.932    0.000 7277.567    0.001 agent.py:49(__call__)
                9266340   77.130    0.000 7181.988    0.001 optimizer.py:84(wrapper)
              308068975 1188.683    0.000 7022.234    0.000 layers.py:844(check)
                5074588   96.913    0.000 6963.270    0.001 agent.py:176(choose_action)
                9266340   39.736    0.000 6840.274    0.001 grad_mode.py:24(decorate_context)
                9266340  289.592    0.000 6716.713    0.001 adam.py:55(step)
                9266340 1404.770    0.000 6111.947    0.001 _functional.py:53(adam)
                3088780  100.405    0.000 5817.503    0.002 agent.py:117(_learn)
                3088780  442.853    0.000 5729.043    0.002 layers.py:793(update)
                3088780 4379.852    0.001 5488.567    0.002 replaybuffer.py:22(sample_data)
                3088780 4311.176    0.001 5358.003    0.002 replaybuffer.py:67(sample_data)
               86485826 2930.263    0.000 5127.054    0.000 layer.py:159(update)
                9266340   31.232    0.000 4981.376    0.001 tensor.py:195(backward)
                9266340   36.520    0.000 4948.855    0.001 __init__.py:68(backward)
                9266340 4733.650    0.001 4733.650    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               63512594  150.130    0.000 4595.394    0.000 conv.py:398(forward)
               63512594   95.172    0.000 4372.843    0.000 conv.py:390(_conv_forward)
               63512594 4277.671    0.000 4277.671    0.000 {built-in method conv2d}
                3088780 2473.653    0.001 4152.224    0.001 replaybuffer.py:28(teleporter_save_data)
                3088780 2056.554    0.001 4051.961    0.001 agent.py:88(interveen)
               89091331  183.405    0.000 3512.484    0.000 linear.py:93(forward)
               89091331   71.582    0.000 3228.820    0.000 functional.py:1737(linear)
               89091331 3139.966    0.000 3139.966    0.000 {built-in method torch._C._nn.linear}
              308068975  490.000    0.000 2469.993    0.000 layers.py:838(isFree)
                3088780 1507.235    0.000 2283.858    0.001 agent.py:67(modify)
              308068975 1495.411    0.000 2095.955    0.000 layers.py:471(check)
                2646089   32.282    0.000 2062.813    0.001 layers.py:849(restart)
             2036179361 1662.411    0.000 1979.993    0.000 layer.py:103(isFree)
               45214389 1949.463    0.000 1949.463    0.000 {built-in method cat}
              120847628  107.523    0.000 1891.255    0.000 activation.py:713(forward)
               14326589   91.043    0.000 1850.268    0.000 agent.py:59(modify_board)
              120847628   98.772    0.000 1783.732    0.000 functional.py:1364(leaky_relu)
              308068975 1276.139    0.000 1782.429    0.000 layers.py:77(check)
                2646089   15.483    0.000 1764.689    0.001 level.py:8(__init__)
              120847628 1664.072    0.000 1664.072    0.000 {built-in method torch._C._nn.leaky_relu}
                2646089  109.022    0.000 1599.930    0.001 levels.py:277(generate)
              159942420 1584.422    0.000 1584.422    0.000 {built-in method clone}
             5456453470  988.260    0.000 1428.726    0.000 enum.py:646(__hash__)
                3088780   57.098    0.000 1424.419    0.000 agent.py:172(__call__)
                5074588 1225.306    0.000 1412.945    0.000 agent.py:187(convert_values)
               23601227  232.581    0.000 1397.287    0.000 level.py:41(notUsed)
                3088780   50.230    0.000 1312.607    0.000 agent.py:112(__call__)
               14326589 1218.462    0.000 1218.462    0.000 {built-in method torch._C._nn.one_hot}
              172971680 1201.826    0.000 1201.826    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
             1203930524 1186.633    0.000 1186.633    0.000 layer.py:154(elements)
              172971680 1063.733    0.000 1063.733    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                9266340  192.857    0.000 1062.061    0.000 optimizer.py:189(zero_grad)
              315498250  256.204    0.000 1060.428    0.000 {built-in method builtins.any}
                3088780  832.216    0.000 1034.069    0.000 replaybuffer.py:73(CF_save_data)
              308068975  729.128    0.000  941.452    0.000 layers.py:62(check)
                3088780   54.822    0.000  881.209    0.000 replaybuffer.py:18(stacker)
                3088780   58.708    0.000  827.944    0.000 replaybuffer.py:63(stacker)
             2449855288  657.862    0.000  804.224    0.000 layers.py:809(<genexpr>)
            10832009298  703.333    0.000  782.560    0.000 {built-in method builtins.len}
               11237809  264.750    0.000  703.916    0.000 exploration.py:53(softmaxer)
               86485840  692.341    0.000  692.341    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               23601227   18.993    0.000  669.696    0.000 level.py:38(elementsIn)
             6656908292  613.371    0.000  613.371    0.000 layer.py:99(positions)
               86485840  611.859    0.000  611.859    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               86485840  558.323    0.000  558.323    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               86485840  556.801    0.000  556.801    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              605400880  395.421    0.000  493.123    0.000 tensor.py:906(grad)
                3088780  272.322    0.000  463.837    0.000 collector.py:46(collect)
              366150316  333.368    0.000  460.770    0.000 layer.py:134(remove)
             5456488781  440.473    0.000  440.473    0.000 {built-in method builtins.hash}
                6177560  164.144    0.000  435.143    0.000 random.py:315(sample)
               23601227  212.498    0.000  433.245    0.000 level.py:39(<listcomp>)
              308068975  283.735    0.000  432.745    0.000 layers.py:48(check)
               86485840  418.611    0.000  418.611    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                9266340   13.940    0.000  400.917    0.000 loss.py:527(forward)
              308878000   66.600    0.000  394.050    0.000 {built-in method builtins.all}
                9266340   36.321    0.000  386.978    0.000 functional.py:2898(mse_loss)
              715735394  170.640    0.000  365.979    0.000 layers.py:799(<genexpr>)
              177357789  362.196    0.000  362.196    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              308068975  240.954    0.000  349.717    0.000 layers.py:23(check)
               63512594   57.298    0.000  315.610    0.000 flatten.py:39(forward)
               86485826  311.430    0.000  311.430    0.000 layer.py:171(<listcomp>)
             1087790329  295.005    0.000  295.005    0.000 level.py:32(inverse)
              516503917  212.468    0.000  287.383    0.000 layer.py:138(add)
               86485826  264.747    0.000  264.747    0.000 layer.py:172(<listcomp>)
               18522623   36.319    0.000  259.528    0.000 layer.py:77(restart)
               63512594  258.311    0.000  258.311    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                6177562  241.670    0.000  241.670    0.000 {built-in method nonzero}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9632957: <Coconuts_Conver4_3counterfactsNOCRASH_2_2> in cluster <dcc> Done

Job <Coconuts_Conver4_3counterfactsNOCRASH_2_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed May 12 15:41:02 2021
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Thu May 13 15:45:12 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu May 13 15:45:12 2021
Terminated at Fri May 14 15:40:30 2021
Results reported at Fri May 14 15:40:30 2021

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

    CPU time :                                   85903.72 sec.
    Max Memory :                                 9094 MB
    Average Memory :                             6104.65 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               7290.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86120 sec.
    Turnaround time :                            172768 sec.

The output (if any) is above this job summary.

