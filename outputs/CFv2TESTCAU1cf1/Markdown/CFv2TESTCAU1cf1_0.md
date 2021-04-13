
# Parameters

    Name :                      CFv2TESTCAU1cf1-0
    Main :                      CFagentv2
    Level :                     Levels.Causal1
    Failed actions chance :     0.0
    Hours :                     16.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Network1 :                  Networks.Teleporter
    K1 :                        500000
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
    K2 :                        100000
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
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                3
    Counterfacts :              1
    Topn :                      5
    Minutes used :              955 minutes.
    Hours used :                15 hours.

# Profiling


      31953967200 function calls (31781473446 primitive calls) in 57314.43 seconds

##    Ordered by: cumulative time
   List reduced from 518 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 57314.426 57314.426 {built-in method builtins.exec}
                      1    5.430    5.430 57314.426 57314.426 <string>:1(<module>)
                      1  164.292  164.292 57308.996 57308.996 main.py:103(CFagentv2)
                5976456   25.274    0.000 18640.201    0.003 agent.py:29(learn)
                5975229  463.772    0.000 15544.284    0.003 learner.py:42(Qlearn)
                1992152   10.127    0.000 8140.572    0.004 game.py:41(step)
                7967381   73.060    0.000 8085.863    0.001 optimizer.py:84(wrapper)
        196516135/24024093  881.088    0.000 7820.570    0.000 module.py:866(_call_impl)
                7967381   33.529    0.000 7752.234    0.001 grad_mode.py:24(decorate_context)
                1992152   13.679    0.000 7711.838    0.004 layers.py:719(step)
                7967381  229.363    0.000 7640.421    0.001 adam.py:55(step)
                1992152  206.154    0.000 7178.338    0.004 agent.py:54(_learn)
                7967381 1584.646    0.000 7159.946    0.001 _functional.py:53(adam)
               16056712  228.299    0.000 7059.964    0.000 container.py:117(forward)
                1992152  203.213    0.000 6672.495    0.003 agent.py:202(_learn)
               14020063   41.409    0.000 6539.592    0.000 network.py:24(forward)
                7967381   35.415    0.000 4796.125    0.001 tensor.py:195(backward)
                7967381   33.493    0.000 4759.506    0.001 __init__.py:68(backward)
                1992152   61.379    0.000 4751.405    0.002 agent.py:117(_learn)
                7967381 4541.041    0.001 4541.041    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                1992152 1195.374    0.001 4214.158    0.002 agent.py:236(counterfact2)
                1992152   34.802    0.000 4140.316    0.002 simulator.py:50(learn)
                1992152  219.691    0.000 4105.514    0.002 simulator.py:23(learn)
                1992153  302.709    0.000 3907.278    0.002 layers.py:685(update)
                1992152  180.170    0.000 3773.405    0.002 layers.py:17(step)
              199114935  332.302    0.000 3574.975    0.000 layer.py:98(move)
                1992152 3060.717    0.002 3573.529    0.002 replaybuffer.py:85(sample_data)
                1992152 2541.793    0.001 3211.194    0.002 replaybuffer.py:22(sample_data)
                4017260  109.178    0.000 3045.868    0.001 agent.py:49(__call__)
                1992152 2288.771    0.001 2938.959    0.001 replaybuffer.py:52(sample_data)
                1992152 1297.061    0.001 2794.148    0.001 agent.py:88(interveen)
               34150073   82.200    0.000 2748.959    0.000 conv.py:398(forward)
               34150073   50.585    0.000 2628.237    0.000 conv.py:390(_conv_forward)
               34150073 2577.653    0.000 2577.653    0.000 {built-in method conv2d}
                1992152 1330.071    0.001 2550.376    0.001 replaybuffer.py:28(teleporter_save_data)
               24857109 1884.434    0.000 1884.434    0.000 {built-in method tensor}
                1992152 1269.597    0.001 1870.156    0.001 agent.py:67(modify)
               38075885   86.036    0.000 1852.887    0.000 linear.py:93(forward)
                1992152 1406.187    0.001 1795.091    0.001 replaybuffer.py:91(simulator_save_data)
              199114935  530.289    0.000 1777.369    0.000 layers.py:736(check)
               20431413   14.881    0.000 1754.003    0.000 game.py:37(board)
               38075885   34.118    0.000 1723.975    0.000 functional.py:1737(linear)
               38075885 1681.158    0.000 1681.158    0.000 {built-in method torch._C._nn.linear}
               23905830  986.076    0.000 1654.920    0.000 layer.py:167(NoRock_update)
              116392455 1613.847    0.000 1613.847    0.000 {built-in method clone}
                4452424   38.798    0.000 1586.732    0.000 layers.py:741(restart)
               33937902 1486.467    0.000 1486.467    0.000 {built-in method cat}
              135441796 1459.399    0.000 1459.399    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                1992152 1033.605    0.001 1421.871    0.001 replaybuffer.py:58(CF_save_data)
              135441796 1268.543    0.000 1268.543    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                4452424   21.432    0.000 1234.273    0.000 level.py:8(__init__)
              199114935  229.083    0.000 1204.646    0.000 layers.py:730(isFree)
                7967381  186.884    0.000 1137.077    0.000 optimizer.py:189(zero_grad)
               56169246   49.278    0.000 1109.931    0.000 activation.py:713(forward)
               56169246   51.050    0.000 1060.652    0.000 functional.py:1364(leaky_relu)
                1990925   36.466    0.000 1057.402    0.001 agent.py:171(__call__)
                4452424   54.843    0.000 1046.580    0.000 levels.py:122(generate)
               56169246  999.434    0.000  999.434    0.000 {built-in method torch._C._nn.leaky_relu}
                1992152   36.712    0.000  975.840    0.000 agent.py:112(__call__)
             1007620323  817.342    0.000  975.563    0.000 layer.py:95(isFree)
               17364603  167.236    0.000  944.379    0.000 level.py:41(notUsed)
                6009412   42.327    0.000  904.347    0.000 agent.py:59(modify_board)
               67720898  804.525    0.000  804.525    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                8046061  788.095    0.000  788.095    0.000 {built-in method torch._C._nn.one_hot}
               67720898  705.453    0.000  705.453    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                2036649   10.182    0.000  690.986    0.000 simulator.py:20(boardforward)
               67720898  661.723    0.000  661.723    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               67720898  654.305    0.000  654.305    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              196755029  145.585    0.000  590.245    0.000 {built-in method builtins.any}
                1992152   35.848    0.000  520.504    0.000 replaybuffer.py:18(stacker)
             1983792644  354.655    0.000  515.414    0.000 enum.py:646(__hash__)
               67720898  512.548    0.000  512.548    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                1990925   37.189    0.000  507.502    0.000 replaybuffer.py:48(stacker)
              199215300   91.118    0.000  503.624    0.000 {built-in method builtins.all}
             1363340132  359.190    0.000  444.660    0.000 layers.py:701(<genexpr>)
              893659814  231.316    0.000  437.090    0.000 layers.py:691(<genexpr>)
                1992152  262.003    0.000  424.728    0.000 collector.py:46(collect)
                5976456  160.242    0.000  424.399    0.000 random.py:315(sample)
              126429441  421.512    0.000  421.512    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               17364603   14.903    0.000  420.283    0.000 level.py:38(elementsIn)
                7967381   12.984    0.000  412.865    0.000 loss.py:527(forward)
              474046376  332.098    0.000  412.212    0.000 tensor.py:906(grad)
               30711523  403.653    0.000  403.653    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                7967381   31.679    0.000  399.882    0.000 functional.py:2898(mse_loss)
              649860573  385.712    0.000  385.712    0.000 layer.py:146(elements)
                1992152   29.236    0.000  368.632    0.000 replaybuffer.py:81(stacker)
              199114935  226.493    0.000  355.339    0.000 layers.py:142(check)
                8434006  327.566    0.000  327.566    0.000 {built-in method nonzero}
        3706670877/3706670873  278.600    0.000  319.855    0.000 {built-in method builtins.len}
                4017260  115.133    0.000  319.582    0.000 exploration.py:53(softmaxer)
               26714544   27.822    0.000  303.513    0.000 layer.py:69(restart)
                1992152   55.011    0.000  281.016    0.000 agent.py:277(counterfact_check)
              199114935  186.964    0.000  277.773    0.000 layers.py:49(check)
              199114935  176.550    0.000  269.835    0.000 layers.py:125(check)
              301957334  220.699    0.000  267.975    0.000 layer.py:130(add)
                7967381  267.412    0.000  267.412    0.000 {built-in method torch._C._nn.mse_loss}
               17364603  132.831    0.000  265.040    0.000 level.py:39(<listcomp>)
               15937216  242.659    0.000  242.659    0.000 {built-in method sum}
              800982133  232.845    0.000  232.845    0.000 level.py:32(inverse)
                4452524  112.480    0.000  226.588    0.000 layers.py:37(reset)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-11-14>
Subject: Job 9511599: <CFv2TESTCAU1cf1_0> in cluster <dcc> Done

Job <CFv2TESTCAU1cf1_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon Apr 12 20:13:40 2021
Job was executed on host(s) <n-62-11-14>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon Apr 12 20:15:44 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Apr 12 20:15:44 2021
Terminated at Tue Apr 13 12:11:06 2021
Results reported at Tue Apr 13 12:11:06 2021

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

    CPU time :                                   57172.19 sec.
    Max Memory :                                 8725 MB
    Average Memory :                             6234.02 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               7659.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   57322 sec.
    Turnaround time :                            57446 sec.

The output (if any) is above this job summary.

