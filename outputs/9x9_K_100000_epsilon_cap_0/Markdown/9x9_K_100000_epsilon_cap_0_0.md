
# Parameters

    Name :                      9x9_K_100000_epsilon_cap_0-0
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
    K :                         100000.0
    Epsilon cap :               0.0
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


      24676744139 function calls (24535938516 primitive calls) in 35685.27 seconds

##    Ordered by: cumulative time
   List reduced from 463 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35705.542 35705.542 {built-in method builtins.exec}
                      1    0.742    0.742 35705.542 35705.542 <string>:1(<module>)
                      1  110.574  110.574 35704.800 35704.800 main.py:10(teleport)
                5028866   18.488    0.000 14450.842    0.003 agent.py:26(learn)
                5028866  341.751    0.000 12363.396    0.002 learner.py:42(Qlearn)
                2514433   86.163    0.000 8636.188    0.003 agent.py:50(_learn)
                2514433   10.178    0.000 7608.617    0.003 game.py:21(step)
                2514433   11.616    0.000 7044.636    0.003 layers.py:212(step)
        158405340/17600728  633.665    0.000 6104.070    0.000 module.py:715(_call_impl)
                2514433   73.297    0.000 5786.311    0.002 agent.py:101(_learn)
               12571862   31.738    0.000 5697.042    0.000 network.py:24(forward)
               12571862  148.363    0.000 5586.788    0.000 container.py:115(forward)
                5028866   31.206    0.000 5001.608    0.001 grad_mode.py:23(decorate_context)
                5028866  166.085    0.000 4909.842    0.001 adam.py:55(step)
                2514433  187.719    0.000 4391.069    0.002 layers.py:17(step)
              251443300  216.097    0.000 4180.625    0.000 layer.py:66(move)
                5028866  926.703    0.000 4034.960    0.001 functional.py:53(adam)
                2514433 1941.077    0.001 3805.789    0.002 agent.py:77(interveen)
                2514433 2105.369    0.001 3802.715    0.002 replaybuffer.py:27(teleporter_save_data)
                5028563  112.418    0.000 3734.840    0.001 agent.py:45(__call__)
                5028866   30.295    0.000 2830.669    0.001 tensor.py:181(backward)
                5028866   18.259    0.000 2800.375    0.001 __init__.py:68(backward)
              251443300  555.530    0.000 2777.000    0.000 layers.py:229(check)
                5028866 2663.875    0.001 2663.875    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2514434  238.421    0.000 2624.301    0.001 layers.py:192(update)
               25143724   45.474    0.000 2052.604    0.000 conv.py:422(forward)
                2514433  884.274    0.000 2045.066    0.001 replaybuffer.py:23(sample_data)
                2514433  936.009    0.000 1990.281    0.001 agent.py:59(modify)
               25143724   55.682    0.000 1983.318    0.000 conv.py:414(_conv_forward)
               25143724 1917.879    0.000 1917.879    0.000 {built-in method conv2d}
               32686720   74.597    0.000 1784.496    0.000 linear.py:92(forward)
               32686720  129.618    0.000 1676.455    0.000 functional.py:1669(linear)
              125046141 1374.778    0.000 1374.778    0.000 {built-in method clone}
              316818612  768.332    0.000 1276.397    0.000 tensor.py:933(grad)
               32686720 1178.197    0.000 1178.197    0.000 {built-in method addmm}
               20115161 1168.551    0.000 1168.551    0.000 {built-in method cat}
                5028866  111.581    0.000 1135.795    0.000 optimizer.py:167(zero_grad)
                2514433   31.108    0.000 1128.089    0.000 agent.py:96(__call__)
                7542996   50.305    0.000 1117.756    0.000 agent.py:54(modify_board)
              251443300  234.141    0.000 1064.621    0.000 layers.py:223(isFree)
                2514433   43.025    0.000  975.303    0.000 replaybuffer.py:19(stacker)
              251443300  595.566    0.000  968.744    0.000 layers.py:124(check)
                1272178   13.132    0.000  862.670    0.001 layers.py:233(restart)
              888197056  688.972    0.000  830.480    0.000 layer.py:63(isFree)
               90519588  788.538    0.000  788.538    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               45258582   39.414    0.000  784.693    0.000 activation.py:713(forward)
               20115472  265.913    0.000  758.731    0.000 layer.py:90(update)
               10116722  755.430    0.000  755.430    0.000 {built-in method tensor}
               45258582   63.335    0.000  745.279    0.000 functional.py:1292(leaky_relu)
                1272178    2.897    0.000  733.393    0.001 levels.py:8(__init__)
                1272178   10.216    0.000  730.496    0.001 level.py:8(__init__)
                7542996  717.671    0.000  717.671    0.000 {built-in method torch._C._nn.one_hot}
              261503120   82.287    0.000  706.343    0.000 {built-in method builtins.all}
                1734550  108.947    0.000  701.226    0.000 levels.py:11(generate)
               90519588  679.669    0.000  679.669    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               45258582  675.333    0.000  675.333    0.000 {built-in method torch._C._nn.leaky_relu}
              404824434  221.905    0.000  675.161    0.000 overrides.py:1070(has_torch_function)
              779809590  194.408    0.000  647.818    0.000 layers.py:197(<genexpr>)
                5028866    5.942    0.000  610.981    0.000 game.py:17(board)
             2139873428  418.275    0.000  581.589    0.000 enum.py:646(__hash__)
               45259794  472.389    0.000  472.389    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                2514433  273.573    0.000  469.028    0.000 collector.py:37(collect)
              251443300  304.580    0.000  468.606    0.000 layers.py:95(check)
               45259794  437.527    0.000  437.527    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              447568887  175.099    0.000  432.648    0.000 {built-in method builtins.any}
              251443400  282.874    0.000  425.461    0.000 layers.py:65(isDone)
              132589137  395.631    0.000  395.631    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               45259794  386.306    0.000  386.306    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                5028563  142.195    0.000  383.124    0.000 exploration.py:53(softmaxer)
              482388358  358.738    0.000  358.738    0.000 layer.py:85(elements)
              251443300  240.817    0.000  353.887    0.000 layers.py:50(check)
              251443300  227.803    0.000  346.887    0.000 layers.py:77(check)
             3732879884  346.630    0.000  346.630    0.000 layer.py:59(positions)
               45259794  330.670    0.000  330.670    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               10059720   46.904    0.000  283.929    0.000 tensor.py:21(wrapped)
               45259794  273.836    0.000  273.836    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                5028866    7.495    0.000  260.302    0.000 loss.py:445(forward)
              852394806  204.406    0.000  254.193    0.000 overrides.py:1083(<genexpr>)
                5028866   28.408    0.000  252.807    0.000 functional.py:2637(mse_loss)
                1734550  126.816    0.000  240.682    0.000 levels.py:76(RFS)
                7255711   82.783    0.000  217.640    0.000 random.py:315(sample)
               32686720  212.669    0.000  212.669    0.000 {method 't' of 'torch._C._TensorBase' objects}
               15086598  186.562    0.000  186.562    0.000 {built-in method sum}
                3816534   21.929    0.000  168.523    0.000 level.py:41(notUsed)
             2139891899  163.317    0.000  163.317    0.000 {built-in method builtins.hash}
                7543299   35.686    0.000  158.126    0.000 tensor.py:506(__rsub__)
                5028866  147.752    0.000  147.752    0.000 {built-in method torch._C._nn.mse_loss}
        436262087/436262085   70.009    0.000  144.930    0.000 {built-in method builtins.len}
               25143724   20.212    0.000  143.966    0.000 flatten.py:39(forward)
                7543299  138.085    0.000  138.085    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                5029619  134.117    0.000  134.117    0.000 {built-in method max}
              221454214   97.165    0.000  130.717    0.000 layer.py:76(add)
               45259884   57.121    0.000  128.231    0.000 tensor.py:596(__hash__)
              160920777  124.766    0.000  124.766    0.000 {built-in method torch._C._get_tracing_state}
               25143724  123.753    0.000  123.753    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                7543299  122.440    0.000  122.440    0.000 {built-in method rsub}
              127097622  119.481    0.000  119.481    0.000 level.py:32(inverse)
                5028563  117.530    0.000  117.530    0.000 {built-in method multinomial}
                5028866   21.281    0.000  113.523    0.000 __init__.py:28(_make_grads)
              167340598   77.656    0.000  113.506    0.000 random.py:250(_randbelow_with_getrandbits)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-15>
Subject: Job 9395475: <9x9_K_100000_epsilon_cap_0_0> in cluster <dcc> Done

Job <9x9_K_100000_epsilon_cap_0_0> was submitted from host <n-62-27-20> by user <s183905> in cluster <dcc> at Tue Mar  9 00:59:03 2021
Job was executed on host(s) <n-62-20-15>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Tue Mar  9 01:04:46 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue Mar  9 01:04:46 2021
Terminated at Tue Mar  9 11:00:07 2021
Results reported at Tue Mar  9 11:00:07 2021

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

    CPU time :                                   35615.02 sec.
    Max Memory :                                 2386 MB
    Average Memory :                             2382.42 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               5806.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35723 sec.
    Turnaround time :                            36064 sec.

The output (if any) is above this job summary.

