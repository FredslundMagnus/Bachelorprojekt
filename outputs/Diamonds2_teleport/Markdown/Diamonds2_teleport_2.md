
# Parameters

    Name :                      Diamonds2_teleport-2
    Main :                      teleport
    Level :                     Levels.Causal5
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
    Topn :                      6
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      95303552140 function calls (95034651369 primitive calls) in 86111.95 seconds

##    Ordered by: cumulative time
   List reduced from 474 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86111.947 86111.947 {built-in method builtins.exec}
                      1    1.552    1.552 86111.947 86111.947 <string>:1(<module>)
                      1  201.472  201.472 86110.394 86110.394 main.py:45(teleport)
                4802222   18.370    0.000 25716.532    0.005 game.py:41(step)
                9604444   34.366    0.000 25639.986    0.003 agent.py:29(learn)
                4802222   24.963    0.000 24640.106    0.005 layers.py:718(step)
                9604444  614.793    0.000 21580.809    0.002 learner.py:42(Qlearn)
                4802222  149.590    0.000 15487.228    0.003 agent.py:54(_learn)
                4802222  367.237    0.000 14509.386    0.003 layers.py:17(step)
              480222200  770.530    0.000 14099.442    0.000 layer.py:98(move)
                4802222 6516.149    0.001 11806.404    0.002 replaybuffer.py:28(teleporter_save_data)
        302513258/33613498 1092.439    0.000 10643.187    0.000 module.py:715(_call_impl)
                4802222  126.194    0.000 10100.381    0.002 agent.py:117(_learn)
                4802223  635.014    0.000 10072.454    0.002 layers.py:684(update)
               24009054   55.554    0.000 9934.579    0.000 network.py:27(forward)
               24009054  260.800    0.000 9742.967    0.000 container.py:115(forward)
              480222200 1855.354    0.000 9188.432    0.000 layers.py:735(check)
                4802222 5869.808    0.001 9140.645    0.002 agent.py:88(interveen)
                9604444   55.086    0.000 8653.437    0.001 grad_mode.py:23(decorate_context)
                9604444  282.255    0.000 8496.410    0.001 adam.py:55(step)
                9604444 1576.003    0.000 6989.479    0.001 functional.py:53(adam)
                9602388  199.226    0.000 6585.846    0.001 agent.py:49(__call__)
                4802222 3719.254    0.001 5751.286    0.001 replaybuffer.py:22(sample_data)
                9604444   53.308    0.000 5073.084    0.001 tensor.py:181(backward)
                9604444   32.527    0.000 5019.775    0.001 __init__.py:68(backward)
                9604444 4777.091    0.000 4777.091    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                4802222 2292.495    0.000 4338.120    0.001 agent.py:67(modify)
              425613419 4193.041    0.000 4193.041    0.000 {built-in method clone}
                7712361   76.672    0.000 3721.972    0.000 layers.py:740(restart)
               48018108   76.321    0.000 3625.198    0.000 conv.py:422(forward)
               48018108   89.028    0.000 3517.770    0.000 conv.py:414(_conv_forward)
               48018108 3413.307    0.000 3413.307    0.000 {built-in method conv2d}
              480222200  856.643    0.000 3380.909    0.000 layers.py:729(isFree)
               62422718  127.630    0.000 3098.549    0.000 linear.py:92(forward)
                7712361   37.114    0.000 3078.686    0.000 level.py:8(__init__)
               62422718  217.313    0.000 2909.433    0.000 functional.py:1669(linear)
                7712361  112.757    0.000 2710.002    0.000 levels.py:249(generate)
               43220007 1530.646    0.000 2677.943    0.000 layer.py:167(NoRock_update)
             1341701422  742.867    0.000 2630.346    0.000 {built-in method builtins.any}
             4260941116 2041.875    0.000 2524.266    0.000 layer.py:95(isFree)
               50130274  443.363    0.000 2478.445    0.000 level.py:41(notUsed)
             9605696556 1617.082    0.000 2334.609    0.000 enum.py:646(__hash__)
              605080026 1322.864    0.000 2190.548    0.000 tensor.py:933(grad)
                4802222   58.351    0.000 2077.521    0.000 agent.py:112(__call__)
               62422718 2060.486    0.000 2060.486    0.000 {built-in method addmm}
               38415720 2034.276    0.000 2034.276    0.000 {built-in method cat}
               14404610   92.628    0.000 1994.497    0.000 agent.py:59(modify_board)
                9604444  177.828    0.000 1910.608    0.000 optimizer.py:167(zero_grad)
                4802222   74.329    0.000 1693.324    0.000 replaybuffer.py:18(stacker)
               20506572 1556.140    0.000 1556.140    0.000 {built-in method tensor}
             4725099390 1191.163    0.000 1440.612    0.000 layers.py:700(<genexpr>)
              172879992 1397.747    0.000 1397.747    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              480222200  859.028    0.000 1366.707    0.000 layers.py:387(check)
               86431772   68.885    0.000 1356.999    0.000 activation.py:713(forward)
              480222200  817.058    0.000 1316.802    0.000 layers.py:349(check)
              480222200  801.702    0.000 1290.954    0.000 layers.py:337(check)
               86431772  102.551    0.000 1288.115    0.000 functional.py:1292(leaky_relu)
               14404610 1284.515    0.000 1284.515    0.000 {built-in method torch._C._nn.one_hot}
              480222200  789.314    0.000 1270.313    0.000 layers.py:375(check)
                9604444   10.943    0.000 1252.762    0.000 game.py:37(board)
              787559876  390.350    0.000 1184.860    0.000 overrides.py:1070(has_torch_function)
              440018029 1175.894    0.000 1175.894    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               86431772 1175.712    0.000 1175.712    0.000 {built-in method torch._C._nn.leaky_relu}
              172879992 1169.493    0.000 1169.493    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               50130274   35.553    0.000 1148.815    0.000 level.py:38(elementsIn)
               33618006  168.216    0.000 1129.842    0.000 tensor.py:21(wrapped)
            11074027630 1038.724    0.000 1038.724    0.000 layer.py:91(positions)
              513840306  163.085    0.000 1021.547    0.000 {built-in method builtins.all}
             1608218962  416.534    0.000  892.875    0.000 layers.py:690(<genexpr>)
                4802222  480.153    0.000  830.003    0.000 collector.py:46(collect)
               86439996  824.752    0.000  824.752    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               86439996  759.319    0.000  759.319    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               50130274  368.836    0.000  742.638    0.000 level.py:39(<listcomp>)
             9605731515  717.533    0.000  717.533    0.000 {built-in method builtins.hash}
             1602567534  693.992    0.000  693.992    0.000 layer.py:146(elements)
                9602388  250.715    0.000  689.661    0.000 exploration.py:53(softmaxer)
               86439996  657.517    0.000  657.517    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              480222200  387.050    0.000  605.487    0.000 layers.py:326(check)
              480222200  378.722    0.000  586.750    0.000 layers.py:364(check)
               86439996  582.556    0.000  582.556    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               69411249   61.405    0.000  544.146    0.000 layer.py:69(restart)
             2364316496  538.232    0.000  538.232    0.000 level.py:32(inverse)
        6005013657/6005013655  395.335    0.000  525.006    0.000 {built-in method builtins.len}
              480222200  335.285    0.000  490.632    0.000 layers.py:23(check)
                9604444   13.991    0.000  455.136    0.000 loss.py:445(forward)
               86439996  452.447    0.000  452.447    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                9604444   49.134    0.000  441.145    0.000 functional.py:2637(mse_loss)
             1671159516  357.272    0.000  441.034    0.000 overrides.py:1083(<genexpr>)
              761886555  307.428    0.000  424.821    0.000 layer.py:130(add)
               24011110  420.835    0.000  420.835    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
             4260941116  398.370    0.000  398.370    0.000 layer.py:203(isBlocking)
                7712461  193.496    0.000  386.934    0.000 layers.py:36(reset)
             4853298388  371.903    0.000  371.903    0.000 {method 'random' of '_random.Random' objects}
               50130274  229.127    0.000  370.623    0.000 {built-in method _functools.reduce}
             2082336422  369.549    0.000  369.549    0.000 enum.py:352(<genexpr>)
               62422718  366.623    0.000  366.623    0.000 {method 't' of 'torch._C._TensorBase' objects}
              494478587  241.376    0.000  357.086    0.000 layer.py:126(remove)
               28813332  337.356    0.000  337.356    0.000 {built-in method sum}
                4802222  121.634    0.000  330.683    0.000 random.py:315(sample)
                7712361  181.636    0.000  308.292    0.000 level.py:16(<dictcomp>)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9550901: <Diamonds2_teleport_2> in cluster <dcc> Done

Job <Diamonds2_teleport_2> was submitted from host <n-62-30-4> by user <s183905> in cluster <dcc> at Tue Apr 20 16:21:48 2021
Job was executed on host(s) <n-62-20-3>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Thu Apr 22 14:00:43 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Apr 22 14:00:43 2021
Terminated at Fri Apr 23 13:56:02 2021
Results reported at Fri Apr 23 13:56:02 2021

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

    CPU time :                                   85902.03 sec.
    Max Memory :                                 2675 MB
    Average Memory :                             2671.43 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13709.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86127 sec.
    Turnaround time :                            250454 sec.

The output (if any) is above this job summary.

