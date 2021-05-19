
# Parameters

    Name :                      Diamonds3_0.0_NN-1
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


      14706106910 function calls (14062881916 primitive calls) in 35708.84 seconds

##    Ordered by: cumulative time
   List reduced from 474 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35708.839 35708.839 {built-in method builtins.exec}
                      1    0.002    0.002 35708.839 35708.839 <string>:1(<module>)
                      1   29.699   29.699 35708.837 35708.837 allGraphsTrain.py:13(graphTrain)
                 111268  129.096    0.001 27366.898    0.246 allGraphsTrain.py:40(<listcomp>)
                 653162    3.310    0.000 27232.446    0.042 allGraphs.py:179(getInterventionsmodel)
        54600254/492616 3748.468    0.000 25532.643    0.052 allGraphs.py:186(recursiveBEST)
               52115268 2109.139    0.000 18775.268    0.000 BayesianNN.py:65(predict_no_convert)
               58627260  123.475    0.000 18642.242    0.000 BayesianNN.py:18(forward)
        648883741/60385781 2078.933    0.000 18610.666    0.000 module.py:715(_call_impl)
               58849796  632.760    0.000 18200.344    0.000 container.py:115(forward)
              176326852  325.037    0.000 8194.743    0.000 linear.py:92(forward)
              176326852  591.165    0.000 7723.372    0.000 functional.py:1669(linear)
              176326852 5233.609    0.000 5233.609    0.000 {built-in method addmm}
                 111268 1029.512    0.009 4251.999    0.038 allGraphs.py:156(transformNot)
              175881780  141.152    0.000 4166.945    0.000 dropout.py:57(forward)
              175881780  520.767    0.000 4025.793    0.000 functional.py:960(dropout)
              175881780 3370.732    0.000 3370.732    0.000 {built-in method dropout}
              176549388  106.980    0.000 2467.730    0.000 activation.py:713(forward)
                1424717   15.339    0.000 2438.221    0.002 BayesianNN.py:57(learn)
                5087275   63.565    0.000 2402.747    0.000 BayesianNN.py:61(predict)
              176549388  176.990    0.000 2360.750    0.000 functional.py:1292(leaky_relu)
                1424717   15.452    0.000 2247.179    0.002 BayesianNN.py:21(learn)
              176549388 2164.192    0.000 2164.192    0.000 {built-in method torch._C._nn.leaky_relu}
              134947705 1810.851    0.000 1810.851    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                 111268    2.733    0.000 1660.036    0.015 allGraphsTrain.py:33(<listcomp>)
               11238169  360.538    0.000 1657.353    0.000 allGraphs.py:114(states)
          779527/160546   63.998    0.000 1615.446    0.010 allGraphs.py:202(recursiveExplore)
              176326852 1213.880    0.000 1213.880    0.000 {method 't' of 'torch._C._TensorBase' objects}
               66521027  202.763    0.000 1184.408    0.000 tensor.py:21(wrapped)
              122395300 1177.401    0.000 1177.401    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
               54837887  162.163    0.000 1072.990    0.000 tensor.py:506(__rsub__)
                1535985    8.175    0.000 1013.156    0.001 grad_mode.py:23(decorate_context)
                1535985   36.699    0.000  989.659    0.001 adam.py:55(step)
               54837887  910.826    0.000  910.826    0.000 {built-in method rsub}
                6511992  675.085    0.000  852.547    0.000 BayesianNN.py:43(convert_data)
                1535985  180.417    0.000  808.747    0.001 functional.py:53(adam)
                 111268    4.272    0.000  765.699    0.007 allGraphs.py:141(transform)
               54726619  700.614    0.000  700.614    0.000 {method 'gt' of 'torch._C._TensorBase' objects}
              275257492  188.127    0.000  614.033    0.000 overrides.py:1070(has_torch_function)
                 111268    0.431    0.000  584.675    0.005 game.py:42(step)
                 111268    0.597    0.000  560.590    0.005 layers.py:827(step)
                1535985    8.519    0.000  554.246    0.000 tensor.py:181(backward)
                1535985    4.657    0.000  545.727    0.000 __init__.py:68(backward)
                1535985  507.458    0.000  507.458    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
              465637658  210.469    0.000  486.659    0.000 {built-in method builtins.any}
              649217545  378.726    0.000  378.726    0.000 {built-in method torch._C._get_tracing_state}
                 111268   20.554    0.000  334.038    0.003 allGraphsTrain.py:44(<listcomp>)
                 111268    8.701    0.000  311.493    0.003 layers.py:17(step)
               11126800   18.331    0.000  301.849    0.000 layer.py:106(move)
               66069182  154.411    0.000  257.923    0.000 tensor.py:933(grad)
                 111269   16.376    0.000  247.847    0.002 layers.py:793(update)
                 111268    0.382    0.000  245.584    0.002 agent.py:29(learn)
                 111268    2.447    0.000  244.965    0.002 agent.py:117(_learn)
                 111268    7.138    0.000  242.518    0.002 learner.py:42(Qlearn)
              750264738  200.904    0.000  241.611    0.000 overrides.py:1083(<genexpr>)
             2654384760  230.753    0.000  230.753    0.000 {method 'values' of 'collections.OrderedDict' objects}
              413818888  227.624    0.000  227.625    0.000 module.py:765(__getattr__)
                1535985   21.728    0.000  224.036    0.000 optimizer.py:167(zero_grad)
               11126800   40.183    0.000  198.519    0.000 layers.py:844(check)
                 111268    8.218    0.000  182.812    0.002 allGraphsTrain.py:51(<listcomp>)
               59072332   38.925    0.000  171.711    0.000 flatten.py:39(forward)
               70199132  169.921    0.000  169.921    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
        1601731097/1601731095  163.940    0.000  165.759    0.000 {built-in method builtins.len}
               18876892  165.196    0.000  165.196    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                1709168  153.721    0.000  153.721    0.000 {built-in method tensor}
               13023985  149.659    0.000  149.659    0.000 {built-in method zeros}
               77647927   50.526    0.000  139.681    0.000 {built-in method builtins.all}
                1209503    1.536    0.000  136.682    0.000 game.py:38(board)
               18876892  135.768    0.000  135.768    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               11683140  131.574    0.000  131.574    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               11126800  126.028    0.000  126.028    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
              177417765   84.509    0.000  115.790    0.000 _VF.py:25(__getattr__)
                 111268   54.644    0.000  104.906    0.001 agent.py:67(modify)
              176326852   99.539    0.000   99.539    0.000 functional.py:1686(<listcomp>)
                9438446   92.977    0.000   92.977    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                 222536    0.576    0.000   87.550    0.000 network.py:28(forward)
               57425079   87.199    0.000   87.199    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                9438446   86.799    0.000   86.799    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                 653162    5.294    0.000   80.769    0.000 allGraphs.py:167(format)
               84915931   62.266    0.000   79.273    0.000 types.py:171(__get__)
                 145557    1.550    0.000   78.752    0.001 layers.py:849(restart)
                9438446   77.175    0.000   77.175    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                1535985    1.926    0.000   73.371    0.000 loss.py:445(forward)
              452785115   72.051    0.000   72.051    0.000 {built-in method builtins.getattr}
                1535985    7.494    0.000   71.445    0.000 functional.py:2637(mse_loss)
              266127109   48.776    0.000   70.383    0.000 enum.py:646(__hash__)
               11126800   17.117    0.000   68.391    0.000 layers.py:838(isFree)
                9438446   67.843    0.000   67.843    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                 145557    0.753    0.000   66.145    0.000 level.py:8(__init__)
              177439652   62.563    0.000   62.563    0.000 {method 'dim' of 'torch._C._TensorBase' objects}
              533366095   58.819    0.000   58.819    0.000 _jit_internal.py:750(is_scripting)
               58849796   40.704    0.000   56.780    0.000 container.py:107(__iter__)
                2698460   55.883    0.000   55.883    0.000 {built-in method cat}
                 145557    2.094    0.000   55.141    0.000 levels.py:303(generate)
                 111268    1.483    0.000   53.944    0.000 agent.py:112(__call__)
                9438446   52.448    0.000   52.448    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              199563081   52.003    0.000   52.003    0.000 tensor.py:24(<genexpr>)
                 890152   28.523    0.000   51.783    0.000 layer.py:175(NoRock_update)
               79323044   41.423    0.000   51.275    0.000 layer.py:103(isFree)
                 873512    8.755    0.000   50.811    0.000 level.py:41(notUsed)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9651550: <Diamonds3_0.0_NN_1> in cluster <dcc> Done

Job <Diamonds3_0.0_NN_1> was submitted from host <n-62-27-18> by user <s183905> in cluster <dcc> at Tue May 18 21:12:59 2021
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Wed May 19 07:10:20 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 19 07:10:20 2021
Terminated at Wed May 19 17:05:34 2021
Results reported at Wed May 19 17:05:34 2021

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

    CPU time :                                   35620.89 sec.
    Max Memory :                                 2065 MB
    Average Memory :                             2064.68 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14319.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35809 sec.
    Turnaround time :                            71555 sec.

The output (if any) is above this job summary.

