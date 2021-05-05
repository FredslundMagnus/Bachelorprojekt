
# Parameters

    Name :                      Causal4_Conver4-1
    Main :                      CFagent
    Level :                     Levels.Causal4
    Failed actions chance :     0
    Use model :                 True
    Depth :                     3
    Model explore :             1000000
    Samples :                   5
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
    Layer super1 :              True
    Layer super2 :              True
    Layer super3 :              True
    Layer super4 :              True
    Layer super5 :              True
    Layer super6 :              True
    Layer super7 :              True
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
    Topn :                      3
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      80330926511 function calls (79995525552 primitive calls) in 86122.87 seconds

##    Ordered by: cumulative time
   List reduced from 514 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86122.870 86122.870 {built-in method builtins.exec}
                      1    4.519    4.519 86122.870 86122.870 <string>:1(<module>)
                      1  393.789  393.789 86118.350 86118.350 main.py:80(CFagent)
               10867743   40.660    0.000 25712.279    0.002 agent.py:29(learn)
                3622581   15.957    0.000 23233.104    0.006 game.py:42(step)
                3622581   22.341    0.000 22396.416    0.006 layers.py:827(step)
               10867733  651.460    0.000 20903.432    0.002 learner.py:42(Qlearn)
                3622581  315.985    0.000 14218.563    0.004 layers.py:17(step)
              362022231 1023.372    0.000 13870.044    0.000 layer.py:106(move)
        375424467/40025199 1479.676    0.000 11883.991    0.000 module.py:866(_call_impl)
               29157466   79.420    0.000 11106.238    0.000 network.py:28(forward)
               29157466  358.799    0.000 10840.733    0.000 container.py:117(forward)
                3622581  870.101    0.000 10618.764    0.003 agent.py:212(counterfact)
                3622581  376.353    0.000 10000.549    0.003 agent.py:54(_learn)
                3622581  371.644    0.000 9159.754    0.003 agent.py:204(_learn)
              362022231 1732.585    0.000 8583.657    0.000 layers.py:844(check)
               10867733   87.356    0.000 8129.656    0.001 optimizer.py:84(wrapper)
                3622582  532.546    0.000 8125.831    0.002 layers.py:793(update)
               10867733   45.521    0.000 7730.216    0.001 grad_mode.py:24(decorate_context)
               10867733  318.413    0.000 7583.972    0.001 adam.py:55(step)
               10867733 1584.852    0.000 6899.658    0.001 _functional.py:53(adam)
                3622581  109.560    0.000 6488.638    0.002 agent.py:117(_learn)
                3622581 5338.573    0.001 6447.962    0.002 replaybuffer.py:22(sample_data)
                3622581 5177.822    0.001 6243.579    0.002 replaybuffer.py:67(sample_data)
               57206272 5850.251    0.000 5850.251    0.000 {built-in method tensor}
                9136338  232.280    0.000 5721.882    0.001 agent.py:49(__call__)
               48896244   29.344    0.000 5650.087    0.000 game.py:38(board)
               10867733   42.280    0.000 5414.478    0.000 tensor.py:195(backward)
               10867733   43.234    0.000 5370.855    0.000 __init__.py:68(backward)
               10867733 5120.782    0.000 5120.782    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
               72451630 2665.420    0.000 4570.001    0.000 layer.py:159(update)
               58314932  123.892    0.000 4021.788    0.000 conv.py:398(forward)
                3622581 1594.366    0.000 3848.117    0.001 agent.py:88(interveen)
               58314932   79.119    0.000 3839.197    0.000 conv.py:390(_conv_forward)
               58314932 3760.078    0.000 3760.078    0.000 {built-in method conv2d}
              362022231  679.134    0.000 3572.830    0.000 layers.py:838(isFree)
                3622581 1776.833    0.000 3160.310    0.001 replaybuffer.py:28(teleporter_save_data)
               80227236  156.392    0.000 3056.901    0.000 linear.py:93(forward)
             3239302220 2382.368    0.000 2893.696    0.000 layer.py:103(isFree)
               80227236   63.427    0.000 2820.229    0.000 functional.py:1737(linear)
               80227236 2741.907    0.000 2741.907    0.000 {built-in method torch._C._nn.linear}
                3622581 1705.084    0.000 2592.088    0.001 agent.py:67(modify)
                1908243   37.999    0.000 2543.256    0.001 agent.py:176(choose_action)
              362258200  280.439    0.000 1955.071    0.000 {built-in method builtins.all}
             7168055184 1270.096    0.000 1819.021    0.000 enum.py:646(__hash__)
               48984679 1802.419    0.000 1802.419    0.000 {built-in method cat}
              362363753  381.898    0.000 1727.484    0.000 {built-in method builtins.any}
             3279296483  902.889    0.000 1719.233    0.000 layers.py:799(<genexpr>)
               12758919   82.357    0.000 1629.139    0.000 agent.py:59(modify_board)
              109384702   90.622    0.000 1607.571    0.000 activation.py:713(forward)
                3622571   59.369    0.000 1566.171    0.000 agent.py:172(__call__)
              109384702   83.346    0.000 1516.949    0.000 functional.py:1364(leaky_relu)
                3622581   56.523    0.000 1488.410    0.000 agent.py:112(__call__)
              109384702 1416.046    0.000 1416.046    0.000 {built-in method torch._C._nn.leaky_relu}
              139725077 1393.087    0.000 1393.087    0.000 {built-in method clone}
              202864336 1359.899    0.000 1359.899    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              362022231 1014.236    0.000 1349.332    0.000 layers.py:77(check)
             3946152881 1107.023    0.000 1345.586    0.000 layers.py:809(<genexpr>)
                3517029   43.801    0.000 1335.016    0.000 layers.py:849(restart)
              362022231  796.136    0.000 1228.605    0.000 layers.py:246(check)
               10867733  221.038    0.000 1218.477    0.000 optimizer.py:189(zero_grad)
                3622581  962.305    0.000 1218.057    0.000 replaybuffer.py:73(CF_save_data)
              202864336 1188.970    0.000 1188.970    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              362022231  709.725    0.000 1150.936    0.000 layers.py:286(check)
               12758919 1072.410    0.000 1072.410    0.000 {built-in method torch._C._nn.one_hot}
             1200919951 1069.259    0.000 1069.259    0.000 layer.py:154(elements)
                3517029   19.396    0.000  962.076    0.000 level.py:8(__init__)
             9405576196  880.112    0.000  880.112    0.000 layer.py:99(positions)
                3622581   71.956    0.000  847.871    0.000 replaybuffer.py:18(stacker)
                3622571   68.274    0.000  812.841    0.000 replaybuffer.py:63(stacker)
              101432168  796.050    0.000  796.050    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                3517029  118.108    0.000  764.993    0.000 levels.py:199(generate)
              362022231  575.452    0.000  743.593    0.000 layers.py:62(check)
              101432168  701.684    0.000  701.684    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
        9539253995/9539253992  607.382    0.000  677.798    0.000 {built-in method builtins.len}
              362258200  430.308    0.000  645.476    0.000 layers.py:113(isDone)
              101432168  626.817    0.000  626.817    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              101432168  614.728    0.000  614.728    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              362022231  376.492    0.000  592.441    0.000 layers.py:273(check)
              710025260  466.210    0.000  575.686    0.000 tensor.py:906(grad)
                9136338  213.898    0.000  568.538    0.000 exploration.py:53(softmaxer)
              362022231  356.836    0.000  563.946    0.000 layers.py:313(check)
               14279220  214.244    0.000  555.712    0.000 random.py:315(sample)
             7168096431  548.932    0.000  548.932    0.000 {built-in method builtins.hash}
                3622581  320.596    0.000  545.603    0.000 collector.py:46(collect)
                7034058   61.792    0.000  534.029    0.000 level.py:41(notUsed)
                1908243  432.814    0.000  507.471    0.000 agent.py:187(convert_values)
              362022231  335.855    0.000  499.150    0.000 layers.py:48(check)
              101432168  475.422    0.000  475.422    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               10867733   14.490    0.000  451.644    0.000 loss.py:527(forward)
               10867733   40.150    0.000  437.154    0.000 functional.py:2898(mse_loss)
              362022231  255.813    0.000  377.114    0.000 layers.py:23(check)
              156106567  325.627    0.000  325.627    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               35170290   47.923    0.000  317.853    0.000 layer.py:77(restart)
             3996654078  316.675    0.000  316.675    0.000 {method 'random' of '_random.Random' objects}
              320713274  221.074    0.000  310.442    0.000 layer.py:134(remove)
              528888359  217.125    0.000  299.026    0.000 layer.py:138(add)
              433333386  189.392    0.000  276.545    0.000 random.py:250(_randbelow_with_getrandbits)
                7245164  274.234    0.000  274.234    0.000 {built-in method nonzero}
               10867733  271.209    0.000  271.209    0.000 {built-in method torch._C._nn.mse_loss}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9606154: <Causal4_Conver4_1> in cluster <dcc> Done

Job <Causal4_Conver4_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon May  3 01:44:21 2021
Job was executed on host(s) <n-62-20-2>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Tue May  4 22:36:34 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue May  4 22:36:34 2021
Terminated at Wed May  5 22:32:08 2021
Results reported at Wed May  5 22:32:08 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
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

python main.py $MYARGS


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   85905.43 sec.
    Max Memory :                                 10166 MB
    Average Memory :                             6645.45 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               6218.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86135 sec.
    Turnaround time :                            247667 sec.

The output (if any) is above this job summary.

