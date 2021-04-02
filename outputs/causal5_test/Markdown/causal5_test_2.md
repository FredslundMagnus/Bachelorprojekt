
# Parameters

    Name :                      causal5_test-2
    Main :                      teleport
    Level :                     Levels.Causal5
    Hours :                     6.0
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
    Minutes used :              358 minutes.
    Hours used :                5 hours.

# Profiling


      17050468535 function calls (16983189856 primitive calls) in 21483.43 seconds

##    Ordered by: cumulative time
   List reduced from 460 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 21483.426 21483.426 {built-in method builtins.exec}
                      1    1.910    1.910 21483.425 21483.425 <string>:1(<module>)
                      1   72.942   72.942 21481.515 21481.515 main.py:42(teleport)
                2403148   11.461    0.000 7158.934    0.003 agent.py:27(learn)
                2403148  174.569    0.000 5969.342    0.002 learner.py:42(Qlearn)
                1201574    6.498    0.000 5270.389    0.004 game.py:36(step)
                1201574    8.250    0.000 4972.025    0.004 layers.py:594(step)
                1201574   46.816    0.000 4313.310    0.004 agent.py:52(_learn)
                1201574  112.258    0.000 3341.819    0.003 layers.py:18(step)
              120157400  156.270    0.000 3218.470    0.000 layer.py:82(move)
        75687813/8410145  303.362    0.000 2925.421    0.000 module.py:715(_call_impl)
                1201574   38.758    0.000 2828.361    0.002 agent.py:113(_learn)
                6006997   15.449    0.000 2715.975    0.000 network.py:24(forward)
                6006997   72.212    0.000 2662.352    0.000 container.py:115(forward)
                1201574 1419.353    0.001 2494.379    0.002 replaybuffer.py:28(teleporter_save_data)
                2403148   18.629    0.000 2328.455    0.001 grad_mode.py:23(decorate_context)
                1201574 1702.966    0.001 2324.344    0.002 replaybuffer.py:22(sample_data)
                2403148   84.964    0.000 2277.531    0.001 adam.py:55(step)
                1201574 1097.030    0.001 1981.433    0.002 agent.py:84(interveen)
              120157400  306.324    0.000 1969.280    0.000 layers.py:611(check)
                2403148  426.995    0.000 1870.009    0.001 functional.py:53(adam)
                2402275   68.783    0.000 1840.970    0.001 agent.py:47(__call__)
                1201575  137.521    0.000 1608.571    0.001 layers.py:565(update)
                2403148   16.342    0.000 1471.728    0.001 tensor.py:181(backward)
                2403148   10.444    0.000 1455.386    0.001 __init__.py:68(backward)
                2403148 1383.965    0.001 1383.965    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                1201574  471.503    0.000 1010.044    0.001 agent.py:65(modify)
               12013994   20.965    0.000 1004.854    0.000 conv.py:422(forward)
               12013994   24.666    0.000  974.355    0.000 conv.py:414(_conv_forward)
               12013994  944.989    0.000  944.989    0.000 {built-in method conv2d}
              120157400  206.427    0.000  927.140    0.000 layers.py:605(isFree)
               82137370  860.001    0.000  860.001    0.000 {built-in method clone}
               15617843   35.358    0.000  839.334    0.000 linear.py:92(forward)
               10814175  473.894    0.000  834.366    0.000 layer.py:143(NoRock_update)
               15617843   57.085    0.000  786.527    0.000 functional.py:1669(linear)
             1011001608  598.550    0.000  720.713    0.000 layer.py:79(isFree)
               10813293  607.492    0.000  607.492    0.000 {built-in method cat}
                1201574   20.236    0.000  596.410    0.000 agent.py:108(__call__)
              151398378  344.453    0.000  572.202    0.000 tensor.py:933(grad)
                3603849   25.206    0.000  562.925    0.000 agent.py:57(modify_board)
               15617843  560.149    0.000  560.149    0.000 {built-in method addmm}
                1201574   26.272    0.000  520.399    0.000 replaybuffer.py:18(stacker)
                2403148   47.037    0.000  497.885    0.000 optimizer.py:167(zero_grad)
             1921453663  332.763    0.000  481.751    0.000 enum.py:646(__hash__)
                5371242  444.000    0.000  444.000    0.000 {built-in method tensor}
               43256664  374.501    0.000  374.501    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               21624840   22.038    0.000  369.029    0.000 activation.py:713(forward)
                3603849  368.832    0.000  368.832    0.000 {built-in method torch._C._nn.one_hot}
                2403148    3.872    0.000  348.328    0.000 game.py:32(board)
               21624840   28.521    0.000  346.992    0.000 functional.py:1292(leaky_relu)
              120157400  211.160    0.000  332.071    0.000 layers.py:371(check)
              126166324   37.284    0.000  331.102    0.000 {built-in method builtins.all}
              120157400  208.280    0.000  330.663    0.000 layers.py:357(check)
              120157400  202.859    0.000  321.338    0.000 layers.py:401(check)
              120157400  202.081    0.000  320.554    0.000 layers.py:415(check)
               21624840  315.727    0.000  315.727    0.000 {built-in method torch._C._nn.leaky_relu}
               43256664  304.159    0.000  304.159    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              367374344   88.282    0.000  303.612    0.000 layers.py:571(<genexpr>)
              194653227  100.251    0.000  303.335    0.000 overrides.py:1070(has_torch_function)
                 557755    7.729    0.000  263.163    0.000 layers.py:615(restart)
                6008824   32.007    0.000  260.378    0.000 tensor.py:21(wrapped)
               85741219  243.709    0.000  243.709    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
             2635973474  239.537    0.000  239.537    0.000 layer.py:75(positions)
              286771785  228.619    0.000  228.619    0.000 layer.py:122(elements)
                1201574  127.726    0.000  219.768    0.000 collector.py:54(collect)
               21628332  215.064    0.000  215.064    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                 557755    4.106    0.000  209.834    0.000 level.py:8(__init__)
               21628332  208.146    0.000  208.146    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              120157500  140.464    0.000  204.317    0.000 layers.py:111(isDone)
                1201628  201.753    0.000  201.755    0.000 {method 'to' of 'torch._C._TensorBase' objects}
                2402275   69.003    0.000  200.204    0.000 exploration.py:53(softmaxer)
              215077367   77.950    0.000  193.902    0.000 {built-in method builtins.any}
                      2    0.000    0.000  180.565   90.283 agent.py:14(__init__)
                      2    0.000    0.000  180.565   90.282 network.py:33(__init__)
                      1    0.000    0.000  180.556  180.556 agent.py:105(__init__)
                      6    0.000    0.000  179.511   29.918 module.py:529(to)
                   72/6    0.001    0.000  179.511   29.918 module.py:357(_apply)
                     54    0.000    0.000  179.509    3.324 module.py:607(convert)
               21628332  178.433    0.000  178.433    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              120157400  115.045    0.000  175.888    0.000 layers.py:344(check)
                 557755    9.772    0.000  174.684    0.000 levels.py:247(generate)
               21628332  156.295    0.000  156.295    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                3625878   31.839    0.000  154.994    0.000 level.py:41(notUsed)
              120157400  103.073    0.000  153.160    0.000 layers.py:388(check)
             1921462702  148.989    0.000  148.989    0.000 {built-in method builtins.hash}
                2403148    4.837    0.000  139.647    0.000 loss.py:445(forward)
                2403148   16.391    0.000  134.810    0.000 functional.py:2637(mse_loss)
               21628332  117.656    0.000  117.656    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
        1277801726/1277801724   83.626    0.000  116.266    0.000 {built-in method builtins.len}
              410932881   91.762    0.000  114.119    0.000 overrides.py:1083(<genexpr>)
               15617843  102.196    0.000  102.196    0.000 {method 't' of 'torch._C._TensorBase' objects}
                1201574    6.965    0.000  100.559    0.000 exploration.py:47(epsilonGreedy)
                1202054  100.307    0.000  100.307    0.000 {method 'ne' of 'torch._C._TensorBase' objects}
                1201574   37.509    0.000   98.651    0.000 random.py:315(sample)
             1011001608   93.346    0.000   93.346    0.000 layer.py:183(isBlocking)
              113380614   62.767    0.000   92.753    0.000 layer.py:102(remove)
                7209444   90.522    0.000   90.522    0.000 {built-in method sum}
              132832764   63.308    0.000   85.852    0.000 layer.py:106(add)
                3604722   18.895    0.000   83.242    0.000 tensor.py:506(__rsub__)
                2403148   77.293    0.000   77.293    0.000 {built-in method torch._C._nn.mse_loss}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-11>
Subject: Job 9492736: <causal5_test_2> in cluster <dcc> Done

Job <causal5_test_2> was submitted from host <n-62-27-19> by user <s183905> in cluster <dcc> at Fri Apr  2 14:23:06 2021
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Fri Apr  2 14:23:08 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Fri Apr  2 14:23:08 2021
Terminated at Fri Apr  2 20:23:44 2021
Results reported at Fri Apr  2 20:23:44 2021

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

    CPU time :                                   21256.66 sec.
    Max Memory :                                 2810 MB
    Average Memory :                             2754.84 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13574.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   21743 sec.
    Turnaround time :                            21638 sec.

The output (if any) is above this job summary.

