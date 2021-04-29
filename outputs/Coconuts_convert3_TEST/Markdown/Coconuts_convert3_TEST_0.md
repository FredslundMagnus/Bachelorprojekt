
# Parameters

    Name :                      Coconuts_convert3_TEST-0
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
    Cf convert :                3
    Counterfacts :              1
    Topn :                      3
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      75675917839 function calls (75315704980 primitive calls) in 86109.09 seconds

##    Ordered by: cumulative time
   List reduced from 511 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86109.088 86109.088 {built-in method builtins.exec}
                      1    4.325    4.325 86109.088 86109.088 <string>:1(<module>)
                      1  411.559  411.559 86104.763 86104.763 main.py:79(CFagent)
               12078510   42.013    0.000 27876.256    0.002 agent.py:29(learn)
               12078506  701.938    0.000 22669.526    0.002 learner.py:42(Qlearn)
                4026170   15.350    0.000 22099.155    0.005 game.py:41(step)
                4026170   22.537    0.000 21309.279    0.005 layers.py:718(step)
                4026170  358.850    0.000 14157.559    0.004 layers.py:17(step)
              402453398 1420.854    0.000 13766.519    0.000 layer.py:98(move)
        403649328/43438160 1519.263    0.000 12418.771    0.000 module.py:866(_call_impl)
               31359654   81.306    0.000 11593.437    0.000 network.py:27(forward)
               31359654  365.990    0.000 11317.001    0.000 container.py:117(forward)
                4026170  409.549    0.000 10843.991    0.003 agent.py:54(_learn)
                4026170  403.562    0.000 9948.821    0.002 agent.py:204(_learn)
               12078506   94.953    0.000 8800.335    0.001 optimizer.py:84(wrapper)
              402453398 1390.942    0.000 8374.866    0.000 layers.py:735(check)
               12078506   47.537    0.000 8371.808    0.001 grad_mode.py:24(decorate_context)
               12078506  339.458    0.000 8220.259    0.001 adam.py:55(step)
               12078506 1712.784    0.000 7497.119    0.001 _functional.py:53(adam)
                4026170  526.706    0.000 7106.861    0.002 agent.py:212(counterfact)
                4026171  586.043    0.000 7096.742    0.002 layers.py:684(update)
                4026170  118.633    0.000 7013.860    0.002 agent.py:117(_learn)
                4026170 5668.040    0.001 6858.560    0.002 replaybuffer.py:22(sample_data)
                4026170 5426.335    0.001 6560.930    0.002 replaybuffer.py:67(sample_data)
               12078506   45.591    0.000 5960.063    0.000 tensor.py:195(backward)
               12078506   43.597    0.000 5912.958    0.000 __init__.py:68(backward)
                9633475  236.360    0.000 5843.448    0.001 agent.py:49(__call__)
               12078506 5648.477    0.000 5648.477    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                4026170 2115.556    0.001 4530.968    0.001 agent.py:88(interveen)
               62719308  128.218    0.000 4203.091    0.000 conv.py:398(forward)
                4026170 2385.644    0.001 4191.596    0.001 replaybuffer.py:28(teleporter_save_data)
               62719308   87.685    0.000 4012.343    0.000 conv.py:390(_conv_forward)
               62719308 3924.657    0.000 3924.657    0.000 {built-in method conv2d}
               49313796 3745.054    0.000 3745.054    0.000 {built-in method tensor}
               56366387 2172.032    0.000 3634.673    0.000 layer.py:151(update)
               40113650   24.617    0.000 3529.167    0.000 game.py:37(board)
               86026622  165.146    0.000 3211.155    0.000 linear.py:93(forward)
              402453398  540.665    0.000 3014.098    0.000 layers.py:729(isFree)
               86026622   66.393    0.000 2959.995    0.000 functional.py:1737(linear)
               86026622 2877.217    0.000 2877.217    0.000 {built-in method torch._C._nn.linear}
                4026170 1793.277    0.000 2739.222    0.001 agent.py:67(modify)
              402453398 1757.877    0.000 2483.886    0.000 layers.py:471(check)
             2695112316 2079.095    0.000 2473.433    0.000 layer.py:95(isFree)
              402453398 1641.101    0.000 2242.429    0.000 layers.py:77(check)
                1595337   29.978    0.000 1996.353    0.001 agent.py:176(choose_action)
               53921325 1911.353    0.000 1911.353    0.000 {built-in method cat}
                4026166   65.341    0.000 1700.587    0.000 agent.py:172(__call__)
              117386276   93.002    0.000 1684.799    0.000 activation.py:713(forward)
              181360895 1681.145    0.000 1681.145    0.000 {built-in method clone}
             6825605572 1164.224    0.000 1677.582    0.000 enum.py:646(__hash__)
               13659645   79.180    0.000 1671.836    0.000 agent.py:59(modify_board)
                4026170   59.883    0.000 1614.411    0.000 agent.py:112(__call__)
              117386276   92.001    0.000 1591.797    0.000 functional.py:1364(leaky_relu)
                2282783   26.472    0.000 1560.892    0.001 layers.py:740(restart)
              117386276 1481.541    0.000 1481.541    0.000 {built-in method torch._C._nn.leaky_relu}
              225465440 1469.240    0.000 1469.240    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              402617100  167.708    0.000 1440.645    0.000 {built-in method builtins.all}
             1950665210  497.677    0.000 1321.669    0.000 layers.py:690(<genexpr>)
              404360488  308.870    0.000 1316.966    0.000 {built-in method builtins.any}
                2282783   12.786    0.000 1314.730    0.001 level.py:8(__init__)
              225465440 1307.625    0.000 1307.625    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               12078506  226.515    0.000 1300.178    0.000 optimizer.py:189(zero_grad)
                2282783   87.429    0.000 1194.505    0.001 levels.py:262(generate)
               13659645 1102.016    0.000 1102.016    0.000 {built-in method torch._C._nn.one_hot}
               20360802  181.078    0.000 1031.884    0.000 level.py:41(notUsed)
              402453398  792.803    0.000 1019.587    0.000 layers.py:62(check)
             3202674536  822.811    0.000 1008.096    0.000 layers.py:700(<genexpr>)
                4026170  816.548    0.000  993.439    0.000 replaybuffer.py:73(CF_save_data)
                4026170   72.430    0.000  904.783    0.000 replaybuffer.py:18(stacker)
                4026166   69.996    0.000  861.342    0.000 replaybuffer.py:63(stacker)
              112732720  859.992    0.000  859.992    0.000 {method 'add' of 'torch._C._TensorBase' objects}
             9684691627  837.498    0.000  837.498    0.000 layer.py:91(positions)
             1220425094  833.424    0.000  833.424    0.000 layer.py:146(elements)
              112732720  738.395    0.000  738.395    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              112732720  692.047    0.000  692.047    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              112732720  689.363    0.000  689.363    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              361992123  410.860    0.000  608.236    0.000 layers.py:113(isDone)
              789129124  489.415    0.000  606.230    0.000 tensor.py:906(grad)
        8045612241/8045612238  526.088    0.000  596.460    0.000 {built-in method builtins.len}
                9633475  215.664    0.000  585.264    0.000 exploration.py:53(softmaxer)
                4026170  340.765    0.000  582.795    0.000 collector.py:46(collect)
                8052340  206.490    0.000  544.786    0.000 random.py:315(sample)
              402453398  356.755    0.000  531.859    0.000 layers.py:48(check)
              112732720  518.703    0.000  518.703    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
             6825651299  513.365    0.000  513.365    0.000 {built-in method builtins.hash}
               12078506   15.718    0.000  487.933    0.000 loss.py:527(forward)
               12078506   46.860    0.000  472.215    0.000 functional.py:2898(mse_loss)
               20360802   17.161    0.000  462.566    0.000 level.py:38(elementsIn)
              402453398  289.547    0.000  423.729    0.000 layers.py:23(check)
              199046706  379.007    0.000  379.007    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              422869944  241.316    0.000  370.227    0.000 layer.py:126(remove)
                1595337  328.497    0.000  346.790    0.000 agent.py:187(convert_values)
              554562613  223.913    0.000  299.973    0.000 layer.py:130(add)
               20360802  145.544    0.000  295.280    0.000 level.py:39(<listcomp>)
               12078506  290.438    0.000  290.438    0.000 {built-in method torch._C._nn.mse_loss}
                8052342  286.356    0.000  286.356    0.000 {built-in method nonzero}
               62719308   44.702    0.000  283.189    0.000 flatten.py:39(forward)
             2695112316  268.279    0.000  268.279    0.000 layer.py:203(isBlocking)
               12079871  267.068    0.000  267.068    0.000 {built-in method max}
               24157020  253.910    0.000  253.910    0.000 {built-in method sum}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9572855: <Coconuts_convert3_TEST_0> in cluster <dcc> Done

Job <Coconuts_convert3_TEST_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon Apr 26 00:55:53 2021
Job was executed on host(s) <n-62-20-6>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon Apr 26 01:33:46 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Apr 26 01:33:46 2021
Terminated at Tue Apr 27 01:28:59 2021
Results reported at Tue Apr 27 01:28:59 2021

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

    CPU time :                                   85906.05 sec.
    Max Memory :                                 10922 MB
    Average Memory :                             6946.09 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               5462.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86115 sec.
    Turnaround time :                            88386 sec.

The output (if any) is above this job summary.

