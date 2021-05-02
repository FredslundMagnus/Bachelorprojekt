
# Parameters

    Name :                      Maze_Conver1-0
    Main :                      CFagent
    Level :                     Levels.Maze
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
    Cf convert :                1
    Counterfacts :              1
    Topn :                      3
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      63553048742 function calls (63217978075 primitive calls) in 86067.22 seconds

##    Ordered by: cumulative time
   List reduced from 517 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86109.743 86109.743 {built-in method builtins.exec}
                      1    5.124    5.124 86109.743 86109.743 <string>:1(<module>)
                      1  452.559  452.559 86104.618 86104.618 main.py:79(CFagent)
               11051454   45.291    0.000 28003.334    0.003 agent.py:29(learn)
               11051450  709.298    0.000 22649.430    0.002 learner.py:42(Qlearn)
                3683818   19.380    0.000 18947.969    0.005 game.py:41(step)
                3683818   25.687    0.000 18129.067    0.005 layers.py:718(step)
        375270780/40201804 1577.349    0.000 12615.202    0.000 module.py:866(_call_impl)
               29150354   80.375    0.000 11751.868    0.000 network.py:27(forward)
               29150354  393.010    0.000 11472.156    0.000 container.py:117(forward)
                3683818  438.995    0.000 10901.388    0.003 agent.py:54(_learn)
                3683818  362.603    0.000 10356.415    0.003 layers.py:17(step)
              368179428  632.618    0.000 9960.546    0.000 layer.py:98(move)
                3683818  432.545    0.000 9960.179    0.003 agent.py:204(_learn)
               11051450   98.807    0.000 8767.563    0.001 optimizer.py:84(wrapper)
                3683818  699.397    0.000 8599.705    0.002 agent.py:212(counterfact)
                3683818 7145.983    0.002 8356.715    0.002 replaybuffer.py:22(sample_data)
               11051450   54.302    0.000 8328.129    0.001 grad_mode.py:24(decorate_context)
               11051450  369.746    0.000 8157.625    0.001 adam.py:55(step)
                3683818 6932.202    0.002 8081.337    0.002 replaybuffer.py:67(sample_data)
                3683819  562.115    0.000 7709.452    0.002 layers.py:684(update)
               11051450 1697.918    0.000 7391.450    0.001 _functional.py:53(adam)
                3683818  120.297    0.000 7067.692    0.002 agent.py:117(_learn)
                9033759  258.446    0.000 6047.084    0.001 agent.py:49(__call__)
               11051450   46.761    0.000 5946.218    0.001 tensor.py:195(backward)
               11051450   50.269    0.000 5897.647    0.001 __init__.py:68(backward)
               11051450 5611.439    0.001 5611.439    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
              368179428 1282.091    0.000 5395.403    0.000 layers.py:735(check)
               49743498 4420.704    0.000 4420.704    0.000 {built-in method tensor}
               58300708  133.038    0.000 4212.627    0.000 conv.py:398(forward)
               41298735   29.128    0.000 4203.864    0.000 game.py:37(board)
               58941096 2296.194    0.000 4093.074    0.000 layer.py:167(NoRock_update)
               58300708   92.172    0.000 4011.761    0.000 conv.py:390(_conv_forward)
                3683818 1571.195    0.000 3967.340    0.001 agent.py:88(interveen)
               58300708 3919.589    0.000 3919.589    0.000 {built-in method conv2d}
              368179428  643.233    0.000 3405.730    0.000 layers.py:729(isFree)
               80083426  163.794    0.000 3235.505    0.000 linear.py:93(forward)
                3683818 1732.093    0.000 2988.171    0.001 replaybuffer.py:28(teleporter_save_data)
               80083426   74.445    0.000 2980.995    0.000 functional.py:1737(linear)
               80083426 2889.591    0.000 2889.591    0.000 {built-in method torch._C._nn.linear}
                3683818 1832.658    0.000 2798.666    0.001 agent.py:67(modify)
             2703204503 2362.592    0.000 2762.497    0.000 layer.py:95(isFree)
                1697513   36.543    0.000 2249.483    0.001 agent.py:176(choose_action)
                2763043   44.725    0.000 2204.057    0.001 layers.py:740(restart)
               49555737 1935.400    0.000 1935.400    0.000 {built-in method cat}
                2763043   26.732    0.000 1897.036    0.001 level.py:8(__init__)
               12717577   87.390    0.000 1724.854    0.000 agent.py:59(modify_board)
                3683814   72.432    0.000 1721.535    0.000 agent.py:172(__call__)
              109233780   98.506    0.000 1709.923    0.000 activation.py:713(forward)
                3769322  245.566    0.000 1692.998    0.000 levels.py:9(generate)
              109233780   97.539    0.000 1611.416    0.000 functional.py:1364(leaky_relu)
                3683818   69.223    0.000 1597.650    0.000 agent.py:112(__call__)
              368179428  986.434    0.000 1581.111    0.000 layers.py:168(check)
              109233780 1494.597    0.000 1494.597    0.000 {built-in method torch._C._nn.leaky_relu}
              206293728 1445.202    0.000 1445.202    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              369302676  331.625    0.000 1429.267    0.000 {built-in method builtins.any}
               11051450  232.595    0.000 1273.123    0.000 optimizer.py:189(zero_grad)
              120863456 1270.590    0.000 1270.590    0.000 {built-in method clone}
              206293728 1261.847    0.000 1261.847    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              368381900  144.861    0.000 1260.547    0.000 {built-in method builtins.all}
                3683818  944.835    0.000 1168.035    0.000 replaybuffer.py:73(CF_save_data)
             1500831605  400.245    0.000 1162.072    0.000 layers.py:690(<genexpr>)
               12717577 1140.516    0.000 1140.516    0.000 {built-in method torch._C._nn.one_hot}
             4029846114  777.734    0.000 1105.075    0.000 enum.py:646(__hash__)
             3290569713  900.203    0.000 1097.641    0.000 layers.py:700(<genexpr>)
             1192179238 1073.698    0.000 1073.698    0.000 layer.py:146(elements)
                3683818   70.245    0.000  914.226    0.000 replaybuffer.py:18(stacker)
                3683814   64.888    0.000  864.499    0.000 replaybuffer.py:63(stacker)
              103146864  845.193    0.000  845.193    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              103146864  747.233    0.000  747.233    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              368381900  471.756    0.000  694.374    0.000 layers.py:113(isDone)
              103146864  688.645    0.000  688.645    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              368179428  443.666    0.000  679.173    0.000 layers.py:141(check)
              103146864  676.877    0.000  676.877    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               17669323  251.764    0.000  646.762    0.000 random.py:315(sample)
        8142799333/8142799330  565.010    0.000  635.204    0.000 {built-in method builtins.len}
                9033759  219.458    0.000  618.408    0.000 exploration.py:53(softmaxer)
              722028132  495.603    0.000  614.327    0.000 tensor.py:906(grad)
             6499710282  596.548    0.000  596.548    0.000 layer.py:91(positions)
              368179428  420.458    0.000  589.898    0.000 layers.py:48(check)
                8289129   73.473    0.000  582.330    0.000 level.py:41(notUsed)
                3683818  332.328    0.000  568.574    0.000 collector.py:46(collect)
              368179428  357.363    0.000  525.058    0.000 layers.py:124(check)
               11051450   19.888    0.000  521.883    0.000 loss.py:527(forward)
                3769322  275.023    0.000  515.319    0.000 levels.py:75(RFS)
               11051450   52.250    0.000  501.995    0.000 functional.py:2898(mse_loss)
              103146864  498.044    0.000  498.044    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              368179428  272.145    0.000  403.970    0.000 layers.py:23(check)
              537707362  234.875    0.000  334.618    0.000 layer.py:130(add)
                1697513  333.300    0.000  333.300    0.000 agent.py:187(convert_values)
             4029888033  327.349    0.000  327.349    0.000 {built-in method builtins.hash}
              378311963  223.179    0.000  326.009    0.000 layer.py:126(remove)
              460475728  208.857    0.000  307.897    0.000 random.py:250(_randbelow_with_getrandbits)
                7367638  306.726    0.000  306.726    0.000 {built-in method nonzero}
               11051450  302.096    0.000  302.096    0.000 {built-in method torch._C._nn.mse_loss}
              137264847  289.646    0.000  289.646    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               58300708   52.642    0.000  287.655    0.000 flatten.py:39(forward)
               11052721  278.564    0.000  278.564    0.000 {built-in method max}
             3317501042  271.126    0.000  271.126    0.000 {method 'random' of '_random.Random' objects}
              276082300  256.720    0.000  256.720    0.000 level.py:32(inverse)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9579172: <Maze_Conver1_0> in cluster <dcc> Done

Job <Maze_Conver1_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Tue Apr 27 02:44:07 2021
Job was executed on host(s) <n-62-20-10>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Fri Apr 30 15:13:06 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Fri Apr 30 15:13:06 2021
Terminated at Sat May  1 15:08:24 2021
Results reported at Sat May  1 15:08:24 2021

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

    CPU time :                                   85902.21 sec.
    Max Memory :                                 10191 MB
    Average Memory :                             6626.54 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               6193.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86119 sec.
    Turnaround time :                            390257 sec.

The output (if any) is above this job summary.

