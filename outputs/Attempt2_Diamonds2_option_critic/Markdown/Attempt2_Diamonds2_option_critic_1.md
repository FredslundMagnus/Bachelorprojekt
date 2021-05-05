
# Parameters

    Name :                      Attempt2_Diamonds2_option_critic-1
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


      49123422946 function calls (47625638970 primitive calls) in 258900.83 seconds

##    Ordered by: cumulative time
   List reduced from 429 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.829 258900.829 {built-in method builtins.exec}
                      1    0.372    0.372 258900.829 258900.829 <string>:1(<module>)
                      1 5941.776 5941.776 258900.457 258900.457 optionCritic.py:195(option_critic_run)
               53264000 9451.566    0.000 111359.086    0.002 optionCritic.py:143(actor_loss_fn)
        1978735487/487876118 9930.201    0.000 110384.214    0.000 module.py:866(_call_impl)
              165651041  805.256    0.000 102989.360    0.001 optionCritic.py:70(get_state)
              165651041 2207.743    0.000 99759.879    0.001 container.py:117(forward)
                2130560   18.811    0.000 76985.829    0.036 tensor.py:195(backward)
                2130560   22.437    0.000 76966.721    0.036 __init__.py:68(backward)
                2130560 76891.308    0.036 76891.308    0.036 {method 'run_backward' of 'torch._C._EngineBase' objects}
              331302082  966.017    0.000 62700.801    0.000 conv.py:398(forward)
              331302082  590.160    0.000 61334.175    0.000 conv.py:390(_conv_forward)
              331302082 60744.015    0.000 60744.015    0.000 {built-in method conv2d}
              653527159 1516.921    0.000 21325.864    0.000 linear.py:93(forward)
               53264000 3267.455    0.000 19205.484    0.000 optionCritic.py:91(get_action)
              653527159  628.515    0.000 19123.321    0.000 functional.py:1737(linear)
              653527159 18352.144    0.000 18352.144    0.000 {built-in method torch._C._nn.linear}
               53264000 1240.959    0.000 14890.881    0.000 optionCritic.py:80(predict_option_termination)
                2130560   53.136    0.000 8143.381    0.004 optimizer.py:84(wrapper)
              106528000 1340.394    0.000 8037.244    0.000 distribution.py:34(__init__)
                2130560   29.212    0.000 7954.073    0.004 grad_mode.py:24(decorate_context)
                2130560  124.469    0.000 7873.945    0.004 rmsprop.py:56(step)
                2130560  132.710    0.000 7608.577    0.004 _functional.py:203(rmsprop)
              496953123  550.424    0.000 7243.262    0.000 activation.py:713(forward)
              496953123  535.869    0.000 6692.838    0.000 functional.py:1364(leaky_relu)
               53264000  533.410    0.000 6381.864    0.000 categorical.py:115(log_prob)
               53264000  513.701    0.000 6343.384    0.000 bernoulli.py:34(__init__)
              496953123 6050.882    0.000 6050.882    0.000 {built-in method torch._C._nn.leaky_relu}
               53264000  728.869    0.000 5406.317    0.000 categorical.py:49(__init__)
              161900437  364.071    0.000 5384.805    0.000 optionCritic.py:77(get_Q)
                 532640   93.367    0.000 4835.432    0.009 optionCritic.py:116(critic_loss_fn)
                2130560   12.879    0.000 4384.576    0.002 game.py:42(step)
              107060640  391.230    0.000 4353.007    0.000 optionCritic.py:88(get_terminations)
                2130560   21.727    0.000 4239.324    0.002 layers.py:827(step)
               29827834 3784.544    0.000 3784.544    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               53264000 2229.408    0.000 3296.931    0.000 constraints.py:398(check)
               53264000  454.600    0.000 2621.388    0.000 distribution.py:240(_validate_sample)
               29827834 2602.713    0.000 2602.713    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                2130560   80.858    0.000 2318.640    0.001 layers.py:17(step)
               53264000  490.032    0.000 2237.407    0.000 bernoulli.py:86(sample)
               53264000 2232.539    0.000 2232.539    0.000 constraints.py:364(check)
               53264000  142.502    0.000 2231.016    0.000 layer.py:106(move)
              165651041  219.080    0.000 2016.929    0.000 activation.py:101(forward)
                2130561  183.418    0.000 1891.020    0.001 layers.py:793(update)
             2564339625 1834.908    0.000 1835.067    0.000 module.py:934(__getattr__)
              165651041  202.945    0.000 1797.849    0.000 functional.py:1195(relu)
               53264000  926.035    0.000 1768.403    0.000 categorical.py:123(entropy)
              372848000 1727.854    0.000 1727.854    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               53264000 1704.979    0.000 1704.979    0.000 constraints.py:249(check)
              165651041  241.261    0.000 1689.189    0.000 flatten.py:39(forward)
              159792000  225.425    0.000 1592.522    0.000 utils.py:106(__get__)
              160857280  216.502    0.000 1590.796    0.000 tensor.py:525(__rsub__)
              106528000  574.074    0.000 1585.612    0.000 functional.py:46(broadcast_tensors)
              165651041 1568.286    0.000 1568.286    0.000 {built-in method relu}
               53264000  372.412    0.000 1551.124    0.000 utils.py:11(broadcast_all)
              165651041 1447.927    0.000 1447.927    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               53264000  295.656    0.000 1432.973    0.000 layers.py:844(check)
               23436160   57.241    0.000 1377.416    0.000 tensor.py:575(__iter__)
              160857280 1345.168    0.000 1345.168    0.000 {built-in method rsub}
              107060640 1318.205    0.000 1318.205    0.000 {method 'max' of 'torch._C._TensorBase' objects}
               23436160 1286.488    0.000 1286.488    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               53264000  343.091    0.000 1242.765    0.000 categorical.py:108(sample)
                 532640 1010.606    0.002 1238.024    0.002 replaybuffer.py:42(sample_option_critic)
              160324640 1222.927    0.000 1222.927    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
             2002171647 1204.862    0.000 1204.862    0.000 {built-in method torch._C._get_tracing_state}
               53264000   64.796    0.000 1200.457    0.000 categorical.py:88(logits)
               53264000   67.528    0.000 1135.661    0.000 utils.py:82(probs_to_logits)
              159792000 1109.351    0.000 1109.351    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
             8671107381 1083.755    0.000 1100.047    0.000 {built-in method builtins.len}
              159792000  997.967    0.000  997.967    0.000 {method 'all' of 'torch._C._TensorBase' objects}
             8080592989  887.675    0.000  887.675    0.000 {method 'values' of 'collections.OrderedDict' objects}
              106528000  856.549    0.000  856.549    0.000 {built-in method broadcast_tensors}
               53264000  824.408    0.000  824.408    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
                2130560   82.833    0.000  736.136    0.000 replaybuffer.py:34(save_option_critic)
                1043181   16.956    0.000  716.684    0.001 layers.py:849(restart)
                2130560  100.697    0.000  652.833    0.000 optimizer.py:189(zero_grad)
               53264000  139.930    0.000  651.775    0.000 utils.py:77(clamp_probs)
               53264000  651.152    0.000  651.152    0.000 {built-in method bernoulli}
              161389920  639.522    0.000  639.522    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
                1043181    9.082    0.000  598.309    0.001 level.py:8(__init__)
               53264000  546.557    0.000  546.557    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
               53264000  134.296    0.000  545.971    0.000 layers.py:838(isFree)
               54307157  541.120    0.000  541.120    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                1043181   21.371    0.000  529.994    0.001 levels.py:249(generate)
              320649280  526.729    0.000  526.729    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               19175049  309.172    0.000  512.477    0.000 layer.py:175(NoRock_update)
               53264000  511.845    0.000  511.845    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
              703416166  297.118    0.000  497.077    0.000 {built-in method builtins.isinstance}
                6782352   83.705    0.000  486.605    0.000 level.py:41(notUsed)
              106528000  461.804    0.000  461.804    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
              160839441  461.026    0.000  461.026    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               29827834  452.672    0.000  452.672    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               53264000  443.071    0.000  443.071    0.000 {built-in method clamp}
               14381284  425.478    0.000  425.478    0.000 {built-in method tensor}
               53264000  416.359    0.000  416.359    0.000 {built-in method log}
              425388660  337.057    0.000  411.675    0.000 layer.py:103(isFree)
               53264000  390.554    0.000  390.554    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
               29827834  387.834    0.000  387.834    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
             1198828623  265.488    0.000  386.248    0.000 enum.py:646(__hash__)
              165651055  369.367    0.000  369.367    0.000 {method 'to' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9606120: <Attempt2_Diamonds2_option_critic_1> in cluster <dcc> Done

Job <Attempt2_Diamonds2_option_critic_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon May  3 01:33:08 2021
Job was executed on host(s) <n-62-11-67>, in queue <hpc>, as user <s183914> in cluster <dcc> at Mon May  3 01:33:09 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon May  3 01:33:09 2021
Terminated at Thu May  6 01:28:30 2021
Results reported at Thu May  6 01:28:30 2021

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

    CPU time :                                   258287.59 sec.
    Max Memory :                                 1025 MB
    Average Memory :                             1005.09 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15359.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258944 sec.
    Turnaround time :                            258922 sec.

The output (if any) is above this job summary.

