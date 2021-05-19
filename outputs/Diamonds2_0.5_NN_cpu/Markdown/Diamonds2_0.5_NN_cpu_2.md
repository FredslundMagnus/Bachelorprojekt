/zhome/ee/d/137643/Desktop/Bachelor/project-env/lib/python3.8/site-packages/torch/cuda/__init__.py:52: UserWarning: CUDA initialization: Found no NVIDIA driver on your system. Please check that you have an NVIDIA GPU and installed a driver from http://www.nvidia.com/Download/index.aspx (Triggered internally at  /pytorch/c10/cuda/CUDAFunctions.cpp:100.)
  return torch._C._cuda_getDeviceCount() > 0

# Parameters

    Name :                      Diamonds2_0.5_NN_cpu-2
    Main :                      graphTrain
    Level :                     Levels.Causal5
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
    Num :                       2
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      12223602781 function calls (11680126954 primitive calls) in 35701.49 seconds

##    Ordered by: cumulative time
   List reduced from 443 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35701.487 35701.487 {built-in method builtins.exec}
                      1    0.002    0.002 35701.487 35701.487 <string>:1(<module>)
                      1   26.899   26.899 35701.485 35701.485 allGraphsTrain.py:13(graphTrain)
                  93409   19.328    0.000 27822.291    0.298 allGraphsTrain.py:40(<listcomp>)
                 613315    3.540    0.000 27795.982    0.045 allGraphs.py:179(getInterventionsmodel)
        44487915/386978 2324.655    0.000 25090.728    0.065 allGraphs.py:186(recursiveBEST)
        549721986/51207676 2848.603    0.000 22780.470    0.000 module.py:715(_call_impl)
               49851431  829.819    0.000 22303.089    0.000 container.py:115(forward)
               49664613  171.953    0.000 21794.967    0.000 BayesianNN.py:18(forward)
               42589108 1302.206    0.000 20066.832    0.000 BayesianNN.py:65(predict_no_convert)
              148993839  189.109    0.000 7505.934    0.000 dropout.py:57(forward)
              148993839  738.172    0.000 7316.825    0.000 functional.py:960(dropout)
              149367475  453.123    0.000 7084.073    0.000 linear.py:92(forward)
              149367475  762.582    0.000 6451.039    0.000 functional.py:1669(linear)
              148993839 6425.227    0.000 6425.227    0.000 {built-in method dropout}
              149367475 3274.326    0.000 3274.326    0.000 {built-in method addmm}
                5812669   76.767    0.000 3271.244    0.001 BayesianNN.py:61(predict)
                  93409  784.133    0.008 3231.956    0.035 allGraphs.py:156(transformNot)
         1086505/226337   80.153    0.000 2643.636    0.012 allGraphs.py:202(recursiveExplore)
                1262836   14.793    0.000 2375.058    0.002 BayesianNN.py:57(learn)
                1262836   19.751    0.000 2236.042    0.002 BayesianNN.py:21(learn)
              149554293  156.119    0.000 2168.904    0.000 activation.py:713(forward)
              149554293  261.169    0.000 2012.785    0.000 functional.py:1292(leaky_relu)
              149554293 1725.355    0.000 1725.355    0.000 {built-in method torch._C._nn.leaky_relu}
                  93409    0.573    0.000 1707.595    0.018 agent.py:29(learn)
                  93409   12.258    0.000 1706.770    0.018 agent.py:117(_learn)
                  93409    7.796    0.000 1694.512    0.018 learner.py:42(Qlearn)
              149367475 1569.571    0.000 1569.571    0.000 {method 't' of 'torch._C._TensorBase' objects}
                1356245    9.204    0.000 1297.196    0.001 tensor.py:181(backward)
                1356245    5.974    0.000 1287.992    0.001 __init__.py:68(backward)
                1356245 1256.009    0.001 1256.009    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                 186818    0.842    0.000 1137.390    0.006 network.py:28(forward)
               45054514  210.070    0.000 1034.599    0.000 tensor.py:506(__rsub__)
                1356245    9.712    0.000 1025.819    0.001 grad_mode.py:23(decorate_context)
                1356245   44.706    0.000  997.907    0.001 adam.py:55(step)
                 373636    1.382    0.000  992.470    0.003 conv.py:422(forward)
                 373636    1.603    0.000  990.593    0.003 conv.py:414(_conv_forward)
                 373636  988.787    0.003  988.787    0.003 {built-in method conv2d}
               54862459  255.120    0.000  974.573    0.000 tensor.py:21(wrapped)
                  93409   14.451    0.000  874.039    0.009 allGraphsTrain.py:33(<listcomp>)
                9434410  416.338    0.000  859.598    0.000 allGraphs.py:114(states)
               45054514  824.528    0.000  824.528    0.000 {built-in method rsub}
                1356245  194.416    0.000  768.450    0.001 functional.py:53(adam)
              234969976  229.555    0.000  760.677    0.000 overrides.py:1070(has_torch_function)
                7075505  530.166    0.000  697.470    0.000 BayesianNN.py:43(convert_data)
              121432300  686.450    0.000  686.450    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
              396322314  256.131    0.000  609.101    0.000 {built-in method builtins.any}
                  93409    1.962    0.000  578.414    0.006 agent.py:112(__call__)
              550002213  560.210    0.000  560.210    0.000 {built-in method torch._C._get_tracing_state}
                  93409    0.614    0.000  553.708    0.006 game.py:42(step)
                  93409    0.861    0.000  541.482    0.006 layers.py:827(step)
               44961105  468.393    0.000  468.393    0.000 {method 'gt' of 'torch._C._TensorBase' objects}
                  93409    4.171    0.000  442.080    0.005 allGraphs.py:141(transform)
               58270076  203.130    0.000  330.720    0.000 tensor.py:933(grad)
              638315454  248.137    0.000  307.948    0.000 overrides.py:1083(<genexpr>)
                  93409   12.119    0.000  302.486    0.003 layers.py:17(step)
                9340900   23.565    0.000  289.167    0.000 layer.py:106(move)
             2248739375  278.272    0.000  278.272    0.000 {method 'values' of 'collections.OrderedDict' objects}
              350596972  265.546    0.000  265.546    0.000 module.py:765(__getattr__)
              132036780  251.999    0.000  251.999    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                1356245   27.655    0.000  245.390    0.000 optimizer.py:167(zero_grad)
                  93410   18.929    0.000  236.899    0.003 layers.py:793(update)
        1356515559/1356515557  225.407    0.000  227.668    0.000 {built-in method builtins.len}
               16648576  186.270    0.000  186.270    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               50038249   40.257    0.000  185.765    0.000 flatten.py:39(forward)
               59379149  180.591    0.000  180.591    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                9340900   37.104    0.000  149.721    0.000 layers.py:844(check)
                  93409   10.331    0.000  139.056    0.001 allGraphsTrain.py:51(<listcomp>)
                  93409   17.225    0.000  134.724    0.001 allGraphsTrain.py:44(<listcomp>)
               64203459   56.471    0.000  129.703    0.000 {built-in method builtins.all}
              150350084   95.630    0.000  128.971    0.000 _VF.py:25(__getattr__)
              149367475  124.030    0.000  124.030    0.000 functional.py:1686(<listcomp>)
               14151011  120.849    0.000  120.849    0.000 {built-in method zeros}
               16648576  116.872    0.000  116.872    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               48588595  109.980    0.000  109.980    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                9340900   23.945    0.000   95.515    0.000 layers.py:838(isFree)
              385422261   93.255    0.000   93.255    0.000 {built-in method builtins.getattr}
                1504889   92.622    0.000   92.622    0.000 {built-in method tensor}
               91085459   73.420    0.000   92.169    0.000 types.py:171(__get__)
                1356245    2.694    0.000   88.335    0.000 loss.py:445(forward)
                1356245    9.833    0.000   85.642    0.000 functional.py:2637(mse_loss)
                1080361    1.754    0.000   80.961    0.000 game.py:38(board)
                8324288   80.558    0.000   80.558    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                9807945   77.587    0.000   77.587    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                3627490   75.507    0.000   75.507    0.000 {built-in method cat}
                 840690   41.200    0.000   74.856    0.000 layer.py:175(NoRock_update)
              451984462   73.470    0.000   73.470    0.000 _jit_internal.py:750(is_scripting)
                8324288   73.102    0.000   73.102    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                  93409   25.842    0.000   72.918    0.001 agent.py:67(modify)
               81044130   57.719    0.000   71.570    0.000 layer.py:103(isFree)
              150301685   68.520    0.000   68.520    0.000 {method 'dim' of 'torch._C._TensorBase' objects}
               10338904   63.942    0.000   63.942    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                9340900   62.367    0.000   62.367    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                8324288   62.266    0.000   62.266    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              164587377   61.106    0.000   61.106    0.000 tensor.py:24(<genexpr>)
               49851431   42.291    0.000   60.706    0.000 container.py:107(__iter__)
                 613315    9.592    0.000   57.712    0.000 allGraphs.py:167(format)
              146088274   38.665    0.000   56.089    0.000 enum.py:646(__hash__)
                  68627    1.239    0.000   55.848    0.001 layers.py:849(restart)
                 280227    1.680    0.000   54.577    0.000 tensor.py:576(__iter__)


