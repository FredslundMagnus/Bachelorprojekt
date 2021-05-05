[W NNPACK.cpp:80] Could not initialize NNPACK! Reason: Unsupported hardware.

# Parameters

    Name :                      SuperLevel2_option_critic-1
    Main :                      option_critic_run
    Level :                     Levels.SuperLevel2
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


      30002396538 function calls (29106815664 primitive calls) in 258900.65 seconds

##    Ordered by: cumulative time
   List reduced from 438 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.649 258900.649 {built-in method builtins.exec}
                      1    0.326    0.326 258900.649 258900.649 <string>:1(<module>)
                      1 3351.607 3351.607 258900.322 258900.322 optionCritic.py:195(option_critic_run)
        1182766779/291326562 8934.722    0.000 112044.509    0.000 module.py:866(_call_impl)
               31848525 8580.609    0.000 105254.942    0.003 optionCritic.py:143(actor_loss_fn)
               99048913  704.398    0.000 104088.513    0.001 optionCritic.py:70(get_state)
               99048913 2453.043    0.000 101348.253    0.001 container.py:117(forward)
                1273941    9.710    0.000 88137.610    0.069 tensor.py:195(backward)
                1273941   12.162    0.000 88127.656    0.069 __init__.py:68(backward)
                1273941 88082.231    0.069 88082.231    0.069 {method 'run_backward' of 'torch._C._EngineBase' objects}
              198097826  768.353    0.000 68106.495    0.000 conv.py:398(forward)
              198097826  342.872    0.000 67028.856    0.000 conv.py:390(_conv_forward)
              198097826 66685.984    0.000 66685.984    0.000 {built-in method conv2d}
               31848525 3415.673    0.000 20014.573    0.001 optionCritic.py:91(get_action)
              390375475 1410.134    0.000 18893.349    0.000 linear.py:93(forward)
              390375475  491.138    0.000 16928.594    0.000 functional.py:1737(linear)
              390375475 16330.167    0.000 16330.167    0.000 {built-in method torch._C._nn.linear}
               31848525 1037.660    0.000 11277.687    0.000 optionCritic.py:80(predict_option_termination)
                 318485   74.302    0.000 7703.267    0.024 optionCritic.py:116(critic_loss_fn)
               63697050  942.158    0.000 7368.594    0.000 distribution.py:34(__init__)
              297146739  378.409    0.000 7030.649    0.000 activation.py:713(forward)
              297146739  379.095    0.000 6652.240    0.000 functional.py:1364(leaky_relu)
               31848525  521.140    0.000 6538.409    0.000 categorical.py:115(log_prob)
              297146739 6188.496    0.000 6188.496    0.000 {built-in method torch._C._nn.leaky_relu}
               31848525  766.771    0.000 5896.599    0.000 categorical.py:49(__init__)
               96413589  398.050    0.000 5556.350    0.000 optionCritic.py:77(get_Q)
               64015535  391.457    0.000 4499.045    0.000 optionCritic.py:88(get_terminations)
               31848525  249.179    0.000 4011.712    0.000 bernoulli.py:34(__init__)
                1273941    7.626    0.000 3914.641    0.003 game.py:41(step)
                1273941   11.362    0.000 3805.017    0.003 layers.py:718(step)
                1273941   28.269    0.000 3778.335    0.003 optimizer.py:84(wrapper)
               31848525 2449.548    0.000 3675.177    0.000 constraints.py:398(check)
                1273941   12.859    0.000 3667.899    0.003 grad_mode.py:24(decorate_context)
                1273941   88.559    0.000 3627.798    0.003 rmsprop.py:56(step)
                1273941  139.497    0.000 3441.742    0.003 _functional.py:203(rmsprop)
               31848525  405.973    0.000 2757.596    0.000 distribution.py:240(_validate_sample)
                1273941   59.427    0.000 2749.671    0.002 layers.py:17(step)
               31848525  198.182    0.000 2685.861    0.000 layer.py:98(move)
               99048913  141.915    0.000 1989.696    0.000 activation.py:101(forward)
               31848525  935.461    0.000 1928.566    0.000 categorical.py:123(entropy)
               31848525  299.115    0.000 1883.364    0.000 layers.py:735(check)
               31848525 1865.455    0.000 1865.455    0.000 constraints.py:249(check)
               99048913  126.399    0.000 1847.781    0.000 functional.py:1195(relu)
               31848525 1793.491    0.000 1793.491    0.000 constraints.py:364(check)
               99048913 1694.713    0.000 1694.713    0.000 {built-in method relu}
              222939675 1651.747    0.000 1651.747    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               17835168 1643.376    0.000 1643.376    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               95545575  192.082    0.000 1620.947    0.000 utils.py:106(__get__)
             1196780130 1563.239    0.000 1563.239    0.000 {built-in method torch._C._get_tracing_state}
               31848525  266.179    0.000 1498.805    0.000 bernoulli.py:86(sample)
               96182545  164.405    0.000 1460.314    0.000 tensor.py:525(__rsub__)
             1532135881 1433.793    0.000 1433.923    0.000 module.py:934(__getattr__)
               95545575 1367.763    0.000 1367.763    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
               99048913   96.477    0.000 1361.275    0.000 flatten.py:39(forward)
               31848525   64.076    0.000 1289.247    0.000 categorical.py:88(logits)
               96182545 1269.277    0.000 1269.277    0.000 {built-in method rsub}
               95864060 1265.235    0.000 1265.235    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
               99048913 1264.798    0.000 1264.798    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               31848525  324.396    0.000 1247.001    0.000 categorical.py:108(sample)
               31848525   67.245    0.000 1225.170    0.000 utils.py:82(probs_to_logits)
               63697050  344.085    0.000 1068.255    0.000 functional.py:46(broadcast_tensors)
                1273942  125.738    0.000 1038.776    0.001 layers.py:684(update)
               64015535 1035.207    0.000 1035.207    0.000 {method 'max' of 'torch._C._TensorBase' objects}
               95545575  944.755    0.000  944.755    0.000 {method 'all' of 'torch._C._TensorBase' objects}
               14013351   39.694    0.000  931.271    0.000 tensor.py:575(__iter__)
             5255963244  902.097    0.000  913.518    0.000 {built-in method builtins.len}
               14013351  860.906    0.000  860.906    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
             4830116029  769.174    0.000  769.174    0.000 {method 'values' of 'collections.OrderedDict' objects}
               31848525  126.731    0.000  757.139    0.000 utils.py:77(clamp_probs)
               31848525  149.914    0.000  752.029    0.000 utils.py:11(broadcast_all)
               13236207  352.436    0.000  736.497    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               31848525  705.710    0.000  705.710    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               63697050  634.983    0.000  634.983    0.000 {built-in method broadcast_tensors}
               31848525  630.408    0.000  630.408    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
               96501030  625.265    0.000  625.265    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
                1273941   64.003    0.000  614.548    0.000 replaybuffer.py:34(save_option_critic)
                 318485  452.413    0.001  596.807    0.002 replaybuffer.py:42(sample_option_critic)
               31848525  587.567    0.000  587.567    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
               31848525  544.662    0.000  544.662    0.000 {built-in method clamp}
              191728120  532.836    0.000  532.836    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               63697050  515.005    0.000  515.005    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               32079569  506.392    0.000  506.392    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               17835168  496.264    0.000  496.264    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               31848525  108.122    0.000  486.485    0.000 layers.py:729(isFree)
               31848525  469.421    0.000  469.421    0.000 {built-in method bernoulli}
               31848525  349.359    0.000  460.357    0.000 layers.py:471(check)
               14013362  281.294    0.000  448.329    0.000 layer.py:151(update)
               17835168  427.201    0.000  427.201    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                1273941   77.601    0.000  422.972    0.000 optimizer.py:189(zero_grad)
               31848525  411.678    0.000  411.678    0.000 {built-in method all}
               17835168  405.632    0.000  405.632    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               31848525  400.786    0.000  400.786    0.000 {built-in method log}
               31848525  395.553    0.000  395.553    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
               13236207   23.150    0.000  384.061    0.000 <__array_function__ internals>:2(prod)
              289462409  308.433    0.000  378.363    0.000 layer.py:95(isFree)
               13236207   21.938    0.000  356.679    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
               13236207   37.244    0.000  334.741    0.000 fromnumeric.py:2912(prod)
               17835168  329.771    0.000  329.771    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              870627943  224.996    0.000  324.698    0.000 enum.py:646(__hash__)
                8599105  315.427    0.000  315.427    0.000 {built-in method tensor}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9601873: <SuperLevel2_option_critic_1> in cluster <dcc> Done

Job <SuperLevel2_option_critic_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Thu Apr 29 21:41:15 2021
Job was executed on host(s) <n-62-23-23>, in queue <hpc>, as user <s183914> in cluster <dcc> at Thu Apr 29 21:41:17 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Apr 29 21:41:17 2021
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

    CPU time :                                   258893.88 sec.
    Max Memory :                                 1180 MB
    Average Memory :                             1157.98 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15204.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258959 sec.
    Turnaround time :                            258908 sec.

The output (if any) is above this job summary.

