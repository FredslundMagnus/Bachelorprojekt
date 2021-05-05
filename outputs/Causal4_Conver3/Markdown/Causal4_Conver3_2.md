
# Parameters

    Name :                      Causal4_Conver3-2
    Main :                      CFagent
    Level :                     Levels.Causal4
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
    Cf convert :                3
    Counterfacts :              1
    Topn :                      3
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      63023772496 function calls (62746652181 primitive calls) in 86121.29 seconds

##    Ordered by: cumulative time
   List reduced from 513 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86121.292 86121.292 {built-in method builtins.exec}
                      1    4.612    4.612 86121.292 86121.292 <string>:1(<module>)
                      1  349.533  349.533 86116.680 86116.680 main.py:80(CFagent)
                8956299   37.438    0.000 29759.092    0.003 agent.py:29(learn)
                8956297  741.822    0.000 24821.128    0.003 learner.py:42(Qlearn)
                2985433   15.623    0.000 19991.078    0.007 game.py:42(step)
                2985433   18.244    0.000 19216.634    0.006 layers.py:827(step)
        310163284/33044660 1410.911    0.000 12731.735    0.000 module.py:866(_call_impl)
                2985433  279.929    0.000 12724.027    0.004 layers.py:17(step)
              298288646  905.854    0.000 12413.276    0.000 layer.py:106(move)
               24088363   73.123    0.000 11940.680    0.000 network.py:28(forward)
               24088363  377.376    0.000 11703.733    0.000 container.py:117(forward)
                2985433  340.282    0.000 11480.975    0.004 agent.py:54(_learn)
                2985433  335.339    0.000 10645.767    0.004 agent.py:204(_learn)
                8956297   86.318    0.000 10532.936    0.001 optimizer.py:84(wrapper)
                8956297   43.001    0.000 10133.302    0.001 grad_mode.py:24(decorate_context)
                8956297  302.765    0.000 9998.850    0.001 adam.py:55(step)
                2985433  953.163    0.000 9874.295    0.003 agent.py:212(counterfact)
                8956297 2063.546    0.000 9354.665    0.001 _functional.py:53(adam)
              298288646 1513.802    0.000 7694.110    0.000 layers.py:844(check)
                2985433   95.201    0.000 7572.013    0.003 agent.py:117(_learn)
                2985434  473.192    0.000 6448.897    0.002 layers.py:793(update)
                8956297   38.821    0.000 6131.798    0.001 tensor.py:195(backward)
                8956297   36.373    0.000 6091.657    0.001 __init__.py:68(backward)
                7562922  219.600    0.000 6054.838    0.001 agent.py:49(__call__)
                8956297 5836.153    0.001 5836.153    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2985433 4201.712    0.001 5270.982    0.002 replaybuffer.py:22(sample_data)
               47298841 5121.536    0.000 5121.536    0.000 {built-in method tensor}
                2985433 3975.986    0.001 5005.393    0.002 replaybuffer.py:67(sample_data)
               40395093   29.787    0.000 4904.725    0.000 game.py:38(board)
                2985433 2168.965    0.001 4549.828    0.002 agent.py:88(interveen)
                2985433 2285.009    0.001 4271.124    0.001 replaybuffer.py:28(teleporter_save_data)
               48176726  115.580    0.000 4186.226    0.000 conv.py:398(forward)
               48176726   72.198    0.000 4018.740    0.000 conv.py:390(_conv_forward)
               59708670 2301.806    0.000 3965.657    0.000 layer.py:159(update)
               48176726 3946.543    0.000 3946.543    0.000 {built-in method conv2d}
               66294223  151.456    0.000 3394.878    0.000 linear.py:93(forward)
              298288646  722.531    0.000 3196.976    0.000 layers.py:838(isFree)
               66294223   60.965    0.000 3171.856    0.000 functional.py:1737(linear)
               66294223 3096.014    0.000 3096.014    0.000 {built-in method torch._C._nn.linear}
                2985433 1892.343    0.001 2847.731    0.001 agent.py:67(modify)
                1598280   40.379    0.000 2659.149    0.002 agent.py:176(choose_action)
             2554068676 2015.807    0.000 2474.445    0.000 layer.py:103(isFree)
              167184208 1913.335    0.000 1913.335    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               90382586   88.625    0.000 1901.857    0.000 activation.py:713(forward)
              131437581 1887.281    0.000 1887.281    0.000 {built-in method clone}
               40402675 1832.071    0.000 1832.071    0.000 {built-in method cat}
               90382586   82.543    0.000 1813.232    0.000 functional.py:1364(leaky_relu)
               90382586 1714.060    0.000 1714.060    0.000 {built-in method torch._C._nn.leaky_relu}
              167184208 1682.784    0.000 1682.784    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               10548355   83.142    0.000 1679.749    0.000 agent.py:59(modify_board)
                2985431   57.900    0.000 1669.964    0.001 agent.py:172(__call__)
             5920034022 1141.515    0.000 1646.019    0.000 enum.py:646(__hash__)
                2985433   56.031    0.000 1559.359    0.001 agent.py:112(__call__)
                8956297  241.743    0.000 1483.087    0.000 optimizer.py:189(zero_grad)
              298557217  329.414    0.000 1457.100    0.000 {built-in method builtins.any}
                2985433 1073.891    0.000 1386.914    0.000 replaybuffer.py:73(CF_save_data)
                2971617   41.701    0.000 1216.570    0.000 layers.py:849(restart)
              298288646  895.592    0.000 1193.331    0.000 layers.py:77(check)
             3251289613  925.168    0.000 1127.687    0.000 layers.py:809(<genexpr>)
              298288646  722.274    0.000 1114.045    0.000 layers.py:286(check)
               10548355 1061.559    0.000 1061.559    0.000 {built-in method torch._C._nn.one_hot}
              298543400  118.258    0.000 1040.155    0.000 {built-in method builtins.all}
               83592104 1036.799    0.000 1036.799    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              298288646  628.451    0.000 1031.571    0.000 layers.py:246(check)
             1201522260  335.540    0.000  961.072    0.000 layers.py:799(<genexpr>)
              999725861  915.712    0.000  915.712    0.000 layer.py:154(elements)
               83592104  909.651    0.000  909.651    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                2971617   18.550    0.000  874.893    0.000 level.py:8(__init__)
               83592104  874.839    0.000  874.839    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               83592104  846.006    0.000  846.006    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                2985433   61.863    0.000  836.874    0.000 replaybuffer.py:18(stacker)
                2985431   63.362    0.000  804.723    0.000 replaybuffer.py:63(stacker)
             7675338315  802.855    0.000  802.855    0.000 layer.py:99(positions)
                2971617  107.248    0.000  696.997    0.000 levels.py:199(generate)
                2985433  416.264    0.000  690.753    0.000 collector.py:46(collect)
               83592104  673.242    0.000  673.242    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              298288646  514.507    0.000  671.282    0.000 layers.py:62(check)
        7871184715/7871184712  573.857    0.000  638.555    0.000 {built-in method builtins.len}
                7562922  228.232    0.000  628.680    0.000 exploration.py:53(softmaxer)
              298543400  385.911    0.000  578.658    0.000 layers.py:113(isDone)
              585144812  459.908    0.000  561.937    0.000 tensor.py:906(grad)
              298288646  350.272    0.000  543.902    0.000 layers.py:273(check)
              298288646  322.948    0.000  516.836    0.000 layers.py:313(check)
              144971367  512.220    0.000  512.220    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
             5920068101  504.511    0.000  504.511    0.000 {built-in method builtins.hash}
               11914100  187.733    0.000  494.820    0.000 random.py:315(sample)
                5943234   55.689    0.000  486.924    0.000 level.py:41(notUsed)
                8956297   12.748    0.000  480.437    0.000 loss.py:527(forward)
                8956297   35.791    0.000  467.689    0.000 functional.py:2898(mse_loss)
                1598280  428.581    0.000  456.124    0.000 agent.py:187(convert_values)
              298288646  305.843    0.000  449.573    0.000 layers.py:48(check)
              298288646  234.221    0.000  353.306    0.000 layers.py:23(check)
               48176726   35.082    0.000  312.149    0.000 flatten.py:39(forward)
                8956297  310.280    0.000  310.280    0.000 {built-in method torch._C._nn.mse_loss}
               17912598  292.743    0.000  292.743    0.000 {built-in method sum}
               29716170   42.617    0.000  289.503    0.000 layer.py:77(restart)
             3293330044  280.363    0.000  280.363    0.000 {method 'random' of '_random.Random' objects}
                5970868  277.740    0.000  277.740    0.000 {built-in method nonzero}
               48176726  277.067    0.000  277.067    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9606152: <Causal4_Conver3_2> in cluster <dcc> Done

Job <Causal4_Conver3_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon May  3 01:44:21 2021
Job was executed on host(s) <n-62-20-16>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon May  3 20:33:41 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon May  3 20:33:41 2021
Terminated at Tue May  4 20:29:11 2021
Results reported at Tue May  4 20:29:11 2021

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

    CPU time :                                   85903.27 sec.
    Max Memory :                                 8932 MB
    Average Memory :                             6046.72 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               7452.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86202 sec.
    Turnaround time :                            153890 sec.

The output (if any) is above this job summary.

