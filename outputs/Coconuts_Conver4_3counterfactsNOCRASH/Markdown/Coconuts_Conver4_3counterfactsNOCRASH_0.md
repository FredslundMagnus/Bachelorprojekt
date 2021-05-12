
# Parameters

    Name :                      Coconuts_Conver4_3counterfactsNOCRASH-0
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
    Num :                       0
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      63186905454 function calls (62851932555 primitive calls) in 86115.50 seconds

##    Ordered by: cumulative time
   List reduced from 512 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86115.495 86115.495 {built-in method builtins.exec}
                      1    4.808    4.808 86115.495 86115.495 <string>:1(<module>)
                      1  376.507  376.507 86110.687 86110.687 main.py:80(CFagent)
                9270177   37.373    0.000 23075.758    0.002 agent.py:29(learn)
                9270168  580.397    0.000 18748.732    0.002 learner.py:42(Qlearn)
                3090059   15.573    0.000 18194.175    0.006 game.py:42(step)
                3090059   20.080    0.000 17545.200    0.006 layers.py:827(step)
                3090059 1290.371    0.000 16778.186    0.005 agent.py:212(counterfact)
        373185663/38214455 1528.425    0.000 12106.988    0.000 module.py:866(_call_impl)
                3090059  295.823    0.000 11841.443    0.004 layers.py:17(step)
              308395680 1185.963    0.000 11517.924    0.000 layer.py:106(move)
               28944287   79.842    0.000 11372.795    0.000 network.py:28(forward)
               28944287  377.891    0.000 11097.169    0.000 container.py:117(forward)
                3090059  341.048    0.000 8984.683    0.003 agent.py:54(_learn)
                3090059  338.036    0.000 8197.108    0.003 agent.py:204(_learn)
                9270168   80.627    0.000 7351.249    0.001 optimizer.py:84(wrapper)
                3090059 6290.639    0.002 7286.402    0.002 replaybuffer.py:22(sample_data)
               87038993 7206.316    0.000 7206.316    0.000 {built-in method tensor}
               79904224   44.591    0.000 7045.784    0.000 game.py:38(board)
                9270168   43.107    0.000 6994.065    0.001 grad_mode.py:24(decorate_context)
              308395680 1187.089    0.000 6907.051    0.000 layers.py:844(check)
                3090059 5940.325    0.002 6886.877    0.002 replaybuffer.py:67(sample_data)
                9270168  302.204    0.000 6856.783    0.001 adam.py:55(step)
                9834855  266.948    0.000 6319.727    0.001 agent.py:49(__call__)
                9270168 1418.625    0.000 6234.943    0.001 _functional.py:53(adam)
                3090059   97.467    0.000 5831.469    0.002 agent.py:117(_learn)
                3090060  462.765    0.000 5654.545    0.002 layers.py:793(update)
               86521645 3019.330    0.000 5245.526    0.000 layer.py:159(update)
                9270168   38.390    0.000 4906.808    0.001 tensor.py:195(backward)
                3659155   70.278    0.000 4886.281    0.001 agent.py:176(choose_action)
                9270168   40.135    0.000 4867.156    0.001 __init__.py:68(backward)
                9270168 4642.206    0.001 4642.206    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3090059 2388.582    0.001 4095.332    0.001 replaybuffer.py:28(teleporter_save_data)
               57888574  129.176    0.000 4092.231    0.000 conv.py:398(forward)
                3090059 2069.663    0.001 4054.755    0.001 agent.py:88(interveen)
               57888574   79.285    0.000 3898.719    0.000 conv.py:390(_conv_forward)
               57888574 3819.434    0.000 3819.434    0.000 {built-in method conv2d}
               80652743  169.933    0.000 3125.199    0.000 linear.py:93(forward)
               80652743   69.241    0.000 2869.819    0.000 functional.py:1737(linear)
               80652743 2783.702    0.000 2783.702    0.000 {built-in method torch._C._nn.linear}
              308395680  499.529    0.000 2647.148    0.000 layers.py:838(isFree)
                3090059 1495.323    0.000 2279.764    0.001 agent.py:67(modify)
             2026812119 1843.068    0.000 2147.618    0.000 layer.py:103(isFree)
              308395680 1507.443    0.000 2093.764    0.000 layers.py:471(check)
              308395680 1262.395    0.000 1738.652    0.000 layers.py:77(check)
               12924914   86.568    0.000 1684.646    0.000 agent.py:59(modify_board)
              109597030   88.260    0.000 1646.521    0.000 activation.py:713(forward)
               43825459 1644.776    0.000 1644.776    0.000 {built-in method cat}
              156066853 1564.921    0.000 1564.921    0.000 {built-in method clone}
              109597030   94.010    0.000 1558.261    0.000 functional.py:1364(leaky_relu)
              109597030 1446.506    0.000 1446.506    0.000 {built-in method torch._C._nn.leaky_relu}
                3090050   59.919    0.000 1398.300    0.000 agent.py:172(__call__)
             5289344705  972.224    0.000 1380.485    0.000 enum.py:646(__hash__)
                1724643   23.706    0.000 1379.033    0.001 layers.py:849(restart)
                3090059   56.555    0.000 1333.559    0.000 agent.py:112(__call__)
              173043124 1229.853    0.000 1229.853    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
             1018220444 1196.383    0.000 1196.383    0.000 layer.py:154(elements)
                1724643   11.878    0.000 1174.671    0.001 level.py:8(__init__)
               12924914 1108.638    0.000 1108.638    0.000 {built-in method torch._C._nn.one_hot}
              173043124 1097.907    0.000 1097.907    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              316551533  253.756    0.000 1070.370    0.000 {built-in method builtins.any}
                1724643   73.386    0.000 1062.851    0.001 levels.py:277(generate)
                9270168  191.816    0.000 1056.358    0.000 optimizer.py:189(zero_grad)
                3659155  851.083    0.000  988.030    0.000 agent.py:187(convert_values)
              309006000   87.379    0.000  957.968    0.000 {built-in method builtins.all}
               15382537  156.356    0.000  926.830    0.000 level.py:41(notUsed)
              937274612  243.865    0.000  909.557    0.000 layers.py:799(<genexpr>)
              308395680  691.073    0.000  881.597    0.000 layers.py:62(check)
                3090059  685.902    0.000  829.823    0.000 replaybuffer.py:73(CF_save_data)
             2458250856  657.796    0.000  816.614    0.000 layers.py:809(<genexpr>)
        10944773142/10944773139  684.716    0.000  760.748    0.000 {built-in method builtins.len}
                3090059   65.304    0.000  750.380    0.000 replaybuffer.py:18(stacker)
                3090050   64.512    0.000  713.522    0.000 replaybuffer.py:63(stacker)
               86521562  702.147    0.000  702.147    0.000 {method 'add' of 'torch._C._TensorBase' objects}
             7421671439  688.977    0.000  688.977    0.000 layer.py:99(positions)
                9834855  236.547    0.000  634.450    0.000 exploration.py:53(softmaxer)
               86521562  617.961    0.000  617.961    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               86521562  573.452    0.000  573.452    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               86521562  572.677    0.000  572.677    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              279941440  361.010    0.000  521.774    0.000 layers.py:113(isDone)
              605651018  400.385    0.000  495.845    0.000 tensor.py:906(grad)
                3090059  276.739    0.000  469.812    0.000 collector.py:46(collect)
                6180118  182.430    0.000  467.111    0.000 random.py:315(sample)
               15382537   13.722    0.000  442.675    0.000 level.py:38(elementsIn)
              308395680  297.930    0.000  440.475    0.000 layers.py:48(check)
               86521562  417.441    0.000  417.441    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                9270168   15.234    0.000  410.068    0.000 loss.py:527(forward)
             5289380016  408.268    0.000  408.268    0.000 {built-in method builtins.hash}
                9270168   40.044    0.000  394.835    0.000 functional.py:2898(mse_loss)
              327203477  264.222    0.000  375.686    0.000 layer.py:134(remove)
              172081817  352.434    0.000  352.434    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              308395680  224.763    0.000  329.073    0.000 layers.py:23(check)
               86521645  328.215    0.000  328.215    0.000 layer.py:171(<listcomp>)
               15382537  140.744    0.000  286.349    0.000 level.py:39(<listcomp>)
               57888574   42.809    0.000  274.516    0.000 flatten.py:39(forward)
               86521645  266.096    0.000  266.096    0.000 layer.py:172(<listcomp>)
                6180120  244.840    0.000  244.840    0.000 {built-in method nonzero}
              423136833  174.456    0.000  243.346    0.000 layer.py:138(add)
                9270168  240.477    0.000  240.477    0.000 {built-in method torch._C._nn.mse_loss}
               57888574  231.706    0.000  231.706    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9624181: <Coconuts_Conver4_3counterfactsNOCRASH_0> in cluster <dcc> Done

Job <Coconuts_Conver4_3counterfactsNOCRASH_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun May  9 01:29:16 2021
Job was executed on host(s) <n-62-20-10>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun May  9 01:29:17 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun May  9 01:29:17 2021
Terminated at Mon May 10 01:24:40 2021
Results reported at Mon May 10 01:24:40 2021

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

    CPU time :                                   85907.24 sec.
    Max Memory :                                 9063 MB
    Average Memory :                             6071.73 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               7321.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86227 sec.
    Turnaround time :                            86124 sec.

The output (if any) is above this job summary.

