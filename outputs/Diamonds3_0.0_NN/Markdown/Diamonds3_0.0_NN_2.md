
# Parameters

    Name :                      Diamonds3_0.0_NN-2
    Main :                      graphTrain
    Level :                     Levels.Causal6
    Failed actions chance :     0.0
    Use model :                 True
    Depth :                     3
    Model explore :             100000
    Samples :                   5
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
    Layer super1 :              True
    Layer super2 :              True
    Layer super3 :              True
    Layer super4 :              True
    Layer super5 :              True
    Layer super6 :              True
    Layer super7 :              True
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
    Counterfacts :              1
    Topn :                      6
    Random counterfacts :       False
    Num :                       2
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      15639318899 function calls (14939691971 primitive calls) in 35716.61 seconds

##    Ordered by: cumulative time
   List reduced from 474 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35716.605 35716.605 {built-in method builtins.exec}
                      1    0.001    0.001 35716.605 35716.605 <string>:1(<module>)
                      1   25.689   25.689 35716.604 35716.604 allGraphsTrain.py:13(graphTrain)
                 110610  108.494    0.001 28158.282    0.255 allGraphsTrain.py:40(<listcomp>)
                 705693    3.282    0.000 28044.836    0.040 allGraphs.py:179(getInterventionsmodel)
        59790086/542661 3800.591    0.000 26389.750    0.049 allGraphs.py:186(recursiveBEST)
               57059244 2179.410    0.000 19457.835    0.000 BayesianNN.py:65(predict_no_convert)
               63753439  131.521    0.000 19206.664    0.000 BayesianNN.py:18(forward)
        705175383/65428793 2115.786    0.000 19150.830    0.000 module.py:715(_call_impl)
               63974659  668.895    0.000 18730.162    0.000 container.py:115(forward)
              191702757  335.596    0.000 8524.446    0.000 linear.py:92(forward)
              191702757  602.435    0.000 8044.985    0.000 functional.py:1669(linear)
              191702757 5444.472    0.000 5444.472    0.000 {built-in method addmm}
              191260317  139.636    0.000 4272.817    0.000 dropout.py:57(forward)
              191260317  546.102    0.000 4133.180    0.000 functional.py:960(dropout)
                 110610  953.877    0.009 3745.657    0.034 allGraphs.py:156(transformNot)
              191260317 3446.696    0.000 3446.696    0.000 {built-in method dropout}
              191923977  109.594    0.000 2504.387    0.000 activation.py:713(forward)
                5350671   63.146    0.000 2398.126    0.000 BayesianNN.py:61(predict)
              191923977  174.257    0.000 2394.793    0.000 functional.py:1292(leaky_relu)
                1343524   14.300    0.000 2219.043    0.002 BayesianNN.py:57(learn)
              191923977 2199.786    0.000 2199.786    0.000 {built-in method torch._C._nn.leaky_relu}
                1343524   13.806    0.000 2043.420    0.002 BayesianNN.py:21(learn)
          795530/163032   62.679    0.000 1570.504    0.010 allGraphs.py:202(recursiveExplore)
              134076904 1533.713    0.000 1533.713    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                 110610    2.717    0.000 1483.691    0.013 allGraphsTrain.py:33(<listcomp>)
               11171711  336.093    0.000 1481.040    0.000 allGraphs.py:114(states)
              191702757 1276.829    0.000 1276.829    0.000 {method 't' of 'torch._C._TensorBase' objects}
               71604583  216.554    0.000 1218.559    0.000 tensor.py:21(wrapped)
               59990533  170.213    0.000 1115.147    0.000 tensor.py:506(__rsub__)
              121671500 1097.443    0.000 1097.443    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
               59990533  944.934    0.000  944.934    0.000 {built-in method rsub}
                1454134    7.508    0.000  918.432    0.001 grad_mode.py:23(decorate_context)
                1454134   32.114    0.000  896.063    0.001 adam.py:55(step)
                6694195  658.076    0.000  831.713    0.000 BayesianNN.py:43(convert_data)
                 110610    4.092    0.000  794.435    0.007 allGraphs.py:141(transform)
                1454134  164.012    0.000  735.920    0.001 functional.py:53(adam)
               59879923  726.513    0.000  726.513    0.000 {method 'gt' of 'torch._C._TensorBase' objects}
              287735510  197.335    0.000  633.346    0.000 overrides.py:1070(has_torch_function)
                 110610    0.355    0.000  534.770    0.005 game.py:42(step)
                1454134    9.044    0.000  522.468    0.000 tensor.py:181(backward)
                1454134    4.233    0.000  513.424    0.000 __init__.py:68(backward)
                 110610    0.502    0.000  512.268    0.005 layers.py:827(step)
              493252636  208.280    0.000  488.067    0.000 {built-in method builtins.any}
                1454134  478.831    0.000  478.831    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
              705507213  388.166    0.000  388.166    0.000 {built-in method torch._C._get_tracing_state}
                 110610   19.323    0.000  297.848    0.003 allGraphsTrain.py:44(<listcomp>)
                 110610    7.894    0.000  287.153    0.003 layers.py:17(step)
               11061000   16.943    0.000  278.377    0.000 layer.py:106(move)
              791638168  200.246    0.000  248.897    0.000 overrides.py:1083(<genexpr>)
                 110610    0.337    0.000  229.542    0.002 agent.py:29(learn)
                 110610    2.228    0.000  228.985    0.002 agent.py:117(_learn)
               62622228  137.112    0.000  228.769    0.000 tensor.py:933(grad)
             2884676191  228.103    0.000  228.103    0.000 {method 'values' of 'collections.OrderedDict' objects}
                 110610    6.550    0.000  226.757    0.002 learner.py:42(Qlearn)
              449609104  224.530    0.000  224.530    0.000 module.py:765(__getattr__)
                 110611   14.745    0.000  224.073    0.002 layers.py:793(update)
                1454134   19.332    0.000  199.717    0.000 optimizer.py:167(zero_grad)
               11061000   36.636    0.000  184.946    0.000 layers.py:844(check)
                 110610    7.925    0.000  173.928    0.002 allGraphsTrain.py:51(<listcomp>)
        1728899995/1728899993  168.791    0.000  170.599    0.000 {built-in method builtins.len}
               64195879   39.948    0.000  166.326    0.000 flatten.py:39(forward)
               75256879  160.494    0.000  160.494    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                1755626  149.713    0.000  149.713    0.000 {built-in method tensor}
               17892048  148.096    0.000  148.096    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               13388391  146.178    0.000  146.178    0.000 {built-in method zeros}
                1258744    1.401    0.000  134.139    0.000 game.py:38(board)
               82665683   49.049    0.000  129.804    0.000 {built-in method builtins.all}
               11614050  124.801    0.000  124.801    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               17892048  121.344    0.000  121.344    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              192714451   81.548    0.000  120.529    0.000 _VF.py:25(__getattr__)
               11061000  116.636    0.000  116.636    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
              191702757   99.379    0.000   99.379    0.000 functional.py:1686(<listcomp>)
                 110610   50.574    0.000   96.412    0.001 agent.py:67(modify)
                8946024   90.884    0.000   90.884    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               62631135   88.328    0.000   88.328    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
              480559517   87.694    0.000   87.694    0.000 {built-in method builtins.getattr}
                 705693    5.149    0.000   81.044    0.000 allGraphs.py:167(format)
               90904498   63.563    0.000   80.174    0.000 types.py:171(__get__)
                 221220    0.529    0.000   80.069    0.000 network.py:28(forward)
                8946024   78.145    0.000   78.145    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                 155000    1.371    0.000   76.116    0.000 layers.py:849(restart)
                8946024   69.729    0.000   69.729    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              192808977   68.209    0.000   68.209    0.000 {method 'dim' of 'torch._C._TensorBase' objects}
              270465343   46.444    0.000   68.022    0.000 enum.py:646(__hash__)
                1454134    1.797    0.000   65.461    0.000 loss.py:445(forward)
                 155000    0.648    0.000   64.325    0.000 level.py:8(__init__)
                1454134    6.575    0.000   63.664    0.000 functional.py:2637(mse_loss)
               11061000   17.160    0.000   61.538    0.000 layers.py:838(isFree)
                8946024   61.187    0.000   61.187    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              579249573   60.543    0.000   60.543    0.000 _jit_internal.py:750(is_scripting)
               63974659   38.965    0.000   56.018    0.000 container.py:107(__iter__)
                 155000    1.997    0.000   54.371    0.000 levels.py:303(generate)
                2751212   54.084    0.000   54.084    0.000 {built-in method cat}
              214813749   52.264    0.000   52.264    0.000 tensor.py:24(<genexpr>)
                 930531    8.505    0.000   50.209    0.000 level.py:41(notUsed)
                 110610    1.246    0.000   48.641    0.000 agent.py:112(__call__)
                8946024   47.579    0.000   47.579    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                 884888   25.763    0.000   47.157    0.000 layer.py:175(NoRock_update)
               85278572   34.065    0.000   44.379    0.000 layer.py:103(isFree)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9651551: <Diamonds3_0.0_NN_2> in cluster <dcc> Done

Job <Diamonds3_0.0_NN_2> was submitted from host <n-62-27-18> by user <s183905> in cluster <dcc> at Tue May 18 21:12:59 2021
Job was executed on host(s) <n-62-20-7>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Wed May 19 17:04:03 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 19 17:04:03 2021
Terminated at Thu May 20 02:59:32 2021
Results reported at Thu May 20 02:59:32 2021

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

    CPU time :                                   35663.40 sec.
    Max Memory :                                 2065 MB
    Average Memory :                             2056.37 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14319.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35776 sec.
    Turnaround time :                            107193 sec.

The output (if any) is above this job summary.

