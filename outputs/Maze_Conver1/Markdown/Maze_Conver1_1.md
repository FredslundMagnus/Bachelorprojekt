
# Parameters

    Name :                      Maze_Conver1-1
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


      66942980972 function calls (66586696937 primitive calls) in 86064.62 seconds

##    Ordered by: cumulative time
   List reduced from 516 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86114.152 86114.152 {built-in method builtins.exec}
                      1    4.429    4.429 86114.151 86114.151 <string>:1(<module>)
                      1  426.898  426.898 86109.723 86109.723 main.py:79(CFagent)
               11678955   43.326    0.000 29151.306    0.002 agent.py:29(learn)
               11678951  731.497    0.000 23704.761    0.002 learner.py:42(Qlearn)
                3892985   16.987    0.000 19690.434    0.005 game.py:41(step)
                3892985   23.447    0.000 18857.398    0.005 layers.py:718(step)
        398949152/42666808 1649.218    0.000 13402.681    0.000 module.py:866(_call_impl)
               30987857   88.939    0.000 12529.820    0.000 network.py:27(forward)
               30987857  398.449    0.000 12231.356    0.000 container.py:117(forward)
                3892985  420.011    0.000 11320.787    0.003 agent.py:54(_learn)
                3892985  358.218    0.000 10715.911    0.003 layers.py:17(step)
                3892985  417.566    0.000 10403.704    0.003 agent.py:204(_learn)
              388969222  653.129    0.000 10318.521    0.000 layer.py:98(move)
               11678951   98.336    0.000 9308.916    0.001 optimizer.py:84(wrapper)
                3892985  735.069    0.000 8894.654    0.002 agent.py:212(counterfact)
               11678951   54.469    0.000 8850.858    0.001 grad_mode.py:24(decorate_context)
               11678951  372.740    0.000 8680.374    0.001 adam.py:55(step)
                3892986  593.498    0.000 8083.953    0.002 layers.py:684(update)
               11678951 1803.692    0.000 7891.844    0.001 _functional.py:53(adam)
                3892985  121.557    0.000 7356.849    0.002 agent.py:117(_learn)
                3892985 5698.362    0.001 6935.592    0.002 replaybuffer.py:22(sample_data)
                3892985 5664.707    0.001 6852.080    0.002 replaybuffer.py:67(sample_data)
                9638204  250.863    0.000 6344.209    0.001 agent.py:49(__call__)
               11678951   47.100    0.000 6051.849    0.001 tensor.py:195(backward)
               11678951   47.938    0.000 6003.080    0.001 __init__.py:68(backward)
              388969222 1409.336    0.000 5789.566    0.000 layers.py:735(check)
               11678951 5720.420    0.000 5720.420    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
               61975714  150.739    0.000 4540.165    0.000 conv.py:398(forward)
               52885709 4539.810    0.000 4539.810    0.000 {built-in method tensor}
               61975714   94.938    0.000 4323.026    0.000 conv.py:390(_conv_forward)
               43979016   30.969    0.000 4318.251    0.000 game.py:37(board)
               61975714 4228.088    0.000 4228.088    0.000 {built-in method conv2d}
                3892985 1585.548    0.000 4113.056    0.001 agent.py:88(interveen)
               62287768 2220.391    0.000 4007.489    0.000 layer.py:167(NoRock_update)
               85177601  180.168    0.000 3446.999    0.000 linear.py:93(forward)
              388969222  667.937    0.000 3320.291    0.000 layers.py:729(isFree)
               85177601   76.970    0.000 3175.035    0.000 functional.py:1737(linear)
               85177601 3080.748    0.000 3080.748    0.000 {built-in method torch._C._nn.linear}
                3892985 1719.569    0.000 3064.821    0.001 replaybuffer.py:28(teleporter_save_data)
                3892985 1892.333    0.000 2873.954    0.001 agent.py:67(modify)
             2862254236 2225.699    0.000 2652.354    0.000 layer.py:95(isFree)
                3164430   45.974    0.000 2554.991    0.001 layers.py:740(restart)
                1884736   38.894    0.000 2475.359    0.001 agent.py:176(choose_action)
                3164430   28.725    0.000 2204.181    0.001 level.py:8(__init__)
               52461019 2001.782    0.000 2001.782    0.000 {built-in method cat}
                4314569  287.112    0.000 1982.838    0.000 levels.py:9(generate)
              116165458   96.387    0.000 1831.092    0.000 activation.py:713(forward)
                3892981   67.291    0.000 1792.923    0.000 agent.py:172(__call__)
               13531189   86.421    0.000 1778.774    0.000 agent.py:59(modify_board)
              116165458  108.711    0.000 1734.704    0.000 functional.py:1364(leaky_relu)
                3892985   63.106    0.000 1689.306    0.000 agent.py:112(__call__)
              388969222 1024.061    0.000 1668.681    0.000 layers.py:168(check)
              116165458 1606.749    0.000 1606.749    0.000 {built-in method torch._C._nn.leaky_relu}
              218007080 1549.925    0.000 1549.925    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              390027156  359.471    0.000 1512.230    0.000 {built-in method builtins.any}
               11678951  249.561    0.000 1383.081    0.000 optimizer.py:189(zero_grad)
              218007080 1368.693    0.000 1368.693    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              130829735 1361.988    0.000 1361.988    0.000 {built-in method clone}
                3892985  983.444    0.000 1230.954    0.000 replaybuffer.py:73(CF_save_data)
             4313324913  858.468    0.000 1227.791    0.000 enum.py:646(__hash__)
              389298600  116.403    0.000 1167.736    0.000 {built-in method builtins.all}
               13531189 1165.293    0.000 1165.293    0.000 {built-in method torch._C._nn.one_hot}
             3475207530  944.817    0.000 1152.759    0.000 layers.py:700(<genexpr>)
             1217912138  323.706    0.000 1102.038    0.000 layers.py:690(<genexpr>)
             1289092560 1020.569    0.000 1020.569    0.000 layer.py:146(elements)
                3892985   72.443    0.000  935.901    0.000 replaybuffer.py:18(stacker)
              109003540  911.348    0.000  911.348    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                3892981   69.497    0.000  896.705    0.000 replaybuffer.py:63(stacker)
              109003540  776.278    0.000  776.278    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              388969222  466.610    0.000  733.400    0.000 layers.py:141(check)
              389298600  489.332    0.000  731.334    0.000 layers.py:113(isDone)
              109003540  731.152    0.000  731.152    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              109003540  720.096    0.000  720.096    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
        8629560143/8629560140  618.580    0.000  693.188    0.000 {built-in method builtins.len}
                9493290   82.432    0.000  684.118    0.000 level.py:41(notUsed)
             6865830403  667.555    0.000  667.555    0.000 layer.py:91(positions)
               19579538  257.317    0.000  666.946    0.000 random.py:315(sample)
              763024864  528.855    0.000  655.952    0.000 tensor.py:906(grad)
              388969222  438.038    0.000  631.998    0.000 layers.py:48(check)
                9638204  230.049    0.000  617.542    0.000 exploration.py:53(softmaxer)
                4314569  321.425    0.000  605.709    0.000 levels.py:75(RFS)
                3892985  351.122    0.000  601.141    0.000 collector.py:46(collect)
              388969222  365.333    0.000  550.625    0.000 layers.py:124(check)
              109003540  538.888    0.000  538.888    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               11678951   17.344    0.000  512.745    0.000 loss.py:527(forward)
               11678951   45.715    0.000  495.401    0.000 functional.py:2898(mse_loss)
              388969222  296.953    0.000  439.176    0.000 layers.py:23(check)
             4313369184  369.331    0.000  369.331    0.000 {built-in method builtins.hash}
              582909089  266.074    0.000  365.487    0.000 layer.py:130(add)
                1884736  357.023    0.000  357.023    0.000 agent.py:187(convert_values)
              400514952  239.861    0.000  342.945    0.000 layer.py:126(remove)
              494659403  228.794    0.000  334.946    0.000 random.py:250(_randbelow_with_getrandbits)
              148253905  317.837    0.000  317.837    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               11678951  306.054    0.000  306.054    0.000 {built-in method torch._C._nn.mse_loss}
              316144631  303.772    0.000  303.772    0.000 level.py:32(inverse)
               61975714   44.972    0.000  302.246    0.000 flatten.py:39(forward)
                7785972  299.647    0.000  299.647    0.000 {built-in method nonzero}
               25315440   40.056    0.000  296.081    0.000 layer.py:69(restart)
             3504945261  287.212    0.000  287.212    0.000 {method 'random' of '_random.Random' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9579173: <Maze_Conver1_1> in cluster <dcc> Done

Job <Maze_Conver1_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Tue Apr 27 02:44:07 2021
Job was executed on host(s) <n-62-20-14>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Fri Apr 30 15:18:23 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Fri Apr 30 15:18:23 2021
Terminated at Sat May  1 15:13:45 2021
Results reported at Sat May  1 15:13:45 2021

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

    CPU time :                                   85871.31 sec.
    Max Memory :                                 10630 MB
    Average Memory :                             6921.25 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               5754.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86124 sec.
    Turnaround time :                            390578 sec.

The output (if any) is above this job summary.

