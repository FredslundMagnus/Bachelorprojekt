
# Parameters

    Name :                      DoorsAndKey_simple-2
    Main :                      simple
    Level :                     Levels.Causal1
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
    Network2 :                  Networks.MiniBig
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
    Cf convert :                3
    Counterfacts :              1
    Topn :                      6
    Random counterfacts :       False
    Num :                       2
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      172614730115 function calls (172384012552 primitive calls) in 86113.72 seconds

##    Ordered by: cumulative time
   List reduced from 408 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86113.719 86113.719 {built-in method builtins.exec}
                      1    0.001    0.001 86113.718 86113.718 <string>:1(<module>)
                      1  147.384  147.384 86113.717 86113.717 main.py:67(simple)
                9613217   33.463    0.000 48246.883    0.005 game.py:42(step)
                9613217   48.351    0.000 46185.970    0.005 layers.py:827(step)
                9613217   27.345    0.000 30105.091    0.003 agent.py:29(learn)
                9613217  208.174    0.000 30058.867    0.003 agent.py:117(_learn)
                9613217  756.796    0.000 29850.693    0.003 learner.py:42(Qlearn)
                9613218 1301.826    0.000 29764.309    0.003 layers.py:793(update)
               53283681  346.710    0.000 18125.867    0.000 layers.py:849(restart)
                9613217  658.743    0.000 16319.796    0.002 layers.py:17(step)
              961321700 1409.944    0.000 15582.433    0.000 layer.py:106(move)
               53283681  170.632    0.000 14355.608    0.000 level.py:8(__init__)
                9613217   55.040    0.000 13035.414    0.001 grad_mode.py:23(decorate_context)
                9613217  317.975    0.000 12874.082    0.001 adam.py:55(step)
               53283681  551.268    0.000 12401.743    0.000 levels.py:122(generate)
              207804979 1862.294    0.000 11333.573    0.000 level.py:41(notUsed)
                9613217 2352.347    0.000 11142.479    0.001 functional.py:53(adam)
        259556859/28839651  978.059    0.000 10891.466    0.000 module.py:715(_call_impl)
               19226434   41.929    0.000 10137.050    0.001 network.py:28(forward)
               19226434  246.166    0.000 9982.881    0.001 container.py:115(forward)
              961321700 2339.587    0.000 7901.086    0.000 layers.py:844(check)
                9613217   54.762    0.000 6609.543    0.001 tensor.py:181(backward)
                9613217   32.062    0.000 6554.780    0.001 __init__.py:68(backward)
                9613217 6275.623    0.001 6275.623    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                9613217  113.752    0.000 5635.007    0.001 agent.py:112(__call__)
              207804979  144.538    0.000 5484.628    0.000 level.py:38(elementsIn)
              961321700 1248.985    0.000 4886.467    0.000 layers.py:838(isFree)
               57679308 2675.145    0.000 4345.697    0.000 layer.py:175(NoRock_update)
            17990355667 2883.688    0.000 4165.219    0.000 enum.py:646(__hash__)
             5642466617 2829.786    0.000 3637.482    0.000 layer.py:103(isFree)
              207804979 1767.375    0.000 3536.823    0.000 level.py:39(<listcomp>)
               38452868   63.279    0.000 3500.458    0.000 conv.py:422(forward)
               38452868   72.231    0.000 3413.609    0.000 conv.py:414(_conv_forward)
               57679302  122.640    0.000 3397.722    0.000 linear.py:92(forward)
             1811680598  948.645    0.000 3333.061    0.000 {built-in method builtins.any}
               38452868 3328.548    0.000 3328.548    0.000 {built-in method conv2d}
              319702086  268.240    0.000 3314.907    0.000 layer.py:77(restart)
               57679302  208.512    0.000 3221.081    0.000 functional.py:1669(linear)
              961321800  367.206    0.000 3052.064    0.000 {built-in method builtins.all}
             4013699347 1067.788    0.000 2794.790    0.000 layers.py:799(<genexpr>)
               40714603 2744.059    0.000 2744.059    0.000 {built-in method tensor}
              672925220 1704.475    0.000 2670.034    0.000 tensor.py:933(grad)
                9613217  241.454    0.000 2623.025    0.000 optimizer.py:167(zero_grad)
               53283781 1274.753    0.000 2584.284    0.000 layers.py:36(reset)
             9585422135 2325.829    0.000 2325.829    0.000 level.py:32(inverse)
              192264340 2325.089    0.000 2325.089    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               57679302 2309.140    0.000 2309.140    0.000 {built-in method addmm}
               19226434   19.311    0.000 2038.084    0.000 game.py:38(board)
              192264340 1989.922    0.000 1989.922    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
             6356266833 1564.642    0.000 1945.043    0.000 layers.py:809(<genexpr>)
            11226814421 1923.156    0.000 1923.156    0.000 enum.py:352(<genexpr>)
              207804979 1114.996    0.000 1803.267    0.000 {built-in method _functools.reduce}
               53283681  763.023    0.000 1679.597    0.000 level.py:16(<dictcomp>)
              961321800 1009.415    0.000 1561.279    0.000 layers.py:113(isDone)
             3005168353 1110.483    0.000 1517.047    0.000 layer.py:138(add)
               76905736   63.722    0.000 1508.318    0.000 activation.py:713(forward)
              961321700  937.207    0.000 1504.951    0.000 layers.py:141(check)
               76905736  100.620    0.000 1444.595    0.000 functional.py:1292(leaky_relu)
               76905736 1334.641    0.000 1334.641    0.000 {built-in method torch._C._nn.leaky_relu}
              961321700  793.922    0.000 1304.159    0.000 layers.py:124(check)
            17990394216 1281.537    0.000 1281.537    0.000 {built-in method builtins.hash}
               96132170 1264.294    0.000 1264.294    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              961321700  770.757    0.000 1223.147    0.000 layers.py:48(check)
              826736742  400.938    0.000 1185.945    0.000 overrides.py:1070(has_torch_function)
            12843044966 1158.665    0.000 1158.665    0.000 layer.py:99(positions)
               96132170 1155.993    0.000 1155.993    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
             6073102360 1090.372    0.000 1090.372    0.000 layer.py:154(elements)
               96132170 1073.470    0.000 1073.470    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                9613217  597.243    0.000 1013.223    0.000 collector.py:46(collect)
              961321700  646.396    0.000  960.256    0.000 layers.py:23(check)
               96132170  954.497    0.000  954.497    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               96132170  760.707    0.000  760.707    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
             8727809118  688.271    0.000  688.271    0.000 level.py:39(<lambda>)
             1008883209  441.884    0.000  654.396    0.000 layer.py:134(remove)
        8301724776/8301724775  534.903    0.000  598.388    0.000 {built-in method builtins.len}
             7890184862  574.896    0.000  574.896    0.000 {method 'append' of 'list' objects}
                9613217   12.330    0.000  525.914    0.000 loss.py:445(forward)
             7028128864  518.216    0.000  518.216    0.000 {method 'random' of '_random.Random' objects}
                9613217   48.004    0.000  513.584    0.000 functional.py:2637(mse_loss)
             4369270534  500.835    0.000  500.835    0.000 layer.py:190(grid)
             4709019957  478.471    0.000  478.471    0.000 layer.py:211(isBlocking)
               57679302  453.527    0.000  453.527    0.000 {method 't' of 'torch._C._TensorBase' objects}
             1711152786  348.807    0.000  433.681    0.000 overrides.py:1083(<genexpr>)
                9613217   33.200    0.000  428.987    0.000 exploration.py:47(epsilonGreedy)
             5448228714  380.401    0.000  380.401    0.000 layer.py:92(isDead)
               19226434  331.562    0.000  331.562    0.000 {built-in method sum}
                9613217  325.676    0.000  325.676    0.000 {built-in method torch._C._nn.mse_loss}
              207804979  109.491    0.000  318.004    0.000 random.py:285(choice)
                9613217  303.340    0.000  303.340    0.000 {method 'tolist' of 'torch._C._TensorBase' objects}
                9614178  284.817    0.000  284.817    0.000 {built-in method max}
               38452868   30.751    0.000  262.925    0.000 flatten.py:39(forward)
               96132220  108.757    0.000  244.099    0.000 tensor.py:596(__hash__)
                9613217  242.122    0.000  242.122    0.000 {built-in method gather}
                9613217   39.161    0.000  239.065    0.000 __init__.py:28(_make_grads)
              319702086  233.160    0.000  233.160    0.000 layer.py:147(clear2)
               38452868  232.174    0.000  232.174    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                9613217   45.136    0.000  220.038    0.000 tensor.py:506(__rsub__)
              259556859  215.500    0.000  215.500    0.000 {built-in method torch._C._get_tracing_state}
                9613217  189.564    0.000  189.564    0.000 {built-in method ones_like}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9624002: <DoorsAndKey_simple_2> in cluster <dcc> Done

Job <DoorsAndKey_simple_2> was submitted from host <n-62-30-2> by user <s183905> in cluster <dcc> at Sat May  8 23:34:14 2021
Job was executed on host(s) <n-62-20-2>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sun May  9 23:29:47 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun May  9 23:29:47 2021
Terminated at Mon May 10 23:25:08 2021
Results reported at Mon May 10 23:25:08 2021

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

    CPU time :                                   85898.38 sec.
    Max Memory :                                 2066 MB
    Average Memory :                             2063.24 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14318.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86121 sec.
    Turnaround time :                            172254 sec.

The output (if any) is above this job summary.

