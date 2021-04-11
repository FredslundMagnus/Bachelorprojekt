
# Parameters

    Name :                      MONTEST_CF_5c2-0
    Main :                      CFagent
    Level :                     Levels.MonsterLevel
    Hours :                     22.0
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
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                5
    Counterfacts :              2
    Topn :                      7
    Minutes used :              1315 minutes.
    Hours used :                21 hours.

# Profiling


      55924782253 function calls (55634421410 primitive calls) in 78910.95 seconds

##    Ordered by: cumulative time
   List reduced from 506 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 78910.946 78910.946 {built-in method builtins.exec}
                      1    4.546    4.546 78910.946 78910.946 <string>:1(<module>)
                      1  168.888  168.888 78906.399 78906.399 main.py:95(CFagent)
                6939054   26.480    0.000 21674.240    0.003 agent.py:29(learn)
                6939054  541.398    0.000 18087.508    0.003 learner.py:42(Qlearn)
                2313018 3192.767    0.001 17183.248    0.007 agent.py:217(counterfact)
                2313018   11.547    0.000 16947.804    0.007 game.py:41(step)
                2313018   13.344    0.000 16456.214    0.007 layers.py:710(step)
        322265808/31906656 1384.037    0.000 12253.207    0.000 module.py:866(_call_impl)
               24967602   70.434    0.000 11620.731    0.000 network.py:24(forward)
               24967602  371.552    0.000 11389.759    0.000 container.py:117(forward)
                2313019  360.869    0.000 9410.862    0.004 layers.py:676(update)
                2313018  244.140    0.000 8352.207    0.004 agent.py:54(_learn)
                2313018  242.132    0.000 7752.641    0.003 agent.py:209(_learn)
                6939054   65.045    0.000 7676.422    0.001 optimizer.py:84(wrapper)
                6939054   31.824    0.000 7374.489    0.001 grad_mode.py:24(decorate_context)
                6939054  214.590    0.000 7275.848    0.001 adam.py:55(step)
                2313018  210.815    0.000 7013.857    0.003 layers.py:17(step)
                4388274  101.141    0.000 6980.699    0.002 agent.py:172(choose_action)
                6939054 1508.558    0.000 6821.332    0.001 _functional.py:53(adam)
              213036467  634.461    0.000 6779.496    0.000 layer.py:98(move)
                9014238  249.152    0.000 6720.648    0.001 agent.py:49(__call__)
                2313018 3392.218    0.001 6366.430    0.003 replaybuffer.py:28(teleporter_save_data)
                2313018   72.358    0.000 5527.469    0.002 agent.py:117(_learn)
                8960752   71.677    0.000 4891.008    0.001 layers.py:731(restart)
               60113428 4653.371    0.000 4653.371    0.000 {built-in method tensor}
               54692018   38.883    0.000 4515.779    0.000 game.py:37(board)
                6939054   30.175    0.000 4482.327    0.001 tensor.py:195(backward)
                6939054   27.458    0.000 4451.046    0.001 __init__.py:68(backward)
                2313018 2663.522    0.001 4387.468    0.002 agent.py:88(interveen)
              213036467  478.702    0.000 4379.127    0.000 layers.py:727(check)
                6939054 4262.725    0.001 4262.725    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                8960752   35.211    0.000 4155.894    0.000 level.py:8(__init__)
               49935204  112.224    0.000 4033.433    0.000 conv.py:398(forward)
               49935204   66.120    0.000 3869.120    0.000 conv.py:390(_conv_forward)
                8960752  685.106    0.000 3816.860    0.000 levels.py:418(generate)
               49935204 3803.000    0.000 3803.000    0.000 {built-in method conv2d}
               41634330 2381.713    0.000 3569.676    0.000 layer.py:151(update)
               70276770  148.439    0.000 3310.620    0.000 linear.py:93(forward)
                2313018 2466.858    0.001 3303.658    0.001 replaybuffer.py:22(sample_data)
               70276770   60.883    0.000 3089.393    0.000 functional.py:1737(linear)
              231930012 3052.480    0.000 3052.480    0.000 {built-in method clone}
                2313018 2290.927    0.001 3037.042    0.001 replaybuffer.py:49(sample_data)
               70276770 3013.123    0.000 3013.123    0.000 {built-in method torch._C._nn.linear}
              213036467 1572.343    0.000 2788.156    0.000 layers.py:531(check)
               44803760  403.400    0.000 2478.121    0.000 level.py:41(notUsed)
                2313018 1546.056    0.001 2234.609    0.001 agent.py:67(modify)
               95244372   77.014    0.000 1866.667    0.000 activation.py:713(forward)
               95244372   87.077    0.000 1789.653    0.000 functional.py:1364(leaky_relu)
                2313018  863.446    0.000 1775.376    0.001 replaybuffer.py:55(CF_save_data)
               95244372 1685.121    0.000 1685.121    0.000 {built-in method torch._C._nn.leaky_relu}
               11327256   82.181    0.000 1682.376    0.000 agent.py:59(modify_board)
              231865460  186.704    0.000 1551.076    0.000 {built-in method builtins.any}
               36770454 1511.288    0.000 1511.288    0.000 {built-in method cat}
              129529008 1387.280    0.000 1387.280    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                4388274 1160.906    0.000 1373.232    0.000 agent.py:183(convert_values)
             1585777686  443.766    0.000 1365.004    0.000 layers.py:692(<genexpr>)
             5580458714  945.175    0.000 1349.519    0.000 enum.py:646(__hash__)
              212883098  268.904    0.000 1338.609    0.000 layers.py:721(isFree)
              129529008 1215.990    0.000 1215.990    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                2313018   40.194    0.000 1212.763    0.001 agent.py:168(__call__)
                2313018   39.102    0.000 1143.540    0.000 agent.py:112(__call__)
                6939054  176.373    0.000 1069.957    0.000 optimizer.py:189(zero_grad)
             1136186178  881.274    0.000 1069.706    0.000 layer.py:95(isFree)
               44803760   35.990    0.000 1068.511    0.000 level.py:38(elementsIn)
               11327256 1064.464    0.000 1064.464    0.000 {built-in method torch._C._nn.one_hot}
              227239423  519.193    0.000  836.863    0.000 layers.py:568(isDead)
              231301900  105.173    0.000  793.284    0.000 {built-in method builtins.all}
              245570286  775.148    0.000  775.148    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               64764504  765.914    0.000  765.914    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               49429796  284.851    0.000  729.977    0.000 random.py:315(sample)
              980280533  277.547    0.000  718.773    0.000 layers.py:682(<genexpr>)
              213036467  507.669    0.000  703.451    0.000 layers.py:71(check)
             1864223291  697.692    0.000  697.692    0.000 layer.py:146(elements)
                9014238  252.733    0.000  694.113    0.000 exploration.py:53(softmaxer)
             1911485325  688.124    0.000  688.124    0.000 level.py:32(inverse)
               44803760  333.338    0.000  671.280    0.000 level.py:39(<listcomp>)
                2313018   44.579    0.000  670.565    0.000 replaybuffer.py:18(stacker)
               64764504  669.699    0.000  669.699    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               53764512   61.676    0.000  645.063    0.000 layer.py:69(restart)
              494297851  500.281    0.000  637.903    0.000 layer.py:126(remove)
               64764504  628.505    0.000  628.505    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               64764504  625.754    0.000  625.754    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                2313018   42.620    0.000  584.049    0.000 replaybuffer.py:45(stacker)
              722182876  357.845    0.000  516.838    0.000 random.py:250(_randbelow_with_getrandbits)
              290983321   99.520    0.000  511.627    0.000 random.py:244(randint)
                2313018  298.150    0.000  492.279    0.000 collector.py:53(collect)
               64764504  484.149    0.000  484.149    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              899805388  353.450    0.000  475.488    0.000 layer.py:130(add)
               35943721  455.572    0.000  455.572    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                8960852  227.763    0.000  454.637    0.000 layers.py:30(reset)
        5472417364/5472417361  393.721    0.000  454.469    0.000 {built-in method builtins.len}
              290983321  175.311    0.000  412.107    0.000 random.py:200(randrange)
             5580485289  404.349    0.000  404.349    0.000 {built-in method builtins.hash}
              453351612  320.193    0.000  395.432    0.000 tensor.py:906(grad)
             4271454046  384.017    0.000  384.017    0.000 layer.py:91(positions)
              231301900  260.172    0.000  383.876    0.000 layers.py:107(isDone)
               44803760  222.667    0.000  361.241    0.000 {built-in method _functools.reduce}
              213036467  246.244    0.000  354.074    0.000 layers.py:42(check)
                6939054   10.406    0.000  348.375    0.000 loss.py:527(forward)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-11-16>
Subject: Job 9507475: <MONTEST_CF_5c2_0> in cluster <dcc> Done

Job <MONTEST_CF_5c2_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sat Apr 10 02:36:49 2021
Job was executed on host(s) <n-62-11-16>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sat Apr 10 03:32:53 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat Apr 10 03:32:53 2021
Terminated at Sun Apr 11 01:28:09 2021
Results reported at Sun Apr 11 01:28:09 2021

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

    CPU time :                                   78718.09 sec.
    Max Memory :                                 7921 MB
    Average Memory :                             5749.48 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               8463.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   78916 sec.
    Turnaround time :                            82280 sec.

The output (if any) is above this job summary.

