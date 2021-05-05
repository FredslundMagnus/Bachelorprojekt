
# Parameters

    Name :                      Attempt2_Diamonds2_option_critic-0
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


      49682383432 function calls (48160737362 primitive calls) in 258900.77 seconds

##    Ordered by: cumulative time
   List reduced from 430 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.774 258900.774 {built-in method builtins.exec}
                      1    0.372    0.372 258900.774 258900.774 <string>:1(<module>)
                      1 6036.311 6036.311 258900.402 258900.402 optionCritic.py:195(option_critic_run)
               54112575 9375.371    0.000 111594.553    0.002 optionCritic.py:143(actor_loss_fn)
        2010214615/495603652 9944.830    0.000 110822.712    0.000 module.py:866(_call_impl)
              168290107  834.460    0.000 103336.371    0.001 optionCritic.py:70(get_state)
              168290107 2182.642    0.000 99999.355    0.001 container.py:117(forward)
                2164503   19.425    0.000 76370.520    0.035 tensor.py:195(backward)
                2164503   24.083    0.000 76350.792    0.035 __init__.py:68(backward)
                2164503 76273.599    0.035 76273.599    0.035 {method 'run_backward' of 'torch._C._EngineBase' objects}
              336580214  933.159    0.000 62979.802    0.000 conv.py:398(forward)
              336580214  508.830    0.000 61656.694    0.000 conv.py:390(_conv_forward)
              336580214 61147.864    0.000 61147.864    0.000 {built-in method conv2d}
              663893759 1562.328    0.000 21596.783    0.000 linear.py:93(forward)
              663893759  653.101    0.000 19347.658    0.000 functional.py:1737(linear)
               54112575 3245.012    0.000 19248.210    0.000 optionCritic.py:91(get_action)
              663893759 18542.606    0.000 18542.606    0.000 {built-in method torch._C._nn.linear}
               54112575 1253.716    0.000 14890.382    0.000 optionCritic.py:80(predict_option_termination)
                2164503   51.185    0.000 8448.838    0.004 optimizer.py:84(wrapper)
                2164503   28.533    0.000 8260.309    0.004 grad_mode.py:24(decorate_context)
                2164503  125.493    0.000 8178.813    0.004 rmsprop.py:56(step)
              108225150 1304.453    0.000 8006.953    0.000 distribution.py:34(__init__)
                2164503  131.673    0.000 7912.941    0.004 _functional.py:203(rmsprop)
              504870321  524.971    0.000 7136.207    0.000 activation.py:713(forward)
              504870321  542.964    0.000 6611.236    0.000 functional.py:1364(leaky_relu)
               54112575  539.711    0.000 6398.682    0.000 categorical.py:115(log_prob)
               54112575  499.810    0.000 6269.605    0.000 bernoulli.py:34(__init__)
              504870321 5949.723    0.000 5949.723    0.000 {built-in method torch._C._nn.leaky_relu}
              164434695  380.341    0.000 5519.550    0.000 optionCritic.py:77(get_Q)
               54112575  744.135    0.000 5414.305    0.000 categorical.py:49(__init__)
                 541125   94.122    0.000 4896.197    0.009 optionCritic.py:116(critic_loss_fn)
              108766275  401.869    0.000 4380.176    0.000 optionCritic.py:88(get_terminations)
                2164503   11.565    0.000 4325.923    0.002 game.py:42(step)
                2164503   23.328    0.000 4183.137    0.002 layers.py:827(step)
               30303036 3999.863    0.000 3999.863    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               54112575 2231.549    0.000 3298.149    0.000 constraints.py:398(check)
               30303036 2744.677    0.000 2744.677    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               54112575  459.230    0.000 2631.573    0.000 distribution.py:240(_validate_sample)
                2164503   80.855    0.000 2272.712    0.001 layers.py:17(step)
               54112575  481.561    0.000 2255.081    0.000 bernoulli.py:86(sample)
               54112575 2210.333    0.000 2210.333    0.000 constraints.py:364(check)
               54112575  138.609    0.000 2184.966    0.000 layer.py:106(move)
              168290107  223.786    0.000 2024.098    0.000 activation.py:101(forward)
                2164504  188.826    0.000 1879.102    0.001 layers.py:793(update)
             2605058193 1816.335    0.000 1816.495    0.000 module.py:934(__getattr__)
              168290107  215.017    0.000 1800.311    0.000 functional.py:1195(relu)
              378788025 1786.341    0.000 1786.341    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               54112575  920.744    0.000 1778.713    0.000 categorical.py:123(entropy)
               54112575 1710.448    0.000 1710.448    0.000 constraints.py:249(check)
              168290107  174.321    0.000 1617.267    0.000 flatten.py:39(forward)
              163419975  224.409    0.000 1602.574    0.000 tensor.py:525(__rsub__)
              162337725  215.816    0.000 1576.153    0.000 utils.py:106(__get__)
              108225150  566.779    0.000 1575.377    0.000 functional.py:46(broadcast_tensors)
              168290107 1556.387    0.000 1556.387    0.000 {built-in method relu}
               54112575  345.989    0.000 1517.771    0.000 utils.py:11(broadcast_all)
              168290107 1442.947    0.000 1442.947    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               54112575  306.022    0.000 1423.313    0.000 layers.py:844(check)
               23809533   57.288    0.000 1388.480    0.000 tensor.py:575(__iter__)
              163419975 1349.121    0.000 1349.121    0.000 {built-in method rsub}
              108766275 1310.639    0.000 1310.639    0.000 {method 'max' of 'torch._C._TensorBase' objects}
               23809533 1297.513    0.000 1297.513    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               54112575  366.223    0.000 1273.296    0.000 categorical.py:108(sample)
                 541125 1028.244    0.002 1257.321    0.002 replaybuffer.py:42(sample_option_critic)
              162878850 1218.500    0.000 1218.500    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
             2034024148 1207.624    0.000 1207.624    0.000 {built-in method torch._C._get_tracing_state}
               54112575   63.363    0.000 1196.398    0.000 categorical.py:88(logits)
               54112575   69.402    0.000 1133.035    0.000 utils.py:82(probs_to_logits)
             8808292150 1110.358    0.000 1129.673    0.000 {built-in method builtins.len}
              162337725 1121.571    0.000 1121.571    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
              162337725 1009.705    0.000 1009.705    0.000 {method 'all' of 'torch._C._TensorBase' objects}
             8209148567  912.167    0.000  912.167    0.000 {method 'values' of 'collections.OrderedDict' objects}
              108225150  845.158    0.000  845.158    0.000 {built-in method broadcast_tensors}
               54112575  834.730    0.000  834.730    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
                2164503   82.773    0.000  735.978    0.000 replaybuffer.py:34(save_option_critic)
                1014744   18.327    0.000  694.202    0.001 layers.py:849(restart)
                2164503  103.800    0.000  663.719    0.000 optimizer.py:189(zero_grad)
               54112575  137.604    0.000  650.166    0.000 utils.py:77(clamp_probs)
               54112575  641.635    0.000  641.635    0.000 {built-in method bernoulli}
              163961100  632.767    0.000  632.767    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
                1014744    8.663    0.000  576.238    0.001 level.py:8(__init__)
               54112575  551.717    0.000  551.717    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
               55127295  530.719    0.000  530.719    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
              325757700  521.754    0.000  521.754    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               19480536  314.392    0.000  519.443    0.000 layer.py:175(NoRock_update)
               54112575  512.561    0.000  512.561    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
                1014744   21.112    0.000  511.489    0.001 levels.py:249(generate)
               54112575  113.053    0.000  507.804    0.000 layers.py:838(isFree)
              714622653  300.641    0.000  507.641    0.000 {built-in method builtins.isinstance}
                6596750   80.907    0.000  468.999    0.000 level.py:41(notUsed)
              108225150  466.856    0.000  466.856    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               54112575  453.311    0.000  453.311    0.000 {built-in method clamp}
               14610397  426.128    0.000  426.128    0.000 {built-in method tensor}
              163356797  425.840    0.000  425.840    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               30303036  423.349    0.000  423.349    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               54112575  413.467    0.000  413.467    0.000 {built-in method log}
              378600099  326.002    0.000  394.750    0.000 layer.py:103(isFree)
               54112575  389.515    0.000  389.515    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
              168290121  381.394    0.000  381.394    0.000 {method 'to' of 'torch._C._TensorBase' objects}
             1189931639  257.977    0.000  375.538    0.000 enum.py:646(__hash__)
              162337750  135.599    0.000  365.037    0.000 {built-in method builtins.all}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9606119: <Attempt2_Diamonds2_option_critic_0> in cluster <dcc> Done

Job <Attempt2_Diamonds2_option_critic_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon May  3 01:33:08 2021
Job was executed on host(s) <n-62-11-67>, in queue <hpc>, as user <s183914> in cluster <dcc> at Mon May  3 01:33:09 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon May  3 01:33:09 2021
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

    CPU time :                                   258267.38 sec.
    Max Memory :                                 1021 MB
    Average Memory :                             999.03 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15363.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258942 sec.
    Turnaround time :                            258919 sec.

The output (if any) is above this job summary.

