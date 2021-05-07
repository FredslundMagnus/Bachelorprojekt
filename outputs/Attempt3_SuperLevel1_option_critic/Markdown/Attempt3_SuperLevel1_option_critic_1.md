
# Parameters

    Name :                      Attempt3_SuperLevel1_option_critic-1
    Main :                      option_critic_run
    Level :                     Levels.SuperLevel
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


      41035292287 function calls (39864605128 primitive calls) in 258900.65 seconds

##    Ordered by: cumulative time
   List reduced from 443 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.651 258900.651 {built-in method builtins.exec}
                      1    0.327    0.327 258900.651 258900.651 <string>:1(<module>)
                      1 4116.690 4116.690 258900.324 258900.324 optionCritic.py:195(option_critic_run)
        1554210722/383633570 9376.678    0.000 112559.440    0.000 module.py:866(_call_impl)
               42064725 8034.710    0.000 111173.894    0.003 optionCritic.py:143(actor_loss_fn)
              130064128  719.190    0.000 104753.287    0.001 optionCritic.py:70(get_state)
              130064128 2283.478    0.000 101946.187    0.001 container.py:117(forward)
              260128256  898.866    0.000 69011.296    0.000 conv.py:398(forward)
                1682589   11.492    0.000 68796.111    0.041 tensor.py:195(backward)
                1682589   16.144    0.000 68784.352    0.041 __init__.py:68(backward)
                1682589 68731.284    0.041 68731.284    0.041 {method 'run_backward' of 'torch._C._EngineBase' objects}
              260128256  469.098    0.000 67787.800    0.000 conv.py:390(_conv_forward)
              260128256 67318.702    0.000 67318.702    0.000 {built-in method conv2d}
                1682589   36.091    0.000 20324.172    0.012 optimizer.py:84(wrapper)
                1682589   20.570    0.000 20189.380    0.012 grad_mode.py:24(decorate_context)
                1682589  103.984    0.000 20132.396    0.012 rmsprop.py:56(step)
               42064725 3481.480    0.000 20042.243    0.000 optionCritic.py:91(get_action)
                1682589  122.832    0.000 19912.479    0.012 _functional.py:203(rmsprop)
              513697698 1519.037    0.000 18390.622    0.000 linear.py:93(forward)
               23556228 17184.240    0.001 17184.240    0.001 {method 'sqrt' of 'torch._C._TensorBase' objects}
              513697698  626.995    0.000 16320.995    0.000 functional.py:1737(linear)
              513697698 15559.754    0.000 15559.754    0.000 {built-in method torch._C._nn.linear}
               42064725 1105.460    0.000 12537.935    0.000 optionCritic.py:80(predict_option_termination)
               84129450 1115.041    0.000 7389.322    0.000 distribution.py:34(__init__)
              390192384  487.959    0.000 6986.289    0.000 activation.py:713(forward)
               42064725  574.156    0.000 6685.223    0.000 categorical.py:115(log_prob)
              390192384  484.063    0.000 6498.331    0.000 functional.py:1364(leaky_relu)
              390192384 5907.779    0.000 5907.779    0.000 {built-in method torch._C._nn.leaky_relu}
                1682589   11.415    0.000 5641.046    0.003 game.py:42(step)
               42064725  764.507    0.000 5640.264    0.000 categorical.py:49(__init__)
              127207009  439.631    0.000 5550.043    0.000 optionCritic.py:77(get_Q)
                1682589   17.403    0.000 5507.778    0.003 layers.py:827(step)
               42064725  335.305    0.000 4634.153    0.000 bernoulli.py:34(__init__)
               84297708  430.200    0.000 4223.007    0.000 optionCritic.py:88(get_terminations)
                1682589   73.151    0.000 3718.110    0.002 layers.py:17(step)
               42064725  238.636    0.000 3638.303    0.000 layer.py:106(move)
               42064725 2309.306    0.000 3411.432    0.000 constraints.py:398(check)
               42064725  465.859    0.000 2673.887    0.000 distribution.py:240(_validate_sample)
                 168258   30.909    0.000 2580.310    0.015 optionCritic.py:116(critic_loss_fn)
               42064725  445.416    0.000 2522.051    0.000 layers.py:844(check)
              130064128  183.033    0.000 1910.612    0.000 activation.py:101(forward)
               42064725 1869.762    0.000 1869.762    0.000 constraints.py:364(check)
               42064725  914.184    0.000 1828.703    0.000 categorical.py:123(entropy)
                1682590  153.320    0.000 1764.357    0.001 layers.py:793(update)
              130064128  162.965    0.000 1727.579    0.000 functional.py:1195(relu)
               42064725  343.381    0.000 1716.901    0.000 bernoulli.py:86(sample)
              126194175  217.679    0.000 1707.457    0.000 utils.py:106(__get__)
               42064725 1683.971    0.000 1683.971    0.000 constraints.py:249(check)
             2015419369 1545.774    0.000 1545.777    0.000 module.py:934(__getattr__)
              130064128 1536.390    0.000 1536.390    0.000 {built-in method relu}
               23556228 1410.507    0.000 1410.507    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              130064128  134.321    0.000 1376.513    0.000 flatten.py:39(forward)
              126530691  173.777    0.000 1367.722    0.000 tensor.py:525(__rsub__)
              294453075 1349.026    0.000 1349.026    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               84129450  474.856    0.000 1334.172    0.000 functional.py:46(broadcast_tensors)
               42064725   71.903    0.000 1320.913    0.000 categorical.py:88(logits)
               42064725  341.696    0.000 1293.953    0.000 categorical.py:108(sample)
             1572719201 1291.981    0.000 1291.981    0.000 {built-in method torch._C._get_tracing_state}
               42064725   72.954    0.000 1249.010    0.000 utils.py:82(probs_to_logits)
              130064128 1242.192    0.000 1242.192    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              126194175 1178.806    0.000 1178.806    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
              126530691 1166.623    0.000 1166.623    0.000 {built-in method rsub}
              126362433 1114.397    0.000 1114.397    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
               18508479   46.828    0.000 1064.255    0.000 tensor.py:575(__iter__)
               84297708 1058.177    0.000 1058.177    0.000 {method 'max' of 'torch._C._TensorBase' objects}
             6967001172 1022.177    0.000 1035.481    0.000 {built-in method builtins.len}
               42064725  208.850    0.000 1020.476    0.000 utils.py:11(broadcast_all)
               18508479  988.019    0.000  988.019    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
              126194175  914.922    0.000  914.922    0.000 {method 'all' of 'torch._C._TensorBase' objects}
             6346907016  862.371    0.000  862.371    0.000 {method 'values' of 'collections.OrderedDict' objects}
               42064725  146.166    0.000  788.281    0.000 utils.py:77(clamp_probs)
               42064725  767.166    0.000  767.166    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               42064725  147.797    0.000  745.345    0.000 layers.py:838(isFree)
               84129450  733.828    0.000  733.828    0.000 {built-in method broadcast_tensors}
               21873670  404.657    0.000  659.627    0.000 layer.py:159(update)
               42064725  642.115    0.000  642.115    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
                1682589   71.616    0.000  616.790    0.000 replaybuffer.py:34(save_option_critic)
               42064725  612.383    0.000  612.383    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
              448364841  468.769    0.000  597.548    0.000 layer.py:103(isFree)
               11278019  270.491    0.000  587.561    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               42064725  415.142    0.000  573.001    0.000 layers.py:471(check)
              126698949  549.091    0.000  549.091    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               42741043  529.381    0.000  529.381    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               42064725  526.282    0.000  526.282    0.000 {built-in method bernoulli}
               23556228  513.195    0.000  513.195    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               84129450  506.581    0.000  506.581    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               42064725  502.999    0.000  502.999    0.000 {built-in method clamp}
                1682589   87.689    0.000  502.276    0.000 optimizer.py:189(zero_grad)
              126194200  136.570    0.000  474.648    0.000 {built-in method builtins.all}
             1283433021  323.681    0.000  466.984    0.000 enum.py:646(__hash__)
              252724866  459.442    0.000  459.442    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               42064725  399.466    0.000  399.466    0.000 {built-in method all}
               23556228  394.089    0.000  394.089    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               42064725  290.439    0.000  393.835    0.000 layers.py:77(check)
               42064725  387.774    0.000  387.774    0.000 {built-in method log}
               41388408   78.818    0.000  380.106    0.000 {built-in method builtins.any}
               42064725  366.700    0.000  366.700    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
               10600312  348.247    0.000  348.247    0.000 {built-in method tensor}
                 168258  270.341    0.002  346.803    0.002 replaybuffer.py:42(sample_option_critic)
              553931803  217.963    0.000  329.805    0.000 {built-in method builtins.isinstance}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9607856: <Attempt3_SuperLevel1_option_critic_1> in cluster <dcc> Done

Job <Attempt3_SuperLevel1_option_critic_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon May  3 13:31:25 2021
Job was executed on host(s) <n-62-21-101>, in queue <hpc>, as user <s183914> in cluster <dcc> at Mon May  3 13:31:27 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon May  3 13:31:27 2021
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

    CPU time :                                   258905.28 sec.
    Max Memory :                                 1319 MB
    Average Memory :                             1302.13 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15065.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   259010 sec.
    Turnaround time :                            258908 sec.

The output (if any) is above this job summary.

