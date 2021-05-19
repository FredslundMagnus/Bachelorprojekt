[W NNPACK.cpp:80] Could not initialize NNPACK! Reason: Unsupported hardware.

# Parameters

    Name :                      Attempt8_Monsters_option_critic-1
    Main :                      option_critic_run
    Level :                     Levels.MonsterLevel
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


      40015503122 function calls (38797829876 primitive calls) in 258901.04 seconds

##    Ordered by: cumulative time
   List reduced from 434 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258901.037 258901.037 {built-in method builtins.exec}
                      1    0.334    0.334 258901.037 258901.037 <string>:1(<module>)
                      1 4363.335 4363.335 258900.702 258900.702 optionCritic.py:195(option_critic_run)
        1612333225/399097036 11110.280    0.000 115493.889    0.000 module.py:866(_call_impl)
               43683328 9855.667    0.000 115351.282    0.003 optionCritic.py:143(actor_loss_fn)
              134804021  837.695    0.000 105231.797    0.001 optionCritic.py:70(get_state)
              134804021 2980.653    0.000 101819.976    0.001 container.py:117(forward)
                1365104   10.569    0.000 71785.738    0.053 tensor.py:195(backward)
                1365104   11.908    0.000 71774.907    0.053 __init__.py:68(backward)
                1365104 71730.926    0.053 71730.926    0.053 {method 'run_backward' of 'torch._C._EngineBase' objects}
              269608042  996.330    0.000 60716.103    0.000 conv.py:398(forward)
              269608042  456.433    0.000 59364.951    0.000 conv.py:390(_conv_forward)
              269608042 58908.517    0.000 58908.517    0.000 {built-in method conv2d}
               43683328 4417.122    0.000 25874.303    0.001 optionCritic.py:91(get_action)
              533901057 1819.723    0.000 23270.700    0.000 linear.py:93(forward)
              533901057  638.531    0.000 20768.750    0.000 functional.py:1737(linear)
              533901057 19992.942    0.000 19992.942    0.000 {built-in method torch._C._nn.linear}
               43683328 1299.989    0.000 13900.503    0.000 optionCritic.py:80(predict_option_termination)
               87366656 1169.046    0.000 9294.126    0.000 distribution.py:34(__init__)
              404412063  475.234    0.000 8901.425    0.000 activation.py:713(forward)
               43683328  678.694    0.000 8447.938    0.000 categorical.py:115(log_prob)
              404412063  501.872    0.000 8426.191    0.000 functional.py:1364(leaky_relu)
              404412063 7818.291    0.000 7818.291    0.000 {built-in method torch._C._nn.leaky_relu}
               43683328  975.869    0.000 7595.958    0.000 categorical.py:49(__init__)
              132901755  513.107    0.000 7118.274    0.000 optionCritic.py:77(get_Q)
               87707932  498.693    0.000 5756.288    0.000 optionCritic.py:88(get_terminations)
                 341276   72.816    0.000 5164.979    0.015 optionCritic.py:116(critic_loss_fn)
               43683328  272.565    0.000 4777.867    0.000 bernoulli.py:34(__init__)
               43683328 3152.227    0.000 4745.751    0.000 constraints.py:398(check)
                1365104    8.315    0.000 4659.841    0.003 game.py:42(step)
                1365104   11.855    0.000 4557.242    0.003 layers.py:827(step)
               43683328  518.025    0.000 3558.814    0.000 distribution.py:240(_validate_sample)
                1365104   26.565    0.000 3301.187    0.002 optimizer.py:84(wrapper)
                1365104   11.788    0.000 3195.037    0.002 grad_mode.py:24(decorate_context)
                1365104   90.169    0.000 3158.545    0.002 rmsprop.py:56(step)
                1365104  136.331    0.000 2968.418    0.002 _functional.py:203(rmsprop)
              134804021  172.067    0.000 2526.599    0.000 activation.py:101(forward)
               43683328 1221.358    0.000 2499.776    0.000 categorical.py:123(entropy)
               43683328 2410.267    0.000 2410.267    0.000 constraints.py:249(check)
              134804021  156.342    0.000 2354.532    0.000 functional.py:1195(relu)
                1365104   70.529    0.000 2345.523    0.002 layers.py:17(step)
               43683328  177.999    0.000 2269.638    0.000 layer.py:106(move)
               43683328 2199.194    0.000 2199.194    0.000 constraints.py:364(check)
                1365105  144.554    0.000 2193.335    0.002 layers.py:793(update)
              134804021 2164.172    0.000 2164.172    0.000 {built-in method relu}
              131049984  229.627    0.000 2066.592    0.000 utils.py:106(__get__)
              305783296 2029.850    0.000 2029.850    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
             1627349369 2014.473    0.000 2014.473    0.000 {built-in method torch._C._get_tracing_state}
              131732536  195.443    0.000 1831.013    0.000 tensor.py:525(__rsub__)
               43683328  303.220    0.000 1772.083    0.000 bernoulli.py:86(sample)
             2093659413 1771.129    0.000 1771.258    0.000 module.py:934(__getattr__)
              131049984 1768.587    0.000 1768.587    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
              134804021  124.772    0.000 1757.648    0.000 flatten.py:39(forward)
               43683328   79.596    0.000 1656.991    0.000 categorical.py:88(logits)
               43683328  223.911    0.000 1656.925    0.000 layers.py:844(check)
              134804021 1632.876    0.000 1632.876    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              131391260 1621.245    0.000 1621.245    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
               43683328  412.460    0.000 1607.962    0.000 categorical.py:108(sample)
              131732536 1599.488    0.000 1599.488    0.000 {built-in method rsub}
               43683328   86.068    0.000 1577.395    0.000 utils.py:82(probs_to_logits)
               19111450 1472.746    0.000 1472.746    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               28406714  655.013    0.000 1384.181    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               87366656  425.379    0.000 1344.961    0.000 functional.py:46(broadcast_tensors)
               87707932 1302.021    0.000 1302.021    0.000 {method 'max' of 'torch._C._TensorBase' objects}
              131049984 1209.024    0.000 1209.024    0.000 {method 'all' of 'torch._C._TensorBase' objects}
             6857760723 1155.236    0.000 1165.984    0.000 {built-in method builtins.len}
               15016144   39.500    0.000 1055.705    0.000 tensor.py:575(__iter__)
                1169250   19.104    0.000 1036.530    0.001 layers.py:849(restart)
               15016144  985.832    0.000  985.832    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
             6584136921  985.518    0.000  985.518    0.000 {method 'values' of 'collections.OrderedDict' objects}
               43683328  147.731    0.000  971.803    0.000 utils.py:77(clamp_probs)
               43683328  567.344    0.000  960.835    0.000 layers.py:538(check)
               43683328  935.924    0.000  935.924    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
                1169250    9.002    0.000  888.599    0.001 level.py:8(__init__)
               43683328  163.976    0.000  887.004    0.000 utils.py:11(broadcast_all)
               43683328  824.071    0.000  824.071    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
               87366656  809.416    0.000  809.416    0.000 {built-in method broadcast_tensors}
                1169250  137.138    0.000  808.195    0.001 levels.py:428(generate)
              132073812  792.882    0.000  792.882    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
                1365104   77.811    0.000  776.380    0.001 replaybuffer.py:34(save_option_critic)
               43683328  767.054    0.000  767.054    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
               28406714   45.542    0.000  729.168    0.000 <__array_function__ internals>:2(prod)
              262782520  716.380    0.000  716.380    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               43683328  698.532    0.000  698.532    0.000 {built-in method clamp}
               28406714   41.373    0.000  674.444    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
               87366656  673.134    0.000  673.134    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               44852547  640.690    0.000  640.690    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               28406714   64.247    0.000  633.071    0.000 fromnumeric.py:2912(prod)
                 341276  457.983    0.001  592.166    0.002 replaybuffer.py:42(sample_option_critic)
               43683328  571.945    0.000  571.945    0.000 {built-in method bernoulli}
               28406714  147.592    0.000  568.825    0.000 fromnumeric.py:70(_wrapreduction)
                5846250   78.590    0.000  541.507    0.000 level.py:41(notUsed)
               43683328  535.222    0.000  535.222    0.000 {built-in method all}
               43683328  519.524    0.000  519.524    0.000 {built-in method log}
               43683328  513.255    0.000  513.255    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
                8190630  327.906    0.000  482.617    0.000 layer.py:159(update)
               19111450  463.383    0.000  463.383    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               43592976   46.439    0.000  438.909    0.000 {built-in method builtins.any}
                1365104   77.359    0.000  415.478    0.000 optimizer.py:189(zero_grad)
              302993100  116.046    0.000  392.676    0.000 layers.py:809(<genexpr>)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9632943: <Attempt8_Monsters_option_critic_1> in cluster <dcc> Done

Job <Attempt8_Monsters_option_critic_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed May 12 15:36:18 2021
Job was executed on host(s) <n-62-23-21>, in queue <hpc>, as user <s183914> in cluster <dcc> at Sun May 16 23:16:53 2021
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

    CPU time :                                   258867.23 sec.
    Max Memory :                                 792 MB
    Average Memory :                             788.00 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15592.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258978 sec.
    Turnaround time :                            632165 sec.

The output (if any) is above this job summary.

