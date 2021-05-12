
# Parameters

    Name :                      Attempt5_Coconuts_option_critic-0
    Main :                      option_critic_run
    Level :                     Levels.Coconuts
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


      16672100163 function calls (16136750946 primitive calls) in 258901.79 seconds

##    Ordered by: cumulative time
   List reduced from 438 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258901.788 258901.788 {built-in method builtins.exec}
                      1    0.342    0.342 258901.788 258901.788 <string>:1(<module>)
                      1 1969.001 1969.001 258901.446 258901.446 optionCritic.py:195(option_critic_run)
                 600167    5.025    0.000 191337.025    0.319 tensor.py:195(backward)
                 600167    6.223    0.000 191331.907    0.319 __init__.py:68(backward)
                 600167 191311.782    0.319 191311.782    0.319 {method 'run_backward' of 'torch._C._EngineBase' objects}
        708394552/174996142 3731.407    0.000 40726.600    0.000 module.py:866(_call_impl)
               19205344 3266.807    0.000 40293.575    0.002 optionCritic.py:143(actor_loss_fn)
               59266490  278.097    0.000 37948.962    0.001 optionCritic.py:70(get_state)
               59266490  770.355    0.000 36785.785    0.001 container.py:117(forward)
              118532980  337.666    0.000 22268.343    0.000 conv.py:398(forward)
              118532980  189.304    0.000 21793.899    0.000 conv.py:390(_conv_forward)
              118532980 21604.595    0.000 21604.595    0.000 {built-in method conv2d}
              234262632  591.948    0.000 8852.512    0.000 linear.py:93(forward)
              234262632  229.210    0.000 8016.771    0.000 functional.py:1737(linear)
              234262632 7729.724    0.000 7729.724    0.000 {built-in method torch._C._nn.linear}
               19205344 1236.145    0.000 7390.995    0.000 optionCritic.py:91(get_action)
               19205344  417.981    0.000 5094.811    0.000 optionCritic.py:80(predict_option_termination)
                 600167   14.192    0.000 4665.133    0.008 optimizer.py:84(wrapper)
                 600167    7.856    0.000 4611.826    0.008 grad_mode.py:24(decorate_context)
                 600167   40.967    0.000 4589.450    0.008 adam.py:55(step)
                 600167  233.711    0.000 4503.123    0.008 _functional.py:53(adam)
               38410688  460.888    0.000 2911.006    0.000 distribution.py:34(__init__)
              177799470  183.077    0.000 2506.089    0.000 activation.py:713(forward)
               19205344  204.148    0.000 2469.037    0.000 categorical.py:115(log_prob)
              177799470  185.413    0.000 2323.012    0.000 functional.py:1364(leaky_relu)
              177799470 2097.665    0.000 2097.665    0.000 {built-in method torch._C._nn.leaky_relu}
               19205344  272.202    0.000 2071.240    0.000 categorical.py:49(__init__)
               57963579  137.050    0.000 2013.981    0.000 optionCritic.py:77(get_Q)
               19205344  156.633    0.000 2001.672    0.000 bernoulli.py:34(__init__)
                 150041   25.303    0.000 1776.121    0.012 optionCritic.py:116(critic_loss_fn)
               38560729  143.306    0.000 1569.559    0.000 optionCritic.py:88(get_terminations)
                 600167    3.297    0.000 1548.329    0.003 game.py:42(step)
                 600167    5.647    0.000 1506.194    0.003 layers.py:827(step)
               19205344  851.156    0.000 1268.821    0.000 constraints.py:398(check)
                 600167   29.585    0.000 1051.505    0.002 layers.py:17(step)
               19205344  107.480    0.000 1019.251    0.000 layer.py:106(move)
               19205344  174.993    0.000 1003.324    0.000 distribution.py:240(_validate_sample)
               16804664  990.788    0.000  990.788    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                8402332  935.209    0.000  935.209    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               19205344  152.431    0.000  759.987    0.000 bernoulli.py:86(sample)
               19205344  753.918    0.000  753.918    0.000 constraints.py:364(check)
               59266490   76.499    0.000  743.654    0.000 activation.py:101(forward)
                8402332  713.795    0.000  713.795    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               19205344  355.176    0.000  686.497    0.000 categorical.py:123(entropy)
               59266490   73.486    0.000  667.155    0.000 functional.py:1195(relu)
              919076127  649.811    0.000  649.860    0.000 module.py:934(__getattr__)
               19205344  646.777    0.000  646.777    0.000 constraints.py:249(check)
               57616032   83.183    0.000  621.960    0.000 utils.py:106(__get__)
               19205344  107.009    0.000  619.368    0.000 layers.py:844(check)
              134437408  619.187    0.000  619.187    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               59266490   72.103    0.000  588.865    0.000 flatten.py:39(forward)
               59266490  582.763    0.000  582.763    0.000 {built-in method relu}
               57916114   67.467    0.000  552.478    0.000 tensor.py:525(__rsub__)
                8402332  549.971    0.000  549.971    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               16804664  544.491    0.000  544.491    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                8402332  531.639    0.000  531.639    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               38410688  192.041    0.000  526.213    0.000 functional.py:46(broadcast_tensors)
               59266490  516.762    0.000  516.762    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               19205344  132.667    0.000  486.485    0.000 categorical.py:108(sample)
                6601837   16.387    0.000  478.257    0.000 tensor.py:575(__iter__)
               57916114  474.110    0.000  474.110    0.000 {built-in method rsub}
               19205344   24.157    0.000  471.069    0.000 categorical.py:88(logits)
                6601837  451.634    0.000  451.634    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               19205344   25.116    0.000  446.912    0.000 utils.py:82(probs_to_logits)
                 600168   59.804    0.000  446.064    0.001 layers.py:793(update)
               38560729  443.592    0.000  443.592    0.000 {method 'max' of 'torch._C._TensorBase' objects}
               57766073  441.573    0.000  441.573    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
              714996389  437.951    0.000  437.951    0.000 {built-in method torch._C._get_tracing_state}
               19205344   89.963    0.000  435.068    0.000 utils.py:11(broadcast_all)
               57616032  425.559    0.000  425.559    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
             3053336838  417.908    0.000  422.691    0.000 {built-in method builtins.len}
               57616032  369.399    0.000  369.399    0.000 {method 'all' of 'torch._C._TensorBase' objects}
             2892844698  369.188    0.000  369.188    0.000 {method 'values' of 'collections.OrderedDict' objects}
                 150041  258.419    0.002  320.537    0.002 replaybuffer.py:42(sample_option_critic)
               19205344  319.538    0.000  319.538    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               38410688  280.473    0.000  280.473    0.000 {built-in method broadcast_tensors}
               19205344   52.368    0.000  267.127    0.000 utils.py:77(clamp_probs)
                 600167   29.097    0.000  258.821    0.000 replaybuffer.py:34(save_option_critic)
               58066155  234.371    0.000  234.371    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               19205344  229.217    0.000  229.217    0.000 {built-in method bernoulli}
               19205344   39.814    0.000  221.580    0.000 layers.py:838(isFree)
               19252809  218.573    0.000  218.573    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               19205344  214.758    0.000  214.758    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
               19205344  210.633    0.000  210.633    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
               19205344  140.430    0.000  194.619    0.000 layers.py:471(check)
              115532146  188.494    0.000  188.494    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
              118917099  152.388    0.000  181.766    0.000 layer.py:103(isFree)
               38410688  180.995    0.000  180.995    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                 600167   30.665    0.000  177.909    0.000 optimizer.py:189(zero_grad)
               19205344  174.816    0.000  174.816    0.000 {built-in method clamp}
                4201176   98.918    0.000  160.484    0.000 layer.py:159(update)
               19205344  111.972    0.000  154.784    0.000 layers.py:77(check)
               19205344  154.670    0.000  154.670    0.000 {built-in method log}
               19205344  154.607    0.000  154.607    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
              252764324   89.711    0.000  144.575    0.000 {built-in method builtins.isinstance}
               19205344  141.741    0.000  141.741    0.000 {built-in method all}
               59266504  128.407    0.000  128.407    0.000 {method 'to' of 'torch._C._TensorBase' objects}
               57616064   38.489    0.000  126.648    0.000 {built-in method builtins.all}
               19205344  125.061    0.000  125.061    0.000 {built-in method multinomial}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9618616: <Attempt5_Coconuts_option_critic_0> in cluster <dcc> Done

Job <Attempt5_Coconuts_option_critic_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Thu May  6 02:11:27 2021
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

    CPU time :                                   258155.62 sec.
    Max Memory :                                 862 MB
    Average Memory :                             847.67 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15522.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   259024 sec.
    Turnaround time :                            507456 sec.

The output (if any) is above this job summary.

