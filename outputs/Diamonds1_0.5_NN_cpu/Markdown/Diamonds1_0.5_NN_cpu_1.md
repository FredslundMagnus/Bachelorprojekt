/zhome/ee/d/137643/Desktop/Bachelor/project-env/lib/python3.8/site-packages/torch/cuda/__init__.py:52: UserWarning: CUDA initialization: Found no NVIDIA driver on your system. Please check that you have an NVIDIA GPU and installed a driver from http://www.nvidia.com/Download/index.aspx (Triggered internally at  /pytorch/c10/cuda/CUDAFunctions.cpp:100.)
  return torch._C._cuda_getDeviceCount() > 0

# Parameters

    Name :                      Diamonds1_0.5_NN_cpu-1
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
    Num :                       1
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      12145642810 function calls (11628077431 primitive calls) in 35700.46 seconds

##    Ordered by: cumulative time
   List reduced from 441 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35700.455 35700.455 {built-in method builtins.exec}
                      1    0.002    0.002 35700.455 35700.455 <string>:1(<module>)
                      1   36.798   36.798 35700.453 35700.453 allGraphsTrain.py:13(graphTrain)
                 114279   23.475    0.000 26720.047    0.234 allGraphsTrain.py:40(<listcomp>)
                 961786    5.086    0.000 26686.759    0.028 allGraphs.py:179(getInterventionsmodel)
        43001830/743088 2248.002    0.000 24623.523    0.033 allGraphs.py:186(recursiveBEST)
        523977748/49319378 2716.727    0.000 22377.573    0.000 module.py:715(_call_impl)
               47465837  869.728    0.000 21865.508    0.000 container.py:115(forward)
               47237279  154.856    0.000 21260.087    0.000 BayesianNN.py:18(forward)
               39962094 1255.148    0.000 19299.581    0.000 BayesianNN.py:65(predict_no_convert)
              141711837  189.925    0.000 7394.610    0.000 dropout.py:57(forward)
              141711837  719.947    0.000 7204.685    0.000 functional.py:960(dropout)
              142168953  447.276    0.000 6921.103    0.000 linear.py:92(forward)
              141711837 6330.129    0.000 6330.129    0.000 {built-in method dropout}
              142168953  735.250    0.000 6300.427    0.000 functional.py:1669(linear)
                 114279  720.187    0.006 3858.394    0.034 allGraphs.py:156(transformNot)
                1739262   20.754    0.000 3323.447    0.002 BayesianNN.py:57(learn)
              142168953 3239.514    0.000 3239.514    0.000 {built-in method addmm}
                1739262   26.655    0.000 3166.463    0.002 BayesianNN.py:21(learn)
                5535923   74.794    0.000 3087.797    0.001 BayesianNN.py:61(predict)
              142397511  155.873    0.000 2120.382    0.000 activation.py:713(forward)
          866553/218698   62.468    0.000 1980.773    0.009 allGraphs.py:202(recursiveExplore)
              142397511  249.742    0.000 1964.509    0.000 functional.py:1292(leaky_relu)
                 114279    0.759    0.000 1883.072    0.016 agent.py:29(learn)
                 114279   20.015    0.000 1881.966    0.016 agent.py:117(_learn)
                 114279    9.641    0.000 1861.951    0.016 learner.py:42(Qlearn)
              142397511 1689.348    0.000 1689.348    0.000 {built-in method torch._C._nn.leaky_relu}
                1853541   13.132    0.000 1515.236    0.001 tensor.py:181(backward)
              142168953 1513.505    0.000 1513.505    0.000 {method 't' of 'torch._C._TensorBase' objects}
                1853541    8.367    0.000 1502.104    0.001 __init__.py:68(backward)
                1853541   13.141    0.000 1460.268    0.001 grad_mode.py:23(decorate_context)
                1853541 1457.944    0.001 1457.944    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                1853541   61.951    0.000 1421.372    0.001 adam.py:55(step)
                 228558    0.984    0.000 1208.452    0.005 network.py:28(forward)
                1853541  280.923    0.000 1105.019    0.001 functional.py:53(adam)
                 457116    1.627    0.000 1004.985    0.002 conv.py:422(forward)
               55020171  249.694    0.000 1003.888    0.000 tensor.py:21(wrapped)
                 457116    1.892    0.000 1002.756    0.002 conv.py:414(_conv_forward)
                 457116 1000.606    0.002 1000.606    0.002 {built-in method conv2d}
               43020876  194.849    0.000  987.314    0.000 tensor.py:506(__rsub__)
              256523397  251.257    0.000  815.754    0.000 overrides.py:1070(has_torch_function)
               43020876  792.465    0.000  792.465    0.000 {built-in method rsub}
                 114279   13.962    0.000  732.273    0.006 allGraphsTrain.py:33(<listcomp>)
               11542280  353.305    0.000  718.318    0.000 allGraphs.py:114(states)
                 114279    5.173    0.000  660.781    0.006 allGraphs.py:141(transform)
              413687497  269.536    0.000  634.207    0.000 {built-in method builtins.any}
                 114279    0.847    0.000  628.726    0.006 game.py:42(step)
                 114279    1.060    0.000  615.262    0.005 layers.py:827(step)
                 114279    2.347    0.000  609.879    0.005 agent.py:112(__call__)
              102851500  608.779    0.000  608.779    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                7275185  432.105    0.000  594.400    0.000 BayesianNN.py:43(convert_data)
              524320585  559.252    0.000  559.252    0.000 {built-in method torch._C._get_tracing_state}
               42906597  464.713    0.000  464.713    0.000 {method 'gt' of 'torch._C._TensorBase' objects}
               79448688  285.113    0.000  462.689    0.000 tensor.py:933(grad)
                1853541   39.914    0.000  347.643    0.000 optimizer.py:167(zero_grad)
              678771589  265.537    0.000  321.027    0.000 overrides.py:1083(<genexpr>)
                 114279   15.059    0.000  312.499    0.003 layers.py:17(step)
                 114280   23.856    0.000  300.185    0.003 layers.py:793(update)
               11427900   27.803    0.000  295.928    0.000 layer.py:106(move)
             2143376829  278.082    0.000  278.082    0.000 {method 'values' of 'collections.OrderedDict' objects}
               22699608  265.964    0.000  265.964    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              334457764  256.278    0.000  256.278    0.000 module.py:765(__getattr__)
              116019574  213.726    0.000  213.726    0.000 {method 'item' of 'torch._C._TensorBase' objects}
        1300990107/1300990105  210.211    0.000  213.013    0.000 {built-in method builtins.len}
                 114279   12.961    0.000  178.123    0.002 allGraphsTrain.py:51(<listcomp>)
               59122295  173.086    0.000  173.086    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               47694395   39.339    0.000  170.434    0.000 flatten.py:39(forward)
               22699608  170.308    0.000  170.308    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                 114279   21.775    0.000  162.411    0.001 allGraphsTrain.py:44(<listcomp>)
               66448171   55.250    0.000  148.703    0.000 {built-in method builtins.all}
               11427900   36.438    0.000  138.975    0.000 layers.py:844(check)
              143565378   93.374    0.000  131.725    0.000 _VF.py:25(__getattr__)
               14550371  123.452    0.000  123.452    0.000 {built-in method zeros}
                1853541    3.612    0.000  123.399    0.000 loss.py:445(forward)
                1853541   13.354    0.000  119.786    0.000 functional.py:2637(mse_loss)
               11349804  115.538    0.000  115.538    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              142168953  113.838    0.000  113.838    0.000 functional.py:1686(<listcomp>)
                2045493  110.846    0.000  110.846    0.000 {built-in method tensor}
               11427900   24.966    0.000  104.003    0.000 layers.py:838(isFree)
               11349804  101.817    0.000  101.817    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               11999295  101.231    0.000  101.231    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                1533182    2.350    0.000   97.456    0.000 game.py:38(board)
               45726575   95.245    0.000   95.245    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
              400199420   93.951    0.000   93.951    0.000 {built-in method builtins.getattr}
                 114279   34.384    0.000   92.417    0.001 agent.py:67(modify)
               11349804   92.206    0.000   92.206    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                 139935    2.131    0.000   89.143    0.001 layers.py:849(restart)
               75382195   69.086    0.000   87.218    0.000 types.py:171(__get__)
               78358944   64.969    0.000   79.036    0.000 layer.py:103(isFree)
                 799960   43.878    0.000   77.762    0.000 layer.py:175(NoRock_update)
                 961786   13.655    0.000   76.858    0.000 allGraphs.py:167(format)
               11427900   75.668    0.000   75.668    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               11349804   73.149    0.000   73.149    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                 139935    1.127    0.000   72.029    0.001 level.py:8(__init__)
                1853541   71.668    0.000   71.668    0.000 {built-in method torch._C._nn.mse_loss}
              431839044   71.599    0.000   71.599    0.000 _jit_internal.py:750(is_scripting)
               10652994   68.368    0.000   68.368    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                 342837    2.125    0.000   66.154    0.000 tensor.py:576(__iter__)
                2819978   64.859    0.000   64.859    0.000 {built-in method cat}
              165060513   62.968    0.000   62.968    0.000 tensor.py:24(<genexpr>)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9653082: <Diamonds1_0.5_NN_cpu_1> in cluster <dcc> Done

