
# Parameters

    Name :                      Attempt6_Diamonds4_option_critic-1
    Main :                      option_critic_run
    Level :                     Levels.Causal7
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


      22175086151 function calls (21487473091 primitive calls) in 258900.73 seconds

##    Ordered by: cumulative time
   List reduced from 430 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.735 258900.735 {built-in method builtins.exec}
                      1    0.360    0.360 258900.735 258900.735 <string>:1(<module>)
                      1 2636.991 2636.991 258900.375 258900.375 optionCritic.py:195(option_critic_run)
                 770866    6.235    0.000 174939.773    0.227 tensor.py:195(backward)
                 770866    8.403    0.000 174933.429    0.227 __init__.py:68(backward)
                 770866 174907.385    0.227 174907.385    0.227 {method 'run_backward' of 'torch._C._EngineBase' objects}
        910691409/225584256 4342.546    0.000 52317.634    0.000 module.py:866(_call_impl)
               24667712 3694.810    0.000 51174.733    0.002 optionCritic.py:143(actor_loss_fn)
               76123017  383.095    0.000 49006.296    0.001 optionCritic.py:70(get_state)
               76123017 1000.183    0.000 47526.638    0.001 container.py:117(forward)
              152246034  397.949    0.000 29901.281    0.000 conv.py:398(forward)
              152246034  217.469    0.000 29341.408    0.000 conv.py:390(_conv_forward)
              152246034 29123.939    0.000 29123.939    0.000 {built-in method conv2d}
              301707273  693.629    0.000 10864.250    0.000 linear.py:93(forward)
              301707273  291.622    0.000 9882.608    0.000 functional.py:1737(linear)
              301707273 9524.335    0.000 9524.335    0.000 {built-in method torch._C._nn.linear}
               24667712 1452.898    0.000 8644.482    0.000 optionCritic.py:91(get_action)
               24667712  536.018    0.000 6246.690    0.000 optionCritic.py:80(predict_option_termination)
                 770866   17.843    0.000 4815.802    0.006 optimizer.py:84(wrapper)
                 770866    9.945    0.000 4747.412    0.006 grad_mode.py:24(decorate_context)
                 770866   47.481    0.000 4718.962    0.006 adam.py:55(step)
                 770866  295.095    0.000 4620.780    0.006 _functional.py:53(adam)
               49335424  553.988    0.000 3474.975    0.000 distribution.py:34(__init__)
              228369051  215.370    0.000 3103.448    0.000 activation.py:713(forward)
              228369051  231.076    0.000 2888.077    0.000 functional.py:1364(leaky_relu)
               24667712  239.672    0.000 2877.811    0.000 categorical.py:115(log_prob)
              228369051 2606.682    0.000 2606.682    0.000 {built-in method torch._C._nn.leaky_relu}
               24667712  197.721    0.000 2492.918    0.000 bernoulli.py:34(__init__)
               75265387  168.532    0.000 2457.726    0.000 optionCritic.py:77(get_Q)
               24667712  326.005    0.000 2420.646    0.000 categorical.py:49(__init__)
                 192716   32.703    0.000 2321.680    0.012 optionCritic.py:116(critic_loss_fn)
               49528140  175.432    0.000 1936.847    0.000 optionCritic.py:88(get_terminations)
                 770866    4.179    0.000 1764.662    0.002 game.py:42(step)
                 770866    7.826    0.000 1713.278    0.002 layers.py:827(step)
               24667712 1000.607    0.000 1484.334    0.000 constraints.py:398(check)
               24667712  200.401    0.000 1165.419    0.000 distribution.py:240(_validate_sample)
               21584236 1024.746    0.000 1024.746    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               24667712  197.217    0.000  935.760    0.000 bernoulli.py:86(sample)
               24667712  935.646    0.000  935.646    0.000 constraints.py:364(check)
               76123017   97.212    0.000  913.131    0.000 activation.py:101(forward)
                 770867   69.947    0.000  904.173    0.001 layers.py:793(update)
               10792118  892.377    0.000  892.377    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               76123017   88.116    0.000  815.919    0.000 functional.py:1195(relu)
             1182926571  805.685    0.000  805.742    0.000 module.py:934(__getattr__)
               24667712  418.070    0.000  801.014    0.000 categorical.py:123(entropy)
                 770866   33.734    0.000  797.584    0.001 layers.py:17(step)
               10792118  791.946    0.000  791.946    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               24667712  761.507    0.000  761.507    0.000 constraints.py:249(check)
               24667712   58.931    0.000  760.823    0.000 layer.py:106(move)
              172673984  740.993    0.000  740.993    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               74003136   95.101    0.000  720.858    0.000 utils.py:106(__get__)
               76123017  714.863    0.000  714.863    0.000 {built-in method relu}
               74388568  105.622    0.000  707.790    0.000 tensor.py:525(__rsub__)
               76123017   70.128    0.000  706.553    0.000 flatten.py:39(forward)
               49335424  232.680    0.000  647.792    0.000 functional.py:46(broadcast_tensors)
               76123017  636.425    0.000  636.425    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               74388568  589.606    0.000  589.606    0.000 {built-in method rsub}
                8479526   20.468    0.000  588.712    0.000 tensor.py:575(__iter__)
               24667712  155.602    0.000  563.110    0.000 categorical.py:108(sample)
                8479526  555.912    0.000  555.912    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               24667712  121.249    0.000  553.726    0.000 utils.py:11(broadcast_all)
               49528140  551.532    0.000  551.532    0.000 {method 'max' of 'torch._C._TensorBase' objects}
               24667712   28.309    0.000  545.040    0.000 categorical.py:88(logits)
               74195852  542.250    0.000  542.250    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
               10792118  539.037    0.000  539.037    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               10792118  538.064    0.000  538.064    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               21584236  535.139    0.000  535.139    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              919170935  530.915    0.000  530.915    0.000 {built-in method torch._C._get_tracing_state}
               24667712   30.375    0.000  516.731    0.000 utils.py:82(probs_to_logits)
               74003136  498.936    0.000  498.936    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
             3937642062  481.962    0.000  487.602    0.000 {built-in method builtins.len}
               24667712  106.231    0.000  478.135    0.000 layers.py:844(check)
                 876854   12.016    0.000  469.667    0.001 layers.py:849(restart)
                 192716  356.053    0.002  432.700    0.002 replaybuffer.py:42(sample_option_critic)
               74003136  430.635    0.000  430.635    0.000 {method 'all' of 'torch._C._TensorBase' objects}
             3718888653  426.500    0.000  426.500    0.000 {method 'values' of 'collections.OrderedDict' objects}
               24667712  384.060    0.000  384.060    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
                 876854    6.320    0.000  379.547    0.000 level.py:8(__init__)
               49335424  350.531    0.000  350.531    0.000 {built-in method broadcast_tensors}
                 876854   13.751    0.000  328.061    0.000 levels.py:456(generate)
                 770866   35.926    0.000  323.120    0.000 replaybuffer.py:34(save_option_critic)
               24667712   63.288    0.000  303.764    0.000 utils.py:77(clamp_probs)
                4208265   53.607    0.000  300.142    0.000 level.py:41(notUsed)
               24667712  284.462    0.000  284.462    0.000 {built-in method bernoulli}
               74581284  275.246    0.000  275.246    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               24667712  243.685    0.000  243.685    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
               25544531  242.065    0.000  242.065    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               24667712  240.476    0.000  240.476    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
              148391704  227.525    0.000  227.525    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                 770866   35.720    0.000  224.061    0.000 optimizer.py:189(zero_grad)
               49335424  211.693    0.000  211.693    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               24667712  203.512    0.000  203.512    0.000 {built-in method clamp}
                5396069  117.136    0.000  191.078    0.000 layer.py:175(NoRock_update)
               24667712   40.468    0.000  182.651    0.000 layers.py:838(isFree)
               24667712  182.592    0.000  182.592    0.000 {built-in method log}
              324655128  115.682    0.000  179.379    0.000 {built-in method builtins.isinstance}
               24667712  177.780    0.000  177.780    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
               74881526  175.114    0.000  175.114    0.000 {method 'item' of 'torch._C._TensorBase' objects}
              524514384  111.473    0.000  166.451    0.000 enum.py:646(__hash__)
               24667712  163.379    0.000  163.379    0.000 {built-in method all}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9624157: <Attempt6_Diamonds4_option_critic_1> in cluster <dcc> Done

Job <Attempt6_Diamonds4_option_critic_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun May  9 01:22:27 2021
Job was executed on host(s) <n-62-11-63>, in queue <hpc>, as user <s183914> in cluster <dcc> at Sun May  9 01:22:28 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun May  9 01:22:28 2021
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

    CPU time :                                   258286.20 sec.
    Max Memory :                                 861 MB
    Average Memory :                             856.47 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15523.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258957 sec.
    Turnaround time :                            258908 sec.

The output (if any) is above this job summary.

