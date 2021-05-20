
# Parameters

    Name :                      Diamonds4_0.0_NN-1
    Main :                      graphTrain
    Level :                     Levels.Causal7
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
    Num :                       1
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      12294320931 function calls (11797946522 primitive calls) in 35708.82 seconds

##    Ordered by: cumulative time
   List reduced from 475 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35708.821 35708.821 {built-in method builtins.exec}
                      1    0.001    0.001 35708.821 35708.821 <string>:1(<module>)
                      1   33.604   33.604 35708.820 35708.820 allGraphsTrain.py:13(graphTrain)
                 133253  167.193    0.001 24918.984    0.187 allGraphsTrain.py:40(<listcomp>)
                 908286    4.022    0.000 24745.762    0.027 allGraphs.py:179(getInterventionsmodel)
        42598435/789073 3521.733    0.000 23552.025    0.030 allGraphs.py:186(recursiveBEST)
        501431519/47206149 1623.608    0.000 17077.461    0.000 module.py:715(_call_impl)
               45156031  100.319    0.000 17010.227    0.000 BayesianNN.py:18(forward)
               39479980 1855.689    0.000 16789.139    0.000 BayesianNN.py:65(predict_no_convert)
               45422537  559.876    0.000 16715.136    0.000 container.py:115(forward)
              136001105  243.814    0.000 7584.817    0.000 linear.py:92(forward)
              136001105  452.002    0.000 7234.397    0.000 functional.py:1669(linear)
                 133253 1452.097    0.011 5549.297    0.042 allGraphs.py:156(transformNot)
              136001105 5051.433    0.000 5051.433    0.000 {built-in method addmm}
              135468093  102.255    0.000 3844.813    0.000 dropout.py:57(forward)
              135468093  413.837    0.000 3742.558    0.000 functional.py:960(dropout)
                1650359   19.332    0.000 3521.700    0.002 BayesianNN.py:57(learn)
                1650359   18.374    0.000 3223.472    0.002 BayesianNN.py:21(learn)
              135468093 3206.866    0.000 3206.866    0.000 {built-in method dropout}
              136267611   82.166    0.000 2467.984    0.000 activation.py:713(forward)
              136267611  139.119    0.000 2385.819    0.000 functional.py:1292(leaky_relu)
                4025692   53.116    0.000 2328.941    0.001 BayesianNN.py:61(predict)
              136267611 2231.844    0.000 2231.844    0.000 {built-in method torch._C._nn.leaky_relu}
                 133253    3.586    0.000 1949.940    0.015 allGraphsTrain.py:33(<listcomp>)
               13458654  506.154    0.000 1946.400    0.000 allGraphs.py:114(states)
              134904823 1858.063    0.000 1858.063    0.000 {method 'item' of 'torch._C._TensorBase' objects}
              119928100 1572.696    0.000 1572.696    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                1783612    9.276    0.000 1530.039    0.001 grad_mode.py:23(decorate_context)
                1783612   41.555    0.000 1503.085    0.001 adam.py:55(step)
                1783612  270.804    0.000 1293.434    0.001 functional.py:53(adam)
                 133253    4.867    0.000 1239.933    0.009 allGraphs.py:141(transform)
               56273442  184.268    0.000 1223.359    0.000 tensor.py:21(wrapped)
              136001105 1191.739    0.000 1191.739    0.000 {method 't' of 'torch._C._TensorBase' objects}
          458475/119213   43.732    0.000 1087.916    0.009 allGraphs.py:202(recursiveExplore)
                5676051  782.129    0.000  980.949    0.000 BayesianNN.py:43(convert_data)
               42281877  132.019    0.000  957.833    0.000 tensor.py:506(__rsub__)
               42281877  825.813    0.000  825.813    0.000 {built-in method rsub}
                1783612    9.920    0.000  802.580    0.000 tensor.py:181(backward)
                1783612    5.366    0.000  792.660    0.000 __init__.py:68(backward)
                1783612  742.706    0.000  742.706    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
               42148624  693.526    0.000  693.526    0.000 {method 'gt' of 'torch._C._TensorBase' objects}
                 133253    0.487    0.000  542.471    0.004 game.py:42(step)
              249235221  162.178    0.000  538.795    0.000 overrides.py:1070(has_torch_function)
                 133253    0.629    0.000  513.007    0.004 layers.py:827(step)
                 133253   35.271    0.000  480.372    0.004 allGraphsTrain.py:44(<listcomp>)
              401940927  174.075    0.000  428.633    0.000 {built-in method builtins.any}
              501831278  382.685    0.000  382.685    0.000 {built-in method torch._C._get_tracing_state}
                 133253    0.419    0.000  354.409    0.003 agent.py:29(learn)
                 133253    2.748    0.000  353.717    0.003 agent.py:117(_learn)
                 133253   10.309    0.000  350.969    0.003 learner.py:42(Qlearn)
               76777306  199.004    0.000  315.189    0.000 tensor.py:933(grad)
                1783612   28.657    0.000  307.457    0.000 optimizer.py:167(zero_grad)
                 133253    8.960    0.000  292.057    0.002 layers.py:17(step)
               13325300   20.271    0.000  282.044    0.000 layer.py:106(move)
                 133253   12.356    0.000  277.528    0.002 allGraphsTrain.py:51(<listcomp>)
               21936356  271.833    0.000  271.833    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               21936356  230.888    0.000  230.888    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              659960069  184.820    0.000  222.003    0.000 overrides.py:1083(<genexpr>)
                 133254   17.206    0.000  219.664    0.002 layers.py:793(update)
               13991565  214.840    0.000  214.840    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               13325300  198.241    0.000  198.241    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               59014343  191.664    0.000  191.664    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                2166367  184.307    0.000  184.307    0.000 {built-in method tensor}
               13325300   37.961    0.000  178.818    0.000 layers.py:844(check)
               11352103  172.570    0.000  172.570    0.000 {built-in method zeros}
             2051148613  170.455    0.000  170.455    0.000 {method 'values' of 'collections.OrderedDict' objects}
              320141701  166.332    0.000  166.332    0.000 module.py:765(__getattr__)
                1574552    1.495    0.000  163.123    0.000 game.py:38(board)
               45689043   27.714    0.000  155.576    0.000 flatten.py:39(forward)
        1277499696/1277499694  146.479    0.000  148.768    0.000 {built-in method builtins.len}
               10968178  147.747    0.000  147.747    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                 133253   77.071    0.001  142.846    0.001 agent.py:67(modify)
               10968178  134.031    0.000  134.031    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               10968178  123.273    0.000  123.273    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                 266506    0.656    0.000  117.031    0.000 network.py:28(forward)
               10968178  111.447    0.000  111.447    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              137251705   56.417    0.000  108.250    0.000 _VF.py:25(__getattr__)
                 908286    6.872    0.000  101.449    0.000 allGraphs.py:167(format)
                1783612    2.127    0.000   95.662    0.000 loss.py:445(forward)
                1783612    8.326    0.000   93.535    0.000 functional.py:2637(mse_loss)
               69598842   35.272    0.000   93.448    0.000 {built-in method builtins.all}
              386605171   89.085    0.000   89.085    0.000 {built-in method builtins.getattr}
               10968178   88.574    0.000   88.574    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               43772178   85.873    0.000   85.873    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                 188024    1.570    0.000   77.469    0.000 layers.py:849(restart)
              136001105   70.638    0.000   70.638    0.000 functional.py:1686(<listcomp>)
                 133253    1.615    0.000   69.218    0.001 agent.py:112(__call__)
              261139093   45.762    0.000   65.982    0.000 enum.py:646(__hash__)
               13325300   17.060    0.000   65.232    0.000 layers.py:838(isFree)
               68086693   49.707    0.000   63.845    0.000 types.py:171(__get__)
                 188024    0.732    0.000   63.755    0.000 level.py:8(__init__)
                1783612   62.655    0.000   62.655    0.000 {built-in method torch._C._nn.mse_loss}
                 188024    2.002    0.000   52.104    0.000 levels.py:456(generate)
              137333755   51.928    0.000   51.928    0.000 {method 'dim' of 'torch._C._TensorBase' objects}
                 932778   28.140    0.000   50.359    0.000 layer.py:175(NoRock_update)
                8404693   48.587    0.000   48.587    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               85685940   37.514    0.000   48.172    0.000 layer.py:103(isFree)
                 902939    8.328    0.000   47.965    0.000 level.py:41(notUsed)
                 533012    0.924    0.000   45.144    0.000 conv.py:422(forward)
                 399759    1.371    0.000   44.143    0.000 tensor.py:576(__iter__)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9651553: <Diamonds4_0.0_NN_1> in cluster <dcc> Done

Job <Diamonds4_0.0_NN_1> was submitted from host <n-62-27-18> by user <s183905> in cluster <dcc> at Tue May 18 21:13:00 2021
Job was executed on host(s) <n-62-20-6>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Wed May 19 17:05:35 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 19 17:05:35 2021
Terminated at Thu May 20 03:00:50 2021
Results reported at Thu May 20 03:00:50 2021

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

    CPU time :                                   35618.63 sec.
    Max Memory :                                 2064 MB
    Average Memory :                             2063.78 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14320.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35716 sec.
    Turnaround time :                            107270 sec.

The output (if any) is above this job summary.

