
    Name :                      test_run_5-0
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


      705469626 function calls (703585615 primitive calls) in 428.44 seconds

##    Ordered by: cumulative time
   List reduced from 230 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000  428.438  428.438 {built-in method builtins.exec}
                      1    0.000    0.000  428.438  428.438 <string>:1(<module>)
                      1    1.339    1.339  428.438  428.438 main.py:18(main)
                 134561    0.560    0.000  285.786    0.002 game.py:19(step)
                 134561    0.233    0.000  236.226    0.002 layers.py:202(step)
                 134561    8.288    0.000  171.136    0.001 layers.py:16(step)
               13456100    6.728    0.000  161.675    0.000 layer.py:65(move)
                 134561    3.257    0.000  132.587    0.001 agent.py:14(__call__)
               13456100   26.616    0.000  129.099    0.000 layers.py:218(check)
         2018415/134561    7.903    0.000   94.361    0.001 module.py:715(_call_impl)
                 134561    0.345    0.000   93.064    0.001 network.py:18(forward)
                 134561    2.255    0.000   91.862    0.001 container.py:115(forward)
                 538244   74.883    0.000   74.883    0.000 {built-in method tensor}
                 269122    0.241    0.000   65.355    0.000 game.py:15(board)
                 134562    7.589    0.000   65.028    0.000 layers.py:189(update)
                 807366    1.357    0.000   62.676    0.000 conv.py:422(forward)
                 807366    1.213    0.000   60.859    0.000 conv.py:414(_conv_forward)
                 807366   59.422    0.000   59.422    0.000 {built-in method conv2d}
               13456100   26.930    0.000   42.897    0.000 layers.py:123(check)
               13456200    3.350    0.000   31.596    0.000 {built-in method builtins.all}
               40369200    8.955    0.000   29.694    0.000 layers.py:193(<genexpr>)
              107662908   18.453    0.000   26.083    0.000 enum.py:646(__hash__)
               13456100    5.037    0.000   25.847    0.000 layers.py:212(isFree)
                1076496    5.667    0.000   23.360    0.000 layer.py:90(update)
               13456100   13.759    0.000   21.572    0.000 layers.py:94(check)
               14000040   17.933    0.000   20.810    0.000 layer.py:62(isFree)
               13456200   12.903    0.000   19.736    0.000 layers.py:64(isDone)
               13456100   11.676    0.000   17.174    0.000 layers.py:49(check)
               13456100   11.223    0.000   16.915    0.000 layers.py:76(check)
              190001990   16.240    0.000   16.240    0.000 layer.py:58(positions)
                 672805    0.525    0.000   13.194    0.000 activation.py:101(forward)
                 672805    0.857    0.000   12.669    0.000 functional.py:1124(relu)
                 672805   11.727    0.000   11.727    0.000 {built-in method relu}
                4870789   11.253    0.000   11.253    0.000 layer.py:85(elements)
                      1    0.000    0.000    8.244    8.244 agent.py:10(__init__)
                      1    0.000    0.000    8.244    8.244 network.py:27(__init__)
                      3    0.000    0.000    8.210    2.737 module.py:529(to)
                   45/3    0.000    0.000    8.209    2.736 module.py:357(_apply)
                     36    0.000    0.000    8.208    0.228 module.py:607(convert)
                     36    8.207    0.228    8.208    0.228 {method 'to' of 'torch._C._TensorBase' objects}
              107662908    7.629    0.000    7.629    0.000 {built-in method builtins.hash}
                 134561    4.635    0.000    4.635    0.000 {method 'tolist' of 'torch._C._TensorBase' objects}
                 134561    4.209    0.000    4.209    0.000 {built-in method max}
               53824400    3.925    0.000    3.925    0.000 layer.py:48(check)
                 134561    0.159    0.000    3.446    0.000 activation.py:1197(forward)
                1076496    3.332    0.000    3.332    0.000 layer.py:97(<listcomp>)
                 134561    0.189    0.000    3.287    0.000 functional.py:1479(softmax)
                1076496    3.108    0.000    3.108    0.000 layer.py:98(<listcomp>)
                 134561    3.083    0.000    3.083    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               13730120    1.678    0.000    1.678    0.000 layer.py:125(isBlocking)
                2018415    1.521    0.000    1.521    0.000 {built-in method torch._C._get_tracing_state}
                 134561    0.116    0.000    1.388    0.000 flatten.py:39(forward)
                 134561    1.272    0.000    1.272    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               13456600    1.004    0.000    1.004    0.000 layer.py:51(isDone)
                1345604    0.693    0.000    0.995    0.000 layer.py:73(remove)
                1749440    0.929    0.000    0.929    0.000 module.py:765(__getattr__)
                1364953    0.631    0.000    0.818    0.000 layer.py:77(add)
                8208221    0.744    0.000    0.744    0.000 {method 'values' of 'collections.OrderedDict' objects}
                 134562    0.551    0.000    0.551    0.000 layers.py:190(<listcomp>)
        4042441/4042440    0.506    0.000    0.506    0.000 {built-in method builtins.len}
                 134562    0.322    0.000    0.322    0.000 layers.py:191(<listcomp>)
                4091087    0.310    0.000    0.310    0.000 {method 'append' of 'list' objects}
                 134562    0.175    0.000    0.258    0.000 auxillaries.py:17(loop)
                      1    0.000    0.000    0.193    0.193 game.py:8(__init__)
                1346424    0.180    0.000    0.180    0.000 {method 'remove' of 'list' objects}
                    100    0.001    0.000    0.161    0.002 layers.py:222(restart)
                 134561    0.101    0.000    0.148    0.000 container.py:107(__iter__)
                    100    0.000    0.000    0.143    0.001 levels.py:8(__init__)
                    100    0.000    0.000    0.143    0.001 level.py:8(__init__)
                    100    0.014    0.000    0.142    0.001 levels.py:11(generate)
                 807438    0.100    0.000    0.100    0.000 _jit_internal.py:750(is_scripting)
                 134563    0.082    0.000    0.082    0.000 {built-in method time.time}
                    300    0.003    0.000    0.067    0.000 level.py:34(notUsed)
                  34500    0.063    0.000    0.063    0.000 level.py:25(inverse)
                 269920    0.051    0.000    0.051    0.000 layers.py:97(isBlocking)
                    100    0.020    0.000    0.040    0.000 levels.py:71(RFS)
                 134561    0.037    0.000    0.037    0.000 {built-in method builtins.iter}
                      3    0.000    0.000    0.034    0.011 network.py:13(__init__)
                     18    0.000    0.000    0.033    0.002 conv.py:394(__init__)
                     18    0.002    0.000    0.033    0.002 conv.py:37(__init__)
                    200    0.012    0.000    0.032    0.000 layers.py:36(reset)
                 134561    0.031    0.000    0.031    0.000 collector.py:11(collect)
                     18    0.000    0.000    0.029    0.002 conv.py:85(reset_parameters)
                     18    0.000    0.000    0.029    0.002 init.py:352(kaiming_uniform_)
                     36    0.026    0.001    0.026    0.001 {method 'uniform_' of 'torch._C._TensorBase' objects}
                      1    0.000    0.000    0.022    0.022 layers.py:146(__init__)
                      8    0.000    0.000    0.022    0.003 layer.py:26(__init__)
                    800    0.002    0.000    0.016    0.000 layer.py:39(restart)
                  45200    0.015    0.000    0.015    0.000 layer.py:100(grid)
                  19200    0.006    0.000    0.009    0.000 levels.py:28(<genexpr>)
                   5100    0.002    0.000    0.006    0.000 random.py:285(choice)
                   4800    0.005    0.000    0.005    0.000 {method 'intersection_update' of 'set' objects}
                   5714    0.003    0.000    0.004    0.000 random.py:250(_randbelow_with_getrandbits)
                   4800    0.003    0.000    0.003    0.000 levels.py:81(<listcomp>)
                  24669    0.003    0.000    0.003    0.000 {method 'add' of 'set' objects}
                    300    0.000    0.000    0.003    0.000 level.py:31(elementsIn)
                     36    0.002    0.000    0.003    0.000 init.py:271(_calculate_fan_in_and_fan_out)
                  14434    0.002    0.000    0.002    0.000 {built-in method builtins.min}
                     18    0.000    0.000    0.002    0.000 init.py:342(_calculate_correct_fan)
                  14434    0.002    0.000    0.002    0.000 {built-in method builtins.max}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-3>
Subject: Job 9335754: <test_run_5_0> in cluster <dcc> Done

Job <test_run_5_0> was submitted from host <n-62-27-18> by user <s183905> in cluster <dcc> at Sat Feb 27 17:40:04 2021
Job was executed on host(s) <n-62-20-3>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sat Feb 27 17:40:05 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat Feb 27 17:40:05 2021
Terminated at Sat Feb 27 17:47:30 2021
Results reported at Sat Feb 27 17:47:30 2021

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

    CPU time :                                   422.70 sec.
    Max Memory :                                 2062 MB
    Average Memory :                             1833.60 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               6130.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                7
    Run time :                                   511 sec.
    Turnaround time :                            446 sec.

The output (if any) is above this job summary.

