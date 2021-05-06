[W NNPACK.cpp:80] Could not initialize NNPACK! Reason: Unsupported hardware.

# Parameters

    Name :                      Attempt3_Diamonds2_option_critic-2
    Main :                      option_critic_run
    Level :                     Levels.Causal5
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


      39005804363 function calls (37752467201 primitive calls) in 258876.37 seconds

##    Ordered by: cumulative time
   List reduced from 430 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.865 258900.865 {built-in method builtins.exec}
                      1    0.328    0.328 258900.865 258900.865 <string>:1(<module>)
                      1 4268.853 4268.853 258900.537 258900.537 optionCritic.py:195(option_critic_run)
               45034475 8560.995    0.000 102258.515    0.002 optionCritic.py:143(actor_loss_fn)
        1663762207/410542852 9830.034    0.000 100571.944    0.000 module.py:866(_call_impl)
              139246595  753.045    0.000 92140.763    0.001 optionCritic.py:70(get_state)
              139246595 2396.476    0.000 89166.646    0.001 container.py:117(forward)
                1801379   12.251    0.000 64300.434    0.036 tensor.py:195(backward)
                1801379   18.556    0.000 64287.923    0.036 __init__.py:68(backward)
                1801379 64229.477    0.036 64229.477    0.036 {method 'run_backward' of 'torch._C._EngineBase' objects}
              278493190  995.211    0.000 54317.216    0.000 conv.py:398(forward)
              278493190  475.992    0.000 52961.094    0.000 conv.py:390(_conv_forward)
              278493190 52485.102    0.000 52485.102    0.000 {built-in method conv2d}
                1801379   39.367    0.000 36789.832    0.020 optimizer.py:84(wrapper)
                1801379   23.847    0.000 36643.108    0.020 grad_mode.py:24(decorate_context)
                1801379  110.723    0.000 36577.053    0.020 rmsprop.py:56(step)
                1801379  136.156    0.000 36336.895    0.020 _functional.py:203(rmsprop)
               25219288 32818.314    0.001 32818.314    0.001 {method 'sqrt' of 'torch._C._TensorBase' objects}
               45034475 3673.107    0.000 21476.881    0.000 optionCritic.py:91(get_action)
              549789447 1733.870    0.000 19412.034    0.000 linear.py:93(forward)
              549789447  659.754    0.000 17040.109    0.000 functional.py:1737(linear)
              549789447 16246.065    0.000 16246.065    0.000 {built-in method torch._C._nn.linear}
               45034475 1152.444    0.000 13179.661    0.000 optionCritic.py:80(predict_option_termination)
               90068950 1193.695    0.000 7769.051    0.000 distribution.py:34(__init__)
              417739785  535.667    0.000 7520.923    0.000 activation.py:713(forward)
               45034475  627.215    0.000 7151.380    0.000 categorical.py:115(log_prob)
              417739785  538.519    0.000 6985.256    0.000 functional.py:1364(leaky_relu)
              417739785 6334.747    0.000 6334.747    0.000 {built-in method torch._C._nn.leaky_relu}
               45034475  823.579    0.000 6027.352    0.000 categorical.py:49(__init__)
              136012695  472.081    0.000 5952.189    0.000 optionCritic.py:77(get_Q)
               45034475  355.101    0.000 4745.976    0.000 bernoulli.py:34(__init__)
               90249087  439.067    0.000 4470.881    0.000 optionCritic.py:88(get_terminations)
               45034475 2429.046    0.000 3631.009    0.000 constraints.py:398(check)
                1801379    9.991    0.000 3325.242    0.002 game.py:42(step)
                1801379   17.743    0.000 3212.382    0.002 layers.py:827(step)
               45034475  497.913    0.000 2816.735    0.000 distribution.py:240(_validate_sample)
               25219288 2330.915    0.000 2330.915    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               45034475 1006.831    0.000 2059.373    0.000 categorical.py:123(entropy)
                 180137   31.700    0.000 2012.334    0.011 optionCritic.py:116(critic_loss_fn)
              139246595  197.968    0.000 2001.741    0.000 activation.py:101(forward)
               45034475 1896.893    0.000 1896.893    0.000 constraints.py:364(check)
              135103425  248.140    0.000 1825.799    0.000 utils.py:106(__get__)
              139246595  170.393    0.000 1803.774    0.000 functional.py:1195(relu)
               45034475 1789.189    0.000 1789.189    0.000 constraints.py:249(check)
               45034475  352.018    0.000 1785.767    0.000 bernoulli.py:86(sample)
                1801379   73.573    0.000 1755.954    0.001 layers.py:17(step)
             2157181829 1733.018    0.000 1733.022    0.000 module.py:934(__getattr__)
               45034475  131.611    0.000 1675.373    0.000 layer.py:106(move)
              139246595 1603.291    0.000 1603.291    0.000 {built-in method relu}
             1683577376 1486.300    0.000 1486.300    0.000 {built-in method torch._C._get_tracing_state}
              135463699  200.835    0.000 1470.431    0.000 tensor.py:525(__rsub__)
              315241325 1469.567    0.000 1469.567    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              139246595  147.897    0.000 1455.692    0.000 flatten.py:39(forward)
                1801380  164.013    0.000 1430.961    0.001 layers.py:793(update)
               45034475   80.390    0.000 1399.370    0.000 categorical.py:88(logits)
               90068950  499.520    0.000 1385.528    0.000 functional.py:46(broadcast_tensors)
               45034475  358.389    0.000 1365.731    0.000 categorical.py:108(sample)
               45034475   80.486    0.000 1318.980    0.000 utils.py:82(probs_to_logits)
              135103425 1315.813    0.000 1315.813    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
              139246595 1307.795    0.000 1307.795    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              135463699 1239.031    0.000 1239.031    0.000 {built-in method rsub}
              135283562 1172.430    0.000 1172.430    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
               90249087 1125.227    0.000 1125.227    0.000 {method 'max' of 'torch._C._TensorBase' objects}
               19815169   49.461    0.000 1107.288    0.000 tensor.py:575(__iter__)
             7199080205 1093.588    0.000 1107.226    0.000 {built-in method builtins.len}
               45034475  231.086    0.000 1063.700    0.000 layers.py:844(check)
               45034475  206.055    0.000 1029.925    0.000 utils.py:11(broadcast_all)
               19815169 1025.543    0.000 1025.543    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
              135103425  945.397    0.000  945.397    0.000 {method 'all' of 'torch._C._TensorBase' objects}
             6794295423  920.916    0.000  920.916    0.000 {method 'values' of 'collections.OrderedDict' objects}
               45034475  146.264    0.000  823.861    0.000 utils.py:77(clamp_probs)
               45034475  810.456    0.000  810.456    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               90068950  751.085    0.000  751.085    0.000 {built-in method broadcast_tensors}
               45034475  677.597    0.000  677.597    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
               45034475  677.289    0.000  677.289    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
                1801379   75.698    0.000  645.105    0.000 replaybuffer.py:34(save_option_critic)
              135643836  579.460    0.000  579.460    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               45034475  579.026    0.000  579.026    0.000 {built-in method clamp}
               45583471  544.574    0.000  544.574    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               45034475  543.102    0.000  543.102    0.000 {built-in method bernoulli}
               90068950  540.916    0.000  540.916    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                1801379   94.608    0.000  518.797    0.000 optimizer.py:189(zero_grad)
              270567124  482.578    0.000  482.578    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               25219288  426.722    0.000  426.722    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               45034475  415.081    0.000  415.081    0.000 {built-in method all}
               45034475  414.633    0.000  414.633    0.000 {built-in method log}
               45034475  405.728    0.000  405.728    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
               12609660  237.783    0.000  393.409    0.000 layer.py:175(NoRock_update)
                 549021    9.848    0.000  382.292    0.001 layers.py:849(restart)
               45034475   85.187    0.000  377.777    0.000 layers.py:838(isFree)
                 180137  289.245    0.002  362.569    0.002 replaybuffer.py:42(sample_option_critic)
              135103450  102.638    0.000  348.627    0.000 {built-in method builtins.all}
               45034475  331.960    0.000  331.960    0.000 {built-in method multinomial}
              593038647  224.623    0.000  329.129    0.000 {built-in method builtins.isinstance}
              132365036  326.397    0.000  326.397    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               25219288  314.664    0.000  314.664    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               25219288  310.124    0.000  310.124    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               11348689  309.920    0.000  309.920    0.000 {built-in method tensor}
                 549021    4.901    0.000  308.730    0.001 level.py:8(__init__)
              139246609  295.991    0.000  295.991    0.000 {method 'to' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9607848: <Attempt3_Diamonds2_option_critic_2> in cluster <dcc> Done

Job <Attempt3_Diamonds2_option_critic_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon May  3 13:31:23 2021
Job was executed on host(s) <n-62-23-23>, in queue <hpc>, as user <s183914> in cluster <dcc> at Mon May  3 13:31:24 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon May  3 13:31:24 2021
Terminated at Thu May  6 13:26:32 2021
Results reported at Thu May  6 13:26:32 2021

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

    CPU time :                                   258181.81 sec.
    Max Memory :                                 1024 MB
    Average Memory :                             1008.25 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15360.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258942 sec.
    Turnaround time :                            258909 sec.

The output (if any) is above this job summary.

