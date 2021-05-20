
# Parameters

    Name :                      Diamonds3_0.5_NN-1
    Main :                      graphTrain
    Level :                     Levels.Causal6
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
    Num :                       1
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      12690866884 function calls (12049530548 primitive calls) in 35708.36 seconds

##    Ordered by: cumulative time
   List reduced from 484 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35708.362 35708.362 {built-in method builtins.exec}
                      1    0.001    0.001 35708.362 35708.362 <string>:1(<module>)
                      1   31.760   31.760 35708.361 35708.361 allGraphsTrain.py:13(graphTrain)
                 109076  126.148    0.001 27069.063    0.248 allGraphsTrain.py:40(<listcomp>)
                 640062    3.070    0.000 26938.199    0.042 allGraphs.py:179(getInterventionsmodel)
        54525596/489757 4673.366    0.000 25265.040    0.052 allGraphs.py:186(recursiveBEST)
               52039874 2109.869    0.000 18634.449    0.000 BayesianNN.py:65(predict_no_convert)
               58451822  151.570    0.000 18435.243    0.000 BayesianNN.py:18(forward)
        646893063/60193323 2278.440    0.000 18381.341    0.000 module.py:866(_call_impl)
               58669974  804.617    0.000 17943.505    0.000 container.py:117(forward)
              175791770  304.808    0.000 7115.723    0.000 linear.py:93(forward)
              175791770  134.278    0.000 6688.490    0.000 functional.py:1737(linear)
              175791770 6523.907    0.000 6523.907    0.000 {built-in method torch._C._nn.linear}
                 109076 1253.648    0.011 4976.462    0.046 allGraphs.py:156(transformNot)
              175355466  128.171    0.000 4106.019    0.000 dropout.py:57(forward)
              175355466  434.206    0.000 3977.848    0.000 functional.py:1059(dropout)
              175355466 3420.136    0.000 3420.136    0.000 {built-in method dropout}
              176009922  106.524    0.000 2851.723    0.000 activation.py:713(forward)
              176009922  125.892    0.000 2745.199    0.000 functional.py:1364(leaky_relu)
              176009922 2595.839    0.000 2595.839    0.000 {built-in method torch._C._nn.leaky_relu}
                1414273   18.808    0.000 2524.960    0.002 BayesianNN.py:57(learn)
                4997675   66.638    0.000 2403.780    0.000 BayesianNN.py:61(predict)
                1414273   17.197    0.000 2320.696    0.002 BayesianNN.py:21(learn)
                 109076    6.866    0.000 1768.569    0.016 allGraphsTrain.py:33(<listcomp>)
               11016777  436.914    0.000 1761.751    0.000 allGraphs.py:114(states)
              132306845 1651.888    0.000 1651.888    0.000 {method 'item' of 'torch._C._TensorBase' objects}
          750647/150305   76.760    0.000 1594.838    0.011 allGraphs.py:202(recursiveExplore)
              119984100 1427.870    0.000 1427.870    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                1523349   11.631    0.000 1085.212    0.001 optimizer.py:84(wrapper)
                1523349    5.710    0.000 1028.182    0.001 grad_mode.py:24(decorate_context)
                1523349   31.933    0.000 1008.174    0.001 adam.py:55(step)
               54745257   57.664    0.000  974.530    0.000 tensor.py:525(__rsub__)
                1523349  205.312    0.000  941.926    0.001 _functional.py:53(adam)
               54745257  906.797    0.000  906.797    0.000 {built-in method rsub}
                6411948  704.810    0.000  899.113    0.000 BayesianNN.py:43(convert_data)
                1523349    5.526    0.000  616.339    0.000 tensor.py:195(backward)
                1523349    5.278    0.000  610.596    0.000 __init__.py:68(backward)
                1523349  573.394    0.000  573.394    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                 109076    0.462    0.000  433.377    0.004 game.py:42(step)
                 109076    3.333    0.000  423.220    0.004 allGraphs.py:141(transform)
                 109076    0.609    0.000  409.064    0.004 layers.py:827(step)
              647220291  403.217    0.000  403.217    0.000 {built-in method torch._C._get_tracing_state}
                 109076   28.412    0.000  355.874    0.003 allGraphsTrain.py:44(<listcomp>)
        2878231051/2878231049  292.925    0.000  294.025    0.000 {built-in method builtins.len}
                 109076    0.424    0.000  249.598    0.002 agent.py:29(learn)
                 109076    2.723    0.000  248.930    0.002 agent.py:117(_learn)
                 109076    8.056    0.000  246.207    0.002 learner.py:42(Qlearn)
             2646242226  218.802    0.000  218.802    0.000 {method 'values' of 'collections.OrderedDict' objects}
                 109076    8.008    0.000  205.104    0.002 layers.py:17(step)
                 109077   14.771    0.000  202.690    0.002 layers.py:793(update)
              412540900  199.445    0.000  199.445    0.000 module.py:934(__getattr__)
               69795726  198.540    0.000  198.540    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               10907600   16.479    0.000  196.164    0.000 layer.py:106(move)
               18716492  192.821    0.000  192.821    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               58888126   37.820    0.000  191.270    0.000 flatten.py:39(forward)
               15870595  186.834    0.000  186.834    0.000 {built-in method zeros}
               18716492  169.945    0.000  169.945    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                1523349   26.013    0.000  160.145    0.000 optimizer.py:189(zero_grad)
                1675561  148.658    0.000  148.658    0.000 {built-in method tensor}
               10907600  145.798    0.000  145.798    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                 109076  131.492    0.001  131.492    0.001 allGraphsTrain.py:51(<listcomp>)
                1185443    1.169    0.000  129.033    0.000 game.py:38(board)
               57255701  120.024    0.000  120.024    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                9358246  105.102    0.000  105.102    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               10907600   25.626    0.000  104.856    0.000 layers.py:844(check)
              176878815   67.954    0.000   99.237    0.000 _VF.py:25(__getattr__)
                 109076   62.039    0.001   93.778    0.001 agent.py:67(modify)
                9358246   88.963    0.000   88.963    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                9358246   88.560    0.000   88.560    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                9358246   88.234    0.000   88.234    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                 218152    0.684    0.000   86.842    0.000 network.py:28(forward)
               83383379   59.899    0.000   77.787    0.000 types.py:171(__get__)
                 640062    5.171    0.000   74.989    0.000 allGraphs.py:167(format)
                1523349    2.199    0.000   74.576    0.000 loss.py:527(forward)
                1523349    5.586    0.000   72.377    0.000 functional.py:2898(mse_loss)
                9358246   68.756    0.000   68.756    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               10907600   15.027    0.000   59.991    0.000 layers.py:838(isFree)
                  97319    1.070    0.000   57.880    0.001 layers.py:849(restart)
               65507782   45.195    0.000   56.034    0.000 tensor.py:906(grad)
                2619520   55.342    0.000   55.342    0.000 {built-in method cat}
              428845840   54.895    0.000   54.895    0.000 {built-in method torch._C._has_torch_function_unary}
                 109076    1.696    0.000   53.996    0.000 agent.py:112(__call__)
               58669974   36.574    0.000   52.697    0.000 container.py:109(__iter__)
                1523349   50.759    0.000   50.759    0.000 {built-in method torch._C._nn.mse_loss}
                  97319    0.559    0.000   49.824    0.001 level.py:8(__init__)
                 872616   25.297    0.000   46.429    0.000 layer.py:175(NoRock_update)
              173556183   31.527    0.000   46.085    0.000 enum.py:646(__hash__)
               76460098   36.030    0.000   44.964    0.000 layer.py:103(isFree)
              232060376   40.654    0.000   40.654    0.000 {built-in method torch._C._has_torch_function_variadic}
               10907700    4.186    0.000   39.922    0.000 {built-in method builtins.all}
               10810382    9.162    0.000   38.897    0.000 {built-in method builtins.any}
                9354133   37.860    0.000   37.860    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               47677939   12.316    0.000   37.021    0.000 layers.py:799(<genexpr>)
                  97319    1.417    0.000   34.884    0.000 levels.py:303(generate)
                 436304    1.018    0.000   34.351    0.000 conv.py:398(forward)
                 436304    0.679    0.000   32.898    0.000 conv.py:390(_conv_forward)
                 436304   32.219    0.000   32.219    0.000 {built-in method conv2d}
                 584491    5.550    0.000   31.983    0.000 level.py:41(notUsed)
              176987109   31.359    0.000   31.359    0.000 {built-in method builtins.getattr}
                3046698    6.261    0.000   31.078    0.000 profiler.py:615(__enter__)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9651530: <Diamonds3_0.5_NN_1> in cluster <dcc> Done

Job <Diamonds3_0.5_NN_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Tue May 18 21:04:58 2021
Job was executed on host(s) <n-62-20-5>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed May 19 07:02:19 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 19 07:02:19 2021
Terminated at Wed May 19 16:57:33 2021
Results reported at Wed May 19 16:57:33 2021

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

    CPU time :                                   35618.39 sec.
    Max Memory :                                 3258 MB
    Average Memory :                             2911.05 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13126.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35814 sec.
    Turnaround time :                            71555 sec.

The output (if any) is above this job summary.

