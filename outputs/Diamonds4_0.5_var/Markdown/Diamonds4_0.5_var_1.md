
# Parameters

    Name :                      Diamonds4_0.5_var-1
    Main :                      graphTrain
    Level :                     Levels.Causal7
    Failed actions chance :     0.5
    Hours :                     10.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.var
    Network1 :                  Networks.Teleporter
    K1 :                        200000.0
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
    K2 :                        100000.0
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
    Softmax cap :               0.0
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                3
    Counterfacts :              2
    Topn :                      5
    Random counterfacts :       False
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      15293331786 function calls (14785857785 primitive calls) in 35708.22 seconds

##    Ordered by: cumulative time
   List reduced from 467 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35708.216 35708.216 {built-in method builtins.exec}
                      1    0.001    0.001 35708.216 35708.216 <string>:1(<module>)
                      1  149.584  149.584 35708.215 35708.215 allGraphsTrain.py:10(graphTrain)
                 604318 6405.178    0.011 14436.999    0.024 allGraphs.py:146(transformNot)
                 604318   15.611    0.000 8775.746    0.015 allGraphsTrain.py:29(<listcomp>)
               61036219 2281.553    0.000 8760.186    0.000 allGraphs.py:110(states)
              604323232 8145.648    0.000 8145.648    0.000 {method 'item' of 'torch._C._TensorBase' objects}
              543886600 7034.276    0.000 7034.276    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 604318  710.873    0.001 3121.955    0.005 allGraphsTrain.py:35(<listcomp>)
                 604318    2.227    0.000 2516.419    0.004 game.py:41(step)
               13563828   23.041    0.000 2411.082    0.000 allGraphs.py:158(getInterventions)
                 604318    2.792    0.000 2382.038    0.004 layers.py:718(step)
                 604318  162.237    0.000 2155.312    0.004 allGraphsTrain.py:37(<listcomp>)
               19156536 1656.417    0.000 1656.417    0.000 {built-in method tensor}
                 604318    2.016    0.000 1606.281    0.003 agent.py:29(learn)
                 604318   12.389    0.000 1602.924    0.003 agent.py:117(_learn)
                 604318   46.468    0.000 1590.535    0.003 learner.py:42(Qlearn)
               16585419    9.088    0.000 1568.166    0.000 game.py:37(board)
                 604319   80.579    0.000 1365.776    0.002 layers.py:684(update)
               13563828   58.442    0.000 1329.173    0.000 allGraphs.py:153(format)
               64057708  160.843    0.000 1316.029    0.000 tensor.py:21(wrapped)
                 604318   56.875    0.000 1262.323    0.002 allGraphsTrain.py:44(<listcomp>)
               12508636   10.420    0.000 1044.456    0.000 allGraphs.py:129(rightIntervention)
                 604318   42.659    0.000 1010.171    0.002 layers.py:17(step)
        112639507/12508636   69.626    0.000  987.891    0.000 {built-in method builtins.min}
               63453390  978.502    0.000  978.502    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               31632455   12.784    0.000  969.247    0.000 allGraphs.py:130(<lambda>)
               60431800   90.881    0.000  962.169    0.000 layer.py:98(move)
        212770378/31632455  299.451    0.000  956.463    0.000 allGraphs.py:74(expected_moves)
               60431800  892.102    0.000  892.102    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
        281268794/67150330   78.318    0.000  788.247    0.000 allGraphs.py:78(<genexpr>)
                 604318  386.283    0.001  682.418    0.001 agent.py:67(modify)
                1877388   14.796    0.000  679.809    0.000 layers.py:740(restart)
                 604318    3.691    0.000  675.139    0.001 grad_mode.py:23(decorate_context)
                 604318   17.431    0.000  664.980    0.001 adam.py:55(step)
        13899314/1812954   54.893    0.000  578.562    0.000 module.py:715(_call_impl)
                 604318  120.972    0.000  573.544    0.001 functional.py:53(adam)
                1877388    7.187    0.000  545.328    0.000 level.py:8(__init__)
                1208636    3.106    0.000  530.357    0.000 network.py:27(forward)
             2184715343  359.358    0.000  523.222    0.000 enum.py:646(__hash__)
                1208636   13.594    0.000  520.272    0.000 container.py:115(forward)
               60431800  121.790    0.000  476.561    0.000 layers.py:735(check)
                1877388   20.086    0.000  472.766    0.000 levels.py:441(generate)
                9011659   78.086    0.000  431.802    0.000 level.py:41(notUsed)
                 604318    3.296    0.000  361.505    0.001 tensor.py:181(backward)
                 604318    2.010    0.000  358.209    0.001 __init__.py:68(backward)
                 604318  340.954    0.001  340.954    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
              113694699   65.145    0.000  316.015    0.000 allGraphs.py:83(layers_not_in)
               60431800   84.143    0.000  310.658    0.000 layers.py:729(isFree)
                 604318    7.602    0.000  305.414    0.001 agent.py:112(__call__)
               62849072  295.567    0.000  295.567    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              167331887   85.459    0.000  293.578    0.000 {built-in method builtins.any}
                4230233  147.882    0.000  255.481    0.000 layer.py:167(NoRock_update)
              113694699  123.526    0.000  250.869    0.000 allGraphs.py:84(<listcomp>)
              412462904  177.204    0.000  226.515    0.000 layer.py:95(isFree)
                9011659    6.376    0.000  205.211    0.000 level.py:38(elementsIn)
                2417272    4.185    0.000  204.302    0.000 conv.py:422(forward)
                1812954    6.963    0.000  200.868    0.000 tensor.py:576(__iter__)
                2417272    4.574    0.000  198.628    0.000 conv.py:414(_conv_forward)
                2417272  193.267    0.000  193.267    0.000 {built-in method conv2d}
                1812954  188.997    0.000  188.997    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
              124489608   34.307    0.000  185.053    0.000 {built-in method builtins.all}
              105151466   52.026    0.000  169.189    0.000 overrides.py:1070(has_torch_function)
             2184717356  163.864    0.000  163.864    0.000 {built-in method builtins.hash}
                2417272    5.315    0.000  155.251    0.000 linear.py:92(forward)
              212770378  102.231    0.000  150.089    0.000 allGraphs.py:45(p)
                2417272   10.008    0.000  147.553    0.000 functional.py:1669(linear)
              468436096  115.512    0.000  141.350    0.000 layers.py:700(<genexpr>)
               33841862   87.619    0.000  138.388    0.000 tensor.py:933(grad)
                9011659   68.431    0.000  135.320    0.000 level.py:39(<listcomp>)
                 604318   13.060    0.000  134.912    0.000 optimizer.py:167(zero_grad)
              143653280   32.979    0.000  134.873    0.000 layers.py:690(<genexpr>)
                9669088  120.121    0.000  120.121    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                 604318   69.520    0.000  116.471    0.000 collector.py:46(collect)
               13141716    9.543    0.000  115.388    0.000 layer.py:69(restart)
                2417272  106.333    0.000  106.333    0.000 {built-in method addmm}
                9669088  102.229    0.000  102.229    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                 604318    4.816    0.000  101.824    0.000 agent.py:59(modify_board)
               60431900   62.480    0.000   95.308    0.000 layers.py:113(isDone)
                1877488   46.118    0.000   91.279    0.000 layers.py:36(reset)
              432671941   87.824    0.000   87.824    0.000 level.py:32(inverse)
               30217600   51.628    0.000   84.365    0.000 layers.py:602(check)
               30208722   50.232    0.000   82.963    0.000 layers.py:617(check)
               30214465   49.914    0.000   82.189    0.000 layers.py:632(check)
              823760964   73.811    0.000   73.811    0.000 layer.py:91(positions)
                3625908    3.072    0.000   73.595    0.000 activation.py:713(forward)
                3625908    4.849    0.000   70.523    0.000 functional.py:1292(leaky_relu)
              276777912   56.063    0.000   66.407    0.000 overrides.py:1083(<genexpr>)
              392007185   66.315    0.000   66.315    0.000 enum.py:352(<genexpr>)
                4834544   65.437    0.000   65.437    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                3625908   65.213    0.000   65.213    0.000 {built-in method torch._C._nn.leaky_relu}
                 604318   64.460    0.000   64.460    0.000 {built-in method torch._C._nn.one_hot}
              255456000   64.013    0.000   64.013    0.000 layer.py:146(elements)
                9011659   39.729    0.000   63.515    0.000 {built-in method _functools.reduce}
                 604318   41.385    0.000   61.529    0.000 allGraphsTrain.py:43(<listcomp>)
              124243227   44.884    0.000   61.176    0.000 layer.py:130(add)
                1877388   32.422    0.000   60.922    0.000 level.py:16(<dictcomp>)
                4834544   59.357    0.000   59.357    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                4834544   54.909    0.000   54.909    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                 604318   12.703    0.000   50.942    0.000 allGraphs.py:137(transform)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9532019: <Diamonds4_0.5_var_1> in cluster <dcc> Done

Job <Diamonds4_0.5_var_1> was submitted from host <n-62-30-7> by user <s183905> in cluster <dcc> at Sat Apr 17 13:28:42 2021
Job was executed on host(s) <n-62-20-3>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sun Apr 18 19:44:26 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun Apr 18 19:44:26 2021
Terminated at Mon Apr 19 05:39:39 2021
Results reported at Mon Apr 19 05:39:39 2021

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
#BSUB -W 720
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $LSB_PROJECT_NAME


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   35618.04 sec.
    Max Memory :                                 2064 MB
    Average Memory :                             2063.89 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14320.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35715 sec.
    Turnaround time :                            144657 sec.

The output (if any) is above this job summary.

