/zhome/ee/d/137643/Desktop/Bachelor/project-env/lib/python3.8/site-packages/torch/cuda/__init__.py:52: UserWarning: CUDA initialization: Found no NVIDIA driver on your system. Please check that you have an NVIDIA GPU and installed a driver from http://www.nvidia.com/Download/index.aspx (Triggered internally at  /pytorch/c10/cuda/CUDAFunctions.cpp:100.)
  return torch._C._cuda_getDeviceCount() > 0

# Parameters

    Name :                      Diamonds4_0.0_NN_cpu_2-2
    Main :                      graphTrain
    Level :                     Levels.Causal7
    Failed actions chance :     0.0
    Use model :                 True
    Depth :                     1
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


      13534644677 function calls (13318502177 primitive calls) in 35700.30 seconds

##    Ordered by: cumulative time
   List reduced from 442 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35700.295 35700.295 {built-in method builtins.exec}
                      1    0.001    0.001 35700.295 35700.295 <string>:1(<module>)
                      1   63.634   63.634 35700.294 35700.294 allGraphsTrain.py:13(graphTrain)
        229567087/26190017 1264.124    0.000 12547.508    0.000 module.py:715(_call_impl)
               20337707  380.335    0.000 11933.543    0.001 container.py:115(forward)
                5539135   65.582    0.000 10520.138    0.002 BayesianNN.py:57(learn)
                5539135   83.322    0.000 9979.411    0.002 BayesianNN.py:21(learn)
                 313175   63.165    0.000 9944.470    0.032 allGraphsTrain.py:40(<listcomp>)
                4304237   17.929    0.000 9845.186    0.002 allGraphs.py:179(getInterventionsmodel)
                 313175 2071.847    0.007 9455.669    0.030 allGraphs.py:156(transformNot)
               19711357   70.263    0.000 9277.743    0.000 BayesianNN.py:18(forward)
        16594659/4181442  855.965    0.000 8470.808    0.002 allGraphs.py:186(recursiveBEST)
               14172222  192.143    0.000 8035.193    0.001 BayesianNN.py:61(predict)
                 313175    1.328    0.000 4564.093    0.015 agent.py:29(learn)
                 313175   19.576    0.000 4562.015    0.015 agent.py:117(_learn)
                 313175   22.882    0.000 4542.439    0.015 learner.py:42(Qlearn)
                 313175   20.281    0.000 4496.823    0.014 allGraphs.py:141(transform)
                5852310   40.862    0.000 4482.050    0.001 grad_mode.py:23(decorate_context)
                5852310  186.080    0.000 4365.789    0.001 adam.py:55(step)
                5852310   38.324    0.000 4071.372    0.001 tensor.py:181(backward)
                5852310   22.978    0.000 4033.047    0.001 __init__.py:68(backward)
                5852310 3901.474    0.001 3901.474    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                5852310  876.525    0.000 3404.627    0.001 functional.py:53(adam)
               60386771  196.399    0.000 3217.828    0.000 linear.py:92(forward)
               59134071   78.899    0.000 3175.588    0.000 dropout.py:57(forward)
               59134071  304.978    0.000 3096.689    0.000 functional.py:960(dropout)
               60386771  331.392    0.000 2940.095    0.000 functional.py:1669(linear)
                 626350    2.173    0.000 2935.144    0.005 network.py:28(forward)
               59134071 2724.559    0.000 2724.559    0.000 {built-in method dropout}
                1252700    3.862    0.000 2495.939    0.002 conv.py:422(forward)
                1252700    3.678    0.000 2490.658    0.002 conv.py:414(_conv_forward)
                1252700 2486.342    0.002 2486.342    0.002 {built-in method conv2d}
                 313175   46.164    0.000 2134.050    0.007 allGraphsTrain.py:33(<listcomp>)
               31630776 1020.031    0.000 2087.894    0.000 allGraphs.py:114(states)
                 313175    1.379    0.000 2058.065    0.007 game.py:42(step)
                 313175    2.199    0.000 2029.212    0.006 layers.py:827(step)
              281857900 1748.655    0.000 1748.655    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
               19711357 1210.379    0.000 1655.105    0.000 BayesianNN.py:43(convert_data)
               60386771 1560.718    0.000 1560.718    0.000 {built-in method addmm}
                 313175    4.386    0.000 1505.948    0.005 agent.py:112(__call__)
              250181530  853.513    0.000 1399.666    0.000 tensor.py:933(grad)
          474596/122795   33.624    0.000 1094.009    0.009 allGraphs.py:202(recursiveExplore)
                 313175   34.481    0.000 1073.144    0.003 layers.py:17(step)
                5852310  124.433    0.000 1056.202    0.000 optimizer.py:167(zero_grad)
               61013121   68.265    0.000 1052.042    0.000 activation.py:713(forward)
               31317500   74.906    0.000 1034.822    0.000 layer.py:106(move)
               61013121  110.531    0.000  983.777    0.000 functional.py:1292(leaky_relu)
                 313176   61.227    0.000  951.466    0.003 layers.py:793(update)
              383809408  301.875    0.000  921.596    0.000 overrides.py:1070(has_torch_function)
               61013121  861.088    0.000  861.088    0.000 {built-in method torch._C._nn.leaky_relu}
               71480420  833.234    0.000  833.234    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               45961568  177.808    0.000  781.939    0.000 tensor.py:21(wrapped)
              486539383  282.366    0.000  753.015    0.000 {built-in method builtins.any}
               60386771  681.190    0.000  681.190    0.000 {method 't' of 'torch._C._TensorBase' objects}
               31317500  139.152    0.000  649.837    0.000 layers.py:844(check)
              318717039  624.485    0.000  624.485    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               71480420  535.782    0.000  535.782    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                 313175   35.891    0.000  474.077    0.002 allGraphsTrain.py:51(<listcomp>)
                 313175   59.698    0.000  454.065    0.001 allGraphsTrain.py:44(<listcomp>)
                 679016    8.746    0.000  414.558    0.001 layers.py:849(restart)
                5852310   11.016    0.000  382.957    0.000 loss.py:445(forward)
                5852310   40.469    0.000  371.940    0.000 functional.py:2637(mse_loss)
              865506374  288.305    0.000  350.282    0.000 overrides.py:1083(<genexpr>)
               39422715  338.891    0.000  338.891    0.000 {built-in method zeros}
                 679016    4.118    0.000  337.769    0.000 level.py:8(__init__)
               35740210  334.301    0.000  334.301    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               35740210  318.312    0.000  318.312    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               13078193   66.189    0.000  314.600    0.000 tensor.py:506(__rsub__)
                7218148  313.277    0.000  313.277    0.000 {built-in method tensor}
                 679016   11.848    0.000  296.474    0.000 levels.py:456(generate)
                5870113    7.634    0.000  283.963    0.000 game.py:38(board)
                3260377   47.291    0.000  272.898    0.000 level.py:41(notUsed)
               35740210  268.858    0.000  268.858    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               32883375  263.327    0.000  263.327    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
              230506612  261.799    0.000  261.799    0.000 {built-in method torch._C._get_tracing_state}
                4304237   47.977    0.000  260.861    0.000 allGraphs.py:167(format)
               13078193  248.411    0.000  248.411    0.000 {built-in method rsub}
              661657277  170.619    0.000  246.417    0.000 enum.py:646(__hash__)
               31317500   66.659    0.000  244.571    0.000 layers.py:838(isFree)
                 313175   96.285    0.000  234.265    0.001 agent.py:67(modify)
                5852310  226.571    0.000  226.571    0.000 {built-in method torch._C._nn.mse_loss}
               35740210  223.967    0.000  223.967    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               31317500  211.774    0.000  211.774    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                2192232  116.123    0.000  202.727    0.000 layer.py:175(NoRock_update)
               52281557  186.066    0.000  186.066    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              214552746  139.124    0.000  177.912    0.000 layer.py:103(isFree)
               26893619  175.451    0.000  175.451    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               77279168   45.821    0.000  166.555    0.000 {built-in method builtins.all}
               12765018  160.769    0.000  160.769    0.000 {method 'gt' of 'torch._C._TensorBase' objects}
                 939525    4.621    0.000  150.913    0.000 tensor.py:576(__iter__)
                 939525  143.480    0.000  143.480    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               35740320   60.670    0.000  136.772    0.000 tensor.py:596(__hash__)
        868968032/868968030  127.936    0.000  135.525    0.000 {built-in method builtins.len}
                3260377    3.579    0.000  133.331    0.000 level.py:38(elementsIn)
              938606055  129.383    0.000  129.383    0.000 {method 'values' of 'collections.OrderedDict' objects}
              149156751  129.167    0.000  129.168    0.000 module.py:765(__getattr__)
               31317500   78.136    0.000  124.090    0.000 layers.py:617(check)
               31317500   77.601    0.000  124.029    0.000 layers.py:632(check)
               31317500   77.285    0.000  123.948    0.000 layers.py:602(check)
              245108672   95.785    0.000  115.209    0.000 layers.py:809(<genexpr>)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9668412: <Diamonds4_0.0_NN_cpu_2_2> in cluster <dcc> Done

Job <Diamonds4_0.0_NN_cpu_2_2> was submitted from host <n-62-30-8> by user <s183905> in cluster <dcc> at Wed May 19 22:59:03 2021
Job was executed on host(s) <n-62-21-97>, in queue <hpc>, as user <s183905> in cluster <dcc> at Wed May 19 22:59:05 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 19 22:59:05 2021
Terminated at Thu May 20 08:54:10 2021
Results reported at Thu May 20 08:54:10 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -n 1
#BSUB -R "rusage[mem=16G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 4320
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $MYARGS
------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   35700.77 sec.
    Max Memory :                                 109 MB
    Average Memory :                             103.45 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               16275.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   35709 sec.
    Turnaround time :                            35707 sec.

The output (if any) is above this job summary.

