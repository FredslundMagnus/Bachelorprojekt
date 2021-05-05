
# Parameters

    Name :                      Attempt2_Maze_option_critic-0
    Main :                      option_critic_run
    Level :                     Levels.Maze
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


      50816523194 function calls (49234382737 primitive calls) in 258900.63 seconds

##    Ordered by: cumulative time
   List reduced from 438 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.625 258900.625 {built-in method builtins.exec}
                      1    0.342    0.342 258900.625 258900.625 <string>:1(<module>)
                      1 5933.661 5933.661 258900.283 258900.283 optionCritic.py:195(option_critic_run)
               56263875 10082.554    0.000 116283.755    0.002 optionCritic.py:143(actor_loss_fn)
        2089741789/514915939 10764.480    0.000 113663.351    0.000 module.py:866(_call_impl)
              174980650  892.374    0.000 105950.630    0.001 optionCritic.py:70(get_state)
              174980650 2413.365    0.000 102328.748    0.001 container.py:117(forward)
                2250555   16.740    0.000 70672.241    0.031 tensor.py:195(backward)
                2250555   21.906    0.000 70655.216    0.031 __init__.py:68(backward)
                2250555 70583.476    0.031 70583.476    0.031 {method 'run_backward' of 'torch._C._EngineBase' objects}
              349961300  975.321    0.000 63368.769    0.000 conv.py:398(forward)
              349961300  545.918    0.000 61961.135    0.000 conv.py:390(_conv_forward)
              349961300 61415.217    0.000 61415.217    0.000 {built-in method conv2d}
              689896589 1634.222    0.000 22125.506    0.000 linear.py:93(forward)
               56263875 3340.511    0.000 19782.218    0.000 optionCritic.py:91(get_action)
              689896589  680.293    0.000 19739.993    0.000 functional.py:1737(linear)
              689896589 18909.460    0.000 18909.460    0.000 {built-in method torch._C._nn.linear}
               56263875 1337.564    0.000 15968.560    0.000 optionCritic.py:80(predict_option_termination)
              112527750 1373.496    0.000 8593.637    0.000 distribution.py:34(__init__)
                2250555   48.977    0.000 8481.469    0.004 optimizer.py:84(wrapper)
                2250555   28.717    0.000 8294.979    0.004 grad_mode.py:24(decorate_context)
                2250555  122.070    0.000 8217.309    0.004 rmsprop.py:56(step)
                2250555  128.356    0.000 7954.271    0.004 _functional.py:203(rmsprop)
              524941950  583.138    0.000 7467.321    0.000 activation.py:713(forward)
               56263875  581.161    0.000 7001.592    0.000 bernoulli.py:34(__init__)
              524941950  556.424    0.000 6884.183    0.000 functional.py:1364(leaky_relu)
               56263875  560.621    0.000 6674.730    0.000 categorical.py:115(log_prob)
              524941950 6217.922    0.000 6217.922    0.000 {built-in method torch._C._nn.leaky_relu}
              170581026  391.215    0.000 5669.871    0.000 optionCritic.py:77(get_Q)
               56263875  737.481    0.000 5487.424    0.000 categorical.py:49(__init__)
                2250555   11.929    0.000 4764.910    0.002 game.py:42(step)
                 562638   97.314    0.000 4636.562    0.008 optionCritic.py:116(critic_loss_fn)
              113090388  453.028    0.000 4628.405    0.000 optionCritic.py:88(get_terminations)
                2250555   18.886    0.000 4616.781    0.002 layers.py:827(step)
               31507764 4087.352    0.000 4087.352    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               56263875 2269.915    0.000 3355.555    0.000 constraints.py:398(check)
               31507764 2803.398    0.000 2803.398    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                2250555   88.348    0.000 2757.421    0.001 layers.py:17(step)
               56263875  475.445    0.000 2737.390    0.000 distribution.py:240(_validate_sample)
               56263875  280.795    0.000 2661.407    0.000 layer.py:106(move)
               56263875 2619.173    0.000 2619.173    0.000 constraints.py:364(check)
               56263875  537.732    0.000 2369.512    0.000 bernoulli.py:86(sample)
              174980650  301.991    0.000 2197.221    0.000 activation.py:101(forward)
             2707452092 1939.065    0.000 1939.229    0.000 module.py:934(__getattr__)
              393847125 1914.891    0.000 1914.891    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              174980650  206.628    0.000 1895.231    0.000 functional.py:1195(relu)
                2250556  185.258    0.000 1833.169    0.001 layers.py:793(update)
               56263875  955.939    0.000 1828.907    0.000 categorical.py:123(entropy)
               56263875 1780.705    0.000 1780.705    0.000 constraints.py:249(check)
              112527750  605.549    0.000 1693.579    0.000 functional.py:46(broadcast_tensors)
              169916901  228.298    0.000 1687.447    0.000 tensor.py:525(__rsub__)
               56263875  281.381    0.000 1677.283    0.000 layers.py:844(check)
              174980650  189.425    0.000 1673.782    0.000 flatten.py:39(forward)
              174980650 1659.492    0.000 1659.492    0.000 {built-in method relu}
              168791625  231.495    0.000 1643.320    0.000 utils.py:106(__get__)
               56263875  371.488    0.000 1641.316    0.000 utils.py:11(broadcast_all)
              174980650 1484.357    0.000 1484.357    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              169916901 1428.231    0.000 1428.231    0.000 {built-in method rsub}
              113090388 1374.638    0.000 1374.638    0.000 {method 'max' of 'torch._C._TensorBase' objects}
               24756105   57.066    0.000 1350.459    0.000 tensor.py:575(__iter__)
             2114497894 1336.573    0.000 1336.573    0.000 {built-in method torch._C._get_tracing_state}
               56263875  381.449    0.000 1306.890    0.000 categorical.py:108(sample)
              169354263 1279.945    0.000 1279.945    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
               24756105 1257.267    0.000 1257.267    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               56263875   68.519    0.000 1237.908    0.000 categorical.py:88(logits)
             9016266623 1195.506    0.000 1212.676    0.000 {built-in method builtins.len}
               56263875   66.026    0.000 1169.389    0.000 utils.py:82(probs_to_logits)
              168791625 1135.395    0.000 1135.395    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 562638  888.697    0.002 1102.995    0.002 replaybuffer.py:42(sample_option_critic)
              168791625 1050.681    0.000 1050.681    0.000 {method 'all' of 'torch._C._TensorBase' objects}
             8533947806 1003.129    0.000 1003.129    0.000 {method 'values' of 'collections.OrderedDict' objects}
              112527750  899.036    0.000  899.036    0.000 {built-in method broadcast_tensors}
               56263875  824.206    0.000  824.206    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
                2250555   81.955    0.000  716.088    0.000 replaybuffer.py:34(save_option_critic)
               56263875  697.904    0.000  697.904    0.000 {built-in method bernoulli}
              170479539  690.292    0.000  690.292    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               56263875  144.232    0.000  682.967    0.000 utils.py:77(clamp_probs)
                 664151    9.677    0.000  625.401    0.001 layers.py:849(restart)
                2250555  106.877    0.000  608.599    0.000 optimizer.py:189(zero_grad)
               56263875  586.547    0.000  586.547    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
              338708526  569.453    0.000  569.453    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               56263875  538.734    0.000  538.734    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
                 664151    4.922    0.000  532.544    0.001 level.py:8(__init__)
               56263875   97.392    0.000  530.144    0.000 layers.py:838(isFree)
              743032985  322.873    0.000  525.404    0.000 {built-in method builtins.isinstance}
               56928000  522.132    0.000  522.132    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               15753892  321.078    0.000  495.377    0.000 layer.py:159(update)
                 664151   33.722    0.000  490.852    0.001 levels.py:277(generate)
              169460274  482.539    0.000  482.539    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               56263875  340.807    0.000  480.158    0.000 layers.py:471(check)
              112527750  472.517    0.000  472.517    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               56263875  461.958    0.000  461.958    0.000 {built-in method clamp}
              168791650  142.510    0.000  453.429    0.000 {built-in method builtins.all}
               56263875  331.814    0.000  451.397    0.000 layers.py:77(check)
              298247235  367.374    0.000  432.752    0.000 layer.py:103(isFree)
              174980664  429.007    0.000  429.007    0.000 {method 'to' of 'torch._C._TensorBase' objects}
                5921782   70.664    0.000  427.654    0.000 level.py:41(notUsed)
               56263875  420.396    0.000  420.396    0.000 {built-in method log}
               15191248  416.935    0.000  416.935    0.000 {built-in method tensor}
               56263875  393.300    0.000  393.300    0.000 {method 'abs' of 'torch._C._TensorBase' objects}


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
Subject: Job 9606134: <Attempt2_Maze_option_critic_0> in cluster <dcc> Exited

Job <Attempt2_Maze_option_critic_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon May  3 01:33:11 2021
Job was executed on host(s) <n-62-11-69>, in queue <hpc>, as user <s183914> in cluster <dcc> at Mon May  3 01:33:12 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon May  3 01:33:12 2021
Terminated at Thu May  6 01:28:32 2021
Results reported at Thu May  6 01:28:32 2021

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

    CPU time :                                   258287.52 sec.
    Max Memory :                                 909 MB
    Average Memory :                             897.68 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15475.00 MB
    Max Swap :                                   -
    Max Processes :                              6
    Max Threads :                                7
    Run time :                                   258948 sec.
    Turnaround time :                            258921 sec.

The output (if any) is above this job summary.

