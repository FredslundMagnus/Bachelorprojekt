
# Parameters

    Name :                      Option_Critic-0
    Main :                      option_critic_run
    Level :                     Levels.Causal2
    Failed actions chance :     0.0
    Hours :                     24.0
    Batch :                     100
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
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                3
    Counterfacts :              2
    Topn :                      5
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      33274823910 function calls (33220564581 primitive calls) in 86109.17 seconds

##    Ordered by: cumulative time
   List reduced from 438 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86109.171 86109.171 {built-in method builtins.exec}
                      1    0.265    0.265 86109.171 86109.171 <string>:1(<module>)
                      1 4904.426 4904.426 86108.907 86108.907 optionCritic.py:194(option_critic_run)
              117672100 9435.518    0.000 38326.774    0.000 optionCritic.py:91(get_action)
              117672100 2078.853    0.000 26449.005    0.000 optionCritic.py:80(predict_option_termination)
        302262698/248133530 1149.578    0.000 14016.431    0.000 module.py:715(_call_impl)
              248133530  388.629    0.000 10805.369    0.000 linear.py:92(forward)
              248133530  737.273    0.000 10274.310    0.000 functional.py:1669(linear)
              117672100 1000.532    0.000 10252.128    0.000 categorical.py:110(log_prob)
              247699771 7231.336    0.000 7231.336    0.000 {built-in method addmm}
              121047662  191.418    0.000 6352.618    0.000 optionCritic.py:77(get_Q)
              117672100 3175.514    0.000 6310.300    0.000 categorical.py:118(entropy)
              353452511 5290.103    0.000 5290.103    0.000 {method 'item' of 'torch._C._TensorBase' objects}
              117672100  385.467    0.000 4497.826    0.000 utils.py:99(__get__)
                1176721    4.503    0.000 4482.051    0.004 game.py:41(step)
              117672100  773.174    0.000 4370.656    0.000 categorical.py:103(sample)
                1176721    6.807    0.000 4278.416    0.004 layers.py:718(step)
              117672100 2051.191    0.000 3865.329    0.000 categorical.py:44(__init__)
              117672100  104.033    0.000 3799.758    0.000 categorical.py:83(logits)
              117672100  122.909    0.000 3695.726    0.000 utils.py:75(probs_to_logits)
              117672100  452.821    0.000 3607.763    0.000 bernoulli.py:86(sample)
                1176721    7.087    0.000 3395.406    0.003 tensor.py:181(backward)
                1176721    4.354    0.000 3388.319    0.003 __init__.py:68(backward)
                1176721 3359.576    0.003 3359.576    0.003 {method 'run_backward' of 'torch._C._EngineBase' objects}
              235344200 2993.336    0.000 2993.336    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                1176721   90.963    0.000 2719.655    0.002 layers.py:17(step)
              235344200  923.569    0.000 2641.003    0.000 functional.py:42(broadcast_tensors)
              117672100  179.115    0.000 2618.806    0.000 layer.py:98(move)
              117672100  443.878    0.000 2389.794    0.000 bernoulli.py:34(__init__)
              117672100 2377.719    0.000 2377.719    0.000 {built-in method multinomial}
                6766146   27.307    0.000 2292.024    0.000 optionCritic.py:70(get_state)
                6766146   57.245    0.000 2180.058    0.000 container.py:115(forward)
              117672100  324.967    0.000 2162.480    0.000 utils.py:70(clamp_probs)
              117672100 2078.097    0.000 2078.097    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
              117672100 1951.104    0.000 1951.104    0.000 {built-in method bernoulli}
              117672100 1837.513    0.000 1837.513    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
                1176721  256.650    0.000 1777.867    0.002 optionCritic.py:142(actor_loss_fn)
              118105860 1760.067    0.000 1760.067    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
              117672100 1719.384    0.000 1719.384    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
              117672100  353.545    0.000 1653.250    0.000 layers.py:735(check)
              117672100 1627.202    0.000 1627.202    0.000 {built-in method clamp}
              120319722 1602.883    0.000 1602.883    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
              474218563 1578.515    0.000 1578.515    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                1176722  155.811    0.000 1543.561    0.001 layers.py:684(update)
              117672100  241.190    0.000 1482.197    0.000 utils.py:7(broadcast_all)
               12943931   33.413    0.000 1479.183    0.000 tensor.py:576(__iter__)
               12943931 1432.874    0.000 1432.874    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
              117672100 1410.336    0.000 1410.336    0.000 {built-in method log}
              248133530 1404.112    0.000 1404.112    0.000 {method 't' of 'torch._C._TensorBase' objects}
                1176721  101.125    0.000 1339.352    0.001 replaybuffer.py:34(save_option_critic)
              235344200 1234.526    0.000 1234.526    0.000 {built-in method broadcast_tensors}
              947694171  474.813    0.000 1179.005    0.000 {built-in method builtins.any}
               13532292   21.324    0.000 1031.284    0.000 conv.py:422(forward)
               13532292   22.329    0.000 1002.631    0.000 conv.py:414(_conv_forward)
               13532292  976.549    0.000  976.549    0.000 {built-in method conv2d}
              235344200  962.517    0.000  962.517    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                1176721    6.493    0.000  876.471    0.001 grad_mode.py:23(decorate_context)
                1176721   83.748    0.000  857.759    0.001 rmsprop.py:55(step)
                7942870  769.425    0.000  769.425    0.000 {built-in method tensor}
              346978100  225.814    0.000  740.358    0.000 overrides.py:1070(has_torch_function)
                 294180  335.530    0.001  732.079    0.002 replaybuffer.py:42(sample_option_critic)
              117672100  139.856    0.000  625.871    0.000 layers.py:729(isFree)
             1006809438  613.500    0.000  613.500    0.000 module.py:765(__getattr__)
              120908082  532.346    0.000  532.346    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
                8237054  279.684    0.000  494.973    0.000 layer.py:167(NoRock_update)
              702681400  397.862    0.000  486.015    0.000 layer.py:95(isFree)
              353016400  122.866    0.000  478.453    0.000 {built-in method builtins.all}
                 294180   67.530    0.000  470.843    0.002 optionCritic.py:115(critic_loss_fn)
              117672100  386.274    0.000  386.274    0.000 {method 'expand' of 'torch._C._TensorBase' objects}
                3530167    4.698    0.000  385.903    0.000 game.py:37(board)
             1531475957  258.887    0.000  380.806    0.000 enum.py:646(__hash__)
              235344200  351.963    0.000  378.236    0.000 distribution.py:209(_extended_shape)
                 294180    5.051    0.000  374.663    0.001 replaybuffer.py:38(stacker_option_critic)
               84723864  207.003    0.000  337.802    0.000 tensor.py:933(grad)
              117672100  204.979    0.000  329.384    0.000 layers.py:207(check)
              711328844  194.764    0.000  328.875    0.000 {built-in method builtins.isinstance}
              117672100  201.189    0.000  325.657    0.000 layers.py:231(check)
                1176721   30.701    0.000  314.821    0.000 optimizer.py:167(zero_grad)
              117672100  312.611    0.000  312.611    0.000 replaybuffer.py:14(save_data)
               20298438   14.811    0.000  306.192    0.000 activation.py:713(forward)
              117672100  189.128    0.000  304.487    0.000 layers.py:219(check)
              315206629  302.513    0.000  302.513    0.000 {built-in method torch._C._get_tracing_state}
              235344200  295.115    0.000  295.115    0.000 distribution.py:24(__init__)
              942089730  239.616    0.000  293.601    0.000 overrides.py:1083(<genexpr>)
               20298438   23.626    0.000  291.381    0.000 functional.py:1292(leaky_relu)
              357981379   83.507    0.000  286.540    0.000 layers.py:690(<genexpr>)
              937906720  229.422    0.000  282.435    0.000 layers.py:700(<genexpr>)
              118919439  129.859    0.000  281.529    0.000 grad_mode.py:85(__enter__)
               20298438  265.309    0.000  265.309    0.000 {built-in method torch._C._nn.leaky_relu}
              237838878  147.651    0.000  227.865    0.000 grad_mode.py:166(__init__)
             2216033410  207.047    0.000  207.047    0.000 layer.py:91(positions)
              118919439   91.480    0.000  201.390    0.000 grad_mode.py:89(__exit__)
              117672100  131.558    0.000  196.931    0.000 grad_mode.py:124(__enter__)
              117672200  127.027    0.000  193.325    0.000 layers.py:113(isDone)
              235344222  189.570    0.000  189.570    0.000 {method 'size' of 'torch._C._TensorBase' objects}
              235344200  111.970    0.000  174.798    0.000 _VF.py:25(__getattr__)
                 433860    5.257    0.000  173.695    0.000 layers.py:740(restart)
                2647622    8.773    0.000  168.459    0.000 optionCritic.py:88(get_terminations)
              118919439  148.802    0.000  160.029    0.000 grad_mode.py:80(__init__)
             1692440529  147.271    0.000  159.639    0.000 {built-in method builtins.len}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-7>
Subject: Job 9526598: <Option_Critic_0> in cluster <dcc> Done

Job <Option_Critic_0> was submitted from host <n-62-30-2> by user <s183905> in cluster <dcc> at Thu Apr 15 17:40:21 2021
Job was executed on host(s) <n-62-20-7>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Thu Apr 15 17:40:26 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Apr 15 17:40:26 2021
Terminated at Fri Apr 16 17:35:41 2021
Results reported at Fri Apr 16 17:35:41 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=16G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 1440
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $LSB_PROJECT_NAME


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   85998.11 sec.
    Max Memory :                                 2307 MB
    Average Memory :                             2306.34 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14077.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86116 sec.
    Turnaround time :                            86120 sec.

The output (if any) is above this job summary.

