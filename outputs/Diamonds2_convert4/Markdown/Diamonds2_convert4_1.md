
# Parameters

    Name :                      Diamonds2_convert4-1
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
    Cf convert :                4
    Counterfacts :              1
    Topn :                      2
    Random counterfacts :       False
    Num :                       1
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      67230689034 function calls (66935174219 primitive calls) in 86113.57 seconds

##    Ordered by: cumulative time
   List reduced from 505 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86113.567 86113.567 {built-in method builtins.exec}
                      1    4.098    4.098 86113.567 86113.567 <string>:1(<module>)
                      1  317.161  317.161 86109.469 86109.469 main.py:80(CFagent)
                9082758   34.504    0.000 27207.189    0.003 agent.py:29(learn)
                9082758  680.750    0.000 22774.973    0.003 learner.py:42(Qlearn)
                3027586   14.976    0.000 16671.211    0.006 game.py:42(step)
                3027586   18.722    0.000 15957.866    0.005 layers.py:827(step)
        330231171/34718047 1342.787    0.000 12024.777    0.000 module.py:866(_call_impl)
               25635289   80.449    0.000 11292.509    0.000 network.py:28(forward)
               25635289  353.600    0.000 11049.849    0.000 container.py:117(forward)
                3027586  292.269    0.000 10473.725    0.003 agent.py:54(_learn)
                3027586 1169.328    0.000 10130.011    0.003 agent.py:212(counterfact)
                3027586  291.290    0.000 9714.627    0.003 agent.py:204(_learn)
                9082758   79.249    0.000 9614.359    0.001 optimizer.py:84(wrapper)
                9082758   37.741    0.000 9241.163    0.001 grad_mode.py:24(decorate_context)
                3027586  257.333    0.000 9142.698    0.003 layers.py:17(step)
                9082758  262.810    0.000 9117.437    0.001 adam.py:55(step)
              302406849  477.594    0.000 8860.216    0.000 layer.py:106(move)
                9082758 1851.830    0.000 8558.114    0.001 _functional.py:53(adam)
                3027586 4486.544    0.001 8325.495    0.003 replaybuffer.py:28(teleporter_save_data)
                3027586   86.720    0.000 6964.992    0.002 agent.py:117(_learn)
                3027587  424.854    0.000 6771.803    0.002 layers.py:793(update)
                3027586 4147.189    0.001 6298.349    0.002 agent.py:88(interveen)
                8275227  198.298    0.000 5896.875    0.001 agent.py:49(__call__)
                9082758   46.644    0.000 5804.604    0.001 tensor.py:195(backward)
                9082758   37.502    0.000 5756.705    0.001 __init__.py:68(backward)
              302406849 1158.313    0.000 5677.317    0.000 layers.py:844(check)
                9082758 5518.565    0.001 5518.565    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3027586 4122.871    0.001 5078.004    0.002 replaybuffer.py:67(sample_data)
                3027586 4105.801    0.001 5075.336    0.002 replaybuffer.py:22(sample_data)
               47569801 4635.239    0.000 4635.239    0.000 {built-in method tensor}
               40572600   28.099    0.000 4437.794    0.000 game.py:38(board)
               51270578  110.967    0.000 3978.565    0.000 conv.py:398(forward)
               51270578   66.755    0.000 3809.060    0.000 conv.py:390(_conv_forward)
               51270578 3742.305    0.000 3742.305    0.000 {built-in method conv2d}
              278899187 3501.523    0.000 3501.523    0.000 {built-in method clone}
                2222132   48.683    0.000 3470.053    0.002 agent.py:176(choose_action)
               70850695  142.549    0.000 3212.237    0.000 linear.py:93(forward)
               54496557 1697.049    0.000 3108.146    0.000 layer.py:175(NoRock_update)
               70850695   56.017    0.000 2994.292    0.000 functional.py:1737(linear)
               70850695 2924.103    0.000 2924.103    0.000 {built-in method torch._C._nn.linear}
                3027586 1811.075    0.001 2689.416    0.001 agent.py:67(modify)
                5047025   54.431    0.000 2623.089    0.001 layers.py:849(restart)
              302406849  527.379    0.000 2236.326    0.000 layers.py:838(isFree)
                5047025   26.307    0.000 2206.881    0.000 level.py:8(__init__)
                5047025   75.380    0.000 1937.549    0.000 levels.py:249(generate)
               32807070  304.447    0.000 1787.018    0.000 level.py:41(notUsed)
               96485984   73.142    0.000 1767.984    0.000 activation.py:713(forward)
                3027586 1313.805    0.000 1763.103    0.001 replaybuffer.py:73(CF_save_data)
              169544816 1754.348    0.000 1754.348    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
             2711256738 1415.386    0.000 1708.946    0.000 layer.py:103(isFree)
               96485984   79.596    0.000 1694.842    0.000 functional.py:1364(leaky_relu)
               41578673 1692.441    0.000 1692.441    0.000 {built-in method cat}
               11302813   76.872    0.000 1627.718    0.000 agent.py:59(modify_board)
               96485984 1598.980    0.000 1598.980    0.000 {built-in method torch._C._nn.leaky_relu}
              169544816 1531.689    0.000 1531.689    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
             6372099543 1033.414    0.000 1505.950    0.000 enum.py:646(__hash__)
                3027586   51.458    0.000 1505.069    0.000 agent.py:172(__call__)
                3027586   47.613    0.000 1420.453    0.000 agent.py:112(__call__)
                9082758  210.321    0.000 1326.590    0.000 optimizer.py:189(zero_grad)
              300739262  271.240    0.000 1165.311    0.000 {built-in method builtins.any}
               11302813 1040.166    0.000 1040.166    0.000 {built-in method torch._C._nn.one_hot}
               84772408  990.933    0.000  990.933    0.000 {method 'add' of 'torch._C._TensorBase' objects}
             2977116750  738.245    0.000  894.071    0.000 layers.py:809(<genexpr>)
               32807070   23.974    0.000  871.557    0.000 level.py:38(elementsIn)
              293229586  860.869    0.000  860.869    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              302406849  539.778    0.000  848.749    0.000 layers.py:375(check)
              302406849  524.816    0.000  827.273    0.000 layers.py:337(check)
               84772408  819.678    0.000  819.678    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              302758700  124.067    0.000  806.793    0.000 {built-in method builtins.all}
             1076644283  803.790    0.000  803.790    0.000 layer.py:154(elements)
               84772408  795.993    0.000  795.993    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               84772408  789.292    0.000  789.292    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              302406849  493.923    0.000  786.850    0.000 layers.py:349(check)
              302406849  494.607    0.000  785.403    0.000 layers.py:387(check)
                3027586   58.565    0.000  757.278    0.000 replaybuffer.py:18(stacker)
                3027586   59.634    0.000  748.932    0.000 replaybuffer.py:63(stacker)
                2222132  638.784    0.000  748.513    0.000 agent.py:187(convert_values)
             1431295455  382.315    0.000  716.958    0.000 layers.py:799(<genexpr>)
                3027586  375.358    0.000  624.721    0.000 collector.py:46(collect)
             6979868703  614.447    0.000  614.447    0.000 layer.py:99(positions)
               84772408  612.607    0.000  612.607    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                8275227  223.720    0.000  612.338    0.000 exploration.py:53(softmaxer)
               32807070  283.811    0.000  570.809    0.000 level.py:39(<listcomp>)
        7509520539/7509520536  484.950    0.000  545.321    0.000 {built-in method builtins.len}
              593406940  394.407    0.000  488.233    0.000 tensor.py:906(grad)
             6372134070  472.543    0.000  472.543    0.000 {built-in method builtins.hash}
                9082758   13.474    0.000  439.471    0.000 loss.py:527(forward)
                9082758   33.072    0.000  425.997    0.000 functional.py:2898(mse_loss)
                6055172  151.581    0.000  407.094    0.000 random.py:315(sample)
              302406849  235.629    0.000  365.119    0.000 layers.py:364(check)
              302406849  231.706    0.000  355.682    0.000 layers.py:326(check)
             1547291746  352.440    0.000  352.440    0.000 level.py:32(inverse)
               45423225   38.396    0.000  347.302    0.000 layer.py:77(restart)
              302406849  204.406    0.000  296.838    0.000 layers.py:23(check)
               51270578   34.387    0.000  294.944    0.000 flatten.py:39(forward)
                9082758  282.175    0.000  282.175    0.000 {built-in method torch._C._nn.mse_loss}
             1627728250  279.415    0.000  279.415    0.000 enum.py:352(<genexpr>)
               32807070  172.509    0.000  276.774    0.000 {built-in method _functools.reduce}
               18165516  266.180    0.000  266.180    0.000 {built-in method sum}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9678089: <Diamonds2_convert4_1> in cluster <dcc> Done

Job <Diamonds2_convert4_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Fri May 21 19:42:40 2021
Job was executed on host(s) <n-62-20-7>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun May 23 20:23:53 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun May 23 20:23:53 2021
Terminated at Mon May 24 20:19:12 2021
Results reported at Mon May 24 20:19:12 2021

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

    CPU time :                                   86087.68 sec.
    Max Memory :                                 3445 MB
    Average Memory :                             3422.60 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               12939.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86119 sec.
    Turnaround time :                            261392 sec.

The output (if any) is above this job summary.

