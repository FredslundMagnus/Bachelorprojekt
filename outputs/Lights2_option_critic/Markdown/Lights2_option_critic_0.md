
# Parameters

    Name :                      Lights2_option_critic-0
    Main :                      option_critic_run
    Level :                     Levels.Causal4
    Failed actions chance :     0.0
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


      58650277431 function calls (56900768423 primitive calls) in 258900.61 seconds

##    Ordered by: cumulative time
   List reduced from 439 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.608 258900.608 {built-in method builtins.exec}
                      1    0.281    0.281 258900.608 258900.608 <string>:1(<module>)
                      1 5508.918 5508.918 258900.327 258900.327 optionCritic.py:195(option_critic_run)
               62215800 8874.810    0.000 108889.066    0.002 optionCritic.py:143(actor_loss_fn)
        2312505055/571084804 9892.435    0.000 108801.396    0.000 module.py:866(_call_impl)
              193491139  792.206    0.000 101325.064    0.001 optionCritic.py:70(get_state)
              193491139 2253.565    0.000 98070.459    0.001 container.py:117(forward)
                2488632   18.725    0.000 78690.848    0.032 tensor.py:195(backward)
                2488632   22.811    0.000 78671.800    0.032 __init__.py:68(backward)
                2488632 78598.918    0.032 78598.918    0.032 {method 'run_backward' of 'torch._C._EngineBase' objects}
              386982278  952.160    0.000 62586.911    0.000 conv.py:398(forward)
              386982278  603.740    0.000 61259.288    0.000 conv.py:390(_conv_forward)
              386982278 60655.549    0.000 60655.549    0.000 {built-in method conv2d}
               62215800 3676.937    0.000 21500.573    0.000 optionCritic.py:91(get_action)
              764575943 1645.644    0.000 19657.074    0.000 linear.py:93(forward)
              764575943  663.766    0.000 17354.509    0.000 functional.py:1737(linear)
              764575943 16536.286    0.000 16536.286    0.000 {built-in method torch._C._nn.linear}
               62215800 1135.125    0.000 13010.052    0.000 optionCritic.py:80(predict_option_termination)
              124431600 1187.626    0.000 7860.619    0.000 distribution.py:34(__init__)
              580473417  523.210    0.000 7245.892    0.000 activation.py:713(forward)
               62215800  611.911    0.000 7151.506    0.000 categorical.py:115(log_prob)
                2488632   52.674    0.000 6938.979    0.003 optimizer.py:84(wrapper)
                2488632   25.917    0.000 6749.285    0.003 grad_mode.py:24(decorate_context)
              580473417  555.007    0.000 6722.682    0.000 functional.py:1364(leaky_relu)
                2488632  138.569    0.000 6674.884    0.003 rmsprop.py:56(step)
                2488632  138.126    0.000 6384.032    0.003 _functional.py:203(rmsprop)
                2488632   12.343    0.000 6199.046    0.002 game.py:41(step)
              580473417 6060.786    0.000 6060.786    0.000 {built-in method torch._C._nn.leaky_relu}
                2488632   20.082    0.000 6034.145    0.002 layers.py:718(step)
               62215800  815.895    0.000 6020.744    0.000 categorical.py:49(__init__)
              190324107  377.388    0.000 5493.238    0.000 optionCritic.py:77(get_Q)
               62215800  390.955    0.000 4948.576    0.000 bernoulli.py:34(__init__)
                 622158   86.799    0.000 4821.589    0.008 optionCritic.py:116(critic_loss_fn)
              125053758  396.016    0.000 4285.635    0.000 optionCritic.py:88(get_terminations)
               62215800 2455.321    0.000 3637.874    0.000 constraints.py:398(check)
                2488632   90.157    0.000 3229.257    0.001 layers.py:17(step)
               62215800  222.516    0.000 3130.903    0.000 layer.py:98(move)
               34840842 3049.922    0.000 3049.922    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               62215800  511.572    0.000 2873.420    0.000 distribution.py:240(_validate_sample)
                2488633  203.208    0.000 2775.929    0.001 layers.py:684(update)
              193491139  229.397    0.000 2106.120    0.000 activation.py:101(forward)
               34840842 2053.226    0.000 2053.226    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               62215800  404.917    0.000 2013.926    0.000 layers.py:735(check)
               62215800 1025.594    0.000 1974.120    0.000 categorical.py:123(entropy)
               62215800 1927.455    0.000 1927.455    0.000 constraints.py:364(check)
              193491139  232.085    0.000 1876.723    0.000 functional.py:1195(relu)
               62215800 1847.278    0.000 1847.278    0.000 constraints.py:249(check)
               62215800  353.815    0.000 1829.984    0.000 bernoulli.py:86(sample)
              186647400  246.039    0.000 1800.971    0.000 utils.py:106(__get__)
             2998956437 1779.059    0.000 1779.223    0.000 module.py:934(__getattr__)
              435510600 1626.104    0.000 1626.104    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              193491139  157.941    0.000 1617.252    0.000 flatten.py:39(forward)
              193491139 1616.479    0.000 1616.479    0.000 {built-in method relu}
              187891716  181.613    0.000 1501.365    0.000 tensor.py:525(__rsub__)
              124431600  513.277    0.000 1470.451    0.000 functional.py:46(broadcast_tensors)
              193491139 1459.311    0.000 1459.311    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               62215800  399.829    0.000 1423.288    0.000 categorical.py:108(sample)
               62215800   72.706    0.000 1364.564    0.000 categorical.py:88(logits)
               27374952   60.999    0.000 1359.511    0.000 tensor.py:575(__iter__)
               62215800   82.896    0.000 1291.858    0.000 utils.py:82(probs_to_logits)
              187891716 1291.444    0.000 1291.444    0.000 {built-in method rsub}
               27374952 1261.947    0.000 1261.947    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
             2339880007 1242.911    0.000 1242.911    0.000 {built-in method torch._C._get_tracing_state}
                 622158 1004.257    0.002 1242.023    0.002 replaybuffer.py:42(sample_option_critic)
              186647400 1240.183    0.000 1240.183    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
              187269558 1205.949    0.000 1205.949    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
              125053758 1183.157    0.000 1183.157    0.000 {method 'max' of 'torch._C._TensorBase' objects}
            10171268368 1154.438    0.000 1171.903    0.000 {built-in method builtins.len}
               62215800  218.162    0.000 1100.663    0.000 utils.py:11(broadcast_all)
                2432415   35.428    0.000 1069.654    0.000 layers.py:740(restart)
              186647400  975.271    0.000  975.271    0.000 {method 'all' of 'torch._C._TensorBase' objects}
             9443511359  946.155    0.000  946.155    0.000 {method 'values' of 'collections.OrderedDict' objects}
               62215800  896.316    0.000  896.316    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
              124431600  806.937    0.000  806.937    0.000 {built-in method broadcast_tensors}
               24886330  526.476    0.000  801.092    0.000 layer.py:151(update)
               62215800  166.227    0.000  765.196    0.000 layers.py:729(isFree)
               62215800  160.348    0.000  759.317    0.000 utils.py:77(clamp_probs)
                2488632   87.748    0.000  752.085    0.000 replaybuffer.py:34(save_option_critic)
                2432415   17.279    0.000  749.189    0.000 level.py:8(__init__)
                2488632  105.670    0.000  641.741    0.000 optimizer.py:189(zero_grad)
              188513874  631.396    0.000  631.396    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
                2432415  100.274    0.000  621.685    0.000 levels.py:199(generate)
               13279037  287.407    0.000  604.576    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
              516495896  487.893    0.000  598.969    0.000 layer.py:95(isFree)
               62215800  598.969    0.000  598.969    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
               62215800  597.260    0.000  597.260    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
               62215800  577.376    0.000  577.376    0.000 {built-in method bernoulli}
               64648191  537.668    0.000  537.668    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
              124431600  523.349    0.000  523.349    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
              374539116  508.285    0.000  508.285    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
             1521109705  347.313    0.000  506.851    0.000 enum.py:646(__hash__)
               62215800  503.843    0.000  503.843    0.000 {built-in method clamp}
               16798270  478.009    0.000  478.009    0.000 {built-in method tensor}
              186647425  125.504    0.000  455.352    0.000 {built-in method builtins.all}
               62215800  449.645    0.000  449.645    0.000 {built-in method log}
               34840842  446.373    0.000  446.373    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               62215800  426.899    0.000  426.899    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
               34840842  421.530    0.000  421.530    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                4864830   49.780    0.000  419.990    0.000 level.py:41(notUsed)
               62215800  399.299    0.000  399.299    0.000 {built-in method all}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9601854: <Lights2_option_critic_0> in cluster <dcc> Done

Job <Lights2_option_critic_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Thu Apr 29 21:41:03 2021
Job was executed on host(s) <n-62-11-69>, in queue <hpc>, as user <s183914> in cluster <dcc> at Thu Apr 29 21:41:05 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Apr 29 21:41:05 2021
Terminated at Sun May  2 21:36:11 2021
Results reported at Sun May  2 21:36:11 2021

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

python main.py $LSB_PROJECT_NAME
------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   257981.44 sec.
    Max Memory :                                 1057 MB
    Average Memory :                             1035.68 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15327.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258918 sec.
    Turnaround time :                            258908 sec.

The output (if any) is above this job summary.

