/zhome/ee/d/137643/Desktop/Bachelor/project-env/lib/python3.8/site-packages/torch/cuda/__init__.py:52: UserWarning: CUDA initialization: Found no NVIDIA driver on your system. Please check that you have an NVIDIA GPU and installed a driver from http://www.nvidia.com/Download/index.aspx (Triggered internally at  /pytorch/c10/cuda/CUDAFunctions.cpp:100.)
  return torch._C._cuda_getDeviceCount() > 0

# Parameters

    Name :                      Diamonds4_0.0_NN_cpu-2
    Main :                      graphTrain
    Level :                     Levels.Causal7
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
    Num :                       2
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      12903048990 function calls (12376693209 primitive calls) in 35700.96 seconds

##    Ordered by: cumulative time
   List reduced from 443 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35700.961 35700.961 {built-in method builtins.exec}
                      1    0.001    0.001 35700.961 35700.961 <string>:1(<module>)
                      1   38.211   38.211 35700.960 35700.960 allGraphsTrain.py:13(graphTrain)
                 135275   26.112    0.000 26291.938    0.194 allGraphsTrain.py:40(<listcomp>)
                 986716    5.471    0.000 26255.566    0.027 allGraphs.py:179(getInterventionsmodel)
        45246854/858357 2255.458    0.000 25049.905    0.029 allGraphs.py:186(recursiveBEST)
        531577182/49974712 2662.507    0.000 22163.090    0.000 module.py:715(_call_impl)
               48160247  858.446    0.000 21659.563    0.000 container.py:115(forward)
               47889697  149.298    0.000 20956.411    0.000 BayesianNN.py:18(forward)
               41890818 1233.410    0.000 19590.053    0.000 BayesianNN.py:65(predict_no_convert)
              143669091  226.164    0.000 7298.397    0.000 dropout.py:57(forward)
              143669091  673.655    0.000 7072.233    0.000 functional.py:960(dropout)
              144210191  419.611    0.000 6833.682    0.000 linear.py:92(forward)
              143669091 6258.292    0.000 6258.292    0.000 {built-in method dropout}
              144210191  692.764    0.000 6251.641    0.000 functional.py:1669(linear)
              144210191 3259.733    0.000 3259.733    0.000 {built-in method addmm}
                 135275  779.849    0.006 3243.837    0.024 allGraphs.py:156(transformNot)
                1679190   19.571    0.000 3081.637    0.002 BayesianNN.py:57(learn)
                1679190   25.586    0.000 2925.069    0.002 BayesianNN.py:21(learn)
                4319689   55.854    0.000 2381.906    0.001 BayesianNN.py:61(predict)
              144480741  134.387    0.000 2104.928    0.000 activation.py:713(forward)
                 135275    0.955    0.000 2074.957    0.015 agent.py:29(learn)
                 135275   18.858    0.000 2073.638    0.015 agent.py:117(_learn)
                 135275   12.542    0.000 2054.780    0.015 learner.py:42(Qlearn)
              144480741  231.319    0.000 1970.541    0.000 functional.py:1292(leaky_relu)
              144480741 1715.660    0.000 1715.660    0.000 {built-in method torch._C._nn.leaky_relu}
                1814465   13.152    0.000 1591.587    0.001 tensor.py:181(backward)
                1814465    8.027    0.000 1578.435    0.001 __init__.py:68(backward)
                1814465 1535.173    0.001 1535.173    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
              144210191 1523.735    0.000 1523.735    0.000 {method 't' of 'torch._C._TensorBase' objects}
                1814465   13.796    0.000 1372.890    0.001 grad_mode.py:23(decorate_context)
                1814465   56.485    0.000 1334.158    0.001 adam.py:55(step)
                 270550    1.197    0.000 1285.731    0.005 network.py:28(forward)
                 135275    7.384    0.000 1158.477    0.009 allGraphs.py:141(transform)
          492761/128359   35.079    0.000 1110.506    0.009 allGraphs.py:202(recursiveExplore)
                 541100    2.086    0.000 1073.321    0.002 conv.py:422(forward)
                 541100    2.467    0.000 1070.533    0.002 conv.py:414(_conv_forward)
                 541100 1067.783    0.002 1067.783    0.002 {built-in method conv2d}
                1814465  271.379    0.000 1049.911    0.001 functional.py:53(adam)
               59092049  259.391    0.000 1033.400    0.000 tensor.py:21(wrapped)
               44888174  199.339    0.000 1006.335    0.000 tensor.py:506(__rsub__)
                 135275   21.991    0.000  808.269    0.006 allGraphsTrain.py:33(<listcomp>)
               44888174  806.997    0.000  806.997    0.000 {built-in method rsub}
                 135275    0.922    0.000  791.849    0.006 game.py:42(step)
               13662876  373.485    0.000  786.285    0.000 allGraphs.py:114(states)
                 135275    1.345    0.000  772.755    0.006 layers.py:827(step)
              259930995  235.127    0.000  760.936    0.000 overrides.py:1070(has_torch_function)
              121747900  691.914    0.000  691.914    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 135275    2.982    0.000  653.788    0.005 agent.py:112(__call__)
              421099208  248.754    0.000  589.517    0.000 {built-in method builtins.any}
              531983007  549.257    0.000  549.257    0.000 {built-in method torch._C._get_tracing_state}
                5998879  344.655    0.000  490.070    0.000 BayesianNN.py:43(convert_data)
               44752899  474.569    0.000  474.569    0.000 {method 'gt' of 'torch._C._TensorBase' objects}
                 135275   16.431    0.000  442.900    0.003 layers.py:17(step)
               13527500   31.220    0.000  424.964    0.000 layer.py:106(move)
               78101440  252.959    0.000  409.437    0.000 tensor.py:933(grad)
                 135276   25.812    0.000  326.592    0.002 layers.py:793(update)
                1814465   34.472    0.000  308.145    0.000 optimizer.py:167(zero_grad)
              690534095  240.252    0.000  295.271    0.000 overrides.py:1083(<genexpr>)
             2174468975  270.617    0.000  270.617    0.000 {method 'values' of 'collections.OrderedDict' objects}
               13527500   53.263    0.000  253.714    0.000 layers.py:844(check)
               22314680  251.540    0.000  251.540    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              339342590  238.322    0.000  238.323    0.000 module.py:765(__getattr__)
              136955670  237.370    0.000  237.370    0.000 {method 'item' of 'torch._C._TensorBase' objects}
        1348330975/1348330973  209.189    0.000  213.868    0.000 {built-in method builtins.len}
                 135275   14.511    0.000  190.485    0.001 allGraphsTrain.py:51(<listcomp>)
               61958297  183.927    0.000  183.927    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                 135275   23.103    0.000  175.797    0.001 allGraphsTrain.py:44(<listcomp>)
               48430797   34.028    0.000  174.101    0.000 flatten.py:39(forward)
               22314680  155.615    0.000  155.615    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               72619649   55.961    0.000  140.239    0.000 {built-in method builtins.all}
                2263717  132.749    0.000  132.749    0.000 {built-in method tensor}
                1814465    3.925    0.000  122.018    0.000 loss.py:445(forward)
                1814465   13.124    0.000  118.092    0.000 functional.py:2637(mse_loss)
              145483556   82.292    0.000  117.742    0.000 _VF.py:25(__getattr__)
                1663092    2.837    0.000  117.710    0.000 game.py:38(board)
               13527500   26.474    0.000  113.279    0.000 layers.py:838(isFree)
                 135275   42.318    0.000  112.724    0.001 agent.py:67(modify)
               11997759  112.600    0.000  112.600    0.000 {built-in method zeros}
                 198508    2.901    0.000  111.409    0.001 layers.py:849(restart)
               11157340  109.547    0.000  109.547    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              144210191  109.215    0.000  109.215    0.000 functional.py:1686(<listcomp>)
               14203875  108.821    0.000  108.821    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               11157340   98.762    0.000   98.762    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               46481057   98.349    0.000   98.349    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
              405533824   90.577    0.000   90.577    0.000 {built-in method builtins.getattr}
                 198508    1.520    0.000   89.985    0.000 level.py:8(__init__)
               11157340   88.835    0.000   88.835    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                 986716   16.446    0.000   88.785    0.000 allGraphs.py:167(format)
              261374430   60.041    0.000   87.320    0.000 enum.py:646(__hash__)
               89551211   71.374    0.000   86.805    0.000 layer.py:103(isFree)
                 946932   48.750    0.000   85.508    0.000 layer.py:175(NoRock_update)
               13527500   82.302    0.000   82.302    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               72603860   65.224    0.000   81.621    0.000 types.py:171(__get__)
                 198508    3.276    0.000   77.555    0.000 levels.py:456(generate)
                 405825    2.504    0.000   74.058    0.000 tensor.py:576(__iter__)
              145563061   72.226    0.000   72.226    0.000 {method 'dim' of 'torch._C._TensorBase' objects}
                 953605   12.751    0.000   71.053    0.000 level.py:41(notUsed)
                1814465   70.663    0.000   70.663    0.000 {built-in method torch._C._nn.mse_loss}
               11157340   70.045    0.000   70.045    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9653104: <Diamonds4_0.0_NN_cpu_2> in cluster <dcc> Done

Job <Diamonds4_0.0_NN_cpu_2> was submitted from host <n-62-30-5> by user <s183905> in cluster <dcc> at Wed May 19 11:40:33 2021
Job was executed on host(s) <n-62-28-30>, in queue <hpc>, as user <s183905> in cluster <dcc> at Wed May 19 11:40:35 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 19 11:40:35 2021
Terminated at Wed May 19 21:35:41 2021
Results reported at Wed May 19 21:35:41 2021

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

    CPU time :                                   35700.89 sec.
    Max Memory :                                 106 MB
    Average Memory :                             99.83 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               16278.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   35706 sec.
    Turnaround time :                            35708 sec.

The output (if any) is above this job summary.

