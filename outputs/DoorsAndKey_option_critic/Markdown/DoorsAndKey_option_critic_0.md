[W NNPACK.cpp:80] Could not initialize NNPACK! Reason: Unsupported hardware.

# Parameters

    Name :                      DoorsAndKey_option_critic-0
    Main :                      option_critic_run
    Level :                     Levels.Causal1
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


      32033992132 function calls (30976547070 primitive calls) in 258900.40 seconds

##    Ordered by: cumulative time
   List reduced from 429 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.404 258900.404 {built-in method builtins.exec}
                      1    0.292    0.292 258900.404 258900.404 <string>:1(<module>)
                      1 3853.280 3853.280 258900.112 258900.112 optionCritic.py:195(option_critic_run)
        1396751511/344195256 10185.415    0.000 105776.721    0.000 module.py:866(_call_impl)
               37604725 9905.964    0.000 104874.129    0.003 optionCritic.py:143(actor_loss_fn)
              116950695  738.314    0.000 96631.114    0.001 optionCritic.py:70(get_state)
              116950695 2757.537    0.000 93572.627    0.001 container.py:117(forward)
                1504189   12.370    0.000 80959.507    0.054 tensor.py:195(backward)
                1504189   14.535    0.000 80946.867    0.054 __init__.py:68(backward)
                1504189 80892.627    0.054 80892.627    0.054 {method 'run_backward' of 'torch._C._EngineBase' objects}
              233901390  886.200    0.000 55679.615    0.000 conv.py:398(forward)
              233901390  383.092    0.000 54459.056    0.000 conv.py:390(_conv_forward)
              233901390 54075.964    0.000 54075.964    0.000 {built-in method conv2d}
               37604725 3911.748    0.000 23120.585    0.001 optionCritic.py:91(get_action)
              461145951 1560.408    0.000 21528.121    0.000 linear.py:93(forward)
              461145951  604.372    0.000 19375.927    0.000 functional.py:1737(linear)
              461145951 18638.888    0.000 18638.888    0.000 {built-in method torch._C._nn.linear}
               37604725 1182.687    0.000 12770.406    0.000 optionCritic.py:80(predict_option_termination)
                1504189   32.497    0.000 11689.335    0.008 optimizer.py:84(wrapper)
                1504189   16.861    0.000 11559.696    0.008 grad_mode.py:24(decorate_context)
                1504189  103.168    0.000 11509.277    0.008 rmsprop.py:56(step)
                1504189  157.628    0.000 11293.354    0.008 _functional.py:203(rmsprop)
               21058640 8936.151    0.000 8936.151    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               75209450 1084.242    0.000 8432.945    0.000 distribution.py:34(__init__)
              350852085  404.329    0.000 7959.852    0.000 activation.py:713(forward)
               37604725  611.843    0.000 7575.234    0.000 categorical.py:115(log_prob)
              350852085  424.253    0.000 7555.523    0.000 functional.py:1364(leaky_relu)
              350852085 7034.614    0.000 7034.614    0.000 {built-in method torch._C._nn.leaky_relu}
               37604725  873.843    0.000 6822.672    0.000 categorical.py:49(__init__)
              114054339  445.116    0.000 6322.572    0.000 optionCritic.py:77(get_Q)
                 376047   84.415    0.000 5944.295    0.016 optionCritic.py:116(critic_loss_fn)
               75585497  443.994    0.000 5125.418    0.000 optionCritic.py:88(get_terminations)
               37604725  275.848    0.000 4495.838    0.000 bernoulli.py:34(__init__)
               37604725 2844.668    0.000 4271.665    0.000 constraints.py:398(check)
               37604725  468.928    0.000 3193.989    0.000 distribution.py:240(_validate_sample)
                1504189    8.265    0.000 2331.415    0.002 game.py:41(step)
              116950695  157.758    0.000 2286.972    0.000 activation.py:101(forward)
               37604725 1082.295    0.000 2231.694    0.000 categorical.py:123(entropy)
                1504189   13.764    0.000 2225.153    0.001 layers.py:718(step)
               37604725 2158.382    0.000 2158.382    0.000 constraints.py:249(check)
              116950695  141.413    0.000 2129.214    0.000 functional.py:1195(relu)
               37604725 2011.295    0.000 2011.295    0.000 constraints.py:364(check)
              116950695 1957.277    0.000 1957.277    0.000 {built-in method relu}
              112814175  213.576    0.000 1843.443    0.000 utils.py:106(__get__)
              263233075 1791.411    0.000 1791.411    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
             1413297590 1789.397    0.000 1789.397    0.000 {built-in method torch._C._get_tracing_state}
               37604725  296.299    0.000 1701.320    0.000 bernoulli.py:86(sample)
              113566269  183.147    0.000 1664.956    0.000 tensor.py:525(__rsub__)
              116950695  113.154    0.000 1587.983    0.000 flatten.py:39(forward)
              112814175 1580.639    0.000 1580.639    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
             1809694981 1543.629    0.000 1543.781    0.000 module.py:934(__getattr__)
              116950695 1474.829    0.000 1474.829    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               37604725   71.424    0.000 1467.090    0.000 categorical.py:88(logits)
              113190222 1449.435    0.000 1449.435    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
              113566269 1448.949    0.000 1448.949    0.000 {built-in method rsub}
               37604725  369.912    0.000 1445.039    0.000 categorical.py:108(sample)
               37604725   76.296    0.000 1395.666    0.000 utils.py:82(probs_to_logits)
               75209450  403.083    0.000 1247.951    0.000 functional.py:46(broadcast_tensors)
               75585497 1193.919    0.000 1193.919    0.000 {method 'max' of 'torch._C._TensorBase' objects}
                1504190  146.778    0.000 1112.283    0.001 layers.py:684(update)
              112814175 1095.912    0.000 1095.912    0.000 {method 'all' of 'torch._C._TensorBase' objects}
                1504189   62.952    0.000 1093.326    0.001 layers.py:17(step)
             6002491152 1060.164    0.000 1073.117    0.000 {built-in method builtins.len}
               37604725  109.232    0.000 1025.103    0.000 layer.py:98(move)
               16546079   45.010    0.000 1024.794    0.000 tensor.py:575(__iter__)
               21058640  962.398    0.000  962.398    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               16546079  944.768    0.000  944.768    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
             5703956739  884.466    0.000  884.466    0.000 {method 'values' of 'collections.OrderedDict' objects}
               37604725  166.832    0.000  866.370    0.000 utils.py:11(broadcast_all)
               37604725  134.263    0.000  850.464    0.000 utils.py:77(clamp_probs)
               37604725  811.812    0.000  811.812    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               75209450  738.101    0.000  738.101    0.000 {built-in method broadcast_tensors}
              113942316  720.219    0.000  720.219    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               37604725  716.201    0.000  716.201    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
                1504189   76.028    0.000  715.599    0.000 replaybuffer.py:34(save_option_critic)
               37604725  688.267    0.000  688.267    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
                 376047  522.749    0.001  680.685    0.002 replaybuffer.py:42(sample_option_critic)
               12752888  324.109    0.000  674.338    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
              226380444  635.132    0.000  635.132    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               37604725  629.423    0.000  629.423    0.000 {built-in method clamp}
               75209450  606.542    0.000  606.542    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               38092795  575.164    0.000  575.164    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               37604725  542.605    0.000  542.605    0.000 {built-in method bernoulli}
               37604725  157.742    0.000  532.292    0.000 layers.py:735(check)
               37604725  472.294    0.000  472.294    0.000 {built-in method all}
                1504189   91.279    0.000  471.003    0.000 optimizer.py:189(zero_grad)
               37604725  468.906    0.000  468.906    0.000 {built-in method log}
               37604725  468.310    0.000  468.310    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
               21058640  452.445    0.000  452.445    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               21058640  402.182    0.000  402.182    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               21058640  382.550    0.000  382.550    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               12752888   20.542    0.000  350.229    0.000 <__array_function__ internals>:2(prod)
               37604725  342.823    0.000  342.823    0.000 {built-in method multinomial}
               12752888   19.874    0.000  325.504    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
               10153279  313.823    0.000  313.823    0.000 {built-in method tensor}
              112814200   81.716    0.000  310.280    0.000 {built-in method builtins.all}
               12752888   32.083    0.000  305.630    0.000 fromnumeric.py:2912(prod)
              113305277  303.038    0.000  303.038    0.000 {method 'item' of 'torch._C._TensorBase' objects}
              116950709  301.263    0.000  301.263    0.000 {method 'to' of 'torch._C._TensorBase' objects}
               37604725   65.079    0.000  300.152    0.000 layers.py:729(isFree)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9601887: <DoorsAndKey_option_critic_0> in cluster <dcc> Done

Job <DoorsAndKey_option_critic_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Thu Apr 29 21:41:25 2021
Job was executed on host(s) <n-62-23-22>, in queue <hpc>, as user <s183914> in cluster <dcc> at Thu Apr 29 21:41:27 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Apr 29 21:41:27 2021
Terminated at Sun May  2 21:36:30 2021
Results reported at Sun May  2 21:36:30 2021

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

    CPU time :                                   258893.80 sec.
    Max Memory :                                 783 MB
    Average Memory :                             767.93 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15601.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258966 sec.
    Turnaround time :                            258905 sec.

The output (if any) is above this job summary.

