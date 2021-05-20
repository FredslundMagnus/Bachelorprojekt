/zhome/ee/d/137643/Desktop/Bachelor/project-env/lib/python3.8/site-packages/torch/cuda/__init__.py:52: UserWarning: CUDA initialization: Found no NVIDIA driver on your system. Please check that you have an NVIDIA GPU and installed a driver from http://www.nvidia.com/Download/index.aspx (Triggered internally at  /pytorch/c10/cuda/CUDAFunctions.cpp:100.)
  return torch._C._cuda_getDeviceCount() > 0

# Parameters

    Name :                      Diamonds1_0.0_NN_cpu_2-0
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
    Num :                       0
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      13122414825 function calls (12888823951 primitive calls) in 35700.30 seconds

##    Ordered by: cumulative time
   List reduced from 440 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35700.297 35700.297 {built-in method builtins.exec}
                      1    0.002    0.002 35700.297 35700.297 <string>:1(<module>)
                      1   83.015   83.015 35700.295 35700.295 allGraphsTrain.py:13(graphTrain)
        247204852/27538112 1372.144    0.000 13280.627    0.000 module.py:715(_call_impl)
               21966674  406.963    0.000 12652.793    0.001 container.py:115(forward)
                 282886   64.679    0.000 11017.869    0.039 allGraphsTrain.py:40(<listcomp>)
                4115986   18.230    0.000 10915.990    0.003 allGraphs.py:179(getInterventionsmodel)
                5288552   63.434    0.000 10073.202    0.002 BayesianNN.py:57(learn)
               21400902   80.524    0.000 9996.181    0.000 BayesianNN.py:18(forward)
                5288552   83.560    0.000 9603.953    0.002 BayesianNN.py:21(learn)
                 282886 1776.711    0.006 9330.373    0.033 allGraphs.py:156(transformNot)
        17311486/3934921  910.095    0.000 8938.062    0.002 allGraphs.py:186(recursiveBEST)
               16112350  214.161    0.000 8934.716    0.001 BayesianNN.py:61(predict)
                 282886    1.896    0.000 4597.067    0.016 agent.py:29(learn)
                 282886   39.490    0.000 4594.412    0.016 agent.py:117(_learn)
                 282886   25.019    0.000 4554.922    0.016 learner.py:42(Qlearn)
                5571438   39.944    0.000 4293.603    0.001 grad_mode.py:23(decorate_context)
                5571438  190.483    0.000 4176.791    0.001 adam.py:55(step)
                5571438   39.497    0.000 3964.993    0.001 tensor.py:181(backward)
                5571438   25.603    0.000 3925.496    0.001 __init__.py:68(backward)
                5571438 3788.726    0.001 3788.726    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                 282886   19.897    0.000 3718.912    0.013 allGraphs.py:141(transform)
               65334250  237.147    0.000 3460.669    0.000 linear.py:92(forward)
               64202706   89.179    0.000 3431.670    0.000 dropout.py:57(forward)
               64202706  338.070    0.000 3342.491    0.000 functional.py:960(dropout)
                5571438  804.814    0.000 3168.268    0.001 functional.py:53(adam)
               65334250  364.603    0.000 3135.022    0.000 functional.py:1669(linear)
                 565772    2.580    0.000 2969.141    0.005 network.py:28(forward)
               64202706 2925.821    0.000 2925.821    0.000 {built-in method dropout}
                1131544    4.332    0.000 2505.615    0.002 conv.py:422(forward)
                1131544    4.863    0.000 2499.750    0.002 conv.py:414(_conv_forward)
                1131544 2494.230    0.002 2494.230    0.002 {built-in method conv2d}
                 282886    2.058    0.000 2136.628    0.008 game.py:42(step)
                 282886    2.721    0.000 2100.022    0.007 layers.py:827(step)
                 282886   50.687    0.000 1813.589    0.006 allGraphsTrain.py:33(<listcomp>)
               28571587  849.412    0.000 1762.908    0.000 allGraphs.py:114(states)
          728222/181065   53.468    0.000 1691.366    0.009 allGraphs.py:202(recursiveExplore)
               65334250 1648.989    0.000 1648.989    0.000 {built-in method addmm}
               21400902 1132.456    0.000 1607.122    0.000 BayesianNN.py:43(convert_data)
              254597800 1526.922    0.000 1526.922    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 282886    5.942    0.000 1504.720    0.005 agent.py:112(__call__)
              237960860  882.970    0.000 1464.689    0.000 tensor.py:933(grad)
               65900022   74.436    0.000 1121.359    0.000 activation.py:713(forward)
                 282886   38.333    0.000 1100.910    0.004 layers.py:17(step)
                5571438  122.460    0.000 1080.770    0.000 optimizer.py:167(zero_grad)
               28288600   74.517    0.000 1058.554    0.000 layer.py:106(move)
               65900022  120.131    0.000 1046.923    0.000 functional.py:1292(leaky_relu)
              371391522  319.177    0.000  995.032    0.000 overrides.py:1070(has_torch_function)
                 282887   61.828    0.000  992.345    0.004 layers.py:793(update)
               65900022  914.130    0.000  914.130    0.000 {built-in method torch._C._nn.leaky_relu}
               43909638  200.723    0.000  837.035    0.000 tensor.py:21(wrapped)
              475452070  317.352    0.000  802.326    0.000 {built-in method builtins.any}
               67988800  773.398    0.000  773.398    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               65334250  715.835    0.000  715.835    0.000 {method 't' of 'torch._C._TensorBase' objects}
               28288600  133.425    0.000  640.303    0.000 layers.py:844(check)
              288177208  523.653    0.000  523.653    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                 282886   34.829    0.000  501.281    0.002 allGraphsTrain.py:51(<listcomp>)
               67988800  489.191    0.000  489.191    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                 705278   10.153    0.000  477.408    0.001 layers.py:849(restart)
                 282886   50.047    0.000  396.307    0.001 allGraphsTrain.py:44(<listcomp>)
                 705278    5.103    0.000  387.504    0.001 level.py:8(__init__)
                5571438   10.895    0.000  374.256    0.000 loss.py:445(forward)
              842219196  302.813    0.000  369.052    0.000 overrides.py:1083(<genexpr>)
               42801805  365.902    0.000  365.902    0.000 {built-in method zeros}
                5571438   40.618    0.000  363.361    0.000 functional.py:2637(mse_loss)
               14206608   74.818    0.000  351.937    0.000 tensor.py:506(__rsub__)
                6751123  338.444    0.000  338.444    0.000 {built-in method tensor}
                 705278   12.946    0.000  338.404    0.000 levels.py:151(generate)
               33994400  325.453    0.000  325.453    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                3384311   57.395    0.000  312.407    0.000 level.py:41(notUsed)
                5530417    8.126    0.000  308.722    0.000 game.py:38(board)
               33994400  297.750    0.000  297.750    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               14206608  277.119    0.000  277.119    0.000 {built-in method rsub}
               29703030  277.062    0.000  277.062    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               28288600   66.312    0.000  274.232    0.000 layers.py:838(isFree)
                4115986   45.499    0.000  266.560    0.000 allGraphs.py:167(format)
              248053510  263.439    0.000  263.439    0.000 {built-in method torch._C._get_tracing_state}
               33994400  254.913    0.000  254.913    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              613484791  177.661    0.000  248.101    0.000 enum.py:646(__hash__)
                 282886   96.422    0.000  243.482    0.001 agent.py:67(modify)
                1980209  126.740    0.000  217.452    0.000 layer.py:175(NoRock_update)
                5571438  214.765    0.000  214.765    0.000 {built-in method torch._C._nn.mse_loss}
               33994400  210.255    0.000  210.255    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              193987418  170.378    0.000  207.920    0.000 layer.py:103(isFree)
               28288600  187.113    0.000  187.113    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               28632426  182.721    0.000  182.721    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               50821046  176.535    0.000  176.535    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                 848658    5.245    0.000  174.253    0.000 tensor.py:576(__iter__)
               13923722  172.569    0.000  172.569    0.000 {method 'gt' of 'torch._C._TensorBase' objects}
                 848658  166.065    0.000  166.065    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
                3384311    3.972    0.000  153.390    0.000 level.py:38(elementsIn)
               33994510   67.127    0.000  148.926    0.000 tensor.py:596(__hash__)
        882943607/882943605  134.867    0.000  142.821    0.000 {built-in method builtins.len}
               72198338   45.903    0.000  139.560    0.000 {built-in method builtins.all}
              160187715  138.331    0.000  138.332    0.000 module.py:765(__getattr__)
             1010786082  130.767    0.000  130.767    0.000 {method 'values' of 'collections.OrderedDict' objects}
               28288600   82.551    0.000  129.234    0.000 layers.py:231(check)
               28288600   79.774    0.000  126.362    0.000 layers.py:207(check)
               28288600   74.360    0.000  119.653    0.000 layers.py:219(check)
              220667376   91.933    0.000  110.482    0.000 layers.py:809(<genexpr>)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9668401: <Diamonds1_0.0_NN_cpu_2_0> in cluster <dcc> Done

Job <Diamonds1_0.0_NN_cpu_2_0> was submitted from host <n-62-30-8> by user <s183905> in cluster <dcc> at Wed May 19 22:59:01 2021
Job was executed on host(s) <n-62-21-108>, in queue <hpc>, as user <s183905> in cluster <dcc> at Wed May 19 22:59:01 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 19 22:59:01 2021
Terminated at Thu May 20 08:54:04 2021
Results reported at Thu May 20 08:54:04 2021

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

    CPU time :                                   35697.12 sec.
    Max Memory :                                 107 MB
    Average Memory :                             101.63 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               16277.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   35733 sec.
    Turnaround time :                            35703 sec.

The output (if any) is above this job summary.

