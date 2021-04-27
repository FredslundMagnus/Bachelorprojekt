
# Parameters

    Name :                      Coconuts_convert4_TEST-0
    Main :                      CFagent
    Level :                     Levels.Coconuts
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
    Cf convert :                4
    Counterfacts :              1
    Topn :                      3
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      67850494120 function calls (67516617405 primitive calls) in 86110.96 seconds

##    Ordered by: cumulative time
   List reduced from 512 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86110.959 86110.959 {built-in method builtins.exec}
                      1    4.478    4.478 86110.959 86110.959 <string>:1(<module>)
                      1  409.090  409.090 86106.480 86106.480 main.py:79(CFagent)
               11211231   42.709    0.000 28282.946    0.003 agent.py:29(learn)
               11211230  710.051    0.000 23031.023    0.002 learner.py:42(Qlearn)
                3737077   17.579    0.000 21983.390    0.006 game.py:41(step)
                3737077   22.062    0.000 21212.379    0.006 layers.py:718(step)
                3737077  352.372    0.000 14575.893    0.004 layers.py:17(step)
              373420657 1408.526    0.000 14186.754    0.000 layer.py:98(move)
        374154865/40279841 1540.517    0.000 12615.668    0.000 module.py:866(_call_impl)
               29068611   84.313    0.000 11772.667    0.000 network.py:27(forward)
               29068611  385.025    0.000 11494.833    0.000 container.py:117(forward)
                3737077  399.901    0.000 10988.410    0.003 agent.py:54(_learn)
                3737077  394.539    0.000 10091.023    0.003 agent.py:204(_learn)
               11211230   99.321    0.000 9017.578    0.001 optimizer.py:84(wrapper)
              373420657 1500.287    0.000 8757.505    0.000 layers.py:735(check)
               11211230   49.838    0.000 8582.302    0.001 grad_mode.py:24(decorate_context)
               11211230  349.669    0.000 8420.883    0.001 adam.py:55(step)
               11211230 1751.148    0.000 7676.004    0.001 _functional.py:53(adam)
                3737077  116.682    0.000 7128.463    0.002 agent.py:117(_learn)
                3737077  529.054    0.000 7112.677    0.002 agent.py:212(counterfact)
                3737078  562.187    0.000 6582.639    0.002 layers.py:684(update)
                3737077 5292.606    0.001 6462.637    0.002 replaybuffer.py:22(sample_data)
                3737077 5061.580    0.001 6188.261    0.002 replaybuffer.py:67(sample_data)
               11211230   45.457    0.000 5982.933    0.001 tensor.py:195(backward)
               11211230   44.964    0.000 5935.830    0.001 __init__.py:68(backward)
                8924373  236.316    0.000 5917.699    0.001 agent.py:49(__call__)
               11211230 5664.473    0.001 5664.473    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3737077 2231.235    0.001 4684.673    0.001 agent.py:88(interveen)
                3737077 2510.367    0.001 4459.925    0.001 replaybuffer.py:28(teleporter_save_data)
               58137222  134.701    0.000 4272.388    0.000 conv.py:398(forward)
               58137222   89.134    0.000 4073.773    0.000 conv.py:390(_conv_forward)
               58137222 3984.639    0.000 3984.639    0.000 {built-in method conv2d}
               52319085 2178.173    0.000 3667.269    0.000 layer.py:151(update)
               45722086 3592.739    0.000 3592.739    0.000 {built-in method tensor}
               37158144   25.021    0.000 3375.163    0.000 game.py:37(board)
               79731679  164.424    0.000 3229.242    0.000 linear.py:93(forward)
              373420657  559.172    0.000 3030.795    0.000 layers.py:729(isFree)
               79731679   67.312    0.000 2979.437    0.000 functional.py:1737(linear)
               79731679 2895.860    0.000 2895.860    0.000 {built-in method torch._C._nn.linear}
                3737077 1819.331    0.000 2775.033    0.001 agent.py:67(modify)
              373420657 1786.728    0.000 2539.206    0.000 layers.py:471(check)
             2453510377 2046.792    0.000 2471.623    0.000 layer.py:95(isFree)
              373420657 1668.994    0.000 2321.283    0.000 layers.py:77(check)
                1458855   30.805    0.000 2067.592    0.001 agent.py:176(choose_action)
               50032215 1889.717    0.000 1889.717    0.000 {built-in method cat}
              174778954 1796.171    0.000 1796.171    0.000 {built-in method clone}
              108800290  101.780    0.000 1733.290    0.000 activation.py:713(forward)
                3737076   64.924    0.000 1725.061    0.000 agent.py:172(__call__)
             6315520826 1184.430    0.000 1717.635    0.000 enum.py:646(__hash__)
               12661450   85.731    0.000 1683.983    0.000 agent.py:59(modify_board)
              108800290   92.726    0.000 1631.510    0.000 functional.py:1364(leaky_relu)
                3737077   60.841    0.000 1631.060    0.000 agent.py:112(__call__)
                2065598   25.469    0.000 1563.012    0.001 layers.py:740(restart)
              108800290 1520.664    0.000 1520.664    0.000 {built-in method torch._C._nn.leaky_relu}
              209276292 1507.818    0.000 1507.818    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              375379280  314.539    0.000 1340.418    0.000 {built-in method builtins.any}
              209276292 1329.155    0.000 1329.155    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               11211230  234.640    0.000 1327.098    0.000 optimizer.py:189(zero_grad)
                2065598   12.128    0.000 1315.763    0.001 level.py:8(__init__)
                2065598   87.444    0.000 1199.765    0.001 levels.py:262(generate)
               12661450 1100.197    0.000 1100.197    0.000 {built-in method torch._C._nn.one_hot}
              373420657  815.645    0.000 1070.748    0.000 layers.py:62(check)
               18423818  178.174    0.000 1036.522    0.000 level.py:41(notUsed)
             2973137616  844.925    0.000 1025.879    0.000 layers.py:700(<genexpr>)
                3737077  817.484    0.000  994.648    0.000 replaybuffer.py:73(CF_save_data)
             8707617368  941.078    0.000  941.078    0.000 layer.py:91(positions)
              373707800   78.115    0.000  928.624    0.000 {built-in method builtins.all}
              803473930  195.214    0.000  899.743    0.000 layers.py:690(<genexpr>)
                3737077   68.996    0.000  886.294    0.000 replaybuffer.py:18(stacker)
              104638146  885.662    0.000  885.662    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                3737076   71.158    0.000  852.051    0.000 replaybuffer.py:63(stacker)
             1124614063  835.306    0.000  835.306    0.000 layer.py:146(elements)
              104638146  763.897    0.000  763.897    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              104638146  715.925    0.000  715.925    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              104638146  692.444    0.000  692.444    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              373707800  467.772    0.000  689.775    0.000 layers.py:113(isDone)
              732467106  504.232    0.000  624.560    0.000 tensor.py:906(grad)
        7579376930/7579376927  546.680    0.000  615.931    0.000 {built-in method builtins.len}
                3737077  348.798    0.000  590.980    0.000 collector.py:46(collect)
                8924373  219.867    0.000  589.917    0.000 exploration.py:53(softmaxer)
              373420657  396.931    0.000  588.992    0.000 layers.py:48(check)
                7474154  205.145    0.000  544.112    0.000 random.py:315(sample)
             6315563305  533.213    0.000  533.213    0.000 {built-in method builtins.hash}
              104638146  524.976    0.000  524.976    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               11211230   17.076    0.000  496.084    0.000 loss.py:527(forward)
               11211230   45.763    0.000  479.007    0.000 functional.py:2898(mse_loss)
               18423818   18.147    0.000  470.095    0.000 level.py:38(elementsIn)
              373420657  301.353    0.000  444.411    0.000 layers.py:23(check)
                1458855  358.541    0.000  418.673    0.000 agent.py:187(convert_values)
              191177480  411.653    0.000  411.653    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              395038863  261.663    0.000  397.445    0.000 layer.py:126(remove)
              510631279  226.806    0.000  309.166    0.000 layer.py:130(add)
               18423818  146.439    0.000  298.021    0.000 level.py:39(<listcomp>)
               11211230  292.462    0.000  292.462    0.000 {built-in method torch._C._nn.mse_loss}
                7474156  290.633    0.000  290.633    0.000 {built-in method nonzero}
             2453510377  285.471    0.000  285.471    0.000 layer.py:203(isBlocking)
               58137222   43.362    0.000  282.090    0.000 flatten.py:39(forward)
               11212495  267.973    0.000  267.973    0.000 {built-in method max}
             2991389376  256.224    0.000  256.224    0.000 {method 'random' of '_random.Random' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9572856: <Coconuts_convert4_TEST_0> in cluster <dcc> Done

Job <Coconuts_convert4_TEST_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon Apr 26 00:55:53 2021
Job was executed on host(s) <n-62-20-14>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon Apr 26 01:57:14 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Apr 26 01:57:14 2021
Terminated at Tue Apr 27 01:52:30 2021
Results reported at Tue Apr 27 01:52:30 2021

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

    CPU time :                                   85873.98 sec.
    Max Memory :                                 10356 MB
    Average Memory :                             6682.63 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               6028.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86115 sec.
    Turnaround time :                            89797 sec.

The output (if any) is above this job summary.

