
# Parameters

    Name :                      Diamonds2_convert1-2
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
    Cf convert :                1
    Counterfacts :              1
    Topn :                      2
    Random counterfacts :       False
    Num :                       2
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      66706344931 function calls (66411943584 primitive calls) in 86116.89 seconds

##    Ordered by: cumulative time
   List reduced from 504 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86116.892 86116.892 {built-in method builtins.exec}
                      1    4.210    4.210 86116.892 86116.892 <string>:1(<module>)
                      1  337.071  337.071 86112.682 86112.682 main.py:80(CFagent)
                9050646   35.038    0.000 27079.845    0.003 agent.py:29(learn)
                9050641  674.745    0.000 22553.582    0.002 learner.py:42(Qlearn)
                3016882   14.101    0.000 16478.378    0.005 game.py:42(step)
                3016882   18.198    0.000 15754.534    0.005 layers.py:827(step)
        328989229/34589573 1325.786    0.000 12115.665    0.000 module.py:866(_call_impl)
               25538932   70.924    0.000 11388.348    0.000 network.py:28(forward)
               25538932  354.678    0.000 11157.646    0.000 container.py:117(forward)
                3016882  317.500    0.000 10454.504    0.003 agent.py:54(_learn)
                3016882 1166.488    0.000 9964.119    0.003 agent.py:212(counterfact)
                3016882  316.321    0.000 9679.721    0.003 agent.py:204(_learn)
                9050641   78.996    0.000 9554.935    0.001 optimizer.py:84(wrapper)
                9050641   37.926    0.000 9185.321    0.001 grad_mode.py:24(decorate_context)
                9050641  262.110    0.000 9055.076    0.001 adam.py:55(step)
                3016882  242.679    0.000 8942.465    0.003 layers.py:17(step)
              301633455  467.748    0.000 8675.609    0.000 layer.py:106(move)
                9050641 1864.778    0.000 8509.920    0.001 _functional.py:53(adam)
                3016882 4543.864    0.002 8413.495    0.003 replaybuffer.py:28(teleporter_save_data)
                3016882   91.932    0.000 6892.072    0.002 agent.py:117(_learn)
                3016883  425.391    0.000 6768.455    0.002 layers.py:793(update)
                3016882 4167.964    0.001 6350.337    0.002 agent.py:88(interveen)
                8243110  223.759    0.000 5963.499    0.001 agent.py:49(__call__)
                9050641   37.292    0.000 5624.620    0.001 tensor.py:195(backward)
              301633455 1144.147    0.000 5618.189    0.000 layers.py:844(check)
                9050641   34.630    0.000 5585.976    0.001 __init__.py:68(backward)
                9050641 5351.846    0.001 5351.846    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3016882 4250.391    0.001 5256.055    0.002 replaybuffer.py:22(sample_data)
                3016882 4214.525    0.001 5193.065    0.002 replaybuffer.py:67(sample_data)
               47419046 4698.110    0.000 4698.110    0.000 {built-in method tensor}
               40445784   27.260    0.000 4496.037    0.000 game.py:38(board)
               51077864  107.424    0.000 4023.602    0.000 conv.py:398(forward)
               51077864   64.988    0.000 3866.878    0.000 conv.py:390(_conv_forward)
               51077864 3801.890    0.000 3801.890    0.000 {built-in method conv2d}
              278482194 3503.413    0.000 3503.413    0.000 {built-in method clone}
               70583032  141.940    0.000 3243.952    0.000 linear.py:93(forward)
                2211422   51.535    0.000 3227.311    0.001 agent.py:176(choose_action)
               54303885 1747.478    0.000 3152.860    0.000 layer.py:175(NoRock_update)
               70583032   57.118    0.000 3035.926    0.000 functional.py:1737(linear)
               70583032 2964.827    0.000 2964.827    0.000 {built-in method torch._C._nn.linear}
                3016882 1820.881    0.001 2696.263    0.001 agent.py:67(modify)
                5048663   56.861    0.000 2597.638    0.001 layers.py:849(restart)
                5048663   26.016    0.000 2185.471    0.000 level.py:8(__init__)
              301633455  489.413    0.000 2136.361    0.000 layers.py:838(isFree)
                5048663   74.432    0.000 1936.342    0.000 levels.py:249(generate)
               96121964   76.022    0.000 1808.678    0.000 activation.py:713(forward)
               32816504  303.239    0.000 1787.355    0.000 level.py:41(notUsed)
                3016882 1321.368    0.000 1772.649    0.001 replaybuffer.py:73(CF_save_data)
              168945292 1751.145    0.000 1751.145    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               41428787 1745.311    0.000 1745.311    0.000 {built-in method cat}
               96121964   80.773    0.000 1732.656    0.000 functional.py:1364(leaky_relu)
             2630908063 1354.365    0.000 1646.948    0.000 layer.py:103(isFree)
               11259992   79.070    0.000 1638.841    0.000 agent.py:59(modify_board)
               96121964 1634.404    0.000 1634.404    0.000 {built-in method torch._C._nn.leaky_relu}
             6596131937 1075.338    0.000 1565.751    0.000 enum.py:646(__hash__)
              168945292 1526.409    0.000 1526.409    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                3016877   53.746    0.000 1517.845    0.001 agent.py:172(__call__)
                3016882   51.770    0.000 1431.847    0.000 agent.py:112(__call__)
                9050641  208.720    0.000 1310.315    0.000 optimizer.py:189(zero_grad)
              299656520  273.053    0.000 1179.982    0.000 {built-in method builtins.any}
               11259992 1047.604    0.000 1047.604    0.000 {built-in method torch._C._nn.one_hot}
               84472646  954.842    0.000  954.842    0.000 {method 'add' of 'torch._C._TensorBase' objects}
             2966396370  741.077    0.000  906.929    0.000 layers.py:809(<genexpr>)
              292759063  887.796    0.000  887.796    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               32816504   23.029    0.000  874.060    0.000 level.py:38(elementsIn)
              301633455  521.318    0.000  828.942    0.000 layers.py:349(check)
              301633455  511.861    0.000  825.493    0.000 layers.py:387(check)
               84472646  823.273    0.000  823.273    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              301688300   84.255    0.000  812.028    0.000 {built-in method builtins.all}
             1074659467  795.777    0.000  795.777    0.000 layer.py:154(elements)
                3016882   61.267    0.000  790.506    0.000 replaybuffer.py:18(stacker)
               84472646  784.498    0.000  784.498    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               84472646  780.911    0.000  780.911    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                3016877   60.689    0.000  771.132    0.000 replaybuffer.py:63(stacker)
              947883781  228.356    0.000  762.746    0.000 layers.py:799(<genexpr>)
              301633455  466.707    0.000  762.049    0.000 layers.py:375(check)
              301633455  463.837    0.000  757.211    0.000 layers.py:337(check)
             7242298846  638.728    0.000  638.728    0.000 layer.py:99(positions)
                3016882  374.212    0.000  621.386    0.000 collector.py:46(collect)
                8243110  223.431    0.000  613.784    0.000 exploration.py:53(softmaxer)
               84472646  609.085    0.000  609.085    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               32816504  287.802    0.000  573.867    0.000 level.py:39(<listcomp>)
        7497896857/7497896854  488.101    0.000  547.788    0.000 {built-in method builtins.len}
              301688300  339.118    0.000  503.493    0.000 layers.py:113(isDone)
             6596166352  490.419    0.000  490.419    0.000 {built-in method builtins.hash}
                2211422  483.287    0.000  483.287    0.000 agent.py:187(convert_values)
              591308606  373.360    0.000  466.513    0.000 tensor.py:906(grad)
                9050641   13.051    0.000  436.718    0.000 loss.py:527(forward)
                9050641   32.690    0.000  423.667    0.000 functional.py:2898(mse_loss)
                6033764  153.829    0.000  411.024    0.000 random.py:315(sample)
              301633455  257.980    0.000  394.470    0.000 layers.py:326(check)
              301633455  240.936    0.000  363.230    0.000 layers.py:364(check)
             1547737434  350.119    0.000  350.119    0.000 level.py:32(inverse)
               45437967   34.782    0.000  340.753    0.000 layer.py:77(restart)
               51077864   34.390    0.000  295.695    0.000 flatten.py:39(forward)
              301633455  199.618    0.000  295.517    0.000 layers.py:23(check)
             1628204346  281.105    0.000  281.105    0.000 enum.py:352(<genexpr>)
                9050641  279.997    0.000  279.997    0.000 {built-in method torch._C._nn.mse_loss}
               32816504  172.361    0.000  277.165    0.000 {built-in method _functools.reduce}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9678084: <Diamonds2_convert1_2> in cluster <dcc> Done

Job <Diamonds2_convert1_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Fri May 21 19:42:38 2021
Job was executed on host(s) <n-62-20-3>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sat May 22 18:36:49 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat May 22 18:36:49 2021
Terminated at Sun May 23 18:32:16 2021
Results reported at Sun May 23 18:32:16 2021

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

    CPU time :                                   85894.63 sec.
    Max Memory :                                 8743 MB
    Average Memory :                             5947.23 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               7641.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86128 sec.
    Turnaround time :                            168578 sec.

The output (if any) is above this job summary.

