
# Parameters

    Name :                      Diamonds1_0.5_NN-0
    Main :                      graphTrain
    Level :                     Levels.Causal2
    Failed actions chance :     0.5
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


      14376919520 function calls (13656613119 primitive calls) in 35722.83 seconds

##    Ordered by: cumulative time
   List reduced from 482 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35722.825 35722.825 {built-in method builtins.exec}
                      1    0.001    0.001 35722.825 35722.825 <string>:1(<module>)
                      1   47.139   47.139 35722.824 35722.824 allGraphsTrain.py:13(graphTrain)
                 130163  159.844    0.001 26913.865    0.207 allGraphsTrain.py:40(<listcomp>)
                1189515    6.917    0.000 26744.449    0.022 allGraphs.py:179(getInterventionsmodel)
        61630294/990058 4467.873    0.000 25232.321    0.025 allGraphs.py:186(recursiveBEST)
               65647382  156.475    0.000 18548.321    0.000 BayesianNN.py:18(forward)
        727178747/68101667 2543.697    0.000 18517.487    0.000 module.py:866(_call_impl)
               57500850 2157.952    0.000 18485.459    0.000 BayesianNN.py:65(predict_no_convert)
               65907708  825.582    0.000 17988.647    0.000 container.py:117(forward)
              197462798  351.273    0.000 7148.092    0.000 linear.py:93(forward)
              197462798  147.844    0.000 6636.448    0.000 functional.py:1737(linear)
              197462798 6453.074    0.000 6453.074    0.000 {built-in method torch._C._nn.linear}
                 130163  965.329    0.007 4921.978    0.038 allGraphs.py:156(transformNot)
              196942146  142.631    0.000 4121.426    0.000 dropout.py:57(forward)
              196942146  510.316    0.000 3978.795    0.000 functional.py:1059(dropout)
              196942146 3316.386    0.000 3316.386    0.000 {built-in method dropout}
                2063796   28.606    0.000 3096.803    0.002 BayesianNN.py:57(learn)
                2063796   23.764    0.000 2851.343    0.001 BayesianNN.py:21(learn)
              197723124  131.618    0.000 2596.287    0.000 activation.py:713(forward)
                6082736   87.640    0.000 2538.325    0.000 BayesianNN.py:61(predict)
              197723124  141.774    0.000 2464.670    0.000 functional.py:1364(leaky_relu)
              197723124 2298.425    0.000 2298.425    0.000 {built-in method torch._C._nn.leaky_relu}
              132228236 1791.825    0.000 1791.825    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                 130163   10.077    0.000 1514.208    0.012 allGraphsTrain.py:33(<listcomp>)
               13146564  320.662    0.000 1504.180    0.000 allGraphs.py:114(states)
          788127/199457   68.360    0.000 1356.326    0.007 allGraphs.py:202(recursiveExplore)
                2193959   18.371    0.000 1216.823    0.001 optimizer.py:84(wrapper)
                2193959    9.175    0.000 1132.959    0.001 grad_mode.py:24(decorate_context)
                2193959   48.807    0.000 1102.824    0.001 adam.py:55(step)
              117147100 1063.940    0.000 1063.940    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                2193959  228.715    0.000 1002.671    0.000 _functional.py:53(adam)
               61359069   55.146    0.000  943.183    0.000 tensor.py:525(__rsub__)
                8146532  671.620    0.000  878.685    0.000 BayesianNN.py:43(convert_data)
               61359069  877.513    0.000  877.513    0.000 {built-in method rsub}
                2193959    8.188    0.000  754.930    0.000 tensor.py:195(backward)
                2193959    8.608    0.000  746.457    0.000 __init__.py:68(backward)
                2193959  695.510    0.000  695.510    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                 130163    5.544    0.000  640.889    0.005 allGraphs.py:141(transform)
                 130163    0.714    0.000  561.715    0.004 game.py:42(step)
                 130163    0.947    0.000  531.825    0.004 layers.py:827(step)
                 130163   26.247    0.000  374.037    0.003 allGraphsTrain.py:44(<listcomp>)
              727569236  359.879    0.000  359.879    0.000 {built-in method torch._C._get_tracing_state}
        3233958280/3233958278  318.797    0.000  320.098    0.000 {built-in method builtins.len}
                 130163    0.640    0.000  272.427    0.002 agent.py:29(learn)
                 130163    3.944    0.000  271.448    0.002 agent.py:117(_learn)
                 130164   21.017    0.000  268.235    0.002 layers.py:793(update)
                 130163    9.330    0.000  267.504    0.002 learner.py:42(Qlearn)
              463938975  265.850    0.000  265.851    0.000 module.py:934(__getattr__)
                 130163   12.067    0.000  261.414    0.002 layers.py:17(step)
             2974622696  256.199    0.000  256.199    0.000 {method 'values' of 'collections.OrderedDict' objects}
               13016300   22.220    0.000  248.053    0.000 layer.py:106(move)
                2419209  228.952    0.000  228.952    0.000 {built-in method tensor}
                1840331    1.985    0.000  207.273    0.000 game.py:38(board)
               20680983  197.189    0.000  197.189    0.000 {built-in method zeros}
               26848160  196.803    0.000  196.803    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                2193959   34.338    0.000  188.650    0.000 optimizer.py:189(zero_grad)
               66168034   40.616    0.000  182.601    0.000 flatten.py:39(forward)
               79184334  180.377    0.000  180.377    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               26848160  174.477    0.000  174.477    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                1189515   11.353    0.000  148.201    0.000 allGraphs.py:167(format)
               13016300  136.795    0.000  136.795    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
              199136105   86.063    0.000  124.047    0.000 _VF.py:25(__getattr__)
               96142642   94.523    0.000  118.887    0.000 types.py:171(__get__)
               13016300   29.818    0.000  116.306    0.000 layers.py:844(check)
               13424080  115.765    0.000  115.765    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               63843912  115.697    0.000  115.697    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                 130163  113.562    0.001  113.562    0.001 allGraphsTrain.py:51(<listcomp>)
                 130163   72.460    0.001  111.553    0.001 agent.py:67(modify)
                 260326    0.848    0.000  106.050    0.000 network.py:28(forward)
                2193959    3.482    0.000  105.014    0.000 loss.py:527(forward)
                2193959    8.642    0.000  101.533    0.000 functional.py:2898(mse_loss)
                 171754    1.964    0.000   97.691    0.001 layers.py:849(restart)
               13424080   97.198    0.000   97.198    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               13424080   93.732    0.000   93.732    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               13424080   92.160    0.000   92.160    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               13016300   19.371    0.000   88.024    0.000 layers.py:838(isFree)
                 171754    1.074    0.000   82.436    0.000 level.py:8(__init__)
               93968620   64.400    0.000   80.456    0.000 tensor.py:906(grad)
               13424080   70.189    0.000   70.189    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                2193959   69.334    0.000   69.334    0.000 {built-in method torch._C._nn.mse_loss}
                 130163    2.784    0.000   69.014    0.001 agent.py:112(__call__)
               89094727   57.244    0.000   68.654    0.000 layer.py:103(isFree)
              505553922   63.012    0.000   63.012    0.000 {built-in method torch._C._has_torch_function_unary}
                 911148   34.594    0.000   61.528    0.000 layer.py:175(NoRock_update)
               65907708   42.668    0.000   60.949    0.000 container.py:109(__iter__)
                 390489    1.117    0.000   58.719    0.000 tensor.py:575(__iter__)
                 390489   56.710    0.000   56.710    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
                 171754    2.270    0.000   54.946    0.000 levels.py:151(generate)
              175539264   37.090    0.000   54.004    0.000 enum.py:646(__hash__)
                2615006   52.031    0.000   52.031    0.000 {built-in method cat}
                 824492    8.888    0.000   50.238    0.000 level.py:41(notUsed)
              261015826   46.478    0.000   46.478    0.000 {built-in method torch._C._has_torch_function_variadic}
               12844647   11.043    0.000   45.339    0.000 {built-in method builtins.any}
                 520652    1.447    0.000   43.835    0.000 conv.py:398(forward)
                 520652    1.116    0.000   41.707    0.000 conv.py:390(_conv_forward)
                4387918    9.696    0.000   41.544    0.000 profiler.py:615(__enter__)
               11778157   41.260    0.000   41.260    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                 520652   40.591    0.000   40.591    0.000 {built-in method conv2d}
                2193959    8.981    0.000   40.124    0.000 __init__.py:28(_make_grads)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9651522: <Diamonds1_0.5_NN_0> in cluster <dcc> Done

Job <Diamonds1_0.5_NN_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Tue May 18 21:04:57 2021
Job was executed on host(s) <n-62-20-12>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Tue May 18 21:04:59 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue May 18 21:04:59 2021
Terminated at Wed May 19 07:00:29 2021
Results reported at Wed May 19 07:00:29 2021

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

    CPU time :                                   35615.64 sec.
    Max Memory :                                 3629 MB
    Average Memory :                             3145.68 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               12755.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35837 sec.
    Turnaround time :                            35732 sec.

The output (if any) is above this job summary.

