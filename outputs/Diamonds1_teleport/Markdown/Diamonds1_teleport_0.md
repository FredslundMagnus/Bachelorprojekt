
# Parameters

    Name :                      Diamonds1_teleport-0
    Main :                      teleport
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


      72839720760 function calls (72613479193 primitive calls) in 86115.24 seconds

##    Ordered by: cumulative time
   List reduced from 472 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86115.235 86115.235 {built-in method builtins.exec}
                      1    1.669    1.669 86115.235 86115.235 <string>:1(<module>)
                      1  275.363  275.363 86113.566 86113.566 main.py:45(teleport)
                8080544   42.313    0.000 25558.187    0.003 agent.py:29(learn)
                4040272   24.297    0.000 22535.879    0.006 game.py:41(step)
                4040272   30.970    0.000 21507.842    0.005 layers.py:718(step)
                8080544  638.245    0.000 21206.617    0.003 learner.py:42(Qlearn)
                4040272  172.066    0.000 15398.802    0.004 agent.py:54(_learn)
                4040272 6793.575    0.002 11965.447    0.003 replaybuffer.py:28(teleporter_save_data)
                4040272  403.841    0.000 11185.206    0.003 layers.py:17(step)
              404027200  715.172    0.000 10744.805    0.000 layer.py:98(move)
        254521237/28280681 1124.238    0.000 10655.737    0.000 module.py:715(_call_impl)
                4040273  639.016    0.000 10243.096    0.003 layers.py:684(update)
                4040272  137.783    0.000 10096.584    0.002 agent.py:117(_learn)
               20200137   62.789    0.000 9858.480    0.000 network.py:27(forward)
               20200137  274.687    0.000 9644.903    0.000 container.py:115(forward)
                4040272 6214.457    0.002 9384.300    0.002 agent.py:88(interveen)
                4040272 6584.576    0.002 8585.612    0.002 replaybuffer.py:22(sample_data)
                8080544   67.382    0.000 8125.567    0.001 grad_mode.py:23(decorate_context)
                8080544  306.632    0.000 7939.603    0.001 adam.py:55(step)
                8079321  258.018    0.000 6702.754    0.001 agent.py:49(__call__)
                8080544 1461.341    0.000 6505.932    0.001 functional.py:53(adam)
              404027200 1276.505    0.000 6310.695    0.000 layers.py:735(check)
                8080544   58.621    0.000 5284.435    0.001 tensor.py:181(backward)
                8080544   43.194    0.000 5225.814    0.001 __init__.py:68(backward)
                8080544 4958.456    0.001 4958.456    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                4040272 2339.294    0.001 4423.855    0.001 agent.py:67(modify)
               10154964  100.419    0.000 4207.280    0.000 layers.py:740(restart)
              379430029 4106.941    0.000 4106.941    0.000 {built-in method clone}
               40400274   73.781    0.000 3668.329    0.000 conv.py:422(forward)
               40400274  100.173    0.000 3554.765    0.000 conv.py:414(_conv_forward)
               40400274 3437.701    0.000 3437.701    0.000 {built-in method conv2d}
               10154964   51.441    0.000 3345.081    0.000 level.py:8(__init__)
               52519867  130.702    0.000 3031.332    0.000 linear.py:92(forward)
              404027200  584.802    0.000 2945.432    0.000 layers.py:729(isFree)
               52519867  214.026    0.000 2832.420    0.000 functional.py:1669(linear)
               10154964  126.542    0.000 2830.754    0.000 levels.py:151(generate)
               48742503  477.444    0.000 2572.491    0.000 level.py:41(notUsed)
               28281911 1520.554    0.000 2568.639    0.000 layer.py:167(NoRock_update)
             2747928064 2006.659    0.000 2360.630    0.000 layer.py:95(isFree)
             1125155690  613.425    0.000 2109.559    0.000 {built-in method builtins.any}
                4040272   79.269    0.000 2068.960    0.001 agent.py:112(__call__)
               12119593  111.129    0.000 2036.915    0.000 agent.py:59(modify_board)
               52519867 2009.237    0.000 2009.237    0.000 {built-in method addmm}
              509074326 1195.286    0.000 1985.858    0.000 tensor.py:933(grad)
               32320953 1951.847    0.000 1951.847    0.000 {built-in method cat}
             7185111875 1279.921    0.000 1864.075    0.000 enum.py:646(__hash__)
                8080544  164.456    0.000 1721.501    0.000 optimizer.py:167(zero_grad)
                4040272   82.563    0.000 1636.563    0.000 replaybuffer.py:18(stacker)
               17302550 1427.837    0.000 1427.837    0.000 {built-in method tensor}
              404027200  867.414    0.000 1337.098    0.000 layers.py:231(check)
               12119593 1316.221    0.000 1316.221    0.000 {built-in method torch._C._nn.one_hot}
              145449792 1309.466    0.000 1309.466    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               72720004   76.774    0.000 1307.118    0.000 activation.py:713(forward)
              432311326  142.402    0.000 1274.090    0.000 {built-in method builtins.all}
              404027200  796.503    0.000 1240.805    0.000 layers.py:207(check)
               72720004  107.992    0.000 1230.344    0.000 functional.py:1292(leaky_relu)
               48742503   38.094    0.000 1200.223    0.000 level.py:38(elementsIn)
             1261411113  333.515    0.000 1162.639    0.000 layers.py:690(<genexpr>)
              404027200  722.387    0.000 1162.557    0.000 layers.py:219(check)
               28284026  169.459    0.000 1156.458    0.000 tensor.py:21(wrapped)
                8080544   15.257    0.000 1128.968    0.000 game.py:37(board)
              391549622 1115.511    0.000 1115.511    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               72720004 1112.443    0.000 1112.443    0.000 {built-in method torch._C._nn.leaky_relu}
              662602398  364.922    0.000 1092.872    0.000 overrides.py:1070(has_torch_function)
             3150978688  871.872    0.000 1081.714    0.000 layers.py:700(<genexpr>)
              145449792 1062.772    0.000 1062.772    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
             7673294908  786.916    0.000  786.916    0.000 layer.py:91(positions)
              404027300  539.084    0.000  786.002    0.000 layers.py:113(isDone)
               48742503  381.778    0.000  776.275    0.000 level.py:39(<listcomp>)
                4040272  440.455    0.000  767.556    0.000 collector.py:46(collect)
               72724896  758.023    0.000  758.023    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               71084748   64.189    0.000  736.351    0.000 layer.py:69(restart)
                8079321  262.492    0.000  734.418    0.000 exploration.py:53(softmaxer)
               72724896  713.453    0.000  713.453    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
             1575174019  702.055    0.000  702.055    0.000 layer.py:146(elements)
               72724896  625.417    0.000  625.417    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
             7185141362  584.159    0.000  584.159    0.000 {built-in method builtins.hash}
               72724896  552.584    0.000  552.584    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               10155064  271.467    0.000  543.149    0.000 layers.py:36(reset)
             2340250691  536.657    0.000  536.657    0.000 level.py:32(inverse)
              404027200  348.227    0.000  535.964    0.000 layers.py:196(check)
                8080544   19.242    0.000  522.579    0.000 loss.py:445(forward)
                8080544   67.740    0.000  503.337    0.000 functional.py:2637(mse_loss)
              764354695  350.427    0.000  501.193    0.000 layer.py:130(add)
              404027200  305.799    0.000  447.983    0.000 layers.py:23(check)
        4289717450/4289717448  320.495    0.000  437.390    0.000 {built-in method builtins.len}
               10154964  253.648    0.000  433.992    0.000 level.py:16(<dictcomp>)
               20201360  409.207    0.000  409.207    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
             1406007882  324.666    0.000  407.857    0.000 overrides.py:1083(<genexpr>)
               72724896  402.876    0.000  402.876    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
             2120310302  400.112    0.000  400.112    0.000 enum.py:352(<genexpr>)
               48742503  240.406    0.000  385.855    0.000 {built-in method _functools.reduce}
               52519867  363.197    0.000  363.197    0.000 {method 't' of 'torch._C._TensorBase' objects}
              409638500  236.628    0.000  358.288    0.000 layer.py:126(remove)
                4040272  135.217    0.000  356.242    0.000 random.py:315(sample)
                4041886  333.900    0.000  333.900    0.000 {method 'ne' of 'torch._C._TensorBase' objects}
               24241632  323.687    0.000  323.687    0.000 {built-in method sum}
                8080544  282.768    0.000  282.768    0.000 {built-in method torch._C._nn.mse_loss}
             2747928064  279.702    0.000  279.702    0.000 layer.py:203(isBlocking)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9550896: <Diamonds1_teleport_0> in cluster <dcc> Done

Job <Diamonds1_teleport_0> was submitted from host <n-62-30-4> by user <s183905> in cluster <dcc> at Tue Apr 20 16:21:48 2021
Job was executed on host(s) <n-62-20-12>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Thu Apr 22 05:22:17 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Apr 22 05:22:17 2021
Terminated at Fri Apr 23 05:17:41 2021
Results reported at Fri Apr 23 05:17:41 2021

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

    CPU time :                                   85888.96 sec.
    Max Memory :                                 2680 MB
    Average Memory :                             2674.60 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13704.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86125 sec.
    Turnaround time :                            219353 sec.

The output (if any) is above this job summary.

