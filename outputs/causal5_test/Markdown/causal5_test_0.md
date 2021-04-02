
# Parameters

    Name :                      causal5_test-0
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


      16229758382 function calls (16165500799 primitive calls) in 21483.63 seconds

##    Ordered by: cumulative time
   List reduced from 459 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 21483.632 21483.632 {built-in method builtins.exec}
                      1    1.853    1.853 21483.631 21483.631 <string>:1(<module>)
                      1   78.776   78.776 21481.779 21481.779 main.py:42(teleport)
                2295268   12.785    0.000 7346.114    0.003 agent.py:27(learn)
                2295268  186.922    0.000 6066.929    0.003 learner.py:42(Qlearn)
                1147634    7.377    0.000 5146.106    0.004 game.py:36(step)
                1147634    8.322    0.000 4834.243    0.004 layers.py:594(step)
                1147634   52.521    0.000 4431.869    0.004 agent.py:52(_learn)
                1147634  110.587    0.000 3266.696    0.003 layers.py:18(step)
              114763400  153.167    0.000 3145.571    0.000 layer.py:82(move)
        72289099/8032527  313.750    0.000 3067.651    0.000 module.py:715(_call_impl)
                1147634   42.371    0.000 2895.608    0.003 agent.py:113(_learn)
                5737259   18.950    0.000 2839.319    0.000 network.py:24(forward)
                5737259   79.966    0.000 2778.190    0.000 container.py:115(forward)
                1147634 1725.450    0.002 2353.939    0.002 replaybuffer.py:22(sample_data)
                1147634 1328.929    0.001 2336.074    0.002 replaybuffer.py:28(teleporter_save_data)
                2295268   19.964    0.000 2310.152    0.001 grad_mode.py:23(decorate_context)
                2295268   85.760    0.000 2253.788    0.001 adam.py:55(step)
                1147634 1042.809    0.001 1966.180    0.002 agent.py:84(interveen)
                2294357   73.325    0.000 1953.829    0.001 agent.py:47(__call__)
              114763400  290.358    0.000 1929.290    0.000 layers.py:611(check)
                2295268  419.597    0.000 1847.065    0.001 functional.py:53(adam)
                1147635  133.426    0.000 1545.247    0.001 layers.py:565(update)
                2295268   17.194    0.000 1520.199    0.001 tensor.py:181(backward)
                2295268   11.801    0.000 1503.005    0.001 __init__.py:68(backward)
                2295268 1423.745    0.001 1423.745    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               11474518   22.371    0.000 1064.109    0.000 conv.py:422(forward)
                1147634  483.676    0.000 1058.277    0.001 agent.py:65(modify)
               11474518   27.873    0.000 1031.462    0.000 conv.py:414(_conv_forward)
               11474518  999.011    0.000  999.011    0.000 {built-in method conv2d}
              114763400  195.171    0.000  902.036    0.000 layers.py:605(isFree)
               14916509   37.119    0.000  879.644    0.000 linear.py:92(forward)
               14916509   60.499    0.000  823.629    0.000 functional.py:1669(linear)
               10328715  460.060    0.000  810.850    0.000 layer.py:143(NoRock_update)
               75400180  809.386    0.000  809.386    0.000 {built-in method clone}
              971377864  595.970    0.000  706.864    0.000 layer.py:79(isFree)
               10327795  615.989    0.000  615.989    0.000 {built-in method cat}
                1147634   22.280    0.000  615.424    0.001 agent.py:108(__call__)
                3441991   30.555    0.000  603.450    0.000 agent.py:57(modify_board)
               14916509  587.425    0.000  587.425    0.000 {built-in method addmm}
              144601938  340.902    0.000  563.471    0.000 tensor.py:933(grad)
                1147634   27.373    0.000  524.510    0.000 replaybuffer.py:18(stacker)
                2295268   46.119    0.000  484.405    0.000 optimizer.py:167(zero_grad)
             1825494738  328.501    0.000  472.750    0.000 enum.py:646(__hash__)
                5144566  463.446    0.000  463.446    0.000 {built-in method tensor}
                3441991  392.454    0.000  392.454    0.000 {built-in method torch._C._nn.one_hot}
               41314824  370.965    0.000  370.965    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               20653768   19.692    0.000  370.608    0.000 activation.py:713(forward)
                2295268    4.760    0.000  365.526    0.000 game.py:32(board)
               20653768   32.602    0.000  350.915    0.000 functional.py:1292(leaky_relu)
              114763400  204.832    0.000  329.016    0.000 layers.py:371(check)
              114763400  206.827    0.000  327.893    0.000 layers.py:357(check)
              120502584   36.980    0.000  320.201    0.000 {built-in method builtins.all}
              114763400  201.051    0.000  317.613    0.000 layers.py:415(check)
              114763400  200.260    0.000  315.883    0.000 layers.py:401(check)
               20653768  315.430    0.000  315.430    0.000 {built-in method torch._C._nn.leaky_relu}
               41314824  300.312    0.000  300.312    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              185914804  100.949    0.000  300.231    0.000 overrides.py:1070(has_torch_function)
              350483776   83.536    0.000  292.488    0.000 layers.py:571(<genexpr>)
                5739084   35.470    0.000  268.871    0.000 tensor.py:21(wrapped)
                 487330    7.093    0.000  238.761    0.000 layers.py:615(restart)
               78842171  227.282    0.000  227.282    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              271875646  224.293    0.000  224.293    0.000 layer.py:122(elements)
             2518268986  222.998    0.000  222.998    0.000 layer.py:75(positions)
                1147634  127.165    0.000  220.714    0.000 collector.py:54(collect)
                2294357   74.309    0.000  216.436    0.000 exploration.py:53(softmaxer)
               20657412  213.318    0.000  213.318    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                1147688  204.131    0.000  204.134    0.000 {method 'to' of 'torch._C._TensorBase' objects}
               20657412  202.432    0.000  202.432    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              114763500  136.443    0.000  198.552    0.000 layers.py:111(isDone)
              205421850   77.294    0.000  190.545    0.000 {built-in method builtins.any}
                 487330    4.132    0.000  190.395    0.000 level.py:8(__init__)
                      2    0.000    0.000  180.878   90.439 agent.py:14(__init__)
                      2    0.000    0.000  180.878   90.439 network.py:33(__init__)
                      1    0.000    0.000  180.869  180.869 agent.py:105(__init__)
                      6    0.000    0.000  179.824   29.971 module.py:529(to)
                   72/6    0.000    0.000  179.824   29.971 module.py:357(_apply)
                     54    0.000    0.000  179.822    3.330 module.py:607(convert)
               20657412  175.622    0.000  175.622    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              114763400  113.663    0.000  168.302    0.000 layers.py:344(check)
               20657412  157.581    0.000  157.581    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                 487330    9.013    0.000  157.179    0.000 levels.py:247(generate)
              114763400  103.730    0.000  152.555    0.000 layers.py:388(check)
                2295268    5.557    0.000  151.003    0.000 loss.py:445(forward)
                2295268   18.493    0.000  145.446    0.000 functional.py:2637(mse_loss)
             1825503345  144.250    0.000  144.250    0.000 {built-in method builtins.hash}
                3167588   28.700    0.000  139.100    0.000 level.py:41(notUsed)
        1220748389/1220748387   82.833    0.000  117.990    0.000 {built-in method builtins.len}
               20657412  111.708    0.000  111.708    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              392484972   88.897    0.000  111.514    0.000 overrides.py:1083(<genexpr>)
               14916509  106.363    0.000  106.363    0.000 {method 't' of 'torch._C._TensorBase' objects}
                1147634    7.414    0.000  104.412    0.000 exploration.py:47(epsilonGreedy)
                1148092  101.549    0.000  101.549    0.000 {method 'ne' of 'torch._C._TensorBase' objects}
                1147634   40.109    0.000  101.520    0.000 random.py:315(sample)
                6885804   93.153    0.000   93.153    0.000 {built-in method sum}
              971377864   92.359    0.000   92.359    0.000 layer.py:183(isBlocking)
                3442902   24.003    0.000   92.024    0.000 tensor.py:506(__rsub__)
              108857724   60.037    0.000   89.345    0.000 layer.py:102(remove)
              125842156   60.488    0.000   83.243    0.000 layer.py:106(add)
                2295268   82.841    0.000   82.841    0.000 {built-in method torch._C._nn.mse_loss}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-12>
Subject: Job 9492734: <causal5_test_0> in cluster <dcc> Done

Job <causal5_test_0> was submitted from host <n-62-27-19> by user <s183905> in cluster <dcc> at Fri Apr  2 14:23:06 2021
Job was executed on host(s) <n-62-20-12>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Fri Apr  2 14:23:06 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Fri Apr  2 14:23:06 2021
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

    CPU time :                                   21254.39 sec.
    Max Memory :                                 2810 MB
    Average Memory :                             2756.58 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13574.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   21743 sec.
    Turnaround time :                            21638 sec.

The output (if any) is above this job summary.

