
# Parameters

    Name :                      9x9_gamme0.99-0
    Main :                      teleport
    Hours :                     10.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Network1 :                  Networks.Teleporter
    Network2 :                  Networks.Mini
    Learner1 :                  Learners.Qlearn
    Learner2 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Exploration2 :              Explorations.epsilonGreedy
    Layer blocks :              True
    Layer goal :                True
    Layer gold :                True
    Layer keys :                True
    Layer door :                True
    Layer holder :              True
    Layer putter :              True
    K :                         200000
    Epsilon cap :               0.2
    Softmax cap :               0.03
    Gamma :                     0.99
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


      26323064419 function calls (26173338240 primitive calls) in 35688.56 seconds

##    Ordered by: cumulative time
   List reduced from 474 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35709.832 35709.832 {built-in method builtins.exec}
                      1    0.820    0.820 35709.832 35709.832 <string>:1(<module>)
                      1  148.832  148.832 35709.012 35709.012 main.py:10(teleport)
                5347900   23.452    0.000 13028.270    0.002 agent.py:26(learn)
                5347900  346.733    0.000 10937.460    0.002 learner.py:42(Qlearn)
                2673950   12.695    0.000 9773.010    0.004 game.py:21(step)
                2673950   16.305    0.000 9168.648    0.003 layers.py:212(step)
                2673950  101.254    0.000 7755.803    0.003 agent.py:50(_learn)
                2673950  233.154    0.000 5891.643    0.002 layers.py:17(step)
        168441482/18716314  722.235    0.000 5724.443    0.000 module.py:866(_call_impl)
              267395000  276.576    0.000 5634.280    0.000 layer.py:66(move)
               13368414   38.650    0.000 5292.501    0.000 network.py:24(forward)
                2673950   85.405    0.000 5237.979    0.002 agent.py:101(_learn)
               13368414  177.492    0.000 5158.939    0.000 container.py:117(forward)
                5347900   51.651    0.000 4182.697    0.001 optimizer.py:84(wrapper)
                5347900   27.196    0.000 3963.288    0.001 grad_mode.py:24(decorate_context)
                5347900  170.782    0.000 3878.139    0.001 adam.py:55(step)
                5346564  151.897    0.000 3587.393    0.001 agent.py:45(__call__)
                5347900  814.962    0.000 3523.891    0.001 _functional.py:53(adam)
                2673950 1669.792    0.001 3402.009    0.001 agent.py:77(interveen)
                2673951  281.121    0.000 3234.738    0.001 layers.py:192(update)
                2673950 1941.631    0.001 3230.581    0.001 replaybuffer.py:27(teleporter_save_data)
              267395000  600.476    0.000 3054.826    0.000 layers.py:229(check)
                5347900   23.591    0.000 2892.880    0.001 tensor.py:195(backward)
                5347900   23.852    0.000 2868.606    0.001 __init__.py:68(backward)
                5347900 2727.849    0.001 2727.849    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2673950 1506.198    0.001 2410.258    0.001 replaybuffer.py:23(sample_data)
              267395000  359.708    0.000 2027.343    0.000 layers.py:223(isFree)
               26736828   62.257    0.000 1932.692    0.000 conv.py:398(forward)
               26736828   40.269    0.000 1841.120    0.000 conv.py:390(_conv_forward)
                2673950 1067.240    0.000 1822.519    0.001 agent.py:59(modify)
               26736828 1800.852    0.000 1800.852    0.000 {built-in method conv2d}
             1579215284 1437.041    0.000 1667.635    0.000 layer.py:63(isFree)
               34757342   74.342    0.000 1433.270    0.000 linear.py:93(forward)
               34757342   29.891    0.000 1321.540    0.000 functional.py:1737(linear)
               34757342 1284.386    0.000 1284.386    0.000 {built-in method torch._C._nn.linear}
               21391608  442.951    0.000 1174.747    0.000 layer.py:90(update)
                2673950   44.164    0.000 1132.838    0.000 agent.py:96(__call__)
              113609955 1109.106    0.000 1109.106    0.000 {built-in method clone}
                8020514   52.583    0.000 1100.555    0.000 agent.py:54(modify_board)
              267395000  679.285    0.000 1083.588    0.000 layers.py:124(check)
                1351616   17.163    0.000  946.242    0.001 layers.py:233(restart)
               11304264  858.005    0.000  858.005    0.000 {built-in method tensor}
               21390264  855.171    0.000  855.171    0.000 {built-in method cat}
                1351616    4.030    0.000  801.613    0.001 levels.py:8(__init__)
                1351616   13.444    0.000  797.583    0.001 level.py:8(__init__)
                1843026  120.081    0.000  761.702    0.000 levels.py:11(generate)
               48125756   42.892    0.000  759.513    0.000 activation.py:713(forward)
              267395100   77.955    0.000  755.583    0.000 {built-in method builtins.all}
                8020514  732.726    0.000  732.726    0.000 {built-in method torch._C._nn.one_hot}
               48125756   41.198    0.000  716.621    0.000 functional.py:1364(leaky_relu)
              808565739  202.270    0.000  709.325    0.000 layers.py:197(<genexpr>)
                5347900    7.534    0.000  691.653    0.000 game.py:17(board)
               96262200  684.368    0.000  684.368    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                2673950   45.906    0.000  684.053    0.000 replaybuffer.py:19(stacker)
               48125756  667.377    0.000  667.377    0.000 {built-in method torch._C._nn.leaky_relu}
             2274588466  442.739    0.000  622.136    0.000 enum.py:646(__hash__)
                5347900  109.499    0.000  605.383    0.000 optimizer.py:189(zero_grad)
               96262200  603.285    0.000  603.285    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              704636643  579.562    0.000  579.562    0.000 layer.py:85(elements)
              267395000  325.644    0.000  505.904    0.000 layers.py:95(check)
              267395100  328.087    0.000  481.087    0.000 layers.py:65(isDone)
                2673950  243.514    0.000  415.671    0.000 collector.py:37(collect)
              267395000  280.790    0.000  401.107    0.000 layers.py:50(check)
               48131100  393.467    0.000  393.467    0.000 {method 'add' of 'torch._C._TensorBase' objects}
             4108735006  378.914    0.000  378.914    0.000 layer.py:59(positions)
              267395000  248.925    0.000  375.354    0.000 layers.py:77(check)
                5346564  132.092    0.000  372.385    0.000 exploration.py:53(softmaxer)
               48131100  355.545    0.000  355.545    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               48131100  330.819    0.000  330.819    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               48131100  328.745    0.000  328.745    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              336917754  223.118    0.000  280.744    0.000 tensor.py:906(grad)
                5347900    9.301    0.000  262.490    0.000 loss.py:527(forward)
                1843026  137.063    0.000  258.132    0.000 levels.py:76(RFS)
                7711618   97.195    0.000  256.180    0.000 random.py:315(sample)
                5347900   27.480    0.000  253.189    0.000 functional.py:2898(mse_loss)
              121630469  245.661    0.000  245.661    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               48131100  239.194    0.000  239.194    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              331564601  153.461    0.000  210.633    0.000 layer.py:76(add)
              253922367  138.131    0.000  202.221    0.000 layer.py:72(remove)
               16043700  183.312    0.000  183.312    0.000 {built-in method sum}
                4054848   25.175    0.000  181.614    0.000 level.py:41(notUsed)
             2274608089  179.401    0.000  179.401    0.000 {built-in method builtins.hash}
                5347900  153.537    0.000  153.537    0.000 {built-in method torch._C._nn.mse_loss}
             1387940062  145.343    0.000  145.343    0.000 layer.py:125(isBlocking)
                2673950   13.635    0.000  144.664    0.000 exploration.py:47(epsilonGreedy)
                5348701  137.690    0.000  137.690    0.000 {built-in method max}
        800759645/800759643   99.210    0.000  137.177    0.000 {built-in method builtins.len}
                8021850   17.391    0.000  136.495    0.000 tensor.py:525(__rsub__)
              135037078  127.100    0.000  127.100    0.000 level.py:32(inverse)
               26736828   18.485    0.000  126.561    0.000 flatten.py:39(forward)
               10812928   18.015    0.000  123.508    0.000 layer.py:40(restart)
              177918229   84.121    0.000  123.349    0.000 random.py:250(_randbelow_with_getrandbits)
                5346564  122.270    0.000  122.270    0.000 {built-in method multinomial}
                8021850  117.267    0.000  117.267    0.000 {built-in method rsub}
                5347900   25.896    0.000  111.568    0.000 __init__.py:28(_make_grads)
             1240272951  110.284    0.000  110.284    0.000 {method 'append' of 'list' objects}
               26736828  108.076    0.000  108.076    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                5347900  107.619    0.000  107.619    0.000 {built-in method gather}
               10695800   23.116    0.000  103.536    0.000 profiler.py:615(__enter__)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-12>
Subject: Job 9395483: <9x9_gamme0.99_0> in cluster <dcc> Done

Job <9x9_gamme0.99_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Tue Mar  9 01:14:59 2021
Job was executed on host(s) <n-62-20-12>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Tue Mar  9 01:25:16 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue Mar  9 01:25:16 2021
Terminated at Tue Mar  9 11:20:57 2021
Results reported at Tue Mar  9 11:20:57 2021

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

    CPU time :                                   35621.18 sec.
    Max Memory :                                 6084 MB
    Average Memory :                             4278.28 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               2108.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35730 sec.
    Turnaround time :                            36358 sec.

The output (if any) is above this job summary.

