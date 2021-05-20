/zhome/ee/d/137643/Desktop/Bachelor/project-env/lib/python3.8/site-packages/torch/cuda/__init__.py:52: UserWarning: CUDA initialization: Found no NVIDIA driver on your system. Please check that you have an NVIDIA GPU and installed a driver from http://www.nvidia.com/Download/index.aspx (Triggered internally at  /pytorch/c10/cuda/CUDAFunctions.cpp:100.)
  return torch._C._cuda_getDeviceCount() > 0

# Parameters

    Name :                      Diamonds1_0.0_NN_cpu_2-1
    Main :                      graphTrain
    Level :                     Levels.Causal2
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
    Num :                       1
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      13770836680 function calls (13532095094 primitive calls) in 35700.15 seconds

##    Ordered by: cumulative time
   List reduced from 439 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35700.154 35700.154 {built-in method builtins.exec}
                      1    0.001    0.001 35700.154 35700.154 <string>:1(<module>)
                      1   56.991   56.991 35700.153 35700.153 allGraphsTrain.py:13(graphTrain)
        252819475/28242025 1389.310    0.000 13025.728    0.000 module.py:715(_call_impl)
               22457745  412.145    0.000 12399.626    0.001 container.py:115(forward)
                 293345   61.215    0.000 11174.844    0.038 allGraphsTrain.py:40(<listcomp>)
                4411758   19.108    0.000 11075.288    0.003 allGraphs.py:179(getInterventionsmodel)
                5490935   64.179    0.000 10365.517    0.002 BayesianNN.py:57(learn)
               21871055   77.612    0.000 10114.992    0.000 BayesianNN.py:18(forward)
                5490935   81.550    0.000 9856.189    0.002 BayesianNN.py:21(learn)
                 293345 1851.114    0.006 9258.108    0.032 allGraphs.py:156(transformNot)
               16380120  218.292    0.000 9096.294    0.001 BayesianNN.py:61(predict)
        17837445/4227820  928.659    0.000 9094.553    0.002 allGraphs.py:186(recursiveBEST)
                5784280   39.368    0.000 4448.425    0.001 grad_mode.py:23(decorate_context)
                 293345    1.415    0.000 4337.875    0.015 agent.py:29(learn)
                 293345   19.239    0.000 4335.722    0.015 agent.py:117(_learn)
                5784280  186.595    0.000 4332.303    0.001 adam.py:55(step)
                 293345   22.327    0.000 4316.483    0.015 learner.py:42(Qlearn)
                 293345   18.576    0.000 4193.718    0.014 allGraphs.py:141(transform)
                5784280   37.899    0.000 3995.236    0.001 tensor.py:181(backward)
                5784280   23.237    0.000 3957.337    0.001 __init__.py:68(backward)
                5784280 3824.969    0.001 3824.969    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               65613165   89.768    0.000 3478.104    0.000 dropout.py:57(forward)
               66786545  217.131    0.000 3438.924    0.000 linear.py:92(forward)
               65613165  348.517    0.000 3388.336    0.000 functional.py:960(dropout)
                5784280  867.462    0.000 3370.890    0.001 functional.py:53(adam)
               66786545  354.841    0.000 3140.104    0.000 functional.py:1669(linear)
               65613165 2966.439    0.000 2966.439    0.000 {built-in method dropout}
                 586690    2.056    0.000 2595.130    0.004 network.py:28(forward)
                1173380    3.646    0.000 2199.532    0.002 conv.py:422(forward)
                1173380    4.015    0.000 2194.537    0.002 conv.py:414(_conv_forward)
                1173380 2189.909    0.002 2189.909    0.002 {built-in method conv2d}
                 293345    1.496    0.000 2102.040    0.007 game.py:42(step)
                 293345    2.168    0.000 2074.462    0.007 layers.py:827(step)
                 293345   18.417    0.000 1853.611    0.006 allGraphsTrain.py:33(<listcomp>)
               29627946  892.079    0.000 1835.200    0.000 allGraphs.py:114(states)
               21871055 1249.697    0.000 1738.469    0.000 BayesianNN.py:43(convert_data)
          738037/183938   53.351    0.000 1706.053    0.009 allGraphs.py:202(recursiveExplore)
               66786545 1659.309    0.000 1659.309    0.000 {built-in method addmm}
              264010900 1583.655    0.000 1583.655    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
              247046650  862.850    0.000 1401.084    0.000 tensor.py:933(grad)
                 293345    4.367    0.000 1313.738    0.004 agent.py:112(__call__)
               67373235   72.441    0.000 1123.446    0.000 activation.py:713(forward)
               67373235  122.691    0.000 1051.005    0.000 functional.py:1292(leaky_relu)
                5784280  119.370    0.000 1046.320    0.000 optimizer.py:167(zero_grad)
                 293346   61.411    0.000 1035.117    0.004 layers.py:793(update)
                 293345   33.754    0.000 1034.454    0.004 layers.py:17(step)
               29334500   71.806    0.000  997.041    0.000 layer.py:106(move)
              384632003  297.603    0.000  926.161    0.000 overrides.py:1070(has_torch_function)
               67373235  915.870    0.000  915.870    0.000 {built-in method torch._C._nn.leaky_relu}
               70584740  818.589    0.000  818.589    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               45258294  177.645    0.000  791.176    0.000 tensor.py:21(wrapped)
              491539451  285.592    0.000  752.306    0.000 {built-in method builtins.any}
               66786545  735.667    0.000  735.667    0.000 {method 't' of 'torch._C._TensorBase' objects}
               29334500  132.928    0.000  618.181    0.000 layers.py:844(check)
              298838679  548.100    0.000  548.100    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               70584740  535.016    0.000  535.016    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                 782257   10.199    0.000  481.607    0.001 layers.py:849(restart)
                 293345   33.576    0.000  456.338    0.002 allGraphsTrain.py:51(<listcomp>)
                 293345   52.479    0.000  416.008    0.001 allGraphsTrain.py:44(<listcomp>)
                 782257    4.801    0.000  390.308    0.000 level.py:8(__init__)
                5784280   10.658    0.000  374.603    0.000 loss.py:445(forward)
               43742111  372.858    0.000  372.858    0.000 {built-in method zeros}
                5784280   39.337    0.000  363.945    0.000 functional.py:2637(mse_loss)
              871556879  289.461    0.000  353.154    0.000 overrides.py:1083(<genexpr>)
               14457069   71.336    0.000  342.698    0.000 tensor.py:506(__rsub__)
                 782257   13.861    0.000  342.527    0.000 levels.py:151(generate)
               35292370  333.373    0.000  333.373    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                3755862   54.755    0.000  315.046    0.000 level.py:41(notUsed)
               35292370  310.883    0.000  310.883    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                7142981  310.203    0.000  310.203    0.000 {built-in method tensor}
                5878484    7.686    0.000  282.555    0.000 game.py:38(board)
               14457069  271.362    0.000  271.362    0.000 {built-in method rsub}
               35292370  270.332    0.000  270.332    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              253699510  266.352    0.000  266.352    0.000 {built-in method torch._C._get_tracing_state}
               30801225  260.543    0.000  260.543    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                4411758   39.032    0.000  253.994    0.000 allGraphs.py:167(format)
              677051619  172.372    0.000  249.070    0.000 enum.py:646(__hash__)
               29334500   62.863    0.000  242.848    0.000 layers.py:838(isFree)
                 293345   95.173    0.000  230.567    0.001 agent.py:67(modify)
               35292370  222.875    0.000  222.875    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                5784280  221.964    0.000  221.964    0.000 {built-in method torch._C._nn.mse_loss}
                2053422  119.881    0.000  204.580    0.000 layer.py:175(NoRock_update)
               29334500  196.855    0.000  196.855    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               74592894   45.107    0.000  192.566    0.000 {built-in method builtins.all}
               29350223  188.512    0.000  188.512    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               52378935  180.673    0.000  180.673    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              192667424  143.245    0.000  179.985    0.000 layer.py:103(isFree)
               14163724  177.642    0.000  177.642    0.000 {method 'gt' of 'torch._C._TensorBase' objects}
                3755862    4.162    0.000  153.866    0.000 level.py:38(elementsIn)
        907862964/907862962  139.401    0.000  146.863    0.000 {built-in method builtins.len}
                 880035    4.576    0.000  144.951    0.000 tensor.py:576(__iter__)
                 880035  137.763    0.000  137.763    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               35292480   61.839    0.000  137.198    0.000 tensor.py:596(__hash__)
             1033735645  133.826    0.000  133.826    0.000 {method 'values' of 'collections.OrderedDict' objects}
              163869453  130.411    0.000  130.411    0.000 module.py:765(__getattr__)
               29334500   76.683    0.000  120.369    0.000 layers.py:219(check)
               98465643   37.343    0.000  119.709    0.000 layers.py:799(<genexpr>)
               29334500   75.197    0.000  117.700    0.000 layers.py:231(check)
               29334500   74.030    0.000  116.976    0.000 layers.py:207(check)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9668402: <Diamonds1_0.0_NN_cpu_2_1> in cluster <dcc> Done

Job <Diamonds1_0.0_NN_cpu_2_1> was submitted from host <n-62-30-8> by user <s183905> in cluster <dcc> at Wed May 19 22:59:01 2021
Job was executed on host(s) <n-62-21-104>, in queue <hpc>, as user <s183905> in cluster <dcc> at Wed May 19 22:59:03 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 19 22:59:03 2021
Terminated at Thu May 20 08:54:05 2021
Results reported at Thu May 20 08:54:05 2021

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

    CPU time :                                   35700.10 sec.
    Max Memory :                                 108 MB
    Average Memory :                             102.03 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               16276.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   35753 sec.
    Turnaround time :                            35704 sec.

The output (if any) is above this job summary.

