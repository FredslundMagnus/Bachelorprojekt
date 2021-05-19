
# Parameters

    Name :                      Diamonds1_0.0_NN-1
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
    Num :                       1
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      14333064122 function calls (13723940784 primitive calls) in 35709.58 seconds

##    Ordered by: cumulative time
   List reduced from 473 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35709.579 35709.579 {built-in method builtins.exec}
                      1    0.001    0.001 35709.579 35709.579 <string>:1(<module>)
                      1   33.020   33.020 35709.578 35709.578 allGraphsTrain.py:13(graphTrain)
                 132335  136.363    0.001 26789.157    0.202 allGraphsTrain.py:40(<listcomp>)
                 975343    4.593    0.000 26645.744    0.027 allGraphs.py:179(getInterventionsmodel)
        52472041/829035 3610.322    0.000 25360.638    0.031 allGraphs.py:186(recursiveBEST)
               49013648 2074.348    0.000 18410.373    0.000 BayesianNN.py:65(predict_no_convert)
        614523604/57475454 2023.511    0.000 18392.124    0.000 module.py:715(_call_impl)
               55440145  125.991    0.000 18389.431    0.000 BayesianNN.py:18(forward)
               55704815  631.476    0.000 17978.372    0.000 container.py:115(forward)
              166849775  317.139    0.000 8192.029    0.000 linear.py:92(forward)
              166849775  566.379    0.000 7735.256    0.000 functional.py:1669(linear)
              166849775 5255.374    0.000 5255.374    0.000 {built-in method addmm}
                 132335 1068.514    0.008 4302.585    0.033 allGraphs.py:156(transformNot)
              166320435  124.297    0.000 4051.180    0.000 dropout.py:57(forward)
              166320435  515.380    0.000 3926.883    0.000 functional.py:960(dropout)
              166320435 3281.764    0.000 3281.764    0.000 {built-in method dropout}
                1638304   18.740    0.000 2918.873    0.002 BayesianNN.py:57(learn)
                1638304   17.839    0.000 2688.196    0.002 BayesianNN.py:21(learn)
              167114445   97.498    0.000 2431.160    0.000 activation.py:713(forward)
                4788193   63.672    0.000 2344.120    0.000 BayesianNN.py:61(predict)
              167114445  179.742    0.000 2333.662    0.000 functional.py:1292(leaky_relu)
              167114445 2134.139    0.000 2134.139    0.000 {built-in method torch._C._nn.leaky_relu}
              133974760 1635.440    0.000 1635.440    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                 132335    3.399    0.000 1560.249    0.012 allGraphsTrain.py:33(<listcomp>)
               13365936  369.165    0.000 1556.916    0.000 allGraphs.py:114(states)
               66102283  214.166    0.000 1242.677    0.000 tensor.py:21(wrapped)
                1770639    9.540    0.000 1215.979    0.001 grad_mode.py:23(decorate_context)
              166849775 1206.303    0.000 1206.303    0.000 {method 't' of 'torch._C._TensorBase' objects}
                1770639   43.563    0.000 1188.119    0.001 adam.py:55(step)
              119101900 1177.189    0.000 1177.189    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
          578075/146308   47.665    0.000 1174.532    0.008 allGraphs.py:202(recursiveExplore)
                 132335    5.608    0.000 1157.780    0.009 allGraphs.py:141(transform)
               52207108  154.315    0.000 1048.720    0.000 tensor.py:506(__rsub__)
                1770639  218.152    0.000  969.411    0.001 functional.py:53(adam)
               52207108  894.405    0.000  894.405    0.000 {built-in method rsub}
                6426497  661.985    0.000  845.682    0.000 BayesianNN.py:43(convert_data)
               52074773  699.598    0.000  699.598    0.000 {method 'gt' of 'torch._C._TensorBase' objects}
              281303066  197.220    0.000  678.265    0.000 overrides.py:1070(has_torch_function)
                1770639   10.030    0.000  660.835    0.000 tensor.py:181(backward)
                1770639    5.745    0.000  650.806    0.000 __init__.py:68(backward)
                 132335    0.474    0.000  614.723    0.005 game.py:42(step)
                1770639  605.205    0.000  605.205    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                 132335    0.626    0.000  587.553    0.004 layers.py:827(step)
              464692375  215.066    0.000  534.770    0.000 {built-in method builtins.any}
                 132335   27.153    0.000  391.682    0.003 allGraphsTrain.py:44(<listcomp>)
              614920609  368.027    0.000  368.027    0.000 {built-in method torch._C._get_tracing_state}
                 132335   10.124    0.000  328.664    0.002 layers.py:17(step)
               13233500   22.210    0.000  317.353    0.000 layer.py:106(move)
               76219588  186.672    0.000  312.790    0.000 tensor.py:933(grad)
                 132335    0.444    0.000  296.682    0.002 agent.py:29(learn)
                 132335    2.819    0.000  295.908    0.002 agent.py:117(_learn)
                 132335    8.544    0.000  293.089    0.002 learner.py:42(Qlearn)
              756800996  243.250    0.000  284.616    0.000 overrides.py:1083(<genexpr>)
                1770639   26.769    0.000  271.061    0.000 optimizer.py:167(zero_grad)
                 132336   18.785    0.000  257.542    0.002 layers.py:793(update)
                 132335   10.351    0.000  226.683    0.002 allGraphsTrain.py:51(<listcomp>)
             2513799231  222.895    0.000  222.895    0.000 {method 'values' of 'collections.OrderedDict' objects}
              392101920  216.370    0.000  216.370    0.000 module.py:765(__getattr__)
               13233500   42.759    0.000  199.004    0.000 layers.py:844(check)
               21777008  195.800    0.000  195.800    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                2225010  182.748    0.000  182.748    0.000 {built-in method tensor}
               69202985  178.097    0.000  178.097    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
        1534215692/1534215690  167.012    0.000  169.298    0.000 {built-in method builtins.len}
               55969485   31.934    0.000  164.748    0.000 flatten.py:39(forward)
               21777008  163.138    0.000  163.138    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                1637019    1.603    0.000  163.110    0.000 game.py:38(board)
               13895175  162.440    0.000  162.440    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               13233500  155.427    0.000  155.427    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               12852995  153.935    0.000  153.935    0.000 {built-in method zeros}
                 132335   67.697    0.001  127.368    0.001 agent.py:67(modify)
               10888504  112.381    0.000  112.381    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              168091074   78.935    0.000  110.775    0.000 _VF.py:25(__getattr__)
               79335883   47.680    0.000  110.239    0.000 {built-in method builtins.all}
                 235345    2.178    0.000  106.825    0.000 layers.py:849(restart)
                 975343    7.577    0.000  105.607    0.000 allGraphs.py:167(format)
                 264670    0.688    0.000  105.186    0.000 network.py:28(forward)
               10888504  103.868    0.000  103.868    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              166849775   95.578    0.000   95.578    0.000 functional.py:1686(<listcomp>)
               10888504   92.579    0.000   92.579    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                 235345    0.986    0.000   87.461    0.000 level.py:8(__init__)
               79580970   69.960    0.000   87.165    0.000 types.py:171(__get__)
                1770639    2.270    0.000   86.267    0.000 loss.py:445(forward)
               54066511   85.710    0.000   85.710    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                1770639    8.515    0.000   83.997    0.000 functional.py:2637(mse_loss)
               10888504   80.490    0.000   80.490    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               13233500   19.962    0.000   76.152    0.000 layers.py:838(isFree)
              449512081   73.273    0.000   73.273    0.000 {built-in method builtins.getattr}
              260644606   50.431    0.000   72.979    0.000 enum.py:646(__hash__)
                 235345    2.798    0.000   72.745    0.000 levels.py:151(generate)
                1129376   11.699    0.000   67.002    0.000 level.py:41(notUsed)
              168173245   66.821    0.000   66.821    0.000 {method 'dim' of 'torch._C._TensorBase' objects}
                 132335    1.612    0.000   63.153    0.000 agent.py:112(__call__)
               10888504   62.787    0.000   62.787    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              505596692   59.375    0.000   59.375    0.000 _jit_internal.py:750(is_scripting)
                 926352   32.438    0.000   57.853    0.000 layer.py:175(NoRock_update)
               90969829   44.580    0.000   56.189    0.000 layer.py:103(isFree)
              198306849   54.453    0.000   54.453    0.000 tensor.py:24(<genexpr>)
               55704815   37.584    0.000   53.627    0.000 container.py:107(__iter__)
                1770639   52.758    0.000   52.758    0.000 {built-in method torch._C._nn.mse_loss}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9651544: <Diamonds1_0.0_NN_1> in cluster <dcc> Done

Job <Diamonds1_0.0_NN_1> was submitted from host <n-62-27-18> by user <s183905> in cluster <dcc> at Tue May 18 21:12:59 2021
Job was executed on host(s) <n-62-20-14>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Tue May 18 21:13:00 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue May 18 21:13:00 2021
Terminated at Wed May 19 07:10:18 2021
Results reported at Wed May 19 07:10:18 2021

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

    CPU time :                                   35608.07 sec.
    Max Memory :                                 2061 MB
    Average Memory :                             2038.34 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14323.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35729 sec.
    Turnaround time :                            35839 sec.

The output (if any) is above this job summary.

