
# Parameters

    Name :                      Coconuts_Conver4_3counterfactsNOCRASH-2
    Main :                      CFagent
    Level :                     Levels.Coconuts
    Failed actions chance :     0
    Use model :                 True
    Depth :                     3
    Model explore :             1000000
    Samples :                   5
    Hours :                     24.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.UCB1
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
    Layer greendown :           True
    Layer greenup :             True
    Layer greenstar :           True
    Layer yellowstar :          True
    Layer bluestar :            True
    Layer coconut :             True
    Layer monster :             True
    Layer greencross :          True
    Layer bluecross :           True
    Layer redcross :            True
    Layer purplecross :         True
    Layer super1 :              True
    Layer super2 :              True
    Layer super3 :              True
    Layer super4 :              True
    Layer super5 :              True
    Layer super6 :              True
    Layer super7 :              True
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                4
    Counterfacts :              3
    Topn :                      5
    Random counterfacts :       False
    Num :                       2
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      68898521499 function calls (68517759752 primitive calls) in 86121.28 seconds

##    Ordered by: cumulative time
   List reduced from 511 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86121.284 86121.284 {built-in method builtins.exec}
                      1    4.215    4.215 86121.284 86121.284 <string>:1(<module>)
                      1  364.033  364.033 86117.069 86117.069 main.py:80(CFagent)
               10328538   39.379    0.000 23931.803    0.002 agent.py:29(learn)
               10328538  606.227    0.000 19435.375    0.002 learner.py:42(Qlearn)
                3442846   14.120    0.000 18278.783    0.005 game.py:42(step)
                3442846 1366.069    0.000 18086.866    0.005 agent.py:212(counterfact)
                3442846   19.250    0.000 17600.447    0.005 layers.py:827(step)
        423966214/43206158 1600.589    0.000 12999.511    0.000 module.py:866(_call_impl)
               32877620   87.139    0.000 12238.911    0.000 network.py:28(forward)
                3442846  301.725    0.000 12199.850    0.004 layers.py:17(step)
               32877620  388.699    0.000 11948.853    0.000 container.py:117(forward)
              343553763 1210.179    0.000 11869.790    0.000 layer.py:106(move)
                3442846  349.823    0.000 9302.563    0.003 agent.py:54(_learn)
                3442846  346.860    0.000 8532.526    0.002 agent.py:204(_learn)
               97849893 7758.117    0.000 7758.117    0.000 {built-in method tensor}
               89936846   46.838    0.000 7597.836    0.000 game.py:38(board)
               10328538   81.959    0.000 7545.014    0.001 optimizer.py:84(wrapper)
               10328538   44.125    0.000 7174.409    0.001 grad_mode.py:24(decorate_context)
              343553763 1209.354    0.000 7155.525    0.000 layers.py:844(check)
               10328538  296.740    0.000 7039.836    0.001 adam.py:55(step)
               11272112  279.520    0.000 6805.290    0.001 agent.py:49(__call__)
               10328538 1453.902    0.000 6405.384    0.001 _functional.py:53(adam)
                3442846  101.723    0.000 6031.701    0.002 agent.py:117(_learn)
                3442846 4850.543    0.001 5882.092    0.002 replaybuffer.py:22(sample_data)
                3442846 4750.806    0.001 5745.459    0.002 replaybuffer.py:67(sample_data)
                4391278   80.193    0.000 5573.194    0.001 agent.py:176(choose_action)
                3442847  469.798    0.000 5354.285    0.002 layers.py:793(update)
               96399681 2986.209    0.000 5258.696    0.000 layer.py:159(update)
               10328538   39.845    0.000 5086.416    0.000 tensor.py:195(backward)
               10328538   38.570    0.000 5045.202    0.000 __init__.py:68(backward)
               10328538 4814.977    0.000 4814.977    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
               65755240  141.854    0.000 4419.759    0.000 conv.py:398(forward)
               65755240  100.318    0.000 4212.362    0.000 conv.py:390(_conv_forward)
                3442846 2040.093    0.001 4122.702    0.001 agent.py:88(interveen)
                3442846 2343.459    0.001 4118.133    0.001 replaybuffer.py:28(teleporter_save_data)
               65755240 4112.044    0.000 4112.044    0.000 {built-in method conv2d}
               91747168  184.018    0.000 3381.677    0.000 linear.py:93(forward)
               91747168   72.893    0.000 3107.134    0.000 functional.py:1737(linear)
               91747168 3017.950    0.000 3017.950    0.000 {built-in method torch._C._nn.linear}
              343553763  491.018    0.000 2642.128    0.000 layers.py:838(isFree)
                3442846 1533.745    0.000 2343.123    0.001 agent.py:67(modify)
              343553763 1536.608    0.000 2154.991    0.000 layers.py:471(check)
             2245239188 1823.591    0.000 2151.110    0.000 layer.py:103(isFree)
              343553763 1315.151    0.000 1822.835    0.000 layers.py:77(check)
               14714958   86.889    0.000 1785.725    0.000 agent.py:59(modify_board)
              124624788   99.759    0.000 1775.904    0.000 activation.py:713(forward)
               49143418 1755.056    0.000 1755.056    0.000 {built-in method cat}
              124624788   94.959    0.000 1676.144    0.000 functional.py:1364(leaky_relu)
              177053312 1636.225    0.000 1636.225    0.000 {built-in method clone}
                2120108   24.715    0.000 1583.225    0.001 layers.py:849(restart)
              124624788 1562.153    0.000 1562.153    0.000 {built-in method torch._C._nn.leaky_relu}
                3442846   57.449    0.000 1471.394    0.000 agent.py:172(__call__)
             5685470792  990.220    0.000 1429.345    0.000 enum.py:646(__hash__)
                3442846   53.878    0.000 1389.665    0.000 agent.py:112(__call__)
                2120108   13.042    0.000 1352.497    0.001 level.py:8(__init__)
              192799376 1256.926    0.000 1256.926    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                2120108   84.958    0.000 1224.911    0.001 levels.py:277(generate)
             1167579494 1219.897    0.000 1219.897    0.000 layer.py:154(elements)
               14714958 1171.508    0.000 1171.508    0.000 {built-in method torch._C._nn.one_hot}
                4391278  959.907    0.000 1115.321    0.000 agent.py:187(convert_values)
               10328538  202.552    0.000 1114.193    0.000 optimizer.py:189(zero_grad)
              192799376 1114.162    0.000 1114.162    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              352493129  261.147    0.000 1110.939    0.000 {built-in method builtins.any}
               18910163  176.827    0.000 1069.016    0.000 level.py:41(notUsed)
              343553763  700.548    0.000  906.780    0.000 layers.py:62(check)
                3442846  722.746    0.000  884.138    0.000 replaybuffer.py:73(CF_save_data)
             2737316736  699.161    0.000  849.792    0.000 layers.py:809(<genexpr>)
        12038296790/12038296787  715.344    0.000  796.284    0.000 {built-in method builtins.len}
                3442846   65.212    0.000  788.910    0.000 replaybuffer.py:18(stacker)
                3442846   66.623    0.000  761.727    0.000 replaybuffer.py:63(stacker)
               96399688  740.513    0.000  740.513    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               11272112  251.274    0.000  676.515    0.000 exploration.py:53(softmaxer)
             7413866679  651.794    0.000  651.794    0.000 layer.py:99(positions)
               96399688  635.087    0.000  635.087    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               96399688  590.929    0.000  590.929    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               96399688  590.439    0.000  590.439    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              674797900  423.304    0.000  524.900    0.000 tensor.py:906(grad)
               18910163   15.770    0.000  512.478    0.000 level.py:38(elementsIn)
                3442846  286.148    0.000  491.023    0.000 collector.py:46(collect)
                6885692  177.848    0.000  462.735    0.000 random.py:315(sample)
              343553763  299.608    0.000  453.523    0.000 layers.py:48(check)
               96399688  440.115    0.000  440.115    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
             5685510023  439.131    0.000  439.131    0.000 {built-in method builtins.hash}
               10328538   14.338    0.000  418.849    0.000 loss.py:527(forward)
              369364495  293.959    0.000  409.515    0.000 layer.py:134(remove)
               10328538   37.873    0.000  404.510    0.000 functional.py:2898(mse_loss)
              344284700   65.144    0.000  397.476    0.000 {built-in method builtins.all}
              772856139  175.758    0.000  372.546    0.000 layers.py:799(<genexpr>)
              195211116  369.015    0.000  369.015    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              343553763  249.811    0.000  364.012    0.000 layers.py:23(check)
               18910163  166.659    0.000  333.676    0.000 level.py:39(<listcomp>)
               96399681  328.145    0.000  328.145    0.000 layer.py:171(<listcomp>)
               65755240   54.803    0.000  305.303    0.000 flatten.py:39(forward)
              488074977  208.586    0.000  280.268    0.000 layer.py:138(add)
               96399681  277.919    0.000  277.919    0.000 layer.py:172(<listcomp>)
               65755240  250.499    0.000  250.499    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                6885694  250.203    0.000  250.203    0.000 {built-in method nonzero}
               10328538  245.502    0.000  245.502    0.000 {built-in method torch._C._nn.mse_loss}
               10330009  227.860    0.000  227.860    0.000 {built-in method max}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9624183: <Coconuts_Conver4_3counterfactsNOCRASH_2> in cluster <dcc> Done

Job <Coconuts_Conver4_3counterfactsNOCRASH_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun May  9 01:29:17 2021
Job was executed on host(s) <n-62-20-2>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon May 10 01:24:44 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon May 10 01:24:44 2021
Terminated at Tue May 11 01:20:22 2021
Results reported at Tue May 11 01:20:22 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
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

python main.py $MYARGS


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   85898.09 sec.
    Max Memory :                                 9616 MB
    Average Memory :                             6346.76 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               6768.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86139 sec.
    Turnaround time :                            172265 sec.

The output (if any) is above this job summary.

