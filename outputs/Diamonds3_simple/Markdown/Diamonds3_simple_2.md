Start
True
True
['main.py', '-name', 'Diamonds3_simple-2', '-hours', '24.0', '-level', 'Levels.Causal6', '-main', 'simple', '-network2', 'Networks.MiniBig']

# Parameters

    Name :                      Diamonds3_simple-2
    Main :                      simple
    Level :                     Levels.Causal6
    Failed actions chance :     0.5
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


      161814228623 function calls (161532553204 primitive calls) in 86113.95 seconds

##    Ordered by: cumulative time
   List reduced from 408 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86113.949 86113.949 {built-in method builtins.exec}
                      1    0.001    0.001 86113.949 86113.949 <string>:1(<module>)
                      1  176.883  176.883 86113.948 86113.948 main.py:71(simple)
               11736461   39.435    0.000 47780.810    0.004 game.py:41(step)
               11736461   53.138    0.000 45325.366    0.004 layers.py:718(step)
               11736461   34.932    0.000 29733.106    0.003 agent.py:29(learn)
               11736461  260.007    0.000 29675.204    0.003 agent.py:117(_learn)
               11736461  765.518    0.000 29415.197    0.003 learner.py:42(Qlearn)
               11736461  895.172    0.000 22927.598    0.002 layers.py:17(step)
               11736462 1638.591    0.000 22276.402    0.002 layers.py:684(update)
             1173646100 1911.507    0.000 21925.520    0.000 layer.py:98(move)
               11736461   68.627    0.000 12141.321    0.001 grad_mode.py:23(decorate_context)
               11736461  413.338    0.000 11941.461    0.001 adam.py:55(step)
             1173646100 2941.862    0.000 11781.331    0.000 layers.py:735(check)
        316884447/35209383 1207.892    0.000 11753.104    0.000 module.py:715(_call_impl)
               23472922   54.884    0.000 10904.834    0.000 network.py:27(forward)
               23472922  293.236    0.000 10705.799    0.000 container.py:115(forward)
               11736461 2184.914    0.000 9790.340    0.001 functional.py:53(adam)
               15510639  135.131    0.000 7011.224    0.000 layers.py:740(restart)
             1173646100 1781.237    0.000 6558.526    0.000 layers.py:729(isFree)
               11736461   64.407    0.000 6479.608    0.001 tensor.py:181(backward)
               11736461   38.140    0.000 6415.202    0.001 __init__.py:68(backward)
               11736461 6117.931    0.001 6117.931    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               11736461  132.840    0.000 6099.988    0.001 agent.py:112(__call__)
               15510639   65.336    0.000 5780.226    0.000 level.py:8(__init__)
             2261362976 1438.750    0.000 5380.093    0.000 {built-in method builtins.any}
               93891696 2887.035    0.000 5197.254    0.000 layer.py:167(NoRock_update)
               15510639  220.918    0.000 5163.959    0.000 levels.py:288(generate)
             8515273020 3749.321    0.000 4777.289    0.000 layer.py:95(isFree)
               93062852  852.927    0.000 4719.077    0.000 level.py:41(notUsed)
            14647568243 2618.879    0.000 3793.914    0.000 enum.py:646(__hash__)
               46945844   82.153    0.000 3786.181    0.000 conv.py:422(forward)
               46945844   95.028    0.000 3672.970    0.000 conv.py:414(_conv_forward)
               70418766  159.331    0.000 3593.781    0.000 linear.py:92(forward)
             1173646200  422.367    0.000 3563.664    0.000 {built-in method builtins.all}
               46945844 3559.422    0.000 3559.422    0.000 {built-in method conv2d}
               49635769 3453.111    0.000 3453.111    0.000 {built-in method tensor}
            10423220049 2742.307    0.000 3368.411    0.000 layers.py:700(<genexpr>)
               70418766  258.134    0.000 3360.750    0.000 functional.py:1669(linear)
             3815653742  981.726    0.000 3284.122    0.000 layers.py:690(<genexpr>)
              821552300 1861.194    0.000 3106.568    0.000 tensor.py:933(grad)
               11736461  291.383    0.000 2751.327    0.000 optimizer.py:167(zero_grad)
               23472922   22.521    0.000 2739.171    0.000 game.py:37(board)
              586854622 1569.410    0.000 2570.002    0.000 layers.py:424(check)
               70418766 2356.570    0.000 2356.570    0.000 {built-in method addmm}
               93062852   69.481    0.000 2184.454    0.000 level.py:38(elementsIn)
              234729220 1978.497    0.000 1978.497    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
             1173646200 1263.350    0.000 1953.092    0.000 layers.py:113(isDone)
              586830357 1028.490    0.000 1674.807    0.000 layers.py:437(check)
              234729220 1658.397    0.000 1658.397    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              586844103 1012.286    0.000 1644.748    0.000 layers.py:452(check)
            16402605000 1574.834    0.000 1574.834    0.000 layer.py:91(positions)
             1009335726  503.368    0.000 1532.027    0.000 overrides.py:1070(has_torch_function)
               93891688   83.601    0.000 1504.475    0.000 activation.py:713(forward)
               93891688  120.069    0.000 1420.874    0.000 functional.py:1292(leaky_relu)
               93062852  687.297    0.000 1408.069    0.000 level.py:39(<listcomp>)
               93891688 1287.745    0.000 1287.745    0.000 {built-in method torch._C._nn.leaky_relu}
             3354849341 1273.511    0.000 1273.511    0.000 layer.py:146(elements)
            14647615272 1175.044    0.000 1175.044    0.000 {built-in method builtins.hash}
              117364610 1120.710    0.000 1120.710    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              117364610 1057.873    0.000 1057.873    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              124085112  103.982    0.000 1054.804    0.000 layer.py:69(restart)
             4414284822 1009.939    0.000 1009.939    0.000 level.py:32(inverse)
               11736461  587.816    0.000 1008.392    0.000 collector.py:46(collect)
              117364610  942.117    0.000  942.117    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
             1588273444  631.565    0.000  880.867    0.000 layer.py:130(add)
             8515273020  832.054    0.000  832.054    0.000 layer.py:203(isBlocking)
            10659625051  815.152    0.000  815.152    0.000 {method 'random' of '_random.Random' objects}
              117364610  814.586    0.000  814.586    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               15510739  396.681    0.000  800.742    0.000 layers.py:36(reset)
              586812212  489.776    0.000  763.286    0.000 layers.py:413(check)
        11529706938/11529706937  689.593    0.000  763.206    0.000 {built-in method builtins.len}
              586794458  483.303    0.000  754.286    0.000 layers.py:402(check)
             3908647207  707.865    0.000  707.865    0.000 enum.py:352(<genexpr>)
               93062852  440.999    0.000  706.904    0.000 {built-in method _functools.reduce}
             1006053657  473.798    0.000  705.261    0.000 layer.py:126(remove)
              117364610  647.719    0.000  647.719    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              586846182  424.741    0.000  627.552    0.000 layers.py:23(check)
             9265084488  626.104    0.000  626.104    0.000 layer.py:84(isDead)
             2089090218  457.262    0.000  565.157    0.000 overrides.py:1083(<genexpr>)
               11736461   14.848    0.000  563.221    0.000 loss.py:445(forward)
               11736461   62.947    0.000  548.373    0.000 functional.py:2637(mse_loss)
               15510639  261.179    0.000  508.910    0.000 level.py:16(<dictcomp>)
               11736461   41.321    0.000  474.369    0.000 exploration.py:47(epsilonGreedy)
               70418766  428.837    0.000  428.837    0.000 {method 't' of 'torch._C._TensorBase' objects}
             4874328798  410.823    0.000  410.823    0.000 {method 'append' of 'list' objects}
               11736461  333.238    0.000  333.238    0.000 {method 'tolist' of 'torch._C._TensorBase' objects}
               23472922  324.154    0.000  324.154    0.000 {built-in method sum}
               11736461  318.409    0.000  318.409    0.000 {built-in method torch._C._nn.mse_loss}
              117364660  137.238    0.000  316.052    0.000 tensor.py:596(__hash__)
               93891696  297.312    0.000  297.312    0.000 layer.py:178(<listcomp>)
               11737634  290.047    0.000  290.047    0.000 {built-in method max}
               93891696  280.742    0.000  280.742    0.000 layer.py:179(<listcomp>)
             3257199820  265.905    0.000  265.905    0.000 level.py:39(<lambda>)
               46945844   35.145    0.000  261.813    0.000 flatten.py:39(forward)
               11736461   44.790    0.000  249.241    0.000 __init__.py:28(_make_grads)
               11736461  240.548    0.000  240.548    0.000 {built-in method gather}
               46945844  226.668    0.000  226.668    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              117262305  143.817    0.000  223.847    0.000 layers.py:442(isDone)
               11736461   54.252    0.000  222.653    0.000 tensor.py:506(__rsub__)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9578842: <Diamonds3_simple_2> in cluster <dcc> Done

Job <Diamonds3_simple_2> was submitted from host <n-62-30-3> by user <s183905> in cluster <dcc> at Mon Apr 26 20:44:05 2021
Job was executed on host(s) <n-62-11-15>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sat May  1 22:47:41 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat May  1 22:47:41 2021
Terminated at Sun May  2 22:43:03 2021
Results reported at Sun May  2 22:43:03 2021

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

    CPU time :                                   85893.85 sec.
    Max Memory :                                 2063 MB
    Average Memory :                             2060.29 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14321.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86122 sec.
    Turnaround time :                            525538 sec.

The output (if any) is above this job summary.

