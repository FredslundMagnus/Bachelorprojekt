
# Parameters

    Name :                      NOBUGcausal3_CFagent_convert1-0
    Main :                      CFagent
    Level :                     Levels.Causal3
    Hours :                     16.0
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
    Cf convert :                1
    Minutes used :              955 minutes.
    Hours used :                15 hours.

# Profiling


      36186144854 function calls (35973929235 primitive calls) in 57321.00 seconds

##    Ordered by: cumulative time
   List reduced from 489 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 57320.998 57320.998 {built-in method builtins.exec}
                      1    4.616    4.616 57320.998 57320.998 <string>:1(<module>)
                      1  163.955  163.955 57316.382 57316.382 main.py:96(CFagent)
                6521625   24.302    0.000 19520.320    0.003 agent.py:28(learn)
                6521614  486.294    0.000 16242.566    0.002 learner.py:42(Qlearn)
                2173875   11.764    0.000 9899.304    0.005 game.py:36(step)
                2173875   14.015    0.000 9397.699    0.004 layers.py:594(step)
        237144661/24930733  963.651    0.000 8709.064    0.000 module.py:866(_call_impl)
               18409119   49.776    0.000 8187.066    0.000 network.py:24(forward)
               18409119  252.114    0.000 8020.716    0.000 container.py:117(forward)
                2173875  233.120    0.000 7538.860    0.003 agent.py:53(_learn)
                2173875 1274.027    0.001 7415.246    0.003 agent.py:199(counterfact)
                2173875  231.294    0.000 6983.516    0.003 agent.py:191(_learn)
                6521614   56.605    0.000 6835.412    0.001 optimizer.py:84(wrapper)
                6521614   30.877    0.000 6567.990    0.001 grad_mode.py:24(decorate_context)
                6521614  193.202    0.000 6474.348    0.001 adam.py:55(step)
                6521614 1343.065    0.000 6070.225    0.001 _functional.py:53(adam)
                2173875 3074.337    0.001 5714.714    0.003 replaybuffer.py:28(teleporter_save_data)
                2173875  189.290    0.000 5474.831    0.003 layers.py:18(step)
              217387489  264.043    0.000 5267.310    0.000 layer.py:82(move)
                2173875   66.201    0.000 4959.130    0.002 agent.py:114(_learn)
                5942997  162.289    0.000 4291.281    0.001 agent.py:48(__call__)
                6521614   27.634    0.000 4119.356    0.001 tensor.py:195(backward)
                6521614   25.023    0.000 4090.776    0.001 __init__.py:68(backward)
                2173875 2374.864    0.001 3935.679    0.002 agent.py:85(interveen)
                6521614 3922.184    0.001 3922.184    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2173876  235.877    0.000 3888.767    0.002 layers.py:565(update)
                2173875 2481.804    0.001 3278.967    0.002 replaybuffer.py:22(sample_data)
               34309757 3125.937    0.000 3125.937    0.000 {built-in method tensor}
               29194290   21.476    0.000 2979.902    0.000 game.py:32(board)
              217387489  473.038    0.000 2962.420    0.000 layers.py:611(check)
               36818238   78.459    0.000 2902.230    0.000 conv.py:398(forward)
               36818238   49.656    0.000 2785.748    0.000 conv.py:390(_conv_forward)
               36818238 2736.093    0.000 2736.093    0.000 {built-in method conv2d}
                2173875 2002.924    0.001 2702.579    0.001 replaybuffer.py:49(sample_data)
              200639499 2575.770    0.000 2575.770    0.000 {built-in method clone}
               34782008 1403.205    0.000 2365.569    0.000 layer.py:143(NoRock_update)
               50879607  101.741    0.000 2328.042    0.000 linear.py:93(forward)
               50879607   41.449    0.000 2175.239    0.000 functional.py:1737(linear)
               50879607 2123.778    0.000 2123.778    0.000 {built-in method torch._C._nn.linear}
                1596769   15.614    0.000 1914.814    0.001 agent.py:167(choose_action)
              217383506  309.350    0.000 1792.565    0.000 layers.py:605(isFree)
                2173875 1112.196    0.001 1784.464    0.001 agent.py:66(modify)
                5858779   52.529    0.000 1539.411    0.000 layers.py:615(restart)
             1527003419 1248.052    0.000 1483.216    0.000 layer.py:79(isFree)
               32029442 1315.545    0.000 1315.545    0.000 {built-in method cat}
               69288726   57.897    0.000 1291.864    0.000 activation.py:713(forward)
               69288726   57.862    0.000 1233.967    0.000 functional.py:1364(leaky_relu)
              121736780 1233.241    0.000 1233.241    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                2173875  563.807    0.000 1189.420    0.001 replaybuffer.py:55(CF_save_data)
                8116872   60.752    0.000 1177.947    0.000 agent.py:58(modify_board)
               69288726 1164.010    0.000 1164.010    0.000 {built-in method torch._C._nn.leaky_relu}
                2173864   40.454    0.000 1097.343    0.001 agent.py:163(__call__)
              121736780 1085.253    0.000 1085.253    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                2173875   39.084    0.000 1041.443    0.000 agent.py:109(__call__)
                5858779   25.374    0.000 1029.529    0.000 level.py:8(__init__)
                6521614  152.565    0.000  936.693    0.000 optimizer.py:189(zero_grad)
              217387600  112.534    0.000  866.059    0.000 {built-in method builtins.all}
                5858779  110.171    0.000  852.842    0.000 levels.py:164(generate)
             1293437724  319.895    0.000  778.565    0.000 layers.py:571(<genexpr>)
             3323665139  543.145    0.000  776.154    0.000 enum.py:646(__hash__)
                8116872  748.395    0.000  748.395    0.000 {built-in method torch._C._nn.one_hot}
              217387489  457.162    0.000  740.615    0.000 layers.py:303(check)
              217387489  402.487    0.000  685.806    0.000 layers.py:262(check)
               60868390  677.962    0.000  677.962    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                2173875   51.339    0.000  643.708    0.000 replaybuffer.py:18(stacker)
              210930235  631.559    0.000  631.559    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               11717558   89.299    0.000  596.588    0.000 level.py:41(notUsed)
               60868390  593.498    0.000  593.498    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
             1082917702  577.449    0.000  577.449    0.000 layer.py:122(elements)
               60868390  561.447    0.000  561.447    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               60868390  557.536    0.000  557.536    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                2173864   47.450    0.000  552.912    0.000 replaybuffer.py:45(stacker)
                5942997  163.776    0.000  449.334    0.000 exploration.py:53(softmaxer)
               46870232   54.501    0.000  442.174    0.000 layer.py:56(restart)
                2173875  266.180    0.000  441.976    0.000 collector.py:54(collect)
               60868390  426.962    0.000  426.962    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               16065308  150.088    0.000  394.093    0.000 random.py:315(sample)
             4017975624  383.458    0.000  383.458    0.000 layer.py:75(positions)
              217387489  240.950    0.000  381.791    0.000 layers.py:329(check)
              426078814  276.463    0.000  344.201    0.000 tensor.py:906(grad)
              217387489  221.016    0.000  340.507    0.000 layers.py:288(check)
              217387600  222.877    0.000  335.577    0.000 layers.py:111(isDone)
        4241235516/4241235513  285.638    0.000  328.766    0.000 {built-in method builtins.len}
                6521614    9.961    0.000  312.851    0.000 loss.py:527(forward)
              218043003  241.231    0.000  303.332    0.000 layer.py:102(remove)
                6521614   23.648    0.000  302.889    0.000 functional.py:2898(mse_loss)
                6521626  291.291    0.000  291.291    0.000 {built-in method nonzero}
              217387489  195.056    0.000  288.391    0.000 layers.py:47(check)
                5858879  139.896    0.000  278.183    0.000 layers.py:33(reset)
              509547211  197.598    0.000  271.433    0.000 layer.py:106(add)
              384364946  244.160    0.000  244.160    0.000 level.py:32(inverse)
             3323690146  233.014    0.000  233.014    0.000 {built-in method builtins.hash}
               36818238   25.893    0.000  210.137    0.000 flatten.py:39(forward)
               11717558   10.278    0.000  205.240    0.000 level.py:38(elementsIn)
              324595339  136.758    0.000  200.807    0.000 random.py:250(_randbelow_with_getrandbits)
                6521614  199.031    0.000  199.031    0.000 {built-in method torch._C._nn.mse_loss}
               13043250  187.596    0.000  187.596    0.000 {built-in method sum}
               36818238  184.244    0.000  184.244    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                6522425  180.002    0.000  180.002    0.000 {built-in method max}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-2>
Subject: Job 9494238: <NOBUGcausal3_CFagent_convert1_0> in cluster <dcc> Done

Job <NOBUGcausal3_CFagent_convert1_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun Apr  4 02:59:52 2021
Job was executed on host(s) <n-62-20-2>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Apr  4 02:59:53 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun Apr  4 02:59:53 2021
Terminated at Sun Apr  4 18:55:29 2021
Results reported at Sun Apr  4 18:55:29 2021

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

    CPU time :                                   57170.95 sec.
    Max Memory :                                 7392 MB
    Average Memory :                             5409.31 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               8992.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   57376 sec.
    Turnaround time :                            57337 sec.

The output (if any) is above this job summary.

