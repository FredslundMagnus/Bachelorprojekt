
# Parameters

    Name :                      cococonuts_CF_conver3-0
    Main :                      CFagent
    Level :                     Levels.Coconuts
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
    Cf convert :                3
    Counterfacts :              1
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      58662531317 function calls (58371834410 primitive calls) in 86110.29 seconds

##    Ordered by: cumulative time
   List reduced from 508 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86110.288 86110.288 {built-in method builtins.exec}
                      1    4.823    4.823 86110.288 86110.288 <string>:1(<module>)
                      1  245.054  245.054 86105.464 86105.464 main.py:94(CFagent)
                9935142   39.441    0.000 32539.242    0.003 agent.py:29(learn)
                9935132  798.422    0.000 27170.622    0.003 learner.py:42(Qlearn)
                3311714   18.470    0.000 19914.564    0.006 game.py:41(step)
                3311714   21.799    0.000 19152.408    0.006 layers.py:710(step)
        325958854/35263638 1490.433    0.000 13151.074    0.000 module.py:866(_call_impl)
                3311714  323.854    0.000 12819.618    0.004 layers.py:17(step)
                3311714  363.693    0.000 12544.134    0.004 agent.py:54(_learn)
              330724074 1275.873    0.000 12459.841    0.000 layer.py:98(move)
               25328506   72.223    0.000 12308.148    0.000 network.py:24(forward)
               25328506  397.115    0.000 12062.078    0.000 container.py:117(forward)
                3311714  360.112    0.000 11635.919    0.004 agent.py:208(_learn)
                9935132   90.081    0.000 11482.554    0.001 optimizer.py:84(wrapper)
                9935132   46.815    0.000 11051.244    0.001 grad_mode.py:24(decorate_context)
                9935132  323.426    0.000 10897.265    0.001 adam.py:55(step)
                9935132 2262.290    0.000 10209.900    0.001 _functional.py:53(adam)
                3311714  106.232    0.000 8291.722    0.003 agent.py:117(_learn)
              330724074  921.704    0.000 7527.380    0.000 layers.py:727(check)
                9935132   43.449    0.000 6841.780    0.001 tensor.py:195(backward)
                9935132   41.636    0.000 6796.677    0.001 __init__.py:68(backward)
                3311714  536.946    0.000 6608.872    0.002 agent.py:216(counterfact)
                9935132 6516.250    0.001 6516.250    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3311715  536.835    0.000 6281.640    0.002 layers.py:676(update)
                7690610  220.473    0.000 6045.497    0.001 agent.py:49(__call__)
                3311714 3089.000    0.001 5796.234    0.002 replaybuffer.py:28(teleporter_save_data)
                3311714 3854.611    0.001 5133.964    0.002 replaybuffer.py:22(sample_data)
                3311714 2479.723    0.001 5063.800    0.002 agent.py:88(interveen)
                3311714 3306.434    0.001 4426.629    0.001 replaybuffer.py:49(sample_data)
               50657012  120.722    0.000 4312.820    0.000 conv.py:398(forward)
               50657012   86.683    0.000 4137.817    0.000 conv.py:390(_conv_forward)
               50657012 4051.134    0.000 4051.134    0.000 {built-in method conv2d}
               69362090  155.382    0.000 3467.666    0.000 linear.py:93(forward)
               40152071 3346.948    0.000 3346.948    0.000 {built-in method tensor}
               46364003 1941.356    0.000 3269.342    0.000 layer.py:151(update)
               69362090   64.452    0.000 3236.605    0.000 functional.py:1737(linear)
               69362090 3155.054    0.000 3155.054    0.000 {built-in method torch._C._nn.linear}
               32527482   25.027    0.000 3107.200    0.000 game.py:37(board)
                3311714 2021.098    0.001 3053.012    0.001 agent.py:67(modify)
              330724074 2092.768    0.000 2890.463    0.000 layers.py:464(check)
              330577161  509.332    0.000 2798.751    0.000 layers.py:721(isFree)
              168194546 2392.773    0.000 2392.773    0.000 {built-in method clone}
             2208208398 1911.847    0.000 2289.420    0.000 layer.py:95(isFree)
              330724074 1662.155    0.000 2247.007    0.000 layers.py:71(check)
              185455784 2075.041    0.000 2075.041    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               47431128 2052.889    0.000 2052.889    0.000 {built-in method cat}
               94690596   82.100    0.000 1957.454    0.000 activation.py:713(forward)
               94690596  103.187    0.000 1875.354    0.000 functional.py:1364(leaky_relu)
              185455784 1821.764    0.000 1821.764    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                3311704   63.268    0.000 1819.246    0.001 agent.py:167(__call__)
                1079346   27.704    0.000 1759.257    0.002 agent.py:171(choose_action)
               94690596 1753.670    0.000 1753.670    0.000 {built-in method torch._C._nn.leaky_relu}
                3311714   60.051    0.000 1708.147    0.001 agent.py:112(__call__)
               11002324   80.221    0.000 1701.824    0.000 agent.py:59(modify_board)
             6245930878 1153.158    0.000 1651.250    0.000 enum.py:646(__hash__)
                1642710   21.089    0.000 1625.647    0.001 layers.py:731(restart)
                9935132  264.722    0.000 1615.233    0.000 optimizer.py:189(zero_grad)
                1642710   10.559    0.000 1424.130    0.001 level.py:8(__init__)
                1642710   84.208    0.000 1332.799    0.001 levels.py:262(generate)
              332840505  281.515    0.000 1189.692    0.000 {built-in method builtins.any}
               20333846  192.911    0.000 1171.301    0.000 level.py:41(notUsed)
               92727892 1135.792    0.000 1135.792    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               11002324 1076.099    0.000 1076.099    0.000 {built-in method torch._C._nn.one_hot}
                3311714   82.856    0.000 1024.752    0.000 replaybuffer.py:18(stacker)
               92727892 1000.202    0.000 1000.202    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              331171500   97.541    0.000  982.865    0.000 {built-in method builtins.all}
               92727892  950.494    0.000  950.494    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               92727892  935.464    0.000  935.464    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
             1017698100  265.233    0.000  928.736    0.000 layers.py:682(<genexpr>)
             2636230320  743.645    0.000  908.178    0.000 layers.py:692(<genexpr>)
              330724074  688.440    0.000  888.674    0.000 layers.py:56(check)
                3311704   75.283    0.000  874.432    0.000 replaybuffer.py:45(stacker)
                3311714  449.532    0.000  742.184    0.000 collector.py:53(collect)
              935645218  741.220    0.000  741.220    0.000 layer.py:146(elements)
             7080576539  726.900    0.000  726.900    0.000 layer.py:91(positions)
               92727892  726.228    0.000  726.228    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                7690610  230.846    0.000  628.703    0.000 exploration.py:53(softmaxer)
              331171500  421.832    0.000  626.781    0.000 layers.py:107(isDone)
              182508574  620.992    0.000  620.992    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              649095328  493.319    0.000  608.612    0.000 tensor.py:906(grad)
                3311714  190.174    0.000  569.986    0.000 replaybuffer.py:55(CF_save_data)
        6032119613/6032119610  454.281    0.000  523.193    0.000 {built-in method builtins.len}
                9935132   14.621    0.000  519.553    0.000 loss.py:527(forward)
               20333846   21.419    0.000  516.750    0.000 level.py:38(elementsIn)
                9935132   41.659    0.000  504.932    0.000 functional.py:2898(mse_loss)
             6245968653  498.099    0.000  498.099    0.000 {built-in method builtins.hash}
              330724074  331.917    0.000  491.422    0.000 layers.py:42(check)
                6623428  183.991    0.000  487.929    0.000 random.py:315(sample)
                9935143  466.315    0.000  466.315    0.000 {built-in method nonzero}
              323677269  227.178    0.000  335.959    0.000 layer.py:126(remove)
                9935132  331.134    0.000  331.134    0.000 {built-in method torch._C._nn.mse_loss}
               20333846  163.490    0.000  326.726    0.000 level.py:39(<listcomp>)
               50657012   38.896    0.000  325.947    0.000 flatten.py:39(forward)
               19870284  309.966    0.000  309.966    0.000 {built-in method sum}
              907124487  302.840    0.000  302.840    0.000 level.py:32(inverse)
                9936232  300.623    0.000  300.623    0.000 {built-in method max}
                1079346  280.793    0.000  298.293    0.000 agent.py:182(convert_values)
               50657012  287.051    0.000  287.051    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              421706614  197.221    0.000  263.981    0.000 layer.py:130(add)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-14>
Subject: Job 9501860: <cococonuts_CF_conver3_0> in cluster <dcc> Done

Job <cococonuts_CF_conver3_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed Apr  7 15:46:06 2021
Job was executed on host(s) <n-62-20-14>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed Apr  7 16:30:45 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed Apr  7 16:30:45 2021
Terminated at Thu Apr  8 16:26:00 2021
Results reported at Thu Apr  8 16:26:00 2021

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

    CPU time :                                   85901.00 sec.
    Max Memory :                                 9632 MB
    Average Memory :                             6424.18 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               6752.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86115 sec.
    Turnaround time :                            88794 sec.

The output (if any) is above this job summary.

