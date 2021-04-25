
# Parameters

    Name :                      MagicalLights2_convert4-2
    Main :                      CFagent
    Level :                     Levels.Causal4
    Failed actions chance :     0.0
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
    Counterfacts :              1
    Topn :                      1
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      69638934872 function calls (69331136517 primitive calls) in 86114.62 seconds

##    Ordered by: cumulative time
   List reduced from 514 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86114.616 86114.616 {built-in method builtins.exec}
                      1    4.251    4.251 86114.616 86114.616 <string>:1(<module>)
                      1  352.704  352.704 86110.365 86110.365 main.py:79(CFagent)
                9953541   34.764    0.000 29570.207    0.003 agent.py:29(learn)
                9953537  740.349    0.000 24666.116    0.002 learner.py:42(Qlearn)
                3317847   14.279    0.000 19057.175    0.006 game.py:41(step)
                3317847   20.182    0.000 18239.358    0.005 layers.py:718(step)
        344505872/36709208 1364.238    0.000 12591.273    0.000 module.py:866(_call_impl)
                3317847  271.938    0.000 12133.105    0.004 layers.py:17(step)
              331168896  883.769    0.000 11833.475    0.000 layer.py:98(move)
               26755671   71.849    0.000 11816.646    0.000 network.py:27(forward)
               26755671  361.775    0.000 11585.995    0.000 container.py:117(forward)
                3317847  338.390    0.000 11406.339    0.003 agent.py:54(_learn)
                3317847  337.517    0.000 10570.307    0.003 agent.py:202(_learn)
                9953537   84.320    0.000 10504.099    0.001 optimizer.py:84(wrapper)
                3317847  990.392    0.000 10433.996    0.003 agent.py:210(counterfact)
                9953537   41.672    0.000 10108.654    0.001 grad_mode.py:24(decorate_context)
                9953537  288.374    0.000 9971.294    0.001 adam.py:55(step)
                9953537 2040.088    0.000 9360.122    0.001 _functional.py:53(adam)
                3317847   98.545    0.000 7538.263    0.002 agent.py:117(_learn)
              331168896 1417.626    0.000 7325.145    0.000 layers.py:735(check)
                9953537   39.381    0.000 6113.586    0.001 tensor.py:195(backward)
                9953537   38.677    0.000 6072.678    0.001 __init__.py:68(backward)
                3317848  454.190    0.000 6059.938    0.002 layers.py:684(update)
                8395474  219.225    0.000 6005.813    0.001 agent.py:49(__call__)
                9953537 5814.156    0.001 5814.156    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3317847 4561.224    0.001 5631.735    0.002 replaybuffer.py:22(sample_data)
               52630075 5563.594    0.000 5563.594    0.000 {built-in method tensor}
                3317847 4417.650    0.001 5456.459    0.002 replaybuffer.py:67(sample_data)
               44993659   30.379    0.000 5343.610    0.000 game.py:37(board)
                3317847 2089.809    0.001 4448.796    0.001 agent.py:88(interveen)
               53511342  116.116    0.000 4200.271    0.000 conv.py:398(forward)
                3317847 2167.191    0.001 4072.960    0.001 replaybuffer.py:28(teleporter_save_data)
               53511342   73.210    0.000 4032.449    0.000 conv.py:390(_conv_forward)
               66356950 2346.512    0.000 4003.304    0.000 layer.py:151(update)
               53511342 3959.239    0.000 3959.239    0.000 {built-in method conv2d}
               73631319  150.800    0.000 3365.211    0.000 linear.py:93(forward)
               73631319   60.319    0.000 3144.085    0.000 functional.py:1737(linear)
               73631319 3069.040    0.000 3069.040    0.000 {built-in method torch._C._nn.linear}
              331168896  558.020    0.000 3034.074    0.000 layers.py:729(isFree)
                3317847 1891.657    0.001 2851.519    0.001 agent.py:67(modify)
                1770970   41.610    0.000 2740.009    0.002 agent.py:175(choose_action)
             2812532230 2003.170    0.000 2476.053    0.000 layer.py:95(isFree)
              185799352 1929.248    0.000 1929.248    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              100386990   79.653    0.000 1869.969    0.000 activation.py:713(forward)
              139970264 1854.597    0.000 1854.597    0.000 {built-in method clone}
               44891771 1841.226    0.000 1841.226    0.000 {built-in method cat}
              100386990   86.139    0.000 1790.316    0.000 functional.py:1364(leaky_relu)
              100386990 1687.507    0.000 1687.507    0.000 {built-in method torch._C._nn.leaky_relu}
               11713321   78.279    0.000 1685.044    0.000 agent.py:59(modify_board)
              185799352 1683.849    0.000 1683.849    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                3317843   58.004    0.000 1654.971    0.000 agent.py:171(__call__)
                3317847   57.463    0.000 1548.488    0.000 agent.py:112(__call__)
             6246028095 1049.083    0.000 1505.948    0.000 enum.py:646(__hash__)
                9953537  229.989    0.000 1446.386    0.000 optimizer.py:189(zero_grad)
                3317847 1090.128    0.000 1414.411    0.000 replaybuffer.py:73(CF_save_data)
              331694121  316.970    0.000 1378.514    0.000 {built-in method builtins.any}
              331168896  891.766    0.000 1192.968    0.000 layers.py:77(check)
                3408527   38.453    0.000 1166.284    0.000 layers.py:740(restart)
               11713321 1071.309    0.000 1071.309    0.000 {built-in method torch._C._nn.one_hot}
             3612139003  877.043    0.000 1061.544    0.000 layers.py:700(<genexpr>)
               92899676 1050.132    0.000 1050.132    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              331168896  652.255    0.000 1023.093    0.000 layers.py:246(check)
              331168896  579.424    0.000  952.439    0.000 layers.py:286(check)
             1114119191  921.375    0.000  921.375    0.000 layer.py:146(elements)
               92899676  905.387    0.000  905.387    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               92899676  869.097    0.000  869.097    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               92899676  853.853    0.000  853.853    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                3317847   61.338    0.000  838.504    0.000 replaybuffer.py:18(stacker)
                3408527   18.314    0.000  820.086    0.000 level.py:8(__init__)
              331784800  142.964    0.000  817.011    0.000 {built-in method builtins.all}
                3317843   63.631    0.000  813.760    0.000 replaybuffer.py:63(stacker)
             8101690352  736.161    0.000  736.161    0.000 layer.py:91(positions)
             1716955734  425.752    0.000  710.767    0.000 layers.py:690(<genexpr>)
                3317847  411.500    0.000  683.049    0.000 collector.py:46(collect)
               92899676  670.501    0.000  670.501    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                3408527  105.406    0.000  659.195    0.000 levels.py:199(generate)
              331168896  494.929    0.000  637.212    0.000 layers.py:62(check)
        8836056624/8836056621  555.409    0.000  618.770    0.000 {built-in method builtins.len}
                8395474  226.339    0.000  614.977    0.000 exploration.py:53(softmaxer)
                1770970  469.323    0.000  556.420    0.000 agent.py:186(convert_values)
              331168896  350.504    0.000  546.534    0.000 layers.py:313(check)
              650297816  430.759    0.000  531.798    0.000 tensor.py:906(grad)
               13452748  187.571    0.000  494.572    0.000 random.py:315(sample)
              331168896  308.069    0.000  489.599    0.000 layers.py:273(check)
                9953537   14.380    0.000  479.795    0.000 loss.py:527(forward)
              155001428  478.137    0.000  478.137    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                9953537   38.375    0.000  465.415    0.000 functional.py:2898(mse_loss)
             6246065870  456.872    0.000  456.872    0.000 {built-in method builtins.hash}
                6817054   52.827    0.000  450.393    0.000 level.py:41(notUsed)
              331168896  289.739    0.000  434.193    0.000 layers.py:48(check)
              331168896  225.548    0.000  332.370    0.000 layers.py:23(check)
                9953537  308.424    0.000  308.424    0.000 {built-in method torch._C._nn.mse_loss}
               53511342   34.663    0.000  305.773    0.000 flatten.py:39(forward)
               34085270   44.736    0.000  297.132    0.000 layer.py:69(restart)
               19907082  290.942    0.000  290.942    0.000 {built-in method sum}
                6635696  281.340    0.000  281.340    0.000 {built-in method nonzero}
              287094777  204.819    0.000  279.833    0.000 layer.py:126(remove)
             3657017088  272.519    0.000  272.519    0.000 {method 'random' of '_random.Random' objects}
               53511342  271.110    0.000  271.110    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9571373: <MagicalLights2_convert4_2> in cluster <dcc> Done

Job <MagicalLights2_convert4_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sat Apr 24 18:36:26 2021
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sat Apr 24 18:48:48 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat Apr 24 18:48:48 2021
Terminated at Sun Apr 25 18:44:09 2021
Results reported at Sun Apr 25 18:44:09 2021

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

    CPU time :                                   85901.66 sec.
    Max Memory :                                 9742 MB
    Average Memory :                             6543.34 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               6642.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86124 sec.
    Turnaround time :                            86863 sec.

The output (if any) is above this job summary.

