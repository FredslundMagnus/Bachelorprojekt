
# Parameters

    Name :                      maze_size_19_high_rest_chance-0
    Main :                      teleport
    Hours :                     10.0
    Batch :                     100
    Width :                     19
    Height :                    19
    Network1 :                  Networks.Teleporter
    Network2 :                  Networks.Mini
    Learner1 :                  Learners.Qlearn
    Learner2 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Exploration2 :              Explorations.epsilonGreedy
    Layer blocks :              True
    Layer goal :                True
    Layer gold :                False
    Layer keys :                False
    Layer door :                False
    Layer holder :              False
    Layer putter :              False
    K :                         200000
    Epsilon cap :               0.2
    Softmax cap :               0.03
    Gamma :                     0.98
    Update :                    10000
    Reset chance :              0.005
    Modified done chance :      0.05
    Miss intervention cost :    -0.2
    Intervention cost :         -0.05
    Replay size :               50000
    Sample size :               50
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      13888840266 function calls (13775895279 primitive calls) in 35652.03 seconds

##    Ordered by: cumulative time
   List reduced from 457 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35708.527 35708.527 {built-in method builtins.exec}
                      1    0.829    0.829 35708.526 35708.526 <string>:1(<module>)
                      1   87.515   87.515 35707.698 35707.698 main.py:10(teleport)
                4034790   13.927    0.000 11380.268    0.003 agent.py:26(learn)
                2017395  265.984    0.000 10854.356    0.005 collector.py:36(collect)
               10086975 9822.361    0.001 10562.052    0.001 {built-in method builtins.sum}
                4034790  296.386    0.000 9782.932    0.002 learner.py:42(Qlearn)
                2017395   68.200    0.000 6764.690    0.003 agent.py:50(_learn)
                2017395    8.217    0.000 4937.197    0.002 game.py:21(step)
        127010787/14115219  518.135    0.000 4607.559    0.000 module.py:866(_call_impl)
                2017395   57.582    0.000 4590.324    0.002 agent.py:101(_learn)
                2017395   10.650    0.000 4383.054    0.002 layers.py:212(step)
               10080429   28.673    0.000 4289.656    0.000 network.py:24(forward)
               10080429  137.970    0.000 4199.335    0.000 container.py:117(forward)
                4034790   34.836    0.000 4140.956    0.001 optimizer.py:84(wrapper)
                4034790   17.380    0.000 3975.046    0.001 grad_mode.py:24(decorate_context)
                4034790  110.484    0.000 3919.169    0.001 adam.py:55(step)
                4034790  809.303    0.000 3676.451    0.001 _functional.py:53(adam)
                4028244   93.762    0.000 2846.698    0.001 agent.py:45(__call__)
                2017396  175.443    0.000 2609.172    0.001 layers.py:192(update)
                2017395 1022.999    0.001 2436.415    0.001 agent.py:77(interveen)
                4034790   16.519    0.000 2426.544    0.001 tensor.py:195(backward)
                4034790   15.075    0.000 2409.379    0.001 __init__.py:68(backward)
                4034790 2304.316    0.001 2304.316    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2017395 1074.278    0.001 1968.486    0.001 replaybuffer.py:27(teleporter_save_data)
                2017395  129.812    0.000 1750.516    0.001 layers.py:17(step)
              201739500  136.907    0.000 1601.363    0.000 layer.py:66(move)
                1087512   12.682    0.000 1535.256    0.001 layers.py:233(restart)
               20160858   45.156    0.000 1502.158    0.000 conv.py:398(forward)
                2017395  848.422    0.000 1463.217    0.001 agent.py:59(modify)
               20160858   25.368    0.000 1438.012    0.000 conv.py:390(_conv_forward)
               20160858 1412.644    0.000 1412.644    0.000 {built-in method conv2d}
                2017395  679.269    0.000 1332.044    0.001 replaybuffer.py:23(sample_data)
                1087512    2.365    0.000 1268.769    0.001 levels.py:8(__init__)
                1087512    5.030    0.000 1266.404    0.001 level.py:8(__init__)
                1087512  244.975    0.000 1250.553    0.001 levels.py:11(generate)
              201739500   84.531    0.000 1219.831    0.000 layers.py:223(isFree)
               26206497   53.551    0.000 1210.062    0.000 linear.py:93(forward)
              292677392 1084.094    0.000 1135.301    0.000 layer.py:63(isFree)
               26206497   22.079    0.000 1132.554    0.000 functional.py:1737(linear)
               26206497 1105.585    0.000 1105.585    0.000 {built-in method torch._C._nn.linear}
                2017395   28.733    0.000  905.849    0.000 agent.py:96(__call__)
                6045639   41.236    0.000  872.937    0.000 agent.py:54(modify_board)
                8544651  833.257    0.000  833.257    0.000 {built-in method tensor}
               12105174   22.312    0.000  771.275    0.000 tensor.py:575(__iter__)
               60150635  762.735    0.000  762.735    0.000 {built-in method clone}
               72626220  737.485    0.000  737.485    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               12105174  726.585    0.000  726.585    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
                4034790    5.031    0.000  689.801    0.000 game.py:17(board)
                1087512  349.694    0.000  685.775    0.001 levels.py:76(RFS)
               36286926   28.358    0.000  682.985    0.000 activation.py:713(forward)
               16132614  664.390    0.000  664.390    0.000 {built-in method cat}
               72626220  663.810    0.000  663.810    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               36286926   32.301    0.000  654.627    0.000 functional.py:1364(leaky_relu)
               36286926  616.133    0.000  616.133    0.000 {built-in method torch._C._nn.leaky_relu}
                4034790   97.303    0.000  592.688    0.000 optimizer.py:189(zero_grad)
                6045639  560.796    0.000  560.796    0.000 {built-in method torch._C._nn.one_hot}
                2017395   35.454    0.000  518.105    0.000 replaybuffer.py:19(stacker)
              201739600   51.487    0.000  498.181    0.000 {built-in method builtins.all}
              605298027  133.115    0.000  468.458    0.000 layers.py:197(<genexpr>)
               36313110  411.091    0.000  411.091    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               36313110  356.209    0.000  356.209    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                6052188  179.755    0.000  348.900    0.000 layer.py:90(update)
               36313110  344.807    0.000  344.807    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               36313110  342.916    0.000  342.916    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              201739600  211.969    0.000  319.878    0.000 layers.py:65(isDone)
                4028244  109.581    0.000  307.738    0.000 exploration.py:53(softmaxer)
               36313110  270.305    0.000  270.305    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                3262536   23.000    0.000  252.500    0.000 layer.py:40(restart)
              254191824  179.506    0.000  221.208    0.000 tensor.py:906(grad)
               66196274  204.620    0.000  204.620    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                4034790    6.070    0.000  198.410    0.000 loss.py:527(forward)
                4034790   14.857    0.000  192.340    0.000 functional.py:2898(mse_loss)
              201739500  143.744    0.000  186.413    0.000 layers.py:229(check)
                1087612   98.654    0.000  165.897    0.000 layers.py:37(reset)
              348003840  104.716    0.000  160.204    0.000 levels.py:33(<genexpr>)
                3104907   53.877    0.000  141.654    0.000 random.py:315(sample)
              542078450  129.026    0.000  129.026    0.000 layer.py:85(elements)
                4034790  126.446    0.000  126.446    0.000 {built-in method torch._C._nn.mse_loss}
              265153570   87.504    0.000  116.811    0.000 layer.py:76(add)
               20160858   13.121    0.000  115.092    0.000 flatten.py:39(forward)
        662108693/662108691   81.267    0.000  115.035    0.000 {built-in method builtins.len}
              191197533   79.624    0.000  114.944    0.000 random.py:250(_randbelow_with_getrandbits)
                4035393  109.793    0.000  109.793    0.000 {built-in method max}
                6052185    8.578    0.000  108.998    0.000 tensor.py:525(__rsub__)
               20160858  101.970    0.000  101.970    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              139115961  101.307    0.000  101.307    0.000 {built-in method torch._C._get_tracing_state}
               88088472   35.996    0.000   99.179    0.000 random.py:285(choice)
                6052185   98.889    0.000   98.889    0.000 {built-in method rsub}
              369216451   67.457    0.000   96.746    0.000 enum.py:646(__hash__)
                4028244   95.585    0.000   95.585    0.000 {built-in method multinomial}
                2017395    7.794    0.000   93.816    0.000 exploration.py:47(epsilonGreedy)
             1055174931   91.351    0.000   91.351    0.000 layer.py:59(positions)
                4034790   86.714    0.000   86.714    0.000 {built-in method gather}
                4034790   16.177    0.000   86.393    0.000 __init__.py:28(_make_grads)
                8069580   19.479    0.000   86.118    0.000 profiler.py:615(__enter__)
               87000960   76.184    0.000   76.184    0.000 {method 'intersection_update' of 'set' objects}
                2017396   71.486    0.000   71.486    0.000 {built-in method nonzero}
                8069580   12.621    0.000   70.680    0.000 profiler.py:607(__init__)
                4034790   66.928    0.000   66.928    0.000 {built-in method ones_like}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-4>
Subject: Job 9393252: <maze_size_19_high_rest_chance_0> in cluster <dcc> Done

Job <maze_size_19_high_rest_chance_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon Mar  8 02:11:21 2021
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon Mar  8 12:06:46 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Mar  8 12:06:46 2021
Terminated at Mon Mar  8 22:02:11 2021
Results reported at Mon Mar  8 22:02:11 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=8G]"
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

    CPU time :                                   35592.36 sec.
    Max Memory :                                 5260 MB
    Average Memory :                             3924.25 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               2932.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35726 sec.
    Turnaround time :                            71450 sec.

The output (if any) is above this job summary.

