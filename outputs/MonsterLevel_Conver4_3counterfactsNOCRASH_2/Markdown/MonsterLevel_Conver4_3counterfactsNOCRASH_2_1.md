
# Parameters

    Name :                      MonsterLevel_Conver4_3counterfactsNOCRASH_2-1
    Main :                      Load_Cfagent
    Level :                     Levels.MonsterLevel
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
    Num :                       1
    Load name :                 MonsterLevel_Conver4_3counterfactsNOCRASH
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      66310007334 function calls (65952590013 primitive calls) in 86110.39 seconds

##    Ordered by: cumulative time
   List reduced from 430 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86110.392 86110.392 {built-in method builtins.exec}
                      1    4.297    4.297 86110.392 86110.392 <string>:1(<module>)
                      1  267.963  267.963 86106.095 86106.095 main.py:109(Load_Cfagent)
                2372674 4421.637    0.002 24124.645    0.010 agent.py:212(counterfact)
                2372674   10.057    0.000 20338.012    0.009 game.py:42(step)
                2372674   13.174    0.000 19871.113    0.008 layers.py:827(step)
                7118022   27.771    0.000 17958.566    0.003 agent.py:29(learn)
                7118022  446.599    0.000 14636.580    0.002 learner.py:42(Qlearn)
        395107955/37693455 1639.126    0.000 13012.528    0.000 module.py:866(_call_impl)
               30575433   88.962    0.000 12370.315    0.000 network.py:28(forward)
               30575433  381.257    0.000 12074.329    0.000 container.py:117(forward)
                2372674  380.504    0.000 10816.215    0.005 layers.py:793(update)
                6983374  138.860    0.000 9534.413    0.001 agent.py:176(choose_action)
                2372674  221.459    0.000 9022.604    0.004 layers.py:17(step)
              234519526  720.071    0.000 8779.076    0.000 layer.py:106(move)
               11728689  310.071    0.000 7620.612    0.001 agent.py:49(__call__)
                2372674  253.463    0.000 6970.803    0.003 agent.py:54(_learn)
               90372088 6690.319    0.000 6690.319    0.000 {built-in method tensor}
               85138417   53.466    0.000 6599.169    0.000 game.py:38(board)
                2372674  252.164    0.000 6415.649    0.003 agent.py:204(_learn)
               10233830   90.136    0.000 6301.560    0.001 layers.py:849(restart)
              234519526  801.305    0.000 5888.325    0.000 layers.py:844(check)
                7118022   58.640    0.000 5671.876    0.001 optimizer.py:84(wrapper)
               10233830   41.138    0.000 5418.762    0.001 level.py:8(__init__)
                7118022   31.528    0.000 5401.363    0.001 grad_mode.py:24(decorate_context)
                7118022  224.131    0.000 5302.680    0.001 adam.py:55(step)
               10233830  814.488    0.000 4941.693    0.000 levels.py:428(generate)
                2372674 2787.888    0.001 4911.024    0.002 replaybuffer.py:28(teleporter_save_data)
                7118022 1112.282    0.000 4830.672    0.001 _functional.py:53(adam)
               56944164 2999.413    0.000 4675.214    0.000 layer.py:159(update)
                2372674   73.126    0.000 4529.590    0.002 agent.py:117(_learn)
               61150866  136.781    0.000 4396.978    0.000 conv.py:398(forward)
                2372674 3551.901    0.001 4282.780    0.002 replaybuffer.py:22(sample_data)
                2372674 3549.015    0.001 4262.090    0.002 replaybuffer.py:67(sample_data)
               61150866  107.926    0.000 4188.702    0.000 conv.py:390(_conv_forward)
               61150866 4080.775    0.000 4080.775    0.000 {built-in method conv2d}
                2372674 2381.780    0.001 3921.745    0.002 agent.py:88(interveen)
                7118022   24.009    0.000 3858.944    0.001 tensor.py:195(backward)
                7118022   27.829    0.000 3833.871    0.001 __init__.py:68(backward)
                7118022 3664.082    0.001 3664.082    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
              234519526 1923.819    0.000 3424.909    0.000 layers.py:538(check)
               86980951  181.154    0.000 3415.534    0.000 linear.py:93(forward)
               51169150  512.221    0.000 3352.389    0.000 level.py:41(notUsed)
               86980951   72.352    0.000 3134.363    0.000 functional.py:1737(linear)
               86980951 3044.868    0.000 3044.868    0.000 {built-in method torch._C._nn.linear}
                2372674 1732.237    0.001 2385.968    0.001 replaybuffer.py:73(CF_save_data)
              233707803 2302.089    0.000 2302.089    0.000 {built-in method clone}
                2372674 1347.832    0.001 1949.434    0.001 agent.py:67(modify)
               14101363   93.486    0.000 1848.821    0.000 agent.py:59(modify_board)
              117556384  101.019    0.000 1845.327    0.000 activation.py:713(forward)
                6983374 1522.339    0.000 1789.776    0.000 agent.py:187(convert_values)
              117556384  102.290    0.000 1744.309    0.000 functional.py:1364(leaky_relu)
             6481026610 1168.138    0.000 1685.873    0.000 enum.py:646(__hash__)
              238274209  188.945    0.000 1683.373    0.000 {built-in method builtins.any}
              234519526  327.621    0.000 1658.212    0.000 layers.py:838(isFree)
              117556384 1621.699    0.000 1621.699    0.000 {built-in method torch._C._nn.leaky_relu}
               51169150   43.314    0.000 1564.653    0.000 level.py:38(elementsIn)
             1613970698  468.167    0.000 1494.961    0.000 layers.py:809(<genexpr>)
               37828103 1386.027    0.000 1386.027    0.000 {built-in method cat}
             1364556158 1111.837    0.000 1330.592    0.000 layer.py:103(isFree)
               14101363 1209.534    0.000 1209.534    0.000 {built-in method torch._C._nn.one_hot}
                2372674   40.690    0.000 1095.524    0.000 agent.py:172(__call__)
               51169150  517.724    0.000 1023.375    0.000 level.py:39(<listcomp>)
                2372674   37.762    0.000 1015.695    0.000 agent.py:112(__call__)
             2174545114  977.432    0.000  977.432    0.000 layer.py:154(elements)
              132869744  945.739    0.000  945.739    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              231156188  587.532    0.000  934.706    0.000 layers.py:575(isDead)
              132869744  836.421    0.000  836.421    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                7118022  145.646    0.000  833.606    0.000 optimizer.py:189(zero_grad)
             2183077407  816.657    0.000  816.657    0.000 level.py:32(inverse)
               55914498  315.117    0.000  813.052    0.000 random.py:315(sample)
              234519526  576.738    0.000  809.650    0.000 layers.py:77(check)
               61402980   77.875    0.000  770.427    0.000 layer.py:77(restart)
              588596457  585.354    0.000  754.947    0.000 layer.py:134(remove)
               11728689  281.665    0.000  750.787    0.000 exploration.py:53(softmaxer)
               61526639  666.331    0.000  666.331    0.000 {method 'item' of 'torch._C._TensorBase' objects}
              349109254  127.020    0.000  635.982    0.000 random.py:244(randint)
             7714311170  545.019    0.000  615.041    0.000 {built-in method builtins.len}
              814669003  426.181    0.000  614.929    0.000 random.py:250(_randbelow_with_getrandbits)
             1043889136  427.405    0.000  575.422    0.000 layer.py:138(add)
                2372674   40.047    0.000  553.143    0.000 replaybuffer.py:18(stacker)
               66434872  548.197    0.000  548.197    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                2372674   42.879    0.000  539.630    0.000 replaybuffer.py:63(stacker)
               10233830  267.946    0.000  536.130    0.000 layers.py:36(reset)
              250181840  518.888    0.000  518.888    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
             6481053857  517.741    0.000  517.741    0.000 {built-in method builtins.hash}
             2640328155  511.218    0.000  511.218    0.000 enum.py:352(<genexpr>)
              349109254  211.218    0.000  508.962    0.000 random.py:200(randrange)
               51169150  307.862    0.000  497.964    0.000 {built-in method _functools.reduce}
               66434872  485.532    0.000  485.532    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
             4780113217  445.568    0.000  445.568    0.000 layer.py:99(positions)
               66434872  444.927    0.000  444.927    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               66434872  438.855    0.000  438.855    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               10233830  200.306    0.000  412.332    0.000 level.py:16(<dictcomp>)
              234519526  265.647    0.000  398.866    0.000 layers.py:48(check)
              234519526  138.185    0.000  392.612    0.000 layers.py:572(<listcomp>)
              465044104  314.023    0.000  391.315    0.000 tensor.py:906(grad)
                2372674  218.119    0.000  371.122    0.000 collector.py:46(collect)
              237267400   58.558    0.000  367.080    0.000 {built-in method builtins.all}
              546576362  147.469    0.000  339.907    0.000 layers.py:799(<genexpr>)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9632959: <MonsterLevel_Conver4_3counterfactsNOCRASH_2_1> in cluster <dcc> Done

Job <MonsterLevel_Conver4_3counterfactsNOCRASH_2_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed May 12 15:41:02 2021
Job was executed on host(s) <n-62-20-13>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Thu May 13 16:28:34 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu May 13 16:28:34 2021
Terminated at Fri May 14 16:23:49 2021
Results reported at Fri May 14 16:23:49 2021

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

    CPU time :                                   85874.46 sec.
    Max Memory :                                 7899 MB
    Average Memory :                             5628.02 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               8485.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86115 sec.
    Turnaround time :                            175367 sec.

The output (if any) is above this job summary.

