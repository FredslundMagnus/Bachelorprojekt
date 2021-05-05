
# Parameters

    Name :                      Attempt2_Diamonds1_option_critic-1
    Main :                      option_critic_run
    Level :                     Levels.Causal2
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


      48819663526 function calls (47252868755 primitive calls) in 258900.78 seconds

##    Ordered by: cumulative time
   List reduced from 427 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.778 258900.778 {built-in method builtins.exec}
                      1    0.369    0.369 258900.778 258900.778 <string>:1(<module>)
                      1 6209.822 6209.822 258900.409 258900.409 optionCritic.py:195(option_critic_run)
               55718150 9840.720    0.000 114733.901    0.002 optionCritic.py:143(actor_loss_fn)
        2069284863/509733849 10213.564    0.000 113004.510    0.000 module.py:866(_call_impl)
              173283446  854.781    0.000 105254.742    0.001 optionCritic.py:70(get_state)
              173283446 2271.749    0.000 101860.898    0.001 container.py:117(forward)
                2228726   19.637    0.000 72473.331    0.033 tensor.py:195(backward)
                2228726   25.452    0.000 72453.384    0.033 __init__.py:68(backward)
                2228726 72374.568    0.032 72374.568    0.032 {method 'run_backward' of 'torch._C._EngineBase' objects}
              346566892  978.934    0.000 63304.834    0.000 conv.py:398(forward)
              346566892  545.544    0.000 61854.574    0.000 conv.py:390(_conv_forward)
              346566892 61309.030    0.000 61309.030    0.000 {built-in method conv2d}
              683017295 1654.710    0.000 22269.750    0.000 linear.py:93(forward)
               55718150 3411.461    0.000 20050.029    0.000 optionCritic.py:91(get_action)
              683017295  664.740    0.000 19899.125    0.000 functional.py:1737(linear)
              683017295 19081.971    0.000 19081.971    0.000 {built-in method torch._C._nn.linear}
               55718150 1324.758    0.000 15614.013    0.000 optionCritic.py:80(predict_option_termination)
                2228726   51.579    0.000 8386.137    0.004 optimizer.py:84(wrapper)
              111436300 1353.425    0.000 8283.759    0.000 distribution.py:34(__init__)
                2228726   29.542    0.000 8195.693    0.004 grad_mode.py:24(decorate_context)
                2228726  129.459    0.000 8110.785    0.004 rmsprop.py:56(step)
                2228726  136.500    0.000 7837.655    0.004 _functional.py:203(rmsprop)
              519850338  549.155    0.000 7584.996    0.000 activation.py:713(forward)
              519850338  535.018    0.000 7035.841    0.000 functional.py:1364(leaky_relu)
               55718150  563.348    0.000 6686.140    0.000 categorical.py:115(log_prob)
               55718150  544.923    0.000 6539.621    0.000 bernoulli.py:34(__init__)
              519850338 6377.293    0.000 6377.293    0.000 {built-in method torch._C._nn.leaky_relu}
              168738772  377.049    0.000 5627.701    0.000 optionCritic.py:77(get_Q)
               55718150  762.805    0.000 5609.895    0.000 categorical.py:49(__init__)
                 557181   98.267    0.000 4754.523    0.009 optionCritic.py:116(critic_loss_fn)
              111993481  417.001    0.000 4558.147    0.000 optionCritic.py:88(get_terminations)
               31202158 3927.884    0.000 3927.884    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                2228726   13.464    0.000 3542.105    0.002 game.py:42(step)
               55718150 2318.744    0.000 3428.859    0.000 constraints.py:398(check)
                2228726   22.979    0.000 3405.384    0.002 layers.py:827(step)
               55718150  475.032    0.000 2709.473    0.000 distribution.py:240(_validate_sample)
               31202158 2708.686    0.000 2708.686    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               55718150  533.849    0.000 2421.514    0.000 bernoulli.py:86(sample)
               55718150 2291.158    0.000 2291.158    0.000 constraints.py:364(check)
              173283446  235.375    0.000 2123.189    0.000 activation.py:101(forward)
                2228726   83.459    0.000 1942.765    0.001 layers.py:17(step)
             2680628314 1911.086    0.000 1911.252    0.000 module.py:934(__getattr__)
              173283446  190.851    0.000 1887.814    0.000 functional.py:1195(relu)
               55718150  139.643    0.000 1851.975    0.000 layer.py:106(move)
               55718150  975.248    0.000 1851.673    0.000 categorical.py:123(entropy)
              390027050 1819.856    0.000 1819.856    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               55718150 1755.652    0.000 1755.652    0.000 constraints.py:249(check)
              173283446  235.091    0.000 1731.281    0.000 flatten.py:39(forward)
              167154450  246.063    0.000 1685.225    0.000 utils.py:106(__get__)
              173283446 1666.996    0.000 1666.996    0.000 {built-in method relu}
              111436300  591.648    0.000 1659.069    0.000 functional.py:46(broadcast_tensors)
              168268812  212.173    0.000 1658.482    0.000 tensor.py:525(__rsub__)
               55718150  368.084    0.000 1617.067    0.000 utils.py:11(broadcast_all)
              173283446 1496.190    0.000 1496.190    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               24515986   59.456    0.000 1446.152    0.000 tensor.py:575(__iter__)
                2228727  188.341    0.000 1431.551    0.001 layers.py:793(update)
              168268812 1415.965    0.000 1415.965    0.000 {built-in method rsub}
               24515986 1352.532    0.000 1352.532    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
              111993481 1350.729    0.000 1350.729    0.000 {method 'max' of 'torch._C._TensorBase' objects}
               55718150  367.963    0.000 1315.408    0.000 categorical.py:108(sample)
              167711631 1308.365    0.000 1308.365    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
                 557181 1068.333    0.002 1296.466    0.002 replaybuffer.py:42(sample_option_critic)
               55718150   66.825    0.000 1265.550    0.000 categorical.py:88(logits)
             2093800849 1262.863    0.000 1262.863    0.000 {built-in method torch._C._get_tracing_state}
               55718150   73.299    0.000 1198.725    0.000 utils.py:82(probs_to_logits)
              167154450 1153.586    0.000 1153.586    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
             8949410913 1127.586    0.000 1146.683    0.000 {built-in method builtins.len}
               55718150  240.357    0.000 1080.542    0.000 layers.py:844(check)
              167154450 1026.396    0.000 1026.396    0.000 {method 'all' of 'torch._C._TensorBase' objects}
             8450422898  999.582    0.000  999.582    0.000 {method 'values' of 'collections.OrderedDict' objects}
              111436300  889.570    0.000  889.570    0.000 {built-in method broadcast_tensors}
               55718150  857.058    0.000  857.058    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
                2228726   85.292    0.000  749.598    0.000 replaybuffer.py:34(save_option_critic)
               55718150  149.277    0.000  690.000    0.000 utils.py:77(clamp_probs)
              168825993  683.050    0.000  683.050    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               55718150  680.205    0.000  680.205    0.000 {built-in method bernoulli}
                2228726  105.703    0.000  671.775    0.000 optimizer.py:189(zero_grad)
               55718150  579.819    0.000  579.819    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
              335423262  557.006    0.000  557.006    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               56188110  554.213    0.000  554.213    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               55718150  540.722    0.000  540.722    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
              735826051  326.665    0.000  516.309    0.000 {built-in method builtins.isinstance}
               55718150  113.981    0.000  511.224    0.000 layers.py:838(isFree)
              167154475  144.369    0.000  492.032    0.000 {built-in method builtins.all}
              111436300  491.295    0.000  491.295    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
              167628890  490.322    0.000  490.322    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               55718150  465.186    0.000  465.186    0.000 {built-in method clamp}
               55718150  435.427    0.000  435.427    0.000 {built-in method log}
               31202158  431.216    0.000  431.216    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               15043903  427.569    0.000  427.569    0.000 {built-in method tensor}
               15601089  257.690    0.000  425.918    0.000 layer.py:175(NoRock_update)
               55718150  407.798    0.000  407.798    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
               57946902  205.907    0.000  404.769    0.000 grad_mode.py:119(__enter__)
              374466184  333.318    0.000  397.243    0.000 layer.py:103(isFree)
              173283460  380.458    0.000  380.458    0.000 {method 'to' of 'torch._C._TensorBase' objects}
               31202158  374.132    0.000  374.132    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               55718150  369.063    0.000  369.063    0.000 {built-in method all}
               55718150  340.619    0.000  340.619    0.000 {built-in method multinomial}
                6686182   13.932    0.000  325.763    0.000 game.py:38(board)


Traceback (most recent call last):
  File "main.py", line 239, in <module>
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
Subject: Job 9606117: <Attempt2_Diamonds1_option_critic_1> in cluster <dcc> Exited

Job <Attempt2_Diamonds1_option_critic_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon May  3 01:33:08 2021
Job was executed on host(s) <n-62-11-67>, in queue <hpc>, as user <s183914> in cluster <dcc> at Mon May  3 01:33:09 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon May  3 01:33:09 2021
Terminated at Thu May  6 01:28:26 2021
Results reported at Thu May  6 01:28:26 2021

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

    CPU time :                                   258277.42 sec.
    Max Memory :                                 870 MB
    Average Memory :                             856.97 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15514.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258942 sec.
    Turnaround time :                            258919 sec.

The output (if any) is above this job summary.

