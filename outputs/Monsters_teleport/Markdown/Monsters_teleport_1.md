
# Parameters

    Name :                      Monsters_teleport-1
    Main :                      teleport
    Level :                     Levels.MonsterLevel
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


      87145934733 function calls (86922452934 primitive calls) in 86105.15 seconds

##    Ordered by: cumulative time
   List reduced from 479 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86105.150 86105.150 {built-in method builtins.exec}
                      1    1.544    1.544 86105.150 86105.150 <string>:1(<module>)
                      1  180.507  180.507 86103.606 86103.606 main.py:45(teleport)
                3990756   18.125    0.000 27850.423    0.007 game.py:41(step)
                7981512   30.745    0.000 27288.150    0.003 agent.py:29(learn)
                3990756   19.220    0.000 26959.061    0.007 layers.py:718(step)
                7981512  658.122    0.000 23358.745    0.003 learner.py:42(Qlearn)
                3990756  128.981    0.000 16400.988    0.004 agent.py:54(_learn)
                3990757  561.957    0.000 13625.121    0.003 layers.py:684(update)
                3990756  333.647    0.000 13287.702    0.003 layers.py:17(step)
              399075600 1065.214    0.000 12918.665    0.000 layer.py:98(move)
                3990756  107.978    0.000 10840.610    0.003 agent.py:117(_learn)
        251415951/27935163  970.387    0.000 10644.932    0.000 module.py:715(_call_impl)
                7981512   48.933    0.000 9990.227    0.001 grad_mode.py:23(decorate_context)
               19953651   54.632    0.000 9962.112    0.000 network.py:27(forward)
                7981512  251.646    0.000 9852.711    0.001 adam.py:55(step)
               19953651  255.780    0.000 9793.632    0.000 container.py:115(forward)
                3990756 5059.772    0.001 9689.770    0.002 replaybuffer.py:28(teleporter_save_data)
              399075600 1161.840    0.000 8884.242    0.000 layers.py:735(check)
                7981512 1806.760    0.000 8505.469    0.001 functional.py:53(adam)
                3990756 4962.346    0.001 8199.641    0.002 agent.py:88(interveen)
               12733841   94.431    0.000 6615.625    0.001 layers.py:740(restart)
                7981383  180.429    0.000 6527.637    0.001 agent.py:49(__call__)
               12733841   46.781    0.000 5612.538    0.000 level.py:8(__init__)
                7981512   48.484    0.000 5321.961    0.001 tensor.py:181(backward)
                7981512   28.409    0.000 5273.478    0.001 __init__.py:68(backward)
              399075600 2838.661    0.000 5154.315    0.000 layers.py:538(check)
               12733841  886.960    0.000 5099.343    0.000 levels.py:413(generate)
                7981512 5035.280    0.001 5035.280    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3990756 2984.565    0.001 4803.286    0.001 replaybuffer.py:22(sample_data)
                3990756 2609.581    0.001 4668.858    0.001 agent.py:67(modify)
              260627542 3646.917    0.000 3646.917    0.000 {built-in method clone}
               39907302   64.742    0.000 3539.857    0.000 conv.py:422(forward)
               39907302   72.820    0.000 3448.821    0.000 conv.py:414(_conv_forward)
               39907302 3362.931    0.000 3362.931    0.000 {built-in method conv2d}
               63669205  541.679    0.000 3339.273    0.000 level.py:41(notUsed)
             1117044183  549.004    0.000 3248.908    0.000 {built-in method builtins.any}
               51879441  112.510    0.000 3188.173    0.000 linear.py:92(forward)
               51879441  196.340    0.000 3025.245    0.000 functional.py:1669(linear)
               23944542 2000.250    0.000 2830.737    0.000 layer.py:151(update)
             2754640979  721.380    0.000 2329.093    0.000 layers.py:700(<genexpr>)
              399075600  469.675    0.000 2188.736    0.000 layers.py:729(isFree)
               51879441 2173.706    0.000 2173.706    0.000 {built-in method addmm}
             9049616408 1510.480    0.000 2162.509    0.000 enum.py:646(__hash__)
                3990756   53.234    0.000 2062.546    0.001 agent.py:112(__call__)
              502835310 1301.205    0.000 2041.311    0.000 tensor.py:933(grad)
                7981512  179.610    0.000 1979.215    0.000 optimizer.py:167(zero_grad)
               11972139   84.361    0.000 1956.312    0.000 agent.py:59(modify_board)
               31925919 1912.099    0.000 1912.099    0.000 {built-in method cat}
              143667216 1775.756    0.000 1775.756    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
             2203980380 1386.886    0.000 1719.061    0.000 layer.py:95(isFree)
                3990756   69.423    0.000 1548.987    0.000 replaybuffer.py:18(stacker)
              143667216 1503.291    0.000 1503.291    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               71833092   58.095    0.000 1468.246    0.000 activation.py:713(forward)
              394716520  898.443    0.000 1451.817    0.000 layers.py:575(isDead)
               63669205   48.403    0.000 1449.876    0.000 level.py:38(elementsIn)
               71833092   94.739    0.000 1410.151    0.000 functional.py:1292(leaky_relu)
               71833092 1306.540    0.000 1306.540    0.000 {built-in method torch._C._nn.leaky_relu}
              399075600  865.212    0.000 1234.354    0.000 layers.py:77(check)
               11972139 1227.399    0.000 1227.399    0.000 {built-in method torch._C._nn.one_hot}
               17095678 1191.073    0.000 1191.073    0.000 {built-in method tensor}
              272599681 1117.597    0.000 1117.597    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               27937546  152.213    0.000 1067.304    0.000 tensor.py:21(wrapped)
              654485197  346.071    0.000 1011.012    0.000 overrides.py:1070(has_torch_function)
               71833608  985.456    0.000  985.456    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                3990756  562.953    0.000  946.613    0.000 collector.py:46(collect)
              589531588  181.353    0.000  943.383    0.000 random.py:244(randint)
               63669205  448.830    0.000  913.579    0.000 level.py:39(<listcomp>)
             2716380069  911.487    0.000  911.487    0.000 level.py:32(inverse)
               76403046   87.376    0.000  884.165    0.000 layer.py:69(restart)
               71833608  882.962    0.000  882.962    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                7981512   10.212    0.000  880.851    0.000 game.py:37(board)
              427013246   97.658    0.000  876.603    0.000 {built-in method builtins.all}
              829964958  180.996    0.000  810.378    0.000 layers.py:690(<genexpr>)
               71833608  809.229    0.000  809.229    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               67659961  307.012    0.000  801.537    0.000 random.py:315(sample)
             1525197778  587.582    0.000  783.155    0.000 layer.py:130(add)
             8641713634  775.290    0.000  775.290    0.000 layer.py:91(positions)
              589531588  312.716    0.000  762.030    0.000 random.py:200(randrange)
             1073099246  523.730    0.000  756.417    0.000 random.py:250(_randbelow_with_getrandbits)
               71833608  719.784    0.000  719.784    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                7981383  252.144    0.000  706.502    0.000 exploration.py:53(softmaxer)
              943307759  428.505    0.000  658.653    0.000 layer.py:126(remove)
             9049645535  652.034    0.000  652.034    0.000 {built-in method builtins.hash}
              399075600  413.109    0.000  627.777    0.000 layers.py:48(check)
              399075700  422.900    0.000  622.747    0.000 layers.py:113(isDone)
               12733941  311.915    0.000  621.783    0.000 layers.py:36(reset)
              399075600  202.541    0.000  591.601    0.000 layers.py:572(<listcomp>)
             3064801906  590.701    0.000  590.701    0.000 layer.py:146(elements)
               71833608  570.332    0.000  570.332    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               63669205  297.059    0.000  487.894    0.000 {built-in method _functools.reduce}
              399075600  176.738    0.000  478.772    0.000 layers.py:573(<listcomp>)
             2750511110  475.994    0.000  475.994    0.000 enum.py:352(<genexpr>)
                7981512   12.110    0.000  455.864    0.000 loss.py:445(forward)
              399075600  307.040    0.000  443.975    0.000 layers.py:23(check)
                7981512   42.579    0.000  443.754    0.000 functional.py:2637(mse_loss)
               19953780  442.459    0.000  442.459    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               12733841  245.519    0.000  440.082    0.000 level.py:16(<dictcomp>)
               51879441  428.040    0.000  428.040    0.000 {method 't' of 'torch._C._TensorBase' objects}
        3538682800/3538682798  272.114    0.000  388.666    0.000 {built-in method builtins.len}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9550924: <Monsters_teleport_1> in cluster <dcc> Done

Job <Monsters_teleport_1> was submitted from host <n-62-30-4> by user <s183905> in cluster <dcc> at Tue Apr 20 16:21:52 2021
Job was executed on host(s) <n-62-20-6>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Tue Apr 27 08:18:25 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue Apr 27 08:18:25 2021
Terminated at Wed Apr 28 08:13:43 2021
Results reported at Wed Apr 28 08:13:43 2021

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

    CPU time :                                   85896.90 sec.
    Max Memory :                                 2676 MB
    Average Memory :                             2670.38 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13708.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86133 sec.
    Turnaround time :                            661911 sec.

The output (if any) is above this job summary.

