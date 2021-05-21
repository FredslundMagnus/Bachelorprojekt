
# Parameters

    Name :                      Diamonds4_0.5_NN-1
    Main :                      graphTrain
    Level :                     Levels.Causal7
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


      12571474103 function calls (11955187118 primitive calls) in 35703.78 seconds

##    Ordered by: cumulative time
   List reduced from 485 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35703.784 35703.784 {built-in method builtins.exec}
                      1    0.002    0.002 35703.784 35703.784 <string>:1(<module>)
                      1   34.238   34.238 35703.782 35703.782 allGraphsTrain.py:13(graphTrain)
                 125741  147.665    0.001 25908.942    0.206 allGraphsTrain.py:40(<listcomp>)
                1186665    5.486    0.000 25752.907    0.022 allGraphs.py:179(getInterventionsmodel)
        52025707/969274 4401.364    0.000 23963.097    0.025 allGraphs.py:186(recursiveBEST)
               56209696  150.177    0.000 17754.999    0.000 BayesianNN.py:18(forward)
        623260177/58648397 2184.399    0.000 17752.472    0.000 module.py:866(_call_impl)
               56461178  830.110    0.000 17297.546    0.000 container.py:117(forward)
               48196766 1944.771    0.000 17241.909    0.000 BayesianNN.py:65(predict_no_convert)
              169132052  289.513    0.000 6839.438    0.000 linear.py:93(forward)
              169132052  126.060    0.000 6429.318    0.000 functional.py:1737(linear)
              169132052 6272.979    0.000 6272.979    0.000 {built-in method torch._C._nn.linear}
                 125741 1219.964    0.010 5788.210    0.046 allGraphs.py:156(transformNot)
              168629088  118.483    0.000 3939.055    0.000 dropout.py:57(forward)
              168629088  429.146    0.000 3820.572    0.000 functional.py:1059(dropout)
                2061478   27.672    0.000 3698.273    0.002 BayesianNN.py:57(learn)
                2061478   23.863    0.000 3385.273    0.002 BayesianNN.py:21(learn)
              168629088 3270.313    0.000 3270.313    0.000 {built-in method dropout}
                5951452   79.678    0.000 2887.560    0.000 BayesianNN.py:61(predict)
              169383534  103.698    0.000 2739.019    0.000 activation.py:713(forward)
              169383534  117.604    0.000 2635.321    0.000 functional.py:1364(leaky_relu)
              169383534 2495.306    0.000 2495.306    0.000 {built-in method torch._C._nn.leaky_relu}
          835748/217391   79.933    0.000 1654.998    0.008 allGraphs.py:202(recursiveExplore)
                 125741    7.472    0.000 1654.629    0.013 allGraphsTrain.py:33(<listcomp>)
               12699942  412.887    0.000 1647.170    0.000 allGraphs.py:114(states)
              127803878 1618.918    0.000 1618.918    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                2187219   16.493    0.000 1549.774    0.001 optimizer.py:84(wrapper)
                2187219    8.671    0.000 1468.080    0.001 grad_mode.py:24(decorate_context)
                2187219   45.344    0.000 1439.885    0.001 adam.py:55(step)
              113167300 1358.301    0.000 1358.301    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                2187219  292.588    0.000 1346.924    0.001 _functional.py:53(adam)
                8012930  907.737    0.000 1151.166    0.000 BayesianNN.py:43(convert_data)
               51800531   55.426    0.000  907.295    0.000 tensor.py:525(__rsub__)
                2187219    8.566    0.000  883.684    0.000 tensor.py:195(backward)
                2187219    8.088    0.000  874.817    0.000 __init__.py:68(backward)
               51800531  840.911    0.000  840.911    0.000 {built-in method rsub}
                2187219  821.171    0.000  821.171    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                 125741    4.268    0.000  710.041    0.006 allGraphs.py:141(transform)
                 125741    0.554    0.000  448.732    0.004 game.py:42(step)
                 125741    0.719    0.000  421.737    0.003 layers.py:827(step)
                 125741   33.555    0.000  411.873    0.003 allGraphsTrain.py:44(<listcomp>)
              623637400  389.800    0.000  389.800    0.000 {built-in method torch._C._get_tracing_state}
                 125741    0.508    0.000  289.206    0.002 agent.py:29(learn)
                 125741    3.155    0.000  288.413    0.002 agent.py:117(_learn)
        2785585335/2785585333  286.634    0.000  287.866    0.000 {built-in method builtins.len}
                 125741    9.388    0.000  285.258    0.002 learner.py:42(Qlearn)
               26749592  275.296    0.000  275.296    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               26749592  243.496    0.000  243.496    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               20400299  237.855    0.000  237.855    0.000 {built-in method zeros}
                2187219   38.214    0.000  231.322    0.000 optimizer.py:189(zero_grad)
                 125741    9.264    0.000  216.985    0.002 layers.py:17(step)
             2549501886  211.194    0.000  211.194    0.000 {method 'values' of 'collections.OrderedDict' objects}
               12574100   19.331    0.000  206.595    0.000 layer.py:106(move)
                 125742   17.201    0.000  203.206    0.002 layers.py:793(update)
                2375593  201.429    0.000  201.429    0.000 {built-in method tensor}
              397793237  200.168    0.000  200.169    0.000 module.py:934(__getattr__)
               69286760  197.171    0.000  197.171    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                1815371    1.714    0.000  181.811    0.000 game.py:38(board)
               56712660   35.917    0.000  180.834    0.000 flatten.py:39(forward)
               12574100  167.998    0.000  167.998    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                 125741  152.534    0.001  152.534    0.001 allGraphsTrain.py:51(<listcomp>)
               13374796  150.373    0.000  150.373    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                1186665    9.302    0.000  128.842    0.000 allGraphs.py:167(format)
               13374796  128.033    0.000  128.033    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               13374796  127.282    0.000  127.282    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               13374796  125.895    0.000  125.895    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               54399700  115.274    0.000  115.274    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                 125741   72.508    0.001  109.157    0.001 agent.py:67(modify)
                2187219    2.876    0.000  108.225    0.000 loss.py:527(forward)
                2187219    7.821    0.000  105.349    0.000 functional.py:2898(mse_loss)
                 251482    0.787    0.000  100.589    0.000 network.py:28(forward)
               12574100   25.999    0.000   99.531    0.000 layers.py:844(check)
               13374796   98.968    0.000   98.968    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              170816307   66.846    0.000   97.534    0.000 _VF.py:25(__getattr__)
               88590198   63.781    0.000   79.592    0.000 types.py:171(__get__)
               93623632   63.289    0.000   78.698    0.000 tensor.py:906(grad)
                2187219   74.486    0.000   74.486    0.000 {built-in method torch._C._nn.mse_loss}
               12574100   17.360    0.000   70.269    0.000 layers.py:838(isFree)
                 134462    1.372    0.000   64.170    0.000 layers.py:849(restart)
                 125741    1.963    0.000   62.213    0.000 agent.py:112(__call__)
                2724910   58.217    0.000   58.217    0.000 {built-in method cat}
              448456026   55.975    0.000   55.975    0.000 {built-in method torch._C._has_torch_function_unary}
                 134462    0.634    0.000   53.457    0.000 level.py:8(__init__)
               84658030   43.040    0.000   52.909    0.000 layer.py:103(isFree)
                 880194   27.159    0.000   48.782    0.000 layer.py:175(NoRock_update)
               56461178   33.541    0.000   47.999    0.000 container.py:109(__iter__)
               11688345   47.902    0.000   47.902    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              172277834   32.020    0.000   46.598    0.000 enum.py:646(__hash__)
                4374438    9.756    0.000   44.819    0.000 profiler.py:615(__enter__)
                2187219    8.150    0.000   43.549    0.000 __init__.py:28(_make_grads)
              223119802   41.671    0.000   41.671    0.000 {built-in method torch._C._has_torch_function_variadic}
                 502964    1.178    0.000   39.628    0.000 conv.py:398(forward)
               12439739    9.577    0.000   39.549    0.000 {built-in method builtins.any}
                 134462    1.577    0.000   38.391    0.000 levels.py:456(generate)
                 502964    0.774    0.000   37.942    0.000 conv.py:390(_conv_forward)
                 502964   37.168    0.000   37.168    0.000 {built-in method conv2d}
                 377223    0.895    0.000   36.066    0.000 tensor.py:575(__iter__)
                 645526    6.292    0.000   35.162    0.000 level.py:41(notUsed)
                4374438    5.932    0.000   35.133    0.000 profiler.py:607(__init__)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9651533: <Diamonds4_0.5_NN_1> in cluster <dcc> Done

Job <Diamonds4_0.5_NN_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Tue May 18 21:04:59 2021
Job was executed on host(s) <n-62-20-2>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed May 19 17:04:03 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 19 17:04:03 2021
Terminated at Thu May 20 02:59:09 2021
Results reported at Thu May 20 02:59:09 2021

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

    CPU time :                                   35617.03 sec.
    Max Memory :                                 3621 MB
    Average Memory :                             3107.49 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               12763.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35708 sec.
    Turnaround time :                            107650 sec.

The output (if any) is above this job summary.

