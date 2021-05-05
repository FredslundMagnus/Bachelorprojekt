
# Parameters

    Name :                      Diamonds4_option_critic-2
    Main :                      option_critic_run
    Level :                     Levels.Causal7
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


      52855291067 function calls (51145699184 primitive calls) in 258900.48 seconds

##    Ordered by: cumulative time
   List reduced from 429 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.478 258900.478 {built-in method builtins.exec}
                      1    0.351    0.351 258900.478 258900.478 <string>:1(<module>)
                      1 6225.020 6225.020 258900.127 258900.127 optionCritic.py:195(option_critic_run)
               60796275 9340.064    0.000 112247.805    0.002 optionCritic.py:143(actor_loss_fn)
        2257903344/556215618 10126.252    0.000 111537.516    0.000 module.py:866(_call_impl)
              189076414  839.120    0.000 103887.163    0.001 optionCritic.py:70(get_state)
              189076414 2286.218    0.000 100552.021    0.001 container.py:117(forward)
                2431851   19.148    0.000 75521.901    0.031 tensor.py:195(backward)
                2431851   24.667    0.000 75502.436    0.031 __init__.py:68(backward)
                2431851 75418.821    0.031 75418.821    0.031 {method 'run_backward' of 'torch._C._EngineBase' objects}
              378152828  935.917    0.000 63063.193    0.000 conv.py:398(forward)
              378152828  539.283    0.000 61725.799    0.000 conv.py:390(_conv_forward)
              378152828 61186.517    0.000 61186.517    0.000 {built-in method conv2d}
               60796275 3660.002    0.000 21476.115    0.000 optionCritic.py:91(get_action)
              745292032 1629.612    0.000 21247.974    0.000 linear.py:93(forward)
              745292032  639.470    0.000 18923.341    0.000 functional.py:1737(linear)
              745292032 18126.799    0.000 18126.799    0.000 {built-in method torch._C._nn.linear}
               60796275 1222.672    0.000 14364.830    0.000 optionCritic.py:80(predict_option_termination)
              121592550 1305.557    0.000 8272.899    0.000 distribution.py:34(__init__)
              567229242  533.273    0.000 7528.439    0.000 activation.py:713(forward)
               60796275  604.050    0.000 7130.772    0.000 categorical.py:115(log_prob)
              567229242  555.113    0.000 6995.166    0.000 functional.py:1364(leaky_relu)
                2431851   59.524    0.000 6557.595    0.003 optimizer.py:84(wrapper)
                2431851   29.915    0.000 6351.194    0.003 grad_mode.py:24(decorate_context)
              567229242 6336.176    0.000 6336.176    0.000 {built-in method torch._C._nn.leaky_relu}
                2431851  138.421    0.000 6267.055    0.003 rmsprop.py:56(step)
               60796275  814.307    0.000 6064.004    0.000 categorical.py:49(__init__)
                2431851  136.988    0.000 5974.468    0.002 _functional.py:203(rmsprop)
               60796275  498.393    0.000 5710.377    0.000 bernoulli.py:34(__init__)
              184142417  380.868    0.000 5612.121    0.000 optionCritic.py:77(get_Q)
                 607962   97.426    0.000 4855.879    0.008 optionCritic.py:116(critic_loss_fn)
              122200512  412.828    0.000 4445.524    0.000 optionCritic.py:88(get_terminations)
               60796275 2491.977    0.000 3683.846    0.000 constraints.py:398(check)
                2431851   11.718    0.000 3618.652    0.001 game.py:41(step)
                2431851   22.239    0.000 3479.198    0.001 layers.py:718(step)
               60796275  502.854    0.000 2901.073    0.000 distribution.py:240(_validate_sample)
               34045908 2534.626    0.000 2534.626    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              189076414  319.493    0.000 2195.751    0.000 activation.py:101(forward)
               60796275  465.604    0.000 2174.332    0.000 bernoulli.py:86(sample)
               60796275 2084.339    0.000 2084.339    0.000 constraints.py:364(check)
                2431851   87.731    0.000 2039.872    0.001 layers.py:17(step)
               60796275 1026.938    0.000 1966.677    0.000 categorical.py:123(entropy)
               60796275  157.512    0.000 1944.002    0.000 layer.py:98(move)
               60796275 1886.733    0.000 1886.733    0.000 constraints.py:249(check)
              189076414  218.665    0.000 1876.258    0.000 functional.py:1195(relu)
             2925014095 1869.458    0.000 1869.632    0.000 module.py:934(__getattr__)
               34045908 1869.418    0.000 1869.418    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              182388825  266.194    0.000 1790.256    0.000 utils.py:106(__get__)
              425573925 1710.368    0.000 1710.368    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              189076414  164.029    0.000 1642.210    0.000 flatten.py:39(forward)
              189076414 1629.254    0.000 1629.254    0.000 {built-in method relu}
              183604749  201.484    0.000 1583.988    0.000 tensor.py:525(__rsub__)
              121592550  553.679    0.000 1561.889    0.000 functional.py:46(broadcast_tensors)
                 607962 1280.302    0.002 1526.006    0.003 replaybuffer.py:42(sample_option_critic)
               26750361   61.575    0.000 1490.928    0.000 tensor.py:575(__iter__)
              189076414 1478.181    0.000 1478.181    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                2431852  197.976    0.000 1408.120    0.001 layers.py:684(update)
               60796275  384.913    0.000 1393.339    0.000 categorical.py:108(sample)
               26750361 1393.277    0.000 1393.277    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
              183604749 1352.446    0.000 1352.446    0.000 {built-in method rsub}
               60796275   72.658    0.000 1334.692    0.000 categorical.py:88(logits)
               60796275  282.731    0.000 1305.861    0.000 utils.py:11(broadcast_all)
              122200512 1262.183    0.000 1262.183    0.000 {method 'max' of 'torch._C._TensorBase' objects}
               60796275   78.348    0.000 1262.035    0.000 utils.py:82(probs_to_logits)
              182996787 1251.771    0.000 1251.771    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
             2284653705 1236.151    0.000 1236.151    0.000 {built-in method torch._C._get_tracing_state}
              182388825 1233.140    0.000 1233.140    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
             9766357748 1151.743    0.000 1169.084    0.000 {built-in method builtins.len}
               60796275  254.715    0.000 1167.025    0.000 layers.py:735(check)
              182388825 1033.644    0.000 1033.644    0.000 {method 'all' of 'torch._C._TensorBase' objects}
             9220689790  942.951    0.000  942.951    0.000 {method 'values' of 'collections.OrderedDict' objects}
               60796275  922.680    0.000  922.680    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
              121592550  841.165    0.000  841.165    0.000 {built-in method broadcast_tensors}
                2431851   88.840    0.000  784.626    0.000 replaybuffer.py:34(save_option_critic)
                2431851  108.757    0.000  764.311    0.000 optimizer.py:189(zero_grad)
               60796275  153.290    0.000  737.544    0.000 utils.py:77(clamp_probs)
              184212711  651.887    0.000  651.887    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               60796275  621.175    0.000  621.175    0.000 {built-in method bernoulli}
               13338842  296.667    0.000  616.332    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               34045908  611.446    0.000  611.446    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               60796275  602.198    0.000  602.198    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
               60796275  584.255    0.000  584.255    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
               61333943  564.953    0.000  564.953    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               34045908  544.852    0.000  544.852    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              365993574  534.334    0.000  534.334    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
              121592550  519.090    0.000  519.090    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               60796275  504.984    0.000  504.984    0.000 {built-in method clamp}
               60796275  108.134    0.000  494.853    0.000 layers.py:729(isFree)
               16414996  454.527    0.000  454.527    0.000 {built-in method tensor}
               17022964  274.463    0.000  453.510    0.000 layer.py:167(NoRock_update)
               60796275  446.142    0.000  446.142    0.000 {built-in method log}
              802888792  282.756    0.000  434.095    0.000 {built-in method builtins.isinstance}
               60796275  430.641    0.000  430.641    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
               60796275  404.978    0.000  404.978    0.000 {built-in method all}
               34045894  386.863    0.000  386.863    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              352086897  325.859    0.000  386.719    0.000 layer.py:95(isFree)
              189076428  362.533    0.000  362.533    0.000 {method 'to' of 'torch._C._TensorBase' objects}
              182388850  116.723    0.000  359.508    0.000 {built-in method builtins.all}
               60796275  358.652    0.000  358.652    0.000 {built-in method multinomial}
                7295557   16.448    0.000  350.281    0.000 game.py:37(board)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9601868: <Diamonds4_option_critic_2> in cluster <dcc> Done

Job <Diamonds4_option_critic_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Thu Apr 29 21:41:12 2021
Job was executed on host(s) <n-62-11-66>, in queue <hpc>, as user <s183914> in cluster <dcc> at Thu Apr 29 21:41:15 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Apr 29 21:41:15 2021
Terminated at Sun May  2 21:36:17 2021
Results reported at Sun May  2 21:36:17 2021

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

    CPU time :                                   258286.12 sec.
    Max Memory :                                 870 MB
    Average Memory :                             856.51 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15514.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258919 sec.
    Turnaround time :                            258905 sec.

The output (if any) is above this job summary.

