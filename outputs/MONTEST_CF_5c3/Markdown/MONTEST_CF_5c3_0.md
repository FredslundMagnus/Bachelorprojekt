
# Parameters

    Name :                      MONTEST_CF_5c3-0
    Main :                      CFagent
    Level :                     Levels.MonsterLevel
    Hours :                     22.0
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
    Cf convert :                5
    Counterfacts :              3
    Topn :                      7
    Minutes used :              1315 minutes.
    Hours used :                21 hours.

# Profiling


      54005973000 function calls (53684994469 primitive calls) in 78909.75 seconds

##    Ordered by: cumulative time
   List reduced from 506 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 78909.748 78909.748 {built-in method builtins.exec}
                      1    5.198    5.198 78909.748 78909.748 <string>:1(<module>)
                      1  209.312  209.312 78904.551 78904.551 main.py:95(CFagent)
                2161518 4349.029    0.002 23117.216    0.011 agent.py:217(counterfact)
                6484554   31.296    0.000 17191.777    0.003 agent.py:29(learn)
                2161518   12.908    0.000 16764.622    0.008 game.py:41(step)
                2161518   16.827    0.000 16311.065    0.008 layers.py:710(step)
                6484554  449.238    0.000 13835.281    0.002 learner.py:42(Qlearn)
        354929970/33953130 1469.452    0.000 11834.203    0.000 module.py:866(_call_impl)
               27468576   75.435    0.000 11198.419    0.000 network.py:24(forward)
               27468576  350.967    0.000 10935.886    0.000 container.py:117(forward)
                2161519  350.178    0.000 9326.164    0.004 layers.py:676(update)
                6169011  131.063    0.000 8507.188    0.001 agent.py:172(choose_action)
               10491975  328.971    0.000 6988.637    0.001 agent.py:49(__call__)
                2161518  215.676    0.000 6944.787    0.003 layers.py:17(step)
                2161518  300.113    0.000 6706.685    0.003 agent.py:54(_learn)
              191406229  602.847    0.000 6705.273    0.000 layer.py:98(move)
               81794583 6372.807    0.000 6372.807    0.000 {built-in method tensor}
               76707120   48.121    0.000 6272.665    0.000 game.py:37(board)
                2161518  294.289    0.000 6072.875    0.003 agent.py:209(_learn)
                6484554   67.928    0.000 5237.741    0.001 optimizer.py:84(wrapper)
                9102589   83.793    0.000 5141.855    0.001 layers.py:731(restart)
                2161518 2986.434    0.001 4983.580    0.002 replaybuffer.py:28(teleporter_save_data)
                6484554   37.159    0.000 4950.555    0.001 grad_mode.py:24(decorate_context)
                6484554  228.213    0.000 4836.768    0.001 adam.py:55(step)
               51876438 2982.232    0.000 4675.592    0.000 layer.py:151(update)
                2161518 3518.760    0.002 4411.535    0.002 replaybuffer.py:22(sample_data)
                6484554 1010.442    0.000 4376.671    0.001 _functional.py:53(adam)
                2161518   76.587    0.000 4364.603    0.002 agent.py:117(_learn)
                9102589   38.578    0.000 4345.949    0.000 level.py:8(__init__)
              191406229  430.071    0.000 4197.848    0.000 layers.py:727(check)
               54937152  123.211    0.000 4004.653    0.000 conv.py:398(forward)
                9102589  693.973    0.000 3965.082    0.000 levels.py:418(generate)
                2161518 3160.940    0.001 3941.261    0.002 replaybuffer.py:49(sample_data)
               54937152   84.874    0.000 3819.230    0.000 conv.py:390(_conv_forward)
                6484554   32.328    0.000 3747.069    0.001 tensor.py:195(backward)
               54937152 3734.357    0.000 3734.357    0.000 {built-in method conv2d}
                6484554   33.054    0.000 3713.688    0.001 __init__.py:68(backward)
                6484554 3529.410    0.001 3529.410    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2161518 2056.086    0.001 3458.415    0.002 agent.py:88(interveen)
               78082692  161.092    0.000 3100.431    0.000 linear.py:93(forward)
               78082692   66.159    0.000 2855.129    0.000 functional.py:1737(linear)
               78082692 2773.147    0.000 2773.147    0.000 {built-in method torch._C._nn.linear}
              191406229 1593.681    0.000 2700.386    0.000 layers.py:531(check)
               45512945  418.311    0.000 2591.381    0.000 level.py:41(notUsed)
              221979807 2145.896    0.000 2145.896    0.000 {built-in method clone}
                2161518 1231.956    0.001 1811.833    0.001 agent.py:67(modify)
               12653493   81.674    0.000 1698.324    0.000 agent.py:59(modify_board)
              105551268   90.399    0.000 1673.262    0.000 activation.py:713(forward)
                6169011 1399.130    0.000 1643.110    0.000 agent.py:183(convert_values)
              105551268   89.153    0.000 1582.863    0.000 functional.py:1364(leaky_relu)
               36430191 1552.855    0.000 1552.855    0.000 {built-in method cat}
                2161518  828.337    0.000 1523.244    0.001 replaybuffer.py:55(CF_save_data)
              191300123  254.242    0.000 1501.754    0.000 layers.py:721(isFree)
              217808033  167.541    0.000 1486.637    0.000 {built-in method builtins.any}
              105551268 1475.469    0.000 1475.469    0.000 {built-in method torch._C._nn.leaky_relu}
             1457893511  412.682    0.000 1319.632    0.000 layers.py:692(<genexpr>)
             5206523749  902.400    0.000 1296.401    0.000 enum.py:646(__hash__)
             1049271626 1072.928    0.000 1247.512    0.000 layer.py:95(isFree)
               12653493 1126.840    0.000 1126.840    0.000 {built-in method torch._C._nn.one_hot}
               45512945   36.810    0.000 1118.968    0.000 level.py:38(elementsIn)
                2161518   50.321    0.000 1049.313    0.000 agent.py:168(__call__)
             1803819317 1048.587    0.000 1048.587    0.000 layer.py:146(elements)
                2161518   48.115    0.000  974.962    0.000 agent.py:112(__call__)
              121045008  847.737    0.000  847.737    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              211323478  529.801    0.000  828.907    0.000 layers.py:568(isDead)
               49835981  298.374    0.000  758.277    0.000 random.py:315(sample)
                6484554  139.903    0.000  751.884    0.000 optimizer.py:189(zero_grad)
              121045008  742.895    0.000  742.895    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
             1941777789  720.920    0.000  720.920    0.000 level.py:32(inverse)
                2161518   52.780    0.000  717.755    0.000 replaybuffer.py:18(stacker)
               10491975  258.132    0.000  715.964    0.000 exploration.py:53(softmaxer)
              449927305  576.087    0.000  711.900    0.000 layer.py:126(remove)
               45512945  352.913    0.000  708.590    0.000 level.py:39(<listcomp>)
               54615534   75.569    0.000  692.287    0.000 layer.py:69(restart)
               54726399  662.053    0.000  662.053    0.000 {method 'item' of 'torch._C._TensorBase' objects}
              191406229  475.501    0.000  658.817    0.000 layers.py:71(check)
                2161518   50.616    0.000  612.219    0.000 replaybuffer.py:45(stacker)
              216151900   91.017    0.000  513.767    0.000 {built-in method builtins.all}
              677792609  348.103    0.000  505.065    0.000 random.py:250(_randbelow_with_getrandbits)
               60522504  499.726    0.000  499.726    0.000 {method 'add' of 'torch._C._TensorBase' objects}
        6077660565/6077660562  420.502    0.000  485.156    0.000 {built-in method builtins.len}
                9102689  240.264    0.000  473.977    0.000 layers.py:30(reset)
              258582726   92.692    0.000  473.527    0.000 random.py:244(randint)
              236794818  470.519    0.000  470.519    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              858795962  341.562    0.000  464.561    0.000 layer.py:130(add)
              915416606  265.615    0.000  450.023    0.000 layers.py:682(<genexpr>)
               60522504  448.362    0.000  448.362    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               60522504  405.477    0.000  405.477    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               60522504  405.152    0.000  405.152    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
             5206548644  394.006    0.000  394.006    0.000 {built-in method builtins.hash}
              258582726  162.399    0.000  380.835    0.000 random.py:200(randrange)
               45512945  229.428    0.000  373.568    0.000 {built-in method _functools.reduce}
             1966160678  365.249    0.000  365.249    0.000 enum.py:352(<genexpr>)
              191406229  250.988    0.000  357.999    0.000 layers.py:42(check)
              423657612  284.780    0.000  353.510    0.000 tensor.py:906(grad)
                2161518  200.190    0.000  340.254    0.000 collector.py:53(collect)
                6484554   13.598    0.000  337.504    0.000 loss.py:527(forward)
             3527963512  330.415    0.000  330.415    0.000 layer.py:91(positions)
                6484554   35.964    0.000  323.906    0.000 functional.py:2898(mse_loss)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-11>
Subject: Job 9507477: <MONTEST_CF_5c3_0> in cluster <dcc> Done

Job <MONTEST_CF_5c3_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sat Apr 10 02:36:49 2021
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sat Apr 10 03:42:56 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat Apr 10 03:42:56 2021
Terminated at Sun Apr 11 01:38:10 2021
Results reported at Sun Apr 11 01:38:10 2021

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

    CPU time :                                   78696.32 sec.
    Max Memory :                                 7598 MB
    Average Memory :                             5584.63 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               8786.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   78916 sec.
    Turnaround time :                            82881 sec.

The output (if any) is above this job summary.

