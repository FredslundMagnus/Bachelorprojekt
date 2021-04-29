
# Parameters

    Name :                      DoorsAndKey_teleport-1
    Main :                      teleport
    Level :                     Levels.Causal1
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


      83329736608 function calls (83038701161 primitive calls) in 86118.23 seconds

##    Ordered by: cumulative time
   List reduced from 473 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86118.232 86118.232 {built-in method builtins.exec}
                      1    1.524    1.524 86118.232 86118.232 <string>:1(<module>)
                      1  214.072  214.072 86116.707 86116.707 main.py:45(teleport)
               10395218   36.038    0.000 27579.121    0.003 agent.py:29(learn)
               10395218  650.250    0.000 23228.014    0.002 learner.py:42(Qlearn)
                5197609   20.898    0.000 21848.740    0.004 game.py:41(step)
                5197609   25.555    0.000 20837.054    0.004 layers.py:718(step)
                5197609  162.003    0.000 16649.823    0.003 agent.py:54(_learn)
                5197609 6808.610    0.001 12253.330    0.002 replaybuffer.py:28(teleporter_save_data)
                5197610  698.753    0.000 11555.983    0.002 layers.py:684(update)
        327415060/36380624 1155.917    0.000 11362.448    0.000 module.py:715(_call_impl)
                5197609  136.104    0.000 10873.643    0.002 agent.py:117(_learn)
               25985406   63.465    0.000 10601.457    0.000 network.py:27(forward)
               25985406  278.471    0.000 10390.565    0.000 container.py:115(forward)
                5197609 6191.768    0.001 9679.041    0.002 agent.py:88(interveen)
               10395218   62.320    0.000 9298.049    0.001 grad_mode.py:23(decorate_context)
                5197609  390.817    0.000 9220.385    0.002 layers.py:17(step)
               10395218  308.128    0.000 9118.845    0.001 adam.py:55(step)
              519760900  811.656    0.000 8784.511    0.000 layer.py:98(move)
               10395218 1667.518    0.000 7506.781    0.001 functional.py:53(adam)
               10392579  211.280    0.000 7041.657    0.001 agent.py:49(__call__)
                5197609 3967.793    0.001 6143.222    0.001 replaybuffer.py:22(sample_data)
               10395218   63.453    0.000 5552.832    0.001 tensor.py:181(backward)
               10395218   34.852    0.000 5489.379    0.001 __init__.py:68(backward)
               15979550  117.303    0.000 5247.630    0.000 layers.py:740(restart)
               10395218 5235.512    0.001 5235.512    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                5197609 2617.883    0.001 4791.525    0.001 agent.py:67(modify)
              519760900 1329.970    0.000 4405.729    0.000 layers.py:735(check)
              445241128 4312.782    0.000 4312.782    0.000 {built-in method clone}
               15979550   59.439    0.000 4072.667    0.000 level.py:8(__init__)
               51970812   84.057    0.000 3865.877    0.000 conv.py:422(forward)
               51970812   94.046    0.000 3749.458    0.000 conv.py:414(_conv_forward)
               51970812 3638.677    0.000 3638.677    0.000 {built-in method conv2d}
               15979550  172.972    0.000 3439.824    0.000 levels.py:122(generate)
               67561000  139.962    0.000 3317.214    0.000 linear.py:92(forward)
               67561000  237.645    0.000 3114.957    0.000 functional.py:1669(linear)
               62320431  543.862    0.000 3108.582    0.000 level.py:41(notUsed)
              519760900  615.385    0.000 2776.347    0.000 layers.py:729(isFree)
               31185660 1394.696    0.000 2334.115    0.000 layer.py:167(NoRock_update)
              654898788 1384.647    0.000 2325.054    0.000 tensor.py:933(grad)
             1444534481  697.625    0.000 2265.930    0.000 {built-in method builtins.any}
                5197609   63.795    0.000 2218.993    0.000 agent.py:112(__call__)
               67561000 2201.241    0.000 2201.241    0.000 {built-in method addmm}
               41578233 2182.340    0.000 2182.340    0.000 {built-in method cat}
             3002678599 1742.758    0.000 2160.961    0.000 layer.py:95(isFree)
               15590188  102.932    0.000 2157.321    0.000 agent.py:59(modify_board)
               10395218  195.055    0.000 2023.148    0.000 optimizer.py:167(zero_grad)
                5197609   80.110    0.000 1813.205    0.000 replaybuffer.py:18(stacker)
              556146793  274.100    0.000 1661.391    0.000 {built-in method builtins.all}
              187113924 1495.834    0.000 1495.834    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
             5946033127 1001.914    0.000 1463.793    0.000 enum.py:646(__hash__)
               93546406   73.203    0.000 1450.147    0.000 activation.py:713(forward)
             2830707273  733.150    0.000 1425.348    0.000 layers.py:690(<genexpr>)
               62320431   45.064    0.000 1422.954    0.000 level.py:38(elementsIn)
               15590188 1389.379    0.000 1389.379    0.000 {built-in method torch._C._nn.one_hot}
               22165937 1379.228    0.000 1379.228    0.000 {built-in method tensor}
               93546406  113.493    0.000 1376.943    0.000 functional.py:1292(leaky_relu)
              852401594  433.175    0.000 1280.954    0.000 overrides.py:1070(has_torch_function)
               93546406 1252.156    0.000 1252.156    0.000 {built-in method torch._C._nn.leaky_relu}
              187113924 1247.637    0.000 1247.637    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              460831316 1221.884    0.000 1221.884    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               36385793  177.230    0.000 1201.940    0.000 tensor.py:21(wrapped)
             3526470150  890.416    0.000 1090.117    0.000 layers.py:700(<genexpr>)
               10395218   13.637    0.000 1063.297    0.000 game.py:37(board)
               95877300   84.329    0.000 1023.707    0.000 layer.py:69(restart)
               93556962  937.572    0.000  937.572    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               62320431  457.464    0.000  917.563    0.000 level.py:39(<listcomp>)
              519760900  550.185    0.000  876.629    0.000 layers.py:141(check)
                5197609  503.860    0.000  869.370    0.000 collector.py:46(collect)
               93556962  811.368    0.000  811.368    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               15979650  391.547    0.000  783.397    0.000 layers.py:36(reset)
               10392579  270.350    0.000  732.719    0.000 exploration.py:53(softmaxer)
             2874651116  718.565    0.000  718.565    0.000 level.py:32(inverse)
               93556962  705.797    0.000  705.797    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              519760900  444.968    0.000  675.186    0.000 layers.py:48(check)
              519760900  435.902    0.000  668.158    0.000 layers.py:124(check)
               93556962  615.948    0.000  615.948    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
             2287205579  599.567    0.000  599.567    0.000 layer.py:146(elements)
             6517362614  581.885    0.000  581.885    0.000 layer.py:91(positions)
             1120203534  411.694    0.000  569.448    0.000 layer.py:130(add)
               15979550  295.776    0.000  539.045    0.000 level.py:16(<dictcomp>)
              519760900  359.850    0.000  528.145    0.000 layers.py:23(check)
               10395218   14.647    0.000  490.921    0.000 loss.py:445(forward)
        4989288717/4989288715  357.771    0.000  489.755    0.000 {built-in method builtins.len}
             2818800770  485.627    0.000  485.627    0.000 enum.py:352(<genexpr>)
               10395218   56.367    0.000  476.274    0.000 functional.py:2637(mse_loss)
               93556962  473.964    0.000  473.964    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
             1808748942  381.638    0.000  471.583    0.000 overrides.py:1083(<genexpr>)
             5946070894  461.885    0.000  461.885    0.000 {built-in method builtins.hash}
               62320431  285.224    0.000  460.327    0.000 {built-in method _functools.reduce}
               25988045  442.397    0.000  442.397    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               67561000  394.442    0.000  394.442    0.000 {method 't' of 'torch._C._TensorBase' objects}
              217346356  252.765    0.000  379.536    0.000 layers.py:113(isDone)
              521300569  240.926    0.000  355.884    0.000 layer.py:126(remove)
               31185654  354.056    0.000  354.056    0.000 {built-in method sum}
                5197609  128.404    0.000  353.274    0.000 random.py:315(sample)
                5199687  329.067    0.000  329.067    0.000 {method 'ne' of 'torch._C._TensorBase' objects}
             3730272173  291.828    0.000  291.828    0.000 {method 'random' of '_random.Random' objects}
               10395218  276.336    0.000  276.336    0.000 {built-in method torch._C._nn.mse_loss}
               51970812   37.533    0.000  271.562    0.000 flatten.py:39(forward)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9550927: <DoorsAndKey_teleport_1> in cluster <dcc> Done

Job <DoorsAndKey_teleport_1> was submitted from host <n-62-30-4> by user <s183905> in cluster <dcc> at Tue Apr 20 16:21:53 2021
Job was executed on host(s) <n-62-20-7>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Tue Apr 27 08:57:05 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue Apr 27 08:57:05 2021
Terminated at Wed Apr 28 08:52:34 2021
Results reported at Wed Apr 28 08:52:34 2021

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

    CPU time :                                   86077.88 sec.
    Max Memory :                                 2680 MB
    Average Memory :                             2674.28 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13704.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86129 sec.
    Turnaround time :                            664241 sec.

The output (if any) is above this job summary.

