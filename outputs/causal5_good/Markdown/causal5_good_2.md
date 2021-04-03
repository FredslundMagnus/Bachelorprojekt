
# Parameters

    Name :                      causal5_good-2
    Main :                      teleport
    Level :                     Levels.Causal5
    Hours :                     20.0
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
    Layer pink1 :               True
    Layer pink2 :               True
    Layer pink3 :               True
    Layer brown1 :              True
    Layer brown2 :              True
    Layer brown3 :              True
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Minutes used :              1197 minutes.
    Hours used :                19 hours.

# Profiling


      60264828523 function calls (60048351892 primitive calls) in 71879.38 seconds

##    Ordered by: cumulative time
   List reduced from 459 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 71879.384 71879.384 {built-in method builtins.exec}
                      1    1.887    1.887 71879.383 71879.383 <string>:1(<module>)
                      1  179.144  179.144 71877.496 71877.496 main.py:42(teleport)
                7731972   28.230    0.000 22349.840    0.003 agent.py:27(learn)
                7731972  529.303    0.000 18813.209    0.002 learner.py:42(Qlearn)
                3865986   15.395    0.000 17944.076    0.005 game.py:36(step)
                3865986   22.496    0.000 17053.853    0.004 layers.py:594(step)
                3865986  131.345    0.000 13511.680    0.003 agent.py:52(_learn)
                3865986 6520.085    0.002 11830.957    0.003 replaybuffer.py:28(teleporter_save_data)
                3865986  309.102    0.000 10750.703    0.003 layers.py:18(step)
              386598600  514.453    0.000 10404.278    0.000 layer.py:82(move)
        243535889/27060269  947.801    0.000 9309.996    0.000 module.py:715(_call_impl)
                3865986  107.653    0.000 8794.247    0.002 agent.py:113(_learn)
               19328297   50.374    0.000 8687.214    0.000 network.py:24(forward)
               19328297  228.297    0.000 8514.857    0.000 container.py:115(forward)
                3865986 5007.217    0.001 7856.188    0.002 agent.py:84(interveen)
                7731972   50.091    0.000 7535.846    0.001 grad_mode.py:23(decorate_context)
                7731972  254.523    0.000 7397.542    0.001 adam.py:55(step)
              386598600 1058.521    0.000 6606.479    0.000 layers.py:611(check)
                3865987  425.596    0.000 6253.377    0.002 layers.py:565(update)
                7731972 1357.953    0.000 6052.403    0.001 functional.py:53(adam)
                7730339  171.712    0.000 5739.923    0.001 agent.py:47(__call__)
                3865986 3363.902    0.001 5313.788    0.001 replaybuffer.py:22(sample_data)
                7731972   45.781    0.000 4415.558    0.001 tensor.py:181(backward)
                7731972   26.518    0.000 4369.777    0.001 __init__.py:68(backward)
              393009750 4217.691    0.000 4217.691    0.000 {built-in method clone}
                7731972 4161.088    0.001 4161.088    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3865986 1559.091    0.000 3205.009    0.001 agent.py:65(modify)
               38656594   70.296    0.000 3140.490    0.000 conv.py:422(forward)
               38656594   77.174    0.000 3042.145    0.000 conv.py:414(_conv_forward)
               38656594 2950.736    0.000 2950.736    0.000 {built-in method conv2d}
              386598600  747.013    0.000 2762.242    0.000 layers.py:605(isFree)
               50252919  117.493    0.000 2734.319    0.000 linear.py:92(forward)
               50252919  195.423    0.000 2562.153    0.000 functional.py:1669(linear)
               34793883 1318.837    0.000 2318.745    0.000 layer.py:143(NoRock_update)
                5029184   55.981    0.000 2272.217    0.000 layers.py:615(restart)
             3372791080 1606.687    0.000 2015.229    0.000 layer.py:79(isFree)
              487114290 1168.106    0.000 1948.504    0.000 tensor.py:933(grad)
               34792241 1945.565    0.000 1945.565    0.000 {built-in method cat}
                5029184   25.791    0.000 1821.801    0.000 level.py:8(__init__)
                3865986   49.438    0.000 1814.386    0.000 agent.py:108(__call__)
               50252919 1802.757    0.000 1802.757    0.000 {built-in method addmm}
             6872812142 1226.478    0.000 1787.441    0.000 enum.py:646(__hash__)
               11596325   76.165    0.000 1723.921    0.000 agent.py:57(modify_board)
                7731972  155.628    0.000 1670.363    0.000 optimizer.py:167(zero_grad)
                3865986   72.303    0.000 1655.210    0.000 replaybuffer.py:18(stacker)
                5029184   83.079    0.000 1608.757    0.000 levels.py:247(generate)
               32693782  286.440    0.000 1439.915    0.000 level.py:41(notUsed)
               16571893 1276.573    0.000 1276.573    0.000 {built-in method tensor}
              139175496 1227.310    0.000 1227.310    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               69581216   60.913    0.000 1198.762    0.000 activation.py:713(forward)
              404606075 1168.949    0.000 1168.949    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               69581216  102.520    0.000 1137.849    0.000 functional.py:1292(leaky_relu)
              386598600  695.440    0.000 1110.969    0.000 layers.py:371(check)
               11596325 1109.220    0.000 1109.220    0.000 {built-in method torch._C._nn.one_hot}
              386598600  684.269    0.000 1107.015    0.000 layers.py:357(check)
              405930706  133.740    0.000 1105.552    0.000 {built-in method builtins.all}
              386598600  654.732    0.000 1064.532    0.000 layers.py:415(check)
              386598600  657.313    0.000 1063.776    0.000 layers.py:401(check)
              626286280  347.390    0.000 1049.137    0.000 overrides.py:1070(has_torch_function)
               69581216 1025.697    0.000 1025.697    0.000 {built-in method torch._C._nn.leaky_relu}
                7731972   10.150    0.000 1012.279    0.000 game.py:32(board)
             1204107488  298.911    0.000 1005.098    0.000 layers.py:571(<genexpr>)
              139175496 1003.936    0.000 1003.936    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
             8502452586  812.725    0.000  812.725    0.000 layer.py:75(positions)
               19332006  105.076    0.000  769.996    0.000 tensor.py:21(wrapped)
                3865986  420.725    0.000  721.024    0.000 collector.py:54(collect)
               69587748  709.967    0.000  709.967    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              692003144  270.825    0.000  670.066    0.000 {built-in method builtins.any}
              386598700  445.476    0.000  664.762    0.000 layers.py:111(isDone)
               69587748  655.921    0.000  655.921    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                7730339  220.478    0.000  597.291    0.000 exploration.py:53(softmaxer)
             1198415251  593.415    0.000  593.415    0.000 layer.py:122(elements)
              386598600  384.407    0.000  583.987    0.000 layers.py:344(check)
               32693782   24.494    0.000  581.296    0.000 level.py:38(elementsIn)
               69587748  574.227    0.000  574.227    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
             6872840333  560.968    0.000  560.968    0.000 {built-in method builtins.hash}
              386598600  345.851    0.000  520.117    0.000 layers.py:388(check)
               69587748  503.557    0.000  503.557    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                7731972   13.648    0.000  403.635    0.000 loss.py:445(forward)
             1322156712  317.505    0.000  393.217    0.000 overrides.py:1083(<genexpr>)
        4079119202/4079119200  281.864    0.000  392.999    0.000 {built-in method builtins.len}
             1541943042  391.442    0.000  391.442    0.000 level.py:32(inverse)
                7731972   44.947    0.000  389.986    0.000 functional.py:2637(mse_loss)
               69587748  379.085    0.000  379.085    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               45262656   37.204    0.000  378.700    0.000 layer.py:56(restart)
               32693782  181.362    0.000  363.957    0.000 level.py:39(<listcomp>)
             3372791080  339.696    0.000  339.696    0.000 layer.py:183(isBlocking)
              566904930  246.295    0.000  338.966    0.000 layer.py:106(add)
               50252919  329.513    0.000  329.513    0.000 {method 't' of 'torch._C._TensorBase' objects}
              393668899  202.326    0.000  301.272    0.000 layer.py:102(remove)
               23195916  289.102    0.000  289.102    0.000 {built-in method sum}
                3865986  105.922    0.000  287.418    0.000 random.py:315(sample)
                5029284  137.515    0.000  274.972    0.000 layers.py:33(reset)
                3867532  265.909    0.000  265.909    0.000 {method 'ne' of 'torch._C._TensorBase' objects}
               11597958   55.396    0.000  244.103    0.000 tensor.py:506(__rsub__)
                3866040  243.448    0.000  243.449    0.000 {method 'to' of 'torch._C._TensorBase' objects}
                7731972  223.498    0.000  223.498    0.000 {built-in method torch._C._nn.mse_loss}
               38656594   28.560    0.000  219.123    0.000 flatten.py:39(forward)
               11597958  218.398    0.000  218.398    0.000 {method 'eq' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-14>
Subject: Job 9492739: <causal5_good_2> in cluster <dcc> Done

Job <causal5_good_2> was submitted from host <n-62-27-19> by user <s183905> in cluster <dcc> at Fri Apr  2 14:23:06 2021
Job was executed on host(s) <n-62-20-14>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Fri Apr  2 14:23:08 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Fri Apr  2 14:23:08 2021
Terminated at Sat Apr  3 10:23:38 2021
Results reported at Sat Apr  3 10:23:38 2021

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

    CPU time :                                   71477.63 sec.
    Max Memory :                                 2812 MB
    Average Memory :                             2795.30 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13572.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   72137 sec.
    Turnaround time :                            72032 sec.

The output (if any) is above this job summary.

