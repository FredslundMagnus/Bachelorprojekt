
# Parameters

    Name :                      Attempt3_SuperLevel1_option_critic-0
    Main :                      option_critic_run
    Level :                     Levels.SuperLevel
    Failed actions chance :     0
    Use model :                 True
    Depth :                     3
    Model explore :             1000000
    Samples :                   5
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
    Minutes used :              4315 minutes.
    Hours used :                71 hours.

# Profiling


      40840504707 function calls (39663478351 primitive calls) in 258900.61 seconds

##    Ordered by: cumulative time
   List reduced from 444 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.609 258900.609 {built-in method builtins.exec}
                      1    0.325    0.325 258900.609 258900.609 <string>:1(<module>)
                      1 4160.517 4160.517 258900.284 258900.284 optionCritic.py:195(option_critic_run)
        1563403132/386487433 9547.532    0.000 114636.288    0.000 module.py:866(_call_impl)
               42292500 7970.730    0.000 113091.661    0.003 optionCritic.py:143(actor_loss_fn)
              130768411  791.067    0.000 106535.577    0.001 optionCritic.py:70(get_state)
              130768411 2372.662    0.000 103595.425    0.001 container.py:117(forward)
                1691700   11.696    0.000 70327.016    0.042 tensor.py:195(backward)
                1691700   17.630    0.000 70315.080    0.042 __init__.py:68(backward)
                1691700 70260.094    0.042 70260.094    0.042 {method 'run_backward' of 'torch._C._EngineBase' objects}
              261536822  994.652    0.000 69988.217    0.000 conv.py:398(forward)
              261536822  452.162    0.000 68643.668    0.000 conv.py:390(_conv_forward)
              261536822 68191.506    0.000 68191.506    0.000 {built-in method conv2d}
               42292500 3497.658    0.000 19970.387    0.000 optionCritic.py:91(get_action)
              517255844 1676.974    0.000 18853.218    0.000 linear.py:93(forward)
              517255844  633.604    0.000 16554.584    0.000 functional.py:1737(linear)
                1691700   37.607    0.000 16247.444    0.010 optimizer.py:84(wrapper)
                1691700   19.878    0.000 16110.824    0.010 grad_mode.py:24(decorate_context)
                1691700  106.246    0.000 16054.500    0.009 rmsprop.py:56(step)
                1691700  117.837    0.000 15824.710    0.009 _functional.py:203(rmsprop)
              517255844 15789.146    0.000 15789.146    0.000 {built-in method torch._C._nn.linear}
               23683782 13366.840    0.001 13366.840    0.001 {method 'sqrt' of 'torch._C._TensorBase' objects}
               42292500 1106.049    0.000 12760.635    0.000 optionCritic.py:80(predict_option_termination)
               84585000 1144.136    0.000 7298.293    0.000 distribution.py:34(__init__)
              392305233  527.072    0.000 7142.975    0.000 activation.py:713(forward)
               42292500  588.705    0.000 6671.002    0.000 categorical.py:115(log_prob)
              392305233  485.814    0.000 6615.903    0.000 functional.py:1364(leaky_relu)
              392305233 6028.103    0.000 6028.103    0.000 {built-in method torch._C._nn.leaky_relu}
              128672352  497.698    0.000 5899.276    0.000 optionCritic.py:77(get_Q)
                1691700   10.658    0.000 5823.168    0.003 game.py:42(step)
                1691700   16.925    0.000 5689.238    0.003 layers.py:827(step)
               42292500  762.478    0.000 5584.293    0.000 categorical.py:49(__init__)
               42292500  349.292    0.000 4666.788    0.000 bernoulli.py:34(__init__)
               84754170  420.600    0.000 4299.393    0.000 optionCritic.py:88(get_terminations)
                1691700   76.037    0.000 3613.470    0.002 layers.py:17(step)
               42292500  237.356    0.000 3530.825    0.000 layer.py:106(move)
               42292500 2260.526    0.000 3348.365    0.000 constraints.py:398(check)
               42292500  475.974    0.000 2695.636    0.000 layers.py:844(check)
               42292500  480.920    0.000 2623.505    0.000 distribution.py:240(_validate_sample)
                 169170   30.485    0.000 2601.508    0.015 optionCritic.py:116(critic_loss_fn)
                1691701  161.864    0.000 2051.389    0.001 layers.py:793(update)
              130768411  200.132    0.000 1911.837    0.000 activation.py:101(forward)
               42292500  909.607    0.000 1835.977    0.000 categorical.py:123(entropy)
               42292500 1807.449    0.000 1807.449    0.000 constraints.py:364(check)
               42292500  361.935    0.000 1746.471    0.000 bernoulli.py:86(sample)
              126877500  234.062    0.000 1728.370    0.000 utils.py:106(__get__)
              130768411  166.079    0.000 1711.705    0.000 functional.py:1195(relu)
             2028662232 1686.149    0.000 1686.152    0.000 module.py:934(__getattr__)
               42292500 1643.700    0.000 1643.700    0.000 constraints.py:249(check)
              130768411 1517.337    0.000 1517.337    0.000 {built-in method relu}
             1582011832 1405.762    0.000 1405.762    0.000 {built-in method torch._C._get_tracing_state}
              130768411  135.514    0.000 1389.719    0.000 flatten.py:39(forward)
              296047500 1378.304    0.000 1378.304    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              127215840  193.451    0.000 1374.229    0.000 tensor.py:525(__rsub__)
               84585000  487.498    0.000 1342.652    0.000 functional.py:46(broadcast_tensors)
               42292500   74.456    0.000 1320.733    0.000 categorical.py:88(logits)
               42292500  339.846    0.000 1271.926    0.000 categorical.py:108(sample)
              130768411 1254.205    0.000 1254.205    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               42292500   75.757    0.000 1246.277    0.000 utils.py:82(probs_to_logits)
              126877500 1187.912    0.000 1187.912    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
               23683782 1185.332    0.000 1185.332    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              127215840 1154.852    0.000 1154.852    0.000 {built-in method rsub}
              127046670 1129.053    0.000 1129.053    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
               18608700   47.291    0.000 1081.179    0.000 tensor.py:575(__iter__)
             6977807698 1043.812    0.000 1056.885    0.000 {built-in method builtins.len}
               84754170 1049.373    0.000 1049.373    0.000 {method 'max' of 'torch._C._TensorBase' objects}
               42292500  211.313    0.000 1039.861    0.000 utils.py:11(broadcast_all)
               18608700 1004.071    0.000 1004.071    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
             6384380939  924.421    0.000  924.421    0.000 {method 'values' of 'collections.OrderedDict' objects}
              126877500  885.560    0.000  885.560    0.000 {method 'all' of 'torch._C._TensorBase' objects}
               42292500  152.153    0.000  784.600    0.000 utils.py:77(clamp_probs)
               42292500  771.169    0.000  771.169    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               21992113  471.554    0.000  745.268    0.000 layer.py:159(update)
               84585000  721.947    0.000  721.947    0.000 {built-in method broadcast_tensors}
               11819109  290.559    0.000  633.796    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               42292500  632.447    0.000  632.447    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
                1691700   72.825    0.000  622.470    0.000 replaybuffer.py:34(save_option_critic)
               42292500  435.030    0.000  613.683    0.000 layers.py:471(check)
               42292500  613.207    0.000  613.207    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
              127385010  550.974    0.000  550.974    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               43749012  535.746    0.000  535.746    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
             1356764215  379.105    0.000  533.080    0.000 enum.py:646(__hash__)
               42292500  530.316    0.000  530.316    0.000 {built-in method bernoulli}
                1691700   90.194    0.000  514.045    0.000 optimizer.py:189(zero_grad)
               42292500  508.410    0.000  508.410    0.000 {built-in method clamp}
               84585000  495.076    0.000  495.076    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               23683782  492.867    0.000  492.867    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               42292500  103.029    0.000  481.932    0.000 layers.py:838(isFree)
              254093340  457.513    0.000  457.513    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                1456539   31.986    0.000  439.334    0.000 layers.py:849(restart)
               42292500  310.520    0.000  422.876    0.000 layers.py:77(check)
               40835986   91.267    0.000  406.068    0.000 {built-in method builtins.any}
              126877525  129.973    0.000  404.620    0.000 {built-in method builtins.all}
               42292500  385.920    0.000  385.920    0.000 {built-in method log}
               42292500  384.332    0.000  384.332    0.000 {built-in method all}
               23683782  384.247    0.000  384.247    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              236024000  309.316    0.000  378.903    0.000 layer.py:103(isFree)
               42292500  370.258    0.000  370.258    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
              556931277  225.268    0.000  361.513    0.000 {built-in method builtins.isinstance}
               10657714  351.915    0.000  351.915    0.000 {built-in method tensor}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9607855: <Attempt3_SuperLevel1_option_critic_0> in cluster <dcc> Done

Job <Attempt3_SuperLevel1_option_critic_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon May  3 13:31:25 2021
Job was executed on host(s) <n-62-21-101>, in queue <hpc>, as user <s183914> in cluster <dcc> at Mon May  3 13:31:27 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon May  3 13:31:27 2021
Terminated at Thu May  6 13:26:33 2021
Results reported at Thu May  6 13:26:33 2021

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

    CPU time :                                   258905.12 sec.
    Max Memory :                                 1316 MB
    Average Memory :                             1300.17 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15068.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   259010 sec.
    Turnaround time :                            258908 sec.

The output (if any) is above this job summary.

