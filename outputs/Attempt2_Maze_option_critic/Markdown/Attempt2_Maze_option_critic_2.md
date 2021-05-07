
# Parameters

    Name :                      Attempt2_Maze_option_critic-2
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


      51594214162 function calls (50014283469 primitive calls) in 258900.63 seconds

##    Ordered by: cumulative time
   List reduced from 434 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.626 258900.626 {built-in method builtins.exec}
                      1    0.342    0.342 258900.626 258900.626 <string>:1(<module>)
                      1 6139.349 6139.349 258900.284 258900.284 optionCritic.py:195(option_critic_run)
               56185275 10215.542    0.000 116478.167    0.002 optionCritic.py:143(actor_loss_fn)
        2087734714/515108878 10683.737    0.000 113260.396    0.000 module.py:866(_call_impl)
              174736204  904.055    0.000 105520.432    0.001 optionCritic.py:70(get_state)
              174736204 2383.508    0.000 101864.701    0.001 container.py:117(forward)
                2247411   18.813    0.000 72084.164    0.032 tensor.py:195(backward)
                2247411   23.576    0.000 72065.054    0.032 __init__.py:68(backward)
                2247411 71991.478    0.032 71991.478    0.032 {method 'run_backward' of 'torch._C._EngineBase' objects}
              349472408  953.770    0.000 62482.558    0.000 conv.py:398(forward)
              349472408  527.207    0.000 61073.595    0.000 conv.py:390(_conv_forward)
              349472408 60546.388    0.000 60546.388    0.000 {built-in method conv2d}
              689845082 1679.456    0.000 22763.165    0.000 linear.py:93(forward)
              689845082  692.679    0.000 20303.809    0.000 functional.py:1737(linear)
               56185275 3500.148    0.000 20227.285    0.000 optionCritic.py:91(get_action)
              689845082 19447.300    0.000 19447.300    0.000 {built-in method torch._C._nn.linear}
               56185275 1350.102    0.000 16183.431    0.000 optionCritic.py:80(predict_option_termination)
              112370550 1433.559    0.000 8692.457    0.000 distribution.py:34(__init__)
              524208612  554.657    0.000 7539.037    0.000 activation.py:713(forward)
               56185275  607.852    0.000 7118.299    0.000 bernoulli.py:34(__init__)
              524208612  560.911    0.000 6984.381    0.000 functional.py:1364(leaky_relu)
               56185275  576.466    0.000 6733.675    0.000 categorical.py:115(log_prob)
              524208612 6304.982    0.000 6304.982    0.000 {built-in method torch._C._nn.leaky_relu}
              171254997  388.306    0.000 5754.434    0.000 optionCritic.py:77(get_Q)
               56185275  765.193    0.000 5639.755    0.000 categorical.py:49(__init__)
                2247411   50.634    0.000 5222.372    0.002 optimizer.py:84(wrapper)
                2247411   12.751    0.000 5182.169    0.002 game.py:42(step)
                2247411   19.361    0.000 5036.893    0.002 layers.py:827(step)
                2247411   26.299    0.000 5033.064    0.002 grad_mode.py:24(decorate_context)
                2247411  125.139    0.000 4957.578    0.002 rmsprop.py:56(step)
              112932402  454.949    0.000 4713.670    0.000 optionCritic.py:88(get_terminations)
                2247411  133.701    0.000 4688.024    0.002 _functional.py:203(rmsprop)
                 561852   98.300    0.000 4517.002    0.008 optionCritic.py:116(critic_loss_fn)
               56185275 2325.920    0.000 3439.594    0.000 constraints.py:398(check)
               56185275  478.759    0.000 2734.840    0.000 distribution.py:240(_validate_sample)
               56185275 2591.500    0.000 2591.500    0.000 constraints.py:364(check)
                2247411   86.424    0.000 2528.534    0.001 layers.py:17(step)
                2247412  186.147    0.000 2481.338    0.001 layers.py:793(update)
               56185275  186.113    0.000 2434.606    0.000 layer.py:106(move)
               56185275  520.893    0.000 2408.328    0.000 bernoulli.py:86(sample)
              174736204  227.112    0.000 2165.811    0.000 activation.py:101(forward)
               31463748 2053.901    0.000 2053.901    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
             2706406643 2048.915    0.000 2049.076    0.000 module.py:934(__getattr__)
              174736204  213.075    0.000 1938.699    0.000 functional.py:1195(relu)
              393296925 1920.295    0.000 1920.295    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               56185275  966.781    0.000 1845.568    0.000 categorical.py:123(entropy)
               56185275  245.949    0.000 1828.243    0.000 layers.py:844(check)
               56185275 1770.995    0.000 1770.995    0.000 constraints.py:249(check)
              112370550  620.976    0.000 1762.100    0.000 functional.py:46(broadcast_tensors)
               56185275  405.655    0.000 1723.236    0.000 utils.py:11(broadcast_all)
              174736204  192.232    0.000 1716.528    0.000 flatten.py:39(forward)
              169679529  236.796    0.000 1706.942    0.000 tensor.py:525(__rsub__)
              174736204 1695.522    0.000 1695.522    0.000 {built-in method relu}
              168555825  233.036    0.000 1667.409    0.000 utils.py:106(__get__)
              174736204 1524.295    0.000 1524.295    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               31463748 1494.439    0.000 1494.439    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              169679529 1439.301    0.000 1439.301    0.000 {built-in method rsub}
              112932402 1408.131    0.000 1408.131    0.000 {method 'max' of 'torch._C._TensorBase' objects}
               24721521   60.863    0.000 1346.740    0.000 tensor.py:575(__iter__)
              169117677 1340.453    0.000 1340.453    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
               56185275  377.885    0.000 1336.667    0.000 categorical.py:108(sample)
             2112456235 1263.212    0.000 1263.212    0.000 {built-in method torch._C._get_tracing_state}
               56185275   65.375    0.000 1261.796    0.000 categorical.py:88(logits)
               24721521 1250.134    0.000 1250.134    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               56185275   69.480    0.000 1196.422    0.000 utils.py:82(probs_to_logits)
                1575494   21.475    0.000 1177.712    0.001 layers.py:849(restart)
              168555825 1158.877    0.000 1158.877    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
             8890013422 1128.335    0.000 1145.957    0.000 {built-in method builtins.len}
                 561852  898.064    0.002 1107.525    0.002 replaybuffer.py:42(sample_option_critic)
               56185275  605.504    0.000 1062.509    0.000 layers.py:538(check)
              168555825 1024.976    0.000 1024.976    0.000 {method 'all' of 'torch._C._TensorBase' objects}
                1575494   12.066    0.000 1003.215    0.001 level.py:8(__init__)
             8525675060 1000.138    0.000 1000.138    0.000 {method 'values' of 'collections.OrderedDict' objects}
              112370550  962.162    0.000  962.162    0.000 {built-in method broadcast_tensors}
                1575494  145.344    0.000  905.651    0.001 levels.py:428(generate)
               56185275  853.890    0.000  853.890    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
                2247411   86.272    0.000  734.444    0.000 replaybuffer.py:34(save_option_critic)
               56185275  697.846    0.000  697.846    0.000 {built-in method bernoulli}
              170241381  691.856    0.000  691.856    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               56185275  149.631    0.000  688.735    0.000 utils.py:77(clamp_probs)
                2247411  105.285    0.000  608.984    0.000 optimizer.py:189(zero_grad)
                7877470   97.130    0.000  603.728    0.000 level.py:41(notUsed)
               56185275  579.555    0.000  579.555    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
               11919784  275.359    0.000  575.301    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
              338235354  574.826    0.000  574.826    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
              757749946  330.619    0.000  558.077    0.000 {built-in method builtins.isinstance}
               56185275  539.104    0.000  539.104    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
               57760743  529.537    0.000  529.537    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               13484472  360.162    0.000  526.249    0.000 layer.py:159(update)
              112370550  499.758    0.000  499.758    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               56066293   58.251    0.000  487.261    0.000 {built-in method builtins.any}
              174736218  476.705    0.000  476.705    0.000 {method 'to' of 'torch._C._TensorBase' objects}
              170135811  469.510    0.000  469.510    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               56185275  467.723    0.000  467.723    0.000 {built-in method clamp}
               56185275  438.207    0.000  438.207    0.000 {built-in method log}
              389551077  137.696    0.000  429.234    0.000 layers.py:809(<genexpr>)
               56185275  410.792    0.000  410.792    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
               15170026  403.575    0.000  403.575    0.000 {built-in method tensor}
               31463748  399.959    0.000  399.959    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}


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
Subject: Job 9606136: <Attempt2_Maze_option_critic_2> in cluster <dcc> Exited

Job <Attempt2_Maze_option_critic_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon May  3 01:33:11 2021
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

    CPU time :                                   258287.33 sec.
    Max Memory :                                 905 MB
    Average Memory :                             891.44 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15479.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258919 sec.
    Turnaround time :                            258921 sec.

The output (if any) is above this job summary.

