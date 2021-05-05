
# Parameters

    Name :                      Attempt2_Lights2_option_critic-0
    Main :                      option_critic_run
    Level :                     Levels.Causal4
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


      47182893674 function calls (45726448204 primitive calls) in 258900.74 seconds

##    Ordered by: cumulative time
   List reduced from 438 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.742 258900.742 {built-in method builtins.exec}
                      1    0.334    0.334 258900.742 258900.742 <string>:1(<module>)
                      1 5604.507 5604.507 258900.408 258900.408 optionCritic.py:195(option_critic_run)
               51793925 9176.209    0.000 109918.468    0.002 optionCritic.py:143(actor_loss_fn)
        1923410495/473698532 9872.239    0.000 109597.364    0.000 module.py:866(_call_impl)
              161079107  813.452    0.000 102055.145    0.001 optionCritic.py:70(get_state)
              161079107 2134.195    0.000 98799.986    0.001 container.py:117(forward)
                2071757   16.792    0.000 76165.790    0.037 tensor.py:195(backward)
                2071757   22.108    0.000 76148.662    0.037 __init__.py:68(backward)
                2071757 76075.238    0.037 76075.238    0.037 {method 'run_backward' of 'torch._C._EngineBase' objects}
              322158214  996.522    0.000 63372.301    0.000 conv.py:398(forward)
              322158214  505.676    0.000 61989.965    0.000 conv.py:390(_conv_forward)
              322158214 61484.289    0.000 61484.289    0.000 {built-in method conv2d}
               51793925 3481.706    0.000 20575.143    0.000 optionCritic.py:91(get_action)
              634777639 1613.335    0.000 20100.192    0.000 linear.py:93(forward)
              634777639  639.394    0.000 17815.899    0.000 functional.py:1737(linear)
              634777639 17029.611    0.000 17029.611    0.000 {built-in method torch._C._nn.linear}
               51793925 1187.078    0.000 14459.193    0.000 optionCritic.py:80(predict_option_termination)
                2071757   47.066    0.000 9434.373    0.005 optimizer.py:84(wrapper)
                2071757   26.116    0.000 9256.157    0.004 grad_mode.py:24(decorate_context)
                2071757  128.834    0.000 9182.307    0.004 rmsprop.py:56(step)
                2071757  130.641    0.000 8899.241    0.004 _functional.py:203(rmsprop)
              103587850 1330.116    0.000 8158.533    0.000 distribution.py:34(__init__)
              483237321  503.625    0.000 7039.084    0.000 activation.py:713(forward)
               51793925  572.203    0.000 6840.016    0.000 categorical.py:115(log_prob)
              483237321  509.831    0.000 6535.459    0.000 functional.py:1364(leaky_relu)
              483237321 5907.794    0.000 5907.794    0.000 {built-in method torch._C._nn.leaky_relu}
               51793925  456.550    0.000 5832.958    0.000 bernoulli.py:34(__init__)
               51793925  780.351    0.000 5760.233    0.000 categorical.py:49(__init__)
              156719711  379.054    0.000 5484.544    0.000 optionCritic.py:77(get_Q)
                2071757   11.822    0.000 5056.133    0.002 game.py:42(step)
                 517939   88.985    0.000 4899.357    0.009 optionCritic.py:116(critic_loss_fn)
                2071757   22.256    0.000 4899.310    0.002 layers.py:827(step)
               29004592 4652.998    0.000 4652.998    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              104105789  391.111    0.000 4284.970    0.000 optionCritic.py:88(get_terminations)
               51793925 2355.681    0.000 3500.439    0.000 constraints.py:398(check)
                2071757   83.557    0.000 3123.076    0.002 layers.py:17(step)
               29004592 3082.062    0.000 3082.062    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               51793925  236.302    0.000 3031.698    0.000 layer.py:106(move)
               51793925  489.198    0.000 2758.319    0.000 distribution.py:240(_validate_sample)
               51793925 2145.657    0.000 2145.657    0.000 constraints.py:364(check)
               51793925  473.571    0.000 2137.733    0.000 bernoulli.py:86(sample)
              161079107  228.880    0.000 1985.154    0.000 activation.py:101(forward)
               51793925  391.755    0.000 1920.019    0.000 layers.py:844(check)
               51793925  992.726    0.000 1899.330    0.000 categorical.py:123(entropy)
             2491427469 1784.658    0.000 1784.835    0.000 module.py:934(__getattr__)
               51793925 1762.723    0.000 1762.723    0.000 constraints.py:249(check)
              161079107  181.486    0.000 1756.273    0.000 functional.py:1195(relu)
                2071758  192.527    0.000 1745.804    0.001 layers.py:793(update)
              155381775  240.086    0.000 1712.682    0.000 utils.py:106(__get__)
              362557475 1660.447    0.000 1660.447    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              161079107  164.422    0.000 1570.337    0.000 flatten.py:39(forward)
              161079107 1545.225    0.000 1545.225    0.000 {built-in method relu}
              156417653  186.905    0.000 1540.268    0.000 tensor.py:525(__rsub__)
              103587850  539.478    0.000 1522.715    0.000 functional.py:46(broadcast_tensors)
              161079107 1405.915    0.000 1405.915    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               51793925  364.207    0.000 1334.126    0.000 categorical.py:108(sample)
              156417653 1324.182    0.000 1324.182    0.000 {built-in method rsub}
               22789327   56.847    0.000 1312.249    0.000 tensor.py:575(__iter__)
               51793925  287.721    0.000 1305.147    0.000 utils.py:11(broadcast_all)
               51793925   68.753    0.000 1291.391    0.000 categorical.py:88(logits)
             1946199822 1268.755    0.000 1268.755    0.000 {built-in method torch._C._get_tracing_state}
              104105789 1248.112    0.000 1248.112    0.000 {method 'max' of 'torch._C._TensorBase' objects}
               51793925   71.740    0.000 1222.637    0.000 utils.py:82(probs_to_logits)
               22789327 1220.510    0.000 1220.510    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
              155381775 1195.920    0.000 1195.920    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
              155899714 1194.385    0.000 1194.385    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
             8469720549 1157.029    0.000 1173.555    0.000 {built-in method builtins.len}
                 517939  896.551    0.002 1125.576    0.002 replaybuffer.py:42(sample_option_critic)
              155381775 1030.896    0.000 1030.896    0.000 {method 'all' of 'torch._C._TensorBase' objects}
             7854721087 1008.153    0.000 1008.153    0.000 {method 'values' of 'collections.OrderedDict' objects}
               51793925  906.982    0.000  906.982    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
              103587850  823.282    0.000  823.282    0.000 {built-in method broadcast_tensors}
                2071757   85.336    0.000  732.086    0.000 replaybuffer.py:34(save_option_critic)
               51793925  144.308    0.000  727.126    0.000 layers.py:838(isFree)
               51793925  151.877    0.000  711.153    0.000 utils.py:77(clamp_probs)
               52095983  691.354    0.000  691.354    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
              156935592  650.252    0.000  650.252    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               51793925  633.346    0.000  633.346    0.000 {built-in method bernoulli}
                2071757  105.104    0.000  626.201    0.000 optimizer.py:189(zero_grad)
               20717580  374.142    0.000  615.709    0.000 layer.py:159(update)
               51793925  598.941    0.000  598.941    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
              420133367  475.710    0.000  582.817    0.000 layer.py:103(isFree)
               51793925  559.276    0.000  559.276    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
              155381800  145.394    0.000  525.512    0.000 {built-in method builtins.all}
              311799428  525.048    0.000  525.048    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
              103587850  502.017    0.000  502.017    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               51793925  478.578    0.000  478.578    0.000 {built-in method clamp}
               13984363  463.459    0.000  463.459    0.000 {built-in method tensor}
              685210457  267.157    0.000  461.679    0.000 {built-in method builtins.isinstance}
               51793925  439.744    0.000  439.744    0.000 {built-in method log}
               51793925  410.415    0.000  410.415    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
               29004592  406.601    0.000  406.601    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               51793925  388.221    0.000  388.221    0.000 {built-in method all}
              985386393  262.161    0.000  376.267    0.000 enum.py:646(__hash__)
               51491868   83.729    0.000  370.365    0.000 {built-in method builtins.any}
                6215275   12.586    0.000  363.030    0.000 game.py:38(board)
              161079121  362.869    0.000  362.869    0.000 {method 'to' of 'torch._C._TensorBase' objects}
               29004592  358.572    0.000  358.572    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               51793925  341.618    0.000  341.618    0.000 {built-in method multinomial}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9606113: <Attempt2_Lights2_option_critic_0> in cluster <dcc> Done

Job <Attempt2_Lights2_option_critic_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon May  3 01:33:07 2021
Job was executed on host(s) <n-62-31-1>, in queue <hpc>, as user <s183914> in cluster <dcc> at Mon May  3 01:33:08 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon May  3 01:33:08 2021
Terminated at Thu May  6 01:28:27 2021
Results reported at Thu May  6 01:28:27 2021

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

    CPU time :                                   258291.36 sec.
    Max Memory :                                 1057 MB
    Average Memory :                             1038.36 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15327.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258951 sec.
    Turnaround time :                            258920 sec.

The output (if any) is above this job summary.

