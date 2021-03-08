
# Parameters

    Name :                      holder_putter_gold_small-0
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
    Layer keys :                False
    Layer door :                False
    Layer holder :              True
    Layer putter :              True
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


      25087782757 function calls (24942534714 primitive calls) in 35689.53 seconds

##    Ordered by: cumulative time
   List reduced from 457 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35709.505 35709.505 {built-in method builtins.exec}
                      1    0.727    0.727 35709.505 35709.505 <string>:1(<module>)
                      1  102.383  102.383 35708.778 35708.778 main.py:10(teleport)
                5187586   17.241    0.000 13543.520    0.003 agent.py:26(learn)
                5187586  329.673    0.000 11560.822    0.002 learner.py:42(Qlearn)
                2593793   78.752    0.000 8095.395    0.003 agent.py:50(_learn)
                2593793    9.024    0.000 6758.714    0.003 game.py:21(step)
                2593793   10.928    0.000 6250.565    0.002 layers.py:212(step)
        163403135/18156103  586.251    0.000 5783.249    0.000 module.py:715(_call_impl)
                2593793   69.934    0.000 5421.375    0.002 agent.py:101(_learn)
               12968517   31.541    0.000 5401.684    0.000 network.py:24(forward)
               12968517  141.224    0.000 5295.094    0.000 container.py:115(forward)
                2593793 2923.210    0.001 5216.222    0.002 replaybuffer.py:27(teleporter_save_data)
                5187586   30.132    0.000 4631.183    0.001 grad_mode.py:23(decorate_context)
                5187586  155.309    0.000 4545.707    0.001 adam.py:55(step)
                2593793 2625.477    0.001 4395.827    0.002 agent.py:77(interveen)
                5187586  829.099    0.000 3733.397    0.001 functional.py:53(adam)
                2593793  167.058    0.000 3671.372    0.001 layers.py:17(step)
                5187138  104.681    0.000 3550.960    0.001 agent.py:45(__call__)
              259379300  245.169    0.000 3482.249    0.000 layer.py:66(move)
                5187586   29.136    0.000 2677.057    0.001 tensor.py:181(backward)
                5187586   16.624    0.000 2647.921    0.001 __init__.py:68(backward)
                2593794  220.593    0.000 2551.749    0.001 layers.py:192(update)
                5187586 2519.980    0.000 2519.980    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2593793  868.888    0.000 1968.413    0.001 replaybuffer.py:23(sample_data)
               25937034   43.659    0.000 1952.238    0.000 conv.py:422(forward)
                2593793  907.849    0.000 1911.947    0.001 agent.py:59(modify)
               25937034   47.178    0.000 1891.869    0.000 conv.py:414(_conv_forward)
               25937034 1836.186    0.000 1836.186    0.000 {built-in method conv2d}
              187010746 1829.693    0.000 1829.693    0.000 {built-in method clone}
              259379300  368.599    0.000 1756.093    0.000 layers.py:229(check)
               33717965   75.125    0.000 1710.370    0.000 linear.py:92(forward)
               33717965  123.947    0.000 1601.892    0.000 functional.py:1669(linear)
              259379300  267.771    0.000 1232.193    0.000 layers.py:223(isFree)
              326817972  705.540    0.000 1178.121    0.000 tensor.py:933(grad)
               33717965 1130.291    0.000 1130.291    0.000 {built-in method addmm}
                2593793   30.572    0.000 1117.619    0.000 agent.py:96(__call__)
               20749896 1111.339    0.000 1111.339    0.000 {built-in method cat}
                7780931   47.588    0.000 1079.537    0.000 agent.py:54(modify_board)
                5187586   97.270    0.000 1033.637    0.000 optimizer.py:167(zero_grad)
             1319527200  799.606    0.000  964.422    0.000 layer.py:63(isFree)
              259379300  572.550    0.000  950.046    0.000 layers.py:124(check)
                2593793   41.229    0.000  927.384    0.000 replaybuffer.py:19(stacker)
                1923068   14.859    0.000  926.074    0.000 layers.py:233(restart)
                1923068    3.300    0.000  764.567    0.000 levels.py:8(__init__)
                1923068    8.910    0.000  761.267    0.000 level.py:8(__init__)
               93376548  742.885    0.000  742.885    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               46686482   39.552    0.000  740.091    0.000 activation.py:713(forward)
                1923068  105.785    0.000  733.380    0.000 levels.py:11(generate)
               46686482   61.786    0.000  700.539    0.000 functional.py:1292(leaky_relu)
                7780931  699.198    0.000  699.198    0.000 {built-in method torch._C._nn.one_hot}
               15562764  309.518    0.000  696.733    0.000 layer.py:90(update)
               10966816  689.436    0.000  689.436    0.000 {built-in method tensor}
              269755944   74.839    0.000  653.268    0.000 {built-in method builtins.all}
               46686482  632.987    0.000  632.987    0.000 {built-in method torch._C._nn.leaky_relu}
               93376548  632.869    0.000  632.869    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              417600327  212.042    0.000  626.674    0.000 overrides.py:1070(has_torch_function)
              791801044  177.040    0.000  600.645    0.000 layers.py:197(<genexpr>)
                5187586    4.979    0.000  530.093    0.000 game.py:17(board)
              194791677  519.390    0.000  519.390    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               46688274  446.436    0.000  446.436    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                2593793  253.709    0.000  436.733    0.000 collector.py:37(collect)
               46688274  396.254    0.000  396.254    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              259379400  261.108    0.000  394.616    0.000 layers.py:65(isDone)
              461693465  160.349    0.000  393.265    0.000 {built-in method builtins.any}
             1454142754  266.715    0.000  381.130    0.000 enum.py:646(__hash__)
                5187138  134.904    0.000  361.661    0.000 exploration.py:53(softmaxer)
               46688274  360.732    0.000  360.732    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              259379300  239.783    0.000  360.709    0.000 layers.py:50(check)
               46688274  312.787    0.000  312.787    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              824671728  290.868    0.000  290.868    0.000 layer.py:85(elements)
               10376544   45.036    0.000  268.635    0.000 tensor.py:21(wrapped)
             3151230431  260.048    0.000  260.048    0.000 layer.py:59(positions)
               46688274  247.229    0.000  247.229    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                5187586    6.944    0.000  245.383    0.000 loss.py:445(forward)
                5187586   27.296    0.000  238.440    0.000 functional.py:2637(mse_loss)
                1923068  125.783    0.000  238.400    0.000 levels.py:76(RFS)
              879294645  187.304    0.000  229.699    0.000 overrides.py:1083(<genexpr>)
                5769204   30.937    0.000  220.009    0.000 level.py:41(notUsed)
              397767475  152.602    0.000  205.474    0.000 layer.py:76(add)
               33717965  201.914    0.000  201.914    0.000 {method 't' of 'torch._C._TensorBase' objects}
                6439929   76.006    0.000  197.433    0.000 random.py:315(sample)
              293324888  127.999    0.000  186.022    0.000 layer.py:72(remove)
               15562758  177.334    0.000  177.334    0.000 {built-in method sum}
                7781379   35.399    0.000  152.781    0.000 tensor.py:506(__rsub__)
              196152936  147.872    0.000  147.872    0.000 level.py:32(inverse)
               11538408   16.176    0.000  142.620    0.000 layer.py:40(restart)
               25937034   18.763    0.000  137.363    0.000 flatten.py:39(forward)
                5187586  137.182    0.000  137.182    0.000 {built-in method torch._C._nn.mse_loss}
                7781379  132.455    0.000  132.455    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
        454177075/454177073   62.758    0.000  130.263    0.000 {built-in method builtins.len}
                5188363  127.236    0.000  127.236    0.000 {built-in method max}
             1319527200  127.206    0.000  127.206    0.000 layer.py:125(isBlocking)
               25937034  118.601    0.000  118.601    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               46688364   52.226    0.000  118.492    0.000 tensor.py:596(__hash__)
                7781379  117.381    0.000  117.381    0.000 {built-in method rsub}
             1454161801  114.418    0.000  114.418    0.000 {built-in method builtins.hash}
              165997964  112.481    0.000  112.481    0.000 {built-in method torch._C._get_tracing_state}
                5187138  110.804    0.000  110.804    0.000 {built-in method multinomial}
                5187586   19.883    0.000  107.148    0.000 __init__.py:28(_make_grads)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-3>
Subject: Job 9395015: <holder_putter_gold_small_0> in cluster <dcc> Done

Job <holder_putter_gold_small_0> was submitted from host <n-62-27-20> by user <s183905> in cluster <dcc> at Mon Mar  8 13:46:25 2021
Job was executed on host(s) <n-62-20-3>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Mon Mar  8 14:40:30 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Mar  8 14:40:30 2021
Terminated at Tue Mar  9 00:36:01 2021
Results reported at Tue Mar  9 00:36:01 2021

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

    CPU time :                                   35620.36 sec.
    Max Memory :                                 2390 MB
    Average Memory :                             2379.40 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               5802.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35733 sec.
    Turnaround time :                            38976 sec.

The output (if any) is above this job summary.

