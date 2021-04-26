
# Parameters

    Name :                      Causal4_Cf_convert2_TopN3-1
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


      70426048048 function calls (70121556857 primitive calls) in 86117.03 seconds

##    Ordered by: cumulative time
   List reduced from 514 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86117.032 86117.032 {built-in method builtins.exec}
                      1    3.927    3.927 86117.032 86117.032 <string>:1(<module>)
                      1  315.062  315.062 86113.105 86113.105 main.py:79(CFagent)
                9639063   34.875    0.000 28474.360    0.003 agent.py:29(learn)
                9639061  707.858    0.000 23860.851    0.002 learner.py:42(Qlearn)
                3213021   14.639    0.000 19213.433    0.006 game.py:41(step)
                3213021   20.652    0.000 18430.911    0.006 layers.py:718(step)
        340573693/36084193 1351.710    0.000 12185.031    0.000 module.py:866(_call_impl)
                3213021  264.833    0.000 11764.323    0.004 layers.py:17(step)
              321302100  816.325    0.000 11473.975    0.000 layer.py:98(move)
               26445132   72.035    0.000 11429.580    0.000 network.py:27(forward)
               26445132  349.440    0.000 11197.302    0.000 container.py:117(forward)
                3213021  301.435    0.000 10963.229    0.003 agent.py:54(_learn)
                3213021 1143.093    0.000 10767.070    0.003 agent.py:210(counterfact)
                3213021  298.986    0.000 10165.637    0.003 agent.py:202(_learn)
                9639061   79.535    0.000 10143.500    0.001 optimizer.py:84(wrapper)
                9639061   39.106    0.000 9752.902    0.001 grad_mode.py:24(decorate_context)
                9639061  278.601    0.000 9623.935    0.001 adam.py:55(step)
                9639061 1951.515    0.000 9040.737    0.001 _functional.py:53(adam)
                3213021   87.320    0.000 7291.370    0.002 agent.py:117(_learn)
              321302100 1399.540    0.000 7211.985    0.000 layers.py:735(check)
                3213022  439.240    0.000 6620.475    0.002 layers.py:684(update)
                9639061   48.133    0.000 6052.077    0.001 tensor.py:195(backward)
                9639061   35.964    0.000 6002.414    0.001 __init__.py:68(backward)
                8400798  193.347    0.000 5897.957    0.001 agent.py:49(__call__)
                9639061 5755.112    0.001 5755.112    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3213021 4531.531    0.001 5522.371    0.002 replaybuffer.py:22(sample_data)
               52175707 5500.454    0.000 5500.454    0.000 {built-in method tensor}
               44769250   29.160    0.000 5290.835    0.000 game.py:37(board)
                3213021 4300.531    0.001 5274.018    0.002 replaybuffer.py:67(sample_data)
                3213021 2551.582    0.001 4785.125    0.001 replaybuffer.py:28(teleporter_save_data)
                3213021 2460.333    0.001 4705.785    0.001 agent.py:88(interveen)
               52890264  113.159    0.000 4040.141    0.000 conv.py:398(forward)
               64260430 2308.379    0.000 3958.822    0.000 layer.py:151(update)
               52890264   68.981    0.000 3873.798    0.000 conv.py:390(_conv_forward)
               52890264 3804.817    0.000 3804.817    0.000 {built-in method conv2d}
               72909354  140.732    0.000 3255.257    0.000 linear.py:93(forward)
               72909354   57.912    0.000 3044.214    0.000 functional.py:1737(linear)
               72909354 2971.383    0.000 2971.383    0.000 {built-in method torch._C._nn.linear}
                1979233   45.187    0.000 2969.120    0.002 agent.py:175(choose_action)
              321302100  539.624    0.000 2884.385    0.000 layers.py:729(isFree)
                3213021 1858.038    0.001 2781.842    0.001 agent.py:67(modify)
             2782118134 1940.924    0.000 2344.762    0.000 layer.py:95(isFree)
              167860052 2165.325    0.000 2165.325    0.000 {built-in method clone}
              179929136 1856.192    0.000 1856.192    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               99354486   75.457    0.000 1798.161    0.000 activation.py:713(forward)
               99354486   79.676    0.000 1722.703    0.000 functional.py:1364(leaky_relu)
               43744019 1714.061    0.000 1714.061    0.000 {built-in method cat}
               11613819   80.226    0.000 1671.329    0.000 agent.py:59(modify_board)
               99354486 1625.503    0.000 1625.503    0.000 {built-in method torch._C._nn.leaky_relu}
              179929136 1625.121    0.000 1625.121    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                3213021 1196.391    0.000 1582.239    0.000 replaybuffer.py:73(CF_save_data)
                3213019   51.947    0.000 1571.466    0.000 agent.py:171(__call__)
             6248815788 1054.190    0.000 1509.731    0.000 enum.py:646(__hash__)
                3213021   48.986    0.000 1467.880    0.000 agent.py:112(__call__)
                4233768   48.367    0.000 1445.598    0.000 layers.py:740(restart)
                9639061  219.333    0.000 1400.911    0.000 optimizer.py:189(zero_grad)
              320281454  308.890    0.000 1383.338    0.000 {built-in method builtins.any}
              321302100  854.439    0.000 1127.177    0.000 layers.py:77(check)
              321302200  190.479    0.000 1101.835    0.000 {built-in method builtins.all}
             3487752752  890.640    0.000 1074.449    0.000 layers.py:700(<genexpr>)
               11613819 1065.411    0.000 1065.411    0.000 {built-in method torch._C._nn.one_hot}
               89964568 1042.623    0.000 1042.623    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                4233768   21.838    0.000 1021.071    0.000 level.py:8(__init__)
              321302100  637.773    0.000 1015.973    0.000 layers.py:246(check)
              321302100  578.022    0.000  955.367    0.000 layers.py:286(check)
             2354833252  552.875    0.000  947.140    0.000 layers.py:690(<genexpr>)
             1235459312  930.728    0.000  930.728    0.000 layer.py:146(elements)
               89964568  865.961    0.000  865.961    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               89964568  841.804    0.000  841.804    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               89964568  829.219    0.000  829.219    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                4233768  132.638    0.000  815.374    0.000 levels.py:199(generate)
                3213021   63.008    0.000  771.364    0.000 replaybuffer.py:18(stacker)
                3213019   62.622    0.000  758.434    0.000 replaybuffer.py:63(stacker)
             7941821656  673.285    0.000  673.285    0.000 layer.py:91(positions)
                3213021  397.025    0.000  655.967    0.000 collector.py:46(collect)
               89964568  645.686    0.000  645.686    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              321302100  480.138    0.000  634.477    0.000 layers.py:62(check)
                8400798  222.702    0.000  612.338    0.000 exploration.py:53(softmaxer)
        8445401649/8445401646  542.799    0.000  603.975    0.000 {built-in method builtins.len}
                1979233  501.226    0.000  569.004    0.000 agent.py:186(convert_values)
                8467536   64.261    0.000  555.190    0.000 level.py:41(notUsed)
              182686890  549.771    0.000  549.771    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              321302100  353.143    0.000  546.067    0.000 layers.py:313(check)
              629752060  417.496    0.000  516.089    0.000 tensor.py:906(grad)
              321302100  324.931    0.000  503.802    0.000 layers.py:273(check)
               14893578  183.927    0.000  484.049    0.000 random.py:315(sample)
                9639061   14.076    0.000  459.919    0.000 loss.py:527(forward)
             6248852443  455.547    0.000  455.547    0.000 {built-in method builtins.hash}
                9639061   33.575    0.000  445.843    0.000 functional.py:2898(mse_loss)
              321302100  273.615    0.000  407.437    0.000 layers.py:48(check)
               42337680   53.611    0.000  362.910    0.000 layer.py:69(restart)
              321302100  228.135    0.000  330.982    0.000 layers.py:23(check)
              312432580  223.496    0.000  301.292    0.000 layer.py:126(remove)
               52890264   35.047    0.000  296.788    0.000 flatten.py:39(forward)
                9639061  294.060    0.000  294.060    0.000 {built-in method torch._C._nn.mse_loss}
              555041112  207.867    0.000  283.671    0.000 layer.py:130(add)
               19278126  278.205    0.000  278.205    0.000 {built-in method sum}
                6426044  269.780    0.000  269.780    0.000 {built-in method nonzero}
             3550237425  264.534    0.000  264.534    0.000 {method 'random' of '_random.Random' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9551813: <Causal4_Cf_convert2_TopN3_1> in cluster <dcc> Done

Job <Causal4_Cf_convert2_TopN3_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed Apr 21 03:20:31 2021
Job was executed on host(s) <n-62-20-7>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Thu Apr 22 03:12:11 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Apr 22 03:12:11 2021
Terminated at Fri Apr 23 03:07:34 2021
Results reported at Fri Apr 23 03:07:34 2021

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

    CPU time :                                   86096.12 sec.
    Max Memory :                                 3452 MB
    Average Memory :                             3412.55 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               12932.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86124 sec.
    Turnaround time :                            172023 sec.

The output (if any) is above this job summary.

