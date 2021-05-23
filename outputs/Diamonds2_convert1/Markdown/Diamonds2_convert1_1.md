
# Parameters

    Name :                      Diamonds2_convert1-1
    Main :                      CFagent
    Level :                     Levels.Causal5
    Failed actions chance :     0
    Use model :                 False
    Depth :                     1
    Model explore :             100000
    Samples :                   5
    Hours :                     24.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.UCB1
    Network1 :                  Networks.Teleporter
    K1 :                        2000000.0
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
    Cf convert :                1
    Counterfacts :              1
    Topn :                      2
    Random counterfacts :       False
    Num :                       1
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      72768728295 function calls (72448663668 primitive calls) in 86110.13 seconds

##    Ordered by: cumulative time
   List reduced from 504 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86110.125 86110.125 {built-in method builtins.exec}
                      1    4.420    4.420 86110.125 86110.125 <string>:1(<module>)
                      1  359.578  359.578 86105.705 86105.705 main.py:80(CFagent)
                9817818   37.498    0.000 24501.954    0.002 agent.py:29(learn)
                9817818  616.666    0.000 19954.799    0.002 learner.py:42(Qlearn)
                3272606   13.364    0.000 19692.514    0.006 game.py:42(step)
                3272606   20.498    0.000 18963.532    0.006 layers.py:827(step)
        357643534/37580598 1467.288    0.000 11908.613    0.000 module.py:866(_call_impl)
               27762780   79.584    0.000 11163.431    0.000 network.py:28(forward)
               27762780  352.808    0.000 10898.928    0.000 container.py:117(forward)
                3272606  280.419    0.000 10731.001    0.003 layers.py:17(step)
              327182581  568.228    0.000 10421.531    0.000 layer.py:106(move)
                3272606 1131.332    0.000 10335.509    0.003 agent.py:212(counterfact)
                3272606  348.845    0.000 9521.695    0.003 agent.py:54(_learn)
                3272606  346.125    0.000 8734.290    0.003 agent.py:204(_learn)
                3272607  505.260    0.000 8183.792    0.003 layers.py:793(update)
                9817818   84.235    0.000 7827.280    0.001 optimizer.py:84(wrapper)
                3272606 4295.545    0.001 7557.966    0.002 replaybuffer.py:28(teleporter_save_data)
                9817818   41.989    0.000 7452.490    0.001 grad_mode.py:24(decorate_context)
                9817818  294.594    0.000 7316.754    0.001 adam.py:55(step)
              327182581 1379.590    0.000 6747.632    0.000 layers.py:844(check)
                9817818 1514.583    0.000 6685.401    0.001 _functional.py:53(adam)
                3272606  100.963    0.000 6187.233    0.002 agent.py:117(_learn)
                8971408  236.727    0.000 5887.684    0.001 agent.py:49(__call__)
                3272606 3653.208    0.001 5796.681    0.002 agent.py:88(interveen)
                3272606 4678.587    0.001 5706.527    0.002 replaybuffer.py:22(sample_data)
                3272606 4556.465    0.001 5549.347    0.002 replaybuffer.py:67(sample_data)
                9817818   39.993    0.000 5149.948    0.001 tensor.py:195(backward)
                9817818   38.974    0.000 5108.492    0.001 __init__.py:68(backward)
                9817818 4872.960    0.000 4872.960    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
               51565199 4856.328    0.000 4856.328    0.000 {built-in method tensor}
               44027565   28.758    0.000 4669.765    0.000 game.py:38(board)
               55525560  122.675    0.000 4031.422    0.000 conv.py:398(forward)
               55525560   76.948    0.000 3848.383    0.000 conv.py:390(_conv_forward)
               55525560 3771.435    0.000 3771.435    0.000 {built-in method conv2d}
               58906917 2065.092    0.000 3715.187    0.000 layer.py:175(NoRock_update)
                2428342   50.633    0.000 3210.131    0.001 agent.py:176(choose_action)
                5600559   68.082    0.000 3198.753    0.001 layers.py:849(restart)
               76743128  168.519    0.000 3081.954    0.000 linear.py:93(forward)
              306471277 3044.298    0.000 3044.298    0.000 {built-in method clone}
               76743128   62.958    0.000 2834.957    0.000 functional.py:1737(linear)
               76743128 2755.770    0.000 2755.770    0.000 {built-in method torch._C._nn.linear}
                5600559   28.860    0.000 2687.042    0.000 level.py:8(__init__)
              327182581  609.970    0.000 2555.456    0.000 layers.py:838(isFree)
                3272606 1687.027    0.001 2520.976    0.001 agent.py:67(modify)
                5600559   93.889    0.000 2386.238    0.000 levels.py:249(generate)
               36407092  374.251    0.000 2199.143    0.000 level.py:41(notUsed)
             2922514519 1583.303    0.000 1945.486    0.000 layer.py:103(isFree)
             7198007561 1289.166    0.000 1852.739    0.000 enum.py:646(__hash__)
               44970074 1698.353    0.000 1698.353    0.000 {built-in method cat}
                3272606 1251.042    0.000 1644.787    0.001 replaybuffer.py:73(CF_save_data)
              104505908   87.808    0.000 1627.347    0.000 activation.py:713(forward)
               12244014   78.633    0.000 1623.744    0.000 agent.py:59(modify_board)
              104505908   86.994    0.000 1539.539    0.000 functional.py:1364(leaky_relu)
                3272606   54.648    0.000 1492.072    0.000 agent.py:172(__call__)
              104505908 1434.588    0.000 1434.588    0.000 {built-in method torch._C._nn.leaky_relu}
                3272606   53.115    0.000 1412.342    0.000 agent.py:112(__call__)
              324932748  329.076    0.000 1410.867    0.000 {built-in method builtins.any}
              183265936 1311.967    0.000 1311.967    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              183265936 1175.233    0.000 1175.233    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                9817818  204.835    0.000 1145.619    0.000 optimizer.py:189(zero_grad)
             3216601410  879.779    0.000 1081.791    0.000 layers.py:809(<genexpr>)
               36407092   29.300    0.000 1068.169    0.000 level.py:38(elementsIn)
               12244014 1065.505    0.000 1065.505    0.000 {built-in method torch._C._nn.one_hot}
              327182581  654.641    0.000 1011.848    0.000 layers.py:337(check)
              327260700  101.925    0.000  987.573    0.000 {built-in method builtins.all}
              327182581  608.756    0.000  967.736    0.000 layers.py:387(check)
              327182581  618.554    0.000  966.938    0.000 layers.py:375(check)
             1036429935  285.971    0.000  928.757    0.000 layers.py:799(<genexpr>)
              327182581  578.009    0.000  927.450    0.000 layers.py:349(check)
             1175739459  925.827    0.000  925.827    0.000 layer.py:154(elements)
                3272606   58.929    0.000  776.341    0.000 replaybuffer.py:18(stacker)
               91632968  769.257    0.000  769.257    0.000 {method 'add' of 'torch._C._TensorBase' objects}
             7859372234  755.521    0.000  755.521    0.000 layer.py:99(positions)
                3272606   60.834    0.000  749.423    0.000 replaybuffer.py:63(stacker)
               36407092  345.234    0.000  694.074    0.000 level.py:39(<listcomp>)
               91632968  660.528    0.000  660.528    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              321987897  657.053    0.000  657.053    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
        8120074532/8120074529  567.120    0.000  629.665    0.000 {built-in method builtins.len}
               91632968  617.738    0.000  617.738    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               91632968  612.599    0.000  612.599    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              327260700  404.000    0.000  602.952    0.000 layers.py:113(isDone)
                8971408  218.345    0.000  583.932    0.000 exploration.py:53(softmaxer)
             7198044888  563.580    0.000  563.580    0.000 {built-in method builtins.hash}
              641430860  424.436    0.000  529.025    0.000 tensor.py:906(grad)
                3272606  297.307    0.000  506.623    0.000 collector.py:46(collect)
                2428342  482.354    0.000  482.354    0.000 agent.py:187(convert_values)
                6545212  178.845    0.000  482.321    0.000 random.py:315(sample)
               91632968  456.877    0.000  456.877    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
             1717075030  430.730    0.000  430.730    0.000 level.py:32(inverse)
                9817818   13.800    0.000  429.208    0.000 loss.py:527(forward)
               50405031   43.828    0.000  426.903    0.000 layer.py:77(restart)
              327182581  271.646    0.000  422.844    0.000 layers.py:326(check)
                9817818   37.158    0.000  415.408    0.000 functional.py:2898(mse_loss)
              327182581  267.621    0.000  414.961    0.000 layers.py:364(check)
              327182581  241.940    0.000  355.578    0.000 layers.py:23(check)
             1806331158  351.657    0.000  351.657    0.000 enum.py:352(<genexpr>)
               36407092  215.065    0.000  344.795    0.000 {built-in method _functools.reduce}
              531746406  227.513    0.000  322.624    0.000 layer.py:138(add)
                5600659  151.972    0.000  306.286    0.000 layers.py:36(reset)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9678083: <Diamonds2_convert1_1> in cluster <dcc> Done

Job <Diamonds2_convert1_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Fri May 21 19:42:38 2021
Job was executed on host(s) <n-62-20-14>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Fri May 21 19:47:34 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Fri May 21 19:47:34 2021
Terminated at Sat May 22 19:42:49 2021
Results reported at Sat May 22 19:42:49 2021

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

    CPU time :                                   85874.84 sec.
    Max Memory :                                 9412 MB
    Average Memory :                             6374.37 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               6972.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86114 sec.
    Turnaround time :                            86411 sec.

The output (if any) is above this job summary.