Job <Diamonds1_0.5_NN_cpu_1> was submitted from host <n-62-30-5> by user <s183905> in cluster <dcc> at Wed May 19 11:40:29 2021
Job was executed on host(s) <n-62-21-107>, in queue <hpc>, as user <s183905> in cluster <dcc> at Wed May 19 11:40:30 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 19 11:40:30 2021
Terminated at Wed May 19 21:35:39 2021
Results reported at Wed May 19 21:35:39 2021

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

    CPU time :                                   35684.19 sec.
    Max Memory :                                 107 MB
    Average Memory :                             100.87 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               16277.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   35709 sec.
    Turnaround time :                            35710 sec.

The output (if any) is above this job summary.

/zhome/ee/d/137643/Desktop/Bachelor/project-env/lib/python3.8/site-packages/torch/cuda/__init__.py:52: UserWarning: CUDA initialization: Found no NVIDIA driver on your system. Please check that you have an NVIDIA GPU and installed a driver from http://www.nvidia.com/Download/index.aspx (Triggered internally at  /pytorch/c10/cuda/CUDAFunctions.cpp:100.)
  return torch._C._cuda_getDeviceCount() > 0

# Parameters

    Name :                      Diamonds1_0.5_NN_cpu-1
    Main :                      graphTrain
    Level :                     Levels.Causal2
    Failed actions chance :     0.5
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
    Num :                       1
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      14965562411 function calls (14675209462 primitive calls) in 35700.31 seconds

