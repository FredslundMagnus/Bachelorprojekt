
# Parameters

    Name :                      causal4_CF_convert4_2-0
    Main :                      CFagent
    Level :                     Levels.Causal4
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
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                4
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      69273396624 function calls (68907405109 primitive calls) in 86109.31 seconds

##    Ordered by: cumulative time
   List reduced from 508 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86109.309 86109.309 {built-in method builtins.exec}
                      1    4.806    4.806 86109.309 86109.309 <string>:1(<module>)
                      1  268.908  268.908 86104.503 86104.503 main.py:96(CFagent)
               11723607   44.796    0.000 26932.358    0.002 agent.py:29(learn)
               11723600  678.080    0.000 21838.284    0.002 learner.py:42(Qlearn)
                3907869   18.993    0.000 20295.352    0.005 game.py:35(step)
                3907869   20.365    0.000 19417.502    0.005 layers.py:448(step)
                3907869  337.450    0.000 13164.464    0.003 layers.py:17(step)
              390698121  933.965    0.000 12795.135    0.000 layer.py:84(move)
        409515199/43525375 1530.791    0.000 12551.455    0.000 module.py:866(_call_impl)
                3907869 1022.915    0.000 12008.670    0.003 agent.py:204(counterfact)
               31801775   80.553    0.000 11742.751    0.000 network.py:24(forward)
               31801775  374.615    0.000 11465.951    0.000 container.py:117(forward)
                3907869  410.455    0.000 10483.582    0.003 agent.py:54(_learn)
                3907869  407.402    0.000 9611.106    0.002 agent.py:196(_learn)
               11723600   89.845    0.000 8519.952    0.001 optimizer.py:84(wrapper)
               11723600   48.360    0.000 8106.991    0.001 grad_mode.py:24(decorate_context)
               11723600  334.453    0.000 7954.044    0.001 adam.py:55(step)
              390698121 1189.801    0.000 7368.423    0.000 layers.py:465(check)
               11723600 1651.615    0.000 7245.016    0.001 _functional.py:53(adam)
                3907869  117.292    0.000 6769.507    0.002 agent.py:115(_learn)
               62504228 6264.334    0.000 6264.334    0.000 {built-in method tensor}
                3907870  408.437    0.000 6196.758    0.002 layers.py:419(update)
               10035063  258.627    0.000 6097.132    0.001 agent.py:49(__call__)
               53565752   31.742    0.000 6060.784    0.000 game.py:31(board)
                3907869 4675.323    0.001 5957.705    0.002 replaybuffer.py:22(sample_data)
               11723600   45.258    0.000 5669.003    0.000 tensor.py:195(backward)
               11723600   41.778    0.000 5622.168    0.000 __init__.py:68(backward)
               11723600 5366.203    0.000 5366.203    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3907869 2940.587    0.001 5157.235    0.001 replaybuffer.py:28(teleporter_save_data)
               78157390 3038.750    0.000 5147.617    0.000 layer.py:129(update)
                3907869 4027.916    0.001 5143.117    0.001 replaybuffer.py:49(sample_data)
                3907869 2179.935    0.001 4528.744    0.001 agent.py:86(interveen)
               63603550  129.162    0.000 4282.984    0.000 conv.py:398(forward)
               63603550   85.597    0.000 4089.675    0.000 conv.py:390(_conv_forward)
               63603550 4004.078    0.000 4004.078    0.000 {built-in method conv2d}
              390665113  690.470    0.000 3840.009    0.000 layers.py:459(isFree)
               87589587  164.992    0.000 3225.809    0.000 linear.py:93(forward)
             3396063623 2625.233    0.000 3149.540    0.000 layer.py:81(isFree)
               87589587   67.471    0.000 2976.188    0.000 functional.py:1737(linear)
                2227381   44.238    0.000 2914.886    0.001 agent.py:168(choose_action)
               87589587 2892.063    0.000 2892.063    0.000 {built-in method torch._C._nn.linear}
                3907869 1436.436    0.000 2410.514    0.001 agent.py:67(modify)
              231001828 2138.761    0.000 2138.761    0.000 {built-in method clone}
               56929456 2001.673    0.000 2001.673    0.000 {built-in method cat}
               13942932   86.980    0.000 1711.690    0.000 agent.py:59(modify_board)
              119391362   90.632    0.000 1709.992    0.000 activation.py:713(forward)
                3907862   70.634    0.000 1648.497    0.000 agent.py:164(__call__)
             6833938160 1139.732    0.000 1635.841    0.000 enum.py:646(__hash__)
              119391362   92.558    0.000 1619.361    0.000 functional.py:1364(leaky_relu)
                3907869   64.087    0.000 1561.172    0.000 agent.py:110(__call__)
              119391362 1508.638    0.000 1508.638    0.000 {built-in method torch._C._nn.leaky_relu}
              390787000  197.722    0.000 1487.542    0.000 {built-in method builtins.all}
                4443948   51.730    0.000 1423.778    0.000 layers.py:469(restart)
              218840524 1412.410    0.000 1412.410    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              390698121  866.445    0.000 1347.450    0.000 layers.py:233(check)
             2385358925  561.701    0.000 1334.009    0.000 layers.py:425(<genexpr>)
              218840524 1254.281    0.000 1254.281    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               11723600  219.346    0.000 1248.251    0.000 optimizer.py:189(zero_grad)
             1443811168 1220.290    0.000 1220.290    0.000 layer.py:124(elements)
              390698121  708.964    0.000 1176.836    0.000 layers.py:270(check)
               13942932 1128.367    0.000 1128.367    0.000 {built-in method torch._C._nn.one_hot}
              390698121  845.715    0.000 1090.842    0.000 layers.py:67(check)
                3907869   81.286    0.000 1012.083    0.000 replaybuffer.py:18(stacker)
                4443948   24.575    0.000  963.420    0.000 level.py:8(__init__)
                3907862   74.170    0.000  853.548    0.000 replaybuffer.py:45(stacker)
                3907869  361.817    0.000  845.331    0.000 replaybuffer.py:55(CF_save_data)
              109420262  832.326    0.000  832.326    0.000 {method 'add' of 'torch._C._TensorBase' objects}
             9339174810  812.623    0.000  812.623    0.000 layer.py:77(positions)
                4443948  140.120    0.000  788.764    0.000 levels.py:199(generate)
              390698121  590.774    0.000  777.065    0.000 layers.py:56(check)
              109420262  735.648    0.000  735.648    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              109420262  666.935    0.000  666.935    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              109420262  664.350    0.000  664.350    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              390787000  448.686    0.000  656.412    0.000 layers.py:100(isDone)
        9586857134/9586857131  573.599    0.000  642.406    0.000 {built-in method builtins.len}
               10035063  223.494    0.000  610.568    0.000 exploration.py:53(softmaxer)
              390698121  389.230    0.000  605.109    0.000 layers.py:257(check)
                2227381  515.101    0.000  603.223    0.000 agent.py:179(convert_values)
               16703634  222.755    0.000  582.706    0.000 random.py:315(sample)
              765941918  464.383    0.000  578.746    0.000 tensor.py:906(grad)
              390698121  362.209    0.000  570.521    0.000 layers.py:294(check)
                3907869  330.736    0.000  562.722    0.000 collector.py:54(collect)
                8887896   61.727    0.000  514.642    0.000 level.py:41(notUsed)
              390698121  349.230    0.000  513.344    0.000 layers.py:42(check)
              109420262  505.657    0.000  505.657    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
             6833982543  496.117    0.000  496.117    0.000 {built-in method builtins.hash}
               11723600   16.030    0.000  471.472    0.000 loss.py:527(forward)
              248852622  458.283    0.000  458.283    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               11723600   41.053    0.000  455.442    0.000 functional.py:2898(mse_loss)
               11723608  443.485    0.000  443.485    0.000 {built-in method nonzero}
               44439480   60.283    0.000  394.882    0.000 layer.py:58(restart)
              397279848  252.216    0.000  362.315    0.000 layer.py:104(remove)
              645469769  259.984    0.000  351.496    0.000 layer.py:108(add)
              508230350  215.260    0.000  317.009    0.000 random.py:250(_randbelow_with_getrandbits)
               78157390  301.843    0.000  301.843    0.000 layer.py:141(<listcomp>)
               63603550   42.829    0.000  283.630    0.000 flatten.py:39(forward)
               11723600  279.839    0.000  279.839    0.000 {built-in method torch._C._nn.mse_loss}
             2723224377  276.071    0.000  276.071    0.000 layer.py:181(isBlocking)
               11724993  257.691    0.000  257.691    0.000 {built-in method max}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-4>
Subject: Job 9496009: <causal4_CF_convert4_2_0> in cluster <dcc> Done

Job <causal4_CF_convert4_2_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon Apr  5 20:00:35 2021
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Tue Apr  6 02:45:54 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue Apr  6 02:45:54 2021
Terminated at Wed Apr  7 02:41:10 2021
Results reported at Wed Apr  7 02:41:10 2021

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

    CPU time :                                   85905.88 sec.
    Max Memory :                                 10812 MB
    Average Memory :                             7172.70 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               5572.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86117 sec.
    Turnaround time :                            110435 sec.

The output (if any) is above this job summary.

