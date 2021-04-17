
# Parameters

    Name :                      ReTest5-0
    Main :                      CFagentv2
    Level :                     Levels.Causal3
    Failed actions chance :     0.0
    Hours :                     12.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.UCB1
    Network1 :                  Networks.Teleporter
    K1 :                        2000000.0
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
    K2 :                        500000.0
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
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                3
    Counterfacts :              1
    Topn :                      5
    Random counterfacts :       True
    Minutes used :              715 minutes.
    Hours used :                11 hours.

# Profiling


      27567172594 function calls (27434466190 primitive calls) in 42914.43 seconds

##    Ordered by: cumulative time
   List reduced from 523 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 42914.429 42914.429 {built-in method builtins.exec}
                      1    5.412    5.412 42914.429 42914.429 <string>:1(<module>)
                      1  182.683  182.683 42909.016 42909.016 main.py:105(CFagentv2)
                4619796   18.297    0.000 13876.971    0.003 agent.py:29(learn)
                4617753  347.196    0.000 11533.530    0.002 learner.py:42(Qlearn)
                1539932    8.236    0.000 7156.235    0.005 game.py:41(step)
                1539932   10.305    0.000 6794.788    0.004 layers.py:718(step)
                6157685   53.626    0.000 5952.518    0.001 optimizer.py:84(wrapper)
        151213731/18509111  658.688    0.000 5781.231    0.000 module.py:866(_call_impl)
                6157685   27.598    0.000 5701.484    0.001 grad_mode.py:24(decorate_context)
                6157685  181.215    0.000 5617.360    0.001 adam.py:55(step)
                1539932  163.692    0.000 5356.640    0.003 agent.py:54(_learn)
                6157685 1159.063    0.000 5252.562    0.001 _functional.py:53(adam)
               12351426  166.763    0.000 5222.778    0.000 container.py:117(forward)
                1539932  160.114    0.000 4969.267    0.003 agent.py:202(_learn)
               10792632   30.197    0.000 4840.386    0.000 network.py:24(forward)
                1539932  136.609    0.000 4294.750    0.003 layers.py:17(step)
              153788123  240.246    0.000 4144.874    0.000 layer.py:98(move)
                6157685   25.113    0.000 3631.762    0.001 tensor.py:195(backward)
                6157685   23.753    0.000 3605.758    0.001 __init__.py:68(backward)
                1539932   45.553    0.000 3523.308    0.002 agent.py:117(_learn)
                6157685 3442.214    0.001 3442.214    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                1539932 2841.814    0.002 3231.843    0.002 replaybuffer.py:85(sample_data)
                1539932  543.413    0.000 3154.075    0.002 agent.py:236(counterfact2)
                1539932   26.384    0.000 3098.593    0.002 simulator.py:50(learn)
                1539932  171.342    0.000 3072.209    0.002 simulator.py:23(learn)
                1539933  221.317    0.000 2474.732    0.002 layers.py:684(update)
                1539932 1922.548    0.001 2437.190    0.002 replaybuffer.py:22(sample_data)
              153788123  516.869    0.000 2436.724    0.000 layers.py:735(check)
                3078196   83.423    0.000 2262.741    0.001 agent.py:49(__call__)
                1539932 1559.172    0.001 2055.604    0.001 replaybuffer.py:52(sample_data)
               26261646   58.504    0.000 2037.744    0.000 conv.py:398(forward)
               26261646   36.458    0.000 1950.453    0.000 conv.py:390(_conv_forward)
               26261646 1913.995    0.000 1913.995    0.000 {built-in method conv2d}
                1539932  796.181    0.001 1904.937    0.001 agent.py:88(interveen)
               20859837 1884.931    0.000 1884.931    0.000 {built-in method tensor}
               17304382   11.757    0.000 1778.316    0.000 game.py:37(board)
               24638920  896.360    0.000 1576.021    0.000 layer.py:167(NoRock_update)
                1539932  813.530    0.001 1536.598    0.001 replaybuffer.py:28(teleporter_save_data)
               29298032   59.083    0.000 1370.810    0.000 linear.py:93(forward)
                1539932  896.537    0.001 1349.114    0.001 agent.py:67(modify)
               29298032   24.947    0.000 1279.692    0.000 functional.py:1737(linear)
              153788123  206.751    0.000 1269.274    0.000 layers.py:729(isFree)
               29298032 1248.197    0.000 1248.197    0.000 {built-in method torch._C._nn.linear}
               26185823 1141.850    0.000 1141.850    0.000 {built-in method cat}
              104674516 1077.722    0.000 1077.722    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              982983162  909.432    0.000 1062.523    0.000 layer.py:95(isFree)
              104674516  929.918    0.000  929.918    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               61680127  848.180    0.000  848.180    0.000 {built-in method clone}
                6157685  135.380    0.000  834.250    0.000 optimizer.py:189(zero_grad)
               43208252   36.545    0.000  813.856    0.000 activation.py:713(forward)
                1537889   30.625    0.000  795.499    0.001 agent.py:171(__call__)
               43208252   39.827    0.000  777.311    0.000 functional.py:1364(leaky_relu)
                1539932  631.760    0.000  769.480    0.000 replaybuffer.py:91(simulator_save_data)
                1539932   30.134    0.000  744.791    0.000 agent.py:112(__call__)
               43208252  730.106    0.000  730.106    0.000 {built-in method torch._C._nn.leaky_relu}
                1539932  539.005    0.000  717.831    0.000 replaybuffer.py:58(CF_save_data)
                4618128   32.229    0.000  672.964    0.000 agent.py:59(modify_board)
               52337258  588.863    0.000  588.863    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                6176922  588.480    0.000  588.480    0.000 {built-in method torch._C._nn.one_hot}
                1880656   20.745    0.000  577.646    0.000 layers.py:740(restart)
             2237307954  376.139    0.000  547.930    0.000 enum.py:646(__hash__)
              153652577  126.278    0.000  527.999    0.000 {built-in method builtins.any}
               52337258  515.703    0.000  515.703    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                1558794    7.107    0.000  507.842    0.000 simulator.py:20(boardforward)
              153788123  331.529    0.000  507.489    0.000 layers.py:246(check)
               52337258  484.588    0.000  484.588    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               52337258  481.320    0.000  481.320    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              153788123  270.374    0.000  443.767    0.000 layers.py:286(check)
                1880656    9.516    0.000  408.686    0.000 level.py:8(__init__)
                1539932   28.418    0.000  406.554    0.000 replaybuffer.py:18(stacker)
             1369013796  330.759    0.000  401.721    0.000 layers.py:700(<genexpr>)
              467194760  397.699    0.000  397.699    0.000 layer.py:146(elements)
                1537889   29.494    0.000  393.189    0.000 replaybuffer.py:48(stacker)
               52337258  376.663    0.000  376.663    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                8381108  133.112    0.000  341.715    0.000 random.py:315(sample)
                1880656   39.761    0.000  322.978    0.000 levels.py:164(generate)
                1539932  191.351    0.000  310.097    0.000 collector.py:46(collect)
              153993300   47.463    0.000  306.368    0.000 {built-in method builtins.all}
                6157685    9.234    0.000  304.985    0.000 loss.py:527(forward)
              366360896  245.273    0.000  303.168    0.000 tensor.py:906(grad)
                6157685   24.575    0.000  295.751    0.000 functional.py:2898(mse_loss)
                1539932   24.374    0.000  284.793    0.000 replaybuffer.py:81(stacker)
              541546156  131.799    0.000  277.395    0.000 layers.py:690(<genexpr>)
        3479104990/3479104986  230.332    0.000  260.608    0.000 {built-in method builtins.len}
              153788123  163.543    0.000  252.710    0.000 layers.py:313(check)
                3078196   86.046    0.000  244.997    0.000 exploration.py:53(softmaxer)
             2765624463  239.521    0.000  239.521    0.000 layer.py:91(positions)
                3761312   32.887    0.000  235.040    0.000 level.py:41(notUsed)
              153788123  144.929    0.000  229.300    0.000 layers.py:273(check)
               69394938  223.180    0.000  223.180    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                1539932   41.513    0.000  220.210    0.000 agent.py:277(counterfact_check)
               15158182  208.795    0.000  208.795    0.000 {method 'item' of 'torch._C._TensorBase' objects}
              153788123  139.206    0.000  207.898    0.000 layers.py:48(check)
                6157685  196.692    0.000  196.692    0.000 {built-in method torch._C._nn.mse_loss}
                4966066  194.702    0.000  194.702    0.000 {built-in method nonzero}
               12319456  180.893    0.000  180.893    0.000 {built-in method sum}
             2237325829  171.795    0.000  171.795    0.000 {built-in method builtins.hash}
              153788123  108.965    0.000  160.485    0.000 layers.py:23(check)
              266400000  105.786    0.000  156.146    0.000 random.py:250(_randbelow_with_getrandbits)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-5>
Subject: Job 9512496: <ReTest5_0> in cluster <dcc> Done

Job <ReTest5_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Tue Apr 13 13:40:47 2021
Job was executed on host(s) <n-62-20-5>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Tue Apr 13 21:01:53 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue Apr 13 21:01:53 2021
Terminated at Wed Apr 14 08:57:15 2021
Results reported at Wed Apr 14 08:57:15 2021

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

    CPU time :                                   42805.19 sec.
    Max Memory :                                 7397 MB
    Average Memory :                             5444.86 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               8987.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   42922 sec.
    Turnaround time :                            69388 sec.

The output (if any) is above this job summary.

