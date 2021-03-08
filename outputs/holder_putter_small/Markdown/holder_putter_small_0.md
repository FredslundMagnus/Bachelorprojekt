
# Parameters

    Name :                      holder_putter_small-0
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
    Layer gold :                False
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


      22802291497 function calls (22670304018 primitive calls) in 35666.82 seconds

##    Ordered by: cumulative time
   List reduced from 455 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35705.399 35705.399 {built-in method builtins.exec}
                      1    0.747    0.747 35705.399 35705.399 <string>:1(<module>)
                      1   92.481   92.481 35704.652 35704.652 main.py:10(teleport)
                4713976   16.961    0.000 13291.117    0.003 agent.py:26(learn)
                4713976  312.967    0.000 11383.608    0.002 learner.py:42(Qlearn)
                2356988   72.821    0.000 7934.721    0.003 agent.py:50(_learn)
                2356988    9.591    0.000 6826.459    0.003 game.py:21(step)
                2356988   11.410    0.000 6368.812    0.003 layers.py:212(step)
        148484979/16498511  573.272    0.000 5600.739    0.000 module.py:715(_call_impl)
                2356988 3037.942    0.001 5486.484    0.002 replaybuffer.py:27(teleporter_save_data)
                2356988   63.588    0.000 5329.764    0.002 agent.py:101(_learn)
               11784535   30.488    0.000 5231.435    0.000 network.py:24(forward)
               11784535  137.308    0.000 5130.355    0.000 container.py:115(forward)
                4713976   28.976    0.000 4624.704    0.001 grad_mode.py:23(decorate_context)
                4713976  151.410    0.000 4541.471    0.001 adam.py:55(step)
                2356988 2793.827    0.001 4503.849    0.002 agent.py:77(interveen)
                4713976  846.144    0.000 3733.343    0.001 functional.py:53(adam)
                4713571   96.311    0.000 3427.368    0.001 agent.py:45(__call__)
                2356989  224.419    0.000 3182.142    0.001 layers.py:192(update)
                2356988  165.443    0.000 3160.130    0.001 layers.py:17(step)
              235698800  247.752    0.000 2973.440    0.000 layer.py:66(move)
                4713976   28.208    0.000 2601.743    0.001 tensor.py:181(backward)
                4713976   17.617    0.000 2573.535    0.001 __init__.py:68(backward)
                4713976 2448.122    0.001 2448.122    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
              185130126 1949.504    0.000 1949.504    0.000 {built-in method clone}
                2356988  925.089    0.000 1908.089    0.001 agent.py:59(modify)
               23569070   44.485    0.000 1889.412    0.000 conv.py:422(forward)
                2356988  818.579    0.000 1869.970    0.001 replaybuffer.py:23(sample_data)
               23569070   45.837    0.000 1828.627    0.000 conv.py:414(_conv_forward)
               23569070 1774.564    0.000 1774.564    0.000 {built-in method conv2d}
               30639629   72.193    0.000 1642.795    0.000 linear.py:92(forward)
                3339595   26.288    0.000 1563.748    0.000 layers.py:233(restart)
               30639629  115.773    0.000 1538.872    0.000 functional.py:1669(linear)
              235698800  293.708    0.000 1345.404    0.000 layers.py:229(check)
                3339595    5.429    0.000 1271.534    0.000 levels.py:8(__init__)
                3339595   15.550    0.000 1266.105    0.000 level.py:8(__init__)
                3339595  189.984    0.000 1216.029    0.000 levels.py:11(generate)
              296980542  699.695    0.000 1173.346    0.000 tensor.py:933(grad)
              235698800  235.649    0.000 1136.128    0.000 layers.py:223(isFree)
               30639629 1085.805    0.000 1085.805    0.000 {built-in method addmm}
                2356988   28.352    0.000 1079.603    0.000 agent.py:96(__call__)
               18855499 1062.928    0.000 1062.928    0.000 {built-in method cat}
                7070559   48.736    0.000 1045.789    0.000 agent.py:54(modify_board)
                4713976  103.613    0.000 1033.004    0.000 optimizer.py:167(zero_grad)
              235698800  582.585    0.000  975.954    0.000 layers.py:124(check)
              998175164  763.151    0.000  900.478    0.000 layer.py:63(isFree)
                2356988   38.075    0.000  879.506    0.000 replaybuffer.py:19(stacker)
               84851568  741.077    0.000  741.077    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               42424164   36.862    0.000  714.711    0.000 activation.py:713(forward)
               11784945  339.583    0.000  681.865    0.000 layer.py:90(update)
               42424164   57.646    0.000  677.850    0.000 functional.py:1292(leaky_relu)
                7070559  670.973    0.000  670.973    0.000 {built-in method torch._C._nn.one_hot}
              245127942   79.130    0.000  658.114    0.000 {built-in method builtins.all}
              379474616  207.735    0.000  629.099    0.000 overrides.py:1070(has_torch_function)
               84851568  628.390    0.000  628.390    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               42424164  614.278    0.000  614.278    0.000 {built-in method torch._C._nn.leaky_relu}
                9971843  600.717    0.000  600.717    0.000 {built-in method tensor}
              725459016  175.634    0.000  600.505    0.000 layers.py:197(<genexpr>)
              192200685  551.096    0.000  551.096    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                3339595  242.787    0.000  463.127    0.000 levels.py:76(RFS)
                4713976    5.194    0.000  445.728    0.000 game.py:17(board)
               42425784  440.595    0.000  440.595    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                2356988  253.247    0.000  434.093    0.000 collector.py:37(collect)
               42425784  403.174    0.000  403.174    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              419542198  161.627    0.000  400.794    0.000 {built-in method builtins.any}
              235698900  254.730    0.000  388.026    0.000 layers.py:65(isDone)
               42425784  353.994    0.000  353.994    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                4713571  130.286    0.000  351.570    0.000 exploration.py:53(softmaxer)
             1175450119  239.034    0.000  340.246    0.000 enum.py:646(__hash__)
               42425784  308.472    0.000  308.472    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                6679190   42.226    0.000  281.620    0.000 level.py:41(notUsed)
                9429042   43.852    0.000  266.180    0.000 tensor.py:21(wrapped)
              910121041  261.702    0.000  261.702    0.000 layer.py:85(elements)
               16697975   28.103    0.000  259.160    0.000 layer.py:40(restart)
              444978726  180.096    0.000  244.651    0.000 layer.py:76(add)
               42425784  243.286    0.000  243.286    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                4713976    6.662    0.000  237.433    0.000 loss.py:445(forward)
              799017432  189.375    0.000  235.767    0.000 overrides.py:1083(<genexpr>)
                4713976   25.643    0.000  230.771    0.000 functional.py:2637(mse_loss)
             2401507735  222.319    0.000  222.319    0.000 layer.py:59(positions)
                5696583   75.337    0.000  196.274    0.000 random.py:315(sample)
              260488410  196.026    0.000  196.026    0.000 level.py:32(inverse)
               30639629  193.119    0.000  193.119    0.000 {method 't' of 'torch._C._TensorBase' objects}
              264637396  124.895    0.000  182.898    0.000 layer.py:72(remove)
                3339695   89.169    0.000  177.161    0.000 layers.py:37(reset)
               14141928  172.677    0.000  172.677    0.000 {built-in method sum}
                7070964   33.824    0.000  147.636    0.000 tensor.py:506(__rsub__)
        442651254/442651252   67.244    0.000  136.942    0.000 {built-in method builtins.len}
                4713976  134.600    0.000  134.600    0.000 {built-in method torch._C._nn.mse_loss}
               23569070   18.017    0.000  133.620    0.000 flatten.py:39(forward)
              184700068   90.373    0.000  131.200    0.000 random.py:250(_randbelow_with_getrandbits)
                7070964  129.459    0.000  129.459    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                4714682  124.416    0.000  124.416    0.000 {built-in method max}
               42425874   52.605    0.000  119.326    0.000 tensor.py:596(__hash__)
             1498391767  118.363    0.000  118.363    0.000 {method 'append' of 'list' objects}
               23569070  115.602    0.000  115.602    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                7070964  113.812    0.000  113.812    0.000 {built-in method rsub}
              150842909  113.495    0.000  113.495    0.000 {built-in method torch._C._get_tracing_state}
              200375700   73.884    0.000  110.060    0.000 levels.py:33(<genexpr>)
                4713571  109.579    0.000  109.579    0.000 {built-in method multinomial}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-14>
Subject: Job 9395013: <holder_putter_small_0> in cluster <dcc> Done

Job <holder_putter_small_0> was submitted from host <n-62-27-20> by user <s183905> in cluster <dcc> at Mon Mar  8 13:46:25 2021
Job was executed on host(s) <n-62-20-14>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Mon Mar  8 13:54:41 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Mar  8 13:54:41 2021
Terminated at Mon Mar  8 23:50:02 2021
Results reported at Mon Mar  8 23:50:02 2021

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

    CPU time :                                   35605.74 sec.
    Max Memory :                                 2384 MB
    Average Memory :                             2381.83 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               5808.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35721 sec.
    Turnaround time :                            36217 sec.

The output (if any) is above this job summary.

