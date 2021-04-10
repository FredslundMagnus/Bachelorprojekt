
# Parameters

    Name :                      TEST_CF_CAUSAL4_2-0
    Main :                      CFagent
    Level :                     Levels.Causal4
    Hours :                     23.0
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
    Cf convert :                2
    Counterfacts :              1
    Topn :                      7
    Minutes used :              1375 minutes.
    Hours used :                22 hours.

# Profiling


      73192703295 function calls (72848241592 primitive calls) in 82520.17 seconds

##    Ordered by: cumulative time
   List reduced from 511 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 82520.171 82520.171 {built-in method builtins.exec}
                      1    4.820    4.820 82520.171 82520.171 <string>:1(<module>)
                      1  235.651  235.651 82515.350 82515.350 main.py:95(CFagent)
               11147877   41.689    0.000 26430.051    0.002 agent.py:29(learn)
               11147868  671.626    0.000 21524.198    0.002 learner.py:42(Qlearn)
                3715959   16.913    0.000 20996.082    0.006 game.py:41(step)
                3715959   19.475    0.000 20168.649    0.005 layers.py:710(step)
                3715959  346.592    0.000 12933.414    0.003 layers.py:17(step)
              371342566 1041.778    0.000 12553.084    0.000 layer.py:98(move)
        385551534/41091522 1499.805    0.000 12224.738    0.000 module.py:866(_call_impl)
               29943654   80.080    0.000 11437.111    0.000 network.py:24(forward)
               29943654  366.041    0.000 11169.206    0.000 container.py:117(forward)
                3715959  920.315    0.000 10801.751    0.003 agent.py:217(counterfact)
                3715959  374.927    0.000 10265.199    0.003 agent.py:54(_learn)
                3715959  371.007    0.000 9426.692    0.003 agent.py:209(_learn)
               11147868   89.681    0.000 8516.680    0.001 optimizer.py:84(wrapper)
               11147868   51.570    0.000 8109.582    0.001 grad_mode.py:24(decorate_context)
               11147868  315.844    0.000 7955.400    0.001 adam.py:55(step)
              371342566 1211.759    0.000 7482.986    0.000 layers.py:727(check)
               11147868 1686.798    0.000 7273.864    0.001 _functional.py:53(adam)
                3715960  529.141    0.000 7186.693    0.002 layers.py:676(update)
                3715959  111.772    0.000 6673.337    0.002 agent.py:117(_learn)
                9393287  240.941    0.000 5862.934    0.001 agent.py:49(__call__)
               58919139 5818.869    0.000 5818.869    0.000 {built-in method tensor}
               50402254   31.808    0.000 5623.888    0.000 game.py:37(board)
               11147868   43.004    0.000 5476.995    0.000 tensor.py:195(backward)
               11147868   43.046    0.000 5432.216    0.000 __init__.py:68(backward)
               11147868 5176.413    0.000 5176.413    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3715959 3832.227    0.001 5051.428    0.001 replaybuffer.py:22(sample_data)
               74319190 2699.923    0.000 4616.903    0.000 layer.py:151(update)
                3715959 2503.101    0.001 4474.911    0.001 replaybuffer.py:28(teleporter_save_data)
                3715959 3383.265    0.001 4458.685    0.001 replaybuffer.py:49(sample_data)
                3715959 1871.916    0.001 4177.854    0.001 agent.py:88(interveen)
               59887308  134.935    0.000 4137.491    0.000 conv.py:398(forward)
               59887308   76.175    0.000 3941.612    0.000 conv.py:390(_conv_forward)
               59887308 3865.437    0.000 3865.437    0.000 {built-in method conv2d}
              371131726  662.085    0.000 3342.596    0.000 layers.py:721(isFree)
               82399044  163.747    0.000 3150.351    0.000 linear.py:93(forward)
               82399044   68.499    0.000 2904.835    0.000 functional.py:1737(linear)
               82399044 2819.848    0.000 2819.848    0.000 {built-in method torch._C._nn.linear}
             3272560072 2201.306    0.000 2680.511    0.000 layer.py:95(isFree)
                3715959 1750.688    0.000 2636.306    0.001 agent.py:67(modify)
                1970590   40.452    0.000 2515.123    0.001 agent.py:172(choose_action)
               53984750 1918.711    0.000 1918.711    0.000 {built-in method cat}
              195947109 1890.260    0.000 1890.260    0.000 {built-in method clone}
             7028840774 1225.416    0.000 1744.271    0.000 enum.py:646(__hash__)
              112342698   90.692    0.000 1672.557    0.000 activation.py:713(forward)
              371471803  377.743    0.000 1661.627    0.000 {built-in method builtins.any}
               13109246   81.397    0.000 1634.170    0.000 agent.py:59(modify_board)
                3715950   59.708    0.000 1609.727    0.000 agent.py:168(__call__)
              112342698   94.836    0.000 1581.865    0.000 functional.py:1364(leaky_relu)
                3715959   55.555    0.000 1518.857    0.000 agent.py:112(__call__)
              112342698 1466.850    0.000 1466.850    0.000 {built-in method torch._C._nn.leaky_relu}
              208093524 1413.009    0.000 1413.009    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                3840157   45.692    0.000 1376.177    0.000 layers.py:731(restart)
              371342566 1040.909    0.000 1369.618    0.000 layers.py:71(check)
             4045314273 1064.941    0.000 1283.884    0.000 layers.py:692(<genexpr>)
              208093524 1262.260    0.000 1262.260    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               11147868  218.472    0.000 1237.189    0.000 optimizer.py:189(zero_grad)
              371342566  761.601    0.000 1206.451    0.000 layers.py:240(check)
              371342566  687.247    0.000 1133.500    0.000 layers.py:280(check)
               13109246 1068.305    0.000 1068.305    0.000 {built-in method torch._C._nn.one_hot}
             1276617144 1057.819    0.000 1057.819    0.000 layer.py:146(elements)
              371596000  176.485    0.000  984.719    0.000 {built-in method builtins.all}
                3840157   20.212    0.000  971.490    0.000 level.py:8(__init__)
                3715959   76.126    0.000  958.508    0.000 replaybuffer.py:18(stacker)
             1853717390  465.713    0.000  853.068    0.000 layers.py:682(<genexpr>)
              104046762  830.434    0.000  830.434    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                3715950   70.264    0.000  821.866    0.000 replaybuffer.py:45(stacker)
                3840157  129.753    0.000  789.367    0.000 levels.py:199(generate)
                3715959  315.667    0.000  762.714    0.000 replaybuffer.py:55(CF_save_data)
             8385701357  741.348    0.000  741.348    0.000 layer.py:91(positions)
              104046762  725.608    0.000  725.608    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              371342566  542.654    0.000  718.657    0.000 layers.py:56(check)
              104046762  665.851    0.000  665.851    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              104046762  662.681    0.000  662.681    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
        9048940809/9048940806  570.378    0.000  639.486    0.000 {built-in method builtins.len}
              371342566  421.481    0.000  639.179    0.000 layers.py:307(check)
              371342566  412.114    0.000  629.588    0.000 layers.py:267(check)
                9393287  220.030    0.000  580.123    0.000 exploration.py:53(softmaxer)
              728327418  455.632    0.000  570.922    0.000 tensor.py:906(grad)
               15112232  212.647    0.000  561.917    0.000 random.py:315(sample)
                3715959  329.679    0.000  556.091    0.000 collector.py:53(collect)
                7680314   62.365    0.000  536.047    0.000 level.py:41(notUsed)
             7028883029  518.863    0.000  518.863    0.000 {built-in method builtins.hash}
              104046762  494.544    0.000  494.544    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              371342566  319.232    0.000  475.588    0.000 layers.py:42(check)
               11147868   15.207    0.000  459.039    0.000 loss.py:527(forward)
               11147868   41.545    0.000  443.832    0.000 functional.py:2898(mse_loss)
              212772305  435.230    0.000  435.230    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               11147878  421.534    0.000  421.534    0.000 {built-in method nonzero}
                1970590  386.749    0.000  411.821    0.000 agent.py:183(convert_values)
               38401570   50.306    0.000  346.261    0.000 layer.py:69(restart)
              343402780  233.903    0.000  324.096    0.000 layer.py:126(remove)
              565082028  225.982    0.000  309.192    0.000 layer.py:130(add)
              454567972  201.028    0.000  293.253    0.000 random.py:250(_randbelow_with_getrandbits)
               74319190  274.839    0.000  274.839    0.000 layer.py:163(<listcomp>)
               11147868  273.351    0.000  273.351    0.000 {built-in method torch._C._nn.mse_loss}
               59887308   40.054    0.000  272.768    0.000 flatten.py:39(forward)
             2598749123  255.515    0.000  255.515    0.000 layer.py:203(isBlocking)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-11-15>
Subject: Job 9505788: <TEST_CF_CAUSAL4_2_0> in cluster <dcc> Done

Job <TEST_CF_CAUSAL4_2_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Fri Apr  9 00:44:40 2021
Job was executed on host(s) <n-62-11-15>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Fri Apr  9 00:44:41 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Fri Apr  9 00:44:41 2021
Terminated at Fri Apr  9 23:40:11 2021
Results reported at Fri Apr  9 23:40:11 2021

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

    CPU time :                                   82301.88 sec.
    Max Memory :                                 10647 MB
    Average Memory :                             7115.73 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               5737.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   82629 sec.
    Turnaround time :                            82531 sec.

The output (if any) is above this job summary.

