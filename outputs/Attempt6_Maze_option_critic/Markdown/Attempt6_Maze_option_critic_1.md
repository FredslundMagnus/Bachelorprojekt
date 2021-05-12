
# Parameters

    Name :                      Attempt6_Maze_option_critic-1
    Main :                      option_critic_run
    Level :                     Levels.Maze
    Failed actions chance :     0
    Use model :                 True
    Depth :                     3
    Model explore :             1000000
    Samples :                   5
    Hours :                     72.0
    Batch :                     32
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.UCB1
    Network1 :                  Networks.Teleporter
    K1 :                        5000000
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
    K2 :                        1000000
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
    Softmax cap :               0.02
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
    Minutes used :              4315 minutes.
    Hours used :                71 hours.

# Profiling


      26303887267 function calls (25475185574 primitive calls) in 258890.09 seconds

##    Ordered by: cumulative time
   List reduced from 442 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.778 258900.778 {built-in method builtins.exec}
                      1    0.318    0.318 258900.778 258900.778 <string>:1(<module>)
                      1 3031.468 3031.468 258900.459 258900.459 optionCritic.py:195(option_critic_run)
                 929037    6.908    0.000 157469.756    0.169 tensor.py:195(backward)
                 929037    9.033    0.000 157462.724    0.169 __init__.py:68(backward)
                 929037 157434.817    0.169 157434.817    0.169 {method 'run_backward' of 'torch._C._EngineBase' objects}
        1097087531/271405895 5291.310    0.000 63685.833    0.000 module.py:866(_call_impl)
               29729184 4493.400    0.000 60884.800    0.002 optionCritic.py:143(actor_loss_fn)
               91742404  473.041    0.000 59721.988    0.001 optionCritic.py:70(get_state)
               91742404 1223.762    0.000 57933.703    0.001 container.py:117(forward)
              183484808  482.431    0.000 36640.218    0.000 conv.py:398(forward)
              183484808  285.974    0.000 35954.841    0.000 conv.py:390(_conv_forward)
              183484808 35668.867    0.000 35668.867    0.000 {built-in method conv2d}
              363148299  857.326    0.000 13115.269    0.000 linear.py:93(forward)
              363148299  351.273    0.000 11896.244    0.000 functional.py:1737(linear)
              363148299 11462.902    0.000 11462.902    0.000 {built-in method torch._C._nn.linear}
               29729184 1715.400    0.000 10218.310    0.000 optionCritic.py:91(get_action)
               29729184  640.320    0.000 7555.087    0.000 optionCritic.py:80(predict_option_termination)
                 929037   20.656    0.000 5830.631    0.006 optimizer.py:84(wrapper)
                 929037   12.464    0.000 5755.117    0.006 grad_mode.py:24(decorate_context)
                 929037   55.378    0.000 5722.948    0.006 adam.py:55(step)
                 929037  333.460    0.000 5607.939    0.006 _functional.py:53(adam)
               59458368  647.294    0.000 4118.747    0.000 distribution.py:34(__init__)
              275227212  273.714    0.000 3697.330    0.000 activation.py:713(forward)
              275227212  283.014    0.000 3423.616    0.000 functional.py:1364(leaky_relu)
               29729184  285.962    0.000 3417.581    0.000 categorical.py:115(log_prob)
                 232259   39.027    0.000 3354.931    0.014 optionCritic.py:116(critic_loss_fn)
              275227212 3081.576    0.000 3081.576    0.000 {built-in method torch._C._nn.leaky_relu}
               29729184  247.647    0.000 2996.332    0.000 bernoulli.py:34(__init__)
               90243680  206.842    0.000 2985.246    0.000 optionCritic.py:77(get_Q)
               29729184  383.305    0.000 2863.026    0.000 categorical.py:49(__init__)
               59690627  215.381    0.000 2297.829    0.000 optionCritic.py:88(get_terminations)
                 929037    4.943    0.000 2207.782    0.002 game.py:42(step)
                 929037    9.003    0.000 2141.986    0.002 layers.py:827(step)
               29729184 1177.123    0.000 1752.951    0.000 constraints.py:398(check)
               29729184  240.551    0.000 1382.185    0.000 distribution.py:240(_validate_sample)
               26013024 1243.269    0.000 1243.269    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               29729184  230.823    0.000 1131.865    0.000 bernoulli.py:86(sample)
                 929038   84.114    0.000 1121.136    0.001 layers.py:793(update)
               29729184 1113.244    0.000 1113.244    0.000 constraints.py:364(check)
               13006512 1105.587    0.000 1105.587    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               91742404  122.980    0.000 1071.394    0.000 activation.py:101(forward)
                 929037   40.958    0.000 1007.929    0.001 layers.py:17(step)
             1424251320  978.106    0.000  978.174    0.000 module.py:934(__getattr__)
               29729184   64.257    0.000  963.131    0.000 layer.py:106(move)
               13006512  961.019    0.000  961.019    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               91742404  102.751    0.000  948.414    0.000 functional.py:1195(relu)
               29729184  489.353    0.000  939.030    0.000 categorical.py:123(entropy)
              208104288  928.566    0.000  928.566    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               29729184  896.264    0.000  896.264    0.000 constraints.py:249(check)
               89187552  121.481    0.000  862.010    0.000 utils.py:106(__get__)
               91742404   88.529    0.000  845.569    0.000 flatten.py:39(forward)
               91742404  829.598    0.000  829.598    0.000 {built-in method relu}
               89652070  102.851    0.000  828.230    0.000 tensor.py:525(__rsub__)
               59458368  284.291    0.000  782.064    0.000 functional.py:46(broadcast_tensors)
               91742404  757.040    0.000  757.040    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               89652070  709.892    0.000  709.892    0.000 {built-in method rsub}
               29729184  140.553    0.000  679.660    0.000 utils.py:11(broadcast_all)
               59690627  678.528    0.000  678.528    0.000 {method 'max' of 'torch._C._TensorBase' objects}
               26013024  671.627    0.000  671.627    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               29729184  185.690    0.000  670.472    0.000 categorical.py:108(sample)
               10219407   23.774    0.000  651.224    0.000 tensor.py:575(__iter__)
               13006512  647.779    0.000  647.779    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               29729184   34.071    0.000  645.203    0.000 categorical.py:88(logits)
               89419811  643.856    0.000  643.856    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
             1107306938  641.273    0.000  641.273    0.000 {built-in method torch._C._get_tracing_state}
               13006512  639.921    0.000  639.921    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               10219407  613.075    0.000  613.075    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               29729184   35.538    0.000  611.132    0.000 utils.py:82(probs_to_logits)
             4780078739  602.454    0.000  609.486    0.000 {built-in method builtins.len}
               29729184  137.312    0.000  608.104    0.000 layers.py:844(check)
               89187552  592.062    0.000  592.062    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 591641   11.296    0.000  576.487    0.001 layers.py:849(restart)
               89187552  515.682    0.000  515.682    0.000 {method 'all' of 'torch._C._TensorBase' objects}
             4480092528  499.476    0.000  499.476    0.000 {method 'values' of 'collections.OrderedDict' objects}
                 591641    7.025    0.000  497.090    0.001 level.py:8(__init__)
                 232259  365.966    0.002  453.050    0.002 replaybuffer.py:42(sample_option_critic)
                 806015   63.098    0.000  447.311    0.001 levels.py:9(generate)
               29729184  447.056    0.000  447.056    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               59458368  418.332    0.000  418.332    0.000 {built-in method broadcast_tensors}
                 929037   42.608    0.000  368.726    0.000 replaybuffer.py:34(save_option_critic)
               29729184   75.242    0.000  362.797    0.000 utils.py:77(clamp_probs)
               29729184  342.544    0.000  342.544    0.000 {built-in method bernoulli}
               89884329  332.608    0.000  332.608    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               30320794  295.436    0.000  295.436    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               29729184  289.296    0.000  289.296    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
               29729184  287.555    0.000  287.555    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
              178839622  282.029    0.000  282.029    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               29729184   52.706    0.000  262.813    0.000 layers.py:838(isFree)
                7432304  151.343    0.000  252.240    0.000 layer.py:175(NoRock_update)
               59458368  251.532    0.000  251.532    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                 929037   43.928    0.000  248.925    0.000 optimizer.py:189(zero_grad)
               29729184  238.694    0.000  238.694    0.000 {built-in method clamp}
              395677063  138.391    0.000  222.314    0.000 {built-in method builtins.isinstance}
               29729184  212.797    0.000  212.797    0.000 {built-in method log}
              180372126  175.316    0.000  210.107    0.000 layer.py:103(isFree)
               29729184  209.234    0.000  209.234    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
               91742418  205.916    0.000  205.916    0.000 {method 'to' of 'torch._C._TensorBase' objects}
               29729184  112.748    0.000  199.466    0.000 layers.py:168(check)
               89781051  198.687    0.000  198.687    0.000 {method 'item' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9624166: <Attempt6_Maze_option_critic_1> in cluster <dcc> Done

Job <Attempt6_Maze_option_critic_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun May  9 01:22:28 2021
Job was executed on host(s) <n-62-11-61>, in queue <hpc>, as user <s183914> in cluster <dcc> at Sun May  9 01:22:29 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun May  9 01:22:29 2021
Terminated at Wed May 12 01:17:34 2021
Results reported at Wed May 12 01:17:34 2021

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

    CPU time :                                   258288.47 sec.
    Max Memory :                                 946 MB
    Average Memory :                             937.59 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15438.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258956 sec.
    Turnaround time :                            258906 sec.

The output (if any) is above this job summary.

