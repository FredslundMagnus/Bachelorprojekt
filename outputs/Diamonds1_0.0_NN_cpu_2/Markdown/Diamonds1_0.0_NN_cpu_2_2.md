/zhome/ee/d/137643/Desktop/Bachelor/project-env/lib/python3.8/site-packages/torch/cuda/__init__.py:52: UserWarning: CUDA initialization: Found no NVIDIA driver on your system. Please check that you have an NVIDIA GPU and installed a driver from http://www.nvidia.com/Download/index.aspx (Triggered internally at  /pytorch/c10/cuda/CUDAFunctions.cpp:100.)
  return torch._C._cuda_getDeviceCount() > 0

# Parameters

    Name :                      Diamonds1_0.0_NN_cpu_2-2
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
    Num :                       2
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      13552364299 function calls (13316379533 primitive calls) in 35700.22 seconds

##    Ordered by: cumulative time
   List reduced from 439 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35700.216 35700.216 {built-in method builtins.exec}
                      1    0.001    0.001 35700.216 35700.216 <string>:1(<module>)
                      1   53.528   53.528 35700.215 35700.215 allGraphsTrain.py:13(graphTrain)
        249423553/27877173 1412.221    0.000 13282.731    0.000 module.py:715(_call_impl)
               22154638  421.398    0.000 12662.930    0.001 container.py:115(forward)
                 294765   61.624    0.000 11306.351    0.038 allGraphsTrain.py:40(<listcomp>)
                4296945   18.356    0.000 11207.617    0.003 allGraphs.py:179(getInterventionsmodel)
               21565108   76.409    0.000 10375.735    0.000 BayesianNN.py:18(forward)
                5427770   63.250    0.000 10321.781    0.002 BayesianNN.py:57(learn)
                5427770   81.987    0.000 9838.131    0.002 BayesianNN.py:21(learn)
        18168912/4155779  960.369    0.000 9603.341    0.002 allGraphs.py:186(recursiveBEST)
                 294765 1885.131    0.006 9568.380    0.032 allGraphs.py:156(transformNot)
               16137338  221.026    0.000 9221.631    0.001 BayesianNN.py:61(predict)
                 294765    1.320    0.000 4346.016    0.015 agent.py:29(learn)
                 294765   38.136    0.000 4343.808    0.015 agent.py:117(_learn)
                5722535   38.730    0.000 4335.806    0.001 grad_mode.py:23(decorate_context)
                 294765   21.859    0.000 4305.672    0.015 learner.py:42(Qlearn)
                5722535  190.794    0.000 4220.431    0.001 adam.py:55(step)
                5722535   39.477    0.000 3927.997    0.001 tensor.py:181(backward)
                5722535   23.244    0.000 3888.519    0.001 __init__.py:68(backward)
                 294765   17.387    0.000 3870.193    0.013 allGraphs.py:141(transform)
                5722535 3752.574    0.001 3752.574    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               64695324   92.703    0.000 3586.082    0.000 dropout.py:57(forward)
               65874384  222.143    0.000 3532.985    0.000 linear.py:92(forward)
               64695324  335.239    0.000 3493.379    0.000 functional.py:960(dropout)
                5722535  829.300    0.000 3238.145    0.001 functional.py:53(adam)
               65874384  359.904    0.000 3222.230    0.000 functional.py:1669(linear)
               64695324 3078.916    0.000 3078.916    0.000 {built-in method dropout}
                 589530    2.042    0.000 2585.376    0.004 network.py:28(forward)
                1179060    3.679    0.000 2200.372    0.002 conv.py:422(forward)
                1179060    3.561    0.000 2195.302    0.002 conv.py:414(_conv_forward)
                1179060 2191.151    0.002 2191.151    0.002 {built-in method conv2d}
                 294765    1.359    0.000 2008.584    0.007 game.py:42(step)
                 294765    2.012    0.000 1981.798    0.007 layers.py:827(step)
                 294765   14.570    0.000 1878.502    0.006 allGraphsTrain.py:33(<listcomp>)
               29771366  915.895    0.000 1863.939    0.000 allGraphs.py:114(states)
               65874384 1700.000    0.000 1700.000    0.000 {built-in method addmm}
               21565108 1169.288    0.000 1648.124    0.000 BayesianNN.py:43(convert_data)
              265288900 1574.550    0.000 1574.550    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
              244473240  883.491    0.000 1431.188    0.000 tensor.py:933(grad)
          566007/141166   40.625    0.000 1337.914    0.009 allGraphs.py:202(recursiveExplore)
                 294765    4.077    0.000 1247.294    0.004 agent.py:112(__call__)
               66463914   79.199    0.000 1113.655    0.000 activation.py:713(forward)
                5722535  127.423    0.000 1067.189    0.000 optimizer.py:167(zero_grad)
               66463914  125.426    0.000 1034.455    0.000 functional.py:1292(leaky_relu)
                 294765   32.940    0.000 1012.568    0.003 layers.py:17(step)
               29476500   69.360    0.000  975.720    0.000 layer.py:106(move)
                 294766   58.769    0.000  964.832    0.003 layers.py:793(update)
              380814509  304.776    0.000  946.056    0.000 overrides.py:1070(has_torch_function)
               66463914  895.870    0.000  895.870    0.000 {built-in method torch._C._nn.leaky_relu}
               45683064  185.053    0.000  807.706    0.000 tensor.py:21(wrapped)
               69849480  782.508    0.000  782.508    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               65874384  760.781    0.000  760.781    0.000 {method 't' of 'torch._C._TensorBase' objects}
              486881043  289.621    0.000  755.915    0.000 {built-in method builtins.any}
               29476500  131.470    0.000  611.104    0.000 layers.py:844(check)
              300195522  561.491    0.000  561.491    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               69849480  495.727    0.000  495.727    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                 294765   35.205    0.000  475.661    0.002 allGraphsTrain.py:51(<listcomp>)
                 729520    9.521    0.000  448.366    0.001 layers.py:849(restart)
                 294765   54.489    0.000  417.838    0.001 allGraphsTrain.py:44(<listcomp>)
                5722535   10.845    0.000  378.892    0.000 loss.py:445(forward)
               43130217  369.214    0.000  369.214    0.000 {built-in method zeros}
                5722535   39.480    0.000  368.047    0.000 functional.py:2637(mse_loss)
                 729520    4.547    0.000  363.935    0.000 level.py:8(__init__)
               14732739   74.619    0.000  356.174    0.000 tensor.py:506(__rsub__)
              863045437  291.793    0.000  355.033    0.000 overrides.py:1083(<genexpr>)
               34924740  331.021    0.000  331.021    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                 729520   12.653    0.000  319.305    0.000 levels.py:151(generate)
               34924740  300.954    0.000  300.954    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                7041256  300.882    0.000  300.882    0.000 {built-in method tensor}
                3500879   50.742    0.000  294.164    0.000 level.py:41(notUsed)
              250307848  293.535    0.000  293.535    0.000 {built-in method torch._C._get_tracing_state}
               14732739  281.555    0.000  281.555    0.000 {built-in method rsub}
                5770771    7.719    0.000  273.933    0.000 game.py:38(board)
               34924740  269.896    0.000  269.896    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               30950325  268.647    0.000  268.647    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
              661223591  170.749    0.000  247.133    0.000 enum.py:646(__hash__)
                4296945   38.050    0.000  246.343    0.000 allGraphs.py:167(format)
               29476500   62.424    0.000  232.465    0.000 layers.py:838(isFree)
                 294765   93.572    0.000  225.821    0.001 agent.py:67(modify)
                5722535  223.845    0.000  223.845    0.000 {built-in method torch._C._nn.mse_loss}
               34924740  217.319    0.000  217.319    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                2063362  114.290    0.000  197.721    0.000 layer.py:175(NoRock_update)
               29476500  195.823    0.000  195.823    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               28726855  185.302    0.000  185.302    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               52220668  181.555    0.000  181.555    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               14437974  173.924    0.000  173.924    0.000 {method 'gt' of 'torch._C._TensorBase' objects}
              200206566  134.370    0.000  170.041    0.000 layer.py:103(isFree)
               75159664   42.648    0.000  168.651    0.000 {built-in method builtins.all}
                 884295    4.521    0.000  147.496    0.000 tensor.py:576(__iter__)
        901311963/901311961  138.272    0.000  145.760    0.000 {built-in method builtins.len}
                3500879    3.925    0.000  144.177    0.000 level.py:38(elementsIn)
                 884295  140.322    0.000  140.322    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               34924850   60.640    0.000  137.157    0.000 tensor.py:596(__hash__)
             1019848850  136.638    0.000  136.638    0.000 {method 'values' of 'collections.OrderedDict' objects}
              161690219  136.478    0.000  136.479    0.000 module.py:765(__getattr__)
               29476500   75.834    0.000  121.552    0.000 layers.py:207(check)
               29476500   72.695    0.000  116.564    0.000 layers.py:219(check)
               29476500   71.836    0.000  115.250    0.000 layers.py:231(check)
              229976640   87.425    0.000  106.256    0.000 layers.py:809(<genexpr>)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9668403: <Diamonds1_0.0_NN_cpu_2_2> in cluster <dcc> Done

Job <Diamonds1_0.0_NN_cpu_2_2> was submitted from host <n-62-30-8> by user <s183905> in cluster <dcc> at Wed May 19 22:59:01 2021
Job was executed on host(s) <n-62-21-98>, in queue <hpc>, as user <s183905> in cluster <dcc> at Wed May 19 22:59:03 2021
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

    CPU time :                                   35701.73 sec.
    Max Memory :                                 105 MB
    Average Memory :                             100.70 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               16279.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   35702 sec.
    Turnaround time :                            35705 sec.

The output (if any) is above this job summary.

