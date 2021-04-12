
# Parameters

    Name :                      causal2_online_var_0.5_test-0
    Main :                      graphTrain
    Level :                     Levels.Causal2
    Failed actions chance :     0.5
    Hours :                     5.0
    Batch :                     100
    Width :                     9
    Height :                    9
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
    Cf convert :                2
    Counterfacts :              1
    Topn :                      7
    Minutes used :              295 minutes.
    Hours used :                4 hours.

# Profiling


      10773601243 function calls (10389322046 primitive calls) in 17711.07 seconds

##    Ordered by: cumulative time
   List reduced from 462 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 17711.074 17711.074 {built-in method builtins.exec}
                      1    0.001    0.001 17711.074 17711.074 <string>:1(<module>)
                      1   86.424   86.424 17711.073 17711.073 allGraphsTrain.py:10(graphTrain)
                 388347 2719.066    0.007 6591.264    0.017 allGraphs.py:120(transformNot)
              388350504 4350.273    0.000 4350.273    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                 388347    8.835    0.000 4139.212    0.011 allGraphsTrain.py:29(<listcomp>)
               39223148  945.242    0.000 4130.417    0.000 allGraphs.py:88(states)
              349512700 3059.499    0.000 3059.499    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 388347    1.205    0.000 1793.460    0.005 game.py:41(step)
                 388347  350.693    0.001 1766.679    0.005 allGraphsTrain.py:35(<listcomp>)
                 388347    1.677    0.000 1716.489    0.004 layers.py:712(step)
                7278403   34.355    0.000 1415.986    0.000 allGraphs.py:127(getInterventions)
                 388348   50.697    0.000 1077.891    0.003 layers.py:678(update)
                 388347   65.392    0.000 1017.571    0.003 allGraphsTrain.py:37(<listcomp>)
               10883553  871.744    0.000  871.744    0.000 {built-in method tensor}
                9220139    4.819    0.000  821.569    0.000 game.py:37(board)
                 388347    1.250    0.000  784.516    0.002 agent.py:29(learn)
                 388347    7.585    0.000  782.495    0.002 agent.py:117(_learn)
                 388347   22.915    0.000  774.911    0.002 learner.py:42(Qlearn)
                6275902    4.845    0.000  729.350    0.000 allGraphs.py:107(rightIntervention)
        81028648/6275902   47.648    0.000  701.288    0.000 {built-in method builtins.min}
               18977608    7.596    0.000  691.573    0.000 allGraphs.py:108(<lambda>)
        155781394/18977608  212.004    0.000  683.977    0.000 allGraphs.py:52(expected_moves)
                 388347   27.416    0.000  634.898    0.002 layers.py:17(step)
               41164782   89.393    0.000  625.774    0.000 tensor.py:21(wrapped)
               38834700   56.687    0.000  603.852    0.000 layer.py:98(move)
                 388347   27.876    0.000  594.555    0.002 allGraphsTrain.py:44(<listcomp>)
        211556532/46601190   56.999    0.000  580.874    0.000 allGraphs.py:56(<genexpr>)
                1576084   11.065    0.000  561.081    0.000 layers.py:734(restart)
                1576084    5.274    0.000  449.792    0.000 level.py:8(__init__)
               40776435  426.073    0.000  426.073    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                1576084   16.554    0.000  395.561    0.000 levels.py:151(generate)
               38834700  395.366    0.000  395.366    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                7565420   66.068    0.000  361.464    0.000 level.py:41(notUsed)
             1570403472  249.122    0.000  361.267    0.000 enum.py:646(__hash__)
                 388347  197.824    0.001  356.163    0.001 agent.py:67(modify)
        8931981/1165041   32.721    0.000  308.336    0.000 module.py:715(_call_impl)
                 388347    2.209    0.000  307.961    0.001 grad_mode.py:23(decorate_context)
                 388347   10.446    0.000  301.654    0.001 adam.py:55(step)
               38834700   77.497    0.000  285.988    0.000 layers.py:729(check)
                 776694    1.978    0.000  281.365    0.000 network.py:24(forward)
                 776694    7.351    0.000  274.881    0.000 container.py:115(forward)
                 388347   54.662    0.000  246.653    0.001 functional.py:53(adam)
               82031149   45.938    0.000  218.395    0.000 allGraphs.py:61(layers_not_in)
               38834700   51.418    0.000  205.921    0.000 layers.py:723(isFree)
              107161311   55.828    0.000  192.449    0.000 {built-in method builtins.any}
               79999582   33.211    0.000  180.783    0.000 {built-in method builtins.all}
                 388347    2.033    0.000  179.953    0.000 tensor.py:181(backward)
                 388347    1.206    0.000  177.920    0.000 __init__.py:68(backward)
                2718436  101.939    0.000  174.368    0.000 layer.py:167(NoRock_update)
               82031149   85.003    0.000  172.458    0.000 allGraphs.py:62(<listcomp>)
                7565420    5.115    0.000  169.928    0.000 level.py:38(elementsIn)
                 388347  168.657    0.000  168.657    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                 388347    4.356    0.000  164.860    0.000 agent.py:112(__call__)
              253343436  123.437    0.000  154.503    0.000 layer.py:95(isFree)
              236522113   61.652    0.000  137.710    0.000 layers.py:684(<genexpr>)
                1165041    4.161    0.000  126.571    0.000 tensor.py:576(__iter__)
               40388088  125.577    0.000  125.577    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                1165041  119.677    0.000  119.677    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
             1570404781  112.145    0.000  112.145    0.000 {built-in method builtins.hash}
                1553388    2.631    0.000  110.383    0.000 conv.py:422(forward)
                7565420   53.023    0.000  108.483    0.000 level.py:39(<listcomp>)
              155781394   72.241    0.000  106.794    0.000 allGraphs.py:37(p)
               67572512   32.989    0.000  106.768    0.000 overrides.py:1070(has_torch_function)
                1553388    2.977    0.000  106.742    0.000 conv.py:414(_conv_forward)
                1553388  103.232    0.000  103.232    0.000 {built-in method conv2d}
               11032588    7.718    0.000   96.604    0.000 layer.py:69(restart)
              298069728   76.619    0.000   94.719    0.000 layers.py:694(<genexpr>)
                1553388    3.367    0.000   81.099    0.000 linear.py:92(forward)
               21747486   47.856    0.000   79.679    0.000 tensor.py:933(grad)
                1576184   37.994    0.000   76.865    0.000 layers.py:30(reset)
                1553388    6.005    0.000   76.163    0.000 functional.py:1669(linear)
              363234122   74.419    0.000   74.419    0.000 level.py:32(inverse)
                 388347    6.394    0.000   68.183    0.000 optimizer.py:167(zero_grad)
               38834800   41.749    0.000   64.812    0.000 layers.py:107(isDone)
                 388347    2.654    0.000   56.663    0.000 agent.py:59(modify_board)
                7565420   34.852    0.000   56.330    0.000 {built-in method _functools.reduce}
              329095634   55.606    0.000   55.606    0.000 enum.py:352(<genexpr>)
                 388347   31.763    0.000   54.131    0.000 collector.py:46(collect)
               19411774   32.787    0.000   54.096    0.000 layers.py:213(check)
                1553388   53.696    0.000   53.696    0.000 {built-in method addmm}
               19419888   32.129    0.000   52.768    0.000 layers.py:225(check)
               19415829   31.576    0.000   52.184    0.000 layers.py:201(check)
                6213552   49.970    0.000   49.970    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              483910561   47.597    0.000   47.597    0.000 layer.py:91(positions)
               93754764   34.558    0.000   47.246    0.000 layer.py:130(add)
                1576084   22.522    0.000   45.561    0.000 level.py:16(<dictcomp>)
              191382044   44.337    0.000   44.337    0.000 layer.py:146(elements)
                 388347   28.310    0.000   41.725    0.000 allGraphsTrain.py:43(<listcomp>)
              177863194   34.989    0.000   41.653    0.000 overrides.py:1083(<genexpr>)
                6213552   41.497    0.000   41.497    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                 388347   37.346    0.000   37.346    0.000 {built-in method torch._C._nn.one_hot}
                2330082    1.983    0.000   35.973    0.000 activation.py:713(forward)
              157948936   30.121    0.000   34.626    0.000 {built-in method builtins.max}
                2330082    3.139    0.000   33.990    0.000 functional.py:1292(leaky_relu)
                2330082   30.540    0.000   30.540    0.000 {built-in method torch._C._nn.leaky_relu}
                 388347    7.867    0.000   29.197    0.000 allGraphs.py:111(transform)
                3106776   28.599    0.000   28.599    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              331297794   26.596    0.000   26.596    0.000 {method 'append' of 'list' objects}
                3106776   26.501    0.000   26.501    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-3>
Subject: Job 9511305: <causal2_online_var_0.5_test_0> in cluster <dcc> Done

Job <causal2_online_var_0.5_test_0> was submitted from host <n-62-27-21> by user <s183905> in cluster <dcc> at Mon Apr 12 16:10:30 2021
Job was executed on host(s) <n-62-20-3>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Mon Apr 12 16:12:39 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Apr 12 16:12:39 2021
Terminated at Mon Apr 12 21:07:58 2021
Results reported at Mon Apr 12 21:07:58 2021

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

    CPU time :                                   17662.38 sec.
    Max Memory :                                 2084 MB
    Average Memory :                             2074.59 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14300.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   17720 sec.
    Turnaround time :                            17848 sec.

The output (if any) is above this job summary.

