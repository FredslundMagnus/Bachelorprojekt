
# Parameters

    Name :                      Maze_Conver4_3counterfactsNOCRASH_2-2
    Main :                      Load_Cfagent
    Level :                     Levels.Maze
    Failed actions chance :     0
    Use model :                 True
    Depth :                     3
    Model explore :             1000000
    Samples :                   5
    Hours :                     11.0
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
    Load name :                 Maze_Conver4_3counterfactsNOCRASH
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      57159226815 function calls (56805647834 primitive calls) in 86050.13 seconds

##    Ordered by: cumulative time
   List reduced from 441 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86116.448 86116.448 {built-in method builtins.exec}
                      1    4.813    4.813 86116.448 86116.448 <string>:1(<module>)
                      1  346.274  346.274 86111.634 86111.634 main.py:109(Load_Cfagent)
                2602212 2711.620    0.001 23671.462    0.009 agent.py:212(counterfact)
                7806636   36.267    0.000 20293.421    0.003 agent.py:29(learn)
                7806636  517.854    0.000 16428.442    0.002 learner.py:42(Qlearn)
                2602212   13.738    0.000 15534.562    0.006 game.py:42(step)
                2602212   20.397    0.000 14950.978    0.006 layers.py:827(step)
        391714880/38138720 1698.865    0.000 13091.160    0.000 module.py:866(_call_impl)
               30332084   85.514    0.000 12375.926    0.000 network.py:28(forward)
               30332084  395.646    0.000 12068.997    0.000 container.py:117(forward)
               92438233 8540.486    0.000 8540.486    0.000 {built-in method tensor}
                6061723  119.041    0.000 8473.592    0.001 agent.py:176(choose_action)
               86698516   52.132    0.000 8427.809    0.000 game.py:38(board)
                2602212  324.456    0.000 7886.693    0.003 agent.py:54(_learn)
                2602212  397.888    0.000 7465.196    0.003 layers.py:793(update)
                2602212  263.613    0.000 7439.453    0.003 layers.py:17(step)
               11259301  327.501    0.000 7435.253    0.001 agent.py:49(__call__)
                2602212  320.439    0.000 7195.195    0.003 agent.py:204(_learn)
              259771406  438.348    0.000 7152.096    0.000 layer.py:106(move)
                2602212 5704.504    0.002 6604.221    0.003 replaybuffer.py:22(sample_data)
                2602212 5489.261    0.002 6340.579    0.002 replaybuffer.py:67(sample_data)
                7806636   78.951    0.000 6331.612    0.001 optimizer.py:84(wrapper)
                7806636   40.640    0.000 6014.515    0.001 grad_mode.py:24(decorate_context)
                7806636  269.489    0.000 5885.859    0.001 adam.py:55(step)
                7806636 1222.658    0.000 5337.173    0.001 _functional.py:53(adam)
               83270768 2957.860    0.000 5303.688    0.000 layer.py:175(NoRock_update)
                2602212   85.911    0.000 5154.941    0.002 agent.py:117(_learn)
               60664168  135.121    0.000 4437.245    0.000 conv.py:398(forward)
                7806636   29.575    0.000 4380.832    0.001 tensor.py:195(backward)
                7806636   39.351    0.000 4350.069    0.001 __init__.py:68(backward)
               60664168  101.309    0.000 4226.969    0.000 conv.py:390(_conv_forward)
                2602212 2461.339    0.001 4182.965    0.002 replaybuffer.py:28(teleporter_save_data)
                7806636 4145.304    0.001 4145.304    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               60664168 4125.660    0.000 4125.660    0.000 {built-in method conv2d}
              259771406  944.862    0.000 3861.125    0.000 layers.py:844(check)
                2602212 2091.401    0.001 3796.484    0.001 agent.py:88(interveen)
                4326400   64.183    0.000 3501.329    0.001 layers.py:849(restart)
               85791828  173.228    0.000 3369.298    0.000 linear.py:93(forward)
               85791828   68.641    0.000 3098.022    0.000 functional.py:1737(linear)
                4326400   38.422    0.000 3034.944    0.001 level.py:8(__init__)
               85791828 3012.748    0.000 3012.748    0.000 {built-in method torch._C._nn.linear}
                5899659  372.347    0.000 2698.337    0.000 levels.py:9(generate)
              259771406  407.005    0.000 2432.699    0.000 layers.py:838(isFree)
                2602212 1371.429    0.001 2053.733    0.001 agent.py:67(modify)
             1941769908 1749.357    0.000 2025.693    0.000 layer.py:103(isFree)
               13861513   94.111    0.000 1833.713    0.000 agent.py:59(modify_board)
              116123912  117.278    0.000 1804.898    0.000 activation.py:713(forward)
                6061723 1520.427    0.000 1754.225    0.000 agent.py:187(convert_values)
              169048724 1707.418    0.000 1707.418    0.000 {built-in method clone}
              116123912   96.512    0.000 1687.621    0.000 functional.py:1364(leaky_relu)
               39883633 1590.593    0.000 1590.593    0.000 {built-in method cat}
              116123912 1571.731    0.000 1571.731    0.000 {built-in method torch._C._nn.leaky_relu}
                2602212 1028.197    0.000 1336.339    0.001 replaybuffer.py:73(CF_save_data)
             1306411307 1325.288    0.000 1325.288    0.000 layer.py:154(elements)
                2602212   54.657    0.000 1238.793    0.000 agent.py:172(__call__)
               13861513 1207.419    0.000 1207.419    0.000 {built-in method torch._C._nn.one_hot}
              259771406  697.583    0.000 1150.735    0.000 layers.py:168(check)
                2602212   52.696    0.000 1129.380    0.000 agent.py:112(__call__)
              145723872 1051.451    0.000 1051.451    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              263701435  238.654    0.000  983.020    0.000 {built-in method builtins.any}
               12979200  115.441    0.000  982.461    0.000 level.py:41(notUsed)
              260221200  107.533    0.000  961.448    0.000 {built-in method builtins.all}
             3465563442  669.455    0.000  951.745    0.000 enum.py:646(__hash__)
              145723872  919.591    0.000  919.591    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                7806636  164.213    0.000  901.378    0.000 optimizer.py:189(zero_grad)
             1121391619  311.676    0.000  887.171    0.000 layers.py:799(<genexpr>)
                5899659  424.586    0.000  802.099    0.000 levels.py:75(RFS)
            10470148993  683.535    0.000  756.339    0.000 {built-in method builtins.len}
             2303053200  606.085    0.000  744.366    0.000 layers.py:809(<genexpr>)
               11259301  271.491    0.000  738.849    0.000 exploration.py:53(softmaxer)
                2602212   49.663    0.000  685.476    0.000 replaybuffer.py:18(stacker)
                2602212   47.832    0.000  645.975    0.000 replaybuffer.py:63(stacker)
               72861936  605.247    0.000  605.247    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               72861936  533.911    0.000  533.911    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               21330142  208.110    0.000  531.480    0.000 random.py:315(sample)
              260221200  344.918    0.000  502.850    0.000 layers.py:113(isDone)
               72861936  493.986    0.000  493.986    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               72861936  491.529    0.000  491.529    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              259771406  283.267    0.000  451.543    0.000 layers.py:141(check)
             4558233538  435.499    0.000  435.499    0.000 layer.py:99(positions)
              510033552  339.629    0.000  425.469    0.000 tensor.py:906(grad)
              259771406  282.158    0.000  413.017    0.000 layers.py:48(check)
               12979200   13.958    0.000  409.138    0.000 level.py:38(elementsIn)
                2602212  239.760    0.000  407.091    0.000 collector.py:46(collect)
              432247121  397.602    0.000  397.602    0.000 level.py:32(inverse)
              333932328  294.017    0.000  390.650    0.000 layer.py:134(remove)
               34611200   53.496    0.000  390.151    0.000 layer.py:77(restart)
              259771406  258.183    0.000  386.833    0.000 layers.py:124(check)
              185512449  376.508    0.000  376.508    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                7806636   14.183    0.000  375.247    0.000 loss.py:527(forward)
                7806636   38.755    0.000  361.064    0.000 functional.py:2898(mse_loss)
               72861936  358.139    0.000  358.139    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              572137665  234.226    0.000  347.542    0.000 layer.py:138(add)
               83270768  335.595    0.000  335.595    0.000 layer.py:186(<listcomp>)
               26081024  332.496    0.000  332.496    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               60664168   50.082    0.000  298.576    0.000 flatten.py:39(forward)
              407689609  200.286    0.000  297.530    0.000 random.py:250(_randbelow_with_getrandbits)
             3465593265  282.296    0.000  282.296    0.000 {built-in method builtins.hash}
              259771406  189.874    0.000  280.911    0.000 layers.py:23(check)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9632954: <Maze_Conver4_3counterfactsNOCRASH_2_2> in cluster <dcc> Done

Job <Maze_Conver4_3counterfactsNOCRASH_2_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed May 12 15:41:02 2021
Job was executed on host(s) <n-62-20-10>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed May 12 16:27:51 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 12 16:27:51 2021
Terminated at Thu May 13 16:23:14 2021
Results reported at Thu May 13 16:23:14 2021

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

    CPU time :                                   85907.49 sec.
    Max Memory :                                 8282 MB
    Average Memory :                             5794.28 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               8102.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86124 sec.
    Turnaround time :                            88932 sec.

The output (if any) is above this job summary.

