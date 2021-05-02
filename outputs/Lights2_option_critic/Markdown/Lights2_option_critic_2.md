
# Parameters

    Name :                      Lights2_option_critic-2
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


      52096615097 function calls (50496356833 primitive calls) in 258900.66 seconds

##    Ordered by: cumulative time
   List reduced from 438 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.661 258900.661 {built-in method builtins.exec}
                      1    0.377    0.377 258900.661 258900.661 <string>:1(<module>)
                      1 5939.342 5939.342 258900.283 258900.283 optionCritic.py:195(option_critic_run)
        2113692897/520833090 9677.870    0.000 109769.849    0.000 module.py:866(_call_impl)
               56908175 8967.791    0.000 109451.617    0.002 optionCritic.py:143(actor_loss_fn)
              176984423  819.980    0.000 102374.625    0.001 optionCritic.py:70(get_state)
              176984423 2205.928    0.000 99127.799    0.001 container.py:117(forward)
                2276327   19.638    0.000 81388.567    0.036 tensor.py:195(backward)
                2276327   24.892    0.000 81368.609    0.036 __init__.py:68(backward)
                2276327 81290.685    0.036 81290.685    0.036 {method 'run_backward' of 'torch._C._EngineBase' objects}
              353968846  915.476    0.000 63539.830    0.000 conv.py:398(forward)
              353968846  504.589    0.000 62245.847    0.000 conv.py:390(_conv_forward)
              353968846 61741.258    0.000 61741.258    0.000 {built-in method conv2d}
               56908175 3468.431    0.000 20228.002    0.000 optionCritic.py:91(get_action)
              697817513 1593.982    0.000 20114.979    0.000 linear.py:93(forward)
              697817513  625.205    0.000 17872.635    0.000 functional.py:1737(linear)
              697817513 17093.162    0.000 17093.162    0.000 {built-in method torch._C._nn.linear}
               56908175 1166.635    0.000 13531.382    0.000 optionCritic.py:80(predict_option_termination)
              113816350 1187.318    0.000 7750.632    0.000 distribution.py:34(__init__)
              530953269  526.406    0.000 7220.605    0.000 activation.py:713(forward)
              530953269  539.983    0.000 6694.199    0.000 functional.py:1364(leaky_relu)
               56908175  575.811    0.000 6692.548    0.000 categorical.py:115(log_prob)
              530953269 6045.938    0.000 6045.938    0.000 {built-in method torch._C._nn.leaky_relu}
               56908175  761.293    0.000 5682.788    0.000 categorical.py:49(__init__)
              172555061  403.757    0.000 5492.206    0.000 optionCritic.py:77(get_Q)
               56908175  423.925    0.000 5254.741    0.000 bernoulli.py:34(__init__)
                 569081   92.262    0.000 5087.829    0.009 optionCritic.py:116(critic_loss_fn)
                2276327   11.887    0.000 4915.614    0.002 game.py:41(step)
                2276327   20.471    0.000 4746.797    0.002 layers.py:718(step)
              114385431  391.634    0.000 4261.915    0.000 optionCritic.py:88(get_terminations)
                2276327   50.710    0.000 4072.321    0.002 optimizer.py:84(wrapper)
                2276327   26.525    0.000 3883.916    0.002 grad_mode.py:24(decorate_context)
                2276327  136.553    0.000 3807.719    0.002 rmsprop.py:56(step)
                2276327  130.589    0.000 3524.160    0.002 _functional.py:203(rmsprop)
               56908175 2331.609    0.000 3457.085    0.000 constraints.py:398(check)
                2276327   82.966    0.000 2989.777    0.001 layers.py:17(step)
               56908175  233.932    0.000 2899.228    0.000 layer.py:98(move)
               56908175  468.189    0.000 2705.434    0.000 distribution.py:240(_validate_sample)
              176984423  220.634    0.000 2023.923    0.000 activation.py:101(forward)
               56908175 1995.484    0.000 1995.484    0.000 constraints.py:364(check)
               56908175  392.440    0.000 1943.591    0.000 bernoulli.py:86(sample)
               56908175  969.260    0.000 1855.805    0.000 categorical.py:123(entropy)
              176984423  193.366    0.000 1803.289    0.000 functional.py:1195(relu)
               56908175  362.194    0.000 1797.212    0.000 layers.py:735(check)
             2738518137 1755.299    0.000 1755.461    0.000 module.py:934(__getattr__)
               56908175 1754.055    0.000 1754.055    0.000 constraints.py:249(check)
                2276328  179.040    0.000 1727.991    0.001 layers.py:684(update)
              170724525  232.590    0.000 1667.465    0.000 utils.py:106(__get__)
              398357225 1610.582    0.000 1610.582    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              176984423  169.592    0.000 1596.137    0.000 flatten.py:39(forward)
              176984423 1580.952    0.000 1580.952    0.000 {built-in method relu}
              171862687  195.216    0.000 1530.596    0.000 tensor.py:525(__rsub__)
                 569081 1267.695    0.002 1519.643    0.003 replaybuffer.py:42(sample_option_critic)
              113816350  504.224    0.000 1444.290    0.000 functional.py:46(broadcast_tensors)
              176984423 1426.545    0.000 1426.545    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               25039597   56.866    0.000 1395.680    0.000 tensor.py:575(__iter__)
               56908175  363.564    0.000 1318.695    0.000 categorical.py:108(sample)
              171862687 1307.195    0.000 1307.195    0.000 {built-in method rsub}
               25039597 1304.117    0.000 1304.117    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               56908175   65.384    0.000 1257.140    0.000 categorical.py:88(logits)
             2138732494 1213.726    0.000 1213.726    0.000 {built-in method torch._C._get_tracing_state}
              171293606 1209.417    0.000 1209.417    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
              114385431 1202.146    0.000 1202.146    0.000 {method 'max' of 'torch._C._TensorBase' objects}
               56908175   70.009    0.000 1191.756    0.000 utils.py:82(probs_to_logits)
               56908175  262.343    0.000 1190.747    0.000 utils.py:11(broadcast_all)
             9312930478 1154.699    0.000 1171.308    0.000 {built-in method builtins.len}
              170724525 1169.940    0.000 1169.940    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
               31868572 1149.716    0.000 1149.716    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              170724525  966.989    0.000  966.989    0.000 {method 'all' of 'torch._C._TensorBase' objects}
             8631756011  933.089    0.000  933.089    0.000 {method 'values' of 'collections.OrderedDict' objects}
               31868572  910.147    0.000  910.147    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               56908175  886.594    0.000  886.594    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
              113816350  791.305    0.000  791.305    0.000 {built-in method broadcast_tensors}
                2276327  105.163    0.000  763.056    0.000 optimizer.py:189(zero_grad)
                2276327   83.532    0.000  754.150    0.000 replaybuffer.py:34(save_option_critic)
               56908175  127.379    0.000  716.465    0.000 layers.py:729(isFree)
               14827211  340.106    0.000  712.219    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               56908175  146.448    0.000  706.327    0.000 utils.py:77(clamp_probs)
               22763280  400.211    0.000  641.707    0.000 layer.py:151(update)
              172431768  631.542    0.000  631.542    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               56908175  600.311    0.000  600.311    0.000 {built-in method bernoulli}
              431269349  493.935    0.000  589.086    0.000 layer.py:95(isFree)
               56908175  567.661    0.000  567.661    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
               57600549  563.053    0.000  563.053    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               56908175  559.880    0.000  559.880    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
               31868572  554.881    0.000  554.881    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               15365209  515.422    0.000  515.422    0.000 {built-in method tensor}
              342587212  508.911    0.000  508.911    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               31868572  508.406    0.000  508.406    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              113816350  487.848    0.000  487.848    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               56908175  475.540    0.000  475.540    0.000 {built-in method clamp}
               56908175  415.420    0.000  415.420    0.000 {built-in method log}
                6828985   16.832    0.000  414.993    0.000 game.py:37(board)
               56908175  406.449    0.000  406.449    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
               31868558  388.275    0.000  388.275    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              754311485  255.270    0.000  386.890    0.000 {built-in method builtins.isinstance}
              170724550  135.223    0.000  385.455    0.000 {built-in method builtins.all}
               56908175  378.773    0.000  378.773    0.000 {built-in method all}
              176984437  372.995    0.000  372.995    0.000 {method 'to' of 'torch._C._TensorBase' objects}
               14827211   21.850    0.000  372.113    0.000 <__array_function__ internals>:2(prod)


Traceback (most recent call last):
  File "main.py", line 227, in <module>
    
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/auxillaries.py", line 132, in run
    enablePrint()
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils/server.py", line 37, in serverRun
    profilingStats()
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils/debug.py", line 62, in profilingStats
    os.remove('stats')
FileNotFoundError: [Errno 2] No such file or directory: 'stats'

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9601856: <Lights2_option_critic_2> in cluster <dcc> Exited

Job <Lights2_option_critic_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Thu Apr 29 21:41:04 2021
Job was executed on host(s) <n-62-11-66>, in queue <hpc>, as user <s183914> in cluster <dcc> at Thu Apr 29 21:41:06 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Apr 29 21:41:06 2021
Terminated at Sun May  2 21:36:12 2021
Results reported at Sun May  2 21:36:12 2021

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

Exited with exit code 1.

Resource usage summary:

    CPU time :                                   258263.61 sec.
    Max Memory :                                 1059 MB
    Average Memory :                             1046.80 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15325.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258914 sec.
    Turnaround time :                            258908 sec.

The output (if any) is above this job summary.

