[W NNPACK.cpp:80] Could not initialize NNPACK! Reason: Unsupported hardware.

# Parameters

    Name :                      Rocks_option_critic-1
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


      30525597557 function calls (29515416487 primitive calls) in 258900.45 seconds

##    Ordered by: cumulative time
   List reduced from 425 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.454 258900.454 {built-in method builtins.exec}
                      1    0.321    0.321 258900.453 258900.453 <string>:1(<module>)
                      1 3854.710 3854.710 258900.132 258900.132 optionCritic.py:195(option_critic_run)
        1334467210/328956547 9977.052    0.000 99914.892    0.000 module.py:866(_call_impl)
               35923925 9521.021    0.000 99628.995    0.003 optionCritic.py:143(actor_loss_fn)
              111723407  750.978    0.000 91190.269    0.001 optionCritic.py:70(get_state)
              111723407 2658.350    0.000 88198.976    0.001 container.py:117(forward)
                1436957   11.164    0.000 75426.773    0.052 tensor.py:195(backward)
                1436957   12.900    0.000 75415.325    0.052 __init__.py:68(backward)
                1436957 75365.791    0.052 75365.791    0.052 {method 'run_backward' of 'torch._C._EngineBase' objects}
              223446814  850.161    0.000 51683.302    0.000 conv.py:398(forward)
              223446814  353.873    0.000 50522.828    0.000 conv.py:390(_conv_forward)
              223446814 50168.954    0.000 50168.954    0.000 {built-in method conv2d}
                1436957   31.978    0.000 24552.271    0.017 optimizer.py:84(wrapper)
                1436957   19.668    0.000 24424.089    0.017 grad_mode.py:24(decorate_context)
                1436957  101.718    0.000 24369.933    0.017 rmsprop.py:56(step)
                1436957  162.593    0.000 24158.587    0.017 _functional.py:203(rmsprop)
               35923925 3654.639    0.000 21986.157    0.001 optionCritic.py:91(get_action)
               20117392 21222.862    0.001 21222.862    0.001 {method 'sqrt' of 'torch._C._TensorBase' objects}
              440679954 1517.227    0.000 20567.407    0.000 linear.py:93(forward)
              440679954  564.124    0.000 18469.483    0.000 functional.py:1737(linear)
              440679954 17781.649    0.000 17781.649    0.000 {built-in method torch._C._nn.linear}
               35923925 1172.074    0.000 12399.196    0.000 optionCritic.py:80(predict_option_termination)
               71847850 1062.230    0.000 8104.630    0.000 distribution.py:34(__init__)
              335170221  431.468    0.000 7664.908    0.000 activation.py:713(forward)
              335170221  415.882    0.000 7233.440    0.000 functional.py:1364(leaky_relu)
               35923925  581.721    0.000 7220.272    0.000 categorical.py:115(log_prob)
              335170221 6724.605    0.000 6724.605    0.000 {built-in method torch._C._nn.leaky_relu}
               35923925  839.826    0.000 6510.322    0.000 categorical.py:49(__init__)
              109102126  443.954    0.000 6088.296    0.000 optionCritic.py:77(get_Q)
                 359239   81.024    0.000 5453.555    0.015 optionCritic.py:116(critic_loss_fn)
               72207089  457.093    0.000 4937.023    0.000 optionCritic.py:88(get_terminations)
               35923925  272.450    0.000 4390.523    0.000 bernoulli.py:34(__init__)
               35923925 2688.531    0.000 4046.398    0.000 constraints.py:398(check)
                1436957    8.268    0.000 3502.740    0.002 game.py:41(step)
                1436957   12.756    0.000 3399.730    0.002 layers.py:718(step)
               35923925  448.909    0.000 3065.509    0.000 distribution.py:240(_validate_sample)
                1436957   68.619    0.000 2219.947    0.002 layers.py:17(step)
              111723407  168.473    0.000 2195.512    0.000 activation.py:101(forward)
               35923925  187.167    0.000 2145.426    0.000 layer.py:98(move)
               35923925 1036.871    0.000 2130.208    0.000 categorical.py:123(entropy)
               35923925 2073.655    0.000 2073.655    0.000 constraints.py:249(check)
              111723407  146.428    0.000 2027.039    0.000 functional.py:1195(relu)
               35923925 1955.999    0.000 1955.999    0.000 constraints.py:364(check)
              111723407 1852.382    0.000 1852.382    0.000 {built-in method relu}
              107771775  209.961    0.000 1767.069    0.000 utils.py:106(__get__)
             1350273737 1738.681    0.000 1738.681    0.000 {built-in method torch._C._get_tracing_state}
              251467475 1723.696    0.000 1723.696    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               20117392 1680.582    0.000 1680.582    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               35923925  301.466    0.000 1650.160    0.000 bernoulli.py:86(sample)
              108490253  182.438    0.000 1606.142    0.000 tensor.py:525(__rsub__)
             1729244790 1530.769    0.000 1530.919    0.000 module.py:934(__getattr__)
              107771775 1509.328    0.000 1509.328    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
              111723407  107.703    0.000 1505.080    0.000 flatten.py:39(forward)
               35923925  173.067    0.000 1504.923    0.000 layers.py:735(check)
               35923925   70.929    0.000 1397.635    0.000 categorical.py:88(logits)
              111723407 1397.377    0.000 1397.377    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              108490253 1391.268    0.000 1391.268    0.000 {built-in method rsub}
               35923925  356.342    0.000 1371.973    0.000 categorical.py:108(sample)
              108131014 1366.133    0.000 1366.133    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
               35923925   73.058    0.000 1326.706    0.000 utils.py:82(probs_to_logits)
               71847850  375.616    0.000 1181.005    0.000 functional.py:46(broadcast_tensors)
                1436958  144.994    0.000 1161.241    0.001 layers.py:684(update)
               72207089 1135.441    0.000 1135.441    0.000 {method 'max' of 'torch._C._TensorBase' objects}
               35923925  980.621    0.000 1091.005    0.000 layers.py:77(check)
              107771775 1042.658    0.000 1042.658    0.000 {method 'all' of 'torch._C._TensorBase' objects}
             5673579489  989.289    0.000 1003.269    0.000 {built-in method builtins.len}
               15806527   44.523    0.000  980.699    0.000 tensor.py:575(__iter__)
               15806527  902.267    0.000  902.267    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
             5449592247  875.330    0.000  875.330    0.000 {method 'values' of 'collections.OrderedDict' objects}
               35923925  172.002    0.000  840.899    0.000 utils.py:11(broadcast_all)
               35923925  127.770    0.000  805.978    0.000 utils.py:77(clamp_probs)
               35923925  773.969    0.000  773.969    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               71847850  702.613    0.000  702.613    0.000 {built-in method broadcast_tensors}
                1436957   72.378    0.000  681.037    0.000 replaybuffer.py:34(save_option_critic)
               35923925  678.208    0.000  678.208    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
              108849492  675.008    0.000  675.008    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
                 359239  499.958    0.001  645.702    0.002 replaybuffer.py:42(sample_option_critic)
               35923925  644.766    0.000  644.766    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
               35923925  598.950    0.000  598.950    0.000 {built-in method clamp}
              216262028  596.695    0.000  596.695    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               71847850  568.807    0.000  568.807    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               36535798  550.061    0.000  550.061    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               35923925  512.982    0.000  512.982    0.000 {built-in method bernoulli}
               35923925  456.148    0.000  456.148    0.000 {built-in method all}
                1436957   89.604    0.000  451.293    0.000 optimizer.py:189(zero_grad)
               35923925  447.670    0.000  447.670    0.000 {built-in method log}
               35923925  439.390    0.000  439.390    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
               20117392  383.721    0.000  383.721    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               20117392  377.176    0.000  377.176    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               35923925   67.408    0.000  362.019    0.000 layers.py:729(isFree)
                7184790  244.726    0.000  360.736    0.000 layer.py:151(update)
                 611897    9.885    0.000  349.084    0.001 layers.py:740(restart)
               20117392  331.653    0.000  331.653    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               35923925  325.657    0.000  325.657    0.000 {built-in method multinomial}
              475643171  206.596    0.000  301.959    0.000 {built-in method builtins.isinstance}
                9699463  295.109    0.000  295.109    0.000 {built-in method tensor}
              157045772  257.899    0.000  294.611    0.000 layer.py:95(isFree)
              108386544  291.900    0.000  291.900    0.000 {method 'item' of 'torch._C._TensorBase' objects}
              111723421  288.327    0.000  288.327    0.000 {method 'to' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9601879: <Rocks_option_critic_1> in cluster <dcc> Done

Job <Rocks_option_critic_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Thu Apr 29 21:41:20 2021
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

    CPU time :                                   258894.17 sec.
    Max Memory :                                 707 MB
    Average Memory :                             688.74 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15677.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258959 sec.
    Turnaround time :                            258904 sec.

The output (if any) is above this job summary.

