
# Parameters

    Name :                      Diamonds3_teleport-1
    Main :                      teleport
    Level :                     Levels.Causal6
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
    Topn :                      6
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      89853086139 function calls (89610616248 primitive calls) in 86121.58 seconds

##    Ordered by: cumulative time
   List reduced from 473 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86121.583 86121.583 {built-in method builtins.exec}
                      1    1.777    1.777 86121.582 86121.582 <string>:1(<module>)
                      1  207.753  207.753 86119.806 86119.806 main.py:45(teleport)
                4330095   18.189    0.000 25589.931    0.006 game.py:41(step)
                8660190   33.064    0.000 24650.089    0.003 agent.py:29(learn)
                4330095   25.941    0.000 24595.385    0.006 layers.py:718(step)
                8660190  595.037    0.000 20694.473    0.002 learner.py:42(Qlearn)
                4330095  146.634    0.000 14894.203    0.003 agent.py:54(_learn)
                4330095  375.625    0.000 12642.036    0.003 layers.py:17(step)
                4330095 7006.349    0.002 12251.894    0.003 replaybuffer.py:28(teleporter_save_data)
              433009500  717.675    0.000 12227.972    0.000 layer.py:98(move)
                4330096  636.455    0.000 11892.401    0.003 layers.py:684(update)
        272778175/30309295 1060.323    0.000 10250.548    0.000 module.py:715(_call_impl)
                4330095  120.558    0.000 9704.004    0.002 agent.py:117(_learn)
               21649105   51.970    0.000 9552.096    0.000 network.py:27(forward)
                4330095 6309.590    0.001 9447.906    0.002 agent.py:88(interveen)
               21649105  254.338    0.000 9369.024    0.000 container.py:115(forward)
                8660190   54.589    0.000 8233.718    0.001 grad_mode.py:23(decorate_context)
                8660190  273.835    0.000 8077.177    0.001 adam.py:55(step)
              433009500 1497.911    0.000 7793.784    0.000 layers.py:735(check)
                8660190 1495.480    0.000 6646.031    0.001 functional.py:53(adam)
                8658820  203.069    0.000 6356.724    0.001 agent.py:49(__call__)
                4330095 4362.827    0.001 6315.063    0.001 replaybuffer.py:22(sample_data)
               10678755  100.795    0.000 4993.885    0.000 layers.py:740(restart)
                8660190   50.586    0.000 4920.849    0.001 tensor.py:181(backward)
                8660190   33.131    0.000 4870.263    0.001 __init__.py:68(backward)
                8660190 4637.685    0.001 4637.685    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                4330095 2327.272    0.001 4321.377    0.001 agent.py:67(modify)
              396462265 4155.486    0.000 4155.486    0.000 {built-in method clone}
               10678755   50.071    0.000 4101.092    0.000 level.py:8(__init__)
               10678755  145.007    0.000 3605.797    0.000 levels.py:288(generate)
               43298210   72.215    0.000 3465.800    0.000 conv.py:422(forward)
               43298210   84.402    0.000 3364.272    0.000 conv.py:414(_conv_forward)
               64071268  584.841    0.000 3306.635    0.000 level.py:41(notUsed)
               43298210 3264.421    0.000 3264.421    0.000 {built-in method conv2d}
               56287125  124.292    0.000 3004.132    0.000 linear.py:92(forward)
              433009500  749.836    0.000 2970.887    0.000 layers.py:729(isFree)
               56287125  221.518    0.000 2822.460    0.000 functional.py:1669(linear)
               34640768 1505.839    0.000 2590.131    0.000 layer.py:167(NoRock_update)
             9960639740 1755.447    0.000 2488.511    0.000 enum.py:646(__hash__)
             1206071302  672.110    0.000 2331.075    0.000 {built-in method builtins.any}
             3450205015 1794.186    0.000 2221.051    0.000 layer.py:95(isFree)
              545592024 1233.770    0.000 2058.014    0.000 tensor.py:933(grad)
                4330095   59.517    0.000 2007.490    0.000 agent.py:112(__call__)
               56287125 1994.462    0.000 1994.462    0.000 {built-in method addmm}
               34639390 1947.246    0.000 1947.246    0.000 {built-in method cat}
               12988915   86.067    0.000 1931.787    0.000 agent.py:59(modify_board)
              463322467  200.326    0.000 1920.407    0.000 {built-in method builtins.all}
                8660190  165.810    0.000 1782.291    0.000 optimizer.py:167(zero_grad)
              433009500 1094.174    0.000 1780.899    0.000 layers.py:424(check)
             1926528220  545.862    0.000 1755.665    0.000 layers.py:690(<genexpr>)
                4330095   75.389    0.000 1624.345    0.000 replaybuffer.py:18(stacker)
               64071268   46.877    0.000 1546.477    0.000 level.py:38(elementsIn)
               18523077 1403.656    0.000 1403.656    0.000 {built-in method tensor}
              155883420 1336.738    0.000 1336.738    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               77936230   65.078    0.000 1302.555    0.000 activation.py:713(forward)
              433009500  814.766    0.000 1269.376    0.000 layers.py:437(check)
               12988915 1256.642    0.000 1256.642    0.000 {built-in method torch._C._nn.one_hot}
               77936230  104.486    0.000 1237.477    0.000 functional.py:1292(leaky_relu)
             3800977605 1002.431    0.000 1230.575    0.000 layers.py:700(<genexpr>)
              433009500  777.116    0.000 1221.880    0.000 layers.py:452(check)
              409451180 1154.593    0.000 1154.593    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              710132951  373.359    0.000 1128.405    0.000 overrides.py:1070(has_torch_function)
               77936230 1122.465    0.000 1122.465    0.000 {built-in method torch._C._nn.leaky_relu}
               30312867  162.502    0.000 1117.466    0.000 tensor.py:21(wrapped)
                8660190   12.242    0.000 1108.437    0.000 game.py:37(board)
              155883420 1105.451    0.000 1105.451    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               64071268  494.924    0.000 1005.709    0.000 level.py:39(<listcomp>)
             9653167909  897.802    0.000  897.802    0.000 layer.py:91(positions)
               77941710  779.610    0.000  779.610    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                4330095  448.717    0.000  777.666    0.000 collector.py:46(collect)
               85430040   75.908    0.000  763.947    0.000 layer.py:69(restart)
             9960671315  733.070    0.000  733.070    0.000 {built-in method builtins.hash}
              433009600  461.103    0.000  722.764    0.000 layers.py:442(isDone)
               77941710  721.240    0.000  721.240    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
             3039116169  710.829    0.000  710.829    0.000 level.py:32(inverse)
             1708526483  690.377    0.000  690.377    0.000 layer.py:146(elements)
                8658820  247.152    0.000  672.627    0.000 exploration.py:53(softmaxer)
               77941710  628.833    0.000  628.833    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              433009500  410.829    0.000  616.379    0.000 layers.py:402(check)
              433009500  385.998    0.000  577.303    0.000 layers.py:413(check)
               77941710  557.557    0.000  557.557    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               10678855  278.532    0.000  554.895    0.000 layers.py:36(reset)
             2691002354  497.080    0.000  497.080    0.000 enum.py:352(<genexpr>)
               64071268  307.750    0.000  493.891    0.000 {built-in method _functools.reduce}
              433009500  330.344    0.000  483.507    0.000 layers.py:23(check)
        5002755332/5002755330  359.135    0.000  479.471    0.000 {built-in method builtins.len}
              824933143  338.419    0.000  477.224    0.000 layer.py:130(add)
                8660190   13.412    0.000  455.713    0.000 loss.py:445(forward)
                8660190   51.945    0.000  442.300    0.000 functional.py:2637(mse_loss)
             1506865029  341.452    0.000  422.610    0.000 overrides.py:1083(<genexpr>)
               77941710  420.879    0.000  420.879    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               10678755  232.983    0.000  416.283    0.000 level.py:16(<dictcomp>)
               21650475  404.941    0.000  404.941    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
              442664029  246.130    0.000  358.405    0.000 layer.py:126(remove)
               56287125  355.713    0.000  355.713    0.000 {method 't' of 'torch._C._TensorBase' objects}
             3450205015  349.142    0.000  349.142    0.000 layer.py:203(isBlocking)
                4330095  116.407    0.000  320.276    0.000 random.py:315(sample)
               25980570  319.259    0.000  319.259    0.000 {built-in method sum}
             3954809370  318.752    0.000  318.752    0.000 {method 'random' of '_random.Random' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9550903: <Diamonds3_teleport_1> in cluster <dcc> Done

Job <Diamonds3_teleport_1> was submitted from host <n-62-30-4> by user <s183905> in cluster <dcc> at Tue Apr 20 16:21:49 2021
Job was executed on host(s) <n-62-20-12>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Fri Apr 23 07:21:03 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Fri Apr 23 07:21:03 2021
Terminated at Sat Apr 24 07:16:35 2021
Results reported at Sat Apr 24 07:16:35 2021

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

    CPU time :                                   85904.01 sec.
    Max Memory :                                 2676 MB
    Average Memory :                             2670.68 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13708.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86133 sec.
    Turnaround time :                            312886 sec.

The output (if any) is above this job summary.

