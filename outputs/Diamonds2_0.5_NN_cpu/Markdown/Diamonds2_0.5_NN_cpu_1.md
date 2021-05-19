/zhome/ee/d/137643/Desktop/Bachelor/project-env/lib/python3.8/site-packages/torch/cuda/__init__.py:52: UserWarning: CUDA initialization: Found no NVIDIA driver on your system. Please check that you have an NVIDIA GPU and installed a driver from http://www.nvidia.com/Download/index.aspx (Triggered internally at  /pytorch/c10/cuda/CUDAFunctions.cpp:100.)
  return torch._C._cuda_getDeviceCount() > 0

# Parameters

    Name :                      Diamonds2_0.5_NN_cpu-1
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
    Num :                       1
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      11488997149 function calls (10991212539 primitive calls) in 35700.90 seconds

##    Ordered by: cumulative time
   List reduced from 443 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35700.902 35700.902 {built-in method builtins.exec}
                      1    0.002    0.002 35700.902 35700.902 <string>:1(<module>)
                      1   32.135   32.135 35700.899 35700.899 allGraphsTrain.py:13(graphTrain)
                 100199   19.467    0.000 27126.188    0.271 allGraphsTrain.py:40(<listcomp>)
                 533782    3.208    0.000 27100.344    0.051 allGraphs.py:179(getInterventionsmodel)
        41472052/374454 2270.941    0.000 25007.581    0.067 allGraphs.py:186(recursiveBEST)
        503002459/46932579 2719.617    0.000 22530.830    0.000 module.py:715(_call_impl)
               45606988  921.009    0.000 22058.808    0.000 container.py:115(forward)
               45406590  156.372    0.000 21407.294    0.000 BayesianNN.py:18(forward)
               39655208 1293.281    0.000 20065.172    0.001 BayesianNN.py:65(predict_no_convert)
              136219770  191.596    0.000 7332.254    0.000 dropout.py:57(forward)
              136219770  724.480    0.000 7140.659    0.000 functional.py:960(dropout)
              136620566  445.940    0.000 7023.259    0.000 linear.py:92(forward)
              136620566  737.919    0.000 6405.794    0.000 functional.py:1669(linear)
              136219770 6265.281    0.000 6265.281    0.000 {built-in method dropout}
                 100199  907.557    0.009 3513.510    0.035 allGraphs.py:156(transformNot)
              136620566 3252.695    0.000 3252.695    0.000 {built-in method addmm}
                4525990   63.192    0.000 2744.502    0.001 BayesianNN.py:61(predict)
                1225392   15.138    0.000 2436.274    0.002 BayesianNN.py:57(learn)
                1225392   19.718    0.000 2291.668    0.002 BayesianNN.py:21(learn)
              136820964  145.861    0.000 2103.673    0.000 activation.py:713(forward)
          776048/159328   60.483    0.000 2036.644    0.013 allGraphs.py:202(recursiveExplore)
              136820964  233.242    0.000 1957.811    0.000 functional.py:1292(leaky_relu)
                 100199    0.740    0.000 1842.983    0.018 agent.py:29(learn)
                 100199   15.534    0.000 1841.957    0.018 agent.py:117(_learn)
                 100199    8.740    0.000 1826.423    0.018 learner.py:42(Qlearn)
              136820964 1698.778    0.000 1698.778    0.000 {built-in method torch._C._nn.leaky_relu}
              136620566 1587.611    0.000 1587.611    0.000 {method 't' of 'torch._C._TensorBase' objects}
                1325591    9.612    0.000 1365.184    0.001 tensor.py:181(backward)
                1325591    6.018    0.000 1355.572    0.001 __init__.py:68(backward)
                1325591 1320.945    0.001 1320.945    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                 200398    0.897    0.000 1250.635    0.006 network.py:28(forward)
                 400796    1.610    0.000 1074.958    0.003 conv.py:422(forward)
                 400796    1.731    0.000 1072.804    0.003 conv.py:414(_conv_forward)
                 400796 1070.857    0.003 1070.857    0.003 {built-in method conv2d}
                1325591    9.699    0.000 1065.382    0.001 grad_mode.py:23(decorate_context)
                1325591   46.765    0.000 1037.062    0.001 adam.py:55(step)
                 100199   15.519    0.000  998.829    0.010 allGraphsTrain.py:33(<listcomp>)
               41814517  203.633    0.000  998.622    0.000 tensor.py:506(__rsub__)
               10120200  474.316    0.000  983.321    0.000 allGraphs.py:114(states)
               52335412  253.629    0.000  979.324    0.000 tensor.py:21(wrapped)
              130259300  803.155    0.000  803.155    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                1325591  208.443    0.000  801.244    0.001 functional.py:53(adam)
               41814517  794.989    0.000  794.989    0.000 {built-in method rsub}
              221018456  236.693    0.000  756.520    0.000 overrides.py:1070(has_torch_function)
                 100199    2.279    0.000  649.405    0.006 agent.py:112(__call__)
                5751382  467.637    0.000  617.067    0.000 BayesianNN.py:43(convert_data)
                 100199    0.706    0.000  594.921    0.006 game.py:42(step)
              370246605  249.252    0.000  592.850    0.000 {built-in method builtins.any}
                 100199    0.998    0.000  581.800    0.006 layers.py:827(step)
              503303056  567.319    0.000  567.319    0.000 {built-in method torch._C._get_tracing_state}
               41714318  455.094    0.000  455.094    0.000 {method 'gt' of 'torch._C._TensorBase' objects}
                 100199    4.387    0.000  416.253    0.004 allGraphs.py:141(transform)
               57077668  209.871    0.000  341.159    0.000 tensor.py:933(grad)
                 100199   13.255    0.000  322.136    0.003 layers.py:17(step)
               10019900   24.722    0.000  307.530    0.000 layer.py:106(move)
              597823646  238.857    0.000  296.330    0.000 overrides.py:1083(<genexpr>)
             2057616824  294.868    0.000  294.868    0.000 {method 'values' of 'collections.OrderedDict' objects}
              141505392  267.977    0.000  267.977    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                 100200   20.871    0.000  257.313    0.003 layers.py:793(update)
                1325591   28.879    0.000  256.378    0.000 optimizer.py:167(zero_grad)
              320875609  252.213    0.000  252.213    0.000 module.py:765(__getattr__)
        1256658119/1256658117  224.001    0.000  226.802    0.000 {built-in method builtins.len}
               16307888  192.557    0.000  192.557    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               55827286  173.010    0.000  173.010    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               45807386   35.932    0.000  170.935    0.000 flatten.py:39(forward)
                 100199   12.124    0.000  167.556    0.002 allGraphsTrain.py:51(<listcomp>)
               10019900   40.753    0.000  162.300    0.000 layers.py:844(check)
                 100199   19.328    0.000  146.775    0.001 allGraphsTrain.py:44(<listcomp>)
               62355412   58.723    0.000  140.407    0.000 {built-in method builtins.all}
              137545361   89.861    0.000  128.125    0.000 _VF.py:25(__getattr__)
              136620566  119.495    0.000  119.495    0.000 functional.py:1686(<listcomp>)
               16307888  118.795    0.000  118.795    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               11502765  107.288    0.000  107.288    0.000 {built-in method zeros}
               44381596  100.412    0.000  100.412    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               10019900   24.092    0.000   98.408    0.000 layers.py:838(isFree)
               10520895   96.396    0.000   96.396    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
              358668982   95.868    0.000   95.868    0.000 {built-in method builtins.getattr}
                1487956   93.623    0.000   93.623    0.000 {built-in method tensor}
                1325591    2.730    0.000   91.908    0.000 loss.py:445(forward)
               78603812   71.361    0.000   90.373    0.000 types.py:171(__get__)
                1325591   10.059    0.000   89.178    0.000 functional.py:2637(mse_loss)
                8153944   83.741    0.000   83.741    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                 100199   28.430    0.000   81.571    0.001 agent.py:67(modify)
                1034778    1.817    0.000   80.664    0.000 game.py:38(board)
                 901800   44.335    0.000   80.510    0.000 layer.py:175(NoRock_update)
                8153944   75.490    0.000   75.490    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               80517252   60.451    0.000   74.315    0.000 layer.py:103(isFree)
              137622676   70.924    0.000   70.924    0.000 {method 'dim' of 'torch._C._TensorBase' objects}
              413638193   70.677    0.000   70.677    0.000 _jit_internal.py:750(is_scripting)
               10019900   68.044    0.000   68.044    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                8153944   65.438    0.000   65.438    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                2667278   62.752    0.000   62.752    0.000 {built-in method cat}
              151859783   41.861    0.000   60.945    0.000 enum.py:646(__hash__)
                 300597    1.953    0.000   60.184    0.000 tensor.py:576(__iter__)
              157006236   59.639    0.000   59.639    0.000 tensor.py:24(<genexpr>)
                 300597   57.183    0.000   57.183    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               45606988   37.953    0.000   56.209    0.000 container.py:107(__iter__)
                8510811   56.165    0.000   56.165    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                8153944   53.508    0.000   53.508    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9653085: <Diamonds2_0.5_NN_cpu_1> in cluster <dcc> Done

Job <Diamonds2_0.5_NN_cpu_1> was submitted from host <n-62-30-5> by user <s183905> in cluster <dcc> at Wed May 19 11:40:29 2021
Job was executed on host(s) <n-62-21-107>, in queue <hpc>, as user <s183905> in cluster <dcc> at Wed May 19 11:40:31 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 19 11:40:31 2021
Terminated at Wed May 19 21:35:42 2021
Results reported at Wed May 19 21:35:42 2021

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

    CPU time :                                   35702.91 sec.
    Max Memory :                                 112 MB
    Average Memory :                             107.10 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               16272.00 MB
    Max Swap :                                   9 MB
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   35709 sec.
    Turnaround time :                            35713 sec.

The output (if any) is above this job summary.

