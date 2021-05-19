
# Parameters

    Name :                      Diamonds1_0.0_NN-0
    Main :                      graphTrain
    Level :                     Levels.Causal2
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
    Num :                       0
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      14814640219 function calls (14171771245 primitive calls) in 35713.63 seconds

##    Ordered by: cumulative time
   List reduced from 472 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35713.631 35713.631 {built-in method builtins.exec}
                      1    0.001    0.001 35713.631 35713.631 <string>:1(<module>)
                      1   36.865   36.865 35713.630 35713.630 allGraphsTrain.py:13(graphTrain)
                 124635  145.432    0.001 27168.864    0.218 allGraphsTrain.py:40(<listcomp>)
                1015675    4.865    0.000 27016.322    0.027 allGraphs.py:179(getInterventionsmodel)
        55298941/851362 3678.195    0.000 25608.617    0.030 allGraphs.py:186(recursiveBEST)
               58543757  132.228    0.000 18633.129    0.000 BayesianNN.py:18(forward)
        648490560/60560290 2096.016    0.000 18622.084    0.000 module.py:715(_call_impl)
               51699234 2067.288    0.000 18587.846    0.000 BayesianNN.py:65(predict_no_convert)
               58793027  629.198    0.000 18201.432    0.000 container.py:115(forward)
              176129811  320.071    0.000 8229.570    0.000 linear.py:92(forward)
              176129811  585.558    0.000 7768.880    0.000 functional.py:1669(linear)
              176129811 5276.377    0.000 5276.377    0.000 {built-in method addmm}
              175631271  138.927    0.000 4135.753    0.000 dropout.py:57(forward)
                 124635  965.022    0.008 4091.372    0.033 allGraphs.py:156(transformNot)
              175631271  521.307    0.000 3996.826    0.000 functional.py:960(dropout)
              175631271 3342.696    0.000 3342.696    0.000 {built-in method dropout}
                1642628   17.835    0.000 2809.497    0.002 BayesianNN.py:57(learn)
                1642628   17.055    0.000 2591.149    0.002 BayesianNN.py:21(learn)
              176379081  104.259    0.000 2449.421    0.000 activation.py:713(forward)
                5201895   65.722    0.000 2438.190    0.000 BayesianNN.py:61(predict)
              176379081  178.139    0.000 2345.162    0.000 functional.py:1292(leaky_relu)
              176379081 2146.996    0.000 2146.996    0.000 {built-in method torch._C._nn.leaky_relu}
              126279020 1692.190    0.000 1692.190    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                 124635    2.998    0.000 1483.701    0.012 allGraphsTrain.py:33(<listcomp>)
               12588236  330.951    0.000 1480.759    0.000 allGraphs.py:114(states)
          655023/164313   52.755    0.000 1288.603    0.008 allGraphs.py:202(recursiveExplore)
               68149599  211.905    0.000 1229.232    0.000 tensor.py:21(wrapped)
              176129811 1209.755    0.000 1209.755    0.000 {method 't' of 'torch._C._TensorBase' objects}
                1767263    9.398    0.000 1161.971    0.001 grad_mode.py:23(decorate_context)
                1767263   42.218    0.000 1134.308    0.001 adam.py:55(step)
                 124635    5.726    0.000 1127.959    0.009 allGraphs.py:141(transform)
              112171900 1060.044    0.000 1060.044    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
               55062924  161.006    0.000 1053.031    0.000 tensor.py:506(__rsub__)
                1767263  206.344    0.000  923.674    0.001 functional.py:53(adam)
               55062924  892.025    0.000  892.025    0.000 {built-in method rsub}
                6844523  662.624    0.000  849.403    0.000 BayesianNN.py:43(convert_data)
               54938289  705.684    0.000  705.684    0.000 {method 'gt' of 'torch._C._TensorBase' objects}
              290168322  196.723    0.000  655.470    0.000 overrides.py:1070(has_torch_function)
                1767263    9.689    0.000  637.705    0.000 tensor.py:181(backward)
                1767263    5.465    0.000  628.016    0.000 __init__.py:68(backward)
                 124635    0.557    0.000  605.237    0.005 game.py:42(step)
                1767263  583.795    0.000  583.795    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                 124635    0.797    0.000  579.073    0.005 layers.py:827(step)
              482057612  219.518    0.000  510.552    0.000 {built-in method builtins.any}
              648864465  383.884    0.000  383.884    0.000 {built-in method torch._C._get_tracing_state}
                 124635   23.911    0.000  372.106    0.003 allGraphsTrain.py:44(<listcomp>)
                 124635   11.046    0.000  322.575    0.003 layers.py:17(step)
               12463500   21.623    0.000  310.349    0.000 layer.py:106(move)
               75969996  180.735    0.000  301.588    0.000 tensor.py:933(grad)
                 124635    0.566    0.000  283.552    0.002 agent.py:29(learn)
                 124635    2.829    0.000  282.672    0.002 agent.py:117(_learn)
                 124635    8.373    0.000  279.843    0.002 learner.py:42(Qlearn)
                1767263   25.580    0.000  262.053    0.000 optimizer.py:167(zero_grad)
              783682012  215.540    0.000  258.253    0.000 overrides.py:1083(<genexpr>)
                 124636   18.461    0.000  254.798    0.002 layers.py:793(update)
              413692906  221.189    0.000  221.189    0.000 module.py:765(__getattr__)
             2652755267  221.080    0.000  221.080    0.000 {method 'values' of 'collections.OrderedDict' objects}
                 124635    9.746    0.000  208.174    0.002 allGraphsTrain.py:51(<listcomp>)
                2194435  188.075    0.000  188.075    0.000 {built-in method tensor}
               12463500   38.768    0.000  187.729    0.000 layers.py:844(check)
               21705696  186.917    0.000  186.917    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
        1604865564/1604865562  172.265    0.000  174.375    0.000 {built-in method builtins.len}
               71505797  174.113    0.000  174.113    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                1638851    1.652    0.000  169.032    0.000 game.py:38(board)
               59042297   33.907    0.000  166.731    0.000 flatten.py:39(forward)
               13689047  157.990    0.000  157.990    0.000 {built-in method zeros}
               21705696  153.780    0.000  153.780    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               13086675  148.212    0.000  148.212    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               12463500  138.922    0.000  138.922    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                 124635   64.483    0.001  123.471    0.001 agent.py:67(modify)
              177398534   82.095    0.000  113.899    0.000 _VF.py:25(__getattr__)
                1015675    7.970    0.000  113.860    0.000 allGraphs.py:167(format)
               80613199   47.377    0.000  111.365    0.000 {built-in method builtins.all}
               10852848  108.323    0.000  108.323    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                 238648    2.289    0.000  107.603    0.000 layers.py:849(restart)
                 249270    0.792    0.000  102.857    0.000 network.py:28(forward)
               10852848   99.516    0.000   99.516    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              176129811   96.984    0.000   96.984    0.000 functional.py:1686(<listcomp>)
                 238648    1.094    0.000   88.204    0.000 level.py:8(__init__)
               10852848   87.834    0.000   87.834    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               57150399   86.240    0.000   86.240    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                1767263    2.436    0.000   84.801    0.000 loss.py:445(forward)
               83863362   65.641    0.000   82.801    0.000 types.py:171(__get__)
                1767263    8.453    0.000   82.365    0.000 functional.py:2637(mse_loss)
               12463500   19.494    0.000   81.218    0.000 layers.py:838(isFree)
               10852848   78.013    0.000   78.013    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              467681567   74.583    0.000   74.583    0.000 {built-in method builtins.getattr}
                 238648    2.869    0.000   72.568    0.000 levels.py:151(generate)
              250172108   47.066    0.000   68.226    0.000 enum.py:646(__hash__)
              177376281   68.073    0.000   68.073    0.000 {method 'dim' of 'torch._C._TensorBase' objects}
                1145966   11.697    0.000   66.700    0.000 level.py:41(notUsed)
                 124635    2.004    0.000   65.764    0.001 agent.py:112(__call__)
               80586140   51.739    0.000   61.724    0.000 layer.py:103(isFree)
               10852848   60.737    0.000   60.737    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              533442072   59.081    0.000   59.081    0.000 _jit_internal.py:750(is_scripting)
                 872452   32.647    0.000   57.909    0.000 layer.py:175(NoRock_update)
              204448797   55.228    0.000   55.228    0.000 tensor.py:24(<genexpr>)
               58793027   36.857    0.000   52.873    0.000 container.py:107(__iter__)
                1767263   51.661    0.000   51.661    0.000 {built-in method torch._C._nn.mse_loss}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9651543: <Diamonds1_0.0_NN_0> in cluster <dcc> Done

Job <Diamonds1_0.0_NN_0> was submitted from host <n-62-27-18> by user <s183905> in cluster <dcc> at Tue May 18 21:12:58 2021
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Tue May 18 21:12:59 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue May 18 21:12:59 2021
Terminated at Wed May 19 07:08:33 2021
Results reported at Wed May 19 07:08:33 2021

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

    CPU time :                                   35622.23 sec.
    Max Memory :                                 2064 MB
    Average Memory :                             2056.36 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14320.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35760 sec.
    Turnaround time :                            35735 sec.

The output (if any) is above this job summary.

