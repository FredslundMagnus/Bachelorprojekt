[W NNPACK.cpp:80] Could not initialize NNPACK! Reason: Unsupported hardware.

# Parameters

    Name :                      Rocks_option_critic-0
    Main :                      option_critic_run
    Level :                     Levels.Rocks
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


      30345267048 function calls (29348302378 primitive calls) in 258900.39 seconds

##    Ordered by: cumulative time
   List reduced from 426 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.385 258900.385 {built-in method builtins.exec}
                      1    0.317    0.317 258900.385 258900.385 <string>:1(<module>)
                      1 3883.059 3883.059 258900.068 258900.068 optionCritic.py:195(option_critic_run)
        1317088333/324732970 9761.544    0.000 99661.583    0.000 module.py:866(_call_impl)
               35453925 9407.772    0.000 99083.842    0.003 optionCritic.py:143(actor_loss_fn)
              110261707  711.214    0.000 90916.481    0.001 optionCritic.py:70(get_state)
              110261707 2640.673    0.000 87990.770    0.001 container.py:117(forward)
                1418157   11.844    0.000 78471.878    0.055 tensor.py:195(backward)
                1418157   12.647    0.000 78459.762    0.055 __init__.py:68(backward)
                1418157 78410.932    0.055 78410.932    0.055 {method 'run_backward' of 'torch._C._EngineBase' objects}
              220523414  843.297    0.000 51622.534    0.000 conv.py:398(forward)
              220523414  355.628    0.000 50464.295    0.000 conv.py:390(_conv_forward)
              220523414 50108.667    0.000 50108.667    0.000 {built-in method conv2d}
                1418157   32.447    0.000 22141.735    0.016 optimizer.py:84(wrapper)
                1418157   18.498    0.000 22011.236    0.016 grad_mode.py:24(decorate_context)
                1418157   98.970    0.000 21959.068    0.015 rmsprop.py:56(step)
               35453925 3664.159    0.000 21853.307    0.001 optionCritic.py:91(get_action)
                1418157  159.095    0.000 21752.664    0.015 _functional.py:203(rmsprop)
              434994677 1511.384    0.000 20669.023    0.000 linear.py:93(forward)
               19854192 18948.978    0.001 18948.978    0.001 {method 'sqrt' of 'torch._C._TensorBase' objects}
              434994677  551.633    0.000 18577.619    0.000 functional.py:1737(linear)
              434994677 17905.068    0.000 17905.068    0.000 {built-in method torch._C._nn.linear}
               35453925 1138.659    0.000 12260.652    0.000 optionCritic.py:80(predict_option_termination)
               70907850 1016.913    0.000 7990.001    0.000 distribution.py:34(__init__)
              330785121  414.061    0.000 7661.991    0.000 activation.py:713(forward)
              330785121  418.658    0.000 7247.930    0.000 functional.py:1364(leaky_relu)
               35453925  568.478    0.000 7189.515    0.000 categorical.py:115(log_prob)
              330785121 6734.310    0.000 6734.310    0.000 {built-in method torch._C._nn.leaky_relu}
               35453925  839.361    0.000 6439.332    0.000 categorical.py:49(__init__)
              107754949  433.132    0.000 6059.292    0.000 optionCritic.py:77(get_Q)
                 354539   81.222    0.000 5617.415    0.016 optionCritic.py:116(critic_loss_fn)
               71262389  427.148    0.000 4892.458    0.000 optionCritic.py:88(get_terminations)
               35453925  265.139    0.000 4326.925    0.000 bernoulli.py:34(__init__)
               35453925 2661.586    0.000 4001.837    0.000 constraints.py:398(check)
                1418157    8.140    0.000 3455.046    0.002 game.py:41(step)
                1418157   12.738    0.000 3352.779    0.002 layers.py:718(step)
               35453925  448.120    0.000 3051.983    0.000 distribution.py:240(_validate_sample)
              110261707  163.320    0.000 2203.787    0.000 activation.py:101(forward)
               35453925 1027.878    0.000 2116.138    0.000 categorical.py:123(entropy)
                1418157   65.310    0.000 2081.710    0.001 layers.py:17(step)
               35453925 2053.254    0.000 2053.254    0.000 constraints.py:249(check)
              110261707  136.246    0.000 2040.467    0.000 functional.py:1195(relu)
               35453925  173.259    0.000 2011.371    0.000 layer.py:98(move)
               35453925 1955.977    0.000 1955.977    0.000 constraints.py:364(check)
              110261707 1874.433    0.000 1874.433    0.000 {built-in method relu}
              106361775  215.911    0.000 1766.758    0.000 utils.py:106(__get__)
             1332688060 1743.579    0.000 1743.579    0.000 {built-in method torch._C._get_tracing_state}
              248177475 1713.350    0.000 1713.350    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               35453925  290.301    0.000 1620.742    0.000 bernoulli.py:86(sample)
              107070853  174.440    0.000 1587.221    0.000 tensor.py:525(__rsub__)
               19854192 1541.188    0.000 1541.188    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
             1706861415 1502.206    0.000 1502.355    0.000 module.py:934(__getattr__)
              106361775 1497.833    0.000 1497.833    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
              110261707  106.508    0.000 1497.004    0.000 flatten.py:39(forward)
               35453925  165.662    0.000 1458.588    0.000 layers.py:735(check)
               35453925   69.868    0.000 1397.680    0.000 categorical.py:88(logits)
              110261707 1390.496    0.000 1390.496    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              106716314 1390.468    0.000 1390.468    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
              107070853 1381.048    0.000 1381.048    0.000 {built-in method rsub}
               35453925  354.402    0.000 1356.045    0.000 categorical.py:108(sample)
               35453925   71.166    0.000 1327.812    0.000 utils.py:82(probs_to_logits)
                1418158  143.235    0.000 1252.581    0.001 layers.py:684(update)
               70907850  378.983    0.000 1181.339    0.000 functional.py:46(broadcast_tensors)
               71262389 1117.991    0.000 1117.991    0.000 {method 'max' of 'torch._C._TensorBase' objects}
               35453925  962.259    0.000 1061.382    0.000 layers.py:77(check)
              106361775 1035.279    0.000 1035.279    0.000 {method 'all' of 'torch._C._TensorBase' objects}
               15599727   44.306    0.000  985.555    0.000 tensor.py:575(__iter__)
             5579697409  938.235    0.000  950.662    0.000 {built-in method builtins.len}
               15599727  907.945    0.000  907.945    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
             5378615039  862.415    0.000  862.415    0.000 {method 'values' of 'collections.OrderedDict' objects}
               35453925  169.600    0.000  834.967    0.000 utils.py:11(broadcast_all)
               35453925  126.373    0.000  812.927    0.000 utils.py:77(clamp_probs)
               35453925  777.994    0.000  777.994    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               70907850  702.487    0.000  702.487    0.000 {built-in method broadcast_tensors}
               35453925  686.554    0.000  686.554    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
              107425392  674.782    0.000  674.782    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
                1418157   70.522    0.000  672.025    0.000 replaybuffer.py:34(save_option_critic)
               35453925  648.596    0.000  648.596    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
                 354539  500.410    0.001  642.719    0.002 replaybuffer.py:42(sample_option_critic)
              213432628  602.379    0.000  602.379    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               35453925  598.057    0.000  598.057    0.000 {built-in method clamp}
               70907850  564.933    0.000  564.933    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               36138021  554.987    0.000  554.987    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               35453925  511.619    0.000  511.619    0.000 {built-in method bernoulli}
                1418157   85.931    0.000  451.266    0.000 optimizer.py:189(zero_grad)
               35453925  446.711    0.000  446.711    0.000 {built-in method all}
               35453925  443.718    0.000  443.718    0.000 {built-in method log}
               35453925  436.531    0.000  436.531    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
               19854192  385.117    0.000  385.117    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               19854192  379.566    0.000  379.566    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                 684120   10.735    0.000  378.115    0.001 layers.py:740(restart)
                7227646  174.996    0.000  371.992    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                7090790  240.960    0.000  355.729    0.000 layer.py:151(update)
               19854192  338.720    0.000  338.720    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               35453925  320.976    0.000  320.976    0.000 {built-in method multinomial}
              106361800   79.422    0.000  313.714    0.000 {built-in method builtins.all}
               35453925   55.425    0.000  296.658    0.000 layers.py:729(isFree)
              469580703  203.276    0.000  293.212    0.000 {built-in method builtins.isinstance}
                9572563  292.340    0.000  292.340    0.000 {built-in method tensor}
              107048731  288.159    0.000  288.159    0.000 {method 'item' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9601878: <Rocks_option_critic_0> in cluster <dcc> Done

Job <Rocks_option_critic_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Thu Apr 29 21:41:19 2021
Job was executed on host(s) <n-62-23-23>, in queue <hpc>, as user <s183914> in cluster <dcc> at Thu Apr 29 21:41:21 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Apr 29 21:41:21 2021
Terminated at Sun May  2 21:36:24 2021
Results reported at Sun May  2 21:36:24 2021

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

    CPU time :                                   258868.66 sec.
    Max Memory :                                 711 MB
    Average Memory :                             689.08 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15673.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258959 sec.
    Turnaround time :                            258905 sec.

The output (if any) is above this job summary.

