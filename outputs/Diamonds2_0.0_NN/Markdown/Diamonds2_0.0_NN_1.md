
# Parameters

    Name :                      Diamonds2_0.0_NN-1
    Main :                      graphTrain
    Level :                     Levels.Causal5
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


      12074798258 function calls (11561110547 primitive calls) in 35717.18 seconds

##    Ordered by: cumulative time
   List reduced from 475 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35717.182 35717.182 {built-in method builtins.exec}
                      1    0.001    0.001 35717.182 35717.182 <string>:1(<module>)
                      1   25.202   25.202 35717.180 35717.180 allGraphsTrain.py:13(graphTrain)
                 100136  124.704    0.001 26147.028    0.261 allGraphsTrain.py:40(<listcomp>)
                 547484    2.879    0.000 26018.025    0.048 allGraphs.py:179(getInterventionsmodel)
        42992791/382336 3607.283    0.000 23807.727    0.062 allGraphs.py:186(recursiveBEST)
               46844495  109.214    0.000 17497.980    0.000 BayesianNN.py:18(forward)
        518680758/48233088 1725.760    0.000 17487.449    0.000 module.py:715(_call_impl)
               41134446 1921.081    0.000 17373.310    0.000 BayesianNN.py:65(predict_no_convert)
               47044767  571.594    0.000 17158.281    0.000 container.py:115(forward)
              140934029  250.143    0.000 7697.063    0.000 linear.py:92(forward)
              140934029  462.466    0.000 7339.607    0.000 functional.py:1669(linear)
              140934029 5121.327    0.000 5121.327    0.000 {built-in method addmm}
                 100136 1508.128    0.015 4949.388    0.049 allGraphs.py:156(transformNot)
              140533485  101.830    0.000 3970.094    0.000 dropout.py:57(forward)
              140533485  413.066    0.000 3868.264    0.000 functional.py:960(dropout)
              140533485 3333.501    0.000 3333.501    0.000 {built-in method dropout}
                4621864   59.819    0.000 2848.134    0.001 BayesianNN.py:61(predict)
              141134301   91.763    0.000 2538.267    0.000 activation.py:713(forward)
              141134301  153.933    0.000 2446.504    0.000 functional.py:1292(leaky_relu)
                1088185   12.435    0.000 2374.814    0.002 BayesianNN.py:57(learn)
              141134301 2277.106    0.000 2277.106    0.000 {built-in method torch._C._nn.leaky_relu}
                 100136    2.696    0.000 2171.310    0.022 allGraphsTrain.py:33(<listcomp>)
               10113837  557.484    0.000 2168.711    0.000 allGraphs.py:114(states)
          794319/165148   80.118    0.000 2135.788    0.013 allGraphs.py:202(recursiveExplore)
                1088185   12.659    0.000 2124.615    0.002 BayesianNN.py:21(learn)
              141279985 1919.537    0.000 1919.537    0.000 {method 'item' of 'torch._C._TensorBase' objects}
              130177400 1702.722    0.000 1702.722    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                5710049 1041.414    0.000 1245.489    0.000 BayesianNN.py:43(convert_data)
              140934029 1214.483    0.000 1214.483    0.000 {method 't' of 'torch._C._TensorBase' objects}
               53854042  175.007    0.000 1157.094    0.000 tensor.py:21(wrapped)
                1188321    6.212    0.000 1026.509    0.001 grad_mode.py:23(decorate_context)
                1188321   28.170    0.000 1008.446    0.001 adam.py:55(step)
               43339762  137.907    0.000  983.222    0.000 tensor.py:506(__rsub__)
                1188321  182.835    0.000  867.847    0.001 functional.py:53(adam)
               43339762  845.315    0.000  845.315    0.000 {built-in method rsub}
                 100136    3.695    0.000  822.411    0.008 allGraphs.py:141(transform)
               43239626  706.854    0.000  706.854    0.000 {method 'gt' of 'torch._C._TensorBase' objects}
                1188321    6.554    0.000  535.003    0.000 tensor.py:181(backward)
                1188321    3.390    0.000  528.449    0.000 __init__.py:68(backward)
                1188321  495.436    0.000  495.436    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                 100136    0.358    0.000  480.119    0.005 game.py:42(step)
              218979109  142.567    0.000  477.795    0.000 overrides.py:1070(has_torch_function)
                 100136    0.500    0.000  456.275    0.005 layers.py:827(step)
              518981166  386.526    0.000  386.526    0.000 {built-in method torch._C._get_tracing_state}
              372208704  164.432    0.000  386.129    0.000 {built-in method builtins.any}
                 100136   26.311    0.000  357.594    0.004 allGraphsTrain.py:44(<listcomp>)
                 100136    6.926    0.000  280.130    0.003 layers.py:17(step)
               10013600   15.407    0.000  272.394    0.000 layer.py:106(move)
                 100136    0.315    0.000  265.629    0.003 agent.py:29(learn)
                 100136    2.046    0.000  265.110    0.003 agent.py:117(_learn)
                 100136    7.717    0.000  263.064    0.003 learner.py:42(Qlearn)
               51311446  132.131    0.000  209.156    0.000 tensor.py:933(grad)
                 100136    9.160    0.000  207.584    0.002 allGraphsTrain.py:51(<listcomp>)
                1188321   19.197    0.000  203.861    0.000 optimizer.py:167(zero_grad)
              598295573  154.697    0.000  191.206    0.000 overrides.py:1083(<genexpr>)
               57258639  185.245    0.000  185.245    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               10013600   36.871    0.000  183.405    0.000 layers.py:844(check)
               14660396  181.900    0.000  181.900    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
             2121767799  175.442    0.000  175.442    0.000 {method 'values' of 'collections.OrderedDict' objects}
                 100137   13.022    0.000  175.179    0.002 layers.py:793(update)
               11420099  171.067    0.000  171.067    0.000 {built-in method zeros}
              330802603  169.566    0.000  169.567    0.000 module.py:765(__getattr__)
               47245039   31.182    0.000  169.277    0.000 flatten.py:39(forward)
               10514280  161.043    0.000  161.043    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               14660396  154.421    0.000  154.421    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
        1301003332/1301003330  151.255    0.000  152.960    0.000 {built-in method builtins.len}
               10013600  148.045    0.000  148.045    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                1500767  147.413    0.000  147.413    0.000 {built-in method tensor}
                1048165    1.051    0.000  127.579    0.000 game.py:38(board)
              141721806   78.634    0.000  107.849    0.000 _VF.py:25(__getattr__)
                 100136   55.012    0.001  103.972    0.001 agent.py:67(modify)
                7330198   99.373    0.000   99.373    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               63867742   38.539    0.000   92.458    0.000 {built-in method builtins.all}
               45956582   90.707    0.000   90.707    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                7330198   89.916    0.000   89.916    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                 200272    0.503    0.000   87.265    0.000 network.py:28(forward)
                7330198   82.811    0.000   82.811    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                7330198   74.306    0.000   74.306    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              140934029   74.099    0.000   74.099    0.000 functional.py:1686(<listcomp>)
               80583422   55.615    0.000   72.743    0.000 types.py:171(__get__)
                 547484    4.370    0.000   71.393    0.000 allGraphs.py:167(format)
              360805752   65.785    0.000   65.785    0.000 {built-in method builtins.getattr}
                2716956   65.161    0.000   65.161    0.000 {built-in method cat}
                1188321    1.379    0.000   63.705    0.000 loss.py:445(forward)
                1188321    5.761    0.000   62.326    0.000 functional.py:2637(mse_loss)
               10013600   17.021    0.000   60.136    0.000 layers.py:838(isFree)
              238241749   41.347    0.000   59.703    0.000 enum.py:646(__hash__)
                7330198   58.966    0.000   58.966    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              141935509   55.118    0.000   55.118    0.000 {method 'dim' of 'torch._C._TensorBase' objects}
                 100136    1.260    0.000   52.437    0.001 agent.py:112(__call__)
                  94777    0.885    0.000   47.624    0.001 layers.py:849(restart)
                8356984   46.733    0.000   46.733    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              426166898   44.799    0.000   44.799    0.000 _jit_internal.py:750(is_scripting)
                 901233   23.974    0.000   44.431    0.000 layer.py:175(NoRock_update)
               47044767   30.373    0.000   43.754    0.000 container.py:107(__iter__)
               88474252   33.729    0.000   43.116    0.000 layer.py:103(isFree)
                1188321   41.447    0.000   41.447    0.000 {built-in method torch._C._nn.mse_loss}
                  94777    0.447    0.000   40.213    0.000 level.py:8(__init__)
              161562126   38.283    0.000   38.283    0.000 tensor.py:24(<genexpr>)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9651547: <Diamonds2_0.0_NN_1> in cluster <dcc> Done

Job <Diamonds2_0.0_NN_1> was submitted from host <n-62-27-18> by user <s183905> in cluster <dcc> at Tue May 18 21:12:59 2021
Job was executed on host(s) <n-62-20-3>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Wed May 19 07:08:30 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 19 07:08:30 2021
Terminated at Wed May 19 17:04:01 2021
Results reported at Wed May 19 17:04:01 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=16G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 1440
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $MYARGS


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   35617.58 sec.
    Max Memory :                                 2064 MB
    Average Memory :                             2056.39 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14320.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35842 sec.
    Turnaround time :                            71462 sec.

The output (if any) is above this job summary.

