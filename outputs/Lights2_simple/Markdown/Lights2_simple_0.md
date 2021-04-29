
# Parameters

    Name :                      Lights2_simple-0
    Main :                      simple
    Level :                     Levels.Causal4
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


      163480092552 function calls (163252907269 primitive calls) in 86117.92 seconds

##    Ordered by: cumulative time
   List reduced from 420 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86117.917 86117.917 {built-in method builtins.exec}
                      1    0.001    0.001 86117.917 86117.917 <string>:1(<module>)
                      1  142.498  142.498 86117.916 86117.916 main.py:66(simple)
                9466038   32.344    0.000 54036.471    0.006 game.py:41(step)
                9466038   43.607    0.000 51824.677    0.005 layers.py:718(step)
                9466038  765.935    0.000 33689.966    0.004 layers.py:17(step)
              946603800 2315.045    0.000 32825.952    0.000 layer.py:98(move)
                9466038   28.349    0.000 24772.122    0.003 agent.py:29(learn)
                9466038  219.854    0.000 24724.083    0.003 agent.py:117(_learn)
                9466038  627.031    0.000 24504.229    0.003 learner.py:42(Qlearn)
              946603800 4569.610    0.000 22544.925    0.000 layers.py:735(check)
                9466039 1315.496    0.000 18034.678    0.002 layers.py:684(update)
                9466038   57.498    0.000 10093.349    0.001 grad_mode.py:23(decorate_context)
                9466038  323.644    0.000 9928.023    0.001 adam.py:55(step)
        255583026/28398114  980.890    0.000 9749.256    0.000 module.py:715(_call_impl)
               18932076   44.738    0.000 9029.917    0.000 network.py:27(forward)
               18932076  226.221    0.000 8868.809    0.000 container.py:115(forward)
                9466038 1842.876    0.000 8168.527    0.001 functional.py:53(adam)
              946603800 1605.537    0.000 6514.478    0.000 layers.py:729(isFree)
               94660390 3276.086    0.000 5664.055    0.000 layer.py:151(update)
                9466038   52.257    0.000 5508.635    0.001 tensor.py:181(backward)
                9466038   31.380    0.000 5456.378    0.001 __init__.py:68(backward)
             1824707602 1336.002    0.000 5262.636    0.000 {built-in method builtins.any}
                9466038 5210.119    0.001 5210.119    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                9466038  112.831    0.000 5077.256    0.001 agent.py:112(__call__)
             7324478692 3811.418    0.000 4908.941    0.000 layer.py:95(isFree)
            17971091087 3406.866    0.000 4817.018    0.000 enum.py:646(__hash__)
               11703951  117.111    0.000 4083.748    0.000 layers.py:740(restart)
              946603800 2610.880    0.000 3534.391    0.000 layers.py:77(check)
            10283899439 2848.490    0.000 3448.863    0.000 layers.py:700(<genexpr>)
              946603800 2006.225    0.000 3221.175    0.000 layers.py:246(check)
               40097356 3194.347    0.000 3194.347    0.000 {built-in method tensor}
               37864152   64.904    0.000 3173.548    0.000 conv.py:422(forward)
               37864152   78.317    0.000 3084.461    0.000 conv.py:414(_conv_forward)
              946603800 1825.745    0.000 3004.250    0.000 layers.py:286(check)
               37864152 2990.754    0.000 2990.754    0.000 {built-in method conv2d}
               56796228  127.091    0.000 2981.436    0.000 linear.py:92(forward)
               11703951   49.731    0.000 2884.317    0.000 level.py:8(__init__)
               56796228  212.431    0.000 2796.189    0.000 functional.py:1669(linear)
               18932076   18.504    0.000 2581.898    0.000 game.py:37(board)
              662622690 1530.704    0.000 2578.427    0.000 tensor.py:933(grad)
               11703951  375.553    0.000 2418.579    0.000 levels.py:199(generate)
                9466038  200.016    0.000 2233.014    0.000 optimizer.py:167(zero_grad)
              946603900  441.438    0.000 2137.540    0.000 {built-in method builtins.all}
            21618534912 2127.641    0.000 2127.641    0.000 layer.py:91(positions)
               56796228 1970.220    0.000 1970.220    0.000 {built-in method addmm}
             4766232744 1208.222    0.000 1812.835    0.000 layers.py:690(<genexpr>)
              946603800 1066.165    0.000 1677.001    0.000 layers.py:313(check)
               23407902  179.384    0.000 1669.244    0.000 level.py:41(notUsed)
              946603800 1205.580    0.000 1639.414    0.000 layers.py:62(check)
              189320760 1633.507    0.000 1633.507    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              946603800 1017.254    0.000 1628.805    0.000 layers.py:273(check)
            17971129036 1410.159    0.000 1410.159    0.000 {built-in method builtins.hash}
              189320760 1377.178    0.000 1377.178    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
             2765689482 1312.327    0.000 1312.327    0.000 layer.py:146(elements)
              814079348  425.151    0.000 1275.910    0.000 overrides.py:1070(has_torch_function)
              946603800  827.870    0.000 1260.919    0.000 layers.py:48(check)
               75728304   62.076    0.000 1246.643    0.000 activation.py:713(forward)
               75728304  104.422    0.000 1184.567    0.000 functional.py:1292(leaky_relu)
              946603800  716.902    0.000 1074.316    0.000 layers.py:23(check)
               75728304 1069.926    0.000 1069.926    0.000 {built-in method torch._C._nn.leaky_relu}
              117039510  145.908    0.000 1041.605    0.000 layer.py:69(restart)
               94660380  940.922    0.000  940.922    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               94660380  883.106    0.000  883.106    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
            10457219691  844.015    0.000  844.015    0.000 {method 'random' of '_random.Random' objects}
                9466038  485.821    0.000  838.432    0.000 collector.py:46(collect)
        11759467400/11759467399  741.514    0.000  801.990    0.000 {built-in method builtins.len}
               94660380  780.746    0.000  780.746    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
             1290030079  526.612    0.000  713.827    0.000 layer.py:130(add)
               94660380  684.404    0.000  684.404    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
             6271772175  682.769    0.000  682.769    0.000 layer.py:203(isBlocking)
              475770158  677.979    0.000  677.979    0.000 level.py:32(inverse)
               23407902   21.772    0.000  630.616    0.000 level.py:38(elementsIn)
               11704051  311.139    0.000  614.536    0.000 layers.py:36(reset)
             9348999490  600.374    0.000  600.374    0.000 layer.py:84(isDead)
               94660380  525.407    0.000  525.407    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                9466038   14.942    0.000  480.915    0.000 loss.py:445(forward)
             1684954924  381.461    0.000  471.313    0.000 overrides.py:1083(<genexpr>)
                9466038   51.874    0.000  465.973    0.000 functional.py:2637(mse_loss)
              549530243  276.909    0.000  413.596    0.000 layer.py:126(remove)
                9466038   34.108    0.000  403.911    0.000 exploration.py:47(epsilonGreedy)
              946603900  278.176    0.000  386.761    0.000 layers.py:52(isDone)
               23407902  185.521    0.000  378.701    0.000 level.py:39(<listcomp>)
               11703951  184.090    0.000  376.350    0.000 level.py:16(<dictcomp>)
               56796228  354.923    0.000  354.923    0.000 {method 't' of 'torch._C._TensorBase' objects}
             4017122579  316.967    0.000  316.967    0.000 {method 'append' of 'list' objects}
               94660390  313.295    0.000  313.295    0.000 layer.py:163(<listcomp>)
               94660390  296.665    0.000  296.665    0.000 layer.py:164(<listcomp>)
                9466038  279.407    0.000  279.407    0.000 {method 'tolist' of 'torch._C._TensorBase' objects}
               18932076  273.516    0.000  273.516    0.000 {built-in method sum}
                9466038  272.099    0.000  272.099    0.000 {built-in method torch._C._nn.mse_loss}
               94660430  112.071    0.000  257.998    0.000 tensor.py:596(__hash__)
             1264028311  245.414    0.000  245.414    0.000 enum.py:352(<genexpr>)
                9466984  244.184    0.000  244.184    0.000 {built-in method max}
               23407902  135.848    0.000  230.143    0.000 {built-in method _functools.reduce}
               37864152   30.379    0.000  212.603    0.000 flatten.py:39(forward)
                9466038   37.474    0.000  206.521    0.000 __init__.py:28(_make_grads)
                9466038  204.288    0.000  204.288    0.000 {built-in method gather}
              126251387   80.479    0.000  204.137    0.000 random.py:285(choice)
             2864722053  200.390    0.000  200.390    0.000 layer.py:81(isDone)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9578831: <Lights2_simple_0> in cluster <dcc> Done

Job <Lights2_simple_0> was submitted from host <n-62-30-3> by user <s183905> in cluster <dcc> at Mon Apr 26 20:44:04 2021
Job was executed on host(s) <n-62-20-15>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Wed Apr 28 12:07:37 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed Apr 28 12:07:37 2021
Terminated at Thu Apr 29 12:03:04 2021
Results reported at Thu Apr 29 12:03:04 2021

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

    CPU time :                                   85887.73 sec.
    Max Memory :                                 2061 MB
    Average Memory :                             2058.09 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14323.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86127 sec.
    Turnaround time :                            227940 sec.

The output (if any) is above this job summary.

