
# Parameters

    Name :                      SuperLevel1_teleport-0
    Main :                      teleport
    Level :                     Levels.SuperLevel
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


      105918593750 function calls (105681626143 primitive calls) in 86105.06 seconds

##    Ordered by: cumulative time
   List reduced from 489 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86105.060 86105.060 {built-in method builtins.exec}
                      1    1.533    1.533 86105.060 86105.060 <string>:1(<module>)
                      1  191.410  191.410 86103.527 86103.527 main.py:45(teleport)
                4242470   17.572    0.000 32312.845    0.008 game.py:41(step)
                4242470   21.970    0.000 31084.317    0.007 layers.py:718(step)
                8484940   29.299    0.000 28895.014    0.003 agent.py:29(learn)
                8484940  693.026    0.000 24719.888    0.003 learner.py:42(Qlearn)
                4242470  353.661    0.000 22538.530    0.005 layers.py:17(step)
              424247000 1437.810    0.000 22149.415    0.000 layer.py:98(move)
                4242470  137.993    0.000 17389.183    0.004 agent.py:54(_learn)
              424247000 2643.576    0.000 15340.078    0.000 layers.py:735(check)
                4242470  111.547    0.000 11458.537    0.003 agent.py:117(_learn)
        266612909/29646313 1021.502    0.000 11234.122    0.000 module.py:715(_call_impl)
                8484940   51.060    0.000 10553.006    0.001 grad_mode.py:23(decorate_context)
               21161373   51.066    0.000 10515.332    0.000 network.py:27(forward)
                8484940  266.836    0.000 10406.860    0.001 adam.py:55(step)
               21161373  258.138    0.000 10346.360    0.000 container.py:115(forward)
                8484940 1905.658    0.000 8976.192    0.001 functional.py:53(adam)
                4242471  565.931    0.000 8494.872    0.002 layers.py:684(update)
                8433963  187.236    0.000 6892.677    0.001 agent.py:49(__call__)
                4242470 2670.990    0.001 6077.452    0.001 agent.py:88(interveen)
                8484940   51.365    0.000 5673.464    0.001 tensor.py:181(backward)
                8484940   28.245    0.000 5622.100    0.001 __init__.py:68(backward)
                8484940 5374.465    0.001 5374.465    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                4242470 3194.811    0.001 5128.687    0.001 replaybuffer.py:22(sample_data)
                4242470 2613.895    0.001 5054.475    0.001 replaybuffer.py:28(teleporter_save_data)
                4242470 2372.118    0.001 4557.162    0.001 agent.py:67(modify)
              424247000  984.269    0.000 4444.062    0.000 layers.py:729(isFree)
               42322746   69.099    0.000 3756.311    0.000 conv.py:422(forward)
               42322746   79.185    0.000 3658.183    0.000 conv.py:414(_conv_forward)
               42322746 3564.949    0.000 3564.949    0.000 {built-in method conv2d}
             5023515881 2716.478    0.000 3459.793    0.000 layer.py:95(isFree)
               54999179  115.959    0.000 3366.077    0.000 linear.py:92(forward)
               55152123 1968.171    0.000 3352.330    0.000 layer.py:151(update)
              424247000 2379.780    0.000 3338.094    0.000 layers.py:471(check)
               54999179  205.726    0.000 3197.908    0.000 functional.py:1669(linear)
             1188109678  772.350    0.000 2988.740    0.000 {built-in method builtins.any}
            12443452015 2051.012    0.000 2929.288    0.000 enum.py:646(__hash__)
              424247000 1674.373    0.000 2327.991    0.000 layers.py:77(check)
               54999179 2300.783    0.000 2300.783    0.000 {built-in method addmm}
                4242470   56.712    0.000 2175.009    0.001 agent.py:112(__call__)
              534551274 1393.528    0.000 2172.172    0.000 tensor.py:933(grad)
                8484940  193.736    0.000 2096.967    0.000 optimizer.py:167(zero_grad)
               12676433   87.891    0.000 2063.314    0.000 agent.py:59(modify_board)
               33888783 2017.259    0.000 2017.259    0.000 {built-in method cat}
              137595855 1992.553    0.000 1992.553    0.000 {built-in method clone}
              152728920 1876.235    0.000 1876.235    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
             5887362208 1500.056    0.000 1827.089    0.000 layers.py:700(<genexpr>)
               18153943 1815.862    0.000 1815.862    0.000 {built-in method tensor}
                4242470   75.663    0.000 1639.990    0.000 replaybuffer.py:18(stacker)
              152728920 1591.641    0.000 1591.641    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               76160552   65.665    0.000 1555.481    0.000 activation.py:713(forward)
               76160552   94.692    0.000 1489.816    0.000 functional.py:1292(leaky_relu)
                8484940   11.497    0.000 1473.813    0.000 game.py:37(board)
              453947686  274.148    0.000 1430.727    0.000 {built-in method builtins.all}
               76160552 1385.928    0.000 1385.928    0.000 {built-in method torch._C._nn.leaky_relu}
            14688614137 1315.864    0.000 1315.864    0.000 layer.py:91(positions)
               12676433 1300.936    0.000 1300.936    0.000 {built-in method torch._C._nn.one_hot}
              424247000  775.836    0.000 1226.267    0.000 layers.py:246(check)
              424247000  743.946    0.000 1199.911    0.000 layers.py:286(check)
             3114573816  787.569    0.000 1184.297    0.000 layers.py:690(<genexpr>)
               29700586  159.106    0.000 1135.762    0.000 tensor.py:21(wrapped)
              695614746  364.897    0.000 1062.221    0.000 overrides.py:1070(has_torch_function)
               76364460 1031.226    0.000 1031.226    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                4242470  595.773    0.000 1001.886    0.000 collector.py:46(collect)
               76364460  930.878    0.000  930.878    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
            12443482942  878.281    0.000  878.281    0.000 {built-in method builtins.hash}
               76364460  855.231    0.000  855.231    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
             1247823306  818.919    0.000  818.919    0.000 layer.py:146(elements)
               76364460  762.607    0.000  762.607    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                8433963  261.604    0.000  742.493    0.000 exploration.py:53(softmaxer)
                3721228   50.631    0.000  697.927    0.000 layers.py:740(restart)
              424247000  447.555    0.000  692.349    0.000 layers.py:313(check)
              424247000  447.914    0.000  691.312    0.000 layers.py:141(check)
              424247000  417.462    0.000  658.289    0.000 layers.py:273(check)
              150272288  623.931    0.000  623.931    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               76364460  596.861    0.000  596.861    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              424247000  404.435    0.000  585.002    0.000 layers.py:62(check)
        6797522136/6797522134  426.837    0.000  552.329    0.000 {built-in method builtins.len}
              424247000  365.164    0.000  549.700    0.000 layers.py:124(check)
              424247000  336.981    0.000  512.039    0.000 layers.py:48(check)
                8484940   12.178    0.000  481.873    0.000 loss.py:445(forward)
                8484940   44.636    0.000  469.695    0.000 functional.py:2637(mse_loss)
               21212350  466.886    0.000  466.886    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               54999179  450.026    0.000  450.026    0.000 {method 't' of 'torch._C._TensorBase' objects}
             5954864154  444.118    0.000  444.118    0.000 {method 'random' of '_random.Random' objects}
              424247000  297.949    0.000  434.557    0.000 layers.py:23(check)
               25454820  405.132    0.000  405.132    0.000 {built-in method sum}
             1475928414  306.302    0.000  384.156    0.000 overrides.py:1083(<genexpr>)
             3788898839  378.477    0.000  378.477    0.000 layer.py:203(isBlocking)
               48375964   52.252    0.000  322.990    0.000 layer.py:69(restart)
              569343153  231.660    0.000  311.452    0.000 layer.py:130(add)
                3721228   20.916    0.000  309.922    0.000 level.py:8(__init__)
                8484940  296.815    0.000  296.815    0.000 {built-in method torch._C._nn.mse_loss}
             5046310464  296.413    0.000  296.413    0.000 layer.py:84(isDead)
               42322746   31.960    0.000  291.569    0.000 flatten.py:39(forward)
              371103612  196.147    0.000  291.521    0.000 layer.py:126(remove)
                4242470  105.484    0.000  286.634    0.000 random.py:315(sample)
                4244156  284.700    0.000  284.700    0.000 {method 'ne' of 'torch._C._TensorBase' objects}
                8486207  261.007    0.000  261.007    0.000 {built-in method max}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9550908: <SuperLevel1_teleport_0> in cluster <dcc> Done

Job <SuperLevel1_teleport_0> was submitted from host <n-62-30-4> by user <s183905> in cluster <dcc> at Tue Apr 20 16:21:49 2021
Job was executed on host(s) <n-62-20-3>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sat Apr 24 07:14:39 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat Apr 24 07:14:39 2021
Terminated at Sun Apr 25 07:09:49 2021
Results reported at Sun Apr 25 07:09:49 2021

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

    CPU time :                                   85894.84 sec.
    Max Memory :                                 2679 MB
    Average Memory :                             2676.05 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13705.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86148 sec.
    Turnaround time :                            398880 sec.

The output (if any) is above this job summary.

