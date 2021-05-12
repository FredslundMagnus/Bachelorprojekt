
# Parameters

    Name :                      Attempt6_Coconuts_option_critic-0
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
    Num :                       0
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              4315 minutes.
    Hours used :                71 hours.

# Profiling


      34802712186 function calls (33853965950 primitive calls) in 258900.74 seconds

##    Ordered by: cumulative time
   List reduced from 439 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.739 258900.739 {built-in method builtins.exec}
                      1    0.314    0.314 258900.739 258900.739 <string>:1(<module>)
                      1 3360.254 3360.254 258900.425 258900.425 optionCritic.py:195(option_critic_run)
                1063616    8.007    0.000 147845.894    0.139 tensor.py:195(backward)
                1063616   10.850    0.000 147837.742    0.139 __init__.py:68(backward)
                1063616 147805.794    0.139 147805.794    0.139 {method 'run_backward' of 'torch._C._EngineBase' objects}
        1257369758/312081029 5842.113    0.000 66452.777    0.000 module.py:866(_call_impl)
               34035712 5020.435    0.000 66012.769    0.002 optionCritic.py:143(actor_loss_fn)
              105032081  494.626    0.000 61855.077    0.001 optionCritic.py:70(get_state)
              105032081 1373.762    0.000 59902.920    0.001 container.py:117(forward)
              210064162  545.287    0.000 36010.295    0.000 conv.py:398(forward)
              210064162  297.931    0.000 35243.152    0.000 conv.py:390(_conv_forward)
              210064162 34945.221    0.000 34945.221    0.000 {built-in method conv2d}
              417113110  961.969    0.000 14791.634    0.000 linear.py:93(forward)
              417113110  392.281    0.000 13423.429    0.000 functional.py:1737(linear)
              417113110 12938.442    0.000 12938.442    0.000 {built-in method torch._C._nn.linear}
               34035712 1963.542    0.000 11643.059    0.000 optionCritic.py:91(get_action)
               34035712  717.085    0.000 8409.322    0.000 optionCritic.py:80(predict_option_termination)
                1063616   22.121    0.000 6922.096    0.007 optimizer.py:84(wrapper)
                1063616   12.614    0.000 6839.911    0.006 grad_mode.py:24(decorate_context)
                1063616   62.110    0.000 6804.335    0.006 adam.py:55(step)
                1063616  372.932    0.000 6673.749    0.006 _functional.py:53(adam)
               68071424  732.592    0.000 4611.783    0.000 distribution.py:34(__init__)
                1063616    5.975    0.000 4315.023    0.004 game.py:42(step)
                1063616    8.963    0.000 4236.496    0.004 layers.py:827(step)
              315096243  309.713    0.000 4186.404    0.000 activation.py:713(forward)
              315096243  321.537    0.000 3876.691    0.000 functional.py:1364(leaky_relu)
               34035712  326.085    0.000 3862.117    0.000 categorical.py:115(log_prob)
              315096243 3490.389    0.000 3490.389    0.000 {built-in method torch._C._nn.leaky_relu}
              104675908  241.138    0.000 3422.245    0.000 optionCritic.py:77(get_Q)
               34035712  258.327    0.000 3286.161    0.000 bernoulli.py:34(__init__)
               34035712  441.585    0.000 3265.594    0.000 categorical.py:49(__init__)
                 265904   42.789    0.000 2697.030    0.010 optionCritic.py:116(critic_loss_fn)
                1063617   98.062    0.000 2691.517    0.003 layers.py:793(update)
               68337328  241.064    0.000 2611.464    0.000 optionCritic.py:88(get_terminations)
               34035712 1332.144    0.000 1985.607    0.000 constraints.py:398(check)
                2036995   27.550    0.000 1877.687    0.001 layers.py:849(restart)
                2036995   12.321    0.000 1603.174    0.001 level.py:8(__init__)
               34035712  270.408    0.000 1553.867    0.000 distribution.py:240(_validate_sample)
                1063616   47.893    0.000 1531.441    0.001 layers.py:17(step)
                2036995  101.266    0.000 1485.161    0.001 levels.py:277(generate)
               34035712  126.715    0.000 1479.350    0.000 layer.py:106(move)
               29781236 1471.417    0.000 1471.417    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               14890618 1324.779    0.000 1324.779    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               18165273  212.820    0.000 1296.632    0.000 level.py:41(notUsed)
               34035712  245.973    0.000 1270.997    0.000 bernoulli.py:86(sample)
               34035712 1227.660    0.000 1227.660    0.000 constraints.py:364(check)
              105032081  130.740    0.000 1218.268    0.000 activation.py:101(forward)
               14890618 1125.372    0.000 1125.372    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              105032081  119.801    0.000 1087.529    0.000 functional.py:1195(relu)
             1634645338 1081.433    0.000 1081.509    0.000 module.py:934(__getattr__)
               34035712  556.991    0.000 1066.756    0.000 categorical.py:123(entropy)
               34035712  174.748    0.000 1066.492    0.000 layers.py:844(check)
               34035712 1008.406    0.000 1008.406    0.000 constraints.py:249(check)
              238249984  987.355    0.000  987.355    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              102107136  130.376    0.000  965.101    0.000 utils.py:106(__get__)
              105032081  103.367    0.000  951.068    0.000 flatten.py:39(forward)
              105032081  949.878    0.000  949.878    0.000 {built-in method relu}
              102638944  118.118    0.000  933.621    0.000 tensor.py:525(__rsub__)
               68071424  314.369    0.000  886.443    0.000 functional.py:46(broadcast_tensors)
              105032081  847.701    0.000  847.701    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               14890618  813.213    0.000  813.213    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              102638944  797.758    0.000  797.758    0.000 {built-in method rsub}
               29781236  785.229    0.000  785.229    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               34035712  216.452    0.000  784.874    0.000 categorical.py:108(sample)
               14890618  774.588    0.000  774.588    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               34035712  165.846    0.000  761.418    0.000 utils.py:11(broadcast_all)
               11699776   26.962    0.000  750.747    0.000 tensor.py:575(__iter__)
               68337328  749.472    0.000  749.472    0.000 {method 'max' of 'torch._C._TensorBase' objects}
             1269069534  732.646    0.000  732.646    0.000 {built-in method torch._C._get_tracing_state}
               34035712   38.848    0.000  731.688    0.000 categorical.py:88(logits)
              102373040  731.096    0.000  731.096    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
               11699776  707.232    0.000  707.232    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               34035712   41.829    0.000  692.840    0.000 utils.py:82(probs_to_logits)
             5436495335  682.381    0.000  690.255    0.000 {built-in method builtins.len}
              102107136  676.005    0.000  676.005    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
               18165273   18.062    0.000  625.873    0.000 level.py:38(elementsIn)
             5134511113  598.973    0.000  598.973    0.000 {method 'values' of 'collections.OrderedDict' objects}
              102107136  574.153    0.000  574.153    0.000 {method 'all' of 'torch._C._TensorBase' objects}
               34035712  506.965    0.000  506.965    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
                 265904  412.289    0.002  506.859    0.002 replaybuffer.py:42(sample_option_critic)
               68071424  476.651    0.000  476.651    0.000 {built-in method broadcast_tensors}
                7445319  311.954    0.000  435.114    0.000 layer.py:159(update)
             1423054223  285.842    0.000  418.836    0.000 enum.py:646(__hash__)
                1063616   49.812    0.000  418.472    0.000 replaybuffer.py:34(save_option_critic)
               18165273  204.526    0.000  408.053    0.000 level.py:39(<listcomp>)
               34035712   82.949    0.000  407.722    0.000 utils.py:77(clamp_probs)
               34035712  380.060    0.000  380.060    0.000 {built-in method bernoulli}
              102904848  369.786    0.000  369.786    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               36072676  341.067    0.000  341.067    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               34035712  326.354    0.000  326.354    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
               34035712  324.772    0.000  324.772    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
              204746080  308.099    0.000  308.099    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               34035712  208.545    0.000  291.699    0.000 layers.py:471(check)
               68071424  290.276    0.000  290.276    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                1063616   48.319    0.000  279.978    0.000 optimizer.py:189(zero_grad)
               34035712  269.747    0.000  269.747    0.000 {built-in method clamp}
              837265989  269.364    0.000  269.364    0.000 level.py:32(inverse)
               34035712  198.685    0.000  266.433    0.000 layers.py:77(check)
               34035712  243.290    0.000  243.290    0.000 {built-in method log}


Traceback (most recent call last):
  File "main.py", line 268, in <module>
    run(Defaults)
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/auxillaries.py", line 133, in run
    (serverRun if isServer else Defaults.main).__call__(getvals(Defaults))
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils/server.py", line 37, in serverRun
    profilingStats()
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils/debug.py", line 62, in profilingStats
    os.remove('stats')
FileNotFoundError: [Errno 2] No such file or directory: 'stats'

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9624168: <Attempt6_Coconuts_option_critic_0> in cluster <dcc> Exited

Job <Attempt6_Coconuts_option_critic_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun May  9 01:22:29 2021
Job was executed on host(s) <n-62-11-61>, in queue <hpc>, as user <s183914> in cluster <dcc> at Sun May  9 01:22:29 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun May  9 01:22:29 2021
Terminated at Wed May 12 01:17:35 2021
Results reported at Wed May 12 01:17:35 2021

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

Exited with exit code 1.

Resource usage summary:

    CPU time :                                   258285.09 sec.
    Max Memory :                                 869 MB
    Average Memory :                             854.86 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15515.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258956 sec.
    Turnaround time :                            258906 sec.

The output (if any) is above this job summary.

