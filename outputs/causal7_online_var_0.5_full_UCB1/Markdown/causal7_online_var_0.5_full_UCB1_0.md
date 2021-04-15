
# Parameters

    Name :                      causal7_online_var_0.5_full_UCB1-0
    Main :                      graphTrain
    Level :                     Levels.Causal7
    Failed actions chance :     0.5
    Hours :                     12.0
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
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                3
    Counterfacts :              2
    Topn :                      5
    Random counterfacts :       False
    Minutes used :              715 minutes.
    Hours used :                11 hours.

# Profiling


      21727665102 function calls (20973085881 primitive calls) in 42909.44 seconds

##    Ordered by: cumulative time
   List reduced from 465 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 42909.441 42909.441 {built-in method builtins.exec}
                      1    0.009    0.009 42909.441 42909.441 <string>:1(<module>)
                      1  275.124  275.124 42909.432 42909.432 allGraphsTrain.py:10(graphTrain)
                 807942 6299.957    0.008 15636.995    0.019 allGraphs.py:146(transformNot)
              807948856 10919.533    0.000 10919.533    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                 807942   21.550    0.000 9967.501    0.012 allGraphsTrain.py:29(<listcomp>)
               81602243 2199.612    0.000 9945.964    0.000 allGraphs.py:110(states)
              727148200 7041.835    0.000 7041.835    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 807942  913.626    0.001 4754.765    0.006 allGraphsTrain.py:35(<listcomp>)
                 807942    4.278    0.000 4017.975    0.005 game.py:41(step)
               18767189   28.413    0.000 3841.139    0.000 allGraphs.py:158(getInterventions)
                 807942    5.736    0.000 3834.142    0.005 layers.py:718(step)
                 807942  155.466    0.000 2450.273    0.003 allGraphsTrain.py:37(<listcomp>)
               26234236 2301.269    0.000 2301.269    0.000 {built-in method tensor}
               22806900   13.638    0.000 2180.156    0.000 game.py:37(board)
                 807943  131.677    0.000 2153.059    0.003 layers.py:684(update)
                 807942    4.047    0.000 2007.554    0.002 agent.py:29(learn)
                 807942   21.091    0.000 2001.033    0.002 agent.py:117(_learn)
                 807942   62.346    0.000 1979.942    0.002 learner.py:42(Qlearn)
               18767189   17.609    0.000 1959.661    0.000 allGraphs.py:133(UCB1)
        168044788/18767189  118.637    0.000 1866.900    0.000 {built-in method builtins.min}
               18767189   83.558    0.000 1853.066    0.000 allGraphs.py:153(format)
               47311198   22.147    0.000 1835.645    0.000 allGraphs.py:134(<lambda>)
        317322387/47311198  488.470    0.000 1813.498    0.000 allGraphs.py:68(expected_moves_UCB1)
                 807942   75.794    0.000 1668.584    0.002 layers.py:17(step)
               80794200  138.474    0.000 1584.347    0.000 layer.py:98(move)
        419288788/100157578  130.601    0.000 1487.460    0.000 allGraphs.py:72(<genexpr>)
               85641852  211.909    0.000 1481.200    0.000 tensor.py:21(wrapped)
                 807942   68.394    0.000 1397.665    0.002 allGraphsTrain.py:44(<listcomp>)
                2541050   25.926    0.000 1048.100    0.000 layers.py:740(restart)
               84833910 1013.207    0.000 1013.207    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               80794200  908.116    0.000  908.116    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                 807942  474.627    0.001  899.066    0.001 agent.py:67(modify)
        18582666/2423826   93.857    0.000  854.526    0.000 module.py:715(_call_impl)
                2541050   12.566    0.000  835.105    0.000 level.py:8(__init__)
             3069418632  548.784    0.000  806.868    0.000 enum.py:646(__hash__)
                1615884    5.505    0.000  771.827    0.000 network.py:24(forward)
                1615884   21.189    0.000  752.847    0.000 container.py:115(forward)
                 807942    6.816    0.000  743.261    0.001 grad_mode.py:23(decorate_context)
               80794200  179.767    0.000  731.467    0.000 layers.py:735(check)
                 807942   28.729    0.000  723.739    0.001 adam.py:55(step)
                2541050   30.839    0.000  711.495    0.000 levels.py:446(generate)
               12196680  119.843    0.000  648.177    0.000 level.py:41(notUsed)
                 807942  132.677    0.000  591.572    0.001 functional.py:53(adam)
               80794200  124.018    0.000  574.724    0.000 layers.py:729(isFree)
              168044788  106.268    0.000  515.106    0.000 allGraphs.py:83(layers_not_in)
                 807942    5.732    0.000  492.805    0.001 tensor.py:181(backward)
                 807942    4.938    0.000  487.073    0.001 __init__.py:68(backward)
              317322387  306.306    0.000  486.426    0.000 allGraphs.py:60(UCB1)
                 807942   16.365    0.000  482.766    0.001 agent.py:112(__call__)
                 807942  459.556    0.001  459.556    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
              552744930  377.098    0.000  450.706    0.000 layer.py:95(isFree)
              223682945  126.598    0.000  430.599    0.000 {built-in method builtins.any}
                5655601  245.924    0.000  422.346    0.000 layer.py:167(NoRock_update)
              168044788  200.021    0.000  408.838    0.000 allGraphs.py:84(<listcomp>)
                2423826   12.638    0.000  338.863    0.000 tensor.py:576(__iter__)
                2423826  317.811    0.000  317.811    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
                3231768    7.534    0.000  307.782    0.000 conv.py:422(forward)
              166436152   54.902    0.000  305.512    0.000 {built-in method builtins.all}
               12196680    9.533    0.000  300.205    0.000 level.py:38(elementsIn)
                3231768    9.684    0.000  296.860    0.000 conv.py:414(_conv_forward)
               84025968  290.013    0.000  290.013    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                3231768  285.833    0.000  285.833    0.000 {built-in method conv2d}
             3069421285  258.084    0.000  258.084    0.000 {built-in method builtins.hash}
              140582042   75.133    0.000  244.515    0.000 overrides.py:1070(has_torch_function)
              249388674   68.527    0.000  227.729    0.000 layers.py:690(<genexpr>)
                3231768    9.178    0.000  221.187    0.000 linear.py:92(forward)
                3231768   15.657    0.000  207.477    0.000 functional.py:1669(linear)
              626026000  168.501    0.000  206.484    0.000 layers.py:700(<genexpr>)
               12196680   96.928    0.000  195.377    0.000 level.py:39(<listcomp>)
               45244806  110.075    0.000  182.246    0.000 tensor.py:933(grad)
               17787350   15.618    0.000  180.696    0.000 layer.py:69(restart)
                 807942   15.490    0.000  157.765    0.000 optimizer.py:167(zero_grad)
                 807942    8.430    0.000  157.488    0.000 agent.py:59(modify_board)
                3231768  150.688    0.000  150.688    0.000 {built-in method addmm}
                2541150   68.490    0.000  137.235    0.000 layers.py:36(reset)
               40397147   85.659    0.000  135.420    0.000 layers.py:632(check)
              585593428  135.007    0.000  135.007    0.000 level.py:32(inverse)
               40392356   79.719    0.000  130.629    0.000 layers.py:617(check)
                 807942   76.144    0.000  130.106    0.000 collector.py:46(collect)
               40400734   75.992    0.000  123.321    0.000 layers.py:602(check)
               12927072  117.719    0.000  117.719    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               62288781   77.994    0.000  115.684    0.000 layers.py:113(isDone)
             1122172404  113.261    0.000  113.261    0.000 layer.py:91(positions)
              345098148  109.920    0.000  109.920    0.000 layer.py:146(elements)
              530559773  104.187    0.000  104.187    0.000 enum.py:352(<genexpr>)
                2541050   58.239    0.000  103.819    0.000 level.py:16(<dictcomp>)
                 807942  103.729    0.000  103.729    0.000 {built-in method torch._C._nn.one_hot}
              167900445   72.170    0.000  100.948    0.000 layer.py:130(add)
                 807942   68.294    0.000   98.309    0.000 allGraphsTrain.py:43(<listcomp>)
              370037704   81.672    0.000   96.901    0.000 overrides.py:1083(<genexpr>)
               12927072   96.806    0.000   96.806    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                4847652    6.415    0.000   96.416    0.000 activation.py:713(forward)
               12196680   59.582    0.000   95.296    0.000 {built-in method _functools.reduce}
                4847652   11.440    0.000   90.002    0.000 functional.py:1292(leaky_relu)
                 807942   21.853    0.000   83.833    0.000 allGraphs.py:137(transform)
                4847652   77.750    0.000   77.750    0.000 {built-in method torch._C._nn.leaky_relu}
                2423826   72.729    0.000   72.729    0.000 {method 'tolist' of 'torch._C._TensorBase' objects}
                1615884   67.743    0.000   67.743    0.000 {built-in method cat}
                6463536   67.301    0.000   67.301    0.000 {method 'add' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-12>
Subject: Job 9512224: <causal7_online_var_0.5_full_UCB1_0> in cluster <dcc> Done

Job <causal7_online_var_0.5_full_UCB1_0> was submitted from host <n-62-30-2> by user <s183905> in cluster <dcc> at Tue Apr 13 11:09:10 2021
Job was executed on host(s) <n-62-20-12>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Wed Apr 14 08:26:01 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed Apr 14 08:26:01 2021
Terminated at Wed Apr 14 20:21:18 2021
Results reported at Wed Apr 14 20:21:18 2021

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

    CPU time :                                   42797.60 sec.
    Max Memory :                                 2078 MB
    Average Memory :                             2073.22 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14306.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   42918 sec.
    Turnaround time :                            119528 sec.

The output (if any) is above this job summary.

