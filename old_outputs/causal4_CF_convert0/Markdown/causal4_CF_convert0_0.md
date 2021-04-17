
# Parameters

    Name :                      causal4_CF_convert0-0
    Main :                      CFagent
    Level :                     Levels.Causal4
    Hours :                     16.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Network1 :                  Networks.Teleporter
    K1 :                        5000000
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
    K2 :                        1000000
    Learner2 :                  Learners.Qlearn
    Exploration2 :              Explorations.epsilonGreedy
    Gamma2 :                    0.95
    Layer blocks :              True
    Layer goal :                True
    Layer gold :                True
    Layer keys :                True
    Layer door :                True
    Layer holder :              True
    Layer putter :              True
    Layer rock :                True
    Layer dirt :                True
    Layer diamond1 :            True
    Layer diamond2 :            True
    Layer diamond3 :            True
    Layer diamond4 :            True
    Layer reddoor :             True
    Layer redkeys :             True
    Layer bluedoor :            True
    Layer bluekeys :            True
    Layer pink1 :               True
    Layer pink2 :               True
    Layer pink3 :               True
    Layer brown1 :              True
    Layer brown2 :              True
    Layer brown3 :              True
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                0
    Minutes used :              955 minutes.
    Hours used :                15 hours.

# Profiling


      46839762140 function calls (46594540549 primitive calls) in 57316.75 seconds

