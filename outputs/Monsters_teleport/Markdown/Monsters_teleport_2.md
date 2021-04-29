
# Parameters

    Name :                      Monsters_teleport-2
    Main :                      teleport
    Level :                     Levels.MonsterLevel
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


      83095406690 function calls (82882111259 primitive calls) in 86114.46 seconds

##    Ordered by: cumulative time
   List reduced from 479 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86114.456 86114.456 {built-in method builtins.exec}
                      1    1.470    1.470 86114.456 86114.456 <string>:1(<module>)
                      1  169.483  169.483 86112.986 86112.986 main.py:45(teleport)
                3808860   16.637    0.000 28278.202    0.007 game.py:41(step)
                7617720   28.261    0.000 27493.803    0.004 agent.py:29(learn)
                3808860   19.118    0.000 27423.507    0.007 layers.py:718(step)
                7617720  649.666    0.000 23640.400    0.003 learner.py:42(Qlearn)
                3808860  126.957    0.000 16474.571    0.004 agent.py:54(_learn)
                3808861  571.062    0.000 13817.688    0.004 layers.py:684(update)
                3808860  363.266    0.000 13561.987    0.004 layers.py:17(step)
              380886000 1116.328    0.000 13163.611    0.000 layer.py:98(move)
                3808860  106.247    0.000 10976.502    0.003 agent.py:117(_learn)
        239956295/26661875  967.689    0.000 10587.473    0.000 module.py:715(_call_impl)
                7617720   47.922    0.000 10178.172    0.001 grad_mode.py:23(decorate_context)
                7617720  266.968    0.000 10041.922    0.001 adam.py:55(step)
               19044155   49.210    0.000 9912.425    0.001 network.py:27(forward)
               19044155  262.627    0.000 9751.374    0.001 container.py:115(forward)
                3808860 4941.041    0.001 9614.066    0.003 replaybuffer.py:28(teleporter_save_data)
              380886000 1249.131    0.000 9106.320    0.000 layers.py:735(check)
                7617720 1835.734    0.000 8655.497    0.001 functional.py:53(adam)
                3808860 4905.066    0.001 8127.961    0.002 agent.py:88(interveen)
               12065396   99.884    0.000 6673.969    0.001 layers.py:740(restart)
                7617575  169.638    0.000 6471.722    0.001 agent.py:49(__call__)
               12065396   45.973    0.000 5673.029    0.000 level.py:8(__init__)
                7617720   53.140    0.000 5432.436    0.001 tensor.py:181(backward)
                7617720   26.829    0.000 5379.297    0.001 __init__.py:68(backward)
              380886000 2843.816    0.000 5211.713    0.000 layers.py:538(check)
               12065396  898.854    0.000 5169.793    0.000 levels.py:413(generate)
                7617720 5146.791    0.001 5146.791    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3808860 2589.217    0.001 4644.954    0.001 agent.py:67(modify)
                3808860 2638.035    0.001 4402.101    0.001 replaybuffer.py:22(sample_data)
              248908585 3684.245    0.000 3684.245    0.000 {built-in method clone}
               38088310   65.660    0.000 3502.618    0.000 conv.py:422(forward)
               38088310   72.046    0.000 3412.806    0.000 conv.py:414(_conv_forward)
               60326980  550.459    0.000 3378.169    0.000 level.py:41(notUsed)
             1066287444  575.737    0.000 3331.558    0.000 {built-in method builtins.any}
               38088310 3327.836    0.000 3327.836    0.000 {built-in method conv2d}
               49514745  112.843    0.000 3190.999    0.000 linear.py:92(forward)
               49514745  196.735    0.000 3030.263    0.000 functional.py:1669(linear)
               22853166 1847.444    0.000 2642.024    0.000 layer.py:151(update)
             2613994472  757.190    0.000 2382.651    0.000 layers.py:700(<genexpr>)
             8608425407 1545.520    0.000 2232.512    0.000 enum.py:646(__hash__)
               49514745 2178.339    0.000 2178.339    0.000 {built-in method addmm}
              380886000  479.233    0.000 2147.869    0.000 layers.py:729(isFree)
              479916414 1333.450    0.000 2076.216    0.000 tensor.py:933(grad)
                3808860   50.554    0.000 2039.904    0.001 agent.py:112(__call__)
                7617720  195.138    0.000 2011.006    0.000 optimizer.py:167(zero_grad)
               11426435   83.350    0.000 1937.744    0.000 agent.py:59(modify_board)
               30470735 1867.204    0.000 1867.204    0.000 {built-in method cat}
              137118960 1796.311    0.000 1796.311    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
             2053610870 1339.967    0.000 1668.636    0.000 layer.py:95(isFree)
              137118960 1522.136    0.000 1522.136    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                3808860   63.709    0.000 1494.533    0.000 replaybuffer.py:18(stacker)
              376883090  922.108    0.000 1471.332    0.000 layers.py:575(isDead)
               68558900   59.271    0.000 1468.376    0.000 activation.py:713(forward)
               60326980   48.908    0.000 1466.816    0.000 level.py:38(elementsIn)
               68558900   89.632    0.000 1409.105    0.000 functional.py:1292(leaky_relu)
              380886000  922.702    0.000 1324.546    0.000 layers.py:77(check)
               68558900 1310.802    0.000 1310.802    0.000 {built-in method torch._C._nn.leaky_relu}
               11426435 1209.163    0.000 1209.163    0.000 {built-in method torch._C._nn.one_hot}
               16331446 1137.513    0.000 1137.513    0.000 {built-in method tensor}
              260335020 1126.106    0.000 1126.106    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              407550300  150.205    0.000 1114.252    0.000 {built-in method builtins.all}
               26664200  150.545    0.000 1042.201    0.000 tensor.py:21(wrapped)
               68559480 1037.485    0.000 1037.485    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              624654168  348.148    0.000 1017.441    0.000 overrides.py:1070(has_torch_function)
             1175107347  314.615    0.000  996.302    0.000 layers.py:690(<genexpr>)
              562675711  190.306    0.000  965.409    0.000 random.py:244(randint)
               60326980  461.456    0.000  944.757    0.000 level.py:39(<listcomp>)
                3808860  560.727    0.000  942.331    0.000 collector.py:46(collect)
             2573823453  913.175    0.000  913.175    0.000 level.py:32(inverse)
               68559480  904.522    0.000  904.522    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               72392376   89.346    0.000  875.102    0.000 layer.py:69(restart)
                7617720    9.993    0.000  834.608    0.000 game.py:37(board)
               64135840  317.740    0.000  816.528    0.000 random.py:315(sample)
               68559480  812.454    0.000  812.454    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              562675711  322.194    0.000  775.102    0.000 random.py:200(randrange)
             8246781835  773.075    0.000  773.075    0.000 layer.py:91(positions)
             1450273778  569.912    0.000  770.665    0.000 layer.py:130(add)
             1022239272  532.204    0.000  762.480    0.000 random.py:250(_randbelow_with_getrandbits)
               68559480  725.720    0.000  725.720    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                7617575  246.395    0.000  692.838    0.000 exploration.py:53(softmaxer)
             8608453166  686.998    0.000  686.998    0.000 {built-in method builtins.hash}
              898401206  432.717    0.000  667.495    0.000 layer.py:126(remove)
              380886100  434.456    0.000  640.548    0.000 layers.py:113(isDone)
              380886000  417.003    0.000  625.404    0.000 layers.py:48(check)
               12065496  308.420    0.000  615.057    0.000 layers.py:36(reset)
              380886000  215.682    0.000  609.195    0.000 layers.py:572(<listcomp>)
             2914527924  583.492    0.000  583.492    0.000 layer.py:146(elements)
               68559480  573.087    0.000  573.087    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
             2606126990  486.699    0.000  486.699    0.000 enum.py:352(<genexpr>)
              380886000  192.171    0.000  484.468    0.000 layers.py:573(<listcomp>)
               60326980  292.200    0.000  473.151    0.000 {built-in method _functools.reduce}
                7617720   11.563    0.000  448.239    0.000 loss.py:445(forward)
               19044300  442.868    0.000  442.868    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                7617720   40.915    0.000  436.676    0.000 functional.py:2637(mse_loss)
               12065396  236.455    0.000  430.400    0.000 level.py:16(<dictcomp>)
              380886000  295.685    0.000  427.396    0.000 layers.py:23(check)
               49514745  425.096    0.000  425.096    0.000 {method 't' of 'torch._C._TensorBase' objects}
               22853160  381.158    0.000  381.158    0.000 {built-in method sum}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9550925: <Monsters_teleport_2> in cluster <dcc> Done

Job <Monsters_teleport_2> was submitted from host <n-62-30-4> by user <s183905> in cluster <dcc> at Tue Apr 20 16:21:52 2021
Job was executed on host(s) <n-62-11-13>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Tue Apr 27 08:18:25 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue Apr 27 08:18:25 2021
Terminated at Wed Apr 28 08:13:53 2021
Results reported at Wed Apr 28 08:13:53 2021

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

    CPU time :                                   86001.27 sec.
    Max Memory :                                 2672 MB
    Average Memory :                             2667.29 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13712.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86192 sec.
    Turnaround time :                            661921 sec.

The output (if any) is above this job summary.

