
# Parameters

    Name :                      Maze_teleport-1
    Main :                      teleport
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
    Cf convert :                3
    Counterfacts :              1
    Topn :                      6
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      76364381504 function calls (76083150753 primitive calls) in 86042.70 seconds

##    Ordered by: cumulative time
   List reduced from 486 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86105.655 86105.655 {built-in method builtins.exec}
                      1    1.608    1.608 86105.655 86105.655 <string>:1(<module>)
                      1  304.959  304.959 86104.047 86104.047 main.py:45(teleport)
               10094132   48.534    0.000 31190.978    0.003 agent.py:29(learn)
                5047066   27.453    0.000 26331.021    0.005 game.py:41(step)
               10094132  771.771    0.000 26038.820    0.003 learner.py:42(Qlearn)
                5047066   36.309    0.000 25077.130    0.005 layers.py:718(step)
                5047066  200.585    0.000 18817.154    0.004 agent.py:54(_learn)
                5047066  516.900    0.000 14633.436    0.003 layers.py:17(step)
              504706600  868.717    0.000 14062.083    0.000 layer.py:98(move)
        316442039/35212299 1367.220    0.000 12731.563    0.000 module.py:715(_call_impl)
                5047066  164.612    0.000 12301.587    0.002 agent.py:117(_learn)
               25118167   65.323    0.000 11801.728    0.000 network.py:27(forward)
               25118167  328.806    0.000 11564.269    0.000 container.py:115(forward)
                5047067  784.166    0.000 10349.536    0.002 layers.py:684(update)
               10094132   78.044    0.000 10141.343    0.001 grad_mode.py:23(decorate_context)
               10094132  368.352    0.000 9924.532    0.001 adam.py:55(step)
                5047066 6711.776    0.001 9098.081    0.002 replaybuffer.py:22(sample_data)
               10094132 1839.176    0.000 8107.370    0.001 functional.py:53(adam)
                9976969  284.032    0.000 7915.026    0.001 agent.py:49(__call__)
              504706600 1885.726    0.000 7752.790    0.000 layers.py:735(check)
               10094132   65.680    0.000 6388.031    0.001 tensor.py:181(backward)
               10094132   55.054    0.000 6322.351    0.001 __init__.py:68(backward)
               10094132 5997.961    0.001 5997.961    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                5047066 2202.763    0.000 5950.854    0.001 agent.py:88(interveen)
                5047066 2577.858    0.001 5094.650    0.001 agent.py:67(modify)
              504706600  849.739    0.000 4645.023    0.000 layers.py:729(isFree)
               50236334   90.704    0.000 4291.420    0.000 conv.py:422(forward)
               50236334  110.229    0.000 4158.698    0.000 conv.py:414(_conv_forward)
               50236334 4028.225    0.000 4028.225    0.000 {built-in method conv2d}
                5047066 2213.867    0.000 4022.604    0.001 replaybuffer.py:28(teleporter_save_data)
             3584454275 3215.545    0.000 3795.284    0.000 layer.py:95(isFree)
               65260369  149.790    0.000 3671.790    0.000 linear.py:92(forward)
               65260369  255.198    0.000 3440.154    0.000 functional.py:1669(linear)
                4088179   67.186    0.000 3399.417    0.001 layers.py:740(restart)
               40376536 1883.849    0.000 3386.251    0.000 layer.py:167(NoRock_update)
                4088179   40.246    0.000 2923.661    0.001 level.py:8(__init__)
             1413437437  803.012    0.000 2844.450    0.000 {built-in method builtins.any}
                5572971  376.447    0.000 2575.053    0.000 levels.py:9(generate)
              635930370 1524.449    0.000 2550.033    0.000 tensor.py:933(grad)
                5047066   88.553    0.000 2469.991    0.000 agent.py:112(__call__)
               65260369 2435.856    0.000 2435.856    0.000 {built-in method addmm}
               15024035  123.669    0.000 2399.496    0.000 agent.py:59(modify_board)
               40259365 2336.020    0.000 2336.020    0.000 {built-in method cat}
              504706600 1373.647    0.000 2252.343    0.000 layers.py:168(check)
               10094132  209.646    0.000 2197.758    0.000 optimizer.py:167(zero_grad)
                5047066   95.081    0.000 1941.951    0.000 replaybuffer.py:18(stacker)
               21536349 1758.537    0.000 1758.537    0.000 {built-in method tensor}
              181694376 1631.009    0.000 1631.009    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               90378536   83.590    0.000 1582.618    0.000 activation.py:713(forward)
               15024035 1541.897    0.000 1541.897    0.000 {built-in method torch._C._nn.one_hot}
              128035822 1516.911    0.000 1516.911    0.000 {built-in method clone}
               90378536  127.047    0.000 1499.028    0.000 functional.py:1292(leaky_relu)
             4505566689 1215.190    0.000 1494.869    0.000 layers.py:700(<genexpr>)
             5124986910 1029.228    0.000 1492.126    0.000 enum.py:646(__hash__)
               35333262  194.006    0.000 1417.867    0.000 tensor.py:21(wrapped)
               10094132   17.872    0.000 1399.160    0.000 game.py:37(board)
              827370282  456.431    0.000 1390.986    0.000 overrides.py:1070(has_torch_function)
               90378536 1359.435    0.000 1359.435    0.000 {built-in method torch._C._nn.leaky_relu}
              181694376 1328.321    0.000 1328.321    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
             1563113171  993.533    0.000  993.533    0.000 layer.py:146(elements)
                5047066  556.995    0.000  963.722    0.000 collector.py:46(collect)
               90847188  931.153    0.000  931.153    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              504706600  557.275    0.000  888.824    0.000 layers.py:141(check)
               90847188  884.300    0.000  884.300    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              504706600  622.394    0.000  878.160    0.000 layers.py:48(check)
               12264537  107.430    0.000  874.882    0.000 level.py:41(notUsed)
                9976969  303.094    0.000  862.874    0.000 exploration.py:53(softmaxer)
             8027494314  809.485    0.000  809.485    0.000 layer.py:91(positions)
              504706600  526.568    0.000  779.967    0.000 layers.py:124(check)
                5572971  414.204    0.000  779.473    0.000 levels.py:75(RFS)
               90847188  777.147    0.000  777.147    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               90847188  687.175    0.000  687.175    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              540039962  124.902    0.000  648.051    0.000 {built-in method builtins.all}
               10094132   23.847    0.000  622.206    0.000 loss.py:445(forward)
               10094132   76.536    0.000  598.359    0.000 functional.py:2637(mse_loss)
        5586316074/5586316072  447.017    0.000  591.840    0.000 {built-in method builtins.len}
              504706600  387.500    0.000  583.666    0.000 layers.py:23(check)
             1056030393  242.577    0.000  564.751    0.000 layers.py:690(<genexpr>)
               20281187  215.498    0.000  564.556    0.000 random.py:315(sample)
             1755333198  428.322    0.000  537.818    0.000 overrides.py:1083(<genexpr>)
              741901521  360.627    0.000  515.371    0.000 layer.py:130(add)
               90847188  506.599    0.000  506.599    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               25235330  504.064    0.000  504.064    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
             5125023597  462.904    0.000  462.904    0.000 {built-in method builtins.hash}
              143059857  459.253    0.000  459.253    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               65260369  447.533    0.000  447.533    0.000 {method 't' of 'torch._C._TensorBase' objects}
              504075926  293.703    0.000  437.976    0.000 layer.py:126(remove)
                5049060  422.189    0.000  422.189    0.000 {method 'ne' of 'torch._C._TensorBase' objects}
               32705432   55.260    0.000  396.127    0.000 layer.py:69(restart)
               30282396  394.728    0.000  394.728    0.000 {built-in method sum}
             4547406466  385.651    0.000  385.651    0.000 {method 'random' of '_random.Random' objects}
              408411695  382.917    0.000  382.917    0.000 level.py:32(inverse)
             3079747675  364.269    0.000  364.269    0.000 layer.py:203(isBlocking)
               12264537   12.731    0.000  344.959    0.000 level.py:38(elementsIn)
               10094132  341.524    0.000  341.524    0.000 {built-in method torch._C._nn.mse_loss}
                5047066   28.838    0.000  318.671    0.000 exploration.py:47(epsilonGreedy)
               10095633  309.311    0.000  309.311    0.000 {built-in method max}
              385938937  202.237    0.000  297.251    0.000 random.py:250(_randbelow_with_getrandbits)
                5572971  181.159    0.000  287.976    0.000 level.py:16(<dictcomp>)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9550915: <Maze_teleport_1> in cluster <dcc> Done

Job <Maze_teleport_1> was submitted from host <n-62-30-4> by user <s183905> in cluster <dcc> at Tue Apr 20 16:21:50 2021
Job was executed on host(s) <n-62-20-10>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sun Apr 25 07:11:59 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun Apr 25 07:11:59 2021
Terminated at Mon Apr 26 07:07:07 2021
Results reported at Mon Apr 26 07:07:07 2021

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

    CPU time :                                   85898.73 sec.
    Max Memory :                                 2680 MB
    Average Memory :                             2677.52 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13704.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86110 sec.
    Turnaround time :                            485117 sec.

The output (if any) is above this job summary.

