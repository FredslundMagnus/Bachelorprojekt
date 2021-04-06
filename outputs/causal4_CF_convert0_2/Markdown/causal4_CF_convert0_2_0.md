
# Parameters

    Name :                      causal4_CF_convert0_2-0
    Main :                      CFagent
    Level :                     Levels.Causal4
    Hours :                     24.0
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
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      58016859889 function calls (57707534118 primitive calls) in 86116.59 seconds

##    Ordered by: cumulative time
   List reduced from 507 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86116.592 86116.592 {built-in method builtins.exec}
                      1    4.794    4.794 86116.592 86116.592 <string>:1(<module>)
                      1  246.476  246.476 86111.798 86111.798 main.py:96(CFagent)
                9859638   38.161    0.000 29413.050    0.003 agent.py:29(learn)
                9859626  742.079    0.000 24453.482    0.002 learner.py:42(Qlearn)
                3286546   17.931    0.000 16719.800    0.005 game.py:35(step)
                3286546   21.812    0.000 15898.825    0.005 layers.py:448(step)
        346056228/36732148 1382.881    0.000 12728.648    0.000 module.py:866(_call_impl)
               26872522   73.856    0.000 11944.369    0.000 network.py:24(forward)
               26872522  362.030    0.000 11702.337    0.000 container.py:117(forward)
                3286546  354.210    0.000 11368.109    0.003 agent.py:54(_learn)
                3286546 1103.133    0.000 11168.637    0.003 agent.py:204(counterfact)
                3286546  274.303    0.000 10805.345    0.003 layers.py:17(step)
                3286546  351.646    0.000 10526.003    0.003 agent.py:196(_learn)
              328625443  775.331    0.000 10498.291    0.000 layer.py:84(move)
                9859626   88.616    0.000 10322.747    0.001 optimizer.py:84(wrapper)
                9859626   43.157    0.000 9920.283    0.001 grad_mode.py:24(decorate_context)
                9859626  295.624    0.000 9785.222    0.001 adam.py:55(step)
                9859626 2015.665    0.000 9167.698    0.001 _functional.py:53(adam)
                3286546   99.724    0.000 7459.637    0.002 agent.py:115(_learn)
                3286546 3993.027    0.001 7451.652    0.002 replaybuffer.py:28(teleporter_save_data)
                8504721  234.804    0.000 6159.886    0.001 agent.py:49(__call__)
                9859626   42.395    0.000 6125.651    0.001 tensor.py:195(backward)
                9859626   38.992    0.000 6081.693    0.001 __init__.py:68(backward)
              328625443  941.733    0.000 6075.007    0.000 layers.py:465(check)
                9859626 5822.050    0.001 5822.050    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               52855096 5642.906    0.000 5642.906    0.000 {built-in method tensor}
                3286546 3123.547    0.001 5489.377    0.002 agent.py:86(interveen)
               45286015   30.544    0.000 5423.348    0.000 game.py:31(board)
                3286546 3951.431    0.001 5148.452    0.002 replaybuffer.py:22(sample_data)
                3286547  351.051    0.000 5041.684    0.002 layers.py:419(update)
                3286546 3312.295    0.001 4361.979    0.001 replaybuffer.py:49(sample_data)
               65730930 2551.811    0.000 4306.560    0.000 layer.py:129(update)
               53745044  122.758    0.000 4257.706    0.000 conv.py:398(forward)
               53745044   72.086    0.000 4079.331    0.000 conv.py:390(_conv_forward)
               53745044 4007.245    0.000 4007.245    0.000 {built-in method conv2d}
               74044474  148.817    0.000 3402.323    0.000 linear.py:93(forward)
               74044474   58.577    0.000 3180.950    0.000 functional.py:1737(linear)
              243726141 3141.955    0.000 3141.955    0.000 {built-in method clone}
              328607959  537.216    0.000 3113.066    0.000 layers.py:459(isFree)
               74044474 3106.636    0.000 3106.636    0.000 {built-in method torch._C._nn.linear}
                1935095   44.893    0.000 2920.775    0.002 agent.py:168(choose_action)
             2891731717 2149.201    0.000 2575.850    0.000 layer.py:81(isFree)
                3286546 1531.848    0.000 2551.805    0.001 agent.py:67(modify)
               47943213 1962.279    0.000 1962.279    0.000 {built-in method cat}
              184046336 1873.722    0.000 1873.722    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              100916996   78.291    0.000 1870.273    0.000 activation.py:713(forward)
              100916996   83.890    0.000 1791.982    0.000 functional.py:1364(leaky_relu)
               11791267   81.469    0.000 1717.631    0.000 agent.py:59(modify_board)
              100916996 1690.166    0.000 1690.166    0.000 {built-in method torch._C._nn.leaky_relu}
                3286534   62.348    0.000 1656.926    0.001 agent.py:164(__call__)
              184046336 1637.910    0.000 1637.910    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                3286546   58.328    0.000 1558.621    0.000 agent.py:110(__call__)
                9859626  229.562    0.000 1411.518    0.000 optimizer.py:189(zero_grad)
             5592761786  943.538    0.000 1316.600    0.000 enum.py:646(__hash__)
                3912369   43.244    0.000 1230.237    0.000 layers.py:469(restart)
              328625443  721.743    0.000 1117.391    0.000 layers.py:270(check)
               11791267 1099.347    0.000 1099.347    0.000 {built-in method torch._C._nn.one_hot}
              328654700  163.864    0.000 1066.290    0.000 {built-in method builtins.all}
               92023168 1023.589    0.000 1023.589    0.000 {method 'add' of 'torch._C._TensorBase' objects}
             1243707903 1016.166    0.000 1016.166    0.000 layer.py:124(elements)
              328625443  593.849    0.000  993.846    0.000 layers.py:233(check)
                3286546   75.427    0.000  967.574    0.000 replaybuffer.py:18(stacker)
                3286546  393.667    0.000  940.714    0.000 replaybuffer.py:55(CF_save_data)
             2016968457  480.689    0.000  939.398    0.000 layers.py:425(<genexpr>)
               92023168  904.178    0.000  904.178    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              328625443  674.025    0.000  871.556    0.000 layers.py:67(check)
               92023168  848.917    0.000  848.917    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               92023168  838.223    0.000  838.223    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                3912369   20.592    0.000  830.950    0.000 level.py:8(__init__)
                3286534   70.066    0.000  828.867    0.000 replaybuffer.py:45(stacker)
              258803942  780.960    0.000  780.960    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                3912369  124.594    0.000  684.602    0.000 levels.py:199(generate)
                3286546  403.456    0.000  668.186    0.000 collector.py:54(collect)
               92023168  647.357    0.000  647.357    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
             7647180216  647.281    0.000  647.281    0.000 layer.py:77(positions)
              328625443  488.343    0.000  645.245    0.000 layers.py:56(check)
                8504721  232.537    0.000  640.311    0.000 exploration.py:53(softmaxer)
        7948214794/7948214791  500.134    0.000  564.425    0.000 {built-in method builtins.len}
              644162260  418.568    0.000  520.375    0.000 tensor.py:906(grad)
                1935095  482.969    0.000  511.929    0.000 agent.py:179(convert_values)
              328625443  318.694    0.000  503.016    0.000 layers.py:294(check)
               14397830  188.190    0.000  496.256    0.000 random.py:315(sample)
              328625443  315.976    0.000  494.145    0.000 layers.py:257(check)
                9859626   14.045    0.000  475.962    0.000 loss.py:527(forward)
                9859626   35.997    0.000  461.917    0.000 functional.py:2898(mse_loss)
                7824738   54.064    0.000  442.573    0.000 level.py:41(notUsed)
                9859639  436.951    0.000  436.951    0.000 {built-in method nonzero}
              328625443  286.728    0.000  424.074    0.000 layers.py:42(check)
             5592799225  373.069    0.000  373.069    0.000 {built-in method builtins.hash}
               39123690   49.998    0.000  344.179    0.000 layer.py:58(restart)
              340242606  232.149    0.000  328.000    0.000 layer.py:104(remove)
               53745044   42.484    0.000  317.879    0.000 flatten.py:39(forward)
                9859626  304.273    0.000  304.273    0.000 {built-in method torch._C._nn.mse_loss}
              557712381  220.235    0.000  301.844    0.000 layer.py:108(add)
               19719276  282.397    0.000  282.397    0.000 {built-in method sum}
               53745044  275.395    0.000  275.395    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                9860804  275.175    0.000  275.175    0.000 {built-in method max}
              433674769  182.321    0.000  267.487    0.000 random.py:250(_randbelow_with_getrandbits)
              146898707  176.595    0.000  258.540    0.000 layers.py:100(isDone)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-3>
Subject: Job 9496005: <causal4_CF_convert0_2_0> in cluster <dcc> Done

Job <causal4_CF_convert0_2_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon Apr  5 20:00:35 2021
Job was executed on host(s) <n-62-20-3>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon Apr  5 20:43:59 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Apr  5 20:43:59 2021
Terminated at Tue Apr  6 20:39:24 2021
Results reported at Tue Apr  6 20:39:24 2021

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

    CPU time :                                   85899.48 sec.
    Max Memory :                                 9799 MB
    Average Memory :                             6664.83 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               6585.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86125 sec.
    Turnaround time :                            88729 sec.

The output (if any) is above this job summary.

