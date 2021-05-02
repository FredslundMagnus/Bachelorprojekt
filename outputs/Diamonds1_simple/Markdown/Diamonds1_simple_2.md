
# Parameters

    Name :                      Diamonds1_simple-2
    Main :                      simple
    Level :                     Levels.Causal2
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


      182999295302 function calls (182767071811 primitive calls) in 86104.32 seconds

##    Ordered by: cumulative time
   List reduced from 406 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86104.318 86104.318 {built-in method builtins.exec}
                      1    0.001    0.001 86104.318 86104.318 <string>:1(<module>)
                      1  147.384  147.384 86104.318 86104.318 main.py:66(simple)
                9675964   31.842    0.000 54238.158    0.006 game.py:41(step)
                9675964   46.102    0.000 52271.143    0.005 layers.py:718(step)
                9675965 1398.124    0.000 28473.484    0.003 layers.py:684(update)
                9675964   29.883    0.000 24851.320    0.003 agent.py:29(learn)
                9675964  217.630    0.000 24801.946    0.003 agent.py:117(_learn)
                9675964  630.484    0.000 24584.316    0.003 learner.py:42(Qlearn)
                9675964  737.810    0.000 23693.829    0.002 layers.py:17(step)
              967596400 1579.065    0.000 22871.265    0.000 layer.py:98(move)
               41239630  318.293    0.000 15516.463    0.000 layers.py:740(restart)
              967596400 3061.391    0.000 14217.569    0.000 layers.py:735(check)
               41239630  153.124    0.000 12421.753    0.000 level.py:8(__init__)
               41239630  469.214    0.000 10934.702    0.000 levels.py:151(generate)
                9675964   58.533    0.000 10221.710    0.001 grad_mode.py:23(decorate_context)
                9675964  353.806    0.000 10054.537    0.001 adam.py:55(step)
              197954807 1861.359    0.000 9989.665    0.000 level.py:41(notUsed)
        261251028/29027892  999.591    0.000 9703.167    0.000 module.py:715(_call_impl)
               19351928   50.778    0.000 9002.639    0.000 network.py:27(forward)
               19351928  230.774    0.000 8836.022    0.000 container.py:115(forward)
                9675964 1861.831    0.000 8254.416    0.001 functional.py:53(adam)
              967596400 1428.266    0.000 5525.405    0.000 layers.py:729(isFree)
                9675964   50.437    0.000 5417.934    0.001 tensor.py:181(backward)
                9675964   32.672    0.000 5367.498    0.001 __init__.py:68(backward)
            21086765064 3666.061    0.000 5237.937    0.000 enum.py:646(__hash__)
                9675964 5119.473    0.001 5119.473    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                9675964  113.678    0.000 5034.726    0.001 agent.py:112(__call__)
              197954807  147.793    0.000 4670.453    0.000 level.py:38(elementsIn)
               67731755 2742.296    0.000 4658.394    0.000 layer.py:167(NoRock_update)
             6653727985 3229.163    0.000 4097.139    0.000 layer.py:95(isFree)
             1835897567 1107.625    0.000 4024.873    0.000 {built-in method builtins.any}
              967596500  443.418    0.000 3286.017    0.000 {built-in method builtins.all}
               38703856   65.639    0.000 3168.029    0.000 conv.py:422(forward)
               38703856   82.642    0.000 3076.512    0.000 conv.py:414(_conv_forward)
              197954807 1477.280    0.000 3022.791    0.000 level.py:39(<listcomp>)
               38703856 2980.068    0.000 2980.068    0.000 {built-in method conv2d}
             4078865178 1087.813    0.000 2962.766    0.000 layers.py:690(<genexpr>)
               58055784  124.971    0.000 2937.345    0.000 linear.py:92(forward)
               58055784  217.247    0.000 2755.863    0.000 functional.py:1669(linear)
              967596400 1713.552    0.000 2752.866    0.000 layers.py:207(check)
              967596400 1702.717    0.000 2729.876    0.000 layers.py:219(check)
               40980103 2704.498    0.000 2704.498    0.000 {built-in method tensor}
              288677410  226.159    0.000 2676.154    0.000 layer.py:69(restart)
              967596400 1643.053    0.000 2670.831    0.000 layers.py:231(check)
              677317510 1562.983    0.000 2602.094    0.000 tensor.py:933(grad)
             7410854960 1986.662    0.000 2448.340    0.000 layers.py:700(<genexpr>)
                9675964  226.031    0.000 2285.386    0.000 optimizer.py:167(zero_grad)
               41239730 1055.808    0.000 2109.513    0.000 layers.py:36(reset)
               19351928   18.144    0.000 2105.892    0.000 game.py:37(board)
             9504299017 2051.121    0.000 2051.121    0.000 level.py:32(inverse)
               58055784 1927.186    0.000 1927.186    0.000 {built-in method addmm}
            18385755825 1775.327    0.000 1775.327    0.000 layer.py:91(positions)
              967596500 1087.522    0.000 1689.723    0.000 layers.py:113(isDone)
              193519280 1638.235    0.000 1638.235    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
            21086803853 1571.884    0.000 1571.884    0.000 {built-in method builtins.hash}
             8611001227 1530.587    0.000 1530.587    0.000 enum.py:352(<genexpr>)
              197954807  939.613    0.000 1499.869    0.000 {built-in method _functools.reduce}
              193519280 1397.779    0.000 1397.779    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
             2445406962  961.224    0.000 1322.593    0.000 layer.py:130(add)
              832132984  432.367    0.000 1271.708    0.000 overrides.py:1070(has_torch_function)
              967596400  803.437    0.000 1242.395    0.000 layers.py:196(check)
               77407712   68.702    0.000 1240.674    0.000 activation.py:713(forward)
               41239630  583.492    0.000 1235.619    0.000 level.py:16(<dictcomp>)
             4985772811 1177.059    0.000 1177.059    0.000 layer.py:146(elements)
               77407712  107.621    0.000 1171.973    0.000 functional.py:1292(leaky_relu)
               77407712 1054.322    0.000 1054.322    0.000 {built-in method torch._C._nn.leaky_relu}
              967596400  713.516    0.000 1030.566    0.000 layers.py:23(check)
               96759640  952.340    0.000  952.340    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               96759640  893.947    0.000  893.947    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                9675964  485.369    0.000  835.965    0.000 collector.py:46(collect)
               96759640  792.755    0.000  792.755    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              998296050  485.509    0.000  724.701    0.000 layer.py:126(remove)
             6653727985  704.171    0.000  704.171    0.000 layer.py:203(isBlocking)
               96759640  691.518    0.000  691.518    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
             7915405684  667.502    0.000  667.502    0.000 {method 'random' of '_random.Random' objects}
        9402854002/9402854001  598.215    0.000  658.811    0.000 {built-in method builtins.len}
             6928418245  560.256    0.000  560.256    0.000 level.py:39(<lambda>)
               96759640  536.777    0.000  536.777    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
             6580626251  530.056    0.000  530.056    0.000 {method 'append' of 'list' objects}
                9675964   13.139    0.000  471.649    0.000 loss.py:445(forward)
             1722321752  369.940    0.000  462.430    0.000 overrides.py:1083(<genexpr>)
             6484498090  461.678    0.000  461.678    0.000 layer.py:84(isDead)
                9675964   50.359    0.000  458.509    0.000 functional.py:2637(mse_loss)
             3381658434  411.144    0.000  411.144    0.000 layer.py:182(grid)
                9675964   36.057    0.000  403.134    0.000 exploration.py:47(epsilonGreedy)
               58055784  355.563    0.000  355.563    0.000 {method 't' of 'torch._C._TensorBase' objects}
              197954807  111.294    0.000  311.032    0.000 random.py:285(choice)
                9675964  283.074    0.000  283.074    0.000 {method 'tolist' of 'torch._C._TensorBase' objects}
               19351928  271.193    0.000  271.193    0.000 {built-in method sum}
                9675964  268.100    0.000  268.100    0.000 {built-in method torch._C._nn.mse_loss}
               96759690  114.421    0.000  261.444    0.000 tensor.py:596(__hash__)
                9676931  243.081    0.000  243.081    0.000 {built-in method max}
               67731755  220.020    0.000  220.020    0.000 layer.py:178(<listcomp>)
               38703856   27.598    0.000  210.164    0.000 flatten.py:39(forward)
                9675964   38.674    0.000  206.826    0.000 __init__.py:28(_make_grads)
               67731755  206.308    0.000  206.308    0.000 layer.py:179(<listcomp>)
              288677410  199.333    0.000  199.333    0.000 layer.py:139(clear2)
                9675964  199.239    0.000  199.239    0.000 {built-in method gather}
               38703856  182.566    0.000  182.566    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9578836: <Diamonds1_simple_2> in cluster <dcc> Done

Job <Diamonds1_simple_2> was submitted from host <n-62-30-3> by user <s183905> in cluster <dcc> at Mon Apr 26 20:44:04 2021
Job was executed on host(s) <n-62-11-14>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Thu Apr 29 14:30:15 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Apr 29 14:30:15 2021
Terminated at Fri Apr 30 14:25:28 2021
Results reported at Fri Apr 30 14:25:28 2021

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

    CPU time :                                   85887.08 sec.
    Max Memory :                                 2069 MB
    Average Memory :                             2065.76 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14315.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86113 sec.
    Turnaround time :                            322884 sec.

The output (if any) is above this job summary.

