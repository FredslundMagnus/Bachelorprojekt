
# Parameters

    Name :                      Attempt6_SuperLevel2_option_critic-0
    Main :                      option_critic_run
    Level :                     Levels.SuperLevel2
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
    Num :                       0
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              4315 minutes.
    Hours used :                71 hours.

# Profiling


      45838276829 function calls (44508001188 primitive calls) in 258900.80 seconds

##    Ordered by: cumulative time
   List reduced from 439 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.803 258900.803 {built-in method builtins.exec}
                      1    0.364    0.364 258900.803 258900.803 <string>:1(<module>)
                      1 5077.890 5077.890 258900.440 258900.440 optionCritic.py:195(option_critic_run)
                1491340   11.795    0.000 100933.616    0.068 tensor.py:195(backward)
                1491340   16.263    0.000 100921.594    0.068 __init__.py:68(backward)
                1491340 100870.877    0.068 100870.877    0.068 {method 'run_backward' of 'torch._C._EngineBase' objects}
        1763310025/437881591 8245.259    0.000 97229.753    0.000 module.py:866(_call_impl)
               47722880 7135.370    0.000 96584.654    0.002 optionCritic.py:143(actor_loss_fn)
              147269826  698.137    0.000 90668.457    0.001 optionCritic.py:70(get_state)
              147269826 1989.734    0.000 87882.157    0.001 container.py:117(forward)
              294539652  822.703    0.000 54576.209    0.000 conv.py:398(forward)
              294539652  428.455    0.000 53427.920    0.000 conv.py:390(_conv_forward)
              294539652 52999.466    0.000 52999.466    0.000 {built-in method conv2d}
              585151417 1386.290    0.000 20159.235    0.000 linear.py:93(forward)
              585151417  564.504    0.000 18187.133    0.000 functional.py:1737(linear)
              585151417 17483.250    0.000 17483.250    0.000 {built-in method torch._C._nn.linear}
               47722880 2832.845    0.000 16797.318    0.000 optionCritic.py:91(get_action)
               47722880 1003.551    0.000 11772.242    0.000 optionCritic.py:80(predict_option_termination)
                1491340   36.113    0.000 7068.753    0.005 optimizer.py:84(wrapper)
                1491340   20.159    0.000 6939.154    0.005 grad_mode.py:24(decorate_context)
                1491340   93.955    0.000 6882.928    0.005 adam.py:55(step)
                1491340  562.576    0.000 6687.292    0.004 _functional.py:53(adam)
               95445760 1024.986    0.000 6622.568    0.000 distribution.py:34(__init__)
              441809478  449.262    0.000 6196.954    0.000 activation.py:713(forward)
              441809478  488.013    0.000 5747.692    0.000 functional.py:1364(leaky_relu)
               47722880  462.175    0.000 5563.245    0.000 categorical.py:115(log_prob)
                1491340    9.301    0.000 5419.667    0.004 game.py:42(step)
                1491340   14.894    0.000 5291.187    0.004 layers.py:827(step)
              441809478 5163.422    0.000 5163.422    0.000 {built-in method torch._C._nn.leaky_relu}
              147070290  337.330    0.000 4862.877    0.000 optionCritic.py:77(get_Q)
               47722880  632.361    0.000 4726.999    0.000 categorical.py:49(__init__)
               47722880  378.042    0.000 4638.268    0.000 bernoulli.py:34(__init__)
                 372835   64.440    0.000 3855.628    0.010 optionCritic.py:116(critic_loss_fn)
               95818595  348.558    0.000 3723.391    0.000 optionCritic.py:88(get_terminations)
                1491340   71.272    0.000 3077.352    0.002 layers.py:17(step)
               47722880  192.132    0.000 3000.170    0.000 layer.py:106(move)
               47722880 1956.754    0.000 2894.677    0.000 constraints.py:398(check)
               47722880  383.662    0.000 2336.337    0.000 layers.py:844(check)
               47722880  388.488    0.000 2264.569    0.000 distribution.py:240(_validate_sample)
                1491341  144.062    0.000 2191.804    0.001 layers.py:793(update)
              147269826  189.055    0.000 1751.877    0.000 activation.py:101(forward)
               47722880 1751.406    0.000 1751.406    0.000 constraints.py:364(check)
               47722880  335.760    0.000 1705.969    0.000 bernoulli.py:86(sample)
              147269826  175.846    0.000 1562.822    0.000 functional.py:1195(relu)
             2292903418 1557.719    0.000 1557.830    0.000 module.py:934(__getattr__)
               47722880  798.529    0.000 1537.480    0.000 categorical.py:123(entropy)
               41757508 1481.911    0.000 1481.911    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               47722880 1475.239    0.000 1475.239    0.000 constraints.py:249(check)
              143168640  187.432    0.000 1394.634    0.000 utils.py:106(__get__)
              334060160 1389.330    0.000 1389.330    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              147269826  147.779    0.000 1366.778    0.000 flatten.py:39(forward)
              147269826 1359.791    0.000 1359.791    0.000 {built-in method relu}
              143914310  163.452    0.000 1356.260    0.000 tensor.py:525(__rsub__)
               95445760  430.852    0.000 1222.103    0.000 functional.py:46(broadcast_tensors)
              147269826 1218.998    0.000 1218.998    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              143914310 1166.531    0.000 1166.531    0.000 {built-in method rsub}
               20878754 1153.293    0.000 1153.293    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               20878754 1147.227    0.000 1147.227    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               47722880  328.752    0.000 1112.683    0.000 categorical.py:108(sample)
               95818595 1092.391    0.000 1092.391    0.000 {method 'max' of 'torch._C._TensorBase' objects}
               16404740   41.522    0.000 1086.949    0.000 tensor.py:575(__iter__)
               47722880   57.883    0.000 1061.938    0.000 categorical.py:88(logits)
              143541475 1044.876    0.000 1044.876    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
               47722880  222.552    0.000 1044.401    0.000 utils.py:11(broadcast_all)
             1779714765 1043.133    0.000 1043.133    0.000 {built-in method torch._C._get_tracing_state}
               16404740 1021.337    0.000 1021.337    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               47722880   59.023    0.000 1004.055    0.000 utils.py:82(probs_to_logits)
             7818718632  974.915    0.000  986.513    0.000 {built-in method builtins.len}
              143168640  972.382    0.000  972.382    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 372835  691.466    0.002  851.746    0.002 replaybuffer.py:42(sample_option_critic)
             7200509926  846.545    0.000  846.545    0.000 {method 'values' of 'collections.OrderedDict' objects}
              143168640  826.939    0.000  826.939    0.000 {method 'all' of 'torch._C._TensorBase' objects}
                3156011   49.607    0.000  822.496    0.000 layers.py:849(restart)
               20878754  805.223    0.000  805.223    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               20878754  773.739    0.000  773.739    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               47722880  755.223    0.000  755.223    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               41757508  754.885    0.000  754.885    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               16404751  497.263    0.000  736.950    0.000 layer.py:159(update)
               95445760  665.611    0.000  665.611    0.000 {built-in method broadcast_tensors}
                1491340   71.272    0.000  628.156    0.000 replaybuffer.py:34(save_option_critic)
               47722880  121.112    0.000  594.027    0.000 utils.py:77(clamp_probs)
              144287145  533.003    0.000  533.003    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               47722880  528.043    0.000  528.043    0.000 {built-in method bernoulli}
               47722880  391.982    0.000  523.317    0.000 layers.py:471(check)
               50878860  484.914    0.000  484.914    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
             1522347785  335.028    0.000  479.430    0.000 enum.py:646(__hash__)
               47722880  472.915    0.000  472.915    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
               47722880  469.848    0.000  469.848    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
                1491340   73.556    0.000  452.883    0.000 optimizer.py:189(zero_grad)
              287082950  440.878    0.000  440.878    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               95445760  407.057    0.000  407.057    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               47722880  393.154    0.000  393.154    0.000 {built-in method clamp}
                3156011   25.553    0.000  391.225    0.000 level.py:8(__init__)
               47722880   66.223    0.000  386.461    0.000 layers.py:838(isFree)
               34716121   54.519    0.000  367.785    0.000 layer.py:77(restart)
               10066549  361.412    0.000  361.412    0.000 {built-in method tensor}
               47722880  351.006    0.000  351.006    0.000 {built-in method log}
               47722880  342.111    0.000  342.111    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
              628086572  212.227    0.000  336.265    0.000 {built-in method builtins.isinstance}
              184013684  268.003    0.000  320.239    0.000 layer.py:103(isFree)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9624162: <Attempt6_SuperLevel2_option_critic_0> in cluster <dcc> Done

Job <Attempt6_SuperLevel2_option_critic_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun May  9 01:22:27 2021
Job was executed on host(s) <n-62-11-63>, in queue <hpc>, as user <s183914> in cluster <dcc> at Sun May  9 01:22:28 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun May  9 01:22:28 2021
Terminated at Wed May 12 01:17:35 2021
Results reported at Wed May 12 01:17:35 2021

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

    CPU time :                                   258287.38 sec.
    Max Memory :                                 1154 MB
    Average Memory :                             1140.53 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15230.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258957 sec.
    Turnaround time :                            258908 sec.

The output (if any) is above this job summary.

