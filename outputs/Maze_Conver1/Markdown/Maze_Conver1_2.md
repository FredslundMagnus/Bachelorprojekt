
# Parameters

    Name :                      Maze_Conver1-2
    Main :                      CFagent
    Level :                     Levels.Maze
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
    Cf convert :                1
    Counterfacts :              1
    Topn :                      3
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      59902362198 function calls (59574814855 primitive calls) in 86071.47 seconds

##    Ordered by: cumulative time
   List reduced from 516 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86115.566 86115.566 {built-in method builtins.exec}
                      1    5.575    5.575 86115.566 86115.566 <string>:1(<module>)
                      1  466.334  466.334 86109.991 86109.991 main.py:79(CFagent)
               10740870   46.256    0.000 27481.190    0.003 agent.py:29(learn)
               10740869  703.929    0.000 22174.483    0.002 learner.py:42(Qlearn)
                3580290   19.418    0.000 17692.412    0.005 game.py:41(step)
                3580290   24.608    0.000 16872.326    0.005 layers.py:718(step)
        366775422/39229770 1559.769    0.000 12463.374    0.000 module.py:866(_call_impl)
               28488901   78.498    0.000 11602.081    0.000 network.py:27(forward)
               28488901  389.124    0.000 11320.328    0.000 container.py:117(forward)
                3580290  431.971    0.000 10706.865    0.003 agent.py:54(_learn)
                3580290  426.148    0.000 9750.544    0.003 agent.py:204(_learn)
                3580290  351.386    0.000 9589.732    0.003 layers.py:17(step)
              357796041  583.016    0.000 9207.263    0.000 layer.py:98(move)
                3580290 7916.727    0.002 9128.470    0.003 replaybuffer.py:22(sample_data)
                3580290 7697.182    0.002 8845.175    0.002 replaybuffer.py:67(sample_data)
                3580290  728.058    0.000 8747.114    0.002 agent.py:212(counterfact)
               10740869  108.683    0.000 8562.245    0.001 optimizer.py:84(wrapper)
               10740869   54.507    0.000 8107.751    0.001 grad_mode.py:24(decorate_context)
               10740869  357.991    0.000 7934.546    0.001 adam.py:55(step)
                3580291  523.265    0.000 7218.055    0.002 layers.py:684(update)
               10740869 1647.997    0.000 7204.251    0.001 _functional.py:53(adam)
                3580290  121.362    0.000 6951.227    0.002 agent.py:117(_learn)
                8862798  270.883    0.000 6040.145    0.001 agent.py:49(__call__)
               10740869   48.744    0.000 5833.797    0.001 tensor.py:195(backward)
               10740869   49.625    0.000 5783.359    0.001 __init__.py:68(backward)
               10740869 5501.943    0.001 5501.943    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
              357796041 1209.338    0.000 5182.520    0.000 layers.py:735(check)
               48610354 4406.418    0.000 4406.418    0.000 {built-in method tensor}
               57284648 2362.886    0.000 4207.315    0.000 layer.py:167(NoRock_update)
               56977802  134.427    0.000 4205.029    0.000 conv.py:398(forward)
               40392967   29.721    0.000 4192.017    0.000 game.py:37(board)
               56977802   89.086    0.000 4003.916    0.000 conv.py:390(_conv_forward)
                3580290 1621.727    0.000 3988.659    0.001 agent.py:88(interveen)
               56977802 3914.830    0.000 3914.830    0.000 {built-in method conv2d}
               78306123  160.044    0.000 3190.642    0.000 linear.py:93(forward)
                3580290 1801.336    0.001 3104.306    0.001 replaybuffer.py:28(teleporter_save_data)
               78306123   65.996    0.000 2943.590    0.000 functional.py:1737(linear)
              357796041  450.786    0.000 2928.728    0.000 layers.py:729(isFree)
               78306123 2861.219    0.000 2861.219    0.000 {built-in method torch._C._nn.linear}
                3580290 1814.813    0.001 2770.067    0.001 agent.py:67(modify)
             2109341944 2155.046    0.000 2477.942    0.000 layer.py:95(isFree)
                1724655   36.870    0.000 2315.850    0.001 agent.py:176(choose_action)
                2865413   46.347    0.000 2273.831    0.001 layers.py:740(restart)
                2865413   26.318    0.000 1958.587    0.001 level.py:8(__init__)
               48245983 1933.167    0.000 1933.167    0.000 {built-in method cat}
                3907271  252.560    0.000 1746.986    0.000 levels.py:9(generate)
               12443088   93.712    0.000 1724.854    0.000 agent.py:59(modify_board)
                3580289   74.430    0.000 1702.794    0.000 agent.py:172(__call__)
              106795024   96.458    0.000 1665.226    0.000 activation.py:713(forward)
                3580290   75.882    0.000 1571.635    0.000 agent.py:112(__call__)
              106795024   87.016    0.000 1568.768    0.000 functional.py:1364(leaky_relu)
              357796041  933.399    0.000 1518.540    0.000 layers.py:168(check)
              106795024 1464.854    0.000 1464.854    0.000 {built-in method torch._C._nn.leaky_relu}
              200496220 1400.067    0.000 1400.067    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              358743978  314.685    0.000 1331.180    0.000 {built-in method builtins.any}
              123404235 1316.710    0.000 1316.710    0.000 {built-in method clone}
              200496220 1250.190    0.000 1250.190    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               10740869  221.487    0.000 1226.168    0.000 optimizer.py:189(zero_grad)
                3580290  958.748    0.000 1194.702    0.000 replaybuffer.py:73(CF_save_data)
               12443088 1134.897    0.000 1134.897    0.000 {built-in method torch._C._nn.one_hot}
             1182434490 1128.721    0.000 1128.721    0.000 layer.py:146(elements)
             3196473183  843.132    0.000 1016.494    0.000 layers.py:700(<genexpr>)
             3647548230  709.611    0.000 1013.864    0.000 enum.py:646(__hash__)
                3580290   70.900    0.000  915.382    0.000 replaybuffer.py:18(stacker)
                3580289   66.795    0.000  862.796    0.000 replaybuffer.py:63(stacker)
              100248110  829.994    0.000  829.994    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              358029100  136.630    0.000  786.144    0.000 {built-in method builtins.all}
              100248110  724.567    0.000  724.567    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
             1485572429  392.001    0.000  692.943    0.000 layers.py:690(<genexpr>)
              357796041  428.001    0.000  684.076    0.000 layers.py:141(check)
              100248110  665.936    0.000  665.936    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              100248110  656.825    0.000  656.825    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               17840535  258.605    0.000  650.068    0.000 random.py:315(sample)
                8862798  220.709    0.000  623.135    0.000 exploration.py:53(softmaxer)
        7933392462/7933392459  550.505    0.000  618.258    0.000 {built-in method builtins.len}
                8596239   72.837    0.000  601.817    0.000 level.py:41(notUsed)
              357796041  411.594    0.000  578.974    0.000 layers.py:48(check)
              701736854  461.315    0.000  572.524    0.000 tensor.py:906(grad)
                3580290  322.098    0.000  548.080    0.000 collector.py:46(collect)
                3907271  285.197    0.000  532.791    0.000 levels.py:75(RFS)
               10740869   20.783    0.000  523.691    0.000 loss.py:527(forward)
             5654238876  522.597    0.000  522.597    0.000 layer.py:91(positions)
               10740869   55.285    0.000  502.908    0.000 functional.py:2898(mse_loss)
              357796041  325.776    0.000  490.873    0.000 layers.py:124(check)
              100248110  485.454    0.000  485.454    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              357796041  258.539    0.000  383.927    0.000 layers.py:23(check)
                1724655  346.104    0.000  346.104    0.000 agent.py:187(convert_values)
              534534377  237.784    0.000  333.291    0.000 layer.py:130(add)
              369566416  231.192    0.000  328.236    0.000 layer.py:126(remove)
              453461760  208.040    0.000  310.830    0.000 random.py:250(_randbelow_with_getrandbits)
             3647589029  304.260    0.000  304.260    0.000 {built-in method builtins.hash}
               10740869  303.343    0.000  303.343    0.000 {built-in method torch._C._nn.mse_loss}
                7160582  303.123    0.000  303.123    0.000 {built-in method nonzero}
              139427612  298.485    0.000  298.485    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               56977802   43.063    0.000  276.358    0.000 flatten.py:39(forward)
               10742113  272.465    0.000  272.465    0.000 {built-in method max}
              286278711  265.812    0.000  265.812    0.000 level.py:32(inverse)
               22923304   35.470    0.000  260.895    0.000 layer.py:69(restart)
             3223977618  255.709    0.000  255.709    0.000 {method 'random' of '_random.Random' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9579174: <Maze_Conver1_2> in cluster <dcc> Done

Job <Maze_Conver1_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Tue Apr 27 02:44:07 2021
Job was executed on host(s) <n-62-20-12>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Fri Apr 30 15:20:06 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Fri Apr 30 15:20:06 2021
Terminated at Sat May  1 15:15:30 2021
Results reported at Sat May  1 15:15:30 2021

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

    CPU time :                                   85908.47 sec.
    Max Memory :                                 9971 MB
    Average Memory :                             6559.70 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               6413.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86126 sec.
    Turnaround time :                            390683 sec.

The output (if any) is above this job summary.

