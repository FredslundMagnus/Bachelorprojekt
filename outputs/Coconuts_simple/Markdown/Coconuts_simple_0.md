
# Parameters

    Name :                      Coconuts_simple-0
    Main :                      simple
    Level :                     Levels.Coconuts
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
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      177385775416 function calls (177187831533 primitive calls) in 86114.22 seconds

##    Ordered by: cumulative time
   List reduced from 418 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86114.224 86114.224 {built-in method builtins.exec}
                      1    0.001    0.001 86114.224 86114.224 <string>:1(<module>)
                      1  140.114  140.114 86114.223 86114.223 main.py:67(simple)
                8247647   28.459    0.000 58576.027    0.007 game.py:42(step)
                8247647   38.196    0.000 56795.165    0.007 layers.py:827(step)
                8247648 1170.294    0.000 30690.503    0.004 layers.py:793(update)
                8247647  702.312    0.000 26015.767    0.003 layers.py:17(step)
              824764700 2209.393    0.000 25236.520    0.000 layer.py:106(move)
                8247647   27.417    0.000 21365.643    0.003 agent.py:29(learn)
                8247647  190.416    0.000 21320.626    0.003 agent.py:117(_learn)
                8247647  550.287    0.000 21130.210    0.003 learner.py:42(Qlearn)
               24778962  205.346    0.000 18524.663    0.001 layers.py:849(restart)
              824764700 3123.286    0.000 18200.469    0.000 layers.py:844(check)
               24778962   97.211    0.000 15935.568    0.001 level.py:8(__init__)
               24778962  970.687    0.000 14882.349    0.001 levels.py:277(generate)
              221003696 2097.843    0.000 13064.484    0.000 level.py:41(notUsed)
                8247647   49.979    0.000 8613.585    0.001 grad_mode.py:23(decorate_context)
        222686469/24742941  861.021    0.000 8473.633    0.000 module.py:715(_call_impl)
                8247647  280.956    0.000 8468.509    0.001 adam.py:55(step)
               16495294   41.869    0.000 7843.465    0.000 network.py:28(forward)
               16495294  204.705    0.000 7697.473    0.000 container.py:115(forward)
                8247647 1533.844    0.000 6924.635    0.001 functional.py:53(adam)
              221003696  167.040    0.000 6271.146    0.000 level.py:38(elementsIn)
            22724746792 3822.250    0.000 5537.879    0.000 enum.py:646(__hash__)
              824764700 3848.607    0.000 5522.407    0.000 layers.py:471(check)
               57733536 3521.921    0.000 5258.689    0.000 layer.py:159(update)
                8247647   46.983    0.000 4731.414    0.001 tensor.py:181(backward)
              824764700 3359.114    0.000 4686.842    0.000 layers.py:77(check)
                8247647   29.014    0.000 4684.431    0.001 __init__.py:68(backward)
                8247647 4464.821    0.001 4464.821    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                8247647   97.391    0.000 4398.133    0.001 agent.py:112(__call__)
              221003696 2013.651    0.000 4061.874    0.000 level.py:39(<listcomp>)
              824764700  883.271    0.000 3642.905    0.000 layers.py:838(isFree)
             1575264737  946.613    0.000 3472.514    0.000 {built-in method builtins.any}
             3676299147 2197.480    0.000 2759.634    0.000 layer.py:103(isFree)
               32990588   59.426    0.000 2747.676    0.000 conv.py:422(forward)
            10186165629 2746.020    0.000 2746.020    0.000 level.py:32(inverse)
               32990588   66.214    0.000 2666.033    0.000 conv.py:414(_conv_forward)
              824764800  454.073    0.000 2624.626    0.000 {built-in method builtins.all}
               32990588 2587.927    0.000 2587.927    0.000 {built-in method conv2d}
               49485882  112.459    0.000 2578.384    0.000 linear.py:92(forward)
               34976818 2441.475    0.000 2441.475    0.000 {built-in method tensor}
               49485882  185.144    0.000 2415.078    0.000 functional.py:1669(linear)
              173452734  327.372    0.000 2323.455    0.000 layer.py:77(restart)
             4920658454 1384.315    0.000 2271.260    0.000 layers.py:799(<genexpr>)
              577335320 1352.994    0.000 2258.593    0.000 tensor.py:933(grad)
              824764700 1714.192    0.000 2248.744    0.000 layers.py:62(check)
             6399886704 1741.277    0.000 2115.828    0.000 layers.py:809(<genexpr>)
              221003696 1265.593    0.000 2042.232    0.000 {built-in method _functools.reduce}
            10568656378 1986.107    0.000 1986.107    0.000 enum.py:352(<genexpr>)
                8247647  181.315    0.000 1936.100    0.000 optimizer.py:167(zero_grad)
               16495294   17.130    0.000 1901.933    0.000 game.py:38(board)
            16803971481 1746.659    0.000 1746.659    0.000 layer.py:99(positions)
            22724779861 1715.635    0.000 1715.635    0.000 {built-in method builtins.hash}
               49485882 1700.187    0.000 1700.187    0.000 {built-in method addmm}
              164952940 1400.872    0.000 1400.872    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               24779062  638.183    0.000 1282.224    0.000 layers.py:36(reset)
              164952940 1175.875    0.000 1175.875    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
             4706550057 1119.781    0.000 1119.781    0.000 layer.py:154(elements)
             2297425160  824.979    0.000 1109.962    0.000 layer.py:138(add)
              709297722  375.633    0.000 1106.479    0.000 overrides.py:1070(has_torch_function)
               65981176   53.458    0.000 1082.814    0.000 activation.py:713(forward)
              824764700  691.190    0.000 1064.867    0.000 layers.py:48(check)
               65981176   89.564    0.000 1029.357    0.000 functional.py:1292(leaky_relu)
              824764700  639.263    0.000  946.110    0.000 layers.py:23(check)
               65981176  930.730    0.000  930.730    0.000 {built-in method torch._C._nn.leaky_relu}
               24778962  413.011    0.000  889.872    0.000 level.py:16(<dictcomp>)
               82476470  795.054    0.000  795.054    0.000 {method 'add' of 'torch._C._TensorBase' objects}
             9282155232  776.639    0.000  776.639    0.000 level.py:39(<lambda>)
               82476470  749.262    0.000  749.262    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                8247647  422.759    0.000  731.267    0.000 collector.py:46(collect)
               82476470  664.072    0.000  664.072    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               82476470  581.396    0.000  581.396    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
        7345758133/7345758132  493.006    0.000  548.000    0.000 {built-in method builtins.len}
             6606365247  527.353    0.000  527.353    0.000 {method 'random' of '_random.Random' objects}
             6654311201  450.346    0.000  450.346    0.000 {method 'append' of 'list' objects}
               82476470  444.891    0.000  444.891    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                8247647   11.590    0.000  421.317    0.000 loss.py:445(forward)
                8247647   48.019    0.000  409.727    0.000 functional.py:2637(mse_loss)
             1468081326  328.438    0.000  404.635    0.000 overrides.py:1083(<genexpr>)
             1649529400  398.847    0.000  398.847    0.000 {method 'union' of 'set' objects}
             3676299147  397.533    0.000  397.533    0.000 layer.py:211(isBlocking)
              424587266  214.694    0.000  384.734    0.000 layer.py:134(remove)
                8247647   31.445    0.000  378.480    0.000 exploration.py:47(epsilonGreedy)
              824764800  250.214    0.000  344.030    0.000 layers.py:52(isDone)
              171445772   69.873    0.000  323.743    0.000 random.py:244(randint)
              808251747  228.205    0.000  323.732    0.000 layers.py:508(isDone)
             4799915028  317.215    0.000  317.215    0.000 layer.py:92(isDead)
               49485882  306.505    0.000  306.505    0.000 {method 't' of 'torch._C._TensorBase' objects}
             2031883658  275.581    0.000  275.581    0.000 layer.py:190(grid)
                8247647  254.077    0.000  254.077    0.000 {method 'tolist' of 'torch._C._TensorBase' objects}
              171445772  109.032    0.000  253.870    0.000 random.py:200(randrange)
                8247647  237.112    0.000  237.112    0.000 {built-in method torch._C._nn.mse_loss}
               16495294  235.139    0.000  235.139    0.000 {built-in method sum}
               82476520   99.686    0.000  227.297    0.000 tensor.py:596(__hash__)
                8248471  216.878    0.000  216.878    0.000 {built-in method max}
              221003696  134.456    0.000  197.380    0.000 random.py:250(_randbelow_with_getrandbits)
               57733536  193.822    0.000  193.822    0.000 layer.py:171(<listcomp>)
                8247647   33.297    0.000  183.154    0.000 __init__.py:28(_make_grads)
               32990588   23.404    0.000  179.003    0.000 flatten.py:39(forward)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9578858: <Coconuts_simple_0> in cluster <dcc> Done

Job <Coconuts_simple_0> was submitted from host <n-62-30-3> by user <s183905> in cluster <dcc> at Mon Apr 26 20:44:08 2021
Job was executed on host(s) <n-62-20-10>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Thu May  6 12:36:40 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu May  6 12:36:40 2021
Terminated at Fri May  7 12:32:29 2021
Results reported at Fri May  7 12:32:29 2021

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

    CPU time :                                   85900.88 sec.
    Max Memory :                                 2066 MB
    Average Memory :                             2060.38 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14318.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86150 sec.
    Turnaround time :                            920901 sec.

The output (if any) is above this job summary.

