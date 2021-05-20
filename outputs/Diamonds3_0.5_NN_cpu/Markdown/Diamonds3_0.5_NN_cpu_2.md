/zhome/ee/d/137643/Desktop/Bachelor/project-env/lib/python3.8/site-packages/torch/cuda/__init__.py:52: UserWarning: CUDA initialization: Found no NVIDIA driver on your system. Please check that you have an NVIDIA GPU and installed a driver from http://www.nvidia.com/Download/index.aspx (Triggered internally at  /pytorch/c10/cuda/CUDAFunctions.cpp:100.)
  return torch._C._cuda_getDeviceCount() > 0

# Parameters

    Name :                      Diamonds3_0.5_NN_cpu-2
    Main :                      graphTrain
    Level :                     Levels.Causal6
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


      12220646909 function calls (11679246883 primitive calls) in 35700.28 seconds

##    Ordered by: cumulative time
   List reduced from 443 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35700.282 35700.282 {built-in method builtins.exec}
                      1    0.001    0.001 35700.282 35700.282 <string>:1(<module>)
                      1   26.516   26.516 35700.281 35700.281 allGraphsTrain.py:13(graphTrain)
                 108701   18.499    0.000 27483.879    0.253 allGraphsTrain.py:40(<listcomp>)
                 524653    2.660    0.000 27460.044    0.052 allGraphs.py:179(getInterventionsmodel)
        45881830/396215 2392.885    0.000 25843.638    0.065 allGraphs.py:186(recursiveBEST)
        546251333/50861713 2796.705    0.000 22846.545    0.000 module.py:715(_call_impl)
               49538962  871.943    0.000 22376.071    0.000 container.py:115(forward)
               49321560  151.605    0.000 21654.357    0.000 BayesianNN.py:18(forward)
               43834950 1344.023    0.000 20667.709    0.000 BayesianNN.py:65(predict_no_convert)
              147964680  193.905    0.000 7474.644    0.000 dropout.py:57(forward)
              147964680  714.067    0.000 7280.739    0.000 functional.py:960(dropout)
              148399484  457.745    0.000 7107.543    0.000 linear.py:92(forward)
              148399484  744.029    0.000 6471.864    0.000 functional.py:1669(linear)
              147964680 6405.995    0.000 6405.995    0.000 {built-in method dropout}
              148399484 3317.223    0.000 3317.223    0.000 {built-in method addmm}
                 108701  795.674    0.007 3257.437    0.030 allGraphs.py:156(transformNot)
                4272560   56.656    0.000 2338.716    0.001 BayesianNN.py:61(predict)
                1214050   14.183    0.000 2278.286    0.002 BayesianNN.py:57(learn)
                1214050   17.644    0.000 2173.749    0.002 BayesianNN.py:21(learn)
              148616886  149.037    0.000 2136.876    0.000 activation.py:713(forward)
              148616886  246.556    0.000 1987.838    0.000 functional.py:1292(leaky_relu)
                 108701    0.596    0.000 1897.048    0.017 agent.py:29(learn)
                 108701   11.187    0.000 1896.162    0.017 agent.py:117(_learn)
                 108701    8.450    0.000 1884.974    0.017 learner.py:42(Qlearn)
              148616886 1713.256    0.000 1713.256    0.000 {built-in method torch._C._nn.leaky_relu}
          652817/128438   50.346    0.000 1574.505    0.012 allGraphs.py:202(recursiveExplore)
              148399484 1537.303    0.000 1537.303    0.000 {method 't' of 'torch._C._TensorBase' objects}
                1322751    9.270    0.000 1370.484    0.001 tensor.py:181(backward)
                1322751    5.565    0.000 1361.215    0.001 __init__.py:68(backward)
                1322751 1330.359    0.001 1330.359    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                 217402    0.758    0.000 1326.364    0.006 network.py:28(forward)
                 434804    1.451    0.000 1154.620    0.003 conv.py:422(forward)
                 434804    1.463    0.000 1152.615    0.003 conv.py:414(_conv_forward)
                 434804 1150.920    0.003 1150.920    0.003 {built-in method conv2d}
               46118695  205.748    0.000 1039.989    0.000 tensor.py:506(__rsub__)
                1322751    9.490    0.000 1033.233    0.001 grad_mode.py:23(decorate_context)
               57532300  253.281    0.000 1017.092    0.000 tensor.py:21(wrapped)
                1322751   44.082    0.000 1005.851    0.001 adam.py:55(step)
                 108701   18.422    0.000  875.543    0.008 allGraphsTrain.py:33(<listcomp>)
               10978902  411.608    0.000  857.130    0.000 allGraphs.py:114(states)
               46118695  834.241    0.000  834.241    0.000 {built-in method rsub}
              234861633  237.096    0.000  788.512    0.000 overrides.py:1070(has_torch_function)
                1322751  200.141    0.000  780.236    0.001 functional.py:53(adam)
              119571600  719.800    0.000  719.800    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 108701    1.867    0.000  687.054    0.006 agent.py:112(__call__)
              396688501  264.077    0.000  623.768    0.000 {built-in method builtins.any}
                 108701    0.617    0.000  602.466    0.006 game.py:42(step)
                 108701    0.912    0.000  591.349    0.005 layers.py:827(step)
              546577436  525.576    0.000  525.576    0.000 {built-in method torch._C._get_tracing_state}
               46009994  482.164    0.000  482.164    0.000 {method 'gt' of 'torch._C._TensorBase' objects}
                5486610  313.350    0.000  435.634    0.000 BayesianNN.py:43(convert_data)
                 108701    3.687    0.000  343.691    0.003 allGraphs.py:141(transform)
               57077416  199.772    0.000  327.686    0.000 tensor.py:933(grad)
                 108701   13.469    0.000  323.437    0.003 layers.py:17(step)
              639353465  258.291    0.000  314.137    0.000 overrides.py:1083(<genexpr>)
               10870100   26.868    0.000  308.575    0.000 layer.py:106(move)
             2234544294  275.350    0.000  275.350    0.000 {method 'values' of 'collections.OrderedDict' objects}
                 108702   22.125    0.000  265.898    0.002 layers.py:793(update)
              348422093  263.450    0.000  263.450    0.000 module.py:765(__getattr__)
                1322751   27.054    0.000  243.233    0.000 optimizer.py:167(zero_grad)
              131656614  237.921    0.000  237.921    0.000 {method 'item' of 'torch._C._TensorBase' objects}
        1353274074/1353274072  230.725    0.000  233.396    0.000 {built-in method builtins.len}
               16307816  189.570    0.000  189.570    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               60626464  176.459    0.000  176.459    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               49756364   37.879    0.000  174.283    0.000 flatten.py:39(forward)
                 108701   12.035    0.000  164.743    0.002 allGraphsTrain.py:51(<listcomp>)
                 108701   20.875    0.000  157.588    0.001 allGraphsTrain.py:44(<listcomp>)
               10870100   38.752    0.000  157.401    0.000 layers.py:844(check)
               68402500   60.803    0.000  147.199    0.000 {built-in method builtins.all}
              149287431   92.606    0.000  133.713    0.000 _VF.py:25(__getattr__)
              148399484  121.832    0.000  121.832    0.000 functional.py:1686(<listcomp>)
               16307816  120.673    0.000  120.673    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               48324912  103.425    0.000  103.425    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               10870100   26.218    0.000  101.431    0.000 layers.py:838(isFree)
              384256916   97.076    0.000   97.076    0.000 {built-in method builtins.getattr}
               10973221   94.074    0.000   94.074    0.000 {built-in method zeros}
               11413605   92.509    0.000   92.509    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                1322751    2.545    0.000   86.050    0.000 loss.py:445(forward)
                1322751    9.235    0.000   83.505    0.000 functional.py:2637(mse_loss)
                 108701   29.775    0.000   82.516    0.001 agent.py:67(modify)
              149486614   79.681    0.000   79.681    0.000 {method 'dim' of 'torch._C._TensorBase' objects}
               69892216   61.825    0.000   79.010    0.000 types.py:171(__get__)
              448949423   78.728    0.000   78.728    0.000 _jit_internal.py:750(is_scripting)
                8153908   78.254    0.000   78.254    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                 869616   42.267    0.000   75.998    0.000 layer.py:175(NoRock_update)
                1556721   75.418    0.000   75.418    0.000 {built-in method tensor}
               84992221   60.682    0.000   75.213    0.000 layer.py:103(isFree)
               10870100   74.446    0.000   74.446    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                8153908   72.502    0.000   72.502    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                  88318    1.501    0.000   67.526    0.001 layers.py:849(restart)
                8153908   63.849    0.000   63.849    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              172596900   63.740    0.000   63.740    0.000 tensor.py:24(<genexpr>)
               49538962   43.301    0.000   62.615    0.000 container.py:107(__iter__)
                1068159    1.539    0.000   61.928    0.000 game.py:38(board)
              159145632   41.754    0.000   61.369    0.000 enum.py:646(__hash__)
                 326103    1.820    0.000   56.630    0.000 tensor.py:576(__iter__)
                  88318    0.785    0.000   56.118    0.001 level.py:8(__init__)
                 326103   53.816    0.000   53.816    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
                2314918   52.928    0.000   52.928    0.000 {built-in method cat}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9653089: <Diamonds3_0.5_NN_cpu_2> in cluster <dcc> Done

