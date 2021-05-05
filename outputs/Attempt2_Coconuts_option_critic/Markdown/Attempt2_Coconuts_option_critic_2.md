
# Parameters

    Name :                      Attempt2_Coconuts_option_critic-2
    Main :                      option_critic_run
    Level :                     Levels.Coconuts
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


      49847440443 function calls (48377234380 primitive calls) in 258900.63 seconds

##    Ordered by: cumulative time
   List reduced from 443 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.626 258900.626 {built-in method builtins.exec}
                      1    0.341    0.341 258900.625 258900.625 <string>:1(<module>)
                      1 5538.483 5538.483 258900.284 258900.284 optionCritic.py:195(option_critic_run)
               52283275 9329.335    0.000 113880.236    0.002 optionCritic.py:143(actor_loss_fn)
        1941424171/478015315 9841.095    0.000 113590.831    0.000 module.py:866(_call_impl)
              162600984  836.853    0.000 106334.345    0.001 optionCritic.py:70(get_state)
              162600984 2273.952    0.000 102993.359    0.001 container.py:117(forward)
                2091331   17.290    0.000 73694.718    0.035 tensor.py:195(backward)
                2091331   19.787    0.000 73677.135    0.035 __init__.py:68(backward)
                2091331 73607.929    0.035 73607.929    0.035 {method 'run_backward' of 'torch._C._EngineBase' objects}
              325201968  947.278    0.000 66235.493    0.000 conv.py:398(forward)
              325201968  550.073    0.000 64868.040    0.000 conv.py:390(_conv_forward)
              325201968 64317.968    0.000 64317.968    0.000 {built-in method conv2d}
              640616299 1572.454    0.000 21182.328    0.000 linear.py:93(forward)
              640616299  641.855    0.000 18928.521    0.000 functional.py:1737(linear)
               52283275 3119.218    0.000 18422.563    0.000 optionCritic.py:91(get_action)
              640616299 18145.839    0.000 18145.839    0.000 {built-in method torch._C._nn.linear}
               52283275 1246.322    0.000 14953.151    0.000 optionCritic.py:80(predict_option_termination)
                2091331   46.599    0.000 8807.756    0.004 optimizer.py:84(wrapper)
                2091331   25.433    0.000 8634.164    0.004 grad_mode.py:24(decorate_context)
                2091331  115.574    0.000 8563.047    0.004 rmsprop.py:56(step)
                2091331  120.636    0.000 8315.791    0.004 _functional.py:203(rmsprop)
              104566550 1281.524    0.000 7925.478    0.000 distribution.py:34(__init__)
              487802952  517.068    0.000 7123.486    0.000 activation.py:713(forward)
              487802952  556.097    0.000 6606.418    0.000 functional.py:1364(leaky_relu)
               52283275  569.224    0.000 6486.284    0.000 bernoulli.py:34(__init__)
               52283275  521.406    0.000 6182.271    0.000 categorical.py:115(log_prob)
              487802952 5935.106    0.000 5935.106    0.000 {built-in method torch._C._nn.leaky_relu}
                2091331   11.345    0.000 5715.716    0.003 game.py:42(step)
                2091331   19.498    0.000 5548.353    0.003 layers.py:827(step)
              158041674  378.293    0.000 5367.614    0.000 optionCritic.py:77(get_Q)
                 522832   91.024    0.000 5192.828    0.010 optionCritic.py:116(critic_loss_fn)
               52283275  689.162    0.000 5133.964    0.000 categorical.py:49(__init__)
               29278628 4377.409    0.000 4377.409    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              105089382  409.526    0.000 4342.098    0.000 optionCritic.py:88(get_terminations)
                2091331   80.676    0.000 4077.051    0.002 layers.py:17(step)
               52283275  280.771    0.000 3989.828    0.000 layer.py:106(move)
               52283275 2107.004    0.000 3142.885    0.000 constraints.py:398(check)
               29278628 2891.497    0.000 2891.497    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               52283275  469.895    0.000 2733.051    0.000 layers.py:844(check)
               52283275  437.614    0.000 2522.451    0.000 distribution.py:240(_validate_sample)
               52283275 2347.666    0.000 2347.666    0.000 constraints.py:364(check)
               52283275  476.670    0.000 2218.599    0.000 bernoulli.py:86(sample)
              162600984  219.281    0.000 2002.392    0.000 activation.py:101(forward)
             2514490328 1858.509    0.000 1858.661    0.000 module.py:934(__getattr__)
              162600984  197.743    0.000 1783.111    0.000 functional.py:1195(relu)
               52283275  893.379    0.000 1707.051    0.000 categorical.py:123(entropy)
               52283275 1640.358    0.000 1640.358    0.000 constraints.py:249(check)
              104566550  571.302    0.000 1595.683    0.000 functional.py:46(broadcast_tensors)
              157895489  221.056    0.000 1592.191    0.000 tensor.py:525(__rsub__)
              365982925 1588.992    0.000 1588.992    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              162600984  186.966    0.000 1582.079    0.000 flatten.py:39(forward)
              162600984 1557.593    0.000 1557.593    0.000 {built-in method relu}
               52283275  355.389    0.000 1548.942    0.000 utils.py:11(broadcast_all)
              156849825  222.582    0.000 1539.502    0.000 utils.py:106(__get__)
                2091332  176.329    0.000 1444.629    0.001 layers.py:793(update)
              162600984 1395.113    0.000 1395.113    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              157895489 1344.631    0.000 1344.631    0.000 {built-in method rsub}
              105089382 1318.750    0.000 1318.750    0.000 {method 'max' of 'torch._C._TensorBase' objects}
               23004641   55.466    0.000 1269.871    0.000 tensor.py:575(__iter__)
              157372657 1224.560    0.000 1224.560    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
               52283275  340.825    0.000 1213.831    0.000 categorical.py:108(sample)
             1964428812 1197.812    0.000 1197.812    0.000 {built-in method torch._C._get_tracing_state}
               23004641 1180.735    0.000 1180.735    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               52283275   59.697    0.000 1153.961    0.000 categorical.py:88(logits)
             8703772886 1087.774    0.000 1105.881    0.000 {built-in method builtins.len}
               52283275   62.963    0.000 1094.265    0.000 utils.py:82(probs_to_logits)
              156849825 1065.754    0.000 1065.754    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 522832  838.397    0.002 1062.043    0.002 replaybuffer.py:42(sample_option_critic)
              156849825  979.632    0.000  979.632    0.000 {method 'all' of 'torch._C._TensorBase' objects}
             7928297668  952.470    0.000  952.470    0.000 {method 'values' of 'collections.OrderedDict' objects}
              104566550  847.514    0.000  847.514    0.000 {built-in method broadcast_tensors}
               52283275  169.194    0.000  811.435    0.000 layers.py:838(isFree)
               52283275  766.632    0.000  766.632    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
                2091331   78.419    0.000  682.774    0.000 replaybuffer.py:34(save_option_critic)
               52283275  656.966    0.000  656.966    0.000 {built-in method bernoulli}
               27187316  384.882    0.000  649.523    0.000 layer.py:159(update)
               52283275  140.285    0.000  642.997    0.000 utils.py:77(clamp_probs)
              571448056  518.122    0.000  642.241    0.000 layer.py:103(isFree)
              158418321  628.275    0.000  628.275    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               52283275  433.338    0.000  592.061    0.000 layers.py:471(check)
                2091331  101.055    0.000  590.253    0.000 optimizer.py:189(zero_grad)
               52283275  535.268    0.000  535.268    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
              314745314  524.166    0.000  524.166    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               52429460  516.536    0.000  516.536    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
             1556344886  343.304    0.000  505.750    0.000 enum.py:646(__hash__)
               52283275  502.712    0.000  502.712    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
              690464797  300.345    0.000  491.741    0.000 {built-in method builtins.isinstance}
               14116486  462.518    0.000  462.518    0.000 {built-in method tensor}
              104566550  454.222    0.000  454.222    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               52283275  319.379    0.000  434.882    0.000 layers.py:77(check)
               52283275  433.254    0.000  433.254    0.000 {built-in method clamp}
              157000216  397.939    0.000  397.939    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               52283275  388.305    0.000  388.305    0.000 {built-in method log}
              162600998  381.701    0.000  381.701    0.000 {method 'to' of 'torch._C._TensorBase' objects}
               52137091   83.335    0.000  380.175    0.000 {built-in method builtins.any}
               52283275  379.812    0.000  379.812    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
               29278628  369.401    0.000  369.401    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                6273997   14.814    0.000  368.463    0.000 game.py:38(board)
              156849850  119.097    0.000  352.610    0.000 {built-in method builtins.all}


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
Subject: Job 9606139: <Attempt2_Coconuts_option_critic_2> in cluster <dcc> Exited

Job <Attempt2_Coconuts_option_critic_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon May  3 01:33:12 2021
Job was executed on host(s) <n-62-11-69>, in queue <hpc>, as user <s183914> in cluster <dcc> at Mon May  3 01:33:13 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon May  3 01:33:13 2021
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

    CPU time :                                   258227.56 sec.
    Max Memory :                                 873 MB
    Average Memory :                             859.93 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15511.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258918 sec.
    Turnaround time :                            258920 sec.

The output (if any) is above this job summary.

