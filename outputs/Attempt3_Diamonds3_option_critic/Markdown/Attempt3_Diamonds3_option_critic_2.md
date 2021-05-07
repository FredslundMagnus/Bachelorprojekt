
# Parameters

    Name :                      Attempt3_Diamonds3_option_critic-2
    Main :                      option_critic_run
    Level :                     Levels.Causal6
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


      45514798097 function calls (44170456311 primitive calls) in 258900.84 seconds

##    Ordered by: cumulative time
   List reduced from 428 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.835 258900.835 {built-in method builtins.exec}
                      1    0.328    0.328 258900.835 258900.835 <string>:1(<module>)
                      1 4673.622 4673.622 258900.507 258900.507 optionCritic.py:195(option_critic_run)
               48304425 9102.059    0.000 111677.831    0.002 optionCritic.py:143(actor_loss_fn)
        1785898146/441682617 10515.245    0.000 110213.268    0.000 module.py:866(_call_impl)
              149357281  777.158    0.000 101304.402    0.001 optionCritic.py:70(get_state)
              149357281 2537.130    0.000 98153.218    0.001 container.py:117(forward)
                1932177   13.072    0.000 67664.497    0.035 tensor.py:195(backward)
                1932177   18.054    0.000 67651.161    0.035 __init__.py:68(backward)
                1932177 67591.753    0.035 67591.753    0.035 {method 'run_backward' of 'torch._C._EngineBase' objects}
              298714562  974.864    0.000 60908.505    0.000 conv.py:398(forward)
              298714562  658.195    0.000 59546.057    0.000 conv.py:390(_conv_forward)
              298714562 58887.863    0.000 58887.863    0.000 {built-in method conv2d}
               48304425 3955.597    0.000 22769.821    0.000 optionCritic.py:91(get_action)
              591039898 1707.475    0.000 20661.955    0.000 linear.py:93(forward)
              591039898  713.956    0.000 18283.131    0.000 functional.py:1737(linear)
                1932177   40.474    0.000 17951.517    0.009 optimizer.py:84(wrapper)
                1932177   22.728    0.000 17803.750    0.009 grad_mode.py:24(decorate_context)
                1932177  114.813    0.000 17741.358    0.009 rmsprop.py:56(step)
                1932177  133.451    0.000 17495.466    0.009 _functional.py:203(rmsprop)
              591039898 17429.947    0.000 17429.947    0.000 {built-in method torch._C._nn.linear}
               27050460 14927.726    0.001 14927.726    0.001 {method 'sqrt' of 'torch._C._TensorBase' objects}
               48304425 1265.820    0.000 14017.916    0.000 optionCritic.py:80(predict_option_termination)
               96608850 1239.051    0.000 8295.505    0.000 distribution.py:34(__init__)
              448071843  542.617    0.000 8120.784    0.000 activation.py:713(forward)
               48304425  659.475    0.000 7593.311    0.000 categorical.py:115(log_prob)
              448071843  539.460    0.000 7578.167    0.000 functional.py:1364(leaky_relu)
              448071843 6925.820    0.000 6925.820    0.000 {built-in method torch._C._nn.leaky_relu}
               48304425  863.591    0.000 6413.865    0.000 categorical.py:49(__init__)
              147218844  473.598    0.000 6386.267    0.000 optionCritic.py:77(get_Q)
               48304425  374.693    0.000 5063.329    0.000 bernoulli.py:34(__init__)
                1932177   10.598    0.000 4892.743    0.003 game.py:42(step)
                1932177   19.924    0.000 4763.651    0.002 layers.py:827(step)
               96802067  451.980    0.000 4708.940    0.000 optionCritic.py:88(get_terminations)
               48304425 2598.183    0.000 3866.531    0.000 constraints.py:398(check)
               48304425  543.594    0.000 3032.246    0.000 distribution.py:240(_validate_sample)
                1932178  175.398    0.000 2689.722    0.001 layers.py:793(update)
                 193217   34.884    0.000 2241.183    0.012 optionCritic.py:116(critic_loss_fn)
              149357281  205.014    0.000 2138.706    0.000 activation.py:101(forward)
               48304425 1042.737    0.000 2109.462    0.000 categorical.py:123(entropy)
               48304425 2080.499    0.000 2080.499    0.000 constraints.py:364(check)
                1932177   77.171    0.000 2045.834    0.001 layers.py:17(step)
               48304425  132.551    0.000 1961.936    0.000 layer.py:106(move)
              149357281  176.064    0.000 1933.691    0.000 functional.py:1195(relu)
               48304425 1924.396    0.000 1924.396    0.000 constraints.py:249(check)
              144913275  264.301    0.000 1909.728    0.000 utils.py:106(__get__)
               48304425  396.543    0.000 1883.353    0.000 bernoulli.py:86(sample)
             2317805478 1838.289    0.000 1838.292    0.000 module.py:934(__getattr__)
              149357281 1724.555    0.000 1724.555    0.000 {built-in method relu}
              338130975 1613.258    0.000 1613.258    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              149357281  157.130    0.000 1600.212    0.000 flatten.py:39(forward)
              145299709  186.445    0.000 1538.680    0.000 tensor.py:525(__rsub__)
             1807152093 1500.734    0.000 1500.734    0.000 {built-in method torch._C._get_tracing_state}
               48304425   77.766    0.000 1457.745    0.000 categorical.py:88(logits)
                1919161   32.469    0.000 1456.354    0.001 layers.py:849(restart)
               96608850  516.315    0.000 1455.773    0.000 functional.py:46(broadcast_tensors)
               48304425  383.069    0.000 1453.210    0.000 categorical.py:108(sample)
              149357281 1443.081    0.000 1443.081    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              144913275 1396.137    0.000 1396.137    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
               48304425   82.331    0.000 1379.978    0.000 utils.py:82(probs_to_logits)
              145299709 1324.245    0.000 1324.245    0.000 {built-in method rsub}
               48304425  273.622    0.000 1306.852    0.000 layers.py:844(check)
               27050460 1303.533    0.000 1303.533    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              145106492 1302.776    0.000 1302.776    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
                1919161   16.652    0.000 1210.669    0.001 level.py:8(__init__)
               96802067 1185.644    0.000 1185.644    0.000 {method 'max' of 'torch._C._TensorBase' objects}
             7785070121 1167.458    0.000 1182.540    0.000 {built-in method builtins.len}
               21253947   52.797    0.000 1169.923    0.000 tensor.py:575(__iter__)
               21253947 1083.533    0.000 1083.533    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
                1919161   42.003    0.000 1077.175    0.001 levels.py:303(generate)
               48304425  215.799    0.000 1076.737    0.000 utils.py:11(broadcast_all)
              144913275 1016.573    0.000 1016.573    0.000 {method 'all' of 'torch._C._TensorBase' objects}
               11515453  174.899    0.000  993.256    0.000 level.py:41(notUsed)
             7292949865  983.029    0.000  983.029    0.000 {method 'values' of 'collections.OrderedDict' objects}
               48304425  864.820    0.000  864.820    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               48304425  156.110    0.000  854.834    0.000 utils.py:77(clamp_probs)
               96608850  803.825    0.000  803.825    0.000 {built-in method broadcast_tensors}
               48304425  705.973    0.000  705.973    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
               48304425  698.724    0.000  698.724    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
                1932177   80.209    0.000  697.698    0.000 replaybuffer.py:34(save_option_critic)
              145492926  649.902    0.000  649.902    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               50223560  599.287    0.000  599.287    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               96608850  576.536    0.000  576.536    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               11026831  268.588    0.000  576.433    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               48304425  575.236    0.000  575.236    0.000 {built-in method clamp}
               48304425  572.709    0.000  572.709    0.000 {built-in method bernoulli}
              290212984  555.312    0.000  555.312    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                1932177   96.741    0.000  544.759    0.000 optimizer.py:189(zero_grad)
               15457424  318.902    0.000  513.019    0.000 layer.py:175(NoRock_update)
             1416347805  343.264    0.000  497.669    0.000 enum.py:646(__hash__)
               11515453   13.645    0.000  476.591    0.000 level.py:38(elementsIn)
               27050460  458.640    0.000  458.640    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               48304425  457.204    0.000  457.204    0.000 {built-in method all}
               48304425  442.813    0.000  442.813    0.000 {built-in method log}
               48304425  100.586    0.000  431.724    0.000 layers.py:838(isFree)
               48304425  420.937    0.000  420.937    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
                 193217  310.071    0.002  386.866    0.002 replaybuffer.py:42(sample_option_critic)
              144913300  102.419    0.000  384.534    0.000 {built-in method builtins.all}
              146836298  356.308    0.000  356.308    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               27050460  352.000    0.000  352.000    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}


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
Subject: Job 9607851: <Attempt3_Diamonds3_option_critic_2> in cluster <dcc> Exited

Job <Attempt3_Diamonds3_option_critic_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon May  3 13:31:24 2021
Job was executed on host(s) <n-62-21-97>, in queue <hpc>, as user <s183914> in cluster <dcc> at Mon May  3 13:31:25 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon May  3 13:31:25 2021
Terminated at Thu May  6 13:26:35 2021
Results reported at Thu May  6 13:26:35 2021

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

    CPU time :                                   258926.75 sec.
    Max Memory :                                 901 MB
    Average Memory :                             883.53 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15483.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258926 sec.
    Turnaround time :                            258911 sec.

The output (if any) is above this job summary.

