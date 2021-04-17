
# Parameters

    Name :                      Newcausal1_CFagent_convert3-0
    Main :                      CFagent
    Level :                     Levels.Causal1
    Hours :                     3.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Network1 :                  Networks.Teleporter
    K1 :                        500000.0
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
    Layer reddoors :            True
    Layer redkeys :             True
    Layer bluedoors :           True
    Layer bluekeys :            True
    Layer pink1 :               True
    Layer pink2 :               True
    Layer pink3 :               True
    Layer brown1 :              True
    Layer brown2 :              True
    Layer brown3 :              True
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                2
    Minutes used :              175 minutes.
    Hours used :                2 hours.

# Profiling


      5245915809 function calls (5207789442 primitive calls) in 10525.21 seconds

##    Ordered by: cumulative time
   List reduced from 484 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 10525.212 10525.212 {built-in method builtins.exec}
                      1    6.772    6.772 10525.212 10525.212 <string>:1(<module>)
                      1   33.361   33.361 10518.439 10518.439 main.py:96(CFagent)
                1164642    4.956    0.000 3884.872    0.003 agent.py:28(learn)
                1164638   98.027    0.000 3228.132    0.003 learner.py:42(Qlearn)
        42595775/4471099  193.864    0.000 1739.185    0.000 module.py:866(_call_impl)
                3306461   10.259    0.000 1634.666    0.000 network.py:24(forward)
                3306461   49.368    0.000 1601.551    0.000 container.py:117(forward)
                 388214   49.360    0.000 1498.671    0.004 agent.py:53(_learn)
                 388214    2.096    0.000 1481.143    0.004 game.py:36(step)
                 388214    2.646    0.000 1395.206    0.004 layers.py:594(step)
                 388214   48.825    0.000 1391.178    0.004 agent.py:189(_learn)
                1164638   11.106    0.000 1356.900    0.001 optimizer.py:84(wrapper)
                1164638    5.727    0.000 1304.788    0.001 grad_mode.py:24(decorate_context)
                1164638   39.034    0.000 1286.661    0.001 adam.py:55(step)
                1164638  268.182    0.000 1205.119    0.001 _functional.py:53(adam)
                 388214  219.882    0.001 1205.043    0.003 agent.py:197(counterfact)
                 388214  593.725    0.002 1086.933    0.003 replaybuffer.py:28(teleporter_save_data)
                 388214   13.360    0.000  986.442    0.003 agent.py:114(_learn)
                1070736   33.106    0.000  853.174    0.001 agent.py:48(__call__)
                1164638    5.490    0.000  815.041    0.001 tensor.py:195(backward)
                1164638    4.920    0.000  809.366    0.001 __init__.py:68(backward)
                1164638  776.105    0.001  776.105    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                 388214  445.425    0.001  752.362    0.002 agent.py:85(interveen)
                 388215   45.446    0.000  719.396    0.002 layers.py:565(update)
                 388214   35.685    0.000  669.528    0.002 layers.py:18(step)
               38789511   50.988    0.000  630.095    0.000 layer.py:82(move)
                 388214  438.130    0.001  625.033    0.002 replaybuffer.py:22(sample_data)
                6612922   16.726    0.000  570.513    0.000 conv.py:398(forward)
                6612922    9.739    0.000  546.246    0.000 conv.py:390(_conv_forward)
                6612922  536.507    0.000  536.507    0.000 {built-in method conv2d}
                 388214  344.682    0.001  514.168    0.001 replaybuffer.py:49(sample_data)
               34560070  486.016    0.000  486.016    0.000 {built-in method clone}
                9142955   21.384    0.000  467.245    0.000 linear.py:93(forward)
                9142955    8.623    0.000  435.969    0.000 functional.py:1737(linear)
                9142955  425.272    0.000  425.272    0.000 {built-in method torch._C._nn.linear}
                5374102  419.392    0.000  419.392    0.000 {built-in method tensor}
                4486137    3.690    0.000  392.376    0.000 game.py:32(board)
                 294663    3.212    0.000  390.760    0.001 agent.py:167(choose_action)
                4658574  220.120    0.000  367.932    0.000 layer.py:143(NoRock_update)
                 388214  218.985    0.001  349.880    0.001 agent.py:66(modify)
                1085764    9.852    0.000  349.781    0.000 layers.py:615(restart)
                5729284  306.788    0.000  306.788    0.000 {built-in method cat}
               38789511   69.874    0.000  266.335    0.000 layers.py:611(check)
               38776599   50.776    0.000  263.910    0.000 layers.py:605(isFree)
               12449416   12.035    0.000  261.867    0.000 activation.py:713(forward)
                1085764    4.865    0.000  258.808    0.000 level.py:8(__init__)
               12449416   12.087    0.000  249.832    0.000 functional.py:1364(leaky_relu)
                 388214  120.210    0.000  246.726    0.001 replaybuffer.py:55(CF_save_data)
               21739904  243.865    0.000  243.865    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               12449416  235.515    0.000  235.515    0.000 {built-in method torch._C._nn.leaky_relu}
                1458950   11.008    0.000  228.667    0.000 agent.py:58(modify_board)
                1085764   13.714    0.000  221.308    0.000 levels.py:122(generate)
                 388210    8.237    0.000  218.689    0.001 agent.py:163(__call__)
               21739904  215.170    0.000  215.170    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              210489420  178.832    0.000  213.134    0.000 layer.py:79(isFree)
                 388214    7.517    0.000  200.730    0.001 agent.py:109(__call__)
                4234690   37.628    0.000  195.436    0.000 level.py:41(notUsed)
                1164638   31.269    0.000  188.328    0.000 optimizer.py:189(zero_grad)
                 388214   15.498    0.000  155.991    0.000 replaybuffer.py:18(stacker)
                1458950  144.481    0.000  144.481    0.000 {built-in method torch._C._nn.one_hot}
                 388210   17.169    0.000  139.747    0.000 replaybuffer.py:45(stacker)
               10869952  133.719    0.000  133.719    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               36407230  122.589    0.000  122.589    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               38821500   13.495    0.000  119.972    0.000 {built-in method builtins.all}
               10869952  118.891    0.000  118.891    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              130780924   35.377    0.000  111.535    0.000 layers.py:571(<genexpr>)
               10869952  111.497    0.000  111.497    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               10869952  110.278    0.000  110.278    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              346426309   64.462    0.000   91.891    0.000 enum.py:646(__hash__)
                1070736   32.133    0.000   88.263    0.000 exploration.py:53(softmaxer)
                 388214   52.882    0.000   87.800    0.000 collector.py:54(collect)
              160154293   85.937    0.000   85.937    0.000 layer.py:122(elements)
               10869952   84.996    0.000   84.996    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                6514584    6.878    0.000   78.647    0.000 layer.py:56(restart)
                4234690    3.433    0.000   77.826    0.000 level.py:38(elementsIn)
               38789511   48.162    0.000   74.240    0.000 layers.py:143(check)
               76089748   56.375    0.000   69.873    0.000 tensor.py:906(grad)
               38821500   47.433    0.000   69.690    0.000 layers.py:111(isDone)
                1164638    1.905    0.000   63.316    0.000 loss.py:527(forward)
                1164638    4.752    0.000   61.411    0.000 functional.py:2898(mse_loss)
        660828775/660828772   51.933    0.000   60.496    0.000 {built-in method builtins.len}
                1085864   29.829    0.000   59.721    0.000 layers.py:33(reset)
                 776428   22.607    0.000   59.124    0.000 random.py:315(sample)
              195330530   56.412    0.000   56.412    0.000 level.py:32(inverse)
                1164643   56.370    0.000   56.370    0.000 {built-in method nonzero}
               38789511   38.127    0.000   56.255    0.000 layers.py:47(check)
               38789511   36.392    0.000   55.526    0.000 layers.py:124(check)
               34874161   41.347    0.000   51.321    0.000 layer.py:102(remove)
                4234690   24.415    0.000   48.079    0.000 level.py:39(<listcomp>)
               75888871   32.806    0.000   44.601    0.000 layer.py:106(add)
              444381078   43.167    0.000   43.167    0.000 layer.py:75(positions)
                6612922    5.112    0.000   42.581    0.000 flatten.py:39(forward)
                1164638   40.818    0.000   40.818    0.000 {built-in method torch._C._nn.mse_loss}
                6612922   37.469    0.000   37.469    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                2329284   37.139    0.000   37.139    0.000 {built-in method sum}
                1164783   36.461    0.000   36.461    0.000 {built-in method max}
               43667080   32.983    0.000   32.983    0.000 {built-in method torch._C._get_tracing_state}
                1552852    2.501    0.000   31.498    0.000 tensor.py:525(__rsub__)
                2184847   30.790    0.000   30.790    0.000 {method 'item' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-14>
Subject: Job 9493846: <Newcausal1_CFagent_convert3_0> in cluster <dcc> Done

Job <Newcausal1_CFagent_convert3_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sat Apr  3 15:09:50 2021
Job was executed on host(s) <n-62-20-14>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sat Apr  3 15:09:51 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat Apr  3 15:09:51 2021
Terminated at Sat Apr  3 18:05:24 2021
Results reported at Sat Apr  3 18:05:24 2021

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

    CPU time :                                   10487.52 sec.
    Max Memory :                                 4071 MB
    Average Memory :                             3669.40 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               12313.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   10533 sec.
    Turnaround time :                            10534 sec.

The output (if any) is above this job summary.

