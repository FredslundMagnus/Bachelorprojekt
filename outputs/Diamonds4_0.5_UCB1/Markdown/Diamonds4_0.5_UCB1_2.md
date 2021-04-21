
# Parameters

    Name :                      Diamonds4_0.5_UCB1-2
    Main :                      graphTrain
    Level :                     Levels.Causal7
    Failed actions chance :     0.5
    Hours :                     10.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.UCB1
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


      14399399976 function calls (13905634477 primitive calls) in 35708.27 seconds

##    Ordered by: cumulative time
   List reduced from 464 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35708.265 35708.265 {built-in method builtins.exec}
                      1    0.001    0.001 35708.265 35708.265 <string>:1(<module>)
                      1  146.828  146.828 35708.264 35708.264 allGraphsTrain.py:10(graphTrain)
                 543698 6416.934    0.012 14365.561    0.026 allGraphs.py:146(transformNot)
                 543698   16.487    0.000 8722.852    0.016 allGraphsTrain.py:29(<listcomp>)
               54913599 2280.241    0.000 8706.397    0.000 allGraphs.py:110(states)
              543702744 8031.460    0.000 8031.460    0.000 {method 'item' of 'torch._C._TensorBase' objects}
              489328600 7003.819    0.000 7003.819    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 543698  696.254    0.001 3277.031    0.006 allGraphsTrain.py:35(<listcomp>)
               12100656   19.577    0.000 2580.777    0.000 allGraphs.py:158(getInterventions)
                 543698    2.178    0.000 2513.430    0.005 game.py:41(step)
                 543698    2.802    0.000 2386.851    0.004 layers.py:718(step)
                 543698  163.838    0.000 2149.625    0.004 allGraphsTrain.py:37(<listcomp>)
                 543698    1.940    0.000 1599.701    0.003 agent.py:29(learn)
                 543698   12.467    0.000 1596.488    0.003 agent.py:117(_learn)
                 543698   46.104    0.000 1584.021    0.003 learner.py:42(Qlearn)
               17135479 1516.190    0.000 1516.190    0.000 {built-in method tensor}
               14819147    9.618    0.000 1430.407    0.000 game.py:37(board)
                 543699   79.452    0.000 1370.878    0.003 layers.py:684(update)
               12100656   11.843    0.000 1337.640    0.000 allGraphs.py:133(UCB1)
               57631988  166.381    0.000 1331.538    0.000 tensor.py:21(wrapped)
                 543698   58.288    0.000 1279.384    0.002 allGraphsTrain.py:44(<listcomp>)
        109634755/12100656   79.794    0.000 1274.399    0.000 {built-in method builtins.min}
               30651719   14.684    0.000 1253.612    0.000 allGraphs.py:134(<lambda>)
        207168854/30651719  334.147    0.000 1238.929    0.000 allGraphs.py:68(expected_moves_UCB1)
               12100656   62.953    0.000 1223.560    0.000 allGraphs.py:153(format)
        274051234/65211312   89.326    0.000 1019.115    0.000 allGraphs.py:72(<genexpr>)
                 543698   43.515    0.000 1009.975    0.002 layers.py:17(step)
               57088290  985.694    0.000  985.694    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               54369800   89.129    0.000  961.044    0.000 layer.py:98(move)
               54369800  888.360    0.000  888.360    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                 543698    3.323    0.000  674.903    0.001 grad_mode.py:23(decorate_context)
                 543698  381.207    0.001  673.480    0.001 agent.py:67(modify)
                1672747   13.947    0.000  673.450    0.000 layers.py:740(restart)
                 543698   17.494    0.000  664.850    0.001 adam.py:55(step)
        12505054/1631094   54.239    0.000  573.570    0.000 module.py:715(_call_impl)
                 543698  120.729    0.000  570.573    0.001 functional.py:53(adam)
                1672747    7.059    0.000  540.864    0.000 level.py:8(__init__)
             2008150911  367.934    0.000  539.545    0.000 enum.py:646(__hash__)
                1087396    3.216    0.000  525.884    0.000 network.py:27(forward)
                1087396   13.885    0.000  515.259    0.000 container.py:115(forward)
               54369800  123.587    0.000  480.628    0.000 layers.py:735(check)
                1672747   19.783    0.000  469.495    0.000 levels.py:441(generate)
                8032551   79.260    0.000  428.741    0.000 level.py:41(notUsed)
                 543698    3.270    0.000  356.797    0.001 tensor.py:181(backward)
                 543698    1.961    0.000  353.527    0.001 __init__.py:68(backward)
              109634755   73.654    0.000  348.597    0.000 allGraphs.py:83(layers_not_in)
              207168854  207.132    0.000  336.840    0.000 allGraphs.py:60(UCB1)
                 543698  336.252    0.001  336.252    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               54369800   80.088    0.000  306.993    0.000 layers.py:729(isFree)
                 543698    7.581    0.000  303.515    0.001 agent.py:112(__call__)
               56544592  299.380    0.000  299.380    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              150562928   86.615    0.000  295.490    0.000 {built-in method builtins.any}
              109634755  135.196    0.000  274.944    0.000 allGraphs.py:84(<listcomp>)
                3805893  148.156    0.000  256.993    0.000 layer.py:167(NoRock_update)
              352100318  178.133    0.000  226.904    0.000 layer.py:95(isFree)
                1631094    7.032    0.000  203.433    0.000 tensor.py:576(__iter__)
                2174792    4.140    0.000  201.734    0.000 conv.py:422(forward)
                8032551    6.277    0.000  200.935    0.000 level.py:38(elementsIn)
              112001888   41.867    0.000  197.000    0.000 {built-in method builtins.all}
                2174792    4.540    0.000  196.074    0.000 conv.py:414(_conv_forward)
                1631094  191.606    0.000  191.606    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
                2174792  190.718    0.000  190.718    0.000 {built-in method conv2d}
               94603586   53.484    0.000  171.637    0.000 overrides.py:1070(has_torch_function)
             2008152732  171.611    0.000  171.611    0.000 {built-in method builtins.hash}
                2174792    5.604    0.000  153.213    0.000 linear.py:92(forward)
                2174792    9.778    0.000  145.198    0.000 functional.py:1669(linear)
               30447142   91.475    0.000  143.337    0.000 tensor.py:933(grad)
              421577224  114.954    0.000  141.613    0.000 layers.py:700(<genexpr>)
              203129001   56.441    0.000  138.086    0.000 layers.py:690(<genexpr>)
                 543698   12.920    0.000  137.235    0.000 optimizer.py:167(zero_grad)
                8032551   63.872    0.000  130.521    0.000 level.py:39(<listcomp>)
                8699168  119.833    0.000  119.833    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                 543698   69.449    0.000  116.880    0.000 collector.py:46(collect)
               11709229    9.579    0.000  114.302    0.000 layer.py:69(restart)
                2174792  104.318    0.000  104.318    0.000 {built-in method addmm}
                8699168  101.439    0.000  101.439    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                 543698    4.565    0.000   99.131    0.000 agent.py:59(modify_board)
                1672847   45.240    0.000   90.552    0.000 layers.py:36(reset)
              385655871   87.693    0.000   87.693    0.000 level.py:32(inverse)
               27180716   52.051    0.000   85.902    0.000 layers.py:632(check)
               27187828   51.060    0.000   84.241    0.000 layers.py:602(check)
               27182724   49.518    0.000   81.142    0.000 layers.py:617(check)
              710351025   75.029    0.000   75.029    0.000 layer.py:91(positions)
                3262188    3.157    0.000   73.518    0.000 activation.py:713(forward)
                3262188    4.936    0.000   70.361    0.000 functional.py:1292(leaky_relu)
              249013952   56.780    0.000   66.892    0.000 overrides.py:1083(<genexpr>)
              349392221   66.452    0.000   66.452    0.000 enum.py:352(<genexpr>)
                3262188   64.951    0.000   64.951    0.000 {built-in method torch._C._nn.leaky_relu}
              228648611   64.930    0.000   64.930    0.000 layer.py:146(elements)
                4349584   64.904    0.000   64.904    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                8032551   40.119    0.000   64.137    0.000 {built-in method _functools.reduce}
                 543698   41.980    0.000   62.863    0.000 allGraphsTrain.py:43(<listcomp>)
                 543698   62.523    0.000   62.523    0.000 {built-in method torch._C._nn.one_hot}
              111185408   45.425    0.000   61.914    0.000 layer.py:130(add)
                1672747   31.775    0.000   59.873    0.000 level.py:16(<dictcomp>)
                4349584   59.138    0.000   59.138    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                4349584   54.242    0.000   54.242    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                 543698   12.875    0.000   50.249    0.000 allGraphs.py:137(transform)
              207162806   49.740    0.000   49.740    0.000 {built-in method math.log}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9531993: <Diamonds4_0.5_UCB1_2> in cluster <dcc> Done

Job <Diamonds4_0.5_UCB1_2> was submitted from host <n-62-30-7> by user <s183905> in cluster <dcc> at Sat Apr 17 13:24:04 2021
Job was executed on host(s) <n-62-20-16>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sun Apr 18 01:35:54 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun Apr 18 01:35:54 2021
Terminated at Sun Apr 18 11:31:08 2021
Results reported at Sun Apr 18 11:31:08 2021

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

    CPU time :                                   35618.32 sec.
    Max Memory :                                 2070 MB
    Average Memory :                             2063.44 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14314.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35715 sec.
    Turnaround time :                            79624 sec.

The output (if any) is above this job summary.

