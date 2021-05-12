
# Parameters

    Name :                      Maze_Conver4_3counterfactsNOCRASH-2
    Main :                      CFagent
    Level :                     Levels.Maze
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
    Num :                       2
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      60865365746 function calls (60505666339 primitive calls) in 86077.07 seconds

##    Ordered by: cumulative time
   List reduced from 517 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86115.295 86115.295 {built-in method builtins.exec}
                      1    4.584    4.584 86115.295 86115.295 <string>:1(<module>)
                      1  364.695  364.695 86110.711 86110.711 main.py:80(CFagent)
                9220737   34.943    0.000 22494.793    0.002 agent.py:29(learn)
                3073579 1749.932    0.001 20915.710    0.007 agent.py:212(counterfact)
                9220737  567.325    0.000 18279.933    0.002 learner.py:42(Qlearn)
                3073579   14.091    0.000 15578.044    0.005 game.py:42(step)
                3073579   19.899    0.000 14914.802    0.005 layers.py:827(step)
        399917789/40220073 1589.366    0.000 12732.737    0.000 module.py:866(_call_impl)
               30999336   84.776    0.000 12002.706    0.000 network.py:28(forward)
               30999336  385.231    0.000 11712.246    0.000 container.py:117(forward)
               99270799 9009.467    0.000 9009.467    0.000 {built-in method tensor}
               92171571   49.459    0.000 8856.549    0.000 game.py:38(board)
                3073579  332.418    0.000 8757.847    0.003 agent.py:54(_learn)
                3073579  300.562    0.000 8382.286    0.003 layers.py:17(step)
              306576749  513.533    0.000 8053.854    0.000 layer.py:106(move)
                3073579  327.235    0.000 7985.444    0.003 agent.py:204(_learn)
                3073579 6258.492    0.002 7222.778    0.002 replaybuffer.py:22(sample_data)
                9220737   82.085    0.000 7144.837    0.001 optimizer.py:84(wrapper)
                3073579 5961.602    0.002 6878.476    0.002 replaybuffer.py:67(sample_data)
               10886871  286.883    0.000 6856.863    0.001 agent.py:49(__call__)
                9220737   42.198    0.000 6791.738    0.001 grad_mode.py:24(decorate_context)
                9220737  284.603    0.000 6662.069    0.001 adam.py:55(step)
                3073580  452.489    0.000 6484.032    0.002 layers.py:793(update)
                4744570   88.748    0.000 6252.829    0.001 agent.py:176(choose_action)
                9220737 1379.828    0.000 6060.784    0.001 _functional.py:53(adam)
                3073579   96.718    0.000 5697.266    0.002 agent.py:117(_learn)
               98354520 3048.217    0.000 5590.728    0.000 layer.py:175(NoRock_update)
                9220737   36.204    0.000 4761.590    0.001 tensor.py:195(backward)
                9220737   40.007    0.000 4724.183    0.001 __init__.py:68(backward)
                9220737 4503.163    0.000 4503.163    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
              306576749 1105.652    0.000 4466.979    0.000 layers.py:844(check)
               61998672  137.361    0.000 4322.276    0.000 conv.py:398(forward)
               61998672   78.652    0.000 4118.220    0.000 conv.py:390(_conv_forward)
               61998672 4039.568    0.000 4039.568    0.000 {built-in method conv2d}
                3073579 1769.069    0.001 3700.800    0.001 agent.py:88(interveen)
                3073579 2034.430    0.001 3470.841    0.001 replaybuffer.py:28(teleporter_save_data)
               86850850  173.680    0.000 3308.828    0.000 linear.py:93(forward)
               86850850   72.843    0.000 3043.551    0.000 functional.py:1737(linear)
               86850850 2953.741    0.000 2953.741    0.000 {built-in method torch._C._nn.linear}
              306576749  477.795    0.000 2634.729    0.000 layers.py:838(isFree)
                3073579 1484.358    0.000 2254.407    0.001 agent.py:67(modify)
             2144594006 1845.889    0.000 2156.934    0.000 layer.py:103(isFree)
                2504723   39.854    0.000 2041.727    0.001 layers.py:849(restart)
               13960450   86.416    0.000 1785.090    0.000 agent.py:59(modify_board)
                2504723   23.284    0.000 1769.392    0.001 level.py:8(__init__)
              117850186   93.172    0.000 1746.502    0.000 activation.py:713(forward)
              117850186   96.706    0.000 1653.330    0.000 functional.py:1364(leaky_relu)
               44696240 1634.620    0.000 1634.620    0.000 {built-in method cat}
                3414695  217.116    0.000 1569.719    0.000 levels.py:9(generate)
              117850186 1537.019    0.000 1537.019    0.000 {built-in method torch._C._nn.leaky_relu}
              138438853 1389.044    0.000 1389.044    0.000 {built-in method clone}
             1167106300 1386.143    0.000 1386.143    0.000 layer.py:154(elements)
                3073579   57.190    0.000 1368.159    0.000 agent.py:172(__call__)
                3073579   56.531    0.000 1310.343    0.000 agent.py:112(__call__)
              306576749  797.568    0.000 1303.922    0.000 layers.py:168(check)
                4744570 1074.740    0.000 1249.644    0.000 agent.py:187(convert_values)
              172120424 1185.618    0.000 1185.618    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              314074013  278.154    0.000 1180.500    0.000 {built-in method builtins.any}
               13960450 1176.348    0.000 1176.348    0.000 {built-in method torch._C._nn.one_hot}
              307358000  127.533    0.000 1135.185    0.000 {built-in method builtins.all}
              172120424 1059.884    0.000 1059.884    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
             1377748617  387.953    0.000 1046.419    0.000 layers.py:799(<genexpr>)
                9220737  187.217    0.000 1036.988    0.000 optimizer.py:189(zero_grad)
                3073579  793.641    0.000  986.432    0.000 replaybuffer.py:73(CF_save_data)
             3479215838  666.655    0.000  953.904    0.000 enum.py:646(__hash__)
             2743679493  734.837    0.000  902.347    0.000 layers.py:809(<genexpr>)
        12111565479/12111565476  749.615    0.000  830.758    0.000 {built-in method builtins.len}
                3073579   55.503    0.000  721.330    0.000 replaybuffer.py:18(stacker)
               86060212  691.371    0.000  691.371    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                3073579   52.670    0.000  685.526    0.000 replaybuffer.py:63(stacker)
               10886871  254.458    0.000  684.790    0.000 exploration.py:53(softmaxer)
               86060212  598.449    0.000  598.449    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                7514169   68.505    0.000  573.571    0.000 level.py:41(notUsed)
              307358000  382.920    0.000  566.593    0.000 layers.py:113(isDone)
               86060212  565.386    0.000  565.386    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               86060212  557.844    0.000  557.844    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               15481271  209.091    0.000  534.386    0.000 random.py:315(sample)
              306576749  326.449    0.000  522.134    0.000 layers.py:141(check)
             5404891723  499.902    0.000  499.902    0.000 layer.py:99(positions)
              602421568  390.830    0.000  489.629    0.000 tensor.py:906(grad)
              306576749  329.579    0.000  474.848    0.000 layers.py:48(check)
                3414695  249.184    0.000  465.263    0.000 levels.py:75(RFS)
                3073579  271.358    0.000  462.660    0.000 collector.py:46(collect)
              306576749  315.840    0.000  461.157    0.000 layers.py:124(check)
               86060212  409.964    0.000  409.964    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                9220737   14.212    0.000  402.885    0.000 loss.py:527(forward)
                9220737   38.712    0.000  388.673    0.000 functional.py:2898(mse_loss)
               98354520  367.198    0.000  367.198    0.000 layer.py:186(<listcomp>)
              346423773  257.559    0.000  348.806    0.000 layer.py:134(remove)
              306576749  219.817    0.000  325.450    0.000 layers.py:23(check)
              155472882  312.205    0.000  312.205    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               98354520  303.331    0.000  303.331    0.000 layer.py:187(<listcomp>)
              486085164  201.968    0.000  292.911    0.000 layer.py:138(add)
             3479250925  287.255    0.000  287.255    0.000 {built-in method builtins.hash}
               61998672   41.682    0.000  283.750    0.000 flatten.py:39(forward)
              394003274  181.138    0.000  269.827    0.000 random.py:250(_randbelow_with_getrandbits)
                6147160  242.777    0.000  242.777    0.000 {built-in method nonzero}
               61998672  242.067    0.000  242.067    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                7514169    8.761    0.000  239.316    0.000 level.py:38(elementsIn)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9624180: <Maze_Conver4_3counterfactsNOCRASH_2> in cluster <dcc> Done

Job <Maze_Conver4_3counterfactsNOCRASH_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun May  9 01:29:16 2021
Job was executed on host(s) <n-62-20-10>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun May  9 01:29:17 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun May  9 01:29:17 2021
Terminated at Mon May 10 01:24:39 2021
Results reported at Mon May 10 01:24:39 2021

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

    CPU time :                                   85904.53 sec.
    Max Memory :                                 9045 MB
    Average Memory :                             6170.20 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               7339.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86227 sec.
    Turnaround time :                            86123 sec.

The output (if any) is above this job summary.

