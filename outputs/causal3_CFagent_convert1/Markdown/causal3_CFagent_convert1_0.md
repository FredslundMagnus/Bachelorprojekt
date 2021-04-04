
# Parameters

    Name :                      causal3_CFagent_convert1-0
    Main :                      CFagent
    Level :                     Levels.Causal3
    Hours :                     13.0
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
    Cf convert :                0
    Minutes used :              775 minutes.
    Hours used :                12 hours.

# Profiling


      28068622300 function calls (27884431333 primitive calls) in 46519.90 seconds

##    Ordered by: cumulative time
   List reduced from 490 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 46519.900 46519.900 {built-in method builtins.exec}
                      1    4.644    4.644 46519.899 46519.899 <string>:1(<module>)
                      1  145.057  145.057 46515.256 46515.256 main.py:96(CFagent)
                6078345   22.748    0.000 18196.775    0.003 agent.py:28(learn)
                6078345  448.594    0.000 15199.504    0.003 learner.py:42(Qlearn)
                2026115   10.952    0.000 7654.144    0.004 game.py:36(step)
        206292099/22102823  854.394    0.000 7530.599    0.000 module.py:866(_call_impl)
                2026115   12.600    0.000 7193.499    0.004 layers.py:594(step)
               16024478   43.904    0.000 7051.716    0.000 network.py:24(forward)
                2026115  205.319    0.000 7015.577    0.003 agent.py:53(_learn)
               16024478  225.999    0.000 6904.387    0.000 container.py:117(forward)
                2026115  202.496    0.000 6503.997    0.003 agent.py:189(_learn)
                6078345   52.479    0.000 6385.657    0.001 optimizer.py:84(wrapper)
                6078345   28.257    0.000 6137.207    0.001 grad_mode.py:24(decorate_context)
                6078345  180.467    0.000 6050.075    0.001 adam.py:55(step)
                6078345 1238.799    0.000 5670.538    0.001 _functional.py:53(adam)
                2026115  425.350    0.000 4976.918    0.002 agent.py:197(counterfact)
                2026115  177.885    0.000 4909.082    0.002 layers.py:18(step)
              202425107  240.632    0.000 4714.398    0.000 layer.py:82(move)
                2026115   57.728    0.000 4642.205    0.002 agent.py:114(_learn)
                6078345   32.408    0.000 3918.913    0.001 tensor.py:195(backward)
                6078345   23.679    0.000 3885.528    0.001 __init__.py:68(backward)
                6078345 3726.221    0.001 3726.221    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                4971818  123.923    0.000 3566.851    0.001 agent.py:48(__call__)
                2026115 1889.804    0.001 3530.077    0.002 replaybuffer.py:28(teleporter_save_data)
                2026115 2324.364    0.001 3038.214    0.001 replaybuffer.py:22(sample_data)
                2026115 1506.978    0.001 2950.319    0.001 agent.py:85(interveen)
              202425107  440.781    0.000 2630.937    0.000 layers.py:611(check)
               28498653 2477.745    0.000 2477.745    0.000 {built-in method tensor}
               32048956   72.500    0.000 2476.551    0.000 conv.py:398(forward)
                2026115 1818.524    0.001 2455.045    0.001 replaybuffer.py:49(sample_data)
               32048956   42.529    0.000 2370.173    0.000 conv.py:390(_conv_forward)
               32048956 2327.644    0.000 2327.644    0.000 {built-in method conv2d}
               22872800   15.350    0.000 2304.982    0.000 game.py:32(board)
                2026116  211.967    0.000 2252.943    0.001 layers.py:565(update)
               44021204   91.904    0.000 2002.670    0.000 linear.py:93(forward)
               32417848 1062.235    0.000 1934.602    0.000 layer.py:143(NoRock_update)
               44021204   37.164    0.000 1867.046    0.000 functional.py:1737(linear)
               44021204 1820.642    0.000 1820.642    0.000 {built-in method torch._C._nn.linear}
              202324132  271.929    0.000 1632.949    0.000 layers.py:605(isFree)
                2026115  919.051    0.000 1542.048    0.001 agent.py:66(modify)
              115866084 1500.907    0.000 1500.907    0.000 {built-in method clone}
                 922085    9.632    0.000 1438.810    0.002 agent.py:167(choose_action)
             1318426648 1162.128    0.000 1361.019    0.000 layer.py:79(isFree)
              113462440 1157.574    0.000 1157.574    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               29285198 1155.053    0.000 1155.053    0.000 {built-in method cat}
               60045682   49.402    0.000 1104.133    0.000 activation.py:713(forward)
               60045682   50.061    0.000 1054.731    0.000 functional.py:1364(leaky_relu)
                2026115   35.634    0.000 1012.224    0.000 agent.py:163(__call__)
              113462440 1008.779    0.000 1008.779    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                6997933   49.002    0.000 1005.509    0.000 agent.py:58(modify_board)
               60045682  993.608    0.000  993.608    0.000 {built-in method torch._C._nn.leaky_relu}
                2026115   34.651    0.000  954.719    0.000 agent.py:109(__call__)
                6078345  146.475    0.000  891.109    0.000 optimizer.py:189(zero_grad)
               56731220  654.024    0.000  654.024    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                6997933  640.402    0.000  640.402    0.000 {built-in method torch._C._nn.one_hot}
              202425107  414.023    0.000  640.335    0.000 layers.py:303(check)
             2644869636  433.070    0.000  616.526    0.000 enum.py:646(__hash__)
              202425107  355.736    0.000  578.589    0.000 layers.py:262(check)
                2026115   48.623    0.000  571.559    0.000 replaybuffer.py:18(stacker)
               56731220  549.764    0.000  549.764    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               56731220  526.196    0.000  526.196    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               56731220  519.204    0.000  519.204    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              202611600   54.153    0.000  513.389    0.000 {built-in method builtins.all}
              573347689  504.643    0.000  504.643    0.000 layer.py:122(elements)
                2026115   47.269    0.000  497.582    0.000 replaybuffer.py:45(stacker)
                1689566   17.975    0.000  486.477    0.000 layers.py:615(restart)
              622265706  139.689    0.000  481.939    0.000 layers.py:571(<genexpr>)
                2026115  171.405    0.000  446.734    0.000 replaybuffer.py:55(CF_save_data)
                2026115  249.952    0.000  413.819    0.000 collector.py:54(collect)
               56731220  404.105    0.000  404.105    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                4971818  136.002    0.000  373.786    0.000 exploration.py:53(softmaxer)
              124890132  368.272    0.000  368.272    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              202425107  227.232    0.000  344.840    0.000 layers.py:329(check)
                1689566    9.331    0.000  332.697    0.000 level.py:8(__init__)
              397118624  266.756    0.000  329.335    0.000 tensor.py:906(grad)
              202611600  223.103    0.000  323.484    0.000 layers.py:111(isDone)
              202425107  198.498    0.000  306.724    0.000 layers.py:288(check)
                7431362  114.368    0.000  306.629    0.000 random.py:315(sample)
        3904482901/3904482898  258.546    0.000  298.075    0.000 {built-in method builtins.len}
             3490496709  297.563    0.000  297.563    0.000 layer.py:75(positions)
                6078345    8.704    0.000  294.126    0.000 loss.py:527(forward)
                6078345   21.916    0.000  285.421    0.000 functional.py:2898(mse_loss)
                6078346  269.631    0.000  269.631    0.000 {built-in method nonzero}
              202425107  183.208    0.000  268.695    0.000 layers.py:47(check)
                1689566   35.378    0.000  258.793    0.000 levels.py:164(generate)
                2948200   16.525    0.000  245.444    0.000 exploration.py:47(epsilonGreedy)
                 922085  197.159    0.000  243.185    0.000 agent.py:178(convert_values)
                6078345  188.846    0.000  188.846    0.000 {built-in method torch._C._nn.mse_loss}
             2644892963  183.460    0.000  183.460    0.000 {built-in method builtins.hash}
               32048956   22.748    0.000  181.162    0.000 flatten.py:39(forward)
                3379132   28.308    0.000  177.948    0.000 level.py:41(notUsed)
               12156690  174.170    0.000  174.170    0.000 {built-in method sum}
                6079136  167.240    0.000  167.240    0.000 {built-in method max}
                9026545   12.848    0.000  162.216    0.000 tensor.py:525(__rsub__)
               32048956  158.414    0.000  158.414    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              169105123  106.279    0.000  153.174    0.000 layer.py:102(remove)
              246242258  102.745    0.000  151.802    0.000 random.py:250(_randbelow_with_getrandbits)
                9026545  147.218    0.000  147.218    0.000 {built-in method rsub}
              254643532  102.964    0.000  142.970    0.000 layer.py:106(add)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-7>
Subject: Job 9493320: <causal3_CFagent_convert1_0> in cluster <dcc> Done

Job <causal3_CFagent_convert1_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Fri Apr  2 22:10:09 2021
Job was executed on host(s) <n-62-20-7>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sat Apr  3 11:06:47 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat Apr  3 11:06:47 2021
Terminated at Sun Apr  4 00:02:16 2021
Results reported at Sun Apr  4 00:02:16 2021

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

    CPU time :                                   46509.52 sec.
    Max Memory :                                 3571 MB
    Average Memory :                             3486.18 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               12813.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   46531 sec.
    Turnaround time :                            93127 sec.

The output (if any) is above this job summary.

