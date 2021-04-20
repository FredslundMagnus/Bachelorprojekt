
# Parameters

    Name :                      Diamonds2_0.5_UCB1-1
    Main :                      graphTrain
    Level :                     Levels.Causal5
    Failed actions chance :     0.5
    Hours :                     10.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.UCB1
    Network1 :                  Networks.Teleporter
    K1 :                        200000.0
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
    K2 :                        100000.0
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
    Softmax cap :               0.0
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                3
    Counterfacts :              2
    Topn :                      5
    Random counterfacts :       False
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      52093907511 function calls (46240776606 primitive calls) in 35706.81 seconds

##    Ordered by: cumulative time
   List reduced from 465 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35706.807 35706.807 {built-in method builtins.exec}
                      1    0.001    0.001 35706.807 35706.807 <string>:1(<module>)
                      1   88.833   88.833 35706.806 35706.806 allGraphsTrain.py:10(graphTrain)
                 353997  369.033    0.001 14756.306    0.042 allGraphsTrain.py:35(<listcomp>)
                7459593   11.477    0.000 14387.273    0.002 allGraphs.py:158(getInterventions)
                7459593    7.944    0.000 13492.637    0.002 allGraphs.py:133(UCB1)
        1004693069/7459593  600.290    0.000 13445.800    0.002 {built-in method builtins.min}
               27931115   13.428    0.000 13429.707    0.000 allGraphs.py:134(<lambda>)
        2001926545/27931115 3534.935    0.000 13416.280    0.000 allGraphs.py:68(expected_moves_UCB1)
        2971228906/96407230  946.845    0.000 13172.999    0.000 allGraphs.py:72(<genexpr>)
                 353997 3842.268    0.011 9318.203    0.026 allGraphs.py:146(transformNot)
                 353997    9.131    0.000 6289.207    0.018 allGraphsTrain.py:29(<listcomp>)
               35753798 1435.522    0.000 6280.096    0.000 allGraphs.py:110(states)
              495599224 6093.174    0.000 6093.174    0.000 {method 'item' of 'torch._C._TensorBase' objects}
              460196700 4567.333    0.000 4567.333    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
             1004693069  610.592    0.000 3852.430    0.000 allGraphs.py:83(layers_not_in)
            14756782455 2474.654    0.000 3584.382    0.000 enum.py:646(__hash__)
             1004693069 1567.065    0.000 3241.838    0.000 allGraphs.py:84(<listcomp>)
             2001926545 1840.632    0.000 2931.217    0.000 allGraphs.py:60(UCB1)
                 353997    1.233    0.000 1842.744    0.005 game.py:41(step)
                 353997    1.860    0.000 1762.935    0.005 layers.py:718(step)
            14756783668 1109.728    0.000 1109.728    0.000 {built-in method builtins.hash}
               10749006 1098.342    0.000 1098.342    0.000 {built-in method tensor}
                 353997   68.786    0.000 1054.755    0.003 allGraphsTrain.py:37(<listcomp>)
                9229579    5.816    0.000 1041.151    0.000 game.py:37(board)
                 353998   51.449    0.000  951.964    0.003 layers.py:684(update)
                7459593   38.492    0.000  883.158    0.000 allGraphs.py:153(format)
                 353997   27.736    0.000  807.009    0.002 layers.py:17(step)
                 353997    1.153    0.000  798.614    0.002 agent.py:29(learn)
                 353997    7.685    0.000  796.655    0.002 agent.py:117(_learn)
                 353997   23.563    0.000  788.970    0.002 learner.py:42(Qlearn)
               35399700   59.944    0.000  775.845    0.000 layer.py:98(move)
               37523682   92.179    0.000  636.564    0.000 tensor.py:21(wrapped)
                 353997   27.814    0.000  604.393    0.002 allGraphsTrain.py:44(<listcomp>)
                 882736    8.832    0.000  452.838    0.001 layers.py:740(restart)
               37169685  433.723    0.000  433.723    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               35399700  418.770    0.000  418.770    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               35399700  102.359    0.000  418.570    0.000 layers.py:735(check)
             2002988536  388.914    0.000  388.914    0.000 {built-in method builtins.max}
                 882736    4.202    0.000  376.832    0.000 level.py:8(__init__)
             2001622016  371.943    0.000  371.943    0.000 {built-in method math.log}
                 353997  188.843    0.001  348.058    0.001 agent.py:67(modify)
                 882736   14.070    0.000  341.638    0.000 levels.py:249(generate)
        8141931/1061991   33.269    0.000  315.309    0.000 module.py:715(_call_impl)
                 353997    2.185    0.000  313.497    0.001 grad_mode.py:23(decorate_context)
                5737604   54.349    0.000  312.594    0.000 level.py:41(notUsed)
                 353997   10.843    0.000  307.154    0.001 adam.py:55(step)
                 707994    1.942    0.000  287.957    0.000 network.py:27(forward)
                 707994    7.809    0.000  281.307    0.000 container.py:115(forward)
                 353997   56.043    0.000  250.824    0.001 functional.py:53(adam)
               35399700   69.889    0.000  242.422    0.000 layers.py:729(isFree)
             2004454127  226.563    0.000  226.563    0.000 {built-in method math.sqrt}
               98236659   61.417    0.000  222.557    0.000 {built-in method builtins.any}
                3185982  107.426    0.000  192.087    0.000 layer.py:167(NoRock_update)
                 353997    2.035    0.000  181.914    0.001 tensor.py:181(backward)
                 353997    1.361    0.000  179.879    0.001 __init__.py:68(backward)
              315272446  133.441    0.000  172.532    0.000 layer.py:95(isFree)
                 353997  170.233    0.000  170.233    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                 353997    4.466    0.000  169.146    0.000 agent.py:112(__call__)
                5737604    4.295    0.000  147.168    0.000 level.py:38(elementsIn)
               36815688  128.903    0.000  128.903    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                1061991    4.449    0.000  127.412    0.000 tensor.py:576(__iter__)
                1061991  120.135    0.000  120.135    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
              345170640   96.665    0.000  117.898    0.000 layers.py:700(<genexpr>)
               72923482   26.809    0.000  115.925    0.000 {built-in method builtins.all}
                1415988    2.664    0.000  111.970    0.000 conv.py:422(forward)
                1415988    3.060    0.000  108.320    0.000 conv.py:414(_conv_forward)
               61595612   33.313    0.000  108.072    0.000 overrides.py:1070(has_torch_function)
                1415988  104.697    0.000  104.697    0.000 {built-in method conv2d}
                5737604   48.608    0.000   95.888    0.000 level.py:39(<listcomp>)
                1415988    3.618    0.000   82.956    0.000 linear.py:92(forward)
               19823886   48.894    0.000   81.142    0.000 tensor.py:933(grad)
              137668678   38.607    0.000   79.307    0.000 layers.py:690(<genexpr>)
                1415988    6.088    0.000   77.801    0.000 functional.py:1669(linear)
                 353997    6.712    0.000   69.957    0.000 optimizer.py:167(zero_grad)
              270603829   67.042    0.000   67.042    0.000 level.py:32(inverse)
                7944624    6.347    0.000   64.476    0.000 layer.py:69(restart)
                 353997    2.685    0.000   56.256    0.000 agent.py:59(modify_board)
               17697027   35.022    0.000   56.001    0.000 layers.py:387(check)
                1415988   54.891    0.000   54.891    0.000 {built-in method addmm}
                 353997   31.677    0.000   54.729    0.000 collector.py:46(collect)
               17702027   33.741    0.000   54.286    0.000 layers.py:349(check)
               17702051   33.221    0.000   53.720    0.000 layers.py:337(check)
              531552011   53.082    0.000   53.082    0.000 layer.py:91(positions)
               17705404   32.621    0.000   52.994    0.000 layers.py:375(check)
                5663952   50.161    0.000   50.161    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              137792982   48.349    0.000   48.349    0.000 layer.py:146(elements)
                 882836   24.227    0.000   48.037    0.000 layers.py:36(reset)
                5737604   29.423    0.000   46.986    0.000 {built-in method _functools.reduce}
              238333805   45.758    0.000   45.758    0.000 enum.py:352(<genexpr>)
              162130894   36.341    0.000   42.993    0.000 overrides.py:1083(<genexpr>)
                5663952   41.998    0.000   41.998    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                 353997   27.333    0.000   40.400    0.000 allGraphsTrain.py:43(<listcomp>)
                2123982    2.011    0.000   37.367    0.000 activation.py:713(forward)
               66063202   27.424    0.000   37.290    0.000 layer.py:130(add)
                 353997   36.897    0.000   36.897    0.000 {built-in method torch._C._nn.one_hot}
                2123982    3.463    0.000   35.356    0.000 functional.py:1292(leaky_relu)
              315272446   32.608    0.000   32.608    0.000 layer.py:203(isBlocking)
                2123982   31.567    0.000   31.567    0.000 {built-in method torch._C._nn.leaky_relu}
        370379027/370379025   24.231    0.000   30.369    0.000 {built-in method builtins.len}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9531986: <Diamonds2_0.5_UCB1_1> in cluster <dcc> Done

Job <Diamonds2_0.5_UCB1_1> was submitted from host <n-62-30-7> by user <s183905> in cluster <dcc> at Sat Apr 17 13:24:03 2021
Job was executed on host(s) <n-62-20-13>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sat Apr 17 13:24:03 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat Apr 17 13:24:03 2021
Terminated at Sat Apr 17 23:19:26 2021
Results reported at Sat Apr 17 23:19:26 2021

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
#BSUB -W 720
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $LSB_PROJECT_NAME


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   35619.54 sec.
    Max Memory :                                 2061 MB
    Average Memory :                             2053.32 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14323.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35723 sec.
    Turnaround time :                            35723 sec.

The output (if any) is above this job summary.

