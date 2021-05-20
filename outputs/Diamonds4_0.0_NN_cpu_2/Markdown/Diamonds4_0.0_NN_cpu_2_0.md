/zhome/ee/d/137643/Desktop/Bachelor/project-env/lib/python3.8/site-packages/torch/cuda/__init__.py:52: UserWarning: CUDA initialization: Found no NVIDIA driver on your system. Please check that you have an NVIDIA GPU and installed a driver from http://www.nvidia.com/Download/index.aspx (Triggered internally at  /pytorch/c10/cuda/CUDAFunctions.cpp:100.)
  return torch._C._cuda_getDeviceCount() > 0

# Parameters

    Name :                      Diamonds4_0.0_NN_cpu_2-0
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
    Num :                       0
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      13622639041 function calls (13395053560 primitive calls) in 35700.21 seconds

##    Ordered by: cumulative time
   List reduced from 443 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35700.211 35700.211 {built-in method builtins.exec}
                      1    0.001    0.001 35700.211 35700.211 <string>:1(<module>)
                      1   64.280   64.280 35700.210 35700.210 allGraphsTrain.py:13(graphTrain)
        241365756/27327236 1293.760    0.000 12825.117    0.000 module.py:715(_call_impl)
               21403852  393.785    0.000 12209.951    0.001 container.py:115(forward)
                5616329   66.302    0.000 10444.513    0.002 BayesianNN.py:57(learn)
                 307055   63.647    0.000 10342.135    0.034 allGraphsTrain.py:40(<listcomp>)
                4430865   21.082    0.000 10240.020    0.002 allGraphs.py:179(getInterventionsmodel)
                5616329   83.176    0.000 9915.211    0.002 BayesianNN.py:21(learn)
               20789742   72.521    0.000 9618.262    0.000 BayesianNN.py:18(forward)
                 307055 1923.124    0.006 9372.633    0.031 allGraphs.py:156(transformNot)
        17430156/4290323  869.463    0.000 8726.408    0.002 allGraphs.py:186(recursiveBEST)
               15173413  202.759    0.000 8394.198    0.001 BayesianNN.py:61(predict)
                 307055    1.575    0.000 4677.760    0.015 agent.py:29(learn)
                 307055   36.309    0.000 4675.232    0.015 agent.py:117(_learn)
                 307055   22.386    0.000 4638.923    0.015 learner.py:42(Qlearn)
                5923384   40.438    0.000 4379.911    0.001 grad_mode.py:23(decorate_context)
                 307055   19.378    0.000 4305.171    0.014 allGraphs.py:141(transform)
                5923384  193.082    0.000 4260.955    0.001 adam.py:55(step)
                5923384   42.009    0.000 4177.423    0.001 tensor.py:181(backward)
                5923384   24.121    0.000 4135.413    0.001 __init__.py:68(backward)
                5923384 4002.081    0.001 4002.081    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               62369226   88.573    0.000 3363.890    0.000 dropout.py:57(forward)
               63597446  204.556    0.000 3293.849    0.000 linear.py:92(forward)
               62369226  323.758    0.000 3275.317    0.000 functional.py:960(dropout)
                5923384  839.879    0.000 3271.032    0.001 functional.py:53(adam)
               63597446  345.839    0.000 3004.762    0.000 functional.py:1669(linear)
               62369226 2879.090    0.000 2879.090    0.000 {built-in method dropout}
                 614110    2.082    0.000 2877.739    0.005 network.py:28(forward)
                1228220    3.826    0.000 2433.010    0.002 conv.py:422(forward)
                1228220    3.882    0.000 2427.698    0.002 conv.py:414(_conv_forward)
                1228220 2423.100    0.002 2423.100    0.002 {built-in method conv2d}
                 307055    1.559    0.000 2057.405    0.007 game.py:42(step)
                 307055    2.434    0.000 2028.459    0.007 layers.py:827(step)
                 307055   33.224    0.000 2002.105    0.007 allGraphsTrain.py:33(<listcomp>)
               31012656  955.263    0.000 1968.888    0.000 allGraphs.py:114(states)
              276349900 1663.420    0.000 1663.420    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
               20789742 1180.951    0.000 1642.908    0.000 BayesianNN.py:43(convert_data)
               63597446 1599.583    0.000 1599.583    0.000 {built-in method addmm}
              253080958  869.822    0.000 1426.615    0.000 tensor.py:933(grad)
                 307055    4.649    0.000 1424.393    0.005 agent.py:112(__call__)
          547258/140542   37.917    0.000 1234.519    0.009 allGraphs.py:202(recursiveExplore)
                 307055   36.202    0.000 1082.185    0.004 layers.py:17(step)
                5923384  125.583    0.000 1061.792    0.000 optimizer.py:167(zero_grad)
               64211556   71.757    0.000 1060.180    0.000 activation.py:713(forward)
               30705500   76.415    0.000 1042.194    0.000 layer.py:106(move)
               64211556  119.646    0.000  988.424    0.000 functional.py:1292(leaky_relu)
                 307056   62.310    0.000  940.754    0.003 layers.py:793(update)
              389811623  302.637    0.000  939.168    0.000 overrides.py:1070(has_torch_function)
               64211556  855.438    0.000  855.438    0.000 {built-in method torch._C._nn.leaky_relu}
               72308828  798.839    0.000  798.839    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              495301790  293.335    0.000  763.703    0.000 {built-in method builtins.any}
               46094379  173.042    0.000  758.318    0.000 tensor.py:21(wrapped)
               63597446  677.066    0.000  677.066    0.000 {method 't' of 'torch._C._TensorBase' objects}
               30705500  133.343    0.000  641.516    0.000 layers.py:844(check)
              312674185  608.339    0.000  608.339    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               72308828  501.224    0.000  501.224    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                 307055   59.049    0.000  454.982    0.001 allGraphsTrain.py:44(<listcomp>)
                 307055   33.839    0.000  445.941    0.001 allGraphsTrain.py:51(<listcomp>)
                 659647    9.024    0.000  411.598    0.001 layers.py:849(restart)
                5923384   11.289    0.000  380.633    0.000 loss.py:445(forward)
                5923384   40.942    0.000  369.344    0.000 functional.py:2637(mse_loss)
              880199387  291.523    0.000  355.423    0.000 overrides.py:1083(<genexpr>)
               41579485  348.284    0.000  348.284    0.000 {built-in method zeros}
                 659647    4.593    0.000  334.286    0.001 level.py:8(__init__)
               36154414  327.222    0.000  327.222    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               13853604   66.964    0.000  321.896    0.000 tensor.py:506(__rsub__)
                7288078  312.932    0.000  312.932    0.000 {built-in method tensor}
               36154414  307.927    0.000  307.927    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                 659647   11.863    0.000  292.262    0.000 levels.py:456(generate)
                5966141    7.923    0.000  283.859    0.000 game.py:38(board)
              242286921  271.525    0.000  271.525    0.000 {built-in method torch._C._get_tracing_state}
                3166271   47.145    0.000  268.447    0.000 level.py:41(notUsed)
               36154414  264.509    0.000  264.509    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               30705500   65.009    0.000  257.483    0.000 layers.py:838(isFree)
                4430865   42.702    0.000  256.182    0.000 allGraphs.py:167(format)
               13853604  254.932    0.000  254.932    0.000 {built-in method rsub}
               32240775  244.395    0.000  244.395    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
              645381217  164.608    0.000  241.963    0.000 enum.py:646(__hash__)
                 307055   95.413    0.000  235.049    0.001 agent.py:67(modify)
                5923384  222.743    0.000  222.743    0.000 {built-in method torch._C._nn.mse_loss}
               36154414  219.607    0.000  219.607    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               30705500  213.993    0.000  213.993    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                2149392  118.955    0.000  208.049    0.000 layer.py:175(NoRock_update)
              206333056  153.784    0.000  192.473    0.000 layer.py:103(isFree)
               52723462  187.327    0.000  187.327    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               28140668  178.076    0.000  178.076    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               13546549  163.221    0.000  163.221    0.000 {method 'gt' of 'torch._C._TensorBase' objects}
               76799979   45.626    0.000  160.056    0.000 {built-in method builtins.all}
                 921165    4.656    0.000  152.933    0.000 tensor.py:576(__iter__)
                 921165  145.511    0.000  145.511    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
        892127690/892127688  137.142    0.000  144.512    0.000 {built-in method builtins.len}
               36154524   63.096    0.000  141.704    0.000 tensor.py:596(__hash__)
              986866876  136.844    0.000  136.844    0.000 {method 'values' of 'collections.OrderedDict' objects}
              156672458  131.787    0.000  131.788    0.000 module.py:765(__getattr__)
                3166271    3.649    0.000  130.933    0.000 level.py:38(elementsIn)
               30705500   81.196    0.000  129.065    0.000 layers.py:602(check)
               30705500   78.966    0.000  124.001    0.000 layers.py:632(check)
               30705500   75.805    0.000  121.262    0.000 layers.py:617(check)
              240367624   90.480    0.000  109.601    0.000 layers.py:809(<genexpr>)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9668410: <Diamonds4_0.0_NN_cpu_2_0> in cluster <dcc> Done

Job <Diamonds4_0.0_NN_cpu_2_0> was submitted from host <n-62-30-8> by user <s183905> in cluster <dcc> at Wed May 19 22:59:02 2021
Job was executed on host(s) <n-62-21-107>, in queue <hpc>, as user <s183905> in cluster <dcc> at Wed May 19 22:59:03 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 19 22:59:03 2021
Terminated at Thu May 20 08:54:06 2021
Results reported at Thu May 20 08:54:06 2021

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

    CPU time :                                   35702.87 sec.
    Max Memory :                                 111 MB
    Average Memory :                             104.78 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               16273.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   35703 sec.
    Turnaround time :                            35704 sec.

The output (if any) is above this job summary.

