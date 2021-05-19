
# Parameters

    Name :                      Diamonds2_0.5_NN-0
    Main :                      graphTrain
    Level :                     Levels.Causal5
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


      14740914508 function calls (13980338514 primitive calls) in 35720.39 seconds

##    Ordered by: cumulative time
   List reduced from 486 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35720.395 35720.395 {built-in method builtins.exec}
                      1    0.001    0.001 35720.395 35720.395 <string>:1(<module>)
                      1   31.325   31.325 35720.394 35720.394 allGraphsTrain.py:13(graphTrain)
                 109894  109.522    0.001 27805.566    0.253 allGraphsTrain.py:40(<listcomp>)
                 716148    3.647    0.000 27690.021    0.039 allGraphs.py:179(getInterventionsmodel)
        65256572/551879 4540.653    0.000 26076.512    0.047 allGraphs.py:186(recursiveBEST)
               62516996 2229.905    0.000 19584.010    0.000 BayesianNN.py:65(predict_no_convert)
               69303538  178.601    0.000 19113.832    0.000 BayesianNN.py:18(forward)
        766277195/71043935 2671.483    0.000 19006.953    0.000 module.py:866(_call_impl)
               69523326  848.797    0.000 18498.533    0.000 container.py:117(forward)
              208350190  384.614    0.000 7287.876    0.000 linear.py:93(forward)
              208350190  163.259    0.000 6736.988    0.000 functional.py:1737(linear)
              208350190 6532.259    0.000 6532.259    0.000 {built-in method torch._C._nn.linear}
                 109894 1071.946    0.010 4398.520    0.040 allGraphs.py:156(transformNot)
              207910614  157.649    0.000 4205.456    0.000 dropout.py:57(forward)
              207910614  557.435    0.000 4047.807    0.000 functional.py:1059(dropout)
              207910614 3315.847    0.000 3315.847    0.000 {built-in method dropout}
              208569978  135.991    0.000 2688.941    0.000 activation.py:713(forward)
              208569978  150.475    0.000 2552.950    0.000 functional.py:1364(leaky_relu)
              208569978 2373.006    0.000 2373.006    0.000 {built-in method torch._C._nn.leaky_relu}
                5375827   70.316    0.000 2337.344    0.000 BayesianNN.py:61(predict)
                1410715   18.054    0.000 2124.458    0.002 BayesianNN.py:57(learn)
                1410715   15.880    0.000 1912.949    0.001 BayesianNN.py:21(learn)
              155263787 1793.919    0.000 1793.919    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                 109894    8.650    0.000 1741.252    0.016 allGraphsTrain.py:33(<listcomp>)
               11099395  372.017    0.000 1732.626    0.000 allGraphs.py:114(states)
          801895/164269   69.380    0.000 1521.263    0.009 allGraphs.py:202(recursiveExplore)
              142862800 1275.179    0.000 1275.179    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
               65452213   63.428    0.000  977.456    0.000 tensor.py:525(__rsub__)
                6786542  749.471    0.000  924.457    0.000 BayesianNN.py:43(convert_data)
               65452213  901.996    0.000  901.996    0.000 {built-in method rsub}
                1520609   11.423    0.000  832.848    0.001 optimizer.py:84(wrapper)
                1520609    6.021    0.000  779.064    0.001 grad_mode.py:24(decorate_context)
                1520609   33.480    0.000  758.899    0.000 adam.py:55(step)
                1520609  156.791    0.000  688.175    0.000 _functional.py:53(adam)
                1520609    5.757    0.000  510.333    0.000 tensor.py:195(backward)
                1520609    5.625    0.000  504.352    0.000 __init__.py:68(backward)
                 109894    0.458    0.000  476.440    0.004 game.py:42(step)
                1520609  470.177    0.000  470.177    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                 109894    0.637    0.000  452.708    0.004 layers.py:827(step)
                 109894    3.732    0.000  393.134    0.004 allGraphs.py:141(transform)
              766606877  374.402    0.000  374.402    0.000 {built-in method torch._C._get_tracing_state}
        3400264642/3400264640  337.618    0.000  338.711    0.000 {built-in method builtins.len}
                 109894   20.757    0.000  286.976    0.003 allGraphsTrain.py:44(<listcomp>)
             3134632106  274.946    0.000  274.946    0.000 {method 'values' of 'collections.OrderedDict' objects}
              488514078  259.835    0.000  259.835    0.000 module.py:934(__getattr__)
                 109894    9.129    0.000  252.410    0.002 layers.py:17(step)
               10989400   18.756    0.000  242.180    0.000 layer.py:106(move)
                 109894    0.500    0.000  209.777    0.002 agent.py:29(learn)
                 109894    2.793    0.000  209.021    0.002 agent.py:117(_learn)
                 109894    6.939    0.000  206.228    0.002 learner.py:42(Qlearn)
                 109895   16.648    0.000  198.978    0.002 layers.py:793(update)
               69743114   41.873    0.000  191.755    0.000 flatten.py:39(forward)
                1759428  184.987    0.000  184.987    0.000 {built-in method tensor}
               80732514  179.905    0.000  179.905    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               16614303  155.265    0.000  155.265    0.000 {built-in method zeros}
                1265619    1.232    0.000  144.388    0.000 game.py:38(board)
              209431223   99.392    0.000  142.165    0.000 _VF.py:25(__getattr__)
               18686884  133.187    0.000  133.187    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                1520609   24.972    0.000  132.893    0.000 optimizer.py:189(zero_grad)
               10989400   31.998    0.000  131.254    0.000 layers.py:844(check)
               18686884  119.861    0.000  119.861    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               68112611  117.436    0.000  117.436    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               10989400  112.411    0.000  112.411    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
              108169448   80.927    0.000  104.263    0.000 types.py:171(__get__)
                 109894   90.242    0.001   90.242    0.001 allGraphsTrain.py:51(<listcomp>)
                 716148    5.842    0.000   88.280    0.000 allGraphs.py:167(format)
                 109894   53.858    0.000   82.230    0.001 agent.py:67(modify)
                 219788    0.755    0.000   79.678    0.000 network.py:28(forward)
                9343442   79.277    0.000   79.277    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               10989400   19.134    0.000   74.676    0.000 layers.py:838(isFree)
                1520609    2.057    0.000   72.471    0.000 loss.py:527(forward)
                1520609    5.645    0.000   70.414    0.000 functional.py:2898(mse_loss)
              493848052   69.536    0.000   69.536    0.000 {built-in method torch._C._has_torch_function_unary}
               69523326   47.805    0.000   69.061    0.000 container.py:109(__iter__)
                9343442   66.580    0.000   66.580    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                9343442   65.705    0.000   65.705    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                9343442   64.113    0.000   64.113    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               65404154   47.118    0.000   58.792    0.000 tensor.py:906(grad)
                 989055   30.562    0.000   56.480    0.000 layer.py:175(NoRock_update)
               88364364   44.291    0.000   55.541    0.000 layer.py:103(isFree)
              275323012   53.836    0.000   53.836    0.000 {built-in method torch._C._has_torch_function_variadic}
              179937255   36.812    0.000   53.689    0.000 enum.py:646(__hash__)
                2770292   51.547    0.000   51.547    0.000 {built-in method cat}
                 109894    1.723    0.000   50.261    0.000 agent.py:112(__call__)
                1520609   48.735    0.000   48.735    0.000 {built-in method torch._C._nn.mse_loss}
                9343442   48.576    0.000   48.576    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               10911871   11.199    0.000   48.083    0.000 {built-in method builtins.any}
                  77630    1.028    0.000   45.578    0.001 layers.py:849(restart)
              209540420   42.838    0.000   42.838    0.000 {built-in method builtins.getattr}
                  77630    0.485    0.000   37.935    0.000 level.py:8(__init__)
              109118700   30.009    0.000   36.884    0.000 layers.py:809(<genexpr>)
                  77630    1.360    0.000   33.700    0.000 levels.py:249(generate)
                 439576    1.126    0.000   31.681    0.000 conv.py:398(forward)
                9802191   31.255    0.000   31.255    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                 504949    5.331    0.000   30.915    0.000 level.py:41(notUsed)
                 439576    0.727    0.000   30.063    0.000 conv.py:390(_conv_forward)
                 439576   29.336    0.000   29.336    0.000 {built-in method conv2d}
               10989500    2.316    0.000   27.401    0.000 {built-in method builtins.all}
                1520609    5.771    0.000   26.994    0.000 __init__.py:28(_make_grads)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9651526: <Diamonds2_0.5_NN_0> in cluster <dcc> Done

Job <Diamonds2_0.5_NN_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Tue May 18 21:04:58 2021
Job was executed on host(s) <n-62-20-15>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Tue May 18 21:04:59 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue May 18 21:04:59 2021
Terminated at Wed May 19 07:00:27 2021
Results reported at Wed May 19 07:00:27 2021

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

    CPU time :                                   35614.31 sec.
    Max Memory :                                 3253 MB
    Average Memory :                             2910.67 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13131.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35728 sec.
    Turnaround time :                            35729 sec.

The output (if any) is above this job summary.

