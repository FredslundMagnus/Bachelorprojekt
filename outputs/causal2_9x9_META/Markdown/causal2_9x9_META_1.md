
# Parameters

    Name :                      causal2_9x9_META-1
    Main :                      metateleport
    Level :                     Levels.Causal2
    Hours :                     11.0
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
    Layer holder :              False
    Layer putter :              False
    Layer rock :                True
    Layer dirt :                True
    Layer diamond1 :            True
    Layer diamond2 :            True
    Layer diamond3 :            True
    Layer diamond4 :            True
    K :                         200000
    Epsilon cap :               0.1
    Softmax cap :               0.02
    Gamma :                     0.98
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.2
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Minutes used :              655 minutes.
    Hours used :                10 hours.

# Profiling


      19490626498 function calls (19370722603 primitive calls) in 39320.15 seconds

##    Ordered by: cumulative time
   List reduced from 470 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 39320.148 39320.148 {built-in method builtins.exec}
                      1    5.026    5.026 39320.148 39320.148 <string>:1(<module>)
                      1   99.196   99.196 39315.121 39315.121 main.py:14(metateleport)
                2606756 6518.865    0.003 11155.134    0.004 replaybuffer.py:27(teleporter_save_data)
                3910134   13.857    0.000 8973.050    0.002 agent.py:27(learn)
                3910134  225.050    0.000 7225.086    0.002 learner.py:42(Qlearn)
                2606756   88.316    0.000 6713.084    0.003 agent.py:51(_learn)
                2606756 4481.217    0.002 6043.024    0.002 agent.py:81(interveen)
                1303378    6.387    0.000 5416.920    0.004 game.py:27(step)
                1303378    8.004    0.000 5137.290    0.004 layers.py:373(step)
                2606756 4171.304    0.002 4996.069    0.002 replaybuffer.py:23(sample_data)
        134238639/14336443  501.293    0.000 4102.583    0.000 module.py:866(_call_impl)
               10426309   28.240    0.000 3829.772    0.000 network.py:24(forward)
              464625760 3817.689    0.000 3817.689    0.000 {built-in method clone}
               10426309  126.063    0.000 3736.109    0.000 container.py:117(forward)
                1303378  105.216    0.000 3671.561    0.003 layers.py:18(step)
              130337800  311.350    0.000 3555.712    0.000 layer.py:74(move)
                5212797  125.938    0.000 3131.048    0.001 agent.py:46(__call__)
                3910134   30.982    0.000 2788.291    0.001 optimizer.py:84(wrapper)
                3910134   15.708    0.000 2650.277    0.001 grad_mode.py:24(decorate_context)
                3910134  110.280    0.000 2598.960    0.001 adam.py:55(step)
                3910134  543.200    0.000 2360.441    0.001 _functional.py:53(adam)
                1303378   36.527    0.000 2237.582    0.002 agent.py:145(_learn)
              130337800  341.747    0.000 2017.536    0.000 layers.py:390(check)
                3910134   14.996    0.000 1874.238    0.000 tensor.py:195(backward)
                3910134   15.477    0.000 1858.711    0.000 __init__.py:68(backward)
                3910134 1769.848    0.000 1769.848    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                1303378  947.726    0.001 1549.705    0.001 agent.py:101(metamodify)
                1303379  138.973    0.000 1446.730    0.001 layers.py:344(update)
               20852618   44.663    0.000 1397.932    0.000 conv.py:398(forward)
               20852618   26.225    0.000 1332.794    0.000 conv.py:390(_conv_forward)
               20852618 1306.569    0.000 1306.569    0.000 {built-in method conv2d}
               28672171   56.625    0.000 1049.945    0.000 linear.py:93(forward)
              130337800  220.321    0.000 1011.959    0.000 layers.py:384(isFree)
               28672171   21.667    0.000  964.909    0.000 functional.py:1737(linear)
                7819553   65.257    0.000  952.134    0.000 agent.py:55(modify_board)
               28672171  938.088    0.000  938.088    0.000 {built-in method torch._C._nn.linear}
              471141935  843.520    0.000  843.520    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               11730411  476.374    0.000  819.519    0.000 layer.py:119(update)
             1153197160  645.126    0.000  791.638    0.000 layer.py:71(isFree)
               23460089  784.564    0.000  784.564    0.000 {built-in method cat}
                2606756   47.085    0.000  642.385    0.000 replaybuffer.py:19(stacker)
                7819553  611.975    0.000  611.975    0.000 {built-in method torch._C._nn.one_hot}
               39098480   30.995    0.000  556.167    0.000 activation.py:713(forward)
                6735812  553.359    0.000  553.359    0.000 {built-in method tensor}
               39098480   29.709    0.000  525.173    0.000 functional.py:1364(leaky_relu)
                1303378   19.904    0.000  507.475    0.000 agent.py:140(__call__)
               39098480  489.067    0.000  489.067    0.000 {built-in method torch._C._nn.leaky_relu}
                3910134    5.227    0.000  484.908    0.000 game.py:23(board)
               72989168  454.128    0.000  454.128    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
             1858868403  318.957    0.000  451.681    0.000 enum.py:646(__hash__)
                3910134   73.897    0.000  415.655    0.000 optimizer.py:189(zero_grad)
               72989168  407.737    0.000  407.737    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              130337800  222.739    0.000  346.024    0.000 layers.py:244(check)
              130337800  211.631    0.000  345.280    0.000 layers.py:230(check)
              130337800  215.146    0.000  341.193    0.000 layers.py:216(check)
              130337900   34.384    0.000  331.742    0.000 {built-in method builtins.all}
                5212797  117.232    0.000  313.352    0.000 exploration.py:53(softmaxer)
              398608655   89.855    0.000  311.788    0.000 layers.py:350(<genexpr>)
              130337800  203.268    0.000  281.910    0.000 layers.py:76(check)
             3117388659  275.356    0.000  275.356    0.000 layer.py:67(positions)
               36494584  273.641    0.000  273.641    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                1303378  143.182    0.000  244.188    0.000 collector.py:54(collect)
               36494584  238.405    0.000  238.405    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              305547070  223.080    0.000  223.080    0.000 layer.py:114(elements)
               36494584  218.370    0.000  218.370    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               36494584  216.627    0.000  216.627    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              130337900  140.811    0.000  209.884    0.000 layers.py:110(isDone)
              255462172  160.854    0.000  198.555    0.000 tensor.py:906(grad)
                2606756   68.443    0.000  177.313    0.000 random.py:315(sample)
              130337800  115.136    0.000  171.341    0.000 layers.py:203(check)
               36494584  163.602    0.000  163.602    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              130337800  103.280    0.000  157.302    0.000 layers.py:63(check)
                3910134    5.181    0.000  156.661    0.000 loss.py:527(forward)
                3910134   13.914    0.000  151.480    0.000 functional.py:2898(mse_loss)
        1531972055/1531972052  115.359    0.000  144.708    0.000 {built-in method builtins.len}
             1858883670  132.727    0.000  132.727    0.000 {built-in method builtins.hash}
               11730402  116.214    0.000  116.214    0.000 {built-in method sum}
             1153197160  113.686    0.000  113.686    0.000 layer.py:175(isBlocking)
                 362670    4.484    0.000  107.002    0.000 layers.py:394(restart)
                5212797   97.124    0.000   97.124    0.000 {built-in method multinomial}
                3910134   93.228    0.000   93.228    0.000 {built-in method torch._C._nn.mse_loss}
              128057788   61.529    0.000   91.454    0.000 layer.py:94(remove)
               20852618   14.299    0.000   91.150    0.000 flatten.py:39(forward)
                6516890    8.640    0.000   89.602    0.000 tensor.py:525(__rsub__)
                3910784   85.061    0.000   85.061    0.000 {built-in method max}
              141207101   61.577    0.000   83.171    0.000 layer.py:98(add)
                6516890   79.492    0.000   79.492    0.000 {built-in method rsub}
               20852618   76.851    0.000   76.851    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              132112651   52.010    0.000   76.702    0.000 random.py:250(_randbelow_with_getrandbits)
                 362670    2.367    0.000   75.021    0.000 level.py:8(__init__)
                2606758   73.892    0.000   73.892    0.000 {built-in method nonzero}
              136846435   72.088    0.000   72.088    0.000 {built-in method torch._C._get_tracing_state}
                3910134   15.942    0.000   70.169    0.000 __init__.py:28(_make_grads)
              109485966   67.074    0.000   67.080    0.000 module.py:934(__getattr__)
                2607796    6.922    0.000   66.614    0.000 tensor.py:575(__iter__)
                3910134   66.526    0.000   66.526    0.000 {built-in method gather}
                 362670    4.615    0.000   66.076    0.000 levels.py:151(generate)
                7820268   14.102    0.000   65.998    0.000 profiler.py:615(__enter__)
                5425156   61.374    0.000   61.374    0.000 {method 'long' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-2>
Subject: Job 9452865: <causal2_9x9_META_1> in cluster <dcc> Done

Job <causal2_9x9_META_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Tue Mar 23 02:18:34 2021
Job was executed on host(s) <n-62-20-2>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Tue Mar 23 02:18:36 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue Mar 23 02:18:36 2021
Terminated at Tue Mar 23 13:14:07 2021
Results reported at Tue Mar 23 13:14:07 2021

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

    CPU time :                                   39215.62 sec.
    Max Memory :                                 6078 MB
    Average Memory :                             4966.67 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               2114.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   39446 sec.
    Turnaround time :                            39333 sec.

The output (if any) is above this job summary.

