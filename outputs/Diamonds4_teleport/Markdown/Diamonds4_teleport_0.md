
# Parameters

    Name :                      Diamonds4_teleport-0
    Main :                      teleport
    Level :                     Levels.Causal7
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


      68848072318 function calls (68621864599 primitive calls) in 86105.46 seconds

##    Ordered by: cumulative time
   List reduced from 475 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86105.463 86105.463 {built-in method builtins.exec}
                      1    1.511    1.511 86105.463 86105.463 <string>:1(<module>)
                      1  180.113  180.113 86103.952 86103.952 main.py:45(teleport)
                8079378   29.472    0.000 29091.141    0.004 agent.py:29(learn)
                8079378  680.623    0.000 25006.551    0.003 learner.py:42(Qlearn)
                4039689   15.372    0.000 18667.046    0.005 game.py:41(step)
                4039689   21.001    0.000 17734.057    0.004 layers.py:718(step)
                4039689  134.165    0.000 17433.045    0.004 agent.py:54(_learn)
                4039689 7441.137    0.002 14416.383    0.004 replaybuffer.py:28(teleporter_save_data)
                4039689  114.715    0.000 11612.559    0.003 agent.py:117(_learn)
        254483208/28276500 1025.989    0.000 11255.815    0.000 module.py:715(_call_impl)
                4039689 7297.387    0.002 10734.682    0.003 agent.py:88(interveen)
                8079378   49.801    0.000 10731.045    0.001 grad_mode.py:23(decorate_context)
                8079378  272.291    0.000 10589.145    0.001 adam.py:55(step)
               20197122   53.648    0.000 10545.881    0.001 network.py:27(forward)
               20197122  287.707    0.000 10370.213    0.001 container.py:115(forward)
                4039689  317.300    0.000 9822.045    0.002 layers.py:17(step)
              403968900  669.452    0.000 9470.132    0.000 layer.py:98(move)
                8079378 1938.581    0.000 9155.267    0.001 functional.py:53(adam)
                4039690  571.053    0.000 7866.134    0.002 layers.py:684(update)
                8078055  183.452    0.000 6882.181    0.001 agent.py:49(__call__)
              403968900 1283.406    0.000 5863.459    0.000 layers.py:735(check)
                8079378   55.443    0.000 5777.565    0.001 tensor.py:181(backward)
                8079378   29.383    0.000 5722.122    0.001 __init__.py:68(backward)
                8079378 5477.104    0.001 5477.104    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
              374667968 5442.911    0.000 5442.911    0.000 {built-in method clone}
                4039689 2545.203    0.001 4695.713    0.001 agent.py:67(modify)
                4039689 2795.051    0.001 4687.958    0.001 replaybuffer.py:22(sample_data)
               40394244   69.923    0.000 3744.234    0.000 conv.py:422(forward)
               40394244   79.527    0.000 3647.263    0.000 conv.py:414(_conv_forward)
               40394244 3552.112    0.000 3552.112    0.000 {built-in method conv2d}
               52511988  122.081    0.000 3366.837    0.000 linear.py:92(forward)
               52511988  209.500    0.000 3190.078    0.000 functional.py:1669(linear)
                7800760   68.419    0.000 3021.541    0.000 layers.py:740(restart)
                7800760   34.601    0.000 2414.264    0.000 level.py:8(__init__)
              403968900  611.915    0.000 2311.763    0.000 layers.py:729(isFree)
               52511988 2293.759    0.000 2293.759    0.000 {built-in method addmm}
              509000868 1388.736    0.000 2179.568    0.000 tensor.py:933(grad)
                4039689   55.973    0.000 2172.505    0.001 agent.py:112(__call__)
                8079378  208.129    0.000 2133.957    0.000 optimizer.py:167(zero_grad)
                7800760   90.792    0.000 2067.628    0.000 levels.py:441(generate)
               12117744   86.575    0.000 2042.208    0.000 agent.py:59(modify_board)
             1127345453  594.585    0.000 1996.969    0.000 {built-in method builtins.any}
               32316189 1996.347    0.000 1996.347    0.000 {built-in method cat}
              145428804 1900.676    0.000 1900.676    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               37445917  346.334    0.000 1884.101    0.000 level.py:41(notUsed)
               28277830 1073.523    0.000 1853.099    0.000 layer.py:167(NoRock_update)
             2814461139 1347.299    0.000 1699.848    0.000 layer.py:95(isFree)
             6645843860 1136.272    0.000 1681.592    0.000 enum.py:646(__hash__)
              386785712 1651.279    0.000 1651.279    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              145428804 1611.450    0.000 1611.450    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                4039689   68.389    0.000 1603.788    0.000 replaybuffer.py:18(stacker)
               72709110   61.288    0.000 1558.119    0.000 activation.py:713(forward)
               72709110  104.316    0.000 1496.831    0.000 functional.py:1292(leaky_relu)
               72709110 1383.669    0.000 1383.669    0.000 {built-in method torch._C._nn.leaky_relu}
               12117744 1272.252    0.000 1272.252    0.000 {built-in method torch._C._nn.one_hot}
               17301579 1269.530    0.000 1269.530    0.000 {built-in method tensor}
              403968900  702.163    0.000 1138.700    0.000 layers.py:602(check)
              403968900  705.109    0.000 1132.234    0.000 layers.py:632(check)
               72714402 1094.175    0.000 1094.175    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              403968900  662.424    0.000 1089.736    0.000 layers.py:617(check)
               28279927  155.196    0.000 1083.721    0.000 tensor.py:21(wrapped)
              662506468  368.863    0.000 1074.976    0.000 overrides.py:1070(has_torch_function)
                4039689  601.014    0.000 1009.079    0.000 collector.py:46(collect)
             3169345920  813.213    0.000 1003.348    0.000 layers.py:700(<genexpr>)
              432248927  115.753    0.000  972.871    0.000 {built-in method builtins.all}
               72714402  955.502    0.000  955.502    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                8079378    9.073    0.000  947.143    0.000 game.py:37(board)
              855257813  195.080    0.000  888.704    0.000 layers.py:690(<genexpr>)
               37445917   28.505    0.000  886.794    0.000 level.py:38(elementsIn)
               72714402  860.079    0.000  860.079    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               72714402  771.582    0.000  771.582    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                8078055  263.565    0.000  737.289    0.000 exploration.py:53(softmaxer)
             7693192981  725.873    0.000  725.873    0.000 layer.py:91(positions)
              403969000  449.717    0.000  677.444    0.000 layers.py:113(isDone)
               72714402  606.258    0.000  606.258    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               37445917  284.359    0.000  577.477    0.000 level.py:39(<listcomp>)
             6645873275  545.326    0.000  545.326    0.000 {built-in method builtins.hash}
               54605320   45.128    0.000  520.179    0.000 layer.py:69(restart)
              403968900  318.577    0.000  496.393    0.000 layers.py:588(check)
                8079378   11.192    0.000  471.002    0.000 loss.py:445(forward)
             1404252851  468.537    0.000  468.537    0.000 layer.py:146(elements)
               20198445  465.835    0.000  465.835    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                8079378   43.608    0.000  459.810    0.000 functional.py:2637(mse_loss)
               52511988  446.054    0.000  446.054    0.000 {method 't' of 'torch._C._TensorBase' objects}
        4258805727/4258805725  318.013    0.000  441.890    0.000 {built-in method builtins.len}
              403968900  290.756    0.000  427.171    0.000 layers.py:23(check)
               24238134  404.803    0.000  404.803    0.000 {built-in method sum}
                7800860  200.688    0.000  400.588    0.000 layers.py:36(reset)
             1405804044  317.769    0.000  393.712    0.000 overrides.py:1083(<genexpr>)
             1797867539  387.503    0.000  387.503    0.000 level.py:32(inverse)
              677721176  270.493    0.000  371.061    0.000 layer.py:130(add)
               40394244   35.689    0.000  296.593    0.000 flatten.py:39(forward)
                7800760  166.066    0.000  291.720    0.000 level.py:16(<dictcomp>)
                8079378  290.620    0.000  290.620    0.000 {built-in method torch._C._nn.mse_loss}
             1628881862  288.427    0.000  288.427    0.000 enum.py:352(<genexpr>)
              411187031  193.507    0.000  285.471    0.000 layer.py:126(remove)
                4039689  103.677    0.000  281.795    0.000 random.py:315(sample)
             2814461139  281.784    0.000  281.784    0.000 layer.py:203(isBlocking)
               37445917  176.412    0.000  280.812    0.000 {built-in method _functools.reduce}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9550905: <Diamonds4_teleport_0> in cluster <dcc> Done

Job <Diamonds4_teleport_0> was submitted from host <n-62-30-4> by user <s183905> in cluster <dcc> at Tue Apr 20 16:21:49 2021
Job was executed on host(s) <n-62-11-13>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Fri Apr 23 07:29:04 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Fri Apr 23 07:29:04 2021
Terminated at Sat Apr 24 07:24:13 2021
Results reported at Sat Apr 24 07:24:13 2021

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

    CPU time :                                   86001.55 sec.
    Max Memory :                                 2677 MB
    Average Memory :                             2674.46 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13707.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86110 sec.
    Turnaround time :                            313344 sec.

The output (if any) is above this job summary.

