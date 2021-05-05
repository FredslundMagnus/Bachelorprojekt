Start
True
True
['main.py', '-name', 'MonsterLevel_Conver1-2', '-hours', '24.0', '-level', 'Levels.MonsterLevel', '-main', 'CFagent', '-CF_convert', '1', '-TopN', '3']

# Parameters

    Name :                      MonsterLevel_Conver1-2
    Main :                      CFagent
    Level :                     Levels.MonsterLevel
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
    Cf convert :                1
    Counterfacts :              1
    Topn :                      3
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      68516035657 function calls (68215875918 primitive calls) in 86123.45 seconds

##    Ordered by: cumulative time
   List reduced from 507 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86123.451 86123.451 {built-in method builtins.exec}
                      1    4.284    4.284 86123.451 86123.451 <string>:1(<module>)
                      1  331.757  331.757 86119.168 86119.168 main.py:84(CFagent)
                8838048   35.140    0.000 26520.770    0.003 agent.py:29(learn)
                8838048  663.877    0.000 22089.570    0.002 learner.py:42(Qlearn)
                2946016   13.922    0.000 20737.270    0.007 game.py:42(step)
                2946016   17.321    0.000 20112.395    0.007 layers.py:827(step)
        334991272/34833224 1333.891    0.000 12331.208    0.000 module.py:866(_call_impl)
               25995176   73.484    0.000 11611.415    0.000 network.py:28(forward)
               25995176  362.117    0.000 11375.427    0.000 container.py:117(forward)
                2946016  307.780    0.000 10225.295    0.003 agent.py:54(_learn)
                2946016  252.013    0.000 10152.530    0.003 layers.py:17(step)
                2946017  427.547    0.000 9919.083    0.003 layers.py:793(update)
              293375411  824.267    0.000 9875.772    0.000 layer.py:106(move)
                2946016  306.969    0.000 9489.418    0.003 agent.py:204(_learn)
                8838048   76.690    0.000 9371.767    0.001 optimizer.py:84(wrapper)
                2946016 1561.480    0.001 9358.453    0.003 agent.py:212(counterfact)
                8838048   36.866    0.000 9016.231    0.001 grad_mode.py:24(decorate_context)
                8838048  249.964    0.000 8893.606    0.001 adam.py:55(step)
                8838048 1822.121    0.000 8363.498    0.001 _functional.py:53(adam)
                2946016   89.946    0.000 6752.916    0.002 agent.py:117(_learn)
              293375411  883.269    0.000 6605.691    0.000 layers.py:844(check)
                8578499  233.226    0.000 6186.859    0.001 agent.py:49(__call__)
                2946016 3174.250    0.001 5917.388    0.002 replaybuffer.py:28(teleporter_save_data)
                8838048   36.930    0.000 5489.708    0.001 tensor.py:195(backward)
                8838048   33.080    0.000 5451.486    0.001 __init__.py:68(backward)
                8838048 5215.885    0.001 5215.885    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2946016 4215.636    0.001 5175.140    0.002 replaybuffer.py:22(sample_data)
                2946016 4184.654    0.001 5121.706    0.002 replaybuffer.py:67(sample_data)
                2946016 2946.743    0.001 5066.582    0.002 agent.py:88(interveen)
                9011836   72.209    0.000 4911.524    0.001 layers.py:849(restart)
                9011836   37.987    0.000 4207.209    0.000 level.py:8(__init__)
               51990352  112.379    0.000 4099.147    0.000 conv.py:398(forward)
               51990352   71.719    0.000 3935.846    0.000 conv.py:390(_conv_forward)
                2686597   60.815    0.000 3909.751    0.001 agent.py:176(choose_action)
               51990352 3864.127    0.000 3864.127    0.000 {built-in method conv2d}
                9011836  624.493    0.000 3823.985    0.000 levels.py:428(generate)
              293375411 2194.229    0.000 3813.335    0.000 layers.py:538(check)
               72093496  146.033    0.000 3320.503    0.000 linear.py:93(forward)
               42084803 3186.533    0.000 3186.533    0.000 {built-in method tensor}
               72093496   56.753    0.000 3102.882    0.000 functional.py:1737(linear)
               35352198 2018.437    0.000 3061.884    0.000 layer.py:159(update)
               72093496 3031.051    0.000 3031.051    0.000 {built-in method torch._C._nn.linear}
               35266556   27.783    0.000 2994.409    0.000 game.py:38(board)
              223833847 2873.093    0.000 2873.093    0.000 {built-in method clone}
                2946016 1886.113    0.001 2745.394    0.001 agent.py:67(modify)
                2946016 1933.626    0.001 2701.185    0.001 replaybuffer.py:73(CF_save_data)
               45059180  398.989    0.000 2592.423    0.000 level.py:41(notUsed)
              293375411  377.842    0.000 1887.599    0.000 layers.py:838(isFree)
               98088672   75.132    0.000 1848.381    0.000 activation.py:713(forward)
              295090283  210.996    0.000 1837.496    0.000 {built-in method builtins.any}
               98088672   77.210    0.000 1773.248    0.000 functional.py:1364(leaky_relu)
              164976896 1729.219    0.000 1729.219    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               40984675 1706.913    0.000 1706.913    0.000 {built-in method cat}
               98088672 1679.420    0.000 1679.420    0.000 {built-in method torch._C._nn.leaky_relu}
               11524515   78.718    0.000 1673.660    0.000 agent.py:59(modify_board)
             2025346656  508.401    0.000 1627.433    0.000 layers.py:809(<genexpr>)
             6899609003 1105.455    0.000 1588.863    0.000 enum.py:646(__hash__)
             1684297512 1247.356    0.000 1509.757    0.000 layer.py:103(isFree)
              164976896 1507.379    0.000 1507.379    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                2946016   52.618    0.000 1494.605    0.001 agent.py:172(__call__)
                2946016   49.223    0.000 1398.458    0.000 agent.py:112(__call__)
                8838048  202.117    0.000 1282.431    0.000 optimizer.py:189(zero_grad)
               45059180   34.432    0.000 1197.836    0.000 level.py:38(elementsIn)
               11524515 1065.159    0.000 1065.159    0.000 {built-in method torch._C._nn.one_hot}
              292144266  630.851    0.000 1014.356    0.000 layers.py:575(isDead)
               82488448  934.219    0.000  934.219    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              293375411  659.514    0.000  933.938    0.000 layers.py:77(check)
               82488448  801.072    0.000  801.072    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               82488448  775.388    0.000  775.388    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               50951212  295.693    0.000  770.750    0.000 random.py:315(sample)
               82488448  768.906    0.000  768.906    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               45059180  384.212    0.000  763.973    0.000 level.py:39(<listcomp>)
                2946016   52.521    0.000  755.023    0.000 replaybuffer.py:18(stacker)
                2946016   52.878    0.000  737.293    0.000 replaybuffer.py:63(stacker)
              238304378  715.551    0.000  715.551    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              426205581  140.047    0.000  678.249    0.000 random.py:244(randint)
             2238680914  678.149    0.000  678.149    0.000 layer.py:154(elements)
                8578499  236.734    0.000  645.441    0.000 exploration.py:53(softmaxer)
             1922417385  645.204    0.000  645.204    0.000 level.py:32(inverse)
              294601700   59.776    0.000  623.236    0.000 {built-in method builtins.all}
               54071016   63.276    0.000  614.875    0.000 layer.py:77(restart)
                2946016  371.873    0.000  613.121    0.000 collector.py:46(collect)
              921857190  426.990    0.000  611.193    0.000 random.py:250(_randbelow_with_getrandbits)
              608696075  130.908    0.000  599.881    0.000 layers.py:799(<genexpr>)
               82488448  598.031    0.000  598.031    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                2686597  577.665    0.000  577.665    0.000 agent.py:187(convert_values)
             6338784906  550.386    0.000  550.386    0.000 layer.py:99(positions)
             1095495954  406.092    0.000  547.253    0.000 layer.py:138(add)
              426205581  223.427    0.000  538.201    0.000 random.py:200(randrange)
              682266657  338.908    0.000  507.435    0.000 layer.py:134(remove)
             6899642634  483.413    0.000  483.413    0.000 {built-in method builtins.hash}
              577419220  373.590    0.000  463.960    0.000 tensor.py:906(grad)
              293375411  315.848    0.000  463.690    0.000 layers.py:48(check)
              294601700  314.846    0.000  462.623    0.000 layers.py:113(isDone)
        4964844054/4964844051  372.637    0.000  433.133    0.000 {built-in method builtins.len}
                8838048   11.856    0.000  429.440    0.000 loss.py:527(forward)
                9011936  214.654    0.000  426.053    0.000 layers.py:36(reset)
                8838048   32.359    0.000  417.584    0.000 functional.py:2898(mse_loss)
              293375411  146.247    0.000  416.947    0.000 layers.py:572(<listcomp>)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9579180: <MonsterLevel_Conver1_2> in cluster <dcc> Done

Job <MonsterLevel_Conver1_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Tue Apr 27 02:44:08 2021
Job was executed on host(s) <n-62-20-6>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun May  2 20:31:28 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun May  2 20:31:28 2021
Terminated at Mon May  3 20:27:16 2021
Results reported at Mon May  3 20:27:16 2021

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

    CPU time :                                   85899.79 sec.
    Max Memory :                                 9025 MB
    Average Memory :                             6255.92 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               7359.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86206 sec.
    Turnaround time :                            582188 sec.

The output (if any) is above this job summary.

