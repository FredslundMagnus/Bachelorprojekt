
# Parameters

    Name :                      SuperCausal_tele-0
    Main :                      teleport
    Level :                     Levels.CausalSuper
    Failed actions chance :     0
    Use model :                 False
    Depth :                     1
    Model explore :             100000
    Samples :                   5
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
    Layer super1 :              True
    Layer super2 :              True
    Layer super3 :              True
    Layer super4 :              True
    Layer super5 :              True
    Layer super6 :              True
    Layer super7 :              True
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
    Num :                       0
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      111820136828 function calls (111543619441 primitive calls) in 86114.00 seconds

##    Ordered by: cumulative time
   List reduced from 491 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86114.004 86114.004 {built-in method builtins.exec}
                      1    1.606    1.606 86114.004 86114.004 <string>:1(<module>)
                      1  231.231  231.231 86112.398 86112.398 main.py:46(teleport)
                4946696   21.917    0.000 30606.860    0.006 game.py:42(step)
                4946696   29.459    0.000 29392.551    0.006 layers.py:827(step)
                9893392   37.309    0.000 28314.786    0.003 agent.py:29(learn)
                9893392  733.162    0.000 23953.448    0.002 learner.py:42(Qlearn)
                4946696  379.992    0.000 21384.115    0.004 layers.py:17(step)
              494669600  794.324    0.000 20960.913    0.000 layer.py:106(move)
                4946696  521.872    0.000 17061.627    0.003 agent.py:54(_learn)
              494669600 2204.113    0.000 15871.510    0.000 layers.py:844(check)
        311101698/34585322 1258.268    0.000 11368.568    0.000 module.py:866(_call_impl)
                4946696  145.431    0.000 11196.824    0.002 agent.py:117(_learn)
               24691930   72.088    0.000 10589.907    0.000 network.py:28(forward)
               24691930  329.464    0.000 10361.493    0.000 container.py:117(forward)
                9893392   82.873    0.000 10106.573    0.001 optimizer.py:84(wrapper)
                9893392   42.295    0.000 9708.097    0.001 grad_mode.py:24(decorate_context)
                9893392  277.852    0.000 9572.632    0.001 adam.py:55(step)
                9893392 1969.311    0.000 8985.484    0.001 _functional.py:53(adam)
                4946697  652.582    0.000 7943.663    0.002 layers.py:793(update)
                9851842  243.821    0.000 7063.262    0.001 agent.py:49(__call__)
                4946696 3383.146    0.001 6836.165    0.001 agent.py:88(interveen)
                4946696 3608.164    0.001 6676.663    0.001 replaybuffer.py:28(teleporter_save_data)
                9893392   40.401    0.000 5958.520    0.001 tensor.py:195(backward)
                9893392   37.930    0.000 5916.639    0.001 __init__.py:68(backward)
                9893392 5655.512    0.001 5655.512    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                4946696 3752.832    0.001 5360.982    0.001 replaybuffer.py:22(sample_data)
                4946696 2746.029    0.001 4162.593    0.001 agent.py:67(modify)
            18034267025 2733.488    0.000 3976.587    0.000 enum.py:646(__hash__)
               49383860  108.599    0.000 3801.798    0.000 conv.py:398(forward)
               49383860   70.645    0.000 3647.020    0.000 conv.py:390(_conv_forward)
              494669600  961.159    0.000 3588.458    0.000 layers.py:838(isFree)
               49383860 3576.375    0.000 3576.375    0.000 {built-in method conv2d}
              494669600 1960.214    0.000 3177.987    0.000 layers.py:734(check)
               64182398  127.660    0.000 2953.902    0.000 linear.py:93(forward)
               49466970 1579.533    0.000 2820.478    0.000 layer.py:175(NoRock_update)
               64182398   53.852    0.000 2768.263    0.000 functional.py:1737(linear)
              494669600 1695.059    0.000 2736.117    0.000 layers.py:700(check)
               64182398 2701.715    0.000 2701.715    0.000 {built-in method torch._C._nn.linear}
             4892357641 2099.985    0.000 2627.299    0.000 layer.py:103(isFree)
              203494742 2548.585    0.000 2548.585    0.000 {built-in method clone}
              494669600 1549.336    0.000 2503.006    0.000 layers.py:717(check)
                4946696   73.651    0.000 2232.154    0.000 agent.py:112(__call__)
               14798538  101.489    0.000 2140.397    0.000 agent.py:59(modify_board)
              492231235  469.115    0.000 2048.979    0.000 {built-in method builtins.any}
              178081056 1840.988    0.000 1840.988    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               21115137 1754.961    0.000 1754.961    0.000 {built-in method tensor}
               88874328   74.099    0.000 1662.497    0.000 activation.py:713(forward)
               39532018 1636.695    0.000 1636.695    0.000 {built-in method cat}
              178081056 1621.010    0.000 1621.010    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               88874328   75.869    0.000 1588.398    0.000 functional.py:1364(leaky_relu)
             5414543574 1300.401    0.000 1579.864    0.000 layers.py:809(<genexpr>)
                2438466   29.358    0.000 1560.346    0.001 layers.py:849(restart)
            16652587048 1535.405    0.000 1535.405    0.000 layer.py:99(positions)
               88874328 1497.681    0.000 1497.681    0.000 {built-in method torch._C._nn.leaky_relu}
                9893392  227.843    0.000 1404.705    0.000 optimizer.py:189(zero_grad)
                9893392   12.234    0.000 1399.415    0.000 game.py:38(board)
               14798538 1361.221    0.000 1361.221    0.000 {built-in method torch._C._nn.one_hot}
                2438466   14.116    0.000 1345.860    0.001 level.py:8(__init__)
              494669600  804.232    0.000 1273.944    0.000 layers.py:686(check)
                4946696   85.502    0.000 1263.513    0.000 replaybuffer.py:18(stacker)
            18034302992 1243.105    0.000 1243.105    0.000 {built-in method builtins.hash}
              494669600  768.744    0.000 1235.972    0.000 layers.py:672(check)
              494669600  752.175    0.000 1207.086    0.000 layers.py:658(check)
                2438466   43.093    0.000 1195.149    0.000 levels.py:261(generate)
               20019000  182.632    0.000 1107.003    0.000 level.py:41(notUsed)
                4946696  606.858    0.000 1006.423    0.000 collector.py:46(collect)
               89040528  996.334    0.000  996.334    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               89040528  858.183    0.000  858.183    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               89040528  840.197    0.000  840.197    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               89040528  832.245    0.000  832.245    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                9851842  272.846    0.000  742.928    0.000 exploration.py:53(softmaxer)
             1174456431  720.913    0.000  720.913    0.000 layer.py:154(elements)
              218293280  689.825    0.000  689.825    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              494669700   95.576    0.000  680.603    0.000 {built-in method builtins.all}
             1124299949  241.786    0.000  641.549    0.000 layers.py:799(<genexpr>)
               89040528  636.732    0.000  636.732    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              494669600  380.548    0.000  582.506    0.000 layers.py:646(check)
        7382847379/7382847377  493.227    0.000  565.627    0.000 {built-in method builtins.len}
               20019000   15.031    0.000  533.874    0.000 level.py:38(elementsIn)
              623283750  416.887    0.000  516.717    0.000 tensor.py:906(grad)
              494669600  330.921    0.000  497.335    0.000 layers.py:23(check)
                9893392   14.480    0.000  483.413    0.000 loss.py:527(forward)
                9893392   36.930    0.000  468.933    0.000 functional.py:2898(mse_loss)
             4892357641  445.703    0.000  445.703    0.000 layer.py:211(isBlocking)
               29680176  425.348    0.000  425.348    0.000 {built-in method sum}
             5463381558  409.059    0.000  409.059    0.000 {method 'random' of '_random.Random' objects}
               20019000  172.331    0.000  346.893    0.000 level.py:39(<listcomp>)
                4946696  121.849    0.000  335.163    0.000 random.py:315(sample)
              445119558  209.414    0.000  311.034    0.000 layer.py:134(remove)
                9893392  307.926    0.000  307.926    0.000 {built-in method torch._C._nn.mse_loss}
              538384353  220.229    0.000  297.355    0.000 layer.py:138(add)
               49383860   37.790    0.000  288.388    0.000 flatten.py:39(forward)
             4922312340  279.463    0.000  279.463    0.000 layer.py:92(isDead)
                9894871  275.066    0.000  275.066    0.000 {built-in method max}
                4946696   22.626    0.000  261.281    0.000 exploration.py:47(epsilonGreedy)
               49383860  250.597    0.000  250.597    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                9851842  236.243    0.000  236.243    0.000 {built-in method multinomial}
              928582776  229.861    0.000  229.861    0.000 level.py:32(inverse)
              126702641  144.793    0.000  217.801    0.000 layers.py:113(isDone)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9672989: <SuperCausal_tele_0> in cluster <dcc> Done

Job <SuperCausal_tele_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Thu May 20 18:43:26 2021
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Thu May 20 18:43:27 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu May 20 18:43:27 2021
Terminated at Fri May 21 18:38:55 2021
Results reported at Fri May 21 18:38:55 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
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

python main.py $MYARGS


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   85893.66 sec.
    Max Memory :                                 9265 MB
    Average Memory :                             5975.33 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               7119.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86171 sec.
    Turnaround time :                            86129 sec.

The output (if any) is above this job summary.

