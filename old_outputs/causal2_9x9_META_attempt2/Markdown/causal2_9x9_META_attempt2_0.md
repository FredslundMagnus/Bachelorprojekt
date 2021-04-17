
# Parameters

    Name :                      causal2_9x9_META_attempt2-0
    Main :                      metateleport
    Level :                     Levels.Causal2
    Hours :                     11.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Network1 :                  Networks.Teleporter
    Network2 :                  Networks.Mini
    Learner1 :                  Learners.Qlearn
    Learner2 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Exploration2 :              Explorations.epsilonGreedy
    Layer blocks :              True
    Layer goal :                True
    Layer gold :                True
    Layer keys :                False
    Layer door :                False
    Layer holder :              False
    Layer putter :              False
    Layer rock :                True
    Layer dirt :                True
    Layer diamond1 :            True
    Layer diamond2 :            True
    Layer diamond3 :            True
    Layer diamond4 :            True
    Layer reddoors :            False
    Layer redkeys :             False
    Layer bluedoors :           False
    Layer bluekeys :            False
    K :                         200000
    Epsilon cap :               0.1
    Softmax cap :               0.025
    Gamma :                     0.98
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.03
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Minutes used :              655 minutes.
    Hours used :                10 hours.

# Profiling


      28629732879 function calls (28458936784 primitive calls) in 39315.78 seconds

