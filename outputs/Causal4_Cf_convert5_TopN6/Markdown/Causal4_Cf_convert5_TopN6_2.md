
# Parameters

    Name :                      Causal4_Cf_convert5_TopN6-2
    Main :                      CFagent
    Level :                     Levels.Causal4
    Failed actions chance :     0.0
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
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                5
    Counterfacts :              1
    Topn :                      6
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      73015327940 function calls (72707554365 primitive calls) in 86113.44 seconds

##    Ordered by: cumulative time
   List reduced from 513 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86113.439 86113.439 {built-in method builtins.exec}
                      1    3.948    3.948 86113.439 86113.439 <string>:1(<module>)
                      1  331.720  331.720 86109.491 86109.491 main.py:79(CFagent)
               10105047   37.517    0.000 29877.653    0.003 agent.py:29(learn)
               10105046  739.064    0.000 25034.885    0.002 learner.py:42(Qlearn)
                3368349   14.848    0.000 20083.975    0.006 game.py:41(step)
                3368349   20.990    0.000 19261.984    0.006 layers.py:718(step)
                3368349  283.385    0.000 12733.319    0.004 layers.py:17(step)
              336416560  907.085    0.000 12422.006    0.000 layer.py:98(move)
        344647370/36875486 1392.144    0.000 12403.432    0.000 module.py:866(_call_impl)
               26770440   81.112    0.000 11605.612    0.000 network.py:27(forward)
                3368349  314.535    0.000 11502.288    0.003 agent.py:54(_learn)
               26770440  368.184    0.000 11357.150    0.000 container.py:117(forward)
                3368349  310.995    0.000 10658.033    0.003 agent.py:202(_learn)
               10105046   85.682    0.000 10627.457    0.001 optimizer.py:84(wrapper)
               10105046   42.544    0.000 10216.693    0.001 grad_mode.py:24(decorate_context)
               10105046  296.554    0.000 10078.051    0.001 adam.py:55(step)
                3368349  873.907    0.000 9798.078    0.003 agent.py:210(counterfact)
               10105046 2047.944    0.000 9452.140    0.001 _functional.py:53(adam)
              336416560 1514.786    0.000 7678.056    0.000 layers.py:735(check)
                3368349   90.521    0.000 7658.106    0.002 agent.py:117(_learn)
                3368350  466.954    0.000 6481.173    0.002 layers.py:684(update)
               10105046   48.876    0.000 6331.670    0.001 tensor.py:195(backward)
               10105046   41.320    0.000 6281.238    0.001 __init__.py:68(backward)
               10105046 6015.152    0.001 6015.152    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                8322976  192.481    0.000 5872.865    0.001 agent.py:49(__call__)
                3368349 4687.751    0.001 5733.918    0.002 replaybuffer.py:22(sample_data)
               52713817 5527.302    0.000 5527.302    0.000 {built-in method tensor}
                3368349 4495.111    0.001 5523.854    0.002 replaybuffer.py:67(sample_data)
               44964607   28.700    0.000 5305.562    0.000 game.py:37(board)
                3368349 1848.030    0.001 4207.185    0.001 agent.py:88(interveen)
               53540880  116.979    0.000 4079.506    0.000 conv.py:398(forward)
               67366990 2267.941    0.000 3974.501    0.000 layer.py:151(update)
               53540880   69.704    0.000 3907.896    0.000 conv.py:390(_conv_forward)
               53540880 3838.192    0.000 3838.192    0.000 {built-in method conv2d}
                3368349 1878.020    0.001 3551.015    0.001 replaybuffer.py:28(teleporter_save_data)
               73574622  144.887    0.000 3297.527    0.000 linear.py:93(forward)
              336416560  667.773    0.000 3212.135    0.000 layers.py:729(isFree)
               73574622   59.447    0.000 3078.693    0.000 functional.py:1737(linear)
               73574622 3002.831    0.000 3002.831    0.000 {built-in method torch._C._nn.linear}
                3368349 1901.476    0.001 2874.816    0.001 agent.py:67(modify)
             3087138233 2079.553    0.000 2544.363    0.000 layer.py:95(isFree)
                1605721   37.979    0.000 2340.181    0.001 agent.py:175(choose_action)
              188627524 1936.372    0.000 1936.372    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              100345062   82.180    0.000 1812.189    0.000 activation.py:713(forward)
               45374810 1792.584    0.000 1792.584    0.000 {built-in method cat}
              100345062   84.385    0.000 1730.010    0.000 functional.py:1364(leaky_relu)
              188627524 1701.848    0.000 1701.848    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               11691325   78.731    0.000 1684.365    0.000 agent.py:59(modify_board)
                3368348   53.007    0.000 1651.289    0.000 agent.py:171(__call__)
              123465303 1634.536    0.000 1634.536    0.000 {built-in method clone}
              100345062 1628.727    0.000 1628.727    0.000 {built-in method torch._C._nn.leaky_relu}
                3368349   51.729    0.000 1549.430    0.000 agent.py:112(__call__)
             6245673935 1065.335    0.000 1534.506    0.000 enum.py:646(__hash__)
               10105046  240.519    0.000 1485.582    0.000 optimizer.py:189(zero_grad)
              337264652  325.568    0.000 1454.610    0.000 {built-in method builtins.any}
                3368349 1009.690    0.000 1296.264    0.000 replaybuffer.py:73(CF_save_data)
              336835000  244.069    0.000 1265.457    0.000 {built-in method builtins.all}
              336416560  911.555    0.000 1210.884    0.000 layers.py:77(check)
             3672859322  935.073    0.000 1129.042    0.000 layers.py:700(<genexpr>)
              336416560  736.155    0.000 1119.533    0.000 layers.py:246(check)
               94313762 1104.247    0.000 1104.247    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               11691325 1074.399    0.000 1074.399    0.000 {built-in method torch._C._nn.one_hot}
             3068691576  717.636    0.000 1059.664    0.000 layers.py:690(<genexpr>)
                2938698   36.166    0.000 1036.557    0.000 layers.py:740(restart)
              336416560  627.147    0.000 1013.450    0.000 layers.py:286(check)
             1062991582  951.081    0.000  951.081    0.000 layer.py:146(elements)
               94313762  899.200    0.000  899.200    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               94313762  876.513    0.000  876.513    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               94313762  858.411    0.000  858.411    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                3368349   65.464    0.000  813.958    0.000 replaybuffer.py:18(stacker)
                3368348   66.144    0.000  800.431    0.000 replaybuffer.py:63(stacker)
                2938698   17.352    0.000  735.971    0.000 level.py:8(__init__)
             8207215194  722.628    0.000  722.628    0.000 layer.py:91(positions)
                3368349  414.479    0.000  688.282    0.000 collector.py:46(collect)
               94313762  678.916    0.000  678.916    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              336416560  523.081    0.000  673.288    0.000 layers.py:62(check)
        8889505763/8889505760  565.320    0.000  629.905    0.000 {built-in method builtins.len}
                8322976  219.972    0.000  607.519    0.000 exploration.py:53(softmaxer)
                2938698   94.094    0.000  581.201    0.000 levels.py:199(generate)
              336416560  361.342    0.000  558.014    0.000 layers.py:273(check)
              660196418  442.645    0.000  548.836    0.000 tensor.py:906(grad)
              336416560  330.540    0.000  514.172    0.000 layers.py:313(check)
               12614094  187.763    0.000  491.683    0.000 random.py:315(sample)
               10105046   15.056    0.000  489.111    0.000 loss.py:527(forward)
               10105046   37.721    0.000  474.055    0.000 functional.py:2898(mse_loss)
             6245712270  469.178    0.000  469.178    0.000 {built-in method builtins.hash}
              336416560  291.936    0.000  432.055    0.000 layers.py:48(check)
              138524976  430.420    0.000  430.420    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                5877396   45.662    0.000  397.067    0.000 level.py:41(notUsed)
                1605721  360.973    0.000  384.894    0.000 agent.py:186(convert_values)
              336416560  232.590    0.000  340.175    0.000 layers.py:23(check)
               10105046  311.986    0.000  311.986    0.000 {built-in method torch._C._nn.mse_loss}
               53540880   37.868    0.000  305.797    0.000 flatten.py:39(forward)
               20210094  291.903    0.000  291.903    0.000 {built-in method sum}
                6736700  284.560    0.000  284.560    0.000 {built-in method nonzero}
             3713184943  273.973    0.000  273.973    0.000 {method 'random' of '_random.Random' objects}
               10106214  270.936    0.000  270.936    0.000 {built-in method max}
               53540880  267.929    0.000  267.929    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              286854896  189.028    0.000  261.269    0.000 layer.py:126(remove)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9533969: <Causal4_Cf_convert5_TopN6_2> in cluster <dcc> Done

Job <Causal4_Cf_convert5_TopN6_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun Apr 18 20:20:08 2021
Job was executed on host(s) <n-62-20-7>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed Apr 21 01:58:37 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed Apr 21 01:58:37 2021
Terminated at Thu Apr 22 01:53:57 2021
Results reported at Thu Apr 22 01:53:57 2021

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

    CPU time :                                   86094.20 sec.
    Max Memory :                                 3436 MB
    Average Memory :                             3401.29 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               12948.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86120 sec.
    Turnaround time :                            279229 sec.

The output (if any) is above this job summary.

