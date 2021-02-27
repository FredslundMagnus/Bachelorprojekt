
# Parameters

    Name :                      test_run_6-0
    Network :                   Networks.Small
    Learner :                   Learners.DoubleQlearn
    Gamma :                     1.0
    Batch :                     100
    Hours :                     0.2
    Width :                     15
    Height :                    15
    Minutes used :              7 minutes.
    Hours used :                0 hours.

# Profiling


      708467950 function calls (706569043 primitive calls) in 428.18 seconds

##    Ordered by: cumulative time
   List reduced from 230 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000  428.187  428.187 {built-in method builtins.exec}
                      1    0.000    0.000  428.187  428.187 <string>:1(<module>)
                      1    1.327    1.327  428.187  428.187 main.py:18(main)
                 135625    0.530    0.000  284.683    0.002 game.py:19(step)
                 135625    0.236    0.000  234.604    0.002 layers.py:202(step)
                 135625    8.526    0.000  169.698    0.001 layers.py:16(step)
               13562500    6.802    0.000  160.021    0.000 layer.py:65(move)
                 135625    3.315    0.000  133.701    0.001 agent.py:14(__call__)
               13562500   27.237    0.000  128.625    0.000 layers.py:218(check)
         2034375/135625    7.811    0.000   95.022    0.001 module.py:715(_call_impl)
                 135625    0.348    0.000   93.727    0.001 network.py:18(forward)
                 135625    2.306    0.000   92.586    0.001 container.py:115(forward)
                 542500   75.715    0.000   75.715    0.000 {built-in method tensor}
                 271250    0.237    0.000   66.016    0.000 game.py:15(board)
                 135626    7.573    0.000   64.836    0.000 layers.py:189(update)
                 813750    1.317    0.000   63.267    0.000 conv.py:422(forward)
                 813750    1.187    0.000   61.480    0.000 conv.py:414(_conv_forward)
                 813750   60.069    0.000   60.069    0.000 {built-in method conv2d}
               13562500   26.065    0.000   41.701    0.000 layers.py:123(check)
               13562600    3.258    0.000   31.274    0.000 {built-in method builtins.all}
               40688400    8.530    0.000   29.424    0.000 layers.py:193(<genexpr>)
              108514108   18.293    0.000   25.861    0.000 enum.py:646(__hash__)
               13562500    4.982    0.000   24.594    0.000 layers.py:212(isFree)
                1085008    5.541    0.000   23.538    0.000 layer.py:90(update)
               13562500   13.467    0.000   21.628    0.000 layers.py:94(check)
               13562600   12.997    0.000   19.885    0.000 layers.py:64(isDone)
               13568184   16.837    0.000   19.612    0.000 layer.py:62(isFree)
               13562500   11.616    0.000   17.157    0.000 layers.py:49(check)
               13562500   11.274    0.000   16.901    0.000 layers.py:76(check)
              191097516   16.700    0.000   16.700    0.000 layer.py:58(positions)
                 678125    0.545    0.000   13.283    0.000 activation.py:101(forward)
                 678125    0.798    0.000   12.737    0.000 functional.py:1124(relu)
                 678125   11.857    0.000   11.857    0.000 {built-in method relu}
                4637868   11.558    0.000   11.558    0.000 layer.py:85(elements)
                      1    0.000    0.000    8.000    8.000 agent.py:10(__init__)
                      1    0.000    0.000    7.999    7.999 network.py:27(__init__)
                      3    0.000    0.000    7.965    2.655 module.py:529(to)
                   45/3    0.000    0.000    7.965    2.655 module.py:357(_apply)
                     36    0.000    0.000    7.964    0.221 module.py:607(convert)
                     36    7.963    0.221    7.964    0.221 {method 'to' of 'torch._C._TensorBase' objects}
              108514108    7.568    0.000    7.568    0.000 {built-in method builtins.hash}
                 135625    4.697    0.000    4.697    0.000 {method 'tolist' of 'torch._C._TensorBase' objects}
                 135625    4.264    0.000    4.264    0.000 {built-in method max}
               54250000    4.001    0.000    4.001    0.000 layer.py:48(check)
                 135625    0.152    0.000    3.414    0.000 activation.py:1197(forward)
                1085008    3.335    0.000    3.335    0.000 layer.py:97(<listcomp>)
                 135625    0.185    0.000    3.262    0.000 functional.py:1479(softmax)
                1085008    3.105    0.000    3.105    0.000 layer.py:98(<listcomp>)
                 135625    3.062    0.000    3.062    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               13567372    1.628    0.000    1.628    0.000 layer.py:125(isBlocking)
                2034375    1.560    0.000    1.560    0.000 {built-in method torch._C._get_tracing_state}
                 135625    0.100    0.000    1.386    0.000 flatten.py:39(forward)
                 135625    1.286    0.000    1.286    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               13563000    1.009    0.000    1.009    0.000 layer.py:51(isDone)
                1763272    0.934    0.000    0.934    0.000 module.py:765(__getattr__)
                1220636    0.622    0.000    0.884    0.000 layer.py:73(remove)
                8273125    0.743    0.000    0.743    0.000 {method 'values' of 'collections.OrderedDict' objects}
                1239992    0.544    0.000    0.717    0.000 layer.py:77(add)
                 135626    0.560    0.000    0.560    0.000 layers.py:190(<listcomp>)
        4074361/4074360    0.522    0.000    0.522    0.000 {built-in method builtins.len}
                 135626    0.327    0.000    0.327    0.000 layers.py:191(<listcomp>)
                3716173    0.280    0.000    0.280    0.000 {method 'append' of 'list' objects}
                 135626    0.171    0.000    0.254    0.000 auxillaries.py:17(loop)
                      1    0.000    0.000    0.187    0.187 game.py:8(__init__)
                1221448    0.156    0.000    0.156    0.000 {method 'remove' of 'list' objects}
                    100    0.001    0.000    0.155    0.002 layers.py:222(restart)
                 135625    0.108    0.000    0.154    0.000 container.py:107(__iter__)
                    100    0.000    0.000    0.139    0.001 levels.py:8(__init__)
                    100    0.000    0.000    0.139    0.001 level.py:8(__init__)
                    100    0.014    0.000    0.137    0.001 levels.py:11(generate)
                 813822    0.098    0.000    0.098    0.000 _jit_internal.py:750(is_scripting)
                 135627    0.082    0.000    0.082    0.000 {built-in method time.time}
                    300    0.003    0.000    0.066    0.000 level.py:34(notUsed)
                  34500    0.062    0.000    0.062    0.000 level.py:25(inverse)
                    100    0.020    0.000    0.038    0.000 levels.py:71(RFS)
                 135625    0.035    0.000    0.035    0.000 collector.py:11(collect)
                 135625    0.035    0.000    0.035    0.000 {built-in method builtins.iter}
                      3    0.000    0.000    0.034    0.011 network.py:13(__init__)
                     18    0.000    0.000    0.033    0.002 conv.py:394(__init__)
                     18    0.002    0.000    0.033    0.002 conv.py:37(__init__)
                    200    0.011    0.000    0.031    0.000 layers.py:36(reset)
                     18    0.000    0.000    0.029    0.002 conv.py:85(reset_parameters)
                     18    0.000    0.000    0.028    0.002 init.py:352(kaiming_uniform_)
                     36    0.025    0.001    0.025    0.001 {method 'uniform_' of 'torch._C._TensorBase' objects}
                      1    0.000    0.000    0.022    0.022 layers.py:146(__init__)
                      8    0.000    0.000    0.022    0.003 layer.py:26(__init__)
                    800    0.002    0.000    0.016    0.000 layer.py:39(restart)
                  45200    0.015    0.000    0.015    0.000 layer.py:100(grid)
                  19200    0.006    0.000    0.009    0.000 levels.py:28(<genexpr>)
                   5100    0.002    0.000    0.006    0.000 random.py:285(choice)
                   5709    0.003    0.000    0.004    0.000 random.py:250(_randbelow_with_getrandbits)
                   4800    0.004    0.000    0.004    0.000 {method 'intersection_update' of 'set' objects}
                   4800    0.003    0.000    0.003    0.000 levels.py:81(<listcomp>)
                     36    0.001    0.000    0.003    0.000 init.py:271(_calculate_fan_in_and_fan_out)
                  24669    0.003    0.000    0.003    0.000 {method 'add' of 'set' objects}
                     18    0.000    0.000    0.003    0.000 init.py:342(_calculate_correct_fan)
                    300    0.000    0.000    0.003    0.000 level.py:31(elementsIn)
                  14310    0.002    0.000    0.002    0.000 {built-in method builtins.min}
                  14310    0.002    0.000    0.002    0.000 {built-in method builtins.max}
                     72    0.002    0.000    0.002    0.000 {method 'size' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-3>
Subject: Job 9335760: <test_run_6_0> in cluster <dcc> Done

Job <test_run_6_0> was submitted from host <n-62-27-18> by user <s183905> in cluster <dcc> at Sat Feb 27 17:54:53 2021
Job was executed on host(s) <n-62-20-3>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sat Feb 27 17:54:54 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat Feb 27 17:54:54 2021
Terminated at Sat Feb 27 18:02:19 2021
Results reported at Sat Feb 27 18:02:19 2021

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

    CPU time :                                   422.86 sec.
    Max Memory :                                 2060 MB
    Average Memory :                             1872.17 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               6132.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                7
    Run time :                                   508 sec.
    Turnaround time :                            446 sec.

The output (if any) is above this job summary.

