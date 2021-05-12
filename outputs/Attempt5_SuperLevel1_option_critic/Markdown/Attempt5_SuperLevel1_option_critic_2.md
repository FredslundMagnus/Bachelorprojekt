
# Parameters

    Name :                      Attempt5_SuperLevel1_option_critic-2
    Main :                      option_critic_run
    Level :                     Levels.SuperLevel
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


      18035661441 function calls (17506592656 primitive calls) in 258901.91 seconds

##    Ordered by: cumulative time
   List reduced from 445 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258901.915 258901.915 {built-in method builtins.exec}
                      1    0.321    0.321 258901.915 258901.915 <string>:1(<module>)
                      1 1912.706 1912.706 258901.593 258901.593 optionCritic.py:195(option_critic_run)
                 593126    5.051    0.000 191023.407    0.322 tensor.py:195(backward)
                 593126    6.327    0.000 191018.258    0.322 __init__.py:68(backward)
                 593126 190997.915    0.322 190997.915    0.322 {method 'run_backward' of 'torch._C._EngineBase' objects}
               18980032 3209.014    0.000 40143.492    0.002 optionCritic.py:143(actor_loss_fn)
        700088514/172947786 3512.173    0.000 40124.411    0.000 module.py:866(_call_impl)
               58571192  282.053    0.000 37399.364    0.001 optionCritic.py:70(get_state)
               58571192  766.443    0.000 36259.069    0.001 container.py:117(forward)
              117142384  340.901    0.000 23441.755    0.000 conv.py:398(forward)
              117142384  175.782    0.000 22956.231    0.000 conv.py:390(_conv_forward)
              117142384 22780.448    0.000 22780.448    0.000 {built-in method conv2d}
              231518978  588.259    0.000 7337.861    0.000 linear.py:93(forward)
               18980032 1216.930    0.000 7267.399    0.000 optionCritic.py:91(get_action)
              231518978  223.825    0.000 6501.140    0.000 functional.py:1737(linear)
              231518978 6223.276    0.000 6223.276    0.000 {built-in method torch._C._nn.linear}
                 593126   13.741    0.000 5340.626    0.009 optimizer.py:84(wrapper)
                 593126    7.535    0.000 5288.001    0.009 grad_mode.py:24(decorate_context)
                 593126   41.471    0.000 5266.823    0.009 adam.py:55(step)
                 593126  234.460    0.000 5179.825    0.009 _functional.py:53(adam)
               18980032  404.706    0.000 4824.778    0.000 optionCritic.py:80(predict_option_termination)
               37960064  434.603    0.000 2787.363    0.000 distribution.py:34(__init__)
              175713576  178.121    0.000 2534.516    0.000 activation.py:713(forward)
               18980032  202.329    0.000 2415.672    0.000 categorical.py:115(log_prob)
              175713576  181.552    0.000 2356.395    0.000 functional.py:1364(leaky_relu)
                 593126    3.143    0.000 2268.897    0.004 game.py:42(step)
                 593126    5.541    0.000 2222.554    0.004 layers.py:827(step)
              175713576 2132.842    0.000 2132.842    0.000 {built-in method torch._C._nn.leaky_relu}
               18980032  268.906    0.000 2048.324    0.000 categorical.py:49(__init__)
               57288217  139.152    0.000 1977.562    0.000 optionCritic.py:77(get_Q)
               18980032  139.928    0.000 1840.064    0.000 bernoulli.py:34(__init__)
                 593126   30.719    0.000 1638.817    0.003 layers.py:17(step)
               18980032  104.747    0.000 1605.452    0.000 layer.py:106(move)
                 148281   24.600    0.000 1589.733    0.011 optionCritic.py:116(critic_loss_fn)
               38108345  140.456    0.000 1548.572    0.000 optionCritic.py:88(get_terminations)
               18980032  844.716    0.000 1247.375    0.000 constraints.py:398(check)
               16607516 1152.000    0.000 1152.000    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               18980032  188.564    0.000 1093.882    0.000 layers.py:844(check)
                8303758 1085.855    0.000 1085.855    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               18980032  172.256    0.000  975.388    0.000 distribution.py:240(_validate_sample)
                8303758  855.053    0.000  855.053    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               58571192   75.526    0.000  725.383    0.000 activation.py:101(forward)
               18980032  707.481    0.000  707.481    0.000 constraints.py:364(check)
               18980032  131.255    0.000  697.956    0.000 bernoulli.py:86(sample)
               18980032  347.034    0.000  669.432    0.000 categorical.py:123(entropy)
              908307737  655.845    0.000  655.892    0.000 module.py:934(__getattr__)
               58571192   76.657    0.000  649.857    0.000 functional.py:1195(relu)
               18980032  625.348    0.000  625.348    0.000 constraints.py:249(check)
                8303758  622.606    0.000  622.606    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               16607516  621.078    0.000  621.078    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               56940096   81.345    0.000  607.778    0.000 utils.py:106(__get__)
                8303758  604.596    0.000  604.596    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              132860224  579.765    0.000  579.765    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                 593127   61.409    0.000  575.386    0.001 layers.py:793(update)
               58571192  562.262    0.000  562.262    0.000 {built-in method relu}
               58571192   57.355    0.000  559.483    0.000 flatten.py:39(forward)
               57236658   64.228    0.000  535.787    0.000 tensor.py:525(__rsub__)
               37960064  184.656    0.000  521.235    0.000 functional.py:46(broadcast_tensors)
               58571192  502.128    0.000  502.128    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               18980032  132.457    0.000  480.574    0.000 categorical.py:108(sample)
               18980032   25.493    0.000  462.692    0.000 categorical.py:88(logits)
               57236658  460.851    0.000  460.851    0.000 {built-in method rsub}
                6524386   15.772    0.000  442.412    0.000 tensor.py:575(__iter__)
              706612900  442.233    0.000  442.233    0.000 {built-in method torch._C._get_tracing_state}
               18980032   24.702    0.000  437.199    0.000 utils.py:82(probs_to_logits)
               57088377  436.620    0.000  436.620    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
               38108345  429.356    0.000  429.356    0.000 {method 'max' of 'torch._C._TensorBase' objects}
             3134799669  424.081    0.000  428.695    0.000 {built-in method builtins.len}
               56940096  421.018    0.000  421.018    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                6524386  416.781    0.000  416.781    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               18980032   82.615    0.000  413.786    0.000 utils.py:11(broadcast_all)
             2858925248  349.561    0.000  349.561    0.000 {method 'values' of 'collections.OrderedDict' objects}
               56940096  348.848    0.000  348.848    0.000 {method 'all' of 'torch._C._TensorBase' objects}
               18980032   70.970    0.000  340.842    0.000 layers.py:838(isFree)
                 148281  250.295    0.002  317.863    0.002 replaybuffer.py:42(sample_option_critic)
               18980032  317.758    0.000  317.758    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               37960064  271.853    0.000  271.853    0.000 {built-in method broadcast_tensors}
              231044578  211.556    0.000  269.871    0.000 layer.py:103(isFree)
               18980032   51.937    0.000  260.898    0.000 utils.py:77(clamp_probs)
               18980032  185.698    0.000  252.592    0.000 layers.py:471(check)
                 593126   29.391    0.000  250.676    0.000 replaybuffer.py:34(save_option_critic)
                7710651  146.137    0.000  250.577    0.000 layer.py:159(update)
               19031591  221.598    0.000  221.598    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               57384939  221.468    0.000  221.468    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               18980032  212.793    0.000  212.793    0.000 {built-in method bernoulli}
               18980032  208.962    0.000  208.962    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
               18980032  201.906    0.000  201.906    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
              559449011  140.745    0.000  201.611    0.000 enum.py:646(__hash__)
              114176754  185.499    0.000  185.499    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                 593126   30.694    0.000  182.394    0.000 optimizer.py:189(zero_grad)
               37960064  179.958    0.000  179.958    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               18980032  170.959    0.000  170.959    0.000 {built-in method clamp}
               18928474   35.117    0.000  164.821    0.000 {built-in method builtins.any}
               18980032  112.596    0.000  156.768    0.000 layers.py:77(check)
               18980032  151.599    0.000  151.599    0.000 {built-in method log}
               18980032  147.347    0.000  147.347    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
                4003603  136.052    0.000  136.052    0.000 {built-in method tensor}
               18980032  135.254    0.000  135.254    0.000 {built-in method all}
                2738446   61.510    0.000  132.489    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9618609: <Attempt5_SuperLevel1_option_critic_2> in cluster <dcc> Done

Job <Attempt5_SuperLevel1_option_critic_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Thu May  6 02:11:26 2021
Job was executed on host(s) <n-62-31-4>, in queue <hpc>, as user <s183914> in cluster <dcc> at Sat May  8 23:13:45 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat May  8 23:13:45 2021
Terminated at Tue May 11 23:09:02 2021
Results reported at Tue May 11 23:09:02 2021

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

    CPU time :                                   258235.58 sec.
    Max Memory :                                 1311 MB
    Average Memory :                             1281.77 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15073.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258972 sec.
    Turnaround time :                            507456 sec.

The output (if any) is above this job summary.