##    Ordered by: cumulative time
   List reduced from 508 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 57316.748 57316.748 {built-in method builtins.exec}
                      1    4.746    4.746 57316.748 57316.748 <string>:1(<module>)
                      1  183.037  183.037 57312.002 57312.002 main.py:96(CFagent)
                8004927   28.229    0.000 18462.975    0.002 agent.py:29(learn)
                8004912  465.750    0.000 14977.905    0.002 learner.py:42(Qlearn)
                2668309   13.488    0.000 13424.668    0.005 game.py:35(step)
                2668309   14.009    0.000 12820.754    0.005 layers.py:448(step)
                2668309  228.040    0.000 8782.915    0.003 layers.py:17(step)
              266509923  627.257    0.000 8532.654    0.000 layer.py:84(move)
        274549240/29329340 1052.092    0.000 8496.086    0.000 module.py:866(_call_impl)
               21324428   54.331    0.000 7943.542    0.000 network.py:24(forward)
               21324428  252.250    0.000 7743.403    0.000 container.py:117(forward)
                2668309  616.644    0.000 7550.148    0.003 agent.py:201(counterfact)
                2668309  276.416    0.000 7191.867    0.003 agent.py:54(_learn)
                2668309  273.564    0.000 6585.601    0.002 agent.py:193(_learn)
                8004912   65.446    0.000 5829.754    0.001 optimizer.py:84(wrapper)
                8004912   33.244    0.000 5543.136    0.001 grad_mode.py:24(decorate_context)
                8004912  233.991    0.000 5435.137    0.001 adam.py:55(step)
                8004912 1135.548    0.000 4943.535    0.001 _functional.py:53(adam)
              266509923  748.782    0.000 4862.348    0.000 layers.py:465(check)
                2668309   77.717    0.000 4640.868    0.002 agent.py:115(_learn)
               42055483 4227.445    0.000 4227.445    0.000 {built-in method tensor}
               35851188   22.233    0.000 4084.743    0.000 game.py:31(board)
                6657629  169.258    0.000 4073.273    0.001 agent.py:49(__call__)
                2668309 3156.854    0.001 4029.812    0.002 replaybuffer.py:22(sample_data)
                2668310  290.876    0.000 3999.246    0.001 layers.py:419(update)
                8004912   30.606    0.000 3906.636    0.000 tensor.py:195(backward)
                8004912   31.789    0.000 3874.886    0.000 __init__.py:68(backward)
                8004912 3694.810    0.000 3694.810    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
               53366190 2003.273    0.000 3447.184    0.000 layer.py:129(update)
                2668309 2647.458    0.001 3412.105    0.001 replaybuffer.py:49(sample_data)
                2668309 1877.939    0.001 3303.324    0.001 replaybuffer.py:28(teleporter_save_data)
                2668309 1395.772    0.001 3010.605    0.001 agent.py:86(interveen)
               42648856   95.020    0.000 2893.521    0.000 conv.py:398(forward)
               42648856   57.185    0.000 2755.179    0.000 conv.py:390(_conv_forward)
               42648856 2697.994    0.000 2697.994    0.000 {built-in method conv2d}
              266398802  465.745    0.000 2621.602    0.000 layers.py:459(isFree)
               58636666  112.397    0.000 2173.156    0.000 linear.py:93(forward)
             2522606865 1793.205    0.000 2155.857    0.000 layer.py:81(isFree)
               58636666   46.664    0.000 2004.311    0.000 functional.py:1737(linear)
               58636666 1946.478    0.000 1946.478    0.000 {built-in method torch._C._nn.linear}
                2668309  985.499    0.000 1653.787    0.001 agent.py:67(modify)
                1325284   25.331    0.000 1502.451    0.001 agent.py:168(choose_action)
              145216371 1361.987    0.000 1361.987    0.000 {built-in method clone}
               38677262 1349.065    0.000 1349.065    0.000 {built-in method cat}
               79961094   66.278    0.000 1157.963    0.000 activation.py:713(forward)
                9325938   53.786    0.000 1149.244    0.000 agent.py:59(modify_board)
                2668294   45.529    0.000 1134.029    0.000 agent.py:164(__call__)
             4593766210  767.274    0.000 1117.125    0.000 enum.py:646(__hash__)
               79961094   68.080    0.000 1091.685    0.000 functional.py:1364(leaky_relu)
                2668309   43.155    0.000 1085.748    0.000 agent.py:110(__call__)
               79961094 1010.844    0.000 1010.844    0.000 {built-in method torch._C._nn.leaky_relu}
              266831000  133.212    0.000  998.994    0.000 {built-in method builtins.all}
              149425004  961.597    0.000  961.597    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
             1615091387  387.434    0.000  895.694    0.000 layers.py:425(<genexpr>)
              149425004  861.390    0.000  861.390    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                8004912  153.514    0.000  848.161    0.000 optimizer.py:189(zero_grad)
              266509923  522.525    0.000  832.201    0.000 layers.py:270(check)
              879445297  820.866    0.000  820.866    0.000 layer.py:124(elements)
                2506197   30.442    0.000  800.312    0.000 layers.py:469(restart)
                9325938  761.911    0.000  761.911    0.000 {built-in method torch._C._nn.one_hot}
              266509923  454.225    0.000  753.013    0.000 layers.py:233(check)
              266509923  564.997    0.000  726.399    0.000 layers.py:67(check)
                2668309   59.322    0.000  685.793    0.000 replaybuffer.py:18(stacker)
                2668294   56.716    0.000  583.664    0.000 replaybuffer.py:45(stacker)
               74712502  563.921    0.000  563.921    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              266509923  426.172    0.000  545.624    0.000 layers.py:56(check)
                2506197   13.560    0.000  543.121    0.000 level.py:8(__init__)
             6414005767  522.769    0.000  522.769    0.000 layer.py:77(positions)
                2668309  207.597    0.000  508.403    0.000 replaybuffer.py:55(CF_save_data)
               74712502  500.950    0.000  500.950    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               74712502  451.519    0.000  451.519    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               74712502  450.723    0.000  450.723    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
        6525611710/6525611707  400.023    0.000  448.082    0.000 {built-in method builtins.len}
                2506197   81.110    0.000  445.663    0.000 levels.py:199(generate)
              266831000  295.224    0.000  434.344    0.000 layers.py:100(isDone)
              266509923  274.778    0.000  431.694    0.000 layers.py:294(check)
              266509923  278.545    0.000  430.230    0.000 layers.py:257(check)
                6657629  151.524    0.000  405.061    0.000 exploration.py:53(softmaxer)
              522987598  324.009    0.000  401.997    0.000 tensor.py:906(grad)
               10349012  151.172    0.000  396.195    0.000 random.py:315(sample)
                2668309  225.968    0.000  382.116    0.000 collector.py:54(collect)
             4593796705  349.856    0.000  349.856    0.000 {built-in method builtins.hash}
               74712502  332.768    0.000  332.768    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              266509923  225.761    0.000  330.068    0.000 layers.py:42(check)
                8004912   11.175    0.000  323.298    0.000 loss.py:527(forward)
                8004912   29.342    0.000  312.123    0.000 functional.py:2898(mse_loss)
                8004928  304.052    0.000  304.052    0.000 {built-in method nonzero}
              157210603  295.296    0.000  295.296    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                5012394   35.486    0.000  287.955    0.000 level.py:41(notUsed)
              241563546  157.842    0.000  226.438    0.000 layer.py:104(remove)
               25061970   33.106    0.000  219.046    0.000 layer.py:58(restart)
               53366190  208.250    0.000  208.250    0.000 layer.py:141(<listcomp>)
              387057609  152.094    0.000  207.255    0.000 layer.py:108(add)
              328075929  136.853    0.000  202.807    0.000 random.py:250(_randbelow_with_getrandbits)
             1997898198  194.814    0.000  194.814    0.000 layer.py:181(isBlocking)
                8004912  191.443    0.000  191.443    0.000 {built-in method torch._C._nn.mse_loss}
               42648856   27.968    0.000  187.234    0.000 flatten.py:39(forward)
                8005843  176.090    0.000  176.090    0.000 {built-in method max}
               11998505   17.058    0.000  165.245    0.000 tensor.py:525(__rsub__)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-2>
Subject: Job 9495290: <causal4_CF_convert0_0> in cluster <dcc> Done

Job <causal4_CF_convert0_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon Apr  5 02:37:26 2021
Job was executed on host(s) <n-62-20-2>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon Apr  5 02:37:27 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Apr  5 02:37:27 2021
Terminated at Mon Apr  5 18:32:54 2021
Results reported at Mon Apr  5 18:32:54 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=16G]"
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

    CPU time :                                   57171.24 sec.
    Max Memory :                                 8323 MB
    Average Memory :                             5818.06 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               8061.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   57386 sec.
    Turnaround time :                            57328 sec.

The output (if any) is above this job summary.

