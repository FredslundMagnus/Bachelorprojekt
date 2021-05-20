/zhome/ee/d/137643/Desktop/Bachelor/project-env/lib/python3.8/site-packages/torch/cuda/__init__.py:52: UserWarning: CUDA initialization: Found no NVIDIA driver on your system. Please check that you have an NVIDIA GPU and installed a driver from http://www.nvidia.com/Download/index.aspx (Triggered internally at  /pytorch/c10/cuda/CUDAFunctions.cpp:100.)
  return torch._C._cuda_getDeviceCount() > 0

# Parameters

    Name :                      Diamonds2_0.0_NN_cpu_2-0
    Main :                      graphTrain
    Level :                     Levels.Causal5
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


      12810852781 function calls (12583697020 primitive calls) in 35700.19 seconds

##    Ordered by: cumulative time
   List reduced from 443 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35700.190 35700.190 {built-in method builtins.exec}
                      1    0.001    0.001 35700.190 35700.190 <string>:1(<module>)
                      1   63.549   63.549 35700.189 35700.189 allGraphsTrain.py:13(graphTrain)
        239521071/26108061 1269.742    0.000 13209.787    0.001 module.py:715(_call_impl)
               21341301  382.009    0.000 12673.012    0.001 container.py:115(forward)
                 249006   54.268    0.000 11201.340    0.045 allGraphsTrain.py:40(<listcomp>)
                3402113   15.401    0.000 11112.048    0.003 allGraphs.py:179(getInterventionsmodel)
               20843289   76.793    0.000 9541.796    0.000 BayesianNN.py:18(forward)
               16325535  213.776    0.000 9230.520    0.001 BayesianNN.py:61(predict)
                 249006 2202.308    0.009 8986.756    0.036 allGraphs.py:156(transformNot)
        16331097/3234557  887.864    0.000 8832.089    0.003 allGraphs.py:186(recursiveBEST)
                4517754   53.738    0.000 8623.876    0.002 BayesianNN.py:57(learn)
                4517754   70.629    0.000 8116.108    0.002 BayesianNN.py:21(learn)
                 249006    1.757    0.000 4651.147    0.019 agent.py:29(learn)
                 249006  140.001    0.001 4648.695    0.019 agent.py:117(_learn)
                 249006   22.186    0.000 4508.694    0.018 learner.py:42(Qlearn)
                4766760   33.207    0.000 3680.772    0.001 grad_mode.py:23(decorate_context)
                4766760   32.598    0.000 3674.630    0.001 tensor.py:181(backward)
                4766760   21.145    0.000 3642.032    0.001 __init__.py:68(backward)
                4766760  153.302    0.000 3583.389    0.001 adam.py:55(step)
                4766760 3530.355    0.001 3530.355    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                 498012    2.399    0.000 3418.996    0.007 network.py:28(forward)
               62529867   89.569    0.000 3320.819    0.000 dropout.py:57(forward)
                 249006   18.613    0.000 3308.407    0.013 allGraphs.py:141(transform)
               63525891  199.552    0.000 3248.160    0.000 linear.py:92(forward)
               62529867  310.159    0.000 3231.250    0.000 functional.py:960(dropout)
                 996024    4.003    0.000 3063.682    0.003 conv.py:422(forward)
                 996024    4.428    0.000 3058.255    0.003 conv.py:414(_conv_forward)
                 996024 3053.282    0.003 3053.282    0.003 {built-in method conv2d}
               63525891  336.142    0.000 2967.639    0.000 functional.py:1669(linear)
               62529867 2850.212    0.000 2850.212    0.000 {built-in method dropout}
                4766760  715.320    0.000 2801.728    0.001 functional.py:53(adam)
                 249006   17.834    0.000 2426.647    0.010 allGraphsTrain.py:33(<listcomp>)
               25149707 1163.806    0.000 2408.824    0.000 allGraphs.py:114(states)
          813355/167556   63.325    0.000 2025.280    0.012 allGraphs.py:202(recursiveExplore)
               20843289 1513.911    0.000 1995.090    0.000 BayesianNN.py:43(convert_data)
              323708400 1994.123    0.000 1994.123    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 249006    1.801    0.000 1987.225    0.008 game.py:42(step)
                 249006    2.504    0.000 1951.543    0.008 layers.py:827(step)
                 249006    5.195    0.000 1814.153    0.007 agent.py:112(__call__)
               63525891 1570.752    0.000 1570.752    0.000 {built-in method addmm}
                 249006   32.539    0.000 1124.682    0.005 layers.py:17(step)
              203690064  667.078    0.000 1120.331    0.000 tensor.py:933(grad)
               24900600   63.178    0.000 1088.884    0.000 layer.py:106(move)
               64023903   68.587    0.000 1028.137    0.000 activation.py:713(forward)
               64023903  116.063    0.000  959.551    0.000 functional.py:1292(leaky_relu)
                4766760   95.860    0.000  840.076    0.000 optimizer.py:167(zero_grad)
               64023903  832.191    0.000  832.191    0.000 {built-in method torch._C._nn.leaky_relu}
                 249007   51.800    0.000  820.720    0.003 layers.py:793(update)
              326111386  256.803    0.000  804.664    0.000 overrides.py:1070(has_torch_function)
               24900600  140.867    0.000  708.488    0.000 layers.py:844(check)
               63525891  690.156    0.000  690.156    0.000 {method 't' of 'torch._C._TensorBase' objects}
              423687479  255.283    0.000  683.009    0.000 {built-in method builtins.any}
               58197144  678.978    0.000  678.978    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               40136975  154.631    0.000  665.015    0.000 tensor.py:21(wrapped)
              353128746  650.289    0.000  650.289    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               58197144  426.611    0.000  426.611    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                 249006   27.572    0.000  374.497    0.002 allGraphsTrain.py:51(<listcomp>)
                 249006   44.722    0.000  355.529    0.001 allGraphsTrain.py:44(<listcomp>)
               41686579  346.639    0.000  346.639    0.000 {built-in method zeros}
                5725549  324.601    0.000  324.601    0.000 {built-in method tensor}
               13991345   65.522    0.000  322.446    0.000 tensor.py:506(__rsub__)
                4766760    9.060    0.000  314.669    0.000 loss.py:445(forward)
              745545412  253.571    0.000  309.549    0.000 overrides.py:1083(<genexpr>)
                 384018    6.959    0.000  308.388    0.001 layers.py:849(restart)
                4766760   34.460    0.000  305.609    0.000 functional.py:2637(mse_loss)
                4647144    6.932    0.000  297.209    0.000 game.py:38(board)
               29098572  289.782    0.000  289.782    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               29098572  265.889    0.000  265.889    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              240268089  261.363    0.000  261.363    0.000 {built-in method torch._C._get_tracing_state}
               24900600   64.961    0.000  260.824    0.000 layers.py:838(isFree)
                 384018    3.197    0.000  258.257    0.001 level.py:8(__init__)
               13991345  256.924    0.000  256.924    0.000 {built-in method rsub}
                3402113   30.931    0.000  237.782    0.000 allGraphs.py:167(format)
              644921721  162.022    0.000  237.488    0.000 enum.py:646(__hash__)
                 384018    9.006    0.000  231.676    0.001 levels.py:249(generate)
               29098572  228.573    0.000  228.573    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                2241063  120.505    0.000  213.934    0.000 layer.py:175(NoRock_update)
                2496789   36.348    0.000  213.370    0.000 level.py:41(notUsed)
               26145630  209.380    0.000  209.380    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                 249006   77.893    0.000  205.409    0.001 agent.py:67(modify)
              213270775  159.824    0.000  195.863    0.000 layer.py:103(isFree)
               29098572  183.596    0.000  183.596    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                4766760  183.477    0.000  183.477    0.000 {built-in method torch._C._nn.mse_loss}
               27399659  168.099    0.000  168.099    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               24900600  166.432    0.000  166.432    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               46739913  161.387    0.000  161.387    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                 747018    4.764    0.000  155.210    0.000 tensor.py:576(__iter__)
               13742339  151.070    0.000  151.070    0.000 {method 'gt' of 'torch._C._TensorBase' objects}
                 747018  147.897    0.000  147.897    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               65037675   41.459    0.000  140.410    0.000 {built-in method builtins.all}
        876687414/876687412  126.607    0.000  132.750    0.000 {built-in method builtins.len}
              979425585  130.285    0.000  130.285    0.000 {method 'values' of 'collections.OrderedDict' objects}
              154903698  125.660    0.000  125.661    0.000 module.py:765(__getattr__)
              140551839   93.322    0.000  119.875    0.000 types.py:171(__get__)
              245166820   95.255    0.000  114.003    0.000 layers.py:809(<genexpr>)
               29098682   50.372    0.000  113.052    0.000 tensor.py:596(__hash__)
               24900600   68.806    0.000  107.804    0.000 layers.py:337(check)
               24900600   66.616    0.000  103.265    0.000 layers.py:387(check)
                2496789    2.772    0.000  102.910    0.000 level.py:38(elementsIn)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9668404: <Diamonds2_0.0_NN_cpu_2_0> in cluster <dcc> Done

Job <Diamonds2_0.0_NN_cpu_2_0> was submitted from host <n-62-30-8> by user <s183905> in cluster <dcc> at Wed May 19 22:59:01 2021
Job was executed on host(s) <n-62-21-108>, in queue <hpc>, as user <s183905> in cluster <dcc> at Wed May 19 22:59:03 2021
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

    CPU time :                                   35697.08 sec.
    Max Memory :                                 108 MB
    Average Memory :                             101.67 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               16276.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   35702 sec.
    Turnaround time :                            35704 sec.

The output (if any) is above this job summary.

