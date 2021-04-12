
# Parameters

    Name :                      MONTEST_CF_6c2-0
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
    Cf convert :                6
    Counterfacts :              2
    Topn :                      7
    Minutes used :              1315 minutes.
    Hours used :                21 hours.

# Profiling


      58127109298 function calls (57825695051 primitive calls) in 78920.07 seconds

##    Ordered by: cumulative time
   List reduced from 506 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 78920.069 78920.069 {built-in method builtins.exec}
                      1    5.338    5.338 78920.069 78920.069 <string>:1(<module>)
                      1  223.010  223.010 78914.730 78914.730 main.py:95(CFagent)
                7205724   36.590    0.000 19288.300    0.003 agent.py:29(learn)
                2401908   14.971    0.000 18935.927    0.008 game.py:41(step)
                2401908   16.455    0.000 18397.385    0.008 layers.py:710(step)
                2401908 2984.823    0.001 17018.422    0.007 agent.py:217(counterfact)
                7205724  509.899    0.000 15496.570    0.002 learner.py:42(Qlearn)
        334536629/33124073 1445.732    0.000 11500.619    0.000 module.py:866(_call_impl)
               25918349   74.497    0.000 10808.209    0.000 network.py:24(forward)
               25918349  351.566    0.000 10550.650    0.000 container.py:117(forward)
                2401909  396.794    0.000 10188.880    0.004 layers.py:676(update)
                2401908  238.652    0.000 8166.127    0.003 layers.py:17(step)
              224929689  703.158    0.000 7905.175    0.000 layer.py:98(move)
                2401908  313.300    0.000 7516.601    0.003 agent.py:54(_learn)
                2401908  305.768    0.000 6813.695    0.003 agent.py:209(_learn)
                4552524  103.413    0.000 6525.569    0.001 agent.py:172(choose_action)
                9356285  305.063    0.000 6454.438    0.001 agent.py:49(__call__)
                7205724   81.064    0.000 5863.083    0.001 optimizer.py:84(wrapper)
                7205724   39.424    0.000 5528.240    0.001 grad_mode.py:24(decorate_context)
                2401908 3185.387    0.001 5418.401    0.002 replaybuffer.py:28(teleporter_save_data)
                7205724  253.639    0.000 5399.714    0.001 adam.py:55(step)
                9083858   83.974    0.000 5125.860    0.001 layers.py:731(restart)
              224929689  507.578    0.000 5003.655    0.000 layers.py:727(check)
                2401908   83.734    0.000 4903.318    0.002 agent.py:117(_learn)
                7205724 1132.078    0.000 4883.875    0.001 _functional.py:53(adam)
               61963595 4843.355    0.000 4843.355    0.000 {built-in method tensor}
               56346946   38.239    0.000 4713.107    0.000 game.py:37(board)
                2401908 3809.306    0.002 4705.083    0.002 replaybuffer.py:22(sample_data)
                9083858   40.819    0.000 4340.882    0.000 level.py:8(__init__)
               43234350 2773.004    0.000 4255.228    0.000 layer.py:151(update)
                2401908 3387.376    0.001 4177.374    0.002 replaybuffer.py:49(sample_data)
                7205724   37.795    0.000 4169.815    0.001 tensor.py:195(backward)
                7205724   39.455    0.000 4130.923    0.001 __init__.py:68(backward)
                9083858  685.857    0.000 3955.059    0.000 levels.py:418(generate)
               51836698  125.313    0.000 3929.037    0.000 conv.py:398(forward)
                7205724 3917.831    0.001 3917.831    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2401908 2266.234    0.001 3862.013    0.002 agent.py:88(interveen)
               51836698   83.527    0.000 3746.151    0.000 conv.py:390(_conv_forward)
               51836698 3662.624    0.000 3662.624    0.000 {built-in method conv2d}
              224929689 1906.267    0.000 3238.357    0.000 layers.py:531(check)
               72951231  155.605    0.000 2972.294    0.000 linear.py:93(forward)
               72951231   62.326    0.000 2736.065    0.000 functional.py:1737(linear)
               72951231 2658.040    0.000 2658.040    0.000 {built-in method torch._C._nn.linear}
               45419290  415.021    0.000 2591.736    0.000 level.py:41(notUsed)
              239715296 2358.701    0.000 2358.701    0.000 {built-in method clone}
                2401908 1389.021    0.001 2068.747    0.001 agent.py:67(modify)
              224854074  280.115    0.000 1714.713    0.000 layers.py:721(isFree)
               11758193   90.590    0.000 1660.767    0.000 agent.py:59(modify_board)
              241122377  189.914    0.000 1659.246    0.000 {built-in method builtins.any}
               98869580   85.373    0.000 1546.107    0.000 activation.py:713(forward)
                2401908  805.803    0.000 1539.086    0.001 replaybuffer.py:55(CF_save_data)
               38179181 1492.131    0.000 1492.131    0.000 {built-in method cat}
             1643806884  484.988    0.000 1469.978    0.000 layers.py:692(<genexpr>)
               98869580   84.319    0.000 1460.734    0.000 functional.py:1364(leaky_relu)
             5765203942  998.190    0.000 1450.467    0.000 enum.py:646(__hash__)
             1233697760 1236.263    0.000 1434.597    0.000 layer.py:95(isFree)
               98869580 1360.095    0.000 1360.095    0.000 {built-in method torch._C._nn.leaky_relu}
                4552524 1122.191    0.000 1316.422    0.000 agent.py:183(convert_values)
                2401908   52.422    0.000 1206.680    0.001 agent.py:168(__call__)
               45419290   37.244    0.000 1123.009    0.000 level.py:38(elementsIn)
               11758193 1095.353    0.000 1095.353    0.000 {built-in method torch._C._nn.one_hot}
                2401908   51.761    0.000 1092.670    0.000 agent.py:112(__call__)
              134506848  945.409    0.000  945.409    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
             1946039780  933.679    0.000  933.679    0.000 layer.py:146(elements)
              236318560  565.028    0.000  894.873    0.000 layers.py:568(isDead)
              240190900  108.199    0.000  872.444    0.000 {built-in method builtins.all}
                7205724  158.010    0.000  840.501    0.000 optimizer.py:189(zero_grad)
              134506848  828.254    0.000  828.254    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               50223106  315.546    0.000  804.670    0.000 random.py:315(sample)
             1051537366  306.327    0.000  795.311    0.000 layers.py:682(<genexpr>)
              224929689  563.846    0.000  776.183    0.000 layers.py:71(check)
             1937780829  720.900    0.000  720.900    0.000 level.py:32(inverse)
               45419290  353.232    0.000  712.172    0.000 level.py:39(<listcomp>)
                2401908   50.387    0.000  695.818    0.000 replaybuffer.py:18(stacker)
               54503148   68.916    0.000  681.587    0.000 layer.py:69(restart)
                9356285  238.450    0.000  669.483    0.000 exploration.py:53(softmaxer)
              528007987  478.380    0.000  637.386    0.000 layer.py:126(remove)
                2401908   49.307    0.000  595.505    0.000 replaybuffer.py:45(stacker)
              315383864  114.510    0.000  562.354    0.000 random.py:244(randint)
              758219572  379.983    0.000  555.302    0.000 random.py:250(_randbelow_with_getrandbits)
               67253424  547.163    0.000  547.163    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              253875397  512.029    0.000  512.029    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              939737439  374.446    0.000  510.663    0.000 layer.py:130(add)
               67253424  497.439    0.000  497.439    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                9083958  236.098    0.000  469.476    0.000 layers.py:30(reset)
               67253424  463.040    0.000  463.040    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
        5524841998/5524841995  391.440    0.000  455.171    0.000 {built-in method builtins.len}
             5765231525  452.282    0.000  452.282    0.000 {built-in method builtins.hash}
               67253424  451.364    0.000  451.364    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              315383864  191.050    0.000  447.844    0.000 random.py:200(randrange)
               36439967  443.070    0.000  443.070    0.000 {method 'item' of 'torch._C._TensorBase' objects}
              240190900  297.674    0.000  426.283    0.000 layers.py:107(isDone)
              224929689  293.909    0.000  420.554    0.000 layers.py:42(check)
             4525875205  415.461    0.000  415.461    0.000 layer.py:91(positions)
              470774052  321.295    0.000  397.368    0.000 tensor.py:906(grad)
                7205724   14.735    0.000  383.114    0.000 loss.py:527(forward)
                2401908  221.849    0.000  379.631    0.000 collector.py:53(collect)
               45419290  229.859    0.000  373.593    0.000 {built-in method _functools.reduce}
                7205724   39.240    0.000  368.379    0.000 functional.py:2898(mse_loss)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-12>
Subject: Job 9507481: <MONTEST_CF_6c2_0> in cluster <dcc> Done

Job <MONTEST_CF_6c2_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sat Apr 10 02:36:50 2021
Job was executed on host(s) <n-62-20-12>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Apr 11 02:59:41 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun Apr 11 02:59:41 2021
Terminated at Mon Apr 12 00:55:12 2021
Results reported at Mon Apr 12 00:55:12 2021

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

    CPU time :                                   78724.98 sec.
    Max Memory :                                 8081 MB
    Average Memory :                             5850.54 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               8303.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   78932 sec.
    Turnaround time :                            166702 sec.

The output (if any) is above this job summary.

