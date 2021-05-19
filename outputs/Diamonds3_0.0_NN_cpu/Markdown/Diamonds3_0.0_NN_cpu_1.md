/zhome/ee/d/137643/Desktop/Bachelor/project-env/lib/python3.8/site-packages/torch/cuda/__init__.py:52: UserWarning: CUDA initialization: Found no NVIDIA driver on your system. Please check that you have an NVIDIA GPU and installed a driver from http://www.nvidia.com/Download/index.aspx (Triggered internally at  /pytorch/c10/cuda/CUDAFunctions.cpp:100.)
  return torch._C._cuda_getDeviceCount() > 0

# Parameters

    Name :                      Diamonds3_0.0_NN_cpu-1
    Main :                      graphTrain
    Level :                     Levels.Causal6
    Failed actions chance :     0.0
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


      12379993673 function calls (11852081382 primitive calls) in 35700.31 seconds

##    Ordered by: cumulative time
   List reduced from 443 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35700.310 35700.310 {built-in method builtins.exec}
                      1    0.001    0.001 35700.310 35700.310 <string>:1(<module>)
                      1   27.266   27.266 35700.309 35700.309 allGraphsTrain.py:13(graphTrain)
                 106682   17.688    0.000 27504.007    0.258 allGraphsTrain.py:40(<listcomp>)
                 543295    2.631    0.000 27480.921    0.051 allGraphs.py:179(getInterventionsmodel)
        44462036/397354 2332.053    0.000 25686.672    0.065 allGraphs.py:186(recursiveBEST)
        532904285/49628215 2797.677    0.000 22883.784    0.000 module.py:715(_call_impl)
               48327607  853.140    0.000 22414.868    0.000 container.py:115(forward)
               48114243  158.641    0.000 21751.037    0.000 BayesianNN.py:18(forward)
               42450466 1332.949    0.000 20611.574    0.000 BayesianNN.py:65(predict_no_convert)
              144342729  191.850    0.000 7499.928    0.000 dropout.py:57(forward)
              144342729  715.585    0.000 7308.078    0.000 functional.py:960(dropout)
              144769457  453.998    0.000 7139.651    0.000 linear.py:92(forward)
              144769457  742.686    0.000 6507.955    0.000 functional.py:1669(linear)
              144342729 6436.726    0.000 6436.726    0.000 {built-in method dropout}
              144769457 3327.892    0.000 3327.892    0.000 {built-in method addmm}
                 106682  762.171    0.007 2839.638    0.027 allGraphs.py:156(transformNot)
                4469851   61.267    0.000 2507.806    0.001 BayesianNN.py:61(predict)
                1193926   14.062    0.000 2256.717    0.002 BayesianNN.py:57(learn)
                1193926   18.686    0.000 2150.250    0.002 BayesianNN.py:21(learn)
              144982821  156.196    0.000 2128.401    0.000 activation.py:713(forward)
              144982821  249.999    0.000 1972.204    0.000 functional.py:1292(leaky_relu)
                 106682    0.561    0.000 1852.008    0.017 agent.py:29(learn)
                 106682   11.186    0.000 1851.173    0.017 agent.py:117(_learn)
                 106682    8.208    0.000 1839.988    0.017 learner.py:42(Qlearn)
          717068/145941   54.164    0.000 1754.308    0.012 allGraphs.py:202(recursiveExplore)
              144982821 1696.859    0.000 1696.859    0.000 {built-in method torch._C._nn.leaky_relu}
              144769457 1559.172    0.000 1559.172    0.000 {method 't' of 'torch._C._TensorBase' objects}
                1300608    8.935    0.000 1336.422    0.001 tensor.py:181(backward)
                1300608    5.372    0.000 1327.487    0.001 __init__.py:68(backward)
                1300608 1297.143    0.001 1297.143    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                 213364    0.795    0.000 1270.576    0.006 network.py:28(forward)
                 426728    1.483    0.000 1104.485    0.003 conv.py:422(forward)
                 426728    1.432    0.000 1102.449    0.003 conv.py:414(_conv_forward)
                 426728 1100.797    0.003 1100.797    0.003 {built-in method conv2d}
               44742491  202.984    0.000 1015.001    0.000 tensor.py:506(__rsub__)
                1300608    8.859    0.000 1014.982    0.001 grad_mode.py:23(decorate_context)
               55944101  257.966    0.000 1005.238    0.000 tensor.py:21(wrapped)
                1300608   42.440    0.000  987.784    0.001 adam.py:55(step)
                 106682   16.422    0.000  846.608    0.008 allGraphsTrain.py:33(<listcomp>)
               10774983  404.282    0.000  830.195    0.000 allGraphs.py:114(states)
               44742491  812.017    0.000  812.017    0.000 {built-in method rsub}
              229671064  245.767    0.000  797.883    0.000 overrides.py:1070(has_torch_function)
                 106682    0.627    0.000  785.240    0.007 game.py:42(step)
                 106682    0.910    0.000  774.196    0.007 layers.py:827(step)
                1300608  192.152    0.000  762.954    0.001 functional.py:53(adam)
                 106682    4.654    0.000  684.730    0.006 allGraphs.py:141(transform)
              117350700  680.779    0.000  680.779    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 106682    1.885    0.000  648.908    0.006 agent.py:112(__call__)
              387580133  265.059    0.000  628.956    0.000 {built-in method builtins.any}
              533224331  589.882    0.000  589.882    0.000 {built-in method torch._C._get_tracing_state}
               44635809  465.281    0.000  465.281    0.000 {method 'gt' of 'torch._C._TensorBase' objects}
                5663777  332.669    0.000  458.966    0.000 BayesianNN.py:43(convert_data)
                 106682   13.395    0.000  441.687    0.004 layers.py:17(step)
               10668200   27.034    0.000  426.898    0.000 layer.py:106(move)
                 106683   22.924    0.000  330.481    0.003 layers.py:793(update)
               56119144  202.783    0.000  330.035    0.000 tensor.py:933(grad)
              624876926  257.269    0.000  317.565    0.000 overrides.py:1083(<genexpr>)
             2179944747  282.476    0.000  282.476    0.000 {method 'values' of 'collections.OrderedDict' objects}
               10668200   56.794    0.000  278.338    0.000 layers.py:844(check)
              339914408  258.593    0.000  258.593    0.000 module.py:765(__getattr__)
                1300608   27.580    0.000  245.657    0.000 optimizer.py:167(zero_grad)
              129213674  233.711    0.000  233.711    0.000 {method 'item' of 'torch._C._TensorBase' objects}
        1331334923/1331334921  213.872    0.000  216.540    0.000 {built-in method builtins.len}
               16034024  185.168    0.000  185.168    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               48540971   40.313    0.000  179.290    0.000 flatten.py:39(forward)
               59209171  176.473    0.000  176.473    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               66612401   62.156    0.000  176.404    0.000 {built-in method builtins.all}
                 106682   12.018    0.000  166.765    0.002 allGraphsTrain.py:51(<listcomp>)
                 106682   18.671    0.000  145.356    0.001 allGraphsTrain.py:44(<listcomp>)
              145643337   94.477    0.000  131.351    0.000 _VF.py:25(__getattr__)
              144769457  118.517    0.000  118.517    0.000 functional.py:1686(<listcomp>)
               16034024  116.079    0.000  116.079    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               47133681  104.824    0.000  104.824    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               10668200   25.136    0.000   99.175    0.000 layers.py:838(isFree)
                 129904    2.043    0.000   97.457    0.001 layers.py:849(restart)
              375421377   97.274    0.000   97.274    0.000 {built-in method builtins.getattr}
               11327555   96.192    0.000   96.192    0.000 {built-in method zeros}
              253628715   64.891    0.000   93.738    0.000 enum.py:646(__hash__)
               11201610   93.547    0.000   93.547    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                1300608    2.584    0.000   84.841    0.000 loss.py:445(forward)
              145836397   82.661    0.000   82.661    0.000 {method 'dim' of 'torch._C._TensorBase' objects}
                 106682   30.766    0.000   82.447    0.001 agent.py:67(modify)
                1300608    9.047    0.000   82.256    0.000 functional.py:2637(mse_loss)
               70649263   64.179    0.000   81.945    0.000 types.py:171(__get__)
                 129904    1.081    0.000   80.975    0.001 level.py:8(__init__)
                8017012   77.807    0.000   77.807    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                 853464   42.387    0.000   76.029    0.000 layer.py:175(NoRock_update)
               76735220   59.079    0.000   74.039    0.000 layer.py:103(isFree)
                1556754   72.868    0.000   72.868    0.000 {built-in method tensor}
              437996951   72.547    0.000   72.547    0.000 _jit_internal.py:750(is_scripting)
                 129904    2.847    0.000   72.137    0.001 levels.py:303(generate)
                8017012   70.647    0.000   70.647    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               10668200   42.903    0.000   68.612    0.000 layers.py:424(check)
               10668200   67.804    0.000   67.804    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                 779602   11.524    0.000   66.347    0.000 level.py:41(notUsed)
                8017012   65.384    0.000   65.384    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               50998377   21.215    0.000   63.607    0.000 layers.py:799(<genexpr>)
              167832303   62.967    0.000   62.967    0.000 tensor.py:24(<genexpr>)
                1076706    1.553    0.000   59.743    0.000 game.py:38(board)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9653100: <Diamonds3_0.0_NN_cpu_1> in cluster <dcc> Done

Job <Diamonds3_0.0_NN_cpu_1> was submitted from host <n-62-30-5> by user <s183905> in cluster <dcc> at Wed May 19 11:40:32 2021
Job was executed on host(s) <n-62-21-107>, in queue <hpc>, as user <s183905> in cluster <dcc> at Wed May 19 11:40:33 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 19 11:40:33 2021
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

    CPU time :                                   35703.15 sec.
    Max Memory :                                 110 MB
    Average Memory :                             104.39 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               16274.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   35709 sec.
    Turnaround time :                            35707 sec.

The output (if any) is above this job summary.

