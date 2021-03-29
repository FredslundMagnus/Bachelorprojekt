
# Parameters

    Name :                      causal2_good_24h-2
    Main :                      teleport
    Level :                     Levels.Causal2
    Hours :                     24.0
    Batch :                     100
    Width :                     9
    Height :                    9
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
    Layer reddoors :            True
    Layer redkeys :             True
    Layer bluedoors :           True
    Layer bluekeys :            True
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      85262692087 function calls (85065703312 primitive calls) in 86109.60 seconds

##    Ordered by: cumulative time
   List reduced from 481 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86109.598 86109.598 {built-in method builtins.exec}
                      1    1.835    1.835 86109.598 86109.598 <string>:1(<module>)
                      1  164.616  164.616 86107.764 86107.764 main.py:43(teleport)
                3517872   15.854    0.000 26331.266    0.007 game.py:27(step)
                3517872   18.388    0.000 25150.635    0.007 layers.py:475(step)
                7035744   25.479    0.000 24946.325    0.004 agent.py:27(learn)
                7035744  589.828    0.000 21389.991    0.003 learner.py:42(Qlearn)
                3517872  290.539    0.000 17695.658    0.005 layers.py:18(step)
              351787200  889.302    0.000 17374.600    0.000 layer.py:76(move)
                3517872  118.991    0.000 14991.420    0.004 agent.py:52(_learn)
                3517872 7323.398    0.002 14123.794    0.004 replaybuffer.py:29(teleporter_save_data)
              351787200 1999.079    0.000 11856.615    0.000 layers.py:492(check)
                3517872   99.823    0.000 9914.307    0.003 agent.py:113(_learn)
        221611779/24624015  915.709    0.000 9718.379    0.000 module.py:715(_call_impl)
                7035744   42.156    0.000 9173.981    0.001 grad_mode.py:23(decorate_context)
               17588271   45.987    0.000 9103.612    0.001 network.py:24(forward)
                7035744  241.522    0.000 9054.893    0.001 adam.py:55(step)
                3517872 6030.133    0.002 9022.178    0.003 agent.py:84(interveen)
               17588271  234.431    0.000 8948.998    0.001 container.py:115(forward)
                7035744 1650.434    0.000 7759.022    0.001 functional.py:53(adam)
                3517873  391.420    0.000 7413.548    0.002 layers.py:446(update)
                7034655  164.680    0.000 5965.897    0.001 agent.py:47(__call__)
              371819184 5265.840    0.000 5265.840    0.000 {built-in method clone}
                7035744   44.546    0.000 4812.983    0.001 tensor.py:181(backward)
                7035744   27.636    0.000 4768.437    0.001 __init__.py:68(backward)
                3517872 2750.184    0.001 4557.630    0.001 replaybuffer.py:23(sample_data)
                7035744 4553.581    0.001 4553.581    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
              351787200 1150.971    0.000 4049.155    0.000 layers.py:486(isFree)
               63321714 1994.358    0.000 3533.628    0.000 layer.py:121(update)
                3517872 1768.347    0.001 3491.632    0.001 agent.py:65(modify)
               35176542   64.081    0.000 3221.302    0.000 conv.py:422(forward)
               35176542   69.622    0.000 3134.796    0.000 conv.py:414(_conv_forward)
               35176542 3053.233    0.000 3053.233    0.000 {built-in method conv2d}
               45729069  105.965    0.000 2899.878    0.000 linear.py:92(forward)
             6129962794 2197.832    0.000 2898.184    0.000 layer.py:73(isFree)
            11991366251 2024.462    0.000 2886.200    0.000 enum.py:646(__hash__)
               45729069  184.954    0.000 2748.798    0.000 functional.py:1669(linear)
                7288397  108.748    0.000 2346.237    0.000 layers.py:496(restart)
              443251926 1272.645    0.000 1986.368    0.000 tensor.py:933(grad)
               45729069 1961.836    0.000 1961.836    0.000 {built-in method addmm}
                7035744  187.327    0.000 1917.177    0.000 optimizer.py:167(zero_grad)
               31659759 1892.555    0.000 1892.555    0.000 {built-in method cat}
                3517872   46.503    0.000 1880.883    0.001 agent.py:108(__call__)
               15107693 1809.587    0.000 1809.587    0.000 {built-in method tensor}
               10552527   76.855    0.000 1769.467    0.000 agent.py:57(modify_board)
              382371711 1640.038    0.000 1640.038    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              126643392 1625.394    0.000 1625.394    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                7288397   44.109    0.000 1603.752    0.000 level.py:8(__init__)
                3517872   64.182    0.000 1559.430    0.000 replaybuffer.py:19(stacker)
                7035744   10.581    0.000 1503.202    0.000 game.py:23(board)
                7288397   85.312    0.000 1415.983    0.000 levels.py:151(generate)
              126643392 1372.872    0.000 1372.872    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               63317340   52.469    0.000 1338.693    0.000 activation.py:713(forward)
               63317340   81.250    0.000 1286.224    0.000 functional.py:1292(leaky_relu)
            14055068272 1279.711    0.000 1279.711    0.000 layer.py:69(positions)
               34982449  269.247    0.000 1246.349    0.000 level.py:41(notUsed)
               63317340 1196.699    0.000 1196.699    0.000 {built-in method torch._C._nn.leaky_relu}
               10552527 1104.223    0.000 1104.223    0.000 {built-in method torch._C._nn.one_hot}
              369378616  142.347    0.000 1023.311    0.000 {built-in method builtins.all}
              351787200  596.697    0.000  951.754    0.000 layers.py:173(check)
              569893394  332.166    0.000  950.433    0.000 overrides.py:1070(has_torch_function)
              351787200  581.028    0.000  935.778    0.000 layers.py:216(check)
             1335604999  933.272    0.000  933.272    0.000 layer.py:116(elements)
             1186410587  297.601    0.000  911.194    0.000 layers.py:452(<genexpr>)
              351787200  560.754    0.000  908.643    0.000 layers.py:230(check)
              351787200  565.620    0.000  907.214    0.000 layers.py:244(check)
              351787200  563.948    0.000  906.005    0.000 layers.py:302(check)
               63321696  895.093    0.000  895.093    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              351787200  550.873    0.000  891.397    0.000 layers.py:261(check)
            11991391922  861.742    0.000  861.742    0.000 {built-in method builtins.hash}
                3517872  510.752    0.000  855.043    0.000 collector.py:54(collect)
              351787200  599.489    0.000  822.456    0.000 layers.py:76(check)
               63321696  797.070    0.000  797.070    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               63321696  738.171    0.000  738.171    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               17591316   95.845    0.000  724.880    0.000 tensor.py:21(wrapped)
               63321696  658.403    0.000  658.403    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                7034655  231.687    0.000  636.753    0.000 exploration.py:53(softmaxer)
              351787200  387.600    0.000  604.766    0.000 layers.py:142(check)
              131191146   88.215    0.000  593.853    0.000 layer.py:50(restart)
              629693952  239.583    0.000  582.997    0.000 {built-in method builtins.any}
              351787300  372.376    0.000  557.069    0.000 layers.py:110(isDone)
              351787200  347.018    0.000  547.655    0.000 layers.py:287(check)
              351787200  343.684    0.000  545.146    0.000 layers.py:328(check)
               63321696  529.173    0.000  529.173    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               34982449   25.819    0.000  464.009    0.000 level.py:38(elementsIn)
             5110284748  463.545    0.000  463.545    0.000 layer.py:177(isBlocking)
        5187717882/5187717880  330.050    0.000  443.998    0.000 {built-in method builtins.len}
              351787200  290.609    0.000  443.914    0.000 layers.py:123(check)
              351787200  275.079    0.000  427.699    0.000 layers.py:47(check)
              351787200  277.299    0.000  427.373    0.000 layers.py:203(check)
              351787200  278.015    0.000  425.844    0.000 layers.py:63(check)
                7035744    9.267    0.000  405.164    0.000 loss.py:445(forward)
                7035744   38.844    0.000  395.898    0.000 functional.py:2637(mse_loss)
               45729069  383.610    0.000  383.610    0.000 {method 't' of 'torch._C._TensorBase' objects}
                7288497  187.426    0.000  375.378    0.000 layers.py:33(reset)
             1679599105  366.511    0.000  366.511    0.000 level.py:32(inverse)
               21107232  340.351    0.000  340.351    0.000 {built-in method sum}
             1203106470  272.210    0.000  338.785    0.000 overrides.py:1083(<genexpr>)
              608107035  246.544    0.000  335.679    0.000 layer.py:100(add)
               34982449  144.250    0.000  286.341    0.000 level.py:39(<listcomp>)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-11-14>
Subject: Job 9474549: <causal2_good_24h_2> in cluster <dcc> Done

Job <causal2_good_24h_2> was submitted from host <n-62-27-21> by user <s183905> in cluster <dcc> at Sun Mar 28 11:07:13 2021
Job was executed on host(s) <n-62-11-14>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sun Mar 28 11:07:15 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun Mar 28 11:07:15 2021
Terminated at Mon Mar 29 11:02:34 2021
Results reported at Mon Mar 29 11:02:34 2021

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

    CPU time :                                   85897.59 sec.
    Max Memory :                                 2817 MB
    Average Memory :                             2811.09 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13567.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86151 sec.
    Turnaround time :                            86121 sec.

The output (if any) is above this job summary.

