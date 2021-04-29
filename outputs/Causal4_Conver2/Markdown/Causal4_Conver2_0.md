
# Parameters

    Name :                      Causal4_Conver2-0
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
    Cf convert :                2
    Counterfacts :              1
    Topn :                      3
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      68273304723 function calls (67968454520 primitive calls) in 86109.10 seconds

##    Ordered by: cumulative time
   List reduced from 515 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86109.103 86109.103 {built-in method builtins.exec}
                      1    3.961    3.961 86109.103 86109.103 <string>:1(<module>)
                      1  311.460  311.460 86105.142 86105.142 main.py:79(CFagent)
                9828372   37.958    0.000 30408.711    0.003 agent.py:29(learn)
                9828363  748.638    0.000 25521.069    0.003 learner.py:42(Qlearn)
                3276124   15.006    0.000 19579.014    0.006 game.py:41(step)
                3276124   18.080    0.000 18767.173    0.006 layers.py:718(step)
        341172959/36324447 1437.980    0.000 12903.069    0.000 module.py:866(_call_impl)
                3276124  287.119    0.000 12385.446    0.004 layers.py:17(step)
               26496084   77.265    0.000 12096.180    0.000 network.py:27(forward)
              327199384  918.664    0.000 12069.037    0.000 layer.py:98(move)
               26496084  378.455    0.000 11848.286    0.000 container.py:117(forward)
                3276124  304.422    0.000 11698.083    0.004 agent.py:54(_learn)
                9828363   86.711    0.000 10890.806    0.001 optimizer.py:84(wrapper)
                3276124  302.023    0.000 10847.167    0.003 agent.py:204(_learn)
                9828363   42.549    0.000 10472.300    0.001 grad_mode.py:24(decorate_context)
                9828363  286.977    0.000 10329.811    0.001 adam.py:55(step)
                3276124  966.865    0.000 10287.771    0.003 agent.py:212(counterfact)
                9828363 2108.707    0.000 9711.903    0.001 _functional.py:53(adam)
                3276124   90.729    0.000 7804.443    0.002 agent.py:117(_learn)
              327199384 1488.390    0.000 7684.938    0.000 layers.py:735(check)
                9828363   49.161    0.000 6413.258    0.001 tensor.py:195(backward)
                9828363   42.915    0.000 6362.616    0.001 __init__.py:68(backward)
                3276125  481.960    0.000 6339.197    0.002 layers.py:684(update)
                8329230  196.132    0.000 6151.394    0.001 agent.py:49(__call__)
                9828363 6093.574    0.001 6093.574    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               51985396 5508.911    0.000 5508.911    0.000 {built-in method tensor}
               44439785   30.043    0.000 5285.218    0.000 game.py:37(board)
                3276124 3848.502    0.001 4884.321    0.001 replaybuffer.py:22(sample_data)
                3276124 3650.999    0.001 4672.880    0.001 replaybuffer.py:67(sample_data)
                3276124 2156.351    0.001 4567.757    0.001 agent.py:88(interveen)
               52992168  120.676    0.000 4246.223    0.000 conv.py:398(forward)
                3276124 2189.416    0.001 4175.235    0.001 replaybuffer.py:28(teleporter_save_data)
               52992168   73.964    0.000 4071.607    0.000 conv.py:390(_conv_forward)
               52992168 3997.643    0.000 3997.643    0.000 {built-in method conv2d}
               65522490 2259.245    0.000 3940.450    0.000 layer.py:151(update)
               72936004  152.198    0.000 3448.760    0.000 linear.py:93(forward)
               72936004   61.854    0.000 3213.250    0.000 functional.py:1737(linear)
               72936004 3135.902    0.000 3135.902    0.000 {built-in method torch._C._nn.linear}
                3276124 1949.676    0.001 2929.479    0.001 agent.py:67(modify)
              327199384  550.171    0.000 2847.212    0.000 layers.py:729(isFree)
                1786252   41.077    0.000 2782.483    0.002 agent.py:176(choose_action)
             2749288873 1884.383    0.000 2297.040    0.000 layer.py:95(isFree)
              183462764 1975.652    0.000 1975.652    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              140463013 1926.349    0.000 1926.349    0.000 {built-in method clone}
               99432088   78.497    0.000 1903.640    0.000 activation.py:713(forward)
               99432088   83.630    0.000 1825.142    0.000 functional.py:1364(leaky_relu)
               44366549 1800.633    0.000 1800.633    0.000 {built-in method cat}
              183462764 1747.261    0.000 1747.261    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               11605354   80.892    0.000 1729.231    0.000 agent.py:59(modify_board)
               99432088 1724.459    0.000 1724.459    0.000 {built-in method torch._C._nn.leaky_relu}
             6439697566 1157.411    0.000 1685.680    0.000 enum.py:646(__hash__)
                3276115   50.047    0.000 1677.319    0.001 agent.py:172(__call__)
                3276124   50.210    0.000 1574.362    0.000 agent.py:112(__call__)
                9828363  236.049    0.000 1501.281    0.000 optimizer.py:189(zero_grad)
              327548577  333.848    0.000 1477.456    0.000 {built-in method builtins.any}
                3276124 1096.366    0.000 1427.282    0.000 replaybuffer.py:73(CF_save_data)
              327199384  922.064    0.000 1222.595    0.000 layers.py:77(check)
                3340048   38.996    0.000 1202.544    0.000 layers.py:740(restart)
              327199384  738.066    0.000 1146.535    0.000 layers.py:286(check)
             3566996972  943.367    0.000 1143.608    0.000 layers.py:700(<genexpr>)
               91731382 1126.652    0.000 1126.652    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               11605354 1096.464    0.000 1096.464    0.000 {built-in method torch._C._nn.one_hot}
              327199384  625.716    0.000 1014.443    0.000 layers.py:246(check)
               91731382  930.831    0.000  930.831    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
             1108791397  925.375    0.000  925.375    0.000 layer.py:146(elements)
               91731382  897.459    0.000  897.459    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               91731382  895.157    0.000  895.157    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              327612500  103.337    0.000  889.137    0.000 {built-in method builtins.all}
                3340048   17.929    0.000  852.553    0.000 level.py:8(__init__)
              992107936  246.446    0.000  827.165    0.000 layers.py:690(<genexpr>)
                3276124   61.258    0.000  805.319    0.000 replaybuffer.py:18(stacker)
                3276115   62.100    0.000  794.163    0.000 replaybuffer.py:63(stacker)
             8411407504  737.002    0.000  737.002    0.000 layer.py:91(positions)
                3276124  424.609    0.000  704.719    0.000 collector.py:46(collect)
               91731382  697.109    0.000  697.109    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                3340048  108.311    0.000  679.192    0.000 levels.py:199(generate)
              327199384  490.809    0.000  654.409    0.000 layers.py:62(check)
        8673080854/8673080851  580.279    0.000  646.577    0.000 {built-in method builtins.len}
                8329230  234.280    0.000  636.034    0.000 exploration.py:53(softmaxer)
              327612500  367.149    0.000  555.529    0.000 layers.py:113(isDone)
              642119758  436.103    0.000  544.136    0.000 tensor.py:906(grad)
              327199384  348.090    0.000  541.984    0.000 layers.py:273(check)
             6439734893  528.275    0.000  528.275    0.000 {built-in method builtins.hash}
              327199384  333.376    0.000  523.089    0.000 layers.py:313(check)
                1786252  438.342    0.000  501.755    0.000 agent.py:187(convert_values)
               13232344  188.807    0.000  497.643    0.000 random.py:315(sample)
              155344482  495.313    0.000  495.313    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                9828363   14.587    0.000  491.772    0.000 loss.py:527(forward)
                9828363   36.315    0.000  477.185    0.000 functional.py:2898(mse_loss)
                6680096   54.768    0.000  463.590    0.000 level.py:41(notUsed)
              327199384  286.168    0.000  429.531    0.000 layers.py:48(check)
              327199384  232.511    0.000  347.168    0.000 layers.py:23(check)
                9828363  315.686    0.000  315.686    0.000 {built-in method torch._C._nn.mse_loss}
               52992168   35.203    0.000  311.332    0.000 flatten.py:39(forward)
               33400480   44.780    0.000  300.076    0.000 layer.py:69(restart)
               19656744  298.304    0.000  298.304    0.000 {built-in method sum}
             3612902508  291.092    0.000  291.092    0.000 {method 'random' of '_random.Random' objects}
                6552250  282.134    0.000  282.134    0.000 {built-in method nonzero}
              292633537  200.818    0.000  277.617    0.000 layer.py:126(remove)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9579163: <Causal4_Conver2_0> in cluster <dcc> Done

Job <Causal4_Conver2_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Tue Apr 27 02:44:06 2021
Job was executed on host(s) <n-62-11-13>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed Apr 28 08:35:33 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed Apr 28 08:35:33 2021
Terminated at Thu Apr 29 08:30:46 2021
Results reported at Thu Apr 29 08:30:46 2021

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

    CPU time :                                   86029.51 sec.
    Max Memory :                                 3450 MB
    Average Memory :                             3412.53 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               12934.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86114 sec.
    Turnaround time :                            193600 sec.

The output (if any) is above this job summary.

