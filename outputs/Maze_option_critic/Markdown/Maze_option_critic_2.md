[W NNPACK.cpp:80] Could not initialize NNPACK! Reason: Unsupported hardware.

# Parameters

    Name :                      Maze_option_critic-2
    Main :                      option_critic_run
    Level :                     Levels.Maze
    Failed actions chance :     0.0
    Hours :                     72.0
    Batch :                     25
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
    Minutes used :              4315 minutes.
    Hours used :                71 hours.

# Profiling


      33213919772 function calls (32154723176 primitive calls) in 258890.00 seconds

##    Ordered by: cumulative time
   List reduced from 441 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.580 258900.580 {built-in method builtins.exec}
                      1    0.344    0.344 258900.580 258900.580 <string>:1(<module>)
                      1 3970.706 3970.706 258900.236 258900.236 optionCritic.py:195(option_critic_run)
        1399053800/344754461 10437.003    0.000 111921.902    0.000 module.py:866(_call_impl)
               37667000 10140.878    0.000 110023.535    0.003 optionCritic.py:143(actor_loss_fn)
              117144371  766.773    0.000 102513.916    0.001 optionCritic.py:70(get_state)
              117144371 2841.341    0.000 99383.062    0.001 container.py:117(forward)
                1506680   11.682    0.000 79609.252    0.053 tensor.py:195(backward)
                1506680   14.827    0.000 79597.268    0.053 __init__.py:68(backward)
                1506680 79542.949    0.053 79542.949    0.053 {method 'run_backward' of 'torch._C._EngineBase' objects}
              234288742  900.779    0.000 60383.890    0.000 conv.py:398(forward)
              234288742  395.150    0.000 59141.650    0.000 conv.py:390(_conv_forward)
              234288742 58746.500    0.000 58746.500    0.000 {built-in method conv2d}
               37667000 4010.167    0.000 23781.839    0.001 optionCritic.py:91(get_action)
              461898832 1624.124    0.000 22200.666    0.000 linear.py:93(forward)
              461898832  618.401    0.000 19953.534    0.000 functional.py:1737(linear)
              461898832 19204.411    0.000 19204.411    0.000 {built-in method torch._C._nn.linear}
               37667000 1224.053    0.000 13237.201    0.000 optionCritic.py:80(predict_option_termination)
               75334000 1126.267    0.000 8696.511    0.000 distribution.py:34(__init__)
              351433113  446.525    0.000 8174.929    0.000 activation.py:713(forward)
               37667000  628.038    0.000 7767.528    0.000 categorical.py:115(log_prob)
              351433113  463.932    0.000 7728.403    0.000 functional.py:1364(leaky_relu)
              351433113 7168.539    0.000 7168.539    0.000 {built-in method torch._C._nn.leaky_relu}
               37667000  919.022    0.000 7055.204    0.000 categorical.py:49(__init__)
              114232420  467.865    0.000 6525.066    0.000 optionCritic.py:77(get_Q)
                 376670   86.460    0.000 6501.905    0.017 optionCritic.py:116(critic_loss_fn)
               75710670  469.680    0.000 5306.294    0.000 optionCritic.py:88(get_terminations)
               37667000  294.405    0.000 4695.517    0.000 bernoulli.py:34(__init__)
               37667000 2919.205    0.000 4386.829    0.000 constraints.py:398(check)
                1506680   31.128    0.000 4224.889    0.003 optimizer.py:84(wrapper)
                1506680   16.316    0.000 4100.362    0.003 grad_mode.py:24(decorate_context)
                1506680  107.004    0.000 4052.814    0.003 rmsprop.py:56(step)
                1506680  158.132    0.000 3827.226    0.003 _functional.py:203(rmsprop)
               37667000  476.162    0.000 3261.424    0.000 distribution.py:240(_validate_sample)
                1506680    9.453    0.000 3117.750    0.002 game.py:41(step)
                1506680   13.902    0.000 3000.339    0.002 layers.py:718(step)
              117144371  167.747    0.000 2359.954    0.000 activation.py:101(forward)
               37667000 1111.159    0.000 2290.492    0.000 categorical.py:123(entropy)
               37667000 2204.279    0.000 2204.279    0.000 constraints.py:249(check)
              117144371  158.424    0.000 2192.207    0.000 functional.py:1195(relu)
               37667000 2077.039    0.000 2077.039    0.000 constraints.py:364(check)
              117144371 2003.815    0.000 2003.815    0.000 {built-in method relu}
              113001000  225.469    0.000 1918.901    0.000 utils.py:106(__get__)
              263669000 1872.180    0.000 1872.180    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
             1415627280 1814.586    0.000 1814.586    0.000 {built-in method torch._C._get_tracing_state}
               21093514 1774.471    0.000 1774.471    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               37667000  325.811    0.000 1758.781    0.000 bernoulli.py:86(sample)
              113754340  186.870    0.000 1705.829    0.000 tensor.py:525(__rsub__)
              113001000 1643.716    0.000 1643.716    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
              117144371  132.293    0.000 1629.013    0.000 flatten.py:39(forward)
             1812659540 1626.459    0.000 1626.611    0.000 module.py:934(__getattr__)
               37667000   74.451    0.000 1529.200    0.000 categorical.py:88(logits)
              113377670 1504.097    0.000 1504.097    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
                1506681  148.083    0.000 1501.124    0.001 layers.py:684(update)
              117144371 1496.720    0.000 1496.720    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              113754340 1485.523    0.000 1485.523    0.000 {built-in method rsub}
                1506680   65.257    0.000 1479.420    0.001 layers.py:17(step)
               37667000  382.380    0.000 1478.183    0.000 categorical.py:108(sample)
               37667000   82.468    0.000 1454.749    0.000 utils.py:82(probs_to_logits)
               37667000  110.177    0.000 1407.316    0.000 layer.py:98(move)
               75334000  433.340    0.000 1314.554    0.000 functional.py:46(broadcast_tensors)
               75710670 1212.445    0.000 1212.445    0.000 {method 'max' of 'torch._C._TensorBase' objects}
              113001000 1127.680    0.000 1127.680    0.000 {method 'all' of 'torch._C._TensorBase' objects}
             6091838764 1083.798    0.000 1097.894    0.000 {built-in method builtins.len}
               16573480   47.398    0.000 1055.628    0.000 tensor.py:575(__iter__)
               16573480  973.239    0.000  973.239    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
             5713359571  945.574    0.000  945.574    0.000 {method 'values' of 'collections.OrderedDict' objects}
               37667000  179.026    0.000  926.674    0.000 utils.py:11(broadcast_all)
               37667000  204.885    0.000  903.127    0.000 layers.py:735(check)
               37667000  149.501    0.000  893.943    0.000 utils.py:77(clamp_probs)
               37667000  846.844    0.000  846.844    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               13779455  364.004    0.000  768.433    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               75334000  750.060    0.000  750.060    0.000 {built-in method broadcast_tensors}
               37667000  744.441    0.000  744.441    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
              114131010  734.678    0.000  734.678    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
                1506680   77.084    0.000  714.872    0.000 replaybuffer.py:34(save_option_critic)
               37667000  700.070    0.000  700.070    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
                 376670  535.849    0.001  695.444    0.002 replaybuffer.py:42(sample_option_critic)
              226755340  645.039    0.000  645.039    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               37667000  642.945    0.000  642.945    0.000 {built-in method clamp}
               75334000  618.172    0.000  618.172    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               38145080  597.855    0.000  597.855    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                 478107   11.839    0.000  561.215    0.001 layers.py:740(restart)
               21093514  553.799    0.000  553.799    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               37667000  547.319    0.000  547.319    0.000 {built-in method bernoulli}
               21093514  513.113    0.000  513.113    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               37667000  487.438    0.000  487.438    0.000 {built-in method all}
                1506680   92.412    0.000  484.327    0.000 optimizer.py:189(zero_grad)
                 478107    6.933    0.000  480.987    0.001 level.py:8(__init__)
               37667000  478.339    0.000  478.339    0.000 {built-in method log}
               37667000  475.397    0.000  475.397    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
               21093514  445.885    0.000  445.885    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                 652474   65.783    0.000  438.325    0.001 levels.py:9(generate)
               13779455   23.733    0.000  404.429    0.000 <__array_function__ internals>:2(prod)
               12053448  248.606    0.000  403.246    0.000 layer.py:167(NoRock_update)
               21093514  381.825    0.000  381.825    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               13779455   22.744    0.000  376.312    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
               13779455   36.715    0.000  353.568    0.000 fromnumeric.py:2912(prod)
               37667000  347.332    0.000  347.332    0.000 {built-in method multinomial}
               10170094  343.253    0.000  343.253    0.000 {built-in method tensor}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9601877: <Maze_option_critic_2> in cluster <dcc> Done

Job <Maze_option_critic_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Thu Apr 29 21:41:18 2021
Job was executed on host(s) <n-62-23-21>, in queue <hpc>, as user <s183914> in cluster <dcc> at Thu Apr 29 21:41:20 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Apr 29 21:41:20 2021
Terminated at Sun May  2 21:36:23 2021
Results reported at Sun May  2 21:36:23 2021

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

python main.py $LSB_PROJECT_NAME
------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   258896.88 sec.
    Max Memory :                                 904 MB
    Average Memory :                             889.11 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15480.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258959 sec.
    Turnaround time :                            258905 sec.

The output (if any) is above this job summary.

