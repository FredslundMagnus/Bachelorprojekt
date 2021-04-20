
# Parameters

    Name :                      Diamonds2_0.0_var-2
    Main :                      graphTrain
    Level :                     Levels.Causal5
    Failed actions chance :     0.0
    Hours :                     10.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.var
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


      45759662427 function calls (40918577816 primitive calls) in 35703.31 seconds

##    Ordered by: cumulative time
   List reduced from 466 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35703.311 35703.311 {built-in method builtins.exec}
                      1    0.001    0.001 35703.311 35703.311 <string>:1(<module>)
                      1  108.539  108.539 35703.309 35703.309 allGraphsTrain.py:10(graphTrain)
                 470662 4631.792    0.010 11248.171    0.024 allGraphs.py:146(transformNot)
                 470662  412.234    0.001 9949.838    0.021 allGraphsTrain.py:35(<listcomp>)
                7070704   12.125    0.000 9537.604    0.001 allGraphs.py:158(getInterventions)
                6336794    5.742    0.000 8702.500    0.001 allGraphs.py:129(rightIntervention)
        830699285/6336794  425.613    0.000 8667.997    0.001 {built-in method builtins.min}
               23443419    9.788    0.000 8655.663    0.000 allGraphs.py:130(<lambda>)
        1655061776/23443419 2514.872    0.000 8645.875    0.000 allGraphs.py:74(expected_moves)
        2455980848/80290708  681.523    0.000 8486.153    0.000 allGraphs.py:78(<genexpr>)
                 470662   10.890    0.000 7541.471    0.016 allGraphsTrain.py:29(<listcomp>)
               47536963 1708.310    0.000 7530.598    0.000 allGraphs.py:110(states)
              658931160 7409.698    0.000 7409.698    0.000 {method 'item' of 'torch._C._TensorBase' objects}
              611861200 5448.757    0.000 5448.757    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
            13006227050 1955.934    0.000 2807.567    0.000 enum.py:646(__hash__)
              831433195  428.705    0.000 2764.486    0.000 allGraphs.py:83(layers_not_in)
                 470662    1.451    0.000 2730.101    0.006 game.py:41(step)
                 470662    2.025    0.000 2628.005    0.006 layers.py:718(step)
              831433195 1110.540    0.000 2335.782    0.000 allGraphs.py:84(<listcomp>)
                 470662   33.538    0.000 1333.045    0.003 layers.py:17(step)
               47066200   70.682    0.000 1295.544    0.000 layer.py:98(move)
                 470663   62.078    0.000 1290.488    0.003 layers.py:684(update)
                 470662   79.833    0.000 1263.516    0.003 allGraphsTrain.py:37(<listcomp>)
             1655061776  791.240    0.000 1151.012    0.000 allGraphs.py:45(p)
               11433654 1115.955    0.000 1115.955    0.000 {built-in method tensor}
                9424015    5.770    0.000 1043.476    0.000 game.py:37(board)
                 470662    1.530    0.000  960.490    0.002 agent.py:29(learn)
                 470662    9.101    0.000  958.051    0.002 agent.py:117(_learn)
                 470662   27.994    0.000  948.950    0.002 learner.py:42(Qlearn)
               47066200  183.197    0.000  868.231    0.000 layers.py:735(check)
            13006228647  851.633    0.000  851.633    0.000 {built-in method builtins.hash}
                7070704   32.154    0.000  811.690    0.000 allGraphs.py:153(format)
               49890172  109.548    0.000  766.030    0.000 tensor.py:21(wrapped)
                 470662   33.308    0.000  726.674    0.002 allGraphsTrain.py:44(<listcomp>)
                1509386   12.816    0.000  683.014    0.000 layers.py:740(restart)
                1509386    5.941    0.000  568.663    0.000 level.py:8(__init__)
               49419510  525.000    0.000  525.000    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                1509386   20.436    0.000  516.225    0.000 levels.py:249(generate)
               47066200  497.766    0.000  497.766    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                9811240   83.233    0.000  473.553    0.000 level.py:41(notUsed)
                 470662  236.496    0.001  430.352    0.001 agent.py:67(modify)
                 470662    2.584    0.000  376.543    0.001 grad_mode.py:23(decorate_context)
        10825226/1411986   39.658    0.000  375.916    0.000 module.py:715(_call_impl)
                 470662   12.787    0.000  368.809    0.001 adam.py:55(step)
                 941324    2.413    0.000  343.261    0.000 network.py:27(forward)
                 941324    8.883    0.000  335.256    0.000 container.py:115(forward)
                 470662   67.209    0.000  302.771    0.001 functional.py:53(adam)
               47066200   79.174    0.000  290.321    0.000 layers.py:729(isFree)
             1657207672  267.810    0.000  272.045    0.000 {built-in method builtins.max}
              130276209   73.138    0.000  257.129    0.000 {built-in method builtins.any}
                4235967  136.755    0.000  239.985    0.000 layer.py:167(NoRock_update)
                 470662    2.336    0.000  222.172    0.000 tensor.py:181(backward)
                9811240    6.451    0.000  221.445    0.000 level.py:38(elementsIn)
                 470662    1.617    0.000  219.837    0.000 __init__.py:68(backward)
              410133030  155.810    0.000  211.148    0.000 layer.py:95(isFree)
                 470662  208.478    0.000  208.478    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                 470662    5.363    0.000  200.939    0.000 agent.py:112(__call__)
               48948848  156.241    0.000  156.241    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                1411986    5.286    0.000  153.406    0.000 tensor.py:576(__iter__)
               96956472   32.528    0.000  145.116    0.000 {built-in method builtins.all}
                1411986  144.845    0.000  144.845    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
                9811240   69.618    0.000  144.511    0.000 level.py:39(<listcomp>)
                1882648    2.956    0.000  134.854    0.000 conv.py:422(forward)
              455569140  110.198    0.000  134.490    0.000 layers.py:700(<genexpr>)
                1882648    3.613    0.000  130.746    0.000 conv.py:414(_conv_forward)
               81895322   39.891    0.000  127.219    0.000 overrides.py:1070(has_torch_function)
                1882648  126.439    0.000  126.439    0.000 {built-in method conv2d}
               47066200   75.500    0.000  123.658    0.000 layers.py:387(check)
               47066200   73.972    0.000  121.197    0.000 layers.py:337(check)
               47066200   74.287    0.000  120.790    0.000 layers.py:349(check)
               47066200   71.667    0.000  118.304    0.000 layers.py:375(check)
             1137786329  105.611    0.000  105.611    0.000 layer.py:91(positions)
              462731515  101.838    0.000  101.838    0.000 level.py:32(inverse)
              186341819   47.174    0.000  101.142    0.000 layers.py:690(<genexpr>)
                1882648    4.099    0.000   98.727    0.000 linear.py:92(forward)
               13584474    9.339    0.000   97.305    0.000 layer.py:69(restart)
               26357126   57.578    0.000   95.607    0.000 tensor.py:933(grad)
                1882648    7.098    0.000   92.761    0.000 functional.py:1669(linear)
                 470662    7.609    0.000   83.160    0.000 optimizer.py:167(zero_grad)
                1509486   36.697    0.000   73.159    0.000 layers.py:36(reset)
                9811240   43.917    0.000   70.483    0.000 {built-in method _functools.reduce}
              407544101   69.754    0.000   69.754    0.000 enum.py:352(<genexpr>)
                 470662    3.218    0.000   69.054    0.000 agent.py:59(modify_board)
                 470662   38.387    0.000   66.338    0.000 collector.py:46(collect)
                1882648   65.852    0.000   65.852    0.000 {built-in method addmm}
                7530592   60.770    0.000   60.770    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              212851401   60.077    0.000   60.077    0.000 layer.py:146(elements)
               47066200   38.276    0.000   59.472    0.000 layers.py:364(check)
               47066200   35.210    0.000   55.959    0.000 layers.py:326(check)
                7530592   51.397    0.000   51.397    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              102937197   37.394    0.000   51.360    0.000 layer.py:130(add)
              215563464   41.501    0.000   49.212    0.000 overrides.py:1083(<genexpr>)
              410133030   47.840    0.000   47.840    0.000 layer.py:203(isBlocking)
                 470662   31.763    0.000   47.573    0.000 allGraphsTrain.py:43(<listcomp>)
               47066200   31.707    0.000   47.135    0.000 layers.py:23(check)
                 470662   45.630    0.000   45.630    0.000 {built-in method torch._C._nn.one_hot}
                2823972    2.316    0.000   43.978    0.000 activation.py:713(forward)
                1509386   19.635    0.000   42.327    0.000 level.py:16(<dictcomp>)
                2823972    3.778    0.000   41.663    0.000 functional.py:1292(leaky_relu)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9532039: <Diamonds2_0.0_var_2> in cluster <dcc> Done

Job <Diamonds2_0.0_var_2> was submitted from host <n-62-30-7> by user <s183905> in cluster <dcc> at Sat Apr 17 13:28:45 2021
Job was executed on host(s) <n-62-20-2>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Tue Apr 20 06:01:09 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue Apr 20 06:01:09 2021
Terminated at Tue Apr 20 15:56:16 2021
Results reported at Tue Apr 20 15:56:16 2021

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

    CPU time :                                   35619.23 sec.
    Max Memory :                                 2067 MB
    Average Memory :                             2066.91 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14317.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35710 sec.
    Turnaround time :                            268051 sec.

The output (if any) is above this job summary.

