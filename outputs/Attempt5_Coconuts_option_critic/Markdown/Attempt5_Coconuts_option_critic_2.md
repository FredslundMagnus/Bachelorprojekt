
# Parameters

    Name :                      Attempt5_Coconuts_option_critic-2
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


      37611249777 function calls (36490580825 primitive calls) in 258901.67 seconds

##    Ordered by: cumulative time
   List reduced from 440 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258901.673 258901.673 {built-in method builtins.exec}
                      1    0.404    0.404 258901.673 258901.673 <string>:1(<module>)
                      1 4033.399 4033.399 258901.269 258901.269 optionCritic.py:195(option_critic_run)
                1256355   10.697    0.000 119232.917    0.095 tensor.py:195(backward)
                1256355   13.409    0.000 119222.028    0.095 __init__.py:68(backward)
                1256355 119178.327    0.095 119178.327    0.095 {method 'run_backward' of 'torch._C._EngineBase' objects}
               40203360 6823.064    0.000 84958.204    0.002 optionCritic.py:143(actor_loss_fn)
        1482963056/366377561 7602.224    0.000 84721.818    0.000 module.py:866(_call_impl)
              124065055  595.348    0.000 78992.339    0.001 optionCritic.py:70(get_state)
              124065055 1658.514    0.000 76519.529    0.001 container.py:117(forward)
              248130110  727.846    0.000 48524.899    0.000 conv.py:398(forward)
              248130110  377.190    0.000 47512.959    0.000 conv.py:390(_conv_forward)
              248130110 47135.769    0.000 47135.769    0.000 {built-in method conv2d}
              490442616 1276.210    0.000 15982.472    0.000 linear.py:93(forward)
               40203360 2634.514    0.000 15818.622    0.000 optionCritic.py:91(get_action)
              490442616  496.956    0.000 14175.837    0.000 functional.py:1737(linear)
              490442616 13560.656    0.000 13560.656    0.000 {built-in method torch._C._nn.linear}
               40203360  868.767    0.000 10247.154    0.000 optionCritic.py:80(predict_option_termination)
                1256355   31.402    0.000 7259.565    0.006 optimizer.py:84(wrapper)
                1256355   16.400    0.000 7144.221    0.006 grad_mode.py:24(decorate_context)
                1256355   87.458    0.000 7097.349    0.006 adam.py:55(step)
                1256355  482.955    0.000 6912.215    0.006 _functional.py:53(adam)
               80406720  922.116    0.000 6039.551    0.000 distribution.py:34(__init__)
              372195165  398.042    0.000 5447.488    0.000 activation.py:713(forward)
               40203360  440.299    0.000 5279.002    0.000 categorical.py:115(log_prob)
              372195165  395.101    0.000 5049.446    0.000 functional.py:1364(leaky_relu)
                1256355    7.506    0.000 4654.324    0.004 game.py:42(step)
              372195165 4563.140    0.000 4563.140    0.000 {built-in method torch._C._nn.leaky_relu}
                1256355   11.971    0.000 4554.204    0.004 layers.py:827(step)
               40203360  588.850    0.000 4460.253    0.000 categorical.py:49(__init__)
              121388338  296.403    0.000 4183.069    0.000 optionCritic.py:77(get_Q)
               40203360  303.333    0.000 3964.983    0.000 bernoulli.py:34(__init__)
                1256355   64.890    0.000 3344.394    0.003 layers.py:17(step)
                 314088   52.506    0.000 3342.992    0.011 optionCritic.py:116(critic_loss_fn)
               80720808  315.989    0.000 3311.930    0.000 optionCritic.py:88(get_terminations)
               40203360  217.422    0.000 3273.309    0.000 layer.py:106(move)
               40203360 1828.273    0.000 2718.152    0.000 constraints.py:398(check)
               40203360  338.794    0.000 2286.354    0.000 layers.py:844(check)
               40203360  381.628    0.000 2124.943    0.000 distribution.py:240(_validate_sample)
              124065055  172.657    0.000 1572.492    0.000 activation.py:101(forward)
               35177928 1557.743    0.000 1557.743    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               40203360 1546.306    0.000 1546.306    0.000 constraints.py:364(check)
               40203360  276.024    0.000 1495.093    0.000 bernoulli.py:86(sample)
               40203360  758.207    0.000 1463.167    0.000 categorical.py:123(entropy)
             1924093112 1400.198    0.000 1400.301    0.000 module.py:934(__getattr__)
              124065055  157.678    0.000 1399.835    0.000 functional.py:1195(relu)
               40203360 1361.933    0.000 1361.933    0.000 constraints.py:249(check)
              120610080  182.062    0.000 1337.224    0.000 utils.py:106(__get__)
               17588964 1313.168    0.000 1313.168    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              281423520 1258.159    0.000 1258.159    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              124065055  135.215    0.000 1231.827    0.000 flatten.py:39(forward)
              124065055 1219.136    0.000 1219.136    0.000 {built-in method relu}
                1256356  133.635    0.000 1191.764    0.001 layers.py:793(update)
              121238256  137.889    0.000 1157.389    0.000 tensor.py:525(__rsub__)
               80406720  385.968    0.000 1121.339    0.000 functional.py:46(broadcast_tensors)
              124065055 1096.612    0.000 1096.612    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               17588964 1095.124    0.000 1095.124    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               40203360  285.259    0.000 1037.884    0.000 categorical.py:108(sample)
               40203360   51.747    0.000 1013.481    0.000 categorical.py:88(logits)
              121238256  996.712    0.000  996.712    0.000 {built-in method rsub}
               40203360   59.726    0.000  961.734    0.000 utils.py:82(probs_to_logits)
             1496782961  957.465    0.000  957.465    0.000 {built-in method torch._C._get_tracing_state}
               13819905   33.996    0.000  955.897    0.000 tensor.py:575(__iter__)
              120924168  937.394    0.000  937.394    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
               80720808  927.469    0.000  927.469    0.000 {method 'max' of 'torch._C._TensorBase' objects}
              120610080  921.277    0.000  921.277    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
               13819905  900.555    0.000  900.555    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
             6570816894  888.847    0.000  898.589    0.000 {built-in method builtins.len}
               40203360  176.617    0.000  892.379    0.000 utils.py:11(broadcast_all)
               35177928  829.315    0.000  829.315    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               17588964  823.544    0.000  823.544    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               17588964  802.087    0.000  802.087    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
             6055917279  781.636    0.000  781.636    0.000 {method 'values' of 'collections.OrderedDict' objects}
              120610080  751.828    0.000  751.828    0.000 {method 'all' of 'torch._C._TensorBase' objects}
                 314088  540.265    0.002  678.291    0.002 replaybuffer.py:42(sample_option_critic)
               40203360  677.858    0.000  677.858    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               40203360  121.775    0.000  636.608    0.000 layers.py:838(isFree)
               80406720  598.467    0.000  598.467    0.000 {built-in method broadcast_tensors}
               40203360  112.693    0.000  569.550    0.000 utils.py:77(clamp_probs)
                1256355   61.536    0.000  537.346    0.000 replaybuffer.py:34(save_option_critic)
              375648574  417.233    0.000  514.833    0.000 layer.py:103(isFree)
               40203360  362.103    0.000  496.978    0.000 layers.py:471(check)
              121552344  482.266    0.000  482.266    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               13819916  284.928    0.000  481.295    0.000 layer.py:159(update)
               40203360  460.982    0.000  460.982    0.000 {built-in method bernoulli}
               40203360  456.857    0.000  456.857    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
               40203360  452.802    0.000  452.802    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
             1108469728  292.623    0.000  424.092    0.000 enum.py:646(__hash__)
               40353442  404.912    0.000  404.912    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
              241848336  394.332    0.000  394.332    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               80406720  387.719    0.000  387.719    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                1256355   64.643    0.000  385.701    0.000 optimizer.py:189(zero_grad)
               40203360  373.720    0.000  373.720    0.000 {built-in method clamp}
               40203360  200.262    0.000  334.930    0.000 layers.py:286(check)
               40203360  332.457    0.000  332.457    0.000 {built-in method log}
               40203360  324.984    0.000  324.984    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
              120610112   88.373    0.000  322.844    0.000 {built-in method builtins.all}
               40203360  215.129    0.000  302.531    0.000 layers.py:77(check)
               40203360  299.550    0.000  299.550    0.000 {built-in method all}
               40053279   65.813    0.000  299.364    0.000 {built-in method builtins.any}


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
Subject: Job 9618618: <Attempt5_Coconuts_option_critic_2> in cluster <dcc> Exited

Job <Attempt5_Coconuts_option_critic_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Thu May  6 02:11:28 2021
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

Exited with exit code 1.

Resource usage summary:

    CPU time :                                   258274.00 sec.
    Max Memory :                                 856 MB
    Average Memory :                             842.46 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15528.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   259024 sec.
    Turnaround time :                            507455 sec.

The output (if any) is above this job summary.

