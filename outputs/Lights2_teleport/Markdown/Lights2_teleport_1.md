
# Parameters

    Name :                      Lights2_teleport-1
    Main :                      teleport
    Level :                     Levels.Causal4
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


      96002189125 function calls (95725832018 primitive calls) in 86110.99 seconds

##    Ordered by: cumulative time
   List reduced from 483 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86110.992 86110.992 {built-in method builtins.exec}
                      1    1.550    1.550 86110.992 86110.992 <string>:1(<module>)
                      1  246.597  246.597 86109.442 86109.442 main.py:45(teleport)
                4947679   21.296    0.000 31223.966    0.006 game.py:41(step)
                4947679   29.318    0.000 29976.172    0.006 layers.py:718(step)
                9895358   39.004    0.000 28358.721    0.003 agent.py:29(learn)
                9895358  672.629    0.000 23785.371    0.002 learner.py:42(Qlearn)
                4947679  444.033    0.000 19540.088    0.004 layers.py:17(step)
              494767900 1441.229    0.000 19049.551    0.000 layer.py:98(move)
                4947679  169.835    0.000 17139.739    0.003 agent.py:54(_learn)
              494767900 2311.551    0.000 12103.198    0.000 layers.py:735(check)
        310930355/34574259 1191.322    0.000 11604.388    0.000 module.py:715(_call_impl)
                4947679  135.684    0.000 11160.297    0.002 agent.py:117(_learn)
               24678901   59.006    0.000 10797.107    0.000 network.py:27(forward)
               24678901  291.614    0.000 10587.952    0.000 container.py:115(forward)
                4947680  728.567    0.000 10362.396    0.002 layers.py:684(update)
                9895358   63.288    0.000 9476.339    0.001 grad_mode.py:23(decorate_context)
                9895358  323.984    0.000 9296.057    0.001 adam.py:55(step)
                9895358 1723.280    0.000 7637.581    0.001 functional.py:53(adam)
                4947679 5039.163    0.001 7269.765    0.001 replaybuffer.py:22(sample_data)
                9835864  232.803    0.000 7215.900    0.001 agent.py:49(__call__)
                4947679 2419.896    0.000 5918.947    0.001 agent.py:88(interveen)
                9895358   58.054    0.000 5675.520    0.001 tensor.py:181(backward)
                9895358   37.703    0.000 5617.467    0.001 __init__.py:68(backward)
                9895358 5347.059    0.001 5347.059    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                4947679 2423.161    0.000 4727.809    0.001 agent.py:67(modify)
              494767900  933.432    0.000 4533.444    0.000 layers.py:729(isFree)
                4947679 2503.456    0.001 4500.360    0.001 replaybuffer.py:28(teleporter_save_data)
               49357802   81.715    0.000 3913.643    0.000 conv.py:422(forward)
               49476800 2332.668    0.000 3854.114    0.000 layer.py:151(update)
               49357802   96.725    0.000 3795.897    0.000 conv.py:414(_conv_forward)
               49357802 3681.023    0.000 3681.023    0.000 {built-in method conv2d}
             4131749913 2939.850    0.000 3600.013    0.000 layer.py:95(isFree)
               64141345  154.458    0.000 3414.854    0.000 linear.py:92(forward)
               64141345  236.225    0.000 3191.340    0.000 functional.py:1669(linear)
             1385149608  844.558    0.000 3135.902    0.000 {built-in method builtins.any}
             9233956346 1692.789    0.000 2417.183    0.000 enum.py:646(__hash__)
              623407608 1426.417    0.000 2378.164    0.000 tensor.py:933(grad)
               64141345 2259.305    0.000 2259.305    0.000 {built-in method addmm}
                4947679   69.343    0.000 2258.610    0.000 agent.py:112(__call__)
               14783543  101.357    0.000 2234.296    0.000 agent.py:59(modify_board)
               39521938 2223.162    0.000 2223.162    0.000 {built-in method cat}
                9895358  195.099    0.000 2062.220    0.000 optimizer.py:167(zero_grad)
              494767900 1429.683    0.000 1912.694    0.000 layers.py:77(check)
                4947679   86.577    0.000 1850.221    0.000 replaybuffer.py:18(stacker)
                4793683   59.080    0.000 1813.828    0.000 layers.py:740(restart)
               21119973 1810.713    0.000 1810.713    0.000 {built-in method tensor}
             5389717487 1470.305    0.000 1799.358    0.000 layers.py:700(<genexpr>)
              494767900 1124.206    0.000 1760.468    0.000 layers.py:246(check)
              145353588 1653.218    0.000 1653.218    0.000 {built-in method clone}
              494767900  986.942    0.000 1612.660    0.000 layers.py:286(check)
              178116444 1533.844    0.000 1533.844    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              529404947  296.367    0.000 1494.526    0.000 {built-in method builtins.all}
                9895358   12.722    0.000 1468.977    0.000 game.py:37(board)
               88820246   74.031    0.000 1466.208    0.000 activation.py:713(forward)
               14783543 1452.335    0.000 1452.335    0.000 {built-in method torch._C._nn.one_hot}
               88820246  113.023    0.000 1392.178    0.000 functional.py:1292(leaky_relu)
              811243229  430.786    0.000 1297.590    0.000 overrides.py:1070(has_torch_function)
               34636947  179.965    0.000 1287.850    0.000 tensor.py:21(wrapped)
                4793683   27.813    0.000 1280.801    0.000 level.py:8(__init__)
              178116444 1273.002    0.000 1273.002    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               88820246 1267.428    0.000 1267.428    0.000 {built-in method torch._C._nn.leaky_relu}
             3099802856  790.443    0.000 1233.094    0.000 layers.py:690(<genexpr>)
            11880067032 1189.896    0.000 1189.896    0.000 layer.py:91(positions)
                4793683  161.128    0.000 1006.193    0.000 levels.py:199(generate)
              494767900  758.085    0.000 1003.543    0.000 layers.py:62(check)
             1539219306  946.723    0.000  946.723    0.000 layer.py:146(elements)
                4947679  518.722    0.000  891.229    0.000 collector.py:46(collect)
              494767900  572.132    0.000  887.382    0.000 layers.py:313(check)
               89058222  881.526    0.000  881.526    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              494767900  524.100    0.000  838.496    0.000 layers.py:273(check)
               89058222  832.539    0.000  832.539    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                9835864  272.189    0.000  767.584    0.000 exploration.py:53(softmaxer)
               89058222  725.965    0.000  725.965    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
             9233992313  724.401    0.000  724.401    0.000 {built-in method builtins.hash}
              494767900  487.838    0.000  711.912    0.000 layers.py:48(check)
                9587366   81.936    0.000  684.066    0.000 level.py:41(notUsed)
               89058222  641.723    0.000  641.723    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
        6664101443/6664101441  459.599    0.000  597.292    0.000 {built-in method builtins.len}
              494767900  383.117    0.000  558.937    0.000 layers.py:23(check)
                9895358   15.075    0.000  527.171    0.000 loss.py:445(forward)
                9895358   59.106    0.000  512.096    0.000 functional.py:2637(mse_loss)
              160137131  498.899    0.000  498.899    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
             1721263767  388.554    0.000  484.945    0.000 overrides.py:1083(<genexpr>)
               89058222  478.575    0.000  478.575    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               24738395  465.273    0.000  465.273    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               47936830   66.193    0.000  457.890    0.000 layer.py:69(restart)
             5461775628  456.833    0.000  456.833    0.000 {method 'random' of '_random.Random' objects}
               14535045  170.222    0.000  451.640    0.000 random.py:315(sample)
              721195369  314.738    0.000  429.918    0.000 layer.py:130(add)
               64141345  412.464    0.000  412.464    0.000 {method 't' of 'torch._C._TensorBase' objects}
                4949645  373.486    0.000  373.486    0.000 {method 'ne' of 'torch._C._TensorBase' objects}
               29686074  363.638    0.000  363.638    0.000 {built-in method sum}
              433077271  230.908    0.000  350.716    0.000 layer.py:126(remove)
             3240258906  344.062    0.000  344.062    0.000 layer.py:203(isBlocking)
             4899743170  329.054    0.000  329.054    0.000 layer.py:84(isDead)
                9895358  295.179    0.000  295.179    0.000 {built-in method torch._C._nn.mse_loss}
                4947679   23.622    0.000  276.795    0.000 exploration.py:47(epsilonGreedy)
                9896835  272.625    0.000  272.625    0.000 {built-in method max}
              194863937  271.655    0.000  271.655    0.000 level.py:32(inverse)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9550893: <Lights2_teleport_1> in cluster <dcc> Done

Job <Lights2_teleport_1> was submitted from host <n-62-30-4> by user <s183905> in cluster <dcc> at Tue Apr 20 16:21:47 2021
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Wed Apr 21 07:27:55 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed Apr 21 07:27:55 2021
Terminated at Thu Apr 22 07:23:13 2021
Results reported at Thu Apr 22 07:23:13 2021

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

    CPU time :                                   85903.40 sec.
    Max Memory :                                 2682 MB
    Average Memory :                             2678.06 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13702.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86119 sec.
    Turnaround time :                            140486 sec.

The output (if any) is above this job summary.

