[W NNPACK.cpp:80] Could not initialize NNPACK! Reason: Unsupported hardware.

# Parameters

    Name :                      Attempt7_Diamonds1_option_critic-0
    Main :                      option_critic_run
    Level :                     Levels.Causal2
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


      40529083633 function calls (39283638658 primitive calls) in 258900.99 seconds

##    Ordered by: cumulative time
   List reduced from 426 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.992 258900.992 {built-in method builtins.exec}
                      1    0.277    0.277 258900.992 258900.992 <string>:1(<module>)
                      1 3555.063 3555.063 258900.715 258900.715 optionCritic.py:195(option_critic_run)
        1649562013/408655495 10522.154    0.000 110542.409    0.000 module.py:866(_call_impl)
               44679616 9373.530    0.000 110405.695    0.002 optionCritic.py:143(actor_loss_fn)
              137878502  805.883    0.000 100809.720    0.001 optionCritic.py:70(get_state)
              137878502 2829.067    0.000 97509.478    0.001 container.py:117(forward)
                1396238    7.360    0.000 68267.571    0.049 tensor.py:195(backward)
                1396238    8.699    0.000 68259.959    0.049 __init__.py:68(backward)
                1396238 68220.246    0.049 68220.246    0.049 {method 'run_backward' of 'torch._C._EngineBase' objects}
              275757004 1007.934    0.000 58224.113    0.000 conv.py:398(forward)
              275757004  419.714    0.000 56883.826    0.000 conv.py:390(_conv_forward)
              275757004 56464.111    0.000 56464.111    0.000 {built-in method conv2d}
               44679616 4127.781    0.000 24693.128    0.001 optionCritic.py:91(get_action)
              546533997 1730.707    0.000 22127.179    0.000 linear.py:93(forward)
              546533997  637.815    0.000 19764.921    0.000 functional.py:1737(linear)
              546533997 18994.356    0.000 18994.356    0.000 {built-in method torch._C._nn.linear}
                1396238   19.397    0.000 17066.410    0.012 optimizer.py:84(wrapper)
                1396238   10.312    0.000 16984.269    0.012 grad_mode.py:24(decorate_context)
                1396238   77.687    0.000 16954.105    0.012 rmsprop.py:56(step)
                1396238  131.237    0.000 16785.268    0.012 _functional.py:203(rmsprop)
               19547326 14569.566    0.001 14569.566    0.001 {method 'sqrt' of 'torch._C._TensorBase' objects}
               44679616 1270.371    0.000 13491.401    0.000 optionCritic.py:80(predict_option_termination)
               89359232 1126.680    0.000 8917.308    0.000 distribution.py:34(__init__)
              413635506  479.792    0.000 8677.617    0.000 activation.py:713(forward)
              413635506  562.610    0.000 8197.825    0.000 functional.py:1364(leaky_relu)
               44679616  659.694    0.000 8124.142    0.000 categorical.py:115(log_prob)
              413635506 7542.749    0.000 7542.749    0.000 {built-in method torch._C._nn.leaky_relu}
               44679616  931.989    0.000 7242.312    0.000 categorical.py:49(__init__)
              136389086  500.105    0.000 6802.833    0.000 optionCritic.py:77(get_Q)
               89708291  490.695    0.000 5474.615    0.000 optionCritic.py:88(get_terminations)
                 349059   70.413    0.000 5031.915    0.014 optionCritic.py:116(critic_loss_fn)
               44679616  273.096    0.000 4658.165    0.000 bernoulli.py:34(__init__)
               44679616 2973.968    0.000 4513.932    0.000 constraints.py:398(check)
               44679616  504.416    0.000 3405.813    0.000 distribution.py:240(_validate_sample)
                1396238    7.813    0.000 3378.938    0.002 game.py:42(step)
                1396238   11.063    0.000 3280.355    0.002 layers.py:827(step)
              137878502  177.909    0.000 2462.228    0.000 activation.py:101(forward)
               44679616 1159.187    0.000 2403.688    0.000 categorical.py:123(entropy)
               44679616 2292.332    0.000 2292.332    0.000 constraints.py:249(check)
              137878502  161.233    0.000 2284.320    0.000 functional.py:1195(relu)
               44679616 2136.923    0.000 2136.923    0.000 constraints.py:364(check)
              137878502 2093.576    0.000 2093.576    0.000 {built-in method relu}
              134038848  217.280    0.000 1981.469    0.000 utils.py:106(__get__)
              312757312 1935.107    0.000 1935.107    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
             1664920631 1928.779    0.000 1928.779    0.000 {built-in method torch._C._get_tracing_state}
                1396239  146.146    0.000 1804.499    0.001 layers.py:793(update)
              134736966  185.947    0.000 1761.293    0.000 tensor.py:525(__rsub__)
               44679616  305.058    0.000 1745.976    0.000 bernoulli.py:86(sample)
              134038848 1703.889    0.000 1703.889    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
              137878502  119.551    0.000 1691.660    0.000 flatten.py:39(forward)
             2142778308 1648.068    0.000 1648.193    0.000 module.py:934(__getattr__)
               44679616   77.152    0.000 1590.826    0.000 categorical.py:88(logits)
              137878502 1572.109    0.000 1572.109    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              134387907 1549.209    0.000 1549.209    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
               44679616  395.700    0.000 1543.081    0.000 categorical.py:108(sample)
              134736966 1542.201    0.000 1542.201    0.000 {built-in method rsub}
               44679616   79.939    0.000 1513.674    0.000 utils.py:82(probs_to_logits)
                1396238   61.801    0.000 1459.095    0.001 layers.py:17(step)
               44679616  108.265    0.000 1392.654    0.000 layer.py:106(move)
               89359232  417.559    0.000 1317.677    0.000 functional.py:46(broadcast_tensors)
               89708291 1268.149    0.000 1268.149    0.000 {method 'max' of 'torch._C._TensorBase' objects}
               19547326 1218.391    0.000 1218.391    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              134038848 1183.602    0.000 1183.602    0.000 {method 'all' of 'torch._C._TensorBase' objects}
             7132455884 1088.417    0.000 1098.805    0.000 {built-in method builtins.len}
                1652153   25.119    0.000  973.428    0.001 layers.py:849(restart)
               15358618   35.993    0.000  942.134    0.000 tensor.py:575(__iter__)
               44679616  141.926    0.000  935.970    0.000 utils.py:77(clamp_probs)
             6736126554  928.867    0.000  928.867    0.000 {method 'values' of 'collections.OrderedDict' objects}
               44679616  196.979    0.000  887.380    0.000 layers.py:844(check)
               44679616  882.214    0.000  882.214    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               15358618  877.309    0.000  877.309    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               44679616  160.669    0.000  862.297    0.000 utils.py:11(broadcast_all)
               44679616  794.044    0.000  794.044    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
               89359232  791.897    0.000  791.897    0.000 {built-in method broadcast_tensors}
                1652153   11.316    0.000  790.899    0.000 level.py:8(__init__)
              135086025  779.270    0.000  779.270    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               16237821  354.526    0.000  741.827    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                1396238   73.270    0.000  729.317    0.001 replaybuffer.py:34(save_option_critic)
               44679616  729.099    0.000  729.099    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
                1652153   27.048    0.000  690.110    0.000 levels.py:151(generate)
              268775814  682.808    0.000  682.808    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               44679616  680.459    0.000  680.459    0.000 {built-in method clamp}
               46331736  646.922    0.000  646.922    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               89359232  645.572    0.000  645.572    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                7929044  100.928    0.000  635.683    0.000 level.py:41(notUsed)
               44679616  568.574    0.000  568.574    0.000 {built-in method bernoulli}
                 349059  431.205    0.001  562.726    0.002 replaybuffer.py:42(sample_option_critic)
               44679616  524.880    0.000  524.880    0.000 {built-in method all}
               44679616  497.766    0.000  497.766    0.000 {built-in method log}
               44679616  494.044    0.000  494.044    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
               16237821   23.346    0.000  387.301    0.000 <__array_function__ internals>:2(prod)
               44679616  365.336    0.000  365.336    0.000 {built-in method multinomial}
               16237821   21.812    0.000  359.014    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
                1396238   74.244    0.000  356.847    0.000 optimizer.py:189(zero_grad)
                9773673  216.578    0.000  350.496    0.000 layer.py:175(NoRock_update)
               16237821   32.741    0.000  337.202    0.000 fromnumeric.py:2912(prod)
              135693791  335.597    0.000  335.597    0.000 {method 'item' of 'torch._C._TensorBase' objects}
              137878516  329.195    0.000  329.195    0.000 {method 'to' of 'torch._C._TensorBase' objects}
               44679616  325.600    0.000  325.600    0.000 {method 'expand' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9632737: <Attempt7_Diamonds1_option_critic_0> in cluster <dcc> Done

Job <Attempt7_Diamonds1_option_critic_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed May 12 14:11:11 2021
Job was executed on host(s) <n-62-23-29>, in queue <hpc>, as user <s183914> in cluster <dcc> at Sun May 16 23:16:53 2021
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

    CPU time :                                   258888.47 sec.
    Max Memory :                                 862 MB
    Average Memory :                             849.65 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15522.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   259038 sec.
    Turnaround time :                            637272 sec.

The output (if any) is above this job summary.

