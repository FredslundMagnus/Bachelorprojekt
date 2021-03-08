
# Parameters

    Name :                      maze_size_13_low_rest_chance-0
    Main :                      teleport
    Hours :                     10.0
    Batch :                     100
    Width :                     13
    Height :                    13
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
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.2
    Intervention cost :         -0.05
    Replay size :               50000
    Sample size :               50
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      14036829459 function calls (13931907352 primitive calls) in 35657.85 seconds

##    Ordered by: cumulative time
   List reduced from 457 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35707.799 35707.799 {built-in method builtins.exec}
                      1    0.826    0.826 35707.799 35707.799 <string>:1(<module>)
                      1   85.534   85.534 35706.973 35706.973 main.py:10(teleport)
                3746510   12.628    0.000 10799.887    0.003 agent.py:26(learn)
                1873255  251.507    0.000 10181.519    0.005 collector.py:36(collect)
                9366275 9198.092    0.001 9905.248    0.001 {built-in method builtins.sum}
                3746510  282.457    0.000 9249.216    0.002 learner.py:42(Qlearn)
                1873255   68.181    0.000 6447.338    0.003 agent.py:50(_learn)
        117986751/13110607  482.882    0.000 4458.502    0.000 module.py:866(_call_impl)
                1873255    7.764    0.000 4413.291    0.002 game.py:21(step)
                1873255   58.963    0.000 4328.480    0.002 agent.py:101(_learn)
                9364097   27.397    0.000 4161.372    0.000 network.py:24(forward)
                9364097  128.698    0.000 4076.008    0.000 container.py:117(forward)
                1873255    8.744    0.000 4020.540    0.002 layers.py:212(step)
                3746510   32.637    0.000 3874.260    0.001 optimizer.py:84(wrapper)
                3746510   16.241    0.000 3721.133    0.001 grad_mode.py:24(decorate_context)
                3746510  102.495    0.000 3669.878    0.001 adam.py:55(step)
                3746510  770.196    0.000 3447.537    0.001 _functional.py:53(adam)
                1873255 1895.905    0.001 3417.012    0.002 replaybuffer.py:27(teleporter_save_data)
                1873255 1690.913    0.001 3052.785    0.002 agent.py:77(interveen)
                3744332   93.260    0.000 2750.537    0.001 agent.py:45(__call__)
                1873256  160.494    0.000 2517.661    0.001 layers.py:192(update)
                3746510   16.103    0.000 2305.480    0.001 tensor.py:195(backward)
                3746510   15.135    0.000 2288.853    0.001 __init__.py:68(backward)
                3746510 2188.217    0.001 2188.217    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               18728194   41.512    0.000 1502.889    0.000 conv.py:398(forward)
                1873255  118.790    0.000 1481.791    0.001 layers.py:17(step)
                2191311   16.032    0.000 1450.623    0.001 layers.py:233(restart)
               18728194   25.239    0.000 1443.970    0.000 conv.py:390(_conv_forward)
               18728194 1418.731    0.000 1418.731    0.000 {built-in method conv2d}
                1873255  838.031    0.000 1410.179    0.001 agent.py:59(modify)
              187325500  154.531    0.000 1345.238    0.000 layer.py:66(move)
                1873255  627.183    0.000 1287.635    0.001 replaybuffer.py:23(sample_data)
              102186100 1252.214    0.000 1252.214    0.000 {built-in method clone}
                2191311    3.415    0.000 1172.172    0.001 levels.py:8(__init__)
                2191311    8.574    0.000 1168.757    0.001 level.py:8(__init__)
               24345781   53.388    0.000 1154.952    0.000 linear.py:93(forward)
                2191311  233.493    0.000 1140.117    0.001 levels.py:11(generate)
               24345781   21.070    0.000 1078.905    0.000 functional.py:1737(linear)
               24345781 1053.015    0.000 1053.015    0.000 {built-in method torch._C._nn.linear}
              187325500  106.054    0.000  873.114    0.000 layers.py:223(isFree)
                1873255   27.912    0.000  858.718    0.000 agent.py:96(__call__)
                5617587   36.554    0.000  817.492    0.000 agent.py:54(modify_board)
              427852700  698.915    0.000  767.061    0.000 layer.py:63(isFree)
               11240278   21.318    0.000  738.833    0.000 tensor.py:575(__iter__)
               11240278  696.256    0.000  696.256    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               67437180  695.357    0.000  695.357    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               14983862  671.189    0.000  671.189    0.000 {built-in method cat}
               33709878   28.082    0.000  658.290    0.000 activation.py:713(forward)
               33709878   29.466    0.000  630.208    0.000 functional.py:1364(leaky_relu)
               67437180  619.449    0.000  619.449    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                2191311  310.424    0.000  604.388    0.000 levels.py:76(RFS)
               33709878  594.872    0.000  594.872    0.000 {built-in method torch._C._nn.leaky_relu}
                3746510   88.695    0.000  546.521    0.000 optimizer.py:189(zero_grad)
                1873255   34.028    0.000  534.458    0.000 replaybuffer.py:19(stacker)
                7938185  534.236    0.000  534.236    0.000 {built-in method tensor}
                5617587  526.692    0.000  526.692    0.000 {built-in method torch._C._nn.one_hot}
              187325600   49.232    0.000  459.734    0.000 {built-in method builtins.all}
              563797349  126.930    0.000  433.379    0.000 layers.py:197(<genexpr>)
                3746510    4.419    0.000  406.791    0.000 game.py:17(board)
                5619768  218.999    0.000  396.219    0.000 layer.py:90(update)
               33718590  383.487    0.000  383.487    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               33718590  333.890    0.000  333.890    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              107803687  330.525    0.000  330.525    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               33718590  319.170    0.000  319.170    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               33718590  315.728    0.000  315.728    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              187325600  191.673    0.000  291.676    0.000 layers.py:65(isDone)
                3744332  103.514    0.000  283.402    0.000 exploration.py:53(softmaxer)
                6573933   23.221    0.000  259.786    0.000 layer.py:40(restart)
               33718590  250.751    0.000  250.751    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              236030184  161.851    0.000  200.028    0.000 tensor.py:906(grad)
                3746510    5.159    0.000  183.450    0.000 loss.py:527(forward)
                2191411   97.097    0.000  180.670    0.000 layers.py:37(reset)
                3746510   14.251    0.000  178.290    0.000 functional.py:2898(mse_loss)
              187325500  135.135    0.000  175.865    0.000 layers.py:229(check)
              339399500  117.502    0.000  159.028    0.000 layer.py:76(add)
              306783540   96.008    0.000  145.413    0.000 levels.py:33(<genexpr>)
                4064566   54.250    0.000  140.728    0.000 random.py:315(sample)
              687966721  138.943    0.000  138.943    0.000 layer.py:85(elements)
                3746510  118.812    0.000  118.812    0.000 {built-in method torch._C._nn.mse_loss}
               18728194   14.353    0.000  112.424    0.000 flatten.py:39(forward)
              177041846   77.800    0.000  112.151    0.000 random.py:250(_randbelow_with_getrandbits)
        613135619/613135617   77.090    0.000  107.584    0.000 {built-in method builtins.len}
                5619765   10.535    0.000  106.692    0.000 tensor.py:525(__rsub__)
                3747071  105.011    0.000  105.011    0.000 {built-in method max}
              129227029  100.633    0.000  100.633    0.000 {built-in method torch._C._get_tracing_state}
               18728194   98.071    0.000   98.071    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              353865239   67.541    0.000   96.928    0.000 enum.py:646(__hash__)
                5619765   94.722    0.000   94.722    0.000 {built-in method rsub}
               78887196   33.690    0.000   94.608    0.000 random.py:285(choice)
                3744332   90.465    0.000   90.465    0.000 {built-in method multinomial}
             1057262062   90.147    0.000   90.147    0.000 layer.py:59(positions)
                1873255    7.143    0.000   88.228    0.000 exploration.py:47(epsilonGreedy)
                3746510   83.040    0.000   83.040    0.000 {built-in method gather}
                3746510   15.237    0.000   82.137    0.000 __init__.py:28(_make_grads)
                7493020   18.044    0.000   79.358    0.000 profiler.py:615(__enter__)
             1164276736   78.917    0.000   78.917    0.000 {method 'append' of 'list' objects}
              120263600   53.467    0.000   77.470    0.000 layer.py:72(remove)
                1873256   66.174    0.000   66.174    0.000 {built-in method nonzero}
                7493020   10.322    0.000   64.723    0.000 profiler.py:607(__init__)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-4>
Subject: Job 9393245: <maze_size_13_low_rest_chance_0> in cluster <dcc> Done

Job <maze_size_13_low_rest_chance_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon Mar  8 02:11:20 2021
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon Mar  8 02:11:21 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Mar  8 02:11:21 2021
Terminated at Mon Mar  8 12:06:45 2021
Results reported at Mon Mar  8 12:06:45 2021

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

    CPU time :                                   35590.64 sec.
    Max Memory :                                 4976 MB
    Average Memory :                             3836.08 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               3216.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35766 sec.
    Turnaround time :                            35725 sec.

The output (if any) is above this job summary.

