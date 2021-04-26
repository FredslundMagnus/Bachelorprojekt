
# Parameters

    Name :                      Diamonds1_teleport-2
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


      75655632373 function calls (75423528086 primitive calls) in 86110.24 seconds

##    Ordered by: cumulative time
   List reduced from 471 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86110.242 86110.242 {built-in method builtins.exec}
                      1    1.477    1.477 86110.242 86110.242 <string>:1(<module>)
                      1  188.545  188.545 86108.764 86108.764 main.py:45(teleport)
                8289950   29.525    0.000 28238.583    0.003 agent.py:29(learn)
                8289950  674.229    0.000 24188.410    0.003 learner.py:42(Qlearn)
                4144975   16.485    0.000 19426.843    0.005 game.py:41(step)
                4144975   24.312    0.000 18473.224    0.004 layers.py:718(step)
                4144975  133.594    0.000 16973.110    0.004 agent.py:54(_learn)
                4144975 7542.346    0.002 14402.841    0.003 replaybuffer.py:28(teleporter_save_data)
                4144975  113.280    0.000 11220.367    0.003 agent.py:117(_learn)
        261116824/29013548  976.526    0.000 10975.345    0.000 module.py:715(_call_impl)
                4144975 7299.944    0.002 10660.045    0.003 agent.py:88(interveen)
                8289950   49.210    0.000 10364.051    0.001 grad_mode.py:23(decorate_context)
               20723598   52.086    0.000 10269.915    0.000 network.py:27(forward)
                8289950  255.984    0.000 10223.190    0.001 adam.py:55(step)
               20723598  261.793    0.000 10103.839    0.000 container.py:115(forward)
                4144975  302.303    0.000 9498.127    0.002 layers.py:17(step)
              414497500  637.594    0.000 9161.489    0.000 layer.py:98(move)
                4144976  553.541    0.000 8923.737    0.002 layers.py:684(update)
                8289950 1887.699    0.000 8843.340    0.001 functional.py:53(adam)
                8288673  184.476    0.000 6752.485    0.001 agent.py:49(__call__)
              414497500 1182.874    0.000 5637.396    0.000 layers.py:735(check)
                8289950   49.671    0.000 5541.234    0.001 tensor.py:181(backward)
                8289950   29.865    0.000 5491.563    0.001 __init__.py:68(backward)
              387842690 5359.311    0.000 5359.311    0.000 {built-in method clone}
                8289950 5249.268    0.001 5249.268    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                4144975 3010.796    0.001 4893.182    0.001 replaybuffer.py:22(sample_data)
                4144975 2599.389    0.001 4726.349    0.001 agent.py:67(modify)
               10532831   84.409    0.000 3852.820    0.000 layers.py:740(restart)
               41447196   69.663    0.000 3667.057    0.000 conv.py:422(forward)
               41447196   75.702    0.000 3571.820    0.000 conv.py:414(_conv_forward)
               41447196 3482.541    0.000 3482.541    0.000 {built-in method conv2d}
               53880844  116.292    0.000 3305.318    0.000 linear.py:92(forward)
               53880844  203.130    0.000 3138.544    0.000 functional.py:1669(linear)
               10532831   39.988    0.000 3075.581    0.000 level.py:8(__init__)
               10532831  113.212    0.000 2643.403    0.000 levels.py:151(generate)
               50553655  443.740    0.000 2413.782    0.000 level.py:41(notUsed)
               53880844 2265.364    0.000 2265.364    0.000 {built-in method addmm}
              414497500  574.115    0.000 2264.550    0.000 layers.py:729(isFree)
                4144975   53.684    0.000 2123.425    0.001 agent.py:112(__call__)
              522266904 1329.332    0.000 2091.504    0.000 tensor.py:933(grad)
                8289950  189.224    0.000 2037.509    0.000 optimizer.py:167(zero_grad)
               12433648   91.535    0.000 2034.669    0.000 agent.py:59(modify_board)
               33158523 1974.197    0.000 1974.197    0.000 {built-in method cat}
               29014832 1146.352    0.000 1952.217    0.000 layer.py:167(NoRock_update)
             1154199045  583.163    0.000 1935.522    0.000 {built-in method builtins.any}
              149219100 1845.225    0.000 1845.225    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
             7128902347 1170.053    0.000 1697.440    0.000 enum.py:646(__hash__)
             2862089206 1359.436    0.000 1690.436    0.000 layer.py:95(isFree)
              400276338 1615.834    0.000 1615.834    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                4144975   69.971    0.000 1596.562    0.000 replaybuffer.py:18(stacker)
              149219100 1562.351    0.000 1562.351    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               74604442   58.755    0.000 1514.541    0.000 activation.py:713(forward)
               74604442   96.416    0.000 1455.787    0.000 functional.py:1292(leaky_relu)
               74604442 1350.455    0.000 1350.455    0.000 {built-in method torch._C._nn.leaky_relu}
               17742870 1305.487    0.000 1305.487    0.000 {built-in method tensor}
               12433648 1275.978    0.000 1275.978    0.000 {built-in method torch._C._nn.one_hot}
              443514571  198.375    0.000 1168.010    0.000 {built-in method builtins.all}
               50553655   35.488    0.000 1138.728    0.000 level.py:38(elementsIn)
              414497500  692.028    0.000 1130.894    0.000 layers.py:207(check)
               29016971  155.835    0.000 1092.302    0.000 tensor.py:21(wrapped)
              414497500  672.017    0.000 1091.560    0.000 layers.py:231(check)
              414497500  636.323    0.000 1039.578    0.000 layers.py:219(check)
              679773531  350.686    0.000 1039.454    0.000 overrides.py:1070(has_torch_function)
               74609550 1017.346    0.000 1017.346    0.000 {method 'add' of 'torch._C._TensorBase' objects}
             2107256408  517.680    0.000  997.783    0.000 layers.py:690(<genexpr>)
                8289950    9.996    0.000  982.629    0.000 game.py:37(board)
                4144975  579.976    0.000  977.218    0.000 collector.py:46(collect)
             3231718152  796.346    0.000  968.300    0.000 layers.py:700(<genexpr>)
               74609550  925.865    0.000  925.865    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               74609550  831.685    0.000  831.685    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               74609550  751.727    0.000  751.727    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               50553655  362.541    0.000  739.205    0.000 level.py:39(<listcomp>)
                8288673  260.077    0.000  730.312    0.000 exploration.py:53(softmaxer)
             7473763661  679.087    0.000  679.087    0.000 layer.py:91(positions)
               73729817   57.492    0.000  668.788    0.000 layer.py:69(restart)
               74609550  588.441    0.000  588.441    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
             7128932554  527.393    0.000  527.393    0.000 {built-in method builtins.hash}
               10532931  256.277    0.000  511.768    0.000 layers.py:36(reset)
             1625496928  499.591    0.000  499.591    0.000 layer.py:146(elements)
             2427216631  490.816    0.000  490.816    0.000 level.py:32(inverse)
              414497500  311.056    0.000  485.163    0.000 layers.py:196(check)
                8289950   11.884    0.000  472.832    0.000 loss.py:445(forward)
                8289950   44.857    0.000  460.948    0.000 functional.py:2637(mse_loss)
               20724875  453.843    0.000  453.843    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
        4390296641/4390296639  316.222    0.000  437.859    0.000 {built-in method builtins.len}
               53880844  436.148    0.000  436.148    0.000 {method 't' of 'torch._C._TensorBase' objects}
              414497500  283.093    0.000  421.337    0.000 layers.py:23(check)
              788973849  299.955    0.000  411.685    0.000 layer.py:130(add)
               24869850  395.449    0.000  395.449    0.000 {built-in method sum}
             1442444049  303.427    0.000  378.502    0.000 overrides.py:1083(<genexpr>)
             2199114986  374.823    0.000  374.823    0.000 enum.py:352(<genexpr>)
               10532831  204.923    0.000  366.952    0.000 level.py:16(<dictcomp>)
               50553655  228.643    0.000  364.035    0.000 {built-in method _functools.reduce}
              421041127  199.132    0.000  290.674    0.000 layer.py:126(remove)
                8289950  288.870    0.000  288.870    0.000 {built-in method torch._C._nn.mse_loss}
               41447196   30.252    0.000  281.190    0.000 flatten.py:39(forward)
                4144975  101.547    0.000  278.429    0.000 random.py:315(sample)
                4146631  266.183    0.000  266.183    0.000 {method 'ne' of 'torch._C._TensorBase' objects}
                8291192  261.830    0.000  261.830    0.000 {built-in method max}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9550898: <Diamonds1_teleport_2> in cluster <dcc> Done

Job <Diamonds1_teleport_2> was submitted from host <n-62-30-4> by user <s183905> in cluster <dcc> at Tue Apr 20 16:21:48 2021
Job was executed on host(s) <n-62-20-5>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Thu Apr 22 07:07:39 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Apr 22 07:07:39 2021
Terminated at Fri Apr 23 07:02:55 2021
Results reported at Fri Apr 23 07:02:55 2021

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

    CPU time :                                   85891.88 sec.
    Max Memory :                                 2682 MB
    Average Memory :                             2679.59 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13702.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86117 sec.
    Turnaround time :                            225667 sec.

The output (if any) is above this job summary.

