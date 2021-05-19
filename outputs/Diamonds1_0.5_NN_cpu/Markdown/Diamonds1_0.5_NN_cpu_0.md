/zhome/ee/d/137643/Desktop/Bachelor/project-env/lib/python3.8/site-packages/torch/cuda/__init__.py:52: UserWarning: CUDA initialization: Found no NVIDIA driver on your system. Please check that you have an NVIDIA GPU and installed a driver from http://www.nvidia.com/Download/index.aspx (Triggered internally at  /pytorch/c10/cuda/CUDAFunctions.cpp:100.)
  return torch._C._cuda_getDeviceCount() > 0

# Parameters

    Name :                      Diamonds1_0.5_NN_cpu-0
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
    Num :                       0
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      17790054609 function calls (16982024130 primitive calls) in 35700.69 seconds

##    Ordered by: cumulative time
   List reduced from 440 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35700.693 35700.693 {built-in method builtins.exec}
                      1    0.002    0.002 35700.693 35700.693 <string>:1(<module>)
                      1   35.261   35.261 35700.691 35700.691 allGraphsTrain.py:13(graphTrain)
                 134614   26.801    0.000 27419.987    0.204 allGraphsTrain.py:40(<listcomp>)
                1223473    7.042    0.000 27380.816    0.022 allGraphs.py:179(getInterventionsmodel)
        69817552/1034145 2604.333    0.000 26072.555    0.025 allGraphs.py:186(recursiveBEST)
        814676583/75994663 2818.342    0.000 22102.642    0.000 module.py:715(_call_impl)
               73868192  799.081    0.000 21590.333    0.000 container.py:115(forward)
               73598964  151.678    0.000 21170.635    0.000 BayesianNN.py:18(forward)
               65402006 1422.349    0.000 20222.922    0.000 BayesianNN.py:65(predict_no_convert)
              221335348  476.215    0.000 7135.051    0.000 linear.py:92(forward)
              220796892  173.459    0.000 7081.731    0.000 dropout.py:57(forward)
              220796892  688.908    0.000 6908.272    0.000 functional.py:960(dropout)
              221335348  770.932    0.000 6441.277    0.000 functional.py:1669(linear)
              220796892 6030.388    0.000 6030.388    0.000 {built-in method dropout}
                 134614  692.986    0.005 3412.030    0.025 allGraphs.py:156(transformNot)
              221335348 3265.068    0.000 3265.068    0.000 {built-in method addmm}
                1991857   20.409    0.000 2865.988    0.001 BayesianNN.py:57(learn)
                1991857   23.560    0.000 2725.796    0.001 BayesianNN.py:21(learn)
                6205101   64.516    0.000 2344.009    0.000 BayesianNN.py:61(predict)
              221604576  154.001    0.000 2031.859    0.000 activation.py:713(forward)
              221604576  246.449    0.000 1877.858    0.000 functional.py:1292(leaky_relu)
                 134614    0.917    0.000 1731.987    0.013 agent.py:29(learn)
                 134614   30.876    0.000 1730.725    0.013 agent.py:117(_learn)
                 134614   12.529    0.000 1699.850    0.013 learner.py:42(Qlearn)
              221604576 1602.120    0.000 1602.120    0.000 {built-in method torch._C._nn.leaky_relu}
              221335348 1452.126    0.000 1452.126    0.000 {method 't' of 'torch._C._TensorBase' objects}
                2126471   12.160    0.000 1364.843    0.001 tensor.py:181(backward)
                2126471    8.007    0.000 1352.683    0.001 __init__.py:68(backward)
                2126471 1312.538    0.001 1312.538    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2126471   13.067    0.000 1286.063    0.001 grad_mode.py:23(decorate_context)
                2126471   61.294    0.000 1247.398    0.001 adam.py:55(step)
          754068/189328   42.292    0.000 1173.238    0.006 allGraphs.py:202(recursiveExplore)
               83617231  261.872    0.000 1105.116    0.000 tensor.py:21(wrapped)
                 269228    1.057    0.000 1050.696    0.004 network.py:28(forward)
               69482761  208.630    0.000 1029.316    0.000 tensor.py:506(__rsub__)
                2126471  235.175    0.000  939.453    0.000 functional.py:53(adam)
              357221741  265.097    0.000  908.559    0.000 overrides.py:1070(has_torch_function)
                 538456    2.023    0.000  868.497    0.002 conv.py:422(forward)
                 538456    2.692    0.000  865.690    0.002 conv.py:414(_conv_forward)
                 538456  862.680    0.002  862.680    0.002 {built-in method conv2d}
               69482761  820.687    0.000  820.687    0.000 {built-in method rsub}
                 134614   23.071    0.000  718.621    0.005 allGraphsTrain.py:33(<listcomp>)
              596101256  308.410    0.000  713.745    0.000 {built-in method builtins.any}
               13596115  336.220    0.000  695.556    0.000 allGraphs.py:114(states)
                 134614    0.960    0.000  664.527    0.005 game.py:42(step)
                 134614    1.259    0.000  646.755    0.005 layers.py:827(step)
                 134614    6.340    0.000  611.587    0.005 allGraphs.py:141(transform)
              121153000  592.907    0.000  592.907    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
               69348147  533.143    0.000  533.143    0.000 {method 'gt' of 'torch._C._TensorBase' objects}
                 134614    3.130    0.000  529.836    0.004 agent.py:112(__call__)
                8196958  356.867    0.000  505.959    0.000 BayesianNN.py:43(convert_data)
              815080425  487.965    0.000  487.965    0.000 {built-in method torch._C._get_tracing_state}
               91196438  259.462    0.000  434.520    0.000 tensor.py:933(grad)
              967440621  298.137    0.000  361.365    0.000 overrides.py:1083(<genexpr>)
                 134614   16.355    0.000  334.603    0.002 layers.py:17(step)
                2126471   38.209    0.000  323.243    0.000 optimizer.py:167(zero_grad)
             3332574524  318.502    0.000  318.502    0.000 {method 'values' of 'collections.OrderedDict' objects}
               13461400   29.517    0.000  316.625    0.000 layer.py:106(move)
              519608228  315.488    0.000  315.488    0.000 module.py:765(__getattr__)
                 134615   24.677    0.000  309.151    0.002 layers.py:793(update)
               26056108  236.392    0.000  236.392    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
        1982252835/1982252833  226.124    0.000  228.669    0.000 {built-in method builtins.len}
              136607329  210.785    0.000  210.785    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               74137420   46.025    0.000  200.837    0.000 flatten.py:39(forward)
               87598820  195.724    0.000  195.724    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               97078731   69.724    0.000  176.245    0.000 {built-in method builtins.all}
                 134614   11.834    0.000  167.825    0.001 allGraphsTrain.py:51(<listcomp>)
              222923363  117.286    0.000  161.239    0.000 _VF.py:25(__getattr__)
                2494043  161.201    0.000  161.201    0.000 {built-in method tensor}
                 134614   20.128    0.000  159.294    0.001 allGraphsTrain.py:44(<listcomp>)
               13461400   37.547    0.000  148.519    0.000 layers.py:844(check)
                1896544    3.173    0.000  147.681    0.000 game.py:38(board)
               26056108  145.681    0.000  145.681    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              221335348  134.235    0.000  134.235    0.000 functional.py:1686(<listcomp>)
                1223473   23.951    0.000  126.933    0.000 allGraphs.py:167(format)
               16393917  115.288    0.000  115.288    0.000 {built-in method zeros}
               13461400   23.470    0.000  111.594    0.000 layers.py:838(isFree)
                2126471    3.353    0.000  110.325    0.000 loss.py:445(forward)
               71876335  107.337    0.000  107.337    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
              580263413  107.289    0.000  107.289    0.000 {built-in method builtins.getattr}
                2126471   14.239    0.000  106.972    0.000 functional.py:2637(mse_loss)
                 134614   32.854    0.000   95.516    0.001 agent.py:67(modify)
              102966812   74.534    0.000   95.249    0.000 types.py:171(__get__)
               14134470   93.778    0.000   93.778    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               13028054   93.271    0.000   93.271    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                 170275    2.430    0.000   91.234    0.001 layers.py:849(restart)
               13028054   88.492    0.000   88.492    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               88510501   74.633    0.000   88.124    0.000 layer.py:103(isFree)
              670116349   86.315    0.000   86.315    0.000 _jit_internal.py:750(is_scripting)
              222681608   83.694    0.000   83.694    0.000 {method 'dim' of 'torch._C._TensorBase' objects}
               73868192   52.924    0.000   76.607    0.000 container.py:107(__iter__)
               13461400   75.206    0.000   75.206    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                 942305   42.259    0.000   74.902    0.000 layer.py:175(NoRock_update)
               13028054   74.284    0.000   74.284    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                 170275    1.225    0.000   73.346    0.000 level.py:8(__init__)
              250851693   71.489    0.000   71.489    0.000 tensor.py:24(<genexpr>)
                 403842    2.504    0.000   70.610    0.000 tensor.py:576(__iter__)
                 403842   66.515    0.000   66.515    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
              188105522   45.286    0.000   65.962    0.000 enum.py:646(__hash__)


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
Subject: Job 9653081: <Diamonds1_0.5_NN_cpu_0> in cluster <dcc> Exited

Job <Diamonds1_0.5_NN_cpu_0> was submitted from host <n-62-30-5> by user <s183905> in cluster <dcc> at Wed May 19 11:40:29 2021
Job was executed on host(s) <n-62-11-67>, in queue <hpc>, as user <s183905> in cluster <dcc> at Wed May 19 11:40:30 2021
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

Exited with exit code 1.

Resource usage summary:

    CPU time :                                   35613.18 sec.
    Max Memory :                                 99 MB
    Average Memory :                             92.90 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               16285.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   35709 sec.
    Turnaround time :                            35710 sec.

The output (if any) is above this job summary.

