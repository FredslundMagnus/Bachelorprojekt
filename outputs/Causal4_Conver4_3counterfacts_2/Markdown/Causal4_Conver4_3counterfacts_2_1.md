
# Parameters

    Name :                      Causal4_Conver4_3counterfacts_2-1
    Main :                      Load_Cfagent
    Level :                     Levels.Causal4
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
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      54744146287 function calls (54452045158 primitive calls) in 86113.80 seconds

##    Ordered by: cumulative time
   List reduced from 436 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86113.801 86113.801 {built-in method builtins.exec}
                      1    7.779    7.779 86113.800 86113.800 <string>:1(<module>)
                      1  384.809  384.809 86106.022 86106.022 main.py:109(Load_Cfagent)
                2147431 2764.483    0.001 25089.326    0.012 agent.py:212(counterfact)
                6442293   31.423    0.000 17944.797    0.003 agent.py:29(learn)
                2147431   11.527    0.000 16068.068    0.007 game.py:42(step)
                2147431   15.556    0.000 15513.074    0.007 layers.py:827(step)
                6442293  461.910    0.000 14303.378    0.002 learner.py:42(Qlearn)
        323597937/31499629 1471.043    0.000 11671.901    0.000 module.py:866(_call_impl)
               25057336   78.729    0.000 11020.326    0.000 network.py:28(forward)
               25057336  342.857    0.000 10751.898    0.000 container.py:117(forward)
               89238760 10106.733    0.000 10106.733    0.000 {built-in method tensor}
               84503027   55.192    0.000 10014.161    0.000 game.py:38(board)
                2147431  231.352    0.000 9826.006    0.005 layers.py:17(step)
              214696961  689.617    0.000 9572.020    0.000 layer.py:106(move)
                2147431 6679.136    0.003 7769.975    0.004 replaybuffer.py:22(sample_data)
                2147431 6518.348    0.003 7570.541    0.004 replaybuffer.py:67(sample_data)
                5016628  107.859    0.000 7489.909    0.001 agent.py:176(choose_action)
                2147431  342.486    0.000 7003.295    0.003 agent.py:54(_learn)
                9303553  353.722    0.000 6654.920    0.001 agent.py:49(__call__)
               85897220 3618.393    0.000 6396.852    0.000 layer.py:159(update)
                2147431  342.861    0.000 6363.482    0.003 agent.py:204(_learn)
              214696961 1138.604    0.000 5813.630    0.000 layers.py:844(check)
                2147431  349.825    0.000 5645.311    0.003 layers.py:793(update)
                6442293   71.007    0.000 5351.990    0.001 optimizer.py:84(wrapper)
                6442293   41.014    0.000 5060.108    0.001 grad_mode.py:24(decorate_context)
                6442293  239.244    0.000 4936.130    0.001 adam.py:55(step)
                2147431   92.435    0.000 4529.708    0.002 agent.py:117(_learn)
                6442293 1036.533    0.000 4460.425    0.001 _functional.py:53(adam)
               50114672  124.156    0.000 3998.971    0.000 conv.py:398(forward)
                6442293   29.206    0.000 3849.761    0.001 tensor.py:195(backward)
                6442293   36.502    0.000 3819.481    0.001 __init__.py:68(backward)
               50114672   91.206    0.000 3806.270    0.000 conv.py:390(_conv_forward)
               50114672 3715.064    0.000 3715.064    0.000 {built-in method conv2d}
                6442293 3636.477    0.001 3636.477    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2147431 2077.826    0.001 3430.633    0.002 replaybuffer.py:28(teleporter_save_data)
                2147431 1592.127    0.001 3107.124    0.001 agent.py:88(interveen)
               70877146  148.625    0.000 3035.912    0.000 linear.py:93(forward)
               70877146   62.009    0.000 2799.844    0.000 functional.py:1737(linear)
               70877146 2723.986    0.000 2723.986    0.000 {built-in method torch._C._nn.linear}
              214696961  442.042    0.000 2606.408    0.000 layers.py:838(isFree)
             2017203433 1831.312    0.000 2164.365    0.000 layer.py:103(isFree)
               32925294 1971.386    0.000 1971.386    0.000 {built-in method cat}
                2147431 1195.431    0.001 1798.248    0.001 agent.py:67(modify)
             1070986183 1648.754    0.000 1648.754    0.000 layer.py:154(elements)
               95934482  102.164    0.000 1613.255    0.000 activation.py:713(forward)
               11450984   82.567    0.000 1605.397    0.000 agent.py:59(modify_board)
                5016628 1340.483    0.000 1541.626    0.000 agent.py:187(convert_values)
               95934482   81.936    0.000 1511.091    0.000 functional.py:1364(leaky_relu)
                3589510   60.897    0.000 1497.023    0.000 layers.py:849(restart)
               95934482 1411.312    0.000 1411.312    0.000 {built-in method torch._C._nn.leaky_relu}
              127686157 1371.312    0.000 1371.312    0.000 {built-in method clone}
             4517001466  879.311    0.000 1237.459    0.000 enum.py:646(__hash__)
                2147431  925.363    0.000 1199.777    0.001 replaybuffer.py:73(CF_save_data)
                2147431   60.029    0.000 1130.640    0.001 agent.py:172(__call__)
                3589510   22.228    0.000 1074.223    0.000 level.py:8(__init__)
               11450984 1052.231    0.000 1052.231    0.000 {built-in method torch._C._nn.one_hot}
              217595882  228.077    0.000 1007.318    0.000 {built-in method builtins.any}
                2147431   58.335    0.000 1003.505    0.000 agent.py:112(__call__)
              214696961  707.213    0.000  933.794    0.000 layers.py:77(check)
              214696961  593.285    0.000  907.209    0.000 layers.py:286(check)
                2147431   62.811    0.000  906.624    0.000 replaybuffer.py:18(stacker)
                2147431   65.711    0.000  877.151    0.000 replaybuffer.py:63(stacker)
              214743100  102.056    0.000  873.102    0.000 {built-in method builtins.all}
              120256136  871.304    0.000  871.304    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                3589510  131.555    0.000  830.397    0.000 levels.py:199(generate)
             1091390436  308.941    0.000  798.285    0.000 layers.py:799(<genexpr>)
              214696961  477.666    0.000  794.949    0.000 layers.py:246(check)
             2322689490  637.148    0.000  779.241    0.000 layers.py:809(<genexpr>)
                6442293  144.012    0.000  768.236    0.000 optimizer.py:189(zero_grad)
              120256136  757.362    0.000  757.362    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
            10292772809  654.994    0.000  720.150    0.000 {built-in method builtins.len}
                9303553  240.189    0.000  659.058    0.000 exploration.py:53(softmaxer)
                7179020   64.971    0.000  573.410    0.000 level.py:41(notUsed)
             5579784566  543.185    0.000  543.185    0.000 layer.py:99(positions)
               60128068  515.689    0.000  515.689    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              214696961  379.845    0.000  509.672    0.000 layers.py:62(check)
               60128068  449.598    0.000  449.598    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              214743100  304.259    0.000  440.486    0.000 layers.py:113(isDone)
               85897220  420.905    0.000  420.905    0.000 layer.py:171(<listcomp>)
               11473882  165.044    0.000  413.565    0.000 random.py:315(sample)
               60128068  408.983    0.000  408.983    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               60128068  404.494    0.000  404.494    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              214696961  239.472    0.000  379.216    0.000 layers.py:313(check)
              255330963  291.442    0.000  377.391    0.000 layer.py:134(remove)
              214696961  239.654    0.000  375.231    0.000 layers.py:273(check)
              420896476  293.590    0.000  361.088    0.000 tensor.py:906(grad)
             4517026249  358.152    0.000  358.152    0.000 {built-in method builtins.hash}
               35895100   53.193    0.000  349.351    0.000 layer.py:77(restart)
                6442293   14.830    0.000  345.641    0.000 loss.py:527(forward)
                2147431  201.001    0.000  342.421    0.000 collector.py:46(collect)
                6442293   38.579    0.000  330.810    0.000 functional.py:2898(mse_loss)
              214696961  223.343    0.000  321.005    0.000 layers.py:48(check)
              141284572  303.198    0.000  303.198    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               60128068  295.936    0.000  295.936    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               21638337  291.172    0.000  291.172    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               85897220  268.088    0.000  268.088    0.000 layer.py:172(<listcomp>)
              451273524  190.056    0.000  267.048    0.000 layer.py:138(add)
               50114672   45.642    0.000  261.370    0.000 flatten.py:39(forward)
              214696961  167.175    0.000  241.499    0.000 layers.py:23(check)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9621661: <Causal4_Conver4_3counterfacts_2_1> in cluster <dcc> Done

Job <Causal4_Conver4_3counterfacts_2_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Fri May  7 14:30:14 2021
Job was executed on host(s) <n-62-20-10>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Fri May  7 14:51:28 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Fri May  7 14:51:28 2021
Terminated at Sat May  8 14:46:47 2021
Results reported at Sat May  8 14:46:47 2021

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

    CPU time :                                   85912.15 sec.
    Max Memory :                                 7421 MB
    Average Memory :                             5353.65 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               8963.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86120 sec.
    Turnaround time :                            87393 sec.

The output (if any) is above this job summary.