##    Ordered by: cumulative time
   List reduced from 473 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 39315.783 39315.783 {built-in method builtins.exec}
                      1    5.277    5.277 39315.783 39315.783 <string>:1(<module>)
                      1  134.906  134.906 39310.506 39310.506 main.py:14(metateleport)
                5582562   18.773    0.000 12879.597    0.002 agent.py:27(learn)
                5582562  321.676    0.000 10372.355    0.002 learner.py:42(Qlearn)
                3721708  125.430    0.000 9646.370    0.003 agent.py:51(_learn)
                1860854    8.068    0.000 8178.371    0.004 game.py:27(step)
                1860854   10.728    0.000 7763.679    0.004 layers.py:475(step)
                3721708 5816.634    0.002 7004.293    0.002 replaybuffer.py:23(sample_data)
        191230109/20435713  714.785    0.000 5857.302    0.000 module.py:866(_call_impl)
               14853151   40.240    0.000 5469.107    0.000 network.py:24(forward)
                1860854  150.510    0.000 5384.706    0.003 layers.py:18(step)
               14853151  180.519    0.000 5339.514    0.000 container.py:117(forward)
              186085400  411.523    0.000 5219.948    0.000 layer.py:76(move)
                7409735  173.665    0.000 4447.407    0.001 agent.py:46(__call__)
                5582562   44.847    0.000 4029.847    0.001 optimizer.py:84(wrapper)
                5582562   23.374    0.000 3831.011    0.001 grad_mode.py:24(decorate_context)
                5582562  155.624    0.000 3756.957    0.001 adam.py:55(step)
                3721708 1519.387    0.000 3714.491    0.001 agent.py:81(interveen)
                3721708 2028.773    0.001 3532.616    0.001 replaybuffer.py:27(teleporter_save_data)
                5582562  775.385    0.000 3421.593    0.001 _functional.py:53(adam)
                1860854   53.523    0.000 3201.765    0.002 agent.py:146(_learn)
              186085400  517.990    0.000 3052.391    0.000 layers.py:492(check)
                5582562   21.685    0.000 2674.872    0.000 tensor.py:195(backward)
                5582562   20.305    0.000 2652.438    0.000 __init__.py:68(backward)
                5582562 2531.210    0.000 2531.210    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                1860855  195.474    0.000 2352.590    0.001 layers.py:446(update)
                1860854 1461.179    0.001 2314.463    0.001 agent.py:101(metamodify)
               29706302   63.533    0.000 1985.823    0.000 conv.py:398(forward)
               29706302   41.201    0.000 1891.966    0.000 conv.py:390(_conv_forward)
               29706302 1850.765    0.000 1850.765    0.000 {built-in method conv2d}
               40837745   78.843    0.000 1512.636    0.000 linear.py:93(forward)
              186085400  322.846    0.000 1463.868    0.000 layers.py:486(isFree)
               40837745   30.069    0.000 1392.706    0.000 functional.py:1737(linear)
               40837745 1354.715    0.000 1354.715    0.000 {built-in method torch._C._nn.linear}
               11131443   88.145    0.000 1339.216    0.000 agent.py:55(modify_board)
              146906582 1299.532    0.000 1299.532    0.000 {built-in method clone}
               18608550  745.853    0.000 1285.889    0.000 layer.py:121(update)
             1718887442  945.035    0.000 1141.022    0.000 layer.py:73(isFree)
               33461691 1125.343    0.000 1125.343    0.000 {built-in method cat}
                3721708   69.772    0.000  930.355    0.000 replaybuffer.py:19(stacker)
               11131443  862.653    0.000  862.653    0.000 {built-in method torch._C._nn.one_hot}
                9581419  835.329    0.000  835.329    0.000 {built-in method tensor}
               55690896   43.326    0.000  791.283    0.000 activation.py:713(forward)
               55690896   41.437    0.000  747.957    0.000 functional.py:1364(leaky_relu)
                5582562    6.277    0.000  737.600    0.000 game.py:23(board)
                1860854   28.814    0.000  712.757    0.000 agent.py:141(__call__)
               55690896  697.666    0.000  697.666    0.000 {built-in method torch._C._nn.leaky_relu}
             2925914272  485.865    0.000  689.040    0.000 enum.py:646(__hash__)
              104207824  669.504    0.000  669.504    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              104207824  595.841    0.000  595.841    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                5582562  102.957    0.000  595.800    0.000 optimizer.py:189(zero_grad)
              186085400  303.864    0.000  477.158    0.000 layers.py:216(check)
              186085400  300.605    0.000  473.971    0.000 layers.py:244(check)
              186085400  296.382    0.000  470.239    0.000 layers.py:230(check)
              186085500   48.747    0.000  463.654    0.000 {built-in method builtins.all}
                7409735  164.346    0.000  439.626    0.000 exploration.py:53(softmaxer)
              571561154  125.590    0.000  435.284    0.000 layers.py:452(<genexpr>)
               52103912  395.251    0.000  395.251    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              186085400  283.204    0.000  392.732    0.000 layers.py:76(check)
             4792402085  392.371    0.000  392.371    0.000 layer.py:69(positions)
              459789107  350.159    0.000  350.159    0.000 layer.py:116(elements)
                1860854  206.943    0.000  349.356    0.000 collector.py:54(collect)
               52103912  340.881    0.000  340.881    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                1120664   11.822    0.000  335.786    0.000 layers.py:496(restart)
               52103912  317.265    0.000  317.265    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               52103912  315.565    0.000  315.565    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              156177171  295.367    0.000  295.367    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              186085500  199.794    0.000  292.609    0.000 layers.py:110(isDone)
              364727468  225.238    0.000  279.858    0.000 tensor.py:906(grad)
                3721708   95.113    0.000  250.308    0.000 random.py:315(sample)
                1120664    6.264    0.000  241.214    0.000 level.py:8(__init__)
               52103912  235.863    0.000  235.863    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              186085400  149.471    0.000  227.520    0.000 layers.py:47(check)
              186085400  153.086    0.000  226.915    0.000 layers.py:203(check)
                5582562    7.136    0.000  226.059    0.000 loss.py:527(forward)
              186085400  146.679    0.000  220.914    0.000 layers.py:63(check)
                5582562   20.095    0.000  218.923    0.000 functional.py:2898(mse_loss)
                1120664   13.040    0.000  213.334    0.000 levels.py:151(generate)
        2397480505/2397480502  171.154    0.000  212.354    0.000 {built-in method builtins.len}
             2925935811  203.178    0.000  203.178    0.000 {built-in method builtins.hash}
                5378087   40.984    0.000  187.550    0.000 level.py:41(notUsed)
               16747686  164.184    0.000  164.184    0.000 {built-in method sum}
             1718887442  153.618    0.000  153.618    0.000 layer.py:177(isBlocking)
                7409735  139.905    0.000  139.905    0.000 {built-in method multinomial}
                5582562  133.022    0.000  133.022    0.000 {built-in method torch._C._nn.mse_loss}
                9304270   12.376    0.000  132.824    0.000 tensor.py:525(__rsub__)
               29706302   19.231    0.000  130.547    0.000 flatten.py:39(forward)
              170740877   85.091    0.000  125.788    0.000 layer.py:96(remove)
              211553873   92.183    0.000  123.803    0.000 layer.py:100(add)
                5583488  121.944    0.000  121.944    0.000 {built-in method max}
                9304270  118.168    0.000  118.168    0.000 {built-in method rsub}
               29706302  111.316    0.000  111.316    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              191510766   72.967    0.000  109.576    0.000 random.py:250(_randbelow_with_getrandbits)
                3721710  104.304    0.000  104.304    0.000 {built-in method nonzero}
              194953297  102.499    0.000  102.499    0.000 {built-in method torch._C._get_tracing_state}
              155955468   97.001    0.000   97.009    0.000 module.py:934(__getattr__)
                5582562   20.039    0.000   96.441    0.000 __init__.py:28(_make_grads)
                5582562   95.748    0.000   95.748    0.000 {built-in method gather}
               11165124   20.914    0.000   94.926    0.000 profiler.py:615(__enter__)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-3>
Subject: Job 9455328: <causal2_9x9_META_attempt2_0> in cluster <dcc> Done

Job <causal2_9x9_META_attempt2_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed Mar 24 02:22:07 2021
Job was executed on host(s) <n-62-20-3>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed Mar 24 02:46:49 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed Mar 24 02:46:49 2021
Terminated at Wed Mar 24 13:42:13 2021
Results reported at Wed Mar 24 13:42:13 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=8G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 1440
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $LSB_PROJECT_NAME


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   39219.03 sec.
    Max Memory :                                 7236 MB
    Average Memory :                             5407.47 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               956.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   39325 sec.
    Turnaround time :                            40806 sec.

The output (if any) is above this job summary.

