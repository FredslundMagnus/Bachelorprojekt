/zhome/ee/d/137643/Desktop/Bachelor/project-env/lib/python3.8/site-packages/torch/cuda/__init__.py:52: UserWarning: CUDA initialization: Found no NVIDIA driver on your system. Please check that you have an NVIDIA GPU and installed a driver from http://www.nvidia.com/Download/index.aspx (Triggered internally at  /pytorch/c10/cuda/CUDAFunctions.cpp:100.)
  return torch._C._cuda_getDeviceCount() > 0

# Parameters

    Name :                      Diamonds1_0.5_NN_cpu_2-1
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


      15508537191 function calls (15208476885 primitive calls) in 35700.23 seconds

##    Ordered by: cumulative time
   List reduced from 439 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35700.229 35700.229 {built-in method builtins.exec}
                      1    0.001    0.001 35700.229 35700.229 <string>:1(<module>)
                      1   91.399   91.399 35700.227 35700.227 allGraphsTrain.py:13(graphTrain)
        317622973/35637713 1292.848    0.000 12379.917    0.000 module.py:715(_call_impl)
               28198526  337.810    0.000 11732.489    0.000 container.py:115(forward)
                 336977 1855.395    0.006 11409.208    0.034 allGraphs.py:156(transformNot)
                7102210   75.065    0.000 10844.482    0.002 BayesianNN.py:57(learn)
                 336977   70.049    0.000 10357.356    0.031 allGraphsTrain.py:40(<listcomp>)
                7102210   83.639    0.000 10291.281    0.001 BayesianNN.py:21(learn)
                5631626   21.469    0.000 10243.651    0.002 allGraphs.py:179(getInterventionsmodel)
               27524572   69.185    0.000 9170.794    0.000 BayesianNN.py:18(forward)
        22923021/5435319  942.213    0.000 8606.601    0.002 allGraphs.py:186(recursiveBEST)
               20422362  219.740    0.000 8260.034    0.000 BayesianNN.py:61(predict)
                7439187   46.870    0.000 4699.838    0.001 grad_mode.py:23(decorate_context)
                7439187  217.005    0.000 4564.583    0.001 adam.py:55(step)
                 336977    2.430    0.000 4522.890    0.013 agent.py:29(learn)
                 336977   63.798    0.000 4519.585    0.013 agent.py:117(_learn)
                 336977   29.710    0.000 4455.787    0.013 learner.py:42(Qlearn)
                7439187   42.426    0.000 4106.059    0.001 tensor.py:181(backward)
                7439187   26.465    0.000 4063.633    0.001 __init__.py:68(backward)
                7439187 3921.468    0.001 3921.468    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                7439187  857.145    0.000 3432.795    0.000 functional.py:53(adam)
               83921624  203.123    0.000 3210.366    0.000 linear.py:92(forward)
               82573716   75.670    0.000 3141.701    0.000 dropout.py:57(forward)
               82573716  295.498    0.000 3066.031    0.000 functional.py:960(dropout)
               83921624  348.868    0.000 2921.639    0.000 functional.py:1669(linear)
                 673954    2.522    0.000 2867.752    0.004 network.py:28(forward)
               82573716 2690.824    0.000 2690.824    0.000 {built-in method dropout}
                 336977   19.129    0.000 2552.528    0.008 allGraphs.py:141(transform)
                1347908    4.960    0.000 2338.758    0.002 conv.py:422(forward)
                1347908    5.739    0.000 2331.832    0.002 conv.py:414(_conv_forward)
                1347908 2325.366    0.002 2325.366    0.002 {built-in method conv2d}
                 336977   58.500    0.000 1962.319    0.006 allGraphsTrain.py:33(<listcomp>)
               34034778  917.167    0.000 1903.825    0.000 allGraphs.py:114(states)
                 336977    2.306    0.000 1847.131    0.005 game.py:42(step)
                 336977    2.934    0.000 1806.088    0.005 layers.py:827(step)
               27524572 1312.469    0.000 1789.911    0.000 BayesianNN.py:43(convert_data)
              303279700 1609.670    0.000 1609.670    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
              317163592  954.042    0.000 1604.451    0.000 tensor.py:933(grad)
               83921624 1519.586    0.000 1519.586    0.000 {built-in method addmm}
                 336977    7.595    0.000 1469.984    0.004 agent.py:112(__call__)
          783239/196307   45.527    0.000 1308.627    0.007 allGraphs.py:202(recursiveExplore)
                7439187  130.779    0.000 1170.866    0.000 optimizer.py:167(zero_grad)
               84595578   67.951    0.000 1077.600    0.000 activation.py:713(forward)
              487745590  340.315    0.000 1063.147    0.000 overrides.py:1070(has_torch_function)
               84595578  109.645    0.000 1009.649    0.000 functional.py:1292(leaky_relu)
                 336977   41.830    0.000  905.906    0.003 layers.py:17(step)
                 336978   65.003    0.000  892.930    0.003 layers.py:793(update)
               84595578  887.419    0.000  887.419    0.000 {built-in method torch._C._nn.leaky_relu}
               90618152  861.020    0.000  861.020    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               33697700   76.780    0.000  859.305    0.000 layer.py:106(move)
              619653379  327.103    0.000  846.314    0.000 {built-in method builtins.any}
               53794196  167.438    0.000  772.348    0.000 tensor.py:21(wrapped)
               83921624  647.210    0.000  647.210    0.000 {method 't' of 'torch._C._TensorBase' objects}
              344082298  584.518    0.000  584.518    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               90618152  550.314    0.000  550.314    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                 336977   29.386    0.000  450.617    0.001 allGraphsTrain.py:51(<listcomp>)
                 336977   52.460    0.000  425.891    0.001 allGraphsTrain.py:44(<listcomp>)
             1100763992  326.841    0.000  401.268    0.000 overrides.py:1083(<genexpr>)
               33697700  102.478    0.000  394.530    0.000 layers.py:844(check)
                7439187   11.562    0.000  393.676    0.000 loss.py:445(forward)
                7439187   46.174    0.000  382.115    0.000 functional.py:2637(mse_loss)
                8764427  379.937    0.000  379.937    0.000 {built-in method tensor}
               55049145  356.264    0.000  356.264    0.000 {built-in method zeros}
                7316512    7.559    0.000  346.564    0.000 game.py:38(board)
                 590009    7.959    0.000  339.429    0.001 layers.py:849(restart)
               45309076  327.031    0.000  327.031    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               45309076  319.127    0.000  319.127    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               18411611   65.577    0.000  313.229    0.000 tensor.py:506(__rsub__)
               33697700   65.987    0.000  310.626    0.000 layers.py:838(isFree)
                5631626   47.169    0.000  304.409    0.000 allGraphs.py:167(format)
                 590009    4.082    0.000  274.364    0.000 level.py:8(__init__)
               45309076  269.762    0.000  269.762    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               35382585  250.339    0.000  250.339    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               18411611  247.653    0.000  247.653    0.000 {built-in method rsub}
              233270176  205.265    0.000  244.639    0.000 layer.py:103(isFree)
                 336977   89.141    0.000  240.001    0.001 agent.py:67(modify)
                 590009    9.742    0.000  238.024    0.000 levels.py:151(generate)
               45309076  231.404    0.000  231.404    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              318633904  229.699    0.000  229.699    0.000 {built-in method torch._C._get_tracing_state}
                7439187  218.052    0.000  218.052    0.000 {built-in method torch._C._nn.mse_loss}
                2833423   38.542    0.000  218.049    0.000 level.py:41(notUsed)
                2358846  121.719    0.000  212.020    0.000 layer.py:175(NoRock_update)
               33697700  200.593    0.000  200.593    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
              525989472  135.649    0.000  197.240    0.000 enum.py:646(__hash__)
               36811577  188.665    0.000  188.665    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               62570180  188.024    0.000  188.024    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                1010931    5.699    0.000  181.013    0.000 tensor.py:576(__iter__)
               87491996   40.840    0.000  173.769    0.000 {built-in method builtins.all}
               18074634  172.470    0.000  172.470    0.000 {method 'gt' of 'torch._C._TensorBase' objects}
                1010931  171.577    0.000  171.577    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               45309186   72.606    0.000  166.664    0.000 tensor.py:596(__hash__)
             1298690418  144.745    0.000  144.745    0.000 {method 'values' of 'collections.OrderedDict' objects}
              205840811  137.705    0.000  137.706    0.000 module.py:765(__getattr__)
        1079217078/1079217076  128.202    0.000  134.730    0.000 {built-in method builtins.len}
               45309076  120.316    0.000  120.316    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              264862328   89.870    0.000  111.715    0.000 layers.py:809(<genexpr>)
                2833423    2.977    0.000  107.114    0.000 level.py:38(elementsIn)
                7439187   36.407    0.000  107.095    0.000 __init__.py:28(_make_grads)
              129077332   83.046    0.000  106.547    0.000 types.py:171(__get__)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9668390: <Diamonds1_0.5_NN_cpu_2_1> in cluster <dcc> Done

Job <Diamonds1_0.5_NN_cpu_2_1> was submitted from host <n-62-30-8> by user <s183905> in cluster <dcc> at Wed May 19 22:58:59 2021
Job was executed on host(s) <n-62-31-4>, in queue <hpc>, as user <s183905> in cluster <dcc> at Wed May 19 22:59:00 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 19 22:59:00 2021
Terminated at Thu May 20 08:54:03 2021
Results reported at Thu May 20 08:54:03 2021

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

    CPU time :                                   35611.66 sec.
    Max Memory :                                 104 MB
    Average Memory :                             97.80 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               16280.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   35735 sec.
    Turnaround time :                            35704 sec.

The output (if any) is above this job summary.

