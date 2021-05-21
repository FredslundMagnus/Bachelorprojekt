
# Parameters

    Name :                      SuperCausal_tele-2
    Main :                      teleport
    Level :                     Levels.CausalSuper
    Failed actions chance :     0
    Use model :                 False
    Depth :                     1
    Model explore :             100000
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
    Topn :                      6
    Random counterfacts :       False
    Num :                       2
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      110840420544 function calls (110565451077 primitive calls) in 86114.82 seconds

##    Ordered by: cumulative time
   List reduced from 491 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86114.822 86114.822 {built-in method builtins.exec}
                      1    1.655    1.655 86114.822 86114.822 <string>:1(<module>)
                      1  220.381  220.381 86113.166 86113.166 main.py:46(teleport)
                4920798   18.871    0.000 30626.346    0.006 game.py:42(step)
                4920798   27.639    0.000 29419.448    0.006 layers.py:827(step)
                9841596   34.949    0.000 28446.913    0.003 agent.py:29(learn)
                9841596  743.543    0.000 24040.584    0.002 learner.py:42(Qlearn)
                4920798  359.287    0.000 21406.129    0.004 layers.py:17(step)
              492079800  781.188    0.000 21002.930    0.000 layer.py:106(move)
                4920798  516.415    0.000 17150.025    0.003 agent.py:54(_learn)
              492079800 2065.187    0.000 16189.705    0.000 layers.py:844(check)
        309364356/34395900 1413.770    0.000 11684.975    0.000 module.py:866(_call_impl)
                4920798  145.628    0.000 11243.062    0.002 agent.py:117(_learn)
               24554304   71.143    0.000 10877.870    0.000 network.py:28(forward)
               24554304  337.954    0.000 10639.030    0.000 container.py:117(forward)
                9841596   83.270    0.000 10056.592    0.001 optimizer.py:84(wrapper)
                9841596   40.980    0.000 9650.327    0.001 grad_mode.py:24(decorate_context)
                9841596  271.396    0.000 9517.738    0.001 adam.py:55(step)
                9841596 1944.293    0.000 8940.399    0.001 _functional.py:53(adam)
                4920799  634.327    0.000 7951.196    0.002 layers.py:793(update)
                9791910  236.072    0.000 7166.261    0.001 agent.py:49(__call__)
                4920798 3328.186    0.001 6830.362    0.001 agent.py:88(interveen)
                4920798 3555.566    0.001 6544.164    0.001 replaybuffer.py:28(teleporter_save_data)
                9841596   40.202    0.000 5960.058    0.001 tensor.py:195(backward)
                9841596   36.677    0.000 5918.388    0.001 __init__.py:68(backward)
                9841596 5661.303    0.001 5661.303    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                4920798 3721.792    0.001 5335.222    0.001 replaybuffer.py:22(sample_data)
                4920798 2724.411    0.001 4135.855    0.001 agent.py:67(modify)
            17974068177 2678.024    0.000 4054.632    0.000 enum.py:646(__hash__)
               49108608  119.569    0.000 3877.315    0.000 conv.py:398(forward)
               49108608   82.731    0.000 3696.700    0.000 conv.py:390(_conv_forward)
               49108608 3613.969    0.000 3613.969    0.000 {built-in method conv2d}
              492079800 2187.087    0.000 3487.188    0.000 layers.py:734(check)
              492079800  866.415    0.000 3340.641    0.000 layers.py:838(isFree)
               63821316  137.811    0.000 2989.699    0.000 linear.py:93(forward)
               49207990 1572.261    0.000 2801.969    0.000 layer.py:175(NoRock_update)
               63821316   51.206    0.000 2779.325    0.000 functional.py:1737(linear)
               63821316 2714.714    0.000 2714.714    0.000 {built-in method torch._C._nn.linear}
              492079800 1671.261    0.000 2660.783    0.000 layers.py:717(check)
              492079800 1663.165    0.000 2636.511    0.000 layers.py:700(check)
              201559681 2494.836    0.000 2494.836    0.000 {built-in method clone}
             4567719840 1946.009    0.000 2474.226    0.000 layer.py:103(isFree)
                4920798   72.217    0.000 2286.439    0.000 agent.py:112(__call__)
               14712708   98.322    0.000 2135.986    0.000 agent.py:59(modify_board)
              489464794  474.955    0.000 2039.622    0.000 {built-in method builtins.any}
              177148728 1821.699    0.000 1821.699    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               21005361 1752.847    0.000 1752.847    0.000 {built-in method tensor}
                2615107   31.541    0.000 1695.982    0.001 layers.py:849(restart)
               88375620   89.208    0.000 1685.553    0.000 activation.py:713(forward)
               39316698 1632.599    0.000 1632.599    0.000 {built-in method cat}
              177148728 1618.492    0.000 1618.492    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               88375620   70.774    0.000 1596.345    0.000 functional.py:1364(leaky_relu)
             5384112723 1290.024    0.000 1564.667    0.000 layers.py:809(<genexpr>)
               88375620 1509.765    0.000 1509.765    0.000 {built-in method torch._C._nn.leaky_relu}
            16408129332 1503.780    0.000 1503.780    0.000 layer.py:99(positions)
                2615107   14.317    0.000 1471.629    0.001 level.py:8(__init__)
                9841596   11.422    0.000 1402.672    0.000 game.py:38(board)
                9841596  220.678    0.000 1389.131    0.000 optimizer.py:189(zero_grad)
            17974104000 1376.614    0.000 1376.614    0.000 {built-in method builtins.hash}
               14712708 1370.763    0.000 1370.763    0.000 {built-in method torch._C._nn.one_hot}
              492079800  831.613    0.000 1312.189    0.000 layers.py:672(check)
                2615107   45.769    0.000 1307.297    0.000 levels.py:261(generate)
              492079800  800.582    0.000 1269.453    0.000 layers.py:686(check)
                4920798   84.423    0.000 1268.448    0.000 replaybuffer.py:18(stacker)
              492079800  799.098    0.000 1265.499    0.000 layers.py:658(check)
               21470037  197.060    0.000 1214.224    0.000 level.py:41(notUsed)
               88574364 1009.415    0.000 1009.415    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                4920798  606.444    0.000 1002.202    0.000 collector.py:46(collect)
               88574364  863.409    0.000  863.409    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               88574364  832.048    0.000  832.048    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               88574364  826.563    0.000  826.563    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                9791910  265.923    0.000  734.181    0.000 exploration.py:53(softmaxer)
             1173989629  713.027    0.000  713.027    0.000 layer.py:154(elements)
              216272389  659.877    0.000  659.877    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               88574364  638.508    0.000  638.508    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              492079900   96.255    0.000  599.245    0.000 {built-in method builtins.all}
              492079800  381.497    0.000  578.473    0.000 layers.py:646(check)
               21470037   15.107    0.000  567.620    0.000 level.py:38(elementsIn)
        7349883034/7349883032  491.938    0.000  562.789    0.000 {built-in method builtins.len}
             1138929302  243.665    0.000  558.597    0.000 layers.py:799(<genexpr>)
              620020602  405.206    0.000  503.768    0.000 tensor.py:906(grad)
                9841596   15.813    0.000  486.073    0.000 loss.py:527(forward)
              492079800  318.969    0.000  476.855    0.000 layers.py:23(check)
                9841596   35.431    0.000  470.260    0.000 functional.py:2898(mse_loss)
             4567719840  449.839    0.000  449.839    0.000 layer.py:211(isBlocking)
               29524788  423.183    0.000  423.183    0.000 {built-in method sum}
             5436104347  398.792    0.000  398.792    0.000 {method 'random' of '_random.Random' objects}
               21470037  186.600    0.000  372.445    0.000 level.py:39(<listcomp>)
                4920798  122.021    0.000  335.789    0.000 random.py:315(sample)
                9841596  311.576    0.000  311.576    0.000 {built-in method torch._C._nn.mse_loss}
              437799567  203.843    0.000  300.963    0.000 layer.py:134(remove)
               49108608   45.039    0.000  296.380    0.000 flatten.py:39(forward)
              538390101  213.380    0.000  291.174    0.000 layer.py:138(add)
                9843067  277.678    0.000  277.678    0.000 {built-in method max}
             4894647930  274.643    0.000  274.643    0.000 layer.py:92(isDead)
                4920798   22.146    0.000  260.256    0.000 exploration.py:47(epsilonGreedy)
               49108608  251.341    0.000  251.341    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              995885406  241.401    0.000  241.401    0.000 level.py:32(inverse)
                9791910  238.576    0.000  238.576    0.000 {built-in method multinomial}
             1035663400  217.912    0.000  217.912    0.000 enum.py:352(<genexpr>)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9672991: <SuperCausal_tele_2> in cluster <dcc> Done

Job <SuperCausal_tele_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Thu May 20 18:43:26 2021
Job was executed on host(s) <n-62-20-2>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Thu May 20 18:43:28 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu May 20 18:43:28 2021
Terminated at Fri May 21 18:38:55 2021
Results reported at Fri May 21 18:38:55 2021

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

    CPU time :                                   85894.23 sec.
    Max Memory :                                 9207 MB
    Average Memory :                             5937.30 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               7177.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86171 sec.
    Turnaround time :                            86129 sec.

The output (if any) is above this job summary.