Traceback (most recent call last):
  File "main.py", line 268, in <module>
    run(Defaults)
  File "/zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/auxillaries.py", line 133, in run
    (serverRun if isServer else Defaults.main).__call__(getvals(Defaults))
  File "/zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils/server.py", line 37, in serverRun
    profilingStats()
  File "/zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils/debug.py", line 62, in profilingStats
    os.remove('stats')
FileNotFoundError: [Errno 2] No such file or directory: 'stats'

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9653086: <Diamonds2_0.5_NN_cpu_2> in cluster <dcc> Exited

Job <Diamonds2_0.5_NN_cpu_2> was submitted from host <n-62-30-5> by user <s183905> in cluster <dcc> at Wed May 19 11:40:30 2021
Job was executed on host(s) <n-62-21-107>, in queue <hpc>, as user <s183905> in cluster <dcc> at Wed May 19 11:40:31 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 19 11:40:31 2021
Terminated at Wed May 19 21:35:43 2021
Results reported at Wed May 19 21:35:43 2021

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

Exited with exit code 1.

Resource usage summary:

    CPU time :                                   35703.48 sec.
    Max Memory :                                 115 MB
    Average Memory :                             110.68 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               16269.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   35709 sec.
    Turnaround time :                            35713 sec.

The output (if any) is above this job summary.

