
# Parameters

    Name :                      Diamonds2_convert2-1
    Main :                      CFagent
    Level :                     Levels.Causal5
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
    K1 :                        2000000.0
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
    Cf convert :                2
    Counterfacts :              1
    Topn :                      2
    Random counterfacts :       False
    Num :                       1
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      68122870798 function calls (67828004939 primitive calls) in 86113.90 seconds

##    Ordered by: cumulative time
   List reduced from 505 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86113.901 86113.901 {built-in method builtins.exec}
                      1    3.892    3.892 86113.901 86113.901 <string>:1(<module>)
                      1  320.696  320.696 86110.009 86110.009 main.py:80(CFagent)
                9070065   33.696    0.000 27142.099    0.003 agent.py:29(learn)
                9070060  668.523    0.000 22737.710    0.003 learner.py:42(Qlearn)
                3023355   15.491    0.000 17008.825    0.006 game.py:42(step)
                3023355   18.939    0.000 16291.158    0.005 layers.py:827(step)
        329514027/34649859 1376.603    0.000 11983.802    0.000 module.py:866(_call_impl)
               25579799   74.387    0.000 11243.769    0.000 network.py:28(forward)
               25579799  353.895    0.000 11007.265    0.000 container.py:117(forward)
                3023355  286.485    0.000 10449.632    0.003 agent.py:54(_learn)
                3023355 1159.408    0.000 10000.956    0.003 agent.py:212(counterfact)
                3023355  284.890    0.000 9692.777    0.003 agent.py:204(_learn)
                9070060   82.956    0.000 9641.244    0.001 optimizer.py:84(wrapper)
                9070060   39.087    0.000 9266.624    0.001 grad_mode.py:24(decorate_context)
                3023355  253.707    0.000 9178.758    0.003 layers.py:17(step)
                9070060  266.621    0.000 9139.424    0.001 adam.py:55(step)
              301927247  484.379    0.000 8898.574    0.000 layer.py:106(move)
                9070060 1859.387    0.000 8575.628    0.001 _functional.py:53(adam)
                3023355 4497.606    0.001 8379.690    0.003 replaybuffer.py:28(teleporter_save_data)
                3023356  437.164    0.000 7068.012    0.002 layers.py:793(update)
                3023355   82.487    0.000 6947.068    0.002 agent.py:117(_learn)
                3023355 4172.261    0.001 6321.442    0.002 agent.py:88(interveen)
                8253841  194.876    0.000 5883.714    0.001 agent.py:49(__call__)
                9070060   45.515    0.000 5778.462    0.001 tensor.py:195(backward)
                9070060   35.365    0.000 5731.647    0.001 __init__.py:68(backward)
              301927247 1178.616    0.000 5716.532    0.000 layers.py:844(check)
                9070060 5494.971    0.001 5494.971    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3023355 4077.880    0.001 5036.079    0.002 replaybuffer.py:22(sample_data)
                3023355 3963.263    0.001 4904.856    0.002 replaybuffer.py:67(sample_data)
               47422076 4647.241    0.000 4647.241    0.000 {built-in method tensor}
               40434095   28.697    0.000 4448.210    0.000 game.py:38(board)
               51159598  110.537    0.000 3932.371    0.000 conv.py:398(forward)
               51159598   66.512    0.000 3772.079    0.000 conv.py:390(_conv_forward)
               51159598 3705.566    0.000 3705.566    0.000 {built-in method conv2d}
              278768770 3536.138    0.000 3536.138    0.000 {built-in method clone}
                2209193   48.302    0.000 3365.690    0.002 agent.py:176(choose_action)
               70692687  141.473    0.000 3187.824    0.000 linear.py:93(forward)
               54420399 1693.970    0.000 3103.379    0.000 layer.py:175(NoRock_update)
               70692687   57.519    0.000 2977.117    0.000 functional.py:1737(linear)
               70692687 2905.180    0.000 2905.180    0.000 {built-in method torch._C._nn.linear}
                3023355 1813.820    0.001 2689.536    0.001 agent.py:67(modify)
                4968000   53.392    0.000 2614.852    0.001 layers.py:849(restart)
              301927247  530.195    0.000 2229.238    0.000 layers.py:838(isFree)
                4968000   27.015    0.000 2196.549    0.000 level.py:8(__init__)
                4968000   76.124    0.000 1925.256    0.000 levels.py:249(generate)
               32292063  303.973    0.000 1773.929    0.000 level.py:41(notUsed)
              169307780 1759.886    0.000 1759.886    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               96272486   80.275    0.000 1758.279    0.000 activation.py:713(forward)
                3023355 1303.641    0.000 1750.992    0.001 replaybuffer.py:73(CF_save_data)
             2686803321 1405.846    0.000 1699.043    0.000 layer.py:103(isFree)
               96272486   77.176    0.000 1678.004    0.000 functional.py:1364(leaky_relu)
               41510721 1662.349    0.000 1662.349    0.000 {built-in method cat}
               11277196   78.031    0.000 1628.089    0.000 agent.py:59(modify_board)
               96272486 1584.309    0.000 1584.309    0.000 {built-in method torch._C._nn.leaky_relu}
              169307780 1533.219    0.000 1533.219    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
             6403018562 1061.854    0.000 1526.345    0.000 enum.py:646(__hash__)
                3023350   49.138    0.000 1499.752    0.000 agent.py:172(__call__)
                3023355   47.297    0.000 1419.541    0.000 agent.py:112(__call__)
                9070060  217.393    0.000 1328.312    0.000 optimizer.py:189(zero_grad)
              300390956  274.760    0.000 1202.358    0.000 {built-in method builtins.any}
              302335600  162.107    0.000 1052.790    0.000 {built-in method builtins.all}
               11277196 1039.299    0.000 1039.299    0.000 {built-in method torch._C._nn.one_hot}
               84653890  990.724    0.000  990.724    0.000 {method 'add' of 'torch._C._TensorBase' objects}
             2973676000  770.872    0.000  927.597    0.000 layers.py:809(<genexpr>)
             1919747391  489.918    0.000  924.908    0.000 layers.py:799(<genexpr>)
              293069316  868.026    0.000  868.026    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               32292063   24.042    0.000  865.539    0.000 level.py:38(elementsIn)
              301927247  541.684    0.000  856.503    0.000 layers.py:337(check)
               84653890  816.116    0.000  816.116    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               84653890  800.928    0.000  800.928    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              301927247  499.614    0.000  796.813    0.000 layers.py:349(check)
             1069976772  796.319    0.000  796.319    0.000 layer.py:154(elements)
              301927247  498.811    0.000  794.687    0.000 layers.py:387(check)
               84653890  790.876    0.000  790.876    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              301927247  491.548    0.000  790.099    0.000 layers.py:375(check)
                3023355   59.226    0.000  743.482    0.000 replaybuffer.py:18(stacker)
                3023350   59.376    0.000  731.533    0.000 replaybuffer.py:63(stacker)
                2209193  574.079    0.000  652.357    0.000 agent.py:187(convert_values)
             7036276745  623.287    0.000  623.287    0.000 layer.py:99(positions)
                3023355  375.790    0.000  623.205    0.000 collector.py:46(collect)
                8253841  223.706    0.000  618.833    0.000 exploration.py:53(softmaxer)
               84653890  609.153    0.000  609.153    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               32292063  280.864    0.000  564.540    0.000 level.py:39(<listcomp>)
        7502068055/7502068052  488.340    0.000  548.114    0.000 {built-in method builtins.len}
              592577314  397.249    0.000  490.275    0.000 tensor.py:906(grad)
             6403053089  464.498    0.000  464.498    0.000 {built-in method builtins.hash}
                9070060   12.723    0.000  441.605    0.000 loss.py:527(forward)
                9070060   35.977    0.000  428.881    0.000 functional.py:2898(mse_loss)
                6046710  154.684    0.000  413.239    0.000 random.py:315(sample)
              301927247  250.208    0.000  377.125    0.000 layers.py:364(check)
              301927247  239.048    0.000  366.683    0.000 layers.py:326(check)
               44712000   36.388    0.000  350.773    0.000 layer.py:77(restart)
             1523004207  346.427    0.000  346.427    0.000 level.py:32(inverse)
              301927247  204.641    0.000  303.737    0.000 layers.py:23(check)
               51159598   42.986    0.000  300.533    0.000 flatten.py:39(forward)
                9070060  281.384    0.000  281.384    0.000 {built-in method torch._C._nn.mse_loss}
             1602184874  279.336    0.000  279.336    0.000 enum.py:352(<genexpr>)
               32292063  172.725    0.000  276.956    0.000 {built-in method _functools.reduce}
              483017876  191.559    0.000  269.288    0.000 layer.py:138(add)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9678086: <Diamonds2_convert2_1> in cluster <dcc> Done

Job <Diamonds2_convert2_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Fri May 21 19:42:39 2021
Job was executed on host(s) <n-62-20-7>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sat May 22 19:38:04 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat May 22 19:38:04 2021
Terminated at Sun May 23 19:33:23 2021
Results reported at Sun May 23 19:33:23 2021

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

    CPU time :                                   86087.41 sec.
    Max Memory :                                 3445 MB
    Average Memory :                             3423.23 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               12939.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86119 sec.
    Turnaround time :                            172244 sec.

The output (if any) is above this job summary.

