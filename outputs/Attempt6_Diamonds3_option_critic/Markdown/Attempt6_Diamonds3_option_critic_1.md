
# Parameters

    Name :                      Attempt6_Diamonds3_option_critic-1
    Main :                      option_critic_run
    Level :                     Levels.Causal6
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


      22881728302 function calls (22158030436 primitive calls) in 258900.90 seconds

##    Ordered by: cumulative time
   List reduced from 429 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.902 258900.902 {built-in method builtins.exec}
                      1    0.300    0.300 258900.902 258900.902 <string>:1(<module>)
                      1 2466.707 2466.707 258900.602 258900.602 optionCritic.py:195(option_critic_run)
                 811320    6.288    0.000 178255.955    0.220 tensor.py:195(backward)
                 811320    7.813    0.000 178249.551    0.220 __init__.py:68(backward)
                 811320 178225.858    0.220 178225.858    0.220 {method 'run_backward' of 'torch._C._EngineBase' objects}
        957718402/236657743 4473.754    0.000 51086.006    0.000 module.py:866(_call_impl)
               25962240 3719.432    0.000 50141.798    0.002 optionCritic.py:143(actor_loss_fn)
               80117851  361.838    0.000 47616.484    0.001 optionCritic.py:70(get_state)
               80117851 1013.967    0.000 46167.462    0.001 container.py:117(forward)
              160235702  420.988    0.000 29507.580    0.000 conv.py:398(forward)
              160235702  233.242    0.000 28919.462    0.000 conv.py:390(_conv_forward)
              160235702 28686.219    0.000 28686.219    0.000 {built-in method conv2d}
              316775594  740.191    0.000 9707.556    0.000 linear.py:93(forward)
               25962240 1470.499    0.000 8771.421    0.000 optionCritic.py:91(get_action)
              316775594  293.947    0.000 8657.661    0.000 functional.py:1737(linear)
              316775594 8295.281    0.000 8295.281    0.000 {built-in method torch._C._nn.linear}
               25962240  514.334    0.000 6089.085    0.000 optionCritic.py:80(predict_option_termination)
               51924480  524.992    0.000 3405.241    0.000 distribution.py:34(__init__)
                 811320   17.550    0.000 3282.191    0.004 optimizer.py:84(wrapper)
                 811320    9.247    0.000 3218.129    0.004 grad_mode.py:24(decorate_context)
                 811320   48.956    0.000 3191.705    0.004 adam.py:55(step)
              240353553  239.108    0.000 3181.818    0.000 activation.py:713(forward)
                 811320  273.290    0.000 3090.669    0.004 _functional.py:53(adam)
              240353553  237.994    0.000 2942.710    0.000 functional.py:1364(leaky_relu)
               25962240  247.578    0.000 2923.962    0.000 categorical.py:115(log_prob)
              240353553 2656.347    0.000 2656.347    0.000 {built-in method torch._C._nn.leaky_relu}
               78450342  196.771    0.000 2566.943    0.000 optionCritic.py:77(get_Q)
               25962240  333.310    0.000 2465.060    0.000 categorical.py:49(__init__)
               25962240  182.869    0.000 2348.589    0.000 bernoulli.py:34(__init__)
                 202830   31.980    0.000 2237.506    0.011 optionCritic.py:116(critic_loss_fn)
               52127310  181.631    0.000 1953.676    0.000 optionCritic.py:88(get_terminations)
                 811320    3.922    0.000 1650.599    0.002 game.py:42(step)
                 811320    7.175    0.000 1600.799    0.002 layers.py:827(step)
               25962240 1015.124    0.000 1501.484    0.000 constraints.py:398(check)
               25962240  207.752    0.000 1181.757    0.000 distribution.py:240(_validate_sample)
                 811320   34.380    0.000  965.802    0.001 layers.py:17(step)
               25962240   61.843    0.000  928.321    0.000 layer.py:106(move)
               80117851  101.573    0.000  909.867    0.000 activation.py:101(forward)
               25962240  896.955    0.000  896.955    0.000 constraints.py:364(check)
               25962240  161.948    0.000  865.257    0.000 bernoulli.py:86(sample)
             1242710344  810.702    0.000  810.758    0.000 module.py:934(__getattr__)
               80117851   86.475    0.000  808.294    0.000 functional.py:1195(relu)
               25962240  420.495    0.000  807.567    0.000 categorical.py:123(entropy)
               25962240  763.734    0.000  763.734    0.000 constraints.py:249(check)
              181735680  759.217    0.000  759.217    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               77886720  100.777    0.000  727.803    0.000 utils.py:106(__get__)
               80117851   87.113    0.000  726.527    0.000 flatten.py:39(forward)
               80117851  708.472    0.000  708.472    0.000 {built-in method relu}
               78292380   82.914    0.000  693.435    0.000 tensor.py:525(__rsub__)
               22716948  659.758    0.000  659.758    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               51924480  233.358    0.000  649.175    0.000 functional.py:46(broadcast_tensors)
               80117851  639.414    0.000  639.414    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                 811321   70.734    0.000  624.290    0.001 layers.py:793(update)
               78292380  597.426    0.000  597.426    0.000 {built-in method rsub}
               25962240  120.959    0.000  582.195    0.000 layers.py:844(check)
               25962240  159.283    0.000  575.408    0.000 categorical.py:108(sample)
              966642922  557.524    0.000  557.524    0.000 {built-in method torch._C._get_tracing_state}
               25962240   29.214    0.000  551.479    0.000 categorical.py:88(logits)
               52127310  546.960    0.000  546.960    0.000 {method 'max' of 'torch._C._TensorBase' objects}
               78089550  545.426    0.000  545.426    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
               25962240  111.255    0.000  541.264    0.000 utils.py:11(broadcast_all)
               11358474  541.021    0.000  541.021    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                8924520   19.694    0.000  538.812    0.000 tensor.py:575(__iter__)
             4164689144  517.142    0.000  522.515    0.000 {built-in method builtins.len}
               25962240   31.807    0.000  522.264    0.000 utils.py:82(probs_to_logits)
               11358474  513.723    0.000  513.723    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               77886720  508.474    0.000  508.474    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                8924520  506.921    0.000  506.921    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
             3910991459  441.700    0.000  441.700    0.000 {method 'values' of 'collections.OrderedDict' objects}
               77886720  424.034    0.000  424.034    0.000 {method 'all' of 'torch._C._TensorBase' objects}
               11358474  386.257    0.000  386.257    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               25962240  383.761    0.000  383.761    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
                 202830  304.737    0.002  377.300    0.002 replaybuffer.py:42(sample_option_critic)
               22716948  357.494    0.000  357.494    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               11358474  355.052    0.000  355.052    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               51924480  339.525    0.000  339.525    0.000 {built-in method broadcast_tensors}
               25962240   62.052    0.000  309.460    0.000 utils.py:77(clamp_probs)
                 811320   35.755    0.000  306.930    0.000 replaybuffer.py:34(save_option_critic)
               78495210  279.183    0.000  279.183    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               25962240  268.457    0.000  268.457    0.000 {built-in method bernoulli}
               25962240  253.233    0.000  253.233    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
               25962240  247.408    0.000  247.408    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
               26120202  239.674    0.000  239.674    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
              156179100  234.763    0.000  234.763    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               25962240   53.258    0.000  231.221    0.000 layers.py:838(isFree)
               51924480  215.160    0.000  215.160    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
                 811320   36.692    0.000  208.991    0.000 optimizer.py:189(zero_grad)
               25962240  205.741    0.000  205.741    0.000 {built-in method clamp}
                6490568  113.025    0.000  192.679    0.000 layer.py:175(NoRock_update)
               77886752   53.263    0.000  191.960    0.000 {built-in method builtins.all}
               25962240  180.997    0.000  180.997    0.000 {built-in method log}
              192080355  147.501    0.000  177.963    0.000 layer.py:103(isFree)
               25962240  177.436    0.000  177.436    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
               25962240  162.326    0.000  162.326    0.000 {built-in method all}
              341692564  107.898    0.000  162.187    0.000 {built-in method builtins.isinstance}
               80117865  159.862    0.000  159.862    0.000 {method 'to' of 'torch._C._TensorBase' objects}
                5476414  152.617    0.000  152.617    0.000 {built-in method tensor}
               25962240  147.824    0.000  147.824    0.000 {built-in method multinomial}
              468764908  102.600    0.000  146.019    0.000 enum.py:646(__hash__)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9624154: <Attempt6_Diamonds3_option_critic_1> in cluster <dcc> Done

Job <Attempt6_Diamonds3_option_critic_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun May  9 01:22:26 2021
Job was executed on host(s) <n-62-11-60>, in queue <hpc>, as user <s183914> in cluster <dcc> at Sun May  9 01:22:27 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun May  9 01:22:27 2021
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

Successfully completed.

Resource usage summary:

    CPU time :                                   258290.30 sec.
    Max Memory :                                 940 MB
    Average Memory :                             923.71 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15444.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258956 sec.
    Turnaround time :                            258909 sec.

The output (if any) is above this job summary.

