/zhome/ee/d/137643/Desktop/Bachelor/project-env/lib/python3.8/site-packages/torch/cuda/__init__.py:52: UserWarning: CUDA initialization: Found no NVIDIA driver on your system. Please check that you have an NVIDIA GPU and installed a driver from http://www.nvidia.com/Download/index.aspx (Triggered internally at  /pytorch/c10/cuda/CUDAFunctions.cpp:100.)
  return torch._C._cuda_getDeviceCount() > 0

# Parameters

    Name :                      Diamonds3_0.0_NN_cpu_2-2
    Main :                      graphTrain
    Level :                     Levels.Causal6
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


      13178697541 function calls (12949199516 primitive calls) in 35700.31 seconds

##    Ordered by: cumulative time
   List reduced from 441 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35700.305 35700.305 {built-in method builtins.exec}
                      1    0.001    0.001 35700.305 35700.305 <string>:1(<module>)
                      1   59.356   59.356 35700.304 35700.304 allGraphsTrain.py:13(graphTrain)
        241810064/26477644 1320.768    0.000 13095.239    0.000 module.py:715(_call_impl)
               21533242  395.553    0.000 12539.228    0.001 container.py:115(forward)
                 265131   54.917    0.000 11214.141    0.042 allGraphsTrain.py:40(<listcomp>)
                3408694   15.118    0.000 11127.092    0.003 allGraphs.py:179(getInterventionsmodel)
               21002980   75.901    0.000 9719.816    0.000 BayesianNN.py:18(forward)
        16897968/3272404  955.571    0.000 9232.289    0.003 allGraphs.py:186(recursiveBEST)
               16323709  223.029    0.000 9165.480    0.001 BayesianNN.py:61(predict)
                4679271   55.650    0.000 8975.024    0.002 BayesianNN.py:57(learn)
                 265131 2091.415    0.008 8940.146    0.034 allGraphs.py:156(transformNot)
                4679271   68.326    0.000 8524.468    0.002 BayesianNN.py:21(learn)
                 265131    1.267    0.000 4766.072    0.018 agent.py:29(learn)
                 265131   50.982    0.000 4764.132    0.018 agent.py:117(_learn)
                 265131   20.472    0.000 4713.150    0.018 learner.py:42(Qlearn)
                4944402   33.706    0.000 3930.790    0.001 tensor.py:181(backward)
                4944402   19.906    0.000 3897.084    0.001 __init__.py:68(backward)
                4944402   32.998    0.000 3857.952    0.001 grad_mode.py:23(decorate_context)
                4944402 3781.652    0.001 3781.652    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                4944402  161.606    0.000 3760.532    0.001 adam.py:55(step)
                 265131   16.609    0.000 3552.960    0.013 allGraphs.py:141(transform)
               63008940   85.760    0.000 3358.277    0.000 dropout.py:57(forward)
               64069464  202.426    0.000 3299.803    0.000 linear.py:92(forward)
               63008940  316.588    0.000 3272.516    0.000 functional.py:960(dropout)
                 530262    1.884    0.000 3117.162    0.006 network.py:28(forward)
               64069464  345.464    0.000 3016.741    0.000 functional.py:1669(linear)
                4944402  747.749    0.000 2926.839    0.001 functional.py:53(adam)
               63008940 2877.835    0.000 2877.835    0.000 {built-in method dropout}
                1060524    3.497    0.000 2739.847    0.003 conv.py:422(forward)
                1060524    3.524    0.000 2735.044    0.003 conv.py:414(_conv_forward)
                1060524 2730.938    0.003 2730.938    0.003 {built-in method conv2d}
                 265131   36.368    0.000 2233.551    0.008 allGraphsTrain.py:33(<listcomp>)
               26778332 1039.544    0.000 2197.191    0.000 allGraphs.py:114(states)
                 265131    1.431    0.000 2119.855    0.008 game.py:42(step)
                 265131    2.157    0.000 2092.510    0.008 layers.py:827(step)
              291644600 1911.497    0.000 1911.497    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
               21002980 1277.568    0.000 1771.370    0.000 BayesianNN.py:43(convert_data)
          675919/136290   52.259    0.000 1657.780    0.012 allGraphs.py:202(recursiveExplore)
               64069464 1602.008    0.000 1602.008    0.000 {built-in method addmm}
                 265131    4.253    0.000 1500.214    0.006 agent.py:112(__call__)
              211376778  746.188    0.000 1211.021    0.000 tensor.py:933(grad)
                 265131   31.381    0.000 1092.659    0.004 layers.py:17(step)
               64599726   68.010    0.000 1072.880    0.000 activation.py:713(forward)
               26513100   65.018    0.000 1057.678    0.000 layer.py:106(move)
               64599726  114.864    0.000 1004.870    0.000 functional.py:1292(leaky_relu)
                 265132   55.562    0.000  994.943    0.004 layers.py:793(update)
                4944402  101.454    0.000  899.869    0.000 optimizer.py:167(zero_grad)
               64599726  877.690    0.000  877.690    0.000 {built-in method torch._C._nn.leaky_relu}
              337155606  268.254    0.000  826.735    0.000 overrides.py:1070(has_torch_function)
               42269079  172.764    0.000  751.152    0.000 tensor.py:21(wrapped)
               60393348  713.674    0.000  713.674    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               64069464  691.154    0.000  691.154    0.000 {method 't' of 'torch._C._TensorBase' objects}
              437017298  264.387    0.000  689.849    0.000 {built-in method builtins.any}
               26513100  142.009    0.000  683.481    0.000 layers.py:844(check)
              322839091  627.039    0.000  627.039    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               60393348  452.330    0.000  452.330    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                 609776    8.977    0.000  446.004    0.001 layers.py:849(restart)
                 265131   31.447    0.000  429.821    0.002 allGraphsTrain.py:51(<listcomp>)
               42005961  378.601    0.000  378.601    0.000 {built-in method zeros}
                 265131   48.199    0.000  378.061    0.001 allGraphsTrain.py:44(<listcomp>)
                 609776    4.064    0.000  372.442    0.001 level.py:8(__init__)
               14430324   72.607    0.000  347.077    0.000 tensor.py:506(__rsub__)
                 609776   12.829    0.000  334.159    0.001 levels.py:303(generate)
                4944402    9.237    0.000  322.927    0.000 loss.py:445(forward)
                4944402   33.917    0.000  313.690    0.000 functional.py:2637(mse_loss)
              769893256  256.898    0.000  311.790    0.000 overrides.py:1083(<genexpr>)
                3659004   53.726    0.000  308.511    0.000 level.py:41(notUsed)
               30196674  297.490    0.000  297.490    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                5880680  277.714    0.000  277.714    0.000 {built-in method tensor}
               14430324  274.470    0.000  274.470    0.000 {built-in method rsub}
               30196674  274.262    0.000  274.262    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              725778870  182.997    0.000  263.302    0.000 enum.py:646(__hash__)
              242605457  254.216    0.000  254.216    0.000 {built-in method torch._C._get_tracing_state}
               26513100   66.055    0.000  251.123    0.000 layers.py:838(isFree)
                4734350    6.337    0.000  249.430    0.000 game.py:38(board)
               27838755  247.179    0.000  247.179    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               30196674  236.967    0.000  236.967    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                3408694   39.904    0.000  220.572    0.000 allGraphs.py:167(format)
                 265131   86.797    0.000  215.736    0.001 agent.py:67(modify)
                2121056  114.251    0.000  200.597    0.000 layer.py:175(NoRock_update)
               68782279   44.075    0.000  195.483    0.000 {built-in method builtins.all}
               30196674  192.813    0.000  192.813    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                4944402  190.530    0.000  190.530    0.000 {built-in method torch._C._nn.mse_loss}
              209844972  147.314    0.000  185.068    0.000 layer.py:103(isFree)
               26513100  179.728    0.000  179.728    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               27556902  178.375    0.000  178.375    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               14165193  171.526    0.000  171.526    0.000 {method 'gt' of 'torch._C._TensorBase' objects}
               48576604  165.451    0.000  165.451    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               26513100   95.853    0.000  157.079    0.000 layers.py:424(check)
                3659004    3.998    0.000  148.366    0.000 level.py:38(elementsIn)
        876814927/876814925  136.994    0.000  143.837    0.000 {built-in method builtins.len}
                 795393    4.187    0.000  133.324    0.000 tensor.py:576(__iter__)
              988773498  131.266    0.000  131.266    0.000 {method 'values' of 'collections.OrderedDict' objects}
              156473346  129.119    0.000  129.120    0.000 module.py:765(__getattr__)
                 795393  126.712    0.000  126.712    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               96595772   37.736    0.000  125.431    0.000 layers.py:799(<genexpr>)
               30196784   52.842    0.000  118.063    0.000 tensor.py:596(__hash__)
              233130816   90.475    0.000  109.201    0.000 layers.py:809(<genexpr>)
               26513100   68.694    0.000  108.012    0.000 layers.py:452(check)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9668409: <Diamonds3_0.0_NN_cpu_2_2> in cluster <dcc> Done

Job <Diamonds3_0.0_NN_cpu_2_2> was submitted from host <n-62-30-8> by user <s183905> in cluster <dcc> at Wed May 19 22:59:02 2021
Job was executed on host(s) <n-62-21-107>, in queue <hpc>, as user <s183905> in cluster <dcc> at Wed May 19 22:59:03 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 19 22:59:03 2021
Terminated at Thu May 20 08:56:01 2021
Results reported at Thu May 20 08:56:01 2021

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

    CPU time :                                   35702.14 sec.
    Max Memory :                                 105 MB
    Average Memory :                             100.06 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               16279.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   35818 sec.
    Turnaround time :                            35819 sec.

The output (if any) is above this job summary.

