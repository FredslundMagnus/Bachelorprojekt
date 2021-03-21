
# Parameters

    Name :                      Rock_level_resethigh-0
    Main :                      teleport
    Level :                     Levels.Rocks
    Hours :                     12.0
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
    Reset chance :              0.005
    Modified done chance :      0.05
    Miss intervention cost :    -0.2
    Intervention cost :         -0.05
    Replay size :               50000
    Sample size :               50
    Minutes used :              715 minutes.
    Hours used :                11 hours.

# Profiling


      38866788255 function calls (38740983088 primitive calls) in 42913.00 seconds

##    Ordered by: cumulative time
   List reduced from 470 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 42912.999 42912.999 {built-in method builtins.exec}
                      1    0.969    0.969 42912.999 42912.999 <string>:1(<module>)
                      1   99.297   99.297 42912.030 42912.030 main.py:13(teleport)
                2246530    8.350    0.000 14980.539    0.007 game.py:27(step)
                2246530   11.457    0.000 14455.466    0.006 layers.py:373(step)
                4493060   15.642    0.000 12449.556    0.003 agent.py:26(learn)
                4493060  328.781    0.000 10674.253    0.002 learner.py:42(Qlearn)
                2246530  171.587    0.000 9318.176    0.004 layers.py:18(step)
              224653000  454.138    0.000 9127.950    0.000 layer.py:74(move)
                2246530   75.109    0.000 7414.638    0.003 agent.py:50(_learn)
              224653000  699.267    0.000 6831.403    0.000 layers.py:390(check)
                2246530 3403.605    0.002 6146.662    0.003 replaybuffer.py:27(teleporter_save_data)
        141529739/15725583  563.145    0.000 5116.044    0.000 module.py:866(_call_impl)
                2246531  230.241    0.000 5111.978    0.002 layers.py:344(update)
                2246530   66.266    0.000 5010.336    0.002 agent.py:101(_learn)
               11232523   32.256    0.000 4765.944    0.000 network.py:24(forward)
               11232523  150.422    0.000 4665.721    0.000 container.py:117(forward)
                4493060   37.708    0.000 4478.989    0.001 optimizer.py:84(wrapper)
                4493060   18.664    0.000 4294.663    0.001 grad_mode.py:24(decorate_context)
                4493060  119.322    0.000 4232.936    0.001 adam.py:55(step)
                2246530 2554.761    0.001 4122.311    0.002 agent.py:77(interveen)
                4493060  879.096    0.000 3972.478    0.001 _functional.py:53(adam)
              224653000 3073.837    0.000 3640.448    0.000 layers.py:76(check)
                4492933  104.713    0.000 3164.243    0.001 agent.py:45(__call__)
                4493060   19.315    0.000 2639.140    0.001 tensor.py:195(backward)
                4493060   17.217    0.000 2619.182    0.001 __init__.py:68(backward)
                4493060 2504.027    0.001 2504.027    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                8380132   69.299    0.000 2233.686    0.000 layers.py:394(restart)
              189528224 2202.597    0.000 2202.597    0.000 {built-in method clone}
               20218779 1351.016    0.000 1989.737    0.000 layer.py:119(update)
                2246530 1145.739    0.001 1811.916    0.001 agent.py:59(modify)
               22465046   49.250    0.000 1706.861    0.000 conv.py:398(forward)
               22465046   28.235    0.000 1637.037    0.000 conv.py:390(_conv_forward)
               22465046 1608.802    0.000 1608.802    0.000 {built-in method conv2d}
              224653000  373.211    0.000 1606.790    0.000 layers.py:384(isFree)
                2246530  797.100    0.000 1584.125    0.001 replaybuffer.py:23(sample_data)
                8380132   31.459    0.000 1410.692    0.000 level.py:8(__init__)
               29204509   60.388    0.000 1326.646    0.000 linear.py:93(forward)
                8380132  202.115    0.000 1261.832    0.000 levels.py:95(generate)
               29204509   23.546    0.000 1239.981    0.000 functional.py:1737(linear)
             1889040199 1014.201    0.000 1233.579    0.000 layer.py:71(isFree)
               29204509 1210.612    0.000 1210.612    0.000 {built-in method torch._C._nn.linear}
                2246530   30.984    0.000  978.717    0.000 agent.py:96(__call__)
                6739463   45.184    0.000  970.955    0.000 agent.py:54(modify_board)
             3984765068  649.304    0.000  935.573    0.000 enum.py:646(__hash__)
               80875080  803.457    0.000  803.457    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               20218643  800.782    0.000  800.782    0.000 {built-in method cat}
               40437032   30.789    0.000  748.375    0.000 activation.py:713(forward)
                9299587  735.864    0.000  735.864    0.000 {built-in method tensor}
               75421188  101.766    0.000  731.597    0.000 layer.py:48(restart)
               40437032   33.676    0.000  717.586    0.000 functional.py:1364(leaky_relu)
               80875080  712.646    0.000  712.646    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               16760264   97.315    0.000  708.423    0.000 level.py:41(notUsed)
               40437032  677.334    0.000  677.334    0.000 {built-in method torch._C._nn.leaky_relu}
                4493060  103.003    0.000  638.697    0.000 optimizer.py:189(zero_grad)
                2246530   40.816    0.000  638.163    0.000 replaybuffer.py:19(stacker)
                6739463  623.803    0.000  623.803    0.000 {built-in method torch._C._nn.one_hot}
              196267687  604.629    0.000  604.629    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                4493060    6.158    0.000  593.041    0.000 game.py:23(board)
              224653000  358.519    0.000  577.842    0.000 layers.py:216(check)
              224653100   64.716    0.000  569.466    0.000 {built-in method builtins.all}
              224653000  349.761    0.000  566.001    0.000 layers.py:230(check)
              224653000  332.429    0.000  539.575    0.000 layers.py:244(check)
              714929803  162.992    0.000  530.224    0.000 layers.py:350(<genexpr>)
             1076703232  365.820    0.000  494.811    0.000 layer.py:98(add)
              224653000  308.469    0.000  476.583    0.000 layers.py:63(check)
                2246530  269.360    0.000  446.802    0.000 collector.py:54(collect)
             5260750475  445.819    0.000  445.819    0.000 layer.py:67(positions)
               40437540  443.360    0.000  443.360    0.000 {method 'add' of 'torch._C._TensorBase' objects}
             2182324004  437.048    0.000  437.048    0.000 layer.py:114(elements)
              485420648  204.388    0.000  414.853    0.000 layer.py:94(remove)
                8380232  199.044    0.000  399.220    0.000 layers.py:33(reset)
               40437540  388.056    0.000  388.056    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               10626662  133.122    0.000  372.315    0.000 random.py:315(sample)
              460907260  370.699    0.000  370.699    0.000 level.py:32(inverse)
               40437540  370.306    0.000  370.306    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               40437540  363.655    0.000  363.655    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              224653100  229.426    0.000  344.981    0.000 layers.py:110(isDone)
                4492933  121.085    0.000  329.254    0.000 exploration.py:53(softmaxer)
             3984781595  286.271    0.000  286.271    0.000 {built-in method builtins.hash}
               40437540  285.608    0.000  285.608    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              224653000  181.543    0.000  278.443    0.000 layers.py:203(check)
              283062834  194.200    0.000  239.255    0.000 tensor.py:906(grad)
                4493060    5.823    0.000  215.282    0.000 loss.py:527(forward)
             3256181459  211.362    0.000  211.362    0.000 {method 'append' of 'list' objects}
                4493060   17.146    0.000  209.459    0.000 functional.py:2898(mse_loss)
              224653000   88.626    0.000  204.881    0.000 layers.py:99(<listcomp>)
        2287187758/2287187756  162.724    0.000  195.677    0.000 {built-in method builtins.len}
               13479180  188.545    0.000  188.545    0.000 {built-in method sum}
               16760264   13.523    0.000  184.397    0.000 level.py:38(elementsIn)
              321885530  123.861    0.000  180.057    0.000 random.py:250(_randbelow_with_getrandbits)
              485420648  172.359    0.000  172.359    0.000 {method 'remove' of 'list' objects}
             1889040199  166.684    0.000  166.684    0.000 layer.py:175(isBlocking)
                4493060  137.081    0.000  137.081    0.000 {built-in method torch._C._nn.mse_loss}
               22465046   13.885    0.000  127.318    0.000 flatten.py:39(forward)
                4493733  121.980    0.000  121.980    0.000 {built-in method max}
                6739590    9.173    0.000  120.609    0.000 tensor.py:525(__rsub__)
               22465046  113.433    0.000  113.433    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                6739590  109.678    0.000  109.678    0.000 {built-in method rsub}
              143777167  105.435    0.000  105.435    0.000 {built-in method torch._C._get_tracing_state}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-2>
Subject: Job 9441988: <Rock_level_resethigh_0> in cluster <dcc> Done

Job <Rock_level_resethigh_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sat Mar 20 01:13:12 2021
Job was executed on host(s) <n-62-20-2>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sat Mar 20 13:08:39 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat Mar 20 13:08:39 2021
Terminated at Sun Mar 21 01:04:02 2021
Results reported at Sun Mar 21 01:04:02 2021

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

    CPU time :                                   42801.98 sec.
    Max Memory :                                 5486 MB
    Average Memory :                             4091.52 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               2706.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   42943 sec.
    Turnaround time :                            85850 sec.

The output (if any) is above this job summary.

