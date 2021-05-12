
# Parameters

    Name :                      Attempt6_DoorsAndKey_option_critic-0
    Main :                      option_critic_run
    Level :                     Levels.Causal1
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
    Num :                       0
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              4315 minutes.
    Hours used :                71 hours.

# Profiling


      14167812794 function calls (13692394403 primitive calls) in 258901.18 seconds

##    Ordered by: cumulative time
   List reduced from 429 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258901.181 258901.181 {built-in method builtins.exec}
                      1    0.351    0.351 258901.181 258901.181 <string>:1(<module>)
                      1 1944.198 1944.198 258900.829 258900.829 optionCritic.py:195(option_critic_run)
                 532980    4.386    0.000 195870.075    0.367 tensor.py:195(backward)
                 532980    5.520    0.000 195865.614    0.367 __init__.py:68(backward)
                 532980 195847.019    0.367 195847.019    0.367 {method 'run_backward' of 'torch._C._EngineBase' objects}
        629131222/155445238 3075.247    0.000 40278.947    0.000 module.py:866(_call_impl)
               52631776  256.317    0.000 37955.105    0.001 optionCritic.py:70(get_state)
               17055360 2689.748    0.000 37926.399    0.002 optionCritic.py:143(actor_loss_fn)
               52631776  701.430    0.000 36944.071    0.001 container.py:117(forward)
              105263552  276.666    0.000 23863.969    0.000 conv.py:398(forward)
              105263552  159.609    0.000 23463.736    0.000 conv.py:390(_conv_forward)
              105263552 23304.127    0.000 23304.127    0.000 {built-in method conv2d}
              208077014  492.551    0.000 8260.852    0.000 linear.py:93(forward)
              208077014  198.560    0.000 7541.686    0.000 functional.py:1737(linear)
              208077014 7295.661    0.000 7295.661    0.000 {built-in method torch._C._nn.linear}
               17055360 1003.446    0.000 5960.601    0.000 optionCritic.py:91(get_action)
               17055360  403.608    0.000 4696.875    0.000 optionCritic.py:80(predict_option_termination)
                 532980   12.431    0.000 3904.287    0.007 optimizer.py:84(wrapper)
                 532980    7.358    0.000 3857.245    0.007 grad_mode.py:24(decorate_context)
                 532980   33.521    0.000 3837.311    0.007 adam.py:55(step)
                 532980  215.186    0.000 3768.464    0.007 _functional.py:53(adam)
               34110720  414.148    0.000 2527.533    0.000 distribution.py:34(__init__)
                 133245   23.812    0.000 2268.571    0.017 optionCritic.py:116(critic_loss_fn)
              157895328  162.964    0.000 2202.882    0.000 activation.py:713(forward)
              157895328  165.678    0.000 2039.918    0.000 functional.py:1364(leaky_relu)
               17055360  165.945    0.000 1980.905    0.000 categorical.py:115(log_prob)
               17055360  162.259    0.000 1965.465    0.000 bernoulli.py:34(__init__)
              157895328 1840.341    0.000 1840.341    0.000 {built-in method torch._C._nn.leaky_relu}
               51514137  118.909    0.000 1698.207    0.000 optionCritic.py:77(get_Q)
               17055360  226.461    0.000 1668.768    0.000 categorical.py:49(__init__)
               34243965  127.779    0.000 1363.163    0.000 optionCritic.py:88(get_terminations)
               17055360  689.017    0.000 1020.739    0.000 constraints.py:398(check)
               14923428  823.395    0.000  823.395    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                 532980    2.783    0.000  816.501    0.002 game.py:42(step)
               17055360  139.630    0.000  805.812    0.000 distribution.py:240(_validate_sample)
                 532980    5.160    0.000  780.557    0.001 layers.py:827(step)
                7461714  753.216    0.000  753.216    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               17055360  168.962    0.000  734.736    0.000 bernoulli.py:86(sample)
               17055360  718.270    0.000  718.270    0.000 constraints.py:364(check)
                7461714  649.797    0.000  649.797    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               52631776   71.251    0.000  638.123    0.000 activation.py:101(forward)
              816306427  578.127    0.000  578.168    0.000 module.py:934(__getattr__)
               52631776   63.813    0.000  566.871    0.000 functional.py:1195(relu)
               17055360  290.527    0.000  554.619    0.000 categorical.py:123(entropy)
              119387520  545.331    0.000  545.331    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               17055360  524.936    0.000  524.936    0.000 constraints.py:249(check)
               51432570   66.429    0.000  507.362    0.000 tensor.py:525(__rsub__)
               52631776   63.179    0.000  506.635    0.000 flatten.py:39(forward)
               51166080   68.867    0.000  496.999    0.000 utils.py:106(__get__)
               52631776  493.845    0.000  493.845    0.000 {built-in method relu}
               34110720  174.704    0.000  481.485    0.000 functional.py:46(broadcast_tensors)
               17055360  100.460    0.000  454.872    0.000 utils.py:11(broadcast_all)
                 532980   23.691    0.000  454.230    0.001 layers.py:17(step)
                7461714  453.290    0.000  453.290    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               52631776  443.456    0.000  443.456    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               14923428  439.399    0.000  439.399    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               51432570  431.735    0.000  431.735    0.000 {built-in method rsub}
                7461714  431.008    0.000  431.008    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               17055360   43.034    0.000  428.272    0.000 layer.py:106(move)
                5862780   14.968    0.000  423.528    0.000 tensor.py:575(__iter__)
               34243965  408.106    0.000  408.106    0.000 {method 'max' of 'torch._C._TensorBase' objects}
                5862780  399.910    0.000  399.910    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               17055360  105.225    0.000  388.458    0.000 categorical.py:108(sample)
               51299325  383.397    0.000  383.397    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
               17055360   19.885    0.000  376.590    0.000 categorical.py:88(logits)
              634994002  372.936    0.000  372.936    0.000 {built-in method torch._C._get_tracing_state}
               17055360   20.930    0.000  356.705    0.000 utils.py:82(probs_to_logits)
               51166080  347.689    0.000  347.689    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
             2700604553  334.347    0.000  338.060    0.000 {built-in method builtins.len}
                 532981   48.940    0.000  318.450    0.001 layers.py:793(update)
               51166080  318.008    0.000  318.008    0.000 {method 'all' of 'torch._C._TensorBase' objects}
                 133245  250.455    0.002  304.858    0.002 replaybuffer.py:42(sample_option_critic)
             2569156664  286.991    0.000  286.991    0.000 {method 'values' of 'collections.OrderedDict' objects}
               17055360  267.968    0.000  267.968    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               34110720  255.648    0.000  255.648    0.000 {built-in method broadcast_tensors}
                 532980   25.557    0.000  226.186    0.000 replaybuffer.py:34(save_option_critic)
               17055360   43.822    0.000  211.627    0.000 utils.py:77(clamp_probs)
               17055360  206.753    0.000  206.753    0.000 {built-in method bernoulli}
               51565815  198.269    0.000  198.269    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               17055360   59.709    0.000  197.614    0.000 layers.py:844(check)
               17055360  167.967    0.000  167.967    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
               17055360  167.805    0.000  167.805    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
              102598650  164.971    0.000  164.971    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               17136927  156.454    0.000  156.454    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                 532980   26.162    0.000  154.682    0.000 optimizer.py:189(zero_grad)
               17055360   28.723    0.000  149.818    0.000 layers.py:838(isFree)
               34110720  147.087    0.000  147.087    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               17055360  140.499    0.000  140.499    0.000 {built-in method clamp}
               51248742  137.104    0.000  137.104    0.000 {method 'item' of 'torch._C._TensorBase' objects}
              224468110   87.164    0.000  136.502    0.000 {built-in method builtins.isinstance}
               17055360  124.148    0.000  124.148    0.000 {built-in method log}
               96104434  101.787    0.000  121.094    0.000 layer.py:103(isFree)
               17055360  120.884    0.000  120.884    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
                3597619  119.672    0.000  119.672    0.000 {built-in method tensor}
               52631790  116.058    0.000  116.058    0.000 {method 'to' of 'torch._C._TensorBase' objects}
               17588366   61.254    0.000  113.608    0.000 grad_mode.py:119(__enter__)
               17055360  110.347    0.000  110.347    0.000 {built-in method all}
               51166112   39.355    0.000  108.958    0.000 {built-in method builtins.all}
                3197886   64.722    0.000  107.972    0.000 layer.py:175(NoRock_update)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9624174: <Attempt6_DoorsAndKey_option_critic_0> in cluster <dcc> Done

Job <Attempt6_DoorsAndKey_option_critic_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun May  9 01:22:29 2021
Job was executed on host(s) <n-62-11-62>, in queue <hpc>, as user <s183914> in cluster <dcc> at Sun May  9 01:22:30 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun May  9 01:22:30 2021
Terminated at Wed May 12 01:17:34 2021
Results reported at Wed May 12 01:17:34 2021

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

    CPU time :                                   258288.53 sec.
    Max Memory :                                 788 MB
    Average Memory :                             782.40 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15596.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258956 sec.
    Turnaround time :                            258905 sec.

The output (if any) is above this job summary.

