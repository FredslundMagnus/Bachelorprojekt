/zhome/ee/d/137643/Desktop/Bachelor/project-env/lib/python3.8/site-packages/torch/cuda/__init__.py:52: UserWarning: CUDA initialization: Found no NVIDIA driver on your system. Please check that you have an NVIDIA GPU and installed a driver from http://www.nvidia.com/Download/index.aspx (Triggered internally at  /pytorch/c10/cuda/CUDAFunctions.cpp:100.)
  return torch._C._cuda_getDeviceCount() > 0

# Parameters

    Name :                      Diamonds1_0.0_NN_cpu-2
    Main :                      graphTrain
    Level :                     Levels.Causal2
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


      11992652004 function calls (11497994138 primitive calls) in 35700.70 seconds

##    Ordered by: cumulative time
   List reduced from 440 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35700.704 35700.704 {built-in method builtins.exec}
                      1    0.001    0.001 35700.704 35700.704 <string>:1(<module>)
                      1   36.871   36.871 35700.703 35700.703 allGraphsTrain.py:13(graphTrain)
                 122652   23.452    0.000 26600.177    0.217 allGraphsTrain.py:40(<listcomp>)
                 816222    4.416    0.000 26568.568    0.033 allGraphs.py:179(getInterventionsmodel)
        42194545/674468 2318.983    0.000 25151.197    0.037 allGraphs.py:186(recursiveBEST)
        499496008/46782198 2651.718    0.000 22184.293    0.000 module.py:715(_call_impl)
               45271381  814.589    0.000 21697.678    0.000 container.py:115(forward)
               45026077  147.116    0.000 20966.942    0.000 BayesianNN.py:18(forward)
               39371682 1276.827    0.000 19674.197    0.000 BayesianNN.py:65(predict_no_convert)
              135078231  174.536    0.000 7276.897    0.000 dropout.py:57(forward)
              135078231  685.386    0.000 7102.361    0.000 functional.py:960(dropout)
              135568839  422.795    0.000 6898.549    0.000 linear.py:92(forward)
              135568839  713.458    0.000 6301.480    0.000 functional.py:1669(linear)
              135078231 6246.540    0.000 6246.540    0.000 {built-in method dropout}
              135568839 3272.291    0.000 3272.291    0.000 {built-in method addmm}
                 122652  780.327    0.006 3009.348    0.025 allGraphs.py:156(transformNot)
                1388165   17.831    0.000 2762.978    0.002 BayesianNN.py:57(learn)
                1388165   22.149    0.000 2630.738    0.002 BayesianNN.py:21(learn)
                4266230   57.961    0.000 2463.707    0.001 BayesianNN.py:61(predict)
              135814143  141.678    0.000 2089.143    0.000 activation.py:713(forward)
                 122652    0.808    0.000 2015.309    0.016 agent.py:29(learn)
                 122652   17.614    0.000 2014.162    0.016 agent.py:117(_learn)
                 122652   10.693    0.000 1996.548    0.016 learner.py:42(Qlearn)
              135814143  234.644    0.000 1947.465    0.000 functional.py:1292(leaky_relu)
              135814143 1687.362    0.000 1687.362    0.000 {built-in method torch._C._nn.leaky_relu}
                1510817   11.796    0.000 1526.213    0.001 tensor.py:181(backward)
              135568839 1518.763    0.000 1518.763    0.000 {method 't' of 'torch._C._TensorBase' objects}
                1510817    6.981    0.000 1514.417    0.001 __init__.py:68(backward)
                1510817 1477.002    0.001 1477.002    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
          565321/141754   42.572    0.000 1341.886    0.009 allGraphs.py:202(recursiveExplore)
                 245304    1.071    0.000 1320.104    0.005 network.py:28(forward)
                1510817   11.636    0.000 1263.075    0.001 grad_mode.py:23(decorate_context)
                1510817   51.576    0.000 1229.679    0.001 adam.py:55(step)
                 490608    1.784    0.000 1112.301    0.002 conv.py:422(forward)
                 490608    1.982    0.000 1109.881    0.002 conv.py:414(_conv_forward)
                 490608 1107.607    0.002 1107.607    0.002 {built-in method conv2d}
               54944756  275.414    0.000 1080.200    0.000 tensor.py:21(wrapped)
                 122652    6.407    0.000 1069.867    0.009 allGraphs.py:141(transform)
               42066296  213.134    0.000 1053.927    0.000 tensor.py:506(__rsub__)
                1510817  247.477    0.000  969.529    0.001 functional.py:53(adam)
               42066296  840.793    0.000  840.793    0.000 {built-in method rsub}
                 122652   24.558    0.000  819.412    0.007 allGraphsTrain.py:33(<listcomp>)
                 122652    0.822    0.000  813.391    0.007 game.py:42(step)
                 122652    1.156    0.000  798.476    0.007 layers.py:827(step)
               12387953  378.025    0.000  794.862    0.000 allGraphs.py:114(states)
              233905157  240.933    0.000  764.977    0.000 overrides.py:1070(has_torch_function)
                 122652    2.569    0.000  707.933    0.006 agent.py:112(__call__)
              110387200  693.908    0.000  693.908    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
              384553320  254.740    0.000  600.884    0.000 {built-in method builtins.any}
              499863964  552.106    0.000  552.106    0.000 {built-in method torch._C._get_tracing_state}
               41943644  496.468    0.000  496.468    0.000 {method 'gt' of 'torch._C._TensorBase' objects}
                5654395  335.498    0.000  472.659    0.000 BayesianNN.py:43(convert_data)
                 122652   15.841    0.000  441.304    0.004 layers.py:17(step)
               12265200   29.764    0.000  423.966    0.000 layer.py:106(move)
               65171502  233.129    0.000  380.267    0.000 tensor.py:933(grad)
                 122653   25.444    0.000  354.387    0.003 layers.py:793(update)
              627233653  244.511    0.000  300.277    0.000 overrides.py:1083(<genexpr>)
                1510817   33.992    0.000  292.616    0.000 optimizer.py:167(zero_grad)
             2043255413  268.737    0.000  268.737    0.000 {method 'values' of 'collections.OrderedDict' objects}
               12265200   54.669    0.000  259.597    0.000 layers.py:844(check)
              318778989  255.290    0.000  255.290    0.000 module.py:765(__getattr__)
              124041541  236.239    0.000  236.239    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               18620412  235.945    0.000  235.945    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
        1261523176/1261523174  220.057    0.000  223.362    0.000 {built-in method builtins.len}
                 122652   14.224    0.000  201.453    0.002 allGraphsTrain.py:51(<listcomp>)
               45516685   55.366    0.000  189.138    0.000 flatten.py:39(forward)
               57781885  178.709    0.000  178.709    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                 122652   22.378    0.000  172.335    0.001 allGraphsTrain.py:44(<listcomp>)
               67210056   61.119    0.000  152.422    0.000 {built-in method builtins.all}
              136589048   89.350    0.000  147.757    0.000 _VF.py:25(__getattr__)
               18620412  145.699    0.000  145.699    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                 207610    3.200    0.000  130.607    0.001 layers.py:849(restart)
               12878460  114.880    0.000  114.880    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
              370607554  114.287    0.000  114.287    0.000 {built-in method builtins.getattr}
                1976646  108.986    0.000  108.986    0.000 {built-in method tensor}
               12265200   25.492    0.000  108.268    0.000 layers.py:838(isFree)
              135568839  108.187    0.000  108.187    0.000 functional.py:1686(<listcomp>)
               11308791  106.450    0.000  106.450    0.000 {built-in method zeros}
                 207610    1.560    0.000  105.543    0.001 level.py:8(__init__)
                1510817    3.069    0.000  104.214    0.000 loss.py:445(forward)
                9310206  103.520    0.000  103.520    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                 122652   39.268    0.000  103.448    0.001 agent.py:67(modify)
                1510817   11.349    0.000  101.145    0.000 functional.py:2637(mse_loss)
               43883216   97.172    0.000   97.172    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                1429483    2.409    0.000   94.279    0.000 game.py:38(board)
                9310206   92.093    0.000   92.093    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                 207610    3.793    0.000   91.946    0.000 levels.py:151(generate)
              238263657   61.625    0.000   89.877    0.000 enum.py:646(__hash__)
                 858571   48.935    0.000   85.950    0.000 layer.py:175(NoRock_update)
                 996780   14.953    0.000   84.456    0.000 level.py:41(notUsed)
               80514276   68.140    0.000   82.776    0.000 layer.py:103(isFree)
               12265200   81.266    0.000   81.266    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               66305953   63.436    0.000   79.724    0.000 types.py:171(__get__)
                9310206   79.297    0.000   79.297    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              136795479   72.508    0.000   72.508    0.000 {method 'dim' of 'torch._C._TensorBase' objects}
                 367956    2.284    0.000   71.700    0.000 tensor.py:576(__iter__)
                 816222   14.990    0.000   70.601    0.000 allGraphs.py:167(format)
              410993784   70.105    0.000   70.105    0.000 _jit_internal.py:750(is_scripting)
                 367956   68.180    0.000   68.180    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9653095: <Diamonds1_0.0_NN_cpu_2> in cluster <dcc> Done

Job <Diamonds1_0.0_NN_cpu_2> was submitted from host <n-62-30-5> by user <s183905> in cluster <dcc> at Wed May 19 11:40:32 2021
Job was executed on host(s) <n-62-21-107>, in queue <hpc>, as user <s183905> in cluster <dcc> at Wed May 19 11:40:32 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 19 11:40:32 2021
Terminated at Wed May 19 21:35:40 2021
Results reported at Wed May 19 21:35:40 2021

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

    CPU time :                                   35702.84 sec.
    Max Memory :                                 106 MB
    Average Memory :                             99.71 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               16278.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   35709 sec.
    Turnaround time :                            35708 sec.

The output (if any) is above this job summary.

