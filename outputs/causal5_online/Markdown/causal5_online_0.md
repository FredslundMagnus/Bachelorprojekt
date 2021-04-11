
# Parameters

    Name :                      causal5_online-0
    Main :                      graphTrain
    Level :                     Levels.Causal5
    Hours :                     12.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Network1 :                  Networks.Teleporter
    K1 :                        200000.0
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
    K2 :                        100000.0
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
    Softmax cap :               0.0
    Update :                    10000
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                2
    Counterfacts :              1
    Topn :                      7
    Minutes used :              715 minutes.
    Hours used :                11 hours.

# Profiling


      46308898533 function calls (46299604210 primitive calls) in 42908.43 seconds

##    Ordered by: cumulative time
   List reduced from 461 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 42908.433 42908.433 {built-in method builtins.exec}
                      1    0.001    0.001 42908.433 42908.433 <string>:1(<module>)
                      1  117.371  117.371 42908.432 42908.432 allGraphsTrain.py:5(graphTrain)
                 464697 6837.504    0.015 15416.057    0.033 allGraphs.py:220(transformNot)
                 464697   11.486    0.000 9932.567    0.021 allGraphsTrain.py:27(<listcomp>)
               46934498 2539.403    0.000 9921.134    0.000 allGraphs.py:141(states)
                 464697  525.436    0.001 9655.265    0.021 allGraphsTrain.py:33(<listcomp>)
                6372742   41.035    0.000 9129.829    0.001 allGraphs.py:228(getInterventions)
              650580112 8732.208    0.000 8732.208    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                5903184   36.479    0.000 8211.797    0.001 allGraphs.py:188(rightIntervention)
              604106700 7719.276    0.000 7719.276    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                8197229  258.392    0.000 7658.201    0.001 allGraphs.py:192(<dictcomp>)
              417547464 2085.668    0.000 7461.897    0.000 allGraphs.py:163(flip_chance)
             4767056861 2763.179    0.000 4510.658    0.000 allGraphs.py:157(compress)
            14984883880 2135.352    0.000 3121.477    0.000 enum.py:646(__hash__)
                 464697    1.827    0.000 2527.589    0.005 game.py:41(step)
                 464697    2.161    0.000 2416.454    0.005 layers.py:710(step)
                 464697  124.748    0.000 1640.731    0.004 allGraphsTrain.py:35(<listcomp>)
                 464698   60.124    0.000 1289.210    0.003 layers.py:676(update)
                 464697    1.644    0.000 1219.954    0.003 agent.py:29(learn)
                 464697    9.565    0.000 1217.344    0.003 agent.py:117(_learn)
                 464697   35.418    0.000 1207.779    0.003 learner.py:42(Qlearn)
                 464697   32.471    0.000 1122.638    0.002 layers.py:17(step)
               10680930 1097.857    0.000 1097.857    0.000 {built-in method tensor}
               46469700   71.209    0.000 1086.042    0.000 layer.py:98(move)
                8696228    6.000    0.000 1023.932    0.000 game.py:37(board)
               49257882  124.319    0.000 1000.636    0.000 tensor.py:21(wrapped)
            14984885445  986.125    0.000  986.125    0.000 {built-in method builtins.hash}
                 464697   44.914    0.000  962.041    0.002 allGraphsTrain.py:42(<listcomp>)
               48793185  741.775    0.000  741.775    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               46469700  112.758    0.000  687.294    0.000 layers.py:727(check)
              537776600  200.748    0.000  685.061    0.000 {built-in method builtins.any}
               46469700  671.894    0.000  671.894    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                1411723   12.240    0.000  629.243    0.000 layers.py:731(restart)
                1411723    5.281    0.000  523.058    0.000 level.py:8(__init__)
                 464697  289.692    0.001  513.994    0.001 agent.py:67(modify)
                 464697    2.581    0.000  509.604    0.001 grad_mode.py:23(decorate_context)
                 464697   13.498    0.000  501.901    0.001 adam.py:55(step)
                1411723   19.036    0.000  475.650    0.000 levels.py:249(generate)
        10688031/1394091   42.549    0.000  440.215    0.000 module.py:715(_call_impl)
                9177408   77.005    0.000  436.020    0.000 level.py:41(notUsed)
                 464697   91.640    0.000  431.558    0.001 functional.py:53(adam)
                 929394    2.364    0.000  402.897    0.000 network.py:24(forward)
                 929394   10.133    0.000  394.885    0.000 container.py:115(forward)
              941503120  185.715    0.000  302.160    0.000 allGraphs.py:192(<genexpr>)
                 464697    2.629    0.000  275.876    0.001 tensor.py:181(backward)
                 464697    1.512    0.000  273.247    0.001 __init__.py:68(backward)
               46469700   73.194    0.000  264.069    0.000 layers.py:721(isFree)
                 464697  259.967    0.001  259.967    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                4182282  133.727    0.000  235.670    0.000 layer.py:167(NoRock_update)
                 464697    5.877    0.000  233.762    0.001 agent.py:112(__call__)
               48328488  225.323    0.000  225.323    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               95727682   45.476    0.000  205.462    0.000 {built-in method builtins.all}
                9177408    5.898    0.000  201.951    0.000 level.py:38(elementsIn)
              392931684  150.165    0.000  190.874    0.000 layer.py:95(isFree)
                1394091    5.356    0.000  155.998    0.000 tensor.py:576(__iter__)
                1858788    3.196    0.000  155.170    0.000 conv.py:422(forward)
                8197229   11.590    0.000  152.576    0.000 allGraphs.py:198(<dictcomp>)
                1858788    3.503    0.000  150.796    0.000 conv.py:414(_conv_forward)
                 464697   34.516    0.000  150.340    0.000 allGraphs.py:209(transform)
                1394091  146.834    0.000  146.834    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
                1858788  146.673    0.000  146.673    0.000 {built-in method conv2d}
              357334531   88.698    0.000  146.522    0.000 layers.py:682(<genexpr>)
              450580770  110.158    0.000  134.904    0.000 layers.py:692(<genexpr>)
                9177408   63.157    0.000  128.874    0.000 level.py:39(<listcomp>)
               80857412   38.973    0.000  126.227    0.000 overrides.py:1070(has_torch_function)
                 469558   24.272    0.000  123.203    0.000 allGraphs.py:170(bestIntervention)
               58537361   66.749    0.000  123.134    0.000 allGraphs.py:150(expand)
                1858788    4.242    0.000  117.445    0.000 linear.py:92(forward)
               46469700   71.648    0.000  115.434    0.000 layers.py:369(check)
               46469700   70.758    0.000  115.060    0.000 layers.py:343(check)
               46469700   70.328    0.000  113.269    0.000 layers.py:331(check)
               46469700   69.354    0.000  112.023    0.000 layers.py:381(check)
                1858788    7.390    0.000  111.374    0.000 functional.py:1669(linear)
               26023086   68.805    0.000  106.909    0.000 tensor.py:933(grad)
                 464697    9.800    0.000  103.324    0.000 optimizer.py:167(zero_grad)
              432835136   95.653    0.000   95.653    0.000 level.py:32(inverse)
                7435152   90.627    0.000   90.627    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               12705507    8.655    0.000   89.900    0.000 layer.py:69(restart)
                 464697   52.937    0.000   88.870    0.000 collector.py:53(collect)
             1025647240   86.974    0.000   86.974    0.000 layer.py:91(positions)
                1858788   79.915    0.000   79.915    0.000 {built-in method addmm}
                 464697    3.636    0.000   77.188    0.000 agent.py:59(modify_board)
                7435152   76.207    0.000   76.207    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                1411823   33.544    0.000   67.873    0.000 layers.py:30(reset)
                9177408   41.940    0.000   67.180    0.000 {built-in method _functools.reduce}
        866966296/866966294   58.326    0.000   66.295    0.000 {built-in method builtins.len}
              381210278   63.808    0.000   63.808    0.000 enum.py:352(<genexpr>)
              202314928   59.001    0.000   59.001    0.000 layer.py:146(elements)
                2788182    2.455    0.000   56.155    0.000 activation.py:713(forward)
               46469700   36.881    0.000   56.022    0.000 layers.py:320(check)
                2788182    3.975    0.000   53.700    0.000 functional.py:1292(leaky_relu)
               46469700   33.692    0.000   51.830    0.000 layers.py:358(check)
                2788182   49.349    0.000   49.349    0.000 {built-in method torch._C._nn.leaky_relu}
              212831494   41.570    0.000   49.273    0.000 overrides.py:1083(<genexpr>)
                3717576   48.984    0.000   48.984    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               97663492   36.025    0.000   48.874    0.000 layer.py:130(add)
                 464697   48.871    0.000   48.871    0.000 {built-in method torch._C._nn.one_hot}
                 464697   31.699    0.000   47.358    0.000 allGraphsTrain.py:41(<listcomp>)
                3717576   45.076    0.000   45.076    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-4>
Subject: Job 9507354: <causal5_online_0> in cluster <dcc> Done

Job <causal5_online_0> was submitted from host <n-62-27-21> by user <s183905> in cluster <dcc> at Fri Apr  9 21:48:59 2021
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Fri Apr  9 22:22:17 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Fri Apr  9 22:22:17 2021
Terminated at Sat Apr 10 10:17:31 2021
Results reported at Sat Apr 10 10:17:31 2021

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

    CPU time :                                   42798.90 sec.
    Max Memory :                                 2083 MB
    Average Memory :                             2081.63 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14301.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   42915 sec.
    Turnaround time :                            44912 sec.

The output (if any) is above this job summary.

