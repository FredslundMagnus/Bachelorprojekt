
# Parameters

    Name :                      test_run_9-0
    Network1 :                  Networks.Small
    Network2 :                  Networks.Mini
    Learner1 :                  Learners.DoubleQlearn
    Learner2 :                  Learners.Qlearn
    Exploration1 :              Explorations.epsilonGreedy
    Exploration2 :              Explorations.epsilonGreedy
    Gamma :                     1.0
    K :                         500000
    Batch :                     100
    Hours :                     0.3
    Width :                     11
    Height :                    11
    Update :                    1000
    Reset chance :              0.002
    Main :                      simple
    Minutes used :              13 minutes.
    Hours used :                0 hours.

# Profiling


      591750057 function calls (589026966 primitive calls) in 791.07 seconds

##    Ordered by: cumulative time
   List reduced from 381 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000  791.815  791.815 {built-in method builtins.exec}
                      1    0.001    0.001  791.815  791.815 <string>:1(<module>)
                      1    1.786    1.786  791.814  791.814 main.py:26(simple)
                 136057    0.209    0.000  291.744    0.002 agent.py:25(learn)
                 136057    2.761    0.000  290.774    0.002 agent.py:68(_learn)
                 136057    8.746    0.000  288.012    0.002 learner.py:42(Qlearn)
                 136057    5.686    0.000  211.911    0.002 collector.py:31(collect)
                 272114  177.843    0.001  205.058    0.001 {built-in method builtins.sum}
                 136057    0.427    0.000  196.697    0.001 game.py:19(step)
                 136057    0.235    0.000  173.503    0.001 layers.py:212(step)
         3129311/408171   11.721    0.000  114.405    0.000 module.py:715(_call_impl)
                 136057    0.797    0.000  113.444    0.001 grad_mode.py:23(decorate_context)
                 136057    3.783    0.000  111.143    0.001 adam.py:55(step)
                 272114    0.601    0.000  104.652    0.000 network.py:24(forward)
                 272114    2.800    0.000  102.517    0.000 container.py:115(forward)
                 136057   19.774    0.000   91.270    0.001 functional.py:53(adam)
                 136058   11.213    0.000   87.141    0.001 layers.py:192(update)
                 136057    8.963    0.000   86.182    0.001 layers.py:17(step)
               13605700    9.696    0.000   75.967    0.000 layer.py:65(move)
                 136057    0.888    0.000   67.605    0.000 tensor.py:181(backward)
                 136057    0.492    0.000   66.717    0.000 __init__.py:68(backward)
                 136057    1.534    0.000   66.598    0.000 agent.py:63(__call__)
                 136057   63.274    0.000   63.274    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
               13605700    7.031    0.000   46.022    0.000 layers.py:222(isFree)
                 544228    0.948    0.000   41.581    0.000 conv.py:422(forward)
                 544228    1.096    0.000   40.286    0.000 conv.py:414(_conv_forward)
                 544228   39.003    0.000   39.003    0.000 {built-in method conv2d}
               26410290   34.601    0.000   38.991    0.000 layer.py:62(isFree)
                 664164   34.963    0.000   34.963    0.000 {built-in method tensor}
               13605800    3.496    0.000   33.341    0.000 {built-in method builtins.all}
               40835079    9.066    0.000   31.331    0.000 layers.py:197(<genexpr>)
                 544228    1.235    0.000   29.910    0.000 linear.py:92(forward)
                7619216   17.317    0.000   28.803    0.000 tensor.py:933(grad)
                 544228    2.184    0.000   28.137    0.000 functional.py:1669(linear)
                 272114    0.752    0.000   27.215    0.000 tensor.py:576(__iter__)
                 272114   25.923    0.000   25.923    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
                 136057    2.447    0.000   25.231    0.000 optimizer.py:167(zero_grad)
                 272114    0.264    0.000   23.297    0.000 game.py:15(board)
                  44657    0.286    0.000   21.990    0.000 layers.py:232(restart)
               13605800   14.106    0.000   21.213    0.000 layers.py:65(isDone)
                 544228   19.850    0.000   19.850    0.000 {built-in method addmm}
                2176912   18.539    0.000   18.539    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                  44657    0.080    0.000   17.574    0.000 levels.py:8(__init__)
                  44657    0.172    0.000   17.493    0.000 level.py:8(__init__)
                 408174    7.768    0.000   17.097    0.000 layer.py:89(update)
                  44657    3.430    0.000   16.889    0.000 levels.py:11(generate)
                2176912   15.321    0.000   15.321    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                9251940    4.639    0.000   13.867    0.000 overrides.py:1070(has_torch_function)
                 816342    0.774    0.000   13.551    0.000 activation.py:713(forward)
                 816342    1.227    0.000   12.777    0.000 functional.py:1292(leaky_relu)
               13605700    9.918    0.000   12.727    0.000 layers.py:228(check)
                 136057    0.682    0.000   11.929    0.000 exploration.py:45(epsilonGreedy)
                      1    0.000    0.000   11.691   11.691 agent.py:60(__init__)
                      1    0.000    0.000   11.691   11.691 agent.py:14(__init__)
                      1    0.000    0.000   11.691   11.691 network.py:33(__init__)
                      3    0.000    0.000   11.590    3.863 module.py:529(to)
                   33/3    0.000    0.000   11.590    3.863 module.py:357(_apply)
                     24    0.000    0.000   11.589    0.483 module.py:607(convert)
                     24   11.588    0.483   11.589    0.483 {method 'to' of 'torch._C._TensorBase' objects}
                 816342   11.437    0.000   11.437    0.000 {built-in method torch._C._nn.leaky_relu}
                1088456   11.305    0.000   11.305    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                1088456    9.706    0.000    9.706    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                  44657    4.636    0.000    8.930    0.000 levels.py:78(RFS)
                1088456    8.796    0.000    8.796    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               10068283    3.516    0.000    8.782    0.000 {built-in method builtins.any}
                1088456    7.536    0.000    7.536    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               20196503    6.692    0.000    6.692    0.000 layer.py:84(elements)
                 136057    0.188    0.000    6.587    0.000 loss.py:445(forward)
                 136057    0.719    0.000    6.398    0.000 functional.py:2637(mse_loss)
               74413316    6.209    0.000    6.209    0.000 layer.py:58(positions)
                1088456    6.009    0.000    6.009    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                 117760    2.425    0.000    5.702    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               19048108    4.188    0.000    5.180    0.000 overrides.py:1083(<genexpr>)
                9710913    3.634    0.000    4.901    0.000 layer.py:75(add)
               16151252    3.075    0.000    4.503    0.000 enum.py:646(__hash__)
                 133971    0.375    0.000    4.092    0.000 layer.py:39(restart)
                6402295    2.780    0.000    4.086    0.000 layer.py:71(remove)
                 136057    3.719    0.000    3.719    0.000 {built-in method torch._C._nn.mse_loss}
                 544228    3.521    0.000    3.521    0.000 {method 't' of 'torch._C._TensorBase' objects}
                 136070    3.410    0.000    3.410    0.000 {built-in method max}
                 136057    3.340    0.000    3.340    0.000 {method 'tolist' of 'torch._C._TensorBase' objects}
                 235520    0.240    0.000    3.278    0.000 <__array_function__ internals>:2(prod)
                 235520    0.204    0.000    2.997    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                  44757    1.553    0.000    2.913    0.000 layers.py:37(reset)
                 544228    0.386    0.000    2.883    0.000 flatten.py:39(forward)
                1088496    1.274    0.000    2.877    0.000 tensor.py:596(__hash__)
                 136057    0.517    0.000    2.843    0.000 __init__.py:28(_make_grads)
               40817100    2.809    0.000    2.809    0.000 layer.py:48(check)
                 235520    0.355    0.000    2.793    0.000 fromnumeric.py:2912(prod)
                 136057    2.731    0.000    2.731    0.000 {built-in method gather}
               26410290    2.694    0.000    2.694    0.000 layer.py:124(isBlocking)
                3401425    2.605    0.000    2.605    0.000 {built-in method torch._C._get_tracing_state}
                 136057    0.605    0.000    2.580    0.000 tensor.py:506(__rsub__)
                 544228    2.497    0.000    2.497    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                 235520    0.698    0.000    2.438    0.000 fromnumeric.py:70(_wrapreduction)
               34046348    2.399    0.000    2.399    0.000 {method 'append' of 'list' objects}
                 136057    2.221    0.000    2.221    0.000 {built-in method ones_like}
        8925048/8925047    1.166    0.000    2.103    0.000 {built-in method builtins.len}
                4287072    1.396    0.000    2.088    0.000 levels.py:35(<genexpr>)
                 136057    1.975    0.000    1.975    0.000 {built-in method rsub}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-7>
Subject: Job 9348363: <test_run_9_0> in cluster <dcc> Done

Job <test_run_9_0> was submitted from host <n-62-30-7> by user <s183905> in cluster <dcc> at Wed Mar  3 14:55:06 2021
Job was executed on host(s) <n-62-20-7>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Wed Mar  3 14:56:54 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed Mar  3 14:56:54 2021
Terminated at Wed Mar  3 15:10:30 2021
Results reported at Wed Mar  3 15:10:30 2021

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

    CPU time :                                   784.13 sec.
    Max Memory :                                 2080 MB
    Average Memory :                             1828.25 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               6112.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   817 sec.
    Turnaround time :                            924 sec.

The output (if any) is above this job summary.