Job <Diamonds3_0.5_NN_cpu_2> was submitted from host <n-62-30-5> by user <s183905> in cluster <dcc> at Wed May 19 11:40:30 2021
Job was executed on host(s) <n-62-21-104>, in queue <hpc>, as user <s183905> in cluster <dcc> at Wed May 19 11:40:32 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 19 11:40:32 2021
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

    CPU time :                                   35700.41 sec.
    Max Memory :                                 109 MB
    Average Memory :                             102.32 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               16275.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   35767 sec.
    Turnaround time :                            35709 sec.

The output (if any) is above this job summary.

/zhome/ee/d/137643/Desktop/Bachelor/project-env/lib/python3.8/site-packages/torch/cuda/__init__.py:52: UserWarning: CUDA initialization: Found no NVIDIA driver on your system. Please check that you have an NVIDIA GPU and installed a driver from http://www.nvidia.com/Download/index.aspx (Triggered internally at  /pytorch/c10/cuda/CUDAFunctions.cpp:100.)
  return torch._C._cuda_getDeviceCount() > 0

# Parameters

    Name :                      Diamonds3_0.5_NN_cpu-2
    Main :                      graphTrain
    Level :                     Levels.Causal6
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
    Num :                       2
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling

Traceback (most recent call last):
  File "main.py", line 268, in <module>
    run(Defaults)
  File "/zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/auxillaries.py", line 133, in run
    (serverRun if isServer else Defaults.main).__call__(getvals(Defaults))
  File "/zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils/server.py", line 37, in serverRun
    profilingStats()
  File "/zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils/debug.py", line 59, in profilingStats
    p = Stats('stats')
  File "/appl/python/3.8.4/lib/python3.8/pstats.py", line 96, in __init__
    self.init(arg)
  File "/appl/python/3.8.4/lib/python3.8/pstats.py", line 110, in init
    self.load_stats(arg)
  File "/appl/python/3.8.4/lib/python3.8/pstats.py", line 123, in load_stats
    with open(arg, 'rb') as f:
FileNotFoundError: [Errno 2] No such file or directory: 'stats'

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9668371: <Diamonds3_0.5_NN_cpu_2> in cluster <dcc> Exited

Job <Diamonds3_0.5_NN_cpu_2> was submitted from host <n-62-30-8> by user <s183905> in cluster <dcc> at Wed May 19 22:55:25 2021
Job was executed on host(s) <n-62-11-69>, in queue <hpc>, as user <s183905> in cluster <dcc> at Wed May 19 22:55:27 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 19 22:55:27 2021
Terminated at Thu May 20 08:50:33 2021
Results reported at Thu May 20 08:50:33 2021

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

    CPU time :                                   35617.22 sec.
    Max Memory :                                 106 MB
    Average Memory :                             100.47 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               16278.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   35732 sec.
    Turnaround time :                            35708 sec.

The output (if any) is above this job summary.

