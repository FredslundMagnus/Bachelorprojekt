
# Parameters

    Name :                      Rock_level_hard_new_parameters-0
    Main :                      teleport
    Level :                     Levels.Rocks
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
    Softmax cap :               0.025
    Gamma :                     0.98
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.04
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Minutes used :              655 minutes.
    Hours used :                10 hours.

# Profiling


      37299475461 function calls (37168547646 primitive calls) in 39313.89 seconds

##    Ordered by: cumulative time
   List reduced from 470 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 39313.886 39313.886 {built-in method builtins.exec}
                      1    1.718    1.718 39313.885 39313.885 <string>:1(<module>)
                      1  101.993  101.993 39312.167 39312.167 main.py:13(teleport)
                2338107    8.602    0.000 15863.636    0.007 game.py:27(step)
                2338107   11.736    0.000 15368.902    0.007 layers.py:373(step)
                2338107  191.401    0.000 10612.593    0.005 layers.py:18(step)
              233810700  507.338    0.000 10402.404    0.000 layer.py:74(move)
                4676214   15.934    0.000 10010.851    0.002 agent.py:26(learn)
                4676214  262.506    0.000 8444.480    0.002 learner.py:42(Qlearn)
              233810700  700.376    0.000 7832.709    0.000 layers.py:390(check)
                2338107   70.474    0.000 5991.393    0.003 agent.py:50(_learn)
                2338108  243.037    0.000 4727.274    0.002 layers.py:344(update)
              233810700 4019.232    0.000 4575.445    0.000 layers.py:76(check)
                2338107 2613.085    0.001 4468.800    0.002 replaybuffer.py:27(teleporter_save_data)
        147292954/16366150  547.830    0.000 4403.836    0.000 module.py:866(_call_impl)
               11689936   31.714    0.000 4085.991    0.000 network.py:24(forward)
                2338107   60.405    0.000 3994.286    0.002 agent.py:101(_learn)
               11689936  128.651    0.000 3979.788    0.000 container.py:117(forward)
                4676214   36.986    0.000 3237.221    0.001 optimizer.py:84(wrapper)
                2338107 1869.284    0.001 3218.301    0.001 agent.py:77(interveen)
                4676214   19.472    0.000 3069.421    0.001 grad_mode.py:24(decorate_context)
                4676214  121.185    0.000 3006.772    0.001 adam.py:55(step)
                4675615   97.759    0.000 2747.645    0.001 agent.py:45(__call__)
                4676214  623.013    0.000 2740.306    0.001 _functional.py:53(adam)
                2338107 2001.700    0.001 2716.206    0.001 replaybuffer.py:23(sample_data)
                4676214   21.300    0.000 2262.794    0.000 tensor.py:195(backward)
                4676214   18.230    0.000 2240.870    0.000 __init__.py:68(backward)
                4676214 2137.160    0.000 2137.160    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
               21042972 1326.086    0.000 2009.647    0.000 layer.py:119(update)
              233810700  342.666    0.000 1814.539    0.000 layers.py:384(isFree)
                6380628   57.828    0.000 1791.624    0.000 layers.py:394(restart)
              188745546 1542.755    0.000 1542.755    0.000 {built-in method clone}
               23379872   50.805    0.000 1504.637    0.000 conv.py:398(forward)
             1834977422 1240.817    0.000 1471.873    0.000 layer.py:71(isFree)
                2338107  893.544    0.000 1456.661    0.001 agent.py:59(modify)
               23379872   29.244    0.000 1432.574    0.000 conv.py:390(_conv_forward)
               23379872 1403.329    0.000 1403.329    0.000 {built-in method conv2d}
                6380628   27.303    0.000 1134.981    0.000 level.py:8(__init__)
               30393594   58.367    0.000 1102.458    0.000 linear.py:93(forward)
               30393594   23.241    0.000 1016.889    0.000 functional.py:1737(linear)
                6380628  156.448    0.000 1013.513    0.000 levels.py:95(generate)
               30393594  988.145    0.000  988.145    0.000 {built-in method torch._C._nn.linear}
             3894253339  645.122    0.000  911.269    0.000 enum.py:646(__hash__)
                2338107   27.632    0.000  855.759    0.000 agent.py:96(__call__)
                7013722   40.758    0.000  850.011    0.000 agent.py:54(modify_board)
                9675734  712.840    0.000  712.840    0.000 {built-in method tensor}
               21042364  685.834    0.000  685.834    0.000 {built-in method cat}
              233810700  374.495    0.000  596.095    0.000 layers.py:216(check)
                4676214    5.606    0.000  593.265    0.000 game.py:23(board)
              233810800   64.855    0.000  590.322    0.000 {built-in method builtins.all}
               57425652   79.288    0.000  581.674    0.000 layer.py:48(restart)
               42083530   31.890    0.000  580.918    0.000 activation.py:713(forward)
              233810700  348.013    0.000  566.385    0.000 layers.py:230(check)
                7013722  560.600    0.000  560.600    0.000 {built-in method torch._C._nn.one_hot}
              233810700  345.883    0.000  559.828    0.000 layers.py:244(check)
                2338107   44.115    0.000  559.538    0.000 replaybuffer.py:19(stacker)
               12761256   75.412    0.000  557.419    0.000 level.py:41(notUsed)
              721135776  164.844    0.000  551.511    0.000 layers.py:350(<genexpr>)
               42083530   31.734    0.000  549.028    0.000 functional.py:1364(leaky_relu)
               84171852  524.392    0.000  524.392    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               42083530  511.051    0.000  511.051    0.000 {built-in method torch._C._nn.leaky_relu}
              233810700  335.035    0.000  486.293    0.000 layers.py:63(check)
                4676214   85.627    0.000  480.481    0.000 optimizer.py:189(zero_grad)
               84171852  474.475    0.000  474.475    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
             1793182765  466.825    0.000  466.825    0.000 layer.py:114(elements)
             5456319286  456.514    0.000  456.514    0.000 layer.py:67(positions)
              877708021  310.528    0.000  420.595    0.000 layer.py:98(add)
              419892183  195.792    0.000  397.061    0.000 layer.py:94(remove)
              233810800  248.415    0.000  365.978    0.000 layers.py:110(isDone)
              195759268  357.862    0.000  357.862    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                8718735  126.707    0.000  353.683    0.000 random.py:315(sample)
               42085926  332.052    0.000  332.052    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                2338107  189.132    0.000  323.069    0.000 collector.py:54(collect)
                6380728  150.332    0.000  311.603    0.000 layers.py:33(reset)
              319031400  295.361    0.000  295.361    0.000 level.py:32(inverse)
              233810700  191.577    0.000  292.079    0.000 layers.py:203(check)
                4675615  105.791    0.000  283.856    0.000 exploration.py:53(softmaxer)
               42085926  271.577    0.000  271.577    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
             3894270514  266.151    0.000  266.151    0.000 {built-in method builtins.hash}
               42085926  253.160    0.000  253.160    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               42085926  251.375    0.000  251.375    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              294601536  183.333    0.000  227.283    0.000 tensor.py:906(grad)
              233810700   84.410    0.000  193.561    0.000 layers.py:99(<listcomp>)
        2430132267/2430132265  160.555    0.000  190.935    0.000 {built-in method builtins.len}
                4676214    6.318    0.000  188.045    0.000 loss.py:527(forward)
               42085926  186.547    0.000  186.547    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
             2703113862  183.718    0.000  183.718    0.000 {method 'append' of 'list' objects}
                4676214   16.730    0.000  181.726    0.000 functional.py:2898(mse_loss)
             1834977422  178.865    0.000  178.865    0.000 layer.py:175(isBlocking)
              308353769  121.637    0.000  176.456    0.000 random.py:250(_randbelow_with_getrandbits)
              419892183  167.726    0.000  167.726    0.000 {method 'remove' of 'list' objects}
               12761256   10.699    0.000  142.082    0.000 level.py:38(elementsIn)
               14028642  140.485    0.000  140.485    0.000 {built-in method sum}
                4676214  110.976    0.000  110.976    0.000 {built-in method torch._C._nn.mse_loss}
                4676914  100.076    0.000  100.076    0.000 {built-in method max}
               23379872   15.171    0.000  100.002    0.000 flatten.py:39(forward)
                7014321    9.070    0.000   97.117    0.000 tensor.py:525(__rsub__)
                4675615   89.590    0.000   89.590    0.000 {built-in method multinomial}
                7014321   86.519    0.000   86.519    0.000 {built-in method rsub}
               23379872   84.830    0.000   84.830    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-7>
Subject: Job 9447917: <Rock_level_hard_new_parameters_0> in cluster <dcc> Done

Job <Rock_level_hard_new_parameters_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon Mar 22 12:54:42 2021
Job was executed on host(s) <n-62-20-7>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon Mar 22 12:54:43 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Mar 22 12:54:43 2021
Terminated at Mon Mar 22 23:50:07 2021
Results reported at Mon Mar 22 23:50:07 2021

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

    CPU time :                                   39299.89 sec.
    Max Memory :                                 3024 MB
    Average Memory :                             3013.00 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               5168.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   39442 sec.
    Turnaround time :                            39325 sec.

The output (if any) is above this job summary.

