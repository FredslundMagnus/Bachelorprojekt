
# Parameters

    Name :                      causal7_online_var-0
    Main :                      graphTrain
    Level :                     Levels.Causal7
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
    Counterfacts :              10
    Topn :                      7
    Minutes used :              715 minutes.
    Hours used :                11 hours.

# Profiling


      17329668647 function calls (16943680650 primitive calls) in 42911.83 seconds

##    Ordered by: cumulative time
   List reduced from 465 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 42911.834 42911.834 {built-in method builtins.exec}
                      1    0.001    0.001 42911.834 42911.834 <string>:1(<module>)
                      1  179.365  179.365 42911.833 42911.833 allGraphsTrain.py:5(graphTrain)
                 676003 7900.296    0.012 17621.734    0.026 allGraphs.py:238(transformNot)
                 676003   20.245    0.000 10679.201    0.016 allGraphsTrain.py:24(<listcomp>)
               68276404 2839.747    0.000 10659.050    0.000 allGraphs.py:198(states)
              676008808 9758.227    0.000 9758.227    0.000 {method 'item' of 'torch._C._TensorBase' objects}
              608403100 8585.480    0.000 8585.480    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 676003    2.881    0.000 3550.318    0.005 game.py:41(step)
                 676003    3.542    0.000 3392.711    0.005 layers.py:710(step)
                 676003  816.161    0.001 2710.305    0.004 allGraphsTrain.py:30(<listcomp>)
                 676003  203.607    0.000 2603.387    0.004 allGraphsTrain.py:32(<listcomp>)
                 676003    2.327    0.000 1959.342    0.003 agent.py:29(learn)
                 676003   15.209    0.000 1955.533    0.003 agent.py:117(_learn)
                 676003   56.551    0.000 1940.323    0.003 learner.py:42(Qlearn)
                 676004   97.876    0.000 1924.206    0.003 layers.py:676(update)
               10063302   57.002    0.000 1894.143    0.000 allGraphs.py:245(getInterventions)
               71656318  201.781    0.000 1612.378    0.000 tensor.py:21(wrapped)
                 676003   72.732    0.000 1551.587    0.002 allGraphsTrain.py:39(<listcomp>)
                 676003   50.986    0.000 1461.089    0.002 layers.py:17(step)
               16315351 1414.207    0.000 1414.207    0.000 {built-in method tensor}
               67600300  111.325    0.000 1403.419    0.000 layer.py:98(move)
               13443318    8.819    0.000 1304.770    0.000 game.py:37(board)
               70980315 1196.274    0.000 1196.274    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               67600300 1073.761    0.000 1073.761    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                2631054   20.993    0.000 1032.433    0.000 layers.py:731(restart)
                9417772    8.613    0.000  864.135    0.000 allGraphs.py:225(rightIntervention)
                 676003  482.484    0.001  838.641    0.001 agent.py:67(modify)
                2631054   10.252    0.000  829.927    0.000 level.py:8(__init__)
                 676003    4.171    0.000  822.964    0.001 grad_mode.py:23(decorate_context)
        84736620/9417772   59.174    0.000  813.865    0.000 {built-in method builtins.min}
               67600300  142.258    0.000  813.601    0.000 layers.py:727(check)
                 676003   21.904    0.000  810.563    0.001 adam.py:55(step)
               23840624   10.564    0.000  797.070    0.000 allGraphs.py:226(<lambda>)
        160055468/23840624  245.100    0.000  786.506    0.000 allGraphs.py:61(expected_moves)
                2631054   31.385    0.000  725.475    0.000 levels.py:446(generate)
        15548069/2028009   67.980    0.000  706.349    0.000 module.py:715(_call_impl)
                 676003  148.697    0.000  696.991    0.001 functional.py:53(adam)
               12631020  119.154    0.000  661.598    0.000 level.py:41(notUsed)
                1352006    3.770    0.000  647.294    0.000 network.py:24(forward)
        211533692/50599830   64.357    0.000  646.318    0.000 allGraphs.py:65(<genexpr>)
                1352006   17.188    0.000  634.396    0.000 container.py:115(forward)
             2442529890  425.748    0.000  624.072    0.000 enum.py:646(__hash__)
                 676003    4.022    0.000  439.341    0.001 tensor.py:181(backward)
                 676003    2.412    0.000  435.319    0.001 __init__.py:68(backward)
                 676003  414.540    0.001  414.540    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               67600300  100.299    0.000  373.048    0.000 layers.py:721(isFree)
                 676003    8.884    0.000  372.159    0.001 agent.py:112(__call__)
               70304312  368.199    0.000  368.199    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              186650021  106.469    0.000  364.846    0.000 {built-in method builtins.any}
                4732028  193.053    0.000  331.099    0.000 layer.py:167(NoRock_update)
               12631020    9.400    0.000  310.616    0.000 level.py:38(elementsIn)
              465788323  212.429    0.000  272.749    0.000 layer.py:95(isFree)
               85382150   57.841    0.000  263.095    0.000 allGraphs.py:70(layers_not_in)
                2028009    8.739    0.000  257.410    0.000 tensor.py:576(__iter__)
              139256718   52.340    0.000  253.474    0.000 {built-in method builtins.all}
                2704012    5.286    0.000  249.132    0.000 conv.py:422(forward)
                2028009  242.882    0.000  242.882    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
                2704012    6.040    0.000  241.945    0.000 conv.py:414(_conv_forward)
                2704012  234.890    0.000  234.890    0.000 {built-in method conv2d}
               85382150  102.676    0.000  205.254    0.000 allGraphs.py:71(<listcomp>)
              117624656   62.651    0.000  203.886    0.000 overrides.py:1070(has_torch_function)
               12631020   99.594    0.000  200.331    0.000 level.py:39(<listcomp>)
             2442532127  198.325    0.000  198.325    0.000 {built-in method builtins.hash}
               67600300  118.916    0.000  192.875    0.000 layers.py:610(check)
               67600300  117.925    0.000  191.061    0.000 layers.py:595(check)
                2704012    6.947    0.000  187.509    0.000 linear.py:92(forward)
               67600300  113.495    0.000  184.619    0.000 layers.py:625(check)
              269479846   79.514    0.000  182.228    0.000 layers.py:682(<genexpr>)
              519754768  146.870    0.000  178.261    0.000 layers.py:692(<genexpr>)
                2704012   11.867    0.000  177.568    0.000 functional.py:1669(linear)
               18417378   15.055    0.000  174.773    0.000 layer.py:69(restart)
               37856222  110.281    0.000  172.792    0.000 tensor.py:933(grad)
                 676003   16.006    0.000  167.020    0.000 optimizer.py:167(zero_grad)
               10816048  145.946    0.000  145.946    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                 676003   85.356    0.000  143.057    0.000 collector.py:46(collect)
                2631154   69.358    0.000  138.010    0.000 layers.py:30(reset)
              606444071  135.184    0.000  135.184    0.000 level.py:32(inverse)
                2704012  127.486    0.000  127.486    0.000 {built-in method addmm}
              160055468   86.356    0.000  125.327    0.000 allGraphs.py:46(p)
               10816048  123.888    0.000  123.888    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                 676003    5.409    0.000  121.553    0.000 agent.py:59(modify_board)
             1229874545  116.834    0.000  116.834    0.000 layer.py:91(positions)
              549436154  105.299    0.000  105.299    0.000 enum.py:352(<genexpr>)
               12631020   63.092    0.000  100.885    0.000 {built-in method _functools.reduce}
                4056018    3.953    0.000   90.173    0.000 activation.py:713(forward)
              161956989   64.845    0.000   88.110    0.000 layer.py:130(add)
                2631054   44.713    0.000   87.703    0.000 level.py:16(<dictcomp>)
                4056018    6.527    0.000   86.220    0.000 functional.py:1292(leaky_relu)
               67600300   54.212    0.000   85.561    0.000 layers.py:581(check)
              330756871   83.303    0.000   83.303    0.000 layer.py:146(elements)
              309609642   66.802    0.000   79.661    0.000 overrides.py:1083(<genexpr>)
                5408024   79.134    0.000   79.134    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                4056018   79.080    0.000   79.080    0.000 {built-in method torch._C._nn.leaky_relu}
                 676003   51.664    0.000   76.739    0.000 allGraphsTrain.py:38(<listcomp>)
                 676003   76.599    0.000   76.599    0.000 {built-in method torch._C._nn.one_hot}
                5408024   72.030    0.000   72.030    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                5408024   65.654    0.000   65.654    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                 676003   16.421    0.000   64.845    0.000 allGraphs.py:229(transform)
                5408024   59.810    0.000   59.810    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-13>
