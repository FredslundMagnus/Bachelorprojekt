
# Parameters

    Name :                      Attempt2_Lights2_option_critic-1
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


      47685865502 function calls (46198925933 primitive calls) in 258900.65 seconds

##    Ordered by: cumulative time
   List reduced from 439 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.651 258900.651 {built-in method builtins.exec}
                      1    0.329    0.329 258900.651 258900.651 <string>:1(<module>)
                      1 5420.750 5420.750 258900.322 258900.322 optionCritic.py:195(option_critic_run)
               52878350 9208.430    0.000 111156.512    0.002 optionCritic.py:143(actor_loss_fn)
        1963519616/483454604 10079.460    0.000 110853.788    0.000 module.py:866(_call_impl)
              164451668  854.741    0.000 103209.932    0.001 optionCritic.py:70(get_state)
              164451668 2134.000    0.000 99835.795    0.001 container.py:117(forward)
                2115134   18.442    0.000 74602.824    0.035 tensor.py:195(backward)
                2115134   21.674    0.000 74584.053    0.035 __init__.py:68(backward)
                2115134 74510.958    0.035 74510.958    0.035 {method 'run_backward' of 'torch._C._EngineBase' objects}
              328903336 1002.872    0.000 63907.257    0.000 conv.py:398(forward)
              328903336  523.091    0.000 62509.718    0.000 conv.py:390(_conv_forward)
              328903336 61986.627    0.000 61986.627    0.000 {built-in method conv2d}
               52878350 3479.073    0.000 20712.328    0.000 optionCritic.py:91(get_action)
              647906272 1683.666    0.000 20441.853    0.000 linear.py:93(forward)
              647906272  647.988    0.000 18070.249    0.000 functional.py:1737(linear)
              647906272 17268.872    0.000 17268.872    0.000 {built-in method torch._C._nn.linear}
               52878350 1183.803    0.000 14277.793    0.000 optionCritic.py:80(predict_option_termination)
                2115134   46.253    0.000 10099.776    0.005 optimizer.py:84(wrapper)
                2115134   26.198    0.000 9923.261    0.005 grad_mode.py:24(decorate_context)
                2115134  136.905    0.000 9849.756    0.005 rmsprop.py:56(step)
                2115134  129.802    0.000 9554.367    0.005 _functional.py:203(rmsprop)
              105756700 1265.025    0.000 8203.861    0.000 distribution.py:34(__init__)
              493355004  556.016    0.000 7098.536    0.000 activation.py:713(forward)
               52878350  579.942    0.000 6930.742    0.000 categorical.py:115(log_prob)
              493355004  513.476    0.000 6542.520    0.000 functional.py:1364(leaky_relu)
              493355004 5920.074    0.000 5920.074    0.000 {built-in method torch._C._nn.leaky_relu}
               52878350  768.883    0.000 5805.615    0.000 categorical.py:49(__init__)
               52878350  447.221    0.000 5787.516    0.000 bernoulli.py:34(__init__)
              159839103  381.450    0.000 5577.920    0.000 optionCritic.py:77(get_Q)
               29611870 5079.285    0.000 5079.285    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                2115134   11.734    0.000 4992.530    0.002 game.py:42(step)
                 528783   89.836    0.000 4964.747    0.009 optionCritic.py:116(critic_loss_fn)
                2115134   21.584    0.000 4835.658    0.002 layers.py:827(step)
              106285483  394.531    0.000 4359.633    0.000 optionCritic.py:88(get_terminations)
               52878350 2382.172    0.000 3537.374    0.000 constraints.py:398(check)
               29611870 3357.823    0.000 3357.823    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                2115134   84.915    0.000 3336.494    0.002 layers.py:17(step)
               52878350  252.059    0.000 3244.031    0.000 layer.py:106(move)
               52878350  498.392    0.000 2829.382    0.000 distribution.py:240(_validate_sample)
               52878350 2180.949    0.000 2180.949    0.000 constraints.py:364(check)
               52878350  424.673    0.000 2107.322    0.000 bernoulli.py:86(sample)
              164451668  213.699    0.000 2026.907    0.000 activation.py:101(forward)
               52878350  386.555    0.000 1978.334    0.000 layers.py:844(check)
               52878350  999.516    0.000 1916.983    0.000 categorical.py:123(entropy)
               52878350 1813.994    0.000 1813.994    0.000 constraints.py:249(check)
              164451668  196.140    0.000 1813.207    0.000 functional.py:1195(relu)
             2543105543 1799.173    0.000 1799.353    0.000 module.py:934(__getattr__)
              158635050  242.671    0.000 1747.486    0.000 utils.py:106(__get__)
              370148450 1703.272    0.000 1703.272    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              164451668  166.447    0.000 1591.284    0.000 flatten.py:39(forward)
              164451668 1588.122    0.000 1588.122    0.000 {built-in method relu}
              159692616  200.710    0.000 1559.658    0.000 tensor.py:525(__rsub__)
              105756700  542.313    0.000 1523.183    0.000 functional.py:46(broadcast_tensors)
                2115135  196.348    0.000 1469.849    0.001 layers.py:793(update)
              164451668 1424.836    0.000 1424.836    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               52878350  370.374    0.000 1340.852    0.000 categorical.py:108(sample)
              159692616 1329.608    0.000 1329.608    0.000 {built-in method rsub}
               52878350   72.524    0.000 1319.547    0.000 categorical.py:88(logits)
               23266474   58.846    0.000 1316.648    0.000 tensor.py:575(__iter__)
               52878350  280.404    0.000 1310.504    0.000 utils.py:11(broadcast_all)
             1986786090 1304.273    0.000 1304.273    0.000 {built-in method torch._C._get_tracing_state}
              106285483 1293.872    0.000 1293.872    0.000 {method 'max' of 'torch._C._TensorBase' objects}
               52878350   73.874    0.000 1247.023    0.000 utils.py:82(probs_to_logits)
               23266474 1222.181    0.000 1222.181    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
              159163833 1220.306    0.000 1220.306    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
              158635050 1207.765    0.000 1207.765    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
             8643154604 1177.679    0.000 1194.532    0.000 {built-in method builtins.len}
                 528783  884.859    0.002 1111.493    0.002 replaybuffer.py:42(sample_option_critic)
              158635050 1049.485    0.000 1049.485    0.000 {method 'all' of 'torch._C._TensorBase' objects}
             8018530132  996.490    0.000  996.490    0.000 {method 'values' of 'collections.OrderedDict' objects}
               52878350  904.760    0.000  904.760    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               52878350  168.600    0.000  850.983    0.000 layers.py:838(isFree)
              105756700  820.217    0.000  820.217    0.000 {built-in method broadcast_tensors}
                2115134   86.744    0.000  751.133    0.000 replaybuffer.py:34(save_option_critic)
               52878350  150.020    0.000  734.074    0.000 utils.py:77(clamp_probs)
              508143088  552.028    0.000  682.384    0.000 layer.py:103(isFree)
              160221399  658.528    0.000  658.528    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
                2115134  107.744    0.000  635.287    0.000 optimizer.py:189(zero_grad)
               52878350  628.347    0.000  628.347    0.000 {built-in method bernoulli}
               21151350  369.593    0.000  612.452    0.000 layer.py:159(update)
               52878350  592.186    0.000  592.186    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
               52878350  584.053    0.000  584.053    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
               53024837  541.543    0.000  541.543    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
              318327666  536.799    0.000  536.799    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
              105756700  501.476    0.000  501.476    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               52878350  478.956    0.000  478.956    0.000 {built-in method clamp}
               14277157  466.268    0.000  466.268    0.000 {built-in method tensor}
               52878350  439.075    0.000  439.075    0.000 {built-in method log}
              698909321  271.047    0.000  436.607    0.000 {built-in method builtins.isinstance}
               52878350  414.410    0.000  414.410    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
               52878350  391.379    0.000  391.379    0.000 {built-in method all}
              980933769  264.045    0.000  387.199    0.000 enum.py:646(__hash__)
               29611870  379.205    0.000  379.205    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                6345406   12.731    0.000  363.836    0.000 game.py:38(board)
              164451682  359.331    0.000  359.331    0.000 {method 'to' of 'torch._C._TensorBase' objects}
              158635075  113.695    0.000  359.275    0.000 {built-in method builtins.all}
               52731864   83.078    0.000  353.136    0.000 {built-in method builtins.any}
               52878350  339.917    0.000  339.917    0.000 {built-in method multinomial}
               29611870  334.564    0.000  334.564    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9606114: <Attempt2_Lights2_option_critic_1> in cluster <dcc> Done

Job <Attempt2_Lights2_option_critic_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon May  3 01:33:07 2021
Job was executed on host(s) <n-62-31-1>, in queue <hpc>, as user <s183914> in cluster <dcc> at Mon May  3 01:33:08 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon May  3 01:33:08 2021
Terminated at Thu May  6 01:28:28 2021
Results reported at Thu May  6 01:28:28 2021

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

    CPU time :                                   258291.25 sec.
    Max Memory :                                 1050 MB
    Average Memory :                             1036.09 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15334.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258952 sec.
    Turnaround time :                            258921 sec.

The output (if any) is above this job summary.

