
# Parameters

    Name :                      Diamonds4_0.5_NN-0
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
    Num :                       0
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      16366790740 function calls (15533612345 primitive calls) in 35703.46 seconds

##    Ordered by: cumulative time
   List reduced from 486 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35703.465 35703.465 {built-in method builtins.exec}
                      1    0.002    0.002 35703.465 35703.465 <string>:1(<module>)
                      1   35.822   35.822 35703.463 35703.463 allGraphsTrain.py:13(graphTrain)
                 140654  132.381    0.001 27462.956    0.195 allGraphsTrain.py:40(<listcomp>)
                1445867    6.451    0.000 27321.433    0.019 allGraphs.py:179(getInterventionsmodel)
        72053172/1252671 4541.336    0.000 26026.562    0.021 allGraphs.py:186(recursiveBEST)
               67017456 2198.791    0.000 19083.373    0.000 BayesianNN.py:65(predict_no_convert)
               75900677  175.253    0.000 19035.250    0.000 BayesianNN.py:18(forward)
        840454520/78634670 2637.348    0.000 18980.270    0.000 module.py:866(_call_impl)
               76181985  847.420    0.000 18426.982    0.000 container.py:117(forward)
              228264647  368.576    0.000 7317.245    0.000 linear.py:93(forward)
              228264647  151.361    0.000 6786.656    0.000 functional.py:1737(linear)
              228264647 6599.275    0.000 6599.275    0.000 {built-in method torch._C._nn.linear}
                 140654  916.903    0.007 4724.095    0.034 allGraphs.py:156(transformNot)
              227702031  151.072    0.000 4211.407    0.000 dropout.py:57(forward)
              227702031  534.487    0.000 4060.335    0.000 functional.py:1059(dropout)
              227702031 3368.618    0.000 3368.618    0.000 {built-in method dropout}
                2312031   28.039    0.000 3080.049    0.001 BayesianNN.py:57(learn)
                2312031   23.892    0.000 2827.421    0.001 BayesianNN.py:21(learn)
              228545955  128.177    0.000 2660.330    0.000 activation.py:713(forward)
              228545955  145.925    0.000 2532.153    0.000 functional.py:1364(leaky_relu)
                6571190   81.476    0.000 2448.873    0.000 BayesianNN.py:61(predict)
              228545955 2359.944    0.000 2359.944    0.000 {built-in method torch._C._nn.leaky_relu}
              142967551 1549.638    0.000 1549.638    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                 140654    8.245    0.000 1373.030    0.010 allGraphsTrain.py:33(<listcomp>)
               14206155  299.016    0.000 1364.795    0.000 allGraphs.py:114(states)
                2452685   16.685    0.000 1206.434    0.000 optimizer.py:84(wrapper)
          750825/193196   55.758    0.000 1139.660    0.006 allGraphs.py:202(recursiveExplore)
                2452685    8.882    0.000 1127.020    0.000 grad_mode.py:24(decorate_context)
                2452685   48.762    0.000 1098.141    0.000 adam.py:55(step)
              126589000 1019.320    0.000 1019.320    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                2452685  226.321    0.000  996.336    0.000 _functional.py:53(adam)
               71498784   59.817    0.000  962.640    0.000 tensor.py:525(__rsub__)
               71498784  891.789    0.000  891.789    0.000 {built-in method rsub}
                8883221  674.732    0.000  874.045    0.000 BayesianNN.py:43(convert_data)
                2452685    7.802    0.000  746.975    0.000 tensor.py:195(backward)
                2452685    7.957    0.000  738.873    0.000 __init__.py:68(backward)
                2452685  689.041    0.000  689.041    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                 140654    4.706    0.000  625.448    0.004 allGraphs.py:141(transform)
                 140654    0.536    0.000  495.170    0.004 game.py:42(step)
                 140654    0.751    0.000  468.298    0.003 layers.py:827(step)
              840876482  365.857    0.000  365.857    0.000 {built-in method torch._C._get_tracing_state}
                 140654   24.619    0.000  338.542    0.002 allGraphsTrain.py:44(<listcomp>)
        3729337732/3729337730  332.822    0.000  334.073    0.000 {built-in method builtins.len}
             3438000065  260.350    0.000  260.350    0.000 {method 'values' of 'collections.OrderedDict' objects}
              536149135  254.136    0.000  254.136    0.000 module.py:934(__getattr__)
                 140654    0.583    0.000  246.320    0.002 agent.py:29(learn)
                 140654    3.503    0.000  245.423    0.002 agent.py:117(_learn)
                 140654    8.161    0.000  241.920    0.002 learner.py:42(Qlearn)
                 140654   10.368    0.000  238.645    0.002 layers.py:17(step)
                 140655   18.834    0.000  227.952    0.002 layers.py:793(update)
               14065400   22.003    0.000  227.127    0.000 layer.py:106(move)
                2772102  222.013    0.000  222.013    0.000 {built-in method tensor}
                2149138    1.807    0.000  203.139    0.000 game.py:38(board)
               29994836  193.828    0.000  193.828    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               76463293   44.013    0.000  193.158    0.000 flatten.py:39(forward)
               22671813  191.219    0.000  191.219    0.000 {built-in method zeros}
                2452685   33.797    0.000  189.186    0.000 optimizer.py:189(zero_grad)
               90528693  184.577    0.000  184.577    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               29994836  173.922    0.000  173.922    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                1445867   10.303    0.000  148.185    0.000 allGraphs.py:167(format)
               14065400  130.860    0.000  130.860    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
              230154716   89.924    0.000  126.578    0.000 _VF.py:25(__getattr__)
               73869954  119.895    0.000  119.895    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               14997418  113.735    0.000  113.735    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               14065400   28.572    0.000  110.604    0.000 layers.py:844(check)
                 140654  105.430    0.001  105.430    0.001 allGraphsTrain.py:51(<listcomp>)
                2452685    3.008    0.000  100.656    0.000 loss.py:527(forward)
              110559847   78.916    0.000   99.762    0.000 types.py:171(__get__)
                 140654   64.342    0.000   98.312    0.001 agent.py:67(modify)
                2452685    8.283    0.000   97.647    0.000 functional.py:2898(mse_loss)
               14997418   97.326    0.000   97.326    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               14997418   94.244    0.000   94.244    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                 281308    0.797    0.000   93.963    0.000 network.py:28(forward)
               14997418   93.005    0.000   93.005    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              104981986   66.646    0.000   83.049    0.000 tensor.py:906(grad)
                 157562    1.583    0.000   77.527    0.000 layers.py:849(restart)
               14065400   18.302    0.000   74.850    0.000 layers.py:838(isFree)
               14997418   71.664    0.000   71.664    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              580086994   67.654    0.000   67.654    0.000 {built-in method torch._C._has_torch_function_unary}
                2452685   66.206    0.000   66.206    0.000 {built-in method torch._C._nn.mse_loss}
                 157562    0.764    0.000   65.256    0.000 level.py:8(__init__)
               76181985   43.118    0.000   61.372    0.000 container.py:109(__iter__)
                 140654    2.092    0.000   58.866    0.000 agent.py:112(__call__)
               92644679   46.148    0.000   56.548    0.000 layer.py:103(isFree)
                 984585   30.709    0.000   55.320    0.000 layer.py:175(NoRock_update)
              183065963   33.733    0.000   49.787    0.000 enum.py:646(__hash__)
              302216116   47.463    0.000   47.463    0.000 {built-in method torch._C._has_torch_function_variadic}
                 157562    1.827    0.000   45.443    0.000 levels.py:456(generate)
               13907939   10.526    0.000   43.638    0.000 {built-in method builtins.any}
                2511824   43.525    0.000   43.525    0.000 {built-in method cat}
                 421962    0.948    0.000   42.347    0.000 tensor.py:575(__iter__)
                 756249    7.366    0.000   41.589    0.000 level.py:41(notUsed)
                 421962   40.571    0.000   40.571    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
                2452685    8.779    0.000   39.758    0.000 __init__.py:28(_make_grads)
                4905370    8.317    0.000   39.219    0.000 profiler.py:615(__enter__)
                 562616    1.292    0.000   38.117    0.000 conv.py:398(forward)
               12732472   37.625    0.000   37.625    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              230276077   36.719    0.000   36.719    0.000 {built-in method builtins.getattr}
                 562616    0.840    0.000   36.259    0.000 conv.py:390(_conv_forward)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9651532: <Diamonds4_0.5_NN_0> in cluster <dcc> Done

Job <Diamonds4_0.5_NN_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Tue May 18 21:04:58 2021
Job was executed on host(s) <n-62-20-2>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed May 19 16:59:14 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 19 16:59:14 2021
Terminated at Thu May 20 02:54:21 2021
Results reported at Thu May 20 02:54:21 2021

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

    CPU time :                                   35619.02 sec.
    Max Memory :                                 3778 MB
    Average Memory :                             3221.54 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               12606.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35708 sec.
    Turnaround time :                            107363 sec.

The output (if any) is above this job summary.