##    Ordered by: cumulative time
   List reduced from 439 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35700.310 35700.310 {built-in method builtins.exec}
                      1    0.001    0.001 35700.309 35700.309 <string>:1(<module>)
                      1   86.171   86.171 35700.308 35700.308 allGraphsTrain.py:13(graphTrain)
        307281029/34351249 1332.776    0.000 12465.362    0.000 module.py:715(_call_impl)
               27292978  351.486    0.000 11804.155    0.000 container.py:115(forward)
                 320402 1794.493    0.006 11222.086    0.035 allGraphs.py:156(transformNot)
                6737869   76.006    0.000 10833.938    0.002 BayesianNN.py:57(learn)
                 320402   72.835    0.000 10549.326    0.033 allGraphsTrain.py:40(<listcomp>)
                5279242   21.760    0.000 10432.578    0.002 allGraphs.py:179(getInterventionsmodel)
                6737869   92.767    0.000 10300.417    0.002 BayesianNN.py:21(learn)
               26652174   78.651    0.000 9364.008    0.000 BayesianNN.py:18(forward)
        21870083/5070213  939.261    0.000 8643.399    0.002 allGraphs.py:186(recursiveBEST)
               19914305  231.797    0.000 8418.876    0.000 BayesianNN.py:61(predict)
                7058271   47.085    0.000 4669.068    0.001 grad_mode.py:23(decorate_context)
                 320402    2.338    0.000 4659.589    0.015 agent.py:29(learn)
                 320402   84.676    0.000 4656.354    0.015 agent.py:117(_learn)
                 320402   29.558    0.000 4571.678    0.014 learner.py:42(Qlearn)
                7058271  221.487    0.000 4527.125    0.001 adam.py:55(step)
                7058271   44.218    0.000 4143.923    0.001 tensor.py:181(backward)
                7058271   27.935    0.000 4099.705    0.001 __init__.py:68(backward)
                7058271 3953.861    0.001 3953.861    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                7058271  840.097    0.000 3370.433    0.000 functional.py:53(adam)
               81238130  215.694    0.000 3259.501    0.000 linear.py:92(forward)
               79956522   78.011    0.000 3198.370    0.000 dropout.py:57(forward)
               79956522  314.990    0.000 3120.359    0.000 functional.py:960(dropout)
               81238130  353.222    0.000 2958.923    0.000 functional.py:1669(linear)
                 640804    3.356    0.000 2761.902    0.004 network.py:28(forward)
               79956522 2725.080    0.000 2725.080    0.000 {built-in method dropout}
                 320402   20.926    0.000 2637.895    0.008 allGraphs.py:141(transform)
                1281608    5.979    0.000 2304.217    0.002 conv.py:422(forward)
                1281608    6.603    0.000 2296.357    0.002 conv.py:414(_conv_forward)
                1281608 2289.056    0.002 2289.056    0.002 {built-in method conv2d}
                 320402   66.049    0.000 1907.768    0.006 allGraphsTrain.py:33(<listcomp>)
                 320402    2.325    0.000 1870.158    0.006 game.py:42(step)
               32360703  886.316    0.000 1841.730    0.000 allGraphs.py:114(states)
                 320402    3.456    0.000 1826.709    0.006 layers.py:827(step)
               26652174 1242.472    0.000 1734.401    0.000 BayesianNN.py:43(convert_data)
              300933070  986.883    0.000 1643.645    0.000 tensor.py:933(grad)
              288362200 1558.466    0.000 1558.466    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
               81238130 1523.691    0.000 1523.691    0.000 {built-in method addmm}
          831916/209029   51.011    0.000 1450.995    0.007 allGraphs.py:202(recursiveExplore)
                 320402    7.677    0.000 1305.238    0.004 agent.py:112(__call__)
                7058271  129.056    0.000 1196.620    0.000 optimizer.py:167(zero_grad)
              464403594  346.872    0.000 1071.194    0.000 overrides.py:1070(has_torch_function)
               81878934   65.322    0.000 1021.779    0.000 activation.py:713(forward)
               81878934  123.704    0.000  956.457    0.000 functional.py:1292(leaky_relu)
                 320403   65.461    0.000  931.993    0.003 layers.py:793(update)
                 320402   41.023    0.000  886.876    0.003 layers.py:17(step)
              591213938  323.649    0.000  848.746    0.000 {built-in method builtins.any}
               32040200   76.005    0.000  841.502    0.000 layer.py:106(move)
               85980860  839.888    0.000  839.888    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               81878934  819.778    0.000  819.778    0.000 {built-in method torch._C._nn.leaky_relu}
               51385369  172.054    0.000  764.300    0.000 tensor.py:21(wrapped)
               81238130  659.358    0.000  659.358    0.000 {method 't' of 'torch._C._TensorBase' objects}
              327142829  566.044    0.000  566.044    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               85980860  527.407    0.000  527.407    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                 320402   28.678    0.000  441.373    0.001 allGraphsTrain.py:51(<listcomp>)
             1049287172  331.368    0.000  408.195    0.000 overrides.py:1083(<genexpr>)
                 320402   51.505    0.000  406.949    0.001 allGraphsTrain.py:44(<listcomp>)
                7058271   12.247    0.000  400.523    0.000 loss.py:445(forward)
               32040200  102.467    0.000  390.471    0.000 layers.py:844(check)
                7058271   48.383    0.000  388.276    0.000 functional.py:2637(mse_loss)
                8259321  387.781    0.000  387.781    0.000 {built-in method tensor}
               53304349  369.968    0.000  369.968    0.000 {built-in method zeros}
                6881253    8.352    0.000  355.857    0.000 game.py:38(board)
                 584628    7.993    0.000  345.483    0.001 layers.py:849(restart)
               42990430  330.497    0.000  330.497    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               42990430  322.457    0.000  322.457    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               17743159   71.206    0.000  321.998    0.000 tensor.py:506(__rsub__)
                5279242   52.688    0.000  313.705    0.000 allGraphs.py:167(format)
               32040200   67.642    0.000  299.535    0.000 layers.py:838(isFree)
                 584628    4.345    0.000  280.324    0.000 level.py:8(__init__)
               42990430  261.601    0.000  261.601    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               17743159  250.792    0.000  250.792    0.000 {built-in method rsub}
               33642210  243.223    0.000  243.223    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                 584628   10.073    0.000  241.872    0.000 levels.py:151(generate)
                 320402   87.545    0.000  237.392    0.001 agent.py:67(modify)
               42990430  233.130    0.000  233.130    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              219149036  193.783    0.000  231.893    0.000 layer.py:103(isFree)
              308242235  231.173    0.000  231.173    0.000 {built-in method torch._C._get_tracing_state}
                2806206   39.436    0.000  221.570    0.000 level.py:41(notUsed)
                7058271  219.424    0.000  219.424    0.000 {built-in method torch._C._nn.mse_loss}
               83425669   48.412    0.000  212.288    0.000 {built-in method builtins.all}
                2242821  119.894    0.000  207.899    0.000 layer.py:175(NoRock_update)
              503663477  132.515    0.000  192.629    0.000 enum.py:646(__hash__)
               32040200  192.561    0.000  192.561    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               35597023  191.586    0.000  191.586    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               59973982  186.228    0.000  186.228    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                 961206    5.650    0.000  183.731    0.000 tensor.py:576(__iter__)
                 961206  174.334    0.000  174.334    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               17422757  171.700    0.000  171.700    0.000 {method 'gt' of 'torch._C._TensorBase' objects}
               42990540   76.497    0.000  170.365    0.000 tensor.py:596(__hash__)
             1256417094  144.668    0.000  144.668    0.000 {method 'values' of 'collections.OrderedDict' objects}
              199071312  138.427    0.000  138.427    0.000 module.py:765(__getattr__)
              136208828   51.046    0.000  137.397    0.000 layers.py:799(<genexpr>)
        1039129932/1039129930  128.781    0.000  135.519    0.000 {built-in method builtins.len}
               42990430  124.227    0.000  124.227    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              251645376   91.364    0.000  111.068    0.000 layers.py:809(<genexpr>)
                7058271   37.514    0.000  108.929    0.000 __init__.py:28(_make_grads)
                2806206    3.059    0.000  108.061    0.000 level.py:38(elementsIn)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9668364: <Diamonds1_0.5_NN_cpu_1> in cluster <dcc> Done

Job <Diamonds1_0.5_NN_cpu_1> was submitted from host <n-62-30-8> by user <s183905> in cluster <dcc> at Wed May 19 22:55:24 2021
Job was executed on host(s) <n-62-31-3>, in queue <hpc>, as user <s183905> in cluster <dcc> at Wed May 19 22:55:25 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 19 22:55:25 2021
Terminated at Thu May 20 08:50:35 2021
Results reported at Thu May 20 08:50:35 2021

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

    CPU time :                                   35611.91 sec.
    Max Memory :                                 103 MB
    Average Memory :                             96.03 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               16281.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   35779 sec.
    Turnaround time :                            35711 sec.

The output (if any) is above this job summary.

