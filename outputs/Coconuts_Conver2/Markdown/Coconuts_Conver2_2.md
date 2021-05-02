
# Parameters

    Name :                      Coconuts_Conver2-2
    Main :                      CFagent
    Level :                     Levels.Coconuts
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
    Cf convert :                2
    Counterfacts :              1
    Topn :                      3
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      70072567981 function calls (69740969542 primitive calls) in 86108.48 seconds

##    Ordered by: cumulative time
   List reduced from 511 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86108.475 86108.475 {built-in method builtins.exec}
                      1    4.431    4.431 86108.475 86108.475 <string>:1(<module>)
                      1  402.110  402.110 86104.044 86104.044 main.py:79(CFagent)
               11141853   42.022    0.000 28298.460    0.003 agent.py:29(learn)
               11141848  723.376    0.000 23046.711    0.002 learner.py:42(Qlearn)
                3713951   16.725    0.000 22671.255    0.006 game.py:41(step)
                3713951   24.677    0.000 21901.167    0.006 layers.py:718(step)
                3713951  358.766    0.000 14444.131    0.004 layers.py:17(step)
              371251177 1436.781    0.000 14051.160    0.000 layer.py:98(move)
        371609642/40012894 1584.229    0.000 12663.355    0.000 module.py:866(_call_impl)
               28871046   87.651    0.000 11825.371    0.000 network.py:27(forward)
               28871046  408.439    0.000 11535.779    0.000 container.py:117(forward)
                3713951  398.066    0.000 10990.830    0.003 agent.py:54(_learn)
                3713951  393.609    0.000 10103.574    0.003 agent.py:204(_learn)
               11141848   98.596    0.000 8990.928    0.001 optimizer.py:84(wrapper)
              371251177 1424.226    0.000 8627.445    0.000 layers.py:735(check)
               11141848   48.151    0.000 8559.615    0.001 grad_mode.py:24(decorate_context)
               11141848  350.982    0.000 8403.849    0.001 adam.py:55(step)
               11141848 1741.395    0.000 7632.102    0.001 _functional.py:53(adam)
                3713952  572.522    0.000 7400.492    0.002 layers.py:684(update)
                3713951  117.879    0.000 7136.729    0.002 agent.py:117(_learn)
                3713951  519.463    0.000 6935.746    0.002 agent.py:212(counterfact)
                3713951 5287.439    0.001 6471.089    0.002 replaybuffer.py:22(sample_data)
                3713951 5073.876    0.001 6208.868    0.002 replaybuffer.py:67(sample_data)
               11141848   44.892    0.000 5956.879    0.001 tensor.py:195(backward)
               11141848   44.865    0.000 5910.378    0.001 __init__.py:68(backward)
                8859005  234.619    0.000 5908.104    0.001 agent.py:49(__call__)
               11141848 5638.873    0.001 5638.873    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3713951 2061.764    0.001 4511.546    0.001 agent.py:88(interveen)
               57742092  136.621    0.000 4223.067    0.000 conv.py:398(forward)
                3713951 2318.607    0.001 4117.968    0.001 replaybuffer.py:28(teleporter_save_data)
               57742092   85.068    0.000 4024.328    0.000 conv.py:390(_conv_forward)
               57742092 3939.261    0.000 3939.261    0.000 {built-in method conv2d}
               51995321 2124.226    0.000 3614.664    0.000 layer.py:151(update)
               45465822 3542.008    0.000 3542.008    0.000 {built-in method tensor}
               36954996   25.077    0.000 3322.940    0.000 game.py:37(board)
               79185236  163.826    0.000 3224.196    0.000 linear.py:93(forward)
              371251177  557.612    0.000 3014.628    0.000 layers.py:729(isFree)
               79185236   66.999    0.000 2976.843    0.000 functional.py:1737(linear)
               79185236 2893.348    0.000 2893.348    0.000 {built-in method torch._C._nn.linear}
                3713951 1800.127    0.000 2744.071    0.001 agent.py:67(modify)
              371251177 1823.670    0.000 2562.575    0.000 layers.py:471(check)
             2426884990 2032.033    0.000 2457.016    0.000 layer.py:95(isFree)
              371251177 1703.931    0.000 2327.341    0.000 layers.py:77(check)
                1442296   30.238    0.000 2012.178    0.001 agent.py:176(choose_action)
               49712441 1905.273    0.000 1905.273    0.000 {built-in method cat}
                3713946   66.289    0.000 1736.248    0.000 agent.py:172(__call__)
             6259525218 1193.099    0.000 1729.217    0.000 enum.py:646(__hash__)
              108056282   93.852    0.000 1727.997    0.000 activation.py:713(forward)
              163155422 1670.460    0.000 1670.460    0.000 {built-in method clone}
               12572956   88.121    0.000 1668.326    0.000 agent.py:59(modify_board)
                3713951   62.135    0.000 1644.236    0.000 agent.py:112(__call__)
              108056282   93.570    0.000 1634.145    0.000 functional.py:1364(leaky_relu)
              371395200  199.739    0.000 1630.266    0.000 {built-in method builtins.all}
                2087142   26.231    0.000 1603.501    0.001 layers.py:740(restart)
              108056282 1522.679    0.000 1522.679    0.000 {built-in method torch._C._nn.leaky_relu}
              207981156 1495.912    0.000 1495.912    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
             2125483083  607.231    0.000 1479.489    0.000 layers.py:690(<genexpr>)
              373022010  319.421    0.000 1410.904    0.000 {built-in method builtins.any}
               11141848  237.898    0.000 1365.045    0.000 optimizer.py:189(zero_grad)
                2087142   13.778    0.000 1350.791    0.001 level.py:8(__init__)
              207981156 1327.510    0.000 1327.510    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                2087142   90.446    0.000 1229.830    0.001 levels.py:262(generate)
             2954464464  898.420    0.000 1091.483    0.000 layers.py:700(<genexpr>)
               12572956 1083.384    0.000 1083.384    0.000 {built-in method torch._C._nn.one_hot}
               18613748  181.854    0.000 1061.704    0.000 level.py:41(notUsed)
              371251177  808.692    0.000 1049.273    0.000 layers.py:62(check)
                3713951  812.968    0.000  990.956    0.000 replaybuffer.py:73(CF_save_data)
                3713951   72.360    0.000  898.856    0.000 replaybuffer.py:18(stacker)
             8890022186  897.971    0.000  897.971    0.000 layer.py:91(positions)
              103990578  873.951    0.000  873.951    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                3713946   72.161    0.000  859.595    0.000 replaybuffer.py:63(stacker)
             1115095259  851.177    0.000  851.177    0.000 layer.py:146(elements)
              103990578  759.339    0.000  759.339    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              103990578  712.370    0.000  712.370    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              103990578  692.627    0.000  692.627    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              727934130  551.616    0.000  679.720    0.000 tensor.py:906(grad)
              334614537  427.044    0.000  630.816    0.000 layers.py:113(isDone)
        7344703536/7344703533  533.329    0.000  604.141    0.000 {built-in method builtins.len}
                3713951  345.114    0.000  587.797    0.000 collector.py:46(collect)
                8859005  219.781    0.000  585.008    0.000 exploration.py:53(softmaxer)
                7427902  206.840    0.000  545.681    0.000 random.py:315(sample)
             6259567473  536.126    0.000  536.126    0.000 {built-in method builtins.hash}
              103990578  524.913    0.000  524.913    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              371251177  346.544    0.000  523.005    0.000 layers.py:48(check)
               11141848   16.100    0.000  489.505    0.000 loss.py:527(forward)
               18613748   18.416    0.000  478.378    0.000 level.py:38(elementsIn)
               11141848   43.365    0.000  473.406    0.000 functional.py:2898(mse_loss)
              371251177  312.366    0.000  451.638    0.000 layers.py:23(check)
              179442324  387.539    0.000  387.539    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                1442296  321.528    0.000  364.422    0.000 agent.py:187(convert_values)
              387165044  230.977    0.000  361.348    0.000 layer.py:126(remove)
               18613748  155.283    0.000  306.991    0.000 level.py:39(<listcomp>)
              506166889  220.195    0.000  300.928    0.000 layer.py:130(add)
               11141848  290.238    0.000  290.238    0.000 {built-in method torch._C._nn.mse_loss}
               57742092   44.808    0.000  288.099    0.000 flatten.py:39(forward)
                7427904  286.842    0.000  286.842    0.000 {built-in method nonzero}
               11143104  269.443    0.000  269.443    0.000 {built-in method max}
             2426884990  268.306    0.000  268.306    0.000 layer.py:203(isBlocking)
              857928224  256.292    0.000  256.292    0.000 level.py:32(inverse)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9579171: <Coconuts_Conver2_2> in cluster <dcc> Done

Job <Coconuts_Conver2_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Tue Apr 27 02:44:07 2021
Job was executed on host(s) <n-62-20-14>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Thu Apr 29 10:57:39 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Apr 29 10:57:39 2021
Terminated at Fri Apr 30 10:52:54 2021
Results reported at Fri Apr 30 10:52:54 2021

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

    CPU time :                                   85871.19 sec.
    Max Memory :                                 10263 MB
    Average Memory :                             6796.83 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               6121.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86114 sec.
    Turnaround time :                            288527 sec.

The output (if any) is above this job summary.

