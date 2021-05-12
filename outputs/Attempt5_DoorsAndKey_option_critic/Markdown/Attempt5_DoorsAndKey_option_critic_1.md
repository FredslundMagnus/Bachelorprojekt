
# Parameters

    Name :                      Attempt5_DoorsAndKey_option_critic-1
    Main :                      option_critic_run
    Level :                     Levels.Causal1
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


      13909055717 function calls (13443406016 primitive calls) in 258901.59 seconds

##    Ordered by: cumulative time
   List reduced from 430 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258901.592 258901.592 {built-in method builtins.exec}
                      1    0.322    0.322 258901.592 258901.592 <string>:1(<module>)
                      1 1832.689 1832.689 258901.270 258901.270 optionCritic.py:195(option_critic_run)
                 522028    4.961    0.000 189362.602    0.363 tensor.py:195(backward)
                 522028    5.724    0.000 189357.543    0.363 __init__.py:68(backward)
                 522028 189338.597    0.363 189338.597    0.363 {method 'run_backward' of 'torch._C._EngineBase' objects}
               16704896 4124.542    0.000 41675.115    0.002 optionCritic.py:143(actor_loss_fn)
        616200148/152247754 3462.878    0.000 41440.412    0.000 module.py:866(_call_impl)
               51550266  277.322    0.000 38475.938    0.001 optionCritic.py:70(get_state)
               51550266  838.257    0.000 37284.035    0.001 container.py:117(forward)
              103100532  311.413    0.000 21796.331    0.000 conv.py:398(forward)
              103100532  172.278    0.000 21369.131    0.000 conv.py:390(_conv_forward)
              103100532 21196.853    0.000 21196.853    0.000 {built-in method conv2d}
              203798020  537.442    0.000 9644.746    0.000 linear.py:93(forward)
              203798020  215.249    0.000 8900.496    0.000 functional.py:1737(linear)
               16704896 1414.504    0.000 8683.298    0.001 optionCritic.py:91(get_action)
              203798020 8629.479    0.000 8629.479    0.000 {built-in method torch._C._nn.linear}
               16704896  433.042    0.000 4772.908    0.000 optionCritic.py:80(predict_option_termination)
                 522028   14.439    0.000 4516.682    0.009 optimizer.py:84(wrapper)
                 522028    6.849    0.000 4460.917    0.009 grad_mode.py:24(decorate_context)
                 522028   36.628    0.000 4440.321    0.009 adam.py:55(step)
                 522028  264.225    0.001 4364.092    0.008 _functional.py:53(adam)
               33409792  398.415    0.000 3211.345    0.000 distribution.py:34(__init__)
               16704896  226.160    0.000 2872.600    0.000 categorical.py:115(log_prob)
              154650798  164.650    0.000 2804.665    0.000 activation.py:713(forward)
              154650798  176.914    0.000 2640.016    0.000 functional.py:1364(leaky_relu)
               16704896  317.779    0.000 2523.678    0.000 categorical.py:49(__init__)
              154650798 2424.507    0.000 2424.507    0.000 {built-in method torch._C._nn.leaky_relu}
               50452293  132.680    0.000 2091.336    0.000 optionCritic.py:77(get_Q)
                 130507   28.270    0.000 2021.087    0.015 optionCritic.py:116(critic_loss_fn)
               16704896  119.289    0.000 1792.768    0.000 bernoulli.py:34(__init__)
               33540299  151.674    0.000 1781.836    0.000 optionCritic.py:88(get_terminations)
               16704896 1052.192    0.000 1600.237    0.000 constraints.py:398(check)
               16704896  176.180    0.000 1253.640    0.000 distribution.py:240(_validate_sample)
               14616772  979.129    0.000  979.129    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                 522028    2.824    0.000  896.352    0.002 game.py:42(step)
                7308386  874.751    0.000  874.751    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               16704896  867.099    0.000  867.099    0.000 constraints.py:249(check)
                 522028    5.268    0.000  858.211    0.002 layers.py:827(step)
               51550266   74.803    0.000  850.723    0.000 activation.py:101(forward)
               16704896  434.188    0.000  846.554    0.000 categorical.py:123(entropy)
               16704896  779.204    0.000  779.204    0.000 constraints.py:364(check)
               51550266   64.558    0.000  775.920    0.000 functional.py:1195(relu)
              116934272  765.593    0.000  765.593    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               51550266  700.555    0.000  700.555    0.000 {built-in method relu}
               51550266   76.323    0.000  690.927    0.000 flatten.py:39(forward)
                7308386  676.130    0.000  676.130    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               50114688   77.678    0.000  671.977    0.000 utils.py:106(__get__)
               50375702   64.845    0.000  661.489    0.000 tensor.py:525(__rsub__)
               16704896  116.130    0.000  644.232    0.000 bernoulli.py:86(sample)
               51550266  614.605    0.000  614.605    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               50375702  584.299    0.000  584.299    0.000 {built-in method rsub}
              621942456  577.100    0.000  577.100    0.000 {built-in method torch._C._get_tracing_state}
              799522583  569.881    0.000  569.923    0.000 module.py:934(__getattr__)
               50114688  568.544    0.000  568.544    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
               16704896  150.984    0.000  566.000    0.000 categorical.py:108(sample)
               50245195  546.056    0.000  546.056    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
               14616772  545.240    0.000  545.240    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               16704896   25.642    0.000  532.931    0.000 categorical.py:88(logits)
                7308386  520.564    0.000  520.564    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               33540299  510.061    0.000  510.061    0.000 {method 'max' of 'torch._C._TensorBase' objects}
               16704896   26.935    0.000  507.290    0.000 utils.py:82(probs_to_logits)
                7308386  500.108    0.000  500.108    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               33409792  153.798    0.000  489.012    0.000 functional.py:46(broadcast_tensors)
                 522028   24.125    0.000  488.950    0.001 layers.py:17(step)
               16704896   43.846    0.000  462.446    0.000 layer.py:106(move)
               50114688  441.510    0.000  441.510    0.000 {method 'all' of 'torch._C._TensorBase' objects}
             2645185452  416.432    0.000  420.592    0.000 {built-in method builtins.len}
                5742308   14.869    0.000  410.688    0.000 tensor.py:575(__iter__)
                5742308  383.958    0.000  383.958    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
                 522029   53.411    0.000  361.435    0.001 layers.py:793(update)
               16704896   68.690    0.000  355.367    0.000 utils.py:11(broadcast_all)
               16704896  340.018    0.000  340.018    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
             2516350858  326.421    0.000  326.421    0.000 {method 'values' of 'collections.OrderedDict' objects}
               16704896   52.036    0.000  293.992    0.000 utils.py:77(clamp_probs)
               33409792  292.416    0.000  292.416    0.000 {built-in method broadcast_tensors}
                 522028   28.863    0.000  292.374    0.001 replaybuffer.py:34(save_option_critic)
               50506209  287.431    0.000  287.431    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
                 130507  221.615    0.002  280.016    0.002 replaybuffer.py:42(sample_option_critic)
               16704896  243.668    0.000  243.668    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
               16704896  241.956    0.000  241.956    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
              100490390  231.381    0.000  231.381    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               33409792  221.886    0.000  221.886    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               16704896   68.040    0.000  219.476    0.000 layers.py:844(check)
               16704896  216.425    0.000  216.425    0.000 {built-in method clamp}
               16704896  212.071    0.000  212.071    0.000 {built-in method bernoulli}
               16781487  204.722    0.000  204.722    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               16704896  187.906    0.000  187.906    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
               16704896  186.363    0.000  186.363    0.000 {built-in method log}
               16704896  184.152    0.000  184.152    0.000 {built-in method all}
                 522028   29.076    0.000  165.012    0.000 optimizer.py:189(zero_grad)
               16704896   32.057    0.000  159.278    0.000 layers.py:838(isFree)
               16704896  146.959    0.000  146.959    0.000 {built-in method multinomial}
               51550280  138.772    0.000  138.772    0.000 {method 'to' of 'torch._C._TensorBase' objects}
               93699010  105.261    0.000  127.221    0.000 layer.py:103(isFree)
                3523693  120.809    0.000  120.809    0.000 {built-in method tensor}
               50114720   33.536    0.000  116.515    0.000 {built-in method builtins.all}
               50192354  115.684    0.000  115.684    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                3132174   67.892    0.000  113.942    0.000 layer.py:175(NoRock_update)
              219855720   77.523    0.000  111.835    0.000 {built-in method builtins.isinstance}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9618623: <Attempt5_DoorsAndKey_option_critic_1> in cluster <dcc> Done

Job <Attempt5_DoorsAndKey_option_critic_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Thu May  6 02:11:29 2021
Job was executed on host(s) <n-62-31-3>, in queue <hpc>, as user <s183914> in cluster <dcc> at Sat May  8 23:13:45 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat May  8 23:13:45 2021
Terminated at Tue May 11 23:09:03 2021
Results reported at Tue May 11 23:09:03 2021

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

    CPU time :                                   258226.95 sec.
    Max Memory :                                 789 MB
    Average Memory :                             773.86 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15595.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   259024 sec.
    Turnaround time :                            507454 sec.

The output (if any) is above this job summary.

