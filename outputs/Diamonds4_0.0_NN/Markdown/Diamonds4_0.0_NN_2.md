
# Parameters

    Name :                      Diamonds4_0.0_NN-2
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


      14686205681 function calls (14076030707 primitive calls) in 35709.76 seconds

##    Ordered by: cumulative time
   List reduced from 475 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35709.761 35709.761 {built-in method builtins.exec}
                      1    0.001    0.001 35709.761 35709.761 <string>:1(<module>)
                      1   39.997   39.997 35709.760 35709.760 allGraphsTrain.py:13(graphTrain)
                 140250  163.098    0.001 25989.043    0.185 allGraphsTrain.py:40(<listcomp>)
                1181248    5.715    0.000 25817.413    0.022 allGraphs.py:179(getInterventionsmodel)
        52518920/1026732 3509.568    0.000 24517.991    0.024 allGraphs.py:186(recursiveBEST)
        616093679/57845619 2007.818    0.000 17840.010    0.000 module.py:715(_call_impl)
               55544306  121.114    0.000 17821.382    0.000 BayesianNN.py:18(forward)
               48539740 1960.973    0.000 17582.023    0.000 BayesianNN.py:65(predict_no_convert)
               55824806  622.932    0.000 17421.864    0.000 container.py:115(forward)
              167193918  316.825    0.000 7853.872    0.000 linear.py:92(forward)
              167193918  570.811    0.000 7406.123    0.000 functional.py:1669(linear)
              167193918 5021.936    0.000 5021.936    0.000 {built-in method addmm}
                 140250 1101.143    0.008 4645.473    0.033 allGraphs.py:156(transformNot)
              166632918  134.594    0.000 3941.804    0.000 dropout.py:57(forward)
              166632918  491.289    0.000 3807.211    0.000 functional.py:960(dropout)
                1880563   20.745    0.000 3260.975    0.002 BayesianNN.py:57(learn)
              166632918 3187.101    0.000 3187.101    0.000 {built-in method dropout}
                1880563   19.720    0.000 2984.081    0.002 BayesianNN.py:21(learn)
                5124003   65.540    0.000 2469.600    0.000 BayesianNN.py:61(predict)
              167474418  100.201    0.000 2355.532    0.000 activation.py:713(forward)
              167474418  172.548    0.000 2255.331    0.000 functional.py:1292(leaky_relu)
              167474418 2063.631    0.000 2063.631    0.000 {built-in method torch._C._nn.leaky_relu}
              142132083 1893.186    0.000 1893.186    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                 140250    3.540    0.000 1688.107    0.012 allGraphsTrain.py:33(<listcomp>)
               14165351  382.792    0.000 1684.618    0.000 allGraphs.py:114(states)
                 140250    6.825    0.000 1342.555    0.010 allGraphs.py:141(transform)
                2020813   10.883    0.000 1336.436    0.001 grad_mode.py:23(decorate_context)
                2020813   48.009    0.000 1305.000    0.001 adam.py:55(step)
               66792999  208.952    0.000 1216.905    0.000 tensor.py:21(wrapped)
              126225400 1211.604    0.000 1211.604    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
          588827/154516   46.509    0.000 1157.679    0.007 allGraphs.py:202(recursiveExplore)
              167193918 1150.605    0.000 1150.605    0.000 {method 't' of 'torch._C._TensorBase' objects}
                2020813  238.357    0.000 1063.864    0.001 functional.py:53(adam)
               52066749  168.695    0.000 1027.416    0.000 tensor.py:506(__rsub__)
                7004566  751.921    0.000  948.091    0.000 BayesianNN.py:43(convert_data)
               52066749  858.721    0.000  858.721    0.000 {built-in method rsub}
                2020813   10.963    0.000  733.303    0.000 tensor.py:181(backward)
                2020813    6.193    0.000  722.340    0.000 __init__.py:68(backward)
               51926499  674.156    0.000  674.156    0.000 {method 'gt' of 'torch._C._TensorBase' objects}
                2020813  671.739    0.000  671.739    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                 140250    0.607    0.000  665.653    0.005 game.py:42(step)
              295532554  201.854    0.000  654.655    0.000 overrides.py:1070(has_torch_function)
                 140250    0.977    0.000  636.312    0.005 layers.py:827(step)
              480561853  216.588    0.000  508.469    0.000 {built-in method builtins.any}
                 140250   27.685    0.000  422.651    0.003 allGraphsTrain.py:44(<listcomp>)
              616514429  376.877    0.000  376.877    0.000 {built-in method torch._C._get_tracing_state}
                 140250   11.396    0.000  352.721    0.003 layers.py:17(step)
               86837706  206.686    0.000  345.241    0.000 tensor.py:933(grad)
               14025000   23.224    0.000  340.067    0.000 layer.py:106(move)
                 140250    0.541    0.000  317.304    0.002 agent.py:29(learn)
                 140250    3.194    0.000  316.372    0.002 agent.py:117(_learn)
                 140250    9.158    0.000  313.177    0.002 learner.py:42(Qlearn)
                2020813   28.502    0.000  298.826    0.000 optimizer.py:167(zero_grad)
                 140251   20.672    0.000  281.672    0.002 layers.py:793(update)
              787354468  210.903    0.000  254.969    0.000 overrides.py:1083(<genexpr>)
                 140250   10.798    0.000  232.573    0.002 allGraphsTrain.py:51(<listcomp>)
              393215798  219.932    0.000  219.933    0.000 module.py:765(__getattr__)
                2503355  217.074    0.000  217.074    0.000 {built-in method tensor}
               24810756  213.767    0.000  213.767    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               14025000   44.757    0.000  209.633    0.000 layers.py:844(check)
             2520199522  208.703    0.000  208.703    0.000 {method 'values' of 'collections.OrderedDict' objects}
                1882499    1.920    0.000  196.106    0.000 game.py:38(board)
               24810756  177.021    0.000  177.021    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               70130306  174.437    0.000  174.437    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               14726250  166.626    0.000  166.626    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               14009133  165.003    0.000  165.003    0.000 {built-in method zeros}
        1546834726/1546834724  158.779    0.000  161.158    0.000 {built-in method builtins.len}
               56105306   33.901    0.000  160.395    0.000 flatten.py:39(forward)
               14025000  158.080    0.000  158.080    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                 140250   71.788    0.001  136.982    0.001 agent.py:67(modify)
                1181248    9.941    0.000  135.511    0.000 allGraphs.py:167(format)
               80818099   48.633    0.000  126.376    0.000 {built-in method builtins.all}
               12405378  125.191    0.000  125.191    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               12405378  114.472    0.000  114.472    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                 280500    0.839    0.000  114.241    0.000 network.py:28(forward)
              168653731   77.688    0.000  109.671    0.000 _VF.py:25(__getattr__)
                 231346    2.344    0.000  107.355    0.000 layers.py:849(restart)
               12405378  101.924    0.000  101.924    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                2020813    2.922    0.000   97.968    0.000 loss.py:445(forward)
              167193918   95.322    0.000   95.322    0.000 functional.py:1686(<listcomp>)
                2020813    9.940    0.000   95.046    0.000 functional.py:2637(mse_loss)
               12405378   89.758    0.000   89.758    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                 231346    1.141    0.000   88.098    0.000 level.py:8(__init__)
               14025000   20.498    0.000   85.064    0.000 layers.py:838(isFree)
               85033740   63.354    0.000   78.578    0.000 types.py:171(__get__)
               53944243   78.377    0.000   78.377    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
              464306652   76.116    0.000   76.116    0.000 {built-in method builtins.getattr}
              273611088   52.315    0.000   75.360    0.000 enum.py:646(__hash__)
                 231346    2.810    0.000   71.340    0.000 levels.py:456(generate)
                 140250    2.022    0.000   70.605    0.001 agent.py:112(__call__)
               12405378   69.767    0.000   69.767    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                1110434   11.353    0.000   65.595    0.000 level.py:41(notUsed)
               89965840   53.011    0.000   64.566    0.000 layer.py:103(isFree)
                 981757   34.971    0.000   62.294    0.000 layer.py:175(NoRock_update)
              168596538   61.449    0.000   61.449    0.000 {method 'dim' of 'torch._C._TensorBase' objects}
                2020813   59.762    0.000   59.762    0.000 {built-in method torch._C._nn.mse_loss}
              507363813   58.596    0.000   58.596    0.000 _jit_internal.py:750(is_scripting)
              200378997   56.571    0.000   56.571    0.000 tensor.py:24(<genexpr>)
                 420750    1.481    0.000   50.497    0.000 tensor.py:576(__iter__)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9651554: <Diamonds4_0.0_NN_2> in cluster <dcc> Done

Job <Diamonds4_0.0_NN_2> was submitted from host <n-62-27-18> by user <s183905> in cluster <dcc> at Tue May 18 21:13:00 2021
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Wed May 19 17:05:35 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 19 17:05:35 2021
Terminated at Thu May 20 03:00:51 2021
Results reported at Thu May 20 03:00:51 2021

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

    CPU time :                                   35621.07 sec.
    Max Memory :                                 2065 MB
    Average Memory :                             2062.66 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14319.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35716 sec.
    Turnaround time :                            107271 sec.

The output (if any) is above this job summary.

