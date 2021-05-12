
# Parameters

    Name :                      Attempt6_Coconuts_option_critic-2
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
    Num :                       2
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              4315 minutes.
    Hours used :                71 hours.

# Profiling


      36369846523 function calls (35404485111 primitive calls) in 258900.82 seconds

##    Ordered by: cumulative time
   List reduced from 438 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.821 258900.821 {built-in method builtins.exec}
                      1    0.364    0.364 258900.821 258900.821 <string>:1(<module>)
                      1 3890.777 3890.777 258900.456 258900.456 optionCritic.py:195(option_critic_run)
                1082243    8.961    0.000 136718.937    0.126 tensor.py:195(backward)
                1082243   11.769    0.000 136709.820    0.126 __init__.py:68(backward)
                1082243 136672.362    0.126 136672.362    0.126 {method 'run_backward' of 'torch._C._EngineBase' objects}
        1279687401/317843946 6362.886    0.000 74051.797    0.000 module.py:866(_call_impl)
               34631776 5362.901    0.000 71082.192    0.002 optionCritic.py:143(actor_loss_fn)
              106871495  544.515    0.000 69224.746    0.001 optionCritic.py:70(get_state)
              106871495 1451.650    0.000 67107.771    0.001 container.py:117(forward)
              213742990  576.816    0.000 40686.032    0.000 conv.py:398(forward)
              213742990  310.916    0.000 39874.249    0.000 conv.py:390(_conv_forward)
              213742990 39563.334    0.000 39563.334    0.000 {built-in method conv2d}
              424715441 1006.625    0.000 16606.842    0.000 linear.py:93(forward)
              424715441  406.816    0.000 15150.195    0.000 functional.py:1737(linear)
              424715441 14642.185    0.000 14642.185    0.000 {built-in method torch._C._nn.linear}
               34631776 2036.634    0.000 12153.628    0.000 optionCritic.py:91(get_action)
               34631776  796.999    0.000 9387.292    0.000 optionCritic.py:80(predict_option_termination)
                1082243   25.185    0.000 6820.694    0.006 optimizer.py:84(wrapper)
                1082243   15.233    0.000 6725.260    0.006 grad_mode.py:24(decorate_context)
                1082243   68.263    0.000 6683.813    0.006 adam.py:55(step)
                1082243  424.493    0.000 6542.483    0.006 _functional.py:53(adam)
               69263552  830.831    0.000 5043.768    0.000 distribution.py:34(__init__)
                1082243    7.724    0.000 4867.064    0.004 game.py:42(step)
                1082243   10.196    0.000 4773.609    0.004 layers.py:827(step)
              320614485  338.445    0.000 4463.262    0.000 activation.py:713(forward)
              320614485  327.874    0.000 4124.817    0.000 functional.py:1364(leaky_relu)
               34631776  340.775    0.000 4041.429    0.000 categorical.py:115(log_prob)
               34631776  316.065    0.000 3857.534    0.000 bernoulli.py:34(__init__)
                 270560   48.722    0.000 3842.400    0.014 optionCritic.py:116(critic_loss_fn)
              320614485 3728.913    0.000 3728.913    0.000 {built-in method torch._C._nn.leaky_relu}
              106806563  243.433    0.000 3614.619    0.000 optionCritic.py:77(get_Q)
               34631776  459.886    0.000 3410.013    0.000 categorical.py:49(__init__)
                1082244  105.371    0.000 3130.687    0.003 layers.py:793(update)
               69534112  254.848    0.000 2775.663    0.000 optionCritic.py:88(get_terminations)
                2370148   33.834    0.000 2217.713    0.001 layers.py:849(restart)
               34631776 1399.430    0.000 2076.385    0.000 constraints.py:398(check)
                2370148   16.085    0.000 1889.893    0.001 level.py:8(__init__)
                2370148  119.485    0.000 1751.624    0.001 levels.py:277(generate)
               34631776  292.565    0.000 1649.888    0.000 distribution.py:240(_validate_sample)
                1082243   53.549    0.000 1627.522    0.002 layers.py:17(step)
               34631776  125.036    0.000 1569.597    0.000 layer.py:106(move)
               21140795  259.588    0.000 1528.226    0.000 level.py:41(notUsed)
               34631776  305.509    0.000 1451.897    0.000 bernoulli.py:86(sample)
               30302792 1443.822    0.000 1443.822    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               34631776 1383.559    0.000 1383.559    0.000 constraints.py:364(check)
              106871495  163.628    0.000 1311.819    0.000 activation.py:101(forward)
               15151396 1267.081    0.000 1267.081    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
             1664165119 1168.110    0.000 1168.194    0.000 module.py:934(__getattr__)
              106871495  121.624    0.000 1148.191    0.000 functional.py:1195(relu)
               34631776  583.661    0.000 1123.197    0.000 categorical.py:123(entropy)
               34631776  180.277    0.000 1123.035    0.000 layers.py:844(check)
               15151396 1073.486    0.000 1073.486    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               34631776 1067.341    0.000 1067.341    0.000 constraints.py:249(check)
              242422432 1060.262    0.000 1060.262    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              104436448  131.938    0.000 1016.834    0.000 tensor.py:525(__rsub__)
              106871495  102.147    0.000 1011.349    0.000 flatten.py:39(forward)
              106871495 1007.732    0.000 1007.732    0.000 {built-in method relu}
              103895328  135.389    0.000 1003.559    0.000 utils.py:106(__get__)
               69263552  357.653    0.000  986.784    0.000 functional.py:46(broadcast_tensors)
              106871495  909.202    0.000  909.202    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               34631776  203.490    0.000  906.940    0.000 utils.py:11(broadcast_all)
               11904673   30.410    0.000  869.947    0.000 tensor.py:575(__iter__)
              104436448  865.373    0.000  865.373    0.000 {built-in method rsub}
               11904673  821.218    0.000  821.218    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               69534112  811.662    0.000  811.662    0.000 {method 'max' of 'torch._C._TensorBase' objects}
               34631776  220.119    0.000  800.539    0.000 categorical.py:108(sample)
               15151396  789.382    0.000  789.382    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
             1291592074  783.527    0.000  783.527    0.000 {built-in method torch._C._get_tracing_state}
               15151396  773.785    0.000  773.785    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              104165888  769.488    0.000  769.488    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
               30302792  763.704    0.000  763.704    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               34631776   41.688    0.000  763.408    0.000 categorical.py:88(logits)
               21140795   20.253    0.000  731.810    0.000 level.py:38(elementsIn)
               34631776   41.877    0.000  721.720    0.000 utils.py:82(probs_to_logits)
             5514857855  704.213    0.000  713.141    0.000 {built-in method builtins.len}
              103895328  702.190    0.000  702.190    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
              103895328  626.843    0.000  626.843    0.000 {method 'all' of 'torch._C._TensorBase' objects}
                 270560  509.348    0.002  617.144    0.002 replaybuffer.py:42(sample_option_critic)
             5225621099  598.658    0.000  598.658    0.000 {method 'values' of 'collections.OrderedDict' objects}
               34631776  547.527    0.000  547.527    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               69263552  525.999    0.000  525.999    0.000 {built-in method broadcast_tensors}
                7575708  359.470    0.000  494.636    0.000 layer.py:159(update)
                1082243   53.957    0.000  478.229    0.000 replaybuffer.py:34(save_option_critic)
               21140795  234.425    0.000  474.236    0.000 level.py:39(<listcomp>)
             1589580753  322.642    0.000  473.380    0.000 enum.py:646(__hash__)
               34631776   86.838    0.000  430.746    0.000 utils.py:77(clamp_probs)
               34631776  427.357    0.000  427.357    0.000 {built-in method bernoulli}
              104707008  399.913    0.000  399.913    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               37001891  355.936    0.000  355.936    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               34631776  343.908    0.000  343.908    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
               34631776  339.895    0.000  339.895    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
              208331776  329.320    0.000  329.320    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                1082243   52.037    0.000  321.849    0.000 optimizer.py:189(zero_grad)
              974380354  316.654    0.000  316.654    0.000 level.py:32(inverse)
               34631776  218.825    0.000  305.814    0.000 layers.py:471(check)
               69263552  296.780    0.000  296.780    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               34631776  289.949    0.000  289.949    0.000 {built-in method clamp}
               16591036   39.588    0.000  286.894    0.000 layer.py:77(restart)
              455793123  177.971    0.000  282.556    0.000 {built-in method builtins.isinstance}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9624170: <Attempt6_Coconuts_option_critic_2> in cluster <dcc> Done

Job <Attempt6_Coconuts_option_critic_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun May  9 01:22:29 2021
Job was executed on host(s) <n-62-11-62>, in queue <hpc>, as user <s183914> in cluster <dcc> at Sun May  9 01:22:30 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun May  9 01:22:30 2021
Terminated at Wed May 12 01:17:34 2021
Results reported at Wed May 12 01:17:34 2021

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

    CPU time :                                   258287.59 sec.
    Max Memory :                                 863 MB
    Average Memory :                             855.24 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15521.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258956 sec.
    Turnaround time :                            258905 sec.

The output (if any) is above this job summary.

