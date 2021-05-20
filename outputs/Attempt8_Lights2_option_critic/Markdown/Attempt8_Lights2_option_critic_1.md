[W NNPACK.cpp:80] Could not initialize NNPACK! Reason: Unsupported hardware.

# Parameters

    Name :                      Attempt8_Lights2_option_critic-1
    Main :                      option_critic_run
    Level :                     Levels.Causal4
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
    Num :                       1
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              4315 minutes.
    Hours used :                71 hours.

# Profiling


      34080557028 function calls (33027255081 primitive calls) in 258901.00 seconds

##    Ordered by: cumulative time
   List reduced from 439 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.997 258900.997 {built-in method builtins.exec}
                      1    0.348    0.348 258900.997 258900.997 <string>:1(<module>)
                      1 3970.768 3970.768 258900.649 258900.649 optionCritic.py:195(option_critic_run)
        1393966459/344502919 9998.086    0.000 126252.227    0.000 module.py:866(_call_impl)
               37786592 8920.429    0.000 119875.085    0.003 optionCritic.py:143(actor_loss_fn)
              116607060  761.113    0.000 116939.558    0.001 optionCritic.py:70(get_state)
              116607060 2685.701    0.000 113882.276    0.001 container.py:117(forward)
              233214120  902.379    0.000 76599.080    0.000 conv.py:398(forward)
              233214120  374.120    0.000 75374.644    0.000 conv.py:390(_conv_forward)
              233214120 75000.524    0.000 75000.524    0.000 {built-in method conv2d}
                1180831    9.649    0.000 67739.059    0.057 tensor.py:195(backward)
                1180831   10.812    0.000 67729.177    0.057 __init__.py:68(backward)
                1180831 67688.731    0.057 67688.731    0.057 {method 'run_backward' of 'torch._C._EngineBase' objects}
               37786592 3994.160    0.000 23385.366    0.001 optionCritic.py:91(get_action)
              461109979 1630.043    0.000 21271.180    0.000 linear.py:93(forward)
              461109979  587.772    0.000 19040.411    0.000 functional.py:1737(linear)
              461109979 18337.400    0.000 18337.400    0.000 {built-in method torch._C._nn.linear}
               37786592 1161.922    0.000 12659.426    0.000 optionCritic.py:80(predict_option_termination)
               75573184 1055.024    0.000 8404.684    0.000 distribution.py:34(__init__)
              349821180  437.594    0.000 8084.516    0.000 activation.py:713(forward)
              349821180  427.720    0.000 7646.921    0.000 functional.py:1364(leaky_relu)
               37786592  599.400    0.000 7617.288    0.000 categorical.py:115(log_prob)
              349821180 7128.940    0.000 7128.940    0.000 {built-in method torch._C._nn.leaky_relu}
                 295207   67.303    0.000 6993.240    0.024 optionCritic.py:116(critic_loss_fn)
               37786592  890.747    0.000 6862.149    0.000 categorical.py:49(__init__)
              114240876  467.577    0.000 6433.071    0.000 optionCritic.py:77(get_Q)
               75868391  455.677    0.000 5243.001    0.000 optionCritic.py:88(get_terminations)
               37786592  271.061    0.000 4394.480    0.000 bernoulli.py:34(__init__)
               37786592 2832.263    0.000 4271.964    0.000 constraints.py:398(check)
                1180831   24.845    0.000 3741.828    0.003 optimizer.py:84(wrapper)
                1180831   11.016    0.000 3645.102    0.003 grad_mode.py:24(decorate_context)
                1180831   80.702    0.000 3610.910    0.003 rmsprop.py:56(step)
                1180831    8.068    0.000 3444.843    0.003 game.py:42(step)
                1180831  124.227    0.000 3439.413    0.003 _functional.py:203(rmsprop)
                1180831   10.307    0.000 3345.929    0.003 layers.py:827(step)
               37786592  468.321    0.000 3199.881    0.000 distribution.py:240(_validate_sample)
              116607060  160.885    0.000 2287.352    0.000 activation.py:101(forward)
               37786592 1102.799    0.000 2262.301    0.000 categorical.py:123(entropy)
                1180831   61.629    0.000 2225.366    0.002 layers.py:17(step)
               37786592 2160.004    0.000 2160.004    0.000 constraints.py:249(check)
               37786592  171.561    0.000 2159.382    0.000 layer.py:106(move)
              116607060  138.686    0.000 2126.467    0.000 functional.py:1195(relu)
               37786592 2013.205    0.000 2013.205    0.000 constraints.py:364(check)
               16531628 1991.872    0.000 1991.872    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              116607060 1960.849    0.000 1960.849    0.000 {built-in method relu}
              113359776  202.853    0.000 1873.860    0.000 utils.py:106(__get__)
             1406955600 1790.883    0.000 1790.883    0.000 {built-in method torch._C._get_tracing_state}
              264506144 1764.376    0.000 1764.376    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              113950190  177.538    0.000 1685.830    0.000 tensor.py:525(__rsub__)
               37786592  277.229    0.000 1624.320    0.000 bernoulli.py:86(sample)
              113359776 1606.296    0.000 1606.296    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
              116607060  107.266    0.000 1565.035    0.000 flatten.py:39(forward)
             1808877878 1561.134    0.000 1561.247    0.000 module.py:934(__getattr__)
               37786592   73.985    0.000 1507.706    0.000 categorical.py:88(logits)
              113654983 1483.057    0.000 1483.057    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
              113950190 1474.047    0.000 1474.047    0.000 {built-in method rsub}
               37786592  371.964    0.000 1458.034    0.000 categorical.py:108(sample)
              116607060 1457.769    0.000 1457.769    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               37786592   78.251    0.000 1433.721    0.000 utils.py:82(probs_to_logits)
               37786592  288.829    0.000 1403.726    0.000 layers.py:844(check)
               26545001  633.175    0.000 1332.912    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               75573184  384.480    0.000 1229.794    0.000 functional.py:46(broadcast_tensors)
               75868391 1195.045    0.000 1195.045    0.000 {method 'max' of 'torch._C._TensorBase' objects}
                1180832  122.064    0.000 1104.521    0.001 layers.py:793(update)
              113359776 1097.966    0.000 1097.966    0.000 {method 'all' of 'torch._C._TensorBase' objects}
             6135573460 1049.335    0.000 1059.446    0.000 {built-in method builtins.len}
               12989141   36.328    0.000  931.180    0.000 tensor.py:575(__iter__)
               37786592  132.908    0.000  886.059    0.000 utils.py:77(clamp_probs)
             5692472896  869.866    0.000  869.866    0.000 {method 'values' of 'collections.OrderedDict' objects}
               12989141  867.360    0.000  867.360    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               37786592  862.757    0.000  862.757    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               37786592  149.103    0.000  821.069    0.000 utils.py:11(broadcast_all)
               37786592  753.151    0.000  753.151    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
               75573184  731.950    0.000  731.950    0.000 {built-in method broadcast_tensors}
              114245397  718.909    0.000  718.909    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               37786592  701.181    0.000  701.181    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
               26545001   41.196    0.000  699.738    0.000 <__array_function__ internals>:2(prod)
                1180831   71.225    0.000  696.002    0.001 replaybuffer.py:34(save_option_critic)
               26545001   39.024    0.000  649.624    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
              227309966  644.783    0.000  644.783    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               37786592  632.043    0.000  632.043    0.000 {built-in method clamp}
               26545001   61.654    0.000  610.599    0.000 fromnumeric.py:2912(prod)
               75573184  604.949    0.000  604.949    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               38077278  573.985    0.000  573.985    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               26545001  141.657    0.000  548.946    0.000 fromnumeric.py:70(_wrapreduction)
               37786592  538.712    0.000  538.712    0.000 {built-in method bernoulli}
                 295207  405.750    0.001  531.823    0.002 replaybuffer.py:42(sample_option_critic)
               37786592  105.227    0.000  484.507    0.000 layers.py:838(isFree)
               37786592  484.301    0.000  484.301    0.000 {built-in method all}
               16531628  477.550    0.000  477.550    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               37786592  469.412    0.000  469.412    0.000 {built-in method log}
               37786592  462.744    0.000  462.744    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
               11808320  270.707    0.000  435.288    0.000 layer.py:159(update)
                1180831   72.849    0.000  385.041    0.000 optimizer.py:189(zero_grad)
              310534216  305.714    0.000  379.279    0.000 layer.py:103(isFree)
               37786592  352.010    0.000  352.010    0.000 {built-in method multinomial}
               26545001  339.347    0.000  339.347    0.000 {method 'reduce' of 'numpy.ufunc' objects}
              116607074  306.362    0.000  306.362    0.000 {method 'to' of 'torch._C._TensorBase' objects}
              113652853  303.299    0.000  303.299    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               16531628  300.063    0.000  300.063    0.000 {method 'add_' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9632922: <Attempt8_Lights2_option_critic_1> in cluster <dcc> Done

Job <Attempt8_Lights2_option_critic_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed May 12 15:36:14 2021
Job was executed on host(s) <n-62-23-24>, in queue <hpc>, as user <s183914> in cluster <dcc> at Sun May 16 23:16:53 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun May 16 23:16:53 2021
Terminated at Wed May 19 23:12:23 2021
Results reported at Wed May 19 23:12:23 2021

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

    CPU time :                                   258892.02 sec.
    Max Memory :                                 1089 MB
    Average Memory :                             1080.55 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15295.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   259038 sec.
    Turnaround time :                            632169 sec.

The output (if any) is above this job summary.

