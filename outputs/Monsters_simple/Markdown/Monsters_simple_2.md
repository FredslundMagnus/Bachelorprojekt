
# Parameters

    Name :                      Monsters_simple-2
    Main :                      simple
    Level :                     Levels.MonsterLevel
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
    Network2 :                  Networks.MiniBig
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
    Topn :                      6
    Random counterfacts :       False
    Num :                       2
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      155229316505 function calls (155023237782 primitive calls) in 86114.63 seconds

##    Ordered by: cumulative time
   List reduced from 417 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86114.633 86114.633 {built-in method builtins.exec}
                      1    0.002    0.002 86114.633 86114.633 <string>:1(<module>)
                      1  135.914  135.914 86114.631 86114.631 main.py:67(simple)
                8586598   35.362    0.000 52046.396    0.006 game.py:42(step)
                8586598   38.213    0.000 50189.956    0.006 layers.py:827(step)
                8586598  693.890    0.000 27403.894    0.003 layers.py:17(step)
                8586598   26.611    0.000 27106.641    0.003 agent.py:29(learn)
                8586598  190.583    0.000 27063.363    0.003 agent.py:117(_learn)
                8586598  685.635    0.000 26872.780    0.003 learner.py:42(Qlearn)
              858659800 2172.680    0.000 26638.746    0.000 layer.py:106(move)
                8586599 1136.230    0.000 22698.967    0.003 layers.py:793(update)
              858659800 2652.945    0.000 18431.273    0.000 layers.py:844(check)
                8586598   49.365    0.000 11768.152    0.001 grad_mode.py:23(decorate_context)
                8586598  280.202    0.000 11624.942    0.001 adam.py:55(step)
              858659800 5605.530    0.000 10399.918    0.000 layers.py:538(check)
                8586598 2120.814    0.000 10064.308    0.001 functional.py:53(adam)
               18065860  131.515    0.000 9748.864    0.001 layers.py:849(restart)
        231838146/25759794  880.802    0.000 9736.696    0.000 module.py:715(_call_impl)
               17173196   40.380    0.000 9043.014    0.001 network.py:28(forward)
               17173196  223.409    0.000 8903.746    0.001 container.py:115(forward)
               18065860   64.856    0.000 8367.378    0.000 level.py:8(__init__)
               18065860 1244.819    0.000 7644.914    0.000 levels.py:428(generate)
             1656316126  882.621    0.000 6131.265    0.000 {built-in method builtins.any}
                8586598   49.349    0.000 5951.575    0.001 tensor.py:181(backward)
                8586598   28.294    0.000 5902.226    0.001 __init__.py:68(backward)
                8586598 5658.532    0.001 5658.532    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               90329300  802.939    0.000 5174.688    0.000 level.py:41(notUsed)
                8586598  107.851    0.000 5038.969    0.001 agent.py:112(__call__)
             5901321866 1508.867    0.000 4859.381    0.000 layers.py:809(<genexpr>)
               51519594 3160.172    0.000 4629.540    0.000 layer.py:159(update)
              858659800 1080.905    0.000 4494.469    0.000 layers.py:838(isFree)
            16276074998 2694.867    0.000 3884.592    0.000 enum.py:646(__hash__)
             5011031457 2702.292    0.000 3413.564    0.000 layer.py:103(isFree)
               34346392   58.434    0.000 3134.117    0.000 conv.py:422(forward)
              849175833 1893.799    0.000 3067.836    0.000 layers.py:575(isDead)
               34346392   65.398    0.000 3054.246    0.000 conv.py:414(_conv_forward)
               51519588  111.668    0.000 3024.875    0.000 linear.py:92(forward)
               34346392 2977.128    0.000 2977.128    0.000 {built-in method conv2d}
               51519588  183.190    0.000 2865.075    0.000 functional.py:1669(linear)
              858659800 1827.744    0.000 2600.224    0.000 layers.py:77(check)
               36399561 2459.513    0.000 2459.513    0.000 {built-in method tensor}
              601061890 1551.082    0.000 2417.926    0.000 tensor.py:933(grad)
               90329300   65.589    0.000 2387.350    0.000 level.py:38(elementsIn)
                8586598  216.280    0.000 2361.110    0.000 optimizer.py:167(zero_grad)
              171731960 2112.209    0.000 2112.209    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               51519588 2055.080    0.000 2055.080    0.000 {built-in method addmm}
             1249012641  391.888    0.000 1941.047    0.000 random.py:244(randint)
               17173196   18.756    0.000 1829.435    0.000 game.py:38(board)
              171731960 1814.464    0.000 1814.464    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
             1249012641  640.470    0.000 1549.159    0.000 random.py:200(randrange)
               90329300  750.093    0.000 1531.179    0.000 level.py:39(<listcomp>)
            17221333624 1502.624    0.000 1502.624    0.000 layer.py:99(positions)
             2811251939 1046.360    0.000 1403.249    0.000 layer.py:138(add)
              858659900  254.260    0.000 1397.148    0.000 {built-in method builtins.all}
               68692784   54.939    0.000 1333.500    0.000 activation.py:713(forward)
             1994278408  835.538    0.000 1309.219    0.000 layer.py:134(remove)
              858659800  851.166    0.000 1296.398    0.000 layers.py:48(check)
               68692784   82.953    0.000 1278.561    0.000 functional.py:1292(leaky_relu)
             3853793847 1270.102    0.000 1270.102    0.000 level.py:32(inverse)
             2795941854  687.825    0.000 1243.141    0.000 layers.py:799(<genexpr>)
              858659800  430.930    0.000 1231.716    0.000 layers.py:572(<listcomp>)
              108395160  119.286    0.000 1215.216    0.000 layer.py:77(restart)
            16276109427 1189.731    0.000 1189.731    0.000 {built-in method builtins.hash}
               68692784 1186.717    0.000 1186.717    0.000 {built-in method torch._C._nn.leaky_relu}
             1651905966  830.462    0.000 1173.939    0.000 random.py:250(_randbelow_with_getrandbits)
               85865980 1136.547    0.000 1136.547    0.000 {method 'add' of 'torch._C._TensorBase' objects}
             5678321868 1081.383    0.000 1081.383    0.000 layer.py:154(elements)
              738447508  366.322    0.000 1063.548    0.000 overrides.py:1070(has_torch_function)
               85865980 1034.925    0.000 1034.925    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              858659800  380.551    0.000 1007.734    0.000 layers.py:573(<listcomp>)
               85865980  961.739    0.000  961.739    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              858659800  638.813    0.000  935.911    0.000 layers.py:23(check)
                8586598  545.216    0.000  922.531    0.000 collector.py:46(collect)
               18065960  432.900    0.000  859.900    0.000 layers.py:36(reset)
               85865980  858.475    0.000  858.475    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
             4660993921  790.823    0.000  790.823    0.000 enum.py:352(<genexpr>)
               90329300  489.496    0.000  790.583    0.000 {built-in method _functools.reduce}
               90329300  304.407    0.000  763.417    0.000 random.py:315(sample)
               85865980  677.315    0.000  677.315    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               18065860  299.385    0.000  621.891    0.000 level.py:16(<dictcomp>)
             8341908144  582.299    0.000  582.299    0.000 {method 'append' of 'list' objects}
             5011031457  501.225    0.000  501.225    0.000 layer.py:211(isBlocking)
                8586598   12.006    0.000  478.031    0.000 loss.py:445(forward)
             6019205198  477.764    0.000  477.764    0.000 {method 'random' of '_random.Random' objects}
                8586598   43.472    0.000  466.025    0.000 functional.py:2637(mse_loss)
               51519588  405.568    0.000  405.568    0.000 {method 't' of 'torch._C._TensorBase' objects}
                8586598   30.161    0.000  385.031    0.000 exploration.py:47(epsilonGreedy)
             1528414604  307.516    0.000  384.864    0.000 overrides.py:1083(<genexpr>)
        4130707014/4130707013  326.638    0.000  384.144    0.000 {built-in method builtins.len}
              858659900  240.371    0.000  316.915    0.000 layers.py:52(isDone)
             1994278408  311.440    0.000  311.440    0.000 {method 'remove' of 'list' objects}
             3793830600  301.087    0.000  301.087    0.000 level.py:39(<lambda>)
               17173196  300.261    0.000  300.261    0.000 {built-in method sum}
                8586598  292.647    0.000  292.647    0.000 {built-in method torch._C._nn.mse_loss}
             4202970200  282.679    0.000  282.679    0.000 layer.py:92(isDead)
                8586598  270.806    0.000  270.806    0.000 {method 'tolist' of 'torch._C._TensorBase' objects}
                8587456  252.576    0.000  252.576    0.000 {built-in method max}
               34346392   22.610    0.000  227.582    0.000 flatten.py:39(forward)
               85866030   99.090    0.000  219.908    0.000 tensor.py:596(__hash__)
                8586598  216.196    0.000  216.196    0.000 {built-in method gather}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9623999: <Monsters_simple_2> in cluster <dcc> Done

Job <Monsters_simple_2> was submitted from host <n-62-30-2> by user <s183905> in cluster <dcc> at Sat May  8 23:34:13 2021
Job was executed on host(s) <n-62-20-2>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sat May  8 23:34:15 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat May  8 23:34:15 2021
Terminated at Sun May  9 23:29:46 2021
Results reported at Sun May  9 23:29:46 2021

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

    CPU time :                                   85898.38 sec.
    Max Memory :                                 2065 MB
    Average Memory :                             2062.00 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14319.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86168 sec.
    Turnaround time :                            86133 sec.

The output (if any) is above this job summary.

