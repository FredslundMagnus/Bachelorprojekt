
# Parameters

    Name :                      MonsterLevel_Conver4_3counterfactsNOCRASH_2-0
    Main :                      Load_Cfagent
    Level :                     Levels.MonsterLevel
    Failed actions chance :     0
    Use model :                 True
    Depth :                     3
    Model explore :             1000000
    Samples :                   5
    Hours :                     11.0
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
    Counterfacts :              3
    Topn :                      5
    Random counterfacts :       False
    Num :                       0
    Load name :                 MonsterLevel_Conver4_3counterfactsNOCRASH
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      65873283316 function calls (65517652547 primitive calls) in 86122.62 seconds

##    Ordered by: cumulative time
   List reduced from 431 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86122.622 86122.622 {built-in method builtins.exec}
                      1    4.100    4.100 86122.622 86122.622 <string>:1(<module>)
                      1  278.336  278.336 86118.522 86118.522 main.py:109(Load_Cfagent)
                2361224 4679.547    0.002 24180.812    0.010 agent.py:212(counterfact)
                2361224   11.398    0.000 19726.323    0.008 game.py:42(step)
                2361224   13.880    0.000 19255.334    0.008 layers.py:827(step)
                7083672   26.177    0.000 17564.359    0.002 agent.py:29(learn)
                7083672  435.230    0.000 14273.995    0.002 learner.py:42(Qlearn)
        393134357/37506409 1609.546    0.000 12564.064    0.000 module.py:866(_call_impl)
               30422737   81.231    0.000 11927.289    0.000 network.py:28(forward)
               30422737  381.619    0.000 11639.304    0.000 container.py:117(forward)
                2361224  365.534    0.000 10425.028    0.004 layers.py:793(update)
                6947098  140.589    0.000 9192.960    0.001 agent.py:176(choose_action)
                2361224  230.621    0.000 8796.646    0.004 layers.py:17(step)
              232931283  700.100    0.000 8544.528    0.000 layer.py:106(move)
               11669519  309.398    0.000 7374.485    0.001 agent.py:49(__call__)
                2361224  265.892    0.000 6818.474    0.003 agent.py:54(_learn)
               89814604 6812.588    0.000 6812.588    0.000 {built-in method tensor}
               84607128   50.083    0.000 6719.402    0.000 game.py:38(board)
                2361224  262.480    0.000 6255.253    0.003 agent.py:204(_learn)
               10145156   88.299    0.000 6026.603    0.001 layers.py:849(restart)
              232931283  758.253    0.000 5704.835    0.000 layers.py:844(check)
                7083672   60.896    0.000 5527.350    0.001 optimizer.py:84(wrapper)
                7083672   32.991    0.000 5262.847    0.001 grad_mode.py:24(decorate_context)
               10145156   42.315    0.000 5177.738    0.001 level.py:8(__init__)
                7083672  223.622    0.000 5160.154    0.001 adam.py:55(step)
                2361224 2938.220    0.001 4991.027    0.002 replaybuffer.py:28(teleporter_save_data)
                2361224 4010.684    0.002 4751.898    0.002 replaybuffer.py:22(sample_data)
               10145156  771.092    0.000 4704.303    0.000 levels.py:428(generate)
                7083672 1083.574    0.000 4689.815    0.001 _functional.py:53(adam)
                2361224 3933.394    0.002 4645.180    0.002 replaybuffer.py:67(sample_data)
               56669364 2923.443    0.000 4560.359    0.000 layer.py:159(update)
                2361224   74.164    0.000 4448.582    0.002 agent.py:117(_learn)
               60845474  135.358    0.000 4207.285    0.000 conv.py:398(forward)
               60845474   93.819    0.000 4002.072    0.000 conv.py:390(_conv_forward)
                2361224 2483.854    0.001 3966.800    0.002 agent.py:88(interveen)
               60845474 3908.253    0.000 3908.253    0.000 {built-in method conv2d}
                7083672   24.889    0.000 3775.665    0.001 tensor.py:195(backward)
                7083672   29.816    0.000 3749.733    0.001 __init__.py:68(backward)
                7083672 3579.509    0.001 3579.509    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               86545763  177.335    0.000 3304.143    0.000 linear.py:93(forward)
              232931283 1874.788    0.000 3301.076    0.000 layers.py:538(check)
               50725780  487.735    0.000 3195.992    0.000 level.py:41(notUsed)
               86545763   70.023    0.000 3028.888    0.000 functional.py:1737(linear)
               86545763 2942.048    0.000 2942.048    0.000 {built-in method torch._C._nn.linear}
                2361224 1776.913    0.001 2409.859    0.001 replaybuffer.py:73(CF_save_data)
              230848233 2234.056    0.000 2234.056    0.000 {built-in method clone}
                2361224 1330.860    0.001 1929.670    0.001 agent.py:67(modify)
               14030743   87.443    0.000 1803.451    0.000 agent.py:59(modify_board)
              116968500  101.456    0.000 1769.653    0.000 activation.py:713(forward)
                6947098 1476.439    0.000 1737.819    0.000 agent.py:187(convert_values)
              237164993  182.062    0.000 1668.366    0.000 {built-in method builtins.any}
              116968500   92.418    0.000 1668.197    0.000 functional.py:1364(leaky_relu)
              232931283  308.691    0.000 1646.816    0.000 layers.py:838(isFree)
             6432094893 1136.498    0.000 1632.433    0.000 enum.py:646(__hash__)
              116968500 1556.682    0.000 1556.682    0.000 {built-in method torch._C._nn.leaky_relu}
             1606465176  463.281    0.000 1486.809    0.000 layers.py:809(<genexpr>)
               50725780   42.083    0.000 1485.784    0.000 level.py:38(elementsIn)
               37642983 1374.059    0.000 1374.059    0.000 {built-in method cat}
             1356198142 1132.564    0.000 1338.124    0.000 layer.py:103(isFree)
               14030743 1198.293    0.000 1198.293    0.000 {built-in method torch._C._nn.one_hot}
                2361224   41.805    0.000 1071.131    0.000 agent.py:172(__call__)
                2361224   39.412    0.000  980.394    0.000 agent.py:112(__call__)
               50725780  483.819    0.000  972.321    0.000 level.py:39(<listcomp>)
             2159297497  956.516    0.000  956.516    0.000 layer.py:154(elements)
              230081322  590.133    0.000  934.554    0.000 layers.py:575(isDead)
              132228544  921.685    0.000  921.685    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              132228544  811.422    0.000  811.422    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                7083672  143.630    0.000  801.771    0.000 optimizer.py:189(zero_grad)
              232931283  567.034    0.000  799.311    0.000 layers.py:77(check)
               55448228  306.859    0.000  789.779    0.000 random.py:315(sample)
             2164164813  782.399    0.000  782.399    0.000 level.py:32(inverse)
              584887699  596.492    0.000  760.089    0.000 layer.py:134(remove)
               60870936   72.710    0.000  738.602    0.000 layer.py:77(restart)
               11669519  269.769    0.000  727.201    0.000 exploration.py:53(softmaxer)
               60993983  717.566    0.000  717.566    0.000 {method 'item' of 'torch._C._TensorBase' objects}
              346518712  119.789    0.000  611.277    0.000 random.py:244(randint)
             7676095710  528.955    0.000  598.286    0.000 {built-in method builtins.len}
              808949740  411.161    0.000  588.312    0.000 random.py:250(_randbelow_with_getrandbits)
                2361224   44.445    0.000  565.366    0.000 replaybuffer.py:18(stacker)
                2361224   44.071    0.000  541.991    0.000 replaybuffer.py:63(stacker)
             1036353595  398.644    0.000  539.249    0.000 layer.py:138(add)
               66114272  533.348    0.000  533.348    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               10145156  260.748    0.000  517.276    0.000 layers.py:36(reset)
             6432122028  495.940    0.000  495.940    0.000 {built-in method builtins.hash}
             2617450263  493.964    0.000  493.964    0.000 enum.py:352(<genexpr>)
              247240200  493.575    0.000  493.575    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              346518712  205.455    0.000  491.488    0.000 random.py:200(randrange)
               50725780  290.624    0.000  471.380    0.000 {built-in method _functools.reduce}
               66114272  461.011    0.000  461.011    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
             4752155144  445.659    0.000  445.659    0.000 layer.py:99(positions)
               66114272  431.935    0.000  431.935    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               66114272  429.871    0.000  429.871    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               10145156  197.584    0.000  407.058    0.000 level.py:16(<dictcomp>)
              232931283  274.330    0.000  405.802    0.000 layers.py:48(check)
              462799904  310.836    0.000  384.158    0.000 tensor.py:906(grad)
              232931283  129.023    0.000  367.817    0.000 layers.py:572(<listcomp>)
              236122400   56.820    0.000  360.296    0.000 {built-in method builtins.all}
                2361224  211.321    0.000  359.015    0.000 collector.py:46(collect)
              543635370  140.325    0.000  333.207    0.000 layers.py:799(<genexpr>)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9632958: <MonsterLevel_Conver4_3counterfactsNOCRASH_2_0> in cluster <dcc> Done

Job <MonsterLevel_Conver4_3counterfactsNOCRASH_2_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed May 12 15:41:02 2021
Job was executed on host(s) <n-62-20-10>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Thu May 13 16:26:42 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu May 13 16:26:42 2021
Terminated at Fri May 14 16:22:15 2021
Results reported at Fri May 14 16:22:15 2021

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

    CPU time :                                   85905.32 sec.
    Max Memory :                                 7855 MB
    Average Memory :                             5553.38 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               8529.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86133 sec.
    Turnaround time :                            175273 sec.

The output (if any) is above this job summary.

