[W NNPACK.cpp:80] Could not initialize NNPACK! Reason: Unsupported hardware.

# Parameters

    Name :                      Attempt3_Diamonds2_option_critic-0
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


      35080899655 function calls (34018719390 primitive calls) in 258900.96 seconds

##    Ordered by: cumulative time
   List reduced from 430 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.961 258900.961 {built-in method builtins.exec}
                      1    0.368    0.368 258900.961 258900.961 <string>:1(<module>)
                      1 3636.412 3636.412 258900.593 258900.593 optionCritic.py:195(option_critic_run)
        1410427237/348346579 10270.134    0.000 122451.416    0.000 module.py:866(_call_impl)
               38165900 9705.819    0.000 120027.475    0.003 optionCritic.py:143(actor_loss_fn)
              118008962  781.553    0.000 113317.283    0.001 optionCritic.py:70(get_state)
              118008962 2794.651    0.000 110222.666    0.001 container.py:117(forward)
              236017924  913.318    0.000 72846.560    0.000 conv.py:398(forward)
              236017924  377.406    0.000 71587.233    0.000 conv.py:390(_conv_forward)
                1526636   11.083    0.000 71398.345    0.047 tensor.py:195(backward)
                1526636   12.811    0.000 71386.979    0.047 __init__.py:68(backward)
                1526636 71334.991    0.047 71334.991    0.047 {method 'run_backward' of 'torch._C._EngineBase' objects}
              236017924 71209.827    0.000 71209.827    0.000 {built-in method conv2d}
               38165900 3844.373    0.000 22647.552    0.001 optionCritic.py:91(get_action)
              466355541 1574.735    0.000 20978.486    0.000 linear.py:93(forward)
              466355541  588.732    0.000 18766.511    0.000 functional.py:1737(linear)
              466355541 18060.187    0.000 18060.187    0.000 {built-in method torch._C._nn.linear}
               38165900 1184.159    0.000 12718.907    0.000 optionCritic.py:80(predict_option_termination)
               76331800 1063.131    0.000 8219.103    0.000 distribution.py:34(__init__)
              354026886  423.840    0.000 7914.283    0.000 activation.py:713(forward)
              354026886  437.258    0.000 7490.443    0.000 functional.py:1364(leaky_relu)
               38165900  611.986    0.000 7399.397    0.000 categorical.py:115(log_prob)
              354026886 6969.033    0.000 6969.033    0.000 {built-in method torch._C._nn.leaky_relu}
               38165900  879.194    0.000 6657.399    0.000 categorical.py:49(__init__)
              115687254  477.285    0.000 6374.218    0.000 optionCritic.py:77(get_Q)
               76484463  465.870    0.000 5170.888    0.000 optionCritic.py:88(get_terminations)
                1526636   30.507    0.000 4786.161    0.003 optimizer.py:84(wrapper)
                1526636   14.132    0.000 4663.728    0.003 grad_mode.py:24(decorate_context)
                1526636  104.135    0.000 4621.397    0.003 rmsprop.py:56(step)
               38165900  274.681    0.000 4458.069    0.000 bernoulli.py:34(__init__)
                1526636  149.410    0.000 4403.622    0.003 _functional.py:203(rmsprop)
               38165900 2719.058    0.000 4125.733    0.000 constraints.py:398(check)
                1526636    9.105    0.000 3529.750    0.002 game.py:42(step)
                 152663   33.408    0.000 3499.130    0.023 optionCritic.py:116(critic_loss_fn)
                1526636   16.103    0.000 3414.543    0.002 layers.py:827(step)
               38165900  470.448    0.000 3061.909    0.000 distribution.py:240(_validate_sample)
               21372886 2545.926    0.000 2545.926    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              118008962  162.942    0.000 2250.608    0.000 activation.py:101(forward)
               38165900 1052.917    0.000 2188.850    0.000 categorical.py:123(entropy)
              118008962  150.601    0.000 2087.666    0.000 functional.py:1195(relu)
               38165900 2036.201    0.000 2036.201    0.000 constraints.py:249(check)
               38165900 1977.706    0.000 1977.706    0.000 constraints.py:364(check)
              118008962 1909.945    0.000 1909.945    0.000 {built-in method relu}
             1427220233 1854.225    0.000 1854.225    0.000 {built-in method torch._C._get_tracing_state}
              114497700  209.061    0.000 1841.507    0.000 utils.py:106(__get__)
              267161300 1755.387    0.000 1755.387    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                1526636   63.898    0.000 1730.909    0.001 layers.py:17(step)
               38165900  296.278    0.000 1693.614    0.000 bernoulli.py:86(sample)
               38165900  112.665    0.000 1661.923    0.000 layer.py:106(move)
                1526637  147.902    0.000 1661.407    0.001 layers.py:793(update)
              114803026  179.838    0.000 1639.298    0.000 tensor.py:525(__rsub__)
             1829429334 1637.224    0.000 1637.227    0.000 module.py:934(__getattr__)
              114497700 1571.359    0.000 1571.359    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
              118008962  115.992    0.000 1538.785    0.000 flatten.py:39(forward)
               38165900   74.277    0.000 1470.867    0.000 categorical.py:88(logits)
              114650363 1441.806    0.000 1441.806    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
              114803026 1427.994    0.000 1427.994    0.000 {built-in method rsub}
               38165900  371.038    0.000 1423.821    0.000 categorical.py:108(sample)
              118008962 1422.792    0.000 1422.792    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               38165900   76.284    0.000 1396.590    0.000 utils.py:82(probs_to_logits)
               76331800  391.252    0.000 1233.089    0.000 functional.py:46(broadcast_tensors)
               76484463 1204.231    0.000 1204.231    0.000 {method 'max' of 'torch._C._TensorBase' objects}
               38165900  241.302    0.000 1154.707    0.000 layers.py:844(check)
              114497700 1076.982    0.000 1076.982    0.000 {method 'all' of 'torch._C._TensorBase' objects}
             6183802417 1045.214    0.000 1056.843    0.000 {built-in method builtins.len}
               16792996   45.205    0.000 1030.501    0.000 tensor.py:575(__iter__)
               16792996  950.304    0.000  950.304    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
             5759717910  916.852    0.000  916.852    0.000 {method 'values' of 'collections.OrderedDict' objects}
               38165900  184.443    0.000  882.684    0.000 utils.py:11(broadcast_all)
               38165900  135.342    0.000  866.945    0.000 utils.py:77(clamp_probs)
               38165900  809.769    0.000  809.769    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               76331800  737.467    0.000  737.467    0.000 {built-in method broadcast_tensors}
                 884253   17.014    0.000  736.539    0.001 layers.py:849(restart)
               38165900  731.604    0.000  731.604    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
                1526636   78.045    0.000  726.770    0.000 replaybuffer.py:34(save_option_critic)
              114955689  697.974    0.000  697.974    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               38165900  677.133    0.000  677.133    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
              229300726  639.240    0.000  639.240    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               38165900  625.589    0.000  625.589    0.000 {built-in method clamp}
                 884253    7.346    0.000  619.345    0.001 level.py:8(__init__)
               76331800  585.181    0.000  585.181    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               39050128  581.342    0.000  581.342    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               21372886  576.510    0.000  576.510    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                 884253   21.150    0.000  558.382    0.001 levels.py:249(generate)
               10135498  270.386    0.000  557.920    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               38165900  556.321    0.000  556.321    0.000 {built-in method bernoulli}
                5745414   77.819    0.000  516.156    0.000 level.py:41(notUsed)
                1526636   95.834    0.000  484.783    0.000 optimizer.py:189(zero_grad)
               38165900  470.857    0.000  470.857    0.000 {built-in method all}
               38165900  453.360    0.000  453.360    0.000 {built-in method log}
               38165900  445.242    0.000  445.242    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
               13739733  256.701    0.000  421.740    0.000 layer.py:175(NoRock_update)
               21372886  412.972    0.000  412.972    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               21372886  369.049    0.000  369.049    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               21372886  349.754    0.000  349.754    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               38165900  337.499    0.000  337.499    0.000 {built-in method multinomial}
               38165900   89.681    0.000  321.249    0.000 layers.py:838(isFree)
              118008976  315.818    0.000  315.818    0.000 {method 'to' of 'torch._C._TensorBase' objects}
              911485437  214.172    0.000  305.337    0.000 enum.py:646(__hash__)
              115385004  305.243    0.000  305.243    0.000 {method 'item' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9607846: <Attempt3_Diamonds2_option_critic_0> in cluster <dcc> Done

Job <Attempt3_Diamonds2_option_critic_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon May  3 13:31:23 2021
Job was executed on host(s) <n-62-23-24>, in queue <hpc>, as user <s183914> in cluster <dcc> at Mon May  3 13:31:24 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon May  3 13:31:24 2021
Terminated at Thu May  6 13:26:33 2021
Results reported at Thu May  6 13:26:33 2021

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

    CPU time :                                   258881.08 sec.
    Max Memory :                                 1029 MB
    Average Memory :                             1010.39 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15355.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258939 sec.
    Turnaround time :                            258910 sec.

The output (if any) is above this job summary.

