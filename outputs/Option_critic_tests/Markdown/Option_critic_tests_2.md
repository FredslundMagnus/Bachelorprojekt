
# Parameters

    Name :                      Option_critic_tests-2
    Main :                      option_critic_run
    Level :                     Levels.Causal1
    Failed actions chance :     0.0
    Hours :                     0.1
    Batch :                     100
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
    Minutes used :              1 minutes.
    Hours used :                0 hours.

# Profiling


      11455675 function calls (11076139 primitive calls) in 60.59 seconds

##    Ordered by: cumulative time
   List reduced from 428 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000   60.588   60.588 {built-in method builtins.exec}
                      1    0.035    0.035   60.587   60.587 <string>:1(<module>)
                      1    1.602    1.602   60.553   60.553 optionCritic.py:195(option_critic_run)
                  13900    2.500    0.000   28.297    0.002 optionCritic.py:143(actor_loss_fn)
          504372/125643    2.521    0.000   26.600    0.000 module.py:866(_call_impl)
                  42081    0.195    0.000   24.645    0.001 optionCritic.py:70(get_state)
                  42081    0.584    0.000   23.850    0.001 container.py:117(forward)
                    139    0.001    0.000   17.357    0.125 tensor.py:195(backward)
                    139    0.002    0.000   17.356    0.125 __init__.py:68(backward)
                    139   17.350    0.125   17.350    0.125 {method 'run_backward' of 'torch._C._EngineBase' objects}
                  84162    0.228    0.000   14.666    0.000 conv.py:398(forward)
                  84162    0.130    0.000   14.343    0.000 conv.py:390(_conv_forward)
                  84162   14.213    0.000   14.213    0.000 {built-in method conv2d}
                  13900    0.975    0.000    5.442    0.000 optionCritic.py:91(get_action)
                 167724    0.413    0.000    5.202    0.000 linear.py:93(forward)
                 167724    0.165    0.000    4.618    0.000 functional.py:1737(linear)
                 167724    4.414    0.000    4.414    0.000 {built-in method torch._C._nn.linear}
                  13900    0.308    0.000    3.829    0.000 optionCritic.py:80(predict_option_termination)
                  27800    0.328    0.000    2.208    0.000 distribution.py:34(__init__)
                 126243    0.141    0.000    1.815    0.000 activation.py:713(forward)
                  13900    0.145    0.000    1.789    0.000 categorical.py:115(log_prob)
                 126243    0.143    0.000    1.674    0.000 functional.py:1364(leaky_relu)
                  13900    0.133    0.000    1.660    0.000 bernoulli.py:34(__init__)
                 126243    1.502    0.000    1.502    0.000 {built-in method torch._C._nn.leaky_relu}
                  13900    0.198    0.000    1.484    0.000 categorical.py:49(__init__)
                  41828    0.093    0.000    1.365    0.000 optionCritic.py:77(get_Q)
                  27834    0.105    0.000    1.139    0.000 optionCritic.py:88(get_terminations)
                  13900    0.620    0.000    0.913    0.000 constraints.py:398(check)
                  13900    0.116    0.000    0.700    0.000 distribution.py:240(_validate_sample)
                  13900    0.651    0.000    0.651    0.000 constraints.py:364(check)
                  13900    0.118    0.000    0.576    0.000 bernoulli.py:86(sample)
                  13778    0.257    0.000    0.555    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                    139    0.001    0.000    0.548    0.004 game.py:41(step)
                    139    0.001    0.000    0.533    0.004 layers.py:718(step)
                  42081    0.057    0.000    0.527    0.000 activation.py:101(forward)
                  41700    0.057    0.000    0.487    0.000 utils.py:106(__get__)
                  13900    0.252    0.000    0.480    0.000 categorical.py:123(entropy)
                  42081    0.051    0.000    0.471    0.000 functional.py:1195(relu)
                  13900    0.460    0.000    0.460    0.000 constraints.py:249(check)
                  97300    0.447    0.000    0.447    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                 657288    0.447    0.000    0.447    0.000 module.py:934(__getattr__)
                  27800    0.147    0.000    0.420    0.000 functional.py:46(broadcast_tensors)
                  41768    0.049    0.000    0.419    0.000 tensor.py:525(__rsub__)
                  42081    0.044    0.000    0.418    0.000 flatten.py:39(forward)
                  42081    0.412    0.000    0.412    0.000 {built-in method relu}
                  13900    0.017    0.000    0.386    0.000 categorical.py:88(logits)
                  42081    0.374    0.000    0.374    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                  13900    0.082    0.000    0.374    0.000 utils.py:11(broadcast_all)
                  13900    0.019    0.000    0.369    0.000 utils.py:82(probs_to_logits)
                  41768    0.362    0.000    0.362    0.000 {built-in method rsub}
                   1529    0.005    0.000    0.360    0.000 tensor.py:575(__iter__)
                   1529    0.351    0.000    0.351    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
                  13900    0.092    0.000    0.350    0.000 categorical.py:108(sample)
                  27834    0.339    0.000    0.339    0.000 {method 'max' of 'torch._C._TensorBase' objects}
                 505901    0.330    0.000    0.330    0.000 {built-in method torch._C._get_tracing_state}
                     34    0.007    0.000    0.323    0.010 optionCritic.py:116(critic_loss_fn)
                  41734    0.320    0.000    0.320    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
                    139    0.015    0.000    0.315    0.002 layers.py:17(step)
                  41700    0.305    0.000    0.305    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                  13900    0.029    0.000    0.298    0.000 layer.py:98(move)
                  13778    0.019    0.000    0.298    0.000 <__array_function__ internals>:2(prod)
                  13900    0.286    0.000    0.286    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
                2161022    0.278    0.000    0.279    0.000 {built-in method builtins.len}
                  41700    0.277    0.000    0.277    0.000 {method 'all' of 'torch._C._TensorBase' objects}
                  13778    0.018    0.000    0.276    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                    140    0.025    0.000    0.260    0.002 layers.py:684(update)
                  13778    0.027    0.000    0.258    0.000 fromnumeric.py:2912(prod)
                  13778    0.061    0.000    0.231    0.000 fromnumeric.py:70(_wrapreduction)
                  27800    0.230    0.000    0.230    0.000 {built-in method broadcast_tensors}
                2059569    0.227    0.000    0.227    0.000 {method 'values' of 'collections.OrderedDict' objects}
                    139    0.022    0.000    0.209    0.002 replaybuffer.py:34(save_option_critic)
                  13900    0.182    0.000    0.182    0.000 {built-in method bernoulli}
                  13900    0.039    0.000    0.180    0.000 utils.py:77(clamp_probs)
                  13900    0.170    0.000    0.170    0.000 {built-in method log}
                  41802    0.163    0.000    0.163    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
                    139    0.004    0.000    0.162    0.001 optimizer.py:84(wrapper)
                  13900    0.046    0.000    0.153    0.000 layers.py:735(check)
                  13900    0.151    0.000    0.151    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
                    139    0.002    0.000    0.148    0.001 grad_mode.py:24(decorate_context)
                  13778    0.144    0.000    0.144    0.000 {method 'reduce' of 'numpy.ufunc' objects}
                  13960    0.143    0.000    0.143    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                    139    0.008    0.000    0.143    0.001 rmsprop.py:56(step)
                  13900    0.141    0.000    0.141    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
                  83468    0.139    0.000    0.139    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                  27800    0.128    0.000    0.128    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                    139    0.009    0.000    0.125    0.001 _functional.py:203(rmsprop)
                  13900    0.122    0.000    0.122    0.000 {built-in method clamp}
                 182325    0.069    0.000    0.111    0.000 {built-in method builtins.isinstance}
                  13900    0.108    0.000    0.108    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
                  13900    0.099    0.000    0.099    0.000 {built-in method multinomial}
                  13900    0.098    0.000    0.098    0.000 {built-in method all}
                  13900    0.022    0.000    0.090    0.000 layers.py:729(isFree)
                  42095    0.090    0.000    0.090    0.000 {method 'to' of 'torch._C._TensorBase' objects}
                  41800    0.029    0.000    0.084    0.000 {built-in method builtins.all}
                  41859    0.080    0.000    0.080    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                  14065    0.035    0.000    0.072    0.000 grad_mode.py:119(__enter__)
                  97754    0.064    0.000    0.071    0.000 {built-in method builtins.getattr}
                    840    0.041    0.000    0.070    0.000 layer.py:167(NoRock_update)
                  27800    0.066    0.000    0.069    0.000 distribution.py:226(_extended_shape)
                    159    0.002    0.000    0.069    0.000 layers.py:740(restart)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9601823: <Option_critic_tests_2> in cluster <dcc> Done

Job <Option_critic_tests_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Thu Apr 29 21:06:51 2021
Job was executed on host(s) <n-62-11-69>, in queue <hpc>, as user <s183914> in cluster <dcc> at Thu Apr 29 21:06:54 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Apr 29 21:06:54 2021
Terminated at Thu Apr 29 21:08:00 2021
Results reported at Thu Apr 29 21:08:00 2021

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

    CPU time :                                   61.90 sec.
    Max Memory :                                 143 MB
    Average Memory :                             95.33 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               16241.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   126 sec.
    Turnaround time :                            69 sec.

The output (if any) is above this job summary.

