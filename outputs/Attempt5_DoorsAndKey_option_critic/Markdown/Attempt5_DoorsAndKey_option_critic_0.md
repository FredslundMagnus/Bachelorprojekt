
# Parameters

    Name :                      Attempt5_DoorsAndKey_option_critic-0
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


      17308216363 function calls (16728928535 primitive calls) in 258901.83 seconds

##    Ordered by: cumulative time
   List reduced from 429 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258901.825 258901.825 {built-in method builtins.exec}
                      1    0.339    0.339 258901.825 258901.825 <string>:1(<module>)
                      1 2094.987 2094.987 258901.486 258901.486 optionCritic.py:195(option_critic_run)
                 649425    5.077    0.000 186792.032    0.288 tensor.py:195(backward)
                 649425    6.906    0.000 186786.850    0.288 __init__.py:68(backward)
                 649425 186764.049    0.288 186764.049    0.288 {method 'run_backward' of 'torch._C._EngineBase' objects}
        766579438/189402967 3813.259    0.000 45235.573    0.000 module.py:866(_call_impl)
               20781600 3550.592    0.000 44555.397    0.002 optionCritic.py:143(actor_loss_fn)
               64130719  295.273    0.000 42319.844    0.001 optionCritic.py:70(get_state)
               64130719  837.881    0.000 41091.236    0.001 container.py:117(forward)
              128261438  365.275    0.000 25635.454    0.000 conv.py:398(forward)
              128261438  184.897    0.000 25126.062    0.000 conv.py:390(_conv_forward)
              128261438 24941.165    0.000 24941.165    0.000 {built-in method conv2d}
              253533686  627.893    0.000 9480.496    0.000 linear.py:93(forward)
              253533686  239.043    0.000 8589.229    0.000 functional.py:1737(linear)
              253533686 8289.942    0.000 8289.942    0.000 {built-in method torch._C._nn.linear}
               20781600 1327.437    0.000 7924.172    0.000 optionCritic.py:91(get_action)
               20781600  442.441    0.000 5335.894    0.000 optionCritic.py:80(predict_option_termination)
                 649425   15.881    0.000 3645.590    0.006 optimizer.py:84(wrapper)
                 649425    8.016    0.000 3588.059    0.006 grad_mode.py:24(decorate_context)
                 649425   42.498    0.000 3564.865    0.005 adam.py:55(step)
                 649425  243.889    0.000 3473.624    0.005 _functional.py:53(adam)
               41563200  479.165    0.000 3128.553    0.000 distribution.py:34(__init__)
              192392157  190.337    0.000 2711.314    0.000 activation.py:713(forward)
               20781600  218.510    0.000 2643.245    0.000 categorical.py:115(log_prob)
              192392157  200.866    0.000 2520.977    0.000 functional.py:1364(leaky_relu)
              192392157 2278.186    0.000 2278.186    0.000 {built-in method torch._C._nn.leaky_relu}
               20781600  294.804    0.000 2217.644    0.000 categorical.py:49(__init__)
               20781600  165.440    0.000 2155.928    0.000 bernoulli.py:34(__init__)
               62765092  146.288    0.000 2116.587    0.000 optionCritic.py:77(get_Q)
                 162356   27.455    0.000 2015.696    0.012 optionCritic.py:116(critic_loss_fn)
               41725556  154.738    0.000 1672.663    0.000 optionCritic.py:88(get_terminations)
               20781600  908.795    0.000 1352.144    0.000 constraints.py:398(check)
                 649425    3.574    0.000 1129.947    0.002 game.py:42(step)
                 649425    6.095    0.000 1087.910    0.002 layers.py:827(step)
               20781600  192.372    0.000 1076.448    0.000 distribution.py:240(_validate_sample)
               20781600  833.299    0.000  833.299    0.000 constraints.py:364(check)
               64130719   84.116    0.000  788.003    0.000 activation.py:101(forward)
               20781600  155.317    0.000  766.487    0.000 bernoulli.py:86(sample)
               18183888  755.234    0.000  755.234    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               20781600  384.223    0.000  735.930    0.000 categorical.py:123(entropy)
              994640910  712.365    0.000  712.417    0.000 module.py:934(__getattr__)
               64130719   72.403    0.000  703.887    0.000 functional.py:1195(relu)
               20781600  690.402    0.000  690.402    0.000 constraints.py:249(check)
              145471200  673.440    0.000  673.440    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                9091944  666.111    0.000  666.111    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               62344800   90.381    0.000  664.020    0.000 utils.py:106(__get__)
                 649425   30.067    0.000  624.332    0.001 layers.py:17(step)
               64130719  619.781    0.000  619.781    0.000 {built-in method relu}
               64130719   62.201    0.000  607.988    0.000 flatten.py:39(forward)
               20781600   55.077    0.000  591.372    0.000 layer.py:106(move)
                9091944  588.208    0.000  588.208    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               62669512   70.122    0.000  587.914    0.000 tensor.py:525(__rsub__)
               41563200  201.482    0.000  567.529    0.000 functional.py:46(broadcast_tensors)
               64130719  545.787    0.000  545.787    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               20781600  142.443    0.000  526.131    0.000 categorical.py:108(sample)
                7143675   17.843    0.000  524.343    0.000 tensor.py:575(__iter__)
               62669512  506.041    0.000  506.041    0.000 {built-in method rsub}
               20781600   26.463    0.000  501.712    0.000 categorical.py:88(logits)
                7143675  495.803    0.000  495.803    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               41725556  479.185    0.000  479.185    0.000 {method 'max' of 'torch._C._TensorBase' objects}
              773723113  478.999    0.000  478.999    0.000 {built-in method torch._C._get_tracing_state}
               20781600   26.259    0.000  475.248    0.000 utils.py:82(probs_to_logits)
               20781600   99.566    0.000  475.169    0.000 utils.py:11(broadcast_all)
               62507156  471.779    0.000  471.779    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
               62344800  459.188    0.000  459.188    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
             3290672233  452.353    0.000  457.156    0.000 {built-in method builtins.len}
                 649426   66.678    0.000  454.312    0.001 layers.py:793(update)
               18183888  417.495    0.000  417.495    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                9091944  405.368    0.000  405.368    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               62344800  397.324    0.000  397.324    0.000 {method 'all' of 'torch._C._TensorBase' objects}
                9091944  393.711    0.000  393.711    0.000 {method 'add' of 'torch._C._TensorBase' objects}
             3130448471  383.915    0.000  383.915    0.000 {method 'values' of 'collections.OrderedDict' objects}
               20781600  344.054    0.000  344.054    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
                 162356  276.377    0.002  343.164    0.002 replaybuffer.py:42(sample_option_critic)
               41563200  308.400    0.000  308.400    0.000 {built-in method broadcast_tensors}
               20781600   56.156    0.000  282.333    0.000 utils.py:77(clamp_probs)
               20781600   85.656    0.000  278.506    0.000 layers.py:844(check)
                 649425   31.592    0.000  274.969    0.000 replaybuffer.py:34(save_option_critic)
               62831868  244.711    0.000  244.711    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               20781600  228.910    0.000  228.910    0.000 {built-in method bernoulli}
               20781600  226.178    0.000  226.178    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
               20781600  223.937    0.000  223.937    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
               20781600   41.580    0.000  204.938    0.000 layers.py:838(isFree)
              125014312  203.551    0.000  203.551    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               20877180  199.378    0.000  199.378    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               41563200  194.909    0.000  194.909    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                 649425   32.916    0.000  189.209    0.000 optimizer.py:189(zero_grad)
               20781600  184.155    0.000  184.155    0.000 {built-in method clamp}
               20781600  166.656    0.000  166.656    0.000 {built-in method log}
              119548937  135.420    0.000  163.359    0.000 layer.py:103(isFree)
               20781600  162.823    0.000  162.823    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
               62344832   43.807    0.000  153.611    0.000 {built-in method builtins.all}
               20781600  149.755    0.000  149.755    0.000 {built-in method all}
              273509605   98.778    0.000  144.455    0.000 {built-in method builtins.isinstance}
                3896556   85.482    0.000  143.432    0.000 layer.py:175(NoRock_update)
                4383622  136.641    0.000  136.641    0.000 {built-in method tensor}
               20781600  135.488    0.000  135.488    0.000 {built-in method multinomial}
               64130733  132.395    0.000  132.395    0.000 {method 'to' of 'torch._C._TensorBase' objects}
               62441709  119.733    0.000  119.733    0.000 {method 'item' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9618622: <Attempt5_DoorsAndKey_option_critic_0> in cluster <dcc> Done

Job <Attempt5_DoorsAndKey_option_critic_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Thu May  6 02:11:28 2021
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

    CPU time :                                   258277.25 sec.
    Max Memory :                                 792 MB
    Average Memory :                             781.85 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15592.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   259024 sec.
    Turnaround time :                            507455 sec.

The output (if any) is above this job summary.

