
# Parameters

    Name :                      Causal4_Cf_convert3_TopN3-0
    Main :                      CFagent
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
    Topn :                      3
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      72953594889 function calls (72629030930 primitive calls) in 86111.22 seconds

##    Ordered by: cumulative time
   List reduced from 514 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86111.223 86111.223 {built-in method builtins.exec}
                      1    4.733    4.733 86111.223 86111.223 <string>:1(<module>)
                      1  386.934  386.934 86106.490 86106.490 main.py:79(CFagent)
               10515531   42.825    0.000 26641.900    0.003 agent.py:29(learn)
                3505177   15.710    0.000 22551.936    0.006 game.py:41(step)
                3505177   21.237    0.000 21728.386    0.006 layers.py:718(step)
               10515525  672.799    0.000 21645.302    0.002 learner.py:42(Qlearn)
                3505177  330.727    0.000 14644.338    0.004 layers.py:17(step)
              350086478 1046.584    0.000 14277.873    0.000 layer.py:98(move)
        363293041/38730773 1535.208    0.000 12364.701    0.000 module.py:866(_call_impl)
               28215248   83.642    0.000 11560.664    0.000 network.py:27(forward)
               28215248  376.916    0.000 11284.136    0.000 container.py:117(forward)
                3505177  893.487    0.000 10545.461    0.003 agent.py:210(counterfact)
                3505177  385.273    0.000 10357.711    0.003 agent.py:54(_learn)
                3505177  378.755    0.000 9498.470    0.003 agent.py:202(_learn)
              350086478 1779.390    0.000 8752.286    0.000 layers.py:735(check)
               10515525   94.615    0.000 8433.951    0.001 optimizer.py:84(wrapper)
               10515525   46.590    0.000 8019.699    0.001 grad_mode.py:24(decorate_context)
               10515525  330.760    0.000 7863.540    0.001 adam.py:55(step)
               10515525 1651.960    0.000 7165.121    0.001 _functional.py:53(adam)
                3505178  541.099    0.000 7032.369    0.002 layers.py:684(update)
                3505177  109.235    0.000 6717.082    0.002 agent.py:117(_learn)
                3505177 5062.890    0.001 6191.934    0.002 replaybuffer.py:22(sample_data)
                3505177 4863.815    0.001 5947.511    0.002 replaybuffer.py:67(sample_data)
                8843057  232.547    0.000 5939.998    0.001 agent.py:49(__call__)
               55402380 5657.286    0.000 5657.286    0.000 {built-in method tensor}
               10515525   43.476    0.000 5602.124    0.001 tensor.py:195(backward)
               10515525   42.540    0.000 5556.931    0.001 __init__.py:68(backward)
               47351358   32.024    0.000 5457.287    0.000 game.py:37(board)
               10515525 5297.144    0.001 5297.144    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               70103550 2729.025    0.000 4688.374    0.000 layer.py:151(update)
               56430496  134.013    0.000 4201.519    0.000 conv.py:398(forward)
               56430496   81.289    0.000 4003.084    0.000 conv.py:390(_conv_forward)
                3505177 1663.149    0.000 3991.983    0.001 agent.py:88(interveen)
               56430496 3921.795    0.000 3921.795    0.000 {built-in method conv2d}
              350086478  770.745    0.000 3757.918    0.000 layers.py:729(isFree)
                3505177 1832.477    0.001 3262.811    0.001 replaybuffer.py:28(teleporter_save_data)
               77635390  169.443    0.000 3155.883    0.000 linear.py:93(forward)
             3339663419 2425.883    0.000 2987.173    0.000 layer.py:95(isFree)
               77635390   65.915    0.000 2904.025    0.000 functional.py:1737(linear)
               77635390 2818.691    0.000 2818.691    0.000 {built-in method torch._C._nn.linear}
                3505177 1749.931    0.000 2661.514    0.001 agent.py:67(modify)
                1846318   42.484    0.000 2541.393    0.001 agent.py:175(choose_action)
             6864442400 1318.256    0.000 1859.822    0.000 enum.py:646(__hash__)
               47399974 1830.037    0.000 1830.037    0.000 {built-in method cat}
              105850638   91.568    0.000 1678.159    0.000 activation.py:713(forward)
              350580060  380.316    0.000 1674.122    0.000 {built-in method builtins.any}
               12348234   81.666    0.000 1667.154    0.000 agent.py:59(modify_board)
                3505171   60.069    0.000 1640.134    0.000 agent.py:171(__call__)
              105850638   88.666    0.000 1586.591    0.000 functional.py:1364(leaky_relu)
                3505177   58.491    0.000 1535.047    0.000 agent.py:112(__call__)
              105850638 1478.882    0.000 1478.882    0.000 {built-in method torch._C._nn.leaky_relu}
              138601394 1436.113    0.000 1436.113    0.000 {built-in method clone}
              196289792 1400.158    0.000 1400.158    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              350086478 1053.686    0.000 1389.168    0.000 layers.py:77(check)
                3442918   44.974    0.000 1332.700    0.000 layers.py:740(restart)
             3817823702 1063.154    0.000 1293.805    0.000 layers.py:700(<genexpr>)
              350086478  805.045    0.000 1255.523    0.000 layers.py:286(check)
               10515525  228.291    0.000 1250.614    0.000 optimizer.py:189(zero_grad)
                3505177  981.836    0.000 1243.013    0.000 replaybuffer.py:73(CF_save_data)
              196289792 1241.786    0.000 1241.786    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              350086478  670.563    0.000 1098.608    0.000 layers.py:246(check)
             1166821332 1095.284    0.000 1095.284    0.000 layer.py:146(elements)
               12348234 1094.813    0.000 1094.813    0.000 {built-in method torch._C._nn.one_hot}
                3442918   20.540    0.000  942.335    0.000 level.py:8(__init__)
             9093281602  887.585    0.000  887.585    0.000 layer.py:91(positions)
                3505177   68.194    0.000  854.382    0.000 replaybuffer.py:18(stacker)
              350517800   69.698    0.000  848.895    0.000 {built-in method builtins.all}
              714577179  168.658    0.000  825.921    0.000 layers.py:690(<genexpr>)
               98144896  825.666    0.000  825.666    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                3505171   67.412    0.000  818.015    0.000 replaybuffer.py:63(stacker)
              350086478  585.482    0.000  766.331    0.000 layers.py:62(check)
                3442918  122.971    0.000  759.060    0.000 levels.py:199(generate)
               98144896  710.074    0.000  710.074    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
        9223092712/9223092709  630.992    0.000  699.847    0.000 {built-in method builtins.len}
               98144896  662.763    0.000  662.763    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              350517800  442.517    0.000  655.019    0.000 layers.py:113(isDone)
               98144896  646.085    0.000  646.085    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              350086478  383.407    0.000  601.426    0.000 layers.py:273(check)
              350086478  380.652    0.000  598.964    0.000 layers.py:313(check)
                8843057  221.619    0.000  597.589    0.000 exploration.py:53(softmaxer)
               13896190  222.379    0.000  584.961    0.000 random.py:315(sample)
              687014356  465.778    0.000  578.752    0.000 tensor.py:906(grad)
                3505177  326.002    0.000  555.428    0.000 collector.py:46(collect)
             6864482303  541.574    0.000  541.574    0.000 {built-in method builtins.hash}
                6885836   59.900    0.000  516.571    0.000 level.py:41(notUsed)
               98144896  494.415    0.000  494.415    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              350086478  335.820    0.000  493.887    0.000 layers.py:48(check)
               10515525   15.785    0.000  467.919    0.000 loss.py:527(forward)
               10515525   42.038    0.000  452.134    0.000 functional.py:2898(mse_loss)
                1846318  400.478    0.000  424.212    0.000 agent.py:186(convert_values)
              350086478  273.271    0.000  405.527    0.000 layers.py:23(check)
               34429180   48.362    0.000  333.748    0.000 layer.py:69(restart)
              154454799  332.999    0.000  332.999    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
             3865216411  331.134    0.000  331.134    0.000 {method 'random' of '_random.Random' objects}
              310209475  228.466    0.000  319.395    0.000 layer.py:126(remove)
             2707272076  310.604    0.000  310.604    0.000 layer.py:203(isBlocking)
              514209821  226.433    0.000  309.904    0.000 layer.py:130(add)
               56430496   45.749    0.000  286.683    0.000 flatten.py:39(forward)
              416277838  194.862    0.000  286.249    0.000 random.py:250(_randbelow_with_getrandbits)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9551815: <Causal4_Cf_convert3_TopN3_0> in cluster <dcc> Done

Job <Causal4_Cf_convert3_TopN3_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed Apr 21 03:20:31 2021
Job was executed on host(s) <n-62-20-16>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Thu Apr 22 03:36:30 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Apr 22 03:36:30 2021
Terminated at Fri Apr 23 03:31:47 2021
Results reported at Fri Apr 23 03:31:47 2021

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

    CPU time :                                   85892.89 sec.
    Max Memory :                                 9933 MB
    Average Memory :                             6589.70 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               6451.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86116 sec.
    Turnaround time :                            173476 sec.

The output (if any) is above this job summary.

