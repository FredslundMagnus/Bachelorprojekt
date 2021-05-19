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

