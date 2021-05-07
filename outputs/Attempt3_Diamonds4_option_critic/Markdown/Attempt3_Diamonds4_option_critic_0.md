
# Parameters

    Name :                      Attempt3_Diamonds4_option_critic-0
    Main :                      option_critic_run
    Level :                     Levels.Causal7
    Failed actions chance :     0
    Use model :                 True
    Depth :                     3
    Model explore :             1000000
    Samples :                   5
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
    Minutes used :              4315 minutes.
    Hours used :                71 hours.

# Profiling


      39369514350 function calls (38119208291 primitive calls) in 258900.94 seconds

##    Ordered by: cumulative time
   List reduced from 429 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.943 258900.943 {built-in method builtins.exec}
                      1    0.333    0.333 258900.943 258900.943 <string>:1(<module>)
                      1 4310.072 4310.072 258900.609 258900.609 optionCritic.py:195(option_critic_run)
               44925575 8624.676    0.000 101154.117    0.002 optionCritic.py:143(actor_loss_fn)
        1659968118/409779216 9834.615    0.000 99422.704    0.000 module.py:866(_call_impl)
              138909878  733.361    0.000 91161.337    0.001 optionCritic.py:70(get_state)
              138909878 2398.409    0.000 88199.893    0.001 container.py:117(forward)
                1797023   12.369    0.000 64145.864    0.036 tensor.py:195(backward)
                1797023   17.027    0.000 64133.241    0.036 __init__.py:68(backward)
                1797023 64077.233    0.036 64077.233    0.036 {method 'run_backward' of 'torch._C._EngineBase' objects}
              277819756  897.277    0.000 53778.099    0.000 conv.py:398(forward)
              277819756  465.451    0.000 52538.643    0.000 conv.py:390(_conv_forward)
              277819756 52073.192    0.000 52073.192    0.000 {built-in method conv2d}
                1797023   38.825    0.000 38623.312    0.021 optimizer.py:84(wrapper)
                1797023   24.086    0.000 38479.426    0.021 grad_mode.py:24(decorate_context)
                1797023  109.587    0.000 38414.720    0.021 rmsprop.py:56(step)
                1797023  140.309    0.000 38179.638    0.021 _functional.py:203(rmsprop)
               25158304 34563.201    0.001 34563.201    0.001 {method 'sqrt' of 'torch._C._TensorBase' objects}
               44925575 3543.609    0.000 20968.828    0.000 optionCritic.py:91(get_action)
              548689094 1546.230    0.000 19155.749    0.000 linear.py:93(forward)
              548689094  653.495    0.000 17001.868    0.000 functional.py:1737(linear)
              548689094 16211.351    0.000 16211.351    0.000 {built-in method torch._C._nn.linear}
               44925575 1144.944    0.000 13029.433    0.000 optionCritic.py:80(predict_option_termination)
               89851150 1168.644    0.000 7705.978    0.000 distribution.py:34(__init__)
              416729634  514.559    0.000 7296.454    0.000 activation.py:713(forward)
               44925575  617.152    0.000 6996.967    0.000 categorical.py:115(log_prob)
              416729634  502.003    0.000 6781.895    0.000 functional.py:1364(leaky_relu)
              416729634 6167.566    0.000 6167.566    0.000 {built-in method torch._C._nn.leaky_relu}
               44925575  822.740    0.000 5990.509    0.000 categorical.py:49(__init__)
              135912911  434.659    0.000 5829.165    0.000 optionCritic.py:77(get_Q)
               44925575  371.074    0.000 4708.831    0.000 bernoulli.py:34(__init__)
               90030852  421.848    0.000 4364.828    0.000 optionCritic.py:88(get_terminations)
               44925575 2450.815    0.000 3611.966    0.000 constraints.py:398(check)
                1797023    9.923    0.000 3425.164    0.002 game.py:42(step)
                1797023   19.699    0.000 3313.536    0.002 layers.py:827(step)
               44925575  490.823    0.000 2767.934    0.000 distribution.py:240(_validate_sample)
               25158304 2447.925    0.000 2447.925    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                 179702   32.619    0.000 2005.566    0.011 optionCritic.py:116(critic_loss_fn)
              138909878  188.260    0.000 1972.976    0.000 activation.py:101(forward)
               44925575  951.235    0.000 1924.049    0.000 categorical.py:123(entropy)
               44925575 1910.227    0.000 1910.227    0.000 constraints.py:364(check)
              134776725  234.625    0.000 1796.084    0.000 utils.py:106(__get__)
              138909878  164.136    0.000 1784.716    0.000 functional.py:1195(relu)
               44925575  335.002    0.000 1756.089    0.000 bernoulli.py:86(sample)
               44925575 1749.971    0.000 1749.971    0.000 constraints.py:249(check)
                1797023   77.339    0.000 1728.275    0.001 layers.py:17(step)
             2152652793 1644.616    0.000 1644.619    0.000 module.py:934(__getattr__)
               44925575  128.927    0.000 1643.918    0.000 layer.py:106(move)
              138909878 1588.513    0.000 1588.513    0.000 {built-in method relu}
                1797024  166.529    0.000 1557.882    0.001 layers.py:793(update)
              314479025 1483.415    0.000 1483.415    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
             1679735371 1452.993    0.000 1452.993    0.000 {built-in method torch._C._get_tracing_state}
              135136129  177.884    0.000 1450.687    0.000 tensor.py:525(__rsub__)
              138909878  139.658    0.000 1443.570    0.000 flatten.py:39(forward)
               44925575   79.106    0.000 1381.034    0.000 categorical.py:88(logits)
               89851150  482.168    0.000 1351.962    0.000 functional.py:46(broadcast_tensors)
               44925575  352.184    0.000 1347.283    0.000 categorical.py:108(sample)
              138909878 1303.912    0.000 1303.912    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               44925575   77.886    0.000 1301.928    0.000 utils.py:82(probs_to_logits)
              134776725 1270.439    0.000 1270.439    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
              135136129 1241.579    0.000 1241.579    0.000 {built-in method rsub}
              134956427 1163.435    0.000 1163.435    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
               90030852 1109.569    0.000 1109.569    0.000 {method 'max' of 'torch._C._TensorBase' objects}
             7183089580 1080.683    0.000 1094.996    0.000 {built-in method builtins.len}
               19767253   48.553    0.000 1093.039    0.000 tensor.py:575(__iter__)
               19767253 1013.667    0.000 1013.667    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               44925575  222.026    0.000 1011.721    0.000 layers.py:844(check)
               44925575  205.646    0.000 1002.429    0.000 utils.py:11(broadcast_all)
             6778782350  938.744    0.000  938.744    0.000 {method 'values' of 'collections.OrderedDict' objects}
              134776725  911.682    0.000  911.682    0.000 {method 'all' of 'torch._C._TensorBase' objects}
               44925575  147.773    0.000  811.340    0.000 utils.py:77(clamp_probs)
               44925575  809.965    0.000  809.965    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               89851150  744.507    0.000  744.507    0.000 {built-in method broadcast_tensors}
               44925575  663.567    0.000  663.567    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
                1797023   77.332    0.000  656.640    0.000 replaybuffer.py:34(save_option_critic)
               44925575  638.570    0.000  638.570    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
              135315831  579.220    0.000  579.220    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               45702357  543.967    0.000  543.967    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                 776806   13.543    0.000  540.007    0.001 layers.py:849(restart)
               44925575  538.093    0.000  538.093    0.000 {built-in method bernoulli}
               89851150  536.469    0.000  536.469    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               44925575  531.518    0.000  531.518    0.000 {built-in method clamp}
                1797023   90.172    0.000  505.488    0.000 optimizer.py:189(zero_grad)
              269912854  484.291    0.000  484.291    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                 776806    6.373    0.000  433.802    0.001 level.py:8(__init__)
               12579168  258.633    0.000  420.433    0.000 layer.py:175(NoRock_update)
               44925575  412.702    0.000  412.702    0.000 {built-in method log}
               44925575  408.263    0.000  408.263    0.000 {built-in method all}
               25158304  407.525    0.000  407.525    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               44925575   92.507    0.000  401.543    0.000 layers.py:838(isFree)
               44925575  392.503    0.000  392.503    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
                 776806   15.007    0.000  377.873    0.000 levels.py:456(generate)
                 179702  287.436    0.002  360.296    0.002 replaybuffer.py:42(sample_option_critic)
                3730852   58.810    0.000  348.079    0.000 level.py:41(notUsed)
              591604522  222.058    0.000  327.659    0.000 {built-in method builtins.isinstance}
               25158304  323.733    0.000  323.733    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               44925575  322.848    0.000  322.848    0.000 {built-in method multinomial}
               11321248  313.193    0.000  313.193    0.000 {built-in method tensor}
              135557125  309.686    0.000  309.686    0.000 {method 'item' of 'torch._C._TensorBase' objects}
              258650565  256.666    0.000  309.035    0.000 layer.py:103(isFree)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9607852: <Attempt3_Diamonds4_option_critic_0> in cluster <dcc> Done

Job <Attempt3_Diamonds4_option_critic_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon May  3 13:31:24 2021
Job was executed on host(s) <n-62-21-97>, in queue <hpc>, as user <s183914> in cluster <dcc> at Mon May  3 13:31:25 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon May  3 13:31:25 2021
Terminated at Thu May  6 13:26:35 2021
Results reported at Thu May  6 13:26:35 2021

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

    CPU time :                                   258926.98 sec.
    Max Memory :                                 868 MB
    Average Memory :                             847.31 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15516.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258926 sec.
    Turnaround time :                            258911 sec.

The output (if any) is above this job summary.

