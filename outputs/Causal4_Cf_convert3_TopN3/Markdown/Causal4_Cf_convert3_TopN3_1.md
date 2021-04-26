
# Parameters

    Name :                      Causal4_Cf_convert3_TopN3-1
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
    Cf convert :                3
    Counterfacts :              1
    Topn :                      3
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      84233558107 function calls (83876374076 primitive calls) in 86121.46 seconds

##    Ordered by: cumulative time
   List reduced from 513 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86121.456 86121.456 {built-in method builtins.exec}
                      1    4.205    4.205 86121.456 86121.456 <string>:1(<module>)
                      1  389.674  389.674 86117.251 86117.251 main.py:79(CFagent)
               11577258   37.480    0.000 26290.350    0.002 agent.py:29(learn)
                3859086   14.353    0.000 23051.851    0.006 game.py:41(step)
                3859086   20.079    0.000 22199.797    0.006 layers.py:718(step)
               11577252  657.666    0.000 21388.560    0.002 learner.py:42(Qlearn)
                3859086  322.656    0.000 14198.965    0.004 layers.py:17(step)
              385704724 1027.383    0.000 13844.856    0.000 layer.py:98(move)
        399811149/42628809 1505.430    0.000 12100.963    0.000 module.py:866(_call_impl)
               31051557   79.685    0.000 11306.914    0.000 network.py:27(forward)
               31051557  366.103    0.000 11042.066    0.000 container.py:117(forward)
                3859086  895.756    0.000 10809.720    0.003 agent.py:210(counterfact)
                3859086  381.813    0.000 10220.510    0.003 agent.py:54(_learn)
                3859086  378.356    0.000 9383.156    0.002 agent.py:202(_learn)
              385704724 1663.280    0.000 8638.997    0.000 layers.py:735(check)
               11577252   91.702    0.000 8398.146    0.001 optimizer.py:84(wrapper)
               11577252   45.848    0.000 7991.754    0.001 grad_mode.py:24(decorate_context)
                3859087  535.654    0.000 7950.046    0.002 layers.py:684(update)
               11577252  322.572    0.000 7845.165    0.001 adam.py:55(step)
               11577252 1627.695    0.000 7158.265    0.001 _functional.py:53(adam)
                3859086  110.147    0.000 6625.887    0.002 agent.py:117(_learn)
                3859086 5080.159    0.001 6195.128    0.002 replaybuffer.py:22(sample_data)
               60993452 6078.279    0.000 6078.279    0.000 {built-in method tensor}
                3859086 4853.359    0.001 5928.253    0.002 replaybuffer.py:67(sample_data)
               52161262   28.950    0.000 5876.080    0.000 game.py:37(board)
                9724385  234.011    0.000 5811.474    0.001 agent.py:49(__call__)
               11577252   41.808    0.000 5520.669    0.000 tensor.py:195(backward)
               11577252   42.417    0.000 5477.418    0.000 __init__.py:68(backward)
               11577252 5221.266    0.000 5221.266    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
               77181730 2703.164    0.000 4640.184    0.000 layer.py:151(update)
               62103114  126.323    0.000 4096.969    0.000 conv.py:398(forward)
               62103114   89.313    0.000 3912.456    0.000 conv.py:390(_conv_forward)
                3859086 1559.520    0.000 3839.308    0.001 agent.py:88(interveen)
               62103114 3823.143    0.000 3823.143    0.000 {built-in method conv2d}
              385704724  701.994    0.000 3483.256    0.000 layers.py:729(isFree)
               85436499  159.491    0.000 3107.847    0.000 linear.py:93(forward)
                3859086 1723.148    0.000 3059.423    0.001 replaybuffer.py:28(teleporter_save_data)
               85436499   68.126    0.000 2869.609    0.000 functional.py:1737(linear)
               85436499 2785.737    0.000 2785.737    0.000 {built-in method torch._C._nn.linear}
             3285064390 2309.155    0.000 2781.262    0.000 layer.py:95(isFree)
                3859086 1723.679    0.000 2626.723    0.001 agent.py:67(modify)
                2031754   41.279    0.000 2477.768    0.001 agent.py:175(choose_action)
              385908700  262.562    0.000 1845.010    0.000 {built-in method builtins.all}
             7573719595 1296.198    0.000 1824.282    0.000 enum.py:646(__hash__)
               52174301 1823.228    0.000 1823.228    0.000 {built-in method cat}
               13583471   81.166    0.000 1658.216    0.000 agent.py:59(modify_board)
              116488056   91.626    0.000 1654.828    0.000 activation.py:713(forward)
              385947310  380.108    0.000 1639.464    0.000 {built-in method builtins.any}
             3151260060  809.032    0.000 1628.363    0.000 layers.py:690(<genexpr>)
                3859080   61.952    0.000 1608.413    0.000 agent.py:171(__call__)
              116488056   87.635    0.000 1563.202    0.000 functional.py:1364(leaky_relu)
                3859086   57.514    0.000 1503.417    0.000 agent.py:112(__call__)
              116488056 1457.450    0.000 1457.450    0.000 {built-in method torch._C._nn.leaky_relu}
              216108696 1401.007    0.000 1401.007    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              385704724 1051.331    0.000 1382.081    0.000 layers.py:77(check)
              143790852 1369.467    0.000 1369.467    0.000 {built-in method clone}
                3820477   44.623    0.000 1315.499    0.000 layers.py:740(restart)
              385704724  822.067    0.000 1268.029    0.000 layers.py:286(check)
             4202970453 1033.301    0.000 1259.355    0.000 layers.py:700(<genexpr>)
              216108696 1248.514    0.000 1248.514    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                3859086  983.372    0.000 1247.366    0.000 replaybuffer.py:73(CF_save_data)
               11577252  217.529    0.000 1229.617    0.000 optimizer.py:189(zero_grad)
              385704724  701.983    0.000 1149.147    0.000 layers.py:246(check)
               13583471 1095.178    0.000 1095.178    0.000 {built-in method torch._C._nn.one_hot}
             1280511817 1085.860    0.000 1085.860    0.000 layer.py:146(elements)
                3820477   19.937    0.000  925.844    0.000 level.py:8(__init__)
             9924666452  880.194    0.000  880.194    0.000 layer.py:91(positions)
                3859086   65.957    0.000  850.478    0.000 replaybuffer.py:18(stacker)
              108054348  824.587    0.000  824.587    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                3859080   66.768    0.000  818.126    0.000 replaybuffer.py:63(stacker)
              385704724  600.424    0.000  775.307    0.000 layers.py:62(check)
                3820477  121.341    0.000  744.594    0.000 levels.py:199(generate)
              108054348  706.933    0.000  706.933    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
        10185082411/10185082408  617.240    0.000  683.979    0.000 {built-in method builtins.len}
              385908700  445.414    0.000  669.820    0.000 layers.py:113(isDone)
              108054348  665.804    0.000  665.804    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              108054348  656.538    0.000  656.538    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              385704724  377.189    0.000  596.555    0.000 layers.py:313(check)
              756380520  465.223    0.000  576.180    0.000 tensor.py:906(grad)
                9724385  215.414    0.000  571.484    0.000 exploration.py:53(softmaxer)
              385704724  358.980    0.000  569.516    0.000 layers.py:273(check)
               15359126  215.257    0.000  563.777    0.000 random.py:315(sample)
                3859086  320.761    0.000  544.470    0.000 collector.py:46(collect)
             7573763418  528.092    0.000  528.092    0.000 {built-in method builtins.hash}
                7640954   59.845    0.000  506.430    0.000 level.py:41(notUsed)
              385704724  338.856    0.000  494.626    0.000 layers.py:48(check)
              108054348  490.891    0.000  490.891    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               11577252   15.106    0.000  455.367    0.000 loss.py:527(forward)
               11577252   40.135    0.000  440.261    0.000 functional.py:2898(mse_loss)
                2031754  380.513    0.000  403.956    0.000 agent.py:186(convert_values)
              385704724  267.033    0.000  385.820    0.000 layers.py:23(check)
               38204770   48.910    0.000  333.025    0.000 layer.py:69(restart)
             4258276357  323.780    0.000  323.780    0.000 {method 'random' of '_random.Random' objects}
              335498877  223.745    0.000  310.431    0.000 layer.py:126(remove)
              161233403  310.213    0.000  310.213    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              563895474  220.348    0.000  301.902    0.000 layer.py:130(add)
              463543379  194.088    0.000  282.830    0.000 random.py:250(_randbelow_with_getrandbits)
                7718174  275.682    0.000  275.682    0.000 {built-in method nonzero}
               77181730  273.200    0.000  273.200    0.000 layer.py:163(<listcomp>)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9551816: <Causal4_Cf_convert3_TopN3_1> in cluster <dcc> Done

Job <Causal4_Cf_convert3_TopN3_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed Apr 21 03:20:31 2021
Job was executed on host(s) <n-62-20-5>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Thu Apr 22 04:49:12 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Apr 22 04:49:12 2021
Terminated at Fri Apr 23 04:44:49 2021
Results reported at Fri Apr 23 04:44:49 2021

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

    CPU time :                                   85905.90 sec.
    Max Memory :                                 10632 MB
    Average Memory :                             6927.61 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               5752.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86138 sec.
    Turnaround time :                            177858 sec.

The output (if any) is above this job summary.

