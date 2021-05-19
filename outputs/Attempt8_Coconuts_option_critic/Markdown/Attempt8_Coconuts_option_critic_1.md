[W NNPACK.cpp:80] Could not initialize NNPACK! Reason: Unsupported hardware.

# Parameters

    Name :                      Attempt8_Coconuts_option_critic-1
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
    Num :                       1
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              4315 minutes.
    Hours used :                71 hours.

# Profiling


      47222316066 function calls (45917317486 primitive calls) in 258900.92 seconds

##    Ordered by: cumulative time
   List reduced from 438 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.920 258900.920 {built-in method builtins.exec}
                      1    0.280    0.280 258900.920 258900.920 <string>:1(<module>)
                      1 3430.739 3430.739 258900.640 258900.640 optionCritic.py:195(option_critic_run)
        1729354820/429111797 10292.340    0.000 109065.073    0.000 module.py:866(_call_impl)
               46816064 9300.444    0.000 108875.906    0.002 optionCritic.py:143(actor_loss_fn)
              144471447  805.788    0.000 99365.481    0.001 optionCritic.py:70(get_state)
              144471447 2835.610    0.000 96141.508    0.001 container.py:117(forward)
                1463002    6.399    0.000 67498.830    0.046 tensor.py:195(backward)
                1463002    8.032    0.000 67492.195    0.046 __init__.py:68(backward)
                1463002 67455.516    0.046 67455.516    0.046 {method 'run_backward' of 'torch._C._EngineBase' objects}
              288942894  929.867    0.000 57649.802    0.000 conv.py:398(forward)
              288942894  396.395    0.000 56394.516    0.000 conv.py:390(_conv_forward)
              288942894 55998.121    0.000 55998.121    0.000 {built-in method conv2d}
               46816064 4081.073    0.000 24374.510    0.001 optionCritic.py:91(get_action)
              573583244 1710.234    0.000 21815.921    0.000 linear.py:93(forward)
              573583244  623.666    0.000 19498.581    0.000 functional.py:1737(linear)
              573583244 18755.766    0.000 18755.766    0.000 {built-in method torch._C._nn.linear}
                1463002   17.047    0.000 17916.368    0.012 optimizer.py:84(wrapper)
                1463002    9.119    0.000 17845.777    0.012 grad_mode.py:24(decorate_context)
                1463002   75.143    0.000 17818.932    0.012 rmsprop.py:56(step)
                1463002  125.670    0.000 17652.399    0.012 _functional.py:203(rmsprop)
               20482022 15431.468    0.001 15431.468    0.001 {method 'sqrt' of 'torch._C._TensorBase' objects}
               46816064 1230.776    0.000 13193.456    0.000 optionCritic.py:80(predict_option_termination)
               93632128 1111.051    0.000 8795.926    0.000 distribution.py:34(__init__)
              433414341  465.583    0.000 8415.617    0.000 activation.py:713(forward)
               46816064  633.469    0.000 8031.345    0.000 categorical.py:115(log_prob)
              433414341  462.352    0.000 7950.033    0.000 functional.py:1364(leaky_relu)
              433414341 7392.713    0.000 7392.713    0.000 {built-in method torch._C._nn.leaky_relu}
               46816064  916.306    0.000 7137.095    0.000 categorical.py:49(__init__)
              143826408  516.995    0.000 6792.880    0.000 optionCritic.py:77(get_Q)
                1463002    6.746    0.000 5760.259    0.004 game.py:42(step)
                1463002    9.656    0.000 5665.191    0.004 layers.py:827(step)
               93997878  474.769    0.000 5395.015    0.000 optionCritic.py:88(get_terminations)
                 365750   67.557    0.000 5014.074    0.014 optionCritic.py:116(critic_loss_fn)
               46816064  258.696    0.000 4550.784    0.000 bernoulli.py:34(__init__)
               46816064 2940.018    0.000 4458.318    0.000 constraints.py:398(check)
                1463003  139.710    0.000 3573.507    0.002 layers.py:793(update)
               46816064  511.456    0.000 3386.878    0.000 distribution.py:240(_validate_sample)
                2646751   36.372    0.000 2553.749    0.001 layers.py:849(restart)
              144471447  181.026    0.000 2395.982    0.000 activation.py:101(forward)
               46816064 1158.906    0.000 2371.480    0.000 categorical.py:123(entropy)
               46816064 2278.077    0.000 2278.077    0.000 constraints.py:249(check)
              144471447  153.715    0.000 2214.956    0.000 functional.py:1195(relu)
                2646751   15.506    0.000 2185.926    0.001 level.py:8(__init__)
               46816064 2120.284    0.000 2120.284    0.000 constraints.py:364(check)
                1463002   61.491    0.000 2077.056    0.001 layers.py:17(step)
                2646751  140.824    0.000 2041.147    0.001 levels.py:277(generate)
              144471447 2032.266    0.000 2032.266    0.000 {built-in method relu}
               46816064  150.872    0.000 2010.917    0.000 layer.py:106(move)
              140448192  223.848    0.000 1981.031    0.000 utils.py:106(__get__)
             1745447842 1932.593    0.000 1932.593    0.000 {built-in method torch._C._get_tracing_state}
              327712448 1897.167    0.000 1897.167    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               23602511  268.469    0.000 1790.685    0.000 level.py:41(notUsed)
              141179692  204.328    0.000 1764.091    0.000 tensor.py:525(__rsub__)
               46816064  278.145    0.000 1668.732    0.000 bernoulli.py:86(sample)
              140448192 1663.970    0.000 1663.970    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
              144471447  122.467    0.000 1644.024    0.000 flatten.py:39(forward)
             2247986464 1604.830    0.000 1604.952    0.000 module.py:934(__getattr__)
               46816064   79.207    0.000 1578.941    0.000 categorical.py:88(logits)
               46816064  405.264    0.000 1543.957    0.000 categorical.py:108(sample)
              141179692 1525.981    0.000 1525.981    0.000 {built-in method rsub}
              144471447 1521.557    0.000 1521.557    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              140813942 1511.056    0.000 1511.056    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
               46816064   82.803    0.000 1499.735    0.000 utils.py:82(probs_to_logits)
               46816064  245.646    0.000 1485.562    0.000 layers.py:844(check)
               93997878 1259.559    0.000 1259.559    0.000 {method 'max' of 'torch._C._TensorBase' objects}
               20482022 1258.516    0.000 1258.516    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               93632128  388.290    0.000 1255.277    0.000 functional.py:46(broadcast_tensors)
              140448192 1151.890    0.000 1151.890    0.000 {method 'all' of 'torch._C._TensorBase' objects}
             7474412900 1108.276    0.000 1118.349    0.000 {built-in method builtins.len}
               46816064  137.746    0.000  922.307    0.000 utils.py:77(clamp_probs)
             7061890727  920.048    0.000  920.048    0.000 {method 'values' of 'collections.OrderedDict' objects}
               16093022   34.472    0.000  914.313    0.000 tensor.py:575(__iter__)
               46816064  857.405    0.000  857.405    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               23602511   22.233    0.000  852.361    0.000 level.py:38(elementsIn)
               16093022  851.235    0.000  851.235    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               46816064  150.182    0.000  827.490    0.000 utils.py:11(broadcast_all)
               46816064  784.561    0.000  784.561    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
              141545442  766.781    0.000  766.781    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               93632128  762.071    0.000  762.071    0.000 {built-in method broadcast_tensors}
                1463002   74.634    0.000  730.210    0.000 replaybuffer.py:34(save_option_critic)
               46816064  730.145    0.000  730.145    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
              281627884  692.186    0.000  692.186    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               46816064  664.546    0.000  664.546    0.000 {built-in method clamp}
               15025373  311.598    0.000  656.410    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               93632128  638.254    0.000  638.254    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               49462780  635.855    0.000  635.855    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               10241021  432.877    0.000  611.213    0.000 layer.py:159(update)
                 365750  435.211    0.001  562.975    0.002 replaybuffer.py:42(sample_option_critic)
               46816064  547.553    0.000  547.553    0.000 {built-in method bernoulli}
             1862533048  372.248    0.000  535.947    0.000 enum.py:646(__hash__)
               23602511  279.941    0.000  533.665    0.000 level.py:39(<listcomp>)
               46816064  511.940    0.000  511.940    0.000 {built-in method all}
               46816064  494.625    0.000  494.625    0.000 {built-in method log}
               46816064  489.589    0.000  489.589    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
               46816064  357.725    0.000  481.913    0.000 layers.py:471(check)
               46816064  273.576    0.000  365.162    0.000 layers.py:77(check)
               46816064  364.653    0.000  364.653    0.000 {built-in method multinomial}
             1087869924  356.784    0.000  356.784    0.000 level.py:32(inverse)
                1463002   71.342    0.000  348.341    0.000 optimizer.py:189(zero_grad)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9632940: <Attempt8_Coconuts_option_critic_1> in cluster <dcc> Done

Job <Attempt8_Coconuts_option_critic_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed May 12 15:36:18 2021
Job was executed on host(s) <n-62-23-22>, in queue <hpc>, as user <s183914> in cluster <dcc> at Sun May 16 23:16:53 2021
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

    CPU time :                                   258862.00 sec.
    Max Memory :                                 863 MB
    Average Memory :                             852.83 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15521.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258978 sec.
    Turnaround time :                            632165 sec.

The output (if any) is above this job summary.

