
# Parameters

    Name :                      MONTEST_CF_6c1-0
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
    Counterfacts :              1
    Topn :                      7
    Minutes used :              1315 minutes.
    Hours used :                21 hours.

# Profiling


      59465485483 function calls (59193639724 primitive calls) in 78916.86 seconds

##    Ordered by: cumulative time
   List reduced from 506 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 78916.858 78916.858 {built-in method builtins.exec}
                      1    4.656    4.656 78916.858 78916.858 <string>:1(<module>)
                      1  214.990  214.990 78912.202 78912.202 main.py:95(CFagent)
                7964547   31.213    0.000 24017.320    0.003 agent.py:29(learn)
                7964547  607.899    0.000 19951.996    0.003 learner.py:42(Qlearn)
                2654849   13.449    0.000 18573.715    0.007 game.py:41(step)
                2654849   17.192    0.000 18006.339    0.007 layers.py:710(step)
        303347237/31503169 1267.260    0.000 11298.171    0.000 module.py:866(_call_impl)
               23538622   63.182    0.000 10630.978    0.000 network.py:24(forward)
               23538622  341.470    0.000 10415.394    0.000 container.py:117(forward)
                2654849 1640.978    0.001 9672.663    0.004 agent.py:217(counterfact)
                2654850  399.592    0.000 9491.380    0.004 layers.py:676(update)
                2654849  288.607    0.000 9265.270    0.003 agent.py:54(_learn)
                2654849  288.265    0.000 8602.620    0.003 agent.py:209(_learn)
                2654849  236.630    0.000 8472.810    0.003 layers.py:17(step)
                7964547   73.005    0.000 8380.782    0.001 optimizer.py:84(wrapper)
              257624869  723.720    0.000 8209.312    0.000 layer.py:98(move)
                7964547   34.192    0.000 8046.121    0.001 grad_mode.py:24(decorate_context)
                7964547  241.119    0.000 7934.774    0.001 adam.py:55(step)
                7964547 1624.813    0.000 7431.470    0.001 _functional.py:53(adam)
                2654849 3832.478    0.001 7138.860    0.003 replaybuffer.py:28(teleporter_save_data)
                2654849   83.282    0.000 6099.439    0.002 agent.py:117(_learn)
                7787004  220.053    0.000 5671.356    0.001 agent.py:49(__call__)
              257624869  510.119    0.000 5174.780    0.000 layers.py:727(check)
                7964547   34.329    0.000 4995.986    0.001 tensor.py:195(backward)
                7964547   31.123    0.000 4960.505    0.001 __init__.py:68(backward)
                2654849 2957.300    0.001 4881.756    0.002 agent.py:88(interveen)
                7964547 4752.661    0.001 4752.661    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                9096647   73.128    0.000 4737.781    0.001 layers.py:731(restart)
                2654849 3275.594    0.001 4239.667    0.002 replaybuffer.py:22(sample_data)
                9096647   35.693    0.000 4016.315    0.000 level.py:8(__init__)
                2477373   59.489    0.000 3934.986    0.002 agent.py:172(choose_action)
                2654849 2968.630    0.001 3826.310    0.001 replaybuffer.py:49(sample_data)
               47077244  101.404    0.000 3732.324    0.000 conv.py:398(forward)
                9096647  642.606    0.000 3665.337    0.000 levels.py:418(generate)
               47077244   66.731    0.000 3582.969    0.000 conv.py:390(_conv_forward)
               47077244 3516.238    0.000 3516.238    0.000 {built-in method conv2d}
              257624869 1961.616    0.000 3385.827    0.000 layers.py:531(check)
              260485719 3339.742    0.000 3339.742    0.000 {built-in method clone}
               31858194 2130.678    0.000 3146.429    0.000 layer.py:151(update)
               65306168  135.236    0.000 3019.163    0.000 linear.py:93(forward)
               38988866 2963.885    0.000 2963.885    0.000 {built-in method tensor}
               65306168   53.568    0.000 2819.084    0.000 functional.py:1737(linear)
               32812810   26.916    0.000 2790.193    0.000 game.py:37(board)
               65306168 2752.505    0.000 2752.505    0.000 {built-in method torch._C._nn.linear}
                2654849 1723.556    0.001 2495.651    0.001 agent.py:67(modify)
               45483235  388.566    0.000 2398.395    0.000 level.py:41(notUsed)
              257571203  310.951    0.000 1800.663    0.000 layers.py:721(isFree)
                2654849  872.908    0.000 1796.848    0.001 replaybuffer.py:55(CF_save_data)
               88844790   77.742    0.000 1692.597    0.000 activation.py:713(forward)
              264807689  189.831    0.000 1689.207    0.000 {built-in method builtins.any}
               39645192 1634.652    0.000 1634.652    0.000 {built-in method cat}
               88844790   73.653    0.000 1614.855    0.000 functional.py:1364(leaky_relu)
              148671544 1528.466    0.000 1528.466    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               88844790 1525.959    0.000 1525.959    0.000 {built-in method torch._C._nn.leaky_relu}
               10441853   74.782    0.000 1516.130    0.000 agent.py:59(modify_board)
             1823540901  466.958    0.000 1500.047    0.000 layers.py:692(<genexpr>)
             1512647187 1265.718    0.000 1489.712    0.000 layer.py:95(isFree)
             6141011593 1001.160    0.000 1428.925    0.000 enum.py:646(__hash__)
                2654849   51.774    0.000 1368.266    0.001 agent.py:168(__call__)
              148671544 1329.733    0.000 1329.733    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                2654849   50.481    0.000 1285.358    0.000 agent.py:112(__call__)
                7964547  189.327    0.000 1157.088    0.000 optimizer.py:189(zero_grad)
               45483235   34.344    0.000 1038.238    0.000 level.py:38(elementsIn)
               10441853  966.684    0.000  966.684    0.000 {built-in method torch._C._nn.one_hot}
              262152839  589.070    0.000  937.186    0.000 layers.py:568(isDead)
               74335772  831.521    0.000  831.521    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                2477373  696.176    0.000  824.068    0.000 agent.py:183(convert_values)
              273582421  816.088    0.000  816.088    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              257624869  574.389    0.000  796.253    0.000 layers.py:71(check)
                2654849   54.484    0.000  779.078    0.000 replaybuffer.py:18(stacker)
               50792933  288.754    0.000  741.099    0.000 random.py:315(sample)
               74335772  727.306    0.000  727.306    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               74335772  684.867    0.000  684.867    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               74335772  682.999    0.000  682.999    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                2654849   53.787    0.000  678.803    0.000 replaybuffer.py:45(stacker)
             1940498487  660.373    0.000  660.373    0.000 level.py:32(inverse)
             2078967462  659.792    0.000  659.792    0.000 layer.py:146(elements)
               45483235  328.326    0.000  656.487    0.000 level.py:39(<listcomp>)
               54579882   66.183    0.000  630.836    0.000 layer.py:69(restart)
              265485000   56.504    0.000  590.349    0.000 {built-in method builtins.all}
                7787004  213.202    0.000  585.832    0.000 exploration.py:53(softmaxer)
              368239517  120.162    0.000  582.521    0.000 random.py:244(randint)
              569637867  129.591    0.000  566.548    0.000 layers.py:682(<genexpr>)
              604458232  399.867    0.000  555.820    0.000 layer.py:126(remove)
              836657851  384.767    0.000  553.843    0.000 random.py:250(_randbelow_with_getrandbits)
                2654849  328.948    0.000  544.280    0.000 collector.py:53(collect)
               74335772  524.635    0.000  524.635    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
             1018532353  388.034    0.000  520.106    0.000 layer.py:130(add)
              368239517  192.790    0.000  462.359    0.000 random.py:200(randrange)
              520350488  352.792    0.000  434.095    0.000 tensor.py:906(grad)
             5128535654  431.836    0.000  431.836    0.000 layer.py:91(positions)
                9096747  218.035    0.000  431.224    0.000 layers.py:30(reset)
             6141041976  427.770    0.000  427.770    0.000 {built-in method builtins.hash}
              265485000  294.896    0.000  423.616    0.000 layers.py:107(isDone)
              257624869  291.984    0.000  417.834    0.000 layers.py:42(check)
                7964547   13.577    0.000  393.599    0.000 loss.py:527(forward)
                7964547   30.468    0.000  380.022    0.000 functional.py:2898(mse_loss)
              257624869  129.822    0.000  372.013    0.000 layers.py:565(<listcomp>)
        4160832411/4160832408  306.918    0.000  360.603    0.000 {built-in method builtins.len}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-5>
Subject: Job 9507479: <MONTEST_CF_6c1_0> in cluster <dcc> Done

Job <MONTEST_CF_6c1_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sat Apr 10 02:36:50 2021
Job was executed on host(s) <n-62-20-5>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Apr 11 00:38:43 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun Apr 11 00:38:43 2021
Terminated at Sun Apr 11 22:34:09 2021
Results reported at Sun Apr 11 22:34:09 2021

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

    CPU time :                                   78717.70 sec.
    Max Memory :                                 8582 MB
    Average Memory :                             6090.37 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               7802.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   78928 sec.
    Turnaround time :                            158239 sec.

The output (if any) is above this job summary.