Subject: Job 9509264: <causal7_online_var_0> in cluster <dcc> Done

Job <causal7_online_var_0> was submitted from host <n-62-27-21> by user <s183905> in cluster <dcc> at Mon Apr 12 00:14:18 2021
Job was executed on host(s) <n-62-20-13>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Mon Apr 12 00:14:20 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Apr 12 00:14:20 2021
Terminated at Mon Apr 12 12:09:39 2021
Results reported at Mon Apr 12 12:09:39 2021

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

    CPU time :                                   42800.40 sec.
    Max Memory :                                 2077 MB
    Average Memory :                             2070.44 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14307.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   42937 sec.
    Turnaround time :                            42921 sec.

The output (if any) is above this job summary.


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-15>
Subject: Job 9509322: <causal7_online_var_0> in cluster <dcc> Exited

Job <causal7_online_var_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon Apr 12 04:00:46 2021
Job was executed on host(s) <n-62-20-15>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon Apr 12 04:00:48 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Apr 12 04:00:48 2021
Terminated at Mon Apr 12 15:56:00 2021
Results reported at Mon Apr 12 15:56:00 2021

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

Exited with exit code 120.

Resource usage summary:

    CPU time :                                   42800.67 sec.
    Max Memory :                                 2862 MB
    Average Memory :                             2599.17 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13522.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   42913 sec.
    Turnaround time :                            42914 sec.

The output (if any) is above this job summary.

