
# Parameters

    Name :                      Diamonds1_0.5_NN-2
    Main :                      graphTrain
    Level :                     Levels.Causal2
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
    Num :                       2
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      11569478502 function calls (11000992955 primitive calls) in 35720.33 seconds

##    Ordered by: cumulative time
   List reduced from 482 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35720.328 35720.328 {built-in method builtins.exec}
                      1    0.001    0.001 35720.328 35720.328 <string>:1(<module>)
                      1   33.378   33.378 35720.327 35720.327 allGraphsTrain.py:13(graphTrain)
                 115847  147.416    0.001 26156.237    0.226 allGraphsTrain.py:40(<listcomp>)
                 974521    4.941    0.000 26001.767    0.027 allGraphs.py:179(getInterventionsmodel)
        47673983/759247 4409.561    0.000 24013.091    0.032 allGraphs.py:186(recursiveBEST)
               51861078  144.829    0.000 17932.627    0.000 BayesianNN.py:18(forward)
        574869301/53941581 2157.169    0.000 17928.523    0.000 module.py:866(_call_impl)
               52092772  771.684    0.000 17480.845    0.000 container.py:117(forward)
               44495064 1957.436    0.000 17415.873    0.000 BayesianNN.py:65(predict_no_convert)
              156046622  292.534    0.000 6960.542    0.000 linear.py:93(forward)
              156046622  123.219    0.000 6542.555    0.000 functional.py:1737(linear)
              156046622 6390.992    0.000 6390.992    0.000 {built-in method torch._C._nn.linear}
                 115847 1240.175    0.011 5548.842    0.048 allGraphs.py:156(transformNot)
              155583234  126.872    0.000 4020.925    0.000 dropout.py:57(forward)
              155583234  445.681    0.000 3894.053    0.000 functional.py:1059(dropout)
                1732962   24.146    0.000 3385.729    0.002 BayesianNN.py:57(learn)
              155583234 3328.624    0.000 3328.624    0.000 {built-in method dropout}
                1732962   20.963    0.000 3114.439    0.002 BayesianNN.py:21(learn)
                5633052   79.611    0.000 2962.869    0.001 BayesianNN.py:61(predict)
              156278316  107.536    0.000 2789.964    0.000 activation.py:713(forward)
              156278316  119.038    0.000 2682.428    0.000 functional.py:1364(leaky_relu)
              156278316 2540.772    0.000 2540.772    0.000 {built-in method torch._C._nn.leaky_relu}
          857950/215274   90.032    0.000 1875.635    0.009 allGraphs.py:202(recursiveExplore)
                 115847    7.214    0.000 1671.564    0.014 allGraphsTrain.py:33(<listcomp>)
               11700648  422.298    0.000 1664.371    0.000 allGraphs.py:114(states)
              117581282 1614.904    0.000 1614.904    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                1848809   15.781    0.000 1443.359    0.001 optimizer.py:84(wrapper)
              104262700 1377.243    0.000 1377.243    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                1848809    7.353    0.000 1369.116    0.001 grad_mode.py:24(decorate_context)
                1848809   40.849    0.000 1344.333    0.001 adam.py:55(step)
                1848809  272.456    0.000 1259.600    0.001 _functional.py:53(adam)
                7366014  870.208    0.000 1114.518    0.000 BayesianNN.py:43(convert_data)
               47673259   50.182    0.000  900.940    0.000 tensor.py:525(__rsub__)
               47673259  841.079    0.000  841.079    0.000 {built-in method rsub}
                1848809    6.878    0.000  818.448    0.000 tensor.py:195(backward)
                1848809    6.779    0.000  811.285    0.000 __init__.py:68(backward)
                1848809  762.886    0.000  762.886    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                 115847    4.003    0.000  668.525    0.006 allGraphs.py:141(transform)
                 115847    0.482    0.000  462.232    0.004 game.py:42(step)
                 115847    0.715    0.000  436.418    0.004 layers.py:827(step)
                 115847   34.305    0.000  417.219    0.004 allGraphsTrain.py:44(<listcomp>)
              575216842  398.795    0.000  398.795    0.000 {built-in method torch._C._get_tracing_state}
        2568022423/2568022421  292.450    0.000  293.674    0.000 {built-in method builtins.len}
                 115847    0.506    0.000  290.505    0.003 agent.py:29(learn)
                 115847    3.124    0.000  289.724    0.003 agent.py:117(_learn)
                 115847    9.475    0.000  286.600    0.002 learner.py:42(Qlearn)
               22649096  257.665    0.000  257.665    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               18429647  237.214    0.000  237.214    0.000 {built-in method zeros}
               22649096  228.890    0.000  228.890    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                 115848   17.233    0.000  218.641    0.002 layers.py:793(update)
                 115847    9.651    0.000  216.294    0.002 layers.py:17(step)
             2351569976  213.582    0.000  213.582    0.000 {method 'values' of 'collections.OrderedDict' objects}
                1848809   34.513    0.000  213.051    0.000 optimizer.py:189(zero_grad)
               11584700   19.418    0.000  205.537    0.000 layer.py:106(move)
               63909166  202.731    0.000  202.731    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              366846281  200.685    0.000  200.685    0.000 module.py:934(__getattr__)
               52324466   32.586    0.000  181.721    0.000 flatten.py:39(forward)
                2072666  177.534    0.000  177.534    0.000 {built-in method tensor}
               11584700  171.631    0.000  171.631    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                1553757    1.480    0.000  157.805    0.000 game.py:38(board)
                 115847  155.078    0.001  155.078    0.001 allGraphsTrain.py:51(<listcomp>)
               11324548  139.935    0.000  139.935    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               11324548  119.419    0.000  119.419    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               11324548  119.123    0.000  119.123    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               11324548  118.349    0.000  118.349    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               50359810  114.118    0.000  114.118    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                 115847   73.921    0.001  109.730    0.001 agent.py:67(modify)
                 974521    8.193    0.000  107.677    0.000 allGraphs.py:167(format)
               11584700   26.446    0.000  101.702    0.000 layers.py:844(check)
                 231694    0.750    0.000   99.701    0.000 network.py:28(forward)
                1848809    2.495    0.000   99.222    0.000 loss.py:527(forward)
                1848809    7.236    0.000   96.727    0.000 functional.py:2898(mse_loss)
              157432043   65.208    0.000   96.413    0.000 _VF.py:25(__getattr__)
               11324548   91.699    0.000   91.699    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               79274602   60.257    0.000   76.447    0.000 types.py:171(__get__)
               79271896   59.144    0.000   73.534    0.000 tensor.py:906(grad)
                 138403    1.453    0.000   70.804    0.001 layers.py:849(restart)
                1848809   68.452    0.000   68.452    0.000 {built-in method torch._C._nn.mse_loss}
               11584700   17.293    0.000   66.655    0.000 layers.py:838(isFree)
                2802398   63.764    0.000   63.764    0.000 {built-in method cat}
                 115847    1.886    0.000   61.503    0.001 agent.py:112(__call__)
                 138403    0.733    0.000   59.045    0.000 level.py:8(__init__)
              405465604   55.316    0.000   55.316    0.000 {built-in method torch._C._has_torch_function_unary}
                 810936   27.724    0.000   49.676    0.000 layer.py:175(NoRock_update)
               76306148   39.180    0.000   49.362    0.000 layer.py:103(isFree)
              159846228   32.384    0.000   48.117    0.000 enum.py:646(__hash__)
               52092772   34.159    0.000   47.908    0.000 container.py:109(__iter__)
               10731869   47.622    0.000   47.622    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                 138403    1.725    0.000   43.941    0.000 levels.py:151(generate)
               11446398    9.870    0.000   41.061    0.000 {built-in method builtins.any}
                 664124    7.089    0.000   40.332    0.000 level.py:41(notUsed)
                3697618    8.244    0.000   39.965    0.000 profiler.py:615(__enter__)
                1848809    7.405    0.000   39.755    0.000 __init__.py:28(_make_grads)
                 463388    1.165    0.000   38.953    0.000 conv.py:398(forward)
              205568690   38.386    0.000   38.386    0.000 {built-in method torch._C._has_torch_function_variadic}
                 463388    0.714    0.000   37.291    0.000 conv.py:390(_conv_forward)
                 463388   36.578    0.000   36.578    0.000 {built-in method conv2d}
                 347541    0.908    0.000   34.863    0.000 tensor.py:575(__iter__)
               11584800    3.664    0.000   34.507    0.000 {built-in method builtins.all}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9651524: <Diamonds1_0.5_NN_2> in cluster <dcc> Done

Job <Diamonds1_0.5_NN_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Tue May 18 21:04:58 2021
Job was executed on host(s) <n-62-20-16>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Tue May 18 21:04:59 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue May 18 21:04:59 2021
Terminated at Wed May 19 07:02:18 2021
Results reported at Wed May 19 07:02:18 2021

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

    CPU time :                                   35619.28 sec.
    Max Memory :                                 3436 MB
    Average Memory :                             2981.19 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               12948.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35945 sec.
    Turnaround time :                            35840 sec.

The output (if any) is above this job summary.

