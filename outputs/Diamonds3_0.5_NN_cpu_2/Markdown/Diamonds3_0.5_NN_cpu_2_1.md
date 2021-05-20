/zhome/ee/d/137643/Desktop/Bachelor/project-env/lib/python3.8/site-packages/torch/cuda/__init__.py:52: UserWarning: CUDA initialization: Found no NVIDIA driver on your system. Please check that you have an NVIDIA GPU and installed a driver from http://www.nvidia.com/Download/index.aspx (Triggered internally at  /pytorch/c10/cuda/CUDAFunctions.cpp:100.)
  return torch._C._cuda_getDeviceCount() > 0

# Parameters

    Name :                      Diamonds3_0.5_NN_cpu_2-1
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
    Num :                       1
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      8361474910 function calls (8208947540 primitive calls) in 35700.34 seconds

##    Ordered by: cumulative time
   List reduced from 441 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35700.340 35700.340 {built-in method builtins.exec}
                      1    0.001    0.001 35700.340 35700.340 <string>:1(<module>)
                      1   72.517   72.517 35700.338 35700.338 allGraphsTrain.py:13(graphTrain)
        162017610/17924780 1075.780    0.000 11728.292    0.001 module.py:715(_call_impl)
                 191482 2450.305    0.013 11487.596    0.060 allGraphs.py:156(transformNot)
               14409283  352.140    0.000 11193.780    0.001 container.py:115(forward)
                3324015   67.224    0.000 9198.850    0.003 BayesianNN.py:57(learn)
                 191482   57.694    0.000 9126.330    0.048 allGraphsTrain.py:40(<listcomp>)
                2069750   12.822    0.000 9041.409    0.004 allGraphs.py:179(getInterventionsmodel)
                3324015   75.476    0.000 8682.658    0.003 BayesianNN.py:21(learn)
               14026319   65.871    0.000 8153.118    0.001 BayesianNN.py:18(forward)
               10702304  143.565    0.000 7393.502    0.001 BayesianNN.py:61(predict)
        9794663/1927579  723.361    0.000 6497.524    0.003 allGraphs.py:186(recursiveBEST)
                 191482    1.734    0.000 6309.604    0.033 agent.py:29(learn)
                 191482   17.382    0.000 6307.104    0.033 agent.py:117(_learn)
                 191482   25.799    0.000 6289.722    0.033 learner.py:42(Qlearn)
                3515497   35.682    0.000 5516.299    0.002 tensor.py:181(backward)
                3515497   20.091    0.000 5480.617    0.002 __init__.py:68(backward)
                3515497 5357.200    0.002 5357.200    0.002 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3515497   37.120    0.000 4050.166    0.001 grad_mode.py:23(decorate_context)
                3515497  158.998    0.000 3943.351    0.001 adam.py:55(step)
                 382964    2.730    0.000 3283.280    0.009 network.py:28(forward)
                3515497  798.929    0.000 3189.944    0.001 functional.py:53(adam)
               42844885  164.789    0.000 2838.679    0.000 linear.py:92(forward)
                 765928    6.677    0.000 2815.893    0.004 conv.py:422(forward)
                 765928    5.592    0.000 2807.426    0.004 conv.py:414(_conv_forward)
                 765928 2801.289    0.004 2801.289    0.004 {built-in method conv2d}
               42078957   61.114    0.000 2750.397    0.000 dropout.py:57(forward)
               42078957  223.779    0.000 2689.283    0.000 functional.py:960(dropout)
               42844885  247.032    0.000 2611.803    0.000 functional.py:1669(linear)
                 191482   50.899    0.000 2548.266    0.013 allGraphsTrain.py:33(<listcomp>)
               19339783 1149.510    0.000 2497.382    0.000 allGraphs.py:114(states)
               42078957 2414.763    0.000 2414.763    0.000 {built-in method dropout}
          709215/142171   87.632    0.000 2301.308    0.016 allGraphs.py:202(recursiveExplore)
              210630700 2236.837    0.000 2236.837    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 191482   13.979    0.000 1792.101    0.009 allGraphs.py:141(transform)
                 191482    5.642    0.000 1712.836    0.009 agent.py:112(__call__)
               14026319 1227.467    0.000 1690.638    0.000 BayesianNN.py:43(convert_data)
               42844885 1458.223    0.000 1458.223    0.000 {built-in method addmm}
                 191482    1.816    0.000 1228.369    0.006 game.py:42(step)
                 191482    2.652    0.000 1185.021    0.006 layers.py:827(step)
              150331682  748.361    0.000 1116.744    0.000 tensor.py:933(grad)
               43227849   51.144    0.000 1018.184    0.000 activation.py:713(forward)
               43227849   78.705    0.000  967.040    0.000 functional.py:1292(leaky_relu)
                3515497   98.792    0.000  892.494    0.000 optimizer.py:167(zero_grad)
               43227849  880.903    0.000  880.903    0.000 {built-in method torch._C._nn.leaky_relu}
               42951892  789.496    0.000  789.496    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              233104443  715.179    0.000  715.179    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               28731220  149.824    0.000  709.128    0.000 tensor.py:21(wrapped)
               42844885  658.992    0.000  658.992    0.000 {method 't' of 'torch._C._TensorBase' objects}
              237019465  208.713    0.000  611.774    0.000 overrides.py:1070(has_torch_function)
                 191483   50.728    0.000  593.989    0.003 layers.py:793(update)
                 191482   28.550    0.000  585.170    0.003 layers.py:17(step)
               19148200   47.824    0.000  554.336    0.000 layer.py:106(move)
               42951892  512.338    0.000  512.338    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              305811026  178.129    0.000  476.806    0.000 {built-in method builtins.any}
                 191482   39.037    0.000  476.202    0.002 allGraphsTrain.py:51(<listcomp>)
                 191482   58.563    0.000  432.661    0.002 allGraphsTrain.py:44(<listcomp>)
               28052639  360.779    0.000  360.779    0.000 {built-in method zeros}
                3515497    9.242    0.000  332.399    0.000 loss.py:445(forward)
                3515497   35.554    0.000  323.157    0.000 functional.py:2637(mse_loss)
                3863467  318.713    0.000  318.713    0.000 {built-in method tensor}
               21475946  317.640    0.000  317.640    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               20105610  302.039    0.000  302.039    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                3027161    6.044    0.000  286.782    0.000 game.py:38(board)
               21475946  283.214    0.000  283.214    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              162592056  278.577    0.000  278.577    0.000 {built-in method torch._C._get_tracing_state}
               19148200   65.403    0.000  277.658    0.000 layers.py:844(check)
               21475946  270.420    0.000  270.420    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                8625610   49.362    0.000  265.613    0.000 tensor.py:506(__rsub__)
                2069750   41.783    0.000  227.692    0.000 allGraphs.py:167(format)
              539250657  183.074    0.000  224.403    0.000 overrides.py:1083(<genexpr>)
                8625610  216.252    0.000  216.252    0.000 {built-in method rsub}
                 191482   77.221    0.000  208.963    0.001 agent.py:67(modify)
               19148200  204.378    0.000  204.378    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               21475946  203.835    0.000  203.835    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                3515497  191.908    0.000  191.908    0.000 {built-in method torch._C._nn.mse_loss}
               19148200   44.700    0.000  182.305    0.000 layers.py:838(isFree)
                 232618    5.094    0.000  176.676    0.001 layers.py:849(restart)
               33940447  175.462    0.000  175.462    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               19058868  161.134    0.000  161.134    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                1531864   87.019    0.000  153.163    0.000 layer.py:175(NoRock_update)
               47879520   29.129    0.000  149.722    0.000 {built-in method builtins.all}
                 232618    2.230    0.000  145.485    0.001 level.py:8(__init__)
                8434128  137.650    0.000  137.650    0.000 {method 'gt' of 'torch._C._TensorBase' objects}
              150921063  114.048    0.000  137.605    0.000 layer.py:103(isFree)
              334293468   93.761    0.000  134.582    0.000 enum.py:646(__hash__)
                 232618    5.048    0.000  128.250    0.001 levels.py:303(generate)
                 574446    4.348    0.000  124.821    0.000 tensor.py:576(__iter__)
               21475946  121.270    0.000  121.270    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                1394970   18.708    0.000  118.048    0.000 level.py:41(notUsed)
                 574446  116.678    0.000  116.678    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
        581981387/581981385  101.210    0.000  108.191    0.000 {built-in method builtins.len}
               69489977   25.074    0.000  102.114    0.000 layers.py:799(<genexpr>)
               21476056   47.845    0.000  101.629    0.000 tensor.py:596(__hash__)
              662479723   99.347    0.000   99.347    0.000 {method 'values' of 'collections.OrderedDict' objects}
                3515497   29.932    0.000   96.479    0.000 __init__.py:28(_make_grads)
              104955627   95.086    0.000   95.087    0.000 module.py:765(__getattr__)
                2651140   93.238    0.000   93.238    0.000 {built-in method cat}
               69053986   66.778    0.000   87.014    0.000 types.py:171(__get__)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9668396: <Diamonds3_0.5_NN_cpu_2_1> in cluster <dcc> Done

Job <Diamonds3_0.5_NN_cpu_2_1> was submitted from host <n-62-30-8> by user <s183905> in cluster <dcc> at Wed May 19 22:59:00 2021
Job was executed on host(s) <n-62-23-29>, in queue <hpc>, as user <s183905> in cluster <dcc> at Wed May 19 22:59:01 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 19 22:59:01 2021
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

    CPU time :                                   35700.08 sec.
    Max Memory :                                 103 MB
    Average Memory :                             98.23 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               16281.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   35798 sec.
    Turnaround time :                            35706 sec.

The output (if any) is above this job summary.

