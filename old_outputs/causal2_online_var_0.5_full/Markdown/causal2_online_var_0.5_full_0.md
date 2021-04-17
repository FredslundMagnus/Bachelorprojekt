
# Parameters

    Name :                      causal2_online_var_0.5_full-0
    Main :                      graphTrain
    Level :                     Levels.Causal2
    Failed actions chance :     0.5
    Hours :                     12.0
    Batch :                     100
    Width :                     9
    Height :                    9
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
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                3
    Counterfacts :              2
    Topn :                      5
    Minutes used :              715 minutes.
    Hours used :                11 hours.

# Profiling


      24312770208 function calls (23347221225 primitive calls) in 42902.98 seconds

##    Ordered by: cumulative time
   List reduced from 463 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 42902.981 42902.981 {built-in method builtins.exec}
                      1    0.001    0.001 42902.981 42902.981 <string>:1(<module>)
                      1  230.532  230.532 42902.980 42902.980 allGraphsTrain.py:10(graphTrain)
                 829346 6251.348    0.008 15674.798    0.019 allGraphs.py:120(transformNot)
              829353032 11007.567    0.000 11007.567    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                 829346   21.247    0.000 9943.241    0.012 allGraphsTrain.py:29(<listcomp>)
               83764047 2215.892    0.000 9922.007    0.000 allGraphs.py:88(states)
              746411800 7023.108    0.000 7023.108    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 829346  898.791    0.001 4789.552    0.006 allGraphsTrain.py:35(<listcomp>)
                 829346    3.979    0.000 4289.995    0.005 game.py:41(step)
                 829346    5.177    0.000 4112.881    0.005 layers.py:718(step)
               19393438   94.393    0.000 3890.761    0.000 allGraphs.py:127(getInterventions)
                 829347  127.123    0.000 2507.600    0.003 layers.py:684(update)
                 829346  153.466    0.000 2454.859    0.003 allGraphsTrain.py:37(<listcomp>)
               27057024 2294.320    0.000 2294.320    0.000 {built-in method tensor}
               23540169   12.612    0.000 2179.503    0.000 game.py:37(board)
               18340353   16.074    0.000 2002.461    0.000 allGraphs.py:107(rightIntervention)
        208186005/18340353  132.863    0.000 1914.187    0.000 {built-in method builtins.min}
                 829346    3.786    0.000 1913.025    0.002 agent.py:29(learn)
                 829346   18.931    0.000 1907.242    0.002 agent.py:117(_learn)
                 829346   57.531    0.000 1888.311    0.002 learner.py:42(Qlearn)
               52181819   22.585    0.000 1884.021    0.000 allGraphs.py:108(<lambda>)
        398031657/52181819  578.624    0.000 1861.436    0.000 allGraphs.py:52(expected_moves)
                 829346   68.865    0.000 1594.229    0.002 layers.py:17(step)
        535695490/122429300  153.694    0.000 1561.184    0.000 allGraphs.py:56(<genexpr>)
               82934600  137.325    0.000 1517.513    0.000 layer.py:98(move)
               87910676  211.781    0.000 1444.673    0.000 tensor.py:21(wrapped)
                 829346   62.390    0.000 1366.349    0.002 allGraphsTrain.py:44(<listcomp>)
                3507263   28.937    0.000 1358.647    0.000 layers.py:740(restart)
                3507263   14.521    0.000 1083.024    0.000 level.py:8(__init__)
               87081330  979.299    0.000  979.299    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                3507263   39.688    0.000  942.781    0.000 levels.py:151(generate)
               82934600  912.633    0.000  912.633    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
             3673082573  614.607    0.000  891.569    0.000 enum.py:646(__hash__)
                 829346  472.574    0.001  863.733    0.001 agent.py:67(modify)
               16834926  157.817    0.000  860.504    0.000 level.py:41(notUsed)
        19074958/2488038   85.327    0.000  769.039    0.000 module.py:715(_call_impl)
                 829346    6.697    0.000  729.433    0.001 grad_mode.py:23(decorate_context)
                 829346   28.093    0.000  710.645    0.001 adam.py:55(step)
               82934600  180.366    0.000  707.170    0.000 layers.py:735(check)
                1658692    4.723    0.000  695.559    0.000 network.py:24(forward)
                1658692   19.772    0.000  677.934    0.000 container.py:115(forward)
              209239090  130.588    0.000  597.513    0.000 allGraphs.py:61(layers_not_in)
                 829346  128.952    0.000  579.289    0.001 functional.py:53(adam)
               82934600  121.477    0.000  537.098    0.000 layers.py:729(isFree)
              209239090  230.093    0.000  466.924    0.000 allGraphs.py:62(<listcomp>)
                 829346    5.300    0.000  460.946    0.001 tensor.py:181(backward)
                 829346    3.918    0.000  455.646    0.001 __init__.py:68(backward)
                5805429  256.517    0.000  432.288    0.000 layer.py:167(NoRock_update)
                 829346  430.409    0.001  430.409    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
              228709852  126.424    0.000  428.924    0.000 {built-in method builtins.any}
                 829346   13.115    0.000  424.545    0.001 agent.py:112(__call__)
              567261048  337.850    0.000  415.621    0.000 layer.py:95(isFree)
               16834926   12.059    0.000  401.690    0.000 level.py:38(elementsIn)
              170845376   76.320    0.000  346.004    0.000 {built-in method builtins.all}
                2488038   10.383    0.000  305.171    0.000 tensor.py:576(__iter__)
               86251984  294.207    0.000  294.207    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              398031657  199.963    0.000  291.972    0.000 allGraphs.py:37(p)
                2488038  288.054    0.000  288.054    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
             3673085290  276.962    0.000  276.962    0.000 {built-in method builtins.hash}
                3317384    6.834    0.000  272.036    0.000 conv.py:422(forward)
                3317384    8.053    0.000  262.360    0.000 conv.py:414(_conv_forward)
               16834926  126.371    0.000  257.869    0.000 level.py:39(<listcomp>)
                3317384  253.075    0.000  253.075    0.000 {built-in method conv2d}
              486321507  131.903    0.000  246.532    0.000 layers.py:690(<genexpr>)
              144306338   74.272    0.000  242.155    0.000 overrides.py:1070(has_torch_function)
               24550841   20.439    0.000  238.404    0.000 layer.py:69(restart)
              635419496  170.162    0.000  206.480    0.000 layers.py:700(<genexpr>)
                3317384    8.506    0.000  197.915    0.000 linear.py:92(forward)
                3317384   14.872    0.000  185.332    0.000 functional.py:1669(linear)
                3507363   92.063    0.000  184.049    0.000 layers.py:36(reset)
               46443430  109.762    0.000  182.478    0.000 tensor.py:933(grad)
              808286364  178.774    0.000  178.774    0.000 level.py:32(inverse)
                 829346   15.536    0.000  157.305    0.000 optimizer.py:167(zero_grad)
                 829346    7.809    0.000  143.452    0.000 agent.py:59(modify_board)
              732320294  134.512    0.000  134.512    0.000 enum.py:352(<genexpr>)
                3317384  132.182    0.000  132.182    0.000 {built-in method addmm}
               16834926   82.380    0.000  131.762    0.000 {built-in method _functools.reduce}
               41468778   79.133    0.000  128.306    0.000 layers.py:207(check)
                 829346   73.560    0.000  126.071    0.000 collector.py:46(collect)
               41471992   76.122    0.000  122.112    0.000 layers.py:219(check)
               41472327   75.813    0.000  121.579    0.000 layers.py:231(check)
                3507263   61.048    0.000  117.189    0.000 level.py:16(<dictcomp>)
               13269536  116.340    0.000  116.340    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              205364566   83.657    0.000  116.052    0.000 layer.py:130(add)
              419550095  110.204    0.000  110.204    0.000 layer.py:146(elements)
             1041097082   99.780    0.000   99.780    0.000 layer.py:91(positions)
               13269536   96.048    0.000   96.048    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              379840736   79.865    0.000   95.428    0.000 overrides.py:1083(<genexpr>)
                 829346   94.887    0.000   94.887    0.000 {built-in method torch._C._nn.one_hot}
                 829346   64.296    0.000   94.390    0.000 allGraphsTrain.py:43(<listcomp>)
                4976076    5.649    0.000   88.144    0.000 activation.py:713(forward)
              401572780   79.781    0.000   84.798    0.000 {built-in method builtins.max}
                4976076    8.543    0.000   82.494    0.000 functional.py:1292(leaky_relu)
                 829346   20.149    0.000   76.140    0.000 allGraphs.py:111(transform)
                4976076   73.190    0.000   73.190    0.000 {built-in method torch._C._nn.leaky_relu}
                2488038   66.799    0.000   66.799    0.000 {method 'tolist' of 'torch._C._TensorBase' objects}
                6634768   65.800    0.000   65.800    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              722914052   64.197    0.000   64.197    0.000 {method 'append' of 'list' objects}
               82703928   42.199    0.000   63.766    0.000 layer.py:126(remove)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-11>
Subject: Job 9511703: <causal2_online_var_0.5_full_0> in cluster <dcc> Done

Job <causal2_online_var_0.5_full_0> was submitted from host <n-62-27-18> by user <s183905> in cluster <dcc> at Mon Apr 12 21:45:53 2021
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Mon Apr 12 21:55:12 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Apr 12 21:55:12 2021
Terminated at Tue Apr 13 09:50:19 2021
Results reported at Tue Apr 13 09:50:19 2021

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

    CPU time :                                   42801.15 sec.
    Max Memory :                                 2090 MB
    Average Memory :                             2089.03 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14294.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   42908 sec.
    Turnaround time :                            43466 sec.

The output (if any) is above this job summary.

