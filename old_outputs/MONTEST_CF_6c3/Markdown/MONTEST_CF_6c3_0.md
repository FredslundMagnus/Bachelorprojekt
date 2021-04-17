
# Parameters

    Name :                      MONTEST_CF_6c3-0
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
    Counterfacts :              3
    Topn :                      7
    Minutes used :              1315 minutes.
    Hours used :                21 hours.

# Profiling


      60700563145 function calls (60334181870 primitive calls) in 78908.21 seconds

##    Ordered by: cumulative time
   List reduced from 506 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 78908.213 78908.213 {built-in method builtins.exec}
                      1    4.509    4.509 78908.213 78908.213 <string>:1(<module>)
                      1  165.166  165.166 78903.704 78903.704 main.py:95(CFagent)
                2462763 4073.370    0.002 23363.953    0.009 agent.py:217(counterfact)
                7388289   27.881    0.000 17551.420    0.002 agent.py:29(learn)
                2462763   11.721    0.000 17528.763    0.007 game.py:41(step)
                2462763   12.577    0.000 17068.427    0.007 layers.py:710(step)
                7388289  449.608    0.000 14301.551    0.002 learner.py:42(Qlearn)
        405120426/38740842 1530.385    0.000 12601.051    0.000 module.py:866(_call_impl)
               31352553   81.166    0.000 11980.261    0.000 network.py:24(forward)
               31352553  376.589    0.000 11714.602    0.000 container.py:117(forward)
                2462764  385.537    0.000 9594.113    0.004 layers.py:676(update)
                7056642  137.076    0.000 9172.789    0.001 agent.py:172(choose_action)
                2462763  223.296    0.000 7442.983    0.003 layers.py:17(step)
               11982096  305.752    0.000 7350.358    0.001 agent.py:49(__call__)
              224097188  654.874    0.000 7193.617    0.000 layer.py:98(move)
                2462763  244.551    0.000 6805.887    0.003 agent.py:54(_learn)
               91857733 6627.660    0.000 6627.660    0.000 {built-in method tensor}
               86106873   51.480    0.000 6528.519    0.000 game.py:37(board)
                2462763  244.166    0.000 6263.983    0.003 agent.py:209(_learn)
                7388289   58.911    0.000 5619.316    0.001 optimizer.py:84(wrapper)
                9931659   80.661    0.000 5380.177    0.001 layers.py:731(restart)
                7388289   30.338    0.000 5355.683    0.001 grad_mode.py:24(decorate_context)
                7388289  210.929    0.000 5259.566    0.001 adam.py:55(step)
                2462763 2901.189    0.001 5124.776    0.002 replaybuffer.py:28(teleporter_save_data)
                7388289 1119.416    0.000 4801.634    0.001 _functional.py:53(adam)
              224097188  503.331    0.000 4611.379    0.000 layers.py:727(check)
                9931659   38.463    0.000 4564.422    0.000 level.py:8(__init__)
               59106318 2846.991    0.000 4440.850    0.000 layer.py:151(update)
                2462763   75.909    0.000 4436.727    0.002 agent.py:117(_learn)
               62705106  136.102    0.000 4281.726    0.000 conv.py:398(forward)
                9931659  739.525    0.000 4189.410    0.000 levels.py:418(generate)
               62705106   77.649    0.000 4084.585    0.000 conv.py:390(_conv_forward)
               62705106 4006.936    0.000 4006.936    0.000 {built-in method conv2d}
                7388289   30.311    0.000 3659.687    0.000 tensor.py:195(backward)
                7388289   28.401    0.000 3628.352    0.000 __init__.py:68(backward)
                2462763 2095.531    0.001 3607.293    0.001 agent.py:88(interveen)
                7388289 3457.567    0.000 3457.567    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2462763 2660.058    0.001 3453.574    0.001 replaybuffer.py:22(sample_data)
               89132133  174.028    0.000 3331.006    0.000 linear.py:93(forward)
                2462763 2481.912    0.001 3189.967    0.001 replaybuffer.py:49(sample_data)
               89132133   71.023    0.000 3071.457    0.000 functional.py:1737(linear)
               89132133 2983.480    0.000 2983.480    0.000 {built-in method torch._C._nn.linear}
              224097188 1681.462    0.000 2937.486    0.000 layers.py:531(check)
               49658295  441.664    0.000 2731.092    0.000 level.py:41(notUsed)
              254196589 2357.175    0.000 2357.175    0.000 {built-in method clone}
                2462763 1279.670    0.001 1865.429    0.001 agent.py:67(modify)
              120484686   97.447    0.000 1795.542    0.000 activation.py:713(forward)
                7056642 1523.961    0.000 1780.927    0.000 agent.py:183(convert_values)
               14444859   85.491    0.000 1767.918    0.000 agent.py:59(modify_board)
              120484686  101.628    0.000 1698.096    0.000 functional.py:1364(leaky_relu)
              248813673  195.735    0.000 1625.943    0.000 {built-in method builtins.any}
              120484686 1578.051    0.000 1578.051    0.000 {built-in method torch._C._nn.leaky_relu}
              224011341  301.246    0.000 1481.561    0.000 layers.py:721(isFree)
                2462763  754.115    0.000 1474.261    0.001 replaybuffer.py:55(CF_save_data)
             1669655113  463.763    0.000 1430.824    0.000 layers.py:692(<genexpr>)
               41535252 1430.477    0.000 1430.477    0.000 {built-in method cat}
             5837968161  973.742    0.000 1413.981    0.000 enum.py:646(__hash__)
             1316015459  972.518    0.000 1180.315    0.000 layer.py:95(isFree)
               49658295   39.731    0.000 1179.197    0.000 level.py:38(elementsIn)
               14444859 1153.985    0.000 1153.985    0.000 {built-in method torch._C._nn.one_hot}
                2462763   39.642    0.000 1070.071    0.000 agent.py:168(__call__)
                2462763   36.938    0.000 1021.442    0.000 agent.py:112(__call__)
              137914728  929.414    0.000  929.414    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
             2048210963  927.282    0.000  927.282    0.000 layer.py:146(elements)
              241425383  558.062    0.000  882.460    0.000 layers.py:568(isDead)
              137914728  826.086    0.000  826.086    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                7388289  146.507    0.000  822.409    0.000 optimizer.py:189(zero_grad)
               54583821  303.134    0.000  780.896    0.000 random.py:315(sample)
              224097188  539.716    0.000  758.723    0.000 layers.py:71(check)
             2118619425  756.219    0.000  756.219    0.000 level.py:32(inverse)
               49658295  370.731    0.000  748.288    0.000 level.py:39(<listcomp>)
               11982096  273.968    0.000  729.489    0.000 exploration.py:53(softmaxer)
               59589954   71.617    0.000  714.971    0.000 layer.py:69(restart)
              528232285  532.564    0.000  677.794    0.000 layer.py:126(remove)
                2462763   44.458    0.000  618.771    0.000 replaybuffer.py:18(stacker)
               59716524  607.315    0.000  607.315    0.000 {method 'item' of 'torch._C._TensorBase' objects}
              775434658  392.611    0.000  558.381    0.000 random.py:250(_randbelow_with_getrandbits)
               68957364  547.697    0.000  547.697    0.000 {method 'add' of 'torch._C._TensorBase' objects}
        7056713690/7056713687  474.348    0.000  545.912    0.000 {built-in method builtins.len}
              307604693  102.382    0.000  540.893    0.000 random.py:244(randint)
                2462763   43.273    0.000  539.652    0.000 replaybuffer.py:45(stacker)
              271104211  520.125    0.000  520.125    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              975203530  368.387    0.000  500.691    0.000 layer.py:130(add)
                9931759  253.958    0.000  498.819    0.000 layers.py:30(reset)
               68957364  481.633    0.000  481.633    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               68957364  440.269    0.000  440.269    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
             5837996416  440.244    0.000  440.244    0.000 {built-in method builtins.hash}
               68957364  438.874    0.000  438.874    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              307604693  181.115    0.000  438.511    0.000 random.py:200(randrange)
               49658295  241.200    0.000  391.177    0.000 {built-in method _functools.reduce}
             2145239798  385.447    0.000  385.447    0.000 enum.py:352(<genexpr>)
              482701632  309.304    0.000  384.254    0.000 tensor.py:906(grad)
                2462763  220.188    0.000  372.175    0.000 collector.py:53(collect)
             4134545537  365.219    0.000  365.219    0.000 layer.py:91(positions)
              224097188  244.046    0.000  356.153    0.000 layers.py:42(check)
              246276400   63.231    0.000  329.471    0.000 {built-in method builtins.all}
              224097188  117.486    0.000  327.639    0.000 layers.py:565(<listcomp>)
               68957364  327.273    0.000  327.273    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                9931659  158.675    0.000  314.602    0.000 level.py:16(<dictcomp>)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-11-15>
Subject: Job 9507483: <MONTEST_CF_6c3_0> in cluster <dcc> Done

Job <MONTEST_CF_6c3_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sat Apr 10 02:36:50 2021
Job was executed on host(s) <n-62-11-15>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Apr 11 05:13:50 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun Apr 11 05:13:50 2021
Terminated at Mon Apr 12 03:09:03 2021
Results reported at Mon Apr 12 03:09:03 2021

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

    CPU time :                                   78711.01 sec.
    Max Memory :                                 8194 MB
    Average Memory :                             5885.84 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               8190.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   78912 sec.
    Turnaround time :                            174733 sec.

The output (if any) is above this job summary.

