
# Parameters

    Name :                      maze_size_15_high_rest_chance-0
    Main :                      teleport
    Hours :                     10.0
    Batch :                     100
    Width :                     15
    Height :                    15
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


      14063328889 function calls (13934103914 primitive calls) in 35668.87 seconds

##    Ordered by: cumulative time
   List reduced from 457 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35713.091 35713.091 {built-in method builtins.exec}
                      1    1.122    1.122 35713.091 35713.091 <string>:1(<module>)
                      1  145.530  145.530 35711.969 35711.969 main.py:10(teleport)
                4616288   19.138    0.000 11285.760    0.002 agent.py:26(learn)
                4616288  300.604    0.000 9449.187    0.002 learner.py:42(Qlearn)
                2308144  238.660    0.000 8650.787    0.004 collector.py:36(collect)
               11540720 7327.371    0.001 8384.415    0.001 {built-in method builtins.sum}
                2308144   98.343    0.000 6749.624    0.003 agent.py:50(_learn)
                2308144   10.694    0.000 5832.437    0.003 game.py:21(step)
                2308144   14.858    0.000 5285.196    0.002 layers.py:212(step)
        145318289/16149717  630.162    0.000 5055.741    0.000 module.py:866(_call_impl)
               11533429   32.983    0.000 4687.098    0.000 network.py:24(forward)
               11533429  151.383    0.000 4574.170    0.000 container.py:117(forward)
                2308144   84.781    0.000 4503.834    0.002 agent.py:101(_learn)
                4616288   43.822    0.000 3588.662    0.001 optimizer.py:84(wrapper)
                4616288   24.141    0.000 3398.814    0.001 grad_mode.py:24(decorate_context)
                4616288  142.584    0.000 3323.119    0.001 adam.py:55(step)
                4608997  143.000    0.000 3177.227    0.001 agent.py:45(__call__)
                4616288  701.675    0.000 3019.360    0.001 _functional.py:53(adam)
                2308145  232.250    0.000 2750.498    0.001 layers.py:192(update)
                2308144 1073.571    0.000 2642.651    0.001 agent.py:77(interveen)
                2308144  188.755    0.000 2496.097    0.001 layers.py:17(step)
                4616288   21.678    0.000 2491.869    0.001 tensor.py:195(backward)
                4616288   21.771    0.000 2469.492    0.001 __init__.py:68(backward)
                4616288 2349.713    0.001 2349.713    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
              230814400  181.581    0.000 2282.797    0.000 layer.py:66(move)
                2308144 1316.676    0.001 2206.111    0.001 replaybuffer.py:23(sample_data)
                2308144 1264.140    0.001 2043.624    0.001 replaybuffer.py:27(teleporter_save_data)
              230814400  104.764    0.000 1785.369    0.000 layers.py:223(isFree)
               23066858   54.000    0.000 1729.880    0.000 conv.py:398(forward)
              327974880 1616.916    0.000 1680.604    0.000 layer.py:63(isFree)
               23066858   34.534    0.000 1650.545    0.000 conv.py:390(_conv_forward)
               23066858 1616.011    0.000 1616.011    0.000 {built-in method conv2d}
                2308144  914.180    0.000 1574.550    0.001 agent.py:59(modify)
                1296602   15.331    0.000 1305.047    0.001 layers.py:233(restart)
               29983999   62.637    0.000 1267.144    0.000 linear.py:93(forward)
               29983999   26.099    0.000 1171.159    0.000 functional.py:1737(linear)
               29983999 1139.336    0.000 1139.336    0.000 {built-in method torch._C._nn.linear}
               13849784   27.015    0.000 1090.391    0.000 tensor.py:575(__iter__)
                1296602    3.603    0.000 1066.680    0.001 levels.py:8(__init__)
                1296602    8.164    0.000 1063.077    0.001 level.py:8(__init__)
               13849784 1041.017    0.000 1041.017    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
                1296602  228.749    0.000 1038.110    0.001 levels.py:11(generate)
                2308144   42.856    0.000 1001.363    0.000 agent.py:96(__call__)
                6917141   45.882    0.000  956.991    0.000 agent.py:54(modify_board)
               18457861  841.844    0.000  841.844    0.000 {built-in method cat}
                9767019  793.142    0.000  793.142    0.000 {built-in method tensor}
                2308144   48.851    0.000  705.862    0.000 replaybuffer.py:19(stacker)
               69361698  690.656    0.000  690.656    0.000 {built-in method clone}
               41517428   37.136    0.000  671.657    0.000 activation.py:713(forward)
              230814500   64.387    0.000  645.482    0.000 {built-in method builtins.all}
                4616288    6.405    0.000  645.461    0.000 game.py:17(board)
                6917141  642.076    0.000  642.076    0.000 {built-in method torch._C._nn.one_hot}
               41517428   35.625    0.000  634.522    0.000 functional.py:1364(leaky_relu)
              692585095  167.769    0.000  607.779    0.000 layers.py:197(<genexpr>)
               41517428  591.251    0.000  591.251    0.000 {built-in method torch._C._nn.leaky_relu}
               83093184  581.835    0.000  581.835    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                1296602  279.138    0.000  539.923    0.000 levels.py:76(RFS)
                4616288   99.494    0.000  534.089    0.000 optimizer.py:189(zero_grad)
               83093184  516.298    0.000  516.298    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                6924435  221.387    0.000  502.138    0.000 layer.py:90(update)
              230814500  285.195    0.000  419.549    0.000 layers.py:65(isDone)
               41546592  346.799    0.000  346.799    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                4608997  117.754    0.000  329.725    0.000 exploration.py:53(softmaxer)
               41546592  305.544    0.000  305.544    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               41546592  281.775    0.000  281.775    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               41546592  274.721    0.000  274.721    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              290826198  204.616    0.000  251.537    0.000 tensor.py:906(grad)
              230814400  181.301    0.000  235.177    0.000 layers.py:229(check)
                4616288   10.019    0.000  223.606    0.000 loss.py:527(forward)
                3889806   21.108    0.000  221.303    0.000 layer.py:40(restart)
              447734727  219.389    0.000  219.389    0.000 layer.py:85(elements)
                4616288   22.393    0.000  213.587    0.000 functional.py:2898(mse_loss)
               41546592  207.015    0.000  207.015    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                3604746   75.145    0.000  194.990    0.000 random.py:315(sample)
               76278839  153.343    0.000  153.343    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                1296702   82.457    0.000  147.548    0.000 layers.py:37(reset)
                4616288  130.537    0.000  130.537    0.000 {built-in method torch._C._nn.mse_loss}
              248947584   83.229    0.000  126.054    0.000 levels.py:33(<genexpr>)
                2308144   12.430    0.000  124.876    0.000 exploration.py:47(epsilonGreedy)
              181617919   83.615    0.000  124.578    0.000 random.py:250(_randbelow_with_getrandbits)
        720219551/720219549   85.918    0.000  121.912    0.000 {built-in method builtins.len}
                4616978  120.102    0.000  120.102    0.000 {built-in method max}
              217144100   85.483    0.000  115.320    0.000 layer.py:76(add)
             1203807447  114.021    0.000  114.021    0.000 layer.py:59(positions)
               23066858   17.897    0.000  113.978    0.000 flatten.py:39(forward)
                6924432   10.790    0.000  112.173    0.000 tensor.py:525(__rsub__)
              357881499   73.769    0.000  105.566    0.000 enum.py:646(__hash__)
                4608997  105.408    0.000  105.408    0.000 {built-in method multinomial}
              159168073  100.104    0.000  100.104    0.000 {built-in method torch._C._get_tracing_state}
                6924432   99.775    0.000   99.775    0.000 {built-in method rsub}
               23066858   96.081    0.000   96.081    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                4616288   23.376    0.000   93.573    0.000 __init__.py:28(_make_grads)
                9232576   21.715    0.000   89.612    0.000 profiler.py:615(__enter__)
                4616288   88.907    0.000   88.907    0.000 {built-in method gather}
                2308145   83.035    0.000   83.035    0.000 {built-in method nonzero}
               63533498   28.833    0.000   81.485    0.000 random.py:285(choice)
              117646479   80.800    0.000   80.807    0.000 module.py:934(__getattr__)
                9232576   13.313    0.000   73.472    0.000 profiler.py:607(__init__)
                2308604   70.497    0.000   70.497    0.000 {method 'tolist' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-10>
Subject: Job 9393250: <maze_size_15_high_rest_chance_0> in cluster <dcc> Done

Job <maze_size_15_high_rest_chance_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon Mar  8 02:11:21 2021
Job was executed on host(s) <n-62-20-10>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon Mar  8 11:54:12 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Mar  8 11:54:12 2021
Terminated at Mon Mar  8 21:51:53 2021
Results reported at Mon Mar  8 21:51:53 2021

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

    CPU time :                                   35623.54 sec.
    Max Memory :                                 5504 MB
    Average Memory :                             4045.62 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               2688.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35735 sec.
    Turnaround time :                            70832 sec.

The output (if any) is above this job summary.

